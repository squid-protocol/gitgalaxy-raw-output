# ARCHITECTURAL_BRIEF: zellij
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_rust/zellij` |
| **Timestamp** | `2026-08-07T04:08:59.715347+00:00` |
| **Scan Duration** | `3.53s` |
| **Git Branch** | `main` |
| **Git Commit** | `0532949bbdcee5116e91807ddb45a85d78a2aafc` |
| **Git Remote** | `https://github.com/zellij-org/zellij.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 303 malicious artifacts.

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
| Total Artifacts | 1571 |
| Analyzed Artifacts (Scanned) | 344 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1227 |
| Total LOC | 167246 |
| Volatility Index | 0.006 |
| % Scanned of codebase = | 21.9% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.686 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3691 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.9444 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 5 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUST | 285 | 158502 | 82.8% |
| MARKDOWN | 20 | 0 | 5.8% |
| YAML | 20 | 5172 | 5.8% |
| PROTO | 17 | 3520 | 4.9% |
| JSON | 1 | 50 | 0.3% |
| SHELL | 1 | 2 | 0.3% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.464`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 220 | 64.0% |
| file_cluster_13 | 50 | 14.5% |
| file_cluster_0 | 22 | 6.4% |
| file_cluster_4 | 11 | 3.2% |
| file_cluster_16 | 11 | 3.2% |
| file_cluster_17 | 8 | 2.3% |
| file_cluster_11 | 2 | 0.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 20 | 5.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1227*

**Composition by Extension & Reason:**
- `.snap`: 901x Unsupported Format (.snap), 6x Excluded (Saturation: Line 5 exceeds 500 chars), 4x Excluded (Saturation: Line 6 exceeds 500 chars)
- `no_extension`: 37x Unsupported Format (.undeterminable), 20x Excluded (Binary Format Detected), 13x Excluded (Saturation: Line 49 exceeds 500 chars)
- `.kdl`: 56x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 22x Unsupported Format (.kdl), 6x Excluded (Unsupported Extension: '.kdl')
- `.toml`: 20x Unsupported Format (.toml), 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.toml')
- `.rs`: 18x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.wasm`: 17x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ico`: 2x Excluded (Explicitly Denied Extension: '.ico')
- `.six`: 2x Excluded (Saturation: Line 1 exceeds 500 chars)
- `.bmp`: 2x Excluded (Explicitly Denied Extension: '.bmp')
- `.css`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.bash`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.fish`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 16.3 | 11.7 | 0.0 |
| Error & Exception Exposure | 0.0 | 95.8 | 24.0 | 21.9 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 50.6 | 53.1 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 10.1 | 2.3 | 80.0 |
| API Exposure | 0.0 | 9.2 | 3.2 | 3.3 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 8.3 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 42.8 | 37.5 | 0.0 |
| Commented Logic Exposure | 0.0 | 99.5 | 2.2 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 94.7 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 12.4 | 1.8 | 0.6 | 0.0 |
| Volatility Exposure | 0.0 | 82.1 | 17.6 | 8.8 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 37.5 | 24.8 | 100.0 |
| Hardcoded Payload Artifacts | 0.0 | 89.9 | 0.3 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `zellij-client/src/web_client/unit/web_client_tests.rs` (Hits: 20)
- `zellij-utils/src/consts.rs` (Hits: 15)
- `zellij-utils/src/input/config.rs` (Hits: 14)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **envs.rs** (`zellij-utils/src/envs.rs`) — 7 inbound connections
2. **metadata.rs** (`xtask/src/metadata.rs`) — 4 inbound connections
3. **flags.rs** (`xtask/src/flags.rs`) — 2 inbound connections
4. **session_serialization.rs** (`zellij-utils/src/session_serialization.rs`) — 2 inbound connections
5. **clippy.rs** (`xtask/src/clippy.rs`) — 1 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **plugin_command.rs** (`zellij-utils/src/plugin_api/plugin_command.rs`) — 225 outbound dependencies
2. **zellij_exports.rs** (`zellij-server/src/plugins/zellij_exports.rs`) — 204 outbound dependencies
3. **screen.rs** (`zellij-server/src/screen.rs`) — 104 outbound dependencies
4. **protobuf_conversion.rs** (`zellij-utils/src/ipc/protobuf_conversion.rs`) — 91 outbound dependencies
5. **mod.rs** (`zellij-server/src/tab/mod.rs`) — 88 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `continue_pane_resize_with_mouse` (@ `zellij-server/src/tab/mouse_handler.rs`) -> Impact: **666.2** | LOC: 1070
- `route_action` (@ `zellij-server/src/route.rs`) -> Impact: **655.7** | LOC: 1030
- `force_change_size` (@ `zellij-server/src/panes/grid.rs`) -> Impact: **558.6** | LOC: 1252
- `try_from` (@ `zellij-utils/src/plugin_api/plugin_command.rs`) -> Impact: **523.5** | LOC: 951
- `try_from` (@ `zellij-utils/src/plugin_api/action.rs`) -> Impact: **467.6** | LOC: 952
- `render` (@ `zellij-server/src/panes/tiled_panes/mod.rs`) -> Impact: **458.9** | LOC: 1259
- `populate_run_plugin_if_needed` (@ `zellij-utils/src/input/layout.rs`) -> Impact: **419.6** | LOC: 1360
- `actions_from_cli` (@ `zellij-utils/src/input/actions.rs`) -> Impact: **386.1** | LOC: 1237
- `try_from` (@ `zellij-utils/src/ipc/protobuf_conversion.rs`) -> Impact: **356.0** | LOC: 919
- `set_pane_frames` (@ `zellij-server/src/panes/tiled_panes/mod.rs`) -> Impact: **314.1** | LOC: 1259
  * *Intent:* *self.display_area.borrow(),

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `zellij-server/src/panes` | 12 | 6778.02 | 29.54% | 74.37% |
| `zellij-server/src` | 15 | 5883.5 | 20.02% | 57.11% |
| `zellij-server/src/panes/tiled_panes` | 4 | 4309.68 | 39.03% | 56.25% |
| `zellij-server/src/tab` | 6 | 4285.92 | 28.33% | 61.9% |
| `zellij-utils/src` | 23 | 4113.82 | 10.63% | 64.79% |
| `zellij-utils/src/input` | 13 | 3994.38 | 16.08% | 72.99% |
| `zellij-utils/src/plugin_api` | 27 | 3720.44 | 6.52% | 44.26% |
| `zellij-utils/src/kdl` | 2 | 2637.44 | 18.36% | 18.93% |
| `zellij-server/src/tab/unit` | 3 | 2574.86 | 11.32% | 51.69% |
| `zellij-server/src/plugins` | 9 | 2357.76 | 20.0% | 50.05% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `default-plugins/status-bar/src/tip/consts.rs` -> **100.0%** Exposure
- `zellij-server/src/tab/unit/tab_tests.rs` -> **100.0%** Exposure
- `zellij-tile/src/lib.rs` -> **100.0%** Exposure
- `zellij-utils/src/home.rs` -> **100.0%** Exposure
- `zellij-utils/src/home_windows.rs` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `zellij-client/src/old_config_converter/unit/convert_config_tests.rs` -> **100.0%** Exposure
- `zellij-client/src/old_config_converter/unit/convert_layout_tests.rs` -> **100.0%** Exposure
- `zellij-server/src/ui/components/mod.rs` -> **100.0%** Exposure
- `zellij-server/src/ui/components/nested_list.rs` -> **100.0%** Exposure
- `zellij-server/src/ui/components/table.rs` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `zellij-server/src/unit/screen_tests.rs` -> **138** Orphaned Functions | **8** Duplicates
- `zellij-server/src/tab/unit/tab_integration_tests.rs` -> **128** Orphaned Functions | **9** Duplicates
- `zellij-server/src/tab/mod.rs` -> **123** Orphaned Functions | **4** Duplicates
- `zellij-server/src/panes/unit/grid_tests.rs` -> **113** Orphaned Functions | **6** Duplicates
- `zellij-utils/src/data.rs` -> **72** Orphaned Functions | **42** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`default-plugins/about/src/tips.rs`** -> AI Confidence: **99.39%**
2. **`zellij-utils/src/plugin_api/plugin_command.rs`** -> AI Confidence: **99.39%**
3. **`default-plugins/about/src/main.rs`** -> AI Confidence: **99.31%**
4. **`default-plugins/layout-manager/src/screens/layout_list/mod.rs`** -> AI Confidence: **99.31%**
5. **`default-plugins/session-manager/src/main.rs`** -> AI Confidence: **99.31%**
6. **`default-plugins/strider/src/main.rs`** -> AI Confidence: **99.31%**
7. **`default-plugins/strider/src/state.rs`** -> AI Confidence: **99.31%**
8. **`src/commands.rs`** -> AI Confidence: **99.31%**
9. **`src/main.rs`** -> AI Confidence: **99.31%**
10. **`xtask/src/build.rs`** -> AI Confidence: **99.31%**
11. **`xtask/src/ci.rs`** -> AI Confidence: **99.31%**
12. **`xtask/src/pipelines.rs`** -> AI Confidence: **99.31%**
13. **`zellij-client/src/old_config_converter/convert_old_yaml_files.rs`** -> AI Confidence: **99.31%**
14. **`zellij-server/src/panes/floating_panes/floating_pane_grid.rs`** -> AI Confidence: **99.31%**
15. **`zellij-server/src/panes/grid.rs`** -> AI Confidence: **99.31%**
16. **`zellij-server/src/panes/search.rs`** -> AI Confidence: **99.31%**
17. **`zellij-server/src/panes/terminal_character.rs`** -> AI Confidence: **99.31%**
18. **`zellij-server/src/pty.rs`** -> AI Confidence: **99.31%**
19. **`zellij-server/src/pty_writer.rs`** -> AI Confidence: **99.31%**
20. **`zellij-server/src/route.rs`** -> AI Confidence: **99.31%**
21. **`zellij-server/src/screen.rs`** -> AI Confidence: **99.31%**
22. **`zellij-server/src/tab/mouse_handler.rs`** -> AI Confidence: **99.31%**
23. **`zellij-server/src/tab/swap_layouts.rs`** -> AI Confidence: **99.31%**
24. **`zellij-server/src/thread_bus.rs`** -> AI Confidence: **99.31%**
25. **`zellij-server/src/ui/components/text.rs`** -> AI Confidence: **99.31%**
26. **`zellij-server/src/ui/pane_contents_and_ui.rs`** -> AI Confidence: **99.31%**
27. **`zellij-utils/src/input/layout.rs`** -> AI Confidence: **99.31%**
28. **`zellij-utils/src/input/web_client.rs`** -> AI Confidence: **99.31%**
29. **`zellij-utils/src/ipc/protobuf_conversion.rs`** -> AI Confidence: **99.31%**
30. **`zellij-utils/src/kdl/kdl_layout_parser.rs`** -> AI Confidence: **99.31%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Hardcoded Payload Artifacts
- `zellij-client/src/remote_attach/unit/remote_attach_tests.rs` -> **89.9376%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `4874` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `default-plugins/status-bar/src/tip/data/sync_tab.rs` (RUST) -> Cumulative Risk: **578.18**
- **Archetype:** `file_cluster_8` (Distance: 10.066 IQR)
- **Magnitude:** 35.56 | **LOC:** 77 | **CtrlFlow:** 5.9% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9999%), Cognitive Load (91.0786%), Tech Debt (90.5672%)
- **Heaviest Functions:** `sync_tab_full` (Impact: 2.5), `sync_tab_medium` (Impact: 2.5), `sync_tab_short` (Impact: 2.3)

### 2. `zellij-server/src/terminal_bytes.rs` (RUST) -> Cumulative Risk: **573.7**
- **Archetype:** `file_cluster_4` (Distance: 14.008 IQR)
- **Magnitude:** 63.68 | **LOC:** 101 | **CtrlFlow:** 32.4% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9996%), State Flux (96.7614%), Tech Debt (86.3872%)
- **Heaviest Functions:** `listen` (Impact: 20.5), `async_send_to_screen` (Impact: 8.7), `new` (Impact: 3.1)

### 3. `default-plugins/session-manager/src/ui/mod.rs` (RUST) -> Cumulative Risk: **573.08**
- **Archetype:** `file_cluster_8` (Distance: 11.688 IQR)
- **Magnitude:** 211.82 | **LOC:** 364 | **CtrlFlow:** 28.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9233%), Documentation (87.821%), Verification (80.0%)
- **Heaviest Functions:** `render_search_results` (Impact: 14.9), `render_panes` (Impact: 13.2), `render_tabs` (Impact: 12.9)

### 4. `default-plugins/strider/src/search_view.rs` (RUST) -> Cumulative Risk: **568.04**
- **Archetype:** `file_cluster_13` (Distance: 11.215 IQR)
- **Magnitude:** 94.38 | **LOC:** 136 | **CtrlFlow:** 27.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (96.0128%), Tech Debt (94.9134%)
- **Heaviest Functions:** `render` (Impact: 20.6), `update_search_results` (Impact: 10.8), `move_selection_down` (Impact: 4.2)

### 5. `zellij-client/src/remote_attach/unit/remote_attach_tests.rs` (RUST) -> Cumulative Risk: **553.98**
- **Archetype:** `file_cluster_13` (Distance: 11.318 IQR)
- **Magnitude:** 241.86 | **LOC:** 952 | **CtrlFlow:** 8.3% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (98.3307%), Tech Debt (90.3336%), Secrets Risk (89.9376%)
- **Heaviest Functions:** `handle_ws_terminal` (Impact: 12.8), `handle_ws_control` (Impact: 12.8), `call_attach_to_remote_session` (Impact: 8.5)

### 6. `default-plugins/layout-manager/src/screens/layout_list/search.rs` (RUST) -> Cumulative Risk: **545.72**
- **Archetype:** `file_cluster_8` (Distance: 10.739 IQR)
- **Magnitude:** 107.92 | **LOC:** 198 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.8552%), Verification (80.0%)
- **Heaviest Functions:** `update_filter` (Impact: 22.6), `render_filter_line` (Impact: 8.8), `get_matched_indices_for_visible` (Impact: 7.5)

### 7. `zellij-client/src/web_client/ipc_listener.rs` (RUST) -> Cumulative Risk: **544.94**
- **Archetype:** `file_cluster_4` (Distance: 12.49 IQR)
- **Magnitude:** 137.34 | **LOC:** 98 | **CtrlFlow:** 29.3% | **Authorship Centralization:** 75.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Cognitive Load (99.9903%), State Flux (99.9608%)
- **Heaviest Functions:** `listen_to_web_server_instructions` (Impact: 18.9), `create_webserver_receiver` (Impact: 11.1), `send_webserver_response` (Impact: 8.7)

### 8. `zellij-server/src/panes/selection.rs` (RUST) -> Cumulative Risk: **526.11**
- **Archetype:** `file_cluster_8` (Distance: 10.258 IQR)
- **Magnitude:** 195.88 | **LOC:** 278 | **CtrlFlow:** 51.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (97.0197%), Verification (80.0%)
- **Heaviest Functions:** `add_word_to_position` (Impact: 55.8), `add_line_to_position` (Impact: 27.7), `contains` (Impact: 22.9)

### 9. `zellij-tile/src/ui_components/nested_list.rs` (RUST) -> Cumulative Risk: **524.36**
- **Archetype:** `file_cluster_8` (Distance: 10.39 IQR)
- **Magnitude:** 94.0 | **LOC:** 168 | **CtrlFlow:** 2.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (89.0903%), Verification (80.0%)
- **Heaviest Functions:** `serialize` (Impact: 3.8), `serialize_nested_list_with_coordinates` (Impact: 3.8), `print_nested_list_with_coordinates` (Impact: 3.6)

### 10. `zellij-utils/src/web_server_commands.rs` (RUST) -> Cumulative Risk: **517.83**
- **Archetype:** `file_cluster_13` (Distance: 12.851 IQR)
- **Magnitude:** 105.12 | **LOC:** 126 | **CtrlFlow:** 33.8% | **Authorship Centralization:** 60.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9887%), Tech Debt (61.5454%)
- **Heaviest Functions:** `shutdown_all_webserver_instances` (Impact: 17.1), `discover_webserver_sockets` (Impact: 13.0), `query_webserver_with_response` (Impact: 9.5)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `zellij-server/src/panes/grid.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.4 IQR)
- **Top Global Matches:** file_cluster_8: 14.4, file_cluster_11: 14.428, file_cluster_13: 14.439
- **Magnitude:** 2862.56 | **LOC:** 4798 | **CtrlFlow:** 47.5% | **Authorship Centralization:** 82.6%
- **Risk Profile:** Cognitive Load (43.0283%), Tech Debt (92.9144%)
**Top Internal Functions/Classes:**
  * `force_change_size` (Impact: 558.6)
  * `csi_dispatch` (Impact: 221.1)
  * `osc_dispatch` (Impact: 113.2)
  * `compute_plugin_highlight_selections` (Impact: 55.2)
  * `render` (Impact: 44.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 571`, `structural_boundaries: 630`, `args: 189`, `func_start: 137`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 527`, `dead_code: 6`, `planned_debt: 17`, `fragile_debt: 4`, `duplicate_logic: 4`, `orphaned_logic: 72`
* *Architecture:* `api: 145`, `import: 26`
* *Defense:* `safety: 437`, `doc: 61`, `test: 1`, `immutability_locks: 3`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::panes::terminal_character::
    AnsiCode, std::fmt::Write, std::cell::RefCell, PaletteColor, std::collections::HashMap, zellij_utils::data::HighlightLayer, VecDeque, zellij_utils::
    consts::DEFAULT_SCROLL_BUFFER_SIZE...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zellij-server/src/tab/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.419 IQR)
