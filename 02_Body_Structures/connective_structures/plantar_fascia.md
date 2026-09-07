---
id: plantar_fascia
type: Connective Structure
subtype: Aponeurosis
preferred_name: Plantar Fascia
aliases: [plantar aponeurosis]
short_definition: "A plantar foot connective tissue structure involved in arch support, toe loading, and force transmission from the foot into posterior and deep lines."
relationships:
  connects_to: [toe_loading, ankle_joint, flexor_hallucis_longus, flexor_digitorum_brevis, gastrocnemius, soleus, superficial_back_line, deep_front_line]
  attaches_to: [calcaneus, forefoot]
  part_of: [superficial_back_line, deep_front_line]
  transmits_force_between: [forefoot, calcaneus, posterior_chain]
  stabilizes: [toe_loading, golf_swing_transition]
  limits: [toe_gripping, loss_of_hip_internal_rotation]
  compensates_for: []
  active_during: [golf_swing_transition]
  assessed_by: [planned_big_toe_pressure_screen]
  improved_by: [planned_tripod_foot_transition_drill]
  supported_by: [anatomy_trains_myers_2009]
  relevant_to: [hip_internal_rotation, lateral_line, spiral_line]
confidence: medium
review_status: draft_graph_mvp
relationship_count: 25
hub_score: 85
centrality: 0.225
updated: 2026-06-29
fma_id: "FMA:45184"
bodyparts3d_id: "BP3D:FMA45184"
openstax_ref: "OpenStax A&P 2e §11.6"
evidence_level: 1
evidence:
  - source_id: anatomy_trains_myers_2009
    evidence_level: 1
    supports: "Identifies Plantar Fascia as a primary structural force transmission node."
  - source_id: openstax_anatomy_physiology_2e
    evidence_level: 1
    supports: "Defines anatomical structure and boundaries of Plantar Fascia."
  - source_id: stecco_fascial_system_2015
    evidence_level: 2
    supports: "Documents histological and macroscopic fascial continuum of Plantar Fascia."
---

# Plantar Fascia

## Relationships

- connects_to -> [[toe_loading]]
- connects_to -> [[ankle_joint]]
- connects_to -> [[flexor_hallucis_longus]]
- connects_to -> [[flexor_digitorum_brevis]]
- connects_to -> [[gastrocnemius]], [[soleus]]
- part_of -> [[superficial_back_line]]
- part_of -> [[deep_front_line]]
- stabilizes -> [[golf_swing_transition]]
- relevant_to -> [[hip_internal_rotation]]

## Movement Reasoning Role

Use this node when the graph needs to reason from ground contact into whole-body force transmission. It should connect foot pressure to fascial-line behavior rather than treating the foot as a local joint problem only.

## Golf Relevance

During transition, poor foot pressure can affect [[toe_loading]], lead [[hip_internal_rotation]], pelvic control, and upstream compensation.

## Evidence Notes

The Myers PDF extract directly references connection from plantar fascia around the heel to the Achilles tendon in the Superficial Back Line chapter context.

## Open Questions

- Decide whether `plantar_aponeurosis` should be an alias only or a separate anatomical node.
