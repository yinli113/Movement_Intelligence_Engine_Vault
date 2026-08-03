---
id: temporal_movement_metrics
type: Movement Function
preferred_name: Temporal Movement Metrics
aliases: [time-series movement metrics, temporal analysis, metric-time interpretation]
category: Biomechanics
short_definition: "Principle that a movement metric only acquires meaning across time — as event values, extrema, extrema timing, rates of change, sequencing, phase transitions, and trial-to-trial consistency — never as a single value sampled at one named event."
evidence_level: 2
evidence:
  - source_id: dr_kwon_golfer_ground_interaction
    evidence_level: 3
    supports: "Golf kinematics are time-series curves with declared events and filtering; peaks need not coincide with conventional event markers."
  - source_id: chambers_sutherland_gait_analysis_2002
    evidence_level: 1
    supports: "Gait variables are reported against normalised cycle time with defined events, illustrating the general temporal-reporting convention."
relationships:
  parent_concepts: [movement_chain_model]
  child_concepts: [golf_swing_events]
  related_concepts: [kinematic_sequence, movement_sequencing, energy_transfer, segment_angle_metrics, personalised_movement_intelligence, x_factor]
confidence: medium
review_status: draft_graph_mvp
relationship_count: 9
hub_score: 0
centrality: 0.0
updated: 2026-07-27
---

# Temporal Movement Metrics

## Definition

A movement is a time-varying process, not a collection of static positions. Any metric the engine records must therefore be interpretable as a **curve over time**, characterised by a family of temporal descriptors rather than one number sampled at one named event such as address, top of backswing, or impact.

## Why It Matters

A value measured at a single named event does not describe the movement. Two people can share the same pelvis-rotation value at impact and have produced it with completely different timing, rates, and coordination. Interpreting event-sampled values as if they were the whole movement is the main way snapshot analysis misleads coaching.

## Temporal Descriptor Family

For each measured variable, the engine distinguishes:

| Descriptor | Question it answers |
| :--- | :--- |
| event value | What was the value at a declared event? |
| maximum / minimum | How large did the excursion become? |
| time of extremum | When did the extremum occur (absolute and normalised time)? |
| rate of change | How fast was the variable rising or falling? |
| inter-segment sequence | Which segment moved, peaked, or reversed first? |
| phase transitions | How did the movement pass between declared phases? |
| loading / unloading duration | How long did lengthening and shortening periods persist? |
| consistency across trials | How repeatable is the pattern within and between sessions? |

A maximum is **not assumed** to occur at a conventional event marker; the time of an extremum is itself a measured descriptor.

## Interpretation Layers

### Measured Mechanics — Levels 2–3

Time-series kinematics with declared coordinate frames, filtering, and operational event definitions are legitimate measurements. Derivatives amplify noise; rates of change require stated smoothing and uncertainty.

### Fascial Interpretation — Levels 1–2 plus explicit inference

Temporal features such as dissociation timing or reversal order may be *associated with* fascial-line loading strategies only as a labelled interpretation; timing does not measure tissue behaviour.

### App Hypothesis — Level 5

Camera-derived event times, image-plane extrema, and their timings are Level 5 descriptors with view, frame-rate, and reliability context. They must not be renamed as force, impulse, energy, or tissue state (see [[golf_kinetics_observability_boundary]]).

## Relationships

| Relationship | Target | Role |
| :--- | :--- | :--- |
| parent | [[movement_chain_model]] | Temporal metrics describe the chain over time. |
| child | [[golf_swing_events]] | Golf event set and normalised swing time. |
| interpreted_with | [[kinematic_sequence]] | Sequence is one temporal descriptor family. |
| interpreted_with | [[segment_angle_metrics]] | Orientation-over-time complements joint angles. |
| personalised_by | [[personalised_movement_intelligence]] | Consistency descriptors feed the personal baseline. |
| golf_application | [[x_factor]] | Dissociation is a temporal curve, not a single angle. |

## Parent Concepts

- [[movement_chain_model]]

## Child Concepts

- [[golf_swing_events]]

## Related Concepts

- [[kinematic_sequence]]
- [[movement_sequencing]]
- [[energy_transfer]]
- [[stretch_shortening_cycle]]

## Evidence Level

General temporal-measurement practice is Level 2; golf instrumented kinematics are Level 3; camera-derived temporal descriptors are Level 5.

## App Use

Store and report metric curves with declared events, normalised time, extrema and their timings, rates, and trial consistency. Reject any report that reduces a metric to a single event-sampled value with no temporal context.

## Open Questions

- Which minimal descriptor set (extrema timing + rate + sequence) carries the most coaching value per unit of camera noise?
- How should extrema-detection confidence be reported when smoothing choices shift the estimated time of maximum?
