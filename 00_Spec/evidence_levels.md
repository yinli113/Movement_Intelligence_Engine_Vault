---
id: evidence_levels
type: Spec
preferred_name: Evidence Hierarchy Spec
aliases: [evidence hierarchy, evidence levels, trust levels]
short_definition: "Rules and hierarchy governing evidence categorization for the cross-domain Movement Intelligence Engine. Level 1 holds the foundational frameworks that define how the engine reasons; Levels 2-4 hold domain taxonomies, instrumented biomechanics, and applied practice frameworks; Level 5 holds app-logic hypotheses. A source's evidence_level alone does not explain why it is included — pair it with source_role."
relationships:
  governs: [vault_spec, golf_kinetics_observability_boundary, ai_movement_analysis_layer]
  contains: []
  connects_to: [golfer_ground_interaction_model, functional_lines, bodyreading_static_posture, functional_movement_screen, gait_cycle, sagittal_posture_types]
  supported_by: [anatomy_trains_myofascial_thomas_w_myers, julie_hammond_breakout, gray_cook_movement_2010, chambers_sutherland_gait_analysis_2002, perry_burnfield_gait_analysis, czaprowski_nonstructural_posture_2018, dr_kwon_golfer_ground_interaction, bourgain_golf_swing_biomechanics_2022, golf_decoded_six_phases_swing]
confidence: high
review_status: active_spec
relationship_count: 25
hub_score: 35
centrality: 0.225
updated: 2026-07-22
---

# Evidence Hierarchy Specification

This vault is a **cross-domain Movement Intelligence Engine** serving golf, gait, static posture, squat, and future movement assessments. To keep speculative coaching or clinical claims from being treated as established fact, the vault uses a 5-tier Evidence Hierarchy. Each source note carries two fields: `evidence_level` (which tier) and `source_role` (why it is included). `evidence_level` alone cannot explain why a source is in the vault — `source_role` records that.

A `domain` field on each source note records which domain it serves (`golf`, `gait`, `static_posture`, `general_movement`, `squat`, …). Levels 1, 2, and 5 are domain-neutral; Levels 3 and 4 are parameterised by domain.

## 1. The Five Levels of Evidence

| Level | Label | Description | Reference Sources | Allowed Use in Reasoning |
| :---: | :--- | :--- | :--- | :--- |
| **1** | **Foundational Frameworks** | The frameworks that define the engine's core philosophy, terminology, observational logic, and interpretation boundaries. Foundational to the engine's reasoning — **not** "highest-quality evidence" and **not** necessarily a gold-standard biomechanics reference. | Myers (Anatomy Trains); Julie Hammond; Gray Cook (Movement); Chambers & Sutherland (gait); Perry & Burnfield (gait eight-phase, framework-cited); Czaprowski et al. (posture) | Define philosophy, terminology, taxonomy, observational structure, and observability limits. Do not, by themselves, authorise measurement, causal interpretation, treatment, or report claims. |
| **2** | **Domain Taxonomies and General Movement Models** | Accepted classifications, phase models, screening structures, and general biomechanical concepts within a domain. | Domain taxonomies and general biomechanics references (e.g., StatPearls; general biomechanics texts) | Classification, phase/segment definitions, screening structures, and general concept definitions. |
| **3** | **Domain-Specific Instrumented Biomechanics** | Research using 3D motion capture, force plates, pressure systems, EMG, validated kinematics, kinetics, or other instrumented measurements. | Instrumented biomechanics literature per domain | Measured/model-derived kinetics, kinematics, EMG, pressure, energetics for that domain. |
| **4** | **Applied Coaching, Clinical, or Practice Frameworks** | Domain-specific interpretation and applied practice models. Must never override Levels 1-3 or upgrade a 2D proxy into a measured kinetic or causal claim. | Coaching manuals, clinical practice frameworks | Domain phase descriptions, applied relevance, coaching cues, practice models. |
| **5** | **App-Logic Hypotheses** | Skeletal landmark calculations, computed scoring algorithms, and movement assessments produced by the apps. | Internal project team, AI application design | MediaPipe proxies, custom metrics scoring, feedback reports. |

