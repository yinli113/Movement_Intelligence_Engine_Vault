---
id: address_to_shaft_parallel
type: Golf Phase
preferred_name: Address to Shaft Parallel
aliases: [phase 1, early takeaway, address to shaft parallel]
short_definition: "First source-defined golf swing phase interval from Address to Shaft Parallel."
relationships:
  contains: [address_position, shaft_parallel_position, toe_loading]
  connects_to: [golf_swing, shaft_parallel_to_end_pelvis_rotation, movement_sequencing]
  produces: [early_backswing_sequence]
  assists: [force_transmission]
  stabilizes: [toe_loading]
  limits: []
  compensates_for: []
  active_during: [golf_swing]
  assessed_by: [planned_address_setup_screen, planned_early_backswing_sequence_screen]
  improved_by: [planned_tripod_foot_transition_drill]
  supported_by: [golf_decoded_six_phases_swing]
  relevant_to: [ground_reaction_force, plantar_fascia]
confidence: medium
review_status: draft_graph_mvp
relationship_count: 10
hub_score: 20
centrality: 0.2
updated: 2026-06-30
---

# Address to Shaft Parallel

## Definition

Address to Shaft Parallel is the first phase interval in the source model.

## Why It Matters

This interval establishes starting conditions for pressure, posture, and early sequencing.

## Supporting Evidence From Source

The [[golf_decoded_six_phases_swing]] screenshot labels the first interval as Address -> Shaft Parallel.

## Related Concepts

| Relationship | Target |
|---|---|
| starts_at | [[address_position]] |
| ends_at | [[shaft_parallel_position]] |
| precedes | [[shaft_parallel_to_end_pelvis_rotation]] |
| relevant_to | [[toe_loading]], [[plantar_fascia]], [[ground_reaction_force]] |

## Parent Concepts

- [[golf_swing]]
- [[movement_sequencing]]

## Child Concepts

- [[address_position]]
- [[shaft_parallel_position]]
- [[toe_loading]]

## Category

Movement Phase
