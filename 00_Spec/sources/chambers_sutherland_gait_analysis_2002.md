---
id: chambers_sutherland_gait_analysis_2002
type: Evidence Source
preferred_name: "A Practical Guide to Gait Analysis"
aliases: [Chambers Sutherland Gait, Practical Guide to Gait Analysis, JAAOS Gait 2002]
short_definition: "Peer-reviewed primer on human gait analysis covering the gait cycle, phases, temporal parameters, determinants of gait, kinematics, kinetics, EMG, foot pressure, and energetics, with the observational-vs-instrumented distinction the vault needs for its gait observability boundary."
author: Henry G. Chambers
contributors: [David H. Sutherland]
publication_year: 2002
publisher: Journal of the American Academy of Orthopaedic Surgeons
citation: "Chambers HG, Sutherland DH. A Practical Guide to Gait Analysis. J Am Acad Orthop Surg 2002;10:222-231."
format: journal_article_pdf
raw_file: raw/literature/A_Practical_Guide_to_Gait_Analysis.9.pdf
domain: gait
evidence_level: 1
source_role: foundational_domain_taxonomy
relationships:
  contains: [gait_cycle, stance_phase, swing_phase, initial_double_limb_support, single_limb_stance, second_double_limb_support, initial_swing, midswing, terminal_swing, gait_temporal_parameters, determinants_of_gait, gait_kinematics, gait_kinetics, gait_emg, foot_pressure, gait_energetics, gait_observability_boundary]
  connects_to: [observational_gait_analysis, ground_reaction_force, center_of_pressure]
  produces: []
  assists: []
  stabilizes: []
  limits: []
  compensates_for: []
  active_during: []
  assessed_by: [observational_gait_analysis, gait_kinematics]
  improved_by: []
  supported_by: []
  relevant_to: [observational_gait_analysis, gait_observability_boundary, gait_cycle]
domain_relevance: "Use this as the primary gait-cycle and gait-analysis reference for the gait assessment app. It supplies the canonical gait-cycle phase model, temporal parameters, the six determinants of gait, and the kinematic/kinetic/EMG/foot-pressure/energetics measurement categories. Crucially, it states that observational gait analysis cannot determine biomechanical causes — the exact boundary the vault enforces between camera-observable descriptors and instrumented kinetics."
evidence:
  - source_id: chambers_sutherland_gait_analysis_2002
    source_type: journal_article_pdf
    locator: "J Am Acad Orthop Surg 2002;10:222-231; local PDF pages 1-10 (10 pages total)"
    supports: "Defines the gait cycle (stance 62% / swing 38%), the eight cycle events, the three stance periods and three swing phases, temporal parameters (velocity, cadence, step/stride length), the six determinants of gait (Saunders), Perry's four prerequisites + Gage's fifth (energy conservation), kinematics, kinetics (joint moments from force plates), EMG, foot pressure, energetics, and the observational-vs-laboratory distinction."
confidence: high
review_status: source_summary_for_graph_mvp
relationship_count: 33
hub_score: 62
centrality: 0.297
updated: 2026-07-22
---

# A Practical Guide to Gait Analysis

## Source Role

This source is a **Level 1 foundational framework** for the gait domain. It defines the engine's canonical gait terminology: the gait cycle, its events, phase/period structure, percentages, temporal parameters, the determinants of gait, and — crucially — the **observational-vs-instrumented observability boundary** (observation cannot determine biomechanical cause; kinematics, kinetics, EMG, foot pressure, and energetics each require specific instrumentation). It is foundational to how the engine reasons about gait.

It is **not** a gold-standard biomechanics reference and **not** a replacement in depth for Perry & Burnfield's *Gait Analysis: Normal and Pathological Function* or Whittle's *Gait Analysis* — those are recorded as **future domain-expansion sources**, not required blockers for the MVP. A foundational gait taxonomy does not, by itself, authorise any measured kinetic, EMG, or causal claim; claims must be traced to this source and `source_role: foundational_domain_taxonomy` only for the terminology, phase structure, and observability boundary they support. Use [[dr_kwon_golfer_ground_interaction]] for golf instrumented kinetics; gait Level 3 instrumented sources are not yet in the vault.

## Graph Extraction Targets

- supports -> [[gait_cycle]]
- supports -> [[stance_phase]]
- supports -> [[swing_phase]]
- supports -> [[initial_double_limb_support]]
- supports -> [[single_limb_stance]]
- supports -> [[second_double_limb_support]]
- supports -> [[initial_swing]]
- supports -> [[midswing]]
- supports -> [[terminal_swing]]
- supports -> [[gait_temporal_parameters]]
- supports -> [[determinants_of_gait]]
- supports -> [[gait_kinematics]]
- supports -> [[gait_kinetics]]
- supports -> [[gait_emg]]
- supports -> [[foot_pressure]]
- supports -> [[gait_energetics]]
- supports -> [[gait_observability_boundary]]
- relevant_to -> [[observational_gait_analysis]]

