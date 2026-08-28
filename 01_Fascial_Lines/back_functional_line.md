---
id: back_functional_line
type: Fascial Line
preferred_name: Back Functional Line
aliases: [BFL, back functional sling]
category: Fascial Line
short_definition: "An Anatomy Trains line connecting latissimus dorsi through the thoracolumbar fascia to contralateral gluteus maximus and vastus lateralis."
evidence_level: 1
evidence:
  - source_id: anatomy_trains_myers_2009
    evidence_level: 1
    supports: "Identifies the Back Functional Line muscular and fascial track."
relationships:
  parent_concepts: [functional_lines]
  child_concepts: []
  related_concepts: [golfer_ground_interaction_model, ground_reaction_force, moment_arm, center_of_mass, force_transmission]
  stable_anatomy: [latissimus_dorsi, gluteus_maximus, vastus_lateralis, thoracolumbar_fascia, shoulder_joint]
  golf_interpretation: [end_pelvis_rotation_to_top_backswing, golf_swing_transition, max_unweighting_to_impact, impact_to_hands_chest_height]
  app_hypotheses: [functional_line_loading_index]
confidence: high
review_status: active_spec
relationship_count: 17
hub_score: 49
centrality: 0.293
updated: 2026-07-16
---

# Back Functional Line

## Definition

The Back Functional Line is a posterior diagonal Anatomy Trains pathway from one upper limb across the posterior trunk to the contralateral pelvis and lower limb.

## Why It Matters

It supplies an anatomical route for reasoning between the hip/sacral region, posterior trunk, and contralateral shoulder without treating that route as a direct kinetic finding.

## Stable Anatomy (Level 1 & 2)

The line tracks shaft of humerus -> [[latissimus_dorsi]] -> [[thoracolumbar_fascia]] crossing the sacral region -> contralateral [[gluteus_maximus]] -> vastus lateralis -> patella and tibial tuberosity. This structural membership does not establish loading, activation, or stored energy in a swing.

## Golf Application Interpretation (Level 3 & 4 context)

Kwon describes the external mechanics; the following line mapping is the vault's Anatomy Trains-based golf interpretation.

The explicit bridge is hip/sacrum -> [[thoracolumbar_fascia]] -> [[back_functional_line]] -> [[latissimus_dorsi]] -> rib cage/scapula/[[shoulder_joint]]. A GRF moment about COM must traverse [[ground_reaction_force]], [[moment_arm]], [[center_of_mass]], and [[golfer_ground_interaction_model]]; it is not direct/residual [[ground_reaction_moment|GRM]] at COP.

| Swing phase | External/mechanical context | Anatomical bridge | Line role | Evidence boundary |
|---|---|---|---|---|
| [[end_pelvis_rotation_to_top_backswing]] | EPR and TB support timing comparison, not a universal force direction. | Hip/sacrum -> thoracolumbar fascia -> contralateral latissimus | loading | Line role is interpreted; tissue tension and energy storage are unknown. |
| [[golf_swing_transition]] | Instrumented GRF and moment data may be analysed over declared bounds. | Gluteal/sacral region -> thoracolumbar fascia -> shoulder girdle | stabilising | Kwon does not establish BFL loading or muscle activation. |
| [[max_unweighting_to_impact]] | BI can anchor timing; ordinary video supplies no kinetics. | Posterior trunk bridge -> rib cage/scapula/shoulder | releasing/decelerating | Deceleration role is a vault interpretation, not measured tissue release. |
| [[impact_to_hands_chest_height]] | External post-impact impulse requires compatible sensors. | Shoulder girdle -> posterior trunk -> pelvis | releasing/decelerating | No quantified elastic-energy claim is supported. |

## App Hypotheses (Level 5)

The lead-hip-to-trail-shoulder distance may be reported only as a **camera-derived diagonal-distance descriptor; tissue loading remains unknown**. Its timing relative to pelvis and thorax orientation may support a Level 5 sequence hypothesis, but it cannot measure BFL stretch, activation, force, energy, or kinetic transfer and cannot diagnose a sequence block.

## Gait Role (Engine Synthesis, Level C)

See [[gait_myofascial_mapping]] for the full synthesis. Summary for this line:

- **Phase role:** Posterior pelvic sling — gluteus maximus → thoracolumbar fascia → contralateral latissimus. Brakes hip flexion and internal rotation at heel strike. This is the "Swingwalker" mechanism (Zorn) and the posterior sling (Vleeming). Active at [[initial_contact]] and [[loading_response]].
- **Restriction pattern:** Short BFL → restricted hip flexion/IR deceleration at heel strike, limited contralateral shoulder–hip diagonal coupling.
- **Compensation signature when restricted:** reduced posterior sling braking, forward trunk lean, over-reliance on [[spiral_line]] anterior portion and [[superficial_back_line]].
- **Best observed from:** **back view** (the posterior diagonal sling — glute max → thoracolumbar fascia → contralateral lat — is literally on the back and only visible from behind). Side and front views are blind to the BFL diagonal.

All mappings are `engine_synthesis` (C); not measured kinetics or causal proof. The **phase role** is directly supported by the source (Myers/Earls Ch.10 line gait roles); the **restriction pattern** and **compensation signature** are engine synthesis from line anatomy + fascial-reciprocal logic, not enumerated in the source. See [[gait_myofascial_mapping]] Evidence boundary.

## Squat Role (Engine Synthesis, Level 5)

In loaded barbell squats and single-leg squats, the [[back_functional_line]] (BFL) forms the primary posterior diagonal sling connecting [[latissimus_dorsi]] across the [[thoracolumbar_fascia]] to the contralateral [[gluteus_maximus]]. It stabilizes the barbell across the upper back while transferring rotational torque to the opposite hip extensor.

See [[squat_switch_failure_modes]] and [[squat_myofascial_mapping]] for evidence boundaries.

### BFL Dynamic Switches & Misalignment Matrix

| Misalignment Pattern | Bony Station | Associated Switch Failure Mode | Express vs. Local Dynamics | Retest Protocol |
|---|---|---|---|---|
| **Pelvic Rotation / Asymmetrical Ascent** | Thoracolumbar Fascia / Sacrum | Cross-Torso Sling Switch Failure | Latissimus Dorsi & Contralateral Gluteus Maximus (Express BFL) fail to synchronize torque across sacrum. | Retest with symmetrical barbell placement and single-leg hip extension assessment. |
| **Trunk Rotation under Load** | Spine of Scapula / Contralateral ASIS | Diagonal Rotational Sling Imbalance | BFL diagonal sling over-pulls one shoulder back relative to pelvis during ascent. | Perform seated thoracic rotation test with locked pelvis. |

*This is a candidate assessment hypothesis, not a tissue diagnosis. Camera data describes 2D/3D image-plane orientation and timing; it does not measure fascial tension, force transmission, or muscle activation.*

## Relationships

| Relationship | Target | Description |
|---|---|---|
| part_of | [[functional_lines]] | Posterior diagonal sub-line. |
| contains | [[latissimus_dorsi]], [[thoracolumbar_fascia]], [[gluteus_maximus]] | Stable Anatomy Trains pathway. |
| anatomical_bridge_for | [[golf_swing_transition]] | Phase-specific vault interpretation only. |
| gait_synthesis | [[gait_myofascial_mapping]] | Engine synthesis mapping to gait phases. |

## Open Questions

- Which instrumented study could test the proposed phase roles independently of camera geometry?
