---
id: kinematic_sequence
type: Movement Pattern
preferred_name: Kinematic Sequence
aliases: [rotational sequence, swing sequencing, segment peak timing]
category: Biomechanics
short_definition: "The observed timing and order of segment kinematics, commonly including angular-velocity peaks."
evidence_level: 3
evidence:
  - source_id: dr_kwon_golfer_ground_interaction
    evidence_level: 3
    supports: "Defines kinematics versus kinetics and reports golf sequence patterns without equating peak order with energy transfer."
  - source_id: bourgain_golf_swing_biomechanics_2022
    evidence_level: 3
    supports: "Systematic review of the proximal-to-distal kinematic-sequence concept as a literature-described population pattern, not a universal individual ideal."
relationships:
  parent_concepts: [movement_chain_model]
  child_concepts: []
  related_concepts: [angular_momentum, energy_transfer, force_transmission, movement_sequencing, functional_lines, x_factor, golf_movement_sequence, temporal_movement_metrics]
confidence: high
review_status: active_spec
relationship_count: 13
hub_score: 19
centrality: 0.172
updated: 2026-07-27
---

# Kinematic Sequence

## Definition

The **kinematic sequence** describes the timing and order of measured segment motion. In golf it commonly compares pelvis, thorax, arm and club angular-velocity curves, provided coordinate frames, rotation sequence, filtering and event definitions are stated.

Temporal peaks in segment angular velocity are kinematics and do not by themselves prove energy transfer. Segment deceleration also does not by itself establish transfer of energy or [[angular_momentum]].

## Why It Matters

Sequence curves are useful descriptions of coordination, but causal claims require kinetics and system-level modelling. A preferred peak order is not automatically efficient, causal or universal.

## Supporting Evidence

[[dr_kwon_golfer_ground_interaction]] anchors the kinematics/kinetics boundary and the cited torsional-separation sequence study. [[golf_decoded_six_phases_swing]] remains Level 4 applied golf interpretation.

## Interpretation Layers

### Measured Mechanics — Level 3

Segment orientations, angular velocities, event times and peak order are kinematics. Forces, moments, impulses and energy require additional measurements and modelling.

### Fascial Interpretation — Levels 1–2 plus explicit inference

[[functional_lines]] remain primary anatomy. Any proposed relationship between their anatomy and a sequence pattern must be labelled interpretation; the temporal sequence does not measure fascial loading.

### App Hypothesis — Level 5

The app may compare observable peak order and timing quality. It must not rename those metrics energy transmission, momentum transfer or kinetic efficiency.

## Relationships

| Relationship | Target | Role |
| :--- | :--- | :--- |
| distinguished_from | [[energy_transfer]] | Kinematic timing is not measured energy transfer. |
| distinguished_from | [[angular_momentum]] | Angular velocity is not system angular momentum. |
| interpreted_with | [[force_transmission]] | Mechanistic interpretation requires separate evidence. |
| anatomically_contextualised_by | [[functional_lines]] | Myofascial anatomy remains a separate evidence layer. |
| supported_by | [[dr_kwon_golfer_ground_interaction]] | Level 3 kinematic boundary. |

## Parent Concepts

- [[movement_chain_model]]

## Child Concepts

- None currently.

## Related Concepts

- [[movement_sequencing]]
- [[energy_transfer]]
- [[force_transmission]]
- [[angular_momentum]]
- [[functional_lines]]
- [[x_factor]]
- [[golf_movement_sequence]]
- [[temporal_movement_metrics]]

## Evidence Level

Golf kinematics are Level 3. Fascial interpretations require their own evidence, and app rules are Level 5.

## App Use

Report coordinate-qualified angular-velocity timing and uncertainty. Do not infer force, moment, impulse, energy, muscle activation or fascial tension from ordinary video.

## Open Questions

- How robust are peak-order classifications to camera view, filtering and event uncertainty?
