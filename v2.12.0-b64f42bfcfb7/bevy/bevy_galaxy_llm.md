# ARCHITECTURAL_BRIEF: bevy
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/bevyengine/bevy.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |
| **Archetype Brains** | trained against engine v2.9.1 (44ffeb1e, 2026-09-19); last measured at engine 49cba5db on language-crucible@v1.7.0 |
| **Function archetypes** | **VALIDATED**, 98.4% agreement with trained state |
| **File archetypes** | **VALIDATED**, 98.7% agreement with trained state |
| **Composition (file)** | **DEGRADED**, 97.4% agreement with trained state -- engine changes since training relabelled 2.6% of crucible files (agreement 97.4%); composition_file inputs disagree with the function model's labels: never read ['Annotated & Test Methods', 'Stateful Encapsulated Methods'], never emitted ['Annotated Framework Methods', 'Tests & Verification'] -- those units drop out and those input columns are always 0.0 (retrain tracked in #4111) |
| **Composition (repo)** | **INVALID**, labels withheld -- not measurable on one corpus; inherits composition_file's measured state; composition_repo reads the composition_file brain labels by name, but none of its 20 inputs (e.g. 'Static: Literature & Documentation') is a label the composition_file brain emits (e.g. 'Annotated Framework Methods Files') -- every input column is 0.0 (retrain tracked in #4111) |

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 2174 analyzed artifact(s), 398514 LOC.
- **Load-bearing artifact:** `crates/bevy_internal/src/lib.rs` -- 434 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `examples/README.md` -- pulls in 404 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `crates/bevy_pbr/src/render/mesh.rs` at magnitude 1889.54 (structural weight, not risk).
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
| Analyzed Artifacts (Scanned) | 2174 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 725 |
| Total LOC | 398514 |
| Volatility Index | 0.002 |
| % Scanned of codebase = | 75.0% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5934 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1774 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 35.7% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.5143 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 32 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUST | 1744 | 395489 | 80.2% |
| MARKDOWN | 192 | 0 | 8.8% |
| PLAINTEXT | 144 | 0 | 6.6% |
| XML | 52 | 1 | 2.4% |
| YAML | 18 | 1988 | 0.8% |
| GROOVY | 6 | 140 | 0.3% |
| SHELL | 3 | 291 | 0.1% |
| JAVASCRIPT | 2 | 36 | 0.1% |
| TYPESCRIPT | 2 | 83 | 0.1% |
| GLSL | 2 | 43 | 0.1% |
| HTML | 2 | 144 | 0.1% |
| MAKEFILE | 2 | 21 | 0.1% |
| JAVA | 2 | 52 | 0.1% |
| BATCH | 2 | 132 | 0.1% |
| JSON | 1 | 94 | 0.0% |

## 4.1 SOURCE ENCODINGS
All 2174 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Generic / Templated Code Files 26%, Data / Markup / Trivial 22%, State Mutators Files 17%, Large Core Modules (3) 14%, Declarative / Non-Code 6%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 1837 | 84.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 336 | 15.5% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 725*

**Composition by Extension & Reason:**
- `.png`: 237x Excluded (Explicitly Denied Extension: '.png')
- `.wgsl`: 155x Unsupported Format (.wgsl), 37x Excluded (Unsupported Extension: '.wgsl')
- `.toml`: 90x Unsupported Format (.toml), 8x Excluded (Unsupported Extension: '.toml'), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.stderr`: 41x Excluded (Unsupported Extension: '.stderr'), 3x Unsupported Format (.stderr)
- `.ktx2`: 20x Excluded (Unsupported Extension: '.ktx2'), 6x Excluded (Binary Format Detected)
- `no_extension`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Unsupported Format (.undeterminable)
- `.glb`: 14x Excluded (Unsupported Extension: '.glb')
- `.gltf`: 14x Excluded (Explicitly Denied Extension: '.gltf')
- `.ron`: 12x Excluded (Unsupported Extension: '.ron')
- `.bin`: 11x Excluded (Unsupported Extension: '.bin')
- `.ttf`: 9x Excluded (Explicitly Denied Extension: '.ttf')
- `.jpg`: 8x Excluded (Explicitly Denied Extension: '.jpg')
- `.md`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.patch`: 7x Unsupported Format (.patch)
- `.ogg`: 4x Excluded (Explicitly Denied Extension: '.ogg')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 80.7 | 8.2 | 5.4 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 94.9 | 35.0 | 48.8 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 11.3 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 18.7 | 2.4 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 99.5 | 32.3 | 29.4 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 22.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 17.6 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 18.3 | 0.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 5.0 | 1.1 | 0.3 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 89.7 | 12.7 | 6.8 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 54.6 | 57.1 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 3416 | 624 | 4 | `crates/bevy_image/src/image.rs` |
| cleanup | 128 | 57 | 0 | `examples/math/render_primitives.rs` |
| guards | 7880 | 1114 | 10 | `crates/bevy_color/src/palettes/tailwind.rs` |
| danger | 5525 | 767 | 6 | `crates/bevy_reflect/src/lib.rs` |
| concurrency | 5682 | 728 | 7 | `crates/bevy_asset/src/processor/mod.rs` |
| connectivity | 22337 | 1616 | 28 | `crates/bevy_ui/src/ui_node.rs` |
| io | 217 | 68 | 0 | `crates/bevy_asset/src/io/file/sync_file_asset.rs` |
| crypto | 0 | 0 | 0 | - |
| ipc | 12 | 9 | 0 | `crates/bevy_pbr/src/render/mesh.rs` |
| time | 23 | 18 | 0 | `.github/start-wasm-example/tests/wasm_example.spec.ts` |
| serialization | 18 | 9 | 0 | `crates/bevy_remote/src/http.rs` |
| regex | 11 | 5 | 0 | `docs-rs/trait-tags.html` |
| events | 1026 | 284 | 1 | `crates/bevy_asset/src/processor/mod.rs` |
| tests | 9781 | 388 | 7 | `crates/bevy_reflect/src/lib.rs` |
| docs | 94992 | 1477 | 116 | `crates/bevy_ecs/src/system/query.rs` |
| debt | 2837 | 509 | 3 | `crates/bevy_ecs/src/query/fetch.rs` |
| mutation | 41700 | 1532 | 51 | `crates/bevy_pbr/src/render/mesh.rs` |
| dead_code | 1184 | 222 | 1 | `crates/bevy_ecs/src/system/mod.rs` |
| credential | 8 | 3 | 0 | `.github/start-wasm-example/package-lock.json` |
| threat | 127 | 95 | 0 | `examples/stress_tests/many_buttons.rs` |
| ml_ai | 5544 | 603 | 6 | `crates/bevy_math/src/ops.rs` |
| ui | 6 | 2 | 0 | `docs-rs/trait-tags.html` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.125**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `crates/bevy_asset/src/io/file/sync_file_asset.rs` (Hits: 26)
- `crates/bevy_asset/src/io/mod.rs` (Hits: 16)
- `examples/mobile/android_example/gradlew` (Hits: 15)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **lib.rs** (`crates/bevy_internal/src/lib.rs`) — 434 inbound connections
2. **mod.rs** (`crates/bevy_ecs/src/schedule/mod.rs`) — 407 inbound connections
3. **reflect.rs** (`crates/bevy_reflect/src/reflect.rs`) — 303 inbound connections
4. **lib.rs** (`crates/bevy_math/src/lib.rs`) — 242 inbound connections
5. **mod.rs** (`crates/bevy_ecs/src/component/mod.rs`) — 180 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **README.md** (`examples/README.md`) — 404 outbound dependencies
2. **lib.rs** (`crates/bevy_ecs/src/lib.rs`) — 164 outbound dependencies
3. **mesh.rs** (`crates/bevy_pbr/src/render/mesh.rs`) — 162 outbound dependencies
4. **mod.rs** (`crates/bevy_render/src/render_resource/mod.rs`) — 161 outbound dependencies
5. **mod.rs** (`crates/bevy_ecs/src/world/mod.rs`) — 151 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `prepare_lights` **(Many-Argument Workhorses)** (@ `crates/bevy_pbr/src/render/light.rs`) -> Impact: **341.3** | LOC: 986
- `assign_objects_to_clusters` **(Many-Argument Workhorses)** (@ `crates/bevy_light/src/cluster/assign.rs`) -> Impact: **313.4** | LOC: 640
  * *Intent:* /// Clusters point lights, spot lights, light probes, and decals. /// /// NOTE: Run this before `update_point_light_frusta`!
