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
relationship_count: 22
hub_score: 63
centrality: 0.198
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

## Evidence Grounding
```yaml
evidence:
  - source_id: dr_kwon_golfer_ground_interaction
    level: domain_biomechanics
    evidence_tier: Level 3
    description: "Kinematic sequencing and proximal-to-distal segmental angular velocity transfer."
  - source_id: anatomy_trains_myers_2009
    level: foundational_anatomical_framework
    evidence_tier: Level 2
    description: "Multi-joint fascial tensioning and elastic recoil mechanisms."
```
