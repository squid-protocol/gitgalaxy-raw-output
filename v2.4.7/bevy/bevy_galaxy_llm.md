# ARCHITECTURAL_BRIEF: bevy
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/bevy` |
| **Timestamp** | `2026-08-07T03:47:02.726702+00:00` |
| **Scan Duration** | `7.69s` |
| **Git Branch** | `main` |
| **Git Commit** | `c7f779b8425e6bd110a5b6be28152206d139367b` |
| **Git Remote** | `https://github.com/bevyengine/bevy.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 1732 malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are a Senior Technical Storyteller and Codebase Architect. GitGalaxy has translated the non-visual architecture of this repository into measurable Structural Signatures (regex-derived counts, not an AST or compiler pass). Your job is to weave those signatures into a coherent, factual narrative about how this system is built -- its architecture, design patterns, and complexity -- not to render a verdict.
> 
> **CORE DIRECTIVES:**
> 1. **Narrate the Architecture, Don't Judge the Author:** Frame every observation as a blameless description of the system's physical reality. High Risk Exposure (e.g., Cognitive Load Exposure) describes where the architecture may be drifting into fragile territory, not developer incompetence -- it is a prompt to investigate, never a verdict.
> 2. **The Physical Reality Rule:** Base your narrative strictly on the provided Structural Signatures and the numbers derived from them. Do not hallucinate meaning, and do not restate a heuristic's raw label (e.g. a 'Logic Bomb' or 'O(2^N)' flag) as a confirmed finding of malice or a guaranteed defect -- explain what the signature actually measures, weave it into the story of the file, and let the reader draw their own conclusion.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`. Tell that balance as part of the narrative, not as an isolated alarm.
> 
> **THE STRUCTURAL SIGNATURE LEXICON:**
> * **Structure & Mass:** `branch` (splits), `linear` (paths), `args` (coupling), `func_start` (entry points).
> * **Risk & Volatility:** `danger` (dynamic execution), `flux` (state mutation), `graveyard` (commented-out logic), `safety_neg` (security bypasses).
> * **Architecture & Domain:** `io` (network latency), `concurrency` (async orchestration), `api` (public surface), `import` (dependencies).
> * **Defensive Guardrails:** `safety` (Error handling), `freeze_hits` (immutability), `cleanup` (state destruction).
## 2. THE 13-POINT RISK EXPOSURE ANALYSIS (EQUATIONS & CONTEXT)
> **How the SAST Engine Calculates Risk Exposure (Lower Risk 0 - Higher Risk Exposure 100%):**
> Most scores use a Sigmoid curve based on density (Hits / LOC) to prevent massive files from mathematically hiding their flaws.
> 
> 1. **Cognitive Load Exposure:** Measures the mental effort required for a developer to read and understand the file. `Density(Branches + (Flux * 2) + Async/Danger)` mitigated by `Doc Coverage`.
> 2. **Error & Exception Risk Exposure:** Measures structural integrity and resilience against runtime errors. `Net Exposure = (Danger + Safety_Neg + Flux) - (Safety + Tests + Docs)`.
> 3. **Tech Debt Exposure:** Measures the density of developer-annotated structural stress. `Density(TODOs [1x] + FIXMEs/Hacks [3x] + Empty Stubs [0.5x])`.
> 4. **Verification Risk Exposure:** Evaluates test coverage by comparing a function's structural complexity against the scope of the tests validating it.
> 5. **API Risk Exposure:** Measures the public surface area of a module. `Ratio(API Hits / Total Functions & Classes)`.
> 6. **Concurrency Risk Exposure:** Measures the density of asynchronous operations, threading, and parallel execution logic.
> 7. **State Flux Risk Exposure:** Measures the frequency of data mutation and variable reassignment.
> 8. **Commented Logic (dead code):** Measures the presence of abandoned, commented-out logic blocks.
> 9. **Spec Match Risk Exposure:** Measures how closely code aligns with formal specifications or architectural requirements.
> 10. **Stability:** Measures the recency of edits relative to the repository's entire lifespan.
> 11. **Deep Churn:** Measures the historical volatility and frequency of modification.
> 12. **Documentation Risk Exposure:** Measures the lack of structured documentation and ownership metadata.
> 13. **Indentation Consistency:** Measures formatting alignment (Tabs vs. Spaces). Provided for codebase standardization context, not a functional risk.
> 
> **--- THE SECURITY & VULNERABILITY LENS ---**
> 14. **Obfuscation & Evasion Risk:** Measures the density of obfuscated logic, packed strings, and non-standard encoding.
> 15. **Logic Bomb / Sabotage Risk:** Measures condition-heavy execution leading to destructive OS, memory, or process commands.
> 16. **Injection Surface Risk Exposure:** Measures external network/I/O input flowing directly into dynamic execution contexts (XSS, SQLi, RCE).
> 17. **Memory Corruption Risk Exposure:** Measures the density of raw pointer math and manual memory allocations (Buffer Overflows, UAF).
> 18. **Secrets Risk Exposure:** Measures the presence of hardcoded credentials exposed to logs or globals.
> 
> **--- STRUCTURAL MAGNITUDE (NOT RISK) ---**
> **19. Function Magnitude (Impact Score):** Measures the physical footprint and 'heaviness' of a specific function. `((BranchHits + 1) * (Args + 1) + (0.05 * LOC)) * 10`. This is NOT a risk score.
> **20. File Magnitude (Total Impact):** Measures the total structural impact of a file. `Sum(Function Impacts) + API + Concurrency + Flux + (LOC / 50)`. This is NOT a risk score.

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 2836 |
| Analyzed Artifacts (Scanned) | 2043 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 793 |
| Total LOC | 324963 |
| Volatility Index | 0.002 |
| % Scanned of codebase = | 72.0% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7875 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2823 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.6225 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 16 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUST | 1709 | 324430 | 83.7% |
| MARKDOWN | 152 | 0 | 7.4% |
| PLAINTEXT | 135 | 0 | 6.6% |
| XML | 23 | 0 | 1.1% |
| BINARY_THREAT | 11 | 11 | 0.5% |
| MAKEFILE | 2 | 21 | 0.1% |
| CPP | 2 | 0 | 0.1% |
| JAVA | 2 | 52 | 0.1% |
| SHELL | 2 | 244 | 0.1% |
| BATCH | 2 | 134 | 0.1% |
| GROOVY | 2 | 44 | 0.1% |
| HTML | 1 | 27 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `3.499`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 659 | 32.3% |
| file_cluster_13 | 351 | 17.2% |
| file_cluster_0 | 299 | 14.6% |
| file_cluster_16 | 294 | 14.4% |
| file_cluster_4 | 105 | 5.1% |
| file_cluster_6 | 14 | 0.7% |
| Unknown | 11 | 0.5% |
| file_cluster_17 | 8 | 0.4% |
| file_cluster_7 | 6 | 0.3% |
| file_cluster_11 | 6 | 0.3% |
| file_cluster_9 | 2 | 0.1% |
| file_cluster_1 | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 287 | 14.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 793*

