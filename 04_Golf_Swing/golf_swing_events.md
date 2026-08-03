---
id: golf_swing_events
type: Golf Phase
preferred_name: Golf Swing Events and Normalised Time
aliases: [golf event set, normalised swing time, golf swing phase events]
category: Golf
short_definition: "The declared golf-swing event sequence (address, backswing, top, transition, early downswing, delivery, impact, early follow-through, finish) expressed on a normalised swing-time axis so metrics are compared by when they happen, not only by position."
evidence_level: 4
evidence:
  - source_id: golf_decoded_six_phases_swing
    evidence_level: 4
    supports: "Provides the applied six-interval swing segmentation the vault preserves."
  - source_id: dr_kwon_golfer_ground_interaction
    evidence_level: 3
    supports: "Supplies operationally defined research events (EPR, TB, BI) for the supported crosswalk entries only."
relationships:
  parent_concepts: [golf_swing, temporal_movement_metrics]
  child_concepts: []
  related_concepts: [x_factor, golf_movement_sequence, golf_swing_transition, kinematic_sequence, golf_kinetics_observability_boundary]
confidence: medium
review_status: draft_graph_mvp
relationship_count: 8
hub_score: 0
centrality: 0.0
updated: 2026-07-27
---

# Golf Swing Events and Normalised Time

## Definition

Golf metrics are interpreted on a **normalised swing-time axis** (0–100% of the swing) against a declared set of events. The vault's working event vocabulary, used for app timing descriptions, is:

address → backswing → top of backswing → transition → early downswing → delivery → impact → early follow-through → finish.

## Why It Matters

Comparing two swings by named positions alone hides the timing that actually distinguishes them. Normalised time lets the engine say a metric peaked at, for example, "78% of the downswing" and compare that timing across trials and sessions — see [[temporal_movement_metrics]].

## Relationship to the Vault's Six Phases

This event vocabulary is an **app timing overlay**, not a replacement for the six Level 4 vault phases defined by [[golf_decoded_six_phases_swing]] and preserved in [[golf_swing]]. The conservative Kwon crosswalk in [[golf_swing]] still governs which events are supported research matches (EPR, TB, BI); unmapped labels must not be substituted for Kwon events.

## Extrema Are Not Pinned to Events

A metric's maximum or minimum is **not assumed** to occur at a conventional event marker. The time of each extremum is itself measured on the normalised axis; for example, maximum pelvis-thorax dissociation may occur just after the top of backswing, during early transition (see [[x_factor]]).

## Interpretation Layers

### Measured Mechanics — Levels 3–4

Research events with operational definitions (EPR, TB, BI) are Level 3 anchors; the six-phase intervals remain Level 4 applied segmentation.

### App Hypothesis — Level 5

Camera-detected event times and normalised-time metrics are Level 5 descriptors with view, frame-rate, and reliability context, governed by [[golf_kinetics_observability_boundary]].

## Relationships

| Relationship | Target | Role |
| :--- | :--- | :--- |
| parent | [[golf_swing]] | Events overlay the six-phase swing model. |
| parent | [[temporal_movement_metrics]] | Provides the normalised-time method. |
| applied_in | [[x_factor]] | Dissociation is tracked against these events. |
| applied_in | [[golf_movement_sequence]] | Full-sequence timing is event-referenced. |
| bounded_by | [[golf_kinetics_observability_boundary]] | Event timing is a camera descriptor. |

## Parent Concepts

- [[golf_swing]]
- [[temporal_movement_metrics]]

## Child Concepts

- None currently.

## Related Concepts

- [[golf_swing_transition]]
- [[kinematic_sequence]]

## Evidence Level

Phase segmentation is Level 4; research event anchors are Level 3; camera event timing is Level 5.

## App Use

Report metric timing as normalised swing time with the nearest declared event named for readability, plus the detection confidence. Never present an unmapped app event label as a validated research event.

## Open Questions

- Which operational definitions make "delivery" and "early downswing" reliably detectable on single-camera video?
- Should normalisation anchor on address→impact or address→finish for partial-swing captures?
