---
id: running_shoulder_rotation
canonical_id: running.rotation.shoulder
type: App Logic
running_node_type: measurement
evidence_level: 5
running_claim_level: A
status: canonical
preferred_name: "Running - Shoulder Rotation and Tilt Proxy"
aliases: [Shoulder Rotation, Shoulder line tilt, Frontal shoulder roll, Shoulder tipping]
domain: running
directly_measured: true
proxy_measurement: true
is_rotation_proxy: true
true_3d_rotation: false
camera_views: [front, back, side]
requires_clinical_correlation: false
confidence_required: contextual
related_nodes: []
source_nodes: [running_arellano_arm_swing_2014, running_preece_spine_pelvis_2016, running_upper_body_rotation_energy_2023, gruenke_kiptum_running_analysis_2023, running_movaia_kiptum_running_form_2023]
relationships:
  required_events: [running_running_cycle, running_initial_contact, running_toe_off]
  supports: [running_arm_leg_coordination, running_pelvis_thorax_rotation, running_rotational_coupling, running_cross_body_coordination, running_head_trunk_pelvis_coordination, running_altered_rotational_coordination]
  constrained_by: [running_measurement_limitations, running_kinematics_are_not_kinetics, running_evidence_gate]
confidence: high
review_status: canonical_definition
relationship_count: 20
hub_score: 38
centrality: 0.19
updated: 2026-10-15
---

# Running - Shoulder Rotation and Tilt Proxy

## Definition

A Level A camera-derived geometric proxy tracking the image-plane orientation and excursion of the shoulder girdle (defined by bilateral acromion/shoulder landmarks `MediaPipe 11` and `12`) across continuous time, evaluated independently during `LEFT_STANCE` and `RIGHT_STANCE` intervals.

## Why It Matters

Shoulder motion is the visible manifestation of upper-body angular momentum counterbalancing and torso elastic recoil. Rather than a sign of wasted energy, coordinated shoulder movement interacts with arm swing and pelvic rotation to stabilize the center of mass and preserve locomotor economy.

## Measurable TillYes Metrics and Camera Views

| Metric | Canonical ID | View | Description |
|---|---|---|---|
| Shoulder-line tilt | `running.frontal.shoulder_tilt` | front/back | Angle of bilateral shoulder line relative to horizontal; anatomical sign convention: positive indicates anatomical-right shoulder lower than left |
| Shoulder-line excursion | `shoulder_line_excursion_deg_projected` | front/back | Within-cycle peak-to-peak angular range of motion (degrees) during validated stance phase |
| Shoulder-pelvis offset | `running.position.shoulder_pelvis_offset` | side | Selected shoulder horizontal offset from pelvic center, normalized to image width |
| Shoulder center offset | `running.frontal.shoulder_centre_offset` | front/back | Midpoint between shoulders relative to pelvic center |

## Scientific Foundations

1. **Angular momentum cancellation**:
   - Controlled experiments by [[running_arellano_arm_swing_2014]] demonstrate that shoulder girdle rotation actively counterbalances lower-body angular momentum around the vertical axis.
   - Arm restriction changed axial pelvis and shoulder motion; use the corrected results in [[running_arellano_arm_swing_2014]]. Frontal tilt is not axial rotation.
2. **Anti-phase coordination with the pelvis**:
- Elastic recoil, head stabilization and individual economy mechanisms are hypotheses here; see [[running_pelvis_thorax_rotation]] and [[running_running_economy]] for the evidence boundary.
- Elastic recoil, head stabilization and individual economy mechanisms are hypotheses here; see [[running_pelvis_thorax_rotation]] and [[running_running_economy]] for the evidence boundary.
3. **Shoulder tipping and dynamic elastic recoil**:
   - In Kelvin Kiptum's marathon mechanics ([[gruenke_kiptum_running_analysis_2023]]), the shoulders tip downward toward the stance foot during initial contact/midstance.
- Elastic recoil, head stabilization and individual economy mechanisms are hypotheses here; see [[running_pelvis_thorax_rotation]] and [[running_running_economy]] for the evidence boundary.

## Bilateral Stance Evaluation: LEFT vs. RIGHT

Shoulder tilt excursion must be evaluated separately during:
- `LEFT_STANCE`: Stance interval of the left foot.
- `RIGHT_STANCE`: Stance interval of the right foot.
- Sampling uncertainty is metric-specific; [[running_dingenen_2d_reliability_2018]] does not validate a universal stride-count threshold for coordination.

## Biomechanical Hypotheses and Alternative Explanations

When shoulder excursion is analyzed alongside pelvic excursion:
1. **Symmetric shoulders with asymmetric pelvic tilt**:
   - If shoulder-line excursion is similar between sides (e.g. 8° left vs 8.5° right) while pelvic tilt excursion differs (e.g. 14° right vs 9° left):
     - **Spinal damping hypothesis**: The thoracic and lumbar spine absorbs pelvic motion via asymmetric lateral bending, preventing pelvic roll from transmitting upward to the shoulder girdle.
     - **Gaze/vestibular priority**: The upper body prioritizes horizontal eye-line and head stability over pelvic symmetry.
2. **Asymmetric shoulder excursion**:
   - **Arm swing asymmetry**: Difference in contralateral arm swing amplitude or elbow flexion angle ([[running_movaia_kiptum_running_form_2023]]) creates unequal counter-torques.
   - **Unilateral shoulder tipping**: Preferential recruitment of the lateral elastic recoil spring on one side.
   - **Structural or muscular asymmetry**: Thoracic curvature, scoliosis, or unilateral latissimus dorsi / pectoral tightness.
3. **Perspective artifacts**:
   - Runner yaw or camera angle changes project false shoulder tilt in 2D video ([[running_reinking_2d_reliability_2018]]).

## Anatomical Bridges

- **Joints & Bones**: [[shoulder_joint]], [[scapulothoracic_joint]], [[acromioclavicular_joint]], [[sternoclavicular_joint]], [[thoracic_spine]], [[cervical_spine]].
- **Key Musculature**: [[latissimus_dorsi]], [[pectoralis_major]], [[trapezius]], [[rhomboids]], [[serratus_anterior]], [[levator_scapulae]], [[deltoid]].
- **Myofascial Lines**: [[running_functional_lines]] (cross-body propulsion sling), [[running_spiral_line]] (helical trunk wrapper).

## Limitations and Evidence Boundaries

- Projected 2D line tilt is not true 3D thorax yaw, vertebral twist, or muscle force.
- High shoulder excursion is not automatically an error or fatigue marker.
- Do not prescribe rigid shoulder immobilization cues based on video analysis.

## Reporting Language

- *Permitted*: "Shoulder-line tilt excursion was symmetric across valid cycles (median 8.2° on left stance vs. 8.5° on right stance)."
- *Permitted*: "Shoulder and pelvis excursions differed; synchronized segment measurements are needed to investigate the explanation."
- *Forbidden*: "Shoulder asymmetry indicates rotator cuff weakness."
- *Forbidden*: "Excessive upper body motion is wasting 10% running economy."

## Review Status

`canonical_definition`. Grounded in peer-reviewed literature and high-speed motion capture findings.

## Audited reasoning route (2026-10-16)
Use [[running_reasoning_retrieval_index]] and its relationship nodes for evidence-separated interpretation. An anatomical or clinical explanation is a hypothesis until independently assessed.
