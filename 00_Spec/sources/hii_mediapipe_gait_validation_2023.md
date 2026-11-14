---
id: hii_mediapipe_gait_validation_2023
type: Evidence Source
preferred_name: "Hii et al. (2023) – Automated Gait Analysis Based on a Marker-Free Pose Estimation Model"
aliases: [Hii 2023, MediaPipe Vicon Gait Validation]
short_definition: "Peer-reviewed Sensors study validating MediaPipe Pose marker-free gait analysis against Vicon 3D motion capture for automated temporal and spatial gait parameters."
author: Chang Soon Tony Hii
contributors: [Kok Beng Gan, Nasharuddin Zainal, Norlinah Mohamed Ibrahim, Shahrul Azmin, Siti Hajar Mat Desa, B. P. C. van de Warrenburg, Hua You]
publication_year: 2023
publisher: Sensors (MDPI)
citation: "Hii CST, Gan KB, Zainal N, et al. Automated Gait Analysis Based on a Marker-Free Pose Estimation Model. Sensors (Basel). 2023;23(14):6489."
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC10383186/
pmid: 37510793
pmcid: PMC10383186
doi: 10.3390/s23146489
format: journal_article
domain: gait
evidence_level: 3
source_role: domain_biomechanics_measurement_comparison
relationships:
  supports: [gait_observability_boundary, gait_temporal_parameters, gait_cycle]
  connects_to: [observational_gait_analysis, stance_phase, swing_phase]
confidence: high
review_status: reviewed_online_abstract_and_metadata
relationship_count: 6
hub_score: 6
centrality: 0.0
updated: 2026-11-13
---

# Hii et al. (2023): MediaPipe vs. Vicon Gait Validation

*Sensors*. 2023;23(14):6489. [Full text (PMC10383186)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10383186/) · [PubMed (37510793)](https://pubmed.ncbi.nlm.nih.gov/37510793/). Reviewed online 2026-11-13; no local PDF archive claimed.

## Direct evidence

Validated an automated marker-free gait analysis pipeline built on **MediaPipe Pose** against a **Vicon** 3D optoelectronic motion-capture system for extracting temporal and spatial gait parameters during walking trials.

## Transfer boundary

Supports using MediaPipe Pose for **temporal gait-event and stride-cycle tracking** as an accessible screening/descriptor layer. Does **not** validate 2D single-camera MediaPipe output as equivalent to 3D Vicon kinematics, kinetics, EMG, or triplanar subtalar foot motion, and does **not** replace clinician verification when foot-contact frames are uncertain. See [[gait_observability_boundary]].
