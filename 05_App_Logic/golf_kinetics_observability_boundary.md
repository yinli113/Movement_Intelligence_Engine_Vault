---
id: golf_kinetics_observability_boundary
type: App Logic
preferred_name: Golf Kinetics Observability Boundary
aliases: [golf measurement boundary, future golf observability policy]
tags: []
category: App Logic
short_definition: "Authoritative policy separating instrumented golf kinetics from single-camera motion descriptors and Level 5 hypotheses."
evidence_level: 5
evidence:
  - source_id: dr_kwon_golfer_ground_interaction
    evidence_level: 3
    supports: "Defines the measured golfer-ground force and moment taxonomy and its instrumentation boundaries."
  - source_id: anatomy_trains_myers_2009
    evidence_level: 1
    supports: "Defines fascial-line structure separately from any camera-derived tissue-state claim."
relationships:
  governs: [ai_movement_analysis_layer]
  parent_concepts: [vault_spec, evidence_levels]
  related_concepts: [golfer_ground_interaction_model, golf_swing, functional_lines, center_of_mass, center_of_pressure, kinematic_sequence]
  stable_anatomy: [functional_lines]
  golf_interpretation: [golf_swing, address_to_shaft_parallel, shaft_parallel_to_end_pelvis_rotation, end_pelvis_rotation_to_top_backswing, golf_swing_transition, max_unweighting_to_impact, impact_to_hands_chest_height]
  app_hypotheses: [torque_generation_score, com_cop_separation_score, functional_line_loading_index, energy_transmission_efficiency]
confidence: high
review_status: active_spec
relationship_count: 22
hub_score: 51
centrality: 0.379
updated: 2026-07-16
---

# Golf Kinetics Observability Boundary

## Definition

This is the authoritative future-golf measurement and reporting policy for the app. It separates quantities requiring kinetic or calibrated 3-D instrumentation from view-dependent geometry and timing that an ordinary single-camera recording may describe.

The current `movement_assessment` engine is gait-only and uses single-camera 2-D MediaPipe image coordinates. Its `docs/metrics.md` limits current outputs to proxies and its `docs/extending-the-engine.md` requires golf to become a separate registered assessment. Nothing in this note activates a golf assessment or changes that scope.

## Controlling Safety Rule

Camera geometry and timing may describe visible motion. They do not measure force, pressure, moment, impulse, energy transfer or energy flow, muscle activation, or fascial state. A Level 3 relationship from Kwon's instrumented mechanics does not upgrade a linked Level 5 camera proxy.

Instrument-derived labels are permitted only when the required synchronised sensors, coordinate definitions, calibration, data-quality gates and independent validation are present. Reports must retain raw evidence, provenance, view, units, uncertainty, algorithm version and unavailable states. They must make no diagnosis or treatment claim.

## Observability Matrix

The status vocabulary is closed: `unavailable`, `camera-observable descriptor`, or `Level 5 hypothesis`. A permitted descriptor is not permission to rename that descriptor as the concept in the first column.

