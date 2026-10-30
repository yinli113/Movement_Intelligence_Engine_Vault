---
id: running_reporting_guardrails
canonical_id: running.guardrail.reporting
type: App Logic
running_node_type: guardrail
evidence_level: 5
running_claim_level: rule
status: canonical
preferred_name: Running - Reporting Guardrails
aliases: [running reporting language]
domain: running
directly_measured: false
camera_views: []
requires_clinical_correlation: false
confidence_required: contextual
related_nodes: []
source_nodes: []
relationships:
  governs: [running_long_forward_landing_pattern, running_altered_rotational_coordination, running_myofascial_hypothesis_layer]
  connects_to: [running_evidence_levels, running_evidence_gate, running_kinematics_are_not_kinetics]
confidence: high
review_status: canonical
relationship_count: 31
hub_score: 61
centrality: 0.277
updated: 2026-09-09
---

# Running - Reporting Guardrails

## Reporting Ladder

| Layer | Required form | Example |
|---|---|---|
| Measured | State value, side, repeats, view, proxy status, confidence | "Right landing offset was larger in 8 of 10 valid strides." |
| Pattern | Describe repeated relationship without cause | "A repeated right-greater landing-offset pattern was present." |
| Interpretation | Use "may reflect" or "is consistent with"; name supporting evidence | "This may reflect a different landing strategy between sides." |
| Hypothesis | Explicitly say hypothesis and require clinical correlation | "This pattern may support a cross-body myofascial hypothesis requiring clinical correlation." |

## Forbidden Transformations

- Foot strike -> good/bad score.
- Cadence below 180 -> poor.
- Asymmetry -> dysfunction.
- Kinematic descriptor -> force, stiffness, injury risk, or diagnosis.
- Reduced rotation -> tight fascial line.
- Kinematic ratio -> running economy.

## Insufficient Evidence

Use: "Insufficient reliable evidence to interpret this feature."

## Relationships

Must be traversed after [[running_evidence_levels]] and before any consumer-facing report.

## Optional website Gemini explanations — 2026-10-20

A requested Gemini explanation may receive only allowlisted metric aggregates, counts, side, view, direction and automatic-event status. Never send source video, landmarks, names or personal history through this adapter. Retrieve this reporting note, evidence gate and measurement limitations with relevant upstream measurement notes. Keep original measurements authoritative; missing evidence stays unavailable. Generated explanations must cite retrieved note IDs and expose source/model provenance. This initial adapter provides bounded descriptions and explanations, not diagnosis, treatment or tissue hypotheses. Unknown references and numerical measurement claims in model prose are rejected; standard dimensional labels such as 2D and 3D are permitted. An unavailable provider must not disable local findings. Generated language remains unverified.

## Gold pattern explanations — 2026-10-20

The website may provide an allowlisted derived Gold packet containing knee phase-profile aggregates, paired peak amplitude/timing differences, repetition counts and sensitivity results. It contains no raw samples, cycle/session identifiers or personal text. Prefer at most two supported explanations addressing pattern, movement location and repetition. A partial curve does not establish a complete swing peak; absent bilateral pairs leave timing-versus-range unresolved. Reporting examples in this vault are examples, never observations of the runner. Gold calculations remain separate from model prose, and claims retain the limitations of the actual measurement and view.


## Front/back coordination explanation — 2026-10-22

Explain the relationship, its location and repetition rather than restating that segments coordinate. Compare cycles and time windows separately. Contrast ordered cycle-level relationships and shoulder/pelvis excursions when those observations are supplied. Describe recorded image-plane tilt, not true rotation, energy transfer, stability or tissue performance. Correlation does not establish a phase lead or causal driver. Retain a single clear source-geometry/sensitivity note when a large tracked angle or sign-changing check makes the relationship tentative. Do not convert a mixed sign tally into a stride-repetition claim or use an elite athlete's identity as a normal reference.


## Findings-first consumer explanation — 2026-10-22

Lead with what this recording establishes: the measured relationship, where it occurs, whether it repeats, and the practical comparison it gives a running coach. State supported observations directly. Use qualified language for the interpretation rather than weakening every observation. Do not fill an insight with generic warnings or generic statements that movement varies. When only aggregates exist, explain the available side/range comparison without inventing phase or repetition.

Review every usable app metric. Group related metrics into useful findings; a metric need not become its own headline. Show which metrics support the explanation and which remain descriptive or unaddressed. A short opening summary can be followed by additional topic explanations. Missing pattern prerequisites restrict that pattern interpretation, not the display or explanation of a valid underlying measurement.

Kiwi should expose the app metric -> vault measurement/descriptor -> pattern context -> linked literature route, including internal vault notes rather than only external links. Retain calculation, purpose, supported comparisons and coaching questions alongside source metadata. Vault examples are reference examples, never this runner's results. Keep generic camera/provider boundaries in one expandable method section; retain a short finding-specific qualification only when it changes the interpretation. Preserve view, proxy, review status and claim-level metadata, numerical validation, and the prohibition on invented diagnosis, force, tissue state or causal claims.
