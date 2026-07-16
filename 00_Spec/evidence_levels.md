---
id: evidence_levels
type: Spec
preferred_name: Evidence Hierarchy Spec
aliases: [evidence hierarchy, evidence levels, trust levels]
short_definition: "Rules and hierarchy governing evidence categorization, separating stable anatomy from golf-specific interpretation and app hypotheses."
relationships:
  governs: [vault_spec, golf_kinetics_observability_boundary, ai_movement_analysis_layer]
  contains: []
  connects_to: [golfer_ground_interaction_model, functional_lines]
confidence: high
review_status: active_spec
relationship_count: 11
hub_score: 16
centrality: 0.19
updated: 2026-07-16
---

# Evidence Hierarchy Specification

To maintain scientific integrity and prevent speculative coaching claims from being treated as established anatomical facts, this vault implements a strict 5-tier Evidence Hierarchy. All notes must clearly separate anatomical constants from swing biomechanics and software hypotheses.

## 1. The Five Levels of Evidence

| Level | Label | Description | Reference Sources | Allowed Use in Reasoning |
| :---: | :--- | :--- | :--- | :--- |
| **1** | **Anatomy Trains Structure** | Confirmed myofascial lines, bony stations, and structural pathways. | Myers, Julie Hammond | Stable structural mapping, line continuity, fascial track membership. |
| **2** | **General Biomechanics Research** | Peer-reviewed research on human movement, fascia properties, and general force transmission. | PubMed, Journal of Biomechanics, StatPearls | Validation of joint actions, muscle function, and general load transmission. |
| **3** | **Golf Biomechanics Research** | Studies analyzing force plates, kinematics, ground reaction forces/moments, and sequencing specific to golf. | Dr. Kwon, journal publications, sports science textbooks | Validation of swing phases, force vectors, torque generation, and COP/COM. |
| **4** | **Applied Golf Coaching Theory** | Expert coaching interpretations and movement patterns observed in professional contexts. | Davide Bertoli, professional coaching manuals | Phase descriptions, applied swing relevance, coaching cues. |
| **5** | **App-Logic Hypotheses** | Skeletal landmark calculations, computed scoring algorithms, and movement assessments. | Internal project team, AI application design | MediaPipe proxies, custom metrics scoring, feedback reports. |

## 2. Content Separation Rule
Every note containing golf swing relevance, movement patterns, or diagnostic hypotheses must explicitly separate sections into:

### Stable Anatomy (Level 1 & 2)
- Focuses on the physical structures: muscles, joints, bones, and fascial continuities.
- Must cite page numbers or sections from textbooks/papers.
- *Example:* The back functional line connects the pectoralis major and latissimus dorsi to the contralateral gluteus maximus via the lumbodorsal fascia.

### Golf Interpretation (Level 3 & 4)
- Details how the anatomical structure loads, stabilizes, or transfers energy during the swing phases.
- Explains how joint limitations affect performance or cause compensations.
- *Example:* Limited lead hip internal rotation prevents proper pelvic deceleration, causing early arm release and blocking back functional line loading.

### App Hypotheses (Level 5)
- Defines what sensors or skeletal tracking landmarks (MediaPipe) observe as proxies.
- Establishes calculated scores and logical rules.
- *Example:* A shoulder-to-contralateral-hip calculation may be reported as a camera-derived diagonal-distance descriptor; tissue loading remains unknown.

## 3. Kinetic Proxy Non-Upgrade Rule

A Level 3 relationship does not upgrade a linked Level 5 proxy into a measured kinetic variable. Camera geometry and timing may describe motion, but they may not be reported as force, pressure, moment, impulse, energy flow, muscle activation, or fascial loading without independent validation and the required instrumentation.

This rule applies even when a Level 3 source establishes a real mechanical relationship. A camera-derived landmark value remains a camera descriptor or Level 5 hypothesis until compatible sensors and an independently validated model support a measured or model-derived quantity. In particular:

- a hip midpoint is not whole-body [[center_of_mass|COM]];
- a visible foot or ankle point is not [[center_of_pressure|COP]] or pressure;
- a landmark separation is not a [[moment_arm]] without the measured force line of action;
- pelvis rotation is not [[pivoting_moment]] or [[ground_reaction_moment|GRM]];
- angle-rate order is not [[angular_momentum]] or energy transfer; and
- shoulder-to-hip geometry is not [[functional_lines|fascial loading]] or muscle activation.

[[golf_kinetics_observability_boundary]] is the authoritative future-golf implementation of this rule. It preserves the exact [[golfer_ground_interaction_model]] taxonomy, the six vault phase hooks and the separate fascial evidence boundary. Reports must use its permitted labels and return unavailable when required instrumentation, operational definitions or validation are absent.

## 4. Reporting and Safety

App outputs must state whether a value is measured by a named sensor, model-derived from compatible calibrated inputs, a camera-observable descriptor, or a Level 5 hypothesis. They must retain units, coordinate/view context, provenance, uncertainty, quality failures and algorithm version.

Evidence levels govern claim strength; they do not authorise diagnosis or treatment. A movement descriptor or hypothesis must not be used to identify injury, tissue pathology, weakness, restriction, pain source or treatment need.
