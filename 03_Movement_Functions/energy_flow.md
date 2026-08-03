---
id: energy_flow
type: Movement Function
preferred_name: Energy Flow (Operational Definition)
aliases: [movement energy flow, coordinated energy transfer, energy-flow timing]
category: Biomechanics
short_definition: "Operationally, the coordinated transfer of motion through the body over time, assessed only through measurable kinematic and timing proxies — never as a vague or mystical score."
evidence_level: 2
evidence:
  - source_id: dr_kwon_golfer_ground_interaction
    evidence_level: 3
    supports: "Supplies the instrumented external mechanics that bound any legitimate energy claim; camera kinematics remain descriptors."
  - source_id: gray_cook_movement_2010
    evidence_level: 1
    supports: "Movement quality is judged by the whole pattern's organisation, not one isolated metric."
relationships:
  parent_concepts: [movement_chain_model]
  child_concepts: []
  related_concepts: [energy_transfer, kinematic_sequence, stretch_shortening_cycle, temporal_movement_metrics, segment_angle_metrics, personalised_movement_intelligence]
confidence: medium
review_status: draft_graph_mvp
relationship_count: 8
hub_score: 0
centrality: 0.0
updated: 2026-07-27
---

# Energy Flow (Operational Definition)

## Definition

**Energy flow** is defined operationally as the **coordinated transfer of motion through the body over time**. It is not a vibe, a score, or a mystical quantity: the engine assesses energy-flow-related behaviour only through measurable proxies and their timing.

The central question is:

> Does the person load, redirect, and release movement smoothly and efficiently **according to their own structure**?

## Why It Matters

Without an operational definition, "energy flow" drifts into an unfalsifiable label. Anchoring it to observable coordination keeps reports honest and keeps the focus on the person's own organisation rather than a single ideal.

## Measurable Proxies

Energy-flow-related behaviour is assessed through descriptors such as:

- ground-contact organisation and lead/trail-side timing;
- COM-proxy displacement;
- pelvis translation and rotation;
- thorax rotation and pelvis-thorax sequencing;
- shoulder, elbow, and wrist timing;
- club or hand path when visible;
- angular and linear velocity, acceleration, and deceleration descriptors;
- segment reversals and radius (hand-path) shortening;
- continuity of movement — the absence of abrupt pauses or compensations.

No single proxy defines energy flow; the movement must not be reduced to one isolated metric.

## Interpretation Layers

### Measured Mechanics — Levels 2–3

True mechanical energy transfer requires force-and-motion work analysis ([[energy_transfer]]). Instrumented golf mechanics are Level 3; video kinematics describe coordination only.

### Fascial Interpretation — Levels 1–2 plus explicit inference

Smooth flow *may be consistent with* effective fascial-line load sharing; this remains a labelled interpretation.

### App Hypothesis — Level 5

Any video-derived "energy flow", "leak", or "efficiency" output is a Level 5 coordination descriptor. Retired scores (ETE and related) remain controlled by [[golf_kinetics_observability_boundary]].

## Relationships

| Relationship | Target | Role |
| :--- | :--- | :--- |
| parent | [[movement_chain_model]] | Flow is a whole-chain property. |
| distinguished_from | [[energy_transfer]] | Flow = coordination; transfer = measured work/energy. |
| described_by | [[temporal_movement_metrics]] | Continuity and timing are temporal descriptors. |
| evidenced_by | [[stretch_shortening_cycle]] | Smooth SSC is one flow indicator. |
| expressed_in_golf | [[golf_movement_sequence]] | Full-sequence golf coordination. |
| personalised_by | [[personalised_movement_intelligence]] | Judged against the individual's own pattern. |

## Parent Concepts

- [[movement_chain_model]]

## Child Concepts

- None currently.

## Related Concepts

- [[kinematic_sequence]]
- [[segment_angle_metrics]]
- [[x_factor]]

## Evidence Level

The operational construct is Level 2; measured energy analysis is Level 3; video flow descriptors are Level 5.

## App Use

Report energy-flow-related behaviour as a *set* of timing, smoothness, and continuity descriptors, always tied to the person's own baseline. Never output a single "energy score", and never diagnose from it.

## Open Questions

- Which minimal proxy panel best captures "smooth load-redirect-release" across camera views?
- How should abrupt-pause detection be thresholded to stay robust at consumer frame rates?
