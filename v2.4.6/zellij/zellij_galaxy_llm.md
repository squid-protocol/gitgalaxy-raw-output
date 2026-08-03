# ARCHITECTURAL_BRIEF: zellij
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_rust/zellij` |
| **Timestamp** | `2026-08-03T19:48:09.691400+00:00` |
| **Scan Duration** | `3.53s` |
| **Git Branch** | `main` |
| **Git Commit** | `0532949bbdcee5116e91807ddb45a85d78a2aafc` |
| **Git Remote** | `https://github.com/zellij-org/zellij.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 303 malicious artifacts.

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
> **Architectural Drift Z-Score:** `5.419`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 218 | 63.4% |
| file_cluster_13 | 51 | 14.8% |
| file_cluster_0 | 23 | 6.7% |
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
| Cognitive Load Exposure | 0.0 | 100.0 | 16.8 | 12.0 | 0.0 |
| Error & Exception Exposure | 0.0 | 93.8 | 23.8 | 21.9 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 49.1 | 41.8 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 38.1 | 2.5 | 80.0 |
| API Exposure | 0.0 | 9.2 | 3.2 | 3.3 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 10.7 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 43.0 | 37.5 | 0.0 |
| Commented Logic Exposure | 0.0 | 99.5 | 2.2 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 94.7 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 12.4 | 1.8 | 0.6 | 0.0 |
| Volatility Exposure | 0.0 | 81.8 | 17.5 | 8.8 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 69.8 | 99.9 | 100.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 64.7 | 100.0 | 100.0 |
| Obfuscation & Evasion Surface | 0.0 | 28.1 | 0.1 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 20.0 | 10.7 | 19.8 | 20.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 2.5 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
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

- `continue_pane_resize_with_mouse` (@ `zellij-server/src/tab/mouse_handler.rs`) -> Impact: **4514.5** | LOC: 1070
- `try_from` (@ `zellij-utils/src/plugin_api/plugin_command.rs`) -> Impact: **3379.6** | LOC: 951
- `try_from` (@ `zellij-utils/src/plugin_api/action.rs`) -> Impact: **2987.6** | LOC: 952
- `populate_run_plugin_if_needed` (@ `zellij-utils/src/input/layout.rs`) -> Impact: **2529.2** | LOC: 1360
- `actions_from_cli` (@ `zellij-utils/src/input/actions.rs`) -> Impact: **2331.5** | LOC: 1237
- `route_action` (@ `zellij-server/src/route.rs`) -> Impact: **2166.1** | LOC: 1030
- `force_change_size` (@ `zellij-server/src/panes/grid.rs`) -> Impact: **1882.6** | LOC: 1252
- `try_from` (@ `zellij-utils/src/plugin_api/event.rs`) -> Impact: **1845.3** | LOC: 506
- `set_pane_frames` (@ `zellij-server/src/panes/tiled_panes/mod.rs`) -> Impact: **1833.1** | LOC: 1259
  * *Intent:* *self.display_area.borrow(),
- `render` (@ `zellij-server/src/panes/floating_panes/mod.rs`) -> Impact: **1726.2** | LOC: 628

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `clear_hover` (@ `default-plugins/about/src/pages.rs`) -> **O(2^N) [Recursive]**
- `handle_selection` (@ `default-plugins/about/src/pages.rs`) -> **O(2^N) [Recursive]**
- `find_predetermined_actions` (@ `default-plugins/compact-bar/src/keybind_utils.rs`) -> **O(2^N) [Recursive]**
  * *Intent:* /// Find predetermined actions based on predicates while maintaining order
- `render` (@ `default-plugins/configuration/src/main.rs`) -> **O(2^N) [Recursive]**
- `reconfigure` (@ `default-plugins/configuration/src/presets_screen.rs`) -> **O(2^N) [Recursive]**
- `render` (@ `default-plugins/session-manager/src/main.rs`) -> **O(2^N) [Recursive]**
- `update` (@ `default-plugins/session-manager/src/main.rs`) -> **O(2^N) [Recursive]**
- `render` (@ `default-plugins/session-manager/src/ui/components.rs`) -> **O(2^N) [Recursive]**
- `populate_tabs_in_tab_line` (@ `default-plugins/tab-bar/src/line.rs`) -> **O(2^N) [Recursive]**
  * *Intent:* // move elements from before_active and after_active into tabs_to_render while they fit in cols // adds collapsed_tabs to the left and right if there'...
