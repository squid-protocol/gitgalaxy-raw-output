# ARCHITECTURAL_BRIEF: river
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_zig/river` |
| **Timestamp** | `2026-08-07T04:29:35.264798+00:00` |
| **Scan Duration** | `0.34s` |
| **Git Branch** | `main` |
| **Git Commit** | `79e09c3628a88b7b71fc178dccd1b5ab8e7681b0` |
| **Git Remote** | `https://github.com/ifreund/river.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 54 malicious artifacts.

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
| Modularity | 0.2947 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
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
| Cognitive Load Exposure | 5.0 | 67.1 | 16.5 | 13.9 | 5.0 |
| Error & Exception Exposure | 0.0 | 86.3 | 46.6 | 55.5 | 0.0 |
| Tech Debt Exposure | 0.0 | 96.0 | 9.9 | 0.0 | 0.0 |
| Testing Exposure | 0.2 | 80.0 | 41.5 | 80.0 | 80.0 |
| API Exposure | 0.0 | 9.5 | 1.4 | 0.9 | 0.0 |
| Concurrency Exposure | 0.0 | 19.7 | 0.3 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 12.1 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 7.7 | 0.7 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 83.7 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 1.8 | 0.3 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 19.7 | 0.0 | 0.0 |
| Documentation Exposure | 0.8 | 100.0 | 47.7 | 50.6 | 1.2 |
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

- `handleRequest` (@ `river/LibinputDevice.zig`) -> Impact: **307.2** | LOC: 330
- `handleRequest` (@ `river/Window.zig`) -> Impact: **151.5** | LOC: 167
- `Deque` (@ `common/deque.zig`) -> Impact: **146.5** | LOC: 250
  * *Intent:* /// A contiguous, growable, double-ended queue. /// /// Pushing/popping items from either end of the queue is O(1).
- `commitOutputState` (@ `river/OutputManager.zig`) -> Impact: **99.1** | LOC: 147
- `init` (@ `river/Server.zig`) -> Impact: **98.0** | LOC: 125
- `manageStart` (@ `river/Window.zig`) -> Impact: **75.0** | LOC: 149
  * *Intent:* /// Send dirty state as part of a manage sequence.
- `createObject` (@ `river/LibinputDevice.zig`) -> Impact: **67.1** | LOC: 130
- `manageStart` (@ `river/Seat.zig`) -> Impact: **62.8** | LOC: 147
- `processButton` (@ `river/Cursor.zig`) -> Impact: **57.2** | LOC: 104
- `main` (@ `river/main.zig`) -> Impact: **56.3** | LOC: 126

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `river` | 51 | 6380.76 | 18.1% | 11.65% |
| `common` | 3 | 604.54 | 30.67% | 17.29% |
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

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `399` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `river/wlroots_log_wrapper.c` (C) -> Cumulative Risk: **523.78**
- **Archetype:** `file_cluster_13` (Distance: 12.228 IQR)
- **Magnitude:** 27.96 | **LOC:** 46 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9556%), Documentation (98.5214%), Tech Debt (94.5687%)
- **Heaviest Functions:** `callback` (Impact: 9.3), `river_init_wlroots_log` (Impact: 2.1)

### 2. `river/LibinputDevice.zig` (ZIG) -> Cumulative Risk: **460.82**
- **Archetype:** `file_cluster_8` (Distance: 12.698 IQR)
- **Magnitude:** 511.46 | **LOC:** 550 | **CtrlFlow:** 69.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Verification (80.0%), Safety Score (78.7805%), State Flux (67.1342%)
- **Heaviest Functions:** `handleRequest` (Impact: 307.2), `createObject` (Impact: 67.1), `create` (Impact: 7.3)

### 3. `river/Scene.zig` (ZIG) -> Cumulative Risk: **458.75**
- **Archetype:** `file_cluster_13` (Distance: 12.24 IQR)
- **Magnitude:** 125.66 | **LOC:** 202 | **CtrlFlow:** 75.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (96.0388%), Documentation (87.0168%), Verification (80.0%)
- **Heaviest Functions:** `init` (Impact: 32.9), `at` (Impact: 23.4), `saveSurfaceTreeIter` (Impact: 8.1)

### 4. `river/OutputManager.zig` (ZIG) -> Cumulative Risk: **454.9**
- **Archetype:** `file_cluster_8` (Distance: 12.225 IQR)
- **Magnitude:** 300.26 | **LOC:** 455 | **CtrlFlow:** 72.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Verification (80.0%), State Flux (76.8341%), Safety Score (63.4374%)
- **Heaviest Functions:** `commitOutputState` (Impact: 99.1), `validateConfigCoordinates` (Impact: 25.7), `handlePowerManagerSetMode` (Impact: 16.8)

### 5. `river/IdleInhibitManager.zig` (ZIG) -> Cumulative Risk: **445.88**
- **Archetype:** `file_cluster_13` (Distance: 11.795 IQR)
- **Magnitude:** 38.5 | **LOC:** 62 | **CtrlFlow:** 75.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (90.7687%), Tech Debt (73.1059%), Safety Score (71.095%)
- **Heaviest Functions:** `checkActive` (Impact: 11.2), `handleNewIdleInhibitor` (Impact: 4.6), `init` (Impact: 3.9)

