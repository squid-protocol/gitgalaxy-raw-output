# ARCHITECTURAL_BRIEF: alacritty
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_rust/alacritty` |
| **Timestamp** | `2026-08-03T19:43:30.875656+00:00` |
| **Scan Duration** | `1.67s` |
| **Git Branch** | `master` |
| **Git Commit** | `f99dc71708d31d5c32d4b3fa611f9a87bf22657e` |
| **Git Remote** | `https://github.com/alacritty/alacritty.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 100 malicious artifacts.

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
| Total Artifacts | 338 |
| Analyzed Artifacts (Scanned) | 259 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 79 |
| Total LOC | 21218 |
| Volatility Index | 0.004 |
| % Scanned of codebase = | 76.6% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7347 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.6667 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 2 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JSON | 135 | 135 | 52.1% |
| RUST | 87 | 20074 | 33.6% |
| MARKDOWN | 8 | 0 | 3.1% |
| PLAINTEXT | 8 | 0 | 3.1% |
| XML | 8 | 0 | 3.1% |
| GLSL | 6 | 259 | 2.3% |
| SHELL | 6 | 679 | 2.3% |
| MAKEFILE | 1 | 71 | 0.4% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.28`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 125 | 48.3% |
| file_cluster_13 | 49 | 18.9% |
| file_cluster_16 | 12 | 4.6% |
| file_cluster_0 | 11 | 4.2% |
| file_cluster_12 | 1 | 0.4% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Minified & Vendor Opaque Mass | 45 | 17.4% |
| Static: Literature & Documentation | 16 | 6.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 79*

**Composition by Extension & Reason:**
- `.recording`: 45x Excluded (Unsupported Extension: '.recording')
- `.toml`: 5x Unsupported Format (.toml), 1x Excluded (Unsupported Extension: '.toml')
- `.scd`: 5x Excluded (Unsupported Extension: '.scd')
- `.yml`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.png`: 3x Excluded (Explicitly Denied Extension: '.png')
- `.md`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sh`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.lock`: 1x Excluded (Unsupported Extension: '.lock')
- `.rs`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ico`: 1x Excluded (Explicitly Denied Extension: '.ico')
- `.manifest`: 1x Excluded (Unsupported Extension: '.manifest')
- `.rc`: 1x Excluded (Unsupported Extension: '.rc')
- `.wxs`: 1x Excluded (Unsupported Extension: '.wxs')
- `.rtf`: 1x Excluded (Unsupported Extension: '.rtf')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 99.9 | 8.3 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 88.8 | 13.1 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 22.4 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 16.6 | 0.0 | 0.0 |
| API Exposure | 0.0 | 8.5 | 1.4 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 3.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 24.4 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 10.7 | 0.4 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 43.5 | 6.7 | 6.7 |
| Instability Exposure | 0.0 | 6.0 | 0.4 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 46.3 | 1.9 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 24.9 | 0.0 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 26.4 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 20.0 | 4.7 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.4 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `extra/completions/alacritty.bash` (Hits: 40)
- `Makefile` (Hits: 10)
- `alacritty/src/window_context.rs` (Hits: 5)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **debug.rs** (`alacritty/src/config/debug.rs`) — 2 inbound connections
2. **ipc.rs** (`alacritty/src/polling/ipc.rs`) — 1 inbound connections
3. **platform.rs** (`alacritty/src/renderer/platform.rs`) — 1 inbound connections
4. **glsl3.rs** (`alacritty/src/renderer/text/glsl3.rs`) — 1 inbound connections
5. **serde_replace.rs** (`alacritty_config_derive/src/serde_replace.rs`) — 1 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **event.rs** (`alacritty/src/event.rs`) — 99 outbound dependencies
2. **mod.rs** (`alacritty/src/display/mod.rs`) — 85 outbound dependencies
3. **mod.rs** (`alacritty/src/input/mod.rs`) — 73 outbound dependencies
4. **mod.rs** (`alacritty_terminal/src/term/mod.rs`) — 63 outbound dependencies
5. **ui_config.rs** (`alacritty/src/config/ui_config.rs`) — 52 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `new` (@ `alacritty/src/event.rs`) -> Impact: **2364.0** | LOC: 1261
  * *Intent:* /// Create a new event processor.
- `_alacritty` (@ `extra/completions/alacritty.bash`) -> Impact: **1031.0** | LOC: 525
- `migrate` (@ `alacritty/src/migrate/mod.rs`) -> Impact: **654.5** | LOC: 290
  * *Intent:* /// Handle migration.
- `box_drawing` (@ `alacritty/src/renderer/text/builtin_font.rs`) -> Impact: **582.2** | LOC: 724
- `deserialize` (@ `alacritty/src/config/bindings.rs`) -> Impact: **570.6** | LOC: 212
- `process_renderer_update` (@ `alacritty/src/display/mod.rs`) -> Impact: **432.6** | LOC: 533
- `execute` (@ `alacritty/src/input/mod.rs`) -> Impact: **268.7** | LOC: 282
- `spawn` (@ `alacritty_terminal/src/event_loop.rs`) -> Impact: **265.0** | LOC: 120
- `new` (@ `alacritty/src/display/mod.rs`) -> Impact: **241.3** | LOC: 122
- `new` (@ `alacritty/src/display/content.rs`) -> Impact: **222.8** | LOC: 91
  * *Intent:* /// Extra storage with rarely present fields for [`RenderableCell`], to reduce the cell size we /// pass around. #[derive(Clone, Debug)]

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `deserialize` (@ `alacritty/src/config/bindings.rs`) -> **O(2^N) [Recursive]**
- `deserialize` (@ `alacritty/src/config/ui_config.rs`) -> **O(2^N) [Recursive]**
- `default` (@ `alacritty/src/config/ui_config.rs`) -> **O(2^N) [Recursive]**
  * *Intent:* #[inline]
- `deserialize` (@ `alacritty/src/config/window.rs`) -> **O(2^N) [Recursive]**
- `deserialize` (@ `alacritty/src/display/color.rs`) -> **O(2^N) [Recursive]**
- `new` (@ `alacritty/src/event.rs`) -> **O(2^N) [Recursive]**
  * *Intent:* /// Create a new event processor.
- `alt_send_esc` (@ `alacritty/src/input/keyboard.rs`) -> **O(2^N) [Recursive]**
- `execute` (@ `alacritty/src/input/mod.rs`) -> **O(2^N) [Recursive]**
- `new` (@ `alacritty/src/renderer/text/gles2.rs`) -> **O(2^N) [Recursive]**
- `new` (@ `alacritty/src/renderer/text/glsl3.rs`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `_alacritty` (@ `extra/completions/alacritty.bash`) -> DB Complexity: **261**
- `new` (@ `alacritty/src/event.rs`) -> DB Complexity: **100**
  * *Intent:* /// Create a new event processor.
- `process_renderer_update` (@ `alacritty/src/display/mod.rs`) -> DB Complexity: **32**
- `box_drawing` (@ `alacritty/src/renderer/text/builtin_font.rs`) -> DB Complexity: **30**
- `new` (@ `alacritty/src/display/content.rs`) -> DB Complexity: **20**
  * *Intent:* /// Extra storage with rarely present fields for [`RenderableCell`], to reduce the cell size we /// pass around. #[derive(Clone, Debug)]
- `migrate` (@ `alacritty/src/migrate/mod.rs`) -> DB Complexity: **20**
  * *Intent:* /// Handle migration.
- `spawn` (@ `alacritty_terminal/src/event_loop.rs`) -> DB Complexity: **17**
- `write_ref_test_results` (@ `alacritty/src/window_context.rs`) -> DB Complexity: **13**
  * *Intent:* // Create the PTY.
- `pty_read` (@ `alacritty_terminal/src/event_loop.rs`) -> DB Complexity: **12**
- `deserialize` (@ `alacritty/src/config/bindings.rs`) -> DB Complexity: **11**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `alacritty/src` | 11 | 3794.2 | 10.51% | 38.19% |
| `alacritty/src/display` | 9 | 3534.64 | 15.08% | 86.5% |
| `alacritty/src/config` | 16 | 2819.04 | 4.28% | 56.46% |
| `alacritty_terminal/src/term` | 4 | 2754.0 | 14.41% | 96.64% |
| `alacritty_terminal/src` | 8 | 1832.34 | 12.88% | 47.87% |
| `alacritty/src/input` | 2 | 1829.78 | 17.39% | 48.83% |
| `alacritty/src/renderer/text` | 6 | 1704.04 | 16.58% | 37.98% |
| `extra/completions` | 2 | 1440.58 | 53.37% | 43.78% |
| `alacritty/src/renderer` | 4 | 1018.6 | 11.94% | 47.63% |
| `alacritty/src/migrate` | 2 | 834.0 | 27.01% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `alacritty_terminal/src/grid/row.rs` -> **100.0%** Exposure
- `alacritty_terminal/src/index.rs` -> **100.0%** Exposure
- `alacritty_terminal/src/term/color.rs` -> **100.0%** Exposure
- `scripts/24-bit-color.sh` -> **100.0%** Exposure
- `scripts/colors.sh` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `alacritty/src/config/mod.rs` -> **100.0%** Exposure
- `alacritty/src/config/serde_utils.rs` -> **100.0%** Exposure
- `extra/completions/alacritty.bash` -> **100.0%** Exposure
- `scripts/create-flamegraph.sh` -> **100.0%** Exposure
- `alacritty/src/renderer/text/mod.rs` -> **99.9949%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `alacritty_terminal/src/term/mod.rs` -> **62** Orphaned Functions | **17** Duplicates
- `alacritty_terminal/src/index.rs` -> **11** Orphaned Functions | **29** Duplicates
- `alacritty_terminal/src/term/search.rs` -> **35** Orphaned Functions | **2** Duplicates
- `alacritty/src/config/bindings.rs` -> **18** Orphaned Functions | **17** Duplicates
- `alacritty_terminal/src/grid/row.rs` -> **6** Orphaned Functions | **14** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`alacritty/src/input/keyboard.rs`** -> AI Confidence: **99.31%**
2. **`alacritty/src/migrate/mod.rs`** -> AI Confidence: **99.31%**
3. **`alacritty_terminal/src/grid/resize.rs`** -> AI Confidence: **99.31%**
4. **`scripts/24-bit-color.sh`** -> AI Confidence: **99.29%**
5. **`scripts/colors.sh`** -> AI Confidence: **99.29%**
6. **`alacritty/src/config/cursor.rs`** -> AI Confidence: **99.24%**
7. **`alacritty/src/display/hint.rs`** -> AI Confidence: **99.24%**
8. **`alacritty/src/polling/mod.rs`** -> AI Confidence: **99.24%**
9. **`alacritty_config_derive/src/serde_replace.rs`** -> AI Confidence: **99.24%**
10. **`alacritty_terminal/src/event_loop.rs`** -> AI Confidence: **99.24%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `alacritty/src/cli.rs` -> **20.0%** Exposure
- `alacritty/src/config/bindings.rs` -> **20.0%** Exposure
- `alacritty/src/config/color.rs` -> **20.0%** Exposure
- `alacritty/src/config/mod.rs` -> **20.0%** Exposure
- `alacritty/src/config/ui_config.rs` -> **20.0%** Exposure
### Weaponizable Injection Vectors
- `alacritty/src/cli.rs` -> **99.9754%** Exposure
- `alacritty_terminal/src/term/mod.rs` -> **3.6453%** Exposure
### Raw Memory Manipulation
- `alacritty/src/renderer/text/builtin_font.rs` -> **0.0005%** Exposure
- `alacritty_terminal/src/index.rs` -> **0.0001%** Exposure
### Algorithmic DoS Exposure
- `alacritty/src/cli.rs` -> **100.0%** Exposure
- `alacritty/src/clipboard.rs` -> **100.0%** Exposure
- `alacritty/src/config/bindings.rs` -> **100.0%** Exposure
- `alacritty/src/config/mod.rs` -> **100.0%** Exposure
- `alacritty/src/config/monitor.rs` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1678` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `alacritty_terminal/src/tty/windows/blocking.rs` (RUST) -> Cumulative Risk: **772.32**
- **Archetype:** `file_cluster_13` (Distance: 13.947 IQR)
- **Magnitude:** 380.82 | **LOC:** 277 | **CtrlFlow:** 30.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Concurrency (99.9998%), Tech Debt (99.9987%)
- **Heaviest Functions:** `new` (Impact: 99.4), `new` (Impact: 87.3), `wake_by_ref` (Impact: 25.9)

