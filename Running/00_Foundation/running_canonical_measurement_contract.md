---
id: running_canonical_measurement_contract
canonical_id: running.foundation.measurement_contract
type: App Logic
running_node_type: contract
evidence_level: 5
running_claim_level: rule
status: canonical
preferred_name: Running - Canonical Measurement Contract
aliases: [TillYes Running measurement contract]
domain: running
directly_measured: false
camera_views: [side, front, back]
requires_clinical_correlation: false
confidence_required: contextual
related_nodes: []
source_nodes: [till_yes_running_literature_foundation]
relationships:
  contains: [running_cadence, running_step_time, running_stride_time, running_contact_time, running_flight_time, running_landing_relationship, running_foot_strike, running_tibial_inclination, running_knee_flexion_at_contact, running_body_centre_proxy, running_com_progression, running_vertical_oscillation, running_horizontal_progression, running_leg_compression_proxy, running_trunk_lean, running_pelvis_rotation, running_thorax_rotation, running_shoulder_rotation, running_pelvis_thorax_rotation, running_till_yes_progression_ratio]
  governed_by: [running_evidence_levels, running_evidence_gate, running_measurement_limitations, running_reporting_guardrails]
confidence: high
review_status: canonical
relationship_count: 32
hub_score: 36
centrality: 0.286
updated: 2026-09-14
---

# Running - Canonical Measurement Contract

This table is the implementation bridge. Each linked note owns its calculation, quality gate, view, limits, literature, and report wording.

| Metric | Canonical ID | Running claim | View | Direct? | Event | Confidence | Supports |
|---|---|---:|---|---|---|---|---|
| [[running_cadence|Cadence]] | `running.rhythm.cadence` | A | side/front/back | computed | repeated contacts | high | rhythm, drift |
| [[running_step_time|Step time]] | `running.rhythm.step_time` | A | any valid event view | computed | contralateral contacts | high | asymmetry |
| [[running_stride_time|Stride time]] | `running.rhythm.stride_time` | A | any valid event view | computed | same-side contacts | high | cycle timing |
| [[running_contact_time|Contact-time proxy]] | `running.rhythm.contact_time` | A | side | proxy | contact to toe-off | medium-high | stance timing |
| [[running_flight_time|Flight-time proxy]] | `running.rhythm.flight_time` | A | side | proxy | toe-off to contact | medium | cycle timing |
| [[running_landing_relationship|Landing relationship]] | `running.landing.relationship` | A | side | proxy | reviewed initial contact | high | landing pattern |
| [[running_foot_strike|Estimated foot strike]] | `running.landing.foot_strike` | A | side | proxy | initial contact | contextual | strategy descriptor |
| [[running_tibial_inclination|Tibial inclination]] | `running.landing.tibial_inclination` | A | side | 2D proxy | initial contact | high | landing pattern |
| [[running_knee_flexion_at_contact|Knee flexion at contact]] | `running.landing.knee_flexion_at_contact` | A | side | 2D proxy | initial contact | high | landing/compression |
| [[running_body_centre_proxy|Body-centre proxy]] | `running.body_centre.proxy` | A | side/front/back | proxy | continuous | method-dependent | trajectory |
| [[running_com_progression|COM progression]] | `running.body_centre.progression` | A | side | proxy unless segmental model | full stride | medium | progression |
| [[running_vertical_oscillation|Vertical excursion]] | `running.body_centre.vertical_oscillation` | A | side | proxy | full stride | medium-high | progression/drift |
| [[running_horizontal_progression|Horizontal progression]] | `running.body_centre.horizontal_progression` | A | side | proxy | full stride | contextual | progression |
| [[running_leg_compression_proxy|Leg compression]] | `running.compression.leg_compression_proxy` | A | side | proxy | contact to max compression | medium-high | compression pattern |
| [[running_trunk_lean|Trunk inclination]] | `running.trunk.lean` | A | side | 2D proxy | continuous or declared phase | high | selected-side segment descriptor |
| [[running_pelvis_rotation|Pelvis rotation]] | `running.rotation.pelvis` | A | front/back | rotation proxy | stride cycle | contextual | coupling |
| [[running_thorax_rotation|Thorax rotation]] | `running.rotation.thorax` | A | front/back | rotation proxy | stride cycle | contextual | coupling |
| [[running_shoulder_rotation|Shoulder-line rotation]] | `running.rotation.shoulder` | A | front/back | rotation proxy | stride cycle | contextual | arm-leg coordination |
| [[running_pelvis_thorax_rotation|Pelvis-thorax relationship]] | `running.rotation.pelvis_thorax` | B | front/back | derived proxy | stride cycle | contextual | rotational interpretation |
| [[running_till_yes_progression_ratio|TillYes Progression Ratio]] | `running.descriptor.till_yes_progression_ratio` | B | side | derived proxy | full stride | contextual | descriptor only |
| [[running_spiral_line|Spiral Line contribution]] | `running.myofascial.spiral_line` | D | n/a | no | n/a | contextual | hypothesis only |