- `ktx2_dfd_header_to_texture_format` **(Many-Argument Workhorses)** (@ `crates/bevy_image/src/ktx2.rs`) -> Impact: **312.1** | LOC: 721
  * *Intent:* /// Reads the [`TextureFormat`] from a KTX2 data format descriptor header. /// /// # Errors /// /// Returns an error for invalid or unsupported textur...
- `load_gltf` **(Many-Argument Workhorses)** (@ `crates/bevy_gltf/src/loader/mod.rs`) -> Impact: **309.8** | LOC: 918
  * *Intent:* /// Loads an entire glTF file.
- `load_node` **(Many-Argument Workhorses)** (@ `crates/bevy_gltf/src/loader/mod.rs`) -> Impact: **219.9** | LOC: 399
  * *Intent:* /// Loads a glTF node.
- `example_control_system` **(Many-Argument Workhorses)** (@ `examples/3d/transmission.rs`) -> Impact: **205.9** | LOC: 218
- `derive_as_bind_group` **(Many-Argument Workhorses)** (@ `crates/bevy_render/macros/src/as_bind_group.rs`) -> Impact: **205.4** | LOC: 1082
- `prepare_uinodes` **(Many-Argument Workhorses)** (@ `crates/bevy_ui_render/src/lib.rs`) -> Impact: **203.5** | LOC: 404
- `changed_windows` **(Many-Argument Workhorses)** (@ `crates/bevy_winit/src/system.rs`) -> Impact: **183.8** | LOC: 295
  * *Intent:* /// Propagates changes from [`Window`] entities to the [`winit`] backend. /// /// # Notes /// /// - [`Window::present_mode`] and [`Window::composite_a...
- `pointer_events` **(Many-Argument Workhorses)** (@ `crates/bevy_picking/src/events.rs`) -> Impact: **181.5** | LOC: 529
  * *Intent:* /// the case of [`Enter`] → [`Leave`], shared parent entities will not receive [`Enter`] /// or [`Leave`]. /// /// Both [`Click`] and [`Release`] targ...

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `examples/3d` | 66 | 7389.82 | 15.92% | 0.0% |
| `crates/bevy_pbr/src/render` | 9 | 4901.34 | 7.99% | 6.13% |
| `crates/bevy_ecs/src/query` | 11 | 3730.16 | 7.13% | 37.26% |
| `crates/bevy_reflect/src` | 24 | 3310.22 | 4.6% | 36.47% |
| `crates/bevy_ecs/src/entity` | 13 | 3158.54 | 7.49% | 68.93% |
| `crates/bevy_asset/src` | 16 | 2950.96 | 6.49% | 19.39% |
| `crates/bevy_ecs/src/system` | 15 | 2887.68 | 8.48% | 44.67% |
| `crates/bevy_pbr/src` | 13 | 2781.94 | 7.3% | 4.28% |
| `crates/bevy_ecs/src/schedule` | 10 | 2736.56 | 7.69% | 34.87% |
| `crates/bevy_ui_render/src` | 10 | 2498.38 | 12.7% | 14.73% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `crates/bevy_audio/src/sinks.rs` -> **100.0%** Exposure
- `crates/bevy_core_pipeline/src/deferred/mod.rs` -> **100.0%** Exposure
- `crates/bevy_core_pipeline/src/prepass/mod.rs` -> **100.0%** Exposure
- `crates/bevy_ecs/src/bundle/mod.rs` -> **100.0%** Exposure
- `crates/bevy_ecs/src/component/mod.rs` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `benches/benches/bevy_ecs/components/add_remove_big_sparse_set.rs` -> **100.0%** Exposure
- `benches/benches/bevy_ecs/components/add_remove_big_table.rs` -> **100.0%** Exposure
- `benches/benches/bevy_ecs/components/add_remove_sparse_set.rs` -> **100.0%** Exposure
- `benches/benches/bevy_ecs/components/add_remove_table.rs` -> **100.0%** Exposure
- `benches/benches/bevy_ecs/empty_archetypes.rs` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `crates/bevy_ecs/src/query/fetch.rs` -> **0** Orphaned Functions | **154** Duplicates
- `crates/bevy_ecs/src/system/mod.rs` -> **86** Orphaned Functions | **2** Duplicates
- `crates/bevy_ecs/src/schedule/executor/mod.rs` -> **50** Orphaned Functions | **18** Duplicates
- `crates/bevy_ecs/src/world/entity_access/mod.rs` -> **68** Orphaned Functions | **0** Duplicates
- `crates/bevy_ecs/src/world/mod.rs` -> **63** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `9` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `28020` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `crates/bevy_pbr/src/render/mesh.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.315)
- **Top Global Matches:** file_cluster_4: 8.315, file_cluster_0: 9.782, file_cluster_15: 10.853
- **Magnitude:** 1889.54 | **LOC:** 4764 | **CtrlFlow:** 9.2% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **162**; blast radius 0.134; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (89.7%), Connectivity (formerly Api Exposure) (80.4%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 52.7132% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `specialize` **(Many-Argument Workhorses)** (Impact: 178.5)
  * `collect_meshes_for_gpu_building` **(Many-Argument Workhorses)** (Impact: 91.4)
    * *Intent:* /// Creates the [`RenderMeshInstanceGpu`]s and [`MeshInputUniform`]s when GPU /// preprocessing is i...
  * `check_views_need_specialization` **(Many-Argument Workhorses)** (Impact: 53.1)
  * `render` **(Many-Argument Workhorses)** (Impact: 51.8)
  * `render` **(Many-Argument Workhorses)** (Impact: 51.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 178 instances
* *High Risk Execution (weighted view):* 3
* *State Mutation (weighted view):* 596
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 340`, `structural_boundaries: 591`, `args: 131`, `func_start: 86`, `class_start: 43`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 4`, `state_mutation: 240`, `dead_code: 1`, `planned_debt: 4`, `fragile_debt: 4`, `duplicate_logic: 4`
* *Architecture:* `api: 149`, `concurrency: 7`, `import: 50`
* *Defense:* `safety: 59`, `doc: 466`, `test: 9`, `sync_locks: 2`, `immutability_locks: 108`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.134
  * `Choke Point (Betweenness):` 4.1e-05 | `Ripple Effect (Closeness):` 0.058975
  * `Imports (Out-Degree: 69):` alloc::sync::Arc, bevy_asset::AssetId, bevy_asset::AssetIndex, bevy_asset::AssetServer, bevy_asset::embedded_asset, bevy_asset::load_embedded_asset, bevy_asset::uuid::Uuid, bevy_camera::Camera...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `crates/bevy_pbr/src/render/light.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.225)
