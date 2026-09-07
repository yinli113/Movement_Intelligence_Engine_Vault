---
id: bourgain_golf_swing_biomechanics_2022
type: Evidence Source
preferred_name: "Bourgain et al. 2022 – Golf Swing Biomechanics: A Systematic Review and Methodological Recommendations for Kinematics"
aliases: [Bourgain 2022, Bourgain golf swing review, golf swing kinematics systematic review, Sports 10(6) 91]
short_definition: "Level 3 systematic review of 92 instrumented golf-swing kinematics studies, categorised into X-factor, crunch factor, swing plane and clubhead trajectory, kinematic sequence, and joint angular kinematics, with methodological recommendations."
author: "Maxime Bourgain; Philippe Rouch; Olivier Rouillon; Patricia Thoreux; Christophe Sauret"
publication_year: 2022
journal: "Sports 10(6): 91"
doi: 10.3390/sports10060091
pmcid: PMC9227529
primary_urls:
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC9227529/
  - https://doi.org/10.3390/sports10060091
format: peer_reviewed_systematic_review
status: reviewed
review_basis: full_text_html_read
evidence_level: 3
source_role: domain_biomechanics
domain: golf
raw_file: raw/literature/bourgain_golf_swing_biomechanics_2022.pdf
accessed: 2026-07-29
relationships:
  contains: [x_factor, kinematic_sequence]
  connects_to: [golf_swing, golf_swing_events, golf_movement_sequence, golf_kinetics_observability_boundary, dr_kwon_golfer_ground_interaction]
  supported_by: []
  relevant_to: [golf_swing, x_factor, kinematic_sequence, golf_swing_events, golf_movement_sequence, temporal_movement_metrics, metric_evidence_classification]
confidence: high
review_status: active_spec
relationship_count: 13
hub_score: 25
centrality: 0.117
updated: 2026-07-29
---

# Bourgain et al. 2022 – Golf Swing Biomechanics: A Systematic Review and Methodological Recommendations for Kinematics

> **Level 3 instrumented golf biomechanics.** Peer-reviewed systematic review (92 articles) of golf-swing kinematics, published in *Sports* 10(6): 91 (2022), DOI 10.3390/sports10060091, PMC9227529. Open access. This note is the canonical register for the review's claims; it complements [[dr_kwon_golfer_ground_interaction]] (primary research program) by supplying a cross-study methodological synthesis. It does not replace Level 1 anatomy, Level 2 general biomechanics, or Level 4 coaching interpretation, and it does not validate any 2D-video or MediaPipe proxy.

## Source Register

| Source ID | Primary source | Role and claim locator | Access result |
| :--- | :--- | :--- | :--- |
| `bourgain_2022_pmc` | [Golf Swing Biomechanics: A Systematic Review… (PMC9227529)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9227529/) | Abstract; §3.4 X-Factor; §3.5 Crunch Factor; §3.7 Kinematic Sequence; §4 Conclusions and Perspectives. | Full-text HTML read 2026-07-29; PDF in `raw/literature/`. |

## Terminology (as used by this source)

| Term | Evidence-safe meaning in this dossier |
| :--- | :--- |
| X-factor | The dissociation between the scapular (shoulder) and pelvic girdles, first introduced by McLean as the angle between the projections of a shoulder line (through both acromia) and a pelvis line (through both ASIS) in the horizontal plane. |
| X-factor stretch | Cheetham et al.'s variant: the same dissociation computed at the **beginning of the downswing** rather than at the transition between backswing and downswing; tends to be higher for golfers who begin the downswing by rotating the pelvis. |
| Crunch factor | The product of the torso's lateral-inclination angle and the axial-rotation speed of the torso relative to the pelvis, introduced as an injury-risk proxy for intervertebral-disc stress. |
| Kinematic sequence | The proximal-to-distal timing order of segmental rotational maxima during the downswing (pelvis → torso → shoulder girdles → arms → hands → club), borrowed from throwing-sport literature. |
| Swing plane / clubhead trajectory | The geometric description of the clubhead path; treated in the review as a kinematic construct. |

## Claim-Level Evidence

