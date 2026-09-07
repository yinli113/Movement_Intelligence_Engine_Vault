---
id: sacrotuberous_ligament
type: Connective Structure
subtype: Ligament
preferred_name: Sacrotuberous Ligament
aliases: [STL]
short_definition: "A posterior pelvic ligament connecting the sacrum region to the ischial tuberosity and relevant to posterior pelvic force transmission."
relationships:
  connects_to: [sacrum, hip_joint, biceps_femoris_long_head, superficial_back_line, spiral_line]
  attaches_to: [sacrum, ischial_tuberosity]
  part_of: [superficial_back_line, spiral_line]
  transmits_force_between: [pelvis, posterior_thigh]
  stabilizes: [golf_swing_transition, hip_internal_rotation]
  limits: [pelvic_sway]
  compensates_for: []
  active_during: [golf_swing_transition]
  assessed_by: [planned_posterior_pelvic_load_screen]
  improved_by: [planned_posterior_chain_loading_drill]
  supported_by: [anatomy_trains_myers_2009]
  relevant_to: [toe_loading, hip_internal_rotation, functional_lines]
confidence: low
review_status: draft_graph_mvp
relationship_count: 14
hub_score: 38
centrality: 0.126
updated: 2026-06-29
fma_id: "FMA:21486"
bodyparts3d_id: "BP3D:FMA21486"
openstax_ref: "OpenStax A&P 2e §11.6"
evidence_level: 1
evidence:
  - source_id: anatomy_trains_myers_2009
    evidence_level: 1
    supports: "Identifies Sacrotuberous Ligament as a primary structural force transmission node."
  - source_id: openstax_anatomy_physiology_2e
    evidence_level: 1
    supports: "Defines anatomical structure and boundaries of Sacrotuberous Ligament."
  - source_id: stecco_fascial_system_2015
    evidence_level: 2
    supports: "Documents histological and macroscopic fascial continuum of Sacrotuberous Ligament."
---

# Sacrotuberous Ligament

## Relationships

- connects_to -> [[sacrum]]
- connects_to -> [[hip_joint]]
- connects_to -> [[biceps_femoris_long_head]]
- part_of -> [[superficial_back_line]]
- part_of -> [[spiral_line]]
- transmits_force_between -> pelvis and posterior thigh
- stabilizes -> [[golf_swing_transition]]
- relevant_to -> [[hip_internal_rotation]]

## Movement Reasoning Role

Use this node when posterior pelvic load, hamstring tension, sacral position, or lead-side hip rotation may be part of the same force-transmission pattern.

## Golf Relevance

In the MVP graph, this is a potential hub between [[toe_loading]], posterior-chain loading, pelvic control, and [[hip_internal_rotation]] during transition.

## Evidence Notes

Myers references the sacrotuberous ligament in line diagrams and posterior/spiral continuity discussions. This node is marked low confidence until the exact book locator is reviewed directly.

## Open Questions

- Confirm exact Anatomy Trains page/table locator.
- Create `posterior_pelvic_load_screen` if this structure remains a high-priority hub.
