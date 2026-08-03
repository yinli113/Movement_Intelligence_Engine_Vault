# Connective Structure Hub Report

> **Historical project report (2026-07-13) — paths and metric values are superseded.** This documents Graph Architecture v2 (connective tissues as first-class nodes); that architecture is in place, and the five hub structures listed exist today under `02_Body_Structures/connective_structures/`.
>
> **Folder mapping then → now:** `wiki/connective_structures/` → `02_Body_Structures/connective_structures/`.
>
> **Metric values:** the hub scores, relationship counts, centrality values, and the "Top 20 Graph Hubs" table below are a **2026-07-13 snapshot**; they are recomputed by `scripts/update_graph_metrics.py` and are not maintained inside this report.
>
> The body below is kept as the original record and has **not** been rewritten.

## Purpose

This report documents Graph Architecture v2: connective tissues are now first-class graph nodes for movement reasoning and force transmission.

The goal is not to replace muscle nodes. The goal is to let the graph reason through structures that transmit, constrain, and distribute force across muscles, joints, fascial lines, compensations, assessments, and exercises.

## What Changed

- Added primary node type: `Connective Structure`.
- Added subtypes: `Fascia`, `Ligament`, `Tendon`, `Aponeurosis`, `Retinaculum`, `Joint Capsule`, and other connective tissues.
- Added template: `[[connective_structure_template]]`.
- Added initial folder: `wiki/connective_structures/`.
- Created first five hub structures:
  - [[sacrotuberous_ligament]]
  - [[thoracolumbar_fascia]]
  - [[plantar_fascia]]
  - [[nuchal_ligament]]
  - [[iliotibial_tract]]
- Added graph metrics to wiki nodes:
  - `relationship_count`
  - `hub_score`
  - `centrality`
  - `confidence`
  - `review_status`
- Added updater script: `scripts/update_graph_metrics.py`.

## Hub Score Method

Hub Score is a reasoning-priority heuristic, not a clinical score.

Current formula:

```text
hub_score =
  relationship_count
  + inbound_relationship_count
  + 3 * connected_fascial_line_count
  + 2 * connected_muscle_count
  + 4 * connected_golf_phase_count
  + 3 * connected_assessment_count
  + 3 * connected_limitation_or_compensation_count
```

`centrality` is currently normalized relationship count against the most connected node in the vault.

## Current Connective Structure Hub Ranking

Only five Connective Structure nodes currently exist, so this is the complete current connective-structure ranking.

| Rank | Node | Relationship Count | Hub Score | Centrality | Notes |
|---:|---|---:|---:|---:|---|
| 1 | [[plantar_fascia]] | 13 | 40 | 0.289 | Strong foot-to-line bridge for [[toe_loading]]. |
| 2 | [[nuchal_ligament]] | 12 | 35 | 0.267 | Neck/head bracing bridge; lower source confidence. |
| 3 | [[thoracolumbar_fascia]] | 14 | 34 | 0.311 | Cross-body force-transfer hub despite lower current inbound count. |
| 4 | [[iliotibial_tract]] | 11 | 30 | 0.244 | Lateral line, hip, and knee force-transmission bridge. |
| 5 | [[sacrotuberous_ligament]] | 10 | 28 | 0.222 | Posterior pelvic and posterior-chain bridge; needs source locator review. |

## Top 20 Current Graph Hubs

This is the computed top 20 across all current node types. It shows where the existing graph is dense today, not where the final architecture should end.

