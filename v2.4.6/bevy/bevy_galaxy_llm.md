# ARCHITECTURAL_BRIEF: bevy
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/bevy` |
| **Timestamp** | `2026-08-03T19:24:30.591950+00:00` |
| **Scan Duration** | `8.07s` |
| **Git Branch** | `main` |
| **Git Commit** | `c7f779b8425e6bd110a5b6be28152206d139367b` |
| **Git Remote** | `https://github.com/bevyengine/bevy.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 1732 malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are analyzing software architecture through the lens of GitGalaxy Static Application Security Testing (SAST). GitGalaxy translates the non-visual architecture of repositories into measurable technical metrics.
> 
> **CORE DIRECTIVES:**
> 1. **Measure Risk, Not Quality:** Do not judge. We measure Risk Exposure (e.g., Cognitive Load Exposure). Frame all insights as blameless, objective observations. High risk highlights where the architecture might be drifting into fragile territory, not developer incompetence.
> 2. **The Physical Reality Rule:** Base your analysis strictly on the provided Structural Signatures (regex hit counts). Do not hallucinate meaning.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`.
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
> **Architectural Drift Z-Score:** `3.497`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 657 | 32.2% |
| file_cluster_13 | 352 | 17.2% |
| file_cluster_0 | 297 | 14.5% |
| file_cluster_16 | 297 | 14.5% |
| file_cluster_4 | 105 | 5.1% |
| file_cluster_6 | 13 | 0.6% |
| Unknown | 11 | 0.5% |
| file_cluster_17 | 8 | 0.4% |
| file_cluster_11 | 7 | 0.3% |
| file_cluster_7 | 6 | 0.3% |
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
| Cognitive Load Exposure | 0.0 | 100.0 | 17.8 | 9.8 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.8 | 38.9 | 42.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 34.6 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 24.7 | 2.4 | 0.0 |
| API Exposure | 0.0 | 12.8 | 2.8 | 3.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 32.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 35.4 | 12.5 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 6.4 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 94.0 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 6.6 | 1.3 | 0.6 | 0.0 |
| Volatility Exposure | 0.0 | 89.2 | 12.8 | 7.3 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 37.6 | 14.9 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 60.7 | 97.2 | 100.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 10.1 | 10.3 | 20.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.3 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
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

- `changed_windows` (@ `crates/bevy_winit/src/system.rs`) -> Impact: **1857.4** | LOC: 290
  * *Intent:* /// Propagates changes from [`Window`] entities to the [`winit`] backend. /// /// # Notes /// /// - [`Window::present_mode`] and [`Window::composite_a...
- `load_node` (@ `crates/bevy_gltf/src/loader/mod.rs`) -> Impact: **1834.1** | LOC: 1044
- `add` (@ `crates/bevy_render/src/render_phase/mod.rs`) -> Impact: **1777.8** | LOC: 1023
  * *Intent:* /// A list of the entities in each bin, along with their cached /// [`InputUniformIndex`].
- `specialize_shadows` (@ `crates/bevy_pbr/src/render/light.rs`) -> Impact: **1564.5** | LOC: 547
- `fold_over_storage_range` (@ `crates/bevy_ecs/src/query/iter.rs`) -> Impact: **1556.9** | LOC: 1722
  * *Intent:* /// Get the next result from the query. /// /// If the [`QueryData`] does not implement [`IterQueryData`], /// then it is not sound to yield multiple ...
- `ktx2_dfd_header_to_texture_format` (@ `crates/bevy_image/src/ktx2.rs`) -> Impact: **1452.6** | LOC: 721
  * *Intent:* /// Reads the [`TextureFormat`] from a KTX2 data format descriptor header. /// /// # Errors /// /// Returns an error for invalid or unsupported textur...
