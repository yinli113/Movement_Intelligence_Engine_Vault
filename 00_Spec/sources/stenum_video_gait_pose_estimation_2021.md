---
id: stenum_video_gait_pose_estimation_2021
type: Evidence Source
preferred_name: "Two-dimensional video-based analysis of human gait using pose estimation"
author: "Stenum J, Rossi C, Roemmich RT"
publication_year: 2021
doi: 10.1371/journal.pcbi.1008935
pmid: 33891585
pmcid: PMC8099131
source_url: https://doi.org/10.1371/journal.pcbi.1008935
evidence_level: 3
source_role: domain_biomechanics_measurement_comparison
review_status: reviewed_online_primary_article
confidence: medium
relationship_count: 2
hub_score: 2
centrality: 0.0
updated: 2026-11-13
---

# Two-dimensional video-based analysis of human gait using pose estimation

Stenum J, Rossi C, Roemmich RT (2021). [Primary article](https://doi.org/10.1371/journal.pcbi.1008935). Reviewed online 13 November 2026; no local PDF archive claimed.

## Direct evidence and transfer boundary

Thirty-one healthy participants, sagittal OpenPose video and instrumented comparison. Supports retaining per-cycle observations alongside aggregation and documenting camera/error limits. OpenPose validation does not transfer numerical accuracy to this MediaPipe pipeline, new phase candidates or clinical populations.

## App translation — engine synthesis

Use actual reviewed/detected event intervals. Compare corresponding phases for descriptive left/right differences; simultaneous curves show coordination. Keep missingness, source role and sample support visible. Display gates in `gait_reporting.v1.json` are engineering choices, not literature-validated clinical rules. Camera observations do not determine muscle weakness, tissue restriction, force or diagnosis.

Related: [[gait_observability_boundary]] · [[gait_cycle]].
