---
id: running_running_economy
canonical_id: running.interpretation.running_economy
type: App Logic
running_node_type: guardrail
evidence_level: 5
running_claim_level: rule
status: canonical
preferred_name: Running - Running Economy
aliases: [Running Economy]
domain: running
directly_measured: false
camera_views: []
requires_clinical_correlation: false
confidence_required: contextual
related_nodes: []
source_nodes: [running_van_hooren_economy_2024]
relationships:
  required_inputs: [running_kinematics_are_not_kinetics]
  supports: [running_till_yes_progression_ratio]
  constrained_by: [running_evidence_gate, running_reporting_guardrails, running_kinematics_are_not_kinetics]
confidence: medium
review_status: evidence_audited_2026_10_16
relationship_count: 11
hub_score: 18
centrality: 0.098
updated: 2026-10-16
---

# Movement relationships and running economy

## Canonical relationship
`running.interpretation.running_economy` — existing guardrail identity retained.

## Principle and evidence
[[running_van_hooren_economy_2024]] (R06, Level 3 systematic review of observational studies) reports biomechanical associations with economy, not causal prescriptions. [[running_upper_body_rotation_energy_2023]] (R04) is an instrumented observational association. [[running_morley_lumbar_restriction_2019]] (R07) and [[running_halvorsen_vertical_frequency_2012]] (R22) are interventions with specific constraints, not ordinary natural-form equivalents.

## Required metrics, phases and views
Segments: whole body, pelvis, thorax and lower limbs. TillYes `running.rhythm.cadence`, `running.frontal.pelvis_tilt`, `running.trunk.lean` and the [[running_vertical_oscillation]] proxy can pose questions across continuous same-speed windows; phase claims need reliable events. Side/frontal descriptors retain their own views. Economy itself requires matched-speed metabolic measurements; no TillYes pose metric substitutes for them.

## Questions and possible relationships
Does a visible pattern change at the same speed? Does the measured metabolic response change too? Could deliberate restriction change several quantities simultaneously? Large visible movement alone cannot rank economy.

## Alternatives and assessment
Speed, body proportions, training, fatigue, shoes and task constraints can explain associations. Compare within-person controlled trials with metabolic testing if the economy question matters. Related anatomical context: [[hip_joint]], [[gluteus_maximus]], [[psoas_major]], [[running_functional_lines]].

## Structured uncertainty
limitation_keys: [kinetics, confounding, population, projection, tracking]. Resolve in [[running_measurement_limitations]]. Clinical interpretation remains distinct from experiment and correlation.

[[running_reasoning_retrieval_index]], [[running_research_handoff_audit]].
