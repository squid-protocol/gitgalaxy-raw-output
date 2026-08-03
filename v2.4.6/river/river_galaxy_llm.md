# ARCHITECTURAL_BRIEF: river
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_zig/river` |
| **Timestamp** | `2026-08-03T20:08:52.261956+00:00` |
| **Scan Duration** | `0.39s` |
| **Git Branch** | `main` |
| **Git Commit** | `79e09c3628a88b7b71fc178dccd1b5ab8e7681b0` |
| **Git Remote** | `https://github.com/ifreund/river.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 54 malicious artifacts.

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
| Total Artifacts | 87 |
| Analyzed Artifacts (Scanned) | 69 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 18 |
| Total LOC | 11835 |
| Volatility Index | 0.058 |
| % Scanned of codebase = | 79.3% |
| Dominant Lang | ZIG |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2757 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3222 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 53.6% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.0152 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 2 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| ZIG | 53 | 11807 | 76.8% |
| XML | 11 | 0 | 15.9% |
| MARKDOWN | 4 | 0 | 5.8% |
| C | 1 | 28 | 1.4% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `6.26`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 48 | 69.6% |
| file_cluster_13 | 17 | 24.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 4 | 5.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 18*

**Composition by Extension & Reason:**
- `.yml`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.zig`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.zon`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.desktop`: 1x Excluded (Unsupported Extension: '.desktop')
- `.scd`: 1x Excluded (Unsupported Extension: '.scd')
- `.xml`: 1x Excluded (Static Asset Blob without Intent: 1855 LOC)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 5.0 | 67.1 | 16.3 | 13.9 | 5.0 |
| Error & Exception Exposure | 0.0 | 80.0 | 24.6 | 7.6 | 0.0 |
| Tech Debt Exposure | 0.0 | 96.0 | 9.9 | 0.0 | 0.0 |
| Testing Exposure | 0.2 | 80.0 | 52.2 | 80.0 | 80.0 |
| API Exposure | 0.0 | 9.5 | 1.4 | 0.9 | 0.0 |
| Concurrency Exposure | 0.0 | 35.0 | 0.5 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 12.1 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 7.7 | 0.7 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 83.7 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 1.8 | 0.3 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 19.7 | 0.0 | 0.0 |
| Documentation Exposure | 0.8 | 100.0 | 78.7 | 99.2 | 100.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 68.8 | 99.6 | 100.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 20.0 | 14.3 | 20.0 | 20.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 1.5 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.5 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `river/main.zig` (Hits: 5)
- `river/XkbConfig.zig` (Hits: 2)
- `river/Cursor.zig` (Hits: 1)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **util.zig** (`river/util.zig`) — 44 inbound connections
2. **Seat.zig** (`river/Seat.zig`) — 21 inbound connections
3. **SceneNodeData.zig** (`river/SceneNodeData.zig`) — 15 inbound connections
4. **Output.zig** (`river/Output.zig`) — 14 inbound connections
5. **Window.zig** (`river/Window.zig`) — 12 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **Seat.zig** (`river/Seat.zig`) — 26 outbound dependencies
2. **Server.zig** (`river/Server.zig`) — 25 outbound dependencies
3. **Cursor.zig** (`river/Cursor.zig`) — 17 outbound dependencies
4. **Window.zig** (`river/Window.zig`) — 14 outbound dependencies
5. **InputManager.zig** (`river/InputManager.zig`) — 11 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `Deque` (@ `common/deque.zig`) -> Impact: **950.5** | LOC: 250
  * *Intent:* /// A contiguous, growable, double-ended queue. /// /// Pushing/popping items from either end of the queue is O(1).
- `handleRequest` (@ `river/LibinputDevice.zig`) -> Impact: **888.6** | LOC: 330
- `init` (@ `river/Server.zig`) -> Impact: **465.2** | LOC: 125
- `handleRequest` (@ `river/Window.zig`) -> Impact: **437.7** | LOC: 167
- `manageStart` (@ `river/Seat.zig`) -> Impact: **395.3** | LOC: 147
- `commitOutputState` (@ `river/OutputManager.zig`) -> Impact: **328.6** | LOC: 147
- `renderFinish` (@ `river/WindowManager.zig`) -> Impact: **259.9** | LOC: 106
  * *Intent:* /// Finish the update sequence and drop stashed buffers. This means that /// the next frame drawn will be the post-transaction state.
- `manageStart` (@ `river/Window.zig`) -> Impact: **243.9** | LOC: 149
  * *Intent:* /// Send dirty state as part of a manage sequence.
- `create` (@ `river/Keyboard.zig`) -> Impact: **226.3** | LOC: 46
- `configure` (@ `river/XdgToplevel.zig`) -> Impact: **203.8** | LOC: 92
  * *Intent:* /// Send a configure event, return true if the configure should be tracked /// and current surfaces saved for frame perfection.

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `Deque` (@ `common/deque.zig`) -> **O(2^N) [Recursive]**
  * *Intent:* /// A contiguous, growable, double-ended queue. /// /// Pushing/popping items from either end of the queue is O(1).
- `create` (@ `river/Keyboard.zig`) -> **O(2^N) [Recursive]**
- `manageStart` (@ `river/Output.zig`) -> **O(2^N) [Recursive]**
- `manageStart` (@ `river/Seat.zig`) -> **O(2^N) [Recursive]**
- `manageFinish` (@ `river/Seat.zig`) -> **O(2^N) [Recursive]**
- `renderFinish` (@ `river/WindowManager.zig`) -> **O(2^N) [Recursive]**
  * *Intent:* /// Finish the update sequence and drop stashed buffers. This means that /// the next frame drawn will be the post-transaction state.
- `manageFinish` (@ `river/WindowManager.zig`) -> **O(2^N) [Recursive]**
- `focus` (@ `river/InputRelay.zig`) -> **O(2^N) [Recursive]**
- `init` (@ `river/InputDevice.zig`) -> **O(2^N) [Recursive]**
- `deinit` (@ `river/InputDevice.zig`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `handleRequest` (@ `river/LibinputDevice.zig`) -> DB Complexity: **25**
- `renderFinish` (@ `river/WindowManager.zig`) -> DB Complexity: **7**
  * *Intent:* /// Finish the update sequence and drop stashed buffers. This means that /// the next frame drawn will be the post-transaction state.
- `commitOutputState` (@ `river/OutputManager.zig`) -> DB Complexity: **6**
- `handleRequest` (@ `river/XkbKeyboard.zig`) -> DB Complexity: **6**
- `grepRiverctl` (@ `river/main.zig`) -> DB Complexity: **6**
- `createObject` (@ `river/LibinputDevice.zig`) -> DB Complexity: **5**
- `drawBorders` (@ `river/Window.zig`) -> DB Complexity: **5**
- `fuzzAgainstArrayList` (@ `common/deque.zig`) -> DB Complexity: **4**
- `update` (@ `river/InputPopup.zig`) -> DB Complexity: **4**
- `autoLayout` (@ `river/OutputManager.zig`) -> DB Complexity: **4**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `river` | 51 | 14812.06 | 18.13% | 11.65% |
| `common` | 3 | 1484.54 | 27.25% | 17.29% |
| `protocol` | 5 | 52.6 | 5.0% | 0.0% |
| `logo` | 3 | 31.56 | 5.0% | 0.0% |
| `protocol/upstream` | 3 | 31.56 | 5.0% | 0.0% |
| `__monolith__` | 4 | 9.6 | 0.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `river/Scene.zig` -> **96.0388%** Exposure
- `river/wlroots_log_wrapper.c` -> **94.5687%** Exposure
- `river/IdleInhibitManager.zig` -> **73.1059%** Exposure
- `river/TextInput.zig` -> **68.4344%** Exposure
- `river/XdgPopup.zig` -> **40.334%** Exposure
### Highest State Flux (Mutation/Volatility)
- `river/wlroots_log_wrapper.c` -> **99.9556%** Exposure
- `river/OutputManager.zig` -> **76.8341%** Exposure
- `river/WindowManager.zig` -> **74.4354%** Exposure
- `river/LibinputDevice.zig` -> **67.1342%** Exposure
- `river/IdleInhibitManager.zig` -> **66.8188%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `river/Scene.zig` -> **0** Orphaned Functions | **2** Duplicates
- `river/main.zig` -> **2** Orphaned Functions | **0** Duplicates
- `river/wlroots_log_wrapper.c` -> **1** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`river/Server.zig`** -> AI Confidence: **99.48%**
2. **`river/Cursor.zig`** -> AI Confidence: **99.42%**
3. **`river/InputManager.zig`** -> AI Confidence: **99.42%**
4. **`river/InputRelay.zig`** -> AI Confidence: **99.42%**
5. **`river/Keyboard.zig`** -> AI Confidence: **99.42%**
6. **`river/XwaylandOverrideRedirect.zig`** -> AI Confidence: **99.42%**
7. **`river/XwaylandWindow.zig`** -> AI Confidence: **99.42%**
8. **`river/main.zig`** -> AI Confidence: **99.39%**
9. **`river/LayerShell.zig`** -> AI Confidence: **99.34%**
10. **`river/OutputManager.zig`** -> AI Confidence: **99.34%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `common/deque.zig` -> **20.0%** Exposure
- `common/flags.zig` -> **20.0%** Exposure
- `common/slotmap.zig` -> **20.0%** Exposure
- `river/Cursor.zig` -> **20.0%** Exposure
- `river/Decoration.zig` -> **20.0%** Exposure
### Weaponizable Injection Vectors
- `river/util.zig` -> **100.0%** Exposure
### Raw Memory Manipulation
- `river/Cursor.zig` -> **0.5364%** Exposure
- `river/PointerConstraint.zig` -> **0.1263%** Exposure
- `river/InputManager.zig` -> **0.1166%** Exposure
- `river/XdgToplevel.zig` -> **0.0137%** Exposure
- `river/XdgDecoration.zig` -> **0.0101%** Exposure
### Algorithmic DoS Exposure
- `common/deque.zig` -> **100.0%** Exposure
- `common/flags.zig` -> **100.0%** Exposure
- `common/slotmap.zig` -> **100.0%** Exposure
- `river/Cursor.zig` -> **100.0%** Exposure
- `river/IdleInhibitManager.zig` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `399` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `river/LibinputDevice.zig` (ZIG) -> Cumulative Risk: **630.2**
- **Archetype:** `file_cluster_8` (Distance: 12.698 IQR)
- **Magnitude:** 1221.96 | **LOC:** 550 | **CtrlFlow:** 69.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Verification (80.0%)
- **Heaviest Functions:** `handleRequest` (Impact: 888.6), `createObject` (Impact: 158.1), `create` (Impact: 28.1)

### 2. `river/OutputManager.zig` (ZIG) -> Cumulative Risk: **612.15**
- **Archetype:** `file_cluster_8` (Distance: 12.237 IQR)
- **Magnitude:** 721.06 | **LOC:** 455 | **CtrlFlow:** 72.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Verification (80.0%)
- **Heaviest Functions:** `commitOutputState` (Impact: 328.6), `validateConfigCoordinates` (Impact: 74.2), `handlePowerManagerSetMode` (Impact: 45.2)

### 3. `river/IdleInhibitManager.zig` (ZIG) -> Cumulative Risk: **597.74**
- **Archetype:** `file_cluster_13` (Distance: 11.803 IQR)
- **Magnitude:** 66.2 | **LOC:** 62 | **CtrlFlow:** 75.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.9827%), Verification (80.0%)
- **Heaviest Functions:** `checkActive` (Impact: 26.8), `init` (Impact: 10.8), `handleNewIdleInhibitor` (Impact: 8.1)

### 4. `river/WindowManager.zig` (ZIG) -> Cumulative Risk: **573.93**
- **Archetype:** `file_cluster_8` (Distance: 11.802 IQR)
- **Magnitude:** 809.92 | **LOC:** 563 | **CtrlFlow:** 74.1% | **Authorship Centralization:** 80.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Verification (80.0%)
- **Heaviest Functions:** `renderFinish` (Impact: 259.9), `manageStart` (Impact: 89.0), `manageFinish` (Impact: 86.7)

### 5. `river/TextInput.zig` (ZIG) -> Cumulative Risk: **572.36**
- **Archetype:** `file_cluster_8` (Distance: 10.171 IQR)
- **Magnitude:** 65.08 | **LOC:** 113 | **CtrlFlow:** 80.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (90.2979%), Safety Score (80.0%)
- **Heaviest Functions:** `handleEnable` (Impact: 25.5), `create` (Impact: 11.3), `handleCommit` (Impact: 11.0)

### 6. `river/Scene.zig` (ZIG) -> Cumulative Risk: **553.18**
- **Archetype:** `file_cluster_13` (Distance: 12.24 IQR)
- **Magnitude:** 219.86 | **LOC:** 202 | **CtrlFlow:** 75.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Tech Debt (96.0388%)
- **Heaviest Functions:** `init` (Impact: 64.1), `at` (Impact: 56.4), `saveSurfaceTreeIter` (Impact: 15.4)

### 7. `river/LockSurface.zig` (ZIG) -> Cumulative Risk: **552.55**
- **Archetype:** `file_cluster_13` (Distance: 11.914 IQR)
- **Magnitude:** 122.94 | **LOC:** 125 | **CtrlFlow:** 64.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (99.9975%), Documentation (99.2291%), Verification (80.0%)
- **Heaviest Functions:** `destroy` (Impact: 70.7), `handleMap` (Impact: 11.2), `updateFocus` (Impact: 10.9)

### 8. `river/InputDevice.zig` (ZIG) -> Cumulative Risk: **538.66**
- **Archetype:** `file_cluster_8` (Distance: 11.241 IQR)
- **Magnitude:** 533.84 | **LOC:** 296 | **CtrlFlow:** 76.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Verification (80.0%)
- **Heaviest Functions:** `handleRequest` (Impact: 199.9), `init` (Impact: 198.9), `deinit` (Impact: 44.6)

### 9. `river/Window.zig` (ZIG) -> Cumulative Risk: **535.05**
- **Archetype:** `file_cluster_8` (Distance: 12.076 IQR)
- **Magnitude:** 1357.8 | **LOC:** 1212 | **CtrlFlow:** 74.6% | **Authorship Centralization:** 77.8%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Churn (89.77%)
- **Heaviest Functions:** `handleRequest` (Impact: 437.7), `manageStart` (Impact: 243.9), `manageFinish` (Impact: 108.2)

### 10. `river/XdgToplevel.zig` (ZIG) -> Cumulative Risk: **534.07**
- **Archetype:** `file_cluster_8` (Distance: 10.127 IQR)
- **Magnitude:** 450.54 | **LOC:** 475 | **CtrlFlow:** 72.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (99.9654%), Verification (80.0%)
- **Heaviest Functions:** `configure` (Impact: 203.8), `handleCommit` (Impact: 60.6), `needsConfigure` (Impact: 58.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `river/Seat.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.39 IQR)
- **Top Global Matches:** file_cluster_8: 12.39, file_cluster_13: 12.467, file_cluster_7: 12.748
- **Magnitude:** 1533.32 | **LOC:** 1035 | **CtrlFlow:** 77.1% | **Authorship Centralization:** 87.5%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (13.0608%), Tech Debt (9.5089%)
**Top Internal Functions/Classes:**
  * `manageStart` (Impact: 395.3 | O(2^N) | DB: 2)
  * `manageFinish` (Impact: 185.0 | O(2^N))
  * `handleRequest` (Impact: 143.9 | O(N^5))
  * `matchXkbBinding` (Impact: 120.1 | O(N^5) | DB: 3)
    * *Intent:* /// Handle any user-defined mapping for passed keycode, modifiers and keyboard state /// Returns tru...
  * `focus` (Impact: 114.9 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 178`, `structural_boundaries: 53`, `args: 29`, `func_start: 29`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 48`, `dead_code: 2`, `planned_debt: 2`
* *Architecture:* `api: 37`, `import: 27`
* *Defense:* `safety: 98`, `doc: 15`, `immutability_locks: 75`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 60.188
  * `Choke Point (Betweenness):` 0.241211 | `Ripple Effect (Closeness):` 0.381787
  * `Imports (Out-Degree: 21):` PointerBinding.zig, LockSurface.zig, XkbBindingsSeat.zig, LayerSurface.zig, InputManager.zig, InputRelay.zig, util.zig, XwaylandOverrideRedirect.zig...
  * `Imported By (In-Degree: 21):` (Excluded from Brief to save tokens)

### `river/Window.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.076 IQR)
- **Top Global Matches:** file_cluster_8: 12.076, file_cluster_13: 12.307, file_cluster_7: 12.353
- **Magnitude:** 1357.8 | **LOC:** 1212 | **CtrlFlow:** 74.6% | **Authorship Centralization:** 77.8%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (11.0154%), Tech Debt (8.7967%)
**Top Internal Functions/Classes:**
  * `handleRequest` (Impact: 437.7 | O(N^5))
  * `manageStart` (Impact: 243.9 | O(N^6))
    * *Intent:* /// Send dirty state as part of a manage sequence.
  * `manageFinish` (Impact: 108.2 | O(N^4) | DB: 1)
    * *Intent:* /// Applies window management state from the window manager and sends a configure /// to the window ...
  * `renderStart` (Impact: 82.4 | O(N^6))
  * `renderFinish` (Impact: 50.6 | O(2^N) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 238`, `structural_boundaries: 81`, `args: 29`, `func_start: 29`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 40`, `dead_code: 3`, `planned_debt: 1`
* *Architecture:* `io: 1`, `api: 40`, `import: 16`
* *Defense:* `safety: 97`, `doc: 50`, `immutability_locks: 78`, `cleanup: 17`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 39.91
  * `Choke Point (Betweenness):` 0.098722 | `Ripple Effect (Closeness):` 0.350346
  * `Imports (Out-Degree: 10):` util.zig, WmNode.zig, XwaylandWindow.zig, Scene.zig, Decoration.zig, Output.zig, slotmap, XdgToplevel.zig...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `river/LibinputDevice.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.27%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.698 IQR)
- **Top Global Matches:** file_cluster_8: 12.698, file_cluster_13: 12.862, file_cluster_0: 13.073
- **Magnitude:** 1221.96 | **LOC:** 550 | **CtrlFlow:** 69.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 25
- **Risk Profile:** Cognitive Load (67.1011%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `handleRequest` (Impact: 888.6 | O(N^5) | DB: 25)
  * `createObject` (Impact: 158.1 | O(N^4) | DB: 5)
  * `create` (Impact: 28.1 | O(2^N))
  * `send` (Impact: 14.3 | O(N^3))
  * `init` (Impact: 11.0 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 172`, `structural_boundaries: 75`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 52`, `state_mutation: 91`
* *Architecture:* `api: 6`, `import: 9`
* *Defense:* `safety: 70`, `doc: 1`, `immutability_locks: 107`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 10.513
  * `Choke Point (Betweenness):` 0.009877 | `Ripple Effect (Closeness):` 0.201212
  * `Imports (Out-Degree: 4):` util.zig, InputDevice.zig, std, c.zig, LibinputAccelConfig.zig, wlroots, wayland
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `common/deque.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.704 IQR)
- **Top Global Matches:** file_cluster_8: 12.704, file_cluster_7: 12.832, file_cluster_13: 13.008
- **Magnitude:** 1134.94 | **LOC:** 435 | **CtrlFlow:** 73.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (15.9141%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Deque` (Impact: 950.5 | O(2^N) | DB: 3)
    * *Intent:* /// A contiguous, growable, double-ended queue. /// /// Pushing/popping items from either end of the...
  * `fuzzAgainstArrayList` (Impact: 118.0 | O(N^5) | DB: 4)
  * `addOrOom` (Impact: 1.8 | O(N^1))
    * *Intent:* /// Integer addition returning `error.OutOfMemory` on overflow.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 131`, `structural_boundaries: 48`, `args: 24`, `func_start: 24`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 34`
* *Architecture:* `api: 22`, `concurrency: 1`, `import: 1`
* *Defense:* `safety: 62`, `doc: 68`, `test: 5`, `immutability_locks: 39`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 8.141
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.250949
  * `Imports (Out-Degree: 0):` std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `river/Server.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.214 IQR)
- **Top Global Matches:** file_cluster_8: 12.214, file_cluster_13: 12.319, file_cluster_7: 12.66
- **Magnitude:** 897.08 | **LOC:** 573 | **CtrlFlow:** 82.4% | **Authorship Centralization:** 83.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (15.7137%), Tech Debt (12.6549%)
**Top Internal Functions/Classes:**
  * `init` (Impact: 465.2 | O(2^N) | DB: 2)
  * `globalFilter` (Impact: 67.2 | O(N^5))
  * `start` (Impact: 63.0 | O(2^N) | DB: 1)
    * *Intent:* /// Create the socket, start the backend, and setup the environment
  * `handleRequestSetCursorShape` (Impact: 51.7 | O(N^4))
  * `allowlist` (Impact: 41.4 | O(N^2))
    * *Intent:* /// Returns true if the global is allowlisted for security contexts
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 140`, `structural_boundaries: 30`, `args: 16`, `func_start: 16`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 12`, `planned_debt: 3`
* *Architecture:* `io: 1`, `api: 3`, `import: 25`
* *Defense:* `safety: 80`, `doc: 5`, `immutability_locks: 62`, `cleanup: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.674
  * `Choke Point (Betweenness):` 0.010316 | `Ripple Effect (Closeness):` 0.014706
  * `Imports (Out-Degree: 21):` TabletTool.zig, InputManager.zig, SceneNodeData.zig, LockManager.zig, util.zig, XwaylandOverrideRedirect.zig, Window.zig, Scene.zig...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `river/WindowManager.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.802 IQR)
