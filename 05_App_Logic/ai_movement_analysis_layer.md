---
id: ai_movement_analysis_layer
type: App Logic
preferred_name: AI Movement Analysis Layer Spec
aliases: [ai metrics, scoring logic, TGS, CCS, FLLI, ETE]
tags: []
category: App Logic
short_definition: "Historical design register for four unvalidated movement scores governed by the golf kinetics observability boundary."
evidence_level: 5
evidence:
  - source_id: dr_kwon_golfer_ground_interaction
    evidence_level: 3
    supports: "Defines instrumented forces, moments, COP, COM-referenced mechanics and their measurement requirements; it does not validate the four app scores."
  - source_id: anatomy_trains_myers_2009
    evidence_level: 1
    supports: "Defines Functional Line structure; it does not validate camera-derived tissue loading."
relationships:
  governed_by: [golf_kinetics_observability_boundary, evidence_levels]
  contains: []
  connects_to: [golfer_ground_interaction_model, ground_reaction_force, ground_reaction_moment, moment_arm, center_of_mass, center_of_pressure, functional_lines, kinematic_sequence]
  app_hypotheses: [torque_generation_score, com_cop_separation_score, functional_line_loading_index, energy_transmission_efficiency]
relationship_count: 12
hub_score: 17
centrality: 0.207
confidence: low
review_status: retired_unvalidated_concepts
updated: 2026-07-16
---

# AI Movement Analysis Layer

## Current Status

The four scores below are retained as **Historical design context**, not as implementable metrics or validated report outputs. Each is an unvalidated Level 5 concept and is not implementable from the current gait-only, single-camera pipeline. [[golf_kinetics_observability_boundary]] is the controlling future-golf measurement and reporting policy.

Level 3 Kwon relationships validate instrumented golf mechanics; they do not validate these score formulas, thresholds, labels or camera proxies. Level 1 Anatomy Trains evidence validates structural line membership; it does not validate visible line loading, activation, recoil or energy storage. No score may be exposed, thresholded or used for diagnosis or treatment until every listed prerequisite is met.

## Retirement and Prerequisite Register

| Historical score | Status | Instrumentation prerequisites | Validation prerequisites |
| :--- | :--- | :--- | :--- |
| Torque Generation Score | unvalidated Level 5 concept; not implementable from the current single-camera pipeline | Two synchronised 3-D force plates plus calibrated high-speed 3-D motion capture, whole-body modelling and declared coordinate systems. | A prespecified criterion definition and representative force-plate validation study covering error, calibration, repeatability, camera view and relevant subgroups. |
| COM–COP Separation Score | unvalidated Level 5 concept; not implementable from the current single-camera pipeline | Synchronised force plates or a validated pressure platform for COP plus calibrated 3-D motion capture and a declared segment-mass model for COM. | Independent validation against simultaneous sensor-derived COP and modelled COM, including threshold rationale, error, repeatability, view and subgroup analyses. |
| Functional Line Loading Index | unvalidated Level 5 concept; not implementable from the current single-camera pipeline | Calibrated 3-D motion capture plus an independently justified tissue-loading reference method; EMG may measure muscle activation but not fascia, and ultrasound/elastography would require its own construct validation. | A validated definition and criterion for line loading, preregistered mapping from structure to outcome, repeatability and error studies; diagonal geometry alone is insufficient validation. |
| Energy Transmission Efficiency | unvalidated Level 5 concept; not implementable from the current single-camera pipeline | Synchronised high-speed calibrated 3-D golfer-and-club motion capture, force plates, segment inertial parameters and validated inverse-dynamics or power methods. | Criterion validation for the claimed energy quantity and efficiency denominator, with uncertainty, repeatability, filtering, timing, error, subgroup and system-boundary analyses. |

## 1. Torque Generation Score (TGS)

### Historical design context

The historical concept attempted to combine ground reaction forces and external moments into a scalar score around whole-body COM:

$$\mathbf{M}_{ext,COM}=\sum_i\mathbf{r}_{COM\rightarrow COP_i}\times\mathbf{F}_i+\mathbf{M}_{pivot}+\mathbf{M}_{foot-contact}$$

This expression is retained only to preserve the original design intent. The exact taxonomy comes from [[golfer_ground_interaction_model]]: the GRF moment about COM, [[pivoting_moment]] and [[foot_contact_moment]] are three distinct external-moment classes. [[ground_reaction_moment|GRM]] is the residual/direct moment at COP underlying foot-contact moment, not a fourth additive class.

The former knee-extension and pelvis-rotation proposals are camera kinematic descriptors. They cannot estimate GRF, external moment or an efficiency score from ordinary video, and the former ±15% accuracy claim has no validation support and is retired.

The historical score was intended to rate the phase alignment of peak vertical force, horizontal shear force and pelvic angular velocity from transition towards Max Unweighting. That design aim is preserved for traceability only; neither the force peaks nor their proposed efficiency relationship are available from the camera descriptors.

### Implementation status

Unavailable. Implement only after the register's bilateral force-plate, calibrated 3-D motion-capture and independent validation prerequisites are satisfied. Until then, a future golf app may report separately defined image-plane knee or pelvis motion descriptors without a torque label.

