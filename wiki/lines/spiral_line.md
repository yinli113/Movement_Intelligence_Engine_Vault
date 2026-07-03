---
id: spiral_line
type: Fascial Line
preferred_name: Spiral Line
aliases: [SPL, spiral fascial line, rotational fascial line]
short_definition: "An Anatomy Trains fascial line model describing diagonal and rotational continuities through the foot, leg, trunk, scapula, and neck."
relationships:
  contains: [splenius_capitis, nuchal_ligament, rhomboids, serratus_anterior, external_oblique, internal_oblique, tensor_fasciae_latae, iliotibial_tract, tibialis_anterior, peroneus_longus, biceps_femoris_long_head, sacrotuberous_ligament, spinalis, longissimus, iliocostalis]
  connects_to: [ankle_joint, knee_joint, hip_joint, lumbar_spine, thoracic_spine, cervical_spine, shoulder_joint, nuchal_ligament, iliotibial_tract, sacrotuberous_ligament]
  assists: [thoracic_rotation, trail_shoulder_external_rotation, hip_internal_rotation]
  stabilizes: [toe_loading, golf_swing_transition]
  limits: [lumbar_twist, pelvic_sway]
  compensates_for: []
  active_during: [golf_swing_transition]
  assessed_by: [planned_rotational_chain_screen]
  improved_by: [planned_spiral_line_rotation_drill]
  supported_by: [anatomy_trains_myers_2009]
  relevant_to: [neck_tension, jaw_clenching, toe_loading]
golf_relevance: "Primary sample node for reasoning about distributed rotation from foot pressure to trunk rotation and trail shoulder loading."
evidence:
  - source_id: anatomy_trains_myers_2009
    source_type: textbook_pdf
    locator: "Chapter 6, Spiral Line; extracted local PDF pages 147 and 150"
    supports: "Myers describes rhomboid-serratus scapular sling continuity and links TFL/IT tract toward tibialis anterior within the Spiral Line model."
confidence: medium
review_status: draft_graph_mvp
relationship_count: 49
hub_score: 144
centrality: 1.0
updated: 2026-06-29
---

# Spiral Line

## Relationships

- contains -> [[splenius_capitis]]
- contains -> [[nuchal_ligament]]
- contains -> [[rhomboids]]
- contains -> [[serratus_anterior]]
- contains -> [[external_oblique]], [[internal_oblique]]
- contains -> [[tensor_fasciae_latae]]
- contains -> [[iliotibial_tract]]
- contains -> [[tibialis_anterior]]
- contains -> [[peroneus_longus]]
- contains -> [[biceps_femoris_long_head]]
- contains -> [[sacrotuberous_ligament]]
- assists -> [[thoracic_rotation]]
- assists -> [[trail_shoulder_external_rotation]]
- stabilizes -> [[toe_loading]]
- active_during -> [[golf_swing_transition]]
- relevant_to -> [[neck_tension]], [[jaw_clenching]]
- supported_by -> `raw/literature/Anatomy_Trains_Myofascial_Thomas_W_Myers.pdf`

## Golf Reasoning

Use this node when rotation is blocked but the symptom appears somewhere else. Example traversal: [[toe_loading]] -> [[hip_internal_rotation]] -> [[thoracic_rotation]] -> [[trail_shoulder_external_rotation]] -> [[neck_tension]].

## Evidence Notes

Myers supports the fascial-line continuities. The golf sequence is a product graph hypothesis that needs assessment nodes for validation.

## Open Questions

- Create `rotational_chain_screen` as an Assessment node.
- Decide whether `lumbar_twist` and `pelvic_sway` should become Limitation Pattern or Compensation nodes.