- `late_gpu_preprocess` (@ `crates/bevy_pbr/src/render/gpu_preprocess.rs`) -> Impact: **1307.4** | LOC: 1228
- `prepare_lights` (@ `crates/bevy_pbr/src/render/light.rs`) -> Impact: **1046.5** | LOC: 522
- `finish` (@ `crates/bevy_pbr/src/render/mesh.rs`) -> Impact: **961.1** | LOC: 1521
- `propagate_parent_transforms` (@ `crates/bevy_transform/src/systems.rs`) -> Impact: **897.7** | LOC: 729

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `insert_many` (@ `benches/benches/bevy_ecs/bundles/insert_many.rs`) -> **O(2^N) [Recursive]**
- `added_archetypes` (@ `benches/benches/bevy_ecs/components/archetype_updates.rs`) -> **O(2^N) [Recursive]**
- `contrived` (@ `benches/benches/bevy_ecs/scheduling/running_systems.rs`) -> **O(2^N) [Recursive]**
- `busy_systems` (@ `benches/benches/bevy_ecs/scheduling/running_systems.rs`) -> **O(2^N) [Recursive]**
- `spawn_commands` (@ `benches/benches/bevy_ecs/world/commands.rs`) -> **O(2^N) [Recursive]**
- `fake_commands` (@ `benches/benches/bevy_ecs/world/commands.rs`) -> **O(2^N) [Recursive]**
- `nonempty_spawn_commands` (@ `benches/benches/bevy_ecs/world/commands.rs`) -> **O(2^N) [Recursive]**
- `with_overload` (@ `benches/benches/bevy_reflect/function.rs`) -> **O(2^N) [Recursive]**
- `call_overload` (@ `benches/benches/bevy_reflect/function.rs`) -> **O(2^N) [Recursive]**
- `dynamic_list_push` (@ `benches/benches/bevy_reflect/list.rs`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `event_target` (@ `crates/bevy_ecs/src/event/mod.rs`) -> DB Complexity: **101**
  * *Intent:* /// println!("The explosion fizzles! This entity is immune!"); /// }); /// ``` /// /// ## [`EntityEvent`] Propagation /// /// When deriving [`EntityEv...
- `cleanup` (@ `crates/bevy_app/src/app.rs`) -> DB Complexity: **100**
- `fold_over_storage_range` (@ `crates/bevy_ecs/src/query/iter.rs`) -> DB Complexity: **85**
  * *Intent:* /// Get the next result from the query. /// /// If the [`QueryData`] does not implement [`IterQueryData`], /// then it is not sound to yield multiple ...
- `propagate_parent_transforms` (@ `crates/bevy_transform/src/systems.rs`) -> DB Complexity: **85**
- `iter_resources_mut` (@ `crates/bevy_ecs/src/world/mod.rs`) -> DB Complexity: **81**
  * *Intent:* /// [`ComponentId`] from the provided [`Entity`] and runs the provided /// closure on it, returning the result if the component was available. /// Thi...
- `from_states_uninitialized` (@ `crates/bevy_ecs/src/query/state.rs`) -> DB Complexity: **71**
- `set_visible` (@ `crates/bevy_camera/src/visibility/mod.rs`) -> DB Complexity: **66**
  * *Intent:* /// Returns `true` if the entity is visible in the hierarchy. /// Otherwise, returns `false`. #[inline]
- `add` (@ `crates/bevy_render/src/render_phase/mod.rs`) -> DB Complexity: **64**
  * *Intent:* /// A list of the entities in each bin, along with their cached /// [`InputUniformIndex`].
- `find_connected_meshlets` (@ `crates/bevy_pbr/src/meshlet/from_mesh.rs`) -> DB Complexity: **56**
- `entity_mut_reborrow_scope_panic` (@ `crates/bevy_ecs/src/world/entity_access/mod.rs`) -> DB Complexity: **54**
  * *Intent:* // regression test for https://github.com/bevyengine/bevy/pull/7387

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `examples/3d` | 66 | 13317.5 | 30.92% | 0.0% |
| `crates/bevy_ecs/src/query` | 11 | 9544.14 | 30.58% | 75.76% |
| `crates/bevy_pbr/src/render` | 9 | 8088.7 | 7.37% | 30.31% |
| `crates/bevy_ecs/src/entity` | 13 | 6632.78 | 17.73% | 89.82% |
| `crates/bevy_asset/src` | 16 | 5441.9 | 18.29% | 64.52% |
| `crates/bevy_image/src` | 15 | 5242.38 | 13.29% | 29.9% |
| `crates/bevy_reflect/src` | 24 | 5146.32 | 9.15% | 78.27% |
| `crates/bevy_ecs/src/system` | 15 | 5096.38 | 24.73% | 95.45% |
| `crates/bevy_ui/src` | 13 | 4371.58 | 19.1% | 54.17% |
| `crates/bevy_asset/src/server` | 3 | 4198.82 | 19.87% | 29.58% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `crates/bevy_animation/src/gltf_curves.rs` -> **100.0%** Exposure
- `crates/bevy_app/src/plugin.rs` -> **100.0%** Exposure
- `crates/bevy_asset/src/transformer.rs` -> **100.0%** Exposure
- `crates/bevy_audio/src/sinks.rs` -> **100.0%** Exposure
- `crates/bevy_camera/src/components.rs` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `benches/benches/bevy_ecs/change_detection.rs` -> **100.0%** Exposure
- `benches/benches/bevy_ecs/components/add_remove.rs` -> **100.0%** Exposure
- `benches/benches/bevy_ecs/components/add_remove_big_sparse_set.rs` -> **100.0%** Exposure
- `benches/benches/bevy_ecs/components/add_remove_big_table.rs` -> **100.0%** Exposure
- `benches/benches/bevy_ecs/components/add_remove_sparse_set.rs` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `crates/bevy_ecs/src/query/fetch.rs` -> **1** Orphaned Functions | **245** Duplicates
- `crates/bevy_ecs/src/entity/index_map.rs` -> **2** Orphaned Functions | **110** Duplicates
- `crates/bevy_ecs/src/system/system_param.rs` -> **1** Orphaned Functions | **96** Duplicates
- `crates/bevy_ecs/src/relationship/relationship_source_collection.rs` -> **7** Orphaned Functions | **86** Duplicates
- `crates/bevy_ecs/src/entity/unique_slice.rs` -> **9** Orphaned Functions | **82** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`examples/input/gamepad_rumble.rs`** -> AI Confidence: **99.34%**
2. **`benches/benches/bevy_reflect/function.rs`** -> AI Confidence: **99.31%**
3. **`crates/bevy_audio/src/audio_output.rs`** -> AI Confidence: **99.31%**
4. **`crates/bevy_camera_controller/src/free_camera.rs`** -> AI Confidence: **99.31%**
5. **`crates/bevy_ecs/macros/src/component.rs`** -> AI Confidence: **99.31%**
6. **`crates/bevy_ecs/macros/src/event.rs`** -> AI Confidence: **99.31%**
7. **`crates/bevy_ecs/src/error/handler.rs`** -> AI Confidence: **99.31%**
8. **`crates/bevy_ecs/src/schedule/auto_insert_apply_deferred.rs`** -> AI Confidence: **99.31%**
9. **`crates/bevy_gltf/src/loader/gltf_ext/material.rs`** -> AI Confidence: **99.31%**
10. **`crates/bevy_gltf/src/loader/gltf_ext/texture.rs`** -> AI Confidence: **99.31%**
11. **`crates/bevy_gltf/src/vertex_attributes.rs`** -> AI Confidence: **99.31%**
12. **`crates/bevy_image/src/basis.rs`** -> AI Confidence: **99.31%**
13. **`crates/bevy_image/src/ktx2.rs`** -> AI Confidence: **99.31%**
14. **`crates/bevy_macro_utils/src/member.rs`** -> AI Confidence: **99.31%**
15. **`crates/bevy_macro_utils/src/shape.rs`** -> AI Confidence: **99.31%**
16. **`crates/bevy_math/src/bounding/raycast2d.rs`** -> AI Confidence: **99.31%**
17. **`crates/bevy_math/src/bounding/raycast3d.rs`** -> AI Confidence: **99.31%**
18. **`crates/bevy_pbr/src/decal/clustered.rs`** -> AI Confidence: **99.31%**
19. **`crates/bevy_pbr/src/deferred/mod.rs`** -> AI Confidence: **99.31%**
20. **`crates/bevy_pbr/src/pbr_material.rs`** -> AI Confidence: **99.31%**
21. **`crates/bevy_pbr/src/prepass/prepass_bindings.rs`** -> AI Confidence: **99.31%**
22. **`crates/bevy_pbr/src/render/mesh_view_bindings.rs`** -> AI Confidence: **99.31%**
23. **`crates/bevy_picking/src/input.rs`** -> AI Confidence: **99.31%**
24. **`crates/bevy_reflect/derive/src/field_attributes.rs`** -> AI Confidence: **99.31%**
25. **`crates/bevy_reflect/derive/src/type_path.rs`** -> AI Confidence: **99.31%**
26. **`crates/bevy_reflect/src/func/error.rs`** -> AI Confidence: **99.31%**
27. **`crates/bevy_render/src/view/window/mod.rs`** -> AI Confidence: **99.31%**
28. **`crates/bevy_scene/src/scene.rs`** -> AI Confidence: **99.31%**
29. **`crates/bevy_sprite/src/picking_backend.rs`** -> AI Confidence: **99.31%**
30. **`crates/bevy_ui/src/picking_backend.rs`** -> AI Confidence: **99.31%**
31. **`crates/bevy_winit/src/converters.rs`** -> AI Confidence: **99.31%**
32. **`crates/bevy_winit/src/system.rs`** -> AI Confidence: **99.31%**
33. **`crates/bevy_winit/src/winit_windows.rs`** -> AI Confidence: **99.31%**
34. **`examples/3d/auto_exposure.rs`** -> AI Confidence: **99.31%**
35. **`examples/3d/bloom_3d.rs`** -> AI Confidence: **99.31%**
36. **`examples/3d/tonemapping.rs`** -> AI Confidence: **99.31%**
37. **`examples/3d/transmission.rs`** -> AI Confidence: **99.31%**
38. **`examples/3d/visibility_range.rs`** -> AI Confidence: **99.31%**
39. **`examples/3d/volumetric_fog.rs`** -> AI Confidence: **99.31%**
40. **`examples/3d/wireframe.rs`** -> AI Confidence: **99.31%**
41. **`examples/app/headless_renderer.rs`** -> AI Confidence: **99.31%**
42. **`examples/diagnostics/log_diagnostics.rs`** -> AI Confidence: **99.31%**
43. **`examples/ecs/system_piping.rs`** -> AI Confidence: **99.31%**
44. **`examples/remote/client.rs`** -> AI Confidence: **99.31%**
45. **`crates/bevy_animation/src/util.rs`** -> AI Confidence: **99.29%**
46. **`examples/input/keyboard_input.rs`** -> AI Confidence: **99.29%**
47. **`examples/input/touch_input.rs`** -> AI Confidence: **99.29%**
48. **`examples/mobile/android_example/settings.gradle`** -> AI Confidence: **99.29%**
49. **`examples/mobile/android_example_native/settings.gradle`** -> AI Confidence: **99.29%**
50. **`crates/bevy_asset/src/handle.rs`** -> AI Confidence: **99.24%**
51. **`crates/bevy_asset/src/id.rs`** -> AI Confidence: **99.24%**
52. **`crates/bevy_asset/src/io/source.rs`** -> AI Confidence: **99.24%**
53. **`crates/bevy_color/src/color.rs`** -> AI Confidence: **99.24%**
54. **`crates/bevy_color/src/laba.rs`** -> AI Confidence: **99.24%**
55. **`crates/bevy_color/src/lcha.rs`** -> AI Confidence: **99.24%**
56. **`crates/bevy_core_pipeline/src/core_3d/mod.rs`** -> AI Confidence: **99.24%**
57. **`crates/bevy_derive/src/derefs.rs`** -> AI Confidence: **99.24%**
58. **`crates/bevy_dev_tools/src/picking_debug.rs`** -> AI Confidence: **99.24%**
59. **`crates/bevy_dev_tools/src/render_debug.rs`** -> AI Confidence: **99.24%**
60. **`crates/bevy_diagnostic/src/system_information_diagnostics_plugin.rs`** -> AI Confidence: **99.24%**
61. **`crates/bevy_ecs/macros/src/query_data.rs`** -> AI Confidence: **99.24%**
62. **`crates/bevy_ecs/src/schedule/error.rs`** -> AI Confidence: **99.24%**
63. **`crates/bevy_ecs/src/world/entity_access/entity_ref.rs`** -> AI Confidence: **99.24%**
64. **`crates/bevy_ecs/src/world/entity_access/except.rs`** -> AI Confidence: **99.24%**
65. **`crates/bevy_ecs/src/world/unsafe_world_cell.rs`** -> AI Confidence: **99.24%**
66. **`crates/bevy_feathers/src/cursor.rs`** -> AI Confidence: **99.24%**
67. **`crates/bevy_gizmos_render/src/pipeline_3d.rs`** -> AI Confidence: **99.24%**
68. **`crates/bevy_image/src/dds.rs`** -> AI Confidence: **99.24%**
69. **`crates/bevy_input/src/gamepad.rs`** -> AI Confidence: **99.24%**
70. **`crates/bevy_internal/src/default_plugins.rs`** -> AI Confidence: **99.24%**
71. **`crates/bevy_light/src/atmosphere.rs`** -> AI Confidence: **99.24%**
72. **`crates/bevy_log/src/android_tracing.rs`** -> AI Confidence: **99.24%**
73. **`crates/bevy_math/src/compass.rs`** -> AI Confidence: **99.24%**
74. **`crates/bevy_math/src/cubic_splines/curve_impls.rs`** -> AI Confidence: **99.24%**
75. **`crates/bevy_math/src/sampling/shape_sampling.rs`** -> AI Confidence: **99.24%**
76. **`crates/bevy_pbr/src/light_probe/irradiance_volume.rs`** -> AI Confidence: **99.24%**
77. **`crates/bevy_pbr/src/meshlet/material_pipeline_prepare.rs`** -> AI Confidence: **99.24%**
78. **`crates/bevy_pbr/src/meshlet/pipelines.rs`** -> AI Confidence: **99.24%**
79. **`crates/bevy_pbr/src/prepass/mod.rs`** -> AI Confidence: **99.24%**
80. **`crates/bevy_pbr/src/render/light.rs`** -> AI Confidence: **99.24%**
81. **`crates/bevy_pbr/src/transmission/texture.rs`** -> AI Confidence: **99.24%**
82. **`crates/bevy_reflect/derive/src/from_reflect.rs`** -> AI Confidence: **99.24%**
83. **`crates/bevy_reflect/src/array.rs`** -> AI Confidence: **99.24%**
84. **`crates/bevy_reflect/src/enums/dynamic_enum.rs`** -> AI Confidence: **99.24%**
85. **`crates/bevy_reflect/src/path/access.rs`** -> AI Confidence: **99.24%**
86. **`crates/bevy_reflect/src/serde/de/struct_utils.rs`** -> AI Confidence: **99.24%**
87. **`crates/bevy_reflect/src/serde/de/tuple_utils.rs`** -> AI Confidence: **99.24%**
88. **`crates/bevy_reflect/src/serde/ser/enums.rs`** -> AI Confidence: **99.24%**
89. **`crates/bevy_reflect/src/serde/ser/structs.rs`** -> AI Confidence: **99.24%**
90. **`crates/bevy_render/src/render_resource/bindless.rs`** -> AI Confidence: **99.24%**
91. **`crates/bevy_render/src/texture/gpu_image.rs`** -> AI Confidence: **99.24%**
92. **`crates/bevy_settings/src/store_fs.rs`** -> AI Confidence: **99.24%**
93. **`crates/bevy_sprite_render/src/mesh2d/wireframe2d.rs`** -> AI Confidence: **99.24%**
94. **`crates/bevy_sprite_render/src/texture_slice/computed_slices.rs`** -> AI Confidence: **99.24%**
95. **`crates/bevy_ui/src/focus.rs`** -> AI Confidence: **99.24%**
96. **`crates/bevy_ui/src/geometry.rs`** -> AI Confidence: **99.24%**
97. **`crates/bevy_ui/src/layout/convert.rs`** -> AI Confidence: **99.24%**
98. **`crates/bevy_ui_widgets/src/menu.rs`** -> AI Confidence: **99.24%**
99. **`crates/bevy_winit/src/cursor/mod.rs`** -> AI Confidence: **99.24%**
100. **`examples/2d/wireframe_2d.rs`** -> AI Confidence: **99.24%**
101. **`examples/3d/deferred_rendering.rs`** -> AI Confidence: **99.24%**
102. **`examples/3d/lightmaps.rs`** -> AI Confidence: **99.24%**
103. **`examples/3d/reflection_probes.rs`** -> AI Confidence: **99.24%**
104. **`examples/3d/shadow_caster_receiver.rs`** -> AI Confidence: **99.24%**
105. **`examples/app/render_recovery.rs`** -> AI Confidence: **99.24%**
106. **`examples/ecs/dynamic.rs`** -> AI Confidence: **99.24%**
107. **`examples/large_scenes/bistro/src/main.rs`** -> AI Confidence: **99.24%**
108. **`examples/large_scenes/caldera_hotel/src/main.rs`** -> AI Confidence: **99.24%**
109. **`examples/large_scenes/mipmap_generator/src/lib.rs`** -> AI Confidence: **99.24%**
110. **`examples/testbed/helpers.rs`** -> AI Confidence: **99.24%**
111. **`examples/ui/navigation/directional_navigation.rs`** -> AI Confidence: **99.24%**
112. **`examples/window/window_settings.rs`** -> AI Confidence: **99.24%**
113. **`tools/export-content/src/app.rs`** -> AI Confidence: **99.24%**
114. **`crates/bevy_ecs/src/world/entity_access/component_fetch.rs`** -> AI Confidence: **99.23%**
115. **`crates/bevy_gltf/src/loader/extensions/khr_materials_specular.rs`** -> AI Confidence: **99.23%**
116. **`crates/bevy_mesh/src/mikktspace.rs`** -> AI Confidence: **99.23%**
117. **`crates/bevy_platform/src/cfg.rs`** -> AI Confidence: **99.23%**
118. **`crates/bevy_reflect/derive/src/documentation.rs`** -> AI Confidence: **99.23%**
119. **`crates/bevy_reflect/derive/src/serialization.rs`** -> AI Confidence: **99.23%**
120. **`crates/bevy_reflect/src/enums/helpers.rs`** -> AI Confidence: **99.23%**
121. **`crates/bevy_reflect/src/serde/ser/tuple_structs.rs`** -> AI Confidence: **99.23%**
122. **`crates/bevy_utils/src/debug_info.rs`** -> AI Confidence: **99.23%**
123. **`examples/3d/ssao.rs`** -> AI Confidence: **99.23%**
124. **`examples/gizmos/3d_gizmos.rs`** -> AI Confidence: **99.23%**
125. **`examples/gizmos/light_gizmos.rs`** -> AI Confidence: **99.23%**
126. **`examples/stress_tests/many_buttons.rs`** -> AI Confidence: **99.23%**
127. **`examples/window/monitor_info.rs`** -> AI Confidence: **99.23%**
128. **`benches/benches/bevy_ecs/observers/custom.rs`** -> AI Confidence: **99.18%**
129. **`benches/benches/bevy_ecs/world/commands.rs`** -> AI Confidence: **99.18%**
130. **`benches/benches/bevy_ecs/world/world_get.rs`** -> AI Confidence: **99.18%**
131. **`benches/benches/bevy_picking/ray_mesh_intersection.rs`** -> AI Confidence: **99.18%**
132. **`benches/benches/bevy_reflect/map.rs`** -> AI Confidence: **99.18%**
133. **`crates/bevy_animation/src/gltf_curves.rs`** -> AI Confidence: **99.18%**
134. **`crates/bevy_animation/src/transition.rs`** -> AI Confidence: **99.18%**
135. **`crates/bevy_anti_alias/src/contrast_adaptive_sharpening/mod.rs`** -> AI Confidence: **99.18%**
136. **`crates/bevy_anti_alias/src/fxaa/mod.rs`** -> AI Confidence: **99.18%**
137. **`crates/bevy_anti_alias/src/taa/mod.rs`** -> AI Confidence: **99.18%**
138. **`crates/bevy_app/src/main_schedule.rs`** -> AI Confidence: **99.18%**
139. **`crates/bevy_app/src/task_pool_plugin.rs`** -> AI Confidence: **99.18%**
140. **`crates/bevy_asset/macros/src/lib.rs`** -> AI Confidence: **99.18%**
141. **`crates/bevy_asset/src/asset_changed.rs`** -> AI Confidence: **99.18%**
142. **`crates/bevy_asset/src/io/android.rs`** -> AI Confidence: **99.18%**
143. **`crates/bevy_asset/src/io/embedded/embedded_watcher.rs`** -> AI Confidence: **99.18%**
144. **`crates/bevy_asset/src/io/embedded/mod.rs`** -> AI Confidence: **99.18%**
145. **`crates/bevy_asset/src/io/file/file_asset.rs`** -> AI Confidence: **99.18%**
146. **`crates/bevy_asset/src/io/file/file_watcher.rs`** -> AI Confidence: **99.18%**
147. **`crates/bevy_asset/src/io/memory.rs`** -> AI Confidence: **99.18%**
148. **`crates/bevy_asset/src/io/mod.rs`** -> AI Confidence: **99.18%**
149. **`crates/bevy_asset/src/io/wasm.rs`** -> AI Confidence: **99.18%**
150. **`crates/bevy_asset/src/loader.rs`** -> AI Confidence: **99.18%**
151. **`crates/bevy_asset/src/loader_builders.rs`** -> AI Confidence: **99.18%**
152. **`crates/bevy_asset/src/processor/process.rs`** -> AI Confidence: **99.18%**
153. **`crates/bevy_asset/src/transformer.rs`** -> AI Confidence: **99.18%**
154. **`crates/bevy_camera/src/components.rs`** -> AI Confidence: **99.18%**
155. **`crates/bevy_color/src/xyza.rs`** -> AI Confidence: **99.18%**
156. **`crates/bevy_core_pipeline/src/core_2d/main_transparent_pass_2d_node.rs`** -> AI Confidence: **99.18%**
157. **`crates/bevy_core_pipeline/src/core_2d/mod.rs`** -> AI Confidence: **99.18%**
158. **`crates/bevy_core_pipeline/src/core_3d/main_opaque_pass_3d_node.rs`** -> AI Confidence: **99.18%**
159. **`crates/bevy_core_pipeline/src/fullscreen_material.rs`** -> AI Confidence: **99.18%**
160. **`crates/bevy_core_pipeline/src/mip_generation/mod.rs`** -> AI Confidence: **99.18%**
161. **`crates/bevy_core_pipeline/src/oit/mod.rs`** -> AI Confidence: **99.18%**
162. **`crates/bevy_core_pipeline/src/oit/resolve/mod.rs`** -> AI Confidence: **99.18%**
163. **`crates/bevy_core_pipeline/src/oit/resolve/node.rs`** -> AI Confidence: **99.18%**
164. **`crates/bevy_core_pipeline/src/prepass/background_motion_vectors.rs`** -> AI Confidence: **99.18%**
165. **`crates/bevy_core_pipeline/src/tonemapping/node.rs`** -> AI Confidence: **99.18%**
166. **`crates/bevy_core_pipeline/src/upscaling/node.rs`** -> AI Confidence: **99.18%**
167. **`crates/bevy_dev_tools/src/ci_testing/mod.rs`** -> AI Confidence: **99.18%**
168. **`crates/bevy_dev_tools/src/diagnostics_overlay.rs`** -> AI Confidence: **99.18%**
169. **`crates/bevy_diagnostic/src/entity_count_diagnostics_plugin.rs`** -> AI Confidence: **99.18%**
170. **`crates/bevy_ecs/macros/src/lib.rs`** -> AI Confidence: **99.18%**
171. **`crates/bevy_ecs/src/bundle/info.rs`** -> AI Confidence: **99.18%**
172. **`crates/bevy_ecs/src/bundle/insert.rs`** -> AI Confidence: **99.18%**
173. **`crates/bevy_ecs/src/bundle/remove.rs`** -> AI Confidence: **99.18%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `examples/mobile/android_example/app/src/main/java/org/bevyengine/example/MainActivity.java` -> **100.0%** Exposure
- `examples/mobile/android_example_native/app/src/main/java/org/bevyengine/example/MainActivity.java` -> **100.0%** Exposure
- `benches/benches/bevy_ecs/bundles/insert_many.rs` -> **20.0%** Exposure
- `benches/benches/bevy_ecs/bundles/spawn_many.rs` -> **20.0%** Exposure
- `benches/benches/bevy_ecs/bundles/spawn_many_zst.rs` -> **20.0%** Exposure
### Weaponizable Injection Vectors
- `crates/bevy_ecs/src/query/state.rs` -> **100.0%** Exposure
- `crates/bevy_macro_utils/src/bevy_manifest.rs` -> **100.0%** Exposure
- `benches/benches/bevy_ecs/iteration/iter_frag_foreach_wide.rs` -> **99.9987%** Exposure
- `benches/benches/bevy_ecs/iteration/iter_frag_wide.rs` -> **99.9987%** Exposure
- `crates/bevy_asset/src/path.rs` -> **99.9609%** Exposure
### Raw Memory Manipulation
- `crates/bevy_math/src/primitives/dim3.rs` -> **0.032%** Exposure
- `crates/bevy_ptr/src/lib.rs` -> **0.0194%** Exposure
- `crates/bevy_color/src/oklcha.rs` -> **0.008%** Exposure
- `crates/bevy_color/src/hsla.rs` -> **0.0027%** Exposure
- `crates/bevy_color/src/oklaba.rs` -> **0.0024%** Exposure
### Algorithmic DoS Exposure
- `benches/benches/bevy_ecs/bundles/insert_many.rs` -> **100.0%** Exposure
- `benches/benches/bevy_ecs/bundles/spawn_many.rs` -> **100.0%** Exposure
- `benches/benches/bevy_ecs/bundles/spawn_many_zst.rs` -> **100.0%** Exposure
- `benches/benches/bevy_ecs/bundles/spawn_one_zst.rs` -> **100.0%** Exposure
- `benches/benches/bevy_ecs/change_detection.rs` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `6` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `28170` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `benches/benches/bevy_ecs/world/commands.rs` (RUST) -> Cumulative Risk: **876.61**
- **Archetype:** `file_cluster_4` (Distance: 12.4 IQR)
- **Magnitude:** 637.4 | **LOC:** 252 | **CtrlFlow:** 22.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `spawn_commands` (Impact: 126.9), `insert_commands` (Impact: 96.5), `fake_commands` (Impact: 95.2)

### 2. `crates/bevy_ecs/src/system/schedule_system.rs` (RUST) -> Cumulative Risk: **861.47**
- **Archetype:** `file_cluster_4` (Distance: 12.697 IQR)
- **Magnitude:** 268.8 | **LOC:** 200 | **CtrlFlow:** 17.7% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** Tech Debt (100.0%), Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `run_unsafe` (Impact: 20.2), `initialize` (Impact: 14.2), `run_unsafe` (Impact: 7.7)

### 3. `crates/bevy_ecs/src/system/commands/mod.rs` (RUST) -> Cumulative Risk: **849.61**
- **Archetype:** `file_cluster_4` (Distance: 21.333 IQR)
- **Magnitude:** 1045.52 | **LOC:** 2882 | **CtrlFlow:** 14.2% | **Authorship Centralization:** 8.3%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), State Flux (99.4089%)
- **Heaviest Functions:** `get_param` (Impact: 22.3), `insert_components` (Impact: 20.1), `init_access` (Impact: 12.9)

