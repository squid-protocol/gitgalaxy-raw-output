# ARCHITECTURAL_BRIEF: zellij
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/zellij-org/zellij.git` |
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
| Total Artifacts | 1571 |
| Analyzed Artifacts (Scanned) | 385 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1186 |
| Total LOC | 249287 |
| Volatility Index | 0.005 |
| % Scanned of codebase = | 24.5% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6823 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3571 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0943 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 7 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUST | 302 | 239156 | 78.4% |
| MARKDOWN | 25 | 0 | 6.5% |
| YAML | 19 | 4921 | 4.9% |
| PROTO | 17 | 3646 | 4.4% |
| JAVASCRIPT | 10 | 1227 | 2.6% |
| SHELL | 7 | 95 | 1.8% |
| CSS | 2 | 162 | 0.5% |
| XML | 1 | 0 | 0.3% |
| JSON | 1 | 50 | 0.3% |
| HTML | 1 | 30 | 0.3% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Flat Modular Platform` (z +0.47; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules 34%, Data / Markup / Trivial 18%, State Mutators Files 10%, Declarative / Non-Code 9%, Tests & Verification Files 7%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 360 | 93.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 25 | 6.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1186*

**Composition by Extension & Reason:**
- `.snap`: 901x Unsupported Format (.snap), 6x Excluded (Saturation: Line 5 exceeds 500 chars), 4x Excluded (Saturation: Line 6 exceeds 500 chars)
- `no_extension`: 37x Unsupported Format (.undeterminable), 20x Excluded (Binary Format Detected), 13x Excluded (Saturation: Line 49 exceeds 500 chars)
- `.kdl`: 62x Excluded (Unsupported Extension: '.kdl'), 22x Unsupported Format (.kdl)
- `.toml`: 20x Unsupported Format (.toml), 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.toml')
- `.wasm`: 17x Excluded (Unsupported Extension: '.wasm')
- `.md`: 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 3x Excluded (Saturation: Line 1 exceeds 500 chars), 1x Excluded (Saturation: Line 28 exceeds 500 chars), 1x Excluded (Saturation: Line 30 exceeds 500 chars)
- `.ico`: 2x Excluded (Explicitly Denied Extension: '.ico')
- `.six`: 2x Excluded (Saturation: Line 1 exceeds 500 chars)
- `.bmp`: 2x Excluded (Explicitly Denied Extension: '.bmp')
- `.lock`: 1x Excluded (Unsupported Extension: '.lock')
- `.gif`: 1x Excluded (Explicitly Denied Extension: '.gif')
- `.png`: 1x Excluded (Explicitly Denied Extension: '.png')
- `.desktop`: 1x Excluded (Unsupported Extension: '.desktop')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 13.8 | 9.3 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 95.3 | 40.3 | 51.7 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 33.6 | 13.8 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 33.5 | 2.4 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 98.5 | 11.1 | 7.1 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 7.9 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 36.7 | 16.3 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 99.5 | 2.1 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 84.2 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 10.0 | 1.7 | 0.4 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 83.6 | 16.8 | 7.5 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 72.0 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 68.6 | 0.2 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 8098 | 268 | 48 | `zellij-server/src/panes/unit/grid_tests.rs` |
| cleanup | 125 | 32 | 0 | `zellij-client/src/web_client/unit/web_client_tests.rs` |
| guards | 4465 | 227 | 32 | `zellij-utils/src/kdl/mod.rs` |
| danger | 7387 | 130 | 17 | `zellij-server/src/tab/unit/tab_tests.rs` |
| concurrency | 3183 | 74 | 8 | `zellij-server/src/unit/screen_tests.rs` |
| connectivity | 7136 | 283 | 38 | `zellij-utils/assets/prost_ipc/client_server_contract.rs` |
| io | 362 | 76 | 3 | `zellij-client/src/web_client/unit/web_client_tests.rs` |
| crypto | 0 | 0 | 0 | - |
| ipc | 5 | 4 | 0 | `zellij-client/src/lib.rs` |
| time | 561 | 43 | 1 | `zellij-server/src/unit/screen_tests.rs` |
| serialization | 46 | 15 | 0 | `zellij-client/src/web_client/unit/web_client_tests.rs` |
| regex | 21 | 10 | 0 | `zellij-client/src/stdin_ansi_parser.rs` |
| events | 594 | 79 | 3 | `zellij-server/src/screen.rs` |
| tests | 5739 | 84 | 14 | `zellij-server/src/tab/unit/tab_tests.rs` |
| docs | 2983 | 121 | 16 | `zellij-tile/src/shim.rs` |
| debt | 673 | 115 | 4 | `src/commands.rs` |
| mutation | 39346 | 301 | 255 | `zellij-server/src/tab/unit/tab_integration_tests.rs` |
| dead_code | 3785 | 234 | 23 | `zellij-server/src/tab/unit/tab_integration_tests.rs` |
| credential | 5 | 3 | 0 | `zellij-client/src/remote_attach/unit/remote_attach_tests.rs` |
| threat | 136 | 40 | 1 | `zellij-utils/src/kdl/mod.rs` |
| ml_ai | 131 | 31 | 0 | `zellij-server/src/panes/tiled_panes/tiled_pane_grid.rs` |
| ui | 22 | 7 | 0 | `zellij-client/assets/xterm.css` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.4085**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `zellij-client/src/web_client/unit/web_client_tests.rs` (Hits: 28)
- `zellij-client/assets/index.html` (Hits: 19)
- `zellij-utils/src/consts.rs` (Hits: 15)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **envs.rs** (`zellij-utils/src/envs.rs`) — 7 inbound connections
2. **utils.js** (`zellij-client/assets/utils.js`) — 5 inbound connections
3. **metadata.rs** (`xtask/src/metadata.rs`) — 4 inbound connections
4. **connection.js** (`zellij-client/assets/connection.js`) — 3 inbound connections
5. **flags.rs** (`xtask/src/flags.rs`) — 2 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **plugin_command.rs** (`zellij-utils/src/plugin_api/plugin_command.rs`) — 225 outbound dependencies
2. **zellij_exports.rs** (`zellij-server/src/plugins/zellij_exports.rs`) — 204 outbound dependencies
3. **screen.rs** (`zellij-server/src/screen.rs`) — 104 outbound dependencies
4. **protobuf_conversion.rs** (`zellij-utils/src/ipc/protobuf_conversion.rs`) — 91 outbound dependencies
5. **mod.rs** (`zellij-server/src/tab/mod.rs`) — 88 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `route_action` **(Many-Argument Workhorses)** (@ `zellij-server/src/route.rs`) -> Impact: **708.4** | LOC: 1372
- `screen_thread_main` **(Many-Argument Workhorses)** (@ `zellij-server/src/screen.rs`) -> Impact: **612.3** | LOC: 1134
  * *Intent:* // The box is here in order to make the // NewClient enum smaller
- `csi_dispatch` **(Many-Argument Workhorses)** (@ `zellij-server/src/panes/grid.rs`) -> Impact: **427.1** | LOC: 605
- `plugin_thread_main` **(Many-Argument Workhorses)** (@ `zellij-server/src/plugins/mod.rs`) -> Impact: **386.3** | LOC: 1014
- `try_from` **(Compute Cores)** (@ `zellij-utils/src/plugin_api/plugin_command.rs`) -> Impact: **384.1** | LOC: 951
- `actions_from_cli` **(Many-Argument Workhorses)** (@ `zellij-utils/src/input/actions.rs`) -> Impact: **348.1** | LOC: 1001
- `try_from` **(Compute Cores)** (@ `zellij-utils/src/plugin_api/action.rs`) -> Impact: **344.6** | LOC: 952
- `update` **(Many-Argument Workhorses)** (@ `default-plugins/fixture-plugin-for-tests/src/main.rs`) -> Impact: **310.0** | LOC: 866
- `try_from` **(Compute Cores)** (@ `zellij-utils/src/ipc/protobuf_conversion.rs`) -> Impact: **299.1** | LOC: 919
- `encode` **(Many-Argument Workhorses)** (@ `zellij-utils/src/vendored/termwiz/input.rs`) -> Impact: **228.3** | LOC: 318
  * *Intent:* /// Returns the byte sequence that represents this KeyCode and Modifier combination.

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `zellij-server/src` | 15 | 8592.62 | 15.61% | 45.9% |
| `zellij-server/src/panes` | 12 | 7073.52 | 27.58% | 68.07% |
| `zellij-server/src/tab` | 6 | 5722.2 | 21.1% | 55.5% |
| `zellij-utils/src/kdl` | 2 | 4830.58 | 24.01% | 9.4% |
| `zellij-utils/src` | 23 | 4254.7 | 7.63% | 54.19% |
| `zellij-server/src/panes/tiled_panes` | 4 | 4118.18 | 27.69% | 52.66% |
| `zellij-server/src/plugins` | 9 | 3851.38 | 12.62% | 36.41% |
| `zellij-utils/src/input` | 13 | 3471.46 | 16.21% | 32.18% |
| `zellij-utils/src/plugin_api` | 27 | 3137.8 | 4.31% | 0.85% |
| `zellij-server/src/tab/unit` | 3 | 3111.38 | 5.15% | 32.67% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `zellij-tile/src/shim.rs` -> **99.9997%** Exposure
- `zellij-server/src/panes/terminal_pane.rs` -> **99.9963%** Exposure
- `zellij-tile/src/ui_components/nested_list.rs` -> **99.9915%** Exposure
- `zellij-server/src/terminal_bytes.rs` -> **99.9768%** Exposure
- `zellij-server/src/panes/plugin_pane.rs` -> **99.9639%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `default-plugins/layout-manager/src/screens/layout_list/mod.rs` -> **100.0%** Exposure
- `default-plugins/layout-manager/src/screens/layout_list/search.rs` -> **100.0%** Exposure
- `zellij-server/src/ui/components/nested_list.rs` -> **100.0%** Exposure
- `zellij-server/src/ui/components/table.rs` -> **100.0%** Exposure
- `zellij-server/src/ui/components/text.rs` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `zellij-server/src/tab/unit/tab_integration_tests.rs` -> **227** Orphaned Functions | **0** Duplicates
- `zellij-server/src/tab/mod.rs` -> **216** Orphaned Functions | **0** Duplicates
- `zellij-tile/src/shim.rs` -> **199** Orphaned Functions | **0** Duplicates
- `zellij-server/src/unit/screen_tests.rs` -> **181** Orphaned Functions | **0** Duplicates
- `zellij-server/src/panes/unit/grid_tests.rs` -> **169** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `zellij-client/src/remote_attach/unit/remote_attach_tests.rs` -> **68.6348%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `4895` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `default-plugins/status-bar/src/tip/data/sync_tab.rs` (RUST) -> Cumulative Risk: **671.48**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +0.40)
- **Magnitude:** 40.16 | **LOC:** 77 | **CtrlFlow:** 1.6% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9999%)
- **Heaviest Functions:** `add_keybinds` (Generic / Templated Code, Impact: 4.4), `sync_tab_full` (Interface Declarations, Impact: 1.9), `sync_tab_medium` (Interface Declarations, Impact: 1.9)

