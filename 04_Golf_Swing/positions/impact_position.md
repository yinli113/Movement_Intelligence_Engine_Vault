---
id: impact_position
type: Movement Pattern
preferred_name: Impact Position
aliases: [impact, ball impact]
short_definition: "Golf swing boundary event where the club contacts the ball."
relationships:
  contains: [force_transmission, energy_transfer]
  connects_to: [max_unweighting_to_impact, impact_to_hands_chest_height, golf_swing]
  produces: [ball_flight]
  assists: []
  stabilizes: []
  limits: []
  compensates_for: []
  active_during: [max_unweighting_to_impact, impact_to_hands_chest_height]
  assessed_by: [planned_impact_sequence_screen]
  improved_by: []
  supported_by: [golf_decoded_six_phases_swing, dr_kwon_golfer_ground_interaction]
  relevant_to: [golfer_ground_interaction_model, ground_reaction_force, moment_arm, center_of_mass, linear_impulse, angular_impulse, functional_lines, spiral_line]
confidence: medium
review_status: draft_graph_mvp
relationship_count: 15
hub_score: 33
centrality: 0.135
updated: 2026-07-16
---

# Impact Position

## Definition

Impact Position is the boundary event where club and ball contact occurs.

## Why It Matters

It is the output checkpoint for what the historical vault described as force transmission and energy transfer through the preceding phases. Those phrases are historical/vault interpretation; under the golf kinetics observability boundary, measured energy transfer is unavailable from ordinary video and requires compatible kinetic and kinematic instrumentation.

## Supporting Evidence From Source

The [[golf_decoded_six_phases_swing]] screenshot labels Impact as the end of [[max_unweighting_to_impact]] and the start of [[impact_to_hands_chest_height]].

## Related Concepts

| Relationship | Target |
|---|---|
| ends | [[max_unweighting_to_impact]] |
| starts | [[impact_to_hands_chest_height]] |
| produces | ball flight |
| related_to | [[force_transmission]], [[energy_transfer]] |
| relevant_to | [[golfer_ground_interaction_model]], [[ground_reaction_force]], [[moment_arm]], [[center_of_mass]], [[linear_impulse]], [[angular_impulse]] |
| crosswalks_to | Kwon BI event |

BI is a source-supported kinematic timing event. It can bound instrumented force and moment integration, but an impact frame does not measure GRF, external moment, impulse, energy transfer or tissue state. Camera event time is bounded by frame rate and visibility; exact contact may fall between frames, and timing uncertainty must be reported.

## Parent Concepts

- [[golf_swing]]

## Child Concepts

- [[force_transmission]]
- [[energy_transfer]]

## Category

Golf
