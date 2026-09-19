# ARCHITECTURAL_BRIEF: bevy
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/bevyengine/bevy.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 2155 analyzed artifact(s), 396190 LOC.
- **Load-bearing artifact:** `crates/bevy_reflect/src/impls/alloc/vec.rs` -- 32 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `examples/README.md` -- pulls in 404 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `crates/bevy_pbr/src/render/mesh.rs` at magnitude 1899.34 (structural weight, not risk).
- **How to read this brief:** section 11 ranks artifacts by structural magnitude with a blast-radius line each; section 7 has the full dependency graph. The surface vectors in section 6 describe what is present in a file, not the probability of a defect -- Appendix A has the equations and the validation record behind that distinction.

## 1.5 SYSTEM ROLE & PHILOSOPHY
> You are a Senior Technical Storyteller and Codebase Architect. GitGalaxy has translated the non-visual architecture of this repository into measurable Structural Signatures (regex-derived counts, not an AST or compiler pass). Your job is to weave those signatures into a coherent, factual narrative about how this system is built -- its architecture, design patterns, and complexity -- not to render a verdict.
> 
> **CORE DIRECTIVES:**
> 1. **Narrate the Architecture, Don't Judge the Author:** Frame every observation as a blameless description of the system's physical reality. A high Structural Surface Profile reading (formerly called Risk Exposure; e.g., Complexity Load, formerly Cognitive Load Exposure) describes where the architecture may be drifting into fragile territory, not developer incompetence -- it is a prompt to investigate, never a verdict. These are activity/content surface meters, not defect-probability estimates (gitgalaxy#2991, evidence in #2982) -- describe what is there, don't imply it predicts a bug.
> 2. **The Physical Reality Rule:** Base your narrative strictly on the provided Structural Signatures and the numbers derived from them. Do not hallucinate meaning, and do not restate a heuristic's raw label (e.g. a 'Logic Bomb' or 'O(2^N)' flag) as a confirmed finding of malice or a guaranteed defect -- explain what the signature actually measures, weave it into the story of the file, and let the reader draw their own conclusion.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`. Tell that balance as part of the narrative, not as an isolated alarm.
> 
> **THE STRUCTURAL SIGNATURE LEXICON:**
> * **Structure & Mass:** `branch` (splits), `linear` (paths), `args` (coupling), `func_start` (entry points).
> * **Risk & Volatility:** `danger` (dynamic execution), `flux` (state mutation), `graveyard` (commented-out logic), `safety_neg` (security bypasses).
> * **Architecture & Domain:** `io` (network latency), `concurrency` (async orchestration), `api` (public surface), `import` (dependencies).
> * **Defensive Guardrails:** `safety` (Error handling), `freeze_hits` (immutability), `cleanup` (state destruction).
> *(Section 2, the structural-surface lexicon and its equations, is now **Appendix A** at the end of this brief -- the findings come first.)*

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 2899 |
| Analyzed Artifacts (Scanned) | 2155 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 744 |
| Total LOC | 396190 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 74.3% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4049 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.6954 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0258 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 20 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUST | 1743 | 395355 | 80.9% |
| MARKDOWN | 185 | 0 | 8.6% |
| PLAINTEXT | 145 | 0 | 6.7% |
| XML | 52 | 1 | 2.4% |
| BINARY_THREAT | 11 | 11 | 0.5% |
| GROOVY | 6 | 140 | 0.3% |
| SHELL | 3 | 291 | 0.1% |
| GLSL | 2 | 43 | 0.1% |
| HTML | 2 | 144 | 0.1% |
| MAKEFILE | 2 | 21 | 0.1% |
| JAVA | 2 | 52 | 0.1% |
| BATCH | 2 | 132 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Flat Modular Platform`
> **Architectural Drift Z-Score:** `3.306`
> **Composition Archetype:** `Flat Modular Platform` (z +3.31; from the repo's file-archetype mix)
> **File Composition:** Generic / Templated Code Files 26%, Data / Markup / Trivial 21%, State Mutators Files 17%, Large Core Modules (3) 14%, Declarative / Non-Code 6%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 1813 | 84.1% |
| Unknown | 11 | 0.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 330 | 15.3% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 744*

**Composition by Extension & Reason:**
- `.png`: 237x Excluded (Explicitly Denied Extension: '.png')
- `.wgsl`: 155x Unsupported Format (.wgsl), 37x Excluded (Unsupported Extension: '.wgsl')
- `.toml`: 90x Unsupported Format (.toml), 8x Excluded (Unsupported Extension: '.toml'), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.stderr`: 41x Excluded (Unsupported Extension: '.stderr'), 3x Unsupported Format (.stderr)
- `.ktx2`: 20x Excluded (Unsupported Extension: '.ktx2'), 6x Excluded (Binary Format Detected)
- `.yml`: 18x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Unsupported Format (.undeterminable)
- `.md`: 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 133 LOC), 1x Excluded (Machine-Generated Source Code Signature: 4 LOC)
- `.glb`: 14x Excluded (Unsupported Extension: '.glb')
- `.gltf`: 14x Excluded (Explicitly Denied Extension: '.gltf')
- `.ron`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 6x Excluded (Unsupported Extension: '.ron')
- `.ttf`: 9x Excluded (Explicitly Denied Extension: '.ttf')
- `.jpg`: 8x Excluded (Explicitly Denied Extension: '.jpg')
- `.patch`: 7x Unsupported Format (.patch)
- `.json`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 80.7 | 8.2 | 5.5 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 35.8 | 46.2 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 27.9 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 18.9 | 2.4 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 18.6 | 9.8 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 21.9 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 18.0 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 6.2 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 5.0 | 1.1 | 0.3 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 89.7 | 12.5 | 6.7 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 53.4 | 54.5 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 18935 | 1288 | 25 | `crates/bevy_ecs/src/query/fetch.rs` |
| cleanup | 127 | 56 | 0 | `examples/math/render_primitives.rs` |
| guards | 7744 | 1100 | 10 | `crates/bevy_color/src/palettes/tailwind.rs` |
| danger | 5521 | 763 | 6 | `crates/bevy_reflect/src/lib.rs` |
| concurrency | 5651 | 719 | 7 | `crates/bevy_asset/src/processor/mod.rs` |
| connectivity | 20457 | 1582 | 26 | `crates/bevy_ui/src/ui_node.rs` |
| io | 206 | 62 | 0 | `crates/bevy_asset/src/io/file/sync_file_asset.rs` |
| crypto | 0 | 0 | 0 | - |
| ipc | 12 | 9 | 0 | `crates/bevy_pbr/src/render/mesh.rs` |
| time | 18 | 16 | 0 | `crates/bevy_asset/src/processor/mod.rs` |
| serialization | 18 | 9 | 0 | `crates/bevy_remote/src/http.rs` |
| regex | 11 | 5 | 0 | `docs-rs/trait-tags.html` |
| events | 1016 | 278 | 1 | `crates/bevy_asset/src/processor/mod.rs` |
| tests | 9774 | 385 | 7 | `crates/bevy_reflect/src/lib.rs` |
| docs | 94930 | 1461 | 117 | `crates/bevy_ecs/src/system/query.rs` |
| debt | 2764 | 495 | 3 | `crates/bevy_ecs/src/query/fetch.rs` |
| mutation | 41567 | 1516 | 52 | `crates/bevy_pbr/src/render/mesh.rs` |
| dead_code | 8526 | 1026 | 10 | `crates/bevy_ecs/src/world/mod.rs` |
| credential | 3 | 2 | 0 | `examples/3d/solari.rs` |
| threat | 965 | 302 | 1 | `crates/bevy_ptr/src/lib.rs` |
| ml_ai | 5533 | 602 | 6 | `crates/bevy_math/src/ops.rs` |
| ui | 6 | 2 | 0 | `docs-rs/trait-tags.html` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.1053**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `crates/bevy_asset/src/io/file/sync_file_asset.rs` (Hits: 26)
- `crates/bevy_asset/src/io/mod.rs` (Hits: 16)
- `examples/mobile/android_example/gradlew` (Hits: 15)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **vec.rs** (`crates/bevy_reflect/src/impls/alloc/vec.rs`) — 32 inbound connections
2. **uniform_buffer.rs** (`crates/bevy_render/src/render_resource/uniform_buffer.rs`) — 23 inbound connections
3. **format.rs** (`tools/ci/src/commands/format.rs`) — 13 inbound connections
4. **tokens.rs** (`crates/bevy_feathers/src/tokens.rs`) — 8 inbound connections
5. **main.rs** (`tools/ci/src/main.rs`) — 4 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **README.md** (`examples/README.md`) — 404 outbound dependencies
2. **mesh.rs** (`crates/bevy_pbr/src/render/mesh.rs`) — 162 outbound dependencies
3. **mod.rs** (`crates/bevy_ecs/src/world/mod.rs`) — 156 outbound dependencies
4. **mod.rs** (`crates/bevy_gltf/src/loader/mod.rs`) — 141 outbound dependencies
5. **mod.rs** (`crates/bevy_render/src/render_resource/mod.rs`) — 140 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `ktx2_dfd_header_to_texture_format` **(Many-Argument Workhorses)** (@ `crates/bevy_image/src/ktx2.rs`) -> Impact: **394.1** | LOC: 721
  * *Intent:* /// Reads the [`TextureFormat`] from a KTX2 data format descriptor header. /// /// # Errors /// /// Returns an error for invalid or unsupported textur...
