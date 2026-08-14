#!/usr/bin/env python3
"""Validate bilingual catalog metadata and render the Simplified Chinese index."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "catalog" / "plugins.json"
MARKERS = ("<!-- CATALOG:START -->", "<!-- CATALOG:END -->")
LANGUAGES = ("en", "zh-CN")
PAGES = {"zh-CN": ROOT / "docs" / "README.zh-CN.md"}
SLUG_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
STATUSES = {"active", "beta", "archived"}
SOURCES = {"official", "community"}
EMPTY_MESSAGES = {
    "en": "No entries yet. [Submit the first plugin.](CONTRIBUTING.md)",
    "zh-CN": "暂未收录。欢迎[提交第一个 Plugin](../CONTRIBUTING.md)。",
}


def fail(message: str) -> None:
    raise ValueError(message)


def load_catalog() -> dict[str, Any]:
    try:
        catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        fail(f"Invalid JSON in {CATALOG_PATH.relative_to(ROOT)}: {error}")

    if not isinstance(catalog, dict):
        fail("Catalog root must be an object.")
    if not isinstance(catalog.get("categories"), list):
        fail("Catalog must contain a categories array.")
    if not isinstance(catalog.get("plugins"), list):
        fail("Catalog must contain a plugins array.")
    return catalog


def require_localized(value: Any, label: str) -> dict[str, str]:
    if not isinstance(value, dict):
        fail(f"{label} must be an object with en and zh-CN text.")
    result: dict[str, str] = {}
    for language in LANGUAGES:
        text = value.get(language)
        if not isinstance(text, str) or not text.strip():
            fail(f"{label}.{language} must be a non-empty string.")
        result[language] = text.strip()
    return result


def validate(catalog: dict[str, Any]) -> tuple[list[dict[str, Any]], dict[str, list[dict[str, Any]]]]:
    categories: list[dict[str, Any]] = []
    category_ids: set[str] = set()
    for index, category in enumerate(catalog["categories"], start=1):
        label = f"categories[{index}]"
        if not isinstance(category, dict):
            fail(f"{label} must be an object.")
        category_id = category.get("id")
        if not isinstance(category_id, str) or not SLUG_PATTERN.fullmatch(category_id):
            fail(f"{label}.id must be a lowercase kebab-case string.")
        if category_id in category_ids:
            fail(f"Duplicate category id: {category_id}")
        category_ids.add(category_id)
        categories.append({"id": category_id, "title": require_localized(category.get("title"), f"{label}.title")})

    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    names: set[str] = set()
    urls: set[str] = set()
    for index, plugin in enumerate(catalog["plugins"], start=1):
        label = f"plugins[{index}]"
        if not isinstance(plugin, dict):
            fail(f"{label} must be an object.")
        name = plugin.get("name")
        url = plugin.get("url")
        category = plugin.get("category")
        if not isinstance(name, str) or not name.strip():
            fail(f"{label}.name must be a non-empty string.")
        if name.casefold() in names:
            fail(f"Duplicate plugin name: {name}")
        names.add(name.casefold())
        if not isinstance(url, str) or urlparse(url).scheme not in {"https", "http"} or not urlparse(url).netloc:
            fail(f"{label}.url must be an absolute http(s) URL.")
        if url in urls:
            fail(f"Duplicate plugin URL: {url}")
        urls.add(url)
        if category not in category_ids:
            fail(f"{label}.category must reference a declared category.")
        status = plugin.get("status", "active")
        source = plugin.get("source", "community")
        if status not in STATUSES:
            fail(f"{label}.status must be one of: {', '.join(sorted(STATUSES))}.")
        if source not in SOURCES:
            fail(f"{label}.source must be one of: {', '.join(sorted(SOURCES))}.")
        grouped[category].append(
            {
                "name": name.strip(),
                "url": url,
                "description": require_localized(plugin.get("description"), f"{label}.description"),
                "status": status,
                "source": source,
            }
        )

    for entries in grouped.values():
        entries.sort(key=lambda entry: entry["name"].casefold())
    return categories, grouped


def escape_markdown(text: str) -> str:
    return text.replace("\\", "\\\\").replace("[", "\\[").replace("]", "\\]").replace("\n", " ")


def render_catalog(language: str, categories: list[dict[str, Any]], grouped: dict[str, list[dict[str, Any]]]) -> str:
    sections: list[str] = []
    for category in categories:
        sections.append(f"### {category['title'][language]}")
        entries = grouped[category["id"]]
        if not entries:
            sections.append(EMPTY_MESSAGES[language])
            continue
        for entry in entries:
            suffix: list[str] = []
            if entry["status"] != "active":
                suffix.append(entry["status"])
            if entry["source"] == "official":
                suffix.append("official")
            label = f" ({', '.join(suffix)})" if suffix else ""
            sections.append(
                f"- [{escape_markdown(entry['name'])}]({entry['url']}) — "
                f"{escape_markdown(entry['description'][language])}{label}"
            )
    return "\n\n".join(sections)


def update_page(path: Path, rendered_catalog: str, check: bool) -> bool:
    content = path.read_text(encoding="utf-8")
    start, end = MARKERS
    if content.count(start) != 1 or content.count(end) != 1:
        fail(f"{path.relative_to(ROOT)} must contain one pair of catalog markers.")
    before, remainder = content.split(start, 1)
    _, after = remainder.split(end, 1)
    expected = f"{before}{start}\n{rendered_catalog}\n{end}{after}"
    if content == expected:
        return False
    if check:
        print(f"Out of date: {path.relative_to(ROOT)}")
        return True
    path.write_text(expected, encoding="utf-8")
    print(f"Updated: {path.relative_to(ROOT)}")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail if generated pages are out of date.")
    arguments = parser.parse_args()
    try:
        categories, grouped = validate(load_catalog())
        changed = False
        for language, path in PAGES.items():
            changed = update_page(path, render_catalog(language, categories, grouped), arguments.check) or changed
    except (OSError, ValueError) as error:
        print(f"Catalog validation failed: {error}", file=sys.stderr)
        return 1
    if arguments.check and changed:
        print("Run: python scripts/generate_readmes.py", file=sys.stderr)
        return 1
    print("Catalog is valid and generated pages are current.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