| Rank | Node | Type | Relationship Count | Hub Score | Centrality |
|---:|---|---|---:|---:|---:|
| 1 | [[deep_front_line]] | Fascial Line | 45 | 145 | 1.000 |
| 2 | [[hip_joint]] | Joint | 31 | 112 | 0.689 |
| 3 | [[thoracic_spine]] | Joint | 27 | 111 | 0.600 |
| 4 | [[spiral_line]] | Fascial Line | 40 | 110 | 0.889 |
| 5 | [[lateral_line]] | Fascial Line | 35 | 100 | 0.778 |
| 6 | [[cervical_spine]] | Joint | 23 | 99 | 0.511 |
| 7 | [[superficial_back_line]] | Fascial Line | 32 | 96 | 0.711 |
| 8 | [[functional_lines]] | Fascial Line | 31 | 85 | 0.689 |
| 9 | [[shoulder_joint]] | Joint | 22 | 84 | 0.489 |
| 10 | [[knee_joint]] | Joint | 21 | 82 | 0.467 |
| 11 | [[hip_internal_rotation]] | mechanic | 22 | 78 | 0.489 |
| 12 | [[ankle_joint]] | Joint | 20 | 77 | 0.444 |
| 13 | [[lumbar_spine]] | Joint | 18 | 76 | 0.400 |
| 14 | [[toe_loading]] | Movement Pattern | 23 | 72 | 0.511 |
| 15 | [[thoracic_rotation]] | mechanic | 17 | 64 | 0.378 |
| 16 | [[neck_tension]] | Compensation | 19 | 62 | 0.422 |
| 17 | [[golf_swing_transition]] | Golf Phase | 18 | 61 | 0.400 |
| 18 | [[hip_flexion]] | mechanic | 15 | 58 | 0.333 |
| 19 | [[anatomy_trains_myofascial_thomas_w_myers]] | Evidence Source | 17 | 55 | 0.378 |
| 20 | [[hip_extension]] | mechanic | 14 | 54 | 0.311 |

## Connective Structures Already Present as Mentions

These terms are already present in source notes, graph notes, or the Myers PDF extraction context and should be candidates for future first-class nodes.

1. [[thoracolumbar_fascia]] - created
2. [[sacrotuberous_ligament]] - created
3. [[plantar_fascia]] - created
4. [[nuchal_ligament]] - created
5. [[iliotibial_tract]] - created
6. Achilles tendon - mentioned in Myers PDF extraction around plantar fascia/SBL context
7. Palmar aponeurosis - listed as a future example, not yet represented as a node
8. Rectus sheath - present in Myers Functional Line/Deep Front Line extraction context
9. Sacral fascia - present in Myers Functional Line extraction context
10. Lumbodorsal fascia - present as alias/evidence context for [[thoracolumbar_fascia]]
11. Endothoracic fascia - present in Deep Front Line extraction context
12. Intercostal layers - present in [[lateral_line]] and Myers extraction context
13. Pelvic floor - present in [[julie_hammond_breakout]]
14. Hyoid complex - present as hyoids in [[julie_hammond_breakout]]
15. TMJ - listed as a high-priority architecture example, not yet represented as a node
16. Joint capsule - new subtype category, not yet represented as a specific node
17. Retinaculum - new subtype category, not yet represented as a specific node
18. Plantar aponeurosis - alias candidate for [[plantar_fascia]]
19. IT band - alias for [[iliotibial_tract]]
20. Thoracic inlet fascia - implied by Deep Front Line extraction context; needs source review

## Reasoning Implications

Preferred graph traversal should now include connective structures:

```text
Movement Pattern
-> Joint Action
-> Muscle
-> Connective Structure
-> Fascial Line
-> Compensation
-> Assessment
-> Exercise
```

Example golf traversal:

```text
[[trail_shoulder_external_rotation]]
-> [[latissimus_dorsi]]
-> [[thoracolumbar_fascia]]
-> [[functional_lines]]
-> [[hip_internal_rotation]]
-> [[toe_loading]]
-> [[plantar_fascia]]
```

## Next Conversion Pass

Prioritize these next connective nodes if the MVP needs more force-transmission depth:

1. Diaphragm as a hub structure, even though it is currently a Muscle note.
2. Pelvic Floor as a Connective Structure or Movement Support Complex.
3. Hyoid Complex for jaw/neck/breathing relationships.
4. Achilles Tendon for foot-to-posterior-chain transfer.
5. Rectus Sheath for Functional Line and Deep Front Line relationships.
6. Sacral Fascia as either alias or separate node from [[thoracolumbar_fascia]].
7. Endothoracic Fascia for Deep Front Line and breathing mechanics.
8. TMJ for jaw clenching and head-neck compensation reasoning.