- **Top Global Matches:** file_cluster_6: 8.225, file_cluster_4: 9.578, file_cluster_0: 16.21
- **Magnitude:** 1233.86 | **LOC:** 2675 | **CtrlFlow:** 10.4% | **Authorship Centralization:** 45.8%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **101**; blast radius 0.138; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (85.3%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (80.0%), Connectivity (formerly Api Exposure) (62.8%)
- **Documentation Coverage:** 73.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `prepare_lights` **(Many-Argument Workhorses)** (Impact: 341.3)
  * `extract_lights` **(Many-Argument Workhorses)** (Impact: 145.1)
  * `queue_shadows` **(Many-Argument Workhorses)** (Impact: 111.8)
    * *Intent:* /// For each shadow cascade, iterates over all the meshes "visible" from it and /// adds them to [`B...
  * `specialize_shadows` **(Many-Argument Workhorses)** (Impact: 105.6)
  * `check_views_lights_need_specialization` **(Many-Argument Workhorses)** (Impact: 26.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 66 instances
* *State Mutation (weighted view):* 241
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 230`, `structural_boundaries: 406`, `args: 70`, `func_start: 28`, `class_start: 24`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 109`, `planned_debt: 5`
* *Architecture:* `api: 100`, `import: 34`
* *Defense:* `safety: 30`, `doc: 53`, `test: 1`, `immutability_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.138
  * `Choke Point (Betweenness):` 8.3e-05 | `Ripple Effect (Closeness):` 0.059183
  * `Imports (Out-Degree: 54):` alloc::sync::Arc, bevy_asset::UntypedAssetId, bevy_camera::Camera3d, bevy_camera::primitives::CUBE_MAP_FACES, bevy_camera::primitives::CascadesFrusta, bevy_camera::primitives::CubeMapFace, bevy_camera::primitives::CubemapFrusta, bevy_camera::primitives::Frustum...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `crates/bevy_gltf/src/loader/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.258)
- **Top Global Matches:** file_cluster_4: 8.258, file_cluster_12: 10.524, file_cluster_5: 11.028
- **Magnitude:** 986.82 | **LOC:** 2759 | **CtrlFlow:** 9.3% | **Authorship Centralization:** 34.8%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **138**; blast radius 0.333; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (79.0%), Mutation Surface (formerly State Flux) (57.2%), Guard Balance (formerly Safety Score) (50.8%)
- **Documentation Coverage:** 76.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `load_gltf` **(Many-Argument Workhorses)** (Impact: 309.8)
    * *Intent:* /// Loads an entire glTF file.
  * `load_node` **(Many-Argument Workhorses)** (Impact: 219.9)
    * *Intent:* /// Loads a glTF node.
  * `load_image` **(Many-Argument Workhorses)** (Impact: 31.6)
    * *Intent:* /// Loads a glTF texture as a bevy [`Image`] and returns it together with its label.
  * `load_material` **(Many-Argument Workhorses)** (Impact: 25.9)
    * *Intent:* /// Loads a glTF material as a bevy [`GltfMaterial`] and returns the label and material.
  * `load_buffers` **(Compute Cores)** (Impact: 19.4)
    * *Intent:* /// Loads the raw glTF buffer data for a specific glTF file.
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 48 instances
* *Concurrency (weighted view):* 31
* *State Mutation (weighted view):* 160
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 219`, `structural_boundaries: 508`, `args: 103`, `func_start: 29`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 30`, `high_risk_execution: 4`, `state_mutation: 64`, `planned_debt: 9`, `unreferenced_by_name: 10`
* *Architecture:* `io: 2`, `api: 36`, `concurrency: 21`, `import: 42`
* *Defense:* `safety: 86`, `doc: 94`, `test: 54`, `sync_locks: 5`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.333
  * `Choke Point (Betweenness):` 0.001776 | `Ripple Effect (Closeness):` 0.07698
  * `Imports (Out-Degree: 67):` extensions, gltf_ext, alloc::sync::Arc, async_lock::RwLock, bevy_animation::AnimatedBy, bevy_animation::AnimationTargetId, bevy_animation::VariableCurve, bevy_animation::animated_field...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `crates/bevy_asset/src/processor/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.536)
- **Top Global Matches:** file_cluster_4: 8.536, file_cluster_5: 9.247, file_cluster_12: 9.292
- **Magnitude:** 955.52 | **LOC:** 1865 | **CtrlFlow:** 12.7% | **Authorship Centralization:** 87.5%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **63**; blast radius 0.537; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (61.3%), Guard Balance (formerly Safety Score) (52.9%)
- **Documentation Coverage:** 20.5128% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `process_asset_internal` **(Many-Argument Workhorses)** (Impact: 72.7)
  * `initialize` **(Compute Cores)** (Impact: 44.9)
    * *Intent:* /// Populates the initial view of each asset by scanning the unprocessed and processed asset folders...
  * `handle_asset_source_event` **(Many-Argument Workhorses)** (Impact: 36.5)
  * `validate_transaction_log_and_recover` **(Defensive Guards)** (Impact: 35.8)
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
* *Structure:* `branch: 181`, `structural_boundaries: 458`, `args: 67`, `func_start: 55`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 32`, `high_risk_execution: 2`, `state_mutation: 44`, `dead_code: 1`, `planned_debt: 4`, `unreferenced_by_name: 5`
* *Architecture:* `api: 39`, `concurrency: 173`, `import: 16`
* *Defense:* `safety: 42`, `doc: 184`, `test: 1`, `sync_locks: 23`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.537
  * `Choke Point (Betweenness):` 0.000614 | `Ripple Effect (Closeness):` 0.145147
  * `Imports (Out-Degree: 17):` log, process, tests, alloc::borrow::ToOwned, alloc::boxed::Box, alloc::string::String, alloc::string::ToString, alloc::sync::Arc...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `crates/bevy_ecs/src/query/fetch.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.747)
- **Top Global Matches:** file_cluster_0: 7.747, file_cluster_5: 9.924, file_cluster_12: 11.511
- **Magnitude:** 934.9 | **LOC:** 4326 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 42.9%
- **Blast Radius:** changing it is visible to **49** in-repo importer(s); it depends on **57**; blast radius 1.626; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (54.8%), Guard Balance (formerly Safety Score) (49.8%)
- **Documentation Coverage:** 93.4783% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fetch` **(Generic / Templated Code)** (Impact: 12.5)
  * `derive_release_state` **(Generic / Templated Code)** (Impact: 12.2)
  * `test_contiguous_query_data` **(Annotated & Test Methods)** (Impact: 10.1)
  * `any_of_contiguous_test` **(Annotated & Test Methods)** (Impact: 7.9)
  * `init_fetch` **(Generic / Templated Code)** (Impact: 7.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 13 instances
* *High Risk Execution (weighted view):* 4
* *State Mutation (weighted view):* 71
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 217`, `structural_boundaries: 696`, `args: 335`, `func_start: 304`, `class_start: 44`
* *Risk/State:* `safety_bypasses: 21`, `high_risk_execution: 5`, `state_mutation: 45`, `planned_debt: 7`, `duplicate_logic: 154`
* *Architecture:* `api: 63`, `concurrency: 12`, `import: 17`
* *Defense:* `safety: 7`, `doc: 620`, `test: 40`, `immutability_locks: 67`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.626
  * `Choke Point (Betweenness):` 0.000407 | `Ripple Effect (Closeness):` 0.212563
  * `Imports (Out-Degree: 27):` bevy_ecs::prelude::Schedule, bevy_ecs_macros::QueryData, bevy_ptr::ThinSlicePtr, bevy_ptr::UnsafeCellDeref, bevy_utils::prelude::DebugName, core::cell::UnsafeCell, core::iter, core::marker::PhantomData...
  * `Imported By (In-Degree: 49):` (Excluded from Brief to save tokens)

### `crates/bevy_mesh/src/mesh.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.127)
- **Top Global Matches:** file_cluster_5: 6.127, file_cluster_12: 7.995, file_cluster_7: 10.008
- **Magnitude:** 930.92 | **LOC:** 3198 | **CtrlFlow:** 9.4% | **Authorship Centralization:** 11.1%
- **Blast Radius:** changing it is visible to **53** in-repo importer(s); it depends on **50**; blast radius 1.308; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (84.2%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (54.4%), Guard Balance (formerly Safety Score) (51.3%)
- **Documentation Coverage:** 17.77% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `triangles` **(Compute Cores)** (Impact: 28.2)
    * *Intent:* /// Get a list of this Mesh's [triangles] as an iterator if possible. /// /// Returns an error if an...
  * `merge_duplicate_vertices` **(Generic / Templated Code)** (Impact: 25.9)
    * *Intent:* /// Remove duplicate vertices and create the index pointing to the unique vertices. /// /// Returns ...
  * `merge` **(Many-Argument Workhorses)** (Impact: 22.7)
    * *Intent:* /// /// Note that attributes of `other` that don't exist on `self` will be ignored. /// /// `Aabb` o...
  * `try_transform_by` **(Defensive Guards)** (Impact: 19.9)
    * *Intent:* /// Transforms the vertex positions, normals, and tangents of the mesh in place by the given [`Trans...
  * `try_scale_by` **(Defensive Guards)** (Impact: 17.9)
    * *Intent:* /// Scales the vertex positions, normals, and tangents of the mesh in place by the given [`Vec3`]. /...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 24 instances
* *High Risk Execution (weighted view):* 3
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 119
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 177`, `structural_boundaries: 378`, `args: 193`, `func_start: 151`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 70`, `high_risk_execution: 6`, `state_mutation: 71`, `planned_debt: 1`, `fragile_debt: 4`
* *Architecture:* `api: 158`, `import: 29`
* *Defense:* `safety: 27`, `doc: 950`, `test: 59`, `immutability_locks: 17`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.308
  * `Choke Point (Betweenness):` 0.001539 | `Ripple Effect (Closeness):` 0.132105
  * `Imports (Out-Degree: 14):` VertexAttributeValues::*, alloc::collections::BTreeMap, bevy_asset::Asset, bevy_asset::RenderAssetUsages, bevy_math::*, bevy_math::Vec3, bevy_math::bounding::Aabb3d, bevy_math::primitives::Triangle3d...
  * `Imported By (In-Degree: 53):` (Excluded from Brief to save tokens)

### `crates/bevy_ecs/src/world/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.724)
- **Top Global Matches:** file_cluster_5: 7.724, file_cluster_0: 8.71, file_cluster_12: 9.603
- **Magnitude:** 911.88 | **LOC:** 4643 | **CtrlFlow:** 4.9% | **Authorship Centralization:** 13.3%
- **Blast Radius:** changing it is visible to **149** in-repo importer(s); it depends on **151**; blast radius 7.018; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (87.1%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (68.9%), Guard Balance (formerly Safety Score) (43.0%)
- **Documentation Coverage:** 14.0401% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `try_insert_batch_with_caller` **(Many-Argument Workhorses)** (Impact: 37.0)
    * *Intent:* /// Split into a new function so we can differentiate the calling location. /// /// This can be call...
  * `try_resource_scope` **(Generic / Templated Code)** (Impact: 26.5)
    * *Intent:* /// Temporarily removes the requested resource from this [`World`] if it exists, runs custom user co...
  * `insert_batch_with_caller` **(Many-Argument Workhorses)** (Impact: 18.0)
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
* *Structure:* `branch: 108`, `structural_boundaries: 567`, `args: 246`, `func_start: 191`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 38`, `high_risk_execution: 16`, `state_mutation: 31`, `planned_debt: 3`, `unreferenced_by_name: 63`
* *Architecture:* `api: 187`, `concurrency: 24`, `import: 32`
* *Defense:* `safety: 21`, `doc: 1921`, `test: 117`, `sync_locks: 10`, `immutability_locks: 1`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.018
  * `Choke Point (Betweenness):` 0.007865 | `Ripple Effect (Closeness):` 0.245333
  * `Imports (Out-Degree: 55):` command_queue, deferred_world, entity_access, entity_fetch, error, filtered_resource, identifier, reflect...
  * `Imported By (In-Degree: 149):` (Excluded from Brief to save tokens)

### `crates/bevy_pbr/src/prepass/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.074)
- **Top Global Matches:** file_cluster_6: 8.074, file_cluster_4: 10.964, file_cluster_8: 16.798
- **Magnitude:** 888.96 | **LOC:** 1504 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **120**; blast radius 0.163; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.2%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (66.0%), Guard Balance (formerly Safety Score) (58.6%)
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
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 2`, `state_mutation: 89`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 46`, `import: 23`
* *Defense:* `safety: 19`, `doc: 19`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.163
  * `Choke Point (Betweenness):` 0.000421 | `Ripple Effect (Closeness):` 0.079621
  * `Imports (Out-Degree: 60):` prepass_bindings, alloc::sync::Arc, bevy_app::App, bevy_app::Plugin, bevy_app::PreUpdate, bevy_asset::AssetServer, bevy_asset::Handle, bevy_asset::embedded_asset...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `crates/bevy_render/src/batching/gpu_preprocessing.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.664)
- **Top Global Matches:** file_cluster_0: 7.664, file_cluster_4: 9.224, file_cluster_15: 9.444
- **Magnitude:** 877.6 | **LOC:** 2732 | **CtrlFlow:** 8.0% | **Authorship Centralization:** 38.9%
- **Blast Radius:** changing it is visible to **15** in-repo importer(s); it depends on **88**; blast radius 0.315; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (73.2%), Mutation Surface (formerly State Flux) (70.9%), Connectivity (formerly Api Exposure) (70.5%)
- **Documentation Coverage:** 15.4412% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `batch_and_prepare_binned_render_phase` **(Many-Argument Workhorses)** (Impact: 80.0)
    * *Intent:* /// Creates batches for a render phase that uses bins.
  * `batch_and_prepare_sorted_render_phase` **(Many-Argument Workhorses)** (Impact: 61.7)
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
* *Structure:* `branch: 144`, `structural_boundaries: 408`, `args: 86`, `func_start: 76`, `class_start: 33`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 83`, `planned_debt: 1`, `duplicate_logic: 5`
* *Architecture:* `api: 133`, `concurrency: 42`, `import: 20`
* *Defense:* `safety: 24`, `doc: 537`, `test: 8`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.315
  * `Choke Point (Betweenness):` 0.000203 | `Ripple Effect (Closeness):` 0.111116
  * `Imports (Out-Degree: 36):` alloc::sync::Arc, bevy_app::App, bevy_app::Plugin, bevy_derive::Deref, bevy_derive::DerefMut, bevy_ecs::prelude::Entity, bevy_ecs::query::Has, bevy_ecs::query::With...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `crates/bevy_ui_render/src/lib.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.379)
- **Top Global Matches:** file_cluster_6: 7.379, file_cluster_4: 12.249, file_cluster_8: 14.666
- **Magnitude:** 874.92 | **LOC:** 1845 | **CtrlFlow:** 10.1% | **Authorship Centralization:** 31.6%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **112**; blast radius 0.888; role: Pure Consumer (Orchestrator)
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
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 80`, `planned_debt: 2`
* *Architecture:* `api: 96`, `concurrency: 14`, `import: 36`
* *Defense:* `safety: 15`, `doc: 108`, `immutability_locks: 30`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.888
  * `Choke Point (Betweenness):` 0.00292 | `Ripple Effect (Closeness):` 0.104582
  * `Imports (Out-Degree: 54):` box_shadow, debug_overlay, gradient, pipeline, render_pass, text, ui_material, ui_material_pipeline...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `crates/bevy_ecs/src/schedule/schedule.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.841)
- **Top Global Matches:** file_cluster_0: 7.841, file_cluster_5: 8.194, file_cluster_12: 8.864
- **Magnitude:** 840.98 | **LOC:** 2665 | **CtrlFlow:** 7.3% | **Authorship Centralization:** 25.0%
- **Blast Radius:** changing it is visible to **33** in-repo importer(s); it depends on **56**; blast radius 3.747; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (78.0%), Mutation Surface (formerly State Flux) (55.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (54.6%)
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
* *Structure:* `branch: 142`, `structural_boundaries: 547`, `args: 259`, `func_start: 140`, `class_start: 31`
* *Risk/State:* `safety_bypasses: 24`, `high_risk_execution: 5`, `state_mutation: 65`, `duplicate_logic: 14`
* *Architecture:* `api: 113`, `import: 22`
* *Defense:* `safety: 12`, `doc: 322`, `test: 119`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.747
  * `Choke Point (Betweenness):` 0.000598 | `Ripple Effect (Closeness):` 0.235045
  * `Imports (Out-Degree: 19):` Direction::Incoming, Direction::Outgoing, alloc::boxed::Box, alloc::collections::BTreeSet, alloc::format, alloc::string::String, alloc::string::ToString, alloc::vec...
  * `Imported By (In-Degree: 33):` (Excluded from Brief to save tokens)

### `crates/bevy_pbr/src/render/gpu_preprocess.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.698)
- **Top Global Matches:** file_cluster_0: 7.698, file_cluster_15: 9.031, file_cluster_4: 9.641
- **Magnitude:** 829.4 | **LOC:** 2947 | **CtrlFlow:** 8.0% | **Authorship Centralization:** 41.7%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **120**; blast radius 0.136; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (63.7%), Connectivity (formerly Api Exposure) (58.3%), Guard Balance (formerly Safety Score) (49.6%)
- **Documentation Coverage:** 50.8475% of unit weight undocumented
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
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 25`, `duplicate_logic: 3`
* *Architecture:* `api: 63`, `import: 17`
* *Defense:* `safety: 16`, `doc: 263`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.136
  * `Choke Point (Betweenness):` 4e-05 | `Ripple Effect (Closeness):` 0.059035
  * `Imports (Out-Degree: 51):` bevy_app::App, bevy_app::Plugin, bevy_asset::Handle, bevy_asset::embedded_asset, bevy_asset::load_embedded_asset, bevy_core_pipeline::deferred::node::late_deferred_prepass, bevy_core_pipeline::mip_generation::experimental::depth::ViewDepthPyramid, bevy_core_pipeline::mip_generation::experimental::depth::early_downsample_depth...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `crates/bevy_asset/src/server/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.038)
