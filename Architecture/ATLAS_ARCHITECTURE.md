# Atlas Architecture

## Mission

Atlas aims to ensure cognitive continuity based on information that is:

- traceable;
- verified;
- transmissible.

## Hierarchy

```text
Global Project
`-- Future powerful / self-improving AI system
    `-- Atlas
        `-- Cognitive continuity ecosystem
            `-- PAC
                `-- Portable capsule and CLI tooling
```

## Canonical PAC Pipeline

```text
PAC-005   Import Conversation
PAC-006   Extract Candidate Knowledge
PAC-007.1 Create Validation Artifact
PAC-007.2 Select + Classify Knowledge
PAC-007.3 Commit to Memory
PAC-008   Generate Cognitive Views & Handover
```

## Core Artifact Pipeline

```text
Conversation
    -> Session
    -> Candidate knowledge
    -> Validation artifact
    -> Selection / classification artifact
    -> Official memory
    -> Cognitive views & handover
```

## Fundamental Invariant

An artifact never modifies its source artifact.

Each stage reads the previous artifact and produces a new artifact.

## Current Architectural Clarification

Atlas currently contains the machinery of cognitive continuity:

- PAC releases;
- architecture;
- QA;
- reviews;
- handovers;
- governance.

Atlas does not yet contain a complete persistent memory layer.

The memory layer will be introduced through:

```text
PAC-007.2 - Knowledge Selection & Classification
PAC-007.3 - Memory Commit
PAC-008   - Generate Cognitive Views & Handover
```

## Memory Domains

Future Atlas memory should be split by domain:

```text
user/
    memory.json

projects/
    Atlas/
        memory.json
    PAC/
        memory.json

shared/
    memory.json
```

## PAC Roles

- PAC-005 imports conversations into session artifacts.
- PAC-006 extracts candidate knowledge from sessions.
- PAC-007.1 creates validation artifacts.
- PAC-007.2 selects and classifies knowledge.
- PAC-007.3 should commit selected knowledge into memory.
- PAC-008 should generate cognitive views and handovers from memory.
