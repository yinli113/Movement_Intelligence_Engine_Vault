---
id: gray_cook_movement_2010
type: Evidence Source
preferred_name: "Movement: Functional Movement Systems: Screening, Assessment, and Corrective Strategies"
aliases: [Gray Cook Movement, Functional Movement Systems, FMS textbook, Movement Cook 2010]
short_definition: "General movement-screening and assessment framework source covering the Functional Movement Screen (FMS), the Selective Functional Movement Assessment (SFMA), and corrective-strategy logic for cross-domain movement analysis."
author: Gray Cook
contributors: [Lee Burton, Kyle Kiesel, Greg Rose, Milo F. Bryant]
publication_year: 2010
publisher: On Target Publications, Santa Cruz, California
isbn: 978-1-931046-72-5
format: textbook_pdf
raw_file: raw/literature/Movement.pdf
domain: general_movement
evidence_level: 1
source_role: foundational_movement_framework
relationships:
  contains: [functional_movement_screen, selective_functional_movement_assessment, deep_squat, hurdle_step, inline_lunge, shoulder_mobility_reaching, active_straight_leg_raise, trunk_stability_pushup, rotary_stability, joint_by_joint_concept, performance_pyramid]
  connects_to: [movement_screening, movement_assessment, corrective_strategy, squat_assessment, bodyreading_static_posture]
  produces: []
  assists: []
  stabilizes: []
  limits: []
  compensates_for: []
  active_during: []
  assessed_by: [functional_movement_screen, selective_functional_movement_assessment]
  improved_by: [corrective_strategy]
  supported_by: []
  relevant_to: [functional_movement_screen, selective_functional_movement_assessment, general_movement_assessment, squat_assessment]
domain_relevance: "Use this as the primary source for movement-pattern screening and assessment logic across all app domains (golf, gait, static posture, squat, future sports). It supplies the FMS seven-test screen, the SFMA clinical breakouts, the joint-by-joint concept, and the performance-pyramid model. It does not supply fascial-line anatomy (use Anatomy Trains) or instrumented kinetics (use Kwon / gait lab sources)."
evidence:
  - source_id: gray_cook_movement_2010
    source_type: textbook_pdf
    locator: "Front matter, table of contents, local PDF pages 3-9; chapters 1-15 and appendices 1-12"
    supports: "Defines screening vs assessment, the FMS seven tests with scoring criteria, the SFMA top-tier assessments and breakouts, the joint-by-joint concept, and corrective-strategy frameworks (mobility before stability, reverse patterning, reactive neuromuscular training, conscious loading)."
confidence: medium
review_status: source_summary_for_graph_mvp
relationship_count: 14
hub_score: 42
centrality: 0.31
updated: 2026-07-22
---

# Movement: Functional Movement Systems

## Source Role

This source is a **Level 1 foundational framework** for the engine. It defines the engine's general movement-screening and assessment philosophy: whole movement patterns before isolated body parts, movement quality before performance, screening versus diagnosis, and movement versus motion. It is foundational to the engine's reasoning across all domains (golf, gait, static posture, squat, future sports) — the same seven FMS patterns and the SFMA clinical logic apply regardless of domain.

It is **not** a gold-standard biomechanics reference, **not** an instrumented-kinetics source, and **not** a fascial-line anatomy reference. A foundational movement framework does not, by itself, authorise any measurement, causal interpretation, treatment recommendation, or report statement; claims must be traced to this source and `source_role: foundational_movement_framework` only for the philosophy/terminology/screening-structure they support. Use [[anatomy_trains_myofascial_thomas_w_myers]] for fascial-line anatomy and [[dr_kwon_golfer_ground_interaction]] / [[chambers_sutherland_gait_analysis_2002]] for instrumented kinetics.

## Graph Extraction Targets

