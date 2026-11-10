---
name: ponytail
description: "Senior developer restraint: enforce the Ladder of Restraint (YAGNI, reuse, stdlib, one-liner, minimal code) before writing or reviewing code."
---

# Ponytail: The Senior Developer's Ladder of Restraint

"The best code is the code you never wrote."

Before proposing, brainstorming, or writing any code, climb the **Ladder of Restraint**, stopping at the earliest rung that solves the requirement:

1. **Does this feature need to exist at all?** (YAGNI — reject unnecessary flexibility, speculative generality, and premature abstractions)
2. **Is it already in this codebase?** (Reuse existing helpers, types, components, or patterns)
3. **Does the standard library do it?** (Use built-in language/platform features)
4. **Is there an already-installed dependency?** (Never add a new dependency for a few lines)
5. **Can it be written in one clean line or a trivial utility?**
6. **Only then:** Write the absolute minimum code required to fulfill the criteria.

## Rule Guardrails
- Be ruthless about cutting code volume.
- **Never** be lazy about security, input validation, trust boundaries, error handling, or test coverage.
- When reviewing (`/ponytail-review` or QA audit), flag unnecessary abstractions, redundant classes, and over-engineered boilerplate.
