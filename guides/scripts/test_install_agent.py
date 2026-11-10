import io
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

        # Test URL with query string and fragment
        rel4, slug4, url4 = install_agent.normalize_agent_ref(
            "https://raw.githubusercontent.com/msitarzewski/agency-agents/main/design/ui.md?plain=1#L5"
        )
        self.assertEqual(rel4, "design/ui.md")
        self.assertEqual(slug4, "ui")
        self.assertEqual(
            url4,
            "https://raw.githubusercontent.com/msitarzewski/agency-agents/main/design/ui.md",
        )

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
            # Standalone genOS repo at root (even if named genOS, has .git)
            standalone_git_dir = root / "genOS"
            standalone_git_script_dir = standalone_git_dir / "guides" / "scripts"
            standalone_git_script_dir.mkdir(parents=True)
            (standalone_git_dir / "AGENTS.md").write_text("# kernel", encoding="utf-8")
            (standalone_git_dir / ".git").mkdir()
            self.assertEqual(install_agent.detect_repo_root(standalone_git_script_dir), standalone_git_dir)

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
                raise urllib.error.HTTPError(url, 404, "Not Found", {}, io.BytesIO(b""))

            with self.assertRaises(urllib.error.HTTPError) as ctx:
                install_agent.install_agent(
                    "engineering/does-not-exist.md",
                    repo_root=repo_root,
                    fetcher=failing_fetch,
                )
            ctx.exception.close()
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

    def test_list_catalog_raises_on_missing_tree_key(self):
        bad_response = json.dumps({"message": "API rate limit exceeded"})
        with self.assertRaises(ValueError):
            install_agent.list_catalog(fetcher=lambda _u: bad_response)

    def test_main_list_catches_value_error_and_prints_stderr(self):
        stderr_capture = io.StringIO()
        with patch("install_agent.list_catalog", side_effect=ValueError("Invalid catalog response from GitHub API: rate limit")), patch("sys.stderr", stderr_capture):
            exit_code = install_agent.main(["--list"])
        self.assertEqual(exit_code, 1)
        self.assertIn("ERROR: Could not fetch catalog", stderr_capture.getvalue())
        self.assertIn("rate limit", stderr_capture.getvalue())

    def test_normalize_agent_ref_supports_tree_urls(self):
        rel, slug, url = install_agent.normalize_agent_ref(
            "https://github.com/msitarzewski/agency-agents/tree/main/engineering/backend-architect.md"
        )
        self.assertEqual(rel, "engineering/backend-architect.md")
        self.assertEqual(slug, "backend-architect")
        self.assertEqual(
            url,
            "https://raw.githubusercontent.com/msitarzewski/agency-agents/main/engineering/backend-architect.md",
        )

    def test_parse_upstream_agent_handles_utf8_bom(self):
        bom_text = "\ufeff" + SAMPLE_UPSTREAM_MD
        desc, body = install_agent.parse_upstream_agent(bom_text)
        self.assertEqual(desc, 'Expert UI builder: handles React, "quotes", and performance')
        self.assertTrue(body.startswith("# Frontend Developer Agent Personality"))
        self.assertIn("Always keep components modular.", body)

    def test_fetch_text_decodes_utf8_bom(self):
        mock_resp = io.BytesIO(b"\xef\xbb\xbf# Hello BOM")
        with patch("urllib.request.urlopen") as mock_urlopen:
            mock_urlopen.return_value.__enter__.return_value = mock_resp
            text = install_agent.fetch_text("https://example.com/file.md")
            self.assertEqual(text, "# Hello BOM")


if __name__ == "__main__":
    unittest.main()