### 2. `alacritty_terminal/src/event_loop.rs` (RUST) -> Cumulative Risk: **766.71**
- **Archetype:** `file_cluster_13` (Distance: 13.727 IQR)
- **Magnitude:** 746.66 | **LOC:** 487 | **CtrlFlow:** 41.4% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `spawn` (Impact: 265.0), `pty_read` (Impact: 192.8), `recv` (Impact: 25.5)

### 3. `alacritty/src/daemon.rs` (RUST) -> Cumulative Risk: **728.84**
- **Archetype:** `file_cluster_0` (Distance: 11.578 IQR)
- **Magnitude:** 108.16 | **LOC:** 168 | **CtrlFlow:** 22.9% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Tech Debt (99.6425%), State Flux (97.7662%)
- **Heaviest Functions:** `spawn_daemon` (Impact: 42.1), `foreground_process_path` (Impact: 21.4), `foreground_process_path` (Impact: 13.2)

### 4. `alacritty_terminal/src/tty/windows/child.rs` (RUST) -> Cumulative Risk: **680.61**
- **Archetype:** `file_cluster_13` (Distance: 13.435 IQR)
- **Magnitude:** 133.48 | **LOC:** 169 | **CtrlFlow:** 11.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `new` (Impact: 31.8), `child_exit_callback` (Impact: 13.9), `event_rx` (Impact: 5.3)

