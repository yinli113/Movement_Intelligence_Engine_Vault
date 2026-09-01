# Myofascial Movement Intelligence Vault Index

Welcome to the compounding knowledge engine for the AI-powered Functional Movement Assessment application. The vault is a **cross-domain movement-intelligence engine**: it integrates Thomas Myers' Anatomy Trains myofascial lines and structural anatomy with Dr. Young-Hoo Kwon's golf biomechanics, and with general movement-science, gait, and static-posture sources so the same engine can drive golf, gait, static-posture, squat, and future movement assessments. The app's guiding question is not "What posture do you have?" but "How does your body organize movement?" (see [[czaprowski_nonstructural_posture_2018]]).

The vault uses an evidence-separated reasoning traversal:
$$\text{source/evidence} \rightarrow \text{external mechanics} \rightarrow \text{swing phase/position} \rightarrow \text{joint/connective anatomical bridge} \rightarrow \text{explicitly labelled myofascial-line interpretation} \rightarrow \text{camera-observable descriptor or unavailable kinetic variable} \rightarrow \text{cautious app-report boundary}$$

Each arrow is a navigation step, not proof that one layer establishes the next. Measured or model-derived kinetics require compatible instrumentation; camera observations remain descriptors. [[center_of_mass|COM]] and [[center_of_pressure|COP]] are distinct quantities and must not be substituted for one another.

---

## Start Here for AI Agents

Use the shortest task route that supports the current question. Obsidian links are navigation edges; follow them selectively and preserve the evidence and observability boundaries in each node.

### Static posture and myofascial report

`[[bodyreading_static_posture]]` -> `[[posture_switch_failure_modes]]` -> `[[myofascial_interpretive_layer]]` -> `[[movement_reporting_standards]]` -> the matching finding in `fascial_knowledge.json` -> only the linked fascial-line and body-structure nodes. Check `[[anatomy_trains_myofascial_thomas_w_myers]]` or its cited PDF locator only when a node is incomplete, ambiguous, or requires source verification.

### Gait analysis

`[[gait_cycle]]` -> `[[gait_observability_boundary]]` -> `[[gait_myofascial_mapping]]` -> `[[gait_switch_failure_modes]]` -> the observed phase/restriction node -> linked line and structure nodes. Preserve `unavailable_from_this_view` when the active view cannot support a line interpretation.

### Golf analysis

`[[golf_swing_events]]` -> `[[golf_kinetics_observability_boundary]]` -> `[[golf_myofascial_mapping]]` -> `[[golf_switch_failure_modes]]` -> `golf_knowledge.v1.json` -> the relevant phase -> linked movement, joint, and optional interpretive-line nodes. Do not upgrade 2D proxies into kinetics.

### Bodyweight squat analysis

`[[bodyweight_squat]]` -> `[[squat_observability_boundary]]` -> `[[squat_joint_muscle_mapping]]` -> `[[squat_myofascial_mapping]]` -> `[[squat_switch_failure_modes]]` -> `squat_knowledge.v1.json`. Keep the non-overhead protocol separate from the FMS `[[deep_squat]]`, and present muscles, joints, fascial lines, and switch failure modes as candidate regions or structural hypotheses rather than detected impairments.

### Vault maintenance

Read `[[spec]]`, `[[naming_conventions]]`, and `[[evidence_levels]]`, then update the smallest connected node set and every dependent listed in the workspace `CONSISTENCY_MAP.md`.

**Stopping rule:** Stop when the current observed pattern is supported; do not traverse the whole vault by default. Read source notes or PDF pages for verification, not as the normal first step.

---

## 📂 Vault Directories

