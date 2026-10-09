import os
from pathlib import Path

target_file = Path("d:/GameOS/integrations/virtual-office/setup-virtual-office.md")
assert target_file.exists(), f"File {target_file} does not exist"

content = target_file.read_text(encoding="utf-8")
required_elements = [
    "Virtual Office Setup Wizard",
    "brain/60_AGENTS.md",
    "Lead Bot",
    "Builder Bots",
    "QA Bot",
    "System Prompt",
    "BOOT",
    "SHUTDOWN",
    "Sanity Gate",
    "bot/<agent-name>"
]

for el in required_elements:
    assert el in content, f"Missing required element: {el}"

assert len(content.splitlines()) >= 50
print("Task 2 verification PASSED!")