## 2. COM–COP Separation Score (CCS)

### Historical design context

The concept was intended to describe geometry relevant to a vertical GRF moment:

$$M=F_zd$$

The equation applies only when $d$ is the perpendicular distance from the chosen reference to the measured force line of action in compatible coordinates. Horizontal COM-COP separation is not a universal moment arm. [[center_of_mass|COM]] is mass-weighted; [[center_of_pressure|COP]] is the measured GRF point of application. A camera hip midpoint and an ankle landmark are neither quantity.

The former proposed threshold placed the camera hip midpoint at 35%–45% of stance width relative to the lead ankle. That threshold and the hip-to-ankle substitution are unvalidated and retired. They are preserved only as study hypotheses, not production logic.

### Implementation status

Unavailable. Implement only after simultaneous sensor-derived COP, calibrated model-derived COM and independent validation establish the construct. A camera may report an explicitly named hip-midpoint or hip-to-ankle image-plane separation descriptor without COM, COP, pressure, moment-arm or torque language.

## 3. Functional Line Loading Index (FLLI)

### Historical design context

The concept proposed combining shoulder-to-contralateral-hip diagonal distance, its rate of change and phase timing. Anatomy Trains supports [[functional_lines]] as structural pathways; it does not establish that greater visible endpoint separation means fascial stretch, loading, elastic energy or muscle activation.

$$\mathrm{FLLI}_{historical}=f(\text{diagonal distance},\text{rate of change},\text{phase timing})$$

This historical functional form does not define or validate a tissue-loading outcome.

The only permitted camera wording is **camera-derived diagonal-distance descriptor; tissue loading remains unknown**. EMG can provide muscle-activation evidence under an appropriate protocol, but it does not directly measure fascia. No current accepted gold-standard Functional Line loading quantity is specified here.

### Implementation status

Unavailable as a loading index. Implement only if a defensible tissue-loading construct, independent reference instrumentation and validation protocol are established. Diagonal geometry may be implemented separately as a view-dependent descriptor with landmark, confidence and phase provenance.

## 4. Energy Transmission Efficiency (ETE)

### Historical design context

The concept proposed a ratio based on pelvis and thorax angular-velocity peaks and their timing. [[kinematic_sequence]] may describe ordered segment angular-velocity peaks, but sequence, deceleration or temporal coincidence does not by itself measure kinetic energy transfer, energy flow, mechanical power, angular momentum transfer or efficiency.

$$\mathrm{ETE}_{historical}=\frac{\omega_{\text{thorax,peak}}}{\omega_{\text{pelvis,peak}}}\left(1-\text{timing-delay deviation}\right)$$

This historical formula has no validated energy numerator, denominator or transfer measure and is not production logic.

Single-camera image-plane line-angle rates are view- and frame-rate-dependent. At common 30 fps capture, short peak delays may be unresolved; even high frame rate does not supply forces, segment inertial properties, 3-D rotations or an efficiency denominator.

### Implementation status

Unavailable. Implement only after synchronised force, calibrated high-speed 3-D golfer-and-club kinematics, inertial modelling, a declared system boundary and criterion validation support the specific energy and efficiency claims. Camera timing and angle-rate descriptors must remain separately labelled.

## Historical Architecture Boundary

The original design linked the scores as if each proved the next. That causal chain is retired. The permitted graph is instead:

```text
instrumented mechanics -> sensor-derived kinetic outputs, after validation
camera geometry/timing -> explicitly named motion descriptors
camera descriptor + Level 3 relationship -> Level 5 hypothesis, never an upgraded kinetic variable
fascial structure + golf context -> separately labelled vault interpretation, tissue state unknown
```

## Relationships

| Relationship | Target | Boundary |
| :--- | :--- | :--- |
| governed_by | [[golf_kinetics_observability_boundary]] | Controls labels, sensors, validation and unavailable states. |
| historical_context_from | [[golfer_ground_interaction_model]] | Supplies measured mechanics but does not validate the scores. |
| distinguishes | [[ground_reaction_force]] / [[ground_reaction_moment]] | Keeps force and residual/direct moment quantities separate. |
| distinguishes | [[center_of_mass]] / [[center_of_pressure]] / [[moment_arm]] | Prevents landmark substitutions for mass, pressure and force-line geometry. |
| bounded_by | [[functional_lines]] | Structural membership does not establish loading or activation. |
| bounded_by | [[kinematic_sequence]] | Peak order is not energy or momentum transfer. |

## Evidence Level

**Level 5 — unvalidated retired concepts.** Related Level 1 or Level 3 evidence does not increase their evidence level.

## App Use

Do not expose TGS, CCS, FLLI or ETE from the current single-camera pipeline. Use only the allow-listed labels in [[golf_kinetics_observability_boundary]], return unavailable when prerequisites fail, and preserve evidence and uncertainty.

## Open Questions

- Is there a scientifically and mechanically defensible criterion construct for any one historical score?
- Which non-kinetic camera descriptors are repeatable enough to retain after view-specific golf validation?