### 5. `alacritty/src/renderer/text/glsl3.rs` (RUST) -> Cumulative Risk: **679.42**
- **Archetype:** `file_cluster_8` (Distance: 10.97 IQR)
- **Magnitude:** 257.16 | **LOC:** 463 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.0253%), State Flux (96.6011%)
- **Heaviest Functions:** `new` (Impact: 40.5), `new` (Impact: 29.4), `render_batch` (Impact: 16.9)

### 6. `alacritty/src/polling/mod.rs` (RUST) -> Cumulative Risk: **678.37**
- **Archetype:** `file_cluster_13` (Distance: 13.202 IQR)
- **Magnitude:** 215.52 | **LOC:** 125 | **CtrlFlow:** 40.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), State Flux (99.3772%)
- **Heaviest Functions:** `spawn` (Impact: 96.0), `poll` (Impact: 73.2), `drop` (Impact: 20.5)

### 7. `alacritty/src/input/mod.rs` (RUST) -> Cumulative Risk: **668.62**
- **Archetype:** `file_cluster_13` (Distance: 12.306 IQR)
- **Magnitude:** 1177.84 | **LOC:** 1560 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 40.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), State Flux (89.3127%)
- **Heaviest Functions:** `execute` (Impact: 268.7), `scroll_terminal` (Impact: 165.6), `process_mouse_bindings` (Impact: 73.7)

### 8. `alacritty/src/display/content.rs` (RUST) -> Cumulative Risk: **659.62**
- **Archetype:** `file_cluster_13` (Distance: 12.774 IQR)
- **Magnitude:** 638.84 | **LOC:** 553 | **CtrlFlow:** 36.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), State Flux (99.8317%), Tech Debt (94.9134%)
- **Heaviest Functions:** `new` (Impact: 222.8), `next` (Impact: 81.2), `new` (Impact: 56.3)

### 9. `alacritty/src/renderer/text/gles2.rs` (RUST) -> Cumulative Risk: **656.54**
- **Archetype:** `file_cluster_13` (Distance: 11.133 IQR)
- **Magnitude:** 263.4 | **LOC:** 505 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), State Flux (98.1241%), Tech Debt (89.4999%)
- **Heaviest Functions:** `new` (Impact: 90.8), `new` (Impact: 42.2), `render_batch` (Impact: 22.6)

### 10. `alacritty_config_derive/src/config_deserialize/de_enum.rs` (RUST) -> Cumulative Risk: **651.81**
- **Archetype:** `file_cluster_13` (Distance: 12.278 IQR)
- **Magnitude:** 73.56 | **LOC:** 76 | **CtrlFlow:** 22.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), State Flux (99.7201%), Documentation (98.7528%)
- **Heaviest Functions:** `derive_deserialize` (Impact: 59.4)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `alacritty/src/event.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.759 IQR)
- **Top Global Matches:** file_cluster_13: 13.759, file_cluster_0: 13.864, file_cluster_8: 14.027
- **Magnitude:** 2608.42 | **LOC:** 2094 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 100
- **Risk Profile:** Cognitive Load (13.7379%), Tech Debt (8.6821%)
**Top Internal Functions/Classes:**
  * `new` (Impact: 2364.0 | O(2^N) | DB: 100)
    * *Intent:* /// Create a new event processor.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 146`, `structural_boundaries: 293`, `args: 73`, `func_start: 65`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 186`, `fragile_debt: 1`
* *Architecture:* `api: 38`, `import: 52`
* *Defense:* `safety: 150`, `doc: 87`, `immutability_locks: 6`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.764
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::config::self, winit::raw_window_handle::HasDisplayHandle, ParsedOptions, std::ffi::OsStr, crate::config::ui_config::HintAction, std::collections::hash_map::Entry, std::os::unix::net::UnixStream, alacritty_terminal::term::search::Match...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty_terminal/src/term/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.873 IQR)
- **Top Global Matches:** file_cluster_0: 12.873, file_cluster_8: 12.936, file_cluster_13: 13.077
- **Magnitude:** 2088.6 | **LOC:** 3303 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (10.3765%), Tech Debt (86.5676%)
**Top Internal Functions/Classes:**
  * `line_to_string` (Impact: 135.4 | O(N^5) | DB: 3)
  * `input` (Impact: 77.5 | O(N^4) | DB: 3)
  * `clear_screen` (Impact: 55.5 | O(N^5) | DB: 3)
  * `set_private_mode` (Impact: 46.4 | O(2^N) | DB: 1)
  * `unset_private_mode` (Impact: 45.7 | O(2^N) | DB: 1)
    * *Intent:* // If clearing more than one line.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 262`, `structural_boundaries: 524`, `args: 127`, `func_start: 141`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 366`, `dead_code: 1`, `duplicate_logic: 17`, `orphaned_logic: 62`
* *Architecture:* `api: 52`, `import: 31`
* *Defense:* `safety: 121`, `doc: 182`, `test: 141`, `immutability_locks: 33`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.764
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Direction, ViMotion, slice, Grid, KeyboardModes, crate::event::VoidListener, NamedColor, crate::grid::Grid...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extra/completions/alacritty.bash` (SHELL | Tier 2 | 🚨 AI THREAT: 99.11%)
- **Global Archetype:** `file_cluster_12` (Drift: 15.313 IQR)
- **Top Global Matches:** file_cluster_12: 15.313, file_cluster_11: 15.38, file_cluster_8: 15.381
- **Magnitude:** 1431.12 | **LOC:** 532 | **CtrlFlow:** 69.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 261
- **Risk Profile:** Cognitive Load (99.9325%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_alacritty` (Impact: 1031.0 | O(N^6) | DB: 261)
  * `Anonymous_Block` (Impact: 8.2 | O(N^1) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 209`, `structural_boundaries: 91`, `args: 3`, `func_start: 1`
* *Risk/State:* `state_mutation: 383`
* *Architecture:* `io: 40`
* *Defense:* `safety: 148`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.764
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty/src/input/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.306 IQR)
- **Top Global Matches:** file_cluster_13: 12.306, file_cluster_8: 12.339, file_cluster_0: 12.341
- **Magnitude:** 1177.84 | **LOC:** 1560 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 40.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (25.9405%), Tech Debt (53.4575%)
**Top Internal Functions/Classes:**
  * `execute` (Impact: 268.7 | O(2^N) | DB: 2)
  * `scroll_terminal` (Impact: 165.6 | O(N^4) | DB: 2)
  * `process_mouse_bindings` (Impact: 73.7 | O(N^3) | DB: 4)
  * `mouse_input` (Impact: 65.3 | O(N^6) | DB: 1)
  * `on_touch_motion` (Impact: 54.1 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 114`, `structural_boundaries: 313`, `args: 106`, `func_start: 98`, `class_start: 5`
* *Risk/State:* `high_risk_execution: 6`, `state_mutation: 153`, `dead_code: 1`, `duplicate_logic: 8`, `orphaned_logic: 10`
* *Architecture:* `api: 22`, `import: 39`
* *Defense:* `safety: 63`, `doc: 31`, `test: 6`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.764
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::cmp::Ordering, Touch, alacritty_terminal::grid::Dimensions, Direction, SizeInfo, crate::config::window::Decorations, MouseScrollDelta, alacritty_terminal::term::ClipboardType...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty/src/display/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.801 IQR)
- **Top Global Matches:** file_cluster_13: 12.801, file_cluster_0: 13.017, file_cluster_8: 13.063
- **Magnitude:** 1113.66 | **LOC:** 1635 | **CtrlFlow:** 25.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 32
- **Risk Profile:** Cognitive Load (16.8273%), Tech Debt (93.275%)
**Top Internal Functions/Classes:**
  * `process_renderer_update` (Impact: 432.6 | O(N^6) | DB: 32)
  * `new` (Impact: 241.3 | O(2^N) | DB: 6)
  * `handle_update` (Impact: 55.3 | O(N^3) | DB: 11)
  * `swap_buffers` (Impact: 52.8 | O(2^N))
  * `source` (Impact: 14.3 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 293`, `args: 66`, `func_start: 46`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 119`, `fragile_debt: 2`, `duplicate_logic: 8`, `orphaned_logic: 6`
* *Architecture:* `api: 47`, `import: 47`
* *Defense:* `safety: 60`, `doc: 86`, `immutability_locks: 5`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.764
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` winit::raw_window_handle::RawWindowHandle, Renderer, glutin::prelude::*, crate::renderer::self, crate::display::cursor::IntoRects, crate::scheduler::Scheduler, std::ops::Deref, crate::display::bell::VisualBell...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty/src/config/bindings.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.442 IQR)
- **Top Global Matches:** file_cluster_16: 12.442, file_cluster_8: 12.503, file_cluster_0: 12.517
- **Magnitude:** 951.32 | **LOC:** 1453 | **CtrlFlow:** 34.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (4.4471%), Tech Debt (95.0052%)
**Top Internal Functions/Classes:**
  * `deserialize` (Impact: 570.6 | O(2^N) | DB: 11)
  * `deserialize` (Impact: 32.8 | O(N^5) | DB: 1)
  * `deserialize` (Impact: 30.1 | O(N^6) | DB: 2)
  * `deserialize` (Impact: 29.8 | O(N^6) | DB: 2)
  * `fmt` (Impact: 21.2 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 107`, `structural_boundaries: 200`, `args: 57`, `func_start: 54`, `class_start: 17`
* *Risk/State:* `state_mutation: 44`, `dead_code: 1`, `duplicate_logic: 17`, `orphaned_logic: 18`
* *Architecture:* `api: 23`, `import: 16`
* *Defense:* `safety: 174`, `doc: 107`, `test: 51`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.764
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` alacritty_config_derive::ConfigDeserialize, std::rc::Rc, Deserializer, MapAccess, winit::keyboard::
    Key, alacritty_terminal::vi_mode::ViMotion, super::*, Display...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty_terminal/src/event_loop.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.727 IQR)