| Concept | Gold-standard measurement | Single-camera status | Permitted app label | Prohibited inference |
| :--- | :--- | :--- | :--- | :--- |
| GRF | Synchronised force plate measuring each foot's three-component ground-reaction-force vector and COP. | unavailable | `sensor-derived GRF` only with compatible force-plate data; no video-only GRF output. | Knee extension, vertical landmark motion, foot motion or phase timing as force magnitude, direction, rate or effectiveness. |
| GRM | Force-plate moment components transformed to the residual/direct ground reaction moment represented at the foot COP. | unavailable | `sensor-derived GRM at COP` only with compatible force-plate moment data. | Pelvis rotation, foot rotation or a camera-derived GRF-about-COM calculation as GRM. |
| COP | Force plate or validated pressure platform calculating the point of application from measured contact forces. | unavailable | `sensor-derived COP`; a foot or ankle landmark may be named only as that landmark. | A visible foot point, ankle point, hip position, apparent balance or body shift as COP, pressure or weight shift. |
| COM | Calibrated 3-D motion capture with a declared whole-body segment model and mass parameters. | unavailable | `hip-midpoint image-plane coordinate` or displacement when that is the actual calculation. | Hip midpoint, torso midpoint or COP as measured whole-body COM. |
| moment arm | Synchronised 3-D force plate and calibrated motion-capture data establishing the chosen reference and measured force line of action. | unavailable | `landmark separation descriptor` when only landmark geometry is available. | COM-COP, hip-ankle or other point separation as the perpendicular moment arm without the measured force vector and compatible coordinates. |
| pivoting moment | Two synchronised force plates resolving each foot's 3-D GRF and COP about combined COP and the vertical axis. | unavailable | `sensor-derived pivoting moment` only after the required bilateral calculation. | Pelvis angular motion, foot orientation, apparent pivoting or single-plate/pressure-mat output as pivoting moment. |
| foot-contact moment | Force-plate residual/direct torsional GRM at each foot COP. | unavailable | `sensor-derived foot-contact moment` only with compatible force-plate moment data. | Foot turn, shoe motion, friction appearance or pivoting moment as direct torsional foot-contact moment. |
| linear impulse | Time integral of synchronised measured external force over explicitly defined event bounds. | unavailable | `sensor-derived linear impulse` with force data, time base and declared interval. | Displacement, velocity, event duration or unweighting appearance as impulse or change in momentum. |
| angular impulse | Time integral of measured external moment about a stated reference over explicitly defined event bounds. | unavailable | `sensor-derived angular impulse` with all three external moment classes handled without duplicate GRM counting. | Rotation amount, angular velocity, phase duration or sequence timing as angular impulse. |
| angular momentum | Calibrated 3-D multi-segment kinematics, segment inertial parameters and a declared golfer-only or golfer-club system and reference. | unavailable | `model-derived angular momentum` only from a validated compatible 3-D model. | Segment angle, angular velocity, deceleration or peak sequence as angular momentum or momentum transfer. |
| pelvis orientation | Calibrated 3-D motion capture using a defined pelvis coordinate system. | Level 5 hypothesis | `image-plane hip-line angle descriptor`, with camera view and confidence. | A 2-D hip-line angle as anatomical 3-D pelvis orientation, moment, force or pelvic torque. |
| thorax orientation | Calibrated 3-D motion capture using a defined thorax coordinate system. | Level 5 hypothesis | `image-plane shoulder-line angle descriptor`, with camera view and confidence. | A 2-D shoulder-line angle as anatomical 3-D thorax orientation, energy transfer or tissue loading. |
| pelvis-thorax separation | Synchronised calibrated 3-D pelvis and thorax orientations in declared coordinate and rotation conventions. | Level 5 hypothesis | `image-plane shoulder-line minus hip-line angle descriptor`. | The descriptor as 3-D torsional separation, stored energy, X-factor efficacy, muscle activation or fascial loading. |
| segment angular velocity | High-speed calibrated 3-D motion capture differentiating a defined segment orientation with filtering and uncertainty controls. | Level 5 hypothesis | `image-plane line-angle rate descriptor`, with frame rate, smoothing, view and reliability. | A 2-D rate or peak order as 3-D angular velocity, kinetic energy, angular momentum or energy transmission. |
| phase timing | A synchronised high-speed 3-D motion/club system applying explicit operational event definitions. | camera-observable descriptor | `camera event-time` or `camera phase-duration descriptor` when the required landmarks are visible. | A vault boundary as an unmatched Kwon event, or timing alone as force, impulse, contact kinetics or a universal ideal. |
| hip-midpoint vertical displacement | Calibrated 3-D motion capture for anatomical displacement; a validated body model is additionally required for any COM claim. | camera-observable descriptor | `image-plane hip-midpoint vertical displacement`, in pixels or normalised image units. | Vertical GRF, unweighting force, jump, pressure change or whole-body COM displacement. |
| foot geometry | Calibrated multi-view or 3-D foot/club motion capture for anatomical position and orientation. | camera-observable descriptor | `image-plane foot-landmark position`, distance or angle descriptor, with view and visibility. | COP, pressure distribution, GRF direction, foot-contact moment, pivoting moment or tissue load. |
| diagonal shoulder-hip distance | Calibrated 3-D landmarks for anatomical inter-landmark distance; independent tissue measures for any tissue-state construct. | camera-observable descriptor | `camera-derived diagonal-distance descriptor; tissue loading remains unknown`. | Fascial stretch/loading, elastic energy, muscle activation, force transmission efficiency or diagnosis. |

## Exact Mechanics Taxonomy Consumed

The matrix consumes [[golfer_ground_interaction_model]] without changing its three-class taxonomy:

```text
External moment about golfer COM
├── GRF moment: r(COM→foot COP) × foot GRF
├── Pivoting moment: individual foot GRFs about the combined COP/vertical axis
└── Foot-contact moment: direct torsional GRM at the foot-ground interface
```