- `mirrored_sessions` (@ `src/tests/e2e/cases.rs`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `finalize_and_apply` (@ `zellij-server/src/panes/hyperlink_tracker.rs`) -> DB Complexity: **197**
- `set_pane_frames` (@ `zellij-server/src/panes/tiled_panes/mod.rs`) -> DB Complexity: **94**
  * *Intent:* *self.display_area.borrow(),
- `force_change_size` (@ `zellij-server/src/panes/grid.rs`) -> DB Complexity: **88**
- `to_kdl` (@ `zellij-utils/src/kdl/mod.rs`) -> DB Complexity: **88**
- `populate_run_plugin_if_needed` (@ `zellij-utils/src/input/layout.rs`) -> DB Complexity: **76**
- `render` (@ `zellij-server/src/panes/floating_panes/mod.rs`) -> DB Complexity: **60**
- `start_server` (@ `zellij-server/src/lib.rs`) -> DB Complexity: **58**
- `cursor_visible_when_pinned_pane_is_focus` (@ `zellij-server/src/tab/unit/tab_integration_tests.rs`) -> DB Complexity: **40**
- `try_from` (@ `zellij-utils/src/kdl/mod.rs`) -> DB Complexity: **38**
- `remove_client` (@ `zellij-server/src/screen.rs`) -> DB Complexity: **37**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `zellij-server/src/panes` | 12 | 13967.92 | 30.54% | 67.64% |
| `zellij-utils/src/plugin_api` | 27 | 13894.34 | 6.52% | 44.26% |
| `zellij-server/src` | 15 | 13378.9 | 20.67% | 56.93% |
| `zellij-server/src/tab` | 6 | 11563.32 | 29.11% | 61.9% |
| `zellij-utils/src/input` | 13 | 9601.48 | 16.42% | 65.01% |
| `zellij-server/src/panes/tiled_panes` | 4 | 9055.28 | 39.38% | 43.57% |
| `zellij-utils/src` | 23 | 7306.42 | 11.08% | 61.77% |
| `zellij-utils/src/kdl` | 2 | 6137.34 | 18.7% | 14.68% |
| `zellij-server/src/plugins` | 9 | 5371.66 | 19.96% | 43.68% |
| `src/tests/e2e` | 4 | 4865.14 | 18.47% | 0.0% |

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
5. **`default-plugins/link/src/main.rs`** -> AI Confidence: **99.31%**
6. **`default-plugins/session-manager/src/main.rs`** -> AI Confidence: **99.31%**
7. **`default-plugins/strider/src/main.rs`** -> AI Confidence: **99.31%**
8. **`default-plugins/strider/src/state.rs`** -> AI Confidence: **99.31%**
9. **`src/commands.rs`** -> AI Confidence: **99.31%**
10. **`src/main.rs`** -> AI Confidence: **99.31%**
11. **`xtask/src/build.rs`** -> AI Confidence: **99.31%**
12. **`xtask/src/ci.rs`** -> AI Confidence: **99.31%**
13. **`xtask/src/pipelines.rs`** -> AI Confidence: **99.31%**
14. **`zellij-client/src/old_config_converter/convert_old_yaml_files.rs`** -> AI Confidence: **99.31%**
15. **`zellij-server/src/panes/floating_panes/floating_pane_grid.rs`** -> AI Confidence: **99.31%**
16. **`zellij-server/src/panes/grid.rs`** -> AI Confidence: **99.31%**
17. **`zellij-server/src/panes/search.rs`** -> AI Confidence: **99.31%**
18. **`zellij-server/src/panes/terminal_character.rs`** -> AI Confidence: **99.31%**
19. **`zellij-server/src/pty.rs`** -> AI Confidence: **99.31%**
20. **`zellij-server/src/pty_writer.rs`** -> AI Confidence: **99.31%**
21. **`zellij-server/src/route.rs`** -> AI Confidence: **99.31%**
22. **`zellij-server/src/screen.rs`** -> AI Confidence: **99.31%**
23. **`zellij-server/src/tab/mouse_handler.rs`** -> AI Confidence: **99.31%**
24. **`zellij-server/src/tab/swap_layouts.rs`** -> AI Confidence: **99.31%**
25. **`zellij-server/src/thread_bus.rs`** -> AI Confidence: **99.31%**
26. **`zellij-server/src/ui/components/text.rs`** -> AI Confidence: **99.31%**
27. **`zellij-server/src/ui/pane_contents_and_ui.rs`** -> AI Confidence: **99.31%**
28. **`zellij-utils/src/errors.rs`** -> AI Confidence: **99.31%**
29. **`zellij-utils/src/input/layout.rs`** -> AI Confidence: **99.31%**
30. **`zellij-utils/src/input/plugins.rs`** -> AI Confidence: **99.31%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `zellij-utils/src/vendored/termwiz/input.rs` -> **28.0967%** Exposure
### Exploit Generation Surface
- `default-plugins/about/src/active_component.rs` -> **20.0%** Exposure
- `default-plugins/about/src/main.rs` -> **20.0%** Exposure
- `default-plugins/about/src/pages.rs` -> **20.0%** Exposure
- `default-plugins/compact-bar/src/keybind_utils.rs` -> **20.0%** Exposure
- `default-plugins/compact-bar/src/line.rs` -> **20.0%** Exposure
### Weaponizable Injection Vectors
- `default-plugins/layout-manager/src/text_input.rs` -> **100.0%** Exposure
- `zellij-client/src/remote_attach/unit/remote_attach_tests.rs` -> **100.0%** Exposure
- `zellij-client/src/web_client/unit/web_client_tests.rs` -> **100.0%** Exposure
- `zellij-utils/src/web_authentication_tokens.rs` -> **100.0%** Exposure
- `zellij-utils/src/setup.rs` -> **99.9999%** Exposure
### Raw Memory Manipulation
- `src/tests/e2e/cases.rs` -> **0.0001%** Exposure
### Hardcoded Payload Artifacts
- `zellij-client/src/remote_attach/unit/remote_attach_tests.rs` -> **89.9376%** Exposure
### Algorithmic DoS Exposure
- `default-plugins/about/src/active_component.rs` -> **100.0%** Exposure
- `default-plugins/about/src/main.rs` -> **100.0%** Exposure
- `default-plugins/about/src/pages.rs` -> **100.0%** Exposure
- `default-plugins/compact-bar/src/keybind_utils.rs` -> **100.0%** Exposure
- `default-plugins/compact-bar/src/line.rs` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `4874` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `zellij-client/src/remote_attach/unit/remote_attach_tests.rs` (RUST) -> Cumulative Risk: **860.25**
- **Archetype:** `file_cluster_13` (Distance: 11.323 IQR)
- **Magnitude:** 347.16 | **LOC:** 952 | **CtrlFlow:** 8.8% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `handle_ws_terminal` (Impact: 35.1), `handle_ws_control` (Impact: 35.1), `call_attach_to_remote_session` (Impact: 19.5)

### 2. `zellij-server/src/terminal_bytes.rs` (RUST) -> Cumulative Risk: **850.51**
- **Archetype:** `file_cluster_4` (Distance: 14.008 IQR)
- **Magnitude:** 181.98 | **LOC:** 101 | **CtrlFlow:** 32.4% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `listen` (Impact: 128.5), `async_send_to_screen` (Impact: 16.6), `new` (Impact: 5.5)

### 3. `zellij-client/src/web_client/websocket_handlers.rs` (RUST) -> Cumulative Risk: **798.49**
- **Archetype:** `file_cluster_8` (Distance: 11.005 IQR)
- **Magnitude:** 241.58 | **LOC:** 278 | **CtrlFlow:** 25.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Concurrency (99.9986%)
- **Heaviest Functions:** `handle_ws_terminal` (Impact: 94.5), `handle_ws_control` (Impact: 82.7), `ws_handler_terminal` (Impact: 4.5)

### 4. `zellij-client/src/web_client/ipc_listener.rs` (RUST) -> Cumulative Risk: **792.47**
- **Archetype:** `file_cluster_4` (Distance: 12.49 IQR)
- **Magnitude:** 188.84 | **LOC:** 98 | **CtrlFlow:** 29.3% | **Authorship Centralization:** 75.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `listen_to_web_server_instructions` (Impact: 61.8), `create_webserver_receiver` (Impact: 16.3), `receive_webserver_instruction` (Impact: 11.4)

### 5. `zellij-client/src/unit/terminal_loop_tests.rs` (RUST) -> Cumulative Risk: **789.96**
- **Archetype:** `file_cluster_4` (Distance: 11.843 IQR)
- **Magnitude:** 477.14 | **LOC:** 776 | **CtrlFlow:** 10.2% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (99.9077%), Injection Surface (96.2967%)
- **Heaviest Functions:** `handle_websocket` (Impact: 82.0), `test_resize_signal_sends_control_message` (Impact: 25.3), `test_control_message_handling` (Impact: 18.2)

### 6. `zellij-client/src/remote_attach/websockets.rs` (RUST) -> Cumulative Risk: **771.8**
- **Archetype:** `file_cluster_13` (Distance: 12.918 IQR)
- **Magnitude:** 344.04 | **LOC:** 279 | **CtrlFlow:** 37.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Concurrency (99.8571%)
- **Heaviest Functions:** `establish_websocket_connections` (Impact: 106.4), `build_tls_config` (Impact: 62.1), `connect_ws` (Impact: 26.8)

### 7. `zellij-client/src/os_input_output_windows.rs` (RUST) -> Cumulative Risk: **770.58**
- **Archetype:** `file_cluster_13` (Distance: 13.741 IQR)
- **Magnitude:** 278.58 | **LOC:** 250 | **CtrlFlow:** 39.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `next` (Impact: 130.1), `recv` (Impact: 57.1), `new` (Impact: 14.4)

### 8. `zellij-server/src/os_input_output_unix.rs` (RUST) -> Cumulative Risk: **760.48**
- **Archetype:** `file_cluster_13` (Distance: 13.752 IQR)
- **Magnitude:** 785.08 | **LOC:** 560 | **CtrlFlow:** 40.4% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Concurrency (98.0299%)
- **Heaviest Functions:** `handle_openpty` (Impact: 122.0), `handle_command_exit` (Impact: 116.0), `read` (Impact: 84.1)

### 9. `zellij-server/src/plugins/plugin_map.rs` (RUST) -> Cumulative Risk: **751.22**
- **Archetype:** `file_cluster_13` (Distance: 11.57 IQR)
- **Magnitude:** 120.6 | **LOC:** 418 | **CtrlFlow:** 11.4% | **Authorship Centralization:** 80.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), State Flux (99.8822%)
- **Heaviest Functions:** `next_event_id` (Impact: 21.5), `apply_event_id` (Impact: 12.4), `new` (Impact: 9.4)

