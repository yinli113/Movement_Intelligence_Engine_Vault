---
id: bodyparts3d_fma_mapping
type: Spec
preferred_name: "BodyParts3D & FMA 3D Mesh Mapping Spec"
aliases: ["BodyParts3D Mapping", "FMA 3D Mapping", "MotionFlow 3D Spec"]
short_definition: "Technical specification mapping vault muscle and connective structure nodes to BodyParts3D polygon mesh concepts and FMA ontology IDs for 3D visualization in motionflow_anatomy_studio."
relationships:
  governs: ["motionflow_anatomy_studio"]
  connects_to: ["bodyparts3d_dbcls", "openstax_anatomy_physiology_2e", "anatomy_trains_myofascial_thomas_w_myers"]
evidence_level: 1
source_role: foundational_anatomical_framework
confidence: high
review_status: active_spec
relationship_count: 54
hub_score: 148
centrality: 0.486
updated: 2026-09-07
---

# BodyParts3D & FMA 3D Mesh Mapping Spec

## 1. Overview & Purpose

This specification defines the 3D computational asset pipeline connecting the **TillYes Movement Intelligence Knowledge Graph** to **motionflow_anatomy_studio** (Blender-based 3D educational and myofascial visualizer).

Every anatomical node in the vault maintains:
- **fma_id**: Standard Foundational Model of Anatomy ontology identifier (e.g. ).
- **bodyparts3d_id**: Standard BodyParts3D (DBCLS) 3D mesh concept identifier (e.g. ).

By grouping discrete BodyParts3D polygon meshes according to Thomas Myers Anatomy Trains tracks,  can dynamically construct, shade, and animate complete myofascial force-transmission lines.

---

## 2. Myofascial Line 3D Mesh Composition Matrix

### 1. Superficial Back Line (SBL)
| Track / Station | Muscle / Structure Node | FMA ID | BodyParts3D Concept | 3D Blender Sub-Mesh |
|---|---|---|---|---|
| Plantar track | [[flexor_digitorum_brevis]] | FMA:45183 | BP3D:FMA45183 | FDB_L, FDB_R |
| Plantar fascia | [[plantar_fascia]] | FMA:45184 | BP3D:FMA45184 | PlantarAponeurosis |
| Posterior lower leg | [[gastrocnemius]] | FMA:22541 | BP3D:FMA22541 | Gastrocnemius_Med, Lat |
| Deep posterior calf | [[soleus]] | FMA:22542 | BP3D:FMA22542 | Soleus_L, Soleus_R |
| Posterior thigh | [[biceps_femoris_long_head]] | FMA:22357 | BP3D:FMA22357 | BicepsFemoris_LH |
| Medial hamstrings | [[semitendinosus]] / [[semimembranosus]] | FMA:22360 / FMA:22359 | BP3D:FMA22360 | Semitendinosus, Semimembranosus |
| Pelvic ligament | [[sacrotuberous_ligament]] | FMA:21486 | BP3D:FMA21486 | SacrotuberousLigament |
| Erector column | [[iliocostalis]], [[longissimus]], [[spinalis]] | FMA:71300, FMA:71301, FMA:71302 | BP3D:FMA71300 | ErectorSpinae_Group |
| Cranial cap | [[occipitofrontalis]] | FMA:46755 | BP3D:FMA46755 | EpicranialAponeurosis |

---

### 2. Superficial Front Line (SFL)
| Track / Station | Muscle / Structure Node | FMA ID | BodyParts3D Concept | 3D Blender Sub-Mesh |
|---|---|---|---|---|
| Dorsal foot extensors | [[extensor_digitorum_longus]], [[extensor_hallucis_longus]] | FMA:22533, FMA:22534 | BP3D:FMA22533 | EDL, EHL |
| Anterior crural | [[tibialis_anterior]] | FMA:22532 | BP3D:FMA22532 | TibialisAnterior_L/R |
| Anterior thigh | [[rectus_femoris]] | FMA:22430 | BP3D:FMA22430 | RectusFemoris_L/R |
| Anterior abdominal | [[rectus_abdominis]] | FMA:9628 | BP3D:FMA9628 | RectusAbdominis |
| Sternal / Neck | [[sternocleidomastoid]] | FMA:13407 | BP3D:FMA13407 | SCM_Sternal, SCM_Clavicular |

---

