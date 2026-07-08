---
id: evidence_levels
type: Spec
preferred_name: Evidence Hierarchy Spec
aliases: [evidence hierarchy, evidence levels, trust levels]
short_definition: "Rules and hierarchy governing evidence categorization, separating stable anatomy from golf-specific interpretation and app hypotheses."
relationships:
  governs: [vault_spec]
  contains: []
  connects_to: []
confidence: high
review_status: active_spec
relationship_count: 1
hub_score: 1
centrality: 0.02
updated: 2026-07-08
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
- *Example:* A decrease in lead hip-to-shoulder separation angle at top of backswing acts as a proxy for reduced front functional line elastic loading.
