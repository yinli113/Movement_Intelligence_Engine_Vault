---
id: lateral_line
type: Fascial Line
preferred_name: Lateral Line
aliases: [LL, lateral fascial line]
short_definition: "An Anatomy Trains fascial line model describing a lateral body pathway from the foot through the lateral leg, pelvis, ribs, and neck."
relationships:
  contains: [peroneus_longus, peroneus_brevis, iliotibial_tract, tensor_fasciae_latae, gluteus_maximus, gluteus_medius, external_oblique, internal_oblique, intercostals, splenius_capitis, sternocleidomastoid]
  connects_to: [ankle_joint, knee_joint, hip_joint, lumbar_spine, thoracic_spine, cervical_spine, iliotibial_tract]
  stabilizes: [toe_loading, hip_internal_rotation, thoracic_rotation]
  limits: [pelvic_sway, lumbar_twist]
  compensates_for: []
  active_during: [golf_swing_transition]
  assessed_by: [planned_lateral_shift_rotation_screen]
  improved_by: [planned_lateral_line_balance_drill]
  supported_by: [anatomy_trains_myers_2009, julie_hammond_breakout]
  relevant_to: [toe_loading, neck_tension, golf_swing_transition]
golf_relevance: "Useful for reasoning about side-to-side balance, lateral shift, rotational braking, and neck involvement when transition becomes sway."
evidence:
  - source_id: anatomy_trains_myers_2009
    source_type: textbook_pdf
    locator: "Chapter 5, Lateral Line; extracted local PDF pages 130-132"
    supports: "Myers describes lateral-line continuity through peroneals/fibularii, lateral knee tissues, iliotibial tract, lateral abdominal obliques, intercostals, scalenes, SCM, and splenii."
  - source_id: julie_hammond_breakout
    source_type: source_summary
    locator: "Key Lines Explored; Lateral Line"
    supports: "Summary describes LL as balancing front/back and left/right and acting as a rotational brake."
confidence: medium
review_status: draft_graph_mvp
relationship_count: 37
hub_score: 108
centrality: 0.755
updated: 2026-06-29
---

# Lateral Line

## Relationships

- contains -> [[peroneus_longus]]
- contains -> [[peroneus_brevis]]
- contains -> [[iliotibial_tract]]
- contains -> [[tensor_fasciae_latae]]
- contains -> [[gluteus_maximus]]
- contains -> [[gluteus_medius]]
- contains -> [[external_oblique]], [[internal_oblique]], [[intercostals]]
- contains -> [[splenius_capitis]], [[sternocleidomastoid]]
- stabilizes -> [[toe_loading]]
- stabilizes -> [[hip_internal_rotation]]
- limits -> pelvic sway during [[golf_swing_transition]]
- connects_to -> [[deep_front_line]] through lateral deep structures discussed by Myers
- supported_by -> `raw/literature/Anatomy_Trains_Myofascial_Thomas_W_Myers.pdf`

## Golf Reasoning

Use this node when a transition fault looks like sway, side bend, or lateral balance loss rather than pure rotation loss. The Lateral Line helps decide whether a foot/hip issue is creating upper-body compensation.

## Evidence Notes

This note uses Myers for fascial-line modeling and should not be treated as a claim that all lateral pain or asymmetry comes from this line.

## Open Questions

- Create `pelvic_sway` as a Limitation Pattern node.
- Create a lateral shift and rib-pelvis rotation assessment node.
