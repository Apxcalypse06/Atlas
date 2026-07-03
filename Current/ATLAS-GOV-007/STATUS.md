# ATLAS-GOV-007 - Legacy Current Cleanup

Status: Done

## Purpose

Remove reclassified legacy governance patch folders from the active `Current/` surface.

## Context

`PAC-007.2.1` through `PAC-007.2.5` were reclassified by `ATLAS-GOV-006` into the `ATLAS-GOV-*` namespace.

Keeping both `Current/PAC-007.2.x/STATUS.md` and `Current/ATLAS-GOV-00x/STATUS.md` made the current state look duplicated and suggested that the legacy IDs were still active PAC work.

## Change

The legacy current folders were removed:

```text
Current/PAC-007.2.1/
Current/PAC-007.2.2/
Current/PAC-007.2.3/
Current/PAC-007.2.4/
Current/PAC-007.2.5/
```

Historical release archives remain preserved under `Releases/PAC-007.2.x/`.

## Rule

The active `Current/` surface should contain:

- active or recent pipeline PAC status folders;
- active Atlas governance status folders;
- no duplicate legacy governance status folders after reclassification.

## Release artifacts

- `Releases/ATLAS-GOV-007/atlas-gov-007-legacy-current-cleanup.zip`
- `Releases/ATLAS-GOV-007/atlas-gov-007-qa-package.zip`

## Verification

```text
py tools\atlas_generate_start_here.py --check
py tools\atlas_validate.py
```

## Non-goals

- no deletion of historical release archives;
- no deletion of `MANIFEST.json` reclassification history;
- no PAC-007.2 selection behavior;
- no PAC-007.3 memory commit;
- no PAC-008 view or handover generation.