- **Top Global Matches:** file_cluster_0: 8.038, file_cluster_5: 8.35, file_cluster_12: 9.664
- **Magnitude:** 808.1 | **LOC:** 2255 | **CtrlFlow:** 7.9% | **Authorship Centralization:** 75.0%
- **Blast Radius:** changing it is visible to **63** in-repo importer(s); it depends on **77**; blast radius 1.204; role: Transceiver (Middle-Tier)
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
* *Structure:* `branch: 128`, `structural_boundaries: 365`, `args: 131`, `func_start: 92`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 32`, `planned_debt: 6`, `duplicate_logic: 9`, `unreferenced_by_name: 33`
* *Architecture:* `io: 1`, `api: 101`, `concurrency: 86`, `import: 18`
* *Defense:* `safety: 32`, `doc: 349`, `sync_locks: 5`, `immutability_locks: 2`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.204
  * `Choke Point (Betweenness):` 0.000866 | `Ripple Effect (Closeness):` 0.16015
  * `Imports (Out-Degree: 19):` info, loaders, alloc::borrow::ToOwned, alloc::boxed::Box, alloc::format, alloc::string::String, alloc::string::ToString, alloc::sync::Arc...
  * `Imported By (In-Degree: 63):` (Excluded from Brief to save tokens)

### `crates/bevy_pbr/src/wireframe.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.826)
- **Top Global Matches:** file_cluster_4: 8.826, file_cluster_0: 9.662, file_cluster_15: 11.907
- **Magnitude:** 804.04 | **LOC:** 1647 | **CtrlFlow:** 11.4% | **Authorship Centralization:** 26.7%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **119**; blast radius 0.131; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (80.3%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (68.9%), Connectivity (formerly Api Exposure) (68.1%)
- **Documentation Coverage:** 78.9474% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `specialize_wireframes` **(Many-Argument Workhorses)** (Impact: 140.8)
  * `queue_wireframes` **(Many-Argument Workhorses)** (Impact: 92.7)
  * `prepare_wireframe_wide_bind_groups` **(Many-Argument Workhorses)** (Impact: 71.9)
  * `render` **(Many-Argument Workhorses)** (Impact: 34.4)
  * `specialize` **(Many-Argument Workhorses)** (Impact: 18.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 39 instances
* *State Mutation (weighted view):* 129
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 155`, `structural_boundaries: 278`, `args: 59`, `func_start: 41`, `class_start: 29`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 51`
* *Architecture:* `api: 83`, `import: 16`
* *Defense:* `safety: 22`, `doc: 81`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.131
  * `Choke Point (Betweenness):` 0.000103 | `Ripple Effect (Closeness):` 0.078766
  * `Imports (Out-Degree: 50):` bevy_app::App, bevy_app::Plugin, bevy_app::PostUpdate, bevy_app::Startup, bevy_asset::AsAssetId, bevy_asset::Asset, bevy_asset::AssetApp, bevy_asset::AssetEventSystems...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `crates/bevy_remote/src/builtin_methods.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.025)
- **Top Global Matches:** file_cluster_4: 9.025, file_cluster_5: 9.216, file_cluster_0: 9.875
- **Magnitude:** 803.9 | **LOC:** 2235 | **CtrlFlow:** 14.2% | **Authorship Centralization:** 18.2%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **64**; blast radius 0.15; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (72.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (61.7%), Guard Balance (formerly Safety Score) (49.8%)
- **Documentation Coverage:** 26.4368% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `process_remote_get_components_watching_request` **(Many-Argument Workhorses)** (Impact: 56.9)
    * *Intent:* /// Handles a `world.get_components+watch` request coming from a client.
  * `process_remote_query_request` **(Many-Argument Workhorses)** (Impact: 46.2)
    * *Intent:* /// Handles a `world.query` request coming from a client.
  * `process_remote_list_components_watching_request` **(Many-Argument Workhorses)** (Impact: 38.2)
    * *Intent:* /// Handles a `world.list_components+watch` request coming from a client.
  * `process_remote_mutate_components_request` **(Defensive Guards)** (Impact: 27.2)
    * *Intent:* /// Handles a `world.mutate_components` request coming from a client. /// /// This method allows you...
  * `serialize_components` **(Defensive Guards)** (Impact: 23.7)
    * *Intent:* /// Serializes the specified components for an entity. /// The iterator yields ([`TypeId`], Option<[...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 70
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 220`, `structural_boundaries: 411`, `args: 101`, `func_start: 56`, `class_start: 45`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 28`, `duplicate_logic: 2`
* *Architecture:* `api: 132`, `import: 15`
* *Defense:* `safety: 29`, `doc: 329`, `test: 23`, `immutability_locks: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.15
  * `Choke Point (Betweenness):` 0.000128 | `Ripple Effect (Closeness):` 0.068006
  * `Imports (Out-Degree: 41):` anyhow::Result, anyhow::anyhow, bevy_ecs::component::Component, bevy_ecs::component::ComponentId, bevy_ecs::entity::Entity, bevy_ecs::event::Event, bevy_ecs::hierarchy::ChildOf, bevy_ecs::lifecycle::RemovedComponentEntity...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `crates/bevy_render/src/render_phase/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.932)
- **Top Global Matches:** file_cluster_0: 7.932, file_cluster_12: 8.84, file_cluster_5: 8.984
- **Magnitude:** 785.54 | **LOC:** 2669 | **CtrlFlow:** 7.9% | **Authorship Centralization:** 62.5%
- **Blast Radius:** changing it is visible to **39** in-repo importer(s); it depends on **77**; blast radius 0.719; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (59.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (54.6%), Guard Balance (formerly Safety Score) (53.0%)
- **Documentation Coverage:** 31.9672% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `render_multidrawable_batch_set` **(I/O & Config Routines)** (Impact: 50.2)
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
* *Structure:* `branch: 136`, `structural_boundaries: 347`, `args: 102`, `func_start: 92`, `class_start: 37`
* *Risk/State:* `safety_bypasses: 16`, `high_risk_execution: 13`, `state_mutation: 71`, `planned_debt: 1`, `fragile_debt: 2`, `duplicate_logic: 6`, `unreferenced_by_name: 8`
* *Architecture:* `api: 105`, `concurrency: 10`, `import: 38`
* *Defense:* `safety: 16`, `doc: 602`, `test: 17`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.719
  * `Choke Point (Betweenness):` 0.00052 | `Ripple Effect (Closeness):` 0.111767
  * `Imports (Out-Degree: 27):` draw, draw_state, rangefinder, bevy_app::App, bevy_app::Plugin, bevy_derive::Deref, bevy_derive::DerefMut, bevy_ecs::entity::Entity...
  * `Imported By (In-Degree: 39):` (Excluded from Brief to save tokens)

### `crates/bevy_ui/src/ui_node.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.851)
- **Top Global Matches:** file_cluster_0: 8.851, file_cluster_12: 9.851, file_cluster_5: 9.91
- **Magnitude:** 733.32 | **LOC:** 3236 | **CtrlFlow:** 4.0% | **Authorship Centralization:** 70.0%
- **Blast Radius:** changing it is visible to **39** in-repo importer(s); it depends on **34**; blast radius 1.194; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (77.4%), Debt Markers (formerly Tech Debt) (62.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (59.6%)
- **Documentation Coverage:** 26.2411% of unit weight undocumented
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
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 34`, `duplicate_logic: 24`
* *Architecture:* `api: 293`, `import: 19`
* *Defense:* `safety: 3`, `doc: 949`, `test: 47`, `immutability_locks: 27`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.194
  * `Choke Point (Betweenness):` 0.001078 | `Ripple Effect (Closeness):` 0.091167
  * `Imports (Out-Degree: 16):` bevy_camera::Camera, bevy_camera::RenderTarget, bevy_camera::visibility::Visibility, bevy_color::Alpha, bevy_color::Color, bevy_derive::Deref, bevy_derive::DerefMut, bevy_ecs::prelude::*...
  * `Imported By (In-Degree: 39):` (Excluded from Brief to save tokens)

### `crates/bevy_image/src/ktx2.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 7.275)
- **Top Global Matches:** file_cluster_3: 7.275, file_cluster_8: 27.377, file_cluster_6: 40.458
- **Magnitude:** 717.12 | **LOC:** 1542 | **CtrlFlow:** 18.9% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **29**; blast radius 0.252; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (51.5%), Mutation Surface (formerly State Flux) (41.4%), Connectivity (formerly Api Exposure) (30.2%)
- **Documentation Coverage:** 23.0769% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ktx2_dfd_header_to_texture_format` **(Many-Argument Workhorses)** (Impact: 312.1)
    * *Intent:* /// Reads the [`TextureFormat`] from a KTX2 data format descriptor header. /// /// # Errors /// /// ...
  * `ktx2_buffer_to_image` **(Many-Argument Workhorses)** (Impact: 107.8)
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
* *Structure:* `branch: 270`, `structural_boundaries: 157`, `args: 30`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 32`, `planned_debt: 3`, `fragile_debt: 1`
* *Architecture:* `io: 2`, `api: 6`, `import: 10`
* *Defense:* `safety: 3`, `doc: 23`, `test: 23`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.252
  * `Choke Point (Betweenness):` 8e-06 | `Ripple Effect (Closeness):` 0.124977
  * `Imports (Out-Degree: 3):` basis_universal::DecodeFlags, basis_universal::LowLevelUastcTranscoder, basis_universal::SliceParametersUastc, basis_universal::TranscoderBlockFormat, bevy_color::Srgba, bevy_utils::default, crate::CompressedImageFormats, ktx2::ChannelTypeQualifiers...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `crates/bevy_input/src/gamepad.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.868)
- **Top Global Matches:** file_cluster_0: 7.868, file_cluster_15: 8.685, file_cluster_12: 8.827
- **Magnitude:** 710.68 | **LOC:** 2979 | **CtrlFlow:** 5.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **53**; blast radius 0.752; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (70.2%), Guard Balance (formerly Safety Score) (47.0%), Mutation Surface (formerly State Flux) (13.6%)
- **Documentation Coverage:** 30.9859% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `gamepad_event_processing_system` **(Many-Argument Workhorses)** (Impact: 55.2)
    * *Intent:* /// Consumes [`RawGamepadEvent`] events, filters them using their [`GamepadSettings`] and if success...
  * `new` **(Many-Argument Workhorses)** (Impact: 39.2)
    * *Intent:* /// + `livezone_upperbound` - the value above which inputs will be rounded up to 1.0. /// + `thresho...
  * `get_axis_position_from_value` **(Compute Cores)** (Impact: 22.0)
  * `clamp` **(Compute Cores)** (Impact: 14.4)
    * *Intent:* /// Clamps the `raw_value` according to the `AxisSettings`.
  * `gamepad_connection_system` **(Compute Cores)** (Impact: 14.1)
    * *Intent:* /// Handles [`GamepadConnectionEvent`]s events. /// /// On connection, adds the components represent...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 31
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 123`, `structural_boundaries: 251`, `args: 108`, `func_start: 115`, `class_start: 26`
* *Risk/State:* `safety_bypasses: 12`, `high_risk_execution: 3`, `state_mutation: 13`, `duplicate_logic: 2`
* *Architecture:* `api: 156`, `import: 20`
* *Defense:* `safety: 14`, `doc: 538`, `test: 88`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.752
  * `Choke Point (Betweenness):` 0.000257 | `Ripple Effect (Closeness):` 0.090747
  * `Imports (Out-Degree: 23):` alloc::string::String, alloc::string::ToString, bevy_app::App, bevy_app::PreUpdate, bevy_ecs::change_detection::DetectChangesMut, bevy_ecs::component::Component, bevy_ecs::entity::Entity, bevy_ecs::message::Message...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `crates/bevy_ecs/src/entity/clone_entities.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.405)
