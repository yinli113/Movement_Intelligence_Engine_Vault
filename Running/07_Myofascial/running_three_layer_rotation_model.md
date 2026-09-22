---
id: running_three_layer_rotation_model
canonical_id: running.myofascial.three_layer_rotation
type: App Logic
running_node_type: myofascial_hypothesis
evidence_level: 5
running_claim_level: D
status: canonical
preferred_name: Running - Three-Layer Rotational System
aliases: [Myers Three Layer Rotation, Tri-Laminar Rotational Model, Three Tiers of Rotation]
domain: running
directly_measured: false
camera_views: [front, back]
requires_clinical_correlation: true
confidence_required: contextual
related_nodes: [running_deep_front_line, running_spiral_line, running_functional_lines, running_pelvis_thorax_rotation, running_cross_body_coordination, running_rotational_reversal]
source_nodes: [anatomy_trains_myofascial_thomas_w_myers]
relationships:
  required_inputs: [running_pelvis_thorax_rotation, running_cross_body_coordination, running_rotational_reversal]
  contains_hypotheses: [running_deep_front_line, running_spiral_line, running_functional_lines]
  constrained_by: [running_evidence_gate, running_reporting_guardrails, running_kinematics_are_not_kinetics]
confidence: medium
review_status: canonical_hypothesis
relationship_count: 14
hub_score: 28
centrality: 0.165
updated: 2026-09-15
---

# Running - Three-Layer Rotational System

## Definition

A running-domain myofascial hypothesis framework grounded in Thomas Myers' *Anatomy Trains* model, structuring human rotational coordination into three functional anatomical depth layers: Deep Axial Core, Helical Postural Wrapper, and Superficial Dynamic "X".

## Architectural Layers

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ LAYER 3: SUPERFICIAL DYNAMIC "X" — FUNCTIONAL LINES (Front & Back)          │
│ Cross-body power transfer between opposite arm swing and contralateral leg  │
│ (Latissimus ⟷ Contralateral Gluteus Maximus / Pectoralis ⟷ Adductor Longus) │
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ LAYER 2: HELICAL POSTURAL WRAPPER — THE SPIRAL LINE (SPL)                   │
│ Torso-pelvis-lower limb helical recoil and pelvis-thorax dissociation       │
│ (Rhomboid-Serratus ⟷ Obliques ⟷ Pelvis ⟷ ITB/Tibialis ⟷ Biceps Femoris)     │
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ LAYER 1: DEEP AXIAL & HIP ROTATORS — DEEP FRONT LINE (DFL)                  │
│ Segmental spinal stabilization and hip rotational center ("Fans of the Hip")│
│ (Multifidi, Rotatores, Suboccipitals, Obturators, Gemelli, Deep Psoas)      │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Layer 1: The Deep Axial & Hip Rotators (Intrinsic Core Axis / Deep Front Line)
* **Anatomical Basis**: Segmental spinal rotators (*rotatores, multifidi*), suboccipitals, and the deep lateral rotators of the hip (*"fans of the hip"*—obturators, gemelli, piriformis, quadratus femoris, deep psoas). Tied to the [[running_deep_front_line|Deep Front Line]].
* **Role in Running**: Provides micro-rotational stabilization and segmental control. It maintains the vertical structural axis and resists excessive spinal shear forces during high-speed gait.
* **Observable Proxy**: Stable vertical alignment, minimal lateral spinal collapse, and steady pelvic tilt in frontal view.

### Layer 2: The Helical Postural Wrapper (The Spiral Line - SPL)
* **Anatomical Basis**: Double-helix loop connecting the skull $\rightarrow$ rhomboids $\rightarrow$ serratus anterior $\rightarrow$ external oblique $\rightarrow$ contralateral internal oblique $\rightarrow$ pelvis (ASIS) $\rightarrow$ IT band/tibialis anterior $\rightarrow$ arch sling $\rightarrow$ biceps femoris $\rightarrow$ erector spinae back to skull. Tied to [[running_spiral_line|Spiral Line]].
* **Role in Running**: Mediates **pelvis-thorax counter-rotation (dissociation)**, stabilizes knee tracking relative to foot pronation/supination, and stores elastic energy during trunk winding.
* **Observable Proxy**: Smooth pelvis-thorax dissociation curve and prompt rotational reversal timing.

### Layer 3: The Superficial Dynamic "X" (Functional Lines - FL)
* **Anatomical Basis**:
  * *Back Functional Line*: Latissimus dorsi $\rightarrow$ Thoracolumbar fascia $\rightarrow$ Contralateral Gluteus Maximus $\rightarrow$ Vastus lateralis.
  * *Front Functional Line*: Pectoralis major $\rightarrow$ Contralateral Rectus abdominis sheath $\rightarrow$ Adductor longus. Tied to [[running_functional_lines|Functional Lines]].
* **Role in Running**: Operates dynamically during the stride cycle to harness elastic momentum between the swinging arm and driving contralateral leg during propulsion and flight.
* **Observable Proxy**: Contralateral arm-leg synchrony and explosive cross-body timing.

## Required Biomechanical Inputs

To hypothesize about this 3-tier structure, the app requires validated upstream kinematic observations:
- [[running_pelvis_thorax_rotation]] (Front/back pelvis and thorax orientation signals)
- [[running_rotational_reversal]] (Timing of directional reversal in trunk/pelvis rotation)
- [[running_cross_body_coordination]] (Contralateral arm and leg swing timing)

## Evidence Gate

Apply [[running_evidence_gate]].
- Hypotheses remain Level D claims and must always require clinical/coaching correlation.
- Video analysis provides projected kinematic proxies, never direct measures of fascial tension, line loading, or force transfer.
- If upstream front/back tracking gates fail, return "Insufficient reliable evidence to evaluate rotational coordination."

## Permitted Reporting Language

* Permitted: "Pelvis and thorax orientation proxies showed distinct counter-directional phases, supporting a candidate Spiral Line and Functional Lines coordination hypothesis."
* Permitted: "Contralateral arm and leg reversal timing was symmetrical across valid stride cycles."

## Forbidden Claims

* Forbidden: "Spiral line is tight."
* Forbidden: "Deep front line core instability detected."
* Forbidden: "Superficial functional lines are generating 40% of propulsion force."
* Any diagnostic or prescriptive treatment claim derived from camera kinematics alone (see [[running_reporting_guardrails]] and [[running_kinematics_are_not_kinetics]]).

## Relationships

* **Framework Source**: [[anatomy_trains_myofascial_thomas_w_myers]]
* **Sub-hypotheses**: [[running_deep_front_line]], [[running_spiral_line]], [[running_functional_lines]]
* **Biomechanics Foundations**: [[running_pelvis_thorax_rotation]], [[running_cross_body_coordination]], [[running_rotational_reversal]], [[running_arm_leg_coordination]]
* **Guardrails**: [[running_reporting_guardrails]], [[running_evidence_levels]], [[running_kinematics_are_not_kinetics]]
