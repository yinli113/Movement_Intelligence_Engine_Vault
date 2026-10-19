---
id: running_pelvic_obliquity_measurement
type: Biomechanics
preferred_name: Running pelvic obliquity measurement
category: Biomechanics
evidence_level: 3
source_role: domain_biomechanics
relationships:
  supported_by: [perpina_martinez_pelvic_imu_running_2023]
  bounded_by: [running_frontal_angle_quality, movement_reporting_standards]
confidence: medium
review_status: source_checked_app_transfer_unvalidated
relationship_count: 3
hub_score: 3
centrality: 0.0
updated: 2026-10-13
---

# Running pelvic obliquity measurement

[[perpina_martinez_pelvic_imu_running_2023]] is the canonical research reference for this measurement context. A projected hip line is a distinct 2D proxy: MediaPipe hips are not an instrumented anatomical pelvis coordinate frame. Preserve source dimensions, anatomical side identity and declared camera view.

Report total maximum-minus-minimum excursion over qualified complete same-side cycles, not ± amplitude. Shoulder-minus-pelvis frontal excursion is not axial rotation. Interpret observations only over retained intervals, governed by [[running_frontal_angle_quality]] and [[movement_reporting_standards]]. Neither the study nor a projected angle measures deep-core function or fascial tissue state.

| Relationship | Target | Boundary |
|---|---|---|
| research context | [[perpina_martinez_pelvic_imu_running_2023]] | IMU group statistics, not a rejection threshold |
| app implementation | [[running_frontal_angle_quality]] | Provisional geometry, temporal and cycle gates |
| reporting | [[movement_reporting_standards]] | Local evidence cannot establish whole-recording behaviour |