### 4. `benches/benches/bevy_ecs/scheduling/run_condition.rs` (RUST) -> Cumulative Risk: **847.1**
- **Archetype:** `file_cluster_8` (Distance: 11.924 IQR)
- **Magnitude:** 160.08 | **LOC:** 119 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `run_condition_yes_with_query` (Impact: 23.7), `run_condition_yes_with_resource` (Impact: 23.7), `run_condition_yes` (Impact: 23.4)

### 5. `benches/benches/bevy_tasks/iter.rs` (RUST) -> Cumulative Risk: **845.02**
- **Archetype:** `file_cluster_17` (Distance: 12.262 IQR)
- **Magnitude:** 182.74 | **LOC:** 146 | **CtrlFlow:** 26.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (99.9998%), Concurrency (99.9964%), State Flux (99.9919%)
- **Heaviest Functions:** `bench_many_maps` (Impact: 41.8), `bench_for_each` (Impact: 41.0), `bench_overhead` (Impact: 28.1)

### 6. `benches/benches/bevy_ecs/change_detection.rs` (RUST) -> Cumulative Risk: **814.31**
- **Archetype:** `file_cluster_8` (Distance: 13.15 IQR)
- **Magnitude:** 477.2 | **LOC:** 380 | **CtrlFlow:** 16.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `multiple_archetype_none_changed_detectio` (Impact: 37.1), `all_changed_detection_generic` (Impact: 29.6), `few_changed_detection_generic` (Impact: 29.6)