- **Top Global Matches:** file_cluster_13: 13.727, file_cluster_0: 13.794, file_cluster_4: 13.866
- **Magnitude:** 746.66 | **LOC:** 487 | **CtrlFlow:** 41.4% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (45.4491%), Tech Debt (57.8109%)
**Top Internal Functions/Classes:**
  * `spawn` (Impact: 265.0 | O(N^6) | DB: 17)
  * `pty_read` (Impact: 192.8 | O(N^6) | DB: 12)
  * `recv` (Impact: 25.5 | O(N^4) | DB: 1)
  * `new` (Impact: 22.2 | O(2^N))
    * *Intent:* /// Create a new event loop.
  * `fmt` (Impact: 14.2 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 77`, `structural_boundaries: 109`, `args: 26`, `func_start: 22`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 91`, `duplicate_logic: 3`, `orphaned_logic: 3`
* *Architecture:* `io: 3`, `api: 12`, `concurrency: 30`, `import: 17`
* *Defense:* `safety: 69`, `doc: 22`, `sync_locks: 3`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.764
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::event::self, std::sync::mpsc::self, std::thread::JoinHandle, crate::sync::FairMutex, std::collections::VecDeque, Sender, log::error, Display...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty/src/display/hint.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.613 IQR)
- **Top Global Matches:** file_cluster_13: 13.613, file_cluster_16: 13.666, file_cluster_0: 13.751
- **Magnitude:** 722.1 | **LOC:** 704 | **CtrlFlow:** 40.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (24.2399%), Tech Debt (87.1217%)
**Top Internal Functions/Classes:**
  * `hint_post_processing` (Impact: 130.2 | O(N^6) | DB: 4)
    * *Intent:* /// Apply some hint post processing heuristics. /// /// This will check the end of the hint and make...
  * `update_matches` (Impact: 69.5 | O(N^6) | DB: 4)
    * *Intent:* /// Update the visible hint matches and key labels.
  * `visible_unique_hyperlinks_iter` (Impact: 51.8 | O(N^4) | DB: 3)
  * `highlighted_at` (Impact: 50.7 | O(N^4))
  * `text` (Impact: 48.4 | O(N^4))
    * *Intent:* /// Get the text content of the hint match. /// /// This will always revalidate the hint text, to ac...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 105`, `structural_boundaries: 154`, `args: 60`, `func_start: 30`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 86`, `dead_code: 1`, `duplicate_logic: 5`, `orphaned_logic: 10`
