# Dr. Kwon Golf Biomechanics Vault Integration Design

**Date:** 2026-07-16  
**Status:** Approved design, pending implementation plan  
**Scope:** `Movement_Intelligence_Engine_Vault` only; no changes to the current gait application

## Objective

Integrate Dr. Young-Hoo Kwon's golfer-ground interaction research into the Movement Intelligence Engine Vault as a Level 3 golf-biomechanics layer while preserving the vault's fascial-line-first architecture.

The finished graph must support this traversal:

```text
Primary Kwon source
-> golfer-ground interaction concept
-> swing phase or position
-> joint and connective-structure pathway
-> myofascial line loading/stabilising/releasing interpretation
-> camera-observable proxy or unavailable kinetic variable
-> cautious app-report boundary
```

## Scope Boundaries

### In scope

- Deep research using Dr. Kwon's own biomechanics material and peer-reviewed publications.
- Claim-level citations and evidence locators.
- A central golfer-ground interaction model and reusable mechanics nodes.
- Bidirectional links to golf phases, positions, body structures, connective structures, and myofascial lines.
- A future-app observability matrix that distinguishes direct measurements from camera-derived proxies.
- Index, source log, graph metrics, orphan checks, and broken-link checks.

### Out of scope

- Changes to the current gait-only movement-assessment application.
- Force, pressure, torque, impulse, or fascial-load estimation from ordinary video.
- Exercise prescription, diagnosis, injury prediction, or treatment recommendations.
- Bulk vault renaming or migration.
- Treating Anatomy Trains interpretations as findings made or validated by Kwon.

## Evidence Architecture

The integration will preserve the five-level evidence hierarchy in `00_Spec/spec.md`:

1. Anatomy Trains structure establishes line membership and stable anatomical pathways.
2. General biomechanics supports tissue, joint, and force-transmission principles.
3. Kwon and peer-reviewed golf biomechanics support golfer-ground kinetics and swing mechanics.
4. Applied golf sources support coaching interpretations only.
5. Camera-derived calculations and app mappings remain explicit hypotheses.

Every mixed-domain note will separate:

- **Measured golf biomechanics (Level 3):** what force plates, motion capture, or inverse-dynamics research measures.
- **Fascial-line interpretation (Levels 1–4 combined):** how an externally measured load may traverse stable anatomical structures in the vault's model.
- **App hypothesis (Level 5):** what pose landmarks might describe without claiming force, pressure, tissue tension, or causation.

## Graph Design

### Source layer

Upgrade `dr_kwon_golfer_ground_interaction` into a source dossier with:

- canonical bibliographic metadata;
- primary and peer-reviewed source list;
- claim-to-source evidence table;
- terminology and equations;
- limitations and disagreements;
- links to every extracted concept;
- explicit separation between Kwon's findings and vault interpretation.

### Central model

Create `golfer_ground_interaction_model` as the primary Level 3 hub. It will connect:

- ground reaction force;
- golfer-ground interaction moment / ground reaction moment;
- centre of mass;
- centre of pressure;
- moment arm;
- free moment or pivoting moment where supported;
- linear and angular impulse;
- angular momentum;
- pressure/weight distribution versus force;
- movement sequencing and swing-phase timing.

New nodes will be created only when a concept is reusable and does not duplicate an existing note.

### Golf-phase layer

The model will link into the six existing swing intervals and their boundary positions. Each affected phase note will distinguish:

- source-defined phase boundary;
- Kwon-supported kinetic behaviour;
- relevant joint and segment behaviour;
- fascial lines loading, stabilising, or releasing;
- direct measurements versus camera-only proxies;
- open questions where timing or direction is not adequately supported.

### Fascial-line-first integration

Myofascial lines remain the primary anatomical reasoning structure. Kwon's research supplies external-force inputs; it does not independently prove fascial loading.

The integration will map kinetics through specific anatomical bridges:

