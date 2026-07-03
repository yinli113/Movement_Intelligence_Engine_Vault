---
id: superficial_back_line
type: Fascial Line
preferred_name: Superficial Back Line
aliases: [SBL, posterior chain, superficial posterior fascial line]
short_definition: "An Anatomy Trains fascial line model describing posterior continuity from the plantar foot through the calves, hamstrings, spinal extensors, and scalp region."
relationships:
  contains: [plantar_fascia, gastrocnemius, soleus, biceps_femoris_long_head, sacrotuberous_ligament, semitendinosus, semimembranosus, spinalis, longissimus, iliocostalis, nuchal_ligament, occipitofrontalis]
  connects_to: [ankle_joint, knee_joint, hip_joint, lumbar_spine, thoracic_spine, cervical_spine, plantar_fascia, sacrotuberous_ligament, nuchal_ligament]
  assists: [toe_loading, hip_internal_rotation]
  stabilizes: [golf_swing_transition]
  limits: [toe_gripping, neck_tension, jaw_clenching]
  compensates_for: []
  active_during: [golf_swing_transition]
  assessed_by: [planned_posterior_chain_load_screen]
  improved_by: [planned_posterior_chain_loading_drill]
  supported_by: [anatomy_trains_myers_2009]
  relevant_to: [toe_loading, neck_tension, jaw_clenching]
golf_relevance: "Useful for reasoning about whether address posture and transition rotation are supported by posterior-chain load or replaced by neck/jaw bracing."
evidence:
  - source_id: anatomy_trains_myers_2009
    source_type: textbook_pdf
    locator: "Chapter 3, Superficial Back Line; extracted local PDF page 104"
    supports: "Myers describes SBL movement considerations including trunk and hip flexion with knees extended and trunk hyperextension."
confidence: medium
review_status: draft_graph_mvp
relationship_count: 34
hub_score: 104
centrality: 0.694
updated: 2026-06-29
---

# Superficial Back Line

## Relationships

- contains -> [[plantar_fascia]]
- contains -> [[gastrocnemius]]
- contains -> [[soleus]]
- contains -> [[biceps_femoris_long_head]], [[semitendinosus]], [[semimembranosus]]
- contains -> [[sacrotuberous_ligament]]
- contains -> [[spinalis]], [[longissimus]], [[iliocostalis]]
- contains -> [[nuchal_ligament]]
- assists -> [[toe_loading]]
- assists -> [[hip_internal_rotation]]
- possible_constraint -> [[neck_tension]]
- possible_constraint -> [[jaw_clenching]]
- active_during -> [[golf_swing_transition]]
- supported_by -> `raw/literature/Anatomy_Trains_Myofascial_Thomas_W_Myers.pdf`

## Golf Reasoning

Use this node when foot pressure, hamstring/calf tone, spinal extension, neck tension, or jaw clenching appear together. It is a graph hypothesis for posterior tension management, not a diagnosis.

## Evidence Notes

The fascial-line membership comes from Myers. Golf relevance is inferred from movement demands and should be validated through planned assessments.

## Open Questions

- Create `posterior_chain_load_screen`.
- Create a simple Exercise node for posterior-chain loading without toe gripping.