### 🛠️ 00. Specifications & Sources (`00_Spec/`)
Authoritative guidelines governing vault schemas, evidence levels, and source data:
- `[[spec]]` - Authoritative project specification.
- `[[naming_conventions]]` - Standard naming and wikilink conventions.
- `[[evidence_levels]]` - The 5-level Evidence Hierarchy.
- **Evidence Sources** (each carries a `domain` field; Levels 1, 2, and 5 are domain-neutral, Levels 3–4 are parameterised by domain — see [[evidence_levels]]):
  - `[[anatomy_trains_myofascial_thomas_w_myers]]` - Primary fascial-line / structural-model evidence source (domain: all).
  - `[[julie_hammond_breakout]]` - Breakout lecture summary on Anatomy Trains and BodyReading (domain: static posture).
  - `[[gray_cook_movement_2010]]` - Functional Movement Screen (FMS) and Selective Functional Movement Assessment (SFMA) framework; the vault's general movement-screening and squat-assessment anchor (domain: general movement / squat).
  - `[[chambers_sutherland_gait_analysis_2002]]` - Peer-reviewed gait-cycle, kinematics, kinetics, and observational-vs-instrumented boundary reference; the gait-domain anchor (domain: gait).
  - `[[perry_burnfield_gait_analysis]]` - Foundational eight-phase gait taxonomy (Level 1, **framework-cited** via Chambers & Sutherland; full text not yet in vault) (domain: gait).
  - `[[czaprowski_nonstructural_posture_2018]]` - Open-access review of the four sagittal posture types and the Bergmark/Richardson stabilizer/mobilizer classification; the vault's static-posture literature and canonical app-philosophy source (domain: static posture).
  - `[[dr_kwon_golfer_ground_interaction]]` - Research-program dossier for Dr Young-Hoo Kwon's golfer-ground interaction mechanics, primary sources, and claim anchors (domain: golf).
  - `[[bourgain_golf_swing_biomechanics_2022]]` - Peer-reviewed systematic review of 92 instrumented golf-swing kinematics studies (X-factor, crunch factor, swing plane, kinematic sequence, joint angular kinematics) with methodological recommendations (domain: golf).
  - `[[golf_decoded_six_phases_swing]]` - Biomechanical 6-phase swing reference (domain: golf).
  - `[[straub_powers_squat_biomechanics_2024]]` - Applied clinical commentary on modifiable squat parameters and relative hip/knee extensor bias (domain: squat).
  - `[[schoenfeld_nsca_squat_biomechanics_2010]]` - NSCA review of squat kinematics, joint moments, and knee-to-toe excursion boundaries (domain: squat).
  - `[[kendall_muscles_testing_function]]` - Gold-standard clinical reference for sagittal/coronal plumb lines, manual muscle testing, and length-tension balance (domain: static posture / general movement).
  - `[[evals]]` - The Medallion Movement Evaluation Architecture (Raw/Bronze/Silver/Gold verification standards).
  - `[[log]]` - Compilation log of vault updates.

### 🗺️ 01. Myofascial Lines (`01_Fascial_Lines/`)
Anatomy Trains lines representing continuous myofascial force-transmission paths:
- `[[functional_lines]]` - The core Functional Lines hub note.
  - `[[back_functional_line]]` | `[[front_functional_line]]` | `[[ipsilateral_functional_line]]`
- `[[superficial_back_line]]` - Posterior postural line and vertical bracing pathway.
- `[[superficial_front_line]]` - Anterior line balancing postural extension.
- `[[lateral_line]]` - Lateral balance and rotational braking line.
- `[[spiral_line]]` - Rotational continuity and transverse plane control.
- `[[deep_front_line]]` - Core support line connecting arch, groin, psoas, and neck.
- `[[myofascial_interpretive_layer]]` - Rules for cautiously associating movement patterns with fascial continuities (never a measured tissue claim).
- **Arm Lines**:
  - `[[superficial_front_arm_line]]` | `[[deep_front_arm_line]]`
  - `[[superficial_back_arm_line]]` | `[[deep_back_arm_line]]`

### 🦴 02. Physical Body Structures (`02_Body_Structures/`)
The physiological segments, muscles, joints, and joint actions of the kinetic chain:
- **Joints**:
  - `[[hip_joint]]` | `[[knee_joint]]` | `[[ankle_joint]]`
  - `[[shoulder_joint]]` | `[[elbow_joint]]` | `[[wrist_joint]]`
  - `[[cervical_spine]]` | `[[thoracic_spine]]` | `[[lumbar_spine]]` | `[[sacrum]]`
- **Connective Structures**:
  - `[[plantar_fascia]]` | `[[thoracolumbar_fascia]]` | `[[sacrotuberous_ligament]]`
  - `[[iliotibial_tract]]` | `[[nuchal_ligament]]`
- **Joint Actions**:
  - `[[hip_internal_rotation]]` | `[[hip_external_rotation]]` | `[[hip_flexion]]` | `[[hip_extension]]` | `[[hip_abduction]]` | `[[hip_adduction]]`
  - `[[thoracic_rotation]]` | `[[trail_shoulder_external_rotation]]`
  - `[[ankle_dorsiflexion]]` | `[[ankle_plantarflexion]]`
  - `[[knee_flexion]]` | `[[knee_extension]]`
  - `[[shoulder_internal_rotation]]` | `[[shoulder_external_rotation]]` | `[[shoulder_abduction]]` | `[[shoulder_adduction]]`
  - `[[elbow_flexion]]`
