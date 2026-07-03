---
id: impact_to_hands_chest_height
type: Golf Phase
preferred_name: Impact to Hands Chest Height
aliases: [phase 6, early follow-through, post-impact to hands chest height]
short_definition: "Sixth source-defined golf swing phase interval from Impact to Hands Chest Height."
relationships:
  contains: [impact_position, hands_chest_height_position, force_transmission, energy_transfer]
  connects_to: [max_unweighting_to_impact, golf_swing]
  produces: [early_follow_through_checkpoint]
  assists: [movement_sequencing]
  stabilizes: []
  limits: []
  compensates_for: []
  active_during: [golf_swing]
  assessed_by: [planned_post_impact_deceleration_screen]
  improved_by: []
  supported_by: [golf_decoded_six_phases_swing]
  relevant_to: [functional_line, spiral_line, superficial_back_line]
confidence: medium
review_status: draft_graph_mvp
relationship_count: 11
hub_score: 30
centrality: 0.224
updated: 2026-06-30
---

# Impact to Hands Chest Height

## Definition

Impact to Hands Chest Height is the source-defined post-impact interval ending when the hands reach chest height.

## Why It Matters

It gives the graph an early deceleration and follow-through checkpoint that can reflect quality of prior force transmission.

## Supporting Evidence From Source

The [[golf_decoded_six_phases_swing]] screenshot labels the sixth interval as Impact -> Hands Chest Height.

## Related Concepts

| Relationship | Target |
|---|---|
| starts_at | [[impact_position]] |
| ends_at | [[hands_chest_height_position]] |
| follows | [[max_unweighting_to_impact]] |
| related_to | [[force_transmission]], [[energy_transfer]] |

## Parent Concepts

- [[golf_swing]]
- [[movement_sequencing]]

## Child Concepts

- [[impact_position]]
- [[hands_chest_height_position]]
- [[force_transmission]]
- [[energy_transfer]]

## Category

Movement Phase