- **Top Global Matches:** file_cluster_5: 7.405, file_cluster_0: 9.336, file_cluster_12: 9.422
- **Magnitude:** 693.54 | **LOC:** 2608 | **CtrlFlow:** 5.1% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **57**; blast radius 0.993; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (62.5%), Concurrency Surface (formerly Concurrency) (57.9%), Guard Balance (formerly Safety Score) (51.0%), Mutation Surface (formerly State Flux) (35.9%)
- **Documentation Coverage:** 46.7033% of unit weight undocumented
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
* *Amplified Cascading Flux:* 17 instances
* *Concurrency (weighted view):* 54
* *State Mutation (weighted view):* 84
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 93`, `structural_boundaries: 632`, `args: 135`, `func_start: 103`, `class_start: 79`
* *Risk/State:* `safety_bypasses: 42`, `high_risk_execution: 6`, `state_mutation: 50`, `planned_debt: 3`, `duplicate_logic: 2`
* *Architecture:* `api: 90`, `concurrency: 44`, `import: 21`
* *Defense:* `safety: 10`, `doc: 325`, `test: 134`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.993
  * `Choke Point (Betweenness):` 0.000368 | `Ripple Effect (Closeness):` 0.196507
  * `Imports (Out-Degree: 27):` alloc::boxed::Box, alloc::collections::VecDeque, alloc::vec, alloc::vec::Vec, bevy_platform::collections::HashMap, bevy_platform::collections::HashSet, bevy_platform::collections::hash_map::Entry, bevy_ptr::OwningPtr...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `crates/bevy_reflect/src/lib.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.522)
