---
id: lateral_line
type: Fascial Line
preferred_name: Lateral Line
aliases: [LL, lateral fascial line]
category: Fascial Line
short_definition: "An Anatomy Trains line describing a lateral pathway from the foot through the lateral leg, pelvis, ribs, and neck."
evidence_level: 1
evidence:
  - source_id: anatomy_trains_myers_2009
    source_type: textbook_pdf
    evidence_level: 1
    locator: "Chapter 5, Lateral Line; extracted local PDF pages 130-132"
    supports: "Describes lateral continuity through fibularii/peroneals, lateral knee tissues, iliotibial tract, obliques, intercostals, and neck structures."
  - source_id: julie_hammond_breakout
    source_type: source_summary
    evidence_level: 1
    locator: "Key Lines Explored; Lateral Line"
    supports: "Summarises Lateral Line structural balance roles."
relationships:
  contains: [peroneus_longus, peroneus_brevis, iliotibial_tract, tensor_fasciae_latae, gluteus_maximus, gluteus_medius, external_oblique, internal_oblique, intercostals, splenius_capitis, sternocleidomastoid]
  connects_to: [plantar_fascia, ankle_joint, knee_joint, hip_joint, lumbar_spine, thoracic_spine, cervical_spine]
  related_concepts: [golfer_ground_interaction_model, ground_reaction_force, moment_arm, center_of_mass]
  golf_interpretation: [address_to_shaft_parallel, shaft_parallel_to_end_pelvis_rotation, golf_swing_transition, max_unweighting_to_impact]
  app_hypotheses: [planned_lateral_shift_rotation_screen]
confidence: medium
review_status: draft_graph_mvp
relationship_count: 41
hub_score: 118
centrality: 0.707
updated: 2026-07-16
---

# Lateral Line

## Definition

The Lateral Line is an Anatomy Trains model of continuity along the outer foot and leg, lateral pelvis, abdominal wall, ribs, and neck.

## Why It Matters

It provides a stable route for interpreting side-to-side organisation while avoiding causal claims from a visible sway or side-bend pattern.

## Stable Anatomy (Level 1 & 2)

The cited pathway includes [[peroneus_longus]] and peroneus brevis, lateral knee tissues, iliotibial tract and tensor fasciae latae, gluteal region, abdominal obliques, intercostals, and lateral neck structures. Structural membership does not establish a golf-phase braking or stabilising action.

## Golf Application Interpretation (Level 3 & 4 context)

Kwon describes the external mechanics; the following line mapping is the vault's Anatomy Trains-based golf interpretation.

The lower traversal is foot/ankle -> [[plantar_fascia]]/deep leg -> [[lateral_line]] through the fibularii/peroneals -> lateral hip/pelvis -> rib cage. Plantar fascia is an entry bridge in the vault graph, not direct Lateral Line membership. External mechanics may contextualise this route but do not identify tissue loading.

| Swing phase | External/mechanical context | Anatomical bridge | Line role | Evidence boundary |
|---|---|---|---|---|
| [[address_to_shaft_parallel]] | No phase-specific kinetic direction is assigned. | Foot/ankle -> lateral leg -> pelvis/ribs | stabilising | Line role is interpretive; pressure and tension are unknown. |
| [[shaft_parallel_to_end_pelvis_rotation]] | GRF moment about COM requires measured force and 3-D geometry. | Lateral foot/leg -> hip/pelvis -> oblique trunk | stabilising | Kwon does not establish Lateral Line loading. |
| [[golf_swing_transition]] | External kinetics require compatible instruments. | Foot/ankle -> lateral hip -> rib cage | loading | Tissue loading and activation remain unknown. |
| [[max_unweighting_to_impact]] | BI supplies a timing anchor only. | Lateral pelvis/trunk pathway | releasing/decelerating | Deceleration role is not a direct tissue measure. |

## App Hypotheses (Level 5)

Camera-derived observations may include pelvis translation, trunk side bend, foot orientation, and phase timing. They cannot measure COP, pressure, force, moments, muscle activation, fascial tension, Lateral Line loading, or energy storage, transfer, release, or dissipation. A lateral-shift descriptor must not be reported as proof of tissue weakness, restriction, or pain source.

## Gait Role (Engine Synthesis, Level C)

See [[gait_myofascial_mapping]] for the full synthesis. Summary for this line:

- **Phase role:** Frontal-plane stability. Prevents the weighted hip from falling inward (adduction). Has the most range to travel and the most adjustment work in gait. The X-fibre pattern of the lateral obliques controls the rotational relationship between pelvis and rib cage. Active throughout stance, especially managing pelvic tilt/shift.
- **Restriction pattern:** Short LL → restricted **hip internal rotation** (in gait, with ITB tightness), restricted frontal-plane pelvic control. Often co-occurs with foot over-pronation.
- **Compensation signature when restricted:** Trendelenburg sign, lateral trunk lean over the stance leg — compensating via [[spiral_line]] (rotational) and [[deep_front_line]] (core brace).
- **Best observed from:** **front + back views** (frontal-plane pelvic level and lateral trunk lean are visible from both; side view is blind to LL frontal-plane findings). Back view adds glute med / TFL / ITB asymmetry.
- **Spine in gait:** LL crosses the thoracic spine via intercostals/lateral obliques and the lumbar spine via lateral obliques. Restricted **thoracic lateral flexion** (asymmetric shoulder height) and restricted **lumbar rotation** (LL obliques, pelvis and shoulders rotate together) are LL restriction patterns. The LL X-fibre pattern controls the rotational relationship between pelvis and rib cage in gait. See [[gait_myofascial_mapping]].

All mappings are `engine_synthesis` (C); not measured kinetics or causal proof. The **phase role** is directly supported by the source (Myers/Earls Ch.10 line gait roles); the **restriction pattern** and **compensation signature** are engine synthesis from line anatomy + fascial-reciprocal logic, not enumerated in the source. The **spine in gait** patterns are independent local-segment patterns from line anatomy — the source supports elastic-recoil propagation, not spine-to-spine ROM propagation. See [[gait_myofascial_mapping]] Evidence boundary.

## Relationships

- contains -> [[peroneus_longus]], [[iliotibial_tract]], [[gluteus_medius]], [[external_oblique]], [[intercostals]]
- connects_to -> [[ankle_joint]], [[hip_joint]], rib cage
- interpreted_during -> [[golf_swing_transition]]
- gait_synthesis -> [[gait_myofascial_mapping]]
- supported_by -> [[anatomy_trains_myofascial_thomas_w_myers]], [[julie_hammond_breakout]]

## Open Questions

- How should camera view alter confidence in pelvis-translation and side-bend descriptors?
