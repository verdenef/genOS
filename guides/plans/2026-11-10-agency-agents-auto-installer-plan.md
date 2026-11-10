# Agency Agents Auto-Installer & Clean Core Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Eliminate manual third-party Agency desktop app installation by adding a zero-dependency stdlib Python installer (`guides/scripts/install_agent.py`) that fetches approved `msitarzewski/agency-agents` personas verbatim into `.agents/skills/` and `.cursor/rules/`, while removing project-specific `.mdc` leftovers from `d:\GameOS`.

**Architecture:** Build `guides/scripts/install_agent.py` strictly using Python 3 standard library (`urllib.request`, `json`, `re`, `pathlib`, `argparse`) driven by unit tests in `guides/scripts/test_install_agent.py`. Clean `d:\GameOS\.cursor\rules\` down to core framework rules only, shield project-installed Agency Agents inside `AGENTS.md` / `guides/prompts/update.md`, wire the installer into `integrations/agency_agents.md` and `setup-init.md`, and record `DEC-007`.

**Tech Stack:** Python 3 stdlib, `unittest`, Markdown (`[[wikilink]]`), YAML, Git.

---

## Global Constraints

- **Human Approval Gate Remains:** Agents still audit the project and wait for human approval of the recommended agent roster before calling `install_agent.py`.
- **Zero External Dependencies:** `install_agent.py` must use Python 3 standard library modules only (runs cleanly on Windows, macOS, and Linux).
- **Verbatim Persona Integrity:** Upstream markdown body from `msitarzewski/agency-agents` must be copied verbatim with valid YAML frontmatter (safely double-quoted/escaped `description`).
- **Update Shielding:** Upgrading genOS (`update`) refreshes core framework skills/rules (`genos*`, `ponytail`, `graphify`, Superpowers) and strictly preserves project-installed Agency Agents.
- **No Unrelated Edits / Doctor Clean:** Keep `brain/` 100% Doctor-compliant with synced Index tables and `[[wikilink]]` syntax.

---

## Tasks

### Task 1: Build Stdlib `guides/scripts/install_agent.py` via TDD

**Files:**
- Create: `guides/scripts/test_install_agent.py`
- Create: `guides/scripts/install_agent.py`

**Interfaces:**
- Consumes: Agent references (`<category>/<slug>.md`, GitHub `blob/main` URLs, or `raw.githubusercontent.com` URLs) + optional `--root <path>`, `--force`, `--list [keyword]`.
- Produces:
  - `normalize_agent_ref(ref: str) -> tuple[str, str, str]` returning `(repo_rel_path, slug, raw_url)`
  - `parse_upstream_agent(raw_text: str) -> tuple[str, str]` returning `(description, verbatim_body)`
  - `detect_repo_root(start_dir: Path) -> Path`
  - `install_agent(ref: str, repo_root: Path, force: bool = False, fetcher=...) -> dict`
  - `list_catalog(query: str = "", fetcher=...) -> list[str]`
  - `<repo_root>/.agents/skills/<slug>/SKILL.md` and `<repo_root>/.cursor/rules/<slug>.mdc`

- [x] **Step 1: Write the failing tests in `guides/scripts/test_install_agent.py`**

```python
import json
import sys
import tempfile
import unittest
import urllib.error
from pathlib import Path
from unittest.mock import patch

SCRIPTS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS_DIR))

import install_agent  # noqa: E402


SAMPLE_UPSTREAM_MD = """---
name: Frontend Developer
description: Expert UI builder: handles React, "quotes", and performance
color: cyan
---

# Frontend Developer Agent Personality

Always keep components modular.
"""


