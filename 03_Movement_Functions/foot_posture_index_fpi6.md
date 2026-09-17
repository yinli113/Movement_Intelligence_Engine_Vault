---
id: foot_posture_index_fpi6
type: Movement Function
preferred_name: Foot Posture Index (FPI-6)
aliases: [FPI-6 assessment, standing foot posture, foot pronation supination index]
short_definition: "A validated 6-item clinical metric quantifying standing static foot posture on a scale from -12 (marked supination) to +12 (marked pronation)."
domain: static_posture
evidence_level: 1
source_role: foundational_domain_taxonomy
supported_by: [redmond_foot_posture_index_2006, czaprowski_nonstructural_posture_2018]
status: reviewed_for_app_v1
reviewed_date: 2026-09-17
connects_to: [foot_posture_observability_boundary, bodyreading_static_posture, deep_front_line, superficial_back_line, spiral_line, lateral_line]
confidence: high
review_status: reviewed_for_app_v1
---

# Foot Posture Index (FPI-6)

## Clinical Framework

The Foot Posture Index (FPI-6) is a validated clinical rating tool designed to measure multi-segment foot posture in relaxed double-limb stance. Rather than relying on a single planar angle, it captures rearfoot, midfoot, and forefoot alignment across frontal, sagittal, and transverse planes.

## Scoring Breakdown

| Item | Criterion | -2 (Marked Supination) | 0 (Neutral) | +2 (Marked Pronation) | View |
|---|---|---|---|---|---|
| **1** | Talar Head Palpation | Palpable laterally only | Equally palpable | Palpable medially only | Palpation / Medial |
| **2** | Malleolar Curvature | Infra-malleolar straight/convex | Above/below curves equal | Infra-malleolar acutely concave | Posterior |
| **3** | Calcaneal Frontal Plane | Inverted > 5° (varus) | Vertical (0° to 2° valgus) | Everted > 5° (valgus) | Posterior |
| **4** | Talonavicular Bulging | Area markedly concave | Area flat | Area markedly convex/bulging | Medial |
| **5** | Medial Longitudinal Arch | High, acutely angled (cavus) | Smooth concentric curve | Severely flattened / floor contact | Medial |
| **6** | Forefoot Abd/Adduction | Medial toes only visible | Medial/lateral toes equally visible | Lateral toes clearly more visible | Posterior |

## Classification Ranges
- **-12 to -5**: Highly Supinated Foot
- **-4 to -1**: Supinated Foot
- **0 to +5**: Neutral / Normal Foot
- **+6 to +9**: Pronated Foot
- **+10 to +12**: Highly Pronated Foot

## App interpretation boundary

The current camera implementation is not a validated automated FPI-6 assessment. Clinical item scores must be explicitly entered by a clinician; palpation cannot be inferred from a photograph. Missing scores remain null, and partial subtotals must not use complete-index classification bands. See [[foot_posture_observability_boundary]].

Photo landmarks provide reviewable 2D descriptors only. Do not infer malleolar curvature or toe visibility from a heel angle. Do not infer muscle fatigue, stiffness, loading, or upstream joint mechanics from a total FPI score. Category-only fascial narratives are withheld pending finding-specific evidence and direct reassessment.
