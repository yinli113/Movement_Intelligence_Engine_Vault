# Shared running measurement validity


### Running shared measurement validity (2026-10-16)
Canonical policy: `running_measurement_quality.v1.json`; runtime copy: `movement_running/src/knowledge/fixtures/running-measurement-quality.v1.json`. Apply both-limb source-pixel resolution, in-frame geometry and provisional side-camera conflict gates before downstream reporting. Preserve raw values and rejection reasons; never reject solely for large angles or asymmetry. Exclude collapsed torso references, withhold linear signed-angle wrap summaries/comparisons, and quarantine legacy side values without source landmarks. Verify mirror/scale invariance, high-visibility collapsed segments, large resolved angles, camera conflicts, cache migration and wrap boundaries. Engineering thresholds are evidence level 5, not camera-validated.

The canonical JSON defines the provisional numeric parameters. Both check:knowledge and sync:knowledge cover this export. Recording review requires at least five assessable frames and 50% conflicting shoulder/hip projections; this flags review and does not classify or relabel camera orientation.