### 10. `zellij-client/src/stdin_handler.rs` (RUST) -> Cumulative Risk: **740.36**
- **Archetype:** `file_cluster_4` (Distance: 11.694 IQR)
- **Magnitude:** 397.82 | **LOC:** 292 | **CtrlFlow:** 37.4% | **Authorship Centralization:** 40.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.787%)
- **Heaviest Functions:** `stdin_loop` (Impact: 298.2), `finalize_events` (Impact: 33.1), `send_done_parsing_after_query_timeout` (Impact: 10.7)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `zellij-server/src/panes/grid.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.399 IQR)
- **Top Global Matches:** file_cluster_8: 14.399, file_cluster_11: 14.419, file_cluster_13: 14.435
- **Magnitude:** 5330.36 | **LOC:** 4798 | **CtrlFlow:** 49.0% | **Authorship Centralization:** 82.6%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 88
- **Risk Profile:** Cognitive Load (46.2976%), Tech Debt (66.3931%)
**Top Internal Functions/Classes:**
  * `force_change_size` (Impact: 1882.6 | O(N^6) | DB: 88)
  * `csi_dispatch` (Impact: 752.6 | O(N^6) | DB: 28)
  * `osc_dispatch` (Impact: 396.2 | O(N^6) | DB: 3)
  * `fmt` (Impact: 171.9 | O(2^N) | DB: 4)
  * `transfer_rows_from_lines_above_to_viewpo` (Impact: 104.0 | O(N^6) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 605`, `structural_boundaries: 630`, `args: 162`, `func_start: 137`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 537`, `dead_code: 6`, `planned_debt: 17`, `fragile_debt: 4`, `duplicate_logic: 2`, `orphaned_logic: 41`
* *Architecture:* `api: 145`, `import: 26`
* *Defense:* `safety: 437`, `doc: 61`, `test: 1`, `immutability_locks: 3`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` TerminalCharacter, MouseEventType, CharsetIndex, Style, collections::BTreeSet, crate::panes::Selection, zellij_utils::data::PaneContents, RegexHighlight...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zellij-server/src/tab/mouse_handler.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.702 IQR)
- **Top Global Matches:** file_cluster_8: 12.702, file_cluster_13: 13.036, file_cluster_0: 13.058
- **Magnitude:** 5028.46 | **LOC:** 1689 | **CtrlFlow:** 53.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 29
- **Risk Profile:** Cognitive Load (30.8715%), Tech Debt (9.26%)
**Top Internal Functions/Classes:**
  * `continue_pane_resize_with_mouse` (Impact: 4514.5 | O(2^N) | DB: 29)
  * `edge_and_delta_to_strategies` (Impact: 151.1 | O(N^4) | DB: 4)
  * `start_pane_resize_with_mouse` (Impact: 54.7 | O(N^4) | DB: 1)
  * `gather_clicked_pane_details` (Impact: 47.0 | O(N^3) | DB: 1)
  * `gather_mouse_event_context` (Impact: 41.8 | O(N^4) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 334`, `structural_boundaries: 292`, `args: 76`, `func_start: 32`, `class_start: 7`
* *Risk/State:* `state_mutation: 100`, `orphaned_logic: 3`
* *Architecture:* `api: 24`, `import: 13`
* *Defense:* `safety: 291`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` MouseEventType, std::time::Instant, crate::background_jobs::BackgroundJob, zellij_utils::position::Position, zellij_utils::data::Direction, Tab, zellij_utils::input::mouse::MouseEvent, ResizeStrategy...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zellij-utils/src/plugin_api/plugin_command.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.896 IQR)
- **Top Global Matches:** file_cluster_8: 14.896, file_cluster_17: 15.15, file_cluster_16: 15.293
- **Magnitude:** 4960.4 | **LOC:** 4886 | **CtrlFlow:** 72.0% | **Authorship Centralization:** 88.9%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (10.5742%), Tech Debt (98.2252%)
**Top Internal Functions/Classes:**
  * `try_from` (Impact: 3379.6 | O(2^N))
  * `try_from` (Impact: 662.0 | O(2^N))
  * `from` (Impact: 36.8 | O(2^N))
  * `into` (Impact: 32.8 | O(N^6))
  * `from` (Impact: 29.3 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 728`, `structural_boundaries: 283`, `args: 260`, `func_start: 85`
* *Risk/State:* `safety_bypasses: 24`, `planned_debt: 1`, `duplicate_logic: 83`
* *Architecture:* `api: 1`, `import: 8`
* *Defense:* `safety: 2087`, `immutability_locks: 52`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` plugin_command::Payload, RunCommandPayload, GetPanePidPayload, OpenTerminalResponse, OpenTerminalInPlaceOfPluginPayload, PaneId, OpenEditPaneInPlaceOfPaneIdPayload, SaveSessionResponse...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zellij-server/src/tab/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.434 IQR)
- **Top Global Matches:** file_cluster_8: 14.434, file_cluster_17: 14.571, file_cluster_11: 14.6
- **Magnitude:** 4836.62 | **LOC:** 6061 | **CtrlFlow:** 46.2% | **Authorship Centralization:** 94.1%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (27.4659%), Tech Debt (99.4741%)
**Top Internal Functions/Classes:**
  * `override_layout` (Impact: 272.1 | O(2^N) | DB: 7)
  * `suppress_pane_and_replace_with_pid` (Impact: 217.4 | O(N^6) | DB: 3)
  * `new_no_preference_pane` (Impact: 191.2 | O(N^6) | DB: 2)
  * `new_stacked_pane` (Impact: 187.5 | O(N^6) | DB: 2)
  * `apply_layout` (Impact: 186.7 | O(2^N) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 406`, `structural_boundaries: 473`, `args: 332`, `func_start: 239`, `class_start: 4`
* *Risk/State:* `state_mutation: 337`, `dead_code: 3`, `planned_debt: 25`, `fragile_debt: 3`, `duplicate_logic: 4`, `orphaned_logic: 123`
* *Architecture:* `io: 1`, `api: 91`, `import: 31`
* *Defense:* `safety: 554`, `doc: 5`, `immutability_locks: 3`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pty::ClientTabIndexOrPaneId, std::net::IpAddr, PaneId, RegexHighlight, std::env::temp_dir, zellij_utils::errors::prelude::*, copy_command::CopyCommand, self::clipboard::ClipboardProvider...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zellij-utils/src/plugin_api/action.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.124 IQR)
- **Top Global Matches:** file_cluster_8: 14.124, file_cluster_16: 14.361, file_cluster_17: 14.386
- **Magnitude:** 4526.08 | **LOC:** 3201 | **CtrlFlow:** 51.0% | **Authorship Centralization:** 88.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (10.718%), Tech Debt (99.7887%)
**Top Internal Functions/Classes:**
  * `try_from` (Impact: 2987.6 | O(2^N))
  * `try_from` (Impact: 505.2 | O(2^N) | DB: 4)
  * `try_from` (Impact: 71.8 | O(N^6))
  * `try_from` (Impact: 59.2 | O(N^6) | DB: 1)
  * `try_from` (Impact: 52.0 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 438`, `structural_boundaries: 420`, `args: 162`, `func_start: 71`
* *Risk/State:* `state_mutation: 24`, `planned_debt: 1`, `duplicate_logic: 71`
* *Architecture:* `api: 1`, `import: 34`
* *Defense:* `safety: 1201`, `immutability_locks: 103`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` PluginUserConfiguration, MouseEventType, std::convert::TryFrom, super::generated_api::api::action::pane_run::RunType, SplitDirection, crate::input::command::OpenFilePayload, NewPanePlacement, RunPluginLocation...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zellij-utils/src/input/layout.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.108 IQR)
- **Top Global Matches:** file_cluster_0: 14.108, file_cluster_17: 14.18, file_cluster_11: 14.213
- **Magnitude:** 4037.38 | **LOC:** 2104 | **CtrlFlow:** 48.5% | **Authorship Centralization:** 80.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 76
- **Risk Profile:** Cognitive Load (38.7058%), Tech Debt (35.8868%)
**Top Internal Functions/Classes:**
  * `populate_run_plugin_if_needed` (Impact: 2529.2 | O(2^N) | DB: 76)
  * `split_space` (Impact: 582.6 | O(2^N) | DB: 12)
  * `populate_plugin_aliases_in_layout` (Impact: 123.0 | O(2^N) | DB: 5)
  * `adjust_geoms_for_rounding_errors` (Impact: 106.2 | O(N^6) | DB: 3)
  * `pane_count` (Impact: 44.1 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 290`, `structural_boundaries: 308`, `args: 116`, `func_start: 102`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 242`, `dead_code: 5`, `planned_debt: 9`, `duplicate_logic: 7`
* *Architecture:* `io: 7`, `api: 147`, `import: 14`
* *Defense:* `safety: 465`, `doc: 2`, `test: 1`, `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` LayoutInfo, std::cmp::Ordering, super::plugins::PluginAliases, ConfigError, std::
    fmt, PathBuf, std::str::FromStr, crate::
    data::Direction...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/tests/e2e/cases.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.249 IQR)
- **Top Global Matches:** file_cluster_8: 12.249, file_cluster_0: 12.521, file_cluster_4: 12.561
- **Magnitude:** 3893.78 | **LOC:** 2955 | **CtrlFlow:** 46.2% | **Authorship Centralization:** 75.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (32.5611%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `mirrored_sessions` (Impact: 395.5 | O(2^N) | DB: 16)
  * `multiple_users_in_different_tabs` (Impact: 332.3 | O(2^N) | DB: 9)
  * `watcher_client_functionality` (Impact: 289.5 | O(2^N) | DB: 9)
  * `send_blocking_command_through_the_cli` (Impact: 271.7 | O(2^N) | DB: 8)
  * `multiple_users_in_same_pane_and_tab` (Impact: 271.2 | O(2^N) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 354`, `structural_boundaries: 413`, `args: 101`, `func_start: 26`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 469`, `fragile_debt: 1`, `orphaned_logic: 17`
* *Architecture:* `api: 71`, `concurrency: 84`, `import: 8`
* *Defense:* `test: 26`, `sync_locks: 9`, `immutability_locks: 47`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::tests::e2e::steps::
    check_focus_on_second_tab, check_third_tab_is_left_wrapped, switch_focus_to_left_tab, insta::assert_snapshot, RemoteTerminal, type_second_tab_content, move_tab_right, Position...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zellij-utils/src/plugin_api/event.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.486 IQR)
- **Top Global Matches:** file_cluster_8: 13.486, file_cluster_17: 13.544, file_cluster_16: 13.715
- **Magnitude:** 3751.58 | **LOC:** 3041 | **CtrlFlow:** 40.7% | **Authorship Centralization:** 91.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 19
- **Risk Profile:** Cognitive Load (13.5416%), Tech Debt (99.1824%)
**Top Internal Functions/Classes:**
  * `try_from` (Impact: 1845.3 | O(2^N) | DB: 8)
  * `try_from` (Impact: 571.8 | O(2^N) | DB: 19)
  * `try_from` (Impact: 128.9 | O(2^N) | DB: 3)
  * `try_from` (Impact: 121.5 | O(N^6))
  * `try_from` (Impact: 111.7 | O(2^N) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 325`, `structural_boundaries: 473`, `args: 168`, `func_start: 77`
* *Risk/State:* `safety_bypasses: 67`, `state_mutation: 131`, `planned_debt: 1`, `duplicate_logic: 57`
* *Architecture:* `io: 1`, `api: 21`, `import: 35`
* *Defense:* `safety: 594`, `test: 44`, `immutability_locks: 86`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` LayoutInfo, PaneManifest, AvailableLayoutInfoPayload, FileMetadata, CwdChangedPayload, Style, std::convert::TryFrom, std::net::IpAddr...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zellij-server/src/panes/tiled_panes/tiled_pane_grid.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.511 IQR)
- **Top Global Matches:** file_cluster_17: 13.511, file_cluster_8: 13.606, file_cluster_11: 13.841
- **Magnitude:** 3494.96 | **LOC:** 2362 | **CtrlFlow:** 44.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (33.8014%), Tech Debt (36.0273%)
**Top Internal Functions/Classes:**
  * `fill_geom_holes_horizontally_downwards` (Impact: 232.4 | O(2^N) | DB: 12)
  * `fill_geom_holes_vertically_to_the_right` (Impact: 232.4 | O(2^N) | DB: 12)
  * `fill_geom_holes_horizontally_upwards` (Impact: 232.2 | O(2^N) | DB: 12)
  * `fill_geom_holes_vertically_to_the_left` (Impact: 232.2 | O(2^N) | DB: 12)
  * `contiguous_panes_with_alignment` (Impact: 199.8 | O(N^6) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 423`, `structural_boundaries: 531`, `args: 244`, `func_start: 70`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 418`, `dead_code: 1`, `planned_debt: 4`, `orphaned_logic: 25`
* *Architecture:* `api: 33`, `import: 16`
* *Defense:* `safety: 328`, `doc: 9`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pane_size::Dimension, std::cmp::Ordering, Direction::Up, Resize, Direction::Down, super::pane_resizer::PaneResizer, Direction::Left, Reverse...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zellij-utils/src/kdl/kdl_layout_parser.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.219 IQR)
- **Top Global Matches:** file_cluster_8: 13.219, file_cluster_17: 13.464, file_cluster_0: 13.695
- **Magnitude:** 3464.56 | **LOC:** 2602 | **CtrlFlow:** 56.9% | **Authorship Centralization:** 75.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (18.2466%), Tech Debt (15.571%)
**Top Internal Functions/Classes:**
  * `parse_floating_pane_node_with_template` (Impact: 241.7 | O(N^5) | DB: 3)
  * `differentiate_pane_and_floating_pane_tem` (Impact: 202.2 | O(N^5) | DB: 2)
  * `parse_pane_node_with_template` (Impact: 181.0 | O(N^6) | DB: 3)
  * `parse_pane_template_node` (Impact: 144.2 | O(N^6) | DB: 1)
  * `parse_tab_template_node` (Impact: 143.2 | O(N^6) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 463`, `structural_boundaries: 351`, `args: 174`, `func_start: 54`, `class_start: 2`
* *Risk/State:* `state_mutation: 116`, `orphaned_logic: 15`
* *Architecture:* `io: 2`, `api: 7`, `import: 7`
* *Defense:* `safety: 446`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` PluginUserConfiguration, Layout, SplitDirection, kdl_first_entry_as_i64, kdl_property_names, kdl_get_string_property_or_child_value, kdl_string_arguments, SplitSize...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zellij-server/src/route.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.813 IQR)
- **Top Global Matches:** file_cluster_8: 12.813, file_cluster_13: 13.171, file_cluster_0: 13.218
- **Magnitude:** 3253.86 | **LOC:** 3192 | **CtrlFlow:** 55.1% | **Authorship Centralization:** 84.8%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 25
- **Risk Profile:** Cognitive Load (14.6396%), Tech Debt (9.2064%)
**Top Internal Functions/Classes:**
  * `route_action` (Impact: 2166.1 | O(N^6) | DB: 8)
  * `route_thread_main` (Impact: 852.8 | O(N^6) | DB: 25)
  * `wait_for_action_completion` (Impact: 57.0 | O(N^6))
  * `drop` (Impact: 10.6 | O(N^4) | DB: 1)
  * `clone` (Impact: 7.5 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 247`, `structural_boundaries: 201`, `args: 42`, `func_start: 40`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 71`, `dead_code: 2`, `orphaned_logic: 4`
* *Architecture:* `api: 18`, `concurrency: 5`, `import: 24`
* *Defense:* `safety: 340`, `test: 13`, `sync_locks: 3`, `immutability_locks: 1`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` SearchDirection, pty::ClientTabIndexOrPaneId, NewPanePlacement, keybinds::Keybinds, ServerToClientMsg, zellij_utils::data::GetPaneCwdResponse, zellij_utils::
    channels::SenderWithContext, UnblockCondition...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zellij-utils/src/ipc/protobuf_conversion.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.393 IQR)
