---
id: thoracolumbar_fascia
type: Connective Structure
subtype: Fascia
preferred_name: Thoracolumbar Fascia
aliases: [lumbodorsal fascia, thoracolumbar aponeurosis]
short_definition: "A broad posterior trunk fascial structure involved in force transfer between spine, pelvis, latissimus dorsi, abdominal wall, and gluteal region."
relationships:
  connects_to: [latissimus_dorsi, gluteus_maximus, external_oblique, internal_oblique, lumbar_spine, sacrum, functional_lines, spiral_line]
  attaches_to: [lumbar_spine, sacrum, pelvis]
  part_of: [functional_lines, spiral_line]
  transmits_force_between: [upper_limb, trunk, pelvis]
  stabilizes: [thoracic_rotation, hip_internal_rotation, golf_swing_transition]
  limits: [lumbar_twist, pelvic_sway]
  compensates_for: []
  active_during: [golf_swing_transition]
  assessed_by: [planned_cross_body_sling_screen]
  improved_by: [glute_max_activations, planned_cross_body_sling_drill]
  supported_by: [anatomy_trains_myers_2009]
  relevant_to: [trail_shoulder_external_rotation, functional_lines, spiral_line]
confidence: medium
review_status: draft_graph_mvp
relationship_count: 23
hub_score: 64
centrality: 0.207
updated: 2026-06-29
fma_id: "FMA:20448"
bodyparts3d_id: "BP3D:FMA20448"
openstax_ref: "OpenStax A&P 2e §11.3"
evidence_level: 1
evidence:
  - source_id: anatomy_trains_myers_2009
    evidence_level: 1
    supports: "Identifies Thoracolumbar Fascia as a primary structural force transmission node."
  - source_id: openstax_anatomy_physiology_2e
    evidence_level: 1
    supports: "Defines anatomical structure and boundaries of Thoracolumbar Fascia."
  - source_id: stecco_fascial_system_2015
    evidence_level: 2
    supports: "Documents histological and macroscopic fascial continuum of Thoracolumbar Fascia."
---

# Thoracolumbar Fascia

## Relationships

- connects_to -> [[latissimus_dorsi]]
- connects_to -> [[gluteus_maximus]]
- connects_to -> [[external_oblique]], [[internal_oblique]]
- connects_to -> [[lumbar_spine]]
- connects_to -> [[sacrum]]
- part_of -> [[functional_lines]]
- part_of -> [[spiral_line]]
- transmits_force_between -> upper limb, trunk, and pelvis
- active_during -> [[golf_swing_transition]]
- relevant_to -> [[trail_shoulder_external_rotation]]

## Movement Reasoning Role

Use this as a high-priority force-transmission hub. It helps the graph reason from trail shoulder loading and trunk rotation into pelvic control rather than stopping at individual muscles.

## Golf Relevance

This is one of the most important MVP structures for transition because it can connect [[latissimus_dorsi]], [[gluteus_maximus]], [[functional_lines]], [[thoracic_rotation]], and [[hip_internal_rotation]].

## Evidence Notes

The Myers source summary identifies lumbodorsal/sacral fascia in the Functional Line table extract. This node uses thoracolumbar fascia as the canonical product term and keeps `lumbodorsal fascia` as an alias.

## Open Questions

- Confirm whether the vault should prefer `thoracolumbar_fascia` or `lumbodorsal_fascia` as the canonical ID long term.
