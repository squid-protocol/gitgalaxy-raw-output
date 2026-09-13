# ARCHITECTURAL_BRIEF: bevy
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/bevyengine/bevy.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
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
## 2. THE 13-POINT STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (EQUATIONS & CONTEXT)
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

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 2835 |
| Analyzed Artifacts (Scanned) | 2096 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 739 |
| Total LOC | 383562 |
| Volatility Index | 0.002 |
| % Scanned of codebase = | 73.9% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4092 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.6889 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.3131 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 21 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUST | 1710 | 382701 | 81.6% |
| MARKDOWN | 157 | 0 | 7.5% |
| PLAINTEXT | 145 | 0 | 6.9% |
| XML | 52 | 1 | 2.5% |
| BINARY_THREAT | 11 | 11 | 0.5% |
| GROOVY | 6 | 166 | 0.3% |
| SHELL | 3 | 291 | 0.1% |
| GLSL | 2 | 43 | 0.1% |
| HTML | 2 | 144 | 0.1% |
| MAKEFILE | 2 | 21 | 0.1% |
| CPP | 2 | 0 | 0.1% |
| JAVA | 2 | 52 | 0.1% |
| BATCH | 2 | 132 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 1782 | 85.0% |
| Unknown | 11 | 0.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 302 | 14.4% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 739*

**Composition by Extension & Reason:**
- `.png`: 237x Excluded (Explicitly Denied Extension: '.png')
- `.wgsl`: 154x Unsupported Format (.wgsl), 37x Excluded (Unsupported Extension: '.wgsl')
- `.toml`: 88x Unsupported Format (.toml), 8x Excluded (Unsupported Extension: '.toml'), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.stderr`: 41x Excluded (Unsupported Extension: '.stderr'), 3x Unsupported Format (.stderr)
- `.ktx2`: 20x Excluded (Unsupported Extension: '.ktx2'), 6x Excluded (Binary Format Detected)
- `.yml`: 18x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
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
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 35.6 | 45.9 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 28.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 18.3 | 2.4 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 18.6 | 9.9 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 21.8 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 17.7 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 6.2 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 90.9 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 6.6 | 1.2 | 0.6 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 89.2 | 12.5 | 7.3 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 53.3 | 54.4 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 18467 | 1264 | 25 | `crates/bevy_ecs/src/query/fetch.rs` |
| cleanup | 121 | 54 | 0 | `examples/math/render_primitives.rs` |
| guards | 7545 | 1074 | 10 | `crates/bevy_color/src/palettes/tailwind.rs` |
| danger | 5344 | 747 | 6 | `crates/bevy_reflect/src/lib.rs` |
| concurrency | 5511 | 704 | 7 | `crates/bevy_asset/src/processor/mod.rs` |
| connectivity | 19846 | 1555 | 26 | `crates/bevy_ui/src/ui_node.rs` |
| io | 205 | 61 | 0 | `crates/bevy_asset/src/io/file/sync_file_asset.rs` |
| crypto | 0 | 0 | 0 | - |
| ipc | 12 | 9 | 0 | `crates/bevy_pbr/src/render/mesh.rs` |
| time | 18 | 16 | 0 | `crates/bevy_asset/src/processor/mod.rs` |
| serialization | 18 | 9 | 0 | `crates/bevy_remote/src/http.rs` |
| regex | 11 | 5 | 0 | `docs-rs/trait-tags.html` |
| events | 997 | 274 | 1 | `crates/bevy_asset/src/processor/mod.rs` |
| tests | 9546 | 381 | 7 | `crates/bevy_reflect/src/lib.rs` |
| docs | 91761 | 1430 | 117 | `crates/bevy_ecs/src/system/query.rs` |
| debt | 2721 | 481 | 3 | `crates/bevy_ecs/src/query/fetch.rs` |
| mutation | 40149 | 1487 | 50 | `crates/bevy_pbr/src/render/mesh.rs` |
| dead_code | 8407 | 1005 | 11 | `crates/bevy_ecs/src/world/mod.rs` |
| credential | 3 | 2 | 0 | `examples/3d/solari.rs` |
| threat | 933 | 292 | 1 | `crates/bevy_ptr/src/lib.rs` |
| ml_ai | 5431 | 593 | 6 | `crates/bevy_math/src/ops.rs` |
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

1. **vec.rs** (`crates/bevy_reflect/src/impls/alloc/vec.rs`) — 29 inbound connections
2. **uniform_buffer.rs** (`crates/bevy_render/src/render_resource/uniform_buffer.rs`) — 23 inbound connections
3. **format.rs** (`tools/ci/src/commands/format.rs`) — 12 inbound connections
4. **tokens.rs** (`crates/bevy_feathers/src/tokens.rs`) — 8 inbound connections
5. **observe.rs** (`crates/bevy_ui_widgets/src/observe.rs`) — 4 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **README.md** (`examples/README.md`) — 395 outbound dependencies
2. **mesh.rs** (`crates/bevy_pbr/src/render/mesh.rs`) — 159 outbound dependencies
3. **mod.rs** (`crates/bevy_ecs/src/world/mod.rs`) — 156 outbound dependencies
4. **mod.rs** (`crates/bevy_gltf/src/loader/mod.rs`) — 142 outbound dependencies
5. **mod.rs** (`crates/bevy_render/src/render_resource/mod.rs`) — 140 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `ktx2_dfd_header_to_texture_format` (@ `crates/bevy_image/src/ktx2.rs`) -> Impact: **394.1** | LOC: 721
  * *Intent:* /// Reads the [`TextureFormat`] from a KTX2 data format descriptor header. /// /// # Errors /// /// Returns an error for invalid or unsupported textur...
- `prepare_lights` (@ `crates/bevy_pbr/src/render/light.rs`) -> Impact: **344.8** | LOC: 983
- `load_gltf` (@ `crates/bevy_gltf/src/loader/mod.rs`) -> Impact: **332.9** | LOC: 933
  * *Intent:* /// Loads an entire glTF file.
- `assign_objects_to_clusters` (@ `crates/bevy_light/src/cluster/assign.rs`) -> Impact: **316.6** | LOC: 640
  * *Intent:* /// Clusters point lights, spot lights, light probes, and decals. /// /// NOTE: Run this before `update_point_light_frusta`!
- `load_node` (@ `crates/bevy_gltf/src/loader/mod.rs`) -> Impact: **223.9** | LOC: 399
  * *Intent:* /// Loads a glTF node.
- `example_control_system` (@ `examples/3d/transmission.rs`) -> Impact: **205.9** | LOC: 218
- `prepare_uinodes` (@ `crates/bevy_ui_render/src/lib.rs`) -> Impact: **203.5** | LOC: 404
- `derive_as_bind_group` (@ `crates/bevy_render/macros/src/as_bind_group.rs`) -> Impact: **202.7** | LOC: 1056
- `changed_windows` (@ `crates/bevy_winit/src/system.rs`) -> Impact: **193.6** | LOC: 295
  * *Intent:* /// Propagates changes from [`Window`] entities to the [`winit`] backend. /// /// # Notes /// /// - [`Window::present_mode`] and [`Window::composite_a...
