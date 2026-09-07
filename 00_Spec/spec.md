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
relationship_count: 15
hub_score: 18
centrality: 0.135
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

1. The vault is a **cross-domain movement-intelligence engine** serving golf, gait, static posture, squat, and future movement assessments. Use Thomas Myers' Anatomy Trains and Julie Hammond as the anatomical/clinical-philosophy foundation for fascial-line structure; Gray Cook for general movement screening; Chambers & Sutherland for gait terminology and the observational-vs-instrumented boundary; Czaprowski et al. for non-structural posture taxonomy and the app philosophy.
2. Treat fascial lines as a primary knowledge structure, not isolated muscles — but do not treat fascial lines as the only structure.
3. Use Davide Bertoli's golf swing video/transcript as a golf-application reference, not as anatomical truth.
4. Separate stable anatomical/taxonomic knowledge from domain-specific interpretation and from app hypotheses.
5. Do not invent facts. Mark inferred relationships as `hypothesis`, `clinical_interpretation`, or Level 5 app logic.
6. Use consistent Obsidian markdown structure, backlinks, aliases, tags, and YAML frontmatter. Each source carries `evidence_level` and `source_role`.
7. Every note should be useful later for AI, MediaPipe, and movement-analysis app development.

## Evidence Hierarchy

See `evidence_levels.md` for the authoritative spec. Summary:

| Level | Label | Meaning | Allowed Use |
|---:|---|---|---|
| 1 | Foundational Frameworks | Sources that define the engine's core philosophy, terminology, observational logic, and interpretation boundaries (Anatomy Trains, Julie Hammond, Gray Cook, Chambers & Sutherland, Perry & Burnfield [gait eight-phase, framework-cited], Czaprowski et al.). Foundational to reasoning — **not** "highest-quality evidence" and **not** necessarily gold-standard biomechanics. | Define philosophy, terminology, taxonomy, observational structure, observability limits. Do not, by themselves, authorise measurement, causal interpretation, treatment, or report claims. |
| 2 | Domain Taxonomies & General Movement Models | Accepted classifications, phase models, screening structures, and general biomechanical concepts within a domain. | Classification, phase/segment definitions, screening structures, general concept definitions. |
| 3 | Domain-Specific Instrumented Biomechanics | Research using 3D motion capture, force plates, pressure systems, EMG, validated kinematics/kinetics. | Measured/model-derived kinetics, kinematics, EMG, pressure, energetics for that domain. |
| 4 | Applied Coaching, Clinical, or Practice Frameworks | Domain-specific interpretation and applied practice models. Must never override Levels 1-3 or upgrade a 2D proxy into a measured kinetic or causal claim. | Domain phase descriptions, applied relevance, coaching cues, practice models. |
| 5 | App-Logic Hypotheses | Project inference for app logic, MediaPipe proxies, report wording, or clinical reasoning. | Must be marked as hypothesis; never anatomical fact. |

`source_role` records why a source is included (e.g., `foundational_anatomical_framework`, `foundational_clinical_philosophy`, `foundational_movement_framework`, `foundational_domain_taxonomy`, `domain_biomechanics`, `applied_practice`); `evidence_level` alone cannot explain it.

Do not present Level 4 or Level 5 claims as anatomical facts. A foundational (Level 1) source may define philosophy, terminology, taxonomy, or observability limits, but every claim must still be traced to the specific source and `source_role` that supports it.

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

## Domain Relationship Blocks

Movement relationships remain embedded in the existing canonical graph notes; do not
create a separate Markdown page for every relationship. For a domain such as squat,
the movement mapping note and the relevant fascial-line notes must contain a
structured relationship block with this sequence:

`observed pattern -> why the line is considered -> muscle-to-line relationship -> potential clinical issues -> direct assessment/retest -> camera boundary`

Use existing YAML `relationships` fields and body wikilinks to connect the movement,
fascial line, muscles, joints, and app-logic notes. The canonical Markdown notes are
the reasoning source. A machine-readable JSON export may mirror the structured
relationship fields for the app, but it must not become a second reasoning source or
replace the Obsidian graph. Potential clinical issues are hypotheses for assessment,
never camera-detected weakness, tightness, activation, or fascial restriction.

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

| Source | evidence_level | source_role |
|---|---|---|
| [[anatomy_trains_myofascial_thomas_w_myers]] | 1 | foundational_anatomical_framework |
| [[julie_hammond_breakout]] | 1 | foundational_clinical_philosophy |
| [[gray_cook_movement_2010]] | 1 | foundational_movement_framework |
| [[chambers_sutherland_gait_analysis_2002]] | 1 | foundational_domain_taxonomy |
| [[perry_burnfield_gait_analysis]] | 1 | foundational_domain_taxonomy (gait eight-phase; framework-cited — full text not yet in vault) |
| [[czaprowski_nonstructural_posture_2018]] | 1 | foundational_clinical_philosophy |
| [[dr_kwon_golfer_ground_interaction]] | 3 | domain_biomechanics (golf) |
| [[golf_decoded_six_phases_swing]] | 4 | applied_practice (golf) |
| Future peer-reviewed fascia/biomechanics papers | 2-3 | domain taxonomy / domain_biomechanics |
| Future gait / posture depth sources (Whittle, Kendall, Sahrmann) | 3-4 | domain_biomechanics / applied_practice |
| App logic notes | 5 | (app-logic hypothesis) |

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