### The six foundational source groups (Level 1)

These six source groups are not equal in publication type or research design, but they are all foundational to the engine because each defines a different part of the reasoning framework. **Level 1 means foundational to the engine's reasoning, not that all six sources have the same research design or independently support every clinical claim.**

- **Anatomy Trains** (`source_role: foundational_anatomical_framework`) — foundational myofascial and anatomical continuity framework.
- **Julie Hammond** (`source_role: foundational_clinical_philosophy`) — foundational clinical translation and movement/posture philosophy.
- **Gray Cook's Movement** (`source_role: foundational_movement_framework`) — foundational whole-movement and screening framework.
- **Chambers and Sutherland** (`source_role: foundational_domain_taxonomy`) — foundational observational gait model and gait terminology (read in full).
- **Perry & Burnfield** (`source_role: foundational_domain_taxonomy`) — foundational eight-phase gait taxonomy (**framework-cited** via Chambers & Sutherland; full text not yet in vault — see [[perry_burnfield_gait_analysis]] caveat).
- **Czaprowski et al.** (`source_role: foundational_clinical_philosophy`) — foundational non-structural sagittal-posture classification and cautious muscle-state interpretation.

A foundational source may define philosophy, terminology, taxonomy, or observability limits. It does **not** automatically support every measurement, causal interpretation, treatment recommendation, or report statement in that domain. Claims must still be traced to the specific source and `source_role` that supports them.

### source_role values

| Value | Meaning |
| :--- | :--- |
| `foundational_anatomical_framework` | Defines the anatomical/structural model the engine uses to reason about continuity and structure (Level 1). |
| `foundational_clinical_philosophy` | Defines clinical interpretation philosophy: posture/movement as a question, adaptability, cautious non-structural interpretation (Level 1). |
| `foundational_movement_framework` | Defines general movement-screening and assessment philosophy across domains (Level 1). |
| `foundational_domain_taxonomy` | Defines the canonical terminology, phases, events, and observability boundary for a domain (Level 1). |
| `domain_biomechanics` | Instrumented biomechanics research within a domain (Level 3). |
| `applied_practice` | Applied coaching, clinical, or practice framework within a domain (Level 4). |

## 2. Current Domain Population

| Domain | Level 1 foundations | Level 2 | Level 3 (instrumented) | Level 4 (applied) | Level 5 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **golf** | Anatomy Trains; Julie Hammond | StatPearls; general biomechanics | Dr. Kwon; Bourgain et al. 2022 | Davide Bertoli; coaching manuals | app metrics |
| **gait** | Chambers & Sutherland 2002; Perry & Burnfield (eight-phase, framework-cited) | general biomechanics (shared) | *future domain-expansion* (e.g., Whittle — **not yet in vault**) | *future domain-expansion* | app metrics |
| **static posture** | Anatomy Trains (BodyReading); Julie Hammond; Czaprowski et al. 2018 | general biomechanics (shared) | *future domain-expansion* (e.g., Kendall; Sahrmann — **not yet in vault**) | *future domain-expansion* | app metrics |
| **general movement / squat** | Gray Cook 2010 (FMS/SFMA) | general biomechanics (shared) | *future domain-expansion* (underlying instrumented squat studies — **not yet reviewed into vault**) | Straub & Powers 2024 clinical commentary | app metrics and squat engine synthesis |

Gait and static posture now have **Level 1 foundations**, but they still lack deeper Level 3 instrumented sources. The gait domain has **two** Level 1 sources: Chambers & Sutherland (observational gait structure + observability boundary, read in full) and Perry & Burnfield (eight-phase taxonomy, **framework-cited** via Chambers — full text not yet in vault). Perry & Burnfield is foundational to the engine's gait phase reasoning but is **not** a page-reviewed depth reference; Whittle remains a future domain-expansion source. Gray Cook supports squat and functional-movement screening, while Straub and Powers provides an applied Level 4 biomechanics commentary. Neither substitutes for reviewing the underlying Level 3 instrumented squat studies.

## 3. Content Separation Rule

Every note containing domain-specific movement relevance, movement patterns, or diagnostic hypotheses must explicitly separate sections into:

### Stable Anatomy & Models (Level 1 & 2)
- Physical structures and established models: muscles, joints, bones, fascial continuities, gait-cycle structure, posture taxonomies, movement-pattern screens.
- Must cite page numbers or sections from textbooks/papers.
- *Example:* The back functional line connects pectoralis major and latissimus dorsi to the contralateral gluteus maximus via the lumbodorsal fascia (Anatomy Trains). The gait cycle stance phase is ~62% of the cycle (Chambers & Sutherland 2002). The four non-structural sagittal posture types are lordotic, kyphotic, flat-back, and sway-back (Czaprowski et al. 2018).

### Domain Interpretation (Level 3 & 4)
- How structure or movement patterns load, stabilise, or transfer energy during the phases of a specific domain.
- *Boundary example — domain/app hypothesis (Level 5, not established Level 3-4 causation):* Limited lead-hip internal rotation may co-occur with altered pelvic-deceleration timing in a given golf capture. That co-occurrence cannot establish that the hip limitation caused either pattern, and camera data cannot confirm Functional Line loading. The same rule applies to gait, squat, and any other domain: a camera-observable co-occurrence is not a Level 3-4 causation.

### App Hypotheses (Level 5)
- What sensors or skeletal tracking landmarks (MediaPipe) observe as proxies; calculated scores and logical rules.
- *Example:* A shoulder-to-contralateral-hip calculation is a camera-derived diagonal-distance descriptor; tissue loading remains unknown. A 2D knee-flexion proxy from a side-view gait recording is a camera-observable descriptor, not a measured joint moment. A deep-squat depth proxy is a camera-observable descriptor, not a measured ankle-dorsiflexion range.

### Foundational-source tracing rule
A foundational (Level 1) source may define philosophy, terminology, taxonomy, or observability limits. It does **not** automatically support every measurement, causal interpretation, treatment recommendation, or report statement in that domain. Every claim must be traced to the specific source and `source_role` that supports it; a foundational taxonomy does not authorise a kinetic claim, and a foundational philosophy does not authorise a muscle-by-muscle treatment conclusion.

## 4. Kinetic Proxy Non-Upgrade Rule

A Level 3 relationship does not upgrade a linked Level 5 proxy into a measured kinetic variable. Camera geometry and timing may describe motion, but they may not be reported as force, pressure, moment, impulse, energy flow, muscle activation, or fascial loading without independent validation and the required instrumentation.

This rule applies even when a Level 3 source establishes a real mechanical relationship. A camera-derived landmark value remains a camera descriptor or Level 5 hypothesis until compatible sensors and an independently validated model support a measured or model-derived quantity. In particular:

- a hip midpoint is not whole-body [[center_of_mass|COM]];
- a visible foot or ankle point is not [[center_of_pressure|COP]] or pressure;
- a landmark separation is not a [[moment_arm]] without the measured force line of action;
- pelvis rotation is not [[pivoting_moment]] or [[ground_reaction_moment|GRM]];
- angle-rate order is not [[angular_momentum]] or energy transfer;
- shoulder-to-hip geometry is not [[functional_lines|fascial loading]] or muscle activation;
- a 2D knee-flexion proxy is not a measured gait kinetic or joint moment;
- a 2D squat-depth proxy is not a measured ankle/knee/hip range of motion.

[[golf_kinetics_observability_boundary]] is the authoritative current implementation of this rule for the golf domain. Each other domain defines its own observability boundary following the same principle: reports must use permitted labels and return unavailable when required instrumentation, operational definitions or validation are absent. The gait-domain boundary is anchored by the observational-vs-instrumented distinction stated in [[chambers_sutherland_gait_analysis_2002]].

## 5. Reporting and Safety

App outputs must state whether a value is measured by a named sensor, model-derived from compatible calibrated inputs, a camera-observable descriptor, or a Level 5 hypothesis. They must retain units, coordinate/view context, provenance, uncertainty, quality failures and algorithm version.

Evidence levels govern claim strength; they do not authorise diagnosis or treatment. A movement descriptor or hypothesis must not be used to identify injury, tissue pathology, weakness, restriction, pain source or treatment need. This applies to every domain the vault serves.
