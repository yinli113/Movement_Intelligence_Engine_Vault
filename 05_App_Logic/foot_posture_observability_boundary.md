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

## Corrected implementation contract — 2026-09-17

- No neutral default for an unexamined item. Missing palpation and unseen criteria are null, never zero.
- Clinical FPI-6 totals and classification require six explicit clinician ratings for the same foot and examination. A partial subtotal is labelled with its item count and never assigned full-index categories.
- A photograph can support visual review of some criteria, but an arbitrary silhouette centre is not an Achilles or calcaneal landmark. Skin segmentation cannot establish anatomy.
- The current app has no validated automatic foot landmark detector. Users place and review points on their chosen foot. Posterior measurements use separate lower-leg and heel axes; medial measurements use a reviewed baseline and arch point. These are unvalidated 2D descriptors, not automatic FPI scores.
- Preserve image aspect ratio and native coordinates. Mirroring reverses the anatomical sign of posterior angles; the selected foot and mirror state must accompany every observation.
- No forced eversion floor, angle-derived toe visibility or ankle curvature, fixed medial landmarks, or fabricated fallback values. A missing or invalid observation remains unavailable.
- One photograph cannot be treated as a multi-view capture. Clinicians may enter ratings from a separate complete examination, with that provenance explicit.
- A total score does not establish muscle activation, tissue tension, stiffness, ground reaction force, diagnosis, or upstream compensation. Category-only fascial and kinetic narratives are withheld.

The clinical framework remains [[foot_posture_index_fpi6]] / [[redmond_foot_posture_index_2006]]. These software gates are Level 5 app policy. Image-based review limitations are also supported by [the image-based FPI reliability study](https://pmc.ncbi.nlm.nih.gov/articles/PMC4004124/).
