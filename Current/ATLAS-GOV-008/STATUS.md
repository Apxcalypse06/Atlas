# ATLAS-GOV-008 - PAC Status Closure Rule

Status: Done

## Purpose

Clarify Atlas PAC status semantics and close completed functional PACs as `DONE`.

## Rule

For pipeline PAC work:

```text
FEATURE_COMPLETE
    -> implementation is complete but release / QA / Atlas validation is not yet fully closed

DONE
    -> implementation, release archive, QA archive, status file, manifest, generated entrypoint, and Atlas validation are complete
```

`FEATURE_COMPLETE` is now a temporary delivery state, not the final status for a completed PAC.

## Status changes

```text
PAC-007.2 FEATURE_COMPLETE -> DONE
PAC-007.3 FEATURE_COMPLETE -> DONE
PAC-008   FEATURE_COMPLETE -> DONE
```

## Why

Atlas had completed PACs with release archives, QA packages, and passing validation, but their status still read `FEATURE_COMPLETE`.

That made completed PACs look unfinished.

## Release artifacts

- `Releases/ATLAS-GOV-008/atlas-gov-008-pac-status-closure.zip`
- `Releases/ATLAS-GOV-008/atlas-gov-008-qa-package.zip`

## Verification

```text
py tools\atlas_generate_start_here.py --check
py tools\atlas_validate.py
```

## Non-goals

- no PAC-007.2 selection behavior changes;
- no PAC-007.3 memory commit changes;
- no PAC-008 cognitive view or handover changes;
- no release archive deletion.
