# PAC-008 - Generate Cognitive Views & Handover

Status: Done

## Goal

Generate cognitive continuity views and a current handover from committed PAC-007.3 memory.

## Implemented command

```bash
pac session handover project.pac.zip --generated-by Tommy
```

## Input artifacts

```text
user/memory.json
projects/<project_id>/memory.json
shared/memory.json
```

Missing memory domains are treated as empty.

## Output artifacts

```text
views/current/user_memory_view.json
views/current/project_memory_view.json
views/current/shared_memory_view.json
views/current/cognitive_summary.json
handovers/current.md
```

## Generation rules

```text
committed memory
    -> domain views
    -> cognitive summary
    -> current handover
```

PAC-008 reads committed memory entries only.

PAC-008 preserves memory provenance in generated JSON views.

PAC-008 groups project memory by project id.

## Source artifact boundary

PAC-008 does not modify:

- source session files;
- analysis artifacts;
- validation artifacts;
- selection artifacts;
- memory domain files.

PAC-008 may update:

- generated view artifacts;
- generated handover artifacts;
- `MANIFEST.json.updated_at`;
- `MANIFEST.json.latest_handover`;
- `MANIFEST.json.latest_cognitive_views`;
- `logs/changelog.md`.

## Release artifacts

- `Releases/PAC-008/pac-cli-pac008-cognitive-views-handover.zip`
- `Releases/PAC-008/pac-cli-pac008-qa-package.zip`

## Verification

```text
py -m pytest -q
70 passed in 4.38s

py tools\atlas_generate_start_here.py --check
START_HERE.md is up to date

py tools\atlas_validate.py
Atlas validation passed
```

## Non-goals

- no KEEP / IGNORE decision logic;
- no selection criteria changes;
- no candidate reclassification;
- no memory commit;
- no modification of committed memory entries;
- no LLM dependency.
