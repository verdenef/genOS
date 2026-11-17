# Git Remote Credential Sanitization Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Strip the plain-text GitHub personal access token embedded in `.git/config`, verify clean Git Credential Manager authentication, and document token revocation on GitHub.

**Architecture:** Use standard Git CLI commands to update the remote URL from token-embedded HTTPS to clean HTTPS (`https://github.com/verdenef/genOS.git`), verify `.git/config` contains no embedded secrets, and confirm credential helper integration.

**Tech Stack:** Git CLI, Windows Git Credential Manager (GCM).

## Global Constraints

- Never commit secrets, tokens, or credentials into repository files or git configuration.
- Do not add external dependencies or scripts for basic Git operations (Ponytail Ladder of Restraint).
- Verification must confirm zero occurrences of `ghp_` or token strings in `.git/config`.

---

### Task 1: Sanitize Remote URL & Verify `.git/config` Hygiene

**Files:**
- Modify: `.git/config` (via Git CLI)

- [x] **Step 1: Check current remote URL for token leakage**

Run:
```powershell
git remote get-url origin
```
Expected: Contains embedded token `https://verdenef:ghp_...`

- [x] **Step 2: Update remote URL to clean HTTPS endpoint**

Run:
```powershell
git remote set-url origin https://github.com/verdenef/genOS.git
```

- [x] **Step 3: Verify clean remote URL**

Run:
```powershell
git remote -v
```
Expected:
```
origin  https://github.com/verdenef/genOS.git (fetch)
origin  https://github.com/verdenef/genOS.git (push)
```

- [x] **Step 4: Verify `.git/config` contains no remaining tokens**

Run:
```powershell
Select-String -Path .git\config -Pattern "ghp_" -Quiet
```
Expected: `False`

---

### Task 2: Verify Credential Helper & Remote Access

**Files:**
- Read-only check: Git environment configuration

- [x] **Step 1: Verify credential helper is set to Windows Credential Manager**

Run:
```powershell
git config --get credential.helper
```
Expected: `manager`

- [x] **Step 2: Verify git remote connectivity without embedded tokens**

Run:
```powershell
git ls-remote --exit-code -h origin HEAD
```
Expected: Clean exit code 0 outputting the current remote HEAD commit hash, using GCM for authentication.

---

### Task 3: Revoke Compromised GitHub Token (Human Action)

**Files:**
- External: GitHub User Account Security Settings

- [x] **Step 1: Navigate to GitHub Personal Access Tokens**
  - Open `https://github.com/settings/tokens` (Classic tokens) or `https://github.com/settings/tokens?type=beta` (Fine-grained tokens).

- [x] **Step 2: Identify and Revoke the Leaked Token**
  - Locate the token prefixed with `ghp_rOx3...` that was used for this repository.
  - Click **Delete** / **Revoke** immediately to invalidate the exposed credential.
