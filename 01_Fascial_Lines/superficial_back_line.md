---
id: superficial_back_line
type: Fascial Line
preferred_name: Superficial Back Line
aliases: [SBL, posterior chain, superficial posterior fascial line]
category: Fascial Line
short_definition: "An Anatomy Trains line describing posterior continuity from the plantar foot through the calves, hamstrings, spinal extensors, and scalp region."
evidence_level: 1
evidence:
  - source_id: anatomy_trains_myers_2009
    source_type: textbook_pdf
    evidence_level: 1
    locator: "Chapter 3, Superficial Back Line; extracted local PDF page 104"
    supports: "Describes posterior line structure and movement considerations."
relationships:
  contains: [plantar_fascia, gastrocnemius, soleus, biceps_femoris_long_head, sacrotuberous_ligament, semitendinosus, semimembranosus, spinalis, longissimus, iliocostalis, nuchal_ligament, occipitofrontalis]
  connects_to: [ankle_joint, knee_joint, hip_joint, lumbar_spine, thoracic_spine, cervical_spine, plantar_fascia, sacrotuberous_ligament, nuchal_ligament]
  related_concepts: [golfer_ground_interaction_model, ground_reaction_force, moment_arm, center_of_mass]
  golf_interpretation: [address_to_shaft_parallel, end_pelvis_rotation_to_top_backswing, golf_swing_transition, impact_to_hands_chest_height]
  app_hypotheses: [planned_posterior_chain_load_screen]
confidence: medium
review_status: draft_graph_mvp
relationship_count: 42
hub_score: 125
centrality: 0.724
updated: 2026-07-16
---

# Superficial Back Line

## Definition

The Superficial Back Line is an Anatomy Trains model of posterior continuity from plantar foot structures through the calf, posterior thigh, sacral connection, spinal extensors, and head.

## Why It Matters

It provides a posterior anatomical bridge from foot/ankle toward the pelvis and trunk while keeping posture and camera appearance separate from tissue state.

## Stable Anatomy (Level 1 & 2)

The cited pathway includes [[plantar_fascia]], [[gastrocnemius]], [[soleus]], hamstrings, [[sacrotuberous_ligament]], spinal extensors, [[nuchal_ligament]], and scalp structures. Line membership does not establish posterior-chain load, activation, or energy storage during golf.

## Golf Application Interpretation (Level 3 & 4 context)

Kwon describes the external mechanics; the following line mapping is the vault's Anatomy Trains-based golf interpretation.

The explicit route is foot/ankle -> [[plantar_fascia]]/deep leg -> [[superficial_back_line]] -> calf/hamstrings -> sacrum -> spinal extensors. External forces and moments may contextualise the swing phase but do not prove load travelling through this route.

| Swing phase | External/mechanical context | Anatomical bridge | Line role | Evidence boundary |
|---|---|---|---|---|
| [[address_to_shaft_parallel]] | No phase-specific force direction is assigned. | Foot/ankle -> plantar fascia -> calf/posterior thigh | stabilising | Role is a vault interpretation; loading is unknown. |
| [[end_pelvis_rotation_to_top_backswing]] | EPR and TB provide timing anchors. | Posterior thigh/sacrum -> spinal extensors | loading | No direct measure of fascial stretch or energy storage. |
| [[golf_swing_transition]] | Instrumented kinetics may contextualise transition. | Plantar foot -> posterior leg -> sacrum/trunk | stabilising | Kwon does not establish SBL loading. |
| [[impact_to_hands_chest_height]] | Post-impact impulse requires measured force/moment and event bounds. | Posterior trunk and lower-limb route | releasing/decelerating | Deceleration role remains interpretive. |

## App Hypotheses (Level 5)

Camera data may describe ankle, knee, hip, trunk, and head landmarks plus phase timing. It cannot measure foot pressure, GRF, moments, muscle activation, fascial tension, SBL loading, or energy. Co-occurring foot, spinal, neck, or jaw descriptors must not be interpreted as a diagnosis or single tissue cause.

## Gait Role (Engine Synthesis, Level C)

See [[gait_myofascial_mapping]] for the full synthesis. Summary for this line:

- **Phase role:** Drives stance — hip extension + plantarflexion from heel strike through foot roll-over. Plantarflexors of the SBL **plus LL and DFL** load the "catapult" for toe-off (Earls — catapult is multi-line, not SBL-only). Active across [[loading_response]], [[mid_stance]], [[terminal_stance]], and [[preswing]].
- **Restriction pattern:** Short SBL → restricted **knee extension** (SBL crosses posterior knee via hamstrings/gastrocnemius), restricted **hip flexion**, restricted **ankle dorsiflexion** (gastroc/soleus must lengthen).
- **Compensation signature when restricted:** flat-footed push-off, forward lean, reduced propulsion — compensating via [[deep_front_line]] (psoas over-pull), [[superficial_front_line]] (anterior drag).
- **Best observed from:** **side view** (hip extension, plantarflexion, heel rise, toe-off, and the four foot rockers are sagittal-plane findings). Back view adds calf/hamstring symmetry; front view is largely blind to SBL sagittal mechanics.
- **Spine in gait:** SBL crosses the cervical spine via nuchal ligament/suboccipitals and the thoracic/lumbar spine via erector spinae. Three **independent** SBL restriction patterns (each caused by SBL shortness at that segment's point on the line, not by one causing the other): (1) restricted **neck flexion** (can't tuck the chin, SBL posterior neck tightness at the cervical point); (2) restricted **thoracic flexion** (SBL erector spinae crosses the posterior thoracic spine; short SBL resists thoracic flexion, holding the thorax extended — NOT restricted thoracic extension, which is an SFL/DFL pattern); (3) restricted **lumbar flexion** (stuck in extension, SBL lumbar erector spinae tightness at the lumbar point). These are local-segment patterns from SBL anatomy; the source does not establish SBL transmits ROM restrictions segment-to-segment. See [[gait_myofascial_mapping]] Whole-chain insight for the evidence boundary.

All mappings are `engine_synthesis` (C); not measured kinetics or causal proof. The **phase role** is directly supported by the source (Myers/Earls Ch.10 line gait roles); the **restriction pattern** and **compensation signature** are engine synthesis from line anatomy + fascial-reciprocal logic, not enumerated in the source. The **spine in gait** patterns are independent local-segment patterns from line anatomy — the source supports elastic-recoil propagation, not spine-to-spine ROM propagation. See [[gait_myofascial_mapping]] Evidence boundary.

## Relationships

- contains -> [[plantar_fascia]], [[gastrocnemius]], [[soleus]], [[sacrotuberous_ligament]], [[nuchal_ligament]]
- connects_to -> [[ankle_joint]], [[hip_joint]], [[thoracic_spine]]
- interpreted_during -> [[golf_swing_transition]]
- gait_synthesis -> [[gait_myofascial_mapping]]
- supported_by -> [[anatomy_trains_myofascial_thomas_w_myers]]

## Open Questions

- Which pose descriptors can be validated against instrumented posterior-chain measures without causal overreach?
