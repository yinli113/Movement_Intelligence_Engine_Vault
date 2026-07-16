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
  connects_to: [movement_sequencing, force_transmission, energy_transfer, golfer_ground_interaction_model]
  produces: [clubhead_speed, ball_flight]
  assists: []
  stabilizes: []
  limits: []
  compensates_for: []
  active_during: []
  assessed_by: [planned_transition_observation_screen]
  improved_by: [planned_transition_sequence_drill]
  supported_by: [golf_decoded_six_phases_swing, dr_kwon_golfer_ground_interaction]
  relevant_to: [functional_lines, spiral_line, deep_front_line, lateral_line, superficial_back_line]
confidence: medium
review_status: graph_mvp_updated
relationship_count: 32
hub_score: 93
centrality: 0.653
updated: 2026-07-16
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

## Kwon Event Crosswalk

The six vault phases remain the Level 4 intervals defined by [[golf_decoded_six_phases_swing]]. This table crosswalks boundary events only; it does not replace those phases with Kwon's research phases. A Kwon label is used only where the operational event is supported by [[dr_kwon_golfer_ground_interaction]].

| Vault boundary event | Kwon terminology | Crosswalk status |
| :--- | :--- | :--- |
| [[address_position|Address]] | not yet mapped | The vault position and Kwon's beginning events have not been shown to use the same operational definition. |
| [[shaft_parallel_position|Shaft Parallel]] | not yet mapped | No supported equivalence has been established. |
| [[end_pelvis_rotation|End Pelvis Rotation]] | EPR | Supported event match; Kwon also uses EPR to begin the extended downswing, without changing the vault's phase boundary. |
| [[top_backswing_position|Top Backswing]] | TB | Supported event match. |
| [[max_unweighting|Max Unweighting]] | not yet mapped | This source-defined vault event is not established as a Kwon event. |
| [[impact_position|Impact]] | BI (ball impact) | Supported event match. |
| [[hands_chest_height_position|Hands Chest Height]] | not yet mapped | It must not be substituted for Kwon's MF or LF events without matching definitions. |

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
| connects_to | [[golfer_ground_interaction_model]] |
| supported_by | [[dr_kwon_golfer_ground_interaction]] |

## Related Concepts

- [[ground_reaction_force]]
- [[toe_loading]]
- [[hip_internal_rotation]]
- [[thoracic_rotation]]
- [[trail_shoulder_external_rotation]]
- [[functional_lines]]
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
