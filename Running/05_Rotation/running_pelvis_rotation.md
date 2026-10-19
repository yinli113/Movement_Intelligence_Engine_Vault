---
id: running_pelvis_rotation
canonical_id: running.rotation.pelvis
type: App Logic
running_node_type: measurement
evidence_level: 5
running_claim_level: A
status: canonical
preferred_name: "Running - Pelvis Rotation and Tilt Proxy"
aliases: [Pelvis Rotation, Pelvic line tilt, Pelvic obliquity proxy, Frontal pelvic roll]
domain: running
directly_measured: true
proxy_measurement: true
is_rotation_proxy: true
true_3d_rotation: false
camera_views: [front, back]
requires_clinical_correlation: false
confidence_required: contextual
related_nodes: []
source_nodes: [running_preece_spine_pelvis_2016, running_mesquita_step_frequency_pelvis_2024, perpina_martinez_pelvic_imu_running_2023, gruenke_kiptum_running_analysis_2023]
relationships:
  required_events: [running_running_cycle, running_initial_contact, running_toe_off]
  supports: [running_pelvis_thorax_rotation, running_rotational_coupling, running_rotational_reversal, running_altered_rotational_coordination, running_left_right_asymmetry, running_head_trunk_pelvis_coordination]
  constrained_by: [running_measurement_limitations, running_kinematics_are_not_kinetics, running_evidence_gate]
confidence: high
review_status: canonical_definition
relationship_count: 22
hub_score: 42
centrality: 0.22
updated: 2026-10-15
---

# Running - Pelvis Rotation and Tilt Proxy

## Definition

A Level A camera-derived geometric proxy tracking the image-plane angular orientation and excursion of the pelvic segment (defined by bilateral hip landmarks) across continuous time, evaluated independently during `LEFT_STANCE` and `RIGHT_STANCE` intervals.

## Why It Matters

Pelvic motion reflects the continuous mechanical interaction among ground reaction forces, stance-limb hip stabilization, cadence, and torso counter-rotation. In world-class marathoners, pelvic movement is active, dynamic, and variable; a rigid, immovable pelvis is neither natural nor metabolically optimal.

## Measurable TillYes Metrics and Camera Views

| Metric | Canonical ID | View | Description |
|---|---|---|---|
| Pelvis-line tilt | `running.frontal.pelvis_tilt` | front/back | Angle of bilateral hip vector (`MediaPipe 23` to `24`) relative to horizontal; anatomical sign convention: positive indicates anatomical-right hip lower than left |
| Pelvis-line excursion | `pelvic_line_excursion_deg_projected` | front/back | Within-cycle peak-to-peak angular range of motion (degrees) during validated stance phase |
| Pelvis center translation | `running.body_centre.proxy` | front/back/side | Midpoint between bilateral hips ($x, y$); proxy for pelvic center progression, not whole-body CoM |

## Scientific Foundations

1. **3D multi-segment coordination**:
   - In 3D motion capture studies ([[running_preece_spine_pelvis_2016]]), the pelvis coordinates in anti-phase with the thoracic spine in the frontal and sagittal planes, while lagging behind the thorax in the transverse plane.
- Frequency and speed may alter coordination under specific conditions; consult [[running_mesquita_step_frequency_pelvis_2024]] and [[running_preece_speed_2016]] rather than infer a deterministic individual response.
2. **Step frequency (cadence) modulation**:
- Frequency and speed may alter coordination under specific conditions; consult [[running_mesquita_step_frequency_pelvis_2024]] and [[running_preece_speed_2016]] rather than infer a deterministic individual response.
3. **Stance hip elevation and lateral recoil**:
- Elastic recoil, head stabilization and individual economy mechanisms are hypotheses here; see [[running_pelvis_thorax_rotation]] and [[running_running_economy]] for the evidence boundary.

## Bilateral Stance Evaluation: LEFT vs. RIGHT

Pelvic tilt excursion must be segmented by stance foot:
- `LEFT_STANCE`: Interval from accepted left initial contact to accepted left toe-off.
- `RIGHT_STANCE`: Interval from accepted right initial contact to accepted right toe-off.
- Report `left_median`, `right_median`, `difference_left_minus_right`, variability band, and valid sample count $n$.
- Sampling uncertainty is metric-specific; [[running_dingenen_2d_reliability_2018]] does not validate a universal stride-count threshold for coordination.

## Biomechanical Hypotheses and Alternative Explanations

When a runner demonstrates asymmetric pelvic-line tilt excursion between left and right stance:
1. **Cadence and temporal asymmetry**: Check if step time is longer on the side with greater excursion; increased stance duration allows gravity to induce more pelvic drop ([[running_mesquita_step_frequency_pelvis_2024]]).
2. **Stance hip abductor capacity**: Greater pelvic drop (Trendelenburg-type excursion) may reflect stance-phase hip abductor demand ([[gluteus_medius]], [[gluteus_minimus]], [[tensor_fasciae_latae]]) or contralateral quadratus lumborum / oblique control.
3. **Elastic spring strategy**: Asymmetric excursion may represent an individual lateral loading strategy where one side utilizes greater hip hike and shoulder tipping for elastic recoil ([[running_spiral_line]]).
4. **Arm swing compensation**: Check if contralateral arm excursion is reduced, forcing the pelvis to rotate more to balance lower limb angular momentum ([[running_arellano_arm_swing_2014]]).
5. **Perspective foreshortening and yaw cross-talk**: 2D front-view cameras conflate out-of-plane axial twisting (yaw) with frontal tilt; an athlete drifting obliquely or turning on a track will display artificial tilt asymmetry ([[running_reinking_2d_reliability_2018]]).
6. **Structural traits**: Anatomical leg length discrepancy, hip joint morphology, or asymmetric foot pronation can alter stance pelvic alignment.

## Anatomical Bridges

- **Joints & Bones**: [[sacrum]], [[sacroiliac_joint]], [[hip_joint]], [[lumbar_spine]].
- **Key Musculature**: [[gluteus_medius]], [[gluteus_minimus]], [[tensor_fasciae_latae]], [[gluteus_maximus]], [[quadratus_lumborum]], [[external_oblique]], [[internal_oblique]], [[psoas_major]], [[piriformis]].
- **Myofascial Lines**: [[running_spiral_line]] (lateral recoil & stirrup), [[running_deep_front_line]] (axial single-leg pillar), [[running_functional_lines]] (contralateral propulsion).

## Limitations and Evidence Boundaries

- Camera 2D pelvic tilt is an image-plane projection, not calibrated 3D bone orientation, joint torque, or force-plate ground reaction force ([[running_kinematics_are_not_kinetics]]).
- Monocular video cannot distinguish between true frontal roll and projected axial rotation (yaw).
- Nonzero asymmetry does not equal clinical pathology, weakness, or injury risk.

## Reporting Language

- *Permitted*: "During right stance, pelvic-line tilt excursion was 14.2° (median of 9 strides), compared to 9.8° during left stance."
- *Permitted*: "The greater right pelvic excursion coexisted with a 35 ms longer right step time, consistent with cadence-dependent stance mechanics."
- *Forbidden*: "Right gluteus medius weakness detected."
- *Forbidden*: "Pelvic instability diagnosed."

## Review Status

`canonical_definition`. Enriched with peer-reviewed biomechanics literature and bilateral quality contracts.

## Audited reasoning route (2026-10-16)
Use [[running_reasoning_retrieval_index]] and its relationship nodes for evidence-separated interpretation. An anatomical or clinical explanation is a hypothesis until independently assessed.