- **Top Global Matches:** file_cluster_8: 14.419, file_cluster_17: 14.556, file_cluster_11: 14.587
- **Magnitude:** 1887.62 | **LOC:** 6061 | **CtrlFlow:** 45.7% | **Authorship Centralization:** 93.9%
- **Risk Profile:** Cognitive Load (27.1129%), Tech Debt (99.4741%)
**Top Internal Functions/Classes:**
  * `suppress_pane_and_replace_with_pid` (Impact: 67.4)
  * `new_no_preference_pane` (Impact: 55.2)
  * `new_stacked_pane` (Impact: 54.1)
  * `horizontal_split` (Impact: 40.1)
  * `vertical_split` (Impact: 40.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 398`, `structural_boundaries: 473`, `args: 330`, `func_start: 239`, `class_start: 4`
* *Risk/State:* `state_mutation: 337`, `dead_code: 3`, `planned_debt: 25`, `fragile_debt: 3`, `duplicate_logic: 4`, `orphaned_logic: 123`
* *Architecture:* `io: 1`, `api: 91`, `import: 31`
* *Defense:* `safety: 554`, `doc: 5`, `immutability_locks: 3`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Palette, PaletteColor, WebSharing, crate::background_jobs::BackgroundJob, crate::plugins::PluginId, zellij_utils::data::PaneContents, str, PaneResizeState...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zellij-server/src/panes/unit/grid_tests.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.979 IQR)
- **Top Global Matches:** file_cluster_0: 13.979, file_cluster_8: 14.06, file_cluster_17: 14.184
- **Magnitude:** 1850.4 | **LOC:** 5688 | **CtrlFlow:** 7.6% | **Authorship Centralization:** 83.3%
- **Risk Profile:** Cognitive Load (30.2864%), Tech Debt (91.0372%)
**Top Internal Functions/Classes:**
  * `sixel_with_image_scrolling_decsdm` (Impact: 17.6)
  * `cursor_hide_persists_through_alternate_s` (Impact: 11.7)
  * `preserve_background_color_on_resize` (Impact: 11.4)
  * `osc_110_111_reset_pane_default_colors` (Impact: 11.3)
  * `sixel_image_in_alternate_buffer` (Impact: 9.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 126`, `structural_boundaries: 1539`, `args: 173`, `func_start: 149`
* *Risk/State:* `safety_bypasses: 25`, `high_risk_execution: 1`, `state_mutation: 1054`, `dead_code: 1`, `fragile_debt: 3`, `duplicate_logic: 6`, `orphaned_logic: 113`
* *Architecture:* `io: 1`, `api: 20`, `import: 21`
* *Defense:* `safety: 1089`, `test: 304`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::fmt::Write, crate::panes::grid::SixelImageStore, std::cell::RefCell, std::collections::HashMap, zellij_utils::data::HighlightLayer, super::resolve_highlight_colors, Style, position::Position...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zellij-server/src/tab/unit/tab_integration_tests.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.189 IQR)
- **Top Global Matches:** file_cluster_8: 12.189, file_cluster_0: 12.552, file_cluster_13: 12.782
- **Magnitude:** 1658.8 | **LOC:** 14801 | **CtrlFlow:** 1.7% | **Authorship Centralization:** 85.0%
- **Risk Profile:** Cognitive Load (8.9388%), Tech Debt (26.2476%)
**Top Internal Functions/Classes:**
  * `cursor_visible_when_pinned_pane_is_focus` (Impact: 75.1)
  * `increase_tiled_pane_sizes_with_stacked_r` (Impact: 16.1)
  * `create_new_tab_with_swap_layouts` (Impact: 12.4)
  * `start` (Impact: 11.2)
  * `cannot_decrease_stack_size_beyond_minimu` (Impact: 9.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 2256`, `args: 181`, `func_start: 175`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1085`, `high_risk_execution: 2`, `state_mutation: 559`, `duplicate_logic: 9`, `orphaned_logic: 128`
* *Architecture:* `io: 2`, `api: 1`, `concurrency: 11`, `import: 43`
* *Defense:* `safety: 2031`, `doc: 4`, `test: 254`, `sync_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` PercentOrFixed, zellij_utils::envs::set_session_name, crate::screen::denormalize_notification_response, zellij_utils::data::Direction, crate::
    os_input_output::ServerOsApi, crate::panes::sixel::SixelImageStore, SenderWithContext, Palette...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zellij-utils/src/input/layout.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.122 IQR)