**Composition by Extension & Reason:**
- `.png`: 237x Excluded (Explicitly Denied Extension: '.png')
- `.wgsl`: 154x Unsupported Format (.wgsl), 37x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 88x Unsupported Format (.toml), 8x Excluded (Unsupported Extension: '.toml'), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.stderr`: 41x Excluded (Unsupported Extension: '.stderr'), 3x Unsupported Format (.stderr)
- `.svg`: 30x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ktx2`: 20x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 6x Excluded (Binary Format Detected)
- `no_extension`: 19x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 17x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 133 LOC), 1x Excluded (Machine-Generated Source Code Signature: 4 LOC)
- `.yml`: 18x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.glb`: 14x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.gltf`: 14x Excluded (Explicitly Denied Extension: '.gltf')
- `.ron`: 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ttf`: 9x Excluded (Explicitly Denied Extension: '.ttf')
- `.jpg`: 8x Excluded (Explicitly Denied Extension: '.jpg')
- `.patch`: 7x Unsupported Format (.patch)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 17.7 | 9.7 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.9 | 38.9 | 41.9 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 37.1 | 9.9 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 8.3 | 2.3 | 0.0 |
| API Exposure | 0.0 | 12.8 | 2.8 | 3.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 28.5 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 35.1 | 12.2 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 6.4 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 94.0 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 6.6 | 1.3 | 0.6 | 0.0 |
| Volatility Exposure | 0.0 | 89.2 | 12.8 | 7.3 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 18.3 | 13.4 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `crates/bevy_asset/src/io/file/sync_file_asset.rs` (Hits: 26)
- `crates/bevy_asset/src/io/mod.rs` (Hits: 16)
- `examples/mobile/android_example/gradlew` (Hits: 14)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **vec.rs** (`crates/bevy_reflect/src/impls/alloc/vec.rs`) — 29 inbound connections
2. **uniform_buffer.rs** (`crates/bevy_render/src/render_resource/uniform_buffer.rs`) — 23 inbound connections
3. **format.rs** (`tools/ci/src/commands/format.rs`) — 12 inbound connections
4. **tokens.rs** (`crates/bevy_feathers/src/tokens.rs`) — 8 inbound connections
5. **observe.rs** (`crates/bevy_ui_widgets/src/observe.rs`) — 4 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **mesh.rs** (`crates/bevy_pbr/src/render/mesh.rs`) — 159 outbound dependencies
2. **mod.rs** (`crates/bevy_ecs/src/world/mod.rs`) — 156 outbound dependencies
3. **mod.rs** (`crates/bevy_gltf/src/loader/mod.rs`) — 142 outbound dependencies
4. **mod.rs** (`crates/bevy_render/src/render_resource/mod.rs`) — 140 outbound dependencies
5. **lib.rs** (`crates/bevy_ecs/src/lib.rs`) — 131 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `collect_meshes_for_gpu_building` (@ `crates/bevy_pbr/src/render/mesh.rs`) -> Impact: **577.3** | LOC: 1144
  * *Intent:* /// The version of [`RenderMeshInstanceGpuQueue`] that omits the /// [`MeshCullingData`], so that we don't waste space when GPU
- `ktx2_dfd_header_to_texture_format` (@ `crates/bevy_image/src/ktx2.rs`) -> Impact: **436.3** | LOC: 721
  * *Intent:* /// Reads the [`TextureFormat`] from a KTX2 data format descriptor header. /// /// # Errors /// /// Returns an error for invalid or unsupported textur...
- `fold_over_storage_range` (@ `crates/bevy_ecs/src/query/iter.rs`) -> Impact: **353.3** | LOC: 1722
  * *Intent:* /// Get the next result from the query. /// /// If the [`QueryData`] does not implement [`IterQueryData`], /// then it is not sound to yield multiple ...
- `finish` (@ `crates/bevy_pbr/src/render/mesh.rs`) -> Impact: **328.9** | LOC: 1521
- `load_node` (@ `crates/bevy_gltf/src/loader/mod.rs`) -> Impact: **299.6** | LOC: 1044
- `late_gpu_preprocess` (@ `crates/bevy_pbr/src/render/gpu_preprocess.rs`) -> Impact: **296.9** | LOC: 1228
- `add` (@ `crates/bevy_render/src/render_phase/mod.rs`) -> Impact: **271.8** | LOC: 1023
  * *Intent:* /// A list of the entities in each bin, along with their cached /// [`InputUniformIndex`].
- `specialize_shadows` (@ `crates/bevy_pbr/src/render/light.rs`) -> Impact: **228.2** | LOC: 547
- `example_control_system` (@ `examples/3d/transmission.rs`) -> Impact: **216.4** | LOC: 218
- `changed_windows` (@ `crates/bevy_winit/src/system.rs`) -> Impact: **207.6** | LOC: 290
  * *Intent:* /// Propagates changes from [`Window`] entities to the [`winit`] backend. /// /// # Notes /// /// - [`Window::present_mode`] and [`Window::composite_a...

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `examples/3d` | 66 | 7331.3 | 30.81% | 0.0% |
| `crates/bevy_ecs/src/query` | 11 | 5795.44 | 30.27% | 80.48% |
| `crates/bevy_ecs/src/entity` | 13 | 3836.58 | 17.18% | 92.09% |
| `crates/bevy_pbr/src/render` | 9 | 3802.0 | 7.09% | 47.43% |
| `crates/bevy_ecs/src/system` | 15 | 3794.88 | 25.15% | 99.64% |
| `crates/bevy_asset/src` | 16 | 3323.0 | 17.46% | 65.03% |
| `crates/bevy_reflect/src` | 24 | 3092.82 | 8.81% | 82.61% |
| `crates/bevy_ecs/src` | 13 | 2516.68 | 20.37% | 85.88% |
| `crates/bevy_ecs/src/schedule` | 10 | 2295.48 | 21.25% | 78.22% |
| `examples/stress_tests` | 22 | 2229.36 | 19.12% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `crates/bevy_animation/src/gltf_curves.rs` -> **100.0%** Exposure
- `crates/bevy_app/src/plugin.rs` -> **100.0%** Exposure
- `crates/bevy_asset/src/transformer.rs` -> **100.0%** Exposure
- `crates/bevy_audio/src/audio_source.rs` -> **100.0%** Exposure
- `crates/bevy_audio/src/sinks.rs` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `benches/benches/bevy_ecs/change_detection.rs` -> **100.0%** Exposure
- `benches/benches/bevy_ecs/components/add_remove.rs` -> **100.0%** Exposure
- `benches/benches/bevy_ecs/components/add_remove_big_sparse_set.rs` -> **100.0%** Exposure
- `benches/benches/bevy_ecs/components/add_remove_big_table.rs` -> **100.0%** Exposure
- `benches/benches/bevy_ecs/components/add_remove_sparse_set.rs` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `crates/bevy_ecs/src/query/fetch.rs` -> **9** Orphaned Functions | **264** Duplicates
- `crates/bevy_ecs/src/system/mod.rs` -> **62** Orphaned Functions | **63** Duplicates
- `crates/bevy_ecs/src/system/system_param.rs` -> **10** Orphaned Functions | **107** Duplicates
- `crates/bevy_ecs/src/entity/index_map.rs` -> **2** Orphaned Functions | **110** Duplicates
- `crates/bevy_ecs/src/relationship/relationship_source_collection.rs` -> **11** Orphaned Functions | **86** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`examples/input/gamepad_rumble.rs`** -> AI Confidence: **99.34%**
2. **`benches/benches/bevy_reflect/function.rs`** -> AI Confidence: **99.31%**
3. **`crates/bevy_audio/src/audio_output.rs`** -> AI Confidence: **99.31%**
4. **`crates/bevy_ecs/macros/src/component.rs`** -> AI Confidence: **99.31%**
5. **`crates/bevy_ecs/macros/src/event.rs`** -> AI Confidence: **99.31%**
6. **`crates/bevy_ecs/src/error/handler.rs`** -> AI Confidence: **99.31%**
7. **`crates/bevy_ecs/src/schedule/auto_insert_apply_deferred.rs`** -> AI Confidence: **99.31%**
8. **`crates/bevy_gltf/src/loader/gltf_ext/material.rs`** -> AI Confidence: **99.31%**
9. **`crates/bevy_gltf/src/loader/gltf_ext/texture.rs`** -> AI Confidence: **99.31%**
10. **`crates/bevy_image/src/basis.rs`** -> AI Confidence: **99.31%**
11. **`crates/bevy_image/src/ktx2.rs`** -> AI Confidence: **99.31%**
12. **`crates/bevy_macro_utils/src/member.rs`** -> AI Confidence: **99.31%**
13. **`crates/bevy_macro_utils/src/shape.rs`** -> AI Confidence: **99.31%**
14. **`crates/bevy_pbr/src/decal/clustered.rs`** -> AI Confidence: **99.31%**
15. **`crates/bevy_pbr/src/deferred/mod.rs`** -> AI Confidence: **99.31%**
16. **`crates/bevy_pbr/src/pbr_material.rs`** -> AI Confidence: **99.31%**
17. **`crates/bevy_pbr/src/prepass/prepass_bindings.rs`** -> AI Confidence: **99.31%**
18. **`crates/bevy_pbr/src/render/mesh_view_bindings.rs`** -> AI Confidence: **99.31%**
19. **`crates/bevy_picking/src/input.rs`** -> AI Confidence: **99.31%**
20. **`crates/bevy_reflect/derive/src/field_attributes.rs`** -> AI Confidence: **99.31%**
21. **`crates/bevy_reflect/derive/src/type_path.rs`** -> AI Confidence: **99.31%**
22. **`crates/bevy_scene/src/scene.rs`** -> AI Confidence: **99.31%**
23. **`crates/bevy_sprite/src/picking_backend.rs`** -> AI Confidence: **99.31%**
24. **`crates/bevy_ui/src/picking_backend.rs`** -> AI Confidence: **99.31%**
25. **`crates/bevy_winit/src/converters.rs`** -> AI Confidence: **99.31%**
26. **`crates/bevy_winit/src/system.rs`** -> AI Confidence: **99.31%**
27. **`crates/bevy_winit/src/winit_windows.rs`** -> AI Confidence: **99.31%**
28. **`examples/3d/auto_exposure.rs`** -> AI Confidence: **99.31%**
29. **`examples/3d/bloom_3d.rs`** -> AI Confidence: **99.31%**
30. **`examples/3d/tonemapping.rs`** -> AI Confidence: **99.31%**
31. **`examples/3d/transmission.rs`** -> AI Confidence: **99.31%**
32. **`examples/3d/visibility_range.rs`** -> AI Confidence: **99.31%**
33. **`examples/3d/volumetric_fog.rs`** -> AI Confidence: **99.31%**
34. **`examples/remote/client.rs`** -> AI Confidence: **99.31%**
35. **`crates/bevy_animation/src/util.rs`** -> AI Confidence: **99.29%**
36. **`examples/input/touch_input.rs`** -> AI Confidence: **99.29%**
37. **`examples/mobile/android_example/gradlew`** -> AI Confidence: **99.29%**
38. **`examples/mobile/android_example_native/gradlew`** -> AI Confidence: **99.29%**
39. **`crates/bevy_asset/src/id.rs`** -> AI Confidence: **99.24%**
40. **`crates/bevy_camera_controller/src/free_camera.rs`** -> AI Confidence: **99.24%**
41. **`crates/bevy_color/src/color.rs`** -> AI Confidence: **99.24%**
42. **`crates/bevy_color/src/laba.rs`** -> AI Confidence: **99.24%**
43. **`crates/bevy_core_pipeline/src/core_3d/mod.rs`** -> AI Confidence: **99.24%**
44. **`crates/bevy_derive/src/derefs.rs`** -> AI Confidence: **99.24%**
45. **`crates/bevy_dev_tools/src/picking_debug.rs`** -> AI Confidence: **99.24%**
46. **`crates/bevy_dev_tools/src/render_debug.rs`** -> AI Confidence: **99.24%**
47. **`crates/bevy_diagnostic/src/system_information_diagnostics_plugin.rs`** -> AI Confidence: **99.24%**
48. **`crates/bevy_ecs/macros/src/query_data.rs`** -> AI Confidence: **99.24%**
49. **`crates/bevy_ecs/src/world/entity_access/entity_ref.rs`** -> AI Confidence: **99.24%**
50. **`crates/bevy_ecs/src/world/entity_access/except.rs`** -> AI Confidence: **99.24%**
51. **`crates/bevy_ecs/src/world/unsafe_world_cell.rs`** -> AI Confidence: **99.24%**
52. **`crates/bevy_feathers/src/cursor.rs`** -> AI Confidence: **99.24%**
53. **`crates/bevy_gizmos_render/src/pipeline_3d.rs`** -> AI Confidence: **99.24%**
54. **`crates/bevy_gltf/src/vertex_attributes.rs`** -> AI Confidence: **99.24%**
55. **`crates/bevy_image/src/dds.rs`** -> AI Confidence: **99.24%**
56. **`crates/bevy_input/src/gamepad.rs`** -> AI Confidence: **99.24%**
57. **`crates/bevy_internal/src/default_plugins.rs`** -> AI Confidence: **99.24%**
58. **`crates/bevy_light/src/atmosphere.rs`** -> AI Confidence: **99.24%**
59. **`crates/bevy_math/src/compass.rs`** -> AI Confidence: **99.24%**
60. **`crates/bevy_math/src/cubic_splines/curve_impls.rs`** -> AI Confidence: **99.24%**
61. **`crates/bevy_mesh/src/mikktspace.rs`** -> AI Confidence: **99.24%**
62. **`crates/bevy_pbr/src/light_probe/irradiance_volume.rs`** -> AI Confidence: **99.24%**
63. **`crates/bevy_pbr/src/meshlet/material_pipeline_prepare.rs`** -> AI Confidence: **99.24%**
64. **`crates/bevy_pbr/src/meshlet/pipelines.rs`** -> AI Confidence: **99.24%**
65. **`crates/bevy_pbr/src/prepass/mod.rs`** -> AI Confidence: **99.24%**
66. **`crates/bevy_pbr/src/render/light.rs`** -> AI Confidence: **99.24%**
67. **`crates/bevy_pbr/src/transmission/texture.rs`** -> AI Confidence: **99.24%**
68. **`crates/bevy_reflect/derive/src/from_reflect.rs`** -> AI Confidence: **99.24%**
69. **`crates/bevy_reflect/src/path/access.rs`** -> AI Confidence: **99.24%**
70. **`crates/bevy_reflect/src/serde/de/struct_utils.rs`** -> AI Confidence: **99.24%**
71. **`crates/bevy_reflect/src/serde/de/tuple_utils.rs`** -> AI Confidence: **99.24%**
72. **`crates/bevy_reflect/src/serde/ser/enums.rs`** -> AI Confidence: **99.24%**
73. **`crates/bevy_reflect/src/serde/ser/tuple_structs.rs`** -> AI Confidence: **99.24%**
74. **`crates/bevy_render/src/render_resource/bindless.rs`** -> AI Confidence: **99.24%**
75. **`crates/bevy_render/src/texture/gpu_image.rs`** -> AI Confidence: **99.24%**
76. **`crates/bevy_render/src/view/window/mod.rs`** -> AI Confidence: **99.24%**
77. **`crates/bevy_sprite_render/src/mesh2d/wireframe2d.rs`** -> AI Confidence: **99.24%**
78. **`crates/bevy_sprite_render/src/texture_slice/computed_slices.rs`** -> AI Confidence: **99.24%**
79. **`crates/bevy_ui/src/focus.rs`** -> AI Confidence: **99.24%**
80. **`crates/bevy_ui/src/geometry.rs`** -> AI Confidence: **99.24%**
81. **`crates/bevy_ui/src/layout/convert.rs`** -> AI Confidence: **99.24%**
82. **`crates/bevy_ui_widgets/src/menu.rs`** -> AI Confidence: **99.24%**
83. **`crates/bevy_utils/src/debug_info.rs`** -> AI Confidence: **99.24%**
84. **`examples/2d/wireframe_2d.rs`** -> AI Confidence: **99.24%**
85. **`examples/3d/deferred_rendering.rs`** -> AI Confidence: **99.24%**
86. **`examples/3d/lightmaps.rs`** -> AI Confidence: **99.24%**
87. **`examples/3d/reflection_probes.rs`** -> AI Confidence: **99.24%**
88. **`examples/3d/shadow_caster_receiver.rs`** -> AI Confidence: **99.24%**
89. **`examples/3d/wireframe.rs`** -> AI Confidence: **99.24%**
90. **`examples/app/headless_renderer.rs`** -> AI Confidence: **99.24%**
91. **`examples/large_scenes/bistro/src/main.rs`** -> AI Confidence: **99.24%**
92. **`examples/large_scenes/caldera_hotel/src/main.rs`** -> AI Confidence: **99.24%**
93. **`examples/ui/navigation/directional_navigation.rs`** -> AI Confidence: **99.24%**
94. **`examples/window/window_settings.rs`** -> AI Confidence: **99.24%**
95. **`tools/export-content/src/app.rs`** -> AI Confidence: **99.24%**
96. **`crates/bevy_ecs/src/world/entity_access/component_fetch.rs`** -> AI Confidence: **99.23%**
97. **`crates/bevy_gltf/src/loader/extensions/khr_materials_specular.rs`** -> AI Confidence: **99.23%**
98. **`crates/bevy_platform/src/cfg.rs`** -> AI Confidence: **99.23%**
99. **`crates/bevy_reflect/derive/src/documentation.rs`** -> AI Confidence: **99.23%**
100. **`crates/bevy_reflect/derive/src/serialization.rs`** -> AI Confidence: **99.23%**
101. **`crates/bevy_reflect/src/enums/helpers.rs`** -> AI Confidence: **99.23%**
102. **`examples/3d/ssao.rs`** -> AI Confidence: **99.23%**
103. **`examples/diagnostics/log_diagnostics.rs`** -> AI Confidence: **99.23%**
104. **`examples/ecs/system_piping.rs`** -> AI Confidence: **99.23%**
105. **`examples/gizmos/3d_gizmos.rs`** -> AI Confidence: **99.23%**
106. **`examples/gizmos/light_gizmos.rs`** -> AI Confidence: **99.23%**
107. **`examples/stress_tests/many_buttons.rs`** -> AI Confidence: **99.23%**
108. **`examples/window/monitor_info.rs`** -> AI Confidence: **99.23%**
109. **`benches/benches/bevy_ecs/observers/custom.rs`** -> AI Confidence: **99.18%**
110. **`benches/benches/bevy_ecs/world/commands.rs`** -> AI Confidence: **99.18%**
111. **`benches/benches/bevy_ecs/world/world_get.rs`** -> AI Confidence: **99.18%**
112. **`benches/benches/bevy_picking/ray_mesh_intersection.rs`** -> AI Confidence: **99.18%**
113. **`benches/benches/bevy_reflect/map.rs`** -> AI Confidence: **99.18%**
114. **`crates/bevy_animation/src/gltf_curves.rs`** -> AI Confidence: **99.18%**
115. **`crates/bevy_animation/src/transition.rs`** -> AI Confidence: **99.18%**
116. **`crates/bevy_anti_alias/src/contrast_adaptive_sharpening/mod.rs`** -> AI Confidence: **99.18%**
117. **`crates/bevy_anti_alias/src/fxaa/mod.rs`** -> AI Confidence: **99.18%**
118. **`crates/bevy_anti_alias/src/taa/mod.rs`** -> AI Confidence: **99.18%**
119. **`crates/bevy_app/src/task_pool_plugin.rs`** -> AI Confidence: **99.18%**
120. **`crates/bevy_asset/macros/src/lib.rs`** -> AI Confidence: **99.18%**
121. **`crates/bevy_asset/src/asset_changed.rs`** -> AI Confidence: **99.18%**
122. **`crates/bevy_asset/src/assets.rs`** -> AI Confidence: **99.18%**
123. **`crates/bevy_asset/src/io/android.rs`** -> AI Confidence: **99.18%**
124. **`crates/bevy_asset/src/io/embedded/embedded_watcher.rs`** -> AI Confidence: **99.18%**
125. **`crates/bevy_asset/src/io/file/file_asset.rs`** -> AI Confidence: **99.18%**
126. **`crates/bevy_asset/src/io/file/file_watcher.rs`** -> AI Confidence: **99.18%**
127. **`crates/bevy_asset/src/io/memory.rs`** -> AI Confidence: **99.18%**
128. **`crates/bevy_asset/src/io/mod.rs`** -> AI Confidence: **99.18%**
129. **`crates/bevy_asset/src/io/processor_gated.rs`** -> AI Confidence: **99.18%**
130. **`crates/bevy_asset/src/io/wasm.rs`** -> AI Confidence: **99.18%**
131. **`crates/bevy_asset/src/loader.rs`** -> AI Confidence: **99.18%**
132. **`crates/bevy_asset/src/loader_builders.rs`** -> AI Confidence: **99.18%**
133. **`crates/bevy_asset/src/processor/process.rs`** -> AI Confidence: **99.18%**
134. **`crates/bevy_asset/src/server/loaders.rs`** -> AI Confidence: **99.18%**
135. **`crates/bevy_camera/src/components.rs`** -> AI Confidence: **99.18%**
136. **`crates/bevy_camera/src/visibility/render_layers.rs`** -> AI Confidence: **99.18%**
137. **`crates/bevy_color/src/oklaba.rs`** -> AI Confidence: **99.18%**
138. **`crates/bevy_color/src/xyza.rs`** -> AI Confidence: **99.18%**
139. **`crates/bevy_core_pipeline/src/core_2d/main_opaque_pass_2d_node.rs`** -> AI Confidence: **99.18%**
140. **`crates/bevy_core_pipeline/src/core_2d/mod.rs`** -> AI Confidence: **99.18%**
141. **`crates/bevy_core_pipeline/src/core_3d/main_opaque_pass_3d_node.rs`** -> AI Confidence: **99.18%**
142. **`crates/bevy_core_pipeline/src/fullscreen_material.rs`** -> AI Confidence: **99.18%**
143. **`crates/bevy_core_pipeline/src/mip_generation/mod.rs`** -> AI Confidence: **99.18%**
144. **`crates/bevy_core_pipeline/src/oit/mod.rs`** -> AI Confidence: **99.18%**
145. **`crates/bevy_core_pipeline/src/oit/resolve/mod.rs`** -> AI Confidence: **99.18%**
146. **`crates/bevy_core_pipeline/src/oit/resolve/node.rs`** -> AI Confidence: **99.18%**
147. **`crates/bevy_core_pipeline/src/prepass/background_motion_vectors.rs`** -> AI Confidence: **99.18%**
148. **`crates/bevy_core_pipeline/src/prepass/node.rs`** -> AI Confidence: **99.18%**
149. **`crates/bevy_core_pipeline/src/tonemapping/node.rs`** -> AI Confidence: **99.18%**
150. **`crates/bevy_core_pipeline/src/upscaling/node.rs`** -> AI Confidence: **99.18%**
151. **`crates/bevy_dev_tools/src/ci_testing/mod.rs`** -> AI Confidence: **99.18%**
152. **`crates/bevy_dev_tools/src/diagnostics_overlay.rs`** -> AI Confidence: **99.18%**
153. **`crates/bevy_diagnostic/src/entity_count_diagnostics_plugin.rs`** -> AI Confidence: **99.18%**
154. **`crates/bevy_ecs/macros/src/lib.rs`** -> AI Confidence: **99.18%**
155. **`crates/bevy_ecs/src/bundle/info.rs`** -> AI Confidence: **99.18%**
156. **`crates/bevy_ecs/src/bundle/insert.rs`** -> AI Confidence: **99.18%**
157. **`crates/bevy_ecs/src/bundle/remove.rs`** -> AI Confidence: **99.18%**
158. **`crates/bevy_ecs/src/change_detection/params.rs`** -> AI Confidence: **99.18%**
159. **`crates/bevy_ecs/src/component/clone.rs`** -> AI Confidence: **99.18%**
160. **`crates/bevy_ecs/src/entity/mod.rs`** -> AI Confidence: **99.18%**
161. **`crates/bevy_ecs/src/entity/remote_allocator.rs`** -> AI Confidence: **99.18%**
162. **`crates/bevy_ecs/src/entity/unique_slice.rs`** -> AI Confidence: **99.18%**
163. **`crates/bevy_ecs/src/event/trigger.rs`** -> AI Confidence: **99.18%**
164. **`crates/bevy_ecs/src/label.rs`** -> AI Confidence: **99.18%**
165. **`crates/bevy_ecs/src/lifecycle.rs`** -> AI Confidence: **99.18%**
166. **`crates/bevy_ecs/src/message/message_registry.rs`** -> AI Confidence: **99.18%**
167. **`crates/bevy_ecs/src/name.rs`** -> AI Confidence: **99.18%**
168. **`crates/bevy_ecs/src/observer/distributed_storage.rs`** -> AI Confidence: **99.18%**
169. **`crates/bevy_ecs/src/observer/entity_cloning.rs`** -> AI Confidence: **99.18%**
170. **`crates/bevy_ecs/src/observer/system_param.rs`** -> AI Confidence: **99.18%**
171. **`crates/bevy_ecs/src/query/fetch.rs`** -> AI Confidence: **99.18%**
172. **`crates/bevy_ecs/src/query/par_iter.rs`** -> AI Confidence: **99.18%**
173. **`crates/bevy_ecs/src/schedule/condition.rs`** -> AI Confidence: **99.18%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `6` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `28170` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `benches/benches/bevy_ecs/world/commands.rs` (RUST) -> Cumulative Risk: **734.85**
- **Archetype:** `file_cluster_4` (Distance: 12.4 IQR)
- **Magnitude:** 264.6 | **LOC:** 252 | **CtrlFlow:** 22.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9729%), Safety Score (95.9165%)
- **Heaviest Functions:** `spawn_commands` (Impact: 19.5), `insert_commands` (Impact: 18.2), `fake_commands` (Impact: 14.7)

