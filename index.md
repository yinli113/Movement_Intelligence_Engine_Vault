# Myofascial Movement Intelligence Vault Index

Welcome to the compounding knowledge engine for the AI-powered Functional Movement Assessment application. This vault integrates Thomas Myers' Anatomy Trains myofascial lines and structural anatomy with Dr. Young-Hoo Kwon's golf biomechanics, foot-ground interaction, forces, and moments.

The vault uses an evidence-separated reasoning traversal:
$$\text{source/evidence} \rightarrow \text{external mechanics} \rightarrow \text{swing phase/position} \rightarrow \text{joint/connective anatomical bridge} \rightarrow \text{explicitly labelled myofascial-line interpretation} \rightarrow \text{camera-observable descriptor or unavailable kinetic variable} \rightarrow \text{cautious app-report boundary}$$

Each arrow is a navigation step, not proof that one layer establishes the next. Measured or model-derived kinetics require compatible instrumentation; camera observations remain descriptors. [[center_of_mass|COM]] and [[center_of_pressure|COP]] are distinct quantities and must not be substituted for one another.

---

## 📂 Vault Directories

### 🛠️ 00. Specifications & Sources (`00_Spec/`)
Authoritative guidelines governing vault schemas, evidence levels, and source data:
- `[[spec]]` - Authoritative project specification.
- `[[naming_conventions]]` - Standard naming and wikilink conventions.
- `[[evidence_levels]]` - The 5-level Evidence Hierarchy.
- **Evidence Sources**:
  - `[[dr_kwon_golfer_ground_interaction]]` - Research-program dossier for Dr Young-Hoo Kwon's golfer-ground interaction mechanics, primary sources, and claim anchors.
  - `[[anatomy_trains_myofascial_thomas_w_myers]]` - Primary fascial-line evidence source.
  - `[[julie_hammond_breakout]]` - Breakout lecture summary on Anatomy Trains and BodyReading.
  - `[[golf_decoded_six_phases_swing]]` - Biomechanical 6-phase swing reference.
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
- **Motor Control & Compensations**:
  - `[[toe_loading]]` - Great toe pressure pattern.
  - `[[neck_tension]]` - head-neck bracing compensation.
  - `[[jaw_clenching]]` - temporomandibular bracing response.
  - `[[bodyreading_static_posture]]` - Standing posture balance.

### 🏌️ 04. Golf Swing Analysis (`04_Golf_Swing/`)
Golf-specific movement patterns and swing interval segmentation:
- `[[golf_swing]]` - Rotational movement pattern overview.
- `[[golf_swing_transition]]` - Lower-to-upper body transition sequence.
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