- supports -> [[functional_movement_screen]] (FMS)
- supports -> [[selective_functional_movement_assessment]] (SFMA)
- supports -> [[deep_squat]] (FMS test 1; also the vault's squat-assessment anchor)
- supports -> [[hurdle_step]] (FMS test 2)
- supports -> [[inline_lunge]] (FMS test 3)
- supports -> [[shoulder_mobility_reaching]] (FMS test 4)
- supports -> [[active_straight_leg_raise]] (FMS test 5)
- supports -> [[trunk_stability_pushup]] (FMS test 6)
- supports -> [[rotary_stability]] (FMS test 7)
- supports -> [[joint_by_joint_concept]] (Appendix 1)
- supports -> [[performance_pyramid]] (Ch. 10)
- relevant_to -> [[movement_screening]]
- relevant_to -> [[squat_assessment]]

## Relevant Sections

- Chapter 1: Introduction to Screening and Assessment — screening vs assessment, body parts vs movement patterns, the movement-vs-motion paradox.
- Chapter 2: Anatomical Science vs Functional Science — stabilizers vs movers, fascial matrix, neuromuscular network, authentic movement.
- Chapter 5: Functional Movement Systems and Movement Patterns — FMS overview, SFMA top-tier, the four basic filters, scoring criteria.
- Chapter 6: Functional Movement Screen Descriptions — the seven FMS tests with scoring sheet and clearing exams.
- Chapter 7: SFMA Introduction and Top-Tier Tests — FN/FP/DP/DN classification, the seven top-tier assessments.
- Chapter 8: SFMA Assessment Breakout Descriptions and Flowcharts — mobility vs stability problem breakouts.
- Chapter 9: Analyzing the Movements in Screens and Assessments — the deep squat, hurdle step, inline lunge, shoulder mobility, ASLR, pushup, rotary stability/rolling.
- Chapters 10-14: Understanding and Developing Corrective Strategies — performance pyramids, the six Ps, mobility before stability, reverse patterning, reactive neuromuscular training, conscious loading.
- Appendix 1: The Joint-by-Joint Concept.
- Appendix 9: FMS Scoring Criteria.
- Appendix 10: Verbal Instructions for the Functional Movement Screen.

## Source Summary for Graph Use

Cook's central contribution is a **movement-pattern model** that separates screening (FMS, no pain, non-clinical) from assessment (SFMA, pain-present, clinical). For the vault's cross-domain engine, the useful extraction is a set of source-backed relationships:

- The [[deep_squat]] is a first-class movement pattern: an overhead deep squat that simultaneously screens bilateral, symmetrical, and functional mobility of the ankles, knees, hips, thoracic spine, and shoulders. It is the vault's anchor for future **squat assessment** and is also FMS test 1.
- The [[functional_movement_screen]] is a seven-test battery (deep squat, hurdle step, inline lunge, shoulder mobility, active straight-leg raise, trunk stability pushup, rotary stability) scored 0-3 with clearing exams. It is a screen, not a diagnosis.
- The [[selective_functional_movement_assessment]] is a clinical, pain-present assessment using FN/FP/DP/DN (Functional/Non-functional × Painful/Non-painful) classification and breakouts that separate mobility from stability/motor-control problems.
- The [[joint_by_joint_concept]] models the body as an alternating stack of mobility-focused and stability-focused joints, which informs where to look for compensation.
- The [[performance_pyramid]] (sport skill / athletic performance / functional movement) frames why a movement screen sits underneath sport-specific performance — directly relevant to the vault's evidence separation between domain skill (Level 4) and foundational movement (Level 2).

## Domain Interpretation

This source supports movement-pattern screening and assessment hypotheses across domains. Example reasoning paths:

- [[squat_assessment]] -> [[deep_squat]] -> ankle/knee/hip/thoracic/shoulder mobility filters
- [[movement_screening]] -> [[functional_movement_screen]] -> seven-pattern baseline -> flag pain for clinical SFMA breakout
- Any sport (golf, running, etc.) -> [[performance_pyramid]] -> foundational movement screen under the sport-specific skill layer
- [[inline_lunge]] and [[hurdle_step]] -> single-leg stability relevant to gait and golf lead-leg mechanics

## Extracted Evidence Notes

- Local PDF pages 3-9 (front matter / contents) list the 15 chapters and 12 appendices, identifying FMS, SFMA, the joint-by-joint concept, FMS scoring criteria, and verbal instructions as the operationally useful sections.
- Chapter 5 (local PDF pages 73-86) defines the four basic filters and FMS scoring criteria (0-3 hierarchy).
- Chapter 6 (local PDF pages 87-106) gives the seven FMS test descriptions with clearing exams for shoulder mobility, pushup, and rotary stability.
- Chapter 7 (local PDF pages 107-132) defines the SFMA FN/FP/DP/DN result categories and the seven top-tier assessments (cervical, upper extremity, multi-segmental flexion/extension/rotation, single-leg stance, overhead deep squat).
- Chapter 9 (local PDF pages 191-216) analyzes the deep squat, hurdle step/single-leg stance, inline lunge, shoulder mobility, ASLR, pushup, and rotary stability/rolling in detail.
- Appendix 1 (local PDF pages 319-329) presents the joint-by-joint concept (alternating mobility/stability joint needs up the kinetic chain).

## Review Notes

- Confidence is `medium` because this is a source summary extracted from the PDF front matter and table of contents plus chapter scope, not a full chapter-by-chapter review.
- FMS/SFMA are screening and assessment frameworks; their outputs are pattern scores and breakouts, not measured kinetics or fascial-line membership. Do not report an FMS score as a kinetic variable or a fascial loading claim.
- Pain discovered during screening must redirect to clinical assessment (SFMA) and qualified professionals; the app must not diagnose from a screen alone.
- Use direct page checks before adding high-stakes relationships.