- **Top Global Matches:** file_cluster_8: 11.802, file_cluster_13: 11.964, file_cluster_7: 12.143
- **Magnitude:** 809.92 | **LOC:** 563 | **CtrlFlow:** 74.1% | **Authorship Centralization:** 80.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (15.6552%), Tech Debt (15.0793%)
**Top Internal Functions/Classes:**
  * `renderFinish` (Impact: 259.9 | O(2^N) | DB: 7)
    * *Intent:* /// Finish the update sequence and drop stashed buffers. This means that /// the next frame drawn wi...
  * `manageStart` (Impact: 89.0 | O(2^N) | DB: 3)
  * `manageFinish` (Impact: 86.7 | O(2^N) | DB: 2)
  * `handleRequest` (Impact: 56.4 | O(N^5))
  * `renderStart` (Impact: 44.6 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 29`, `args: 24`, `func_start: 24`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 51`, `planned_debt: 2`, `fragile_debt: 1`
* *Architecture:* `api: 15`, `import: 13`
* *Defense:* `safety: 36`, `doc: 15`, `immutability_locks: 25`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.974
  * `Choke Point (Betweenness):` 0.000512 | `Ripple Effect (Closeness):` 0.019608
  * `Imports (Out-Degree: 8):` util.zig, ShellSurface.zig, Window.zig, WmNode.zig, Scene.zig, Output.zig, slotmap, std...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `river/Cursor.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.42%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.797 IQR)
- **Top Global Matches:** file_cluster_8: 11.797, file_cluster_13: 12.116, file_cluster_7: 12.14
- **Magnitude:** 783.28 | **LOC:** 928 | **CtrlFlow:** 81.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (8.9464%), Tech Debt (9.811%)
**Top Internal Functions/Classes:**
  * `processButton` (Impact: 187.1 | O(N^6) | DB: 2)
  * `processMotionRelative` (Impact: 57.5 | O(N^6) | DB: 2)
  * `updateHovered` (Impact: 56.4 | O(N^6))
  * `handleRequestSetCursor` (Impact: 55.9 | O(N^5))
  * `setTheme` (Impact: 49.6 | O(N^5))
    * *Intent:* /// Set the cursor theme for the given seat, as well as the xwayland theme if /// this is the defaul...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 121`, `structural_boundaries: 27`, `args: 41`, `func_start: 41`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 29`, `planned_debt: 2`
* *Architecture:* `io: 1`, `api: 17`, `import: 18`
* *Defense:* `safety: 60`, `doc: 26`, `immutability_locks: 87`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 10.854
  * `Choke Point (Betweenness):` 0.016974 | `Ripple Effect (Closeness):` 0.250247
  * `Imports (Out-Degree: 13):` util.zig, XwaylandOverrideRedirect.zig, Window.zig, PointerBinding.zig, Scene.zig, InputDevice.zig, DragIcon.zig, LockSurface.zig...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `river/OutputManager.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.237 IQR)
