---
id: golf_swing
type: Movement Pattern
preferred_name: Golf Swing
aliases: [golf swing, full golf swing]
short_definition: "A whole-body rotational sport movement that transfers force from ground contact through the body to the club."
sports: [Golf]
phases:
  - address_to_shaft_parallel
  - shaft_parallel_to_end_pelvis_rotation
  - end_pelvis_rotation_to_top_backswing
  - golf_swing_transition
  - max_unweighting_to_impact
  - impact_to_hands_chest_height
relationships:
  contains: [address_to_shaft_parallel, shaft_parallel_to_end_pelvis_rotation, end_pelvis_rotation_to_top_backswing, golf_swing_transition, max_unweighting_to_impact, impact_to_hands_chest_height]
  connects_to: [movement_sequencing, force_transmission, energy_transfer]
  produces: [clubhead_speed, ball_flight]
  assists: []
  stabilizes: []
  limits: []
  compensates_for: []
  active_during: []
  assessed_by: [planned_transition_observation_screen]
  improved_by: [planned_transition_sequence_drill]
  supported_by: [golf_decoded_six_phases_swing]
  relevant_to: [functional_line, spiral_line, deep_front_line, lateral_line, superficial_back_line]
confidence: medium
review_status: graph_mvp_updated
relationship_count: 28
hub_score: 86
centrality: 0.571
updated: 2026-06-30
---

# Golf Swing

## Definition

The Golf Swing is a whole-body rotational sport movement that transfers force from ground contact through the body to the club.

## Why It Matters

It is the parent movement pattern for the golf phase graph. The swing should be reasoned through [[movement_sequencing]], [[force_transmission]], and [[energy_transfer]], not isolated muscle action.

```mermaid
graph TD
    A[Address to Shaft Parallel] --> B[Shaft Parallel to End Pelvis Rotation]
    B --> C[End Pelvis Rotation to Top Backswing]
    C --> D[Golf Transition Phase]
    D --> E[Max Unweighting to Impact]
    E --> F[Impact to Hands Chest Height]
    
    style D fill:#f9f,stroke:#333,stroke-width:2px
```

## Supporting Evidence From Source

The [[golf_decoded_six_phases_swing]] screenshot defines six swing intervals from Address through Hands Chest Height.

## Relationship Table

| Relationship | Target |
|---|---|
| contains | [[address_to_shaft_parallel]] |
| contains | [[shaft_parallel_to_end_pelvis_rotation]] |
| contains | [[end_pelvis_rotation_to_top_backswing]] |
| contains | [[golf_swing_transition]] |
| contains | [[max_unweighting_to_impact]] |
| contains | [[impact_to_hands_chest_height]] |
| connects_to | [[movement_sequencing]] |
| connects_to | [[force_transmission]] |
| connects_to | [[energy_transfer]] |

## Related Concepts

- [[ground_reaction_force]]
- [[toe_loading]]
- [[hip_internal_rotation]]
- [[thoracic_rotation]]
- [[trail_shoulder_external_rotation]]
- [[functional_line]]
- [[spiral_line]]

## Parent Concepts

- [[golf]]

## Child Concepts

- [[address_to_shaft_parallel]]
- [[shaft_parallel_to_end_pelvis_rotation]]
- [[end_pelvis_rotation_to_top_backswing]]
- [[golf_swing_transition]]
- [[max_unweighting_to_impact]]
- [[impact_to_hands_chest_height]]

## Category

Golf