- **Top Global Matches:** file_cluster_8: 13.393, file_cluster_17: 13.684, file_cluster_16: 13.961
- **Magnitude:** 3025.84 | **LOC:** 4458 | **CtrlFlow:** 65.4% | **Authorship Centralization:** 88.6%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (8.8158%), Tech Debt (90.715%)
**Top Internal Functions/Classes:**
  * `try_from` (Impact: 1131.1 | O(N^6))
  * `try_from` (Impact: 187.9 | O(N^6))
  * `try_from` (Impact: 144.8 | O(N^6))
  * `try_from` (Impact: 86.9 | O(N^5))
  * `try_from` (Impact: 80.9 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 502`, `structural_boundaries: 265`, `args: 437`, `func_start: 94`
* *Risk/State:* `duplicate_logic: 81`
* *Architecture:* `import: 53`
* *Defense:* `safety: 639`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` data::InputMode, AttachWatcherClientMsg, FirstClientConnectedMsg, TiledPlacement, RunPluginLocation, PaneId, ClientExitedMsg, SubscribeToPaneRendersMsg...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zellij-server/src/screen.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.634 IQR)
- **Top Global Matches:** file_cluster_13: 14.634, file_cluster_8: 14.695, file_cluster_17: 14.729
- **Magnitude:** 2962.56 | **LOC:** 9125 | **CtrlFlow:** 51.9% | **Authorship Centralization:** 89.1%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 37
- **Risk Profile:** Cognitive Load (16.028%), Tech Debt (10.082%)
**Top Internal Functions/Classes:**
  * `remove_client` (Impact: 951.4 | O(N^6) | DB: 37)
  * `apply_layout` (Impact: 900.7 | O(2^N) | DB: 2)
  * `switch_active_tab` (Impact: 199.4 | O(N^6) | DB: 1)
  * `add_client` (Impact: 122.0 | O(2^N) | DB: 3)
  * `new_tab` (Impact: 81.4 | O(N^4) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 292`, `structural_boundaries: 271`, `args: 96`, `func_start: 37`, `class_start: 2`
* *Risk/State:* `state_mutation: 151`, `dead_code: 3`, `planned_debt: 9`
* *Architecture:* `io: 1`, `api: 48`, `import: 29`
* *Defense:* `safety: 348`, `doc: 109`, `test: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` tab::SuppressedPanes, std::net::IpAddr, RegexHighlight, zellij_utils::errors::prelude::*, EventType, Styling, PaneContents, crate::session_layout_metadata::PaneLayoutMetadata...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zellij-server/src/plugins/zellij_exports.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.633 IQR)
- **Top Global Matches:** file_cluster_8: 12.633, file_cluster_17: 13.066, file_cluster_13: 13.202
- **Magnitude:** 2743.1 | **LOC:** 5353 | **CtrlFlow:** 32.6% | **Authorship Centralization:** 86.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (7.3548%), Tech Debt (24.7365%)
**Top Internal Functions/Classes:**
  * `host_run_plugin_command` (Impact: 235.7 | O(N^6) | DB: 5)
  * `open_plugin_pane_floating` (Impact: 110.3 | O(2^N))
  * `open_plugin_pane_in_new_tab` (Impact: 104.5 | O(2^N))
  * `load_new_plugin` (Impact: 92.2 | O(N^6))
  * `get_pane_scrollback` (Impact: 78.2 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 281`, `structural_boundaries: 581`, `args: 405`, `func_start: 118`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 51`, `dead_code: 1`, `planned_debt: 11`, `fragile_debt: 1`, `duplicate_logic: 10`
* *Architecture:* `io: 4`, `api: 7`, `concurrency: 7`, `import: 34`
* *Defense:* `safety: 374`, `doc: 2`, `sync_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 5.127
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002899
  * `Imports (Out-Degree: 0):` crate::pty::ClientTabIndexOrPaneId, log::warn, ProtobufParseLayoutResponse, ProtobufOpenPluginPaneFloatingResponse, OpenTerminalResponse, zellij_utils::plugin_api::plugin_command::EnvVariable, ProtobufOpenCommandPaneFloatingResponse, std::time::SystemTime...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `zellij-utils/src/input/actions.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.361 IQR)
- **Top Global Matches:** file_cluster_8: 13.361, file_cluster_0: 13.535, file_cluster_7: 13.774
- **Magnitude:** 2717.46 | **LOC:** 3874 | **CtrlFlow:** 39.5% | **Authorship Centralization:** 87.5%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (5.1425%), Tech Debt (58.3831%)
**Top Internal Functions/Classes:**
  * `actions_from_cli` (Impact: 2331.5 | O(2^N) | DB: 1)
  * `test_switch_session_with_layout_string` (Impact: 14.2 | O(N^4))
  * `test_new_pane_tiled_with_tab_id` (Impact: 12.4 | O(N^3))
  * `test_new_pane_tiled_without_tab_id` (Impact: 12.4 | O(N^3))
  * `test_new_pane_floating_with_tab_id` (Impact: 12.4 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 202`, `structural_boundaries: 310`, `args: 120`, `func_start: 92`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 82`, `state_mutation: 3`, `planned_debt: 4`, `duplicate_logic: 6`, `orphaned_logic: 28`
* *Architecture:* `api: 7`, `import: 16`
* *Defense:* `safety: 696`, `doc: 74`, `test: 344`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` OriginatingPlugin, Layout, LayoutInfo, ConfigError, RunPluginLocation, NewPanePlacement, PaneId, crate::cli::CliAction...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zellij-utils/src/kdl/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.121 IQR)
- **Top Global Matches:** file_cluster_8: 13.121, file_cluster_17: 13.487, file_cluster_0: 13.498
- **Magnitude:** 2672.78 | **LOC:** 7185 | **CtrlFlow:** 34.9% | **Authorship Centralization:** 83.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 88
- **Risk Profile:** Cognitive Load (19.1508%), Tech Debt (13.7947%)
**Top Internal Functions/Classes:**
  * `try_from` (Impact: 951.4 | O(N^6) | DB: 38)
  * `to_kdl` (Impact: 660.1 | O(N^6) | DB: 88)
  * `try_from` (Impact: 213.6 | O(N^5) | DB: 3)
  * `new_from_string` (Impact: 172.6 | O(N^6) | DB: 2)
  * `new_from_bytes` (Impact: 32.9 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 329`, `structural_boundaries: 614`, `args: 171`, `func_start: 28`, `class_start: 271`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 411`, `dead_code: 6`, `planned_debt: 5`, `duplicate_logic: 7`
* *Architecture:* `io: 1`, `api: 21`, `import: 24`
* *Defense:* `safety: 462`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` PluginUserConfiguration, LayoutInfo, SearchDirection, PaneManifest, Themes, ConfigError, std::net::IpAddr, PaneId...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zellij-server/src/panes/tiled_panes/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.194 IQR)
- **Top Global Matches:** file_cluster_17: 13.194, file_cluster_8: 13.21, file_cluster_0: 13.388
- **Magnitude:** 2639.6 | **LOC:** 2800 | **CtrlFlow:** 33.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 94
- **Risk Profile:** Cognitive Load (35.0573%), Tech Debt (43.4896%)
**Top Internal Functions/Classes:**
  * `set_pane_frames` (Impact: 1833.1 | O(2^N) | DB: 94)
    * *Intent:* *self.display_area.borrow(),
  * `add_pane_without_stacked_resize` (Impact: 88.3 | O(2^N) | DB: 4)
  * `relayout` (Impact: 35.7 | O(2^N) | DB: 3)
  * `add_pane` (Impact: 34.1 | O(N^4) | DB: 1)
  * `add_pane_to_stack_of_active_pane` (Impact: 32.4 | O(N^4) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 188`, `structural_boundaries: 381`, `args: 142`, `func_start: 91`
* *Risk/State:* `safety_bypasses: 53`, `state_mutation: 233`, `dead_code: 3`, `planned_debt: 7`, `orphaned_logic: 20`
* *Architecture:* `api: 84`, `import: 6`
* *Defense:* `safety: 231`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::
    cell::RefCell, RESIZE_PERCENT, Style, SplitDirection, collections::BTreeMap, PaneId, Resize, ClientId...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zellij-server/src/tab/unit/tab_integration_tests.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.688 IQR)
