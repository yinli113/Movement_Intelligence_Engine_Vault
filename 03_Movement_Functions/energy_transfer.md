---
id: energy_transfer
type: Physics
preferred_name: Energy Transfer
aliases: [mechanical energy transfer, energy flow]
category: Physics
short_definition: "The quantified transfer of mechanical energy between defined system components."
evidence_level: 2
evidence:
  - source_id: dr_kwon_golfer_ground_interaction
    evidence_level: 3
    supports: "Provides external forces and moments relevant to mechanical work but does not itself establish tissue-level energy transfer."
relationships:
  parent_concepts: [movement_chain_model]
  child_concepts: [elastic_energy]
  related_concepts: [golfer_ground_interaction_model, force_transmission, kinematic_sequence, angular_momentum, functional_lines]
confidence: medium
review_status: active_spec
relationship_count: 25
hub_score: 69
centrality: 0.225
updated: 2026-07-16
---

# Energy Transfer

## Definition

**Energy transfer** is the quantified movement of mechanical energy between defined system components. It requires work, power or energy analysis with explicit forces or moments, velocities, reference frames and system boundaries.

## Why It Matters

Energy is not force, moment, momentum or angular velocity. Segment peak timing and deceleration can coexist with transfer, storage, dissipation or external work; kinematics alone cannot choose among them.

## Supporting Evidence

### Measured Mechanics — Levels 2–3

Force and motion data can support work and power calculations when synchronised and modelled. [[dr_kwon_golfer_ground_interaction]] supplies Level 3 external mechanics, not a direct measure of energy moving through tissues.

### Fascial Interpretation — Levels 1–2 plus explicit inference

[[functional_lines]] remain the primary anatomical structure. Claims about elastic storage or release along a line require independent fascia evidence and must not be attributed to Kwon's force-plate results.

### App Hypothesis — Level 5

Any “energy flow”, “energy leak” or “transmission efficiency” label derived from video sequencing is a Level 5 hypothesis and should be replaced with the observed kinematic feature unless validated against an energetic measure.

## Sensor Boundary

Ordinary video cannot measure energy transfer, force, pressure, moments, impulses, muscle activation or fascial tension. Temporal peaks in segment angular velocity do not by themselves prove energy transfer.

## Relationships

| Relationship | Target | Role |
| :--- | :--- | :--- |
| distinguished_from | [[kinematic_sequence]] | Peak timing does not measure energy. |
| distinguished_from | [[force_transmission]] | Force and energy are separate quantities. |
| may_be_modelled_with | [[golfer_ground_interaction_model]] | External forces and moments may enter work analysis. |
| anatomically_interpreted_with | [[functional_lines]] | Requires a separate evidence layer. |
| supported_by | [[dr_kwon_golfer_ground_interaction]] | External mechanics, not tissue energy transfer. |

## Parent Concepts

- [[movement_chain_model]]

## Child Concepts

- Elastic energy remains a legacy unresolved YAML relationship; no standalone concept node currently exists.

## Related Concepts

- [[force_transmission]]
- [[kinematic_sequence]]
- [[angular_momentum]]
- [[functional_lines]]

## Evidence Level

General energy mechanics are Level 2; golf-specific measured mechanics are Level 3; video-derived energetic interpretations are Level 5.

## App Use

In video-only mode, report sequence timing, displacement and velocity rather than energy transfer or efficiency. Energetic labels require compatible force and kinematic data.

## Open Questions

- Which validated joint-power or golfer-club work measures could ground future app features?