* *Architecture:* `api: 19`, `import: 18`
* *Defense:* `safety: 86`, `doc: 64`, `test: 40`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.764
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Direction, std::rc::Rc, Dimensions, alacritty_terminal::vte::ansi::Handler, super::*, HintAction, alacritty_terminal::term::search::Match, alacritty_terminal::term::test::mock_term...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty/src/migrate/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.31 IQR)
- **Top Global Matches:** file_cluster_13: 13.31, file_cluster_8: 13.465, file_cluster_0: 13.52
- **Magnitude:** 713.94 | **LOC:** 335 | **CtrlFlow:** 48.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 20
- **Risk Profile:** Cognitive Load (26.013%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `migrate` (Impact: 654.5 | O(2^N) | DB: 20)
    * *Intent:* /// Handle migration.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 67`, `args: 19`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 54`
* *Architecture:* `api: 1`, `import: 8`
* *Defense:* `safety: 46`, `doc: 12`, `test: 5`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.764
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::fs, crate::cli::MigrateOptions, tempfile::NamedTempFile, toml_edit::DocumentMut, crate::config, std::path::Path, Item, mem...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty/src/renderer/text/builtin_font.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.086 IQR)
- **Top Global Matches:** file_cluster_8: 12.086, file_cluster_7: 12.458, file_cluster_13: 12.487
- **Magnitude:** 690.32 | **LOC:** 1033 | **CtrlFlow:** 31.3% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 30
- **Risk Profile:** Cognitive Load (9.512%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `box_drawing` (Impact: 582.2 | O(N^6) | DB: 30)
  * `builtin_glyph` (Impact: 15.9 | O(N^3) | DB: 1)
    * *Intent:* /// Returns the rasterized glyph if the character is part of the built-in font.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 173`, `args: 245`, `func_start: 11`
* *Risk/State:* `state_mutation: 79`
* *Architecture:* `api: 1`, `import: 5`
* *Defense:* `safety: 31`, `doc: 39`, `test: 7`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.764
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ops, crossfont::Metrics, std::cmp, mem, RasterizedGlyph, crossfont::BitmapBuffer, crate::config::ui_config::Delta, Metrics...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty/src/input/keyboard.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.062 IQR)
- **Top Global Matches:** file_cluster_13: 12.062, file_cluster_0: 12.156, file_cluster_8: 12.216
- **Magnitude:** 651.94 | **LOC:** 719 | **CtrlFlow:** 50.3% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (8.8337%), Tech Debt (44.2013%)
**Top Internal Functions/Classes:**
  * `key_release` (Impact: 175.4 | O(N^4) | DB: 5)
  * `alt_send_esc` (Impact: 141.3 | O(2^N) | DB: 1)
  * `process_key_bindings` (Impact: 91.8 | O(N^5) | DB: 4)
  * `should_build_sequence` (Impact: 78.6 | O(N^6))
  * `try_build_named_normal` (Impact: 41.8 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 82`, `args: 25`, `func_start: 14`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 31`, `dead_code: 3`, `duplicate_logic: 2`, `orphaned_logic: 4`
* *Architecture:* `api: 4`, `import: 13`
* *Defense:* `safety: 37`, `doc: 30`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.764
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` winit::keyboard::ModifiersKeyState, winit::event::ElementState, winit::platform::macos::OptionAsAlt, winit::platform::modifier_supplement::KeyEventExtModifierSupplement, ModifiersState, std::borrow::Cow, crate::input::ActionContext, Execute...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty/src/display/content.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.774 IQR)
- **Top Global Matches:** file_cluster_13: 12.774, file_cluster_16: 12.841, file_cluster_8: 13.03
- **Magnitude:** 638.84 | **LOC:** 553 | **CtrlFlow:** 36.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 20
- **Risk Profile:** Cognitive Load (30.1177%), Tech Debt (94.9134%)
**Top Internal Functions/Classes:**
  * `new` (Impact: 222.8 | O(2^N) | DB: 20)
    * *Intent:* /// Extra storage with rarely present fields for [`RenderableCell`], to reduce the cell size we /// ...
  * `next` (Impact: 81.2 | O(2^N) | DB: 3)
  * `new` (Impact: 56.3 | O(N^3) | DB: 2)
  * `advance` (Impact: 30.9 | O(N^4) | DB: 1)
    * *Intent:* /// Advance the hint iterator. /// /// If the point is within a hint, the keyboard shortcut characte...
  * `renderable_cursor` (Impact: 29.6 | O(N^3) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 121`, `args: 38`, `func_start: 24`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 85`, `duplicate_logic: 8`, `orphaned_logic: 1`
* *Architecture:* `api: 23`, `import: 17`
* *Defense:* `safety: 26`, `doc: 45`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.764
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` SizeInfo, alacritty_terminal::grid::Dimensions, alacritty_terminal::vte::ansi::Color, NamedColor, std::num::NonZeroU32, Flags, crate::display::color::CellRgb, mem...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty_terminal/src/selection.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.618 IQR)
- **Top Global Matches:** file_cluster_0: 12.618, file_cluster_13: 12.618, file_cluster_8: 12.717
- **Magnitude:** 550.14 | **LOC:** 669 | **CtrlFlow:** 36.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (23.6556%), Tech Debt (96.6668%)
**Top Internal Functions/Classes:**
  * `contains_cell` (Impact: 156.1 | O(N^6))
    * *Intent:* /// Check if the cell at a point is part of the selection.
  * `range_simple` (Impact: 56.8 | O(N^4) | DB: 2)
  * `range_semantic` (Impact: 43.0 | O(N^5) | DB: 2)
  * `include_all` (Impact: 36.9 | O(N^5) | DB: 1)
  * `contains` (Impact: 35.0 | O(N^4))
    * *Intent:* /// Check if a point lies within the selection.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 100`, `args: 33`, `func_start: 28`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 73`, `duplicate_logic: 2`, `orphaned_logic: 18`
* *Architecture:* `api: 10`, `import: 12`
* *Defense:* `safety: 18`, `doc: 83`, `test: 48`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.764
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::index::Column, crate::index::Boundary, Flags, GridCell, crate::vte::ansi::CursorShape, std::ops::Bound, super::*, RangeBounds...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty_terminal/src/term/search.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.875 IQR)
- **Top Global Matches:** file_cluster_0: 12.875, file_cluster_13: 13.191, file_cluster_11: 13.358
- **Magnitude:** 546.56 | **LOC:** 1252 | **CtrlFlow:** 13.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (27.8712%), Tech Debt (99.9842%)
**Top Internal Functions/Classes:**
  * `next_match_left` (Impact: 114.3 | O(N^6) | DB: 6)
  * `skip_fullwidth` (Impact: 73.1 | O(N^5) | DB: 2)
  * `next` (Impact: 37.1 | O(N^3) | DB: 1)
  * `new` (Impact: 30.9 | O(N^5))
    * *Intent:* /// Build the forward and backward search DFAs.
  * `skip` (Impact: 8.4 | O(N^3) | DB: 1)
    * *Intent:* /// Find the next regex match to the right of the origin point. /// /// The origin is always include...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 386`, `args: 47`, `func_start: 41`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 46`, `state_mutation: 149`, `dead_code: 4`, `fragile_debt: 7`, `duplicate_logic: 2`, `orphaned_logic: 35`