### 2. `crates/bevy_ecs/src/system/commands/mod.rs` (RUST) -> Cumulative Risk: **729.62**
- **Archetype:** `file_cluster_4` (Distance: 21.325 IQR)
- **Magnitude:** 807.12 | **LOC:** 2882 | **CtrlFlow:** 14.2% | **Authorship Centralization:** 8.3%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9999%), State Flux (99.4089%), Tech Debt (96.5508%)
- **Heaviest Functions:** `insert_components` (Impact: 14.0), `insert_if` (Impact: 6.5), `insert_if_new_and` (Impact: 6.5)

### 3. `benches/benches/bevy_ecs/scheduling/run_condition.rs` (RUST) -> Cumulative Risk: **693.29**
- **Archetype:** `file_cluster_8` (Distance: 11.907 IQR)
- **Magnitude:** 117.88 | **LOC:** 119 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9983%), Safety Score (90.9144%)
- **Heaviest Functions:** `run_condition_yes_with_query` (Impact: 10.3), `run_condition_yes_with_resource` (Impact: 10.3), `run_condition_yes` (Impact: 10.0)

### 4. `crates/bevy_ecs/src/system/schedule_system.rs` (RUST) -> Cumulative Risk: **682.54**
- **Archetype:** `file_cluster_4` (Distance: 12.684 IQR)
- **Magnitude:** 169.8 | **LOC:** 200 | **CtrlFlow:** 17.7% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** Tech Debt (100.0%), Concurrency (100.0%), Spec Match (100.0%), State Flux (99.9559%)
- **Heaviest Functions:** `run_unsafe` (Impact: 4.1), `initialize` (Impact: 3.8), `refresh_hotpatch` (Impact: 2.2)

