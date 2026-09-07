---
id: perry_burnfield_gait_analysis
type: Evidence Source
preferred_name: "Perry & Burnfield – Gait Analysis: Normal and Pathological Function"
aliases: [Perry Burnfield, Perry Gait Analysis, Gait Analysis Normal and Pathological Function, Perry 1992, Burnfield 2010]
short_definition: "Level 1 foundational gait taxonomy (eight-phase gait model) cited via Chambers & Sutherland, which presents Perry's phase nomenclature. The full Perry & Burnfield text is NOT yet in the vault; this note is a framework-level citation, not a page-reviewed source. It complements Chambers & Sutherland (observational/observability-boundary) as the gait domain's phase-taxonomy foundation."
author: Jacquelin Perry
contributors: [Judith M. Burnfield]
publication_year: 2010
publisher: Slack Incorporated (2nd ed.; 1st ed. Perry 1992)
format: framework_cited
status: reviewed
review_basis: framework_cited_via_chambers_sutherland
evidence_level: 1
source_role: foundational_domain_taxonomy
domain: gait
is_framework_cited: true
relationships:
  cited_via: [chambers_sutherland_gait_analysis_2002]
  contains: [initial_contact, loading_response, mid_stance, terminal_stance, preswing, initial_swing, midswing, terminal_swing]
  connects_to: [gait_cycle, stance_phase, swing_phase, gait_observability_boundary, observational_gait_analysis]
  supported_by: [chambers_sutherland_gait_analysis_2002]
  relevant_to: [gait_cycle, stance_phase, swing_phase]
confidence: medium
review_status: generated_legacy_needs_review
relationship_count: 21
hub_score: 35
centrality: 0.189
updated: 2026-07-24
---

# Perry & Burnfield – Gait Analysis: Normal and Pathological Function

> **Framework-cited Level 1 source.** The full Perry & Burnfield text is **not yet in the vault** (no PDF). This note is elevated to Level 1 because the **eight-phase gait model** is foundational to the engine's gait reasoning, and it is cited via [[chambers_sutherland_gait_analysis_2002]], which presents Perry's phase nomenclature (Chambers & Sutherland p.2, Table 2). No page-locator claims are made against Perry & Burnfield directly; all such claims are traced to Chambers & Sutherland (read in full) until the Perry & Burnfield PDF is obtained and reviewed. Do not treat this note as a page-reviewed source.

## Source Role

This source is a **Level 1 foundational framework** for the gait domain, with `source_role: foundational_domain_taxonomy`. It supplies the **eight-phase gait model** — the clinically standard phase taxonomy (Initial Contact, Loading Response, Mid Stance, Terminal Stance, Preswing, Initial Swing, Mid Swing, Terminal Swing) — that the engine uses as its fine-grained gait phase frame.

It **complements** [[chambers_sutherland_gait_analysis_2002]], which remains the Level 1 source for the **observational-vs-instrumented observability boundary** and the coarser three-period/three-phase framing. The two gait Level 1 sources have distinct roles:
- **Chambers & Sutherland** (`foundational_domain_taxonomy`) — observational gait structure + observability boundary (read in full).
- **Perry & Burnfield** (`foundational_domain_taxonomy`) — eight-phase gait taxonomy (framework-cited via Chambers; full text not yet in vault).

## Why Level 1 (and the caveat)

Level 1 means **foundational to the engine's reasoning**, not "highest-quality evidence" and not a page-reviewed gold-standard reference. The eight-phase model is foundational because it is the canonical phase taxonomy the engine reasons with. However, because the full text is not in the vault, this source note is **framework-cited**: claims that require page locators are traced to Chambers & Sutherland (which presents Perry's phases) until the Perry & Burnfield PDF is obtained. When the PDF is added, this note should be upgraded to a full page-reviewed source note (with `review_basis` changed and page locators added).

## Source-derived model (eight phases)

The Perry eight-phase model divides the [[gait_cycle]] (0-100%) into:

- **Stance (~0-60%):**
  - [[initial_contact]] — 0% (instant of foot strike).
  - [[loading_response]] — ~0-10% (weight acceptance, double-limb support).
  - [[mid_stance]] — ~10-30% (single-limb stance, body over the foot).
  - [[terminal_stance]] — ~30-50% (heel rise, roll-over).
  - [[preswing]] — ~50-60% (toe-off preparation, double-limb support).
- **Swing (~60-100%):**
  - [[initial_swing]] — ~60-73% (limb acceleration, knee flexion).
  - [[midswing]] — ~73-87% (foot clearance, limb passes stance limb).
  - [[terminal_swing]] — ~87-100% (limb deceleration, positioning for next strike).

The three swing phases are already represented as reviewed nodes (supported by Chambers & Sutherland, which uses the same swing-phase names). The five stance phases are added here as the fine-grained Perry taxonomy; they map onto the coarser Chambers three-period model (see each node's "Mapping" section).

## Joint involvement

Whole lower limb across the phases; phase-specific joint roles are detailed in each child phase node.

## Muscle involvement

No muscle claims from this source note; muscle activity is the [[gait_emg]] category and requires instrumentation.

## Movement or phase relationships

Parent of the eight phase nodes (A via Chambers); complements the [[stance_phase]]/[[swing_phase]] coarse framing (A); bounded by [[gait_observability_boundary]] (A).

## Possible myofascial relationships

None directly. Mapping gait phases to fascial lines is an engine synthesis (C).

## What a 2D app can observe

- Phase boundaries (foot strike, toe-off) and the eight-phase timing from a 2D side view, as descriptors.

## What the app must not infer

- Kinetics, EMG, foot pressure, energetics, or causal etiology (each requires instrumentation).
- That this source note is page-reviewed — it is framework-cited only.

## Related concepts

[[gait_cycle]], [[stance_phase]], [[swing_phase]], [[initial_contact]], [[loading_response]], [[mid_stance]], [[terminal_stance]], [[preswing]], [[initial_swing]], [[midswing]], [[terminal_swing]], [[gait_observability_boundary]], [[observational_gait_analysis]], [[chambers_sutherland_gait_analysis_2002]].

## Sources

- [[chambers_sutherland_gait_analysis_2002]] — p.2 (Table 2) presents Perry's phase nomenclature; the eight-phase model is cited via this read-in-full source.
- Perry J, Burnfield JM. *Gait Analysis: Normal and Pathological Function.* 2nd ed. Slack Incorporated, 2010 (1st ed. Perry 1992). **Not yet in the vault.**

## Evidence-separation rules

- **(A)** The eight-phase model and phase names — cited via Chambers & Sutherland (read in full), which presents Perry's phase nomenclature. No direct page-locator claims against Perry & Burnfield.
- **(B)** Cross-links to [[chambers_sutherland_gait_analysis_2002]], [[gait_observability_boundary]] — same Level 1 domain.
- **(C)** Any fascial-line mapping of a gait phase is `engine_synthesis` and must be labelled.
- **Caveat:** This is a framework-cited Level 1 source. Upgrade to a full page-reviewed source note when the PDF is obtained.
