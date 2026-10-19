---
id: running_spiral_line
canonical_id: running.myofascial.spiral_line
type: App Logic
running_node_type: myofascial_hypothesis
evidence_level: 5
running_claim_level: D
status: canonical
preferred_name: "Running - Spiral Line (Middle System)"
aliases: [Spiral Line Running, Middle Rotational System, Helical Postural Wrapper, Lateral Elastic Spring]
domain: running
directly_measured: false
camera_views: []
requires_clinical_correlation: true
confidence_required: contextual
related_nodes: []
source_nodes: [myers_three_rotational_systems_2024, anatomy_trains_myofascial_thomas_w_myers, gruenke_kiptum_running_analysis_2023]
relationships:
  required_inputs: [running_pelvis_thorax_rotation, running_rotational_coupling, running_altered_rotational_coordination, running_pelvis_rotation, running_shoulder_rotation]
  related_concepts: [running_three_layer_rotation_model, running_cross_body_myofascial_hypothesis, running_head_trunk_pelvis_coordination, running_evidence_gate, running_reporting_guardrails, spiral_line]
confidence: medium
review_status: canonical_hypothesis
relationship_count: 16
hub_score: 26
centrality: 0.13
updated: 2026-10-15
---

# Running - Spiral Line (Middle System)

## Definition

A Level D myofascial hypothesis node representing the double-spiral helical continuity linking the cranium, trunk obliques, pelvis, lateral thigh, and plantar foot stirrup during running.

## Anatomical Continuity (Middle System)

```
                       [[splenius_capitis]] & Occiput
                                     │
                                     ▼
                               [[rhomboids]]
                                     │
                                     ▼
                            [[serratus_anterior]]
                                     │
                                     ▼
                            [[external_oblique]]
                                     │
                                     ▼
                    Contralateral [[internal_oblique]]
                                     │
                                     ▼
                           Pelvis (ASIS Landmark)
                                     │
                                     ▼ (Lateral Thigh & Leg)
                   [[tensor_fasciae_latae]] (TFL) & [[iliotibial_tract]] (ITB)
                                     │
                                     ▼
                           [[tibialis_anterior]]
                                     │
                                     ▼ (Plantar Stirrup Sling)
                            [[peroneus_longus]]
                                     │
                                     ▼
                      [[biceps_femoris_long_head]]
                                     │
                                     ▼
                              Ischial Tuberosity
                                     │
                                     ▼
                         [[sacrotuberous_ligament]]
                                     │
                                     ▼
            [[iliocostalis]] / [[longissimus]] / [[spinalis]]
                                     │
                                     ▼
                              Back to Cranium
```

## Role in Running Locomotion

1. **Thoraco-Pelvic Rotational Dissociation**:
   - Mediates the continuous counter-rotation and phase lag between the shoulder girdle and the pelvis ([[running_pelvis_thorax_rotation]]).
   - Stores rotational strain energy in the abdominal obliques and erector spinae during midstance winding, assisting directional reversal.
2. **The Lateral Elastic Spring Recoil**:
   - As documented in world-record marathon running ([[gruenke_kiptum_running_analysis_2023]]), stance-side hip elevation paired with shoulder tipping creates an opposing lateral shift of the midsection toward the swing leg.
   - This prestretches the stance-side [[tensor_fasciae_latae]], [[iliotibial_tract]], and abdominal obliques.
   - Rather than active concentric muscular contraction ("muscling it"), the prestretched Spiral Line executes dynamic elastic recoil, snapping back to propel the body forward and upward into flight.
3. **Plantar Stirrup and Knee Tracking**:
   - The sling created under the foot between [[tibialis_anterior]] and [[peroneus_longus]] dynamically regulates foot pronation/supination and maintains knee tracking alignment under stance compression.

## Kinematic Observables and Measurable Proxies

- Simultaneous shoulder-line tilt and pelvic-line tilt curves (`running.frontal.shoulder_tilt`, `running.frontal.pelvis_tilt`).
- Shoulder-pelvis continuous phase lag (`shoulder_pelvis_lag_pct_stride`).
- Ankle-to-knee horizontal landing offset (foot landing underneath flexed knee).
- Midstance shoulder tipping and pelvic excursion.

## Asymmetry Hypothesis Guidance

- If pelvic-line tilt excursion differs significantly between left and right stance (e.g. 14° right vs 9° left) while shoulder excursion is symmetric:
  - Investigate the Middle System (Spiral Line) helical recoil and lateral spring loading.
  - Testable hypothesis: Stance-side hip elevation and shoulder tipping on the right may reflect preferential utilization of the lateral recoil mechanism, or asymmetric thoracic lateral flexion damping.

## Limitations and Evidence Boundaries

- The Spiral Line is a qualitative anatomical model; 2D camera landmarks cannot measure fascial tensile force, elastic strain energy in Joules, or muscle recruitment (EMG).
- Do not claim that "the spiral line is restricted or weak." Always frame as a candidate movement hypothesis requiring clinical correlation.

## Reporting Language

- *Permitted*: "Repeatable thoraco-pelvic dissociation and midstance shoulder tipping support a candidate Middle System (Spiral Line) elastic recoil hypothesis, which may warrant clinical correlation."
- *Forbidden*: "Spiral line dysfunction diagnosed on the right side."

## Review Status

`canonical_hypothesis`. Updated with full lateral leg, peroneal stirrup, and elastic recoil continuity.
