"""Offline package integrity checks; not a UX, WCAG, or complete secret audit."""
from __future__ import annotations

import argparse
import datetime
import json
import re
import sys
import unicodedata
from pathlib import Path
from urllib.parse import unquote, urlsplit

CATALOGS = (
    "product-ia.md", "layout-density.md", "visual-copy.md", "interaction.md",
    "data-viz.md", "accessibility.md", "performance-integrity.md",
)
REQUIRED = (
    "SKILL.md", "README.md", "README.zh-CN.md", "LICENSE",
    "agents/openai.yaml", "references/index.md", "references/evidence.md",
    "references/sources.json", "references/output-contracts.md",
    "workflows/create.md", "workflows/review.md", "workflows/verify.md",
    "tests/scenarios.json",
) + tuple("references/" + name for name in CATALOGS)
FIELDS = ("Signal", "Risk", "Repair", "Exception", "Check", "Basis")
BASES = {"Standard", "Guidance", "Synthesis", "Hypothesis"}
SOURCE_TYPES = {"standard", "guidance", "heuristic", "explanation", "research"}
ACCESS = {"verified", "partial", "limited"}
SKIP_DIRS = {".git", "__pycache__"}
ALLOWED_SUFFIXES = {"", ".md", ".json", ".py", ".yaml", ".yml", ".txt", ".html"}
SECRET_PATTERNS = (
    ("private key", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")),
    ("GitHub token", re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}\b")),
    ("GitHub fine-grained token", re.compile(r"\bgithub_pat_[A-Za-z0-9_]{30,}\b")),
    ("OpenAI-like token", re.compile(r"\bsk-(?:proj-|svcacct-)?[A-Za-z0-9_-]{24,}\b")),
    ("AWS access identifier", re.compile(r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b")),
    ("absolute user path", re.compile(r"(?:[A-Za-z]:[\\/]Users[\\/]|/" + r"(?:Users|home)/)[^\s\"'<>]+")),
)

def without_fences(text: str) -> str:
    fence = re.escape(chr(96) * 3)
    return re.sub(r"(?ms)^" + fence + r".*?^" + fence + r"[ \t]*$", "", text)

def anchors(text: str) -> set[str]:
    found: set[str] = set()
    counts: dict[str, int] = {}
    for match in re.finditer(r"(?m)^#{1,6}\s+(.+?)(?:\s+#+)?$", without_fences(text)):
        title = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", match.group(1))
        title = unicodedata.normalize("NFC", title).lower().strip()
        slug = re.sub(r"[^\w\- ]", "", title).replace(" ", "-")
        number = counts.get(slug, 0)
        counts[slug] = number + 1
        found.add(slug if number == 0 else slug + "-" + str(number))
    found.update(re.findall(r'\bid=["\']([^"\']+)["\']', text))
    return found

def collect_files(root: Path) -> list[Path]:
    return sorted(
        path for path in root.rglob("*")
        if path.is_file()
        and not any(part in SKIP_DIRS for part in path.relative_to(root).parts)
        and path.suffix != ".pyc"
    )

def inspect_package(root: Path) -> dict:
    root = root.resolve()
    errors: list[str] = []
    warnings: list[str] = []
    counts = {"files": 0, "sources": 0, "patterns": 0, "scenarios": 0}
    if not root.is_dir():
        return {"ok": False, "errors": ["Package directory missing"], "warnings": [], "counts": counts}
    for relative in REQUIRED:
        if not (root / relative).is_file():
            errors.append("Required file missing: " + relative)
    texts: dict[Path, str] = {}
    for path in collect_files(root):
        relative = path.relative_to(root).as_posix()
        counts["files"] += 1
        if path.is_symlink() or not path.resolve().is_relative_to(root):
            errors.append("Symlink or escaping file: " + relative)
            continue
        if path.name == ".env" or path.name.startswith(".env."):
            errors.append("Environment file must not be exported: " + relative)
        if path.suffix.lower() not in ALLOWED_SUFFIXES:
            errors.append("Unapproved artifact type: " + relative)
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except (UnicodeError, OSError):
            errors.append("Not readable UTF-8 text: " + relative)
            continue
        texts[path] = content
        if content.startswith("\ufeff"):
            errors.append("Unexpected UTF-8 BOM: " + relative)
        for label, pattern in SECRET_PATTERNS:
            if pattern.search(content):
                errors.append("Potential " + label + " in " + relative + " (value withheld)")
    skill = texts.get(root / "SKILL.md", "")
    frontmatter = re.match(r"\A---\n(.*?)\n---(?:\n|$)", skill, flags=re.S)
    if not frontmatter:
        errors.append("SKILL.md requires leading YAML frontmatter")
    else:
        fields = dict(re.findall(r"(?m)^([a-z_]+):\s*(.*)$", frontmatter.group(1)))
        if fields.get("name") != "anti-ai-design":
            errors.append("Skill name does not match package")
        if not fields.get("description", "").strip():
            errors.append("Skill description missing")
    metadata = texts.get(root / "agents/openai.yaml", "")
    if "default_prompt:" in metadata and "$anti-ai-design" not in metadata:
        errors.append("Default prompt does not invoke the skill")

    source_path = root / "references/sources.json"
    source_ids: set[str] = set()
    source_status: dict[str, str] = {}
    try:
        registry = json.loads(texts.get(source_path, "{}"))
        sources = registry["sources"]
        if registry.get("schema_version") != 1 or not isinstance(sources, list):
            raise ValueError("Invalid source schema")
        for source in sources:
            identifier = source["id"]
            if not re.fullmatch(r"S\d{2}", identifier) or identifier in source_ids:
                raise ValueError("Invalid or duplicate source ID")
            source_ids.add(identifier)
            source_status[identifier] = source["verification"]
            if source["type"] not in SOURCE_TYPES or source["verification"] not in ACCESS:
                raise ValueError("Invalid source type/access")
            url = urlsplit(source["url"])
            if url.scheme != "https" or not url.netloc or url.username or url.password:
                raise ValueError("Source URL must be credential-free HTTPS")
            datetime.date.fromisoformat(source["checked_on"])
            for field in ("title", "publisher", "supports", "limits"):
                if not str(source.get(field, "")).strip():
                    raise ValueError("Incomplete source entry")
        counts["sources"] = len(sources)
        if not sources:
            raise ValueError("Empty sources")
    except (KeyError, TypeError, ValueError, json.JSONDecodeError):
        errors.append("Invalid/incomplete source registry")

    # Validate actual Markdown targets, including anchors and traversal.
    for path, content in texts.items():
        if path.suffix != ".md":
            continue
        relative = path.relative_to(root).as_posix()
        for identifier in re.findall(r"\[(S\d{2})\]", content):
            if identifier not in source_ids:
                errors.append("Unknown source " + identifier + " in " + relative)
        for match in re.finditer(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", without_fences(content)):
            target = match.group(1).strip().strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme or target.startswith("//"):
                continue
            file_target = unquote(parsed.path)
            target_path = (path.parent / file_target).resolve() if file_target else path
            if not target_path.is_relative_to(root):
                errors.append("Link escapes package in " + relative)
                continue
            if not target_path.is_file():
                errors.append("Broken local link in " + relative + ": " + file_target)
                continue
            if parsed.fragment and target_path.suffix == ".md":
                target_text = texts.get(target_path, "")
                if unquote(parsed.fragment) not in anchors(target_text):
                    errors.append("Broken anchor in " + relative + ": " + target)

    pattern_ids: set[str] = set()
    for catalog in CATALOGS:
        path = root / "references" / catalog
        text = texts.get(path, "")
        matches = list(re.finditer(r"(?m)^## (AP\d{3}): (.+)$", text))
        if not matches:
            errors.append("Catalog has no diagnostic entries: " + catalog)
        for index, match in enumerate(matches):
            identifier = match.group(1)
            if identifier in pattern_ids:
                errors.append("Duplicate pattern ID: " + identifier)
            pattern_ids.add(identifier)
            end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
            # Later non-pattern headings must not supply fields to an incomplete entry.
            block = text[match.end():end]
            block = re.split(r"(?m)^## ", block, maxsplit=1)[0]
            for field in FIELDS:
                if not re.search(r"(?m)^- \*\*" + field + r":\*\* \S", block):
                    errors.append("Missing " + field + " in " + identifier)
            basis = re.search(r"(?m)^- \*\*Basis:\*\* ([A-Za-z]+);", block)
            if not basis or basis.group(1) not in BASES:
                errors.append("Invalid basis in " + identifier)
            cited = re.findall(r"\[(S\d{2})\]", block)
            if not cited:
                errors.append("Missing source basis in " + identifier)
            if basis and basis.group(1) in {"Standard", "Guidance"}:
                if any(source_status.get(s) != "verified" for s in cited):
                    errors.append("Unverified direct basis in " + identifier)
    counts["patterns"] = len(pattern_ids)

    try:
        scenarios = json.loads(texts.get(root / "tests/scenarios.json", "{}"))
        if scenarios.get("schema_version") != 1 or not isinstance(scenarios["scenarios"], list):
            raise ValueError("Invalid scenario schema")
        seen: set[str] = set()
        modes: set[str] = set()
        for scenario in scenarios["scenarios"]:
            if not scenario["id"] or scenario["id"] in seen:
                raise ValueError("Duplicate/empty scenario ID")
            seen.add(scenario["id"])
            modes.add(scenario["mode"])
            if scenario["mode"] not in {"create", "review", "refactor"}:
                raise ValueError("Invalid scenario mode")
            for field in ("prompt", "context"):
                if not isinstance(scenario[field], str) or not scenario[field].strip():
                    raise ValueError("Incomplete scenario")
            for field in ("must", "must_not"):
                if not isinstance(scenario[field], list) or not scenario[field]:
                    raise ValueError("Missing behavioral criteria")
                if any(not isinstance(v, str) or not v.strip() for v in scenario[field]):
                    raise ValueError("Empty behavioral criterion")
        if not {"create", "review", "refactor"}.issubset(modes):
            raise ValueError("Scenario set lacks supported modes")
        counts["scenarios"] = len(seen)
    except (KeyError, TypeError, ValueError, json.JSONDecodeError):
        errors.append("Invalid/incomplete behavioral scenarios")

    warnings.append("Offline checks do not prove UX quality, WCAG conformance, external link reachability, or absence of every secret.")
    return {"ok": not errors, "errors": errors, "warnings": warnings, "counts": counts}

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", default=".")
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args()
    result = inspect_package(Path(args.path))
    if args.as_json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print("PASS" if result["ok"] else "FAIL")
        print("Counts:", json.dumps(result["counts"]))
        for error in result["errors"]:
            print("ERROR:", error)
        for warning in result["warnings"]:
            print("NOTE:", warning)
    return 0 if result["ok"] else 1

if __name__ == "__main__":
    sys.exit(main())
