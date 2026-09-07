---
id: address_position
type: Movement Pattern
preferred_name: Address Position
aliases: [address, setup position, golf address]
short_definition: "Initial golf setup position before the club begins moving into the backswing."
relationships:
  contains: []
  connects_to: [address_to_shaft_parallel, golf_swing, toe_loading]
  produces: [initial_conditions]
  assists: [movement_sequencing]
  stabilizes: [toe_loading]
  limits: []
  compensates_for: []
  active_during: [address_to_shaft_parallel]
  assessed_by: [planned_address_setup_screen]
  improved_by: []
  supported_by: [golf_decoded_six_phases_swing]
  relevant_to: [force_transmission]
confidence: medium
review_status: draft_graph_mvp
relationship_count: 6
hub_score: 13
centrality: 0.054
updated: 2026-06-30
---

# Address Position

## Definition

Address Position is the initial setup state before the club moves into the backswing.

## Why It Matters

It defines the starting constraints for balance, [[toe_loading]], posture, and future force transmission.

## Supporting Evidence From Source

The [[golf_decoded_six_phases_swing]] screenshot uses Address as the first boundary of the first phase: [[address_to_shaft_parallel]].

## Related Concepts

| Relationship | Target |
|---|---|
| starts | [[address_to_shaft_parallel]] |
| connects_to | [[toe_loading]] |
| parent | [[golf_swing]] |

## Parent Concepts

- [[golf_swing]]

## Child Concepts

- [[toe_loading]]

## Category

Golf