### 6. `river/WindowManager.zig` (ZIG) -> Cumulative Risk: **445.63**
- **Archetype:** `file_cluster_8` (Distance: 11.8 IQR)
- **Magnitude:** 289.22 | **LOC:** 563 | **CtrlFlow:** 74.1% | **Authorship Centralization:** 80.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Verification (80.0%), State Flux (74.4354%), Churn (58.84%)
- **Heaviest Functions:** `renderFinish` (Impact: 41.7), `handleRequest` (Impact: 20.6), `manageStart` (Impact: 19.7)

### 7. `river/Seat.zig` (ZIG) -> Cumulative Risk: **418.93**
- **Archetype:** `file_cluster_8` (Distance: 12.381 IQR)
- **Magnitude:** 507.12 | **LOC:** 1035 | **CtrlFlow:** 76.8% | **Authorship Centralization:** 87.5%
- **Primary Risk Drivers:** Spec Match (100.0%), Verification (80.0%), Churn (79.63%), Documentation (64.6088%)
- **Heaviest Functions:** `manageStart` (Impact: 62.8), `handleRequest` (Impact: 50.0), `matchXkbBinding` (Impact: 41.7)

### 8. `river/main.zig` (ZIG) -> Cumulative Risk: **413.03**
- **Archetype:** `file_cluster_8` (Distance: 12.107 IQR)
- **Magnitude:** 177.68 | **LOC:** 295 | **CtrlFlow:** 77.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Verification (80.0%), Documentation (62.8743%), Churn (47.4%)
- **Heaviest Functions:** `main` (Impact: 56.3), `detectClassic` (Impact: 23.3), `grepRiverctl` (Impact: 22.9)

### 9. `river/Keyboard.zig` (ZIG) -> Cumulative Risk: **409.24**
- **Archetype:** `file_cluster_8` (Distance: 11.656 IQR)
- **Magnitude:** 138.74 | **LOC:** 251 | **CtrlFlow:** 78.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (87.8044%), Verification (80.0%), Churn (42.83%)
- **Heaviest Functions:** `create` (Impact: 34.3), `setGroup` (Impact: 14.9), `processKey` (Impact: 9.3)

### 10. `river/Window.zig` (ZIG) -> Cumulative Risk: **407.36**
- **Archetype:** `file_cluster_8` (Distance: 12.076 IQR)
- **Magnitude:** 583.9 | **LOC:** 1212 | **CtrlFlow:** 74.6% | **Authorship Centralization:** 77.8%
- **Primary Risk Drivers:** Spec Match (100.0%), Churn (89.77%), Verification (80.0%), Documentation (50.7688%)
- **Heaviest Functions:** `handleRequest` (Impact: 151.5), `manageStart` (Impact: 75.0), `manageFinish` (Impact: 45.9)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `river/Window.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.076 IQR)
- **Top Global Matches:** file_cluster_8: 12.076, file_cluster_13: 12.307, file_cluster_7: 12.353
- **Magnitude:** 583.9 | **LOC:** 1212 | **CtrlFlow:** 74.6% | **Authorship Centralization:** 77.8%
- **Risk Profile:** Cognitive Load (11.0154%), Tech Debt (8.7967%)
**Top Internal Functions/Classes:**
  * `handleRequest` (Impact: 151.5)
  * `manageStart` (Impact: 75.0)
    * *Intent:* /// Send dirty state as part of a manage sequence.
  * `manageFinish` (Impact: 45.9)
    * *Intent:* /// Applies window management state from the window manager and sends a configure /// to the window ...
  * `renderStart` (Impact: 26.1)
  * `applySurfaceClip` (Impact: 19.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 238`, `structural_boundaries: 81`, `args: 29`, `func_start: 29`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 40`, `dead_code: 3`, `planned_debt: 1`
* *Architecture:* `io: 1`, `api: 40`, `import: 16`
* *Defense:* `safety: 97`, `doc: 50`, `immutability_locks: 78`, `cleanup: 17`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 39.91
  * `Choke Point (Betweenness):` 0.098722 | `Ripple Effect (Closeness):` 0.350346
  * `Imports (Out-Degree: 10):` build_options, WmNode.zig, std, SceneNodeData.zig, Seat.zig, wayland, Decoration.zig, wlroots...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `river/LibinputDevice.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.27%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.698 IQR)
