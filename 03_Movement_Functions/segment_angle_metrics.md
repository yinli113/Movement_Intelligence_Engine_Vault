---
id: segment_angle_metrics
type: Movement Function
preferred_name: Segment-Angle and COM-Proxy Metrics
aliases: [segment orientation metrics, segment-line angles, base-of-support organisation metrics]
category: Biomechanics
short_definition: "Segment orientations measured relative to the ground or base of support (e.g., shank, thigh, pelvis line, trunk axis, lead-side support line) that describe how the body shifts and organises itself, complementing isolated joint-flexion angles."
evidence_level: 2
evidence:
  - source_id: chambers_sutherland_gait_analysis_2002
    evidence_level: 1
    supports: "Observational gait analysis describes segment alignment relative to the ground and base of support, distinct from instrumented joint kinetics."
  - source_id: dr_kwon_golfer_ground_interaction
    evidence_level: 3
    supports: "Segment and body-line orientations participate in the golfer-ground interaction model; measured forces require instrumentation."
relationships:
  parent_concepts: [movement_chain_model]
  child_concepts: []
  related_concepts: [center_of_mass, temporal_movement_metrics, kinematic_sequence, golf_movement_sequence, golf_kinetics_observability_boundary]
confidence: medium
review_status: draft_graph_mvp
relationship_count: 8
hub_score: 16
centrality: 0.072
updated: 2026-07-27
---

# Segment-Angle and COM-Proxy Metrics

## Definition

**Segment-angle metrics** describe the orientation of a body segment or body line **relative to the ground (or base of support)**, rather than the flexion angle between two segments. They capture how the body shifts and organises itself globally, which isolated joint angles miss.

## Why It Matters

A knee-flexion angle says nothing about where the shank points relative to the ground or how mass is being supported. Segment-to-ground orientation is often the more informative descriptor of support, force redirection posture, and whole-body organisation — especially from a single camera.

## Example Measures

| Measure | Definition (camera-observable form) |
| :--- | :--- |
| shank angle | knee-ankle line orientation relative to the ground |
| thigh angle | hip-knee line orientation relative to the ground |
| pelvis line orientation | left-right hip-line tilt |
| trunk axis | pelvis-midpoint to shoulder-midpoint line |
| lead-side support line | lead shoulder-to-ankle (or hip-to-ankle) organisation |
| hip-to-knee vector | frontal-plane support descriptor |
| knee-to-ankle vector | shank organisation under load |
| shoulder-to-hip vector | trunk organisation over the pelvis |

## Interpretation Layers

### Measured Mechanics — Levels 2–3

With calibrated 3-D capture these become anatomical orientations; combined with measured forces they may inform moment analysis. A 2-D segment line does **not** prove the direction or magnitude of ground-reaction force.

### Fascial Interpretation — Levels 1–2 plus explicit inference

Shifts in segment organisation *could reflect* changing load distribution across fascial lines; the association is interpretive only.

### App Hypothesis — Level 5

Image-plane segment-line angles are Level 5 descriptors requiring camera-view and confidence context. They must not be renamed as force lines, COP, or tissue loading.

## Relationships

| Relationship | Target | Role |
| :--- | :--- | :--- |
| parent | [[movement_chain_model]] | Segment organisation is a chain property. |
| complements | [[temporal_movement_metrics]] | Orientations tracked over time. |
| related | [[center_of_mass]] | Segment organisation around the COM proxy. |
| applied_in | [[golf_movement_sequence]] | Full-body golf organisation metrics. |
| bounded_by | [[golf_kinetics_observability_boundary]] | 2-D lines are not force vectors. |

## Parent Concepts

- [[movement_chain_model]]

## Child Concepts

- None currently.

## Related Concepts

- [[center_of_mass]]
- [[kinematic_sequence]]
- [[golf_movement_sequence]]

## Evidence Level

General segment-orientation description is Level 2; instrumented orientation-plus-force analysis is Level 3; single-camera line angles are Level 5.

## App Use

Report segment-to-ground orientations as image-plane descriptors with view and confidence. Use them to describe support and weight-shift organisation; never present a segment line as a ground-reaction-force direction or magnitude.

## Open Questions

- Which two or three segment angles give the most stable single-camera description of golf support organisation?
- How should camera-view obliquity degrade confidence in frontal-plane segment angles?
