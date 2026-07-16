---
id: movement_sequencing
type: Motor Control
preferred_name: Movement Sequencing
aliases: [kinematic sequencing, movement timing, sequencing]
short_definition: "The ordered timing of body segment actions that allows movement to transfer force efficiently across the system."
relationships:
  contains: [golf_swing, golf_swing_transition]
  connects_to: [force_transmission, energy_transfer, golf_decoded_six_phases_swing]
  produces: [coordinated_movement]
  assists: [golf_swing_transition]
  stabilizes: []
  limits: []
  compensates_for: []
  active_during: [golf_swing]
  assessed_by: [planned_transition_observation_screen]
  improved_by: [planned_transition_sequence_drill]
  supported_by: [golf_decoded_six_phases_swing]
  relevant_to: [thoracic_rotation, hip_internal_rotation, trail_shoulder_external_rotation]
confidence: medium
review_status: draft_graph_mvp
relationship_count: 21
hub_score: 61
centrality: 0.362
updated: 2026-06-30
---

# Movement Sequencing

## Definition

Movement sequencing is the ordered timing of segment actions that allows movement to emerge from the interaction of joints, muscles, connective structures, external forces, and motor control.

## Why It Matters

For golf analysis, sequencing lets the graph ask whether force is being transferred through the system or recreated by compensation at a later segment.

## Supporting Evidence From Source

The [[golf_decoded_six_phases_swing]] source presents the swing as six phase intervals, which supports modeling the swing as a time-ordered sequence rather than one static position.

## Related Concepts

- [[golf_swing]]
- [[golf_swing_transition]]
- [[force_transmission]]
- [[energy_transfer]]

## Parent Concepts

- [[golf]]
- Motor Control

## Child Concepts

- [[address_to_shaft_parallel]]
- [[shaft_parallel_to_end_pelvis_rotation]]
- [[end_pelvis_rotation_to_top_backswing]]
- [[golf_swing_transition]]
- [[max_unweighting_to_impact]]
- [[impact_to_hands_chest_height]]

## Category

Motor Control