- **Top Global Matches:** file_cluster_8: 12.688, file_cluster_0: 13.002, file_cluster_13: 13.219
- **Magnitude:** 2509.4 | **LOC:** 14801 | **CtrlFlow:** 4.7% | **Authorship Centralization:** 85.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 40
- **Risk Profile:** Cognitive Load (9.366%), Tech Debt (26.2476%)
**Top Internal Functions/Classes:**
  * `cursor_visible_when_pinned_pane_is_focus` (Impact: 412.9 | O(N^6) | DB: 40)
  * `start` (Impact: 36.1 | O(N^6) | DB: 1)
  * `increase_tiled_pane_sizes_with_stacked_r` (Impact: 26.5 | O(N^3) | DB: 5)
  * `create_new_tab_with_swap_layouts` (Impact: 22.5 | O(N^2) | DB: 11)
  * `cannot_decrease_stack_size_beyond_minimu` (Impact: 17.7 | O(N^6) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 112`, `structural_boundaries: 2256`, `args: 181`, `func_start: 175`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1085`, `high_risk_execution: 2`, `state_mutation: 565`, `duplicate_logic: 9`, `orphaned_logic: 128`
* *Architecture:* `io: 2`, `api: 1`, `concurrency: 11`, `import: 43`
* *Defense:* `safety: 2031`, `doc: 4`, `test: 254`, `sync_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Layout, input::command::RunCommand, Style, ipc::ClientToServerMsg, NewPanePlacement, ServerToClientMsg, std::net::IpAddr, std::sync::Mutex...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zellij-server/src/panes/unit/grid_tests.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.172 IQR)
- **Top Global Matches:** file_cluster_0: 14.172, file_cluster_8: 14.27, file_cluster_17: 14.375
- **Magnitude:** 2501.1 | **LOC:** 5688 | **CtrlFlow:** 12.7% | **Authorship Centralization:** 83.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (32.6699%), Tech Debt (91.0372%)
**Top Internal Functions/Classes:**
  * `sixel_with_image_scrolling_decsdm` (Impact: 34.9 | O(N^2) | DB: 17)
  * `cursor_hide_persists_through_alternate_s` (Impact: 26.4 | O(N^2) | DB: 11)
  * `sixel_image_in_alternate_buffer` (Impact: 23.4 | O(N^2) | DB: 10)
  * `preserve_background_color_on_resize` (Impact: 18.3 | O(N^3) | DB: 12)
  * `vim_scroll_region_down` (Impact: 17.7 | O(2^N) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 223`, `structural_boundaries: 1539`, `args: 173`, `func_start: 149`
* *Risk/State:* `safety_bypasses: 25`, `high_risk_execution: 1`, `state_mutation: 1060`, `dead_code: 1`, `fragile_debt: 3`, `duplicate_logic: 6`, `orphaned_logic: 113`
* *Architecture:* `io: 1`, `api: 20`, `import: 21`
* *Defense:* `safety: 1089`, `test: 304`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Style, super::super::Grid, insta::assert_snapshot, RegexHighlight, zellij_utils::
    data::Palette, zellij_utils::data::HighlightLayer, HighlightStyle, crate::panes::terminal_character::AnsiCode...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zellij-server/src/panes/tiled_panes/stacked_panes.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.295 IQR)
