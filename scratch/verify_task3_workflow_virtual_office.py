import os
from pathlib import Path

target_file = Path("d:/GameOS/guides/prompts/workflow-virtual-office.md")
assert target_file.exists(), f"File {target_file} does not exist"

content = target_file.read_text(encoding="utf-8")
required_sections = [
    "Phase 1: Morning Briefing & Roadmap Audit",
    "Phase 2: Task Dispatch & Branch Isolation",
    "Phase 3: QA Verification & Peer Review Loop",
    "Phase 4: Pull Request Preparation & Daily Summary",
    "Escalation Valve",
    "Sanity Gate"
]

for section in required_sections:
    assert section in content, f"Missing section: {section}"

assert "50_ROADMAP.md" in content
assert "bot/<agent-name>" in content
assert "2-retry" in content or "two retries" in content.lower()
print("Task 3 verification PASSED!")
