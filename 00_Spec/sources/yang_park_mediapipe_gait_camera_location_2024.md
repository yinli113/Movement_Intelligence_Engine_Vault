---
id: yang_park_mediapipe_gait_camera_location_2024
type: Evidence Source
preferred_name: "Yang & Park (2024) – Improving Gait Analysis Techniques with Markerless Pose Estimation Based on Smartphone Location"
aliases: [Yang Park 2024, MediaPipe Gait Camera Location]
short_definition: "Peer-reviewed smartphone MediaPipe BlazePose vs. marker-based motion capture study showing camera placement dependence (lateral view best for sagittal ankle angle; front-diagonal for hip/knee)."
author: Junhyuk Yang
contributors: [Kiwon Park]
publication_year: 2024
publisher: Bioengineering (MDPI)
citation: "Yang J, Park K. Improving Gait Analysis Techniques with Markerless Pose Estimation Based on Smartphone Location. Bioengineering (Basel). 2024;11(2):141."
source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC10886083/
pmid: 38391625
pmcid: PMC10886083
format: journal_article
domain: gait
evidence_level: 3
source_role: domain_biomechanics_measurement_comparison
relationships:
  supports: [gait_observability_boundary, gait_kinematics, ankle_dorsiflexion, ankle_plantarflexion, knee_flexion, hip_flexion]
  connects_to: [observational_gait_analysis, gait_cycle]
confidence: high
review_status: reviewed_online_abstract_and_metadata
relationship_count: 8
hub_score: 8
centrality: 0.0
updated: 2026-11-13
---

# Yang & Park (2024): MediaPipe Gait Camera-Location Validation

*Bioengineering*. 2024. [Full text (PMC10886083)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10886083/) · [PubMed (38391625)](https://pubmed.ncbi.nlm.nih.gov/38391625/). Reviewed online 2026-11-13; no local PDF archive claimed.

## Direct evidence

Evaluated MediaPipe BlazePose 2D coordinates (shoulder, hip, knee, ankle, toe, heel) from five smartphone camera placements against a marker-based motion capture system during walking. Demonstrated that joint-angle accuracy depends strongly on camera perspective: the **ankle angle** was most accurately captured from the **lateral (side) view**, whereas **hip and knee angles** showed highest accuracy from front-diagonal placements, with joint- and camera-specific errors under controlled placement; the results do not support a universal error below 5°.

## Transfer boundary

Supports using a **lateral (side) camera view** for sagittal ankle, knee, and hip descriptor proxies in `movement_assessment`, while proving that uncontrolled camera angle/placement introduces perspective error. Does **not** validate uncontrolled home/clinic single-camera recordings as equivalent to 3D lab kinematics or multi-camera setups, and does **not** authorize triplanar foot pronation/supination measurement. See [[gait_observability_boundary]].