- **Top Global Matches:** file_cluster_17: 13.295, file_cluster_8: 13.375, file_cluster_11: 13.56
- **Magnitude:** 2491.54 | **LOC:** 1234 | **CtrlFlow:** 41.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (59.6527%), Tech Debt (57.6353%)
**Top Internal Functions/Classes:**
  * `fill_space_over_visible_stacked_pane` (Impact: 132.2 | O(2^N) | DB: 5)
  * `combine_horizontally_aligned_panes_to_st` (Impact: 131.3 | O(N^5) | DB: 10)
  * `combine_vertically_aligned_panes_to_stac` (Impact: 124.5 | O(N^5) | DB: 10)
  * `fill_space_over_one_liner_pane_above_fle` (Impact: 105.6 | O(2^N) | DB: 5)
  * `fill_space_over_one_liner_pane_below_fle` (Impact: 105.6 | O(2^N) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 287`, `structural_boundaries: 401`, `args: 115`, `func_start: 49`, `class_start: 1`
* *Risk/State:* `state_mutation: 366`, `dead_code: 3`, `planned_debt: 1`, `orphaned_logic: 22`
* *Architecture:* `api: 27`, `import: 5`
* *Defense:* `safety: 148`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pane_size::Dimension, std::rc::Rc, tab::Pane, PaneGeom, crate::
    panes::PaneId, std::cell::RefCell, std::collections::HashMap, HashSet...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zellij-server/src/panes/floating_panes/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.604 IQR)
- **Top Global Matches:** file_cluster_17: 13.604, file_cluster_8: 13.666, file_cluster_13: 13.826
- **Magnitude:** 2333.72 | **LOC:** 1367 | **CtrlFlow:** 35.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 60
- **Risk Profile:** Cognitive Load (39.7575%), Tech Debt (75.1903%)
**Top Internal Functions/Classes:**
  * `render` (Impact: 1726.2 | O(2^N) | DB: 60)
  * `replace_pane` (Impact: 62.5 | O(N^5) | DB: 2)
  * `stack` (Impact: 56.0 | O(N^6))
  * `position_floating_pane_layout` (Impact: 52.4 | O(N^4) | DB: 4)
  * `set_pane_frames` (Impact: 35.9 | O(N^4) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 112`, `structural_boundaries: 206`, `args: 145`, `func_start: 70`, `class_start: 1`
* *Risk/State:* `state_mutation: 157`, `planned_debt: 4`, `orphaned_logic: 21`
* *Architecture:* `api: 69`, `import: 11`
* *Defense:* `safety: 164`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pane_size::Dimension, std::cmp::Ordering, input::command::RunCommand, Offset, Style, PaneId, zellij_utils::
    data::ModeInfo, ClientId...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zellij-server/src/unit/screen_tests.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.747 IQR)