* *Architecture:* `api: 6`, `import: 18`
* *Defense:* `safety: 84`, `doc: 31`, `test: 87`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.764
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Direction, regex_automata::util::syntax::Config, regex_automata::hybrid::dfa::Builder, warn, crate::index::Boundary, Flags, crate::index::Column, Cache...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty/src/config/ui_config.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.877 IQR)
- **Top Global Matches:** file_cluster_13: 12.877, file_cluster_0: 12.891, file_cluster_16: 12.914
- **Magnitude:** 527.78 | **LOC:** 738 | **CtrlFlow:** 31.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (4.5858%), Tech Debt (97.0463%)
**Top Internal Functions/Classes:**
  * `deserialize` (Impact: 128.8 | O(2^N) | DB: 3)
  * `compiled` (Impact: 51.2 | O(2^N) | DB: 2)
  * `deserialize` (Impact: 51.0 | O(2^N) | DB: 1)
  * `deserialize_bindings` (Impact: 32.2 | O(N^4) | DB: 2)
    * *Intent:* /// Shell startup directory.
  * `positive_url_parsing_regex_test` (Impact: 18.7 | O(N^3) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 129`, `args: 30`, `func_start: 28`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 39`, `duplicate_logic: 9`, `orphaned_logic: 8`
* *Architecture:* `api: 53`, `import: 34`
* *Defense:* `safety: 78`, `doc: 67`, `test: 5`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.764
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::collections::HashMap, alacritty_config_derive::ConfigDeserialize, crate::config::bindings::
    self, std::rc::Rc, Shell, crate::config::selection::Selection, Deserializer, std::path::PathBuf...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty/src/config/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.132 IQR)