### 7. `crates/bevy_ecs/src/query/state.rs` (RUST) -> Cumulative Risk: **810.79**
- **Archetype:** `file_cluster_0` (Distance: 17.229 IQR)
- **Magnitude:** 1386.84 | **LOC:** 2438 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 40.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `from_states_uninitialized` (Impact: 511.4), `init_access` (Impact: 25.7), `par_many_fold_init_unchecked_manual` (Impact: 25.4)

### 8. `crates/bevy_render/src/extract_component.rs` (RUST) -> Cumulative Risk: **806.16**
- **Archetype:** `file_cluster_16` (Distance: 12.865 IQR)
- **Magnitude:** 121.9 | **LOC:** 123 | **CtrlFlow:** 31.6% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Concurrency (99.8804%)
- **Heaviest Functions:** `extract_visible_components` (Impact: 38.4), `extract_components` (Impact: 23.4), `build` (Impact: 17.9)

### 9. `crates/bevy_dev_tools/src/easy_screenshot.rs` (RUST) -> Cumulative Risk: **804.93**
- **Archetype:** `file_cluster_13` (Distance: 12.315 IQR)
- **Magnitude:** 326.0 | **LOC:** 399 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 60.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `build` (Impact: 214.6), `build` (Impact: 13.4), `build` (Impact: 7.3)

### 10. `benches/benches/bevy_ecs/world/world_get.rs` (RUST) -> Cumulative Risk: **801.61**
- **Archetype:** `file_cluster_8` (Distance: 11.992 IQR)
- **Magnitude:** 777.62 | **LOC:** 500 | **CtrlFlow:** 23.4% | **Authorship Centralization:** 25.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), State Flux (99.9961%)
- **Heaviest Functions:** `world_query_get` (Impact: 138.1), `query_get` (Impact: 82.9), `world_query_iter` (Impact: 82.4)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `crates/bevy_pbr/src/render/light.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.069 IQR)
- **Top Global Matches:** file_cluster_0: 13.069, file_cluster_13: 13.164, file_cluster_16: 13.265
- **Magnitude:** 3101.08 | **LOC:** 2518 | **CtrlFlow:** 39.4% | **Authorship Centralization:** 39.1%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 28
- **Risk Profile:** Cognitive Load (15.917%), Tech Debt (21.7541%)
**Top Internal Functions/Classes:**
  * `specialize_shadows` (Impact: 1564.5 | O(2^N) | DB: 21)
  * `prepare_lights` (Impact: 1046.5 | O(N^6) | DB: 28)
  * `check_views_lights_need_specialization` (Impact: 107.3 | O(N^6) | DB: 3)
  * `remove_light_view_entities` (Impact: 37.5 | O(N^5) | DB: 2)
  * `extract_ambient_light_resource` (Impact: 23.1 | O(N^3) | DB: 2)
    * *Intent:* // This is needed because of the orphan rule not allowing implementing // foreign trait ExtractResou...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 160`, `structural_boundaries: 246`, `args: 57`, `func_start: 25`, `class_start: 23`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 160`, `dead_code: 7`, `planned_debt: 5`, `orphaned_logic: 9`
* *Architecture:* `api: 87`, `import: 34`
* *Defense:* `safety: 94`, `doc: 49`, `immutability_locks: 27`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` render_resource::*, RenderLayers, core::any::TypeId, view::NoIndirectDrawing, VolumetricLight, CubemapVisibleEntities, ShadowFilteringMethod, bevy_transform::components::GlobalTransform...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_gltf/src/loader/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.104 IQR)
- **Top Global Matches:** file_cluster_0: 13.104, file_cluster_17: 13.286, file_cluster_13: 13.3
- **Magnitude:** 2946.44 | **LOC:** 2931 | **CtrlFlow:** 27.9% | **Authorship Centralization:** 27.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 46
- **Risk Profile:** Cognitive Load (7.5759%), Tech Debt (11.265%)
**Top Internal Functions/Classes:**
  * `load_node` (Impact: 1834.1 | O(2^N) | DB: 46)
  * `load_gltf` (Impact: 616.8 | O(N^6) | DB: 20)
  * `load_material` (Impact: 115.4 | O(N^6))
  * `load_image` (Impact: 114.0 | O(N^6))
  * `load` (Impact: 7.9 | O(N^2) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 146`, `structural_boundaries: 378`, `args: 85`, `func_start: 35`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 133`, `dead_code: 14`, `planned_debt: 9`, `orphaned_logic: 1`
* *Architecture:* `io: 1`, `api: 29`, `concurrency: 48`, `import: 42`
* *Defense:* `safety: 154`, `doc: 86`, `test: 55`, `sync_locks: 4`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` gltf::
    accessor::Iter, primitive_topology, GltfMaterial, uv_channel, AssetPlugin, ImageSampler, Serialize, serde::Deserialize...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_ecs/src/query/iter.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.11%)
- **Global Archetype:** `file_cluster_11` (Drift: 16.138 IQR)
- **Top Global Matches:** file_cluster_11: 16.138, file_cluster_0: 16.156, file_cluster_16: 16.219
- **Magnitude:** 2857.14 | **LOC:** 3394 | **CtrlFlow:** 25.3% | **Authorship Centralization:** 42.9%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 85
- **Risk Profile:** Cognitive Load (19.4751%), Tech Debt (82.6007%)
**Top Internal Functions/Classes:**
  * `fold_over_storage_range` (Impact: 1556.9 | O(2^N) | DB: 85)
    * *Intent:* /// Get the next result from the query. /// /// If the [`QueryData`] does not implement [`IterQueryD...
  * `next` (Impact: 357.9 | O(2^N) | DB: 9)
    * *Intent:* /// - if `K > N`, there are no combinations. /// /// The output combination is not guaranteed to hav...
  * `fetch_next_aliased_unchecked` (Impact: 92.8 | O(N^6) | DB: 2)
  * `size_hint` (Impact: 40.5 | O(N^4))
    * *Intent:* /// An [`Iterator`] over sorted query results of a [`QueryManyIter`]. /// /// This struct is created...
  * `next` (Impact: 32.6 | O(2^N) | DB: 1)
    * *Intent:* // Re-collect into a `Vec` to eagerly drop the lens items.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 197`, `structural_boundaries: 581`, `args: 148`, `func_start: 83`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 1`, `state_mutation: 287`, `dead_code: 68`, `planned_debt: 29`, `duplicate_logic: 19`
* *Architecture:* `api: 48`, `concurrency: 78`, `import: 19`
* *Defense:* `safety: 133`, `doc: 1097`, `test: 28`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` EntityRef, Tables, Debug, crate::
    archetype::Archetype, query::
        ArchetypeFilter, change_detection::Tick, EntityRefExcept, iter::FusedIterator...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_image/src/ktx2.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.46 IQR)
- **Top Global Matches:** file_cluster_8: 11.46, file_cluster_0: 11.962, file_cluster_7: 11.973
- **Magnitude:** 2653.52 | **LOC:** 1542 | **CtrlFlow:** 67.7% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 25
- **Risk Profile:** Cognitive Load (12.1268%), Tech Debt (11.0986%)
**Top Internal Functions/Classes:**
  * `ktx2_dfd_header_to_texture_format` (Impact: 1452.6 | O(N^6))
    * *Intent:* /// Reads the [`TextureFormat`] from a KTX2 data format descriptor header. /// /// # Errors /// /// ...
  * `ktx2_buffer_to_image` (Impact: 491.3 | O(N^6) | DB: 25)
    * *Intent:* /// Converts KTX2 bytes to a bevy [`Image`] using the given compressed format support. /// /// # Err...
  * `ktx2_format_to_texture_format` (Impact: 320.8 | O(N^5))
    * *Intent:* /// Converts a KTX2 texture format identifier to a [`TextureFormat`]. /// /// # Errors /// /// Retur...
  * `get_transcoded_formats` (Impact: 191.8 | O(N^6))
    * *Intent:* /// Determines an appropriate wgpu-compatible format based on compressed format support, and a /// b...
  * `sample_information_to_data_type` (Impact: 74.2 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 329`, `structural_boundaries: 157`, `args: 45`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 54`, `planned_debt: 3`, `fragile_debt: 1`, `orphaned_logic: 1`
* *Architecture:* `io: 2`, `api: 5`, `import: 10`
* *Defense:* `safety: 147`, `doc: 23`, `test: 23`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` basis_universal::
    DecodeFlags, TextureFormat, TextureViewDimension, super::CompressedImageFormats, bevy_utils::default, TextureChannelLayout, LowLevelUastcTranscoder, SampleInformation...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_winit/src/system.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.006 IQR)