### 2. `zellij-client/src/unit/terminal_loop_tests.rs` (RUST) -> Cumulative Risk: **663.73**
- **Archetype:** `file_cluster_15` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.59)
- **Magnitude:** 249.54 | **LOC:** 776 | **CtrlFlow:** 3.3% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9515%), Safety Score (88.0537%)
- **Heaviest Functions:** `handle_websocket` (Compute Cores, Impact: 25.7), `test_control_message_handling` (I/O & Config Routines, Impact: 7.2), `test_resize_signal_sends_control_message` (I/O & Config Routines, Impact: 6.5)

### 3. `zellij-server/src/panes/grid.rs` (RUST) -> Cumulative Risk: **639.89**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -1.26)
- **Magnitude:** 3523.62 | **LOC:** 4798 | **CtrlFlow:** 20.7% | **Authorship Centralization:** 86.4%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9136%), Documentation (92.6154%), Verification (80.0%)
- **Heaviest Functions:** `csi_dispatch` (Many-Argument Workhorses, Impact: 427.1), `osc_dispatch` (Many-Argument Workhorses, Impact: 113.2), `change_size` (Many-Argument Workhorses, Impact: 93.3)

### 4. `zellij-server/src/panes/selection.rs` (RUST) -> Cumulative Risk: **638.69**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -1.02)
- **Magnitude:** 239.38 | **LOC:** 278 | **CtrlFlow:** 23.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9768%), Tech Debt (98.0358%), Documentation (94.4444%)
- **Heaviest Functions:** `add_word_to_position` (Many-Argument Workhorses, Impact: 55.8), `add_line_to_position` (Defensive Guards, Impact: 27.7), `contains` (Compute Cores, Impact: 22.9)

