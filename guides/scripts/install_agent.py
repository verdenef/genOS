"""Fetch and install msitarzewski/agency-agents personas into .agents/skills/ and .cursor/rules/."""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

UPSTREAM_REPO = "msitarzewski/agency-agents"
RAW_BASE = f"https://raw.githubusercontent.com/{UPSTREAM_REPO}/main/"
BLOB_PREFIX = f"https://github.com/{UPSTREAM_REPO}/blob/main/"
TREE_PREFIX = f"https://github.com/{UPSTREAM_REPO}/tree/main/"
TREE_API_URL = f"https://api.github.com/repos/{UPSTREAM_REPO}/git/trees/main?recursive=1"
DEFAULT_DESCRIPTION = "Specialist agent persona imported from msitarzewski/agency-agents"
EXCLUDED_ROOTS = {"docs", ".github", "examples", "scripts", "templates"}


def fetch_text(url: str, timeout: int = 15) -> str:
    """Download UTF-8 text from an HTTP/HTTPS URL using stdlib urllib."""
    req = urllib.request.Request(url, headers={"User-Agent": "genOS-agent-installer/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read().decode("utf-8-sig")


def normalize_agent_ref(ref: str) -> tuple[str, str, str]:
    """Convert an agent ID or GitHub URL into (rel_path, slug, raw_url)."""
    cleaned = ref.strip().replace("\\", "/")
    # Strip URL query strings or fragments (? / #)
    for sep in ("?", "#"):
        if sep in cleaned:
            cleaned = cleaned.split(sep, 1)[0]

    if cleaned.startswith(RAW_BASE):
        rel = cleaned[len(RAW_BASE):]
    elif cleaned.startswith(BLOB_PREFIX):
        rel = cleaned[len(BLOB_PREFIX):]
    elif cleaned.startswith(TREE_PREFIX):
        rel = cleaned[len(TREE_PREFIX):]
    elif "://" in cleaned:
        raise ValueError(f"Unsupported URL (expected {UPSTREAM_REPO}): {ref}")
    else:
        rel = cleaned.lstrip("/")

    if not rel or ".." in Path(rel).parts or "/" not in rel:
        raise ValueError(f"Invalid agent path (expected <category>/<agent>.md): {ref}")
    if not rel.endswith(".md"):
        rel = f"{rel}.md"

    slug = re.sub(r"[^a-z0-9-]+", "-", Path(rel).stem.lower()).strip("-")
    if not slug:
        raise ValueError(f"Could not derive slug from: {ref}")
    return rel, slug, f"{RAW_BASE}{rel}"


def parse_upstream_agent(raw_text: str) -> tuple[str, str]:
    """Extract YAML description and return verbatim markdown body after frontmatter."""
    normalized = raw_text.lstrip("\ufeff").replace("\r\n", "\n")
    match = re.match(r"^---\n(.*?)\n---\n*", normalized, flags=re.DOTALL)
    if not match:
        return DEFAULT_DESCRIPTION, normalized.lstrip("\n")

    frontmatter = match.group(1)
    body = normalized[match.end():].lstrip("\n")
    desc_match = re.search(r"^description:\s*(.+)$", frontmatter, flags=re.MULTILINE)
    if not desc_match:
        return DEFAULT_DESCRIPTION, body

    desc = desc_match.group(1).strip()
    if len(desc) >= 2 and desc[0] == desc[-1] and desc[0] in ('"', "'"):
        desc = desc[1:-1]
    return (desc or DEFAULT_DESCRIPTION), body


def detect_repo_root(start_dir: Path | None = None) -> Path:
    """Resolve the project root containing .agents/ and .cursor/ (supports genOS/ subfolder)."""
    cur = (start_dir or Path(__file__).resolve().parent).resolve()
    for candidate in [cur, *cur.parents]:
        if (candidate / "AGENTS.md").exists():
            # If installed inside <project>/genOS/ (without its own .git), install rules/skills at <project>/
            if candidate.name.lower() == "genos" and candidate.parent != candidate and not (candidate / ".git").exists():
                return candidate.parent
            return candidate
    return Path.cwd().resolve()


def _render_skill_md(slug: str, description: str, body: str) -> str:
    return f"---\nname: {slug}\ndescription: {json.dumps(description)}\n---\n\n{body}"


def _render_cursor_mdc(description: str, body: str) -> str:
    return f'---\ndescription: {json.dumps(description)}\nglobs: ""\nalwaysApply: false\n---\n\n{body}'


def install_agent(
    ref: str,
    repo_root: Path,
    force: bool = False,
    fetcher=fetch_text,
) -> dict[str, str]:
    """Fetch an upstream agent and write both SKILL.md and .mdc under repo_root."""
    rel, slug, raw_url = normalize_agent_ref(ref)
    skill_path = repo_root / ".agents" / "skills" / slug / "SKILL.md"
    rule_path = repo_root / ".cursor" / "rules" / f"{slug}.mdc"

    if not force and skill_path.exists() and rule_path.exists():
        return {"slug": slug, "rel": rel, "status": "skipped", "skill": str(skill_path), "rule": str(rule_path)}

    raw_text = fetcher(raw_url)
    description, body = parse_upstream_agent(raw_text)

    if force or not skill_path.exists():
        skill_path.parent.mkdir(parents=True, exist_ok=True)
        skill_path.write_text(_render_skill_md(slug, description, body), encoding="utf-8")

    if force or not rule_path.exists():
        rule_path.parent.mkdir(parents=True, exist_ok=True)
        rule_path.write_text(_render_cursor_mdc(description, body), encoding="utf-8")

    return {"slug": slug, "rel": rel, "status": "installed", "skill": str(skill_path), "rule": str(rule_path)}


def list_catalog(query: str = "", fetcher=fetch_text) -> list[str]:
    """Fetch and filter available agent markdown IDs from upstream tree API."""
    data = json.loads(fetcher(TREE_API_URL))
    if "tree" not in data:
        msg = data.get("message", "Unknown GitHub API error")
        raise ValueError(f"Invalid catalog response from GitHub API: {msg}")
    needle = query.strip().lower()
    agents = []
    for entry in data.get("tree", []):
        path = entry.get("path", "")
        if entry.get("type") != "blob" or not path.endswith(".md") or "/" not in path:
            continue
        top = path.split("/", 1)[0].lower()
        if top in EXCLUDED_ROOTS:
            continue
        if not needle or needle in path.lower():
            agents.append(path)
    return sorted(agents)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Install Agency Agents into .agents/skills/ and .cursor/rules/.")
    parser.add_argument("agents", nargs="*", help="Agent IDs (<category>/<slug>.md) or GitHub URLs")
    parser.add_argument("--root", type=Path, default=None, help="Target repository root")
    parser.add_argument("--force", action="store_true", help="Overwrite existing SKILL.md / .mdc files")
    parser.add_argument("--list", nargs="?", const="", default=None, metavar="QUERY", help="List available upstream agents")
    args = parser.parse_args(argv)

    if args.list is not None:
        try:
            for item in list_catalog(args.list):
                print(item)
            return 0
        except (urllib.error.URLError, json.JSONDecodeError, ValueError) as exc:
            print(f"ERROR: Could not fetch catalog ({TREE_API_URL}): {exc}", file=sys.stderr)
            return 1

    if not args.agents:
        parser.print_help()
        return 1

    repo_root = args.root.resolve() if args.root else detect_repo_root()
    exit_code = 0
    for ref in args.agents:
        try:
            res = install_agent(ref, repo_root=repo_root, force=args.force)
            print(f"[{res['status'].upper()}] {res['slug']} -> {res['skill']} & {res['rule']}")
        except (ValueError, urllib.error.URLError) as exc:
            print(f"ERROR installing '{ref}': {exc}", file=sys.stderr)
            exit_code = 1
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