- **Top Global Matches:** file_cluster_13: 13.132, file_cluster_0: 13.289, file_cluster_16: 13.361
- **Magnitude:** 498.2 | **LOC:** 454 | **CtrlFlow:** 35.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (10.1675%), Tech Debt (96.3549%)
**Top Internal Functions/Classes:**
  * `imports` (Impact: 91.2 | O(2^N) | DB: 1)
  * `load_imports` (Impact: 75.5 | O(N^4) | DB: 2)
  * `installed_config` (Impact: 37.4 | O(N^5))
  * `deserialize_config` (Impact: 35.9 | O(N^3) | DB: 5)
  * `prune_yaml_nulls` (Impact: 31.7 | O(N^6) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 113`, `args: 38`, `func_start: 24`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 63`, `duplicate_logic: 7`, `orphaned_logic: 3`
* *Architecture:* `api: 26`, `import: 16`
* *Defense:* `safety: 60`, `doc: 27`, `test: 7`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.764
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` toml::Table, fs, MouseAction, warn, serde_yaml::Error, std::path::Path, SearchAction, KeyBinding...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty/src/renderer/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.182 IQR)
- **Top Global Matches:** file_cluster_13: 12.182, file_cluster_8: 12.485, file_cluster_16: 12.529
- **Magnitude:** 488.3 | **LOC:** 401 | **CtrlFlow:** 32.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (10.8878%), Tech Debt (62.9554%)
**Top Internal Functions/Classes:**
  * `new` (Impact: 162.8 | O(2^N))
    * *Intent:* /// Create a new renderer. /// /// This will automatically pick between the GLES2 and GLSL3 renderer...
  * `draw_string` (Impact: 39.3 | O(N^4) | DB: 3)
    * *Intent:* /// Draw a string in a variable location. Used for printing the render timer, warnings and /// error...
  * `load_extensions` (Impact: 25.3 | O(N^6) | DB: 4)
    * *Intent:* /// Load available OpenGL extensions.
  * `draw_cells` (Impact: 25.2 | O(2^N) | DB: 3)
  * `was_context_reset` (Impact: 22.8 | O(N^4))
    * *Intent:* /// Get the context reset status.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 86`, `args: 22`, `func_start: 19`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 50`, `duplicate_logic: 2`, `orphaned_logic: 5`
* *Architecture:* `api: 16`, `import: 25`
* *Defense:* `safety: 30`, `doc: 19`, `sync_locks: 1`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.764
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` LoaderApi, RenderRect, std::fmt, crate::renderer::rects::RectRenderer, log::LevelFilter, std::sync::atomic::AtomicBool, crossfont::Metrics, crate::display::color::Rgb...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty/src/display/window.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.782 IQR)
- **Top Global Matches:** file_cluster_0: 11.782, file_cluster_13: 11.967, file_cluster_8: 12.106
- **Magnitude:** 387.6 | **LOC:** 538 | **CtrlFlow:** 26.9% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (6.2811%), Tech Debt (66.0283%)
**Top Internal Functions/Classes:**
  * `new` (Impact: 53.9 | O(N^4) | DB: 2)
    * *Intent:* /// Create a new window. /// /// This creates a window and fully initializes a window.
  * `set_fullscreen` (Impact: 21.1 | O(2^N))
  * `get_platform_window` (Impact: 14.8 | O(N^3) | DB: 1)
  * `source` (Impact: 14.2 | O(2^N))
  * `fmt` (Impact: 14.2 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 68`, `args: 44`, `func_start: 43`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 25`, `duplicate_logic: 5`
* *Architecture:* `io: 1`, `api: 54`, `import: 18`
* *Defense:* `safety: 39`, `doc: 37`, `test: 2`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.764
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` winit::monitor::MonitorHandle, winit::platform::x11::WindowAttributesExtX11, glutin::platform::x11::X11VisualInfo, winit::platform::macos::OptionAsAlt, Fullscreen, crate::config::window::Decorations, WindowAttributesExtWindows, WindowConfig...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty_terminal/src/tty/windows/blocking.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.947 IQR)
- **Top Global Matches:** file_cluster_13: 13.947, file_cluster_4: 14.024, file_cluster_16: 14.08
- **Magnitude:** 380.82 | **LOC:** 277 | **CtrlFlow:** 30.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (41.3994%), Tech Debt (99.9987%)
**Top Internal Functions/Classes:**
  * `new` (Impact: 99.4 | O(2^N) | DB: 5)
  * `new` (Impact: 87.3 | O(2^N) | DB: 5)
  * `wake_by_ref` (Impact: 25.9 | O(N^4) | DB: 1)
  * `register` (Impact: 22.8 | O(N^3) | DB: 1)
  * `register` (Impact: 18.4 | O(N^3) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 69`, `args: 18`, `func_start: 15`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 51`, `duplicate_logic: 10`, `orphaned_logic: 2`
* *Architecture:* `io: 1`, `api: 10`, `concurrency: 24`, `import: 10`
* *Defense:* `safety: 49`, `doc: 21`, `sync_locks: 9`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.764
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` PollerIocpExt, piper::Reader, Waker, std::task::Context, pipe, polling::Event, Poll, Mutex...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty/src/display/color.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.832 IQR)
- **Top Global Matches:** file_cluster_16: 11.832, file_cluster_0: 11.899, file_cluster_13: 11.915
- **Magnitude:** 331.38 | **LOC:** 369 | **CtrlFlow:** 35.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (22.4313%), Tech Debt (98.3356%)
**Top Internal Functions/Classes:**
  * `fill_cube` (Impact: 80.1 | O(N^6) | DB: 2)
  * `deserialize` (Impact: 58.2 | O(2^N) | DB: 1)
  * `from_str` (Impact: 41.0 | O(N^4) | DB: 1)
  * `fill_gray_ramp` (Impact: 22.8 | O(N^4) | DB: 2)
  * `deserialize` (Impact: 19.6 | O(N^5) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 83`, `args: 29`, `func_start: 25`, `class_start: 6`
* *Risk/State:* `state_mutation: 30`, `duplicate_logic: 8`
* *Architecture:* `api: 14`, `import: 10`
* *Defense:* `safety: 31`, `doc: 4`, `test: 2`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.764
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` alacritty_terminal::vte::ansi::NamedColor, std::ops::Add, Mul, Deserializer, Deref, alacritty_config_derive::SerdeReplace, Display, crate::config::color::Colors...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty/src/config/window.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.854 IQR)
- **Top Global Matches:** file_cluster_0: 11.854, file_cluster_16: 11.898, file_cluster_13: 12.011
- **Magnitude:** 288.78 | **LOC:** 327 | **CtrlFlow:** 38.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (3.9834%), Tech Debt (93.8781%)
**Top Internal Functions/Classes:**
  * `deserialize` (Impact: 100.8 | O(2^N) | DB: 3)
  * `dimensions` (Impact: 77.6 | O(2^N))
  * `option_as_alt` (Impact: 10.8 | O(2^N))
  * `from` (Impact: 8.3 | O(N^3))
  * `from` (Impact: 8.3 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 44`, `args: 17`, `func_start: 16`, `class_start: 10`
* *Risk/State:* `state_mutation: 7`, `duplicate_logic: 5`
* *Architecture:* `api: 36`, `import: 9`
* *Defense:* `safety: 34`, `doc: 29`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.764
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` alacritty_config_derive::ConfigDeserialize, winit::platform::macos::OptionAsAlt, Deserializer, warn, MapAccess, crate::config::LOG_TARGET_CONFIG, log::error, winit::window::Fullscreen...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty_terminal/src/tty/unix.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.566 IQR)
- **Top Global Matches:** file_cluster_13: 12.566, file_cluster_0: 12.859, file_cluster_8: 13.051
- **Magnitude:** 284.02 | **LOC:** 449 | **CtrlFlow:** 23.0% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (10.418%), Tech Debt (87.1217%)
**Top Internal Functions/Classes:**
  * `default_shell_command` (Impact: 176.8 | O(2^N) | DB: 6)
  * `from_env` (Impact: 31.8 | O(N^4) | DB: 2)
    * *Intent:* /// look for shell, username, longname, and home dir in the respective environment variables /// bef...
  * `get_pw_entry` (Impact: 12.6 | O(N^2) | DB: 6)
    * *Intent:* /// Return a Passwd struct with pointers into the provided buf. /// /// # Unsafety /// /// If `buf` ...
  * `set_controlling_terminal` (Impact: 9.6 | O(N^2))
    * *Intent:* /// Really only needed on BSD, but should be fine elsewhere.
  * `child` (Impact: 5.3 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 94`, `args: 14`, `func_start: 12`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 28`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 2`, `api: 7`, `concurrency: 1`, `import: 25`
* *Defense:* `safety: 43`, `doc: 18`, `test: 3`, `immutability_locks: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.764
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` signal_hook::SigId, InputModes, EventedPty, O_NONBLOCK, Result, rustix_openpty::openpty, unregister, std::path::Path...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty/src/renderer/rects.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.008 IQR)
- **Top Global Matches:** file_cluster_13: 12.008, file_cluster_0: 12.141, file_cluster_8: 12.189
- **Magnitude:** 270.28 | **LOC:** 497 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (11.765%), Tech Debt (99.8934%)
**Top Internal Functions/Classes:**
  * `update_flag` (Impact: 43.4 | O(N^4) | DB: 5)
  * `update_uniforms` (Impact: 41.6 | O(N^4))
  * `draw` (Impact: 36.1 | O(N^5) | DB: 3)
  * `new` (Impact: 21.8 | O(2^N))
  * `rects` (Impact: 18.5 | O(2^N) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 83`, `args: 16`, `func_start: 13`, `class_start: 5`
* *Risk/State:* `state_mutation: 37`, `fragile_debt: 1`, `duplicate_logic: 5`, `orphaned_logic: 4`
* *Architecture:* `api: 23`, `import: 14`
* *Defense:* `safety: 32`, `doc: 15`, `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.764
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::collections::HashMap, alacritty_terminal::grid::Dimensions, alacritty_terminal::index::Column, crate::display::SizeInfo, renderer, crate::gl::types::*, crate::renderer::shader::ShaderError, alacritty_terminal::term::cell::Flags...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty/src/renderer/text/gles2.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.133 IQR)
- **Top Global Matches:** file_cluster_13: 11.133, file_cluster_8: 11.191, file_cluster_16: 11.196
- **Magnitude:** 263.4 | **LOC:** 505 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (17.6705%), Tech Debt (89.4999%)
**Top Internal Functions/Classes:**
  * `new` (Impact: 90.8 | O(2^N) | DB: 9)
  * `new` (Impact: 42.2 | O(2^N))
  * `render_batch` (Impact: 22.6 | O(N^4) | DB: 1)
  * `drop` (Impact: 8.2 | O(N^3) | DB: 1)
  * `with_api` (Impact: 6.4 | O(N^3) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 74`, `args: 15`, `func_start: 14`, `class_start: 3`
* *Risk/State:* `state_mutation: 47`, `duplicate_logic: 4`, `orphaned_logic: 3`
* *Architecture:* `api: 4`, `import: 13`
* *Defense:* `safety: 5`, `doc: 16`, `immutability_locks: 5`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.764
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` crate::renderer::Error, RenderingGlyphFlags, LoaderApi, std::ptr, crate::display::SizeInfo, super::
    Glyph, LoadGlyph, RenderingPass...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alacritty/src/renderer/text/glsl3.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.97 IQR)
- **Top Global Matches:** file_cluster_8: 10.97, file_cluster_13: 10.975, file_cluster_16: 10.998
- **Magnitude:** 257.16 | **LOC:** 463 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (20.2807%), Tech Debt (92.6132%)
**Top Internal Functions/Classes:**
  * `new` (Impact: 40.5 | O(2^N))
  * `new` (Impact: 29.4 | O(2^N) | DB: 8)
  * `render_batch` (Impact: 16.9 | O(N^4) | DB: 1)
  * `add_item` (Impact: 10.6 | O(N^3) | DB: 2)
  * `drop` (Impact: 8.2 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 78`, `args: 24`, `func_start: 24`, `class_start: 5`
* *Risk/State:* `state_mutation: 53`, `duplicate_logic: 7`
* *Architecture:* `api: 17`, `import: 13`
* *Defense:* `safety: 6`, `doc: 10`, `immutability_locks: 6`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 6.963
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003876
  * `Imports (Out-Degree: 0):` crate::renderer::Error, RenderingGlyphFlags, LoaderApi, std::ptr, crate::display::SizeInfo, super::
    Glyph, LoadGlyph, RenderingPass...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `alacritty_terminal/src/selection.rs` (RUST) | Magnitude: 550.14 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 369, structural_boundaries: 100, doc: 83, state_mutation: 73
- `alacritty/src/config/window.rs` (RUST) | Magnitude: 288.78 | Delta: **0.044 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 185, structural_boundaries: 44, api: 36, safety: 34
- `alacritty_terminal/src/term/mod.rs` (RUST) | Magnitude: 2088.6 | Delta: **0.063 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 2318, structural_boundaries: 524, state_mutation: 366, branch: 262
- `alacritty/src/daemon.rs` (RUST) | Magnitude: 108.16 | Delta: **0.064 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 79, structural_boundaries: 37, state_mutation: 19, decorators: 19
- `alacritty_terminal/src/term/cell.rs` (RUST) | Magnitude: 95.22 | Delta: **0.084 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 111, structural_boundaries: 34, generics: 26, safety: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `extra/completions/alacritty.bash` (SHELL) | Magnitude: 1431.12 | Delta: **0.067 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 441, state_mutation: 383, branch: 209, safety: 148

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `alacritty/src/config/general.rs` (RUST) | Magnitude: 12.72 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 13, doc: 12, structural_boundaries: 5, api: 5
- `alacritty/src/config/ui_config.rs` (RUST) | Magnitude: 527.78 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 380, structural_boundaries: 129, generics: 89, safety: 78
- `alacritty/src/display/damage.rs` (RUST) | Magnitude: 179.06 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 179, structural_boundaries: 73, state_mutation: 34, doc: 27
- `alacritty/src/config/terminal.rs` (RUST) | Magnitude: 17.72 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 10, indent_spaces: 9, generics: 7, api: 5
- `alacritty/src/renderer/text/atlas.rs` (RUST) | Magnitude: 166.7 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 169, doc: 47, structural_boundaries: 37, state_mutation: 29

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `alacritty/src/config/font.rs` (RUST) | Magnitude: 18.02 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 22, doc: 21, structural_boundaries: 12, generics: 11
- `alacritty_terminal/src/term/color.rs` (RUST) | Magnitude: 23.62 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 16, doc: 14, generics: 10
- `alacritty/src/config/bindings.rs` (RUST) | Magnitude: 951.32 | Delta: **0.061 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 998, structural_boundaries: 200, safety: 174, generics: 140
- `alacritty/src/config/mouse.rs` (RUST) | Magnitude: 15.5 | Delta: **0.062 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 9, generics: 8, api: 6
- `alacritty/src/display/color.rs` (RUST) | Magnitude: 331.38 | Delta: **0.067 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 248, structural_boundaries: 83, generics: 50, branch: 45

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `alacritty/src/renderer/text/glsl3.rs` (RUST) | Magnitude: 257.16 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 295, structural_boundaries: 78, state_mutation: 53, generics: 35
- `alacritty/src/config/bell.rs` (RUST) | Magnitude: 19.42 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 9, api: 6, doc: 6
- `alacritty/src/config/cursor.rs` (RUST) | Magnitude: 110.9 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 93, structural_boundaries: 18, decorators: 14, api: 13
- `alacritty/src/panic.rs` (RUST) | Magnitude: 7.4 | Delta: **0.036 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 6, import: 4, args: 3
- `alacritty/src/config/serde_utils.rs` (RUST) | Magnitude: 43.5 | Delta: **0.058 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 62, structural_boundaries: 31, state_mutation: 15, test: 11

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `alacritty/src/display/mod.rs` -> **skewb1k** (100.0% isolated ownership) | Magnitude: 1113.66
- `alacritty/src/config/bindings.rs` -> **Jonas** (100.0% isolated ownership) | Magnitude: 951.32
- `alacritty/src/config/mod.rs` -> **Jonas** (100.0% isolated ownership) | Magnitude: 498.2
- `alacritty/src/polling/mod.rs` -> **Christian Duerr** (100.0% isolated ownership) | Magnitude: 215.52
- `alacritty/src/polling/ipc.rs` -> **Christian Duerr** (100.0% isolated ownership) | Magnitude: 167.06

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `alacritty/src/renderer/platform.rs` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 56.1452%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `alacritty_terminal/src/thread.rs` -> **Severity: 0.31** (Embedded: 0.0039 * Error Risk: 80.0%)
- `alacritty/src/renderer/text/glsl3.rs` -> **Severity: 0.253** (Embedded: 0.0039 * Error Risk: 65.3819%)
- `alacritty/src/renderer/platform.rs` -> **Severity: 0.092** (Embedded: 0.0039 * Error Risk: 23.6994%)
- `alacritty_config_derive/src/serde_replace.rs` -> **Severity: 0.082** (Embedded: 0.0039 * Error Risk: 21.1415%)
- `alacritty/src/polling/ipc.rs` -> **Severity: 0.046** (Embedded: 0.0039 * Error Risk: 11.8946%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `alacritty/src/config/debug.rs` -> **Severity: 1288.714** (Blast Radius: 12.888 * Doc Risk: 99.9933%)
- `alacritty/src/renderer/platform.rs` -> **Severity: 696.3** (Blast Radius: 6.963 * Doc Risk: 100.0%)
- `alacritty_config_derive/src/serde_replace.rs` -> **Severity: 693.178** (Blast Radius: 6.963 * Doc Risk: 99.5516%)
- `alacritty/src/renderer/text/glsl3.rs` -> **Severity: 689.513** (Blast Radius: 6.963 * Doc Risk: 99.0253%)
- `alacritty/src/polling/ipc.rs` -> **Severity: 627.962** (Blast Radius: 6.963 * Doc Risk: 90.1855%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