- `pointer_events` (@ `crates/bevy_picking/src/events.rs`) -> Impact: **188.7** | LOC: 529
  * *Intent:* /// the case of [`Enter`] → [`Leave`], shared parent entities will not receive [`Enter`] /// or [`Leave`]. /// /// Both [`Click`] and [`Release`] targ...

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `examples/3d` | 66 | 7387.32 | 15.92% | 0.0% |
| `crates/bevy_pbr/src/render` | 9 | 4616.28 | 8.08% | 13.84% |
| `crates/bevy_ecs/src/query` | 11 | 3598.12 | 7.59% | 50.57% |
| `crates/bevy_reflect/src` | 24 | 3301.82 | 4.78% | 60.71% |
| `crates/bevy_ecs/src/entity` | 13 | 3078.98 | 7.5% | 84.78% |
| `crates/bevy_asset/src` | 16 | 2823.56 | 6.51% | 33.89% |
| `crates/bevy_ecs/src/system` | 15 | 2814.08 | 8.85% | 81.31% |
| `crates/bevy_pbr/src` | 14 | 2781.78 | 6.82% | 25.97% |
| `crates/bevy_ecs/src/schedule` | 10 | 2727.72 | 7.77% | 41.17% |
| `crates/bevy_ui_render/src` | 10 | 2417.02 | 10.08% | 37.37% |

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
- `crates/bevy_ecs/src/world/entity_access/mod.rs` -> **68** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `28175` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `crates/bevy_ecs/macros/src/event.rs` (RUST) -> Cumulative Risk: **673.21**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 151.68 | **LOC:** 209 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9244%), State Flux (98.712%), Documentation (87.5%)
- **Heaviest Functions:** `derive_entity_event` (Impact: 42.0), `derive_event` (Impact: 17.8), `get_event_target_field` (Impact: 17.7)

### 2. `crates/bevy_gizmos/src/gizmos.rs` (RUST) -> Cumulative Risk: **667.96**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 331.7 | **LOC:** 953 | **CtrlFlow:** 5.5% | **Authorship Centralization:** 40.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (98.1405%), State Flux (95.7796%), Verification (80.0%)
- **Heaviest Functions:** `get_param` (Impact: 10.7), `queue` (Impact: 6.8), `linestrip_gradient` (Impact: 6.6)

### 3. `crates/bevy_reflect/src/impls/indexmap.rs` (RUST) -> Cumulative Risk: **663.8**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 214.04 | **LOC:** 500 | **CtrlFlow:** 7.6% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9999%), Concurrency (90.8487%)
- **Heaviest Functions:** `from_reflect` (Impact: 7.7), `reflect_clone` (Impact: 6.2), `from_reflect` (Impact: 6.2)

### 4. `crates/bevy_pbr/src/render/mesh.rs` (RUST) -> Cumulative Risk: **644.96**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 1777.06 | **LOC:** 4358 | **CtrlFlow:** 9.2% | **Authorship Centralization:** 30.3%
- **Primary Risk Drivers:** Spec Match (100.0%), Api Exposure (98.2692%), State Flux (96.8649%), Churn (89.25%)
- **Heaviest Functions:** `specialize` (Impact: 178.4), `collect_meshes_for_gpu_building` (Impact: 76.1), `extract_meshes_for_gpu_building` (Impact: 59.1)

### 5. `crates/bevy_render/src/render_resource/uniform_buffer.rs` (RUST) -> Cumulative Risk: **642.02**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 169.36 | **LOC:** 403 | **CtrlFlow:** 10.1% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9873%), State Flux (96.5982%), Api Exposure (89.8239%)
- **Heaviest Functions:** `get_writer` (Impact: 22.8), `write_buffer` (Impact: 12.8), `write_buffer` (Impact: 10.7)

### 6. `crates/bevy_reflect/src/impls/smallvec.rs` (RUST) -> Cumulative Risk: **641.37**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 159.54 | **LOC:** 240 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9994%), Api Exposure (81.155%)
- **Heaviest Functions:** `from_reflect` (Impact: 6.2), `get` (Impact: 5.5), `get_mut` (Impact: 5.5)

### 7. `crates/bevy_transform/src/systems.rs` (RUST) -> Cumulative Risk: **638.68**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 557.92 | **LOC:** 1174 | **CtrlFlow:** 10.5% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9952%), State Flux (85.7071%), Verification (80.0%)
- **Heaviest Functions:** `mark_dirty_trees` (Impact: 129.3), `propagate_descendants_unchecked` (Impact: 33.6), `propagation_worker` (Impact: 31.6)

