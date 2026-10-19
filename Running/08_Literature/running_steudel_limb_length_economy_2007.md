---
id: running_steudel_limb_length_economy_2007
canonical_id: literature.running.steudel_limb_length_economy_2007
type: Evidence Source
running_node_type: literature
evidence_level: 3
running_claim_level: literature
status: canonical
source_role: domain_biomechanics
preferred_name: "Literature - The evolution of human running: effects of changes in lower-limb length on locomotor economy"
aliases: [Steudel-Numbers et al. 2007, Lower limb length and economy]
domain: running
doi: "10.1016/j.jhevol.2007.04.001"
year: 2007
authors: ["Karen L. Steudel-Numbers", "Timothy D. Weaver", "Cara M. Wall-Scheffler"]
topic: "lower-limb length, stride dynamics, and locomotor economy"
source_url: "https://doi.org/10.1016/j.jhevol.2007.04.001"
directly_measured: false
camera_views: []
requires_clinical_correlation: false
confidence_required: contextual
related_nodes: []
source_nodes: []
relationships:
  supports: [running_body_proportion_comparison, running_running_economy]
  derived_from: [till_yes_running_literature_foundation]
confidence: high
review_status: claim_scope_audited_2026_10_19
relationship_count: 3
hub_score: 8
centrality: 0.04
updated: 2026-10-15
claim_audit: {"checked_on": "2026-10-19", "study_design": "cross_sectional", "verification_depth": "bibliographic_record_and_abstract", "permitted_scope": "Limb proportions/economy association; not recovery-knee folding or hip-flexor effort evidence.", "app_measurement_validation": "not_established", "athlete_specific_causation": "not_established", "record_url": "https://europepmc.org/article/MED/17574650"}
verified_bibliography: {"title": "The evolution of human running: effects of changes in lower-limb length on locomotor economy.", "authors": "Steudel-Numbers KL, Weaver TD, Wall-Scheffler CM.", "doi": "10.1016/j.jhevol.2007.04.001", "journal": "Journal of human evolution", "issue_date": "2007 Aug", "first_publication_date": "2007-06-14", "volume": "53", "pages": "191-196"}

---

# Literature - The evolution of human running: effects of changes in lower-limb length on locomotor economy

## Citation

Steudel-Numbers, K. L., Weaver, T. D., & Wall-Scheffler, C. M. (2007). *The evolution of human running: effects of changes in lower-limb length on locomotor economy*. Journal of Human Evolution, 53(2), 191–196. DOI: [10.1016/j.jhevol.2007.04.001](https://doi.org/10.1016/j.jhevol.2007.04.001).

## Topic

Evolutionary biomechanics, limb length ratios, stride kinematics, and running economy.

## Principal Relevant Findings

1. **Limb length vs. stride length**:
   - Longer limbs describe a longer arc for a given angular excursion ($s = r \cdot \theta$), but relative leg length correlates with cost of transport, **not simply or automatically with stride length**.
   - Running stride length is governed by complex dynamic factors: cadence, ground reaction impulse, vertical stiffness, stance compliance, and flight velocity. Longer legs do not guarantee longer strides.
2. **Individual anthropometric scaling**:
   - Kinematic excursions must be interpreted relative to an athlete's body proportions (stature, limb ratios) rather than through fixed absolute distance metrics.

## Limitations and Evidence Boundaries

- Group evolutionary and laboratory treadmill analysis; cannot predict individual marathon performance from leg length alone.
- 2D camera perspective distorts perceived limb lengths under varying out-of-plane rotation.

## Nodes Supported

- [[running_body_proportion_comparison]]
- [[running_running_economy]]
- [[running_swing_knee_inertia]] — excluded attribution: this study does not directly test recovery-knee flexion/inertia.

## Application Implication

Informs TillYes body-proportion normalization guardrails: long limbs produce larger linear tip velocities and longer arc paths at identical joint angles, but do not prove greater propulsion or overstriding without event-aligned landing coordinates.

## Review Status

Primary abstract verified; this audit does not claim a full-text data extraction.


## Handoff audit R11 (2026-10-16)
Contribution: 3 · observational anthropometry/economy. Verification: Primary abstract. Reasoning destination: [[running_body_proportion_comparison]]. Audit: [[running_research_handoff_audit]].

## Attribution correction — 2026-10-19
Do not cite this paper for compact recovery-knee folding, reduced swing-leg inertia or reduced hip-flexor effort. Those were mismatched app claims. The arc-length equation above is general geometry, not an experimental finding from this paper. For the general knee-flexion mechanism use [[running_swing_knee_inertia]] and its synthesis source. No specific athlete or TillYes measurement is validated here.

## Claim applicability audit — 2026-10-19
Limb proportions/economy association; not recovery-knee folding or hip-flexor effort evidence.

Verification and citation metadata are recorded in `claim_audit` above. Consult [[running_literature_claim_audit_2026_10_19]] and [[running_reasoning_retrieval_index]] before exporting a research-backed statement.