class TestInstallAgent(unittest.TestCase):
    def test_normalize_agent_ref_formats(self):
        rel, slug, url = install_agent.normalize_agent_ref("engineering/engineering-frontend-developer.md")
        self.assertEqual(rel, "engineering/engineering-frontend-developer.md")
        self.assertEqual(slug, "engineering-frontend-developer")
        self.assertEqual(
            url,
            "https://raw.githubusercontent.com/msitarzewski/agency-agents/main/engineering/engineering-frontend-developer.md",
        )

        rel2, slug2, url2 = install_agent.normalize_agent_ref(
            "https://github.com/msitarzewski/agency-agents/blob/main/game-development/game-designer.md"
        )
        self.assertEqual(rel2, "game-development/game-designer.md")
        self.assertEqual(slug2, "game-designer")
        self.assertEqual(
            url2,
            "https://raw.githubusercontent.com/msitarzewski/agency-agents/main/game-development/game-designer.md",
        )

        rel3, slug3, _ = install_agent.normalize_agent_ref("design/design-ui-designer")
        self.assertEqual(rel3, "design/design-ui-designer.md")
        self.assertEqual(slug3, "design-ui-designer")

    def test_normalize_rejects_traversal_and_foreign_urls(self):
        with self.assertRaises(ValueError):
            install_agent.normalize_agent_ref("../secrets.md")
        with self.assertRaises(ValueError):
            install_agent.normalize_agent_ref("https://example.com/malicious.md")

    def test_parse_upstream_agent_preserves_body_and_extracts_description(self):
        desc, body = install_agent.parse_upstream_agent(SAMPLE_UPSTREAM_MD)
        self.assertEqual(desc, 'Expert UI builder: handles React, "quotes", and performance')
        self.assertTrue(body.startswith("# Frontend Developer Agent Personality"))
        self.assertIn("Always keep components modular.", body)

    def test_parse_upstream_agent_missing_frontmatter_fallback(self):
        desc, body = install_agent.parse_upstream_agent("# Plain Persona\n\nFollow rules.\n")
        self.assertEqual(desc, install_agent.DEFAULT_DESCRIPTION)
        self.assertTrue(body.startswith("# Plain Persona"))

    def test_detect_repo_root_standalone_and_nested(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            # Standalone genOS repo at root
            standalone_script_dir = root / "guides" / "scripts"
            standalone_script_dir.mkdir(parents=True)
            (root / "AGENTS.md").write_text("# kernel", encoding="utf-8")
            self.assertEqual(install_agent.detect_repo_root(standalone_script_dir), root)

            # Nested inside <project>/genOS/
            project = Path(tmp) / "my-game"
            nested_script_dir = project / "genOS" / "guides" / "scripts"
            nested_script_dir.mkdir(parents=True)
            (project / "genOS" / "AGENTS.md").write_text("# kernel", encoding="utf-8")
            self.assertEqual(install_agent.detect_repo_root(nested_script_dir), project)

    def test_install_agent_writes_both_targets_and_respects_force(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp)
            result = install_agent.install_agent(
                "engineering/engineering-frontend-developer.md",
                repo_root=repo_root,
                force=False,
                fetcher=lambda _url: SAMPLE_UPSTREAM_MD,
            )
            skill_path = repo_root / ".agents" / "skills" / "engineering-frontend-developer" / "SKILL.md"
            rule_path = repo_root / ".cursor" / "rules" / "engineering-frontend-developer.mdc"
            self.assertTrue(skill_path.exists())
            self.assertTrue(rule_path.exists())
            self.assertEqual(result["status"], "installed")

            skill_text = skill_path.read_text(encoding="utf-8")
            self.assertIn("name: engineering-frontend-developer\n", skill_text)
            self.assertIn(
                'description: "Expert UI builder: handles React, \\"quotes\\", and performance"\n',
                skill_text,
            )
            self.assertIn("# Frontend Developer Agent Personality", skill_text)

            rule_text = rule_path.read_text(encoding="utf-8")
            self.assertIn('globs: ""\n', rule_text)
            self.assertIn("alwaysApply: false\n", rule_text)
            self.assertIn("Always keep components modular.", rule_text)

            # Existing custom file is preserved when force=False
            rule_path.write_text("custom local edit", encoding="utf-8")
            res_skip = install_agent.install_agent(
                "engineering/engineering-frontend-developer.md",
                repo_root=repo_root,
                force=False,
                fetcher=lambda _url: SAMPLE_UPSTREAM_MD,
            )
            self.assertEqual(res_skip["status"], "skipped")
            self.assertEqual(rule_path.read_text(encoding="utf-8"), "custom local edit")

            # Force overwrites cleanly
            res_force = install_agent.install_agent(
                "engineering/engineering-frontend-developer.md",
                repo_root=repo_root,
                force=True,
                fetcher=lambda _url: SAMPLE_UPSTREAM_MD,
            )
            self.assertEqual(res_force["status"], "installed")
            self.assertIn("# Frontend Developer Agent Personality", rule_path.read_text(encoding="utf-8"))

    def test_install_agent_writes_nothing_on_http_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp)

            def failing_fetch(url):
                raise urllib.error.HTTPError(url, 404, "Not Found", {}, None)

            with self.assertRaises(urllib.error.HTTPError):
                install_agent.install_agent(
                    "engineering/does-not-exist.md",
                    repo_root=repo_root,
                    fetcher=failing_fetch,
                )
            self.assertFalse((repo_root / ".agents").exists())
            self.assertFalse((repo_root / ".cursor").exists())

    def test_list_catalog_filters_meta_docs_and_applies_query(self):
        fake_tree = json.dumps({
            "tree": [
                {"path": "README.md", "type": "blob"},
                {"path": "CONTRIBUTING.md", "type": "blob"},
                {"path": "engineering/engineering-frontend-developer.md", "type": "blob"},
                {"path": "game-development/game-designer.md", "type": "blob"},
                {"path": "docs/guide.md", "type": "blob"},
            ]
        })
        all_agents = install_agent.list_catalog(fetcher=lambda _u: fake_tree)
        self.assertEqual(
            all_agents,
            ["engineering/engineering-frontend-developer.md", "game-development/game-designer.md"],
        )
        filtered = install_agent.list_catalog(query="frontend", fetcher=lambda _u: fake_tree)
        self.assertEqual(filtered, ["engineering/engineering-frontend-developer.md"])