### 5. `zellij-client/src/web_client/unit/web_client_tests.rs` (RUST) -> Cumulative Risk: **627.66**
- **Archetype:** `file_cluster_15` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.38)
- **Magnitude:** 742.66 | **LOC:** 2824 | **CtrlFlow:** 4.6% | **Authorship Centralization:** 72.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.8262%), Safety Score (93.6355%)
- **Heaviest Functions:** `test_kicked_by_host_sends_close_code_4001` (I/O & Config Routines, Impact: 26.1), `test_full_session_flow` (I/O & Config Routines, Impact: 21.3), `test_normal_exit_sends_normal_close_code` (I/O & Config Routines, Impact: 18.2)

### 6. `default-plugins/layout-manager/src/screens/layout_list/search.rs` (RUST) -> Cumulative Risk: **625.41**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `State Mutators Files` (z +0.21)
- **Magnitude:** 115.82 | **LOC:** 198 | **CtrlFlow:** 9.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.8552%)
- **Heaviest Functions:** `update_filter` (Many-Argument Workhorses, Impact: 20.9), `render_filter_line` (Generic / Templated Code, Impact: 8.8), `get_matched_indices_for_visible` (Generic / Templated Code, Impact: 6.8)

### 7. `zellij-server/src/output/mod.rs` (RUST) -> Cumulative Risk: **621.47**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.64)
- **Magnitude:** 1000.2 | **LOC:** 1327 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 90.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.7507%), Verification (80.0%)
- **Heaviest Functions:** `remove_covered_sixel_parts` (Many-Argument Workhorses, Impact: 97.4), `serialize_chunks` (Many-Argument Workhorses, Impact: 75.9), `remove_covered_parts` (Many-Argument Workhorses, Impact: 41.2)

### 8. `default-plugins/strider/src/shared.rs` (RUST) -> Cumulative Risk: **610.19**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.32)
- **Magnitude:** 147.14 | **LOC:** 171 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9835%), Safety Score (80.4959%)
- **Heaviest Functions:** `calculate_list_bounds` (Many-Argument Workhorses, Impact: 33.9), `render_current_path` (Many-Argument Workhorses, Impact: 24.7), `truncate_path` (Compute Cores, Impact: 17.1)

### 9. `zellij-client/src/remote_attach/unit/remote_attach_tests.rs` (RUST) -> Cumulative Risk: **609.4**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.67)
- **Magnitude:** 245.16 | **LOC:** 952 | **CtrlFlow:** 2.6% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (98.2143%), Concurrency (92.6304%), Tech Debt (80.2675%)
- **Heaviest Functions:** `handle_ws_terminal` (Defensive Guards, Impact: 11.6), `handle_ws_control` (Defensive Guards, Impact: 11.6), `handle_session` (Defensive Guards, Impact: 6.3)

