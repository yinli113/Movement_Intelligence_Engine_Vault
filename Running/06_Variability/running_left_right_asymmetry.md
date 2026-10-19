---
id: running_left_right_asymmetry
canonical_id: running.variability.left_right_asymmetry
type: Movement Pattern
running_node_type: movement_pattern
evidence_level: 5
running_claim_level: B
status: canonical
preferred_name: "Running - Left-Right Asymmetry and Bilateral Stance Dynamics"
aliases: [Left Right Asymmetry, Bilateral asymmetry, Stance symmetry index, Asymmetry decomposition]
domain: running
directly_measured: false
camera_views: [side, front, back]
requires_clinical_correlation: false
confidence_required: contextual
related_nodes: []
source_nodes: [running_dingenen_2d_reliability_2018, running_reinking_2d_reliability_2018, till_yes_running_literature_foundation]
relationships:
  required_inputs: [running_variability, running_running_cycle, running_initial_contact, running_toe_off, running_pelvis_rotation, running_shoulder_rotation, running_step_time]
  supports: [running_altered_rotational_coordination, running_different_load_distribution_strategy, running_three_layer_rotation_model]
  constrained_by: [running_evidence_gate, running_reporting_guardrails, running_measurement_limitations, running_kinematics_are_not_kinetics]
confidence: high
review_status: canonical_definition
relationship_count: 32
hub_score: 56
centrality: 0.28
updated: 2026-10-15
---

# Running - Left-Right Asymmetry and Bilateral Stance Dynamics

## Definition

A rigorous, side-paired comparison between validated `LEFT_STANCE` and `RIGHT_STANCE` cycles, evaluating whether movement differences represent genuine bilateral motor strategies or data artifacts.

## Why It Matters

Asymmetry is ubiquitous in human locomotion, including among world-record marathon runners. A nonzero left-right difference is not automatic proof of pathology, muscle weakness, or injury risk. Rather than flattening asymmetry into a single generic score, TillYes decomposes asymmetry into **four distinct biomechanical concepts**.

## The Four Separated Asymmetry Concepts

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 1. MAGNITUDE ASYMMETRY                                                      │
│ Difference in cycle-wise amplitude of a comparable metric                   │
│ e.g. Pelvic-line tilt excursion: Left median 9.8° vs Right median 14.2°     │
└─────────────────────────────────────────────────────────────────────────────┘
                                       │
┌─────────────────────────────────────────────────────────────────────────────┐
│ 2. TIMING ASYMMETRY                                                         │
│ Difference in the timing of peak, trough, onset, or directional reversal    │
│ e.g. Left stance contact time 215 ms vs Right stance contact time 245 ms    │
└─────────────────────────────────────────────────────────────────────────────┘
                                       │
┌─────────────────────────────────────────────────────────────────────────────┐
│ 3. COORDINATION ASYMMETRY                                                   │
│ Difference in signed lag or coupling between two measured quantities        │
│ e.g. Shoulder-pelvis reversal lag: 3% stride during Left vs 7% during Right │
└─────────────────────────────────────────────────────────────────────────────┘
                                       │
┌─────────────────────────────────────────────────────────────────────────────┐
│ 4. RELIABILITY ASYMMETRY                                                    │
│ Difference in tracking confidence, visibility, or accepted-cycle counts     │
│ e.g. 10 accepted left strides (high confidence) vs 4 right strides (occluded)│
│ CRITICAL: Reflects camera/lighting artifact, NOT athlete asymmetry!         │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Calculation and Symmetry Index Formulation

1. **Reporting Structure**:
   - For any evaluated metric, report: `left_median`, `right_median`, `difference_left_minus_right`, `variability_left` (IQR/SD), `variability_right` (IQR/SD), `n_valid_left`, `n_valid_right`, and `confidence`.
2. **Symmetry Index (SI)**:
   - When an amplitude index is requested, use the explicit signed formulation:
     $$SI_{\%} = \frac{200 \cdot (L - R)}{|L| + |R|}$$
   - Guard condition: Output `not available` when the denominator $(|L| + |R|) < \epsilon$ (near zero).
   - Sign convention must be stated (e.g. positive indicates left dominance, negative indicates right dominance).
3. **Circular Quantities**:
   - For angular or phase timing quantities, do not use linear percentage SI. Compute wrapped angular phase differences using circular statistics.

## Quality Gates and Minimum Sample Size

- Per [[running_dingenen_2d_reliability_2018]], a stable kinematic mean requires at least **7 valid strides per side** ($n_{\text{left}} \ge 7$ and $n_{\text{right}} \ge 7$).
- If either side has fewer than 7 accepted strides, the app must display **"exploratory / insufficient data for side comparison"** rather than reporting definitive asymmetry percentages.
- Never pool cycles into global min-to-max; evaluate per-stride excursions first, then calculate medians.

## Biomechanical Hypotheses Guided by Asymmetry

Bilateral asymmetry guides investigation across [[running_three_layer_rotation_model]]:
- Asymmetric arm swing or toe-off knee extension $\rightarrow$ [[running_functional_lines]] (Outer System).
- Asymmetric pelvic tilt excursion or shoulder-pelvis phase lag $\rightarrow$ [[running_spiral_line]] (Middle System).
- Uncompensated single-leg pelvic drop or arch collapse $\rightarrow$ [[running_deep_front_line]] (Inner System).

## Limitations and Evidence Boundaries

- 2D camera asymmetry can be artificially caused by camera perspective, runner curvature on turns, or lighting differentials ([[running_reinking_2d_reliability_2018]]).
- Kinematic asymmetry does not measure force distribution, bone loading, or muscle strength in Newtons.
- Never diagnose an athlete with "weak glutes" or "pathological gait" based on kinematic asymmetry alone.

## Reporting Language

- *Permitted*: "Pelvic-line tilt excursion showed magnitude asymmetry: median 14.2° during right stance vs. 9.8° during left stance across 10 valid strides per side ($SI = -36.7\%$, right greater)."
- *Permitted*: "Right stance contact time was 25 ms longer than left, coexisting with greater right pelvic excursion (Mesquita et al., 2024)."
- *Forbidden*: "Left leg is pathological or injured."
- *Forbidden*: "Asymmetry exceeds normal limits; clinical treatment required."

## Review Status

`canonical_definition`. Enriched with 4-way asymmetry taxonomy and strict reliability gates.