if __name__ == "__main__":
    unittest.main()
```

- [x] **Step 2: Run the tests to verify they fail**

Run: `python -m unittest discover -s guides/scripts -p "test_*.py" -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'install_agent'`.

- [x] **Step 3: Write minimal implementation in `guides/scripts/install_agent.py`**

```python
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
TREE_API_URL = f"https://api.github.com/repos/{UPSTREAM_REPO}/git/trees/main?recursive=1"
DEFAULT_DESCRIPTION = "Specialist agent persona imported from msitarzewski/agency-agents"
EXCLUDED_ROOTS = {"docs", ".github", "examples", "scripts", "templates"}


def fetch_text(url: str, timeout: int = 15) -> str:
    """Download UTF-8 text from an HTTP/HTTPS URL using stdlib urllib."""
    req = urllib.request.Request(url, headers={"User-Agent": "genOS-agent-installer/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read().decode("utf-8")


def normalize_agent_ref(ref: str) -> tuple[str, str, str]:
    """Convert an agent ID or GitHub URL into (rel_path, slug, raw_url)."""
    cleaned = ref.strip().replace("\\", "/")
    if cleaned.startswith(RAW_BASE):
        rel = cleaned[len(RAW_BASE):]
    elif cleaned.startswith(BLOB_PREFIX):
        rel = cleaned[len(BLOB_PREFIX):]
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
    normalized = raw_text.replace("\r\n", "\n")
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
            # If installed inside <project>/genOS/, install rules/skills at <project>/
            if candidate.name.lower() == "genos" and candidate.parent != candidate:
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
        except (urllib.error.URLError, json.JSONDecodeError) as exc:
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
```

- [x] **Step 4: Run unit tests & verify live fetch**

Run: `python -m unittest discover -s guides/scripts -p "test_*.py" -v`
Expected: `Ran 7 tests ... OK`

- [x] **Step 5: Commit Task 1**

```bash
git add guides/scripts/install_agent.py guides/scripts/test_install_agent.py
git commit -m "feat(workforce): add zero-dependency stdlib Agency Agents auto-installer"
```

---

### Task 2: Clean Core `.cursor/rules/` Cleanup

**Files:**
- Delete: `.cursor/rules/academic-historian.mdc`
- Delete: `.cursor/rules/academic-statistician.mdc`
- Delete: `.cursor/rules/design-ux-researcher.mdc`
- Delete: `.cursor/rules/engineering-minimal-change-engineer.mdc`
- Delete: `.cursor/rules/engineering-mobile-release-engineer.mdc`
- Delete: `.cursor/rules/engineering-technical-writer.mdc`
- Delete: `.cursor/rules/game-audio-engineer.mdc`
- Delete: `.cursor/rules/game-designer.mdc`
- Delete: `.cursor/rules/level-designer.mdc`
- Delete: `.cursor/rules/marketing-app-store-optimizer.mdc`
- Delete: `.cursor/rules/narrative-designer.mdc`
- Delete: `.cursor/rules/testing-accessibility-auditor.mdc`
- Delete: `.cursor/rules/testing-reality-checker.mdc`
- Delete: `.cursor/rules/unity-architect.mdc`

**Interfaces:**
- Consumes: Clean core specification (`docs/superpowers/specs/2026-11-10-agency-agents-auto-installer-design.md`).
- Produces: Minimal core `.cursor/rules/` directory (`genos*.mdc`, `ponytail.mdc`, `graphify.mdc` only).

- [x] **Step 1: Delete the 14 project-specific `.mdc` files from `d:\GameOS\.cursor\rules/`**
- [x] **Step 2: Verify exact remaining `.cursor/rules/` directory contents (7 core files only)**

Run: `Get-ChildItem d:\GameOS\.cursor\rules | Select-Object -ExpandProperty Name`
Expected: `genos-doctor.mdc`, `genos-kickoff.mdc`, `genos-shutdown.mdc`, `genos-update.mdc`, `genos.mdc`, `graphify.mdc`, `ponytail.mdc`.

- [x] **Step 3: Commit Task 2**

```bash
git add -A .cursor/rules/
git commit -m "chore(rules): remove project-specific Agency Agent leftovers for clean core"
```

---

### Task 3: Wire Auto-Installer & Update Shielding Into Protocols and Docs

**Files:**
- Modify: `integrations/agency_agents.md`
- Modify: `guides/prompts/setup-init.md`
- Modify: `AGENTS.md`
- Modify: `guides/prompts/update.md`
- Modify: `README.md`
- Modify: `guides/guide.md`

**Interfaces:**
- Consumes: `guides/scripts/install_agent.py` CLI interface.
- Produces: Automatic Agency Agent installation workflow and upgrade preservation guarantees.

- [x] **Step 1: Update `integrations/agency_agents.md`**
  - Replace manual installation steps with running `python <genos>/guides/scripts/install_agent.py <id_or_url>...` after explicit human approval, plus `--list [keyword]` for catalog browsing and manual URL fallback if offline.
- [x] **Step 2: Update `guides/prompts/setup-init.md`**
  - In Phase 3 step 1, run `python <genos>/guides/scripts/install_agent.py ...` for approved `recommended_agents` from the active profile so both `.agents/skills/<slug>/SKILL.md` and `.cursor/rules/<slug>.mdc` are created cleanly without the Agency desktop app.
- [x] **Step 3: Update `AGENTS.md` & `guides/prompts/update.md`**
  - In `Framework Update Protocol` step 2 & step 3 (`AGENTS.md`) and `Strict Brain Shield` (`guides/prompts/update.md`), explicitly shield project-installed Agency Agents inside `.agents/skills/` and `.cursor/rules/` (only refreshing core genOS framework skills/rules: `genos*`, `ponytail`, `graphify`, Superpowers).
  - In `Optional Integrations` (`AGENTS.md`), reference `guides/scripts/install_agent.py` for automated workforce installation.
- [x] **Step 4: Update `README.md` & `guides/guide.md`**
  - Document `guides/scripts/install_agent.py` in repository structure and note zero-app automated installation of `msitarzewski/agency-agents` on approval.
- [x] **Step 5: Commit Task 3**

```bash
git add integrations/agency_agents.md guides/prompts/setup-init.md AGENTS.md guides/prompts/update.md README.md guides/guide.md
git commit -m "docs(workforce): integrate auto-installer workflow and shield project agents on update"
```

---

### Task 4: Record `DEC-007`, Update Brain Systems/Roadmap & Verify

**Files:**
- Modify: `brain/30_DECISIONS.md`
- Modify: `brain/50_ROADMAP.md`
- Modify: `brain/systems/Workforce.md`
- Modify: `brain/20_PROGRESS.yaml`

**Interfaces:**
- Consumes: Approved spec and completed tasks 1–3.
- Produces: Synchronized Project Brain (`DEC-007`, `M2` deliverables, `Workforce.md` runtime paths, `session_summary`).

- [x] **Step 1: Record `DEC-007: Zero-App Agency Agents Auto-Installer & Clean Core` in `brain/30_DECISIONS.md`** (Index row + detailed entry).
- [x] **Step 2: Add `[[DEC-007]]` deliverable to `M2` in `brain/50_ROADMAP.md`**.
- [x] **Step 3: Update `brain/systems/Workforce.md`** with `guides/scripts/install_agent.py` and clean core/update shielding invariants.
- [x] **Step 4: Update `brain/20_PROGRESS.yaml`** `session_summary` cleanly.
- [x] **Step 5: Run full verification**
  - Run `python -m unittest discover -s guides/scripts -p "test_*.py" -v` (confirm all unit tests pass).
  - Run `python guides/scripts/install_agent.py --list frontend` and a live install into a temp dir (`--root <temp>`) to verify live upstream integration.
  - Run Doctor diagnostic audit (`8/8` checks PASS).
- [x] **Step 6: Commit & push to `main` and sync `genos-v3`**

```bash
git add brain/ docs/superpowers/plans/2026-11-10-agency-agents-auto-installer.md guides/plans/2026-11-10-agency-agents-auto-installer-plan.md
git commit -m "docs(brain): record DEC-007 Agency Agents auto-installer and clean core"
git push origin main
```

---

## Execution Handoff

After saving this plan, start execution using one of the following commands:

**Option 1: Subagent-Driven (Recommended):**
```
kickoff execute the approved plan: docs/superpowers/plans/2026-11-10-agency-agents-auto-installer.md using subagent-driven-development
```

**Option 2: Inline Execution:**
```
kickoff execute the approved plan: docs/superpowers/plans/2026-11-10-agency-agents-auto-installer.md
```