### 10. `zellij-client/src/os_input_output_windows.rs` (RUST) -> Cumulative Risk: **608.22**
- **Archetype:** `file_cluster_14` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.50)
- **Magnitude:** 118.26 | **LOC:** 250 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (98.611%), State Flux (92.8978%), Verification (80.0%)
- **Heaviest Functions:** `next` (Defensive Guards, Impact: 15.9), `enable_mouse_support` (Compute Cores, Impact: 9.3), `disable_mouse_support` (Compute Cores, Impact: 9.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `zellij-server/src/tab/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 3744.2 | **LOC:** 6061 | **CtrlFlow:** 16.9% | **Authorship Centralization:** 93.9%
- **Risk Profile:** Cognitive Load (19.996%), Tech Debt (97.5406%)
**Top Internal Functions/Classes:**
  * `suppress_pane_and_replace_with_pid` **(Many-Argument Workhorses)** (Impact: 64.0)
  * `write_to_pane_id` **(Many-Argument Workhorses)** (Impact: 60.1)
  * `new_no_preference_pane` **(Many-Argument Workhorses)** (Impact: 52.9)
  * `new_stacked_pane` **(Many-Argument Workhorses)** (Impact: 52.1)
  * `extract_pane` **(Many-Argument Workhorses)** (Impact: 49.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Cascading Flux:* 96 instances
* *Memory Alloc (weighted view):* 19
* *State Mutation (weighted view):* 365
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 957`, `structural_boundaries: 1040`, `args: 663`, `func_start: 420`, `class_start: 4`
* *Risk/State:* `state_mutation: 173`, `dead_code: 3`, `planned_debt: 25`, `fragile_debt: 3`, `unreferenced_by_name: 216`
* *Architecture:* `io: 1`, `api: 259`, `import: 31`
* *Defense:* `safety: 207`, `doc: 5`, `test: 3`, `immutability_locks: 3`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.423
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ClientId, FloatingPaneCoordinates, HashMap, HashSet, InputMode, KeyWithModifier, Line, ModeInfo...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zellij-server/src/panes/grid.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 3523.62 | **LOC:** 4798 | **CtrlFlow:** 20.7% | **Authorship Centralization:** 86.4%
- **Risk Profile:** Cognitive Load (57.5894%), Tech Debt (45.9538%)
**Top Internal Functions/Classes:**
  * `csi_dispatch` **(Many-Argument Workhorses)** (Impact: 427.1)
  * `osc_dispatch` **(Many-Argument Workhorses)** (Impact: 113.2)
  * `change_size` **(Many-Argument Workhorses)** (Impact: 93.3)
  * `compute_plugin_highlight_selections` **(Compute Cores)** (Impact: 46.0)
    * *Intent:* /// Pre-compute plugin highlight selections across all logical line groups in /// the viewport. Hove...
  * `get_selected_text` **(Compute Cores)** (Impact: 42.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 279 instances
* *State Mutation (weighted view):* 1025
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 898`, `structural_boundaries: 959`, `args: 274`, `func_start: 194`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 467`, `dead_code: 6`, `planned_debt: 17`, `fragile_debt: 4`, `unreferenced_by_name: 53`
* *Architecture:* `api: 186`, `import: 26`
* *Defense:* `safety: 113`, `doc: 61`, `test: 1`, `immutability_locks: 3`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.423
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CharsetIndex, Cursor, CursorShape, Debug, EMPTY_TERMINAL_CHARACTER, Formatter, HighlightSelection, HighlightStyle...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zellij-server/src/screen.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 3258.52 | **LOC:** 9125 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 89.1%
- **Risk Profile:** Cognitive Load (13.8257%), Tech Debt (7.9707%)
**Top Internal Functions/Classes:**
  * `screen_thread_main` **(Many-Argument Workhorses)** (Impact: 612.3)
    * *Intent:* // The box is here in order to make the // NewClient enum smaller
  * `apply_layout` **(Many-Argument Workhorses)** (Impact: 105.4)
  * `render_to_clients` **(Compute Cores)** (Impact: 68.5)
  * `reconfigure` **(Many-Argument Workhorses)** (Impact: 61.1)
  * `focus_plugin_pane` **(Many-Argument Workhorses)** (Impact: 60.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 189 instances
* *State Mutation (weighted view):* 629
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1523`, `structural_boundaries: 1316`, `args: 404`, `func_start: 131`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 251`, `dead_code: 3`, `planned_debt: 9`
* *Architecture:* `io: 5`, `api: 102`, `import: 30`
* *Defense:* `safety: 288`, `doc: 109`, `test: 7`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.423
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` BRACKETED_PASTE_END, ClientId, ClientTabIndexOrPaneId, Direction, EventType, FloatingPaneCoordinates, GetFocusedPaneInfoResponse, HashMap...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zellij-utils/src/kdl/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 3016.6 | **LOC:** 7185 | **CtrlFlow:** 12.0% | **Authorship Centralization:** 83.3%
- **Risk Profile:** Cognitive Load (24.6408%), Tech Debt (10.9365%)
**Top Internal Functions/Classes:**
  * `to_kdl` **(Compute Cores)** (Impact: 178.5)
  * `try_from` **(Compute Cores)** (Impact: 111.5)
  * `to_kdl` **(Defensive Guards)** (Impact: 87.1)
  * `from_kdl` **(Many-Argument Workhorses)** (Impact: 61.1)
  * `from_string` **(Defensive Guards)** (Impact: 56.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 309 instances
* *State Mutation (weighted view):* 1066
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 826`, `structural_boundaries: 1618`, `args: 520`, `func_start: 129`
* *Risk/State:* `safety_bypasses: 136`, `state_mutation: 448`, `dead_code: 6`, `planned_debt: 5`, `unreferenced_by_name: 16`
* *Architecture:* `io: 3`, `api: 44`, `concurrency: 3`, `import: 28`
* *Defense:* `safety: 310`, `doc: 6`, `test: 54`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.423
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` BTreeSet, ConfigError, DEFAULT_STYLES, Direction, FloatingPaneCoordinates, HashMap, HashSet, InputMode...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zellij-server/src/plugins/unit/plugin_tests.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1824.8 | **LOC:** 12897 | **CtrlFlow:** 3.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (6.9192%), Tech Debt (34.109%)
**Top Internal Functions/Classes:**
  * `mode_update_payload_is_lightweight_for_opted_in_plugins` **(I/O & Config Routines)** (Impact: 21.8)
  * `create_plugin_thread_with_pty_receiver` **(Many-Argument Workhorses)** (Impact: 16.7)
  * `create_plugin_thread` **(Many-Argument Workhorses)** (Impact: 15.5)
  * `reconfiguration_resends_keybinds_to_opted_in_plugins` **(I/O & Config Routines)** (Impact: 14.1)
  * `create_plugin_thread_with_background_jobs_receiver` **(Many-Argument Workhorses)** (Impact: 13.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 19 instances
* *Concurrency (weighted view):* 207
* *State Mutation (weighted view):* 81
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 395`, `structural_boundaries: 2924`, `args: 324`, `func_start: 150`
* *Risk/State:* `safety_bypasses: 496`, `state_mutation: 43`, `dead_code: 7`, `planned_debt: 4`, `unreferenced_by_name: 146`
* *Architecture:* `io: 3`, `api: 146`, `concurrency: 197`, `import: 25`
* *Defense:* `safety: 153`, `test: 167`, `sync_locks: 328`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.423
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ChannelWithContext, Event, InputMode, KeyWithModifier, ModeInfo, Mutex, PermissionStatus, PermissionType...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zellij-utils/src/kdl/kdl_layout_parser.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1813.98 | **LOC:** 2602 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (23.3852%), Tech Debt (7.8666%)
**Top Internal Functions/Classes:**
  * `parse_floating_pane_node_with_template` **(Many-Argument Workhorses)** (Impact: 78.1)
  * `populate_layout_child` **(Many-Argument Workhorses)** (Impact: 76.3)
  * `differentiate_pane_and_floating_pane_template` **(Compute Cores)** (Impact: 57.9)
  * `parse_pane_node_with_template` **(Many-Argument Workhorses)** (Impact: 51.6)
  * `layout_with_one_pane` **(Many-Argument Workhorses)** (Impact: 47.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 84 instances
* *State Mutation (weighted view):* 265
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 621`, `structural_boundaries: 529`, `args: 225`, `func_start: 69`, `class_start: 2`
* *Risk/State:* `state_mutation: 97`, `unreferenced_by_name: 1`
* *Architecture:* `io: 2`, `api: 9`, `import: 7`
* *Defense:* `safety: 128`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.423
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` HashMap, HashSet, Layout, LayoutConstraint, PercentOrFixed, PluginUserConfiguration, Run, RunPluginOrAlias...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zellij-server/src/unit/screen_tests.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1629.6 | **LOC:** 8080 | **CtrlFlow:** 2.0% | **Authorship Centralization:** 86.7%
- **Risk Profile:** Cognitive Load (13.5404%), Tech Debt (76.6181%)
**Top Internal Functions/Classes:**
  * `run_with_alias` **(Many-Argument Workhorses)** (Impact: 12.6)
    * *Intent:* // same as the above function, but starts a plugin with a plugin alias
  * `run` **(Many-Argument Workhorses)** (Impact: 12.4)
  * `new` **(Compute Cores)** (Impact: 12.3)
  * `background_plugin_receives_broadcasts_regardless_of_active_tab` **(I/O & Config Routines)** (Impact: 12.3)
  * `integration_scrollback_from_pre_subscription_pty_bytes` **(Tests & Verification)** (Impact: 10.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 12 instances
* *Amplified Cascading Flux:* 25 instances
* *High Risk Execution (weighted view):* 24
* *Concurrency (weighted view):* 298
* *State Mutation (weighted view):* 262
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 149`, `structural_boundaries: 2153`, `args: 254`, `func_start: 199`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 463`, `high_risk_execution: 26`, `state_mutation: 212`, `fragile_debt: 1`, `unreferenced_by_name: 181`
* *Architecture:* `io: 1`, `api: 144`, `concurrency: 238`, `import: 36`
* *Defense:* `safety: 32`, `test: 411`, `sync_locks: 236`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.423
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ChannelWithContext, ClientId, ClientToServerMsg, CopyOptions, ErrorContext, EventType, FloatingPaneCoordinates, InputMode...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zellij-server/src/panes/tiled_panes/tiled_pane_grid.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1514.4 | **LOC:** 2362 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (25.6029%), Tech Debt (32.6681%)
**Top Internal Functions/Classes:**
  * `change_pane_size` **(Many-Argument Workhorses)** (Impact: 168.8)
    * *Intent:* /// Change a tiled panes size based on the given strategy. /// /// Returns true upon successful resi...
  * `contiguous_panes_with_alignment` **(Many-Argument Workhorses)** (Impact: 54.3)
    * *Intent:* /// Searches for contiguous panes
  * `can_change_pane_size` **(Many-Argument Workhorses)** (Impact: 53.4)
    * *Intent:* // Check if panes in the desired direction can be resized. Returns the maximum resize that's // poss...
  * `fill_geom_holes_horizontally_downwards` **(Many-Argument Workhorses)** (Impact: 38.3)
  * `fill_geom_holes_vertically_to_the_right` **(Many-Argument Workhorses)** (Impact: 38.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 104 instances
* *State Mutation (weighted view):* 326
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 440`, `structural_boundaries: 549`, `args: 240`, `func_start: 72`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 118`, `dead_code: 1`, `planned_debt: 4`, `unreferenced_by_name: 24`
* *Architecture:* `api: 35`, `import: 17`
* *Defense:* `safety: 70`, `doc: 9`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.423
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Direction, Direction::Down, Direction::Left, Direction::Right, Direction::Up, HashSet, MIN_TERMINAL_WIDTH, PaneGeom...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tests/e2e/cases.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 1513.92 | **LOC:** 2955 | **CtrlFlow:** 20.4% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (26.3668%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `mirrored_sessions` **(Compute Cores)** (Impact: 39.5)
  * `watcher_client_functionality` **(Compute Cores)** (Impact: 33.6)
  * `multiple_users_in_different_tabs` **(Compute Cores)** (Impact: 31.9)
  * `multiple_users_in_different_panes_and_same_tab` **(Compute Cores)** (Impact: 27.8)
  * `multiple_users_in_same_pane_and_tab` **(Compute Cores)** (Impact: 26.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 38 instances
* *Amplified Cascading Flux:* 102 instances
* *Concurrency (weighted view):* 269
* *State Mutation (weighted view):* 366
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 549`, `structural_boundaries: 665`, `args: 172`, `func_start: 45`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 162`, `fragile_debt: 1`, `unreferenced_by_name: 40`
* *Architecture:* `api: 89`, `concurrency: 79`, `import: 8`
* *Defense:* `test: 48`, `sync_locks: 13`, `immutability_locks: 47`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.423
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Line, Position, RemoteTerminal, Step, check_second_tab_opened, check_third_tab_is_left_wrapped, check_third_tab_is_right_wrapped, check_third_tab_moved_left...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zellij-server/src/tab/unit/tab_integration_tests.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 1507.28 | **LOC:** 14801 | **CtrlFlow:** 0.5% | **Authorship Centralization:** 85.0%
- **Risk Profile:** Cognitive Load (5.5456%), Tech Debt (30.8104%)
**Top Internal Functions/Classes:**
  * `create_new_tab_with_swap_layouts` **(Many-Argument Workhorses)** (Impact: 12.4)
  * `focus_follows_mouse_skips_stacked_one_liner_pane` **(I/O & Config Routines)** (Impact: 10.3)
  * `render_stacks_without_pane_frames` **(I/O & Config Routines)** (Impact: 9.7)
  * `start` **(Compute Cores)** (Impact: 8.2)
  * `non_overlapping_highlights_from_different_layers_coexist` **(Tests & Verification)** (Impact: 7.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Rce:* 1 instances
* *Amplified Cascading Flux:* 21 instances
* *High Risk Execution (weighted view):* 13
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 153
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 3086`, `args: 256`, `func_start: 247`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1565`, `high_risk_execution: 16`, `state_mutation: 111`, `unreferenced_by_name: 227`
* *Architecture:* `io: 2`, `api: 1`, `concurrency: 6`, `import: 44`
* *Defense:* `safety: 15`, `doc: 4`, `test: 434`, `sync_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.423
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ChannelWithContext, ClientId, ErrorContext, HashMap, HighlightStyle, InputMode, Ipv4Addr, Layout...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zellij-server/src/plugins/zellij_exports.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1506.96 | **LOC:** 5353 | **CtrlFlow:** 8.7% | **Authorship Centralization:** 86.7%
- **Risk Profile:** Cognitive Load (7.2445%), Tech Debt (8.6837%)
**Top Internal Functions/Classes:**
  * `host_run_plugin_command` **(Compute Cores)** (Impact: 70.6)
  * `switch_session` **(Many-Argument Workhorses)** (Impact: 23.7)
  * `get_pane_scrollback` **(Many-Argument Workhorses)** (Impact: 23.1)
  * `try_save_layout` **(Many-Argument Workhorses)** (Impact: 22.9)
  * `load_new_plugin` **(Many-Argument Workhorses)** (Impact: 20.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 12 instances
* *High Risk Execution (weighted view):* 1
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 412`, `structural_boundaries: 889`, `args: 609`, `func_start: 218`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 2`, `state_mutation: 20`, `dead_code: 1`, `planned_debt: 11`, `fragile_debt: 1`
* *Architecture:* `io: 9`, `api: 5`, `concurrency: 7`, `import: 52`
* *Defense:* `safety: 50`, `doc: 2`, `sync_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.482
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002584
  * `Imports (Out-Degree: 0):` BreakPanesToTabWithIdResponse, BreakPanesToTabWithIndexResponse, CommandToRun, CommandType, ConnectToSession, DeleteLayoutResponse, Direction, EditLayoutResponse...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `zellij-server/src/panes/tiled_panes/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1415.36 | **LOC:** 2800 | **CtrlFlow:** 13.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (13.0944%), Tech Debt (81.7174%)
**Top Internal Functions/Classes:**
  * `render` **(Many-Argument Workhorses)** (Impact: 120.9)
  * `stacked_resize_pane_with_id` **(Many-Argument Workhorses)** (Impact: 96.1)
  * `set_pane_frames` **(Compute Cores)** (Impact: 30.7)
  * `add_pane_with_stacked_resize` **(Many-Argument Workhorses)** (Impact: 25.8)
  * `toggle_pane_fullscreen` **(Compute Cores)** (Impact: 23.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 49 instances
* *State Mutation (weighted view):* 190
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 342`, `structural_boundaries: 642`, `args: 200`, `func_start: 128`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 66`, `state_mutation: 92`, `dead_code: 3`, `planned_debt: 7`, `unreferenced_by_name: 66`
* *Architecture:* `api: 114`, `import: 6`
* *Defense:* `safety: 116`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.423
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ClientId, HashMap, HashSet, MIN_TERMINAL_HEIGHT, MIN_TERMINAL_WIDTH, ModeInfo, Pane, PaneGeom...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zellij-server/src/route.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1413.88 | **LOC:** 3192 | **CtrlFlow:** 12.6% | **Authorship Centralization:** 84.4%
- **Risk Profile:** Cognitive Load (22.1137%), Tech Debt (9.985%)
**Top Internal Functions/Classes:**
  * `route_action` **(Many-Argument Workhorses)** (Impact: 708.4)
  * `route_thread_main` **(Many-Argument Workhorses)** (Impact: 179.9)
  * `build_tabs_table_row` **(Many-Argument Workhorses)** (Impact: 14.6)
  * `wait_for_action_completion` **(Many-Argument Workhorses)** (Impact: 14.2)
  * `build_table_row` **(Many-Argument Workhorses)** (Impact: 14.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 80 instances
* *State Mutation (weighted view):* 251
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 378`, `structural_boundaries: 283`, `args: 83`, `func_start: 40`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 91`, `dead_code: 2`, `unreferenced_by_name: 9`
* *Architecture:* `api: 18`, `concurrency: 5`, `import: 24`
* *Defense:* `safety: 72`, `test: 13`, `sync_locks: 3`, `immutability_locks: 1`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.423
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ClientToServerMsg, ConnectToSession, Direction, Event, ExitReason, HashSet, InputMode, IpcReceiverWithContext...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zellij-utils/src/data.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1350.3 | **LOC:** 3612 | **CtrlFlow:** 7.2% | **Authorship Centralization:** 84.4%
- **Risk Profile:** Cognitive Load (4.8573%), Tech Debt (91.2833%)
**Top Internal Functions/Classes:**
  * `new` **(Many-Argument Workhorses)** (Impact: 29.0)
  * `from_cli` **(Many-Argument Workhorses)** (Impact: 22.6)
  * `from_config` **(Compute Cores)** (Impact: 22.0)
  * `extract_text_by_columns` **(Many-Argument Workhorses)** (Impact: 15.4)
    * *Intent:* /// Extract text from a line between two column positions, accounting for wide characters
  * `eq` **(Compute Cores)** (Impact: 13.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 37 instances
* *State Mutation (weighted view):* 149
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 225`, `structural_boundaries: 426`, `args: 216`, `func_start: 181`, `class_start: 75`
* *Risk/State:* `state_mutation: 75`, `dead_code: 1`, `planned_debt: 3`, `fragile_debt: 2`, `unreferenced_by_name: 97`
* *Architecture:* `io: 3`, `api: 464`, `concurrency: 1`, `import: 21`
* *Defense:* `safety: 27`, `doc: 142`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.423
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` BTreeSet, EnumDiscriminants, EnumIter, EnumString, FromStr, HashMap, HashSet, Hasher...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zellij-utils/src/input/layout.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1230.66 | **LOC:** 2104 | **CtrlFlow:** 16.4% | **Authorship Centralization:** 77.8%
- **Risk Profile:** Cognitive Load (20.7083%), Tech Debt (9.4083%)
**Top Internal Functions/Classes:**
  * `split_space` **(Many-Argument Workhorses)** (Impact: 84.4)
  * `position_panes_in_space` **(Many-Argument Workhorses)** (Impact: 37.2)
  * `adjust_geoms_for_rounding_errors` **(Many-Argument Workhorses)** (Impact: 30.2)
  * `list_available_layouts` **(Defensive Guards)** (Impact: 27.0)
  * `truncate` **(Compute Cores)** (Impact: 22.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 68 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 243
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 313`, `structural_boundaries: 344`, `args: 179`, `func_start: 118`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 1`, `state_mutation: 107`, `dead_code: 5`, `planned_debt: 9`
* *Architecture:* `io: 7`, `api: 162`, `import: 12`
* *Defense:* `safety: 56`, `doc: 2`, `test: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.423
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ConfigError, Dimension, Formatter, LayoutInfo, LayoutMetadata, LayoutParsingError, LayoutWithError, PaneGeom...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zellij-server/src/pty.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1110.52 | **LOC:** 2262 | **CtrlFlow:** 14.5% | **Authorship Centralization:** 68.8%
- **Risk Profile:** Cognitive Load (14.4318%), Tech Debt (7.7512%)
**Top Internal Functions/Classes:**
  * `pty_thread_main` **(Many-Argument Workhorses)** (Impact: 186.8)
  * `spawn_terminals_for_layout` **(Many-Argument Workhorses)** (Impact: 183.9)
  * `spawn_terminals_for_layout_override` **(Many-Argument Workhorses)** (Impact: 131.9)
  * `apply_run_instruction` **(Many-Argument Workhorses)** (Impact: 72.9)
  * `spawn_terminal` **(Many-Argument Workhorses)** (Impact: 44.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 40 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 29
* *State Mutation (weighted view):* 129
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 311`, `structural_boundaries: 339`, `args: 122`, `func_start: 29`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 49`, `dead_code: 5`, `planned_debt: 1`
* *Architecture:* `api: 29`, `concurrency: 24`, `import: 13`
* *Defense:* `safety: 79`, `doc: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.423
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ClientId, Event, FloatingPaneCoordinates, GetPaneCwdResponse, GetPanePidResponse, GetPaneRunningCommandResponse, Layout, NewPanePlacement...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zellij-server/src/panes/tiled_panes/stacked_panes.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1009.12 | **LOC:** 1234 | **CtrlFlow:** 23.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.1067%), Tech Debt (57.6924%)
**Top Internal Functions/Classes:**
  * `combine_horizontally_aligned_panes_to_stack` **(Many-Argument Workhorses)** (Impact: 41.9)
  * `combine_vertically_aligned_panes_to_stack` **(Many-Argument Workhorses)** (Impact: 39.8)
  * `expand_pane` **(Compute Cores)** (Impact: 35.9)
  * `fill_space_over_visible_stacked_pane` **(Compute Cores)** (Impact: 28.2)
  * `resize_panes_in_stack` **(Many-Argument Workhorses)** (Impact: 26.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 84 instances
* *State Mutation (weighted view):* 296
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 286`, `structural_boundaries: 401`, `args: 115`, `func_start: 49`, `class_start: 1`
* *Risk/State:* `state_mutation: 128`, `dead_code: 3`, `planned_debt: 1`, `unreferenced_by_name: 22`
* *Architecture:* `api: 27`, `import: 5`
* *Defense:* `safety: 19`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.423
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` HashSet, MIN_TERMINAL_HEIGHT, PaneGeom, crate::
    panes::PaneId, pane_size::Dimension, std::cell::RefCell, std::collections::HashMap, std::rc::Rc...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zellij-server/src/output/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1000.2 | **LOC:** 1327 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 90.0%
- **Risk Profile:** Cognitive Load (35.5165%), Tech Debt (63.6736%)
**Top Internal Functions/Classes:**
  * `remove_covered_sixel_parts` **(Many-Argument Workhorses)** (Impact: 97.4)
  * `serialize_chunks` **(Many-Argument Workhorses)** (Impact: 75.9)
  * `remove_covered_parts` **(Many-Argument Workhorses)** (Impact: 41.2)
  * `serialize_chunks_with_newlines` **(Many-Argument Workhorses)** (Impact: 37.5)
  * `serialize_with_size` **(Many-Argument Workhorses)** (Impact: 36.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 74 instances
* *State Mutation (weighted view):* 257
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 226`, `structural_boundaries: 304`, `args: 83`, `func_start: 51`, `class_start: 6`
* *Risk/State:* `state_mutation: 109`, `dead_code: 3`, `planned_debt: 6`, `unreferenced_by_name: 22`
* *Architecture:* `api: 68`, `import: 12`
* *Defense:* `safety: 38`, `doc: 1`, `test: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.423
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CharacterStyles, ClientId, DEFAULT_STYLES, EMPTY_TERMINAL_CHARACTER, HashSet, PaneContents, PaneId, PaneRenderReport...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `default-plugins/session-manager/src/ui/components.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 988.48 | **LOC:** 1848 | **CtrlFlow:** 13.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (22.5591%), Tech Debt (40.7279%)
**Top Internal Functions/Classes:**
  * `render_unified_results` **(Many-Argument Workhorses)** (Impact: 169.7)
  * `render_controls_line` **(Many-Argument Workhorses)** (Impact: 54.1)
  * `render_new_session_block` **(Many-Argument Workhorses)** (Impact: 49.7)
  * `render_new_session_folder_prompt` **(Many-Argument Workhorses)** (Impact: 36.0)
  * `rebuild` **(Many-Argument Workhorses)** (Impact: 34.6)
    * *Intent:* /// Rebuild the cache from the current `unified_results`.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 53 instances
* *State Mutation (weighted view):* 178
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 220`, `structural_boundaries: 353`, `args: 64`, `func_start: 56`, `class_start: 12`
* *Risk/State:* `state_mutation: 72`, `planned_debt: 1`, `unreferenced_by_name: 23`
* *Architecture:* `api: 83`, `import: 11`
* *Defense:* `safety: 15`, `doc: 18`, `test: 12`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.423
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` NewSessionInfo, SessionUiInfo, TabUiInfo, crate::ActiveScreen, crate::single_screen::UnifiedSearchResult, crate::ui::PaneUiInfo, humantime::format_duration, std::path::PathBuf...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zellij-server/src/tab/mouse_handler.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 983.16 | **LOC:** 1689 | **CtrlFlow:** 22.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (16.9512%), Tech Debt (9.1257%)
**Top Internal Functions/Classes:**
  * `determine_mouse_action` **(Compute Cores)** (Impact: 137.3)
  * `edge_and_delta_to_strategies` **(Many-Argument Workhorses)** (Impact: 57.8)
  * `execute_send_to_terminal` **(Many-Argument Workhorses)** (Impact: 50.3)
  * `execute_mouse_action` **(Many-Argument Workhorses)** (Impact: 49.9)
  * `execute_update_hover` **(Many-Argument Workhorses)** (Impact: 38.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 32 instances
* *State Mutation (weighted view):* 97
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 340`, `structural_boundaries: 313`, `args: 84`, `func_start: 36`, `class_start: 7`
* *Risk/State:* `state_mutation: 33`, `unreferenced_by_name: 3`
* *Architecture:* `api: 24`, `import: 13`
* *Defense:* `safety: 63`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.423
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Direction::*, MouseEventType, Resize, Resize::*, ResizeStrategy, Tab, crate::ClientId, crate::background_jobs::BackgroundJob...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zellij-server/src/tab/unit/tab_tests.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 975.12 | **LOC:** 15590 | **CtrlFlow:** 0.1% | **Authorship Centralization:** 76.9%
- **Risk Profile:** Cognitive Load (4.899%), Tech Debt (46.7451%)
**Top Internal Functions/Classes:**
  * `toggle_focused_pane_fullscreen` **(Tests & Verification)** (Impact: 10.2)
  * `toggle_focused_pane_fullscreen_with_stacked_resizes` **(Tests & Verification)** (Impact: 8.2)
  * `close_pane_with_multiple_panes_to_the_left_away_from_screen_edges` **(I/O & Config Routines)** (Impact: 8.0)
  * `close_pane_with_multiple_panes_to_the_right_away_from_screen_edges` **(I/O & Config Routines)** (Impact: 8.0)
  * `create_new_tab_with_layout` **(Many-Argument Workhorses)** (Impact: 7.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 30
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 894`, `args: 158`, `func_start: 157`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1632`, `high_risk_execution: 15`, `state_mutation: 28`, `fragile_debt: 60`, `unreferenced_by_name: 139`
* *Architecture:* `io: 1`, `api: 120`, `concurrency: 3`, `import: 18`
* *Defense:* `safety: 1`, `test: 1326`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.423
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ClientId, Ipv4Addr, NewPanePlacement, Palette, Resize, ResizeStrategy, ServerToClientMsg, SizeInPixels...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zellij-utils/assets/prost_ipc/client_server_contract.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 974.18 | **LOC:** 3175 | **CtrlFlow:** 1.2% | **Authorship Centralization:** 90.6%
- **Risk Profile:** Cognitive Load (2.5956%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `as_str_name` **(State Mutators)** (Impact: 4.3)
    * *Intent:* /// String value of the enum field names used in the ProtoBuf definition. /// /// The values are not...
  * `from_str_name` **(State Mutators)** (Impact: 4.3)
    * *Intent:* /// Creates an enum from field names used in the ProtoBuf definition.
  * `as_str_name` **(State Mutators)** (Impact: 3.9)
    * *Intent:* /// String value of the enum field names used in the ProtoBuf definition. /// /// The values are not...
  * `from_str_name` **(State Mutators)** (Impact: 3.9)
    * *Intent:* /// Creates an enum from field names used in the ProtoBuf definition.
  * `as_str_name` **(State Mutators)** (Impact: 3.8)
    * *Intent:* /// String value of the enum field names used in the ProtoBuf definition. /// /// The values are not...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 289`, `args: 36`, `func_start: 36`, `class_start: 257`
* *Risk/State:* None
* *Architecture:* `api: 792`
* *Defense:* `doc: 144`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.423
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zellij-server/src/plugins/wasm_bridge.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 962.04 | **LOC:** 2316 | **CtrlFlow:** 9.8% | **Authorship Centralization:** 82.4%
- **Risk Profile:** Cognitive Load (11.4759%), Tech Debt (28.4068%)
**Top Internal Functions/Classes:**
  * `load_plugin` **(Many-Argument Workhorses)** (Impact: 56.7)
  * `apply_event_to_plugin` **(Many-Argument Workhorses)** (Impact: 53.0)
  * `apply_cached_events_and_resizes_for_plugin` **(Many-Argument Workhorses)** (Impact: 36.1)
  * `reconfigure` **(Many-Argument Workhorses)** (Impact: 35.6)
  * `get_or_load_plugins` **(Many-Argument Workhorses)** (Impact: 32.7)
    * *Intent:* // gets all running plugins details matching this run_plugin, if none are running, loads one and // ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 43 instances
* *State Mutation (weighted view):* 150
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 209`, `structural_boundaries: 441`, `args: 141`, `func_start: 59`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 66`, `state_mutation: 64`, `dead_code: 5`, `planned_debt: 3`, `fragile_debt: 2`, `unreferenced_by_name: 18`
* *Architecture:* `io: 2`, `api: 70`, `concurrency: 4`, `import: 25`
* *Defense:* `safety: 40`, `doc: 3`, `sync_locks: 86`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.423
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ClientId, Debouncer, EventType, FileIdMap, HashMap, HashSet, InputMode, LayoutInfo...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zellij-utils/src/ipc/protobuf_conversion.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 959.44 | **LOC:** 4458 | **CtrlFlow:** 11.8% | **Authorship Centralization:** 88.6%
- **Risk Profile:** Cognitive Load (8.8158%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `try_from` **(Compute Cores)** (Impact: 299.1)
  * `try_from` **(Compute Cores)** (Impact: 42.7)
  * `try_from` **(Defensive Guards)** (Impact: 33.1)
  * `try_from` **(Compute Cores)** (Impact: 26.4)
  * `try_from` **(Defensive Guards)** (Impact: 20.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 502`, `structural_boundaries: 265`, `args: 437`, `func_start: 94`
* *Risk/State:* None
* *Architecture:* `import: 53`
* *Defense:* `safety: 99`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.423
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ActionMsg, AttachClientMsg, AttachWatcherClientMsg, BackgroundColorMsg, CliPipeOutputMsg, ClientExitedMsg, ClientToServerMsg, ColorRegister...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `default-plugins/session-manager/src/main.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 950.8 | **LOC:** 1309 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (53.708%), Tech Debt (13.7365%)
**Top Internal Functions/Classes:**
  * `handle_selection` **(Compute Cores)** (Impact: 104.9)
  * `render` **(Many-Argument Workhorses)** (Impact: 99.7)
  * `handle_single_screen_search_key` **(Many-Argument Workhorses)** (Impact: 87.7)
  * `handle_attach_to_session` **(Many-Argument Workhorses)** (Impact: 83.3)
  * `handle_new_session_key` **(Compute Cores)** (Impact: 29.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 108 instances
* *State Mutation (weighted view):* 350
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 280`, `structural_boundaries: 172`, `args: 29`, `func_start: 21`, `class_start: 2`
* *Risk/State:* `state_mutation: 134`, `dead_code: 1`, `planned_debt: 1`, `unreferenced_by_name: 5`
* *Architecture:* `import: 8`
* *Defense:* `safety: 27`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.423
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Colors, SessionUiInfo, SingleScreenState, UnifiedSearchResult, new_session_info::NewSessionInfo, render_error, render_new_session_block, render_prompt...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `zellij-server/src/tab/mod.rs` -> Churn: **76.57%** | Cog Load: 19.996% | Debt: 97.5406%
- `zellij-utils/src/data.rs` -> Churn: **75.93%** | Cog Load: 4.8573% | Debt: 91.2833%
- `zellij-server/src/unit/screen_tests.rs` -> Churn: **74.57%** | Cog Load: 13.5404% | Debt: 76.6181%
- `zellij-utils/src/input/actions.rs` -> Churn: **69.9%** | Cog Load: 6.0935% | Debt: 79.0688%
- `zellij-server/src/panes/grid.rs` -> Churn: **68.09%** | Cog Load: 57.5894% | Debt: 45.9538%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `zellij-server/src/tab/mod.rs` -> **Aram Drevekenin** (93.9% isolated ownership) | Magnitude: 3744.2
- `zellij-server/src/panes/grid.rs` -> **Aram Drevekenin** (86.4% isolated ownership) | Magnitude: 3523.62
- `zellij-server/src/screen.rs` -> **Aram Drevekenin** (89.1% isolated ownership) | Magnitude: 3258.52
- `zellij-utils/src/kdl/mod.rs` -> **Aram Drevekenin** (83.3% isolated ownership) | Magnitude: 3016.6
- `zellij-server/src/plugins/unit/plugin_tests.rs` -> **Aram Drevekenin** (100.0% isolated ownership) | Magnitude: 1824.8

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `zellij-client/assets/input.js` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 99.866%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `zellij-utils/src/envs.rs` -> **Severity: 1.011** (Embedded: 0.0181 * Error Risk: 55.8935%)
- `zellij-client/assets/connection.js` -> **Severity: 0.659** (Embedded: 0.0078 * Error Risk: 85.0324%)
- `zellij-client/assets/links.js` -> **Severity: 0.55** (Embedded: 0.0058 * Error Risk: 94.6849%)
- `xtask/src/metadata.rs` -> **Severity: 0.535** (Embedded: 0.0103 * Error Risk: 51.8064%)
- `zellij-client/assets/input.js` -> **Severity: 0.477** (Embedded: 0.0052 * Error Risk: 92.3882%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `zellij-utils/src/envs.rs` -> **Severity: 1248.0** (Blast Radius: 15.808 * Doc Risk: 78.9474%)
- `xtask/src/flags.rs` -> **Severity: 616.8** (Blast Radius: 6.168 * Doc Risk: 100.0%)
- `zellij-utils/src/session_serialization.rs` -> **Severity: 594.636** (Blast Radius: 6.541 * Doc Risk: 90.9091%)
- `zellij-server/src/plugins/zellij_exports.rs` -> **Severity: 446.19** (Blast Radius: 4.482 * Doc Risk: 99.5516%)
- `zellij-utils/src/input/keybinds.rs` -> **Severity: 416.186** (Blast Radius: 4.482 * Doc Risk: 92.8571%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
