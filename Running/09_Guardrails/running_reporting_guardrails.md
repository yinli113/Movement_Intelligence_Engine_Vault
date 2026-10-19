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
