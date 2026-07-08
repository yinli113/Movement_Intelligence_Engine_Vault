---
id: toe_loading
type: Movement Pattern
preferred_name: Toe Loading
aliases: [big toe loading, forefoot pressure, hallux loading]
short_definition: "A movement pattern describing the ability to accept pressure through the forefoot and great toe without excessive gripping or collapse."
relationships:
  contains: []
  connects_to: [ankle_joint, knee_joint, hip_joint, flexor_hallucis_longus, flexor_digitorum_longus, flexor_digitorum_brevis, tibialis_posterior, peroneus_longus, gastrocnemius, soleus]
  produces: [lead_side_ground_contact]
  assists: [hip_internal_rotation]
  stabilizes: [golf_swing_transition]
  limits: []
  compensates_for: []
  active_during: [golf_swing_transition]
  assessed_by: [planned_big_toe_pressure_screen]
  improved_by: [planned_tripod_foot_transition_drill]
  supported_by: [statpearls_flexor_hallucis_longus, statpearls_foot_muscles, anatomy_trains_myers_2009]
  relevant_to: [deep_front_line, lateral_line, spiral_line, superficial_back_line]
golf_relevance: "A root MVP node for reasoning from ground contact into lead hip rotation and transition sequencing."
evidence:
  - source_id: statpearls_flexor_hallucis_longus
    source_type: online_reference
    locator: "NCBI Bookshelf, Flexor Hallucis Longus Muscle"
    supports: "FHL flexes the great toe and assists plantarflexion/inversion, supporting basic anatomy for hallux loading."
  - source_id: statpearls_foot_muscles
    source_type: online_reference
    locator: "NCBI Bookshelf, Foot Muscles"
    supports: "Deep posterior leg and plantar muscles contribute to toe flexion and foot support."
  - source_id: anatomy_trains_myers_2009
    source_type: textbook_pdf
    locator: "Lateral Line and Deep Front Line chapters"
    supports: "Myers model connects foot structures into fascial-line tracks relevant to ground contact."
confidence: medium
review_status: draft_graph_mvp
relationship_count: 29
hub_score: 88
centrality: 0.58
updated: 2026-06-29
---

# Toe Loading

## Relationships

- connects_to -> [[ankle_joint]]
- connects_to -> [[knee_joint]]
- connects_to -> [[hip_joint]]
- connects_to -> [[flexor_hallucis_longus]]
- connects_to -> [[flexor_digitorum_longus]]
- connects_to -> [[flexor_digitorum_brevis]]
- connects_to -> [[tibialis_posterior]]
- connects_to -> [[peroneus_longus]]
- assists -> [[hip_internal_rotation]]
- active_during -> [[golf_swing_transition]]
- relevant_to -> [[deep_front_line]], [[lateral_line]], [[spiral_line]], [[superficial_back_line]]

## Golf Reasoning

Use this node first when transition faults look like lead-side instability. If toe loading fails, the graph should test whether limited [[hip_internal_rotation]], pelvic sway, [[neck_tension]], or [[jaw_clenching]] are downstream compensations.

## Evidence Notes

Standard anatomy supports the muscle actions. The golf transfer relationship is plausible but should be validated with pressure/observation assessments.

## Open Questions

- Create `big_toe_pressure_screen` as an Assessment node.
- Create `tripod_foot_transition_drill` as an Exercise node.
