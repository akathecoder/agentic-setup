#!/usr/bin/env python3
"""Build self-contained portable and Cursor CodeForge plugin packages."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "plugins" / "codeforge"
OUTPUT = ROOT / "dist" / "plugins"
AGENT_SCHEMA = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
AGENT_FIELDS = {
    "$schema",
    "name",
    "version",
    "description",
    "author",
    "homepage",
    "repository",
    "license",
    "keywords",
    "extensions",
}
SKILL_FIELDS = {"name", "description", "disable-model-invocation", "argument-hint"}


def require_within_root(path: Path) -> Path:
    resolved = path.resolve()
    try:
        resolved.relative_to(ROOT)
    except ValueError as error:
        raise ValueError(f"Path escapes repository root: {path}") from error
    return resolved


def frontmatter_keys(path: Path) -> list[str]:
    lines = path.read_text().splitlines()
    if not lines or lines[0] != "---":
        raise ValueError(f"Missing frontmatter: {path}")
    try:
        end = lines.index("---", 1)
    except ValueError as error:
        raise ValueError(f"Unclosed frontmatter: {path}") from error
    return [line.split(":", 1)[0] for line in lines[1:end] if ":" in line]


def selected_skills() -> list[tuple[str, Path]]:
    selected: list[tuple[str, Path]] = []
    for entry in sorted((SOURCE / "skills").iterdir()):
        if not entry.is_symlink():
            raise ValueError(f"Skill selection must be a symlink: {entry}")
        target = require_within_root(entry)
        skill_file = target / "SKILL.md"
        if not skill_file.is_file():
            raise ValueError(f"Selected skill has no SKILL.md: {entry}")
        keys = frontmatter_keys(skill_file)
        if any(key not in SKILL_FIELDS for key in keys):
            raise ValueError(f"Unsupported skill frontmatter in {skill_file}")
        if not keys[:2] == ["name", "description"]:
            raise ValueError(
                f"Skill name and description must lead frontmatter: {skill_file}"
            )
        name = skill_file.read_text().splitlines()[1].split(":", 1)[1].strip()
        if name != entry.name:
            raise ValueError(f"Skill name does not match selection: {entry}")
        selected.append((name, target))
    if not selected:
        raise ValueError("CodeForge must select at least one skill")
    return selected


def selected_rules() -> list[tuple[str, Path]]:
    rules_dir = SOURCE / "com.cursor" / "rules"
    selected: list[tuple[str, Path]] = []
    for entry in sorted(rules_dir.glob("*.mdc")):
        if not entry.is_symlink():
            raise ValueError(f"Rule selection must be a symlink: {entry}")
        target = require_within_root(entry)
        keys = frontmatter_keys(target)
        if keys != ["description", "globs", "alwaysApply"]:
            raise ValueError(f"Unexpected rule frontmatter in {target}")
        selected.append((entry.name, target))
    return selected


def metadata() -> dict[str, object]:
    data = json.loads((SOURCE / "plugin.json").read_text())
    if set(data) - AGENT_FIELDS:
        raise ValueError("plugin.json has unsupported Agent Plugin fields")
    if data.get("$schema") != AGENT_SCHEMA or data.get("name") != "codeforge":
        raise ValueError("plugin.json must be the CodeForge Agent Plugins manifest")
    return data


def copy_selected_skills(destination: Path, skills: list[tuple[str, Path]]) -> None:
    destination.mkdir(parents=True)
    for name, source in skills:
        shutil.copytree(source, destination / name, symlinks=False)


def copy_selected_rules(destination: Path, rules: list[tuple[str, Path]]) -> None:
    destination.mkdir(parents=True)
    for name, source in rules:
        shutil.copy2(source, destination / name)


def assert_self_contained(package: Path) -> None:
    for path in package.rglob("*"):
        if path.is_symlink():
            raise ValueError(f"Built package contains a symlink: {path}")


def build(destination: Path) -> None:
    skills = selected_skills()
    rules = selected_rules()
    manifest = metadata()

    agent = destination / "codeforge"
    agent.mkdir(parents=True)
    (agent / "plugin.json").write_text(json.dumps(manifest, indent=2) + "\n")
    shutil.copy2(SOURCE / "README.md", agent / "README.md")
    copy_selected_skills(agent / "skills", skills)

    cursor = destination / "cursor-codeforge"
    cursor_manifest = {
        key: value for key, value in manifest.items() if key != "$schema"
    }
    cursor_manifest["name"] = "cursor-codeforge"
    (cursor / ".cursor-plugin").mkdir(parents=True)
    (cursor / ".cursor-plugin" / "plugin.json").write_text(
        json.dumps(cursor_manifest, indent=2) + "\n"
    )
    shutil.copy2(SOURCE / "README.md", cursor / "README.md")
    copy_selected_skills(cursor / "skills", skills)
    copy_selected_rules(cursor / "rules", rules)

    assert_self_contained(agent)
    assert_self_contained(cursor)


def snapshot(directory: Path) -> dict[str, str]:
    if not directory.exists():
        return {}
    result: dict[str, str] = {}
    for path in sorted(directory.rglob("*")):
        relative = str(path.relative_to(directory))
        if path.is_dir():
            result[f"dir:{relative}"] = ""
        else:
            result[f"file:{relative}"] = hashlib.sha256(path.read_bytes()).hexdigest()
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Fail when dist is stale")
    args = parser.parse_args()

    with tempfile.TemporaryDirectory() as temporary:
        expected = Path(temporary) / "plugins"
        build(expected)
        if args.check:
            if snapshot(expected) != snapshot(OUTPUT):
                raise SystemExit(
                    "Generated plugins are stale. Run: python scripts/build_plugins.py"
                )
            return
        OUTPUT.parent.mkdir(parents=True, exist_ok=True)
        shutil.rmtree(OUTPUT, ignore_errors=True)
        shutil.copytree(expected, OUTPUT)


if __name__ == "__main__":
    try:
        main()
    except ValueError as error:
        raise SystemExit(f"Plugin build failed: {error}") from error
