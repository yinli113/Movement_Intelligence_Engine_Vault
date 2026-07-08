---
id: vault_spec
type: Spec
preferred_name: Fascial Movement Intelligence Vault Spec
aliases: [project spec, vault spec, graph operating spec]
short_definition: "Authoritative operating specification for the fascial movement intelligence Obsidian knowledge graph."
relationships:
  governs: [fascial_line_model, golf_swing, movement_sequencing, force_transmission, energy_transfer, mediapipe_landmark_mapping]
  separates: [stable_anatomical_knowledge, golf_application_interpretation, app_logic_hypothesis]
  supported_by: [anatomy_trains_myers_2009, julie_hammond_breakout, golf_decoded_six_phases_swing]
confidence: high
review_status: active_spec
relationship_count: 9
hub_score: 11
centrality: 0.18
updated: 2026-07-01
---

# Fascial Movement Intelligence Vault Spec

## Purpose

This vault is a permanent Obsidian knowledge graph for human movement, fascia, biomechanics, and golf swing analysis.

The long-term goal is to support an AI app that analyzes golf swing movement using:

- fascial line loading
- posture and body structure relationships
- movement sequencing
- force transmission
- energy-flow timing
- compensation detection
- MediaPipe-observable movement proxies

The vault is not a textbook summary library. Markdown notes are the view. The product is the graph.

## Foundational Rules

1. Use Thomas Myers' Anatomy Trains and Julie Hammond as the anatomical foundation for fascial-line structure.
2. Treat fascial lines as the primary knowledge structure, not isolated muscles.
3. Use Davide Bertoli's golf swing video/transcript as a golf-application reference, not as anatomical truth.
4. Separate stable anatomical knowledge from golf-specific interpretation.
5. Do not invent facts. Mark inferred relationships as `hypothesis`, `clinical_interpretation`, or Level 5 app logic.
6. Use consistent Obsidian markdown structure, backlinks, aliases, tags, and YAML frontmatter.
7. Every note should be useful later for AI, MediaPipe, and movement-analysis app development.

## Evidence Hierarchy

| Level | Label | Meaning | Allowed Use |
|---:|---|---|---|
| 1 | Anatomy Trains anatomical structure | Anatomy Trains / Julie Hammond fascial-line anatomy and structural relationships | Stable fascial-line definitions and structure membership |
| 2 | Peer-reviewed fascia and biomechanics research | Research literature on fascia, biomechanics, motor control, anatomy, or force transmission | Strengthen anatomy and biomechanics relationships |
| 3 | Golf biomechanics research | Golf-specific biomechanics research | Validate swing phase mechanics, sequencing, kinetics, and kinematics |
| 4 | Davide Bertoli golf application interpretation | Golf coaching/application interpretation from Davide Bertoli material | Golf relevance and applied swing interpretation only |
| 5 | Our AI app hypothesis | Project inference for app logic, MediaPipe proxies, report wording, or clinical reasoning | Must be marked as hypothesis; never anatomical fact |

Do not present Level 4 or Level 5 claims as anatomical facts.

## Required Top-Level Structure

```text
00_Spec/
  spec.md
  naming_conventions.md
  evidence_levels.md

01_Fascial_Lines/
  Superficial Back Line
  Superficial Front Line
  Lateral Line
  Spiral Line
  Deep Front Line
  Functional Lines
  Arm Lines

02_Body_Structures/
  Pelvis
  Lumbar Spine
  Thoracic Spine
  Rib Cage
  Scapula
  Shoulder Complex
  Hip Complex
  Foot and Ankle
  Sacrotuberous Ligament
  Thoracolumbar Fascia
  Diaphragm
  Psoas
  Pelvic Floor

03_Movement_Functions/
  Stability
  Rotation
  Counter-Rotation
  Elastic Loading
  Eccentric Loading
  Energy Transfer
  Ground Reaction Force
  Center of Mass
  Compensation
  Timing Delay

04_Golf_Swing/
  Golf Swing Overview
  Six Phases of Golf Swing
  Phase 1 Address to Shaft Parallel
  Phase 2 Shaft Parallel to End Pelvis Rotation
  Phase 3 End Pelvis Rotation to Top of Backswing
  Phase 4 Top of Backswing to Maximum Unweighting
  Phase 5 Maximum Unweighting to Impact
  Phase 6 Impact to Follow Through

05_App_Logic/
  Static Fascial Line Assessment
  Dynamic Fascial Loading
  Energy Flow Sequence
  MediaPipe Landmark Mapping
  Compensation Detection
  Confidence Scoring
  Report Output Logic
```

Current legacy folders under `wiki/` may remain during migration. New or converted MVP notes should follow this structure unless a deliberate migration plan says otherwise.

## Primary Node Types

- `Fascial Line`
- `Muscle`
- `Connective Structure`
- `Joint`
- `Joint Action`
- `Body Structure`
- `Movement Function`
- `Golf Phase`
- `Movement Pattern`
- `Limitation Pattern`
- `Compensation`
- `Assessment`
- `Exercise`
- `Evidence Source`
- `App Logic`
- `Spec`

## Concept Categories

Every important concept should be classified into one or more of:

- Anatomy
- Muscle
- Joint
- Bone
- Ligament
- Fascia
- Fascial Line
- Movement Phase
- Movement Pattern
- Biomechanics
- Physics
- Motor Control
- Rehabilitation
- Golf
- App Logic

## Required YAML Frontmatter

