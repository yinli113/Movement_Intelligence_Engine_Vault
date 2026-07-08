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
  supported_by: [golf_decoded_six_phases_swing]
  relevant_to: [functional_lines, spiral_line]
confidence: medium
review_status: draft_graph_mvp
relationship_count: 8
hub_score: 27
centrality: 0.16
updated: 2026-06-30
---

# Impact Position

## Definition

Impact Position is the boundary event where club and ball contact occurs.

## Why It Matters

It is the output checkpoint for force transmission and energy transfer through the preceding phases.

## Supporting Evidence From Source

The [[golf_decoded_six_phases_swing]] screenshot labels Impact as the end of [[max_unweighting_to_impact]] and the start of [[impact_to_hands_chest_height]].

## Related Concepts

| Relationship | Target |
|---|---|
| ends | [[max_unweighting_to_impact]] |
| starts | [[impact_to_hands_chest_height]] |
| produces | ball flight |
| related_to | [[force_transmission]], [[energy_transfer]] |

## Parent Concepts

- [[golf_swing]]

## Child Concepts

- [[force_transmission]]
- [[energy_transfer]]

## Category

Golf
