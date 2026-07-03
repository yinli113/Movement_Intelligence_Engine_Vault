---
id: deep_front_line
type: Fascial Line
preferred_name: Deep Front Line
aliases: [DFL, deep anterior line, deep front fascial line]
short_definition: "An Anatomy Trains fascial line model describing a deep anterior support pathway through the foot, inner leg, pelvis, diaphragm, neck, and jaw region."
relationships:
  contains: [plantar_fascia, tibialis_posterior, flexor_hallucis_longus, flexor_digitorum_longus, popliteus, adductor_longus, adductor_brevis, adductor_magnus, pectineus, gracilis, psoas_major, iliacus, diaphragm, quadratus_lumborum, transversus_abdominis, longus_colli, longus_capitis, scalenes, masseter, temporalis]
  connects_to: [ankle_joint, knee_joint, hip_joint, lumbar_spine, thoracic_spine, cervical_spine, plantar_fascia]
  stabilizes: [toe_loading, hip_internal_rotation, thoracic_rotation, neck_tension]
  limits: []
  compensates_for: []
  active_during: [golf_swing_transition]
  assessed_by: [planned_breath_and_inner_arch_screen]
  improved_by: [planned_breath_foot_integration_drill]
  supported_by: [anatomy_trains_myers_2009, julie_hammond_breakout]
  relevant_to: [golf_swing_transition, jaw_clenching, neck_tension, toe_loading]
golf_relevance: "Useful for reasoning about inner-foot support, pelvic organization, breathing mechanics, and neck/jaw bracing during golf transition."
evidence:
  - source_id: anatomy_trains_myers_2009
    source_type: textbook_pdf
    locator: "Chapter 9, Deep Front Line; local PDF pages around chapter start and extracted page 209"
    supports: "Deep Front Line includes deep leg, pelvic, diaphragm, thoracic inlet, neck, and jaw-related structures in the Anatomy Trains model."
  - source_id: julie_hammond_breakout
    source_type: source_summary
    locator: "Core Anatomy Trains Concepts; Deep Front Line section"
    supports: "Summary describes DFL as lifting inner arch, supporting lumbar spine, breathing, neck, and head balance."
confidence: medium
review_status: draft_graph_mvp
relationship_count: 46
hub_score: 143
centrality: 0.939
updated: 2026-06-29
---

# Deep Front Line

## Relationships

- contains -> [[plantar_fascia]]
- contains -> [[tibialis_posterior]]
- contains -> [[flexor_hallucis_longus]]
- contains -> [[flexor_digitorum_longus]]
- contains -> [[popliteus]]
- contains -> [[adductor_longus]], [[adductor_brevis]], [[adductor_magnus]], [[pectineus]], [[gracilis]]
- contains -> [[psoas_major]], [[iliacus]], [[diaphragm]], [[quadratus_lumborum]], [[transversus_abdominis]]
- contains -> [[longus_colli]], [[longus_capitis]], [[scalenes]], [[masseter]], [[temporalis]]
- stabilizes -> [[toe_loading]]
- stabilizes -> [[hip_internal_rotation]]
- influences -> [[neck_tension]]
- possible_constraint -> [[jaw_clenching]]
- active_during -> [[golf_swing_transition]]
- supported_by -> `raw/literature/Anatomy_Trains_Myofascial_Thomas_W_Myers.pdf`
- supported_by -> [[julie_hammond_breakout]]

## Golf Reasoning

Use this node when a golf transition problem involves inner-foot collapse, breath holding, pelvic instability, neck bracing, or jaw clenching. Treat the DFL as a fascial-line model from Anatomy Trains, not as a medical diagnosis.

## Evidence Notes

Myers is the primary fascial-line reference. The Julie Hammond note is a secondary summary and should not be treated as final truth.

## Open Questions

- Create a dedicated Evidence Source node for the Myers PDF.
- Create Assessment and Exercise nodes for breath, inner arch support, and jaw/neck quieting.