### 8. `crates/bevy_ui_render/src/lib.rs` (RUST) -> Cumulative Risk: **634.83**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 859.02 | **LOC:** 1820 | **CtrlFlow:** 9.9% | **Authorship Centralization:** 35.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (80.6433%), Verification (80.0%), Documentation (75.0%)
- **Heaviest Functions:** `prepare_uinodes` (Impact: 203.5), `extract_uinode_borders` (Impact: 44.7), `extract_text_shadows` (Impact: 43.9)

### 9. `crates/bevy_reflect/src/impls/macros/set.rs` (RUST) -> Cumulative Risk: **628.81**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 113.3 | **LOC:** 208 | **CtrlFlow:** 8.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (94.2676%), Verification (80.0%)
- **Heaviest Functions:** `from_reflect` (Impact: 6.3), `reflect_clone` (Impact: 4.7), `remove` (Impact: 4.0)

### 10. `crates/bevy_ecs/src/spawn.rs` (RUST) -> Cumulative Risk: **621.79**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 223.04 | **LOC:** 776 | **CtrlFlow:** 3.9% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Verification (80.0%), Documentation (75.6098%)
- **Heaviest Functions:** `apply_effect` (Impact: 4.3), `spawn` (Impact: 4.2), `apply_effect` (Impact: 4.0)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `crates/bevy_pbr/src/render/mesh.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1777.06 | **LOC:** 4358 | **CtrlFlow:** 9.2% | **Authorship Centralization:** 30.3%
- **Risk Profile:** Cognitive Load (17.2571%), Tech Debt (15.3306%)
**Top Internal Functions/Classes:**
  * `specialize` (Impact: 178.4)
  * `collect_meshes_for_gpu_building` (Impact: 76.1)
    * *Intent:* /// Creates the [`RenderMeshInstanceGpu`]s and [`MeshInputUniform`]s when GPU
  * `extract_meshes_for_gpu_building` (Impact: 59.1)
    * *Intent:* /// Extracts meshes from the main world into the render world and queues /// [`MeshInputUniform`]s t...
  * `render` (Impact: 56.7)
  * `check_views_need_specialization` (Impact: 53.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 168 instances
* *High Risk Execution (weighted view):* 2
* *Concurrency (weighted view):* 17
* *State Mutation (weighted view):* 551
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 314`, `structural_boundaries: 543`, `args: 120`, `func_start: 78`, `class_start: 42`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 3`, `state_mutation: 215`, `dead_code: 4`, `planned_debt: 4`, `fragile_debt: 4`, `duplicate_logic: 4`
* *Architecture:* `api: 139`, `concurrency: 7`, `import: 50`
* *Defense:* `safety: 57`, `doc: 403`, `test: 7`, `sync_locks: 2`, `immutability_locks: 107`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.456
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` *, Affine3Ext, AssetId, AssetIndex, AssetServer, BaseMeshPipelineKey, CORE_3D_DEPTH_FORMAT, Camera...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_pbr/src/render/light.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1186.98 | **LOC:** 2518 | **CtrlFlow:** 10.6% | **Authorship Centralization:** 39.1%
- **Risk Profile:** Cognitive Load (17.6617%), Tech Debt (23.5991%)
**Top Internal Functions/Classes:**
  * `prepare_lights` (Impact: 344.8)
  * `queue_shadows` (Impact: 124.3)
    * *Intent:* /// For each shadow cascade, iterates over all the meshes "visible" from it and /// adds them to [`B...
  * `extract_lights` (Impact: 111.8)
  * `specialize_shadows` (Impact: 108.6)
  * `shadow_pass` (Impact: 29.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 62 instances
* *State Mutation (weighted view):* 223
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 223`, `structural_boundaries: 363`, `args: 64`, `func_start: 26`, `class_start: 24`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 99`, `dead_code: 7`, `planned_debt: 5`, `unreferenced_by_name: 16`
* *Architecture:* `api: 96`, `import: 34`
* *Defense:* `safety: 30`, `doc: 49`, `test: 1`, `immutability_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.456
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` AmbientLight, CUBE_MAP_FACES, CascadeShadowConfig, Cascades, CascadesFrusta, ClusterableObjectType, CubeMapFace, CubemapFrusta...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_gltf/src/loader/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1046.64 | **LOC:** 2931 | **CtrlFlow:** 9.2% | **Authorship Centralization:** 27.3%
- **Risk Profile:** Cognitive Load (12.1543%), Tech Debt (25.3847%)
**Top Internal Functions/Classes:**
  * `load_gltf` (Impact: 332.9)
    * *Intent:* /// Loads an entire glTF file.
  * `load_node` (Impact: 223.9)
    * *Intent:* /// Loads a glTF node.
  * `load_image` (Impact: 31.6)
    * *Intent:* /// Loads a glTF texture as a bevy [`Image`] and returns it together with its label.
  * `load_material` (Impact: 25.9)
    * *Intent:* /// Loads a glTF material as a bevy [`GltfMaterial`] and returns the label and material.
  * `load_buffers` (Impact: 19.4)
    * *Intent:* /// Loads the raw glTF buffer data for a specific glTF file.
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 49 instances
* *Concurrency (weighted view):* 30
* *State Mutation (weighted view):* 171
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 234`, `structural_boundaries: 545`, `args: 112`, `func_start: 38`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 34`, `high_risk_execution: 4`, `state_mutation: 73`, `dead_code: 14`, `planned_debt: 9`, `duplicate_logic: 3`, `unreferenced_by_name: 12`
* *Architecture:* `io: 2`, `api: 29`, `concurrency: 20`, `import: 42`
* *Defense:* `safety: 87`, `doc: 86`, `test: 55`, `sync_locks: 5`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.456
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AnimatedBy, AnimationTargetId, AssetApp, AssetLoadError, AssetLoader, AssetPath, AssetPlugin, AssetServer...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_asset/src/processor/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 975.72 | **LOC:** 1865 | **CtrlFlow:** 13.5% | **Authorship Centralization:** 85.7%
- **Risk Profile:** Cognitive Load (41.5883%), Tech Debt (14.6331%)
**Top Internal Functions/Classes:**
  * `process_asset_internal` (Impact: 72.7)
  * `initialize` (Impact: 50.5)
    * *Intent:* /// Populates the initial view of each asset by scanning the unprocessed and processed asset folders...
  * `handle_asset_source_event` (Impact: 41.0)
  * `validate_transaction_log_and_recover` (Impact: 40.0)
  * `rename` (Impact: 25.7)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.456
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` AssetAction, AssetActionMinimal, AssetHash, AssetLoadError, AssetMeta, AssetMetaCheck, AssetMetaDyn, AssetMetaMinimal...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_ecs/src/query/fetch.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 942.9 | **LOC:** 4326 | **CtrlFlow:** 8.3% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (7.1083%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `fetch` (Impact: 12.5)
  * `derive_release_state` (Impact: 12.2)
  * `test_contiguous_query_data` (Impact: 10.1)
  * `any_of_contiguous_test` (Impact: 7.9)
  * `init_fetch` (Impact: 7.8)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.456
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Access, Archetypes, ComponentId, ComponentTicksRef, Components, ContiguousComponentTicksMut, ContiguousComponentTicksRef, ContiguousMut...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_mesh/src/mesh.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 937.9 | **LOC:** 3177 | **CtrlFlow:** 9.7% | **Authorship Centralization:** 14.3%
- **Risk Profile:** Cognitive Load (7.4239%), Tech Debt (10.4194%)
**Top Internal Functions/Classes:**
  * `triangles` (Impact: 28.2)
    * *Intent:* /// Get a list of this Mesh's [triangles] as an iterator if possible. /// /// Returns an error if an...
  * `merge_duplicate_vertices` (Impact: 25.9)
    * *Intent:* /// Remove duplicate vertices and create the index pointing to the unique vertices. /// /// Returns ...
  * `merge` (Impact: 24.4)
    * *Intent:* /// /// Note that attributes of `other` that don't exist on `self` will be ignored. /// /// `Aabb` o...
  * `try_transform_by` (Impact: 19.9)
    * *Intent:* /// Transforms the vertex positions, normals, and tangents of the mesh in place by the given [`Trans...
  * `try_scale_by` (Impact: 17.9)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.456
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` *, FourIterators, HashMap, Hasher, Indices, MeshAttributeData, MeshBuilder, MeshTrianglesError...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_ecs/src/world/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 930.3 | **LOC:** 4641 | **CtrlFlow:** 5.3% | **Authorship Centralization:** 18.2%
- **Risk Profile:** Cognitive Load (5.1522%), Tech Debt (87.0766%)
**Top Internal Functions/Classes:**
  * `try_insert_batch_with_caller` (Impact: 37.0)
    * *Intent:* /// Split into a new function so we can differentiate the calling location. /// /// This can be call...
  * `try_resource_scope` (Impact: 26.4)
    * *Intent:* /// Temporarily removes the requested resource from this [`World`] if it exists, runs custom user co...
  * `insert_batch_with_caller` (Impact: 22.4)
    * *Intent:* /// Split into a new function so we can differentiate the calling location. /// /// This can be call...
  * `drop` (Impact: 10.3)
  * `remove_resource_by_id` (Impact: 9.2)
    * *Intent:* /// Removes the resource of a given type, if it exists. /// Returns `true` if the resource is succes...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 8 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 14 instances
* *High Risk Execution (weighted view):* 8
* *Concurrency (weighted view):* 29
* *State Mutation (weighted view):* 61
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 116`, `structural_boundaries: 566`, `args: 246`, `func_start: 191`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 38`, `high_risk_execution: 16`, `state_mutation: 33`, `dead_code: 230`, `planned_debt: 3`, `unreferenced_by_name: 63`
* *Architecture:* `api: 187`, `concurrency: 24`, `import: 32`
* *Defense:* `safety: 21`, `doc: 1921`, `test: 117`, `sync_locks: 10`, `immutability_locks: 1`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.456
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ADD, Archetypes, AtomicU32, BundleId, BundleInfo, BundleInserter, BundleSpawner, Bundles...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_pbr/src/prepass/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 888.84 | **LOC:** 1503 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 37.5%
- **Risk Profile:** Cognitive Load (39.0419%), Tech Debt (14.8266%)
**Top Internal Functions/Classes:**
  * `specialize_prepass_material_meshes` (Impact: 164.3)
  * `queue_prepass_material_meshes` (Impact: 149.3)
  * `specialize` (Impact: 145.2)
  * `check_prepass_views_need_specialization` (Impact: 17.9)
  * `prepare_previous_view_uniforms` (Impact: 11.9)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.456
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` *, AlphaMode, AssetServer, Camera3d, DeferredAlphaMaskDrawFunction, DeferredFragmentShader, DeferredOpaqueDrawFunction, DeferredVertexShader...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_ui_render/src/lib.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 859.02 | **LOC:** 1820 | **CtrlFlow:** 9.9% | **Authorship Centralization:** 35.0%
- **Risk Profile:** Cognitive Load (10.6961%), Tech Debt (8.0582%)
**Top Internal Functions/Classes:**
  * `prepare_uinodes` (Impact: 203.5)
  * `extract_uinode_borders` (Impact: 44.7)
  * `extract_text_shadows` (Impact: 43.9)
  * `extract_uinode_images` (Impact: 38.4)
  * `extract_text_decorations` (Impact: 36.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 9 instances
* *Amplified Cascading Flux:* 40 instances
* *Concurrency (weighted view):* 59
* *State Mutation (weighted view):* 160
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 151`, `structural_boundaries: 234`, `args: 64`, `func_start: 17`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 80`, `dead_code: 12`, `planned_debt: 2`
* *Architecture:* `api: 94`, `concurrency: 14`, `import: 36`
* *Defense:* `safety: 15`, `doc: 108`, `immutability_locks: 28`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.456
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AddRenderCommand, AssetId, Assets, BorderColor, BoxShadowSamples, CalculatedClip, Camera2d, Camera3d...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_ecs/src/schedule/schedule.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 823.94 | **LOC:** 2639 | **CtrlFlow:** 7.4% | **Authorship Centralization:** 62.5%
- **Risk Profile:** Cognitive Load (6.5944%), Tech Debt (33.2315%)
**Top Internal Functions/Classes:**
  * `build_schedule` (Impact: 39.3)
    * *Intent:* /// Builds an execution-optimized [`SystemSchedule`] from the current state /// of the graph. Also r...
  * `process_configs` (Impact: 38.3)
    * *Intent:* /// Adds the config nodes to the graph. /// /// `collect_nodes` controls whether the `NodeId`s of th...
  * `update_schedule` (Impact: 32.5)
    * *Intent:* /// Updates the `SystemSchedule` from the `ScheduleGraph`.
  * `get_node_name_inner` (Impact: 25.6)
  * `build_schedule_inner` (Impact: 20.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 30 instances
* *High Risk Execution (weighted view):* 3
* *State Mutation (weighted view):* 118
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 143`, `structural_boundaries: 541`, `args: 257`, `func_start: 138`, `class_start: 31`
* *Risk/State:* `safety_bypasses: 24`, `high_risk_execution: 5`, `state_mutation: 58`, `dead_code: 22`, `duplicate_logic: 14`
* *Architecture:* `api: 110`, `import: 22`
* *Defense:* `safety: 12`, `doc: 313`, `test: 119`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.456
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Components, DefaultErrorHandler, Direction::Incoming, HashSet, IndexSet, IntoScheduleConfigs, IntoSystemSet, Outgoing...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_pbr/src/wireframe.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 820.08 | **LOC:** 1644 | **CtrlFlow:** 12.0% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (10.7782%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `specialize_wireframes` (Impact: 140.7)
  * `queue_wireframes` (Impact: 92.7)
  * `prepare_wireframe_wide_bind_groups` (Impact: 71.9)
  * `render` (Impact: 36.9)
  * `render` (Impact: 18.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 39 instances
* *State Mutation (weighted view):* 129
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 162`, `structural_boundaries: 278`, `args: 59`, `func_start: 41`, `class_start: 29`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 51`, `dead_code: 2`
* *Architecture:* `api: 83`, `import: 16`
* *Defense:* `safety: 22`, `doc: 81`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.456
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` *, AsAssetId, Asset, AssetApp, AssetEventSystems, AssetId, AssetServer, Assets...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_asset/src/server/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 809.76 | **LOC:** 2245 | **CtrlFlow:** 8.6% | **Authorship Centralization:** 76.9%
- **Risk Profile:** Cognitive Load (12.8779%), Tech Debt (94.9797%)
**Top Internal Functions/Classes:**
  * `load_internal` (Impact: 66.6)
    * *Intent:* /// Performs an async asset load. /// /// `input_handle` must only be [`Some`] if `should_load` was ...
  * `get_meta_loader_and_reader` (Impact: 45.5)
  * `handle_internal_asset_events` (Impact: 34.4)
    * *Intent:* /// A system that manages internal [`AssetServer`] events, such as finalizing asset loads.
  * `load_folder_internal` (Impact: 32.2)
  * `load_folder` (Impact: 26.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 11 instances
* *Concurrency (weighted view):* 101
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 54
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 138`, `structural_boundaries: 364`, `args: 130`, `func_start: 91`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 32`, `dead_code: 12`, `planned_debt: 6`, `duplicate_logic: 9`, `unreferenced_by_name: 33`
* *Architecture:* `io: 1`, `api: 100`, `concurrency: 86`, `import: 18`
* *Defense:* `safety: 32`, `doc: 347`, `sync_locks: 5`, `immutability_locks: 2`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.456
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Asset, AssetActionMinimal, AssetEvent, AssetHandleProvider, AssetId, AssetIndex, AssetLoadFailedEvent, AssetMetaCheck...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_image/src/ktx2.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 804.12 | **LOC:** 1542 | **CtrlFlow:** 21.9% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (12.8699%), Tech Debt (11.0986%)
**Top Internal Functions/Classes:**
  * `ktx2_dfd_header_to_texture_format` (Impact: 394.1)
    * *Intent:* /// Reads the [`TextureFormat`] from a KTX2 data format descriptor header. /// /// # Errors /// /// ...
  * `ktx2_buffer_to_image` (Impact: 113.8)
    * *Intent:* /// Converts KTX2 bytes to a bevy [`Image`] using the given compressed format support. /// /// # Err...
  * `ktx2_format_to_texture_format` (Impact: 101.4)
    * *Intent:* /// Converts a KTX2 texture format identifier to a [`TextureFormat`]. /// /// # Errors /// /// Retur...
  * `get_transcoded_formats` (Impact: 52.0)
    * *Intent:* /// Determines an appropriate wgpu-compatible format based on compressed format support, and a /// b...
  * `sample_information_to_data_type` (Impact: 22.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 74
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 314`, `structural_boundaries: 157`, `args: 30`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 32`, `planned_debt: 3`, `fragile_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 2`, `api: 5`, `import: 10`
* *Defense:* `safety: 3`, `doc: 23`, `test: 23`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.456
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AstcChannel, ColorModel, DfdBlockBasic, DfdBlockHeaderBasic, DfdHeader, Extent3d, Header, Image...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_render/src/batching/gpu_preprocessing.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 778.16 | **LOC:** 2382 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 36.4%
- **Risk Profile:** Cognitive Load (15.6321%), Tech Debt (37.2245%)
**Top Internal Functions/Classes:**
  * `batch_and_prepare_binned_render_phase` (Impact: 79.3)
    * *Intent:* /// Creates batches for a render phase that uses bins.
  * `batch_and_prepare_sorted_render_phase` (Impact: 64.2)
    * *Intent:* /// Batch the items in a sorted render phase, when GPU instance buffer building /// is in use. This ...
  * `write_batched_instance_buffers` (Impact: 24.5)
    * *Intent:* /// A system that writes all instance buffers to the GPU.
  * `from_world` (Impact: 19.5)
  * `get_or_create_work_item_buffer` (Impact: 16.2)
    * *Intent:* /// Returns the set of work item buffers for the given view, first creating it /// if necessary. ///...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 32 instances
* *Concurrency (weighted view):* 62
* *State Mutation (weighted view):* 142
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 122`, `structural_boundaries: 368`, `args: 80`, `func_start: 73`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 78`, `dead_code: 6`, `duplicate_logic: 5`, `unreferenced_by_name: 19`
* *Architecture:* `api: 111`, `concurrency: 42`, `import: 21`
* *Defense:* `safety: 24`, `doc: 489`, `test: 7`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.456
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AtomicRawBufferVec, AtomicSparseBufferVec, BinnedRenderPhaseBatch, BinnedRenderPhaseBatchSet, BinnedRenderPhaseBatchSets, Buffer, BufferUsages, CachedRenderPipelinePhaseItem...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_ui/src/ui_node.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 723.02 | **LOC:** 3213 | **CtrlFlow:** 4.0% | **Authorship Centralization:** 60.0%
- **Risk Profile:** Cognitive Load (3.8325%), Tech Debt (91.456%)
**Top Internal Functions/Classes:**
  * `invalid_grid_placement_values` (Impact: 13.8)
  * `contains_point` (Impact: 13.1)
    * *Intent:* // Returns true if `point` within the node. // // Matches the sdf function in `ui.wgsl` that is used...
  * `resolve_clip_rect` (Impact: 9.3)
    * *Intent:* /// Resolve the node's clipping rect in local space
  * `resolve_single_corner` (Impact: 7.3)
    * *Intent:* /// Resolve the border radius for a single corner from the given context values. /// Returns the rad...
  * `get` (Impact: 6.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 46
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 228`, `args: 188`, `func_start: 168`, `class_start: 45`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 34`, `dead_code: 12`, `duplicate_logic: 24`, `unreferenced_by_name: 36`
* *Architecture:* `api: 283`, `import: 19`
* *Defense:* `safety: 3`, `doc: 943`, `test: 47`, `immutability_locks: 27`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.456
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` BLUE, Camera, Camera2d, Color, DerefMut, FocusPolicy, Rect, RenderTarget...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_input/src/gamepad.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 719.08 | **LOC:** 2979 | **CtrlFlow:** 5.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.7932%), Tech Debt (9.3819%)
**Top Internal Functions/Classes:**
  * `gamepad_event_processing_system` (Impact: 55.2)
    * *Intent:* /// Consumes [`RawGamepadEvent`] events, filters them using their [`GamepadSettings`] and if success...
  * `new` (Impact: 39.2)
    * *Intent:* /// + `livezone_upperbound` - the value above which inputs will be rounded up to 1.0. /// + `thresho...
  * `get_axis_position_from_value` (Impact: 22.0)
  * `gamepad_connection_system` (Impact: 15.9)
    * *Intent:* /// Handles [`GamepadConnectionEvent`]s events. /// /// On connection, adds the components represent...
  * `clamp` (Impact: 14.4)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.456
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AxisSettings, AxisSettingsError, ButtonAxisSettings, ButtonInput, ButtonSettings, ButtonSettingsError, ButtonState, Disconnected...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_remote/src/builtin_methods.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 711.62 | **LOC:** 1877 | **CtrlFlow:** 15.9% | **Authorship Centralization:** 11.1%
- **Risk Profile:** Cognitive Load (5.8214%), Tech Debt (28.9427%)
**Top Internal Functions/Classes:**
  * `process_remote_get_components_watching_request` (Impact: 56.9)
    * *Intent:* /// Handles a `world.get_components+watch` request coming from a client.
  * `process_remote_query_request` (Impact: 46.2)
    * *Intent:* /// Handles a `world.query` request coming from a client.
  * `process_remote_list_components_watching_request` (Impact: 38.2)
    * *Intent:* /// Handles a `world.list_components+watch` request coming from a client.
  * `process_remote_mutate_components_request` (Impact: 27.2)
    * *Intent:* /// Handles a `world.mutate_components` request coming from a client. /// /// This method allows you...
  * `serialize_components` (Impact: 25.7)
    * *Intent:* /// Serializes the specified components for an entity. /// The iterator yields ([`TypeId`], Option<[...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 55
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 209`, `structural_boundaries: 331`, `args: 82`, `func_start: 43`, `class_start: 30`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 23`, `dead_code: 3`, `unreferenced_by_name: 21`
* *Architecture:* `api: 111`, `import: 15`
* *Defense:* `safety: 28`, `doc: 284`, `test: 10`, `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.456
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` BrpError, BrpResult, Deserialize, EntityWorldMut, FilteredEntityRef, GetPath, JsonSchemaBevyType, Local...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_reflect/src/lib.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 709.74 | **LOC:** 4268 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 18.2%
- **Risk Profile:** Cognitive Load (4.5353%), Tech Debt (9.0422%)
**Top Internal Functions/Classes:**
  * `reflect_type_info` (Impact: 15.4)
  * `reflect_complex_patch` (Impact: 8.7)
  * `should_contain_docs` (Impact: 8.0)
  * `should_reflect_debug` (Impact: 6.9)
  * `custom_cmp` (Impact: 5.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 125
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 907`, `args: 132`, `func_start: 129`, `class_start: 185`
* *Risk/State:* `safety_bypasses: 159`, `high_risk_execution: 3`, `state_mutation: 115`, `dead_code: 2`, `planned_debt: 11`
* *Architecture:* `api: 186`, `import: 76`
* *Defense:* `safety: 12`, `doc: 635`, `test: 374`, `sync_locks: 6`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.456
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` *, ::alloc::
            borrow::Cow, ::glam::quat, ::serde::de::DeserializeSeed, Deserialize, Deserializer, Formatter, FromReflect...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_pbr/src/render/gpu_preprocess.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 697.26 | **LOC:** 2552 | **CtrlFlow:** 7.8% | **Authorship Centralization:** 36.4%
- **Risk Profile:** Cognitive Load (3.9721%), Tech Debt (12.0278%)
**Top Internal Functions/Classes:**
  * `early_gpu_preprocess` (Impact: 99.6)
  * `prepare_preprocess_bind_groups` (Impact: 57.8)
    * *Intent:* /// A system that attaches the mesh uniform buffers to the bind groups for the /// variants of the m...
  * `run_build_indirect_parameters` (Impact: 43.3)
  * `late_gpu_preprocess` (Impact: 31.1)
  * `specialize` (Impact: 28.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 61
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 161`, `structural_boundaries: 268`, `args: 27`, `func_start: 39`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 23`, `dead_code: 3`, `duplicate_logic: 3`, `unreferenced_by_name: 3`
* *Architecture:* `api: 48`, `import: 16`
* *Defense:* `safety: 13`, `doc: 218`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.456
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` BindGroup, BindGroupEntries, BindGroupLayoutDescriptor, BindingResource, Buffer, BufferBinding, BufferVec, CachedComputePipelineId...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_ecs/src/entity/clone_entities.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 667.14 | **LOC:** 2608 | **CtrlFlow:** 5.2% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (8.4159%), Tech Debt (79.8767%)
**Top Internal Functions/Classes:**
  * `clone_entity_internal` (Impact: 60.1)
    * *Intent:* /// Clones and inserts components from the `source` entity into the entity mapped by `mapper` from `...
  * `clone_components` (Impact: 37.0)
  * `filter_allow` (Impact: 21.8)
    * *Intent:* /// Allows a component through the filter, also allow required components if /// [`Self::attach_requ...
  * `clone_entity_mapped_internal` (Impact: 19.3)
  * `clone_components` (Impact: 16.9)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.456
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` BundleRemover, Children, ComponentCloneBehavior, ComponentCloneFn, ComponentId, ComponentInfo, Entity, EntityAllocator...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_ecs/src/system/system_param.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 664.58 | **LOC:** 3013 | **CtrlFlow:** 6.4% | **Authorship Centralization:** 22.2%
- **Risk Profile:** Cognitive Load (6.0831%), Tech Debt (99.9997%)
**Top Internal Functions/Classes:**
  * `init_access` (Impact: 9.9)
  * `get_param` (Impact: 9.8)
  * `init_access` (Impact: 7.9)
  * `init_access` (Impact: 7.9)
  * `get_param` (Impact: 7.9)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.456
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ComponentTicksRef, Components, DeferredWorld, DerefMut, Display, EntityAllocator, FilteredAccess, FilteredAccessSet...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_asset/src/lib.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 649.96 | **LOC:** 3073 | **CtrlFlow:** 5.2% | **Authorship Centralization:** 63.6%
- **Risk Profile:** Cognitive Load (4.892%), Tech Debt (27.816%)
**Top Internal Functions/Classes:**
  * `load_dependencies` (Impact: 26.5)
  * `load_error_events` (Impact: 19.8)
    * *Intent:* /// Tests that `AssetLoadFailedEvent<A>` events are emitted and can be used to retry failed assets.
  * `asset_load_error_event_handler` (Impact: 18.6)
  * `load` (Impact: 13.0)
  * `load_folder` (Impact: 12.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 11 instances
* *Concurrency (weighted view):* 39
* *State Mutation (weighted view):* 46
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 121`, `structural_boundaries: 668`, `args: 137`, `func_start: 98`, `class_start: 40`
* *Risk/State:* `safety_bypasses: 65`, `high_risk_execution: 9`, `state_mutation: 24`, `planned_debt: 3`, `duplicate_logic: 9`
* *Architecture:* `io: 9`, `api: 97`, `concurrency: 29`, `import: 40`
* *Defense:* `safety: 11`, `doc: 264`, `test: 191`, `sync_locks: 3`, `immutability_locks: 9`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.456
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Asset, AssetApp, AssetEvent, AssetId, AssetLoadError, AssetLoadFailedEvent, AssetMode, AssetPath...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_animation/src/lib.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 623.18 | **LOC:** 1706 | **CtrlFlow:** 9.3% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (9.7288%), Tech Debt (7.8859%)
**Top Internal Functions/Classes:**
  * `animate_targets` (Impact: 103.0)
    * *Intent:* /// A system that modifies animation targets (e.g. bones in a skinned mesh) /// according to the cur...
  * `trigger_untargeted_animation_events` (Impact: 28.8)
    * *Intent:* /// A system that triggers untargeted animation events for the currently-playing animations.
  * `from_animation` (Impact: 27.8)
  * `update` (Impact: 19.6)
    * *Intent:* /// Update the animation given the delta time and the duration of the clip being played.
  * `advance_animations` (Impact: 17.5)
    * *Intent:* /// A system that advances the time for all playing animations.
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 17 instances
* *Concurrency (weighted view):* 18
* *State Mutation (weighted view):* 81
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 111`, `structural_boundaries: 285`, `args: 110`, `func_start: 85`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 47`, `dead_code: 2`, `planned_debt: 1`
* *Architecture:* `api: 89`, `concurrency: 8`, `import: 24`
* *Defense:* `safety: 10`, `doc: 302`, `test: 12`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.456
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` AnimationClip, AnimationGraphAssetLoader, AnimationNodeIndex, AnimationPlayer, AnimationPlugin, AnimationTargetId, App, AssetApp...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_pbr/src/material.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 619.14 | **LOC:** 1782 | **CtrlFlow:** 8.5% | **Authorship Centralization:** 31.8%
- **Risk Profile:** Cognitive Load (8.6533%), Tech Debt (9.9379%)
**Top Internal Functions/Classes:**
  * `queue_material_meshes` (Impact: 127.1)
    * *Intent:* /// For each view, iterates over all the meshes visible from that view and adds /// them to [`Binned...
  * `specialize_material_meshes` (Impact: 90.4)
  * `prepare_asset` (Impact: 29.0)
  * `specialize` (Impact: 20.4)
  * `render` (Impact: 16.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 29 instances
* *State Mutation (weighted view):* 105
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 115`, `structural_boundaries: 264`, `args: 57`, `func_start: 47`, `class_start: 39`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 47`, `dead_code: 5`, `planned_debt: 8`
* *Architecture:* `api: 79`, `import: 34`
* *Defense:* `safety: 14`, `doc: 225`, `immutability_locks: 4`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.456
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Asset, AssetEventSystems, AssetId, AssetServer, Assets, DerefMut, DirtySpecializations, ErasedMaterialPipelineKey...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/bevy_math/src/primitives/dim2.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 617.76 | **LOC:** 2638 | **CtrlFlow:** 4.3% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (3.2922%), Tech Debt (99.605%)
**Top Internal Functions/Classes:**
  * `closest_point` (Impact: 12.1)
    * *Intent:* /// Finds the point on the rhombus that is closest to the given `point`. /// /// If the point is out...
  * `closest_point` (Impact: 9.7)
    * *Intent:* /// Finds the point on the annulus that is closest to the given `point`: /// /// - If the point is o...
  * `winding_order` (Impact: 7.7)
    * *Intent:* /// Get the [`WindingOrder`] of the triangle
  * `perimeter` (Impact: 7.0)
  * `closest_point` (Impact: 6.7)
    * *Intent:* /// Returns the point on the [`Segment2d`] that is closest to the specified `point`.
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 3 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 80`, `structural_boundaries: 266`, `args: 201`, `func_start: 196`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 3`, `state_mutation: 9`, `dead_code: 7`, `planned_debt: 2`, `duplicate_logic: 26`, `unreferenced_by_name: 34`
* *Architecture:* `api: 168`, `import: 15`
* *Defense:* `safety: 3`, `doc: 419`, `test: 96`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.456
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Dir2, FRAC_PI_2, FRAC_PI_3, FloatPow, InvalidDirectionError, Isometry2d, PI, Primitive2d...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `crates/bevy_text/src/text.rs` -> Churn: **81.46%** | Cog Load: 5.5206% | Debt: 98.9347%
- `crates/bevy_ecs/src/system/system_param.rs` -> Churn: **74.52%** | Cog Load: 6.0831% | Debt: 99.9997%
- `crates/bevy_ecs/src/query/fetch.rs` -> Churn: **70.17%** | Cog Load: 7.1083% | Debt: 100.0%
- `crates/bevy_asset/src/server/mod.rs` -> Churn: **66.79%** | Cog Load: 12.8779% | Debt: 94.9797%
- `crates/bevy_ecs/src/system/commands/mod.rs` -> Churn: **64.91%** | Cog Load: 8.3274% | Debt: 99.1891%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `crates/bevy_asset/src/processor/mod.rs` -> **andriyDev** (85.7% isolated ownership) | Magnitude: 975.72
- `crates/bevy_ecs/src/schedule/stepping.rs` -> **Tauan Binato** (100.0% isolated ownership) | Magnitude: 480.2
- `crates/bevy_pbr/src/meshlet/from_mesh.rs` -> **JMS55** (100.0% isolated ownership) | Magnitude: 474.74
- `crates/bevy_mesh/src/primitives/dim2.rs` -> **Chris Biscardi** (100.0% isolated ownership) | Magnitude: 457.46
- `crates/bevy_asset/src/processor/tests.rs` -> **andriyDev** (87.5% isolated ownership) | Magnitude: 357.72

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `crates/bevy_reflect/src/impls/alloc/vec.rs` -> **Severity: 1060.5** (Blast Radius: 10.605 * Doc Risk: 100.0%)
- `crates/bevy_render/src/render_resource/uniform_buffer.rs` -> **Severity: 634.6** (Blast Radius: 9.185 * Doc Risk: 69.0909%)
- `tools/ci/src/commands/format.rs` -> **Severity: 420.5** (Blast Radius: 4.205 * Doc Risk: 100.0%)
- `tools/ci/src/main.rs` -> **Severity: 192.0** (Blast Radius: 1.92 * Doc Risk: 100.0%)
- `crates/bevy_ui_widgets/src/observe.rs` -> **Severity: 122.618** (Blast Radius: 1.686 * Doc Risk: 72.7273%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