- `prepare_lights` **(Many-Argument Workhorses)** (@ `crates/bevy_pbr/src/render/light.rs`) -> Impact: **345.0** | LOC: 986
- `load_gltf` **(Many-Argument Workhorses)** (@ `crates/bevy_gltf/src/loader/mod.rs`) -> Impact: **323.2** | LOC: 918
  * *Intent:* /// Loads an entire glTF file.
- `assign_objects_to_clusters` **(Many-Argument Workhorses)** (@ `crates/bevy_light/src/cluster/assign.rs`) -> Impact: **316.6** | LOC: 640
  * *Intent:* /// Clusters point lights, spot lights, light probes, and decals. /// /// NOTE: Run this before `update_point_light_frusta`!
- `load_node` **(Many-Argument Workhorses)** (@ `crates/bevy_gltf/src/loader/mod.rs`) -> Impact: **223.9** | LOC: 399
  * *Intent:* /// Loads a glTF node.
- `derive_as_bind_group` **(Many-Argument Workhorses)** (@ `crates/bevy_render/macros/src/as_bind_group.rs`) -> Impact: **206.1** | LOC: 1068
- `example_control_system` **(Many-Argument Workhorses)** (@ `examples/3d/transmission.rs`) -> Impact: **205.9** | LOC: 218
- `prepare_uinodes` **(Many-Argument Workhorses)** (@ `crates/bevy_ui_render/src/lib.rs`) -> Impact: **203.5** | LOC: 404
- `changed_windows` **(Many-Argument Workhorses)** (@ `crates/bevy_winit/src/system.rs`) -> Impact: **193.6** | LOC: 295
  * *Intent:* /// Propagates changes from [`Window`] entities to the [`winit`] backend. /// /// # Notes /// /// - [`Window::present_mode`] and [`Window::composite_a...
