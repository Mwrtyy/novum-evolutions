# EXP-001 Copilot judging automation status

Status: `BLOCKED_BY_ACCOUNT_COPILOT_ACCESS`

## What is ready

- 24 frozen blinded A/B packets
- 72 role-specific judge prompts
- resumable Copilot CLI judge runner: `scripts/auto_judge_exp001_copilot.py`
- full workflow: `.github/workflows/copilot-auto-judge-exp001.yml`
- judge model requested: `gpt-5.4`
- isolated `COPILOT_HOME` per judge invocation
- JSON schema/range validation before a judgment is accepted
- immediate stop on account-policy denial
- per-judge soft cap: 40 GitHub AI Credits
- automatic aggregation only after all 72 judgments are locked
- A/B mapping is not used by the judge runner

## Smoke test

Workflow run: `31232051492`

The runner successfully:

1. received `CopilotRequests: write` on `GITHUB_TOKEN`;
2. checked out the repository;
3. installed the current `@github/copilot` CLI;
4. reached the Copilot request.

The Copilot request was rejected by GitHub with:

`Access denied by policy settings`

GitHub's diagnostic says this means the account either lacks an active Copilot entitlement or Copilot CLI is blocked by policy.

No blind judgment was accepted or counted from the failed smoke test.

## Required external action

Copilot access must be enabled for the repository owner's GitHub account before the full workflow can run. This account-level setting cannot be changed through repository contents permissions.

After access is enabled, run the smoke test again. Only after a valid JSON smoke judgment should the full 72-judgment workflow be executed.

## Retired path

The previous GitHub Models workflow is disabled. GitHub Models inference was fully retired on 2026-07-30 and must not be used for EXP-001.
