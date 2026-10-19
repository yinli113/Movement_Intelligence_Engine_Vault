---
id: running_functional_lines
canonical_id: running.myofascial.functional_lines
type: App Logic
running_node_type: myofascial_hypothesis
evidence_level: 5
running_claim_level: D
status: canonical
preferred_name: "Running - Functional Lines (Outer System)"
aliases: [Functional Lines Running, Outer Rotational System, Back Functional Line Running, Front Functional Line Running]
domain: running
directly_measured: false
camera_views: []
requires_clinical_correlation: true
confidence_required: contextual
related_nodes: []
source_nodes: [myers_three_rotational_systems_2024, anatomy_trains_myofascial_thomas_w_myers]
relationships:
  required_inputs: [running_arm_leg_coordination, running_cross_body_coordination, running_altered_rotational_coordination, running_shoulder_rotation, running_rotational_reversal]
  related_concepts: [running_three_layer_rotation_model, running_cross_body_myofascial_hypothesis, running_evidence_gate, running_reporting_guardrails, functional_lines, back_functional_line, front_functional_line]
confidence: medium
review_status: canonical_hypothesis
relationship_count: 14
hub_score: 22
centrality: 0.11
updated: 2026-10-15
---

# Running - Functional Lines (Outer System)

## Definition

A Level D myofascial hypothesis node representing the superficial cross-body power transmission slings (Back Functional Line and Front Functional Line) that couple contralateral arm swing to trailing lower limb propulsion during running.

## Anatomical Continuity (Outer System)

```
[Contralateral Arm Swing / Shoulder Drive]
                   │
                   ▼
       [[latissimus_dorsi]] (BFL)  /  [[pectoralis_major]] (FFL)
                   │
                   ▼
       [[thoracolumbar_fascia]] (BFL)  /  [[rectus_sheath]] (FFL)
                   │
                   ▼
       [[gluteus_maximus]] (BFL)  /  [[adductor_longus]] (FFL)
                   │
                   ▼ (Full Limb Propulsion Continuation)
       [[vastus_lateralis]]
                   │
                   ▼
       [[patellar_ligament]] & Tibial Tuberosity
```

- **Back Functional Line (BFL)**: Connects [[latissimus_dorsi]] across the [[thoracolumbar_fascia]] to the contralateral [[gluteus_maximus]], continuing down the lateral thigh via the **[[vastus_lateralis]] to the [[patellar_ligament]] and tibial tuberosity**.
- **Front Functional Line (FFL)**: Connects lower [[pectoralis_major]] across the sternum and [[rectus_sheath]] / [[rectus_abdominis]] to the contralateral pubic tubercle and [[adductor_longus]].

## Role in Running Locomotion

1. **Contralateral Propulsion and Flight Drive**:
   - Operates dynamically during late stance and toe-off to harness elastic momentum between the swinging arm and the driving opposite leg.
   - Contralateral arm backward drive tightens the Back Functional Line, assisting explosive hip extension, trailing knee extension, and push-off drive.
2. **Scissor Angle Generation**:
   - Coordinates the simultaneous explosive hip extension of the trailing stance leg with contralateral hip flexion of the leading swing leg.

## Kinematic Observables and Measurable Proxies

- Contralateral arm-leg phase timing and synchrony ([[running_arm_leg_coordination]]).
- Trailing knee extension angle at toe-off (smooth extension to ~160°–168°).
- Inter-thigh scissor angle at toe-off.
- Upper-arm humeral backward excursion relative to trunk.

## Asymmetry Hypothesis Guidance

- If contralateral arm-to-leg timing or push-off knee extension angle differs significantly between `LEFT_STANCE` and `RIGHT_STANCE`:
  - Investigate contralateral force transmission and upper-lower body coordination across the Functional Lines.
  - Testable hypothesis: Asymmetric arm swing drive may reflect unequal push-off momentum from the opposite leg rather than local shoulder stiffness.

## Limitations and Evidence Boundaries

- Functional lines are conceptual anatomic models; monocular 2D camera video cannot measure fascial tensile stress in Pascals, load transfer, or muscle firing.
- Do not claim that "Functional Lines are tight" or "BFL force transmission is 30% reduced."

## Reporting Language

- *Permitted*: "Observed contralateral arm-leg timing asymmetry supports a candidate Functional Lines coordination hypothesis, which may warrant clinical/coaching correlation."
- *Forbidden*: "Functional Line failure diagnosed."

## Review Status

`canonical_hypothesis`. Updated with full limb vastus lateralis continuation.
