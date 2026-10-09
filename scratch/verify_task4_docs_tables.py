import os
from pathlib import Path

readme_path = Path("d:/GameOS/README.md")
guide_path = Path("d:/GameOS/guides/guide.md")

readme = readme_path.read_text(encoding="utf-8")
guide = guide_path.read_text(encoding="utf-8")

# Check README
assert "workflow-virtual-office.md" in readme, "README missing workflow-virtual-office.md link"
assert "setup-virtual-office.md" in readme or "integrations/virtual-office" in readme, "README missing virtual office integration"

# Check guide.md
assert "workflow-virtual-office.md" in guide, "guide.md missing workflow-virtual-office.md link"
assert "Virtual Office" in guide, "guide.md missing Virtual Office section"

print("Task 4 verification PASSED!")