Every graph note should begin with YAML:

```yaml
---
id: canonical_snake_case_id
type: Fascial Line
preferred_name: Human Readable Name
aliases: []
tags: []
category: Fascial Line
short_definition: "One sentence definition."
evidence_level: 1
evidence:
  - source_id: anatomy_trains_myers_2009
    evidence_level: 1
    supports: "Specific supported claim."
relationships:
  parent_concepts: []
  child_concepts: []
  related_concepts: []
  stable_anatomy: []
  golf_interpretation: []
  app_hypotheses: []
relationship_count: 0
hub_score: 0
centrality: 0.0
confidence: medium
review_status: draft
updated: 2026-07-01
---
```

Use plain IDs in YAML. Use Obsidian links in markdown body.

## Required Markdown Sections

Every important concept note should include:

1. `## Definition`
2. `## Why It Matters`
3. `## Supporting Evidence`
4. `## Relationships`
5. `## Parent Concepts`
6. `## Child Concepts`
7. `## Related Concepts`
8. `## Evidence Level`
9. `## App Use`
10. `## Open Questions`

Prefer relationship tables over prose where possible.

## Fascial Line Note Requirements

Each fascial line note must include:

- Definition
- Anatomy Trains source role
- Main anatomical structures
- Related joints
- Movement functions
- Loading direction
- Release direction
- Golf swing relevance
- Possible restrictions
- Possible compensations
- MediaPipe-observable proxies
- Evidence level
- Links to related notes

Stable anatomy and golf interpretation must be separated:

```text
Stable Anatomy
-> Anatomy Trains structure membership
-> Level 1 or Level 2 evidence

Golf Interpretation
-> swing phase relevance
-> possible restriction or compensation
-> Level 3, 4, or 5 evidence
```

## Golf Phase Note Requirements

Each golf phase note must include:

- Phase definition
- Main movement goal
- Center of Mass behaviour
- Pelvis behaviour
- Thorax/rib cage behaviour
- Shoulder/scapula behaviour
- Main fascial lines loading
- Main fascial lines stabilizing
- Main fascial lines releasing
- Possible timing delays
- Possible energy-flow blocks
- Compensation patterns
- MediaPipe measurements
- App report wording
- Evidence level
- Links to related notes

Do not state golf-application interpretations as anatomy. Golf phase notes should explicitly separate:

- source-defined phase boundaries
- biomechanical research
- golf application interpretation
- app hypothesis

## Relationship-First Graph Rules

The graph should prioritize relationships over isolated facts.

Preferred reasoning paths:

```text
Movement Pattern
-> Joint Action
-> Muscle
-> Connective Structure
-> Fascial Line
-> Compensation
-> Assessment
-> Exercise
```

```text
Golf Phase
-> Center of Mass behaviour
-> Ground Reaction Force
-> Fascial Line loading
-> Connective Structure force transfer
-> Timing Delay
-> Compensation
-> App Report Output
```

Whenever possible:

- connect concepts instead of listing them
- infer missing relationships cautiously
- avoid duplicate nodes
- mark inferred relationships as hypotheses
- think in terms of force transmission, energy transfer, loading, release, and sequencing

## Source Roles

| Source | Role |
|---|---|
| [[anatomy_trains_myofascial_thomas_w_myers]] | Level 1 source for Anatomy Trains fascial-line structure |
| [[julie_hammond_breakout]] | Level 1 supporting source summary for Anatomy Trains concepts and BodyReading language |
| [[golf_decoded_six_phases_swing]] | Level 4 golf-application source for six-phase swing interpretation |
| Future peer-reviewed fascia/biomechanics papers | Level 2 support |
| Future golf biomechanics papers | Level 3 support |
| App logic notes | Level 5 hypothesis |

## MediaPipe Readiness

Do not integrate MediaPipe implementation until the graph schema is stable.

However, notes should prepare for MediaPipe by listing observable proxies, such as:

- pelvis rotation angle
- thorax rotation angle
- shoulder/scapula proxy landmarks
- hip sway
- center of mass proxy
- foot pressure proxy if unavailable, inferred from posture and timing only
- timing between phase events
- left/right asymmetry

MediaPipe proxy fields are hypotheses unless validated against biomechanics or measurement sources.

## Confidence and Review Status

Use `confidence` to describe relationship reliability:

- `high`: direct stable evidence from source and low interpretation burden
- `medium`: supported by source plus moderate interpretation
- `low`: plausible but needs review

Use `review_status` values:

- `active_spec`
- `draft_graph_mvp`
- `source_extracted`
- `needs_evidence`
- `clinical_interpretation`
- `app_hypothesis`
- `needs_review`

## Migration Rule

Do not bulk-move or bulk-rename the existing vault without a migration plan.

For now:

1. New controlling spec files go in `00_Spec/`.
2. New high-level graph notes should use the new numbered structure.
3. Existing `wiki/` notes can remain as legacy graph nodes during transition.
4. When a numbered-folder note replaces a legacy note, link both ways or document the merge.
5. Do not duplicate concepts. Prefer merging into the existing node or creating a redirect-style note.

## Done Criteria for Future Work

A future conversion is done when:

- important concepts are graph nodes
- relationships are explicit
- evidence levels are marked
- stable anatomy is separated from golf interpretation
- app hypotheses are marked as hypotheses
- backlinks exist
- no duplicate nodes are created
- no broken Obsidian links remain
- graph metrics can be recalculated