### 5. `crates/bevy_gizmos/src/lib.rs` (RUST) -> Cumulative Risk: **668.67**
- **Archetype:** `file_cluster_16` (Distance: 12.736 IQR)
- **Magnitude:** 204.9 | **LOC:** 356 | **CtrlFlow:** 12.9% | **Authorship Centralization:** 37.5%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9992%), State Flux (99.3767%), Verification (80.0%)
- **Heaviest Functions:** `update_gizmo_meshes` (Impact: 17.3), `insert_gizmo_config` (Impact: 9.9), `init_gizmo_group` (Impact: 6.5)

### 6. `crates/bevy_gizmos/src/gizmos.rs` (RUST) -> Cumulative Risk: **665.29**
- **Archetype:** `file_cluster_0` (Distance: 15.972 IQR)
- **Magnitude:** 418.18 | **LOC:** 953 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 40.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9009%), State Flux (98.3355%), Verification (80.0%)
- **Heaviest Functions:** `get_param` (Impact: 11.8), `queue` (Impact: 10.8), `linestrip_gradient` (Impact: 7.4)

### 7. `crates/bevy_pbr/src/meshlet/asset.rs` (RUST) -> Cumulative Risk: **645.7**
- **Archetype:** `file_cluster_4` (Distance: 14.469 IQR)
- **Magnitude:** 281.16 | **LOC:** 320 | **CtrlFlow:** 28.0% | **Authorship Centralization:** 80.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), State Flux (99.9999%), Documentation (86.9228%)
- **Heaviest Functions:** `load` (Impact: 33.7), `save` (Impact: 33.6), `read_slice` (Impact: 8.4)

### 8. `crates/bevy_ecs/src/system/exclusive_function_system.rs` (RUST) -> Cumulative Risk: **639.23**
- **Archetype:** `file_cluster_16` (Distance: 11.615 IQR)
- **Magnitude:** 154.86 | **LOC:** 354 | **CtrlFlow:** 10.3% | **Authorship Centralization:** 25.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.481%), Concurrency (98.715%), State Flux (96.7972%)
- **Heaviest Functions:** `run` (Impact: 14.5), `run_unsafe` (Impact: 5.4), `refresh_hotpatch` (Impact: 4.5)

### 9. `crates/bevy_ecs/src/query/par_iter.rs` (RUST) -> Cumulative Risk: **627.66**
- **Archetype:** `file_cluster_4` (Distance: 18.779 IQR)
- **Magnitude:** 193.44 | **LOC:** 470 | **CtrlFlow:** 24.6% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Tech Debt (99.995%), Dead Code (85.7608%)
- **Heaviest Functions:** `for_each_init` (Impact: 8.8), `for_each_init` (Impact: 8.8), `for_each_init` (Impact: 8.8)

### 10. `crates/bevy_ecs/src/lib.rs` (RUST) -> Cumulative Risk: **625.3**
- **Archetype:** `file_cluster_4` (Distance: 12.299 IQR)
- **Magnitude:** 952.32 | **LOC:** 2074 | **CtrlFlow:** 4.1% | **Authorship Centralization:** 22.2%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Tech Debt (96.4024%), State Flux (85.4317%)
- **Heaviest Functions:** `changed_trackers` (Impact: 9.7), `remove_tracking` (Impact: 8.7), `bundle_derive` (Impact: 8.3)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `crates/bevy_pbr/src/render/mesh.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.847 IQR)
- **Top Global Matches:** file_cluster_16: 13.847, file_cluster_13: 13.881, file_cluster_8: 14.015
- **Magnitude:** 1396.74 | **LOC:** 4358 | **CtrlFlow:** 37.4% | **Authorship Centralization:** 30.3%
- **Risk Profile:** Cognitive Load (10.3941%), Tech Debt (71.8359%)
**Top Internal Functions/Classes:**
  * `collect_meshes_for_gpu_building` (Impact: 577.3)
    * *Intent:* /// The version of [`RenderMeshInstanceGpuQueue`] that omits the /// [`MeshCullingData`], so that we...
  * `finish` (Impact: 328.9)
  * `extract_meshes_for_cpu_building` (Impact: 28.3)
  * `set_mesh_motion_vector_flags` (Impact: 15.3)
    * *Intent:* /// Information that is gathered during the parallel portion of mesh extraction /// when GPU mesh un...
  * `atomic_u64_zero_bit_iter` (Impact: 12.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 190`, `structural_boundaries: 318`, `args: 62`, `func_start: 42`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 176`, `dead_code: 4`, `planned_debt: 4`, `fragile_debt: 4`, `duplicate_logic: 14`
* *Architecture:* `api: 62`, `import: 50`
* *Defense:* `safety: 157`, `doc: 403`, `test: 6`, `sync_locks: 2`, `immutability_locks: 32`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` bevy_render::
    batching::
        gpu_preprocessing::
            self, NotShadowCaster, BaseMeshPipelineKey, ROQueryItem, std::sync::mpsc, bevy_core_pipeline::oit::OrderIndependentTransparencySettings, bevy_mesh::
    skinning::SkinnedMesh, mesh::allocator::MeshAllocator...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_ecs/src/query/iter.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.11%)
- **Global Archetype:** `file_cluster_11` (Drift: 16.105 IQR)
- **Top Global Matches:** file_cluster_11: 16.105, file_cluster_0: 16.117, file_cluster_16: 16.185
- **Magnitude:** 1270.14 | **LOC:** 3394 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 42.9%
- **Risk Profile:** Cognitive Load (18.5403%), Tech Debt (99.9697%)
**Top Internal Functions/Classes:**
  * `fold_over_storage_range` (Impact: 353.3)
    * *Intent:* /// Get the next result from the query. /// /// If the [`QueryData`] does not implement [`IterQueryD...
  * `next` (Impact: 44.0)
    * *Intent:* /// - if `K > N`, there are no combinations. /// /// The output combination is not guaranteed to hav...
  * `fetch_next_aliased_unchecked` (Impact: 32.1)
    * *Intent:* // SAFETY:
  * `fetch_next_aliased_unchecked` (Impact: 27.9)
  * `size_hint` (Impact: 17.1)
    * *Intent:* /// An [`Iterator`] over sorted query results of a [`QueryManyIter`]. /// /// This struct is created...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 194`, `structural_boundaries: 581`, `args: 149`, `func_start: 83`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 1`, `state_mutation: 281`, `dead_code: 68`, `planned_debt: 29`, `duplicate_logic: 59`
