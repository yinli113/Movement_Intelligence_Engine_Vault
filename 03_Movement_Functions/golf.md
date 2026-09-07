---
id: golf
type: Golf
preferred_name: Golf
aliases: [golf performance, golf movement]
short_definition: "Sport context for applying the movement intelligence graph to swing analysis, performance, and rehabilitation reasoning."
relationships:
  contains: [golf_swing]
  connects_to: [movement_sequencing, force_transmission, energy_transfer]
  produces: []
  assists: []
  stabilizes: []
  limits: []
  compensates_for: []
  active_during: []
  assessed_by: []
  improved_by: []
  supported_by: [golf_decoded_six_phases_swing]
  relevant_to: [golf_swing_transition]
confidence: medium
review_status: draft_graph_mvp
relationship_count: 6
hub_score: 12
centrality: 0.054
updated: 2026-06-30
---

# Golf

## Definition

Golf is the sport context for applying the movement intelligence graph to swing analysis, performance, and rehabilitation reasoning.

## Why It Matters

It gives the graph a domain boundary so anatomy and biomechanics can be interpreted relative to golf-specific movement phases and performance goals.

## Supporting Evidence From Source

The [[golf_decoded_six_phases_swing]] source introduces a golf-specific phase model.

## Related Concepts

- [[golf_swing]]
- [[movement_sequencing]]
- [[force_transmission]]
- [[energy_transfer]]

## Parent Concepts

- Sports Performance

## Child Concepts

- [[golf_swing]]
- [[golf_swing_transition]]

## Category

Golf

## Evidence Grounding
```yaml
evidence:
  - source_id: dr_kwon_golfer_ground_interaction
    level: domain_biomechanics
    evidence_tier: Level 3
    description: "Ground reaction force vectors and rotational momentum generation in golf swings."
  - source_id: anatomy_trains_myers_2009
    level: foundational_anatomical_framework
    evidence_tier: Level 2
    description: "Diagonal functional lines and spiral line loading across swing phases."
```