### Video-workspace continuous descriptor set

The video-first Running workspace may expose these Level A image-plane descriptors when decoded source geometry, required landmarks, view, anatomical side, and direction gates are satisfied. Every plotted point remains linked to its raw evidence frame. Gaps remain gaps; the app must not interpolate across missing landmarks or a changed reference. These IDs are canonical app contracts, not normative targets.

| Descriptor | Canonical ID | View | Reference and sign | Unit | Boundary |
|---|---|---|---|---|---|
| Shoulder-pelvis offset | `running.position.shoulder_pelvis_offset` | side | selected shoulder from moving pelvis centre; positive ahead in declared running direction | percent decoded image width | not distance in centimetres |
| Ankle-pelvis offset | `running.position.ankle_pelvis_offset` | side | selected ankle from moving pelvis centre; positive ahead in declared running direction | percent decoded image width | continuous position descriptor, not landing |
| Head-pelvis offset | `running.position.head_pelvis_offset` | side | nose landmark from moving pelvis centre; positive ahead in declared running direction | percent decoded image width | head landmark proxy |
| Selected ankle-shoulder inclination | `running.alignment.selected_ankle_shoulder_inclination` | side | selected ankle-to-shoulder line; positive forward in declared running direction | aspect-corrected projected degrees from frame vertical | not whole-body centre-of-mass lean |
| Trunk inclination | `running.trunk.lean` | side | selected hip-to-shoulder segment; positive forward in declared running direction | aspect-corrected projected degrees from frame vertical | frame vertical is uncalibrated |
| Knee flexion | `running.knee.flexion` | side | selected hip-knee-ankle included angle subtracted from 180 degrees | aspect-corrected projected degrees | image-plane flexion, not 3D joint angle |
| Shoulder-centre offset | `running.frontal.shoulder_centre_offset` | front/back | shoulder centre from pelvis centre; positive anatomical right | percent decoded image width | not centre of pressure |
| Head-pelvis offset | `running.frontal.head_pelvis_offset` | front/back | nose landmark from pelvis centre; positive anatomical right | percent decoded image width | head landmark proxy |
| Left/right ankle offset | `running.frontal.left_ankle_offset`, `running.frontal.right_ankle_offset` | front/back | named anatomical ankle from pelvis centre; positive anatomical right | percent decoded image width | not step width or physical distance |
| Left/right knee offset | `running.frontal.left_knee_offset`, `running.frontal.right_knee_offset` | front/back | named anatomical knee from pelvis centre; positive anatomical right | percent decoded image width | not knee loading or diagnosis |
| Pelvis tilt | `running.frontal.pelvis_tilt` | front/back | anatomical left-to-right hip line; positive means anatomical-right landmark lower in the image | aspect-corrected projected degrees | image-plane only |
| Shoulder tilt | `running.frontal.shoulder_tilt` | front/back | anatomical left-to-right shoulder line; positive means anatomical-right landmark lower in the image | aspect-corrected projected degrees | image-plane only |

`running.alignment.whole_body_lean` is retained only for stored-session compatibility. Its mixed shoulder-centre to selected-ankle reference must not be surfaced as whole-body lean. `running.landing.relationship` remains reserved for the selected ankle-pelvis relationship at a reviewed initial-contact event. The continuous ankle-pelvis trace must not use the landing label.

Stride/event-derived descriptors such as knee-flexion excursion, step-width proxy, lateral sway, and path symmetry remain separate from the raw continuous frame series and retain their existing evidence gates.

Front/back rotation language remains a camera-derived proxy. No single-camera overlay or chart may be described as force, stiffness, tissue loading, injury risk, or a direct fascial finding.

## Multi-Stride Output Contract

Where possible return mean, median, standard deviation, valid stride count, left/right difference, early mean, late mean, trend, confidence, quality flags, and algorithm version. See [[running_variability]], [[running_left_right_asymmetry]], and [[running_fatigue_drift]].

## Evidence and Safety Contract

- A values remain camera descriptors or declared proxies under vault Level 5 until validated.
- B nodes must name their A inputs.
- C nodes must name measurements/patterns and matched literature.
- D nodes must name a C interpretation and require clinical correlation.
- [[running_kinematics_are_not_kinetics]] always applies.
- [[running_running_economy]] is not directly measurable from pose video.
- If a gate fails, return "Insufficient reliable evidence to interpret this feature."

## Open Questions

- Operational thresholds, validation datasets, and algorithm versions remain implementation work; this graph intentionally does not invent them.