* *Architecture:* `api: 50`, `concurrency: 78`, `import: 19`
* *Defense:* `safety: 133`, `doc: 1097`, `test: 28`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::println, EntityRefExcept, FilteredEntityRef, core::
    cmp::Ordering, EntityMut, bevy_ecs::prelude::*, Entity, crate::component::Component...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_ecs/src/query/state.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_0` (Drift: 17.188 IQR)
- **Top Global Matches:** file_cluster_0: 17.188, file_cluster_4: 17.199, file_cluster_11: 17.47
- **Magnitude:** 1194.94 | **LOC:** 2438 | **CtrlFlow:** 13.3% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (48.2929%), Tech Debt (14.6746%)
**Top Internal Functions/Classes:**
  * `from_states_uninitialized` (Impact: 182.7)
  * `par_fold_init_unchecked_manual` (Impact: 39.3)
    * *Intent:* /// /// A combination is an arrangement of a collection of items where order does not matter. /// //...
  * `join_filtered` (Impact: 28.2)
  * `update_archetypes_unsafe_world_cell` (Impact: 18.3)
  * `new_archetype` (Impact: 15.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 482`, `args: 107`, `func_start: 89`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 22`, `high_risk_execution: 3`, `state_mutation: 247`, `dead_code: 60`, `duplicate_logic: 4`
* *Architecture:* `api: 114`, `concurrency: 295`, `import: 12`
* *Defense:* `safety: 35`, `doc: 756`, `test: 77`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` TableId, tracing::Span, FilteredEntityRef, bevy_ecs::prelude::*, FilteredAccess, change_detection::Tick, EntitySet, ContiguousQueryData...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_ecs/src/query/fetch.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.875 IQR)
- **Top Global Matches:** file_cluster_0: 14.875, file_cluster_16: 14.876, file_cluster_11: 15.035
- **Magnitude:** 1181.76 | **LOC:** 4326 | **CtrlFlow:** 26.6% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (18.0213%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `update_component_access` (Impact: 19.8)
  * `derive_release_state` (Impact: 16.6)
  * `test_contiguous_query_data` (Impact: 15.2)
  * `any_of_contiguous_test` (Impact: 12.3)
    * *Intent:* #[doc(fake_variadic)]
  * `option_contiguous_test` (Impact: 8.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 247`, `structural_boundaries: 680`, `args: 312`, `func_start: 282`, `class_start: 38`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 291`, `dead_code: 50`, `planned_debt: 7`, `duplicate_logic: 264`, `orphaned_logic: 9`
* *Architecture:* `api: 45`, `concurrency: 72`, `import: 10`
* *Defense:* `safety: 129`, `doc: 620`, `test: 37`, `immutability_locks: 100`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` EntityRefExcept, bevy_ecs_macros::QueryData, FilteredEntityRef, iter, variadics_please::all_tuples, EntityMut, bevy_ecs::prelude::*, Entity...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_ecs/src/entity/clone_entities.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.336 IQR)
- **Top Global Matches:** file_cluster_0: 13.336, file_cluster_4: 13.486, file_cluster_16: 13.535
- **Magnitude:** 997.62 | **LOC:** 2608 | **CtrlFlow:** 13.4% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (41.0067%), Tech Debt (97.6701%)
**Top Internal Functions/Classes:**
  * `clone_components` (Impact: 40.2)
  * `clone_entity_mapped_internal` (Impact: 26.0)
  * `clone_entity_internal` (Impact: 25.4)
  * `filter_allow` (Impact: 21.8)
  * `clone_components` (Impact: 18.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 92`, `structural_boundaries: 595`, `args: 118`, `func_start: 91`, `class_start: 77`
* *Risk/State:* `safety_bypasses: 41`, `high_risk_execution: 1`, `state_mutation: 244`, `dead_code: 10`, `planned_debt: 3`, `duplicate_logic: 13`, `orphaned_logic: 39`
* *Architecture:* `api: 45`, `concurrency: 259`, `import: 24`
* *Defense:* `safety: 109`, `doc: 325`, `test: 135`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` relationship::RelationshipHookMode, query::DebugCheckedUnwrap, bevy_ecs::prelude::*, FromWorld, Entity, ComponentCloneBehavior, EntityMapper, alloc::boxed::Box...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_pbr/src/render/light.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.95 IQR)
- **Top Global Matches:** file_cluster_0: 12.95, file_cluster_13: 13.047, file_cluster_16: 13.145
- **Magnitude:** 965.48 | **LOC:** 2518 | **CtrlFlow:** 39.3% | **Authorship Centralization:** 39.1%
- **Risk Profile:** Cognitive Load (15.618%), Tech Debt (34.4441%)
**Top Internal Functions/Classes:**
  * `specialize_shadows` (Impact: 228.2)
  * `prepare_lights` (Impact: 206.4)
  * `queue_shadows` (Impact: 128.1)
  * `shadow_pass` (Impact: 31.4)
  * `check_views_lights_need_specialization` (Impact: 28.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 159`, `structural_boundaries: 246`, `args: 52`, `func_start: 25`, `class_start: 23`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 150`, `dead_code: 7`, `planned_debt: 5`, `orphaned_logic: 15`
* *Architecture:* `api: 87`, `import: 34`
* *Defense:* `safety: 94`, `doc: 49`, `immutability_locks: 27`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` DirectionalLightShadowMap, array, decal::clustered::RenderClusteredDecals, mesh::allocator::MeshAllocator, bevy_ecs::
    entity::EntityHashMap, RenderQueue, ViewVisibility, CubeMapFace...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_ecs/src/lib.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.299 IQR)
- **Top Global Matches:** file_cluster_4: 12.299, file_cluster_0: 12.374, file_cluster_16: 12.562
- **Magnitude:** 952.32 | **LOC:** 2074 | **CtrlFlow:** 4.1% | **Authorship Centralization:** 22.2%
- **Risk Profile:** Cognitive Load (82.8388%), Tech Debt (96.4024%)
**Top Internal Functions/Classes:**
  * `changed_trackers` (Impact: 9.7)
  * `remove_tracking` (Impact: 8.7)
  * `bundle_derive` (Impact: 8.3)
  * `table_add_remove_many` (Impact: 8.2)
  * `sparse_set_add_remove_many` (Impact: 7.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 449`, `args: 99`, `func_start: 71`, `class_start: 32`
* *Risk/State:* `safety_bypasses: 78`, `state_mutation: 159`, `dead_code: 2`, `planned_debt: 1`, `orphaned_logic: 58`
* *Architecture:* `api: 38`, `concurrency: 501`, `import: 17`
* *Defense:* `safety: 57`, `doc: 24`, `test: 266`, `sync_locks: 13`, `immutability_locks: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` sync::atomic::AtomicUsize, MessageWriter, System, bevy_tasks::ComputeTaskPool, TaskPool, IntoScheduleConfigs, Schedules, crate::entity::ComponentCloneCtx...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_ecs/src/world/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_0` (Drift: 22.567 IQR)
- **Top Global Matches:** file_cluster_0: 22.567, file_cluster_11: 22.703, file_cluster_4: 22.732
- **Magnitude:** 952.14 | **LOC:** 4641 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 18.2%
- **Risk Profile:** Cognitive Load (28.4784%), Tech Debt (97.8959%)
**Top Internal Functions/Classes:**
  * `iter_resources_mut` (Impact: 153.7)
    * *Intent:* /// [`ComponentId`] from the provided [`Entity`] and runs the provided /// closure on it, returning ...
  * `get_entity_mut` (Impact: 13.4)
    * *Intent:* /// Gets an immutable reference to a non-send resource of the given type, if it exists. #[deprecated...
  * `spawn_at_unchecked` (Impact: 10.6)
    * *Intent:* /// y: f32, /// } /// /// let mut world = World::new(); /// let e1 = world.spawn(Position { x: 0.0, ...
  * `remove_resource_by_id` (Impact: 9.2)
  * `try_schedule_scope` (Impact: 7.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 93`, `structural_boundaries: 440`, `args: 134`, `func_start: 93`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 37`, `high_risk_execution: 3`, `state_mutation: 206`, `dead_code: 230`, `planned_debt: 3`, `duplicate_logic: 16`, `orphaned_logic: 26`
* *Architecture:* `api: 94`, `concurrency: 136`, `import: 37`
* *Defense:* `safety: 133`, `doc: 1921`, `test: 124`, `sync_locks: 11`, `immutability_locks: 2`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` std::println, EntityRefExcept, OccupiedComponentEntry, BundleSpawner, RequiredComponentsError, bevy_ecs::change_detection::MutUntyped, FilteredEntityMut, ComponentIds...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_asset/src/server/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.002 IQR)
- **Top Global Matches:** file_cluster_0: 14.002, file_cluster_16: 14.066, file_cluster_4: 14.145
- **Magnitude:** 919.5 | **LOC:** 2245 | **CtrlFlow:** 30.8% | **Authorship Centralization:** 76.9%
- **Risk Profile:** Cognitive Load (27.9792%), Tech Debt (78.9768%)
**Top Internal Functions/Classes:**
  * `wait_for_asset_id` (Impact: 128.0)
    * *Intent:* /// Returns the path for the given `id`, if it has one.
  * `handle_internal_asset_events` (Impact: 51.8)
  * `load_internal` (Impact: 44.7)
    * *Intent:* /// /// #[derive(Resource)] /// struct LoadingUntypedHandle(Handle<LoadedUntypedAsset>); /// /// fn ...
  * `get_meta_loader_and_reader` (Impact: 35.2)
  * `load_folder_internal` (Impact: 32.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 152`, `structural_boundaries: 342`, `args: 109`, `func_start: 73`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 66`, `dead_code: 12`, `planned_debt: 6`, `duplicate_logic: 4`, `orphaned_logic: 26`
* *Architecture:* `io: 1`, `api: 85`, `concurrency: 193`, `import: 28`
* *Defense:* `safety: 216`, `doc: 347`, `test: 1`, `sync_locks: 13`, `immutability_locks: 34`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` MissingAssetWriterError, bevy_ecs::prelude::Res, ErasedAssetIndex, AssetSource, AssetSourceId, tracing::Instrument, bevy_platform::
    collections::HashSet, future::Future...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_asset/src/lib.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.838 IQR)
- **Top Global Matches:** file_cluster_16: 12.838, file_cluster_8: 13.002, file_cluster_0: 13.012
- **Magnitude:** 911.52 | **LOC:** 3073 | **CtrlFlow:** 17.5% | **Authorship Centralization:** 63.6%
- **Risk Profile:** Cognitive Load (15.0871%), Tech Debt (99.3504%)
**Top Internal Functions/Classes:**
  * `load_dependencies` (Impact: 39.7)
  * `load_error_events` (Impact: 36.5)
  * `asset_dependency_is_tracked_when_not_loa` (Impact: 29.0)
  * `asset_load_error_event_handler` (Impact: 20.4)
  * `load_folder` (Impact: 18.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 125`, `structural_boundaries: 590`, `args: 120`, `func_start: 83`, `class_start: 35`
* *Risk/State:* `safety_bypasses: 64`, `high_risk_execution: 4`, `state_mutation: 237`, `planned_debt: 3`, `duplicate_logic: 33`, `orphaned_logic: 29`
* *Architecture:* `io: 9`, `api: 28`, `concurrency: 98`, `import: 15`
* *Defense:* `safety: 105`, `doc: 264`, `test: 192`, `sync_locks: 2`, `immutability_locks: 18`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` io::
            gated::GateOpener, WriteDefaultMetaError, AssetSourceId, Plugin, AssetReaderError, assets::*, Process, bevy_ecs::prelude::Component...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_render/src/render_phase/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.425 IQR)
- **Top Global Matches:** file_cluster_16: 13.425, file_cluster_13: 13.486, file_cluster_0: 13.71
- **Magnitude:** 879.06 | **LOC:** 1733 | **CtrlFlow:** 27.9% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (21.5752%), Tech Debt (99.9739%)
**Top Internal Functions/Classes:**
  * `add` (Impact: 271.8)
    * *Intent:* /// A list of the entities in each bin, along with their cached /// [`InputUniformIndex`].
  * `render_unbatchable_meshes` (Impact: 128.7)
  * `add` (Impact: 45.1)
    * *Intent:* /// Removes a single entity from its bin. ///
  * `render_batchable_meshes` (Impact: 38.9)
  * `remove_entity_from_bin` (Impact: 37.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 77`, `structural_boundaries: 199`, `args: 48`, `func_start: 46`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 112`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 21`, `orphaned_logic: 7`
* *Architecture:* `api: 48`, `concurrency: 28`, `import: 27`
* *Defense:* `safety: 60`, `doc: 420`, `test: 1`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` MainEntityHashMap, iter, hash::Hash, bevy_utils::default, system::lifetimeless::SRes, nonmax::NonMaxU32, BatchedInstanceBuffers, bevy_platform::collections::hash_map::Entry...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_gltf/src/loader/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.996 IQR)
- **Top Global Matches:** file_cluster_0: 12.996, file_cluster_17: 13.181, file_cluster_13: 13.198
- **Magnitude:** 873.54 | **LOC:** 2931 | **CtrlFlow:** 27.7% | **Authorship Centralization:** 27.3%
- **Risk Profile:** Cognitive Load (11.2926%), Tech Debt (61.6104%)
**Top Internal Functions/Classes:**
  * `load_node` (Impact: 299.6)
  * `load_gltf` (Impact: 126.8)
  * `load_material` (Impact: 39.3)
  * `load_image` (Impact: 17.5)
  * `next` (Impact: 11.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 145`, `structural_boundaries: 378`, `args: 84`, `func_start: 35`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 131`, `dead_code: 14`, `planned_debt: 9`, `duplicate_logic: 8`, `orphaned_logic: 13`
* *Architecture:* `io: 1`, `api: 29`, `concurrency: 48`, `import: 42`
* *Defense:* `safety: 154`, `doc: 86`, `test: 55`, `sync_locks: 4`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` bevy_gltf::*, GltfMaterialName, gltf_curves::*, NoFrustumCulling, AssetSourceId, GltfExtras, bevy_animation::prelude::*, Handle...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_image/src/ktx2.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.396 IQR)
- **Top Global Matches:** file_cluster_8: 11.396, file_cluster_0: 11.907, file_cluster_7: 11.913
- **Magnitude:** 860.62 | **LOC:** 1542 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (11.5861%), Tech Debt (11.0986%)
**Top Internal Functions/Classes:**
  * `ktx2_dfd_header_to_texture_format` (Impact: 436.3)
    * *Intent:* /// Reads the [`TextureFormat`] from a KTX2 data format descriptor header. /// /// # Errors /// /// ...
  * `ktx2_buffer_to_image` (Impact: 125.7)
    * *Intent:* /// Converts KTX2 bytes to a bevy [`Image`] using the given compressed format support. /// /// # Err...
  * `ktx2_format_to_texture_format` (Impact: 114.8)
    * *Intent:* /// Converts a KTX2 texture format identifier to a [`TextureFormat`]. /// /// # Errors /// /// Retur...
  * `get_transcoded_formats` (Impact: 57.7)
    * *Intent:* /// Determines an appropriate wgpu-compatible format based on compressed format support, and a /// b...
  * `sample_information_to_data_type` (Impact: 26.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 314`, `structural_boundaries: 157`, `args: 30`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 52`, `planned_debt: 3`, `fragile_debt: 1`, `orphaned_logic: 1`
* *Architecture:* `io: 2`, `api: 5`, `import: 10`
* *Defense:* `safety: 147`, `doc: 23`, `test: 23`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` TextureFormat, crate::CompressedImageFormats, TextureDimension, bevy_utils::default, ktx2::SupercompressionScheme, DfdHeader, TextureViewDescriptor, super::CompressedImageFormats...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_asset/src/processor/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.028 IQR)
- **Top Global Matches:** file_cluster_4: 14.028, file_cluster_13: 14.353, file_cluster_0: 14.467
- **Magnitude:** 854.06 | **LOC:** 1865 | **CtrlFlow:** 28.7% | **Authorship Centralization:** 85.7%
- **Risk Profile:** Cognitive Load (49.6429%), Tech Debt (20.6986%)
**Top Internal Functions/Classes:**
  * `write_default_meta_file_for_path` (Impact: 180.1)
    * *Intent:* // If we can't upgrade the task sender, that means all sources of tasks // (like the source event li...
  * `initialize` (Impact: 62.1)
    * *Intent:* // we must wait for uncontested write access to the asset source to ensure existing
  * `clean_empty_processed_ancestor_folders` (Impact: 38.9)
    * *Intent:* /// Populates the initial view of each asset by scanning the unprocessed and processed asset folders...
  * `process_asset_internal` (Impact: 37.9)
  * `get_asset_paths` (Impact: 26.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 100`, `structural_boundaries: 248`, `args: 35`, `func_start: 30`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 91`, `dead_code: 7`, `planned_debt: 4`, `orphaned_logic: 4`
* *Architecture:* `api: 19`, `concurrency: 268`, `import: 15`
* *Defense:* `safety: 108`, `doc: 184`, `test: 1`, `sync_locks: 13`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` AssetActionMinimal, AssetServer, PathBuf, bevy_ecs::prelude::*, WriteDefaultMetaError, HashSet, AssetSourceBuilders, RwLock...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_ecs/src/system/commands/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 21.325 IQR)
- **Top Global Matches:** file_cluster_4: 21.325, file_cluster_0: 21.337, file_cluster_11: 21.423
- **Magnitude:** 807.12 | **LOC:** 2882 | **CtrlFlow:** 14.2% | **Authorship Centralization:** 8.3%
- **Risk Profile:** Cognitive Load (52.8055%), Tech Debt (96.5508%)
**Top Internal Functions/Classes:**
  * `insert_components` (Impact: 14.0)
  * `insert_if` (Impact: 6.5)
    * *Intent:* /// Runs a cached system, registering it if necessary.
  * `insert_if_new_and` (Impact: 6.5)
  * `try_insert_if` (Impact: 6.5)
  * `try_insert_if_new_and` (Impact: 6.5)
    * *Intent:* /// /// It will internally return a [`TryRunScheduleError`](crate::world::error::TryRunScheduleError...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 363`, `args: 113`, `func_start: 80`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 242`, `dead_code: 140`, `planned_debt: 10`, `duplicate_logic: 9`, `orphaned_logic: 19`
* *Architecture:* `api: 70`, `concurrency: 240`, `import: 15`
* *Defense:* `safety: 13`, `doc: 1661`, `test: 49`, `immutability_locks: 34`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Ordering, observer::IntoEntityObserver, resource::Resource, SystemParamValidationError, sync::atomic::AtomicUsize, RegisteredSystem, ErrorContext, FromWorld...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_input/src/gamepad.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.851 IQR)
- **Top Global Matches:** file_cluster_0: 13.851, file_cluster_13: 14.114, file_cluster_8: 14.211
- **Magnitude:** 801.12 | **LOC:** 2979 | **CtrlFlow:** 45.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.2729%), Tech Debt (87.267%)
**Top Internal Functions/Classes:**
  * `gamepad_event_processing_system` (Impact: 123.7)
    * *Intent:* /// Try to set the value below which negative inputs will be rounded down to -1.0. /// /// # Errors ...
  * `gamepad_connection_system` (Impact: 115.5)
  * `new` (Impact: 42.1)
  * `get_axis_position_from_value` (Impact: 22.0)
  * `new` (Impact: 15.3)
    * *Intent:* /// Returns `true` if any item in the [`GamepadButton`] iterator has been pressed.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 116`, `structural_boundaries: 141`, `args: 67`, `func_start: 74`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 69`, `dead_code: 10`, `duplicate_logic: 24`
* *Architecture:* `api: 111`, `import: 20`
* *Defense:* `safety: 197`, `doc: 538`, `test: 39`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ButtonInput, bevy_input::gamepad::Gamepad, derive_more::derive::From, MessageWriter, bevy_math::ops, Entity, core::time::Duration, bevy_input::gamepad::GamepadSettings...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_camera/src/visibility/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.932 IQR)
- **Top Global Matches:** file_cluster_0: 12.932, file_cluster_13: 12.978, file_cluster_16: 12.994
- **Magnitude:** 783.8 | **LOC:** 1295 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 36.4%
- **Risk Profile:** Cognitive Load (28.7943%), Tech Debt (84.0438%)
**Top Internal Functions/Classes:**
  * `set_visible` (Impact: 144.5)
    * *Intent:* /// Returns `true` if the entity is visible in the hierarchy. /// Otherwise, returns `false`. #[inli...
  * `set_visible` (Impact: 142.3)
  * `visibility_propagate_system` (Impact: 84.1)
    * *Intent:* /// Label for the [`calculate_bounds`], `calculate_bounds_2d` and `calculate_bounds_text2d` systems,...
  * `check_visibility` (Impact: 65.2)
  * `view_visibility_lifecycle` (Impact: 13.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 191`, `args: 50`, `func_start: 34`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 36`, `state_mutation: 105`, `dead_code: 4`, `duplicate_logic: 9`, `orphaned_logic: 11`
* *Architecture:* `api: 34`, `concurrency: 69`, `import: 22`
* *Defense:* `safety: 34`, `doc: 187`, `test: 67`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` PostUpdate, bevy_ecs::prelude::*, bevy_asset::AssetEventSystems, Inherited, Visible, bevy_ecs::entity::EntityHashMap, bevy_ecs::world::DeferredWorld, bevy_app::Plugin...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_ecs/src/system/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.647 IQR)
- **Top Global Matches:** file_cluster_0: 14.647, file_cluster_4: 14.845, file_cluster_11: 14.936
- **Magnitude:** 772.0 | **LOC:** 2028 | **CtrlFlow:** 3.6% | **Authorship Centralization:** 30.0%
- **Risk Profile:** Cognitive Load (45.7297%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `sys` (Impact: 12.9)
  * `world_collections_system` (Impact: 9.1)
  * `write_system_state` (Impact: 8.2)
    * *Intent:* #[test]
  * `get_many_is_ordered` (Impact: 7.8)
  * `changed_resource_system` (Impact: 7.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 434`, `args: 149`, `func_start: 138`, `class_start: 34`
* *Risk/State:* `safety_bypasses: 23`, `high_risk_execution: 8`, `state_mutation: 271`, `dead_code: 14`, `planned_debt: 13`, `duplicate_logic: 63`, `orphaned_logic: 62`
* *Architecture:* `api: 18`, `concurrency: 110`, `import: 26`
* *Defense:* `safety: 20`, `doc: 275`, `test: 98`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::println, function_system::*, resource::Resource, system::
            Commands, crate::
        archetype::Archetypes, ApplyDeferred, EntityMut, bevy_ecs::prelude::*...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_pbr/src/render/gpu_preprocess.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.646 IQR)
- **Top Global Matches:** file_cluster_8: 12.646, file_cluster_16: 12.648, file_cluster_13: 12.873
- **Magnitude:** 768.4 | **LOC:** 2552 | **CtrlFlow:** 39.0% | **Authorship Centralization:** 36.4%
- **Risk Profile:** Cognitive Load (6.1847%), Tech Debt (46.7381%)
**Top Internal Functions/Classes:**
  * `late_gpu_preprocess` (Impact: 296.9)
  * `early_gpu_preprocess` (Impact: 105.8)
  * `specialize` (Impact: 28.3)
  * `pipelines_are_loaded` (Impact: 26.4)
  * `specialize` (Impact: 24.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 127`, `structural_boundaries: 199`, `args: 23`, `func_start: 26`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 70`, `dead_code: 3`, `duplicate_logic: 10`, `orphaned_logic: 9`
* *Architecture:* `api: 19`, `import: 16`
* *Defense:* `safety: 113`, `doc: 218`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` super::ShadowView, occlusion_culling::OcclusionCulling, BufferBinding, DynamicBindGroupLayoutEntries, IntoScheduleConfigs, query::Has, Plugin, PreprocessWorkItem...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_app/src/app.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_0` (Drift: 19.698 IQR)
- **Top Global Matches:** file_cluster_0: 19.698, file_cluster_11: 19.856, file_cluster_4: 19.963
- **Magnitude:** 733.52 | **LOC:** 2033 | **CtrlFlow:** 16.8% | **Authorship Centralization:** 25.0%
- **Risk Profile:** Cognitive Load (35.5515%), Tech Debt (99.9984%)
**Top Internal Functions/Classes:**
  * `cleanup` (Impact: 122.1)
  * `add_boxed_plugin` (Impact: 42.4)
    * *Intent:* /// Registers a system and returns a [`SystemId`] so it can later be called by [`World::run_system`]...
  * `plugins_state` (Impact: 11.3)
  * `test_derive_app_label` (Impact: 7.2)
    * *Intent:* /// For the panicking version, see [`App::register_required_components_with`]. /// /// Note that req...
  * `test_update_clears_trackers_once` (Impact: 6.6)
    * *Intent:* /// Returns a reference to the [`SubApp`] with the given label. /// /// # Panics ///
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 248`, `args: 102`, `func_start: 95`, `class_start: 28`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 3`, `state_mutation: 169`, `dead_code: 69`, `planned_debt: 6`, `fragile_debt: 2`, `duplicate_logic: 17`, `orphaned_logic: 28`
* *Architecture:* `api: 60`, `concurrency: 50`, `import: 23`
* *Defense:* `safety: 34`, `doc: 888`, `test: 59`, `sync_locks: 1`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ScheduleError, MessageWriter, core::fmt::Debug, message::message_update_system, Plugin, NoopPluginGroup, bevy_ecs::
    component::RequiredComponentsError, bevy_ecs::
        change_detection::DetectChanges...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_ecs/src/system/system_param.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_0` (Drift: 17.699 IQR)
- **Top Global Matches:** file_cluster_0: 17.699, file_cluster_11: 17.825, file_cluster_16: 17.952
- **Magnitude:** 732.12 | **LOC:** 3013 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 22.2%
- **Risk Profile:** Cognitive Load (23.7908%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `init_access` (Impact: 16.9)
    * *Intent:* /// Returns the inner `T`. /// /// The inner value is `pub`, so you can also obtain it by destructur...
  * `init_access` (Impact: 10.8)
    * *Intent:* // Pretend to add the param to the system alone to gather the new access,
  * `init_access` (Impact: 10.7)
    * *Intent:* /// A [`SystemParam`] that stores a buffer which gets applied to the [`World`] during /// [`ApplyDef...
  * `get_param` (Impact: 8.8)
  * `get_param` (Impact: 7.2)
    * *Intent:* /// // Tracks whether or not there is a threat the player should be aware of. /// #[derive(Resource,...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 119`, `structural_boundaries: 444`, `args: 146`, `func_start: 130`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 11`, `high_risk_execution: 4`, `state_mutation: 264`, `dead_code: 66`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 107`, `orphaned_logic: 10`
* *Architecture:* `api: 39`, `concurrency: 2`, `import: 23`
* *Defense:* `safety: 69`, `doc: 826`, `test: 14`, `immutability_locks: 66`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` resource::Resource, IS_RESOURCE, variadics_please::all_tuples, bevy_ecs::prelude::*, FromWorld, FilteredAccess, ReadOnlyQueryData, component::ComponentId...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_pbr/src/wireframe.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.917 IQR)
- **Top Global Matches:** file_cluster_16: 12.917, file_cluster_0: 13.013, file_cluster_8: 13.09
- **Magnitude:** 673.74 | **LOC:** 1644 | **CtrlFlow:** 35.9% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (7.8612%), Tech Debt (22.5079%)
**Top Internal Functions/Classes:**
  * `queue_wireframes` (Impact: 96.2)
  * `prepare_wireframe_wide_bind_groups` (Impact: 75.1)
  * `render` (Impact: 36.9)
  * `check_wireframe_entities_needing_special` (Impact: 31.3)
    * *Intent:* /// Applies or removes a wireframe material on any mesh without a [`Wireframe`] or [`NoWireframe`] c...
  * `specialize` (Impact: 20.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 134`, `structural_boundaries: 239`, `args: 47`, `func_start: 29`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 129`, `dead_code: 2`, `duplicate_logic: 6`
* *Architecture:* `api: 67`, `import: 17`
* *Defense:* `safety: 93`, `doc: 81`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CachedRenderPipelinePhaseItem, hash::FixedHasher, Plugin, RenderQueue, extract_resource::ExtractResource, render_asset::
        prepare_assets, Handle, set_mesh_motion_vector_flags...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_ecs/src/entity/unique_slice.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.372 IQR)
- **Top Global Matches:** file_cluster_16: 13.372, file_cluster_8: 13.862, file_cluster_7: 13.991
- **Magnitude:** 669.4 | **LOC:** 1896 | **CtrlFlow:** 26.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (12.8141%), Tech Debt (99.9998%)
**Top Internal Functions/Classes:**
  * `eq` (Impact: 5.3)
  * `eq` (Impact: 5.3)
  * `eq` (Impact: 5.3)
  * `eq` (Impact: 5.3)
  * `first_chunk` (Impact: 4.8)
    * *Intent:* /// Returns an array reference to the first `N` items in the slice. /// /// Equivalent to [`[T]::fir...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 117`, `structural_boundaries: 318`, `args: 161`, `func_start: 154`, `class_start: 3`
* *Risk/State:* `state_mutation: 173`, `dead_code: 3`, `duplicate_logic: 82`, `orphaned_logic: 9`
* *Architecture:* `api: 108`, `import: 6`
* *Defense:* `safety: 101`, `doc: 470`, `immutability_locks: 39`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` super::
    unique_vec::self, RangeInclusive, SliceIndex, Entity, EntitySet, Index, vec::Vec, iter::FusedIterator...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_ecs/src/query/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.792 IQR)
- **Top Global Matches:** file_cluster_4: 12.792, file_cluster_0: 13.1, file_cluster_16: 13.171
- **Magnitude:** 625.62 | **LOC:** 837 | **CtrlFlow:** 9.7% | **Authorship Centralization:** 27.3%
- **Risk Profile:** Cognitive Load (81.2343%), Tech Debt (91.0182%)
**Top Internal Functions/Classes:**
  * `query_filtered_exactsizeiterator_len` (Impact: 20.6)
  * `derived_worldqueries` (Impact: 10.9)
  * `many_entities` (Impact: 8.9)
  * `assert_all_sizes_iterator_equal` (Impact: 8.1)
  * `debug_checked_unwrap` (Impact: 7.9)
    * *Intent:* /// # Panics /// Panics if the value is `None` or `Err`, only in debug mode. /// /// # Safety /// Th...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 260`, `args: 46`, `func_start: 31`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 152`, `duplicate_logic: 8`, `orphaned_logic: 14`
* *Architecture:* `api: 12`, `concurrency: 291`, `import: 16`
* *Defense:* `safety: 47`, `doc: 12`, `test: 50`, `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` bevy_ecs_macros::QueryData, error::*, hash::Hash, Entity, System, ReadOnlyQueryData, prelude::AnyOf, fetch::*...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_transform/src/systems.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.28 IQR)
- **Top Global Matches:** file_cluster_4: 12.28, file_cluster_13: 12.387, file_cluster_0: 12.461
- **Magnitude:** 590.62 | **LOC:** 1174 | **CtrlFlow:** 22.0% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (46.0458%), Tech Debt (29.6935%)
**Top Internal Functions/Classes:**
  * `propagate_parent_transforms` (Impact: 113.2)
  * `propagate_parent_transforms` (Impact: 73.1)
  * `propagate_descendants_unchecked` (Impact: 70.5)
    * *Intent:* /// Recursively propagates the transforms for `entity` and all of its descendants. /// /// # Panics ...
  * `propagate_recursive` (Impact: 25.0)
  * `panic_when_hierarchy_cycle` (Impact: 8.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 199`, `args: 34`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 122`, `dead_code: 2`, `planned_debt: 4`, `duplicate_logic: 2`
* *Architecture:* `api: 13`, `concurrency: 111`, `import: 21`
* *Defense:* `safety: 19`, `doc: 72`, `test: 32`, `sync_locks: 5`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Ordering, bevy_ecs::prelude::*, parallel::propagate_parent_transforms, serial::propagate_parent_transforms, bevy_tasks::ComputeTaskPool, TaskPool, Transform, Vec3...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `crates/bevy_ecs/src/query/fetch.rs` (RUST) | Magnitude: 1181.76 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 2462, generics: 1066, structural_boundaries: 680, doc: 620
- `benches/benches/bevy_ecs/components/add_remove.rs` (RUST) | Magnitude: 16.06 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 9, state_mutation: 4, class_start: 3
- `crates/bevy_ecs/src/schedule/condition.rs` (RUST) | Magnitude: 520.4 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: doc: 1074, indent_spaces: 699, generics: 313, structural_boundaries: 303
- `crates/bevy_gilrs/src/lib.rs` (RUST) | Magnitude: 47.66 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 56, structural_boundaries: 33, doc: 19, decorators: 18
- `crates/bevy_color/src/lcha.rs` (RUST) | Magnitude: 128.24 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 256, doc: 43, structural_boundaries: 41, args: 35

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `examples/ecs/hotpatching_systems.rs` (RUST) | Magnitude: 41.14 | Delta: **0.047 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 42, doc: 15, concurrency: 15, structural_boundaries: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `crates/bevy_ecs/src/query/iter.rs` (RUST) | Magnitude: 1270.14 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 2101, doc: 1097, structural_boundaries: 581, generics: 465
- `crates/bevy_render/src/extract_resource.rs` (RUST) | Magnitude: 54.82 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 35, doc: 18, structural_boundaries: 17, generics: 13
- `crates/bevy_ecs/macros/src/component.rs` (RUST) | Magnitude: 441.46 | Delta: **0.044 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 276, branch: 92, safety: 79, structural_boundaries: 54
- `crates/bevy_reflect/src/func/reflect_fn.rs` (RUST) | Magnitude: 85.82 | Delta: **0.082 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 114, generics: 66, doc: 63, state_mutation: 54
- `crates/bevy_reflect/src/func/reflect_fn_mut.rs` (RUST) | Magnitude: 162.4 | Delta: **0.084 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 116, state_mutation: 75, doc: 70, generics: 70

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `crates/bevy_sprite_render/src/sprite_mesh/sprite_material.rs` (RUST) | Magnitude: 133.44 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 257, structural_boundaries: 71, state_mutation: 31, api: 29
- `crates/bevy_render/src/mesh/allocator.rs` (RUST) | Magnitude: 376.7 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 578, doc: 234, structural_boundaries: 146, branch: 69
- `crates/bevy_anti_alias/src/contrast_adaptive_sharpening/mod.rs` (RUST) | Magnitude: 64.24 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 129, structural_boundaries: 36, doc: 25, generics: 21
- `examples/3d/clustered_decals.rs` (RUST) | Magnitude: 129.9 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 118, doc: 59, state_mutation: 50, structural_boundaries: 38
- `crates/bevy_core_pipeline/src/tonemapping/mod.rs` (RUST) | Magnitude: 33.44 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 135, doc: 44, structural_boundaries: 32, generics: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `crates/bevy_core_pipeline/src/fullscreen_material.rs` (RUST) | Magnitude: 98.44 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 217, structural_boundaries: 62, generics: 37, safety: 31
- `crates/bevy_platform/src/time/fallback.rs` (RUST) | Magnitude: 51.6 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 81, doc: 43, structural_boundaries: 27, pointers: 16
- `crates/bevy_ecs/src/never.rs` (RUST) | Magnitude: 17.2 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 27, indent_spaces: 7, structural_boundaries: 6, sec_high_risk_execution: 3
- `crates/bevy_ecs/src/reflect/bundle.rs` (RUST) | Magnitude: 121.76 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 199, doc: 60, structural_boundaries: 40, generics: 24
- `crates/bevy_material/src/alpha.rs` (RUST) | Magnitude: 16.22 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 46, indent_spaces: 6, decorators: 3, structural_boundaries: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `crates/bevy_asset/macros/src/lib.rs` (RUST) | Magnitude: 38.14 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 75, structural_boundaries: 33, args: 20, safety: 12
- `benches/benches/bevy_ecs/scheduling/schedule.rs` (RUST) | Magnitude: 72.76 | Delta: **0.054 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 59, structural_boundaries: 49, state_mutation: 41, args: 20
- `crates/bevy_math/src/sampling/mesh_sampling.rs` (RUST) | Magnitude: 7.84 | Delta: **0.08 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 25, indent_spaces: 20, structural_boundaries: 11, generics: 8
- `benches/benches/bevy_ecs/scheduling/running_systems.rs` (RUST) | Magnitude: 156.06 | Delta: **0.109 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 114, state_mutation: 94, structural_boundaries: 87, args: 32
- `crates/bevy_ecs/compile_fail/tests/ui/query_lifetime_safety.rs` (RUST) | Magnitude: 41.26 | Delta: **0.14 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 62, structural_boundaries: 55, state_mutation: 28, safety_bypasses: 21

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `examples/2d/sprite_animation.rs` (RUST) | Magnitude: 66.4 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 85, state_mutation: 25, structural_boundaries: 23, concurrency: 14
- `crates/bevy_reflect/src/impls/macros/map.rs` (RUST) | Magnitude: 154.84 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 204, structural_boundaries: 52, safety: 44, args: 43
- `examples/transforms/scale.rs` (RUST) | Magnitude: 60.48 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 48, state_mutation: 33, structural_boundaries: 17, concurrency: 8
- `examples/app/persisting_preferences.rs` (RUST) | Magnitude: 71.92 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 81, state_mutation: 26, structural_boundaries: 19, concurrency: 14
- `examples/ecs/one_shot_systems.rs` (RUST) | Magnitude: 62.98 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 57, concurrency: 24, structural_boundaries: 16, doc: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `crates/bevy_reflect/src/serde/de/processor.rs` (RUST) | Magnitude: 12.5 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 190, dead_code: 19, indent_spaces: 19, safety: 9
- `crates/bevy_ecs/src/change_detection/traits.rs` (RUST) | Magnitude: 59.78 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: doc: 316, indent_spaces: 78, structural_boundaries: 35, args: 22
- `crates/bevy_reflect/src/type_info.rs` (RUST) | Magnitude: 107.12 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: doc: 289, indent_spaces: 227, structural_boundaries: 50, generics: 46
- `crates/bevy_ui_render/src/ui_material.rs` (RUST) | Magnitude: 23.78 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 93, indent_spaces: 33, generics: 27, structural_boundaries: 23
- `crates/bevy_render/src/render_resource/atomic_pod.rs` (RUST) | Magnitude: 23.88 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 103, indent_spaces: 40, structural_boundaries: 9, state_mutation: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `crates/bevy_ecs/src/component/constants.rs` (RUST) | Magnitude: 19.12 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 7, api: 6, immutability_locks: 6, encapsulation: 6
- `crates/bevy_dylib/src/lib.rs` (RUST) | Magnitude: 15.22 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 49, indent_spaces: 5, decorators: 3, structural_boundaries: 1
- `crates/bevy_math/src/ops.rs` (RUST) | Magnitude: 150.9 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 248, indent_spaces: 166, scientific: 88, api: 58
- `crates/bevy_color/src/palettes/basic.rs` (RUST) | Magnitude: 31.34 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 20, api: 16, immutability_locks: 16, encapsulation: 16
- `crates/bevy_winit/src/winit_config.rs` (RUST) | Magnitude: 6.8 | Delta: **0.054 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 53, indent_spaces: 13, structural_boundaries: 4, api: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `crates/bevy_render/src/texture/texture_cache.rs` (RUST) | Magnitude: 38.86 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 71, structural_boundaries: 17, doc: 13, state_mutation: 10
- `crates/bevy_ui/src/layout/debug.rs` (RUST) | Magnitude: 47.46 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 68, structural_boundaries: 20, branch: 10, state_mutation: 7
- `benches/benches/bevy_ecs/world/despawn_recursive.rs` (RUST) | Magnitude: 17.46 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 12, args: 7, closures: 6
- `crates/bevy_ecs/src/storage/table/column.rs` (RUST) | Magnitude: 91.52 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 256, doc: 148, api: 30, args: 28
- `crates/bevy_pbr/src/render/gpu_preprocess.rs` (RUST) | Magnitude: 768.4 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 1349, doc: 218, structural_boundaries: 199, generics: 137

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `crates/bevy_macro_utils/src/member.rs` (RUST) | Magnitude: 5.68 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: doc: 41, dead_code: 7, args: 3, api: 2
- `crates/bevy_reflect/src/serde/ser/processor.rs` (RUST) | Magnitude: 9.48 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: doc: 168, dead_code: 21, indent_spaces: 19, safety: 8

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `crates/bevy_pbr/src/render/mesh.rs` -> Churn: **89.25%** | Cog Load: 10.3941% | Debt: 71.8359%
- `crates/bevy_text/src/text.rs` -> Churn: **81.46%** | Cog Load: 6.5164% | Debt: 100.0%
- `crates/bevy_ecs/src/lib.rs` -> Churn: **74.52%** | Cog Load: 82.8388% | Debt: 96.4024%
- `crates/bevy_ecs/src/system/system_param.rs` -> Churn: **74.52%** | Cog Load: 23.7908% | Debt: 100.0%
- `crates/bevy_ui/src/widget/text.rs` -> Churn: **73.15%** | Cog Load: 28.0347% | Debt: 93.6453%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `crates/bevy_asset/src/processor/mod.rs` -> **andriyDev** (85.7% isolated ownership) | Magnitude: 854.06
- `crates/bevy_gizmos/src/primitives/dim3.rs` -> **Kevin Chen** (100.0% isolated ownership) | Magnitude: 589.28
- `crates/bevy_asset/src/processor/tests.rs` -> **andriyDev** (87.5% isolated ownership) | Magnitude: 538.88
- `crates/bevy_pbr/src/meshlet/from_mesh.rs` -> **JMS55** (100.0% isolated ownership) | Magnitude: 527.24
- `crates/bevy_gizmos/src/primitives/dim2.rs` -> **Joel Uckelman** (100.0% isolated ownership) | Magnitude: 495.56

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `crates/bevy_feathers/src/tokens.rs` -> **Severity: 322.1** (Blast Radius: 3.221 * Doc Risk: 100.0%)
- `crates/bevy_reflect/src/impls/alloc/vec.rs` -> **Severity: 250.056** (Blast Radius: 10.934 * Doc Risk: 22.8696%)
- `tools/ci/src/commands/format.rs` -> **Severity: 198.479** (Blast Radius: 4.336 * Doc Risk: 45.7746%)
- `crates/bevy_feathers/src/palette.rs` -> **Severity: 150.393** (Blast Radius: 1.612 * Doc Risk: 93.2958%)
- `crates/bevy_render/src/render_resource/uniform_buffer.rs` -> **Severity: 141.062** (Blast Radius: 9.467 * Doc Risk: 14.9004%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
