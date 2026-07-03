# PAC-007.3 - Memory Commit

Status: Done

## Goal

Commit PAC-007.2 selected knowledge candidates into memory domain files.

## Implemented command

```bash
pac session commit project.pac.zip --session SES-... --committed-by Tommy
```

## Input artifact

```text
sessions/selection/<session_id>.selection.json
```

## Commit rules

```text
keep=false
    -> ignored

keep=true, category=user
    -> user/memory.json

keep=true, category=project, project_id=<project_id>
    -> projects/<project_id>/memory.json

keep=true, category=shared
    -> shared/memory.json
```

## Provenance

Committed memory entries preserve:

- session id;
- selection path;
- selection version;
- source analysis path;
- source validation path;
- selected by / selected at;
- candidate index;
- candidate source.

## Release artifacts

- `Releases/PAC-007.3/pac-cli-pac0073-memory-commit.zip`
- `Releases/PAC-007.3/pac-cli-pac0073-qa-package.zip`

## Verification

```text
py -m pytest -q
65 passed in 4.15s
```

## Non-goals

- no KEEP / IGNORE decision logic;
- no selection criteria changes;
- no candidate reclassification;
- no PAC-008 cognitive views;
- no handover generation.