- **Muscles**:
  - `[[gluteus_maximus]]` | `[[gluteus_medius]]` | `[[gluteus_minimus]]`
  - `[[psoas_major]]` | `[[iliacus]]` | `[[adductor_longus]]` | `[[adductor_magnus]]` | `[[adductor_brevis]]` | `[[gracilis]]` | `[[pectineus]]`
  - `[[latissimus_dorsi]]` | `[[pectoralis_major]]` | `[[pectoralis_minor]]`
  - `[[rectus_abdominis]]` | `[[transversus_abdominis]]` | `[[external_oblique]]` | `[[internal_oblique]]`
  - `[[quadratus_lumborum]]` | `[[diaphragm]]`
  - `[[biceps_femoris_long_head]]` | `[[biceps_femoris_short_head]]` | `[[semitendinosus]]` | `[[semimembranosus]]`
  - `[[rectus_femoris]]` | `[[sartorius]]` | `[[tensor_fasciae_latae]]`
  - `[[gastrocnemius]]` | `[[soleus]]` | `[[tibialis_anterior]]` | `[[tibialis_posterior]]`
  - `[[flexor_hallucis_longus]]` | `[[flexor_digitorum_longus]]` | `[[flexor_digitorum_brevis]]`
  - `[[extensor_hallucis_longus]]` | `[[extensor_digitorum_longus]]`
  - `[[peroneus_longus]]` | `[[peroneus_brevis]]` | `[[popliteus]]`
  - `[[sternocleidomastoid]]` | `[[scalenes]]` | `[[splenius_capitis]]` | `[[trapezius]]` | `[[rhomboids]]` | `[[serratus_anterior]]`
  - `[[deltoid]]` | `[[biceps_brachii]]` | `[[triceps_brachii]]` | `[[supraspinatus]]` | `[[infraspinatus]]` | `[[subscapularis]]` | `[[teres_minor]]`

### ⚙️ 03. Movement Biomechanics (`03_Movement_Functions/`)
Rotational forces, physics vectors, and transmission dynamics:
- `[[movement_chain_model]]` - The central force flow model.
- `[[golfer_ground_interaction_model]]` - The central golfer-ground interaction model and three-class external-moment taxonomy.
- `[[gait_myofascial_mapping]]` - **Engine synthesis** mapping Anatomy Trains lines to gait phases, motion-restriction patterns, and compensation signatures (built from Earls/Myers "Anatomy Trains in Gait", Ch.10). Closes the gait-observation → fascial-line graph edge so the movement_assessment app can reason from observed gait restrictions to candidate lines. All mappings are `engine_synthesis` (C), not measured kinetics.
- `[[bodyweight_squat]]` - Canonical non-overhead unloaded squat movement and V1 app protocol.
- `[[sagittal_plumb_line_alignment]]` - Toes · Mid-Foot · Heel 3-line reference rules and center-of-mass trajectory.
- `[[coronal_plumb_line_alignment]]` - Midline gravitational axis and bilateral stance envelope.
- `[[knee_to_toe_progression_boundary]]` - Kinetic moment trade-offs and forward tibial excursion limits.
- `[[length_tension_postural_relationship]]` - Agonist-antagonist tone balance, MMT retest paths, and non-diagnostic observational hypotheses.
- `[[squat_joint_muscle_mapping]]` - Metric-to-joint and candidate muscle-region mapping with competing explanations.
- `[[squat_myofascial_mapping]]` - Explicit Level 5 engine synthesis for optional squat fascial-line hypotheses.
- `[[squat_cross_view_synthesis]]` - Rules for combining independent side/front squat recordings without false synchronization.
- `[[ground_reaction_force]]` - Net vertical and shear ground forces.
- `[[ground_reaction_moment]]` - The direct/residual GRM represented at COP, distinct from a GRF moment about COM.
- `[[pivoting_moment]]` - The vertical-axis moment from individual-foot GRFs about combined COP.
- `[[foot_contact_moment]]` - The direct torsional contact-moment class underlain by GRM at each foot COP.
- `[[linear_impulse]]` - The time integral of net external force and change in linear momentum.
- `[[angular_impulse]]` - The time integral of net external moment about COM and change in angular momentum.
- `[[torque]]` - A moment of force about a selected axis or centre.
- `[[moment_arm]]` - The perpendicular distance from the selected axis or centre to a force line of action; it is not inherently a horizontal COM–COP separation.
- `[[center_of_mass]]` - The mass-weighted mean position of the defined body system.
- `[[center_of_pressure]]` - The point of application of the resultant ground-reaction force.
- `[[angular_momentum]]` - Conservation and rotational velocity values.
- `[[kinematic_sequence]]` - segment coordination timing (Pelvis → Thorax → Lead Arm).
- `[[force_transmission]]` - General vector transfer.
- `[[energy_transfer]]` - General kinetic energy transfer.
- **Temporal & Individual Analysis (2026-07-27)**:
  - `[[temporal_movement_metrics]]` - Metrics interpreted across time: event values, extrema and their timing, rates, sequence, phase transitions, and trial consistency.
  - `[[stretch_shortening_cycle]]` - Eccentric preparation → coupling → concentric release; whether a movement creates, stores, and releases elastic behaviour smoothly.
  - `[[energy_flow]]` - Operational definition: coordinated transfer of motion through the body over time, assessed only via measurable proxies.
  - `[[segment_angle_metrics]]` - Segment orientation relative to the ground/base of support (shank, thigh, pelvis line, trunk axis, lead-side support line).
  - `[[personalised_movement_intelligence]]` - Individual baseline, trial consistency, and personal best pattern over population comparison.