- **Top Global Matches:** file_cluster_0: 14.122, file_cluster_17: 14.197, file_cluster_11: 14.235
- **Magnitude:** 1654.98 | **LOC:** 2104 | **CtrlFlow:** 48.5% | **Authorship Centralization:** 80.0%
- **Risk Profile:** Cognitive Load (36.8761%), Tech Debt (99.8928%)
**Top Internal Functions/Classes:**
  * `populate_run_plugin_if_needed` (Impact: 419.6)
  * `split_space` (Impact: 90.5)
  * `position_panes_in_space` (Impact: 39.9)
  * `replace_next_empty_slot_with_run` (Impact: 34.2)
  * `adjust_geoms_for_rounding_errors` (Impact: 32.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 290`, `structural_boundaries: 308`, `args: 156`, `func_start: 102`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 238`, `dead_code: 5`, `planned_debt: 9`, `duplicate_logic: 41`
* *Architecture:* `io: 7`, `api: 171`, `import: 14`
* *Defense:* `safety: 465`, `doc: 2`, `test: 1`, `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` PaneGeom, super::plugins::PluginAliases, PluginsConfigError, LayoutInfo, Serialize, std::fs::File, std::cmp::Ordering, input::
        command::RunCommand...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zellij-server/src/tab/mouse_handler.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.656 IQR)
