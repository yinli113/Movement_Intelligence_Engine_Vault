---
id: perpina_martinez_pelvic_imu_running_2023
type: Evidence Source
preferred_name: Pelvic IMU running kinematics (Perpiñá-Martínez et al., 2023)
evidence_level: 3
source_role: domain_biomechanics
confidence: medium
review_status: source_checked_app_transfer_unvalidated
relationship_count: 2
hub_score: 2
centrality: 0.0
updated: 2026-10-13
---

# Pelvic IMU running kinematics

Perpiñá-Martínez S. et al. (2023), *Differences between Sexes and Speed Levels in Pelvic 3D Kinematic Patterns during Running Using an Inertial Measurement Unit (IMU)*. DOI: 10.3390/ijerph20043631. [PubMed](https://pubmed.ncbi.nlm.nih.gov/36834324/) · [Full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC9961938/).

## Source observations

Methods §§2.1–2.2: 101 healthy experienced runners (51 men, 50 women), treadmill, S1-mounted BTS G-Sensor, self-selected speeds grouped by sex-specific speed categories. Reliability subset: 29 participants.

Table 2 pelvic obliquity excursion, group mean (SD), degrees:

| Speed category | Men | Women |
|---|---:|---:|
| Slow | 9.27 (2.53) | 8.11 (1.34) |
| Medium | 7.84 (2.16) | 9.64 (1.77) |
| Fast | 8.75 (1.44) | 7.81 (1.99) |

Table 2 therefore spans 7.81–9.64° across group means; the discussion's 7.84 lower endpoint omits the fast-female mean. These are group means, not individual acceptance limits.

## App boundary

The study does not validate MediaPipe hip-line angles, elite marathon broadcast footage, filtering thresholds, or a core-stability score. Its IMU result is research context for [[running_pelvic_obliquity_measurement]], not a hard rejection interval. Engineering rejection rules belong to [[running_frontal_angle_quality]].
