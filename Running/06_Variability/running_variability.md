---
id: running_variability
canonical_id: running.variability.stride_to_stride
type: Movement Pattern
running_node_type: movement_pattern
evidence_level: 5
running_claim_level: B
status: canonical
preferred_name: "Running - Stride-to-Stride Variability and Motor Repeatability"
aliases: [Variability, Motor repeatability, Stride dispersion, Kinematic consistency]
domain: running
directly_measured: false
camera_views: [side, front, back]
requires_clinical_correlation: false
confidence_required: contextual
related_nodes: []
source_nodes: [running_dingenen_2d_reliability_2018, running_zandbergen_fatigue_2023, running_trowell_fatigue_2025, running_winter_fatigue_2017]
relationships:
  required_inputs: [running_running_cycle, running_cadence, running_contact_time, running_landing_relationship, running_evidence_gate]
  supports: [running_fatigue_drift, running_left_right_asymmetry, running_head_trunk_pelvis_coordination]
  constrained_by: [running_evidence_gate, running_reporting_guardrails, running_measurement_limitations, running_kinematics_are_not_kinetics]
confidence: high
review_status: canonical_definition
relationship_count: 35
hub_score: 64
centrality: 0.30
updated: 2026-10-15
---

# Running - Stride-to-Stride Variability and Motor Repeatability

## Definition

The stride-to-stride dispersion, consistency, and temporal structure of a validated Level A kinematic metric across multiple accepted cycles within a continuous running bout.

## Why It Matters

High-performing runners frequently demonstrate remarkable motor repeatability. However, biomechanical variability is not inherently an error or flaw; functional variability allows the neuromusculoskeletal system to distribute mechanical stress across tissue microstructures and adapt to terrain fluctuations.

## Measurement and Sampling Requirements

1. **Minimum Cycle Sample Size**:
   - Per [[running_dingenen_2d_reliability_2018]], at least **7 valid steps / strides per side** are necessary to establish a dependable mean and variance estimate for 2D running variables.
   - Sessions with $< 7$ accepted strides must be flagged as *exploratory / preliminary data*.
2. **Within-Cycle vs. Pooled Dispersion**:
   - Compute excursions per stride first, then evaluate the median and interquartile range (or standard deviation) across strides.
   - Do **not** compute a single pooled max-minus-min across an entire video, as landmark tracking spikes or camera pans can artificially inflate the perceived excursion.

## Repeatability vs. Optimality Guardrail

- **Critical Principle**: A highly repeatable movement pattern is evidence of **motor consistency**, NOT automatic proof of optimal running economy, healthy tissue state, or superior performance.
- An unusual gait (such as large shoulder tipping or pelvic roll) that is executed with low stride-to-stride variability represents a stable, individual coordination strategy, not an acute coordination failure.

## Limitations and Evidence Boundaries

- Tracking noise and landmark jitter contribute to measured kinematic variance; low camera frame rates (< 60 fps) artificially increase temporal variability estimates.
- Kinematic repeatability does not measure neuromuscular fatigue, motor unit recruitment, or metabolic cost.

## Reporting Language

- *Permitted*: "Pelvic-line excursion was highly repeatable across 10 valid strides (median 12.1°, standard deviation 0.8°)."
- *Forbidden*: "Low variability proves this runner's form is physiologically optimal."
- *Forbidden*: "Elevated variability indicates muscle weakness."

## Review Status

`canonical_definition`. Grounded in reliability literature and motor control theory.