- **Top Global Matches:** file_cluster_8: 12.656, file_cluster_13: 12.997, file_cluster_0: 13.02
- **Magnitude:** 1620.96 | **LOC:** 1689 | **CtrlFlow:** 52.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (26.5561%), Tech Debt (9.26%)
**Top Internal Functions/Classes:**
  * `continue_pane_resize_with_mouse` (Impact: 666.2)
  * `determine_mouse_action` (Impact: 137.3)
  * `edge_and_delta_to_strategies` (Impact: 63.9)
  * `execute_send_to_terminal` (Impact: 54.8)
  * `execute_mouse_action` (Impact: 54.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 320`, `structural_boundaries: 292`, `args: 72`, `func_start: 32`, `class_start: 7`
* *Risk/State:* `state_mutation: 96`, `orphaned_logic: 3`
* *Architecture:* `api: 24`, `import: 13`
* *Defense:* `safety: 291`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` zellij_utils::pane_size::PaneGeom, Resize::*, ResizeStrategy, crate::background_jobs::BackgroundJob, zellij_utils::data::Direction, crate::plugins::PluginInstruction, Tab, std::time::Instant...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zellij-server/src/panes/tiled_panes/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.228 IQR)
- **Top Global Matches:** file_cluster_17: 13.228, file_cluster_8: 13.244, file_cluster_0: 13.415
- **Magnitude:** 1578.3 | **LOC:** 2800 | **CtrlFlow:** 32.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (34.5066%), Tech Debt (94.1899%)
**Top Internal Functions/Classes:**
  * `render` (Impact: 458.9)
  * `set_pane_frames` (Impact: 314.1)
    * *Intent:* *self.display_area.borrow(),
  * `toggle_pane_fullscreen` (Impact: 21.6)
  * `focus_pane_at_position` (Impact: 15.4)
  * `move_pane` (Impact: 15.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 185`, `structural_boundaries: 381`, `args: 141`, `func_start: 91`
* *Risk/State:* `safety_bypasses: 53`, `state_mutation: 231`, `dead_code: 3`, `planned_debt: 7`, `orphaned_logic: 52`
* *Architecture:* `api: 84`, `import: 6`
* *Defense:* `safety: 231`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` PaneGeom, tiled_pane_grid::split, MIN_TERMINAL_WIDTH, std::
    cell::RefCell, Pane, SplitDirection, crate::
    os_input_output::ServerOsApi, input::
        command::RunCommand...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zellij-server/src/unit/screen_tests.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.58 IQR)