- `pointer_events` **(Many-Argument Workhorses)** (@ `crates/bevy_picking/src/events.rs`) -> Impact: **188.7** | LOC: 529
  * *Intent:* /// the case of [`Enter`] → [`Leave`], shared parent entities will not receive [`Enter`] /// or [`Leave`]. /// /// Both [`Click`] and [`Release`] targ...

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `examples/3d` | 66 | 7391.52 | 15.92% | 0.0% |
| `crates/bevy_pbr/src/render` | 9 | 4923.14 | 8.04% | 13.54% |
| `crates/bevy_ecs/src/query` | 11 | 3722.76 | 7.68% | 50.78% |
| `crates/bevy_reflect/src` | 24 | 3289.62 | 4.77% | 64.4% |
| `crates/bevy_ecs/src/entity` | 13 | 3080.84 | 7.5% | 84.74% |
| `crates/bevy_asset/src` | 16 | 2953.76 | 6.56% | 34.98% |
| `crates/bevy_ecs/src/system` | 15 | 2814.08 | 8.85% | 81.31% |
| `crates/bevy_pbr/src` | 13 | 2784.34 | 7.32% | 27.96% |
| `crates/bevy_ecs/src/schedule` | 10 | 2750.46 | 7.79% | 41.16% |
| `crates/bevy_ui_render/src` | 10 | 2488.08 | 12.73% | 35.29% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `crates/bevy_audio/src/sinks.rs` -> **100.0%** Exposure
- `crates/bevy_color/src/color_ops.rs` -> **100.0%** Exposure
- `crates/bevy_core_pipeline/src/deferred/mod.rs` -> **100.0%** Exposure
- `crates/bevy_core_pipeline/src/prepass/mod.rs` -> **100.0%** Exposure
- `crates/bevy_ecs/src/bundle/mod.rs` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `benches/benches/bevy_ecs/components/add_remove_big_sparse_set.rs` -> **100.0%** Exposure
- `benches/benches/bevy_ecs/components/add_remove_big_table.rs` -> **100.0%** Exposure
- `benches/benches/bevy_ecs/components/add_remove_sparse_set.rs` -> **100.0%** Exposure
- `benches/benches/bevy_ecs/components/add_remove_table.rs` -> **100.0%** Exposure
- `benches/benches/bevy_ecs/empty_archetypes.rs` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `crates/bevy_ecs/src/query/fetch.rs` -> **11** Orphaned Functions | **154** Duplicates
- `crates/bevy_ecs/src/entity/unique_slice.rs` -> **61** Orphaned Functions | **38** Duplicates
- `crates/bevy_ecs/src/system/mod.rs` -> **86** Orphaned Functions | **2** Duplicates
- `crates/bevy_ecs/src/system/system_param.rs` -> **22** Orphaned Functions | **59** Duplicates
- `crates/bevy_ecs/src/schedule/executor/mod.rs` -> **50** Orphaned Functions | **18** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `3` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `29124` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `crates/bevy_pbr/src/render/mesh.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1899.34 | **LOC:** 4764 | **CtrlFlow:** 9.3% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **162**; blast radius 0.444; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (98.6%), Mutation Surface (formerly State Flux) (97.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (89.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 52.7132% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `specialize` **(Many-Argument Workhorses)** (Impact: 178.5)
  * `collect_meshes_for_gpu_building` **(Many-Argument Workhorses)** (Impact: 91.4)
    * *Intent:* /// Creates the [`RenderMeshInstanceGpu`]s and [`MeshInputUniform`]s when GPU /// preprocessing is i...
  * `render` **(Many-Argument Workhorses)** (Impact: 56.7)
  * `check_views_need_specialization` **(Many-Argument Workhorses)** (Impact: 53.1)
  * `render` **(Many-Argument Workhorses)** (Impact: 51.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 178 instances
* *High Risk Execution (weighted view):* 3
* *State Mutation (weighted view):* 596
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 344`, `structural_boundaries: 591`, `args: 131`, `func_start: 86`, `class_start: 43`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 4`, `state_mutation: 240`, `dead_code: 4`, `planned_debt: 4`, `fragile_debt: 4`, `duplicate_logic: 4`
* *Architecture:* `api: 149`, `concurrency: 7`, `import: 50`
* *Defense:* `safety: 59`, `doc: 466`, `test: 9`, `sync_locks: 2`, `immutability_locks: 108`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` *, Affine3Ext, AssetId, AssetIndex, AssetServer, BaseMeshPipelineKey, CORE_3D_DEPTH_FORMAT, Camera...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_pbr/src/render/light.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1243.96 | **LOC:** 2675 | **CtrlFlow:** 10.6% | **Authorship Centralization:** 45.8%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **101**; blast radius 0.444; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (85.7%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (80.0%), Guard Balance (formerly Safety Score) (64.3%)
- **Documentation Coverage:** 73.1707% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `prepare_lights` **(Many-Argument Workhorses)** (Impact: 345.0)
  * `extract_lights` **(Many-Argument Workhorses)** (Impact: 145.1)
  * `queue_shadows` **(Many-Argument Workhorses)** (Impact: 111.8)
    * *Intent:* /// For each shadow cascade, iterates over all the meshes "visible" from it and /// adds them to [`B...
  * `specialize_shadows` **(Many-Argument Workhorses)** (Impact: 105.6)
  * `shadow_pass` **(Many-Argument Workhorses)** (Impact: 29.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 67 instances
* *State Mutation (weighted view):* 243
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 235`, `structural_boundaries: 406`, `args: 70`, `func_start: 28`, `class_start: 24`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 109`, `dead_code: 7`, `planned_debt: 5`, `unreferenced_by_name: 16`
* *Architecture:* `api: 96`, `import: 34`
* *Defense:* `safety: 30`, `doc: 53`, `test: 1`, `immutability_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AmbientLight, CUBE_MAP_FACES, CascadeShadowConfig, Cascades, CascadesFrusta, ClusterableObjectType, CubeMapFace, CubemapFrusta...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_gltf/src/loader/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1006.22 | **LOC:** 2759 | **CtrlFlow:** 9.7% | **Authorship Centralization:** 34.8%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **141**; blast radius 0.444; role: Isolated/Orphan
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (79.0%), Mutation Surface (formerly State Flux) (58.1%), Guard Balance (formerly Safety Score) (52.5%)
- **Documentation Coverage:** 76.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `load_gltf` **(Many-Argument Workhorses)** (Impact: 323.2)
    * *Intent:* /// Loads an entire glTF file.
  * `load_node` **(Many-Argument Workhorses)** (Impact: 223.9)
    * *Intent:* /// Loads a glTF node.
  * `load_image` **(Many-Argument Workhorses)** (Impact: 31.6)
    * *Intent:* /// Loads a glTF texture as a bevy [`Image`] and returns it together with its label.
  * `load_material` **(Many-Argument Workhorses)** (Impact: 25.9)
    * *Intent:* /// Loads a glTF material as a bevy [`GltfMaterial`] and returns the label and material.
  * `load_buffers` **(Compute Cores)** (Impact: 19.4)
    * *Intent:* /// Loads the raw glTF buffer data for a specific glTF file.
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 49 instances
* *Concurrency (weighted view):* 31
* *State Mutation (weighted view):* 162
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 228`, `structural_boundaries: 508`, `args: 103`, `func_start: 29`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 30`, `high_risk_execution: 4`, `state_mutation: 64`, `dead_code: 13`, `planned_debt: 9`, `unreferenced_by_name: 10`
* *Architecture:* `io: 2`, `api: 36`, `concurrency: 21`, `import: 42`
* *Defense:* `safety: 86`, `doc: 94`, `test: 54`, `sync_locks: 5`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AnimatedBy, AnimationTargetId, AssetApp, AssetLoadError, AssetLoader, AssetPath, AssetPlugin, AssetServer...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_asset/src/processor/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 975.72 | **LOC:** 1865 | **CtrlFlow:** 13.5% | **Authorship Centralization:** 87.5%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **60**; blast radius 0.444; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (61.3%), Guard Balance (formerly Safety Score) (58.6%)
- **Documentation Coverage:** 20.5128% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `process_asset_internal` **(Many-Argument Workhorses)** (Impact: 72.7)
  * `initialize` **(Compute Cores)** (Impact: 50.5)
    * *Intent:* /// Populates the initial view of each asset by scanning the unprocessed and processed asset folders...
  * `handle_asset_source_event` **(Many-Argument Workhorses)** (Impact: 41.0)
  * `validate_transaction_log_and_recover` **(Defensive Guards)** (Impact: 40.0)
  * `rename` **(Many-Argument Workhorses)** (Impact: 25.7)
    * *Intent:* /// Remove the info for the old path, and move over its info to the new path. This should only /// h...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 19 instances
* *Amplified Cascading Flux:* 29 instances
* *High Risk Execution (weighted view):* 1
* *Concurrency (weighted view):* 268
* *State Mutation (weighted view):* 102
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 193`, `structural_boundaries: 458`, `args: 67`, `func_start: 55`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 32`, `high_risk_execution: 2`, `state_mutation: 44`, `dead_code: 7`, `planned_debt: 4`, `unreferenced_by_name: 5`
* *Architecture:* `api: 39`, `concurrency: 173`, `import: 16`
* *Defense:* `safety: 42`, `doc: 184`, `test: 1`, `sync_locks: 23`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` AssetAction, AssetActionMinimal, AssetHash, AssetLoadError, AssetMeta, AssetMetaCheck, AssetMetaDyn, AssetMetaMinimal...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_ecs/src/query/fetch.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 942.9 | **LOC:** 4326 | **CtrlFlow:** 8.3% | **Authorship Centralization:** 42.9%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **70**; blast radius 0.444; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (50.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (39.6%)
- **Documentation Coverage:** 93.2692% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fetch` **(Generic / Templated Code)** (Impact: 12.5)
  * `derive_release_state` **(Generic / Templated Code)** (Impact: 12.2)
  * `test_contiguous_query_data` **(Annotated & Test Methods)** (Impact: 10.1)
  * `any_of_contiguous_test` **(Annotated & Test Methods)** (Impact: 7.9)
  * `init_fetch` **(Generic / Templated Code)** (Impact: 7.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 22 instances
* *High Risk Execution (weighted view):* 4
* *State Mutation (weighted view):* 89
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 233`, `structural_boundaries: 696`, `args: 335`, `func_start: 304`, `class_start: 44`
* *Risk/State:* `safety_bypasses: 21`, `high_risk_execution: 5`, `state_mutation: 45`, `dead_code: 50`, `planned_debt: 7`, `duplicate_logic: 154`, `unreferenced_by_name: 11`
* *Architecture:* `api: 53`, `concurrency: 12`, `import: 17`
* *Defense:* `safety: 7`, `doc: 620`, `test: 40`, `immutability_locks: 67`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Access, Archetypes, ComponentId, ComponentTicksRef, Components, ContiguousComponentTicksMut, ContiguousComponentTicksRef, ContiguousMut...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_mesh/src/mesh.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 939.42 | **LOC:** 3198 | **CtrlFlow:** 9.6% | **Authorship Centralization:** 11.1%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **55**; blast radius 0.444; role: Isolated/Orphan
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (54.4%), Guard Balance (formerly Safety Score) (54.1%)
- **Documentation Coverage:** 17.77% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `triangles` **(Compute Cores)** (Impact: 28.2)
    * *Intent:* /// Get a list of this Mesh's [triangles] as an iterator if possible. /// /// Returns an error if an...
  * `merge_duplicate_vertices` **(Generic / Templated Code)** (Impact: 25.9)
    * *Intent:* /// Remove duplicate vertices and create the index pointing to the unique vertices. /// /// Returns ...
  * `merge` **(Many-Argument Workhorses)** (Impact: 24.4)
    * *Intent:* /// /// Note that attributes of `other` that don't exist on `self` will be ignored. /// /// `Aabb` o...
  * `try_transform_by` **(Defensive Guards)** (Impact: 19.9)
    * *Intent:* /// Transforms the vertex positions, normals, and tangents of the mesh in place by the given [`Trans...
  * `try_scale_by` **(Defensive Guards)** (Impact: 17.9)
    * *Intent:* /// Scales the vertex positions, normals, and tangents of the mesh in place by the given [`Vec3`]. /...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 25 instances
* *High Risk Execution (weighted view):* 3
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 121
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 181`, `structural_boundaries: 378`, `args: 193`, `func_start: 151`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 70`, `high_risk_execution: 6`, `state_mutation: 71`, `dead_code: 14`, `planned_debt: 1`, `fragile_debt: 4`
* *Architecture:* `api: 158`, `import: 29`
* *Defense:* `safety: 27`, `doc: 950`, `test: 59`, `immutability_locks: 17`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` *, FourIterators, HashMap, Hasher, Indices, MeshAttributeData, MeshBuilder, MeshTrianglesError...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_ecs/src/world/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 924.48 | **LOC:** 4643 | **CtrlFlow:** 5.3% | **Authorship Centralization:** 13.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **156**; blast radius 0.444; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (87.1%), Dead Code Surface (formerly Dead Code) (86.4%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (68.9%)
- **Documentation Coverage:** 14.0401% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `try_insert_batch_with_caller` **(Many-Argument Workhorses)** (Impact: 37.0)
    * *Intent:* /// Split into a new function so we can differentiate the calling location. /// /// This can be call...
  * `try_resource_scope` **(Generic / Templated Code)** (Impact: 26.5)
    * *Intent:* /// Temporarily removes the requested resource from this [`World`] if it exists, runs custom user co...
  * `insert_batch_with_caller` **(Many-Argument Workhorses)** (Impact: 22.4)
    * *Intent:* /// Split into a new function so we can differentiate the calling location. /// /// This can be call...
  * `drop` **(Compute Cores)** (Impact: 10.4)
  * `remove_resource_by_id` **(Defensive Guards)** (Impact: 9.2)
    * *Intent:* /// Removes the resource of a given type, if it exists. /// Returns `true` if the resource is succes...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 8 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 12 instances
* *High Risk Execution (weighted view):* 8
* *Concurrency (weighted view):* 29
* *State Mutation (weighted view):* 55
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 116`, `structural_boundaries: 567`, `args: 246`, `func_start: 191`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 38`, `high_risk_execution: 16`, `state_mutation: 31`, `dead_code: 230`, `planned_debt: 3`, `unreferenced_by_name: 63`
* *Architecture:* `api: 187`, `concurrency: 24`, `import: 32`
* *Defense:* `safety: 21`, `doc: 1921`, `test: 117`, `sync_locks: 10`, `immutability_locks: 1`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ADD, Archetypes, AtomicU32, BundleId, BundleInfo, BundleInserter, BundleSpawner, Bundles...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_pbr/src/prepass/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 888.96 | **LOC:** 1504 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **119**; blast radius 0.444; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (66.0%)
- **Documentation Coverage:** 83.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `specialize_prepass_material_meshes` **(Many-Argument Workhorses)** (Impact: 164.3)
  * `queue_prepass_material_meshes` **(Many-Argument Workhorses)** (Impact: 149.3)
  * `specialize` **(Many-Argument Workhorses)** (Impact: 145.3)
  * `check_prepass_views_need_specialization` **(Many-Argument Workhorses)** (Impact: 17.9)
  * `prepare_previous_view_uniforms` **(Many-Argument Workhorses)** (Impact: 11.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 75 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 239
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 185`, `structural_boundaries: 217`, `args: 29`, `func_start: 19`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 2`, `state_mutation: 89`, `dead_code: 1`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 46`, `import: 23`
* *Defense:* `safety: 19`, `doc: 19`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` *, AlphaMode, AssetServer, Camera3d, DeferredAlphaMaskDrawFunction, DeferredFragmentShader, DeferredOpaqueDrawFunction, DeferredVertexShader...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_render/src/batching/gpu_preprocessing.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 877.0 | **LOC:** 2732 | **CtrlFlow:** 8.0% | **Authorship Centralization:** 38.9%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **88**; blast radius 0.444; role: Isolated/Orphan
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (73.2%), Mutation Surface (formerly State Flux) (70.9%), Concurrency Surface (formerly Concurrency) (65.4%)
- **Documentation Coverage:** 14.2857% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `batch_and_prepare_binned_render_phase` **(Many-Argument Workhorses)** (Impact: 80.0)
    * *Intent:* /// Creates batches for a render phase that uses bins.
  * `batch_and_prepare_sorted_render_phase` **(Many-Argument Workhorses)** (Impact: 64.1)
    * *Intent:* /// Batch the items in a sorted render phase, when GPU instance buffer building /// is in use. This ...
  * `write_binned_instance_buffers` **(Many-Argument Workhorses)** (Impact: 60.6)
    * *Intent:* /// Writes the bin data for each render phase to the GPU. /// /// The bin data consists of the IDs o...
  * `write_batched_instance_buffers` **(Many-Argument Workhorses)** (Impact: 25.9)
    * *Intent:* /// A system that writes all instance buffers to the GPU.
  * `from_world` **(Compute Cores)** (Impact: 21.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 33 instances
* *Concurrency (weighted view):* 62
* *State Mutation (weighted view):* 149
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 145`, `structural_boundaries: 408`, `args: 86`, `func_start: 76`, `class_start: 33`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 83`, `dead_code: 6`, `planned_debt: 1`, `duplicate_logic: 5`, `unreferenced_by_name: 21`
* *Architecture:* `api: 130`, `concurrency: 42`, `import: 20`
* *Defense:* `safety: 24`, `doc: 537`, `test: 8`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AtomicRawBufferVec, AtomicSparseBufferVec, BinnedRenderPhaseBatch, BinnedRenderPhaseBatchSet, BinnedRenderPhaseBatchSets, Buffer, BufferUsages, CachedRenderPipelinePhaseItem...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_ui_render/src/lib.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 874.92 | **LOC:** 1845 | **CtrlFlow:** 10.1% | **Authorship Centralization:** 31.6%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **105**; blast radius 0.444; role: Isolated/Orphan
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (78.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (74.4%), Concurrency Surface (formerly Concurrency) (73.0%)
- **Documentation Coverage:** 75.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `prepare_uinodes` **(Many-Argument Workhorses)** (Impact: 203.5)
  * `extract_text_shadows` **(Many-Argument Workhorses)** (Impact: 49.2)
  * `extract_uinode_borders` **(Many-Argument Workhorses)** (Impact: 44.7)
  * `extract_text_decorations` **(Many-Argument Workhorses)** (Impact: 41.2)
  * `extract_uinode_images` **(Many-Argument Workhorses)** (Impact: 38.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 9 instances
* *Amplified Cascading Flux:* 39 instances
* *Concurrency (weighted view):* 59
* *State Mutation (weighted view):* 158
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 157`, `structural_boundaries: 236`, `args: 68`, `func_start: 17`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 80`, `dead_code: 12`, `planned_debt: 2`
* *Architecture:* `api: 96`, `concurrency: 14`, `import: 36`
* *Defense:* `safety: 15`, `doc: 108`, `immutability_locks: 30`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AddRenderCommand, AssetId, Assets, BorderColor, BoxShadowSamples, CalculatedClip, Camera2d, Camera3d...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_ecs/src/schedule/schedule.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 842.68 | **LOC:** 2665 | **CtrlFlow:** 7.3% | **Authorship Centralization:** 25.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **61**; blast radius 0.444; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (94.3%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (55.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (54.6%)
- **Documentation Coverage:** 45.9574% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `build_schedule` **(Many-Argument Workhorses)** (Impact: 39.3)
    * *Intent:* /// Builds an execution-optimized [`SystemSchedule`] from the current state /// of the graph. Also r...
  * `process_configs` **(Many-Argument Workhorses)** (Impact: 38.3)
    * *Intent:* /// Adds the config nodes to the graph. /// /// `collect_nodes` controls whether the `NodeId`s of th...
  * `update_schedule` **(Many-Argument Workhorses)** (Impact: 32.5)
    * *Intent:* /// Updates the `SystemSchedule` from the `ScheduleGraph`.
  * `get_node_name_inner` **(Compute Cores)** (Impact: 25.6)
  * `build_schedule_inner` **(Many-Argument Workhorses)** (Impact: 20.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 32 instances
* *High Risk Execution (weighted view):* 3
* *State Mutation (weighted view):* 129
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 143`, `structural_boundaries: 547`, `args: 259`, `func_start: 140`, `class_start: 31`
* *Risk/State:* `safety_bypasses: 24`, `high_risk_execution: 5`, `state_mutation: 65`, `dead_code: 22`, `duplicate_logic: 14`
* *Architecture:* `api: 113`, `import: 22`
* *Defense:* `safety: 12`, `doc: 322`, `test: 119`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Components, Direction::Incoming, FallbackErrorHandler, HashSet, IndexSet, IntoScheduleConfigs, IntoSystemSet, Outgoing...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_pbr/src/render/gpu_preprocess.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 827.4 | **LOC:** 2947 | **CtrlFlow:** 8.0% | **Authorship Centralization:** 41.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **120**; blast radius 0.444; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (63.7%), Guard Balance (formerly Safety Score) (48.8%), Mutation Surface (formerly State Flux) (19.6%)
- **Documentation Coverage:** 49.1228% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `early_gpu_preprocess` **(Many-Argument Workhorses)** (Impact: 96.7)
  * `prepare_preprocess_bind_groups` **(Many-Argument Workhorses)** (Impact: 66.2)
    * *Intent:* /// A system that attaches buffers to bind groups for the variants of the /// compute shaders relati...
  * `create_bin_unpacking_bind_groups` **(Many-Argument Workhorses)** (Impact: 43.9)
    * *Intent:* /// Creates all bind groups needed to run the `unpack_bins` shader for all the /// phases for a sing...
  * `run_build_indirect_parameters` **(Many-Argument Workhorses)** (Impact: 43.3)
  * `unpack_bins` **(Many-Argument Workhorses)** (Impact: 34.8)
    * *Intent:* /// A rendering system that invokes a compute shader for each batch set in order /// to generate pre...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 63
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 188`, `structural_boundaries: 319`, `args: 32`, `func_start: 46`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 25`, `dead_code: 3`, `duplicate_logic: 3`, `unreferenced_by_name: 3`
* *Architecture:* `api: 61`, `import: 17`
* *Defense:* `safety: 16`, `doc: 263`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` BatchedInstanceBuffers, BinUnpackingBuffers, BinUnpackingBuffersKey, BinUnpackingJob, BinUnpackingMetadataIndex, BindGroup, BindGroupEntries, BindGroupLayoutDescriptor...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_pbr/src/wireframe.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 820.24 | **LOC:** 1647 | **CtrlFlow:** 11.9% | **Authorship Centralization:** 26.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **119**; blast radius 0.444; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (80.3%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (68.9%), Connectivity (formerly Api Exposure) (68.1%)
- **Documentation Coverage:** 78.9474% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `specialize_wireframes` **(Many-Argument Workhorses)** (Impact: 140.8)
  * `queue_wireframes` **(Many-Argument Workhorses)** (Impact: 92.7)
  * `prepare_wireframe_wide_bind_groups` **(Many-Argument Workhorses)** (Impact: 71.9)
  * `render` **(Many-Argument Workhorses)** (Impact: 36.9)
  * `render` **(Many-Argument Workhorses)** (Impact: 18.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 39 instances
* *State Mutation (weighted view):* 129
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 162`, `structural_boundaries: 278`, `args: 59`, `func_start: 41`, `class_start: 29`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 51`, `dead_code: 2`
* *Architecture:* `api: 83`, `import: 16`
* *Defense:* `safety: 22`, `doc: 81`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` *, AsAssetId, Asset, AssetApp, AssetEventSystems, AssetId, AssetServer, Assets...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_asset/src/server/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 813.3 | **LOC:** 2255 | **CtrlFlow:** 8.5% | **Authorship Centralization:** 75.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **82**; blast radius 0.444; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (94.9%), Concurrency Surface (formerly Concurrency) (92.7%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (56.8%)
- **Documentation Coverage:** 19.186% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `load_internal` **(Many-Argument Workhorses)** (Impact: 66.6)
    * *Intent:* /// Performs an async asset load. /// /// `input_handle` must only be [`Some`] if `should_load` was ...
  * `get_meta_loader_and_reader` **(Many-Argument Workhorses)** (Impact: 45.5)
  * `handle_internal_asset_events` **(Defensive Guards)** (Impact: 34.4)
    * *Intent:* /// A system that manages internal [`AssetServer`] events, such as finalizing asset loads.
  * `load_folder_internal` **(Many-Argument Workhorses)** (Impact: 32.2)
  * `load_folder` **(Many-Argument Workhorses)** (Impact: 26.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 11 instances
* *Concurrency (weighted view):* 101
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 54
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 138`, `structural_boundaries: 365`, `args: 131`, `func_start: 92`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 32`, `dead_code: 12`, `planned_debt: 6`, `duplicate_logic: 9`, `unreferenced_by_name: 33`
* *Architecture:* `io: 1`, `api: 101`, `concurrency: 86`, `import: 18`
* *Defense:* `safety: 32`, `doc: 349`, `sync_locks: 5`, `immutability_locks: 2`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Asset, AssetActionMinimal, AssetEvent, AssetHandleProvider, AssetId, AssetIndex, AssetLoadFailedEvent, AssetMetaCheck...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_image/src/ktx2.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 804.12 | **LOC:** 1542 | **CtrlFlow:** 21.9% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **29**; blast radius 0.444; role: Isolated/Orphan
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (54.5%), Mutation Surface (formerly State Flux) (41.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (17.9%)
- **Documentation Coverage:** 16.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ktx2_dfd_header_to_texture_format` **(Many-Argument Workhorses)** (Impact: 394.1)
    * *Intent:* /// Reads the [`TextureFormat`] from a KTX2 data format descriptor header. /// /// # Errors /// /// ...
  * `ktx2_buffer_to_image` **(Many-Argument Workhorses)** (Impact: 113.8)
    * *Intent:* /// Converts KTX2 bytes to a bevy [`Image`] using the given compressed format support. /// /// # Err...
  * `ktx2_format_to_texture_format` **(Many-Argument Workhorses)** (Impact: 101.4)
    * *Intent:* /// Converts a KTX2 texture format identifier to a [`TextureFormat`]. /// /// # Errors /// /// Retur...
  * `get_transcoded_formats` **(Many-Argument Workhorses)** (Impact: 52.0)
    * *Intent:* /// Determines an appropriate wgpu-compatible format based on compressed format support, and a /// b...
  * `sample_information_to_data_type` **(Compute Cores)** (Impact: 22.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 74
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 314`, `structural_boundaries: 157`, `args: 30`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 32`, `planned_debt: 3`, `fragile_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 2`, `api: 5`, `import: 10`
* *Defense:* `safety: 3`, `doc: 23`, `test: 23`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AstcChannel, ColorModel, DfdBlockBasic, DfdBlockHeaderBasic, DfdHeader, Extent3d, Header, Image...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_remote/src/builtin_methods.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 800.3 | **LOC:** 2235 | **CtrlFlow:** 14.4% | **Authorship Centralization:** 18.2%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **64**; blast radius 0.444; role: Isolated/Orphan
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (61.7%), Guard Balance (formerly Safety Score) (49.5%), Debt Markers (formerly Tech Debt) (34.9%)
- **Documentation Coverage:** 20.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `process_remote_get_components_watching_request` **(Many-Argument Workhorses)** (Impact: 56.9)
    * *Intent:* /// Handles a `world.get_components+watch` request coming from a client.
  * `process_remote_query_request` **(Many-Argument Workhorses)** (Impact: 46.2)
    * *Intent:* /// Handles a `world.query` request coming from a client.
  * `process_remote_list_components_watching_request` **(Many-Argument Workhorses)** (Impact: 38.2)
    * *Intent:* /// Handles a `world.list_components+watch` request coming from a client.
  * `process_remote_mutate_components_request` **(Defensive Guards)** (Impact: 27.2)
    * *Intent:* /// Handles a `world.mutate_components` request coming from a client. /// /// This method allows you...
  * `serialize_components` **(Defensive Guards)** (Impact: 25.7)
    * *Intent:* /// Serializes the specified components for an entity. /// The iterator yields ([`TypeId`], Option<[...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 70
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 222`, `structural_boundaries: 411`, `args: 101`, `func_start: 56`, `class_start: 45`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 28`, `dead_code: 3`, `duplicate_logic: 2`, `unreferenced_by_name: 24`
* *Architecture:* `api: 125`, `import: 15`
* *Defense:* `safety: 29`, `doc: 329`, `test: 23`, `immutability_locks: 22`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` BrpError, BrpResult, Deserialize, EntityWorldMut, FilteredEntityRef, GetPath, JsonSchemaBevyType, Local...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_render/src/render_phase/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 788.24 | **LOC:** 2669 | **CtrlFlow:** 8.0% | **Authorship Centralization:** 62.5%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **76**; blast radius 0.444; role: Isolated/Orphan
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (59.8%), Guard Balance (formerly Safety Score) (58.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (54.6%)
- **Documentation Coverage:** 31.9672% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `render_multidrawable_batch_set` **(I/O & Config Routines)** (Impact: 51.2)
    * *Intent:* /// A `proptest`-based randomized test for `RenderMultidrawableBatchSet`. /// /// `proptest` works b...
  * `render_batchable_meshes` **(Many-Argument Workhorses)** (Impact: 48.5)
    * *Intent:* /// Renders all batchable meshes queued in this phase.
  * `remove_entity_from_bin` **(Many-Argument Workhorses)** (Impact: 30.0)
    * *Intent:* /// Removes an entity from a bin. /// /// If this makes the bin empty, this function removes the bin...
  * `add` **(Many-Argument Workhorses)** (Impact: 25.8)
    * *Intent:* /// Bins a new entity. /// /// The `phase_type` parameter specifies whether the entity is a /// prep...
  * `render_unbatchable_meshes` **(Many-Argument Workhorses)** (Impact: 23.2)
    * *Intent:* /// Renders all unbatchable meshes queued in this phase.
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 25 instances
* *Concurrency (weighted view):* 15
* *State Mutation (weighted view):* 121
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 137`, `structural_boundaries: 347`, `args: 102`, `func_start: 92`, `class_start: 37`
* *Risk/State:* `safety_bypasses: 16`, `high_risk_execution: 13`, `state_mutation: 71`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 2`, `duplicate_logic: 6`, `unreferenced_by_name: 8`
* *Architecture:* `api: 105`, `concurrency: 10`, `import: 38`
* *Defense:* `safety: 16`, `doc: 602`, `test: 17`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` BatchedInstanceBuffer, BatchedInstanceBuffers, DerefMut, EntityIndex, Features, GetFullBatchData, GpuPreprocessingSupport, GpuResourceAppExt...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_ui/src/ui_node.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 725.32 | **LOC:** 3236 | **CtrlFlow:** 4.0% | **Authorship Centralization:** 70.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **45**; blast radius 0.444; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (91.2%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (59.6%), Guard Balance (formerly Safety Score) (39.7%)
- **Documentation Coverage:** 24.0876% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `invalid_grid_placement_values` **(Annotated & Test Methods)** (Impact: 13.8)
  * `contains_point` **(Compute Cores)** (Impact: 13.1)
    * *Intent:* // Returns true if `point` within the node. // // Matches the sdf function in `ui.wgsl` that is used...
  * `resolve_clip_rect` **(Many-Argument Workhorses)** (Impact: 9.3)
    * *Intent:* /// Resolve the node's clipping rect in local space
  * `resolve_single_corner` **(Defensive Guards)** (Impact: 7.3)
    * *Intent:* /// Resolve the border radius for a single corner from the given context values. /// Returns the rad...
  * `get` **(State Mutators)** (Impact: 6.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 46
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 229`, `args: 188`, `func_start: 168`, `class_start: 46`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 34`, `dead_code: 12`, `duplicate_logic: 24`, `unreferenced_by_name: 36`
* *Architecture:* `api: 285`, `import: 19`
* *Defense:* `safety: 3`, `doc: 949`, `test: 47`, `immutability_locks: 27`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` BLUE, Camera, Camera2d, Color, ContentSize, DerefMut, FocusPolicy, Rect...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_input/src/gamepad.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 719.08 | **LOC:** 2979 | **CtrlFlow:** 5.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **66**; blast radius 0.444; role: Isolated/Orphan
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (70.2%), Guard Balance (formerly Safety Score) (41.0%), Mutation Surface (formerly State Flux) (13.6%)
- **Documentation Coverage:** 30.9859% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `gamepad_event_processing_system` **(Many-Argument Workhorses)** (Impact: 55.2)
    * *Intent:* /// Consumes [`RawGamepadEvent`] events, filters them using their [`GamepadSettings`] and if success...
  * `new` **(Many-Argument Workhorses)** (Impact: 39.2)
    * *Intent:* /// + `livezone_upperbound` - the value above which inputs will be rounded up to 1.0. /// + `thresho...
  * `get_axis_position_from_value` **(Compute Cores)** (Impact: 22.0)
  * `gamepad_connection_system` **(Compute Cores)** (Impact: 15.9)
    * *Intent:* /// Handles [`GamepadConnectionEvent`]s events. /// /// On connection, adds the components represent...
  * `clamp` **(Compute Cores)** (Impact: 14.4)
    * *Intent:* /// Clamps the `raw_value` according to the `AxisSettings`.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 31
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 128`, `structural_boundaries: 251`, `args: 108`, `func_start: 115`, `class_start: 26`
* *Risk/State:* `safety_bypasses: 12`, `high_risk_execution: 3`, `state_mutation: 13`, `dead_code: 10`, `duplicate_logic: 2`
* *Architecture:* `api: 156`, `import: 20`
* *Defense:* `safety: 14`, `doc: 538`, `test: 88`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AxisSettings, AxisSettingsError, ButtonAxisSettings, ButtonInput, ButtonSettings, ButtonSettingsError, ButtonState, Disconnected...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_reflect/src/lib.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 709.74 | **LOC:** 4268 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 28.6%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **109**; blast radius 0.444; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (71.3%), Guard Balance (formerly Safety Score) (58.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (40.8%), Mutation Surface (formerly State Flux) (33.2%)
- **Documentation Coverage:** 95.935% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `reflect_type_info` **(Annotated & Test Methods)** (Impact: 15.4)
  * `reflect_complex_patch` **(I/O & Config Routines)** (Impact: 8.7)
  * `should_contain_docs` **(Annotated & Test Methods)** (Impact: 8.0)
  * `should_reflect_debug` **(Annotated & Test Methods)** (Impact: 6.9)
  * `custom_cmp` **(Generic / Templated Code)** (Impact: 5.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 125
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 907`, `args: 132`, `func_start: 129`, `class_start: 185`
* *Risk/State:* `safety_bypasses: 159`, `high_risk_execution: 3`, `state_mutation: 115`, `dead_code: 2`, `planned_debt: 11`
* *Architecture:* `api: 186`, `import: 76`
* *Defense:* `safety: 12`, `doc: 635`, `test: 374`, `sync_locks: 6`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` *, ::alloc::
            borrow::Cow, ::glam::quat, ::serde::de::DeserializeSeed, Deserialize, Deserializer, Formatter, FromReflect...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_ecs/src/query/access.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 691.66 | **LOC:** 2033 | **CtrlFlow:** 5.2% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **33**; blast radius 0.444; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (79.1%), Mutation Surface (formerly State Flux) (56.2%), Guard Balance (formerly Safety Score) (42.8%)
- **Documentation Coverage:** 25.9615% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `is_compatible` **(Compute Cores)** (Impact: 12.6)
    * *Intent:* /// Returns `true` if the access and `other` can be active at the same time. /// /// [`Access`] inst...
  * `is_subset` **(Compute Cores)** (Impact: 12.6)
    * *Intent:* /// Returns `true` if the set is a subset of another, i.e. `other` contains /// at least all the val...
  * `extend` **(Compute Cores)** (Impact: 9.9)
    * *Intent:* /// Adds all access and filters from `other`. /// /// Corresponds to a conjunction operation (AND) f...
  * `is_compatible` **(Compute Cores)** (Impact: 9.3)
    * *Intent:* /// Returns `true` if this and `other` can be active at the same time. /// /// Access conflict resol...
  * `get_conflicts` **(Compute Cores)** (Impact: 7.5)
    * *Intent:* /// Returns a vector of elements that this set and `other` cannot access at the same time.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 91
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 349`, `args: 181`, `func_start: 171`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 65`, `dead_code: 6`, `planned_debt: 2`
* *Architecture:* `api: 159`, `import: 26`
* *Defense:* `doc: 315`, `test: 98`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Access, AccessConflicts, ComponentAccessKind, ComponentIdSet, FilteredAccess, FilteredAccessSet, FixedBitSet, Intersection...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_ecs/src/entity/clone_entities.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 667.14 | **LOC:** 2608 | **CtrlFlow:** 5.2% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **62**; blast radius 0.444; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (79.9%), Concurrency Surface (formerly Concurrency) (57.9%), Guard Balance (formerly Safety Score) (53.3%), Mutation Surface (formerly State Flux) (36.9%)
- **Documentation Coverage:** 35.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `clone_entity_internal` **(Many-Argument Workhorses)** (Impact: 60.1)
    * *Intent:* /// Clones and inserts components from the `source` entity into the entity mapped by `mapper` from `...
  * `clone_components` **(Many-Argument Workhorses)** (Impact: 37.0)
  * `filter_allow` **(Many-Argument Workhorses)** (Impact: 21.8)
    * *Intent:* /// Allows a component through the filter, also allow required components if /// [`Self::attach_requ...
  * `clone_entity_mapped_internal` **(Many-Argument Workhorses)** (Impact: 19.3)
  * `clone_components` **(Generic / Templated Code)** (Impact: 16.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 18 instances
* *Concurrency (weighted view):* 54
* *State Mutation (weighted view):* 86
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 95`, `structural_boundaries: 632`, `args: 135`, `func_start: 103`, `class_start: 79`
* *Risk/State:* `safety_bypasses: 42`, `high_risk_execution: 6`, `state_mutation: 50`, `dead_code: 10`, `planned_debt: 3`, `duplicate_logic: 2`, `unreferenced_by_name: 41`
* *Architecture:* `api: 58`, `concurrency: 44`, `import: 21`
* *Defense:* `safety: 10`, `doc: 325`, `test: 134`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` BundleRemover, Children, ComponentCloneBehavior, ComponentCloneFn, ComponentId, ComponentInfo, Entity, EntityAllocator...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_ecs/src/system/system_param.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 664.58 | **LOC:** 3013 | **CtrlFlow:** 6.4% | **Authorship Centralization:** 26.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **68**; blast radius 0.444; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (68.9%), Guard Balance (formerly Safety Score) (44.3%)
- **Documentation Coverage:** 79.1667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `init_access` **(Generic / Templated Code)** (Impact: 9.9)
  * `get_param` **(Generic / Templated Code)** (Impact: 9.8)
  * `init_access` **(Generic / Templated Code)** (Impact: 7.9)
  * `init_access` **(Generic / Templated Code)** (Impact: 7.9)
  * `get_param` **(Generic / Templated Code)** (Impact: 7.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 8 instances
* *High Risk Execution (weighted view):* 7
* *State Mutation (weighted view):* 39
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 109`, `structural_boundaries: 580`, `args: 207`, `func_start: 196`, `class_start: 38`
* *Risk/State:* `safety_bypasses: 13`, `high_risk_execution: 9`, `state_mutation: 23`, `dead_code: 66`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 59`, `unreferenced_by_name: 22`
* *Architecture:* `api: 63`, `concurrency: 18`, `import: 19`
* *Defense:* `safety: 6`, `doc: 826`, `test: 23`, `immutability_locks: 4`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ComponentTicksRef, Components, DeferredWorld, DerefMut, Display, EntityAllocator, FilteredAccess, FilteredAccessSet...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_asset/src/lib.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 652.12 | **LOC:** 3087 | **CtrlFlow:** 5.2% | **Authorship Centralization:** 52.9%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **110**; blast radius 0.444; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (71.8%), Connectivity (formerly Api Exposure) (63.0%), Guard Balance (formerly Safety Score) (53.0%), Concurrency Surface (formerly Concurrency) (30.3%)
- **Documentation Coverage:** 85.9259% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `load_dependencies` **(I/O & Config Routines)** (Impact: 26.5)
  * `load_error_events` **(I/O & Config Routines)** (Impact: 19.8)
    * *Intent:* /// Tests that `AssetLoadFailedEvent<A>` events are emitted and can be used to retry failed assets.
  * `asset_load_error_event_handler` **(Many-Argument Workhorses)** (Impact: 18.6)
  * `load` **(Many-Argument Workhorses)** (Impact: 13.0)
  * `load_folder` **(I/O & Config Routines)** (Impact: 12.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 11 instances
* *Concurrency (weighted view):* 39
* *State Mutation (weighted view):* 46
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 122`, `structural_boundaries: 671`, `args: 138`, `func_start: 99`, `class_start: 40`
* *Risk/State:* `safety_bypasses: 65`, `high_risk_execution: 9`, `state_mutation: 24`, `planned_debt: 3`, `duplicate_logic: 5`
* *Architecture:* `io: 9`, `api: 97`, `concurrency: 29`, `import: 40`
* *Defense:* `safety: 11`, `doc: 264`, `test: 191`, `sync_locks: 3`, `immutability_locks: 9`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Asset, AssetApp, AssetEvent, AssetId, AssetLoadError, AssetLoadFailedEvent, AssetMode, AssetPath...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_pbr/src/material_bind_groups.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 623.22 | **LOC:** 2086 | **CtrlFlow:** 8.3% | **Authorship Centralization:** 25.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **58**; blast radius 0.444; role: Isolated/Orphan
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (79.0%), Guard Balance (formerly Safety Score) (62.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (40.0%)
- **Documentation Coverage:** 11.5385% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `prepare_bind_group` **(Many-Argument Workhorses)** (Impact: 27.1)
    * *Intent:* /// Recreates the bind group if this slab has been changed since the last /// time we created it.
  * `insert_resources` **(Many-Argument Workhorses)** (Impact: 26.5)
    * *Intent:* /// Inserts the given [`BindingResources`] into this slab. /// /// Returns a table that maps the bin...
  * `create_sampler_binding_resource_arrays` **(Many-Argument Workhorses)** (Impact: 22.9)
    * *Intent:* /// Accumulates sampler binding arrays into binding resource arrays suitable /// for passing to `wgp...
  * `create_texture_binding_resource_arrays` **(Many-Argument Workhorses)** (Impact: 22.9)
    * *Intent:* /// Accumulates texture binding arrays into binding resource arrays suitable /// for passing to `wgp...
  * `prepare_bind_groups` **(Many-Argument Workhorses)** (Impact: 21.4)
    * *Intent:* /// Prepares any as-yet unprepared bind groups that this allocator is /// managing. /// /// Unprepar...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 31 instances
* *High Risk Execution (weighted view):* 4
* *State Mutation (weighted view):* 138
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 122`, `structural_boundaries: 243`, `args: 81`, `func_start: 65`, `class_start: 23`
* *Risk/State:* `safety_bypasses: 27`, `high_risk_execution: 5`, `state_mutation: 76`, `dead_code: 7`, `planned_debt: 1`, `unreferenced_by_name: 5`
* *Architecture:* `api: 27`, `import: 13`
* *Defense:* `safety: 22`, `doc: 370`, `test: 7`, `immutability_locks: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` BindGroupEntry, BindGroupLayoutDescriptor, BindingNumber, BindingResource, BindingResources, BindlessDescriptor, BindlessIndex, BindlessIndexTableDescriptor...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `crates/bevy_text/src/text.rs` -> Churn: **78.95%** | Cog Load: 5.4219% | Debt: 98.6973%
- `crates/bevy_render/src/batching/gpu_preprocessing.rs` -> Churn: **73.15%** | Cog Load: 14.1527% | Debt: 57.8759%
- `crates/bevy_ecs/src/system/system_param.rs` -> Churn: **68.88%** | Cog Load: 6.0831% | Debt: 99.9997%
- `crates/bevy_ecs/src/world/mod.rs` -> Churn: **68.88%** | Cog Load: 5.013% | Debt: 87.0991%
- `crates/bevy_core_pipeline/src/core_3d/mod.rs` -> Churn: **63.72%** | Cog Load: 8.5917% | Debt: 99.7109%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `crates/bevy_asset/src/processor/mod.rs` -> **andriyDev** (87.5% isolated ownership) | Magnitude: 975.72
- `crates/bevy_math/src/primitives/dim2.rs` -> **Lynn** (100.0% isolated ownership) | Magnitude: 617.76
- `crates/bevy_tasks/src/task_pool.rs` -> **Gingeh** (100.0% isolated ownership) | Magnitude: 505.32
- `crates/bevy_ecs/src/schedule/stepping.rs` -> **Tauan Binato** (100.0% isolated ownership) | Magnitude: 480.2
- `crates/bevy_asset/src/server/info.rs` -> **andriyDev** (100.0% isolated ownership) | Magnitude: 479.48

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `crates/bevy_render/src/render_resource/uniform_buffer.rs` -> **Severity: 0.696** (Embedded: 0.0107 * Error Risk: 65.0828%)
- `crates/bevy_platform/src/time/fallback.rs` -> **Severity: 0.079** (Embedded: 0.0012 * Error Risk: 64.1355%)
- `crates/bevy_reflect/src/impls/core/panic.rs` -> **Severity: 0.066** (Embedded: 0.0014 * Error Risk: 47.1%)
- `crates/bevy_reflect/src/impls/core/option.rs` -> **Severity: 0.061** (Embedded: 0.0009 * Error Risk: 65.3982%)
- `crates/bevy_ui_widgets/src/observe.rs` -> **Severity: 0.057** (Embedded: 0.001 * Error Risk: 54.685%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `crates/bevy_reflect/src/impls/alloc/vec.rs` -> **Severity: 1126.6** (Blast Radius: 11.266 * Doc Risk: 100.0%)
- `crates/bevy_render/src/render_resource/uniform_buffer.rs` -> **Severity: 617.673** (Blast Radius: 8.94 * Doc Risk: 69.0909%)
- `tools/ci/src/commands/format.rs` -> **Severity: 428.2** (Blast Radius: 4.282 * Doc Risk: 100.0%)
- `tools/ci/src/main.rs` -> **Severity: 186.9** (Blast Radius: 1.869 * Doc Risk: 100.0%)
- `crates/bevy_reflect/src/impls/core/panic.rs` -> **Severity: 113.6** (Blast Radius: 1.136 * Doc Risk: 100.0%)

## APPENDIX A. STRUCTURAL SURFACE LEXICON (EQUATIONS & CONTEXT)
> **How the SAST Engine Calculates the Structural Surface Profile (Lower 0 - Higher Surface Presence 100%):**
> Most scores use a Sigmoid curve based on density (Hits / LOC) to prevent massive files from mathematically hiding their flaws. These 13 vectors are activity/content surface meters -- they describe what is present in a file, not the probability of a defect. The temporal-crucible validation record (gitgalaxy#2982, ~3,550 scanned snapshots, two repositories, pre-registered) tested the per-file-standing-risk claim to exhaustion and found it does not hold; see docs/vectors.md for the full record and gitgalaxy#2991 for the rename this drove. `risk_*` names remain the underlying column/key names for schema compatibility -- see the 'formerly' aliases below.
> 
> 1. **Complexity Load** (formerly Cognitive Load Exposure)**:** Measures the mental effort required for a developer to read and understand the file. `Density(Branches + (Flux * 2) + Async/Danger)` mitigated by `Doc Coverage`.
> 2. **Guard Balance** (formerly Error & Exception Risk Exposure)**:** Measures structural integrity and resilience against runtime errors. `Net Exposure = (Danger + Safety_Neg + Flux) - (Safety + Tests + Docs)`.
> 3. **Debt Markers** (formerly Tech Debt Exposure)**:** Measures the density of developer-annotated structural stress. `Density(TODOs [1x] + FIXMEs/Hacks [3x] + Empty Stubs [0.5x])`.
> 4. **Test Surface** (formerly Verification Risk Exposure)**:** Evaluates test coverage by comparing a function's structural complexity against the scope of the tests validating it.
> 5. **Connectivity** (formerly API Risk Exposure)**:** Measures the public surface area of a module. `Ratio(API Hits / Total Functions & Classes)`.
> 6. **Concurrency Surface** (formerly Concurrency Risk Exposure)**:** Measures the density of asynchronous operations, threading, and parallel execution logic.
> 7. **Mutation Surface** (formerly State Flux Risk Exposure)**:** Measures the frequency of data mutation and variable reassignment.
> 8. **Dead Code Surface** (formerly Commented Logic (dead code))**:** Measures the presence of abandoned, commented-out logic blocks.
> 9. **Spec Alignment** (formerly Spec Match Risk Exposure)**:** Measures how closely code aligns with formal specifications or architectural requirements.
> 10. **Historical Stability** (formerly Stability; predictive layer, promotion pending #2987)**:** Measures the recency of edits relative to the repository's entire lifespan. Part of the family the validation record actually supports as predictive -- currently ablated to zero in every scan (`GITGALAXY_DISABLE_GIT_HISTORY`, temporal-crucible#29).
> 11. **Historical Churn** (formerly Deep Churn; predictive layer, promotion pending #2987)**:** Measures the historical volatility and frequency of modification. Same predictive-layer status and ablation caveat as Historical Stability above.
> 12. **Documentation Surface** (formerly Documentation Risk Exposure)**:** Of the units extracted from a file, the weight-share a reader cannot recover from documentation -- public units count double, runtime-dynamic units count more, and a folder-level documentation umbrella shields the whole file. A ratio over units, not a density over lines; files with no extracted units have no value.
> 13. **Indentation Consistency:** Measures formatting alignment (Tabs vs. Spaces). Provided for codebase standardization context, not a functional risk.
> 
> **--- THE SECURITY & VULNERABILITY LENS ---**
> 14. **Obfuscation & Evasion Risk:** Measures the density of obfuscated logic, packed strings, and non-standard encoding.
> 15. **Logic Bomb / Sabotage Risk:** Measures condition-heavy execution leading to destructive OS, memory, or process commands.
> 16. **Injection Surface Risk Exposure:** Measures external network/I/O input flowing directly into dynamic execution contexts (XSS, SQLi, RCE).
> 17. **Memory Corruption Risk Exposure:** Measures the density of raw pointer math and manual memory allocations (Buffer Overflows, UAF).
> 18. **Credential Material** (formerly Secrets Risk Exposure)**:** Measures the presence of hardcoded credentials exposed to logs or globals.
> 
> **--- STRUCTURAL MAGNITUDE (NOT RISK) ---**
> **19. Function Magnitude (Impact Score):** Measures the physical footprint and 'heaviness' of a specific function. `((BranchHits + 1) * (Args + 1) + (0.05 * LOC)) * 10`. This is NOT a risk score.
> **20. File Magnitude (Total Impact):** Measures the total structural impact of a file. `Sum(Function Impacts) + API + Concurrency + Flux + (LOC / 50)`. This is NOT a risk score.

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with high Structural Magnitude combined with a wide Blast Radius, severe Z-Scores (Architectural Drift), or extreme spikes in individual surface vectors (like Mutation Surface or Complexity Load). Do NOT sum the surface vectors together or treat any total of them as a score -- they are independently scaled meters in different units (#3112). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