- **Top Global Matches:** file_cluster_5: 6.522, file_cluster_7: 9.328, file_cluster_12: 9.502
- **Magnitude:** 693.34 | **LOC:** 4268 | **CtrlFlow:** 1.0% | **Authorship Centralization:** 28.6%
- **Blast Radius:** changing it is visible to **131** in-repo importer(s); it depends on **141**; blast radius 6.001; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (71.3%), Guard Balance (formerly Safety Score) (58.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (40.8%), Mutation Surface (formerly State Flux) (30.7%)
- **Documentation Coverage:** 95.935% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `reflect_type_info` **(Annotated & Test Methods)** (Impact: 15.4)
  * `reflect_complex_patch` **(I/O & Config Routines)** (Impact: 7.7)
  * `should_reflect_debug` **(Annotated & Test Methods)** (Impact: 6.9)
  * `custom_cmp` **(Generic / Templated Code)** (Impact: 5.5)
  * `should_composite_reflect_clone` **(Annotated & Test Methods)** (Impact: 5.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 117
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 907`, `args: 132`, `func_start: 129`, `class_start: 185`
* *Risk/State:* `safety_bypasses: 159`, `high_risk_execution: 3`, `state_mutation: 115`, `planned_debt: 11`
* *Architecture:* `api: 186`, `import: 76`
* *Defense:* `safety: 12`, `doc: 635`, `test: 374`, `sync_locks: 6`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.001
  * `Choke Point (Betweenness):` 0.022772 | `Ripple Effect (Closeness):` 0.262989
  * `Imports (Out-Degree: 35):` alloc, array, attributes, bevy_platform, core, enums, error, fields...
  * `Imported By (In-Degree: 131):` (Excluded from Brief to save tokens)

### `crates/bevy_ecs/src/query/access.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.18)
- **Top Global Matches:** file_cluster_0: 7.18, file_cluster_13: 7.856, file_cluster_15: 8.284
- **Magnitude:** 691.66 | **LOC:** 2033 | **CtrlFlow:** 5.2% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **31** in-repo importer(s); it depends on **28**; blast radius 1.518; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (75.6%), Mutation Surface (formerly State Flux) (56.2%), Guard Balance (formerly Safety Score) (47.6%)
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
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 65`, `planned_debt: 2`
* *Architecture:* `api: 159`, `import: 26`
* *Defense:* `doc: 315`, `test: 98`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.518
  * `Choke Point (Betweenness):` 1.7e-05 | `Ripple Effect (Closeness):` 0.210102
  * `Imports (Out-Degree: 3):` alloc::format, alloc::string::String, alloc::vec, alloc::vec::Vec, core::fmt, core::fmt::Debug, core::iter::FusedIterator, crate::component::ComponentId...
  * `Imported By (In-Degree: 31):` (Excluded from Brief to save tokens)

### `crates/bevy_ecs/src/system/system_param.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.026)
- **Top Global Matches:** file_cluster_0: 7.026, file_cluster_5: 9.308, file_cluster_13: 10.688
- **Magnitude:** 665.88 | **LOC:** 3013 | **CtrlFlow:** 6.1% | **Authorship Centralization:** 26.7%
- **Blast Radius:** changing it is visible to **79** in-repo importer(s); it depends on **58**; blast radius 4.418; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (68.9%), Connectivity (formerly Api Exposure) (64.4%)
- **Documentation Coverage:** 80.9322% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `init_access` **(Generic / Templated Code)** (Impact: 9.9)
  * `get_param` **(Generic / Templated Code)** (Impact: 9.8)
  * `init_access` **(Generic / Templated Code)** (Impact: 7.9)
  * `init_access` **(Generic / Templated Code)** (Impact: 7.9)
  * `get_param` **(Generic / Templated Code)** (Impact: 7.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 3 instances
* *High Risk Execution (weighted view):* 7
* *State Mutation (weighted view):* 29
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 104`, `structural_boundaries: 580`, `args: 207`, `func_start: 196`, `class_start: 38`
* *Risk/State:* `safety_bypasses: 13`, `high_risk_execution: 9`, `state_mutation: 23`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 59`
* *Architecture:* `api: 83`, `concurrency: 18`, `import: 19`
* *Defense:* `safety: 6`, `doc: 826`, `test: 23`, `immutability_locks: 4`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.418
  * `Choke Point (Betweenness):` 0.001166 | `Ripple Effect (Closeness):` 0.230496
  * `Imports (Out-Degree: 24):` alloc::borrow::Cow, alloc::boxed::Box, alloc::vec::Vec, bevy_ecs_macros::SystemParam, bevy_platform::cell::SyncCell, bevy_ptr::UnsafeCellDeref, bevy_utils::prelude::DebugName, core::any::Any...
  * `Imported By (In-Degree: 79):` (Excluded from Brief to save tokens)

### `crates/bevy_asset/src/lib.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.364)
- **Top Global Matches:** file_cluster_5: 6.364, file_cluster_12: 8.878, file_cluster_0: 9.066
- **Magnitude:** 648.72 | **LOC:** 3087 | **CtrlFlow:** 5.1% | **Authorship Centralization:** 52.9%
- **Blast Radius:** changing it is visible to **144** in-repo importer(s); it depends on **127**; blast radius 4.63; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (71.8%), Connectivity (formerly Api Exposure) (63.0%), Guard Balance (formerly Safety Score) (51.0%), Concurrency Surface (formerly Concurrency) (30.3%)
- **Documentation Coverage:** 85.9259% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `load_dependencies` **(I/O & Config Routines)** (Impact: 25.5)
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
* *Structure:* `branch: 119`, `structural_boundaries: 671`, `args: 138`, `func_start: 99`, `class_start: 40`
* *Risk/State:* `safety_bypasses: 65`, `high_risk_execution: 9`, `state_mutation: 24`, `planned_debt: 3`, `duplicate_logic: 5`
* *Architecture:* `io: 9`, `api: 97`, `concurrency: 29`, `import: 40`
* *Defense:* `safety: 11`, `doc: 264`, `test: 191`, `sync_locks: 3`, `immutability_locks: 9`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.63
  * `Choke Point (Betweenness):` 0.010433 | `Ripple Effect (Closeness):` 0.215607
  * `Imports (Out-Degree: 43):` asset_changed, assets, direct_access_ext, event, folder, handle, id, io...
  * `Imported By (In-Degree: 144):` (Excluded from Brief to save tokens)

### `crates/bevy_math/src/primitives/dim2.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.97)
- **Top Global Matches:** file_cluster_0: 7.97, file_cluster_13: 8.376, file_cluster_15: 9.469
- **Magnitude:** 639.76 | **LOC:** 2638 | **CtrlFlow:** 4.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **15** in-repo importer(s); it depends on **29**; blast radius 1.412; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (94.3%), Connectivity (formerly Api Exposure) (85.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (45.7%)
- **Documentation Coverage:** 19.6481% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `closest_point` **(Compute Cores)** (Impact: 12.1)
    * *Intent:* /// Finds the point on the rhombus that is closest to the given `point`. /// /// If the point is out...
  * `closest_point` **(Compute Cores)** (Impact: 9.7)
    * *Intent:* /// Finds the point on the annulus that is closest to the given `point`: /// /// - If the point is o...
  * `winding_order` **(Annotated & Test Methods)** (Impact: 7.7)
    * *Intent:* /// Get the [`WindingOrder`] of the triangle
  * `perimeter` **(Compute Cores)** (Impact: 7.0)
  * `closest_point` **(Compute Cores)** (Impact: 6.7)
    * *Intent:* /// Returns the point on the [`Segment2d`] that is closest to the specified `point`.
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 3 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 80`, `structural_boundaries: 266`, `args: 201`, `func_start: 196`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 3`, `state_mutation: 9`, `planned_debt: 2`, `duplicate_logic: 26`
* *Architecture:* `api: 190`, `import: 15`
* *Defense:* `safety: 3`, `doc: 419`, `test: 96`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.412
  * `Choke Point (Betweenness):` 0.000159 | `Ripple Effect (Closeness):` 0.125124
  * `Imports (Out-Degree: 12):` alloc::vec::Vec, approx::assert_abs_diff_eq, approx::assert_relative_eq, bevy_reflect::Reflect, bevy_reflect::ReflectDeserialize, bevy_reflect::ReflectSerialize, bevy_reflect::std_traits::ReflectDefault, core::f32::consts::FRAC_1_SQRT_2...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `crates/bevy_reflect/derive/src/impls/common.rs` (RUST) | Magnitude: 95.8 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 199, structural_boundaries: 49, args: 33, pointers: 25
- `examples/3d/spherical_area_lights.rs` (RUST) | Magnitude: 13.2 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 49, structural_boundaries: 11, core_var_decl: 8, design_snake_case: 8
- `crates/bevy_window/src/monitor.rs` (RUST) | Magnitude: 17.7 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 24, indent_spaces: 23, api: 15, decorators: 15
- `crates/bevy_time/src/virt.rs` (RUST) | Magnitude: 78.34 | Delta: **0.036** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 209, doc: 147, test: 75, structural_boundaries: 34
- `examples/2d/mesh2d_alpha_mode.rs` (RUST) | Magnitude: 17.22 | Delta: **0.037** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 74, concurrency: 7, structural_boundaries: 6, generics: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `crates/bevy_render/src/diagnostic/tracy_gpu.rs` (RUST) | Magnitude: 12.6 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 51, structural_boundaries: 14, core_var_decl: 8, design_snake_case: 8
- `crates/bevy_app/src/lib.rs` (RUST) | Magnitude: 32.16 | Delta: **0.043** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 25, indent_spaces: 18, api: 14, import: 12
- `crates/bevy_core_pipeline/src/lib.rs` (RUST) | Magnitude: 24.02 | Delta: **0.094** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 31, structural_boundaries: 29, api: 17, import: 11
- `crates/bevy_log/src/lib.rs` (RUST) | Magnitude: 57.26 | Delta: **0.097** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: doc: 192, indent_spaces: 143, structural_boundaries: 50, core_var_decl: 32
- `crates/bevy_ecs/src/storage/blob_array.rs` (RUST) | Magnitude: 162.4 | Delta: **0.115** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 283, doc: 153, structural_boundaries: 64, decorators: 36

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `crates/bevy_pbr/src/parallax.rs` (RUST) | Magnitude: 6.48 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: doc: 25, indent_spaces: 12, structural_boundaries: 3, api: 3
- `crates/bevy_color/src/xyza.rs` (RUST) | Magnitude: 83.96 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 180, structural_boundaries: 33, api: 29, doc: 28
- `crates/bevy_text/src/bounds.rs` (RUST) | Magnitude: 18.46 | Delta: **0.031** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 35, doc: 16, api: 9, structural_boundaries: 7
- `benches/benches/bevy_ecs/components/insert_simple.rs` (RUST) | Magnitude: 6.64 | Delta: **0.043** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 11, class_start: 5, decorators: 4
- `examples/ecs/custom_schedule.rs` (RUST) | Magnitude: 12.78 | Delta: **0.085** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 27, structural_boundaries: 11, args: 8, func_start: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `crates/bevy_ecs/compile_fail/tests/ui/system_state_get_lifetime_safety.rs` (RUST) | Magnitude: 2.88 | Delta: **0.069** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: structural_boundaries: 14, indent_spaces: 9, safety_bypasses: 4, core_var_decl: 4
- `crates/bevy_ecs/compile_fail/tests/ui/system_state_iter_lifetime_safety.rs` (RUST) | Magnitude: 2.58 | Delta: **0.087** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: structural_boundaries: 14, indent_spaces: 9, safety_bypasses: 4, core_var_decl: 4
- `crates/bevy_ecs/compile_fail/tests/ui/system_query_iter_lifetime_safety.rs` (RUST) | Magnitude: 2.1 | Delta: **0.09** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 12, indent_spaces: 5, core_var_decl: 4, design_snake_case: 3
- `crates/bevy_ecs/compile_fail/tests/ui/query_lens_lifetime_safety.rs` (RUST) | Magnitude: 4.64 | Delta: **0.103** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 49, indent_spaces: 29, core_var_decl: 8, design_snake_case: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `crates/bevy_pbr/src/meshlet/visibility_buffer_raster_node.rs` (RUST) | Magnitude: 162.14 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 596, structural_boundaries: 73, branch: 29, core_var_decl: 21
- `examples/large_scenes/mipmap_generator/examples/test_compression.rs` (RUST) | Magnitude: 64.64 | Delta: **0.055** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 106, structural_boundaries: 32, core_var_decl: 16, design_snake_case: 15
- `crates/bevy_image/src/image_texture_conversion.rs` (RUST) | Magnitude: 125.5 | Delta: **0.076** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 176, core_var_decl: 66, design_snake_case: 65, state_mutation: 45
- `crates/bevy_color/src/color.rs` (RUST) | Magnitude: 218.42 | Delta: **0.08** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 580, doc: 243, scientific: 101, args: 54
- `examples/math/bounding_2d.rs` (RUST) | Magnitude: 153.36 | Delta: **0.089** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 312, structural_boundaries: 83, core_var_decl: 39, design_snake_case: 34

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `crates/bevy_reflect/derive/src/generics.rs` (RUST) | Magnitude: 11.98 | Delta: **0.059** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 52, structural_boundaries: 16, core_var_decl: 9, design_snake_case: 9
- `crates/bevy_asset/macros/src/lib.rs` (RUST) | Magnitude: 31.64 | Delta: **0.079** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 75, structural_boundaries: 33, core_var_decl: 22, args: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `crates/bevy_platform/src/sync/mod.rs` (RUST) | Magnitude: 23.46 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 16, sync_locks: 10, import: 9, api: 8
- `crates/bevy_reflect/src/impls/core/mod.rs` (RUST) | Magnitude: 15.22 | Delta: **0.098** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 11
- `crates/bevy_log/src/once.rs` (RUST) | Magnitude: 15.6 | Delta: **0.102** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: doc: 15, indent_spaces: 15, decorators: 5, reflection_metaprogramming: 5
- `benches/src/lib.rs` (RUST) | Magnitude: 13.12 | Delta: **0.111** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: doc: 38, indent_spaces: 3, decorators: 1, reflection_metaprogramming: 1
- `tools/ci/src/commands/mod.rs` (RUST) | Magnitude: 0.03 | Delta: **0.201** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 32, api: 16, import: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `crates/bevy_reflect/src/func/args/mod.rs` (RUST) | Magnitude: 22.28 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 14, api: 7, import: 7, doc: 4
- `crates/bevy_color/src/color_difference.rs` (RUST) | Magnitude: 5.84 | Delta: **0.061** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 5, indent_spaces: 4, structural_boundaries: 2, args: 2
- `crates/bevy_ui/src/widget/mod.rs` (RUST) | Magnitude: 21.24 | Delta: **0.113** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 12, api: 6, import: 6, doc: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `examples/3d/anti_aliasing.rs` (RUST) | Magnitude: 292.02 | Delta: **0.071** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 433, structural_boundaries: 63, branch: 57, state_mutation: 50
- `crates/bevy_ecs/macros/src/query_data.rs` (RUST) | Magnitude: 203.54 | Delta: **0.11** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 552, structural_boundaries: 118, branch: 62, generics: 61
- `examples/3d/tonemapping.rs` (RUST) | Magnitude: 444.56 | Delta: **0.163** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 489, branch: 87, structural_boundaries: 71, state_mutation: 54

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `crates/bevy_pbr/src/material_bind_groups.rs` (RUST) | Magnitude: 616.02 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 1351, doc: 370, structural_boundaries: 243, generics: 128
- `crates/bevy_ecs_serialization/src/dynamic_scene_builder.rs` (RUST) | Magnitude: 176.0 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 409, doc: 188, structural_boundaries: 147, core_var_decl: 78
- `crates/bevy_asset/src/loader_builders.rs` (RUST) | Magnitude: 139.86 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 261, doc: 176, structural_boundaries: 85, generics: 74
- `crates/bevy_ecs/src/relationship/relationship_source_collection.rs` (RUST) | Magnitude: 356.54 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 515, structural_boundaries: 190, args: 128, func_start: 118
- `crates/bevy_ui/src/geometry.rs` (RUST) | Magnitude: 310.66 | Delta: **0.049** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 602, doc: 474, api: 95, args: 92

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `crates/bevy_material/macros/src/lib.rs` (RUST) | Magnitude: 12.48 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 10, core_var_decl: 5, design_snake_case: 5
- `crates/bevy_tasks/examples/busy_behavior.rs` (RUST) | Magnitude: 7.84 | Delta: **0.072** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 8, core_var_decl: 5, design_snake_case: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `crates/bevy_sprite_render/src/texture_slice/computed_slices.rs` (RUST) | Magnitude: 75.76 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 107, structural_boundaries: 28, doc: 21, branch: 19
- `examples/ui/ui_drag_and_drop.rs` (RUST) | Magnitude: 34.2 | Delta: **0.061** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 87, structural_boundaries: 48, args: 9, branch: 8
- `crates/bevy_reflect/src/enums/helpers.rs` (RUST) | Magnitude: 70.0 | Delta: **0.068** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 114, structural_boundaries: 37, doc: 36, branch: 29

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `crates/bevy_text/src/text.rs` -> Churn: **78.95%** | Cog Load: 5.4219% | Debt: 69.2183%
- `crates/bevy_ecs/src/system/system_param.rs` -> Churn: **68.88%** | Cog Load: 5.6643% | Debt: 99.9977%
- `crates/bevy_ecs/src/world/mod.rs` -> Churn: **68.88%** | Cog Load: 4.9332% | Debt: 87.0991%
- `crates/bevy_core_pipeline/src/core_3d/mod.rs` -> Churn: **63.72%** | Cog Load: 8.543% | Debt: 99.7109%
- `crates/bevy_render/src/view/mod.rs` -> Churn: **63.72%** | Cog Load: 4.1756% | Debt: 58.9291%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `crates/bevy_asset/src/processor/mod.rs` -> **andriyDev** (87.5% isolated ownership) | Magnitude: 955.52
- `crates/bevy_math/src/primitives/dim2.rs` -> **Lynn** (100.0% isolated ownership) | Magnitude: 639.76
- `crates/bevy_tasks/src/task_pool.rs` -> **Gingeh** (100.0% isolated ownership) | Magnitude: 503.32
- `crates/bevy_asset/src/server/info.rs` -> **andriyDev** (100.0% isolated ownership) | Magnitude: 479.48
- `crates/bevy_ecs/src/schedule/stepping.rs` -> **Tauan Binato** (100.0% isolated ownership) | Magnitude: 471.1

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `crates/bevy_internal/src/lib.rs` -> **Severity: 1.071** (Bridge: 0.0911 * Flux: 11.7597%)
- `crates/bevy_reflect/src/lib.rs` -> **Severity: 0.7** (Bridge: 0.0228 * Flux: 30.741%)
- `crates/bevy_reflect/src/type_registry.rs` -> **Severity: 0.346** (Bridge: 0.0069 * Flux: 50.0%)
- `crates/bevy_reflect/src/serde/mod.rs` -> **Severity: 0.29** (Bridge: 0.0122 * Flux: 23.8724%)
- `crates/bevy_ecs/src/lib.rs` -> **Severity: 0.27** (Bridge: 0.0106 * Flux: 25.4589%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `crates/bevy_reflect/src/attributes.rs` -> **Severity: 17.125** (Embedded: 0.2141 * Error Risk: 80.0%)
- `crates/bevy_reflect/src/serde/mod.rs` -> **Severity: 16.338** (Embedded: 0.229 * Error Risk: 71.3437%)
- `crates/bevy_reflect/src/generics.rs` -> **Severity: 15.543** (Embedded: 0.2163 * Error Risk: 71.8719%)
- `crates/bevy_reflect/src/path/mod.rs` -> **Severity: 15.425** (Embedded: 0.1928 * Error Risk: 80.0%)
- `crates/bevy_reflect/src/lib.rs` -> **Severity: 15.307** (Embedded: 0.263 * Error Risk: 58.2033%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `crates/bevy_ecs/src/schedule/mod.rs` -> **Severity: 2253.641** (Blast Radius: 23.073 * Doc Risk: 97.6744%)
- `crates/bevy_reflect/src/kind.rs` -> **Severity: 924.437** (Blast Radius: 12.711 * Doc Risk: 72.7273%)
- `crates/bevy_platform/src/hash.rs` -> **Severity: 862.6** (Blast Radius: 12.939 * Doc Risk: 66.6667%)
- `crates/bevy_reflect/src/reflect.rs` -> **Severity: 668.01** (Blast Radius: 29.864 * Doc Risk: 22.3684%)
- `crates/bevy_reflect/src/lib.rs` -> **Severity: 575.706** (Blast Radius: 6.001 * Doc Risk: 95.935%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 426 literal sites + 15 sites through wrappers = 441

- `update_system_two` (function, debug_prints, primitive): 6 call sites in 1 files -- `examples/ecs/system_stepping.rs`
- `pre_update_system` (function, debug_prints, primitive): 3 call sites in 1 files -- `examples/ecs/system_stepping.rs`
- `update_system_three` (function, debug_prints, primitive): 3 call sites in 1 files -- `examples/ecs/system_stepping.rs`
- `update_system_one` (function, debug_prints, primitive): 2 call sites in 1 files -- `examples/ecs/system_stepping.rs`
- `update_system_four` (function, debug_prints, primitive): 1 call sites in 1 files -- `examples/ecs/system_stepping.rs`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 89094 call pairs -- scoped 22.1%, unique 0.0%, ambiguous 32.9%, external 45.0%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| rust | 89048 | 22.1% | 0.0% | 32.9% | 45.0% |
| html | 15 | 6.7% | 0.0% | 0.0% | 93.3% |
| shell | 14 | 28.6% | 0.0% | 0.0% | 71.4% |
| typescript | 9 | 0.0% | 0.0% | 0.0% | 100.0% |
| java | 8 | 25.0% | 0.0% | 0.0% | 75.0% |

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