- **Top Global Matches:** file_cluster_8: 12.58, file_cluster_0: 12.737, file_cluster_17: 12.971
- **Magnitude:** 1505.58 | **LOC:** 8080 | **CtrlFlow:** 6.3% | **Authorship Centralization:** 87.1%
- **Risk Profile:** Cognitive Load (15.7973%), Tech Debt (84.817%)
**Top Internal Functions/Classes:**
  * `background_plugin_receives_broadcasts_re` (Impact: 17.4)
  * `new` (Impact: 15.2)
  * `delivery_path_a_and_b_produce_same_conte` (Impact: 14.5)
  * `integration_scrollback_from_pre_subscrip` (Impact: 14.5)
  * `tab_switch_only_updates_active_tab_plugi` (Impact: 13.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 107`, `structural_boundaries: 1581`, `args: 207`, `func_start: 160`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 376`, `high_risk_execution: 1`, `state_mutation: 338`, `fragile_debt: 1`, `duplicate_logic: 8`, `orphaned_logic: 138`
* *Architecture:* `io: 1`, `api: 105`, `concurrency: 189`, `import: 36`
* *Defense:* `safety: 852`, `test: 351`, `sync_locks: 163`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::panes::sixel::SixelImageStore, Palette, interprocess::local_socket::Stream, zellij_utils::ipc::ExitReason, Ipv4Addr, WebSharing, crate::background_jobs::BackgroundJob, route::route_action...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zellij-server/src/panes/tiled_panes/tiled_pane_grid.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.494 IQR)
- **Top Global Matches:** file_cluster_17: 13.494, file_cluster_8: 13.587, file_cluster_11: 13.826
- **Magnitude:** 1415.46 | **LOC:** 2362 | **CtrlFlow:** 43.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (33.304%), Tech Debt (36.0273%)
**Top Internal Functions/Classes:**
  * `contiguous_panes_with_alignment` (Impact: 58.3)
  * `fill_geom_holes_horizontally_downwards` (Impact: 42.3)
  * `fill_geom_holes_vertically_to_the_right` (Impact: 42.3)
  * `fill_geom_holes_horizontally_upwards` (Impact: 42.2)
  * `fill_geom_holes_vertically_to_the_left` (Impact: 42.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 415`, `structural_boundaries: 531`, `args: 235`, `func_start: 70`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 416`, `dead_code: 1`, `planned_debt: 4`, `orphaned_logic: 25`
* *Architecture:* `api: 33`, `import: 16`
* *Defense:* `safety: 328`, `doc: 9`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` PaneGeom, super::pane_resizer::PaneResizer, MIN_TERMINAL_WIDTH, zellij_utils::data::Direction, std::cmp::Ordering, Viewport, Direction::Down, zellij_utils::
    errors::prelude::*...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tests/e2e/cases.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.259 IQR)
- **Top Global Matches:** file_cluster_8: 12.259, file_cluster_0: 12.531, file_cluster_4: 12.571
- **Magnitude:** 1393.58 | **LOC:** 2955 | **CtrlFlow:** 46.0% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (32.5077%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `mirrored_sessions` (Impact: 62.9)
  * `multiple_users_in_different_tabs` (Impact: 51.7)
  * `watcher_client_functionality` (Impact: 50.5)
  * `multiple_users_in_different_panes_and_sa` (Impact: 44.6)
    * *Intent:* // back to normal mode
  * `multiple_users_in_same_pane_and_tab` (Impact: 42.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 352`, `structural_boundaries: 413`, `args: 110`, `func_start: 26`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 469`, `fragile_debt: 1`, `orphaned_logic: 17`
* *Architecture:* `api: 71`, `concurrency: 84`, `import: 8`
* *Defense:* `test: 26`, `sync_locks: 9`, `immutability_locks: 47`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Step, std::fmt::Write, super::remote_runner::RemoteRunner, move_tab_right, switch_focus_to_left_tab, regex::Regex, check_third_tab_moved_to_beginning, std::path::Path...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zellij-utils/src/kdl/kdl_layout_parser.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.227 IQR)
- **Top Global Matches:** file_cluster_8: 13.227, file_cluster_17: 13.471, file_cluster_0: 13.702
- **Magnitude:** 1319.36 | **LOC:** 2602 | **CtrlFlow:** 56.8% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (18.2144%), Tech Debt (15.571%)
**Top Internal Functions/Classes:**
  * `parse_floating_pane_node_with_template` (Impact: 84.9)
  * `differentiate_pane_and_floating_pane_tem` (Impact: 70.2)
  * `parse_pane_node_with_template` (Impact: 55.4)
  * `parse_pane_node` (Impact: 46.4)
  * `parse_pane_template_node` (Impact: 44.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 462`, `structural_boundaries: 351`, `args: 186`, `func_start: 54`, `class_start: 2`
* *Risk/State:* `state_mutation: 116`, `orphaned_logic: 15`
* *Architecture:* `io: 2`, `api: 7`, `import: 7`
* *Defense:* `safety: 446`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` kdl_parsing_error, PercentOrFixed, kdl_string_arguments, kdl_property_or_child_value_node, SplitDirection, kdl_get_int_property_or_child_value, Layout, std::str::FromStr...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zellij-utils/src/kdl/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.089 IQR)
- **Top Global Matches:** file_cluster_8: 13.089, file_cluster_17: 13.457, file_cluster_0: 13.469
- **Magnitude:** 1318.08 | **LOC:** 7185 | **CtrlFlow:** 34.3% | **Authorship Centralization:** 83.3%
- **Risk Profile:** Cognitive Load (18.5%), Tech Debt (22.2989%)
**Top Internal Functions/Classes:**
  * `try_from` (Impact: 229.3)
  * `to_kdl` (Impact: 210.6)
  * `try_from` (Impact: 59.3)
  * `new_from_string` (Impact: 55.2)
  * `from_kdl` (Impact: 33.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 321`, `structural_boundaries: 614`, `args: 170`, `func_start: 28`, `class_start: 271`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 407`, `dead_code: 6`, `planned_debt: 5`, `duplicate_logic: 14`
* *Architecture:* `io: 1`, `api: 21`, `import: 24`
* *Defense:* `safety: 462`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` PercentOrFixed, LayoutInfo, strum::IntoEnumIterator, kdl_layout_parser::KdlLayoutParser, OnForceClose, SearchOption, crate::home::find_default_config_dir, PermissionCache...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zellij-server/src/screen.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.573 IQR)
- **Top Global Matches:** file_cluster_13: 14.573, file_cluster_8: 14.631, file_cluster_17: 14.674
- **Magnitude:** 1311.56 | **LOC:** 9125 | **CtrlFlow:** 50.4% | **Authorship Centralization:** 89.1%
- **Risk Profile:** Cognitive Load (9.3693%), Tech Debt (10.082%)
**Top Internal Functions/Classes:**
  * `remove_client` (Impact: 280.3)
  * `apply_layout` (Impact: 109.9)
  * `focus_plugin_pane` (Impact: 63.6)
  * `reconfigure` (Impact: 62.3)
  * `switch_active_tab` (Impact: 55.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 275`, `structural_boundaries: 271`, `args: 96`, `func_start: 37`, `class_start: 2`
* *Risk/State:* `state_mutation: 139`, `dead_code: 3`, `planned_debt: 9`
* *Architecture:* `io: 1`, `api: 59`, `import: 29`
* *Defense:* `safety: 348`, `doc: 109`, `test: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::str, Palette, PaletteColor, zellij_utils::ipc::ExitReason, Ipv4Addr, WebSharing, crate::background_jobs::BackgroundJob, ScreenContext...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zellij-server/src/route.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.83 IQR)
- **Top Global Matches:** file_cluster_8: 12.83, file_cluster_13: 13.19, file_cluster_0: 13.235
- **Magnitude:** 1276.76 | **LOC:** 3192 | **CtrlFlow:** 55.0% | **Authorship Centralization:** 84.8%
- **Risk Profile:** Cognitive Load (14.5952%), Tech Debt (11.6648%)
**Top Internal Functions/Classes:**
  * `route_action` (Impact: 655.7)
  * `route_thread_main` (Impact: 273.0)
  * `wait_for_action_completion` (Impact: 15.6)
  * `build_tabs_table_row` (Impact: 15.6)
  * `build_table_row` (Impact: 15.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 246`, `structural_boundaries: 201`, `args: 63`, `func_start: 40`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 69`, `dead_code: 2`, `orphaned_logic: 9`
* *Architecture:* `api: 18`, `concurrency: 5`, `import: 24`
* *Defense:* `safety: 340`, `test: 13`, `sync_locks: 3`, `immutability_locks: 1`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` RwLock, SearchOption, crate::
    os_input_output::ServerOsApi, ListTabsResponse, super::*, ServerToClientMsg, layout::Layout, zellij_utils::data::GetPaneCwdResponse...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zellij-utils/src/ipc/protobuf_conversion.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.393 IQR)
- **Top Global Matches:** file_cluster_8: 13.393, file_cluster_17: 13.684, file_cluster_16: 13.961
- **Magnitude:** 1170.94 | **LOC:** 4458 | **CtrlFlow:** 65.4% | **Authorship Centralization:** 88.6%
- **Risk Profile:** Cognitive Load (8.8158%), Tech Debt (90.715%)
**Top Internal Functions/Classes:**
  * `try_from` (Impact: 356.0)
  * `try_from` (Impact: 58.0)
  * `try_from` (Impact: 44.9)
  * `try_from` (Impact: 31.5)
  * `try_from` (Impact: 24.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 502`, `structural_boundaries: 265`, `args: 437`, `func_start: 94`
* *Risk/State:* `duplicate_logic: 81`
* *Architecture:* `import: 53`
* *Defense:* `safety: 639`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::client_server_contract::client_server_contract::
            MouseEventType, crate::client_server_contract::client_server_contract::pane_id::PaneType, crate::client_server_contract::client_server_contract::LayoutConstraintFloatingPair, PaneMetadata, StartWebServerMsg, WebSharing, crate::client_server_contract::client_server_contract::UnblockCondition, crate::client_server_contract::client_server_contract::Direction...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zellij-server/src/panes/tiled_panes/stacked_panes.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.289 IQR)
