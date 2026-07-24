---
id: gait_cycle
type: Movement Function
preferred_name: "Gait Cycle"
aliases: [stride cycle, gait cycle 0-100%]
short_definition: "The interval from one foot strike of a limb to the next foot strike of the same limb, normalised 0-100%, with stance ~62% and swing ~38%; the foundational unit of gait analysis."
domain: gait
evidence_level: 2
source_role: foundational_domain_taxonomy
supported_by: [chambers_sutherland_gait_analysis_2002]
status: reviewed
reviewed_date: 2026-07-22
contains: [stance_phase, swing_phase, initial_double_limb_support, single_limb_stance, second_double_limb_support, initial_swing, midswing, terminal_swing]
connects_to: [gait_temporal_parameters, determinants_of_gait, observational_gait_analysis, gait_observability_boundary]
directly_supported_claims:
  - "The gait cycle is one foot strike to the next foot strike of the same limb, normalised 0-100%."
  - "Stance is ~62% and swing ~38% of the cycle."
  - "The cycle is divided into three stance periods and three swing phases, defined by eight events."
app_translation:
  - "Use the gait cycle as the normalisation frame: report phase percentages and event timings from a 2D side view."
  - "A 2D app can identify foot-strike/toe-off events and phase boundaries, but cannot measure kinetics, EMG, or causation."
---

# Gait Cycle

## Definition

The **gait cycle** is the interval from one foot strike of a limb to the next foot strike of the same limb, normalised 0-100%. Stance is ~62% and swing ~38% (Chambers & Sutherland, *A Practical Guide to Gait Analysis*, p.2). It is the foundational unit of gait analysis.

## Why it matters

The cycle is the frame against which every gait variable (kinematics, kinetics, EMG, pressure) is reported. Without a shared cycle frame, gait findings cannot be compared across steps, people, or sessions.

## Source-derived model

- One foot strike → next same-foot foot strike = 100%.
- Stance ~62%, swing ~38%.
- Three stance periods + three swing phases, bounded by eight events (foot strike, opposite toe-off, reversal of fore-aft shear, opposite foot strike, toe-off, foot clearance, tibia vertical, successive foot strike).

## Joint involvement

Whole lower limb: [[hip_joint]], [[knee_joint]], [[ankle_joint]], plus pelvis and trunk.

## Muscle involvement

No muscle claims from this node; muscle activity is the [[gait_emg]] category.

## Movement or phase relationships

Parent of [[stance_phase]] (A) and [[swing_phase]] (A), each subdivided into three periods/phases (A). Related to [[gait_temporal_parameters]] (A) and [[determinants_of_gait]] (A).

## Possible myofascial relationships

None directly. Mapping the cycle to fascial lines is an engine synthesis (C).

## What a 2D app can observe

- Foot-strike and toe-off events, phase boundaries, and step/stride timing from a 2D side view.

## What the app must not infer

- Kinetics, EMG, foot pressure, or energetics (each requires instrumentation).
- Causal etiology of an abnormal gait.

## Related concepts

[[stance_phase]], [[swing_phase]], [[gait_temporal_parameters]], [[determinants_of_gait]], [[observational_gait_analysis]], [[gait_observability_boundary]].

## Sources

- [[chambers_sutherland_gait_analysis_2002]] — p.2 (Tables 1-2).

## Evidence-separation rules

- **(A)** Cycle definition, 62/38 split, three+three periods, eight events — directly from Chambers & Sutherland.
- **(B)** Cross-links to [[gait_temporal_parameters]], [[determinants_of_gait]] — same Level 1 source.
- **(C)** Any fascial-line mapping is `engine_synthesis`.