## Relevant Sections

- Characteristics of Gait — the gait cycle, stance/swing split (62%/38%), cycle events, periods, and phases (Tables 1 and 2).
- Temporal Parameters — velocity, cadence, step length, stride length, cycle time.
- Force — COM trajectory (vertical ~4 cm rise/fall, lateral ~5 cm), double-sinusoidal curve.
- Determinants of Gait — Saunders et al.'s six determinants (pelvic rotation, pelvic list, stance knee flexion, foot/ankle motion, lateral pelvic displacement, axial lower-limb rotations); Perry's four prerequisites; Gage's fifth (energy conservation).
- Gait Analysis — systematic observational approach by plane (coronal, sagittal, transverse), videotaping for rotational abnormalities.
- Gait Analysis in the Motion Analysis Laboratory — the explicit observational-vs-instrumented boundary.
- Kinematics, Kinetics, Muscle Activity (EMG), Foot Pressure, Energetics — the five measurement categories.
- Applications — developmental disabilities, total joint arthroplasty, amputations, sports medicine.

## Source Summary for Graph Use

Chambers & Sutherland's central contribution is a **canonical gait-cycle model** plus an explicit statement of the **observational-vs-instrumented boundary**. For the vault's gait engine, the useful extraction is:

- The [[gait_cycle]] is one foot strike to the next foot strike of the same limb, normalized 0-100%, with stance ~62% and swing ~38%.
- The cycle is divided into three stance periods (initial double-limb support, single-limb stance, second double-limb support/preswing) and three swing phases (initial, mid, terminal), defined by eight events (foot strike, opposite toe-off, reversal of fore-aft shear, opposite foot strike, toe-off, foot clearance, tibia vertical, successive foot strike).
- [[gait_temporal_parameters]] include velocity, cadence, step length (one foot strike to contralateral foot strike), stride length (one foot strike to next same-foot strike), and cycle time.
- The [[determinants_of_gait]] (Saunders) are six movements whose loss compromises gait smoothness; loss of two or more produces uncompensated, inefficient gait.
- The five measurement categories ([[gait_kinematics]], [[gait_kinetics]], [[gait_emg]], [[foot_pressure]], [[gait_energetics]]) each require specific instrumentation; observational gait alone cannot determine biomechanical cause.

## Domain Interpretation — Observability Boundary

This source directly anchors the gait-domain observability boundary (the gait analogue of [[golf_kinetics_observability_boundary]]):

- "Observational gait analysis is limited because it cannot determine the biomechanical causes of an abnormal gait. Although one can infer causation, without measurements of kinetics or of muscular activity by dynamic electromyography (EMG), one can rarely be sure of the etiology of a problem." (local PDF p.4)
- Therefore a camera-derived gait descriptor (e.g., a knee-flexion proxy from a side-view recording) is a **camera-observable descriptor**, not a measured kinetic, EMG, foot-pressure, or energetic variable. It cannot diagnose gait etiology or direct treatment.
- This mirrors the vault's Level 5 / kinetic-proxy non-upgrade rule and should govern gait-app reporting exactly as Kwon's boundary governs golf-app reporting.

## Extracted Evidence Notes

- Local PDF p.1 (abstract) states gait analysis ranges from simple observation to computerized 3D motion analysis with energy measurement, and that it provides objective pre/post-operative outcome data.
- Local PDF p.2 (Tables 1 and 2) defines the gait cycle events, periods, and phases with % cycle and function.
- Local PDF p.2-3 defines temporal parameters (velocity, cadence, step/stride length) with age-specific normal values.
- Local PDF p.3 defines the COM double-sinusoidal trajectory and the six determinants of gait (Saunders et al.).
- Local PDF p.3-4 lists Perry's four prerequisites of normal gait and Gage's fifth (energy conservation).
- Local PDF p.4 states the observational-vs-instrumented boundary quoted above.
- Local PDF p.4-5 describes kinematics (3D marker-based motion analysis) and kinetics (force plates, joint moments, internal vs external moments).
- Local PDF p.5-6 describes EMG (surface vs fine-wire), foot pressure (in-shoe vs force-plate), and energetics (expired gas, heart rate, mechanical work from force plates).
- Local PDF p.7-9 lists applications: developmental disabilities (cerebral palsy), total joint arthroplasty, amputations, and sports medicine (throwing, batting, running, bicycling; ACL injury/reconstruction effects on gait).

## Review Notes

- Confidence is `high` because this is a peer-reviewed journal article read in full (10 pages) with explicit, quotable definitions and the observability-boundary statement.
- The article cites Perry (1992), Inman, Saunders, Gage — the canonical gait literature. Where deeper gait-cycle detail is needed, Perry & Burnfield *Gait Analysis: Normal and Pathological Function* is the gold-standard follow-on (not yet in the vault).
- Observational gait descriptors must not be reported as kinetics, EMG, or diagnosis. Use direct page checks before adding high-stakes relationships.
