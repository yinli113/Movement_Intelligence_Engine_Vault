---
id: neck_tension
type: Compensation
preferred_name: Neck Tension
aliases: [cervical bracing, upper neck tension, head-neck bracing]
short_definition: "A possible compensation pattern where cervical and shoulder-girdle muscles increase tone during rotation or force-transfer demand."
relationships:
  contains: []
  connects_to: [cervical_spine, thoracic_spine, sternocleidomastoid, scalenes, splenius_capitis, trapezius, longus_colli]
  produces: [jaw_clenching, shoulder_elevation]
  assists: []
  stabilizes: []
  limits: [thoracic_rotation, trail_shoulder_external_rotation]
  compensates_for: [limited_thoracic_rotation, poor_toe_loading, poor_cross_body_force_transfer]
  active_during: [golf_swing_transition]
  assessed_by: [planned_head_neck_rotation_observation]
  improved_by: [planned_thoracic_rotation_breath_drill]
  supported_by: [statpearls_sternocleidomastoid, statpearls_scalenus, anatomy_trains_myers_2009]
  relevant_to: [jaw_clenching, trail_shoulder_external_rotation, spiral_line, deep_front_line]
golf_relevance: "Useful for reasoning when trail shoulder loading or trunk rotation is replaced by head-neck bracing during transition."
evidence:
  - source_id: statpearls_sternocleidomastoid
    source_type: online_reference
    locator: "NCBI Bookshelf, Anatomy Head and Neck: Sternocleidomastoid Muscle"
    supports: "SCM contributes to cervical rotation, flexion/extension behavior, and inspiration."
  - source_id: statpearls_scalenus
    source_type: online_reference
    locator: "NCBI Bookshelf, Anatomy Head and Neck, Scalenus Muscle"
    supports: "Scalenes connect cervical vertebrae to upper ribs and can assist cervical motion and rib elevation."
  - source_id: anatomy_trains_myers_2009
    source_type: textbook_pdf
    locator: "Lateral Line and Deep Front Line chapters"
    supports: "Myers model includes cervical/neck structures in fascial-line continuity."
confidence: medium
review_status: draft_graph_mvp
relationship_count: 21
hub_score: 70
centrality: 0.429
updated: 2026-06-29
---

# Neck Tension

## Relationships

- connects_to -> [[cervical_spine]]
- connects_to -> [[thoracic_spine]]
- connects_to -> [[sternocleidomastoid]]
- connects_to -> [[scalenes]]
- connects_to -> [[splenius_capitis]]
- connects_to -> [[trapezius]]
- produces -> [[jaw_clenching]]
- limits -> [[thoracic_rotation]]
- limits -> [[trail_shoulder_external_rotation]]
- active_during -> [[golf_swing_transition]]
- relevant_to -> [[spiral_line]], [[deep_front_line]], [[superficial_back_line]]

## Golf Reasoning

Use this node when a golfer holds the head still by bracing. Follow the graph toward [[thoracic_rotation]], [[trail_shoulder_external_rotation]], [[toe_loading]], and [[functional_line]] before treating the neck as an isolated issue.

## Evidence Notes

Standard anatomy references support the muscle and joint definitions. The swing-compensation relationships are MVP reasoning hypotheses.

## Open Questions

- Create `head_neck_rotation_observation` as an Assessment node.
- Create `thoracic_rotation_breath_drill` as an Exercise node.