- **Top Global Matches:** file_cluster_17: 13.289, file_cluster_8: 13.369, file_cluster_11: 13.555
- **Magnitude:** 1122.54 | **LOC:** 1234 | **CtrlFlow:** 41.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (59.5726%), Tech Debt (57.6353%)
**Top Internal Functions/Classes:**
  * `combine_horizontally_aligned_panes_to_st` (Impact: 46.3)
  * `combine_vertically_aligned_panes_to_stac` (Impact: 44.0)
  * `expand_pane` (Impact: 35.9)
  * `resize_panes_in_stack` (Impact: 29.3)
  * `fill_space_over_visible_stacked_pane` (Impact: 28.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 286`, `structural_boundaries: 401`, `args: 115`, `func_start: 49`, `class_start: 1`
* *Risk/State:* `state_mutation: 366`, `dead_code: 3`, `planned_debt: 1`, `orphaned_logic: 22`
* *Architecture:* `api: 27`, `import: 5`
* *Defense:* `safety: 148`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` PaneGeom, pane_size::Dimension, MIN_TERMINAL_HEIGHT, std::rc::Rc, tab::Pane, zellij_utils::
    errors::prelude::*, std::cell::RefCell, std::collections::HashMap...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zellij-utils/src/plugin_api/plugin_command.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.907 IQR)
- **Top Global Matches:** file_cluster_8: 14.907, file_cluster_17: 15.163, file_cluster_16: 15.304
- **Magnitude:** 1120.3 | **LOC:** 4886 | **CtrlFlow:** 72.9% | **Authorship Centralization:** 88.9%
- **Risk Profile:** Cognitive Load (10.5742%), Tech Debt (98.2252%)
**Top Internal Functions/Classes:**
  * `try_from` (Impact: 523.5)
  * `try_from` (Impact: 122.0)
  * `into` (Impact: 11.2)
  * `into` (Impact: 11.2)
  * `key_to_rebind_to_plugin_command_assets` (Impact: 9.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 728`, `structural_boundaries: 271`, `args: 276`, `func_start: 85`
* *Risk/State:* `safety_bypasses: 24`, `planned_debt: 1`, `duplicate_logic: 83`
* *Architecture:* `api: 1`, `import: 8`
* *Defense:* `safety: 2087`, `immutability_locks: 52`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` save_layout_response, EditLayoutResponse, show_floating_panes_response, BreakPanesToNewTabResponse, FocusOrCreateTabResponse, RunningCommand, RerunCommandPanePayload, RevokeWebLoginTokenPayload...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zellij-utils/src/plugin_api/action.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.167 IQR)
- **Top Global Matches:** file_cluster_8: 14.167, file_cluster_16: 14.403, file_cluster_17: 14.427
- **Magnitude:** 1099.58 | **LOC:** 3201 | **CtrlFlow:** 51.0% | **Authorship Centralization:** 88.0%
- **Risk Profile:** Cognitive Load (10.718%), Tech Debt (99.7887%)
**Top Internal Functions/Classes:**
  * `try_from` (Impact: 467.6)
  * `try_from` (Impact: 109.2)
  * `try_from` (Impact: 22.1)
  * `try_from` (Impact: 21.9)
  * `try_from` (Impact: 19.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 438`, `structural_boundaries: 420`, `args: 231`, `func_start: 71`
* *Risk/State:* `state_mutation: 24`, `planned_debt: 1`, `duplicate_logic: 71`
* *Architecture:* `api: 1`, `import: 34`
* *Defense:* `safety: 1201`, `immutability_locks: 103`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::input::mouse::MouseEvent, PercentOrFixed, SplitDirection, SearchOption, crate::input::command::RunCommand, super::generated_api::api::action::run_plugin_or_alias::PluginType, PaneId, crate::input::command::OpenFilePayload...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zellij-server/src/plugins/zellij_exports.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.594 IQR)
- **Top Global Matches:** file_cluster_8: 12.594, file_cluster_17: 13.031, file_cluster_13: 13.168
- **Magnitude:** 1042.5 | **LOC:** 5353 | **CtrlFlow:** 30.8% | **Authorship Centralization:** 86.7%
- **Risk Profile:** Cognitive Load (7.1757%), Tech Debt (24.7365%)
**Top Internal Functions/Classes:**
  * `host_run_plugin_command` (Impact: 70.6)
  * `get_pane_scrollback` (Impact: 23.1)
  * `parse_layout` (Impact: 22.8)
  * `get_focused_pane_info` (Impact: 22.6)
  * `sanitize_layout_name` (Impact: 21.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 258`, `structural_boundaries: 581`, `args: 400`, `func_start: 118`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 51`, `dead_code: 1`, `planned_debt: 11`, `fragile_debt: 1`, `duplicate_logic: 10`
* *Architecture:* `io: 4`, `api: 7`, `concurrency: 7`, `import: 34`
* *Defense:* `safety: 374`, `doc: 2`, `sync_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 5.127
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002899
  * `Imports (Out-Degree: 0):` ProtobufHideFloatingPanesResponse, EditLayoutResponse, show_floating_panes_response, io::Read, FocusOrCreateTabResponse, zellij_utils::plugin_api::plugin_command::ProtobufCurrentSessionLastSavedTimeResponse, ProtobufNewTabResponse, ProtobufGetLayoutDirResponse...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `zellij-utils/src/plugin_api/event.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.483 IQR)
- **Top Global Matches:** file_cluster_8: 13.483, file_cluster_17: 13.541, file_cluster_16: 13.712
- **Magnitude:** 1025.08 | **LOC:** 3041 | **CtrlFlow:** 40.7% | **Authorship Centralization:** 91.7%
- **Risk Profile:** Cognitive Load (13.5416%), Tech Debt (99.1824%)
**Top Internal Functions/Classes:**
  * `try_from` (Impact: 285.3)
  * `try_from` (Impact: 103.8)
  * `try_from` (Impact: 36.5)
  * `try_from` (Impact: 25.0)
  * `try_from` (Impact: 21.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 325`, `structural_boundaries: 473`, `args: 168`, `func_start: 77`
* *Risk/State:* `safety_bypasses: 67`, `state_mutation: 131`, `planned_debt: 1`, `duplicate_logic: 57`
* *Architecture:* `io: 1`, `api: 21`, `import: 35`
* *Defense:* `safety: 594`, `test: 44`, `immutability_locks: 86`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` input_mode::InputMode, PaneRenderReportPayload, LayoutInfo, ClientInfo, super::generated_api::api::
    action::Action, PaneId, CopyDestination, PaneMetadata...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `default-plugins/session-manager/src/ui/components.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.12 IQR)
