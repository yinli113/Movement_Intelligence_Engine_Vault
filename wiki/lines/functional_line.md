---
id: functional_line
type: Fascial Line
preferred_name: Functional Line
aliases: [FL, functional lines, back functional line, front functional line, functional sling]
short_definition: "An Anatomy Trains fascial line model describing cross-body connections between shoulder girdle, trunk, pelvis, and lower limb used in force transfer."
relationships:
  contains: [latissimus_dorsi, gluteus_maximus, rectus_abdominis, pectoralis_major, adductor_longus, thoracolumbar_fascia]
  connects_to: [shoulder_joint, thoracic_spine, lumbar_spine, sacrum, hip_joint, knee_joint, thoracolumbar_fascia]
  produces: [cross_body_force_transfer]
  assists: [trail_shoulder_external_rotation, thoracic_rotation]
  stabilizes: [golf_swing_transition]
  limits: []
  compensates_for: []
  active_during: [golf_swing_transition]
  assessed_by: [planned_cross_body_sling_screen]
  improved_by: [glute_max_activations]
  supported_by: [anatomy_trains_myers_2009]
  relevant_to: [hip_internal_rotation, thoracic_rotation, trail_shoulder_external_rotation]
golf_relevance: "Central MVP line for reasoning about how lead hip rotation and trunk rotation transfer into trail shoulder loading and club delivery."
evidence:
  - source_id: anatomy_trains_myers_2009
    source_type: textbook_pdf
    locator: "Chapter 8, Functional Lines; extracted local PDF page 185"
    supports: "Back Functional Line includes latissimus dorsi, lumbodorsal/sacral fascia, gluteus maximus, and lower-limb continuation; Front Functional Line includes pectoralis major, rectus sheath, and adductor longus."
confidence: medium
review_status: draft_graph_mvp
relationship_count: 40
hub_score: 111
centrality: 0.816
updated: 2026-06-29
---

# Functional Line

## Relationships

- contains -> [[latissimus_dorsi]]
- contains -> [[thoracolumbar_fascia]]
- contains -> [[gluteus_maximus]]
- contains -> [[rectus_abdominis]]
- contains -> [[pectoralis_major]]
- contains -> [[adductor_longus]]
- connects_to -> [[shoulder_joint]]
- connects_to -> [[hip_joint]]
- assists -> [[trail_shoulder_external_rotation]]
- assists -> [[thoracic_rotation]]
- active_during -> [[golf_swing_transition]]
- improved_by -> [[glute_max_activations]]
- supported_by -> `raw/literature/Anatomy_Trains_Myofascial_Thomas_W_Myers.pdf`

## Golf Reasoning

Use this node to test whether transition force is traveling through the body or being recreated by the arms. If [[hip_internal_rotation]] and [[thoracic_rotation]] are available but the trail arm still throws early, inspect the Functional Line relationships.

## Evidence Notes

Myers supports the fascial-line membership. Golf transfer logic is a movement-reasoning hypothesis and should be validated with assessments.

## Open Questions

- Create `cross_body_sling_screen` as an Assessment node.
- Create golf-specific sling integration Exercise nodes beyond the existing glute activation note.
