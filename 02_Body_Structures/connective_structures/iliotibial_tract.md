---
id: iliotibial_tract
type: Connective Structure
subtype: Fascia
preferred_name: Iliotibial Tract
aliases: [iliotibial band, IT band, ITB, ITT]
short_definition: "A lateral thigh fascial structure involved in force transmission between hip, lateral thigh, knee, and lateral fascial-line behavior."
relationships:
  connects_to: [tensor_fasciae_latae, gluteus_maximus, gluteus_medius, knee_joint, hip_joint, lateral_line, spiral_line]
  attaches_to: [pelvis, lateral_tibia]
  part_of: [lateral_line, spiral_line]
  transmits_force_between: [hip_joint, knee_joint, lateral_leg]
  stabilizes: [hip_internal_rotation, golf_swing_transition]
  limits: [pelvic_sway, knee_valgus]
  compensates_for: []
  active_during: [golf_swing_transition]
  assessed_by: [planned_lateral_shift_rotation_screen]
  improved_by: [planned_lateral_line_balance_drill]
  supported_by: [anatomy_trains_myers_2009]
  relevant_to: [toe_loading, lateral_line, spiral_line]
confidence: medium
review_status: draft_graph_mvp
relationship_count: 12
hub_score: 35
centrality: 0.207
updated: 2026-06-29
---

# Iliotibial Tract

## Relationships

- connects_to -> [[tensor_fasciae_latae]]
- connects_to -> [[gluteus_maximus]]
- connects_to -> [[gluteus_medius]]
- connects_to -> [[hip_joint]]
- connects_to -> [[knee_joint]]
- part_of -> [[lateral_line]]
- part_of -> [[spiral_line]]
- stabilizes -> [[golf_swing_transition]]
- relevant_to -> [[hip_internal_rotation]]

## Movement Reasoning Role

Use this node when lateral hip, thigh, knee, and foot-pressure behavior need to be reasoned together. It helps the graph move beyond isolated TFL or glute notes.

## Golf Relevance

In transition, the Iliotibial Tract can help connect lateral line control, pelvic sway, knee position, and lead hip rotation.

## Evidence Notes

The Myers PDF extract directly references the Iliotibial Tract in Lateral Line material and describes its continuity with peroneals/fibularii, lateral knee tissues, abductors, and lateral abdominal obliques.

## Open Questions

- Create `knee_valgus` or normalize existing knee-valgus draft language into a Limitation Pattern node.
