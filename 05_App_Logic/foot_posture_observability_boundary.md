---
id: foot_posture_observability_boundary
type: App Logic
preferred_name: Foot Posture Observability Boundary
aliases: [fpi6_camera_boundary, foot_evidence_boundary]
short_definition: "Defines the Level-5 proxy boundary for camera-assisted Foot Posture Index (FPI-6) calculation, separating measured 2D image metrics from clinical palpation and diagnoses."
domain: static_posture
evidence_level: 5
source_role: app_logic_observability
supported_by: [redmond_foot_posture_index_2006]
status: reviewed_for_app_v1
reviewed_date: 2026-09-17
connects_to: [foot_posture_index_fpi6]
confidence: high
---

# Foot Posture Observability Boundary

## 1. Observability Mapping

| FPI-6 Criterion | Camera Observability | Evidence State | 2D Geometric Proxy |
|---|---|---|---|
| **1. Talar Head Palpation** | Not directly visible by 2D camera | `manual_input_required` / `estimated` | Default 0 (neutral) unless overridden via CLI/UI |
| **2. Supra/Infra Malleolar Curve** | Directly observable from rear view | `measured` | Contour concavity ratio above vs below lateral malleolus |
| **3. Calcaneal Frontal Position** | Directly observable from rear view | `measured` | Achilles midline vs calcaneus vertical angle (degrees) |
| **4. Talonavicular Bulging** | Observable from medial/sagittal view | `estimated` | Medial midfoot silhouette convexity index |
| **5. Medial Longitudinal Arch** | Directly observable from medial view | `measured` | Navicular/instep height ratio to foot length |
| **6. Forefoot Abd/Adduction** | Observable from rear vantage point | `measured` | Lateral vs medial toe visibility ratio ("too many toes" count) |

## 2. Evidence Integrity & Non-Diagnostic Guardrails

1. **Proxy metrics are not physical palpation**: 2D camera angles approximate skeletal alignment but do not measure subtalar bone contact, internal tissue stress, or joint laxity.
2. **Cautious Hypothesis Language**: Results must describe observed geometric patterns (e.g. "mild calcaneal eversion proxy observed"), never clinical pathology (e.g. do not diagnose "posterior tibial tendon dysfunction" or "rigid flatfoot").
3. **Multi-View Integration**: A full FPI-6 assessment requires both `foot_posterior` and `foot_medial` vantage points. Single-view captures must report view-bounded partial scores.