| External/mechanical concept | Anatomical bridge | Primary fascial-line questions |
|---|---|---|
| Foot-ground force and moment | Foot/ankle, plantar fascia, tibia, hip | Deep Front, Spiral, Lateral, and Superficial Back Line support |
| Pelvis translation and rotation | Hip joints, sacrum, thoracolumbar fascia | Functional Lines, Spiral Line, and Lateral Line transmission/braking |
| Trunk rotation and side bend | Lumbar/thoracic spine, rib cage, abdominal wall | Functional, Spiral, Lateral, and Deep Front Line coordination |
| Upper-body and club acceleration/deceleration | Scapula/shoulder complex and arm lines | Functional Lines and arm-line continuation |

For every fascial claim:

- stable line anatomy must cite Level 1 or Level 2 evidence;
- golf relevance must be labelled interpretation rather than direct Kwon evidence;
- loading, stabilising, and releasing roles must be phase-specific;
- camera geometry must not be called fascial tension, elasticity, or force;
- unsupported causal language will be removed or marked `needs_evidence`.

At minimum, the integration will review and link the Back, Front, and Ipsilateral Functional Lines, Spiral Line, Deep Front Line, Lateral Line, Superficial Back Line, and relevant arm lines.

## App Translation Boundary

A dedicated app-facing note or matrix will classify each concept as:

| Class | Meaning | Example |
|---|---|---|
| Direct kinetic measurement | Requires force plates, pressure insoles, or validated instrumentation | GRF, COP, free moment, impulse |
| Motion-capture measurement | Requires calibrated 3D kinematics or validated modelling | segment angular velocity, COM estimate |
| Camera-observable descriptor | Pose landmarks can describe geometry or timing with view-specific limits | pelvis/thorax orientation proxy, vertical hip-midpoint motion |
| Level 5 hypothesis | A proposed relationship requiring validation | inferred phase association with a fascial-line pattern |
| Unavailable/prohibited claim | Must not appear as measured output from video | torque generation, ground force, fascial tension, energy transfer efficiency |

Future app language will use `camera-observed`, `image-plane proxy`, `timing descriptor`, and `consistent with` where appropriate. It will not use `measured force`, `pressure`, `tissue loading`, or diagnostic wording without the required sensors and validation.

## Files and Responsibilities

Implementation is expected to touch:

- `00_Spec/sources/dr_kwon_golfer_ground_interaction.md`
- a new central model note under `03_Movement_Functions/`
- existing reusable mechanics notes under `03_Movement_Functions/`
- relevant phase and position notes under `04_Golf_Swing/`
- relevant fascial-line notes under `01_Fascial_Lines/`
- an app-observability note under `05_App_Logic/`
- `index.md`, `00_Spec/log.md`, and graph metrics

The exact file list will be decided after source extraction and duplicate-node review.

## Quality and Verification

The implementation will be accepted when:

- primary claims have precise, reachable citations;
- Kwon-derived claims are not attributed to Anatomy Trains, and fascial interpretations are not attributed to Kwon;
- all new notes have required frontmatter and required markdown sections;
- every new note has an index link and at least one contextual backlink;
- the graph can traverse from source to mechanics to phase to fascial line to app boundary;
- direct measurements and video proxies are visibly separated;
- no new broken wikilinks or orphan notes remain;
- graph metrics are recalculated;
- unrelated user changes remain untouched;
- the final Git commit contains only this integration's intended files.

## Risks and Controls

- **Terminology drift:** preserve Kwon's definitions and record aliases rather than collapsing different moment concepts.
- **Overclaiming from video:** enforce the observability matrix and app-language prohibitions.
- **Fascial causality overreach:** use stable anatomy plus explicitly labelled golf interpretation.
- **Source fragility:** prefer peer-reviewed papers and stable primary pages; store complete bibliographic data and access dates.
- **Graph sprawl:** reuse existing nodes and create only concepts that support multiple traversals.

