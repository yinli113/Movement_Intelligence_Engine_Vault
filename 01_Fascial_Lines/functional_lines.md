---
id: functional_lines
type: Fascial Line
preferred_name: Functional Lines
aliases: [FL, functional line, back functional line, front functional line, ipsilateral functional line, functional slings]
category: Fascial Line
short_definition: "An Anatomy Trains model of cross-body and ipsilateral muscular-fascial connections between the shoulder girdle, trunk, pelvis, and lower limbs."
evidence_level: 1
evidence:
  - source_id: anatomy_trains_myers_2009
    evidence_level: 1
    supports: "Identifies the Back, Front, and Ipsilateral Functional Line pathways and their component structures."
  - source_id: dr_kwon_golfer_ground_interaction
    evidence_level: 3
    supports: "Describes external golfer-ground mechanics; it does not establish fascial-line loading or tissue-specific force transfer."
relationships:
  parent_concepts: [fascial_line_model]
  child_concepts: [back_functional_line, front_functional_line, ipsilateral_functional_line]
  related_concepts: [golfer_ground_interaction_model, ground_reaction_force, ground_reaction_moment, moment_arm, center_of_mass, force_transmission]
  stable_anatomy: [latissimus_dorsi, gluteus_maximus, pectoralis_major, rectus_abdominis, adductor_longus, thoracolumbar_fascia, shoulder_joint]
  golf_interpretation: [end_pelvis_rotation_to_top_backswing, golf_swing_transition, max_unweighting_to_impact, impact_to_hands_chest_height, x_factor]
  app_hypotheses: [functional_line_loading_index]
confidence: high
review_status: active_spec
relationship_count: 59
hub_score: 172
centrality: 1.0
updated: 2026-07-27
---

# Functional Lines

## Definition

The Functional Lines are Anatomy Trains pathways linking the limbs across or along the trunk. The family includes the [[back_functional_line]], [[front_functional_line]], and [[ipsilateral_functional_line]].

## Why It Matters

These lines provide the vault's primary anatomical bridge between measured external mechanics and structures spanning the hip, sacrum, trunk, rib cage, scapula, and shoulder. This bridge is an anatomical interpretation, not a claim that the lines generate, convert, or directly reveal external moments.

## Stable Anatomy (Level 1 & 2)

- [[back_functional_line]]: [[latissimus_dorsi]] -> [[thoracolumbar_fascia]] across the sacral region -> contralateral [[gluteus_maximus]] -> vastus lateralis.
- [[front_functional_line]]: [[pectoralis_major]] -> [[rectus_abdominis|abdominal wall and rectus sheath]] -> contralateral [[adductor_longus]].
- [[ipsilateral_functional_line]]: [[latissimus_dorsi]] -> [[external_oblique]] -> ipsilateral [[sartorius]].

These are Level 1 Anatomy Trains structural continuities. They do not, by themselves, establish tissue loading, muscle activation, energy storage, or a kinetic contribution in a golf swing.

## Golf Application Interpretation (Level 3 & 4 context)

Kwon describes the external mechanics; the following line mapping is the vault's Anatomy Trains-based golf interpretation.

The external-to-anatomical traversal is:

[[ground_reaction_force|measured GRF]] + [[moment_arm]] + [[center_of_mass|COM]] -> GRF moment about COM -> hip/sacrum -> [[thoracolumbar_fascia]] -> [[back_functional_line]] -> rib cage/scapula/[[shoulder_joint]].

Separate traversals are adductors/abdominal wall -> [[front_functional_line]] and ipsilateral trunk/hip linkage -> [[ipsilateral_functional_line]]. At the upper end, rib cage/scapula/[[shoulder_joint|shoulder]] -> relevant Functional and Arm Lines links the trunk model to the upper limb. Direct/residual [[ground_reaction_moment|GRM]] remains a force-plate moment at COP; it is not the GRF moment about COM and is not converted by a fascial line.

| Swing phase | External/mechanical context | Anatomical bridge | Line role | Evidence boundary |
|---|---|---|---|---|
| [[shaft_parallel_to_end_pelvis_rotation]] | EPR can anchor timing; any GRF moment about COM requires measured GRF and 3-D moment-arm geometry. | Hip/sacrum -> [[thoracolumbar_fascia]] and adductors/abdominal wall -> Functional Lines | loading | Level 3 external context; line role is a vault interpretation. |
| [[end_pelvis_rotation_to_top_backswing]] | No universal force or moment direction is assigned to this interval. | Pelvis/trunk -> posterior, anterior, and ipsilateral pathways | loading | Level 1 structure plus Level 3/4 context; tissue state is unknown. |
| [[golf_swing_transition]] | Instrumented forces and moments may be analysed over declared event bounds. | Hip/sacrum and abdominal wall -> Functional Lines -> rib cage/scapula/shoulder | stabilising | Kwon does not establish line loading or muscle activation. |
| [[max_unweighting_to_impact]] | BI is a timing anchor; external kinetics require compatible sensors. | Trunk pathways -> shoulder girdle and relevant Arm Lines | releasing/decelerating | Phase role is interpretive, not a measured energy-release claim. |
| [[impact_to_hands_chest_height]] | Post-impact impulse analysis requires measured force/moment and declared bounds. | Rib cage/scapula/shoulder -> Functional and Arm Lines | releasing/decelerating | Deceleration role and tissue loading remain unmeasured. |

## App Hypotheses (Level 5)

Ordinary video may yield pelvis/thorax orientation, phase timing, and shoulder-to-contralateral-hip diagonal-distance descriptors when landmarks and view permit. A shoulder-to-hip value is a **camera-derived diagonal-distance descriptor; tissue loading remains unknown**. It is not a direct measure of fascial stretch, force, activation, elastic energy, GRF, GRM, COP, or a GRF moment about COM.

Any Functional Line Loading Index must therefore be labelled a Level 5 hypothesis and report view, landmark, and confidence limits. It must not diagnose weakness, restriction, or injury.

## Rotational Dissociation Interpretation (2026-07-27)

For rotational sports such as golf, the Functional Lines — with their contralateral pelvis-trunk-shoulder pathways — are the primary anatomy through which pelvis-thorax dissociation ([[x_factor]]) and the golf [[stretch_shortening_cycle]] are *cautiously* interpreted. A smoothly created, well-timed, smoothly released dissociation **may be consistent with** elastic load sharing along these lines; per [[myofascial_interpretive_layer]] this is always a labelled interpretation, never a measured fascial-force, stiffness, or energy-storage claim.

## Relationships

| Relationship | Target | Description |
|---|---|---|
| contains | [[back_functional_line]] | Posterior contralateral pathway through the thoracolumbar fascia. |
| contains | [[front_functional_line]] | Anterior contralateral pathway through the abdominal wall and adductors. |
| contains | [[ipsilateral_functional_line]] | Same-side trunk-to-hip pathway. |
| interprets | [[golfer_ground_interaction_model]] | Adds a separately labelled anatomical bridge to external mechanics. |
| relevant_to | [[ground_reaction_moment]] | Keeps direct/residual GRM at COP distinct from line interpretation. |

## Open Questions

- Which phase-role assignments can be tested with synchronised motion capture, force plates, and independent tissue measures?
- How reliable are diagonal-distance descriptors across camera views and landmark occlusion?
