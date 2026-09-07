---
id: shaft_parallel_position
type: Movement Pattern
preferred_name: Shaft Parallel Position
aliases: [shaft parallel, club shaft parallel]
short_definition: "Golf swing boundary event where the club shaft reaches a parallel orientation during early backswing."
relationships:
  contains: []
  connects_to: [address_to_shaft_parallel, shaft_parallel_to_end_pelvis_rotation, golf_swing]
  produces: [early_backswing_checkpoint]
  assists: [movement_sequencing]
  stabilizes: []
  limits: []
  compensates_for: []
  active_during: [address_to_shaft_parallel, shaft_parallel_to_end_pelvis_rotation]
  assessed_by: [planned_early_backswing_sequence_screen]
  improved_by: []
  supported_by: [golf_decoded_six_phases_swing]
  relevant_to: [force_transmission]
confidence: medium
review_status: draft_graph_mvp
relationship_count: 6
hub_score: 18
centrality: 0.054
updated: 2026-06-30
---

# Shaft Parallel Position

## Definition

Shaft Parallel Position is a swing boundary event used by the source to divide early backswing from the next pelvis-rotation interval.

## Why It Matters

It gives the graph a timing marker for early sequencing before pelvis rotation reaches its endpoint.

## Supporting Evidence From Source

The [[golf_decoded_six_phases_swing]] screenshot labels Shaft Parallel as the end of [[address_to_shaft_parallel]] and the start of [[shaft_parallel_to_end_pelvis_rotation]].

## Related Concepts

| Relationship | Target |
|---|---|
| ends | [[address_to_shaft_parallel]] |
| starts | [[shaft_parallel_to_end_pelvis_rotation]] |
| parent | [[golf_swing]] |

## Parent Concepts

- [[golf_swing]]

## Child Concepts

- [[movement_sequencing]]

## Category

Golf
