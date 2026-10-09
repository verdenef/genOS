import os
from pathlib import Path

target_file = Path("d:/GameOS/integrations/virtual-office/README.md")
assert target_file.exists(), f"File {target_file} does not exist"

content = target_file.read_text(encoding="utf-8")
required_sections = [
    "# genOS Virtual Office Integration",
    "## 1. Overview",
    "## 2. Prerequisites",
    "## 3. Architecture & Data Flow",
    "## 4. Bot Roles & Responsibilities",
    "## 5. Branch & PR Conventions",
    "## 6. Daily Operational Cycle",
    "## 7. Troubleshooting & Escalation"
]

for section in required_sections:
    assert section in content, f"Missing section: {section}"

assert "[[60_AGENTS.md]]" in content or "60_AGENTS.md" in content
assert "bot/<agent-name>" in content
assert len(content.splitlines()) >= 80

print("Task 1 verification PASSED!")