- **Top Global Matches:** file_cluster_8: 12.747, file_cluster_0: 12.887, file_cluster_17: 13.119
- **Magnitude:** 2268.48 | **LOC:** 8080 | **CtrlFlow:** 9.0% | **Authorship Centralization:** 87.1%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (16.2004%), Tech Debt (84.817%)
**Top Internal Functions/Classes:**
  * `background_plugin_receives_broadcasts_re` (Impact: 78.0 | O(N^6) | DB: 4)
  * `new` (Impact: 75.2 | O(2^N))
  * `tab_switch_only_updates_active_tab_plugi` (Impact: 51.7 | O(N^6) | DB: 2)
  * `drop_all_pty_messages` (Impact: 43.3 | O(N^6) | DB: 1)
  * `delivery_path_a_and_b_produce_same_conte` (Impact: 38.8 | O(N^4) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 156`, `structural_boundaries: 1581`, `args: 204`, `func_start: 160`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 376`, `high_risk_execution: 1`, `state_mutation: 338`, `fragile_debt: 1`, `duplicate_logic: 8`, `orphaned_logic: 138`
* *Architecture:* `io: 1`, `api: 105`, `concurrency: 189`, `import: 36`
* *Defense:* `safety: 852`, `test: 351`, `sync_locks: 163`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` PluginUserConfiguration, RunPluginLocation, pty::ClientTabIndexOrPaneId, std::net::IpAddr, zellij_utils::
    channels::self, insta::assert_snapshot, zellij_utils::input::options::Options, Screen...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `default-plugins/session-manager/src/ui/components.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.128 IQR)