- **Top Global Matches:** file_cluster_13: 13.006, file_cluster_8: 13.034, file_cluster_0: 13.099
- **Magnitude:** 2440.38 | **LOC:** 651 | **CtrlFlow:** 50.6% | **Authorship Centralization:** 25.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (18.6654%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `changed_windows` (Impact: 1857.4 | O(2^N) | DB: 11)
    * *Intent:* /// Propagates changes from [`Window`] entities to the [`winit`] backend. /// /// # Notes /// /// - ...
  * `changed_cursor_options` (Impact: 135.4 | O(N^6) | DB: 6)
  * `create_windows` (Impact: 114.7 | O(N^6) | DB: 7)
    * *Intent:* /// Creates new windows on the [`winit`] backend for each entity with a newly-added /// [`Window`] c...
  * `check_keyboard_focus_lost` (Impact: 81.5 | O(N^5) | DB: 9)
    * *Intent:* /// Check whether keyboard focus was lost. This is different from window /// focus in that swapping ...
  * `despawn_windows` (Impact: 74.9 | O(N^5) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 117`, `structural_boundaries: 114`, `args: 16`, `func_start: 6`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 84`
* *Architecture:* `api: 15`, `concurrency: 1`, `import: 14`
* *Defense:* `safety: 70`, `doc: 20`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` WindowCreated, info, Window, LogicalSize, RawHandleWrapper, PhysicalSize, WindowResized, OnMonitor...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_render/src/render_phase/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.564 IQR)
- **Top Global Matches:** file_cluster_16: 13.564, file_cluster_13: 13.635, file_cluster_0: 13.863
- **Magnitude:** 1984.96 | **LOC:** 1733 | **CtrlFlow:** 27.9% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 64
- **Risk Profile:** Cognitive Load (12.7708%), Tech Debt (9.3902%)
**Top Internal Functions/Classes:**
  * `add` (Impact: 1777.8 | O(2^N) | DB: 64)
    * *Intent:* /// A list of the entities in each bin, along with their cached /// [`InputUniformIndex`].
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 77`, `structural_boundaries: 199`, `args: 48`, `func_start: 46`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 114`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `api: 48`, `concurrency: 28`, `import: 27`
* *Defense:* `safety: 60`, `doc: 420`, `test: 1`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Render, bevy_material::labels::DrawFunctionId, crate::renderer::RenderDevice, MainEntityHashMap, DerefMut, bevy_material::descriptor::CachedRenderPipelineId, GetFullBatchData, system::lifetimeless::SRes...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_pbr/src/render/gpu_preprocess.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.797 IQR)
- **Top Global Matches:** file_cluster_16: 12.797, file_cluster_8: 12.799, file_cluster_13: 13.023
- **Magnitude:** 1964.6 | **LOC:** 2552 | **CtrlFlow:** 39.0% | **Authorship Centralization:** 36.4%
- **Algorithmic:** O(N^6) | **DB Complexity:** 31
- **Risk Profile:** Cognitive Load (4.7908%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `late_gpu_preprocess` (Impact: 1307.4 | O(N^6) | DB: 31)
  * `early_gpu_preprocess` (Impact: 500.2 | O(N^6) | DB: 5)
  * `clear_indirect_parameters_metadata` (Impact: 31.9 | O(N^5) | DB: 1)
    * *Intent:* /// The bind group used for the single invocation of the compute shader when /// indirect drawing is...
  * `write_mesh_culling_data_buffer` (Impact: 5.4 | O(N^2) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 127`, `structural_boundaries: 199`, `args: 28`, `func_start: 26`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 72`, `dead_code: 3`
* *Architecture:* `api: 19`, `import: 16`
* *Defense:* `safety: 113`, `doc: 218`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Render, PreviousViewUniforms, BufferBinding, texture_2d, TextureSampleType, entity::Entity, IndirectParametersGpuMetadata, renderer::RenderContext...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_asset/src/server/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.042 IQR)
- **Top Global Matches:** file_cluster_0: 14.042, file_cluster_16: 14.106, file_cluster_4: 14.177
- **Magnitude:** 1908.4 | **LOC:** 2245 | **CtrlFlow:** 31.6% | **Authorship Centralization:** 76.9%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (29.5696%), Tech Debt (48.7748%)
**Top Internal Functions/Classes:**
  * `wait_for_asset_id` (Impact: 425.0 | O(N^6) | DB: 13)
    * *Intent:* /// Returns the path for the given `id`, if it has one.
  * `load_internal` (Impact: 375.1 | O(2^N) | DB: 4)
    * *Intent:* /// /// #[derive(Resource)] /// struct LoadingUntypedHandle(Handle<LoadedUntypedAsset>); /// /// fn ...
  * `get_meta_loader_and_reader` (Impact: 169.9 | O(N^6) | DB: 3)
  * `load_folder_internal` (Impact: 102.2 | O(N^6) | DB: 4)
  * `load_with_meta_transform` (Impact: 46.6 | O(N^5) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 158`, `structural_boundaries: 342`, `args: 88`, `func_start: 73`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 70`, `dead_code: 12`, `planned_debt: 6`, `orphaned_logic: 22`
* *Architecture:* `io: 1`, `api: 85`, `concurrency: 198`, `import: 28`
* *Defense:* `safety: 216`, `doc: 347`, `test: 1`, `sync_locks: 13`, `immutability_locks: 34`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` core::any::TypeId, AssetActionMinimal, ErasedLoadedAsset, LoadedUntypedAsset, AssetMetaDyn, AssetMetaCheck, AssetLoadFailedEvent, bevy_tasks::IoTaskPool...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_ecs/src/query/fetch.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_16` (Drift: 14.919 IQR)
- **Top Global Matches:** file_cluster_16: 14.919, file_cluster_0: 14.92, file_cluster_11: 15.076
- **Magnitude:** 1879.56 | **LOC:** 4326 | **CtrlFlow:** 27.2% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (18.2891%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `update_component_access` (Impact: 106.4 | O(2^N) | DB: 6)
  * `fetch_contiguous` (Impact: 30.0 | O(2^N) | DB: 2)
    * *Intent:* /// /// # Footguns /// /// Note that a `Query<Has<T>>` will match all existing entities. /// Beware!...
  * `set_archetype` (Impact: 23.4 | O(2^N) | DB: 2)
  * `set_archetype` (Impact: 21.9 | O(2^N) | DB: 1)
  * `set_table` (Impact: 21.9 | O(2^N) | DB: 2)
    * *Intent:* /// When `Mut<T>` is used in a query, it will be converted to `Ref<T>` when transformed into its rea...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 254`, `structural_boundaries: 680`, `args: 317`, `func_start: 282`, `class_start: 36`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 291`, `dead_code: 50`, `planned_debt: 7`, `duplicate_logic: 245`, `orphaned_logic: 1`
* *Architecture:* `api: 45`, `concurrency: 72`, `import: 10`
* *Defense:* `safety: 129`, `doc: 620`, `test: 37`, `immutability_locks: 100`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` EntityRef, ContiguousRef, bevy_ecs::entity::Entity, crate::
    archetype::Archetype, bevy_ptr::ThinSlicePtr, FilteredAccess, EntityRefExcept, UnsafeCellDeref...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_pbr/src/wireframe.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.949 IQR)
- **Top Global Matches:** file_cluster_16: 12.949, file_cluster_0: 13.044, file_cluster_8: 13.124
- **Magnitude:** 1642.64 | **LOC:** 1644 | **CtrlFlow:** 36.3% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (7.906%), Tech Debt (22.5079%)
**Top Internal Functions/Classes:**
  * `queue_wireframes` (Impact: 286.7 | O(N^5) | DB: 4)
  * `render` (Impact: 187.1 | O(N^6) | DB: 1)
  * `prepare_wireframe_wide_bind_groups` (Impact: 179.6 | O(N^4) | DB: 5)
  * `check_wireframe_entities_needing_special` (Impact: 148.5 | O(N^6) | DB: 3)
    * *Intent:* /// Applies or removes a wireframe material on any mesh without a [`Wireframe`] or [`NoWireframe`] c...
  * `specialize` (Impact: 91.8 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 136`, `structural_boundaries: 239`, `args: 32`, `func_start: 29`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 129`, `dead_code: 2`, `duplicate_logic: 6`
* *Architecture:* `api: 67`, `import: 17`
* *Defense:* `safety: 93`, `doc: 81`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` MeshPipelineKey, Render, core::any::TypeId, ExtractedCamera, MainEntityHashMap, MeshSlabs, sync_world::MainEntity, PhaseItemExtraIndex...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_input/src/gamepad.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.863 IQR)
- **Top Global Matches:** file_cluster_0: 13.863, file_cluster_13: 14.123, file_cluster_8: 14.22
- **Magnitude:** 1462.52 | **LOC:** 2979 | **CtrlFlow:** 46.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 23
- **Risk Profile:** Cognitive Load (6.4241%), Tech Debt (79.7652%)
**Top Internal Functions/Classes:**
  * `gamepad_connection_system` (Impact: 655.5 | O(2^N) | DB: 23)
  * `new` (Impact: 121.5 | O(N^5))
  * `new` (Impact: 43.3 | O(N^5))
    * *Intent:* /// Returns `true` if any item in the [`GamepadButton`] iterator has been pressed.
  * `get_axis_position_from_value` (Impact: 42.8 | O(N^3))
  * `clamp` (Impact: 28.3 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 122`, `structural_boundaries: 141`, `args: 67`, `func_start: 74`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 69`, `dead_code: 10`, `duplicate_logic: 21`
* *Architecture:* `api: 102`, `import: 20`
* *Defense:* `safety: 197`, `doc: 538`, `test: 39`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ButtonInput, MessageReader, ButtonSettings, bevy_math::ops, bevy_ecs::entity::Entity, GamepadRumbleIntensity, super::
        gamepad_connection_system, core::time::Duration...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_ecs/src/entity/clone_entities.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.349 IQR)
- **Top Global Matches:** file_cluster_0: 13.349, file_cluster_4: 13.5, file_cluster_16: 13.548
- **Magnitude:** 1459.12 | **LOC:** 2608 | **CtrlFlow:** 13.4% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (41.1759%), Tech Debt (95.301%)
**Top Internal Functions/Classes:**
  * `clone_components` (Impact: 122.6 | O(N^5) | DB: 5)
  * `clone_entity_internal` (Impact: 74.9 | O(N^6) | DB: 11)
  * `filter_allow` (Impact: 62.1 | O(N^5) | DB: 3)
  * `clone_entity_mapped_internal` (Impact: 61.7 | O(N^4) | DB: 4)
  * `clone_components` (Impact: 56.8 | O(N^5) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 92`, `structural_boundaries: 595`, `args: 119`, `func_start: 91`, `class_start: 77`
* *Risk/State:* `safety_bypasses: 41`, `high_risk_execution: 1`, `state_mutation: 246`, `dead_code: 10`, `planned_debt: 3`, `duplicate_logic: 10`, `orphaned_logic: 38`
* *Architecture:* `api: 45`, `concurrency: 259`, `import: 24`
* *Defense:* `safety: 109`, `doc: 325`, `test: 135`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` alloc::boxed::Box, core::any::TypeId, lifecycle::HookContext, crate::
    archetype::Archetype, FilterableIds, Marker, crate::reflect::AppTypeRegistry, ReflectComponent...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_ecs/src/world/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_0` (Drift: 22.62 IQR)
- **Top Global Matches:** file_cluster_0: 22.62, file_cluster_11: 22.746, file_cluster_4: 22.781
- **Magnitude:** 1443.34 | **LOC:** 4641 | **CtrlFlow:** 17.8% | **Authorship Centralization:** 18.2%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 81
- **Risk Profile:** Cognitive Load (30.5133%), Tech Debt (26.0351%)
**Top Internal Functions/Classes:**
  * `iter_resources_mut` (Impact: 675.7 | O(2^N) | DB: 81)
    * *Intent:* /// [`ComponentId`] from the provided [`Entity`] and runs the provided /// closure on it, returning ...
  * `despawn_no_free_with_caller` (Impact: 20.8 | O(2^N) | DB: 2)
    * *Intent:* /// A faster version of [`spawn_at`](Self::spawn_at) for the empty bundle.
  * `spawn_at_unchecked` (Impact: 19.8 | O(N^4) | DB: 6)
    * *Intent:* /// y: f32, /// } /// /// let mut world = World::new(); /// let e1 = world.spawn(Position { x: 0.0, ...
  * `despawn_with_caller` (Impact: 18.7 | O(2^N) | DB: 1)
    * *Intent:* /// Spawns `bundle` on `entity`.
  * `register_component_hooks_by_id` (Impact: 12.3 | O(N^2) | DB: 2)
    * *Intent:* /// Retrieves this world's [`Storages`] collection. #[inline]
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 95`, `structural_boundaries: 440`, `args: 134`, `func_start: 93`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 37`, `high_risk_execution: 1`, `state_mutation: 222`, `dead_code: 230`, `planned_debt: 3`, `orphaned_logic: 14`
* *Architecture:* `api: 94`, `concurrency: 136`, `import: 37`
* *Defense:* `safety: 133`, `doc: 1921`, `test: 124`, `sync_locks: 11`, `immutability_locks: 2`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` core::any::TypeId, MovingPtr, alloc::
        borrow::ToOwned, entity_access::
    ComponentEntry, InsertMode, world::
        command_queue::RawCommandQueue, FilteredEntityRef, REMOVE...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_light/src/lib.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.723 IQR)
- **Top Global Matches:** file_cluster_13: 12.723, file_cluster_0: 12.944, file_cluster_16: 12.998
- **Magnitude:** 1409.64 | **LOC:** 703 | **CtrlFlow:** 36.5% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(N^6) | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (8.9566%), Tech Debt (16.3886%)
**Top Internal Functions/Classes:**
  * `check_point_light_mesh_visibility` (Impact: 774.9 | O(N^6) | DB: 14)
  * `check_dir_light_mesh_visibility` (Impact: 517.3 | O(N^6) | DB: 18)
  * `build` (Impact: 8.1 | O(N^6) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 113`, `args: 17`, `func_start: 3`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 63`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 1`, `orphaned_logic: 1`
* *Architecture:* `api: 36`, `import: 26`
* *Defense:* `safety: 29`, `doc: 105`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` RenderLayers, core::any::TypeId, VolumetricLight, CubemapVisibleEntities, SpotLightTexture, bevy_transform::components::GlobalTransform, AmbientLight, Cascades...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_ecs/src/query/state.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_0` (Drift: 17.229 IQR)
- **Top Global Matches:** file_cluster_0: 17.229, file_cluster_4: 17.239, file_cluster_11: 17.505
- **Magnitude:** 1386.84 | **LOC:** 2438 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 40.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 71
- **Risk Profile:** Cognitive Load (48.5729%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `from_states_uninitialized` (Impact: 511.4 | O(N^6) | DB: 71)
  * `init_access` (Impact: 25.7 | O(N^4) | DB: 2)
  * `par_many_fold_init_unchecked_manual` (Impact: 25.4 | O(N^5) | DB: 4)
    * *Intent:* /// Returns an [`Iterator`] over all possible combinations of `K` query results for the /// given [`...
  * `try_new` (Impact: 12.5 | O(N^3) | DB: 2)
  * `fmt` (Impact: 9.2 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 76`, `structural_boundaries: 482`, `args: 111`, `func_start: 89`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 22`, `high_risk_execution: 3`, `state_mutation: 255`, `dead_code: 60`
* *Architecture:* `api: 98`, `concurrency: 295`, `import: 12`
* *Defense:* `safety: 35`, `doc: 756`, `test: 77`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::entity::UniqueEntityEquivalentSlice, prelude::FromWorld, fixedbitset::FixedBitSet, TableId, crate::
    archetype::Archetype, prelude::*, alloc::format, QueryIter...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_asset/src/lib.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.847 IQR)
- **Top Global Matches:** file_cluster_16: 12.847, file_cluster_8: 13.01, file_cluster_0: 13.024
- **Magnitude:** 1380.82 | **LOC:** 3073 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 63.6%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (15.6857%), Tech Debt (92.1612%)
**Top Internal Functions/Classes:**
  * `load_error_events` (Impact: 111.8 | O(N^6) | DB: 8)
  * `load_folder` (Impact: 101.9 | O(2^N) | DB: 5)
  * `load` (Impact: 87.6 | O(2^N) | DB: 6)
  * `asset_dependency_is_tracked_when_not_loa` (Impact: 68.0 | O(N^4) | DB: 10)
  * `load_dependencies` (Impact: 64.0 | O(N^3) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 131`, `structural_boundaries: 590`, `args: 120`, `func_start: 83`, `class_start: 35`
* *Risk/State:* `safety_bypasses: 64`, `high_risk_execution: 4`, `state_mutation: 235`, `planned_debt: 3`, `duplicate_logic: 18`, `orphaned_logic: 28`
* *Architecture:* `io: 9`, `api: 28`, `concurrency: 98`, `import: 15`
* *Defense:* `safety: 105`, `doc: 264`, `test: 192`, `sync_locks: 2`, `immutability_locks: 18`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` core::any::TypeId, direct_access_ext::DirectAssetAccessExt, Process, server::*, bevy_ecs::
        message::MessageCursor, AssetPlugin, Serialize, AsyncSeekExt...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_pbr/src/material_bind_groups.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.379 IQR)
- **Top Global Matches:** file_cluster_16: 13.379, file_cluster_8: 13.448, file_cluster_0: 13.515
- **Magnitude:** 1363.8 | **LOC:** 2057 | **CtrlFlow:** 37.2% | **Authorship Centralization:** 25.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (8.9311%), Tech Debt (99.9469%)
**Top Internal Functions/Classes:**
  * `prepare_bind_group` (Impact: 381.0 | O(N^6) | DB: 12)
  * `insert_resources` (Impact: 90.6 | O(N^6) | DB: 3)
    * *Intent:* /// Returns the bindings in the binding index table. /// /// If the current [`MaterialBindlessIndexT...
  * `prepare` (Impact: 88.3 | O(2^N) | DB: 2)
  * `check_allocation` (Impact: 80.9 | O(N^6) | DB: 1)
  * `prepare_bind_groups` (Impact: 73.8 | O(N^6) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 110`, `structural_boundaries: 186`, `args: 54`, `func_start: 46`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 23`, `high_risk_execution: 1`, `state_mutation: 107`, `dead_code: 7`, `planned_debt: 1`, `duplicate_logic: 31`, `orphaned_logic: 4`
* *Architecture:* `api: 16`, `import: 3`
* *Defense:* `safety: 111`, `doc: 370`, `test: 6`, `immutability_locks: 6`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` core::hash::Hash, BufferBinding, WgpuSampler, bevy_render::
    render_resource::
        BindGroup, PreparedBindGroup, BufferInitDescriptor, BindingNumber, OwnedBindingResource...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_animation/src/lib.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.246 IQR)
- **Top Global Matches:** file_cluster_0: 13.246, file_cluster_13: 13.304, file_cluster_16: 13.325
- **Magnitude:** 1331.86 | **LOC:** 1706 | **CtrlFlow:** 32.1% | **Authorship Centralization:** 40.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (22.4971%), Tech Debt (60.2586%)
**Top Internal Functions/Classes:**
  * `animate_targets` (Impact: 565.4 | O(N^6) | DB: 6)
    * *Intent:* /// Returns the repeat mode assigned to this active animation.
  * `from_animation` (Impact: 97.7 | O(N^5))
  * `next` (Impact: 40.6 | O(2^N) | DB: 1)
  * `get_or_insert_with` (Impact: 34.5 | O(2^N) | DB: 5)
  * `test_animation_target_id` (Impact: 33.3 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 109`, `structural_boundaries: 231`, `args: 35`, `func_start: 53`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 121`, `dead_code: 2`, `planned_debt: 1`, `orphaned_logic: 19`
* *Architecture:* `api: 51`, `concurrency: 48`, `import: 25`
* *Defense:* `safety: 65`, `doc: 302`, `test: 12`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Assets, hash::NoOpHash, AnimationNodeIndex, Map, core::
    any::TypeId, animation_event::*, AnimationPlayer, crate::
    animation_curves::AnimationCurve...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_pbr/src/render/mesh.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.817 IQR)
- **Top Global Matches:** file_cluster_16: 13.817, file_cluster_13: 13.857, file_cluster_8: 13.981
- **Magnitude:** 1294.64 | **LOC:** 4358 | **CtrlFlow:** 37.4% | **Authorship Centralization:** 30.3%
- **Algorithmic:** O(N^6) | **DB Complexity:** 50
- **Risk Profile:** Cognitive Load (10.106%), Tech Debt (11.1671%)
**Top Internal Functions/Classes:**
  * `finish` (Impact: 961.1 | O(N^6) | DB: 50)
  * `atomic_u64_zero_bit_iter` (Impact: 30.1 | O(N^5) | DB: 41)
  * `build` (Impact: 22.1 | O(N^6) | DB: 1)
    * *Intent:* #[derive(Debug, Hash, PartialEq, Eq, Clone, SystemSet)]
  * `mesh_key_msaa_samples` (Impact: 5.5 | O(N^2))
  * `new` (Impact: 4.3 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 190`, `structural_boundaries: 318`, `args: 53`, `func_start: 42`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 178`, `dead_code: 4`, `planned_debt: 4`, `fragile_debt: 4`
* *Architecture:* `api: 56`, `import: 50`
* *Defense:* `safety: 157`, `doc: 403`, `test: 6`, `sync_locks: 2`, `immutability_locks: 32`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` render_resource::*, RenderLayers, core::any::TypeId, MeshPipelineKey, Parallel, ShadowFilteringMethod, prepass::MotionVectorPrepass, bevy_render::RenderSystems::PrepareAssets...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_asset/src/server/info.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.099 IQR)
- **Top Global Matches:** file_cluster_16: 13.099, file_cluster_0: 13.172, file_cluster_13: 13.177
- **Magnitude:** 1280.22 | **LOC:** 829 | **CtrlFlow:** 37.3% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (16.8907%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `process_asset_load` (Impact: 509.1 | O(2^N) | DB: 10)
  * `process_asset_fail` (Impact: 212.1 | O(N^6) | DB: 18)
  * `propagate_loaded_state` (Impact: 155.9 | O(2^N) | DB: 2)
  * `propagate_failed_state` (Impact: 62.4 | O(2^N) | DB: 2)
  * `create_handle_internal` (Impact: 53.6 | O(N^4) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 101`, `structural_boundaries: 170`, `args: 34`, `func_start: 24`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 96`, `dead_code: 3`
* *Architecture:* `api: 45`, `import: 12`
* *Defense:* `safety: 116`, `doc: 37`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` core::any::TypeId, bevy_utils::TypeIdMap, ErasedLoadedAsset, RecursiveDependencyLoadState, AssetIndex, Handle, AssetLoadError, sync::Arc...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_pbr/src/meshlet/material_pipeline_prepare.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.578 IQR)
- **Top Global Matches:** file_cluster_8: 11.578, file_cluster_13: 11.659, file_cluster_16: 11.732
- **Magnitude:** 1269.1 | **LOC:** 480 | **CtrlFlow:** 45.1% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (14.5602%), Tech Debt (11.5589%)
**Top Internal Functions/Classes:**
  * `prepare_material_meshlet_meshes_main_opa` (Impact: 673.6 | O(N^6) | DB: 10)
    * *Intent:* /// Prepare [`Material`] pipelines for [`MeshletMesh`](`super::MeshletMesh`) entities for use in [`m...
  * `prepare_material_meshlet_meshes_prepass` (Impact: 525.4 | O(N^6) | DB: 12)
    * *Intent:* /// Prepare [`Material`] pipelines for [`MeshletMesh`](`super::MeshletMesh`) entities for use in [`m...
  * `fake_vertex_buffer_layout` (Impact: 8.5 | O(N^5) | DB: 1)
    * *Intent:* // Meshlet materials don't use a traditional vertex buffer, but the material specialization requires...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 79`, `args: 21`, `func_start: 3`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 45`, `orphaned_logic: 2`
* *Architecture:* `api: 8`, `import: 14`
* *Defense:* `safety: 30`, `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` render_resource::*, MeshVertexBufferLayout, bevy_mesh::VertexBufferLayout, bevy_material::
    key::ErasedMaterialPipelineKey, ShadowFilteringMethod, OpaqueRendererMethod, tonemapping::DebandDither, DerefMut...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_ecs/src/entity/unique_slice.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.375 IQR)
- **Top Global Matches:** file_cluster_16: 13.375, file_cluster_8: 13.865, file_cluster_7: 13.994
- **Magnitude:** 1249.9 | **LOC:** 1896 | **CtrlFlow:** 26.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (12.8141%), Tech Debt (99.9998%)
**Top Internal Functions/Classes:**
  * `first_chunk` (Impact: 18.2 | O(2^N))
    * *Intent:* /// Returns an array reference to the first `N` items in the slice. /// /// Equivalent to [`[T]::fir...
  * `split_first_chunk` (Impact: 18.2 | O(2^N))
    * *Intent:* /// Returns an array reference to the first `N` items in the slice and the remaining slice. /// /// ...
  * `split_last_chunk` (Impact: 18.2 | O(2^N))
    * *Intent:* /// Returns an array reference to the last `N` items in the slice and the remaining slice. /// /// E...
  * `last_chunk` (Impact: 18.2 | O(2^N))
    * *Intent:* /// Returns an array reference to the last `N` items in the slice. /// /// Equivalent to [`[T]::last...
  * `split_at_checked` (Impact: 17.9 | O(2^N))
    * *Intent:* /// Divides one mutable slice into two at an index, without doing bounds checking. /// /// Equivalen...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 117`, `structural_boundaries: 318`, `args: 161`, `func_start: 154`, `class_start: 3`
* *Risk/State:* `state_mutation: 173`, `dead_code: 3`, `duplicate_logic: 82`, `orphaned_logic: 9`
* *Architecture:* `api: 108`, `import: 6`
* *Defense:* `safety: 101`, `doc: 470`, `immutability_locks: 39`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` UniqueEntityEquivalentVec, bevy_platform::sync::Arc, Index, core::
    array::TryFromSliceError, RangeToInclusive, ToOwned, iter::FusedIterator, ptr...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_reflect/derive/src/derive_data.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.02 IQR)
- **Top Global Matches:** file_cluster_16: 13.02, file_cluster_0: 13.033, file_cluster_13: 13.127
- **Magnitude:** 1244.8 | **LOC:** 1423 | **CtrlFlow:** 36.8% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (5.7831%), Tech Debt (98.61%)
**Top Internal Functions/Classes:**
  * `from_input` (Impact: 202.9 | O(N^6) | DB: 5)
  * `impl_is_generic` (Impact: 166.5 | O(2^N) | DB: 3)
  * `get_clone_impl` (Impact: 113.0 | O(2^N) | DB: 1)
  * `to_info_tokens` (Impact: 65.0 | O(2^N) | DB: 1)
    * *Intent:* /// Get an iterator of fields which are ignored by the reflection API
  * `get_clone_impl` (Impact: 62.8 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 111`, `structural_boundaries: 191`, `args: 82`, `func_start: 58`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 35`, `dead_code: 6`, `duplicate_logic: 26`, `orphaned_logic: 6`
* *Architecture:* `api: 73`, `import: 15`
* *Defense:* `safety: 136`, `doc: 248`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` remote::RemoteType, DeriveInput, ReflectTraitToImpl, bevy_macro_utils::ResultSifter, spanned::Spanned, FQOption, Variant, quote...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_asset/src/processor/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.052 IQR)
- **Top Global Matches:** file_cluster_4: 14.052, file_cluster_13: 14.388, file_cluster_0: 14.503
- **Magnitude:** 1241.26 | **LOC:** 1865 | **CtrlFlow:** 29.7% | **Authorship Centralization:** 85.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 34
- **Risk Profile:** Cognitive Load (49.7777%), Tech Debt (15.0742%)
**Top Internal Functions/Classes:**
  * `write_default_meta_file_for_path` (Impact: 666.4 | O(N^6) | DB: 34)
    * *Intent:* // If we can't upgrade the task sender, that means all sources of tasks // (like the source event li...
  * `start` (Impact: 57.9 | O(2^N))
  * `spawn_source_change_event_listeners` (Impact: 48.2 | O(N^6))
  * `queue_initial_processing_tasks` (Impact: 11.7 | O(N^4))
  * `new` (Impact: 9.0 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 105`, `structural_boundaries: 248`, `args: 34`, `func_start: 30`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 93`, `dead_code: 7`, `planned_debt: 4`, `orphaned_logic: 2`
* *Architecture:* `api: 19`, `concurrency: 278`, `import: 15`
* *Defense:* `safety: 108`, `doc: 184`, `test: 1`, `sync_locks: 13`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` AssetActionMinimal, instrument::Instrument, ProcessedInfoMinimal, crate::
    io::
        AssetReaderError, WriteDefaultMetaError, string::String, AssetMetaDyn, AssetSourceBuilders...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/3d/ssr.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.222 IQR)
- **Top Global Matches:** file_cluster_8: 12.222, file_cluster_0: 12.426, file_cluster_4: 12.427
- **Magnitude:** 1222.68 | **LOC:** 880 | **CtrlFlow:** 34.9% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 22
- **Risk Profile:** Cognitive Load (37.3093%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `adjust_app_settings` (Impact: 780.5 | O(N^6) | DB: 22)
    * *Intent:* // Adjusts app settings per user input.
  * `move_camera` (Impact: 57.2 | O(N^4) | DB: 6)
    * *Intent:* // Processes input related to camera movement.
  * `adjustment_button` (Impact: 42.0 | O(N^5))
  * `spawn_capsules` (Impact: 15.0 | O(N^5) | DB: 3)
    * *Intent:* // Spawns the row of capsules.
  * `fmt` (Impact: 14.3 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 123`, `args: 24`, `func_start: 21`, `class_start: 16`
* *Risk/State:* `state_mutation: 119`, `duplicate_logic: 2`, `orphaned_logic: 2`
* *Architecture:* `concurrency: 62`, `import: 4`
* *Defense:* `safety: 35`, `doc: 34`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` BUTTON_BORDER, render::render_resource::AsBindGroup, ShaderType, ScreenSpaceReflections, MaterialExtension, vec4, prelude::*, main_ui_node...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `benches/benches/bevy_ecs/components/add_remove.rs` (RUST) | Magnitude: 23.76 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 9, state_mutation: 4, class_start: 3
- `crates/bevy_ecs/src/schedule/condition.rs` (RUST) | Magnitude: 716.1 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: doc: 1074, indent_spaces: 699, generics: 313, structural_boundaries: 303
- `crates/bevy_gilrs/src/lib.rs` (RUST) | Magnitude: 69.96 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 56, structural_boundaries: 33, doc: 19, decorators: 18
- `examples/ecs/message.rs` (RUST) | Magnitude: 111.92 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 67, state_mutation: 30, structural_boundaries: 17, generics: 15
- `crates/bevy_material/src/lib.rs` (RUST) | Magnitude: 47.08 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 55, doc: 33, api: 29, encapsulation: 29

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `examples/ecs/hotpatching_systems.rs` (RUST) | Magnitude: 58.54 | Delta: **0.049 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 42, doc: 15, concurrency: 15, structural_boundaries: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `crates/bevy_ecs/src/query/iter.rs` (RUST) | Magnitude: 2857.14 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 2101, doc: 1097, structural_boundaries: 581, generics: 465
- `crates/bevy_render/src/extract_resource.rs` (RUST) | Magnitude: 140.12 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 35, doc: 18, structural_boundaries: 17, generics: 13
- `crates/bevy_ecs/macros/src/component.rs` (RUST) | Magnitude: 695.36 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 276, branch: 92, safety: 79, structural_boundaries: 54
- `crates/bevy_ecs/src/change_detection/traits.rs` (RUST) | Magnitude: 152.78 | Delta: **0.04 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: doc: 316, indent_spaces: 78, state_mutation: 38, structural_boundaries: 35
- `crates/bevy_reflect/src/func/reflect_fn_mut.rs` (RUST) | Magnitude: 424.0 | Delta: **0.076 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 116, state_mutation: 75, doc: 70, generics: 70

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `crates/bevy_core_pipeline/src/fullscreen_material.rs` (RUST) | Magnitude: 215.14 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 217, structural_boundaries: 62, generics: 37, safety: 31
- `crates/bevy_render/src/mesh/allocator.rs` (RUST) | Magnitude: 658.5 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 578, doc: 234, structural_boundaries: 146, branch: 69
- `crates/bevy_render/src/texture/texture_cache.rs` (RUST) | Magnitude: 71.76 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 71, structural_boundaries: 17, doc: 13, state_mutation: 10
- `crates/bevy_sprite_render/src/sprite_mesh/sprite_material.rs` (RUST) | Magnitude: 257.94 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 257, structural_boundaries: 71, state_mutation: 31, api: 29
- `crates/bevy_ui/src/layout/debug.rs` (RUST) | Magnitude: 140.36 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 68, structural_boundaries: 20, branch: 10, state_mutation: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `crates/bevy_ecs/src/query/fetch.rs` (RUST) | Magnitude: 1879.56 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 2462, generics: 1066, structural_boundaries: 680, doc: 620
- `crates/bevy_anti_alias/src/dlss/mod.rs` (RUST) | Magnitude: 206.14 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 252, structural_boundaries: 63, doc: 42, generics: 34
- `crates/bevy_platform/src/time/fallback.rs` (RUST) | Magnitude: 66.6 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 81, doc: 43, structural_boundaries: 27, pointers: 16
- `crates/bevy_pbr/src/render/gpu_preprocess.rs` (RUST) | Magnitude: 1964.6 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 1349, doc: 218, structural_boundaries: 199, generics: 137
- `crates/bevy_ecs/src/never.rs` (RUST) | Magnitude: 17.2 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 27, indent_spaces: 7, structural_boundaries: 6, sec_high_risk_execution: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `benches/benches/bevy_ecs/scheduling/schedule.rs` (RUST) | Magnitude: 84.86 | Delta: **0.062 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 59, structural_boundaries: 49, state_mutation: 41, args: 20
- `crates/bevy_math/src/sampling/mesh_sampling.rs` (RUST) | Magnitude: 20.24 | Delta: **0.095 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 25, indent_spaces: 20, structural_boundaries: 11, generics: 8
- `benches/benches/bevy_ecs/scheduling/running_systems.rs` (RUST) | Magnitude: 340.46 | Delta: **0.111 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 114, state_mutation: 94, structural_boundaries: 87, args: 32
- `crates/bevy_asset/macros/src/lib.rs` (RUST) | Magnitude: 71.24 | Delta: **0.136 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 75, structural_boundaries: 33, args: 20, safety: 12
- `crates/bevy_ecs/compile_fail/tests/ui/query_lifetime_safety.rs` (RUST) | Magnitude: 43.06 | Delta: **0.14 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 62, structural_boundaries: 55, state_mutation: 28, safety_bypasses: 21

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `crates/bevy_reflect/src/impls/macros/map.rs` (RUST) | Magnitude: 414.64 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 204, structural_boundaries: 52, safety: 44, args: 43
- `examples/2d/sprite_animation.rs` (RUST) | Magnitude: 95.3 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 85, state_mutation: 25, structural_boundaries: 23, concurrency: 14
- `examples/transforms/scale.rs` (RUST) | Magnitude: 74.88 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 48, state_mutation: 33, structural_boundaries: 17, concurrency: 8
- `examples/ecs/one_shot_systems.rs` (RUST) | Magnitude: 78.18 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 57, concurrency: 24, structural_boundaries: 16, doc: 13
- `examples/app/persisting_preferences.rs` (RUST) | Magnitude: 93.92 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 81, state_mutation: 26, structural_boundaries: 19, concurrency: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `crates/bevy_reflect/src/serde/de/processor.rs` (RUST) | Magnitude: 22.5 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 190, dead_code: 19, indent_spaces: 19, safety: 9
- `crates/bevy_reflect/src/type_info.rs` (RUST) | Magnitude: 195.52 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: doc: 289, indent_spaces: 227, structural_boundaries: 50, generics: 46
- `crates/bevy_ui_render/src/ui_material.rs` (RUST) | Magnitude: 39.58 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 93, indent_spaces: 33, generics: 27, structural_boundaries: 23
- `crates/bevy_render/src/render_resource/atomic_pod.rs` (RUST) | Magnitude: 65.48 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 103, indent_spaces: 40, structural_boundaries: 9, state_mutation: 7
- `examples/shader_advanced/custom_render_phase.rs` (RUST) | Magnitude: 38.3 | Delta: **0.091 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 36, doc: 25, safety: 13, structural_boundaries: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `crates/bevy_ecs/src/component/constants.rs` (RUST) | Magnitude: 19.12 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 7, api: 6, immutability_locks: 6, encapsulation: 6
- `crates/bevy_dylib/src/lib.rs` (RUST) | Magnitude: 15.22 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 49, indent_spaces: 5, decorators: 3, structural_boundaries: 1
- `crates/bevy_math/src/ops.rs` (RUST) | Magnitude: 172.2 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 248, indent_spaces: 166, scientific: 88, api: 58
- `crates/bevy_color/src/palettes/basic.rs` (RUST) | Magnitude: 31.34 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 20, api: 16, immutability_locks: 16, encapsulation: 16
- `crates/bevy_winit/src/winit_config.rs` (RUST) | Magnitude: 8.8 | Delta: **0.054 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 53, indent_spaces: 13, structural_boundaries: 4, api: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `crates/bevy_ecs/src/storage/table/column.rs` (RUST) | Magnitude: 131.02 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 256, doc: 148, api: 30, args: 28
- `benches/benches/bevy_ecs/world/despawn_recursive.rs` (RUST) | Magnitude: 34.26 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 12, args: 7, closures: 6
- `crates/bevy_feathers/src/controls/color_slider.rs` (RUST) | Magnitude: 275.68 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 264, structural_boundaries: 50, state_mutation: 36, doc: 33
- `examples/shader/shader_material_wesl.rs` (RUST) | Magnitude: 76.0 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 80, structural_boundaries: 21, state_mutation: 18, generics: 14
- `examples/gltf/gltf_skinned_mesh.rs` (RUST) | Magnitude: 34.88 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 30, doc: 14, structural_boundaries: 12, state_mutation: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `crates/bevy_reflect/src/serde/ser/processor.rs` (RUST) | Magnitude: 16.28 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: doc: 168, dead_code: 21, indent_spaces: 19, safety: 8
- `crates/bevy_macro_utils/src/member.rs` (RUST) | Magnitude: 5.68 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: doc: 41, dead_code: 7, args: 3, api: 2

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `crates/bevy_text/src/text.rs` -> Churn: **81.46%** | Cog Load: 6.5845% | Debt: 100.0%
- `crates/bevy_ecs/src/lib.rs` -> Churn: **74.52%** | Cog Load: 82.8441% | Debt: 96.4024%
- `crates/bevy_ecs/src/system/system_param.rs` -> Churn: **74.52%** | Cog Load: 25.1188% | Debt: 100.0%
- `crates/bevy_ui/src/widget/text.rs` -> Churn: **73.15%** | Cog Load: 28.0347% | Debt: 93.6453%
- `crates/bevy_asset/src/processor/tests.rs` -> Churn: **71.7%** | Cog Load: 41.8224% | Debt: 81.0086%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `crates/bevy_asset/src/processor/mod.rs` -> **andriyDev** (85.7% isolated ownership) | Magnitude: 1241.26
- `crates/bevy_asset/src/server/loaders.rs` -> **andriyDev** (100.0% isolated ownership) | Magnitude: 1010.2
- `crates/bevy_ecs/src/schedule/graph/dag.rs` -> **Christian Hughes** (100.0% isolated ownership) | Magnitude: 904.64
- `crates/bevy_ui/src/focus.rs` -> **charlotte 🌸** (100.0% isolated ownership) | Magnitude: 904.18
- `crates/bevy_ecs/src/schedule/stepping.rs` -> **Tauan Binato** (100.0% isolated ownership) | Magnitude: 814.14

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `tools/ci/src/commands/format.rs` -> **Severity: 404.693** (Blast Radius: 4.336 * Doc Risk: 93.3332%)
- `crates/bevy_reflect/src/impls/alloc/vec.rs` -> **Severity: 360.461** (Blast Radius: 10.934 * Doc Risk: 32.967%)
- `crates/bevy_feathers/src/tokens.rs` -> **Severity: 322.1** (Blast Radius: 3.221 * Doc Risk: 100.0%)
- `crates/bevy_render/src/render_resource/uniform_buffer.rs` -> **Severity: 291.486** (Blast Radius: 9.467 * Doc Risk: 30.7897%)
- `crates/bevy_feathers/src/palette.rs` -> **Severity: 150.453** (Blast Radius: 1.612 * Doc Risk: 93.3333%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
