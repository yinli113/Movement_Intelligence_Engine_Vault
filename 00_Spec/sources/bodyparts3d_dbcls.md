---
id: bodyparts3d_dbcls
type: Evidence Source
preferred_name: "BodyParts3D (DBCLS)"
aliases: [BodyParts3D, Anatomography, DBCLS BodyParts3D]
short_definition: "Curated open-access 3D anatomical model database and dictionary developed by DBCLS, mapped to Foundational Model of Anatomy (FMA) ontology IDs."
author: Database Center for Life Science (DBCLS), Research Organization of Information and Systems, Japan
publication_year: 2011
format: open_access_3d_database
license: CC BY-SA 2.1 JP
domain: 3d_computational_anatomy
evidence_level: 1
source_role: foundational_anatomical_framework
confidence: high
review_status: active_spec
relationships:
  cited_by: []
  connects_to: []
relationship_count: 1
hub_score: 2
centrality: 0.009
updated: 2026-09-07
---

# BodyParts3D (DBCLS)

## Source Role

BodyParts3D is a freely accessible anatomical dictionary and database of 3D human body models developed by the Database Center for Life Science (DBCLS, Japan). It serves as the bridge between:
1. **The Semantic Knowledge Graph**: Grounding muscle, joint, bone, and connective structure nodes in computable **Foundational Model of Anatomy (FMA)** concept IDs.
2. **The 3D Visualization Pipeline**: Supplying standardized 3D polygon meshes ( / ) for  (Blender-based movement and myofascial visualizer).

## Key Characteristics

- **Ontology Grounding**: Every geometric mesh is bound directly to an FMA identifier (e.g., FMA:22442 for Vastus lateralis).
- **Hierarchical Tree Structure**: Models can be aggregated from microscopic/segmental elements up to whole functional systems and kinetic chains.
- **Topological Consistency**: Preserves mutual surface boundaries and contact interfaces between muscles, bones, and surrounding fascial planes.

## Applications in TillYes Workspace

- ****: Direct import of BodyParts3D segment meshes into Blender to render Anatomy Trains myofascial lines (e.g. SBL, SFL, LL, SPL, BFL, FFL, DFL, Arm Lines).
- **Geometric Landmark Validation**: Extracting 3D centroid vectors and attachment coordinates for origin-to-insertion lines of action.