[[ground_reaction_force]] (GRF) and [[ground_reaction_moment]] (GRM) remain distinct. GRM is the residual/direct moment at COP that underlies [[foot_contact_moment]]; it is not a duplicate fourth class and is not the GRF moment about COM. [[pivoting_moment]], [[linear_impulse]], [[angular_impulse]] and [[angular_momentum]] retain their stated sensors, reference systems and integration bounds.

## Six-Phase Hooks

The future golf assessment preserves the six Level 4 vault phases and the conservative Kwon event crosswalk in [[golf_swing]]. Event detection remains a camera timing descriptor unless validated against the relevant operational definition.

| Vault phase hook | Permitted single-camera use |
| :--- | :--- |
| [[address_to_shaft_parallel]] | Describe visible landmark geometry and candidate boundary timing; Address and Shaft Parallel remain not yet mapped to Kwon events. |
| [[shaft_parallel_to_end_pelvis_rotation]] | EPR may anchor the end event when its operational criteria are met; do not infer kinetics across the interval. |
| [[end_pelvis_rotation_to_top_backswing]] | EPR and TB are supported boundary matches; the interval remains the vault phase rather than a substituted Kwon phase. |
| [[golf_swing_transition]] | TB may anchor the start; Max Unweighting remains not yet mapped and cannot imply vertical force or impulse. |
| [[max_unweighting_to_impact]] | BI may anchor Impact; Max Unweighting remains a source-defined timing label, not measured unweighting force. |
| [[impact_to_hands_chest_height]] | BI may anchor the start; Hands Chest Height must not be relabelled MF or LF without matched definitions. |

## Fascial Evidence Boundary

[[functional_lines]] and the other fascial lines remain the primary anatomical structure. Kwon supplies Level 3 external mechanics; Anatomy Trains supplies Level 1 structural pathways; any mapping between them is a separately labelled vault interpretation. Camera output cannot establish line loading, tension, recoil, energy storage/release, tissue state or muscle activation.

Diagonal geometry may support the exact label **camera-derived diagonal-distance descriptor; tissue loading remains unknown**. It may not support the Functional Line Loading Index or a tissue-specific finding without an independently validated construct and the required instrumentation.

## Sensor and Validation Gates

Before any unavailable or Level 5 concept becomes an implemented output, its assessment specification must define:

1. the system boundary, coordinate systems, units, source view and operational events;
2. the required synchronised force, pressure, 3-D motion, club, EMG or independent tissue instrumentation;
3. missing-data, occlusion, frame-rate, calibration and reliability failure behaviour, returning unavailable rather than a plausible value;
4. criterion labels and a representative consented validation dataset with train/validation/test separation where modelling is used;
5. absolute and relative error, calibration, subgroup and view analyses, repeatability, versioning and rollback; and
6. report wording that distinguishes measured sensor data, camera-observable descriptors and Level 5 hypotheses.

## Relationships

| Relationship | Target | Role |
| :--- | :--- | :--- |
| governed_by | [[evidence_levels]] | Applies the five-level hierarchy and proxy non-upgrade rule. |
| consumes | [[golfer_ground_interaction_model]] | Preserves the exact external-moment taxonomy. |
| consumes | [[golf_swing]] | Preserves the six vault phase hooks and event crosswalk. |
| consumes | [[functional_lines]] | Preserves the line-first anatomical model and tissue-state boundary. |
| governs | [[ai_movement_analysis_layer]] | Retires unsupported score implementation while retaining historical context. |
| distinguishes | [[center_of_mass]] / [[center_of_pressure]] | Prevents hip or foot geometry from being relabelled as COM or COP. |
| distinguishes | [[kinematic_sequence]] / [[angular_momentum]] | Prevents timing and angular-velocity order from being called energy or momentum transfer. |

## Evidence Level

**Level 5 — app policy grounded in separate Level 1 anatomical and Level 3 instrumented-mechanics sources.** The policy does not upgrade its proxies into measurements.

## App Use

Use this matrix as the output allow-list for a future separately registered golf assessment. If the exact permitted label and its reliability/provenance requirements cannot be satisfied, return unavailable. Do not diagnose, prescribe treatment, or imply injury risk from these descriptors.

## Open Questions

- Which camera views and frame rates produce repeatable golf event-time and image-plane orientation descriptors?
- Which instrumented validation protocol, if any, could justify promoting a specific Level 5 descriptor while retaining a non-kinetic label?
