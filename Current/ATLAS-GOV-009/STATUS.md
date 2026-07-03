# ATLAS-GOV-009 - Memory Feedback Rule

Status: Done

## Purpose

Define how assistants should handle stable user information when working with Atlas memory.

## Rule

For stable user information that clearly concerns the user, an assistant does not need to ask again whether the information may be kept.

Examples:

```text
preferred name
stable personal attributes
stable working preferences
stable accessibility or communication preferences
long-term user goals
```

The assistant should still use the controlled Atlas memory pipeline:

```text
PAC-007.2 select / classify
PAC-007.3 commit memory
PAC-008 regenerate views and handover when needed
PAC-009 maintain existing memory when needed
```

## Required Feedback

After handling memory-relevant user information, the assistant should explicitly tell the user whether it was recorded in Atlas.

Examples:

```text
I noted this in Atlas memory.
I did not note this in Atlas because it looked temporary / not useful for continuity.
I cannot note this yet because the memory pipeline was not run.
```

## Boundary

This rule does not allow free manual edits of memory files.

Assistants should not silently claim memory was updated unless Atlas was actually updated through the controlled pipeline.

## Release artifacts

- `Releases/ATLAS-GOV-009/atlas-gov-009-memory-feedback-rule.zip`
- `Releases/ATLAS-GOV-009/atlas-gov-009-qa-package.zip`

## Verification

```text
py tools\atlas_generate_start_here.py --check
py tools\atlas_validate.py
```

## Non-goals

- no PAC-007.2 selection behavior changes;
- no PAC-007.3 memory commit changes;
- no PAC-008 view generation changes;
- no PAC-009 maintenance command changes;
- no automatic memory write outside the Atlas pipeline.
