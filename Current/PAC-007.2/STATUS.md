# PAC-007.2 - Knowledge Selection & Classification

Status: Done

## Goal

Transform extracted and validated analysis items into selected/classified knowledge candidates.

## Implemented command

```bash
pac session select project.pac.zip --session SES-... --selected-by Tommy
```

## Required decision pipeline

```text
Information extracted
    -> keep / ignore
    -> if keep: user / project / shared
    -> if project: project_id
```

## Output artifact

```text
sessions/selection/<session_id>.selection.json
```

Candidate shape:

```json
{
  "statement": "...",
  "keep": true,
  "category": "project",
  "project_id": "Atlas",
  "reason": "Decision relevant to project continuity",
  "source": {
    "analysis_field": "decisions",
    "index": 0
  }
}
```

## Release artifacts

- `Releases/PAC-007.2/pac-cli-pac0072-selection-classification.zip`
- `Releases/PAC-007.2/pac-cli-pac0072-qa-package.zip`

## Verification

```text
py -m pytest -q
58 passed in 2.74s
```

## Non-goals

- no direct commit to `user/memory.json`;
- no direct commit to `projects/<project_id>/memory.json`;
- no direct commit to `shared/memory.json`;
- no modification of source sessions;
- no modification of source analyses;
- no modification of validation artifacts;
- no PAC-008 handover generation.