- **Top Global Matches:** file_cluster_8: 11.128, file_cluster_0: 11.526, file_cluster_16: 11.579
- **Magnitude:** 2229.42 | **LOC:** 1848 | **CtrlFlow:** 38.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (18.24%), Tech Debt (84.011%)
**Top Internal Functions/Classes:**
  * `render_unified_results` (Impact: 431.4 | O(N^4) | DB: 5)
  * `render_new_session_block` (Impact: 173.0 | O(N^6) | DB: 1)
  * `render` (Impact: 171.6 | O(2^N) | DB: 13)
  * `render_controls_line` (Impact: 163.8 | O(N^5))
  * `render` (Impact: 103.8 | O(N^6) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 220`, `structural_boundaries: 351`, `args: 66`, `func_start: 54`, `class_start: 12`
* *Risk/State:* `state_mutation: 135`, `planned_debt: 1`, `duplicate_logic: 10`, `orphaned_logic: 20`
* *Architecture:* `api: 83`, `import: 11`
* *Defense:* `safety: 91`, `doc: 18`, `test: 8`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::single_screen::UnifiedSearchResult, crate::ActiveScreen, zellij_tile::prelude::*, std::time::Duration, super::*, SessionUiInfo, humantime::format_duration, NewSessionInfo...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zellij-server/src/panes/floating_panes/floating_pane_grid.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.808 IQR)
- **Top Global Matches:** file_cluster_8: 12.808, file_cluster_17: 12.818, file_cluster_13: 13.076
- **Magnitude:** 2188.16 | **LOC:** 946 | **CtrlFlow:** 50.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (35.6694%), Tech Debt (29.5608%)
**Top Internal Functions/Classes:**
  * `resize` (Impact: 627.0 | O(2^N) | DB: 5)
  * `change_pane_size` (Impact: 577.5 | O(2^N) | DB: 2)
  * `find_room_for_new_pane` (Impact: 69.4 | O(N^6) | DB: 1)
  * `can_move_pane_left` (Impact: 51.1 | O(N^4))
  * `can_move_pane_right` (Impact: 51.1 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 218`, `structural_boundaries: 216`, `args: 114`, `func_start: 34`, `class_start: 1`
* *Risk/State:* `state_mutation: 147`, `orphaned_logic: 14`
* *Architecture:* `api: 18`, `import: 9`
* *Defense:* `safety: 108`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Size, std::cmp::Ordering, MIN_TERMINAL_WIDTH, crate::tab::MIN_TERMINAL_HEIGHT, zellij_utils::data::Direction, std::rc::Rc, tab::Pane, PaneGeom...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zellij-server/src/output/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_11` (Drift: 13.594 IQR)
- **Top Global Matches:** file_cluster_11: 13.594, file_cluster_8: 13.612, file_cluster_17: 13.641
- **Magnitude:** 1849.18 | **LOC:** 1327 | **CtrlFlow:** 44.4% | **Authorship Centralization:** 90.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 22
- **Risk Profile:** Cognitive Load (52.9671%), Tech Debt (51.131%)
**Top Internal Functions/Classes:**
  * `serialize_with_size` (Impact: 731.9 | O(N^6) | DB: 22)
  * `serialize_chunks` (Impact: 267.7 | O(N^6) | DB: 9)
  * `serialize_chunks_with_newlines` (Impact: 113.4 | O(N^5) | DB: 6)
  * `serialize` (Impact: 98.2 | O(2^N) | DB: 5)
  * `adjust_middle_segment_for_wide_chars` (Impact: 80.6 | O(N^4) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 186`, `structural_boundaries: 233`, `args: 49`, `func_start: 26`, `class_start: 2`
* *Risk/State:* `state_mutation: 163`, `dead_code: 3`, `planned_debt: 6`, `orphaned_logic: 12`
* *Architecture:* `api: 24`, `import: 12`
* *Defense:* `safety: 166`, `doc: 1`, `test: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` TerminalCharacter, crate::panes::Selection, PaneId, ClientId, panes::LinkHandler, zellij_utils::data::HighlightLayer, zellij_utils::errors::prelude::*, HashSet...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `zellij-server/src/panes/sixel.rs` (RUST) | Magnitude: 699.66 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 414, structural_boundaries: 103, safety: 66, branch: 60
- `zellij-utils/src/vendored/termwiz/input.rs` (RUST) | Magnitude: 149.68 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 344, sec_reflection_metaprogramming: 177, doc: 58, args: 48
- `zellij-server/src/output/unit/output_tests.rs` (RUST) | Magnitude: 281.26 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 593, structural_boundaries: 225, test: 118, safety: 117
- `zellij-tile/src/lib.rs` (RUST) | Magnitude: 72.72 | Delta: **0.057 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 96, doc: 81, structural_boundaries: 44, args: 17
- `default-plugins/status-bar/src/tip/cache.rs` (RUST) | Magnitude: 163.28 | Delta: **0.062 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 80, structural_boundaries: 26, safety: 23, state_mutation: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `zellij-server/src/output/mod.rs` (RUST) | Magnitude: 1849.18 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 833, structural_boundaries: 233, branch: 186, safety: 166
- `zellij-server/src/panes/alacritty_functions.rs` (RUST) | Magnitude: 178.1 | Delta: **0.06 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 63, branch: 33, safety: 27, structural_boundaries: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `zellij-server/src/pty_writer.rs` (RUST) | Magnitude: 186.7 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 107, structural_boundaries: 25, branch: 23, safety: 23
- `zellij-utils/src/input/mod.rs` (RUST) | Magnitude: 165.82 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 154, structural_boundaries: 49, state_mutation: 28, branch: 21
- `zellij-utils/src/input/keybinds.rs` (RUST) | Magnitude: 189.7 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 113, state_mutation: 26, structural_boundaries: 25, branch: 16
- `zellij-utils/src/logging.rs` (RUST) | Magnitude: 61.54 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 89, structural_boundaries: 21, safety: 18, memory_alloc: 10
- `zellij-client/src/web_client/utils.rs` (RUST) | Magnitude: 130.46 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 55, branch: 27, safety: 15, structural_boundaries: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `zellij-utils/src/ipc.rs` (RUST) | Magnitude: 310.14 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 303, safety: 82, structural_boundaries: 75, state_mutation: 62
- `zellij-utils/src/channels.rs` (RUST) | Magnitude: 10.1 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 10, indent_spaces: 8, structural_boundaries: 6, api: 6
- `zellij-utils/src/plugin_api/command.rs` (RUST) | Magnitude: 9.06 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 11, generics: 8, args: 4
- `zellij-utils/src/data.rs` (RUST) | Magnitude: 1661.48 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 1610, safety: 519, api: 283, encapsulation: 283
- `zellij-utils/src/plugin_api/file.rs` (RUST) | Magnitude: 10.34 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 11, generics: 8, args: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `zellij-server/src/panes/tiled_panes/mod.rs` (RUST) | Magnitude: 2639.6 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 1556, structural_boundaries: 381, state_mutation: 233, safety: 231
- `zellij-server/src/panes/floating_panes/mod.rs` (RUST) | Magnitude: 2333.72 | Delta: **0.062 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 933, structural_boundaries: 206, safety: 164, state_mutation: 157
- `zellij-server/src/panes/tiled_panes/stacked_panes.rs` (RUST) | Magnitude: 2491.54 | Delta: **0.08 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 1188, structural_boundaries: 401, state_mutation: 366, branch: 287
- `zellij-server/src/panes/tiled_panes/tiled_pane_grid.rs` (RUST) | Magnitude: 3494.96 | Delta: **0.095 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 2080, structural_boundaries: 531, branch: 423, state_mutation: 418
- `zellij-server/src/panes/tiled_panes/pane_resizer.rs` (RUST) | Magnitude: 429.18 | Delta: **0.098 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 283, structural_boundaries: 73, branch: 54, state_mutation: 53

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `zellij-server/src/os_input_output_windows.rs` (RUST) | Magnitude: 752.18 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 461, structural_boundaries: 116, safety: 98, branch: 75
- `zellij-client/src/os_input_output.rs` (RUST) | Magnitude: 176.36 | Delta: **0.078 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 138, safety: 67, concurrency: 59, structural_boundaries: 52
- `zellij-server/src/os_input_output.rs` (RUST) | Magnitude: 888.82 | Delta: **0.086 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 582, safety: 181, structural_boundaries: 159, state_mutation: 96
- `zellij-client/src/web_client/unit/web_client_tests.rs` (RUST) | Magnitude: 1177.96 | Delta: **0.101 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 1887, structural_boundaries: 735, concurrency: 362, safety: 284
- `zellij-server/src/tab/copy_command.rs` (RUST) | Magnitude: 83.16 | Delta: **0.103 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 46, structural_boundaries: 16, concurrency: 10, branch: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `zellij-tile/src/ui_components/nested_list.rs` (RUST) | Magnitude: 175.0 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 138, structural_boundaries: 33, args: 25, api: 22
- `zellij-utils/src/input/config.rs` (RUST) | Magnitude: 913.52 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 1193, safety: 209, structural_boundaries: 183, branch: 96
- `zellij-server/src/ui/pane_boundaries_frame.rs` (RUST) | Magnitude: 808.94 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 389, structural_boundaries: 131, state_mutation: 75, branch: 69
- `zellij-server/src/panes/floating_panes/floating_pane_grid.rs` (RUST) | Magnitude: 2188.16 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 823, branch: 218, structural_boundaries: 216, state_mutation: 147
- `default-plugins/status-bar/src/tip/data/sync_tab.rs` (RUST) | Magnitude: 37.56 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 50, concurrency: 18, structural_boundaries: 16, state_mutation: 6

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `zellij-utils/src/ipc/protobuf_conversion.rs` -> Churn: **76.09%** | Cog Load: 8.8158% | Debt: 90.715%
- `zellij-server/src/tab/mod.rs` -> Churn: **75.49%** | Cog Load: 27.4659% | Debt: 99.4741%
- `zellij-utils/src/data.rs` -> Churn: **74.88%** | Cog Load: 4.734% | Debt: 99.9991%
- `zellij-server/src/unit/screen_tests.rs` -> Churn: **73.59%** | Cog Load: 16.2004% | Debt: 84.817%
- `zellij-utils/src/errors.rs` -> Churn: **69.98%** | Cog Load: 3.4652% | Debt: 50.3994%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `zellij-server/src/panes/grid.rs` -> **Aram Drevekenin** (82.6% isolated ownership) | Magnitude: 5330.36
- `zellij-server/src/tab/mouse_handler.rs` -> **Aram Drevekenin** (100.0% isolated ownership) | Magnitude: 5028.46
- `zellij-utils/src/plugin_api/plugin_command.rs` -> **Aram Drevekenin** (88.9% isolated ownership) | Magnitude: 4960.4
- `zellij-server/src/tab/mod.rs` -> **Aram Drevekenin** (94.1% isolated ownership) | Magnitude: 4836.62
- `zellij-utils/src/plugin_api/action.rs` -> **Aram Drevekenin** (88.0% isolated ownership) | Magnitude: 4526.08

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

- `zellij-utils/src/envs.rs` -> **Severity: 1808.4** (Blast Radius: 18.084 * Doc Risk: 100.0%)
- `xtask/src/flags.rs` -> **Severity: 705.6** (Blast Radius: 7.056 * Doc Risk: 100.0%)
- `zellij-utils/src/session_serialization.rs` -> **Severity: 632.537** (Blast Radius: 7.483 * Doc Risk: 84.5299%)
- `zellij-server/src/plugins/zellij_exports.rs` -> **Severity: 512.7** (Blast Radius: 5.127 * Doc Risk: 100.0%)
- `zellij-utils/src/input/keybinds.rs` -> **Severity: 512.7** (Blast Radius: 5.127 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
