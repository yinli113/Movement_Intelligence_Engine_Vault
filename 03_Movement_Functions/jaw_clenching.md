---
id: jaw_clenching
type: Compensation
preferred_name: Jaw Clenching
aliases: [jaw tension, bracing jaw, bruxing]
short_definition: "A possible bracing behavior where jaw-closing muscles increase tone during movement effort or stabilization demand."
relationships:
  contains: []
  connects_to: [masseter, temporalis, cervical_spine]
  produces: [neck_tension]
  assists: []
  stabilizes: []
  limits: [breathing_mechanics, thoracic_rotation]
  compensates_for: [neck_tension, poor_toe_loading, limited_thoracic_rotation]
  active_during: [golf_swing_transition]
  assessed_by: [planned_jaw_breath_observation]
  improved_by: [planned_exhale_transition_drill]
  supported_by: [anatomy_trains_myers_2009, julie_hammond_breakout]
  relevant_to: [deep_front_line, superficial_back_line, spiral_line]
golf_relevance: "Useful as a visible compensation signal during transition, especially when trunk rotation, foot loading, or shoulder loading is being braced rather than coordinated."
evidence:
  - source_id: anatomy_trains_myers_2009
    source_type: textbook_pdf
    locator: "Chapter 9, Deep Front Line; jaw-region structures noted in local vault source summary"
    supports: "Masseter and temporalis are represented in the existing DFL graph and Julie source summary."
  - source_id: standard_anatomy_reference
    source_type: online_reference
    locator: "Standard muscle anatomy for masseter and temporalis actions should be added as an Evidence Source node."
    supports: "Basic jaw-closing anatomy only; not a claim that jaw clenching diagnoses a swing fault."
confidence: low
review_status: draft_graph_mvp
relationship_count: 17
hub_score: 50
centrality: 0.293
updated: 2026-06-29
---

# Jaw Clenching

## Relationships

- connects_to -> [[masseter]]
- connects_to -> [[temporalis]]
- connects_to -> [[cervical_spine]]
- compensates_for -> [[neck_tension]]
- possible_constraint -> [[thoracic_rotation]]
- possible_constraint -> [[toe_loading]]
- active_during -> [[golf_swing_transition]]
- relevant_to -> [[deep_front_line]]
- relevant_to -> [[superficial_back_line]]

## Golf Reasoning

Use jaw clenching as an observation node, not a diagnosis. If it appears during [[golf_swing_transition]], trace backward through [[neck_tension]], [[thoracic_rotation]], [[hip_internal_rotation]], and [[toe_loading]].

## Evidence Notes

The fascial-line relationship is low-confidence until the Myers PDF is converted into structured evidence. The compensation relationship is a reasoning hypothesis.

## Open Questions

- Create `jaw_breath_observation` as an Assessment node.
- Create `exhale_transition_drill` as an Exercise node only after assessment logic is defined.
