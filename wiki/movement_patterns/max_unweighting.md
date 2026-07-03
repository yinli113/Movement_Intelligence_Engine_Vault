---
id: max_unweighting
type: Movement Pattern
preferred_name: Max Unweighting
aliases: [maximum unweighting, max vertical unweighting]
short_definition: "Golf swing boundary event in the source model marking the end of the transition interval and start of the impact-directed interval."
relationships:
  contains: [toe_loading, force_transmission]
  connects_to: [golf_swing_transition, max_unweighting_to_impact, ground_reaction_force, energy_transfer]
  produces: [downswing_force_redirection]
  assists: [force_transmission]
  stabilizes: [golf_swing_transition]
  limits: []
  compensates_for: []
  active_during: [golf_swing_transition, max_unweighting_to_impact]
  assessed_by: [planned_unweighting_timing_screen]
  improved_by: [planned_transition_sequence_drill]
  supported_by: [golf_decoded_six_phases_swing]
  relevant_to: [plantar_fascia, deep_front_line, functional_line]
confidence: low
review_status: draft_graph_mvp
relationship_count: 12
hub_score: 32
centrality: 0.245
updated: 2026-06-30
---

# Max Unweighting

## Definition

Max Unweighting is the source-defined boundary event after Top Backswing and before Impact.

## Why It Matters

It gives the graph a place to reason about external force interaction, pressure shift, and transition from stored energy toward impact. The exact biomechanics need additional source support beyond the screenshot.

## Supporting Evidence From Source

The [[golf_decoded_six_phases_swing]] screenshot labels Max Unweighting as the end of [[golf_swing_transition]] and the start of [[max_unweighting_to_impact]].

## Related Concepts

| Relationship | Target |
|---|---|
| ends | [[golf_swing_transition]] |
| starts | [[max_unweighting_to_impact]] |
| related_to | [[force_transmission]] |
| related_to | [[energy_transfer]] |
| possible_related_to | [[toe_loading]], [[plantar_fascia]] |

## Parent Concepts

- [[golf_swing]]
- [[movement_sequencing]]

## Child Concepts

- [[force_transmission]]
- [[energy_transfer]]

## Category

Golf