- **Top Global Matches:** file_cluster_8: 12.698, file_cluster_13: 12.862, file_cluster_0: 13.073
- **Magnitude:** 511.46 | **LOC:** 550 | **CtrlFlow:** 69.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (67.1011%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `handleRequest` (Impact: 307.2)
  * `createObject` (Impact: 67.1)
  * `create` (Impact: 7.3)
  * `send` (Impact: 7.3)
  * `handleRequestInert` (Impact: 4.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 172`, `structural_boundaries: 75`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 52`, `state_mutation: 91`
* *Architecture:* `api: 6`, `import: 9`
* *Defense:* `safety: 70`, `doc: 1`, `immutability_locks: 107`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 10.513
  * `Choke Point (Betweenness):` 0.009877 | `Ripple Effect (Closeness):` 0.201212
  * `Imports (Out-Degree: 4):` std, LibinputAccelConfig.zig, c.zig, InputDevice.zig, wayland, wlroots, util.zig
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `river/Seat.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.381 IQR)
- **Top Global Matches:** file_cluster_8: 12.381, file_cluster_13: 12.459, file_cluster_7: 12.739
- **Magnitude:** 507.12 | **LOC:** 1035 | **CtrlFlow:** 76.8% | **Authorship Centralization:** 87.5%
- **Risk Profile:** Cognitive Load (12.9143%), Tech Debt (9.5089%)
**Top Internal Functions/Classes:**
  * `manageStart` (Impact: 62.8)
  * `handleRequest` (Impact: 50.0)
  * `matchXkbBinding` (Impact: 41.7)
    * *Intent:* /// Handle any user-defined mapping for passed keycode, modifiers and keyboard state /// Returns tru...
  * `manageFinish` (Impact: 29.1)
  * `focus` (Impact: 24.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 175`, `structural_boundaries: 53`, `args: 29`, `func_start: 29`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 48`, `dead_code: 2`, `planned_debt: 2`
* *Architecture:* `api: 37`, `import: 27`
* *Defense:* `safety: 98`, `doc: 15`, `immutability_locks: 75`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 60.188
  * `Choke Point (Betweenness):` 0.241211 | `Ripple Effect (Closeness):` 0.381787
  * `Imports (Out-Degree: 21):` std, PointerConstraint.zig, InputRelay.zig, Keyboard.zig, LayerShellSeat.zig, PointerBinding.zig, XwaylandOverrideRedirect.zig, LockSurface.zig...
  * `Imported By (In-Degree: 21):` (Excluded from Brief to save tokens)

### `common/deque.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.709 IQR)
- **Top Global Matches:** file_cluster_8: 12.709, file_cluster_7: 12.836, file_cluster_13: 13.012
- **Magnitude:** 385.74 | **LOC:** 435 | **CtrlFlow:** 73.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (26.1719%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Deque` (Impact: 146.5)
    * *Intent:* /// A contiguous, growable, double-ended queue. /// /// Pushing/popping items from either end of the...
  * `fuzzAgainstArrayList` (Impact: 41.8)
  * `ensureTotalCapacityPrecise` (Impact: 25.8)
    * *Intent:* /// If the current capacity is less than `new_capacity`, this function will /// modify the deque so ...
  * `next` (Impact: 9.1)
  * `bufferIndex` (Impact: 9.1)
    * *Intent:* /// Returns the index in `buffer` where the element at the given /// index in the logical deque is s...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 131`, `structural_boundaries: 48`, `args: 24`, `func_start: 24`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 34`
* *Architecture:* `api: 23`, `concurrency: 1`, `import: 1`
* *Defense:* `safety: 62`, `doc: 68`, `test: 5`, `immutability_locks: 39`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 8.141
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.250949
  * `Imports (Out-Degree: 0):` std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `river/Cursor.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.42%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.774 IQR)
- **Top Global Matches:** file_cluster_8: 11.774, file_cluster_13: 12.095, file_cluster_7: 12.118
- **Magnitude:** 349.08 | **LOC:** 928 | **CtrlFlow:** 81.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (8.9464%), Tech Debt (9.811%)
**Top Internal Functions/Classes:**
  * `processButton` (Impact: 57.2)
  * `processMotionRelative` (Impact: 18.5)
  * `setTheme` (Impact: 17.6)
    * *Intent:* /// Set the cursor theme for the given seat, as well as the xwayland theme if /// this is the defaul...
  * `updateHovered` (Impact: 17.4)
  * `handleRequestSetCursor` (Impact: 14.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 121`, `structural_boundaries: 27`, `args: 41`, `func_start: 41`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 29`, `planned_debt: 2`
* *Architecture:* `io: 1`, `api: 17`, `import: 18`
* *Defense:* `safety: 60`, `doc: 26`, `immutability_locks: 87`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 10.854
  * `Choke Point (Betweenness):` 0.016974 | `Ripple Effect (Closeness):` 0.250247
  * `Imports (Out-Degree: 13):` build_options, PointerBinding.zig, std, XwaylandOverrideRedirect.zig, LockSurface.zig, PointerConstraint.zig, TabletTool.zig, InputDevice.zig...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `river/OutputManager.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.225 IQR)
- **Top Global Matches:** file_cluster_8: 12.225, file_cluster_13: 12.269, file_cluster_7: 12.615
- **Magnitude:** 300.26 | **LOC:** 455 | **CtrlFlow:** 72.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (32.1883%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `commitOutputState` (Impact: 99.1)
  * `validateConfigCoordinates` (Impact: 25.7)
  * `handlePowerManagerSetMode` (Impact: 16.8)
  * `autoLayout` (Impact: 15.3)
  * `handleManagerApply` (Impact: 14.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 119`, `structural_boundaries: 45`, `args: 12`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 52`
* *Architecture:* `api: 7`, `import: 13`
* *Defense:* `safety: 39`, `doc: 4`, `immutability_locks: 40`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.974
  * `Choke Point (Betweenness):` 0.000307 | `Ripple Effect (Closeness):` 0.019608
  * `Imports (Out-Degree: 7):` build_options, XwaylandOverrideRedirect.zig, std, LockSurface.zig, SceneNodeData.zig, wayland, wlroots, Output.zig...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `river/Server.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.196 IQR)
- **Top Global Matches:** file_cluster_8: 12.196, file_cluster_13: 12.302, file_cluster_7: 12.642
- **Magnitude:** 292.08 | **LOC:** 573 | **CtrlFlow:** 82.4% | **Authorship Centralization:** 83.3%
- **Risk Profile:** Cognitive Load (15.7137%), Tech Debt (12.6549%)
**Top Internal Functions/Classes:**
  * `init` (Impact: 98.0)
  * `allowlist` (Impact: 28.4)
    * *Intent:* /// Returns true if the global is allowlisted for security contexts
  * `globalFilter` (Impact: 23.2)
  * `start` (Impact: 16.2)
    * *Intent:* /// Create the socket, start the backend, and setup the environment
  * `handleRequestSetCursorShape` (Impact: 15.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 140`, `structural_boundaries: 30`, `args: 16`, `func_start: 16`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 12`, `planned_debt: 3`
* *Architecture:* `io: 1`, `api: 3`, `import: 25`
* *Defense:* `safety: 80`, `doc: 5`, `immutability_locks: 62`, `cleanup: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.674
  * `Choke Point (Betweenness):` 0.010316 | `Ripple Effect (Closeness):` 0.014706
  * `Imports (Out-Degree: 21):` std, XdgDecoration.zig, XdgToplevel.zig, XwaylandOverrideRedirect.zig, Output.zig, Seat.zig, TabletTool.zig, wayland...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `river/WindowManager.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.8 IQR)
- **Top Global Matches:** file_cluster_8: 11.8, file_cluster_13: 11.963, file_cluster_7: 12.142
- **Magnitude:** 289.22 | **LOC:** 563 | **CtrlFlow:** 74.1% | **Authorship Centralization:** 80.0%
- **Risk Profile:** Cognitive Load (15.6552%), Tech Debt (15.0793%)
**Top Internal Functions/Classes:**
  * `renderFinish` (Impact: 41.7)
    * *Intent:* /// Finish the update sequence and drop stashed buffers. This means that /// the next frame drawn wi...
  * `handleRequest` (Impact: 20.6)
  * `manageStart` (Impact: 19.7)
  * `manageFinish` (Impact: 13.9)
  * `handleTimeout` (Impact: 13.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 29`, `args: 24`, `func_start: 24`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 51`, `planned_debt: 2`, `fragile_debt: 1`
* *Architecture:* `api: 15`, `import: 13`
* *Defense:* `safety: 36`, `doc: 15`, `immutability_locks: 25`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.974
  * `Choke Point (Betweenness):` 0.000512 | `Ripple Effect (Closeness):` 0.019608
  * `Imports (Out-Degree: 8):` WmNode.zig, std, Seat.zig, wayland, Scene.zig, wlroots, Output.zig, ShellSurface.zig...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `river/Output.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.168 IQR)
- **Top Global Matches:** file_cluster_8: 11.168, file_cluster_13: 11.342, file_cluster_7: 11.434
- **Magnitude:** 237.24 | **LOC:** 549 | **CtrlFlow:** 75.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (8.7931%), Tech Debt (12.7474%)
**Top Internal Functions/Classes:**
  * `renderAndCommit` (Impact: 48.2)
  * `manageStart` (Impact: 31.9)
  * `create` (Impact: 25.8)
  * `handleRequest` (Impact: 14.5)
  * `fromHeadState` (Impact: 13.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 28`, `args: 16`, `func_start: 16`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 22`, `dead_code: 2`, `planned_debt: 3`
* *Architecture:* `io: 1`, `api: 11`, `import: 9`
* *Defense:* `safety: 29`, `doc: 28`, `test: 1`, `sync_locks: 3`, `immutability_locks: 52`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 36.252
  * `Choke Point (Betweenness):` 0.023499 | `Ripple Effect (Closeness):` 0.338402
  * `Imports (Out-Degree: 5):` std, LayerShellOutput.zig, LockSurface.zig, SceneNodeData.zig, wayland, wlroots, util.zig, Window.zig
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `river/KeyboardGroup.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.044 IQR)
- **Top Global Matches:** file_cluster_8: 11.044, file_cluster_13: 11.27, file_cluster_7: 11.367
- **Magnitude:** 224.92 | **LOC:** 442 | **CtrlFlow:** 77.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (13.0551%), Tech Debt (19.7981%)
**Top Internal Functions/Classes:**
  * `handleKey` (Impact: 51.7)
  * `match` (Impact: 27.4)
  * `processKey` (Impact: 15.5)
  * `handleBuiltinBinding` (Impact: 14.6)
    * *Intent:* /// Handle any builtin, hardcoded compositor keybindings such as VT switching. /// Returns true if t...
  * `unref` (Impact: 13.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 98`, `structural_boundaries: 28`, `args: 14`, `func_start: 14`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 18`, `planned_debt: 3`, `fragile_debt: 1`
* *Architecture:* `api: 12`, `import: 10`
* *Defense:* `safety: 25`, `doc: 18`, `test: 2`, `immutability_locks: 44`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 12.888
  * `Choke Point (Betweenness):` 0.000256 | `Ripple Effect (Closeness):` 0.250247
  * `Imports (Out-Degree: 5):` XkbBinding.zig, std, InputDevice.zig, Seat.zig, wayland, wlroots, Keyboard.zig, util.zig...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `river/XdgToplevel.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.11 IQR)
- **Top Global Matches:** file_cluster_8: 10.11, file_cluster_7: 10.541, file_cluster_13: 10.553
- **Magnitude:** 184.44 | **LOC:** 475 | **CtrlFlow:** 72.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (12.0209%), Tech Debt (12.4862%)
**Top Internal Functions/Classes:**
  * `configure` (Impact: 44.4)
    * *Intent:* /// Send a configure event, return true if the configure should be tracked /// and current surfaces ...
  * `needsConfigure` (Impact: 39.0)
  * `handleCommit` (Impact: 19.0)
  * `handleDestroy` (Impact: 12.5)
  * `handleRequestFullscreen` (Impact: 9.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 31`, `args: 19`, `func_start: 19`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 3`, `dead_code: 1`, `planned_debt: 2`
* *Architecture:* `api: 4`, `import: 10`
* *Defense:* `safety: 16`, `doc: 12`, `immutability_locks: 45`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 12.668
  * `Choke Point (Betweenness):` 0.01926 | `Ripple Effect (Closeness):` 0.238235
  * `Imports (Out-Degree: 6):` std, XdgDecoration.zig, XdgPopup.zig, Seat.zig, wayland, wlroots, Output.zig, util.zig...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `river/main.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.107 IQR)
- **Top Global Matches:** file_cluster_8: 12.107, file_cluster_13: 12.118, file_cluster_0: 12.463
- **Magnitude:** 177.68 | **LOC:** 295 | **CtrlFlow:** 77.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (36.0481%), Tech Debt (22.3537%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 56.3)
  * `detectClassic` (Impact: 23.3)
  * `grepRiverctl` (Impact: 22.9)
  * `defaultInitPath` (Impact: 17.2)
  * `logFn` (Impact: 16.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 98`, `structural_boundaries: 28`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 27`, `orphaned_logic: 2`
* *Architecture:* `io: 5`, `api: 5`, `import: 9`
* *Defense:* `safety: 45`, `doc: 2`, `sync_locks: 1`, `immutability_locks: 44`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.704
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` build_options, std, c.zig, builtin, wlroots, Server.zig, util.zig, flags...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `river/InputDevice.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.218 IQR)
- **Top Global Matches:** file_cluster_8: 11.218, file_cluster_13: 11.247, file_cluster_16: 11.511
- **Magnitude:** 171.24 | **LOC:** 296 | **CtrlFlow:** 74.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (15.7734%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `handleRequest` (Impact: 51.2)
  * `init` (Impact: 42.1)
  * `createObject` (Impact: 11.4)
  * `activeMapping` (Impact: 10.5)
    * *Intent:* /// Retuns the curretly active mapping for the device, or an empty box if /// the movement of the de...
  * `deinit` (Impact: 10.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 19`, `args: 9`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 17`
* *Architecture:* `api: 6`, `import: 12`
* *Defense:* `safety: 20`, `doc: 3`, `immutability_locks: 26`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 25.654
  * `Choke Point (Betweenness):` 0.052422 | `Ripple Effect (Closeness):` 0.275735
  * `Imports (Out-Degree: 7):` std, LibinputDevice.zig, c.zig, Seat.zig, wayland, XkbKeyboard.zig, wlroots, Keyboard.zig...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `river/Keyboard.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.42%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.656 IQR)
- **Top Global Matches:** file_cluster_8: 11.656, file_cluster_13: 11.721, file_cluster_7: 12.018
- **Magnitude:** 138.74 | **LOC:** 251 | **CtrlFlow:** 78.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (14.1217%), Tech Debt (27.5483%)
**Top Internal Functions/Classes:**
  * `create` (Impact: 34.3)
  * `setGroup` (Impact: 14.9)
  * `processKey` (Impact: 9.3)
  * `maybeDestroy` (Impact: 9.2)
  * `setKeymap` (Impact: 7.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 13`, `args: 15`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 12`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `api: 12`, `import: 9`
* *Defense:* `safety: 25`, `doc: 6`, `immutability_locks: 23`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 22.337
  * `Choke Point (Betweenness):` 0.008816 | `Ripple Effect (Closeness):` 0.268283
  * `Imports (Out-Degree: 4):` KeyboardGroup.zig, std, InputDevice.zig, Seat.zig, wayland, wlroots, util.zig, xkbcommon
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `river/InputManager.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.42%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.94 IQR)
- **Top Global Matches:** file_cluster_8: 11.94, file_cluster_13: 11.964, file_cluster_7: 12.386
- **Magnitude:** 138.62 | **LOC:** 288 | **CtrlFlow:** 80.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (15.2369%), Tech Debt (17.2732%)
**Top Internal Functions/Classes:**
  * `handleRequest` (Impact: 29.0)
  * `init` (Impact: 26.1)
  * `bind` (Impact: 12.0)
  * `handleNewVirtualPointer` (Impact: 5.1)
  * `handleNewVirtualKeyboard` (Impact: 5.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 10`, `args: 16`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 18`, `planned_debt: 2`
* *Architecture:* `api: 5`, `import: 13`
* *Defense:* `safety: 27`, `doc: 2`, `immutability_locks: 28`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.411
  * `Choke Point (Betweenness):` 0.004748 | `Ripple Effect (Closeness):` 0.248162
  * `Imports (Out-Degree: 7):` build_options, std, PointerConstraint.zig, InputDevice.zig, TextInput.zig, InputRelay.zig, Seat.zig, wayland...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `common/slotmap.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.22%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.274 IQR)
- **Top Global Matches:** file_cluster_8: 13.274, file_cluster_13: 13.55, file_cluster_0: 13.564
- **Magnitude:** 132.32 | **LOC:** 272 | **CtrlFlow:** 83.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (36.4854%), Tech Debt (14.9005%)
**Top Internal Functions/Classes:**
  * `SlotMap` (Impact: 47.7)
  * `next` (Impact: 9.2)
  * `getSlot` (Impact: 9.1)
  * `expectIterate` (Impact: 9.0)
  * `get` (Impact: 7.2)
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

### `river/Scene.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.14%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.24 IQR)
- **Top Global Matches:** file_cluster_13: 12.24, file_cluster_8: 12.248, file_cluster_7: 12.448
- **Magnitude:** 125.66 | **LOC:** 202 | **CtrlFlow:** 75.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (10.2157%), Tech Debt (96.0388%)
**Top Internal Functions/Classes:**
  * `init` (Impact: 32.9)
  * `at` (Impact: 23.4)
    * *Intent:* /// Return information about what is currently rendered in the interactive_tree /// tree at the give...
  * `saveSurfaceTreeIter` (Impact: 8.1)
  * `dropSaved` (Impact: 7.5)
  * `init` (Impact: 7.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 14`, `args: 9`, `func_start: 9`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 12`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 12`, `import: 6`
* *Defense:* `safety: 25`, `doc: 20`, `immutability_locks: 23`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 19.02
  * `Choke Point (Betweenness):` 0.008288 | `Ripple Effect (Closeness):` 0.252368
  * `Imports (Out-Degree: 1):` build_options, std, SceneNodeData.zig, wayland, wlroots
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `river/LayerShell.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.833 IQR)
- **Top Global Matches:** file_cluster_13: 11.833, file_cluster_8: 12.105, file_cluster_0: 12.313
- **Magnitude:** 121.74 | **LOC:** 194 | **CtrlFlow:** 75.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (24.2292%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `checkExclusiveFocus` (Impact: 24.1)
  * `handleRequest` (Impact: 24.0)
  * `handleNewSurface` (Impact: 22.1)
  * `supported` (Impact: 12.5)
  * `bind` (Impact: 7.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 15`, `args: 8`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 15`, `dead_code: 1`
* *Architecture:* `api: 4`, `import: 12`
* *Defense:* `safety: 18`, `doc: 1`, `immutability_locks: 30`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.974
  * `Choke Point (Betweenness):` 0.000732 | `Ripple Effect (Closeness):` 0.019608
  * `Imports (Out-Degree: 8):` std, LayerShellOutput.zig, SceneNodeData.zig, Seat.zig, wayland, wlroots, Output.zig, LayerSurface.zig...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `river/XkbKeyboard.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.24 IQR)
- **Top Global Matches:** file_cluster_8: 11.24, file_cluster_13: 11.249, file_cluster_7: 11.672
- **Magnitude:** 119.04 | **LOC:** 208 | **CtrlFlow:** 68.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (19.8815%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `sendState` (Impact: 25.6)
  * `handleRequest` (Impact: 23.0)
  * `createObject` (Impact: 22.7)
  * `handleRequestInert` (Impact: 4.8)
  * `init` (Impact: 4.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 14`, `args: 7`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 23`
* *Architecture:* `api: 6`, `import: 10`
* *Defense:* `safety: 13`, `doc: 2`, `immutability_locks: 29`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.359
  * `Choke Point (Betweenness):` 0.01745 | `Ripple Effect (Closeness):` 0.201212
  * `Imports (Out-Degree: 4):` std, InputDevice.zig, wayland, wlroots, Keyboard.zig, XkbKeymap.zig, util.zig, xkbcommon
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `river/XwaylandWindow.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.42%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.763 IQR)
- **Top Global Matches:** file_cluster_8: 9.763, file_cluster_7: 10.288, file_cluster_13: 10.467
- **Magnitude:** 116.32 | **LOC:** 347 | **CtrlFlow:** 88.2% | **Authorship Centralization:** 85.7%
- **Risk Profile:** Cognitive Load (7.7075%), Tech Debt (13.0264%)
**Top Internal Functions/Classes:**
  * `configure` (Impact: 23.3)
    * *Intent:* /// Always returns false as we do not care about frame perfection for Xwayland windows.
  * `handleMap` (Impact: 13.6)
  * `handleSetSizeHints` (Impact: 11.3)
  * `handleSetOverrideRedirect` (Impact: 9.7)
  * `handleSetDecorations` (Impact: 5.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 6`, `args: 18`, `func_start: 18`
* *Risk/State:* `safety_bypasses: 1`, `planned_debt: 1`
* *Architecture:* `api: 3`, `import: 8`
* *Defense:* `safety: 12`, `doc: 7`, `immutability_locks: 41`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.807
  * `Choke Point (Betweenness):` 0.000348 | `Ripple Effect (Closeness):` 0.236345
  * `Imports (Out-Degree: 4):` XwaylandOverrideRedirect.zig, std, wayland, wlroots, Output.zig, util.zig, Window.zig
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `river/TabletTool.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.27%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.988 IQR)
- **Top Global Matches:** file_cluster_8: 9.988, file_cluster_13: 10.43, file_cluster_7: 10.438
- **Magnitude:** 114.94 | **LOC:** 271 | **CtrlFlow:** 79.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.9209%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `axis` (Impact: 38.8)
  * `passthrough` (Impact: 13.1)
    * *Intent:* /// Send a motion event for the surface under the tablet tool's cursor if any. /// Send a proximity_...
  * `allowSetCursor` (Impact: 12.7)
  * `tip` (Impact: 9.4)
  * `maybeExitDown` (Impact: 5.6)
    * *Intent:* /// Exit down mode if the tool is up and there are no buttons pressed.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 12`, `args: 13`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 3`
* *Architecture:* `api: 8`, `import: 6`
* *Defense:* `safety: 11`, `doc: 7`, `test: 1`, `immutability_locks: 17`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.684
  * `Choke Point (Betweenness):` 0.000219 | `Ripple Effect (Closeness):` 0.189678
  * `Imports (Out-Degree: 2):` std, wayland, wlroots, util.zig, Tablet.zig
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `river/LockManager.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.33%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.583 IQR)
- **Top Global Matches:** file_cluster_13: 11.583, file_cluster_8: 11.625, file_cluster_7: 11.844
- **Magnitude:** 110.3 | **LOC:** 246 | **CtrlFlow:** 74.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (14.0299%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `maybeLock` (Impact: 20.8)
  * `handleLock` (Impact: 13.5)
  * `lockSurfaceFromOutput` (Impact: 12.8)
  * `handleDestroy` (Impact: 5.9)
  * `init` (Impact: 5.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 13`, `args: 10`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 21`
* *Architecture:* `api: 5`, `import: 8`
* *Defense:* `safety: 15`, `doc: 12`, `sync_locks: 40`, `immutability_locks: 20`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.974
  * `Choke Point (Betweenness):` 8.8e-05 | `Ripple Effect (Closeness):` 0.019608
  * `Imports (Out-Degree: 3):` build_options, std, LockSurface.zig, wayland, wlroots, Output.zig, util.zig
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `river/InputRelay.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.42%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.25 IQR)
- **Top Global Matches:** file_cluster_8: 11.25, file_cluster_13: 11.382, file_cluster_7: 11.575
- **Magnitude:** 100.94 | **LOC:** 234 | **CtrlFlow:** 81.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (12.0648%), Tech Debt (17.3049%)
**Top Internal Functions/Classes:**
  * `focus` (Impact: 18.9)
  * `handleInputMethodCommit` (Impact: 15.4)
  * `sendInputMethodState` (Impact: 13.8)
  * `newInputMethod` (Impact: 8.1)
  * `disableTextInput` (Impact: 5.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 8`, `args: 10`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 13`, `planned_debt: 1`
* *Architecture:* `api: 7`, `import: 7`
* *Defense:* `safety: 15`, `doc: 9`, `immutability_locks: 25`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 17.035
  * `Choke Point (Betweenness):` 0.014368 | `Ripple Effect (Closeness):` 0.268283
  * `Imports (Out-Degree: 4):` std, InputPopup.zig, TextInput.zig, Seat.zig, wayland, wlroots, util.zig
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `river/PointerConstraint.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.518 IQR)
- **Top Global Matches:** file_cluster_13: 11.518, file_cluster_8: 11.626, file_cluster_0: 11.901
- **Magnitude:** 96.66 | **LOC:** 223 | **CtrlFlow:** 66.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (19.3543%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `updateState` (Impact: 22.4)
    * *Intent:* /// Called when the cursor position or content in the scene graph changes
  * `maybeActivate` (Impact: 20.6)
  * `handleCommit` (Impact: 6.7)
    * *Intent:* // It is necessary to listen for the commit event rather than the set_region // event as the latter ...
  * `handleDestroy` (Impact: 5.3)
  * `warpToHintIfSet` (Impact: 4.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 16`, `args: 9`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 19`, `dead_code: 1`
* *Architecture:* `api: 6`, `import: 6`
* *Defense:* `safety: 6`, `doc: 3`, `immutability_locks: 34`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.872
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.250247
  * `Imports (Out-Degree: 2):` std, Seat.zig, wayland, wlroots, util.zig
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `river/Decoration.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.14%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.848 IQR)
- **Top Global Matches:** file_cluster_8: 10.848, file_cluster_13: 10.907, file_cluster_7: 11.346
- **Magnitude:** 91.74 | **LOC:** 166 | **CtrlFlow:** 73.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.8726%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `create` (Impact: 25.6)
  * `handleRequest` (Impact: 14.4)
  * `clientCommit` (Impact: 10.8)
  * `renderFinish` (Impact: 10.0)
  * `handleRequestInert` (Impact: 4.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 9`, `args: 9`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 6`
* *Architecture:* `api: 6`, `import: 8`
* *Defense:* `safety: 12`, `doc: 1`, `immutability_locks: 20`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.096
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.234484
  * `Imports (Out-Degree: 2):` build_options, std, wayland, Scene.zig, wlroots, util.zig
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `river/Scene.zig` (ZIG) | Magnitude: 125.66 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 140, branch: 44, pointers: 30, safety: 25
- `river/XkbBindings.zig` (ZIG) | Magnitude: 42.7 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 52, encapsulation: 19, globals: 16, immutability_locks: 16
- `river/c.zig` (ZIG) | Magnitude: 16.2 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: import: 6, indent_spaces: 6, api: 1, globals: 1
- `river/LockManager.zig` (ZIG) | Magnitude: 110.3 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 143, sync_locks: 40, branch: 37, encapsulation: 32
- `river/LayerSurface.zig` (ZIG) | Magnitude: 61.64 | Delta: **0.05 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 101, encapsulation: 35, pointers: 32, globals: 31

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `river/XkbKeyboard.zig` (ZIG) | Magnitude: 119.04 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 154, encapsulation: 40, globals: 37, bitwise_ops: 31
- `river/main.zig` (ZIG) | Magnitude: 177.68 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 210, branch: 98, encapsulation: 46, safety: 45
- `river/InputManager.zig` (ZIG) | Magnitude: 138.62 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 165, pointers: 65, encapsulation: 44, branch: 40
- `river/InputDevice.zig` (ZIG) | Magnitude: 171.24 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 215, branch: 55, encapsulation: 34, globals: 30
- `river/OutputManager.zig` (ZIG) | Magnitude: 300.26 | Delta: **0.044 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 327, branch: 119, encapsulation: 63, globals: 55

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `river/LibinputDevice.zig` -> **Isaac Freund** (100.0% isolated ownership) | Magnitude: 511.46
- `river/Seat.zig` -> **Isaac Freund** (87.5% isolated ownership) | Magnitude: 507.12
- `river/Cursor.zig` -> **Isaac Freund** (100.0% isolated ownership) | Magnitude: 349.08
- `river/OutputManager.zig` -> **Isaac Freund** (100.0% isolated ownership) | Magnitude: 300.26
- `river/Server.zig` -> **Isaac Freund** (83.3% isolated ownership) | Magnitude: 292.08

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

- `river/util.zig` -> **Severity: 52.577** (Embedded: 0.6497 * Error Risk: 80.925%)
- `river/LockSurface.zig` -> **Severity: 23.918** (Embedded: 0.3135 * Error Risk: 76.3006%)
- `river/SceneNodeData.zig` -> **Severity: 23.445** (Embedded: 0.3008 * Error Risk: 77.9428%)
- `river/PointerConstraint.zig` -> **Severity: 21.595** (Embedded: 0.2502 * Error Risk: 86.2961%)
- `river/LayerSurface.zig` -> **Severity: 19.505** (Embedded: 0.3008 * Error Risk: 64.8448%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `river/util.zig` -> **Severity: 14261.4** (Blast Radius: 142.614 * Doc Risk: 100.0%)
- `river/SceneNodeData.zig` -> **Severity: 6139.638** (Blast Radius: 66.88 * Doc Risk: 91.8008%)
- `river/Seat.zig` -> **Severity: 3888.674** (Blast Radius: 60.188 * Doc Risk: 64.6088%)
- `river/Window.zig` -> **Severity: 2026.183** (Blast Radius: 39.91 * Doc Risk: 50.7688%)
- `river/Keyboard.zig` -> **Severity: 1961.287** (Blast Radius: 22.337 * Doc Risk: 87.8044%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