- **Top Global Matches:** file_cluster_8: 12.237, file_cluster_13: 12.28, file_cluster_7: 12.627
- **Magnitude:** 721.06 | **LOC:** 455 | **CtrlFlow:** 72.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (32.1883%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `commitOutputState` (Impact: 328.6 | O(N^6) | DB: 6)
  * `validateConfigCoordinates` (Impact: 74.2 | O(N^5) | DB: 1)
  * `handlePowerManagerSetMode` (Impact: 45.2 | O(N^3))
  * `handleManagerApply` (Impact: 40.7 | O(N^4) | DB: 1)
  * `init` (Impact: 37.6 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 119`, `structural_boundaries: 45`, `args: 12`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 52`
* *Architecture:* `api: 7`, `import: 13`
* *Defense:* `safety: 39`, `doc: 4`, `immutability_locks: 40`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.974
  * `Choke Point (Betweenness):` 0.000307 | `Ripple Effect (Closeness):` 0.019608
  * `Imports (Out-Degree: 7):` util.zig, XwaylandOverrideRedirect.zig, Window.zig, DragIcon.zig, LockSurface.zig, Output.zig, std, build_options...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `river/Output.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.178 IQR)
- **Top Global Matches:** file_cluster_8: 11.178, file_cluster_13: 11.352, file_cluster_7: 11.443
- **Magnitude:** 686.94 | **LOC:** 549 | **CtrlFlow:** 75.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (8.7931%), Tech Debt (12.7474%)
**Top Internal Functions/Classes:**
  * `manageStart` (Impact: 198.2 | O(2^N) | DB: 1)
  * `renderAndCommit` (Impact: 138.2 | O(N^5) | DB: 1)
  * `create` (Impact: 93.3 | O(2^N) | DB: 1)
  * `fromHeadState` (Impact: 43.2 | O(N^6))
  * `handleRequest` (Impact: 41.3 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 28`, `args: 16`, `func_start: 16`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 22`, `dead_code: 2`, `planned_debt: 3`
* *Architecture:* `io: 1`, `api: 11`, `import: 9`
* *Defense:* `safety: 29`, `doc: 28`, `test: 1`, `sync_locks: 3`, `immutability_locks: 52`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 36.252
  * `Choke Point (Betweenness):` 0.023499 | `Ripple Effect (Closeness):` 0.338402
  * `Imports (Out-Degree: 5):` util.zig, Window.zig, LockSurface.zig, LayerShellOutput.zig, std, wlroots, wayland, SceneNodeData.zig
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `river/InputDevice.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.241 IQR)
- **Top Global Matches:** file_cluster_8: 11.241, file_cluster_13: 11.263, file_cluster_16: 11.53
- **Magnitude:** 533.84 | **LOC:** 296 | **CtrlFlow:** 76.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (16.9867%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `handleRequest` (Impact: 199.9 | O(N^6) | DB: 1)
  * `init` (Impact: 198.9 | O(2^N) | DB: 3)
  * `deinit` (Impact: 44.6 | O(2^N) | DB: 2)
  * `createObject` (Impact: 19.2 | O(N^2))
  * `activeMapping` (Impact: 15.5 | O(N^2) | DB: 1)
    * *Intent:* /// Retuns the curretly active mapping for the device, or an empty box if /// the movement of the de...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 19`, `args: 9`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 17`
* *Architecture:* `api: 6`, `import: 12`
* *Defense:* `safety: 20`, `doc: 3`, `immutability_locks: 26`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 25.654
  * `Choke Point (Betweenness):` 0.052422 | `Ripple Effect (Closeness):` 0.275735
  * `Imports (Out-Degree: 7):` util.zig, Keyboard.zig, XkbKeyboard.zig, Tablet.zig, std, c.zig, Seat.zig, LibinputDevice.zig...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `river/KeyboardGroup.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.049 IQR)
- **Top Global Matches:** file_cluster_8: 11.049, file_cluster_13: 11.274, file_cluster_7: 11.372
- **Magnitude:** 493.82 | **LOC:** 442 | **CtrlFlow:** 77.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (13.0551%), Tech Debt (19.7981%)
**Top Internal Functions/Classes:**
  * `handleKey` (Impact: 176.5 | O(N^5) | DB: 1)
  * `processKey` (Impact: 43.2 | O(N^5) | DB: 2)
  * `match` (Impact: 40.4 | O(N^2))
  * `handleBuiltinBinding` (Impact: 35.3 | O(N^4))
    * *Intent:* /// Handle any builtin, hardcoded compositor keybindings such as VT switching. /// Returns true if t...
  * `ledUpdate` (Impact: 31.7 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 98`, `structural_boundaries: 28`, `args: 14`, `func_start: 14`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 18`, `planned_debt: 3`, `fragile_debt: 1`
* *Architecture:* `api: 12`, `import: 10`
* *Defense:* `safety: 25`, `doc: 18`, `test: 2`, `immutability_locks: 44`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 12.888
  * `Choke Point (Betweenness):` 0.000256 | `Ripple Effect (Closeness):` 0.250247
  * `Imports (Out-Degree: 5):` XkbBinding.zig, util.zig, xkbcommon, Keyboard.zig, InputDevice.zig, std, Seat.zig, wlroots...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `river/XdgToplevel.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.127 IQR)
- **Top Global Matches:** file_cluster_8: 10.127, file_cluster_7: 10.557, file_cluster_13: 10.568
- **Magnitude:** 450.54 | **LOC:** 475 | **CtrlFlow:** 72.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (12.0209%), Tech Debt (12.4862%)
**Top Internal Functions/Classes:**
  * `configure` (Impact: 203.8 | O(2^N))
    * *Intent:* /// Send a configure event, return true if the configure should be tracked /// and current surfaces ...
  * `handleCommit` (Impact: 60.6 | O(N^5))
  * `needsConfigure` (Impact: 58.1 | O(N^2))
  * `handleDestroy` (Impact: 22.9 | O(N^3))
  * `handleRequestFullscreen` (Impact: 18.0 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 31`, `args: 19`, `func_start: 19`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 3`, `dead_code: 1`, `planned_debt: 2`
* *Architecture:* `api: 4`, `import: 10`
* *Defense:* `safety: 16`, `doc: 12`, `immutability_locks: 45`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 12.668
  * `Choke Point (Betweenness):` 0.01926 | `Ripple Effect (Closeness):` 0.238235
  * `Imports (Out-Degree: 6):` util.zig, XdgDecoration.zig, Window.zig, XdgPopup.zig, Output.zig, std, Seat.zig, wlroots...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `river/Keyboard.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.42%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.662 IQR)
- **Top Global Matches:** file_cluster_8: 11.662, file_cluster_13: 11.727, file_cluster_7: 12.024
- **Magnitude:** 415.54 | **LOC:** 251 | **CtrlFlow:** 78.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (14.1217%), Tech Debt (27.5483%)
**Top Internal Functions/Classes:**
  * `create` (Impact: 226.3 | O(2^N) | DB: 1)
  * `setGroup` (Impact: 35.7 | O(N^4) | DB: 1)
  * `processKey` (Impact: 35.2 | O(2^N))
  * `setKeymap` (Impact: 21.4 | O(2^N))
  * `maybeDestroy` (Impact: 13.5 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 13`, `args: 15`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 12`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `api: 12`, `import: 9`
* *Defense:* `safety: 25`, `doc: 6`, `immutability_locks: 23`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 22.337
  * `Choke Point (Betweenness):` 0.008816 | `Ripple Effect (Closeness):` 0.268283
  * `Imports (Out-Degree: 4):` util.zig, xkbcommon, InputDevice.zig, std, KeyboardGroup.zig, Seat.zig, wlroots, wayland
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `river/main.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.127 IQR)
- **Top Global Matches:** file_cluster_8: 12.127, file_cluster_13: 12.137, file_cluster_0: 12.481
- **Magnitude:** 359.08 | **LOC:** 295 | **CtrlFlow:** 77.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (36.0481%), Tech Debt (22.3537%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 156.3 | O(N^5) | DB: 4)
  * `detectClassic` (Impact: 45.3 | O(N^3))
  * `grepRiverctl` (Impact: 44.9 | O(N^3) | DB: 6)
  * `defaultInitPath` (Impact: 41.2 | O(N^4))
  * `logFn` (Impact: 27.7 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 98`, `structural_boundaries: 28`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 27`, `orphaned_logic: 2`
* *Architecture:* `io: 5`, `api: 5`, `import: 9`
* *Defense:* `safety: 45`, `doc: 2`, `sync_locks: 1`, `immutability_locks: 44`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.704
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` util.zig, process.zig, Server.zig, flags, std, build_options, c.zig, builtin...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `river/InputManager.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.42%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.96 IQR)
- **Top Global Matches:** file_cluster_8: 11.96, file_cluster_13: 11.983, file_cluster_7: 12.406
- **Magnitude:** 322.92 | **LOC:** 288 | **CtrlFlow:** 80.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (15.2369%), Tech Debt (17.2732%)
**Top Internal Functions/Classes:**
  * `init` (Impact: 98.8 | O(2^N) | DB: 1)
  * `handleRequest` (Impact: 96.1 | O(N^6) | DB: 2)
  * `bind` (Impact: 28.8 | O(N^4) | DB: 1)
  * `processEvents` (Impact: 10.8 | O(2^N) | DB: 1)
  * `handleNewVirtualPointer` (Impact: 9.8 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 10`, `args: 16`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 18`, `planned_debt: 2`
* *Architecture:* `api: 5`, `import: 13`
* *Defense:* `safety: 27`, `doc: 2`, `immutability_locks: 28`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.411
  * `Choke Point (Betweenness):` 0.004748 | `Ripple Effect (Closeness):` 0.248162
  * `Imports (Out-Degree: 7):` util.zig, Keyboard.zig, InputDevice.zig, PointerConstraint.zig, std, build_options, Seat.zig, wlroots...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `river/LayerShell.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.836 IQR)
- **Top Global Matches:** file_cluster_13: 11.836, file_cluster_8: 12.108, file_cluster_0: 12.316
- **Magnitude:** 272.14 | **LOC:** 194 | **CtrlFlow:** 75.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (24.2292%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `checkExclusiveFocus` (Impact: 69.1 | O(N^5) | DB: 2)
  * `handleRequest` (Impact: 68.7 | O(N^5))
  * `handleNewSurface` (Impact: 63.0 | O(N^4) | DB: 1)
  * `supported` (Impact: 18.6 | O(N^2) | DB: 1)
  * `init` (Impact: 16.0 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 15`, `args: 8`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 15`, `dead_code: 1`
* *Architecture:* `api: 4`, `import: 12`
* *Defense:* `safety: 18`, `doc: 1`, `immutability_locks: 30`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.974
  * `Choke Point (Betweenness):` 0.000732 | `Ripple Effect (Closeness):` 0.019608
  * `Imports (Out-Degree: 8):` util.zig, LayerShellSeat.zig, Output.zig, slotmap, LayerShellOutput.zig, std, LayerSurface.zig, Seat.zig...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `river/InputRelay.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.42%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.263 IQR)
- **Top Global Matches:** file_cluster_8: 11.263, file_cluster_13: 11.394, file_cluster_7: 11.587
- **Magnitude:** 237.04 | **LOC:** 234 | **CtrlFlow:** 81.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (12.0648%), Tech Debt (17.3049%)
**Top Internal Functions/Classes:**
  * `focus` (Impact: 105.5 | O(2^N) | DB: 2)
  * `sendInputMethodState` (Impact: 32.0 | O(N^4) | DB: 1)
  * `handleInputMethodCommit` (Impact: 29.2 | O(N^3))
  * `newInputMethod` (Impact: 11.5 | O(N^2))
  * `disableTextInput` (Impact: 11.0 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 8`, `args: 10`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 13`, `planned_debt: 1`
* *Architecture:* `api: 7`, `import: 7`
* *Defense:* `safety: 15`, `doc: 9`, `immutability_locks: 25`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 17.035
  * `Choke Point (Betweenness):` 0.014368 | `Ripple Effect (Closeness):` 0.268283
  * `Imports (Out-Degree: 4):` util.zig, InputPopup.zig, std, Seat.zig, wlroots, wayland, TextInput.zig
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `river/TabletTool.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.27%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.996 IQR)
- **Top Global Matches:** file_cluster_8: 9.996, file_cluster_13: 10.438, file_cluster_7: 10.446
- **Magnitude:** 237.04 | **LOC:** 271 | **CtrlFlow:** 79.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (13.9209%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `axis` (Impact: 110.8 | O(N^5))
  * `tip` (Impact: 29.4 | O(N^6))
  * `passthrough` (Impact: 25.2 | O(N^3))
    * *Intent:* /// Send a motion event for the surface under the tablet tool's cursor if any. /// Send a proximity_...
  * `allowSetCursor` (Impact: 18.6 | O(N^2))
  * `proximity` (Impact: 8.9 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 12`, `args: 13`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 3`
* *Architecture:* `api: 8`, `import: 6`
* *Defense:* `safety: 11`, `doc: 7`, `test: 1`, `immutability_locks: 17`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.684
  * `Choke Point (Betweenness):` 0.000219 | `Ripple Effect (Closeness):` 0.189678
  * `Imports (Out-Degree: 2):` util.zig, Tablet.zig, std, wlroots, wayland
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `river/XkbKeyboard.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.24 IQR)
- **Top Global Matches:** file_cluster_8: 11.24, file_cluster_13: 11.249, file_cluster_7: 11.672
- **Magnitude:** 226.44 | **LOC:** 208 | **CtrlFlow:** 68.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (19.8815%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `sendState` (Impact: 61.3 | O(N^4) | DB: 1)
  * `createObject` (Impact: 53.9 | O(N^4) | DB: 1)
  * `handleRequest` (Impact: 53.2 | O(N^4) | DB: 6)
  * `init` (Impact: 11.0 | O(2^N) | DB: 2)
  * `deinit` (Impact: 7.5 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 14`, `args: 7`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 23`
* *Architecture:* `api: 6`, `import: 10`
* *Defense:* `safety: 13`, `doc: 2`, `immutability_locks: 29`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.359
  * `Choke Point (Betweenness):` 0.01745 | `Ripple Effect (Closeness):` 0.201212
  * `Imports (Out-Degree: 4):` XkbKeymap.zig, util.zig, xkbcommon, InputDevice.zig, Keyboard.zig, std, wlroots, wayland
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `river/Scene.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.14%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.24 IQR)
- **Top Global Matches:** file_cluster_13: 12.24, file_cluster_8: 12.248, file_cluster_7: 12.448
- **Magnitude:** 219.86 | **LOC:** 202 | **CtrlFlow:** 75.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (10.2157%), Tech Debt (96.0388%)
**Top Internal Functions/Classes:**
  * `init` (Impact: 64.1 | O(N^3) | DB: 1)
  * `at` (Impact: 56.4 | O(N^4) | DB: 2)
    * *Intent:* /// Return information about what is currently rendered in the interactive_tree /// tree at the give...
  * `saveSurfaceTreeIter` (Impact: 15.4 | O(N^3))
  * `init` (Impact: 14.4 | O(N^3))
  * `dropSaved` (Impact: 14.4 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 14`, `args: 9`, `func_start: 9`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 12`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 12`, `import: 6`
* *Defense:* `safety: 25`, `doc: 20`, `immutability_locks: 23`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 19.02
  * `Choke Point (Betweenness):` 0.008288 | `Ripple Effect (Closeness):` 0.252368
  * `Imports (Out-Degree: 1):` std, build_options, wlroots, wayland, SceneNodeData.zig
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `river/XwaylandWindow.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.42%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.771 IQR)
- **Top Global Matches:** file_cluster_8: 9.771, file_cluster_7: 10.296, file_cluster_13: 10.474
- **Magnitude:** 219.52 | **LOC:** 347 | **CtrlFlow:** 88.2% | **Authorship Centralization:** 85.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (7.7075%), Tech Debt (13.0264%)
**Top Internal Functions/Classes:**
  * `configure` (Impact: 85.6 | O(2^N))
    * *Intent:* /// Always returns false as we do not care about frame perfection for Xwayland windows.
  * `handleSetSizeHints` (Impact: 21.7 | O(N^3))
  * `handleMap` (Impact: 19.6 | O(N^2))
  * `handleSetOverrideRedirect` (Impact: 18.4 | O(N^3))
  * `handleRequestConfigure` (Impact: 10.0 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 6`, `args: 18`, `func_start: 18`
* *Risk/State:* `safety_bypasses: 1`, `planned_debt: 1`
* *Architecture:* `api: 3`, `import: 8`
* *Defense:* `safety: 12`, `doc: 7`, `immutability_locks: 41`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.807
  * `Choke Point (Betweenness):` 0.000348 | `Ripple Effect (Closeness):` 0.236345
  * `Imports (Out-Degree: 4):` util.zig, XwaylandOverrideRedirect.zig, Window.zig, Output.zig, std, wlroots, wayland
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `common/slotmap.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.22%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.284 IQR)
- **Top Global Matches:** file_cluster_8: 13.284, file_cluster_13: 13.56, file_cluster_0: 13.574
- **Magnitude:** 207.42 | **LOC:** 272 | **CtrlFlow:** 83.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (36.4854%), Tech Debt (14.9005%)
**Top Internal Functions/Classes:**
  * `SlotMap` (Impact: 152.7 | O(N^6) | DB: 1)
  * `expectIterate` (Impact: 16.1 | O(N^2) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 106`, `structural_boundaries: 21`, `args: 9`, `func_start: 9`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 24`, `planned_debt: 1`
* *Architecture:* `api: 10`, `import: 1`
* *Defense:* `safety: 91`, `doc: 8`, `test: 7`, `immutability_locks: 30`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 13.66
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.248941
  * `Imports (Out-Degree: 0):` std
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `river/LockManager.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.33%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.591 IQR)
- **Top Global Matches:** file_cluster_13: 11.591, file_cluster_8: 11.634, file_cluster_7: 11.853
- **Magnitude:** 202.6 | **LOC:** 246 | **CtrlFlow:** 74.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (14.0299%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `maybeLock` (Impact: 58.9 | O(N^5) | DB: 3)
  * `handleLock` (Impact: 36.8 | O(N^4) | DB: 1)
  * `lockSurfaceFromOutput` (Impact: 24.9 | O(N^3) | DB: 1)
  * `sendLocked` (Impact: 10.7 | O(2^N))
  * `handleDestroy` (Impact: 8.5 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 13`, `args: 10`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 21`
* *Architecture:* `api: 5`, `import: 8`
* *Defense:* `safety: 15`, `doc: 12`, `sync_locks: 40`, `immutability_locks: 20`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.974
  * `Choke Point (Betweenness):` 8.8e-05 | `Ripple Effect (Closeness):` 0.019608
  * `Imports (Out-Degree: 3):` util.zig, LockSurface.zig, Output.zig, std, build_options, wlroots, wayland
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `river/WmNode.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.14%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.475 IQR)
- **Top Global Matches:** file_cluster_8: 10.475, file_cluster_13: 10.618, file_cluster_7: 10.983
- **Magnitude:** 193.38 | **LOC:** 137 | **CtrlFlow:** 70.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (22.496%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `handleRequest` (Impact: 143.7 | O(N^5))
  * `createObject` (Impact: 10.6 | O(N^2))
  * `get` (Impact: 8.1 | O(N^2))
  * `init` (Impact: 5.5 | O(2^N) | DB: 1)
  * `makeInert` (Impact: 5.5 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 11`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 1`
* *Architecture:* `api: 8`, `import: 7`
* *Defense:* `safety: 10`, `doc: 1`, `immutability_locks: 16`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 14.174
  * `Choke Point (Betweenness):` 0.002275 | `Ripple Effect (Closeness):` 0.236345
  * `Imports (Out-Degree: 3):` util.zig, ShellSurface.zig, Window.zig, std, wayland
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `river/Decoration.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.14%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.848 IQR)
- **Top Global Matches:** file_cluster_8: 10.848, file_cluster_13: 10.907, file_cluster_7: 11.346
- **Magnitude:** 180.44 | **LOC:** 166 | **CtrlFlow:** 73.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (13.8726%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `create` (Impact: 73.2 | O(2^N) | DB: 1)
  * `handleRequest` (Impact: 27.8 | O(N^3))
  * `renderFinish` (Impact: 27.3 | O(N^5) | DB: 1)
  * `clientCommit` (Impact: 16.0 | O(N^2))
  * `makeInert` (Impact: 5.5 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 9`, `args: 9`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 6`
* *Architecture:* `api: 6`, `import: 8`
* *Defense:* `safety: 12`, `doc: 1`, `immutability_locks: 20`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.096
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.234484
  * `Imports (Out-Degree: 2):` util.zig, Scene.zig, std, build_options, wlroots, wayland
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `river/Scene.zig` (ZIG) | Magnitude: 219.86 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 140, branch: 44, pointers: 30, safety: 25
- `river/XkbBindings.zig` (ZIG) | Magnitude: 92.7 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 52, encapsulation: 19, globals: 16, immutability_locks: 16
- `river/c.zig` (ZIG) | Magnitude: 16.2 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: import: 6, indent_spaces: 6, api: 1, globals: 1
- `river/LockManager.zig` (ZIG) | Magnitude: 202.6 | Delta: **0.043 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 143, sync_locks: 40, branch: 37, encapsulation: 32
- `river/LayerSurface.zig` (ZIG) | Magnitude: 103.14 | Delta: **0.051 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 101, encapsulation: 35, pointers: 32, globals: 31

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `river/XkbKeyboard.zig` (ZIG) | Magnitude: 226.44 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 154, encapsulation: 40, globals: 37, bitwise_ops: 31
- `river/main.zig` (ZIG) | Magnitude: 359.08 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 210, branch: 98, encapsulation: 46, safety: 45
- `river/InputDevice.zig` (ZIG) | Magnitude: 533.84 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 215, branch: 61, encapsulation: 34, globals: 30
- `river/InputManager.zig` (ZIG) | Magnitude: 322.92 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 165, pointers: 65, encapsulation: 44, branch: 40
- `river/OutputManager.zig` (ZIG) | Magnitude: 721.06 | Delta: **0.043 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 327, branch: 119, encapsulation: 63, globals: 55

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `river/Seat.zig` -> **Isaac Freund** (87.5% isolated ownership) | Magnitude: 1533.32
- `river/LibinputDevice.zig` -> **Isaac Freund** (100.0% isolated ownership) | Magnitude: 1221.96
- `river/Server.zig` -> **Isaac Freund** (83.3% isolated ownership) | Magnitude: 897.08
- `river/Cursor.zig` -> **Isaac Freund** (100.0% isolated ownership) | Magnitude: 783.28
- `river/OutputManager.zig` -> **Isaac Freund** (100.0% isolated ownership) | Magnitude: 721.06

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `river/Seat.zig` -> **Severity: 3.922** (Bridge: 0.2412 * Flux: 16.2606%)
- `river/LockSurface.zig` -> **Severity: 1.385** (Bridge: 0.0256 * Flux: 54.1912%)
- `river/Window.zig` -> **Severity: 1.113** (Bridge: 0.0987 * Flux: 11.2732%)
- `river/InputDevice.zig` -> **Severity: 0.956** (Bridge: 0.0524 * Flux: 18.2314%)
- `river/XkbKeyboard.zig` -> **Severity: 0.73** (Bridge: 0.0175 * Flux: 41.8443%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `river/util.zig` -> **Severity: 41.148** (Embedded: 0.6497 * Error Risk: 63.3333%)
- `river/LockSurface.zig` -> **Severity: 22.33** (Embedded: 0.3135 * Error Risk: 71.2371%)
- `river/PointerConstraint.zig` -> **Severity: 20.02** (Embedded: 0.2502 * Error Risk: 80.0%)
- `river/SceneNodeData.zig` -> **Severity: 19.579** (Embedded: 0.3008 * Error Risk: 65.0877%)
- `river/LayerSurface.zig` -> **Severity: 16.438** (Embedded: 0.3008 * Error Risk: 54.6479%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `river/util.zig` -> **Severity: 14261.4** (Blast Radius: 142.614 * Doc Risk: 100.0%)
- `river/SceneNodeData.zig` -> **Severity: 6684.041** (Blast Radius: 66.88 * Doc Risk: 99.9408%)
- `river/Seat.zig` -> **Severity: 6018.8** (Blast Radius: 60.188 * Doc Risk: 100.0%)
- `river/Window.zig` -> **Severity: 3991.0** (Blast Radius: 39.91 * Doc Risk: 100.0%)
- `river/Output.zig` -> **Severity: 3625.2** (Blast Radius: 36.252 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