- **Top Global Matches:** file_cluster_8: 11.12, file_cluster_0: 11.518, file_cluster_16: 11.571
- **Magnitude:** 986.32 | **LOC:** 1848 | **CtrlFlow:** 38.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (18.24%), Tech Debt (84.011%)
**Top Internal Functions/Classes:**
  * `render_unified_results` (Impact: 179.3)
  * `render_controls_line` (Impact: 58.0)
  * `render_new_session_block` (Impact: 52.8)
  * `render_new_session_folder_prompt` (Impact: 38.4)
  * `render_layout_selection_list` (Impact: 34.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 220`, `structural_boundaries: 351`, `args: 62`, `func_start: 54`, `class_start: 12`
* *Risk/State:* `state_mutation: 135`, `planned_debt: 1`, `duplicate_logic: 10`, `orphaned_logic: 20`
* *Architecture:* `api: 83`, `import: 11`
* *Defense:* `safety: 91`, `doc: 18`, `test: 8`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::path::PathBuf, SessionUiInfo, TabUiInfo, crate::ActiveScreen, std::time::Duration, super::*, crate::ui::PaneUiInfo, unicode_width::UnicodeWidthChar...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zellij-server/src/panes/hyperlink_tracker.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.832 IQR)
- **Top Global Matches:** file_cluster_8: 12.832, file_cluster_0: 12.888, file_cluster_13: 13.085
- **Magnitude:** 963.28 | **LOC:** 1345 | **CtrlFlow:** 19.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (76.3656%), Tech Debt (40.3063%)
**Top Internal Functions/Classes:**
  * `finalize_and_apply` (Impact: 283.9)
  * `update` (Impact: 33.2)
  * `test_multiple_urls_in_sequence` (Impact: 31.2)
  * `test_multiline_url_detection` (Impact: 27.3)
  * `test_link_anchor_types` (Impact: 27.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 113`, `structural_boundaries: 457`, `args: 36`, `func_start: 34`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 1`, `state_mutation: 337`, `orphaned_logic: 22`
* *Architecture:* `api: 4`, `import: 9`
* *Defense:* `safety: 117`, `test: 106`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::collections::VecDeque, LinkAnchor, super::*, crate::panes::link_handler::LinkHandler, crate::panes::terminal_character::Cursor, crate::panes::terminal_character::LinkAnchor, crate::panes::grid::Row, TerminalCharacter
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zellij-server/src/output/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_11` (Drift: 13.573 IQR)
- **Top Global Matches:** file_cluster_11: 13.573, file_cluster_8: 13.588, file_cluster_17: 13.619
- **Magnitude:** 934.78 | **LOC:** 1327 | **CtrlFlow:** 44.0% | **Authorship Centralization:** 90.0%
- **Risk Profile:** Cognitive Load (32.4794%), Tech Debt (55.3527%)
**Top Internal Functions/Classes:**
  * `serialize_with_size` (Impact: 220.9)
  * `remove_covered_sixel_parts` (Impact: 106.0)
  * `serialize_chunks` (Impact: 80.2)
  * `remove_covered_parts` (Impact: 45.7)
  * `serialize_chunks_with_newlines` (Impact: 39.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 183`, `structural_boundaries: 233`, `args: 46`, `func_start: 26`, `class_start: 2`
* *Risk/State:* `state_mutation: 161`, `dead_code: 3`, `planned_debt: 6`, `orphaned_logic: 13`
* *Architecture:* `api: 24`, `import: 12`
* *Defense:* `safety: 166`, `doc: 1`, `test: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::collections::VecDeque, zellij_utils::pane_size::PaneGeom, crate::
    panes::sixel::SixelImageStore, panes::terminal_character::AnsiCode, panes::LinkHandler, crate::panes::Row, std::fmt::Write, PaneId...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zellij-utils/src/data.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_16` (Drift: 14.116 IQR)
- **Top Global Matches:** file_cluster_16: 14.116, file_cluster_0: 14.135, file_cluster_8: 14.219
- **Magnitude:** 932.18 | **LOC:** 3612 | **CtrlFlow:** 34.4% | **Authorship Centralization:** 84.8%
- **Risk Profile:** Cognitive Load (4.734%), Tech Debt (99.9991%)
**Top Internal Functions/Classes:**
  * `new` (Impact: 30.8)
  * `from_cli` (Impact: 27.5)
  * `from` (Impact: 16.1)
    * *Intent:* /// Text was copied to the clipboard anywhere in the app
  * `eq` (Impact: 13.2)
  * `from` (Impact: 12.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 147`, `structural_boundaries: 280`, `args: 146`, `func_start: 126`, `class_start: 43`
* *Risk/State:* `state_mutation: 105`, `dead_code: 1`, `planned_debt: 3`, `fragile_debt: 2`, `duplicate_logic: 42`, `orphaned_logic: 72`
* *Architecture:* `io: 3`, `api: 283`, `import: 21`
* *Defense:* `safety: 519`, `doc: 142`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` PercentOrFixed, Serialize, std::str::self, EnumString, crate::pane_size::PaneGeom, KeyboardEncoding, crate::vendored::termwiz::
    input::KittyKeyboardFlags, BTreeSet...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zellij-utils/src/input/actions.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.485 IQR)
- **Top Global Matches:** file_cluster_8: 13.485, file_cluster_0: 13.65, file_cluster_7: 13.894
- **Magnitude:** 922.16 | **LOC:** 3874 | **CtrlFlow:** 39.5% | **Authorship Centralization:** 87.5%
- **Risk Profile:** Cognitive Load (4.5449%), Tech Debt (98.081%)
**Top Internal Functions/Classes:**
  * `actions_from_cli` (Impact: 386.1)
  * `test_send_keys_multiple_keys` (Impact: 8.0)
  * `test_new_pane_tiled_with_tab_id` (Impact: 7.2)
  * `test_new_pane_tiled_without_tab_id` (Impact: 7.2)
  * `test_new_pane_floating_with_tab_id` (Impact: 7.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 202`, `structural_boundaries: 310`, `args: 200`, `func_start: 92`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 82`, `state_mutation: 3`, `planned_debt: 4`, `duplicate_logic: 6`, `orphaned_logic: 85`
* *Architecture:* `api: 7`, `import: 16`
* *Defense:* `safety: 696`, `doc: 74`, `test: 344`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::input::mouse::MouseEvent, LayoutInfo, super::layout::
    FloatingPaneLayout, Serialize, super::*, crate::home::find_default_config_dir, PaneId, crate::data::FloatingPaneCoordinates...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `zellij-server/src/panes/sixel.rs` (RUST) | Magnitude: 295.16 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 414, structural_boundaries: 103, safety: 66, branch: 60
- `zellij-utils/src/vendored/termwiz/input.rs` (RUST) | Magnitude: 97.58 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 344, sec_reflection_metaprogramming: 177, doc: 58, structural_boundaries: 43
- `zellij-tile/src/lib.rs` (RUST) | Magnitude: 49.22 | Delta: **0.058 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 96, doc: 81, structural_boundaries: 44, args: 17
- `default-plugins/status-bar/src/tip/cache.rs` (RUST) | Magnitude: 76.38 | Delta: **0.062 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 80, structural_boundaries: 26, safety: 23, state_mutation: 20
- `zellij-server/src/unit/os_input_output_tests.rs` (RUST) | Magnitude: 85.32 | Delta: **0.063 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 120, structural_boundaries: 49, concurrency: 22, decorators: 22

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `zellij-server/src/output/mod.rs` (RUST) | Magnitude: 934.78 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 833, structural_boundaries: 233, branch: 183, safety: 166
- `zellij-server/src/panes/alacritty_functions.rs` (RUST) | Magnitude: 100.8 | Delta: **0.06 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 63, branch: 33, safety: 27, structural_boundaries: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `zellij-server/src/pty_writer.rs` (RUST) | Magnitude: 66.7 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 107, structural_boundaries: 25, branch: 23, safety: 23
- `zellij-utils/src/input/mod.rs` (RUST) | Magnitude: 100.62 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 154, structural_boundaries: 49, state_mutation: 28, branch: 21
- `zellij-utils/src/input/keybinds.rs` (RUST) | Magnitude: 95.4 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 113, state_mutation: 26, structural_boundaries: 25, branch: 15
- `zellij-utils/src/logging.rs` (RUST) | Magnitude: 40.34 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 89, structural_boundaries: 21, safety: 18, memory_alloc: 10
- `zellij-server/src/background_jobs.rs` (RUST) | Magnitude: 156.5 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 409, structural_boundaries: 122, safety: 85, branch: 49

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `zellij-utils/src/ipc.rs` (RUST) | Magnitude: 201.54 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 303, safety: 82, structural_boundaries: 75, state_mutation: 62
- `zellij-utils/src/channels.rs` (RUST) | Magnitude: 9.0 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 10, indent_spaces: 8, structural_boundaries: 6, api: 6
- `zellij-utils/src/plugin_api/command.rs` (RUST) | Magnitude: 6.16 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 11, generics: 8, args: 4
- `zellij-utils/src/data.rs` (RUST) | Magnitude: 932.18 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 1610, safety: 519, api: 283, encapsulation: 283
- `zellij-utils/src/plugin_api/file.rs` (RUST) | Magnitude: 6.44 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 11, generics: 8, args: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `zellij-server/src/panes/tiled_panes/mod.rs` (RUST) | Magnitude: 1578.3 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 1556, structural_boundaries: 381, safety: 231, state_mutation: 231
- `zellij-server/src/panes/floating_panes/mod.rs` (RUST) | Magnitude: 800.22 | Delta: **0.058 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 933, structural_boundaries: 206, safety: 164, state_mutation: 153
- `zellij-server/src/panes/tiled_panes/stacked_panes.rs` (RUST) | Magnitude: 1122.54 | Delta: **0.08 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 1188, structural_boundaries: 401, state_mutation: 366, branch: 286
- `zellij-server/src/panes/tiled_panes/tiled_pane_grid.rs` (RUST) | Magnitude: 1415.46 | Delta: **0.093 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 2080, structural_boundaries: 531, state_mutation: 416, branch: 415
- `zellij-server/src/panes/tiled_panes/pane_resizer.rs` (RUST) | Magnitude: 193.38 | Delta: **0.098 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 283, structural_boundaries: 73, branch: 53, state_mutation: 53

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `zellij-server/src/os_input_output_windows.rs` (RUST) | Magnitude: 362.88 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 461, structural_boundaries: 116, safety: 98, branch: 75
- `zellij-client/src/os_input_output.rs` (RUST) | Magnitude: 143.46 | Delta: **0.078 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 138, safety: 67, concurrency: 59, structural_boundaries: 52
- `zellij-server/src/os_input_output.rs` (RUST) | Magnitude: 458.92 | Delta: **0.086 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 582, safety: 181, structural_boundaries: 159, branch: 94
- `zellij-client/src/web_client/unit/web_client_tests.rs` (RUST) | Magnitude: 786.36 | Delta: **0.096 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 1887, structural_boundaries: 735, concurrency: 362, safety: 284
- `zellij-server/src/tab/copy_command.rs` (RUST) | Magnitude: 37.86 | Delta: **0.103 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 46, structural_boundaries: 16, concurrency: 10, branch: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `zellij-tile/src/ui_components/nested_list.rs` (RUST) | Magnitude: 94.0 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 138, structural_boundaries: 33, args: 29, api: 22
- `zellij-utils/src/input/config.rs` (RUST) | Magnitude: 408.42 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 1193, safety: 209, structural_boundaries: 183, branch: 94
- `zellij-server/src/ui/pane_boundaries_frame.rs` (RUST) | Magnitude: 282.54 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 389, structural_boundaries: 131, state_mutation: 75, branch: 69
- `default-plugins/status-bar/src/tip/data/sync_tab.rs` (RUST) | Magnitude: 35.56 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 50, concurrency: 18, structural_boundaries: 16, state_mutation: 6
- `zellij-client/src/web_client/utils.rs` (RUST) | Magnitude: 49.66 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 55, safety: 15, branch: 14, structural_boundaries: 14

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `zellij-utils/src/ipc/protobuf_conversion.rs` -> Churn: **76.39%** | Cog Load: 8.8158% | Debt: 90.715%
- `zellij-server/src/tab/mod.rs` -> Churn: **75.17%** | Cog Load: 27.1129% | Debt: 99.4741%
- `zellij-utils/src/data.rs` -> Churn: **75.17%** | Cog Load: 4.734% | Debt: 99.9991%
- `zellij-server/src/unit/screen_tests.rs` -> Churn: **73.88%** | Cog Load: 15.7973% | Debt: 84.817%
- `zellij-utils/src/errors.rs` -> Churn: **70.25%** | Cog Load: 3.1875% | Debt: 64.9084%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `zellij-server/src/panes/grid.rs` -> **Aram Drevekenin** (82.6% isolated ownership) | Magnitude: 2862.56
- `zellij-server/src/tab/mod.rs` -> **Aram Drevekenin** (93.9% isolated ownership) | Magnitude: 1887.62
- `zellij-server/src/panes/unit/grid_tests.rs` -> **Aram Drevekenin** (83.3% isolated ownership) | Magnitude: 1850.4
- `zellij-server/src/tab/unit/tab_integration_tests.rs` -> **Aram Drevekenin** (85.0% isolated ownership) | Magnitude: 1658.8
- `zellij-server/src/tab/mouse_handler.rs` -> **Aram Drevekenin** (100.0% isolated ownership) | Magnitude: 1620.96

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `zellij-utils/src/envs.rs` -> **Severity: 0.634** (Embedded: 0.0203 * Error Risk: 31.2282%)
- `xtask/src/metadata.rs` -> **Severity: 0.208** (Embedded: 0.0116 * Error Risk: 17.9746%)
- `zellij-utils/src/session_serialization.rs` -> **Severity: 0.18** (Embedded: 0.0058 * Error Risk: 31.1099%)
- `zellij-utils/src/input/keybinds.rs` -> **Severity: 0.17** (Embedded: 0.0029 * Error Risk: 58.7102%)
- `xtask/src/test.rs` -> **Severity: 0.13** (Embedded: 0.0029 * Error Risk: 44.846%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `zellij-utils/src/envs.rs` -> **Severity: 1808.1** (Blast Radius: 18.084 * Doc Risk: 99.9834%)
- `xtask/src/flags.rs` -> **Severity: 705.6** (Blast Radius: 7.056 * Doc Risk: 100.0%)
- `zellij-utils/src/input/keybinds.rs` -> **Severity: 512.7** (Blast Radius: 5.127 * Doc Risk: 100.0%)
- `default-plugins/about/src/active_component.rs` -> **Severity: 277.2** (Blast Radius: 2.772 * Doc Risk: 100.0%)
- `default-plugins/layout-manager/src/errors.rs` -> **Severity: 277.2** (Blast Radius: 2.772 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
