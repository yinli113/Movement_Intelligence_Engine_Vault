---
id: max_unweighting_to_impact
type: Golf Phase
preferred_name: Max Unweighting to Impact
aliases: [phase 5, downswing to impact, unweighting to impact]
short_definition: "Fifth source-defined golf swing phase interval from Max Unweighting to Impact."
relationships:
  contains: [max_unweighting, impact_position, ground_reaction_force, force_transmission, energy_transfer]
  connects_to: [golf_swing_transition, impact_to_hands_chest_height, golf_swing]
  produces: [impact_position]
  assists: [force_transmission, energy_transfer]
  stabilizes: []
  limits: []
  compensates_for: []
  active_during: [golf_swing]
  assessed_by: [planned_impact_sequence_screen]
  improved_by: [planned_transition_sequence_drill]
  supported_by: [golf_decoded_six_phases_swing]
  relevant_to: [functional_lines, spiral_line, plantar_fascia]
confidence: medium
review_status: draft_graph_mvp
relationship_count: 14
hub_score: 41
centrality: 0.28
updated: 2026-06-30
---

# Max Unweighting to Impact

## Definition

Max Unweighting to Impact is the source-defined interval from the unweighting boundary event to ball impact.

## Why It Matters

This interval is where the graph should reason about force redirection into impact, not just local muscle contraction.

## Supporting Evidence From Source

The [[golf_decoded_six_phases_swing]] screenshot labels the fifth interval as Max Unweighting -> Impact.

## Related Concepts

| Relationship | Target |
|---|---|
| starts_at | [[max_unweighting]] |
| ends_at | [[impact_position]] |
| follows | [[golf_swing_transition]] |
| precedes | [[impact_to_hands_chest_height]] |
| related_to | [[ground_reaction_force]], [[force_transmission]], [[energy_transfer]] |

## Parent Concepts

- [[golf_swing]]
- [[movement_sequencing]]

## Child Concepts

- [[max_unweighting]]
- [[impact_position]]
- [[ground_reaction_force]]
- [[force_transmission]]
- [[energy_transfer]]

## Category

Movement Phase
