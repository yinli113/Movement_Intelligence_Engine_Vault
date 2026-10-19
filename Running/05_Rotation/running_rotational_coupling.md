---
id: running_rotational_coupling
canonical_id: running.rotation.coupling
type: Movement Pattern
running_node_type: movement_pattern
evidence_level: 5
running_claim_level: B
status: canonical
preferred_name: "Running - Rotational Coupling Across Segments"
aliases: [Rotational Coupling, Multi-segment coupling, Phase lag, Upper-lower body coupling]
domain: running
directly_measured: false
camera_views: [front, back, side]
requires_clinical_correlation: false
confidence_required: contextual
related_nodes: []
source_nodes: [running_preece_spine_pelvis_2016, running_arellano_arm_swing_2014, running_upper_body_rotation_energy_2023, running_morley_lumbar_restriction_2019]
relationships:
  required_inputs: [running_pelvis_rotation, running_shoulder_rotation, running_pelvis_thorax_rotation, running_arm_leg_coordination, running_running_cycle, running_variability]
  supports: [running_altered_rotational_coordination, running_cross_body_coordination, running_head_trunk_pelvis_coordination, running_three_layer_rotation_model]
  constrained_by: [running_evidence_gate, running_reporting_guardrails, running_kinematics_are_not_kinetics, running_measurement_limitations]
confidence: high
review_status: canonical_definition
relationship_count: 22
hub_score: 40
centrality: 0.20
updated: 2026-10-15
---

# Running - Rotational Coupling Across Segments

## Definition

A derived kinematic representation of the continuous timing, relative phase, and repeatability connecting head, shoulder, arm, thorax, pelvis, and leg proxy movements across valid stride cycles.

## Why It Matters

Running locomotion is governed by dynamic angular momentum equilibrium. Leg swings produce large rotational moments around the longitudinal axis; rotational coupling across the arms, shoulder girdle, spine, and pelvis cancels these moments, maintains gaze stability, and enables passive elastic recoil.

## Multi-Segment Coordination Mechanisms

1. **Upper-to-Lower Body Momentum Balancing**:
   - As established by [[running_arellano_arm_swing_2014]], swinging the arms and rotating the shoulder girdle counteracts the angular momentum of the lower extremities.
   - If arm swing is compact or asymmetric, the pelvis and trunk adjust their phase coupling and amplitude to preserve total body yaw balance.
2. **Phase Lag in the Transverse Plane**:
   - In 3D motion capture ([[running_preece_spine_pelvis_2016]]), the pelvis consistently lags behind the thorax in the transverse plane, acting as a delayed rotational spring.
   - This phase delay stores elastic potential in diagonal abdominal and fascial structures during midstance compression, releasing it at push-off.
3. **Speed and Energy Interactions**:
   - Rotational coupling amplitude scales directly with running speed; greater upper-body longitudinal rotation associates with superior running economy in junior elite runners ([[running_upper_body_rotation_energy_2023]]).
   - Restricting spinal mobility raises oxygen cost and disrupts coupling ([[running_morley_lumbar_restriction_2019]]).

## Bilateral Coupling Patterns: Left vs. Right Stance

- **Symmetrical Coupling**: Phase lag and peak reversal timing between shoulders and pelvis are identical between `LEFT_STANCE` and `RIGHT_STANCE`.
- **Asymmetrical Lag**: The pelvis lags the shoulders by a longer phase duration during one stance than the other.
- **Amplitude Decoupling**: Large pelvic tilt excursion coexisting with modest shoulder tilt, mediated by spinal lateral flexion.

## Biomechanical Hypotheses for Asymmetric Coupling

- **Contralateral Power Sling Drive**: Asymmetry in push-off drive between left and right legs alters the torque required from the opposite arm and shoulder ([[running_functional_lines]]).
- **Unilateral Spiral Line Recruitment**: Preferential lateral spring loading (shoulder tipping and stance-hip elevation) on one side ([[running_spiral_line]], [[gruenke_kiptum_running_analysis_2023]]).
- **Deep Core Axial Control**: Differences in single-leg stance axial stability ([[running_deep_front_line]]) altering pelvis support.
- Sampling uncertainty is metric-specific; [[running_dingenen_2d_reliability_2018]] does not validate a universal stride-count threshold for coordination.

## Anatomical Bridges

- **Spinal Segments & Pelvis**: [[thoracic_spine]], [[lumbar_spine]], [[sacrum]], [[hip_joint]], [[shoulder_joint]].
- **Muscles**: [[latissimus_dorsi]], [[external_oblique]], [[internal_oblique]], [[gluteus_maximus]], [[gluteus_medius]], [[psoas_major]], [[rectus_abdominis]], [[rhomboids]], [[serratus_anterior]].
- **Fascial Structures**: [[thoracolumbar_fascia]], [[running_three_layer_rotation_model]].

## Limitations and Evidence Boundaries

- Coupling is computed from 2D projected line angles; it is not a direct measure of 3D angular momentum, ground reaction force, or fascial tension.
- Higher or lower coupling is not an index of injury risk or athlete impairment.

## Reporting Language

- *Permitted*: "Shoulder-pelvis phase lag was 5.1% of stride during left stance and 4.8% during right stance across 10 valid cycles."
- *Forbidden*: "Impaired rotational coupling detected in thoracic spine."

## Review Status

`canonical_definition`. Grounded in experimental momentum studies and 3D kinematics.

## Audited reasoning route (2026-10-16)
Use [[running_reasoning_retrieval_index]] and its relationship nodes for evidence-separated interpretation. An anatomical or clinical explanation is a hypothesis until independently assessed.