| Required distinction | Evidence-safe claim | Locator | Boundary |
| :--- | :--- | :--- | :--- |
| X-factor definition | The X-factor describes pelvis–thorax (pelvic vs. scapular girdle) rotational dissociation; the review confirms the vault's move away from "shoulder turn minus hip turn" as a sufficient definition. | §3.4.1 | The review notes the original "larger X-factor → better performance" belief is an assumption, not a finding; the vault must not treat a bigger X-factor as automatically better. |
| X-factor methodological non-consensus | Three studies (Brown et al.; Kwon et al.) showed X-factor values depend on the chosen computation method (which torso/pelvis lines and reference frames are used); there is no consensus on how to obtain the torso rotation. | §3.4.2 | X-factor values are not comparable across methods; the app must record its operational definition and not mix conventions. |
| X-factor stretch | X-factor stretch is computed at the start of the downswing and is higher for golfers who initiate the downswing with pelvis rotation — consistent with the vault's transition-phase treatment. | §3.4.1 (Cheetham et al.) | The review does not establish that more stretch is better; it remains a description of timing, not a target. |
| Crunch factor | The crunch factor combines torso lateral inclination with axial-rotation speed as a proposed lumbar-injury proxy. | §3.5.1 | Lindsay et al., Cole et al., and Joyce et al. reported **no correlation** between crunch factor and lumbar-injury risk; there is no consensus on its computation. It must not be reported as an injury diagnostic. |
| Kinematic sequence | The proximal-to-distal sequence (pelvis → torso → shoulder girdle → arms → hands → club) is considered in the literature as a candidate pattern for maximising clubhead speed, based on temporal additivity of velocities from throwing sports. | §3.7.1 | Nine articles defined a golf proximal-to-distal sequence, but the review does not establish it as a universal ideal for every golfer; the vault treats it as a population pattern, not an individual target. |
| Four-phase consensus | There is a consensus definition of the movement into four main phases: address, backswing, downswing, and follow-through. | §4 | This coarser consensus sits alongside the vault's finer six-phase model and the event-level [[golf_swing_events]] set; they are different granularities, not contradictions. |
| Cohort bias | Studies mainly focused on right-handed male golfers; there is a lack of research on women and left-handed players, and published comparisons show biomechanical sex differences. | §4 | Population reference ranges derived from this literature are male- and right-hand-dominant; individual baselines ([[personalised_movement_intelligence]]) remain essential. |
| Instrumentation | Three-dimensional optoelectronic motion-capture is the common approach for joint angular kinematics; International Society of Biomechanics recommendations are rarely followed and methodologies are often not fully described. | §4 | This is 3D instrumented evidence (Level 3). It does not license 2D-video proxies to claim measured kinematics; see [[golf_kinetics_observability_boundary]]. |
| Methodological standardisation | The lack of methodological consensus prevents generalisation and has produced contradictory results across studies; standardisation (including ISB conventions for segment/joint kinematics) is recommended. | Abstract; §4 | App metrics must state their operational definitions and camera/landmark requirements; cross-study numeric thresholds should not be imported as app targets. |

## What Bourgain et al. Directly Supports

- A cross-study synthesis of instrumented golf-swing kinematics, categorised into X-factor, crunch factor, swing plane/clubhead trajectory, kinematic sequence, and joint angular kinematics (Level 3).
- The pelvis–thorax dissociation framing of the X-factor and the existence of the X-factor-stretch timing variant — supporting the vault's refined [[x_factor]] treatment.
- The proximal-to-distal kinematic-sequence concept as a literature-described (not universal) pattern — supporting the cautious framing in [[kinematic_sequence]].
- The principle that metric values depend on operational definitions and methods — reinforcing the [[metric_evidence_classification]] rule that every metric must record its claim type and operational definition.

## What Bourgain et al. Does Not Directly Support

- It does not establish any 2D-video, MediaPipe, or landmark-derived metric as equivalent to 3D instrumented measurement.
- It does not validate "larger X-factor" or "more X-factor stretch" as better; it reports the belief and the methodological problems, not a causal performance law.
- It does not support using the crunch factor as an individual injury-risk score (the review itself reports null correlations with lumbar injury).
- It does not provide population reference ranges that generalise to women, left-handed golfers, or any specific individual.
- It does not make any fascial, myofascial-line, or tissue-loading claim; any mapping to [[functional_lines]] or the [[myofascial_interpretive_layer]] is engine synthesis and must be labelled as such.

## Relationships

| Relationship | Target | Evidence boundary |
| :--- | :--- | :--- |
| contains | [[x_factor]] | Level 3 synthesis of X-factor definitions, methods, and the stretch variant. |
| contains | [[kinematic_sequence]] | Level 3 synthesis of the proximal-to-distal sequence concept. |
| connects_to | [[golf_swing]] | Domain anchor. |
| connects_to | [[golf_swing_events]] | Four-phase consensus complements the finer event set. |
| connects_to | [[golf_movement_sequence]] | Segmental sequence evidence. |
| connects_to | [[golf_kinetics_observability_boundary]] | Reinforces the instrumented-vs-2D boundary. |
| connects_to | [[dr_kwon_golfer_ground_interaction]] | Kwon is one of the primary-research programs this review synthesises; the two Level 3 sources are complementary. |
| relevant_to | [[metric_evidence_classification]] | Source of the operational-definition / methodological-consensus principle. |

## Evidence Level

**Level 3 — Domain-Specific Instrumented Biomechanics (systematic review).** `source_role: domain_biomechanics`. The review can validate golf-specific kinematic constructs and methodological cautions. It does not replace Level 1 fascial anatomy, Level 2 general biomechanics, Level 4 coaching interpretation, or Level 5 app hypotheses.

## App Use

- Use the pelvis–thorax dissociation definition and the methodological-non-consensus finding to keep the app's X-factor metric labelled with its own operational definition and camera requirements.
- Treat the kinematic sequence as a descriptive population pattern; do not rank an individual against it as an ideal.
- Do not output the crunch factor as an injury risk from video; the source itself reports no injury correlation.
- State that any app threshold derived from this literature is male/right-hand biased and is a Level 5 hypothesis until individually validated.

## Open Questions

- Which of the reviewed X-factor computation methods is most robust to the app's camera views and landmark set, and how should the chosen operational definition be recorded?
- Can the proximal-to-distal sequence be described from 2D video as a timing order without claiming measured angular velocities?
- How should the vault represent the sex- and handedness-bias of the underlying cohorts in any future population-reference node?