### 3. Lateral Line (LL)
| Track / Station | Muscle / Structure Node | FMA ID | BodyParts3D Concept | 3D Blender Sub-Mesh |
|---|---|---|---|---|
| Lateral crural | [[peroneus_longus]], [[peroneus_brevis]] | FMA:22538, FMA:22539 | BP3D:FMA22538 | PeroneusLongus, Brevis |
| Lateral fascial band | [[iliotibial_tract]] | FMA:51048 | BP3D:FMA51048 | IT_Band_L/R |
| Lateral pelvis | [[tensor_fasciae_latae]], [[gluteus_medius]] | FMA:22429, FMA:22354 | BP3D:FMA22429 | TFL, GluteusMedius |
| Lateral abdominal wall | [[external_oblique]], [[internal_oblique]] | FMA:13397, FMA:13398 | BP3D:FMA13397 | ExternalOblique, InternalOblique |
| Thoracic / Neck | [[intercostals]], [[splenius_capitis]] | FMA:71310, FMA:22704 | BP3D:FMA71310 | Intercostals_Lateral, SpleniusCapitis |

---

### 4. Back Functional Line (BFL)
| Track / Station | Muscle / Structure Node | FMA ID | BodyParts3D Concept | 3D Blender Sub-Mesh |
|---|---|---|---|---|
| Upper posterior limb | [[latissimus_dorsi]] | FMA:13404 | BP3D:FMA13404 | LatissimusDorsi_L/R |
| Fascial bridge | [[thoracolumbar_fascia]] | FMA:20448 | BP3D:FMA20448 | ThoracolumbarFascia_Dorsal |
| Contralateral pelvis | [[gluteus_maximus]] | FMA:22353 | BP3D:FMA22353 | GluteusMaximus_Contra |
| Lateral knee continuation | [[vastus_lateralis]] | FMA:22431 | BP3D:FMA22431 | VastusLateralis_Contra |

---

### 5. Front Functional Line (FFL)
| Track / Station | Muscle / Structure Node | FMA ID | BodyParts3D Concept | 3D Blender Sub-Mesh |
|---|---|---|---|---|
| Anterior chest | [[pectoralis_major]] | FMA:9625 | BP3D:FMA9625 | PectoralisMajor_L/R |
| Abdominal fascial sheath | [[rectus_abdominis]] | FMA:9628 | BP3D:FMA9628 | RectusSheath_Anterior |
| Contralateral inner thigh | [[adductor_longus]] | FMA:22439 | BP3D:FMA22439 | AdductorLongus_Contra |

---

### 6. Deep Front Line (DFL)
| Track / Station | Muscle / Structure Node | FMA ID | BodyParts3D Concept | 3D Blender Sub-Mesh |
|---|---|---|---|---|
| Deep posterior crural | [[tibialis_posterior]], [[flexor_hallucis_longus]], [[flexor_digitorum_longus]] | FMA:45169, FMA:45168, FMA:45167 | BP3D:FMA45169 | TibPost, FHL, FDL |
| Deep knee capsule | [[popliteus]] | FMA:22543 | BP3D:FMA22543 | Popliteus_L/R |
| Deep adductor complex | [[adductor_magnus]], [[adductor_brevis]], [[pectineus]], [[gracilis]] | FMA:22441, FMA:22440, FMA:22438 | BP3D:FMA22441 | AdductorMagnus_Brevis |
| Pelvic core / Iliopsoas | [[psoas_major]], [[iliacus]], [[quadratus_lumborum]] | FMA:18060, FMA:22310, FMA:15570 | BP3D:FMA18060 | PsoasMajor, Iliacus, QL |
| Core diaphragm | [[diaphragm]], [[transversus_abdominis]] | FMA:13295, FMA:15572 | BP3D:FMA13295 | Diaphragm_Dome, TransversusAbdominis |
| Deep anterior cervical | [[scalenes]], [[longus_colli]], [[longus_capitis]] | FMA:71306, FMA:46314, FMA:46313 | BP3D:FMA71306 | Scalenes_Group, PrevertebralMuscles |
| Craniofacial terminus | [[masseter]], [[temporalis]] | FMA:49006, FMA:49007 | BP3D:FMA49006 | Masseter, Temporalis |

---

## 3. Blender Python Integration Architecture

In , meshes tagged with  can be grouped into line collections dynamically via Blender Python (bpy).
