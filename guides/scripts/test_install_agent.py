import json
import sys
import tempfile
import unittest
import urllib.error
from pathlib import Path

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