- **Motor Control & Compensations**:
  - `[[toe_loading]]` - Great toe pressure pattern.
  - `[[neck_tension]]` - head-neck bracing compensation.
  - `[[jaw_clenching]]` - temporomandibular bracing response.
  - `[[bodyreading_static_posture]]` - Standing posture balance.

### 🏌️ 04. Golf Swing Analysis (`04_Golf_Swing/`)
Golf-specific movement patterns and swing interval segmentation:
- `[[golf_swing]]` - Rotational movement pattern overview.
- `[[golf_swing_transition]]` - Lower-to-upper body transition sequence.
- `[[golf_swing_events]]` - Declared event set and normalised swing time; maxima are not pinned to conventional events.
- `[[x_factor]]` - Pelvis-thorax rotational dissociation as a time-varying curve, including transition X-factor stretch.
- `[[golf_movement_sequence]]` - Full observable sequence from feet/ankles through pelvis, thorax, and upper limbs to the head.
- **Swing Phases**:
  - `[[address_to_shaft_parallel]]` - Phase 1
  - `[[shaft_parallel_to_end_pelvis_rotation]]` - Phase 2
  - `[[end_pelvis_rotation_to_top_backswing]]` - Phase 3
  - `[[golf_swing_transition]]` - Phase 4 (Transition)
  - `[[max_unweighting_to_impact]]` - Phase 5
  - `[[impact_to_hands_chest_height]]` - Phase 6
- **Swing Positions**:
  - `[[address_position]]` | `[[shaft_parallel_position]]` | `[[end_pelvis_rotation]]` | `[[top_backswing_position]]` | `[[max_unweighting]]` | `[[impact_position]]` | `[[hands_chest_height_position]]`

### 🤖 05. AI Application Logic (`05_App_Logic/`)
Scoring metrics, assessments, and remedial exercises:
- `[[golf_kinetics_observability_boundary]]` - Authoritative boundary between instrumented kinetics, camera-observable descriptors, and Level 5 hypotheses.
- `[[metric_evidence_classification]]` - Every metric declares its claim type, source, view/landmark needs, confidence limits, and dimensionality validity.
- `[[movement_reporting_standards]]` - Non-judgmental reporting vocabulary and the seven-question report structure.
- `[[squat_observability_boundary]]` - Side/front camera allow-list and prohibited squat inferences.
- `[[squat_cross_view_synthesis]]` - Cross-view relationship types, quality gates, themes, and non-upgrade rules.
- `[[ai_movement_analysis_layer]]` - Historical record of TGS, CCS, FLLI, and ETE—retired, unvalidated historical Level 5 concepts controlled by [[golf_kinetics_observability_boundary]], not a current metrics framework:
  - **Torque Generation Score (TGS)** — retired and unvalidated.
  - **COM-COP Separation Score (CCS)** — retired and unvalidated.
  - **Functional Line Loading Index (FLLI)** — retired and unvalidated.
  - **Energy Transmission Efficiency (ETE)** — retired and unvalidated.
- **Assessments**:
  - `[[glute_max_tests]]` - Strength and length test protocols.
- **Interventions**:
  - `[[glute_max_releases]]` - releases and rolling.
  - `[[glute_max_activations]]` - activation bridges and sling drills.
