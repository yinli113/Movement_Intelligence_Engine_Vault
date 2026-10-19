---
id: running_frontal_angle_quality
type: App Logic
preferred_name: Running frontal angle quality and recording coverage
category: App Logic
evidence_level: 5
source_role: app_logic_hypothesis
relationships:
  contextualized_by: [perpina_martinez_pelvic_imu_running_2023, running_pelvic_obliquity_measurement]
  governed_by: [movement_reporting_standards]
confidence: provisional
review_status: engineering_policy_not_camera_validated
relationship_count: 3
hub_score: 3
centrality: 0.0
updated: 2026-10-14
---

# Running frontal angle quality and recording coverage

Canonical executable policy: `running_angle_quality.v1.json`. Runtime owner: website Running module. The source [[perpina_martinez_pelvic_imu_running_2023]] provides context only; all thresholds below are provisional engineering choices, not study-derived normal limits or validated camera accuracy.

- Reject nonfinite/out-of-frame geometry, insufficient visibility, and projected 2D segment lengths below max(8 source pixels, 0.15 × projected shoulder-centre–hip-centre length). Require both hips and shoulders; a visibility score alone cannot establish geometry.
- Flag for review only a transient deviation exceeding 10° from the local median within ±100 ms, requiring at least two finite neighbours on each side. Retain the value, validity and raw angle; a temporal deviation alone does not reject a frame or stride. A well-resolved steep line is retained with a camera/identity review flag. Do not clip angles to population averages or replace missing peaks by interpolation.
- Apply the existing 400–2400 ms stride timing contract plus ordered contact/toe-off checks. Reject a cycle crossing any invalid metric sample or gap exceeding min(100 ms, 20% of cycle duration). Require endpoints within 10% of cycle boundaries, >=5 samples and >=3 complete same-side cycles for a summary.
- Report angle-usable seconds separately from seconds inside complete accepted cycles. Count time, not capture-loop frames. Display 5-second windows with replay targets, rejection counts and retained cycle counts. Never stitch separated periods into one cycle.
- Under 70% accepted-cycle time coverage, or fewer than 10 accepted cycles, label conclusions local-only; these display thresholds do not prove statistical representativeness. With fewer than three cycles, withhold excursion while preserving coverage and replay.
- No fatigue/trend/whole-video inference from sparse retained periods. A long video may still support local observations; if few complete cycles remain, say the recording cannot answer that metric. Other metrics need their own coverage.
- Cached angle results without the current policy version must be reprocessed from raw landmarks. The arbitrary linear axial-alignment score remains removed.

This policy implements [[running_pelvic_obliquity_measurement]] within [[movement_reporting_standards]]. Raw recordings remain unchanged. Camera angle, subject identity and occlusion still require visual review.

## Validation correction (2026-10-14)
Population comparisons, temporal changes and steep orientations are review flags only. Technical rejection is reserved for insufficient source geometry, unresolved full segment length, visibility/missing coordinates, invalid event timing or incomplete cycle coverage. `validateFrontalCycle` exports exact rejection reasons independently of review flags for each side. A rejected left candidate must not suppress available right-side cycles.

## Plain-language reporting (2026-10-14)
Lead with the percentage of recording time covered by complete usable hip-line strides; distinguish this from individual angle-sample time and the paired shoulder–hip subset. Label the existing relative excursion as “change in shoulder–hip angle difference”, never a coordination score. Explain the plotted stride separately from the mean across accepted strides. Do not assume consistency from one loop. Low coverage cannot support a whole-recording coordination assessment. Recommend a steady front/back camera, clearly visible hips and shoulders, good lighting, minimal obstruction and consecutive strides of the same runner. A repeatable pattern may support a personal comparison under matched conditions; it does not by itself justify corrective exercise or a claim of better performance.

## Retained-stride descriptive report (2026-10-14)
Describe all accepted paired strides in three sections: hip tilt, shoulder tilt, and their relationship. Report mean and min/max per-stride ranges, observed positive/negative extremum phase intervals, and elapsed-time-weighted sign quadrants after per-stride range-midpoint centering. Estimate quadrant duration by linear interpolation between paired timestamps, splitting at zero crossings; these are time proportions, not frame counts. Compare only unique interior positive peaks within each same-side stride. Count hip-first, shoulder-first, same-sample and unresolved (ties, flat series or boundary maxima); mean lead times describe only strides in that ordering group. Do not infer movement onset, causal leadership, preferred coordination or 3D rotation. State whether that peak ordering repeats across all accepted strides, with counts. Keep one short recording limitation including paired-cycle percentage and hip-only cycle percentage. These descriptors do not alter acceptance or replace raw data.

## Dynamic X sampling and selection audit (2026-10-14)
Uploaded-video captures start with a fresh pose tracker and a fixed 30 Hz source-time sampling grid from the beginning, awaiting decoded seeks. This is the analysis sampling rate, not native video FPS or a guarantee of model accuracy. Failure to decode stops capture; raw captured samples are preserved. Webcam acquisition remains live.

Dynamic X retains its existing 400–2400 ms event timing, finite valid degree-valued samples, >=5 samples, 10% endpoint tolerance, 20% maximum inter-sample gap and >=1° swing-span checks. Small missing sections already may be bridged; do not reconstruct missing peaks or lower visibility requirements to increase sample size. Opposite-arm/thigh peaks and rejected samples remain inspectable. A side requires >=2 accepted cycles to compute a descriptive circular resultant length; this is not a reliability threshold. Show each side separately, its count and circular angular standard deviation of peak phase, with missing-side evidence explicit. Report the leave-one-stride-out score range only where each contributing side retains >=2 cycles after omission; it is a sensitivity check, not a confidence interval.

Show exclusion reasons by side (counts may overlap). Compare the same data using stricter endpoint/gap tolerances (5%/10%), current (10%/20%), and wider (15%/25%), with all other gates unchanged. These are engineering sensitivity scenarios, not validated quality categories. Preserve the current primary result; never select the scenario that gives the highest score. Neither agreement across scenarios nor a high percentage establishes representative sampling or good coordination.
