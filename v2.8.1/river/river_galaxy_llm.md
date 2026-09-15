# ARCHITECTURAL_BRIEF: river
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/ifreund/river.git` |
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
| Total Artifacts | 87 |
| Analyzed Artifacts (Scanned) | 69 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 18 |
| Total LOC | 10963 |
| Volatility Index | 0.087 |
| % Scanned of codebase = | 79.3% |
| Dominant Lang | ZIG |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3026 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3124 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 53.6% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.6714 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 3 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| ZIG | 53 | 10935 | 76.8% |
| XML | 11 | 0 | 15.9% |
| MARKDOWN | 4 | 0 | 5.8% |
| C | 1 | 28 | 1.4% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Hub-Coupled App` (z +0.76; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules 32%, State Mutators Files 23%, Data / Markup / Trivial 22%, Defensive Guards Files 17%, Many-Argument Workhorses Files 3%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 65 | 94.2% |

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

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 35.3 | 9.8 | 10.1 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 89.8 | 42.7 | 50.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 62.2 | 5.6 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 13.2 | 2.5 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 80.8 | 31.2 | 33.3 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 14.7 | 0.2 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 47.8 | 44.2 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 7.7 | 0.7 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 81.5 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 4.0 | 2.3 | 2.2 | 4.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 8.3 | 100.0 | 30.5 | 23.1 | 8.3 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 71.8 | 87.5 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1567 | 51 | 43 | `river/Cursor.zig` |
| cleanup | 338 | 50 | 10 | `river/Server.zig` |
| guards | 1141 | 53 | 45 | `river/Seat.zig` |
| danger | 440 | 49 | 18 | `river/LibinputDevice.zig` |
| concurrency | 39 | 4 | 0 | `river/LockManager.zig` |
| connectivity | 294 | 54 | 9 | `river/Window.zig` |
| io | 12 | 8 | 1 | `river/main.zig` |
| crypto | 0 | 0 | 0 | - |
| ipc | 8 | 8 | 1 | `river/Cursor.zig` |
| time | 0 | 0 | 0 | - |
| serialization | 0 | 0 | 0 | - |
| regex | 0 | 0 | 0 | - |
| events | 48 | 42 | 1 | `river/process.zig` |
| tests | 15 | 3 | 0 | `common/slotmap.zig` |
| docs | 345 | 34 | 15 | `common/deque.zig` |
| debt | 33 | 19 | 2 | `river/KeyboardGroup.zig` |
| mutation | 2085 | 54 | 72 | `river/Window.zig` |
| dead_code | 14 | 9 | 1 | `river/Window.zig` |
| credential | 0 | 0 | 0 | - |
| threat | 10 | 5 | 0 | `river/Window.zig` |
| ml_ai | 96 | 16 | 6 | `river/Cursor.zig` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.6667**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.1905**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `river/main.zig` (Hits: 5)
- `river/Cursor.zig` (Hits: 1)
- `river/Output.zig` (Hits: 1)

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

- `handleRequest` **(Many-Argument Workhorses)** (@ `river/LibinputDevice.zig`) -> Impact: **198.5** | LOC: 330
- `handleRequest` **(Many-Argument Workhorses)** (@ `river/Window.zig`) -> Impact: **76.3** | LOC: 167
- `createObject` **(Many-Argument Workhorses)** (@ `river/LibinputDevice.zig`) -> Impact: **63.7** | LOC: 130
- `manageStart` **(Defensive Guards)** (@ `river/Window.zig`) -> Impact: **55.5** | LOC: 149
  * *Intent:* /// Send dirty state as part of a manage sequence.
- `commitOutputState` **(Defensive Guards)** (@ `river/OutputManager.zig`) -> Impact: **51.2** | LOC: 147
- `manageStart` **(Defensive Guards)** (@ `river/Seat.zig`) -> Impact: **45.5** | LOC: 147
- `Deque` **(Compute Cores)** (@ `common/deque.zig`) -> Impact: **45.0** | LOC: 250
  * *Intent:* /// A contiguous, growable, double-ended queue. /// /// Pushing/popping items from either end of the queue is O(1).
- `handleKey` **(Many-Argument Workhorses)** (@ `river/KeyboardGroup.zig`) -> Impact: **44.9** | LOC: 101
- `processButton` **(Many-Argument Workhorses)** (@ `river/Cursor.zig`) -> Impact: **36.4** | LOC: 104
- `main` **(Defensive Guards)** (@ `river/main.zig`) -> Impact: **35.3** | LOC: 126

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `river` | 51 | 4970.2 | 11.87% | 6.58% |
| `common` | 3 | 331.36 | 10.09% | 9.08% |
| `protocol` | 5 | 52.6 | 0.0% | 0.0% |
| `logo` | 3 | 31.56 | 0.0% | 0.0% |
| `protocol/upstream` | 3 | 31.56 | 0.0% | 0.0% |
| `__monolith__` | 4 | 9.6 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `river/wlroots_log_wrapper.c` -> **62.2459%** Exposure
- `river/TextInput.zig` -> **42.9275%** Exposure
- `river/IdleInhibitManager.zig` -> **26.8941%** Exposure
- `river/Keyboard.zig` -> **20.5537%** Exposure
- `river/KeyboardGroup.zig` -> **17.9302%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `common/deque.zig` -> **100.0%** Exposure
- `river/Window.zig` -> **99.8502%** Exposure
- `river/Keyboard.zig` -> **99.6869%** Exposure
- `river/XdgToplevel.zig` -> **99.5891%** Exposure
- `river/Decoration.zig` -> **98.9199%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `river/main.zig` -> **2** Orphaned Functions | **0** Duplicates
- `river/wlroots_log_wrapper.c` -> **1** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `401` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `river/Output.zig` (ZIG) -> Cumulative Risk: **581.28**
- **Archetype:** `file_cluster_5` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.26)
- **Magnitude:** 223.02 | **LOC:** 549 | **CtrlFlow:** 13.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (98.7568%), Documentation (91.6667%), Verification (80.0%)
- **Heaviest Functions:** `renderAndCommit` (Compute Cores, Impact: 27.2), `manageStart` (Defensive Guards, Impact: 22.6), `create` (Defensive Guards, Impact: 13.1)

### 2. `river/XwaylandWindow.zig` (ZIG) -> Cumulative Risk: **568.95**
- **Archetype:** `file_cluster_5` (Distance: N/A IQR)
- **Composition Archetype:** `State Mutators Files` (z +0.47)
- **Magnitude:** 120.24 | **LOC:** 347 | **CtrlFlow:** 9.7% | **Authorship Centralization:** 93.3%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (96.9013%), Churn (92.55%), Documentation (85.7143%)
- **Heaviest Functions:** `configure` (Compute Cores, Impact: 15.2), `handleSetSizeHints` (State Mutators, Impact: 9.4), `handleSetOverrideRedirect` (Defensive Guards, Impact: 5.3)

### 3. `river/XdgToplevel.zig` (ZIG) -> Cumulative Risk: **564.14**
- **Archetype:** `file_cluster_14` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.58)
- **Magnitude:** 196.2 | **LOC:** 475 | **CtrlFlow:** 12.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.5891%), Safety Score (85.6433%), Verification (80.0%)
- **Heaviest Functions:** `configure` (Compute Cores, Impact: 24.4), `handleCommit` (Many-Argument Workhorses, Impact: 19.0), `needsConfigure` (Compute Cores, Impact: 16.5)

### 4. `river/Window.zig` (ZIG) -> Cumulative Risk: **543.79**
- **Archetype:** `file_cluster_14` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.76)
- **Magnitude:** 584.34 | **LOC:** 1212 | **CtrlFlow:** 14.1% | **Authorship Centralization:** 84.2%
- **Primary Risk Drivers:** Spec Match (100.0%), Churn (100.0%), State Flux (99.8502%), Api Exposure (74.5006%)
- **Heaviest Functions:** `handleRequest` (Many-Argument Workhorses, Impact: 76.3), `manageStart` (Defensive Guards, Impact: 55.5), `manageFinish` (Compute Cores, Impact: 24.1)

### 5. `river/Seat.zig` (ZIG) -> Cumulative Risk: **528.06**
- **Archetype:** `file_cluster_5` (Distance: N/A IQR)
- **Composition Archetype:** `Defensive Guards Files` (z +0.94)
- **Magnitude:** 424.4 | **LOC:** 1035 | **CtrlFlow:** 13.3% | **Authorship Centralization:** 92.9%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (91.6667%), State Flux (91.3962%), Churn (84.95%)
- **Heaviest Functions:** `manageStart` (Defensive Guards, Impact: 45.5), `handleRequest` (Defensive Guards, Impact: 23.1), `focus` (Defensive Guards, Impact: 23.1)

### 6. `river/KeyboardGroup.zig` (ZIG) -> Cumulative Risk: **523.75**
- **Archetype:** `file_cluster_14` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.33)
- **Magnitude:** 171.74 | **LOC:** 442 | **CtrlFlow:** 16.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (90.9091%), Verification (80.0%), Churn (76.86%)
- **Heaviest Functions:** `handleKey` (Many-Argument Workhorses, Impact: 44.9), `processKey` (Compute Cores, Impact: 15.5), `match` (Compute Cores, Impact: 13.6)

### 7. `river/Keyboard.zig` (ZIG) -> Cumulative Risk: **520.83**
- **Archetype:** `file_cluster_5` (Distance: N/A IQR)
- **Composition Archetype:** `Defensive Guards Files` (z +1.50)
- **Magnitude:** 134.62 | **LOC:** 251 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.6869%), Churn (69.41%)
- **Heaviest Functions:** `create` (Defensive Guards, Impact: 20.3), `processKey` (Defensive Guards, Impact: 9.3), `setGroup` (Defensive Guards, Impact: 8.1)

### 8. `river/XkbBinding.zig` (ZIG) -> Cumulative Risk: **501.84**
- **Archetype:** `file_cluster_5` (Distance: N/A IQR)
- **Composition Archetype:** `State Mutators Files` (z +1.40)
- **Magnitude:** 87.54 | **LOC:** 229 | **CtrlFlow:** 9.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Verification (80.0%), State Flux (78.9336%), Documentation (73.3333%)
- **Heaviest Functions:** `match` (Many-Argument Workhorses, Impact: 27.4), `handleRequest` (Many-Argument Workhorses, Impact: 11.1), `handleDestroy` (Defensive Guards, Impact: 7.6)

### 9. `river/InputDevice.zig` (ZIG) -> Cumulative Risk: **493.14**
- **Archetype:** `file_cluster_5` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.16)
- **Magnitude:** 133.42 | **LOC:** 296 | **CtrlFlow:** 15.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Verification (80.0%), Documentation (71.4286%), State Flux (63.8475%)
- **Heaviest Functions:** `init` (Many-Argument Workhorses, Impact: 34.3), `handleRequest` (Many-Argument Workhorses, Impact: 34.2), `deinit` (Compute Cores, Impact: 8.4)

### 10. `river/WindowManager.zig` (ZIG) -> Cumulative Risk: **490.99**
- **Archetype:** `file_cluster_14` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +1.38)
- **Magnitude:** 227.46 | **LOC:** 563 | **CtrlFlow:** 13.0% | **Authorship Centralization:** 90.9%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (97.0588%), State Flux (95.1952%), Churn (72.41%)
- **Heaviest Functions:** `renderFinish` (Compute Cores, Impact: 29.3), `manageStart` (Defensive Guards, Impact: 16.5), `manageFinish` (Defensive Guards, Impact: 11.7)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `river/Window.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 584.34 | **LOC:** 1212 | **CtrlFlow:** 14.1% | **Authorship Centralization:** 84.2%
- **Risk Profile:** Cognitive Load (18.2498%), Tech Debt (8.1275%)
**Top Internal Functions/Classes:**
  * `handleRequest` **(Many-Argument Workhorses)** (Impact: 76.3)
  * `manageStart` **(Defensive Guards)** (Impact: 55.5)
    * *Intent:* /// Send dirty state as part of a manage sequence.
  * `manageFinish` **(Compute Cores)** (Impact: 24.1)
    * *Intent:* /// Applies window management state from the window manager and sends a configure /// to the window ...
  * `renderStart` **(Compute Cores)** (Impact: 17.7)
  * `applySurfaceClip` **(Many-Argument Workhorses)** (Impact: 17.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 66 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 223
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 141`, `structural_boundaries: 86`, `args: 29`, `func_start: 29`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 26`, `high_risk_execution: 1`, `state_mutation: 91`, `dead_code: 3`, `planned_debt: 1`
* *Architecture:* `io: 1`, `api: 32`, `import: 16`
* *Defense:* `safety: 97`, `doc: 50`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 39.718
  * `Choke Point (Betweenness):` 0.098722 | `Ripple Effect (Closeness):` 0.350346
  * `Imports (Out-Degree: 10):` Decoration.zig, Output.zig, Scene.zig, SceneNodeData.zig, Seat.zig, WmNode.zig, XdgToplevel.zig, XwaylandWindow.zig...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `river/Seat.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 424.4 | **LOC:** 1035 | **CtrlFlow:** 13.3% | **Authorship Centralization:** 92.9%
- **Risk Profile:** Cognitive Load (14.8876%), Tech Debt (8.663%)
**Top Internal Functions/Classes:**
  * `manageStart` **(Defensive Guards)** (Impact: 45.5)
  * `handleRequest` **(Defensive Guards)** (Impact: 23.1)
  * `focus` **(Defensive Guards)** (Impact: 23.1)
  * `manageFinish` **(Defensive Guards)** (Impact: 22.9)
  * `matchXkbBinding` **(Many-Argument Workhorses)** (Impact: 22.7)
    * *Intent:* /// Handle any user-defined mapping for passed keycode, modifiers and keyboard state /// Returns tru...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 30 instances
* *State Mutation (weighted view):* 103
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 115`, `structural_boundaries: 55`, `args: 29`, `func_start: 29`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 43`, `dead_code: 2`, `planned_debt: 2`
* *Architecture:* `api: 31`, `import: 27`
* *Defense:* `safety: 98`, `doc: 15`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 59.897
  * `Choke Point (Betweenness):` 0.241211 | `Ripple Effect (Closeness):` 0.381787
  * `Imports (Out-Degree: 21):` Cursor.zig, DragIcon.zig, InputDevice.zig, InputManager.zig, InputRelay.zig, Keyboard.zig, KeyboardGroup.zig, LayerShellSeat.zig...
  * `Imported By (In-Degree: 21):` (Excluded from Brief to save tokens)

### `river/Cursor.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 316.6 | **LOC:** 928 | **CtrlFlow:** 9.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (11.5044%), Tech Debt (8.84%)
**Top Internal Functions/Classes:**
  * `processButton` **(Many-Argument Workhorses)** (Impact: 36.4)
  * `processMotionRelative` **(Many-Argument Workhorses)** (Impact: 16.8)
  * `handleRequestSetCursor` **(Many-Argument Workhorses)** (Impact: 15.7)
  * `updateHovered` **(Defensive Guards)** (Impact: 14.6)
  * `setTheme` **(Defensive Guards)** (Impact: 13.6)
    * *Intent:* /// Set the cursor theme for the given seat, as well as the xwayland theme if /// this is the defaul...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 64
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 27`, `args: 41`, `func_start: 41`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 28`, `planned_debt: 2`
* *Architecture:* `io: 1`, `api: 12`, `import: 18`
* *Defense:* `safety: 60`, `doc: 26`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 10.801
  * `Choke Point (Betweenness):` 0.016974 | `Ripple Effect (Closeness):` 0.250247
  * `Imports (Out-Degree: 13):` DragIcon.zig, InputDevice.zig, LockSurface.zig, Output.zig, PointerBinding.zig, PointerConstraint.zig, Scene.zig, Seat.zig...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `river/LibinputDevice.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 301.2 | **LOC:** 550 | **CtrlFlow:** 24.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (16.1347%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `handleRequest` **(Many-Argument Workhorses)** (Impact: 198.5)
  * `createObject` **(Many-Argument Workhorses)** (Impact: 63.7)
  * `send` **(Compute Cores)** (Impact: 5.6)
  * `handleRequestInert` **(State Mutators)** (Impact: 4.3)
  * `init` **(Defensive Guards)** (Impact: 4.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 127`, `structural_boundaries: 75`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 52`, `state_mutation: 2`
* *Architecture:* `api: 5`, `import: 9`
* *Defense:* `safety: 70`, `doc: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 10.462
  * `Choke Point (Betweenness):` 0.009877 | `Ripple Effect (Closeness):` 0.201212
  * `Imports (Out-Degree: 4):` InputDevice.zig, LibinputAccelConfig.zig, c.zig, std, util.zig, wayland, wlroots
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `river/WindowManager.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 227.46 | **LOC:** 563 | **CtrlFlow:** 13.0% | **Authorship Centralization:** 90.9%
- **Risk Profile:** Cognitive Load (13.2127%), Tech Debt (13.091%)
**Top Internal Functions/Classes:**
  * `renderFinish` **(Compute Cores)** (Impact: 29.3)
    * *Intent:* /// Finish the update sequence and drop stashed buffers. This means that /// the next frame drawn wi...
  * `manageStart` **(Defensive Guards)** (Impact: 16.5)
  * `manageFinish` **(Defensive Guards)** (Impact: 11.7)
  * `handleRequest` **(Many-Argument Workhorses)** (Impact: 10.8)
  * `handleDestroy` **(Defensive Guards)** (Impact: 9.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 17 instances
* *State Mutation (weighted view):* 61
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 32`, `args: 24`, `func_start: 24`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 27`, `planned_debt: 2`, `fragile_debt: 1`
* *Architecture:* `api: 10`, `import: 13`
* *Defense:* `safety: 36`, `doc: 15`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.945
  * `Choke Point (Betweenness):` 0.000512 | `Ripple Effect (Closeness):` 0.019608
  * `Imports (Out-Degree: 8):` Output.zig, Scene.zig, Seat.zig, ShellSurface.zig, Window.zig, WmNode.zig, slotmap, std...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `river/Output.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 223.02 | **LOC:** 549 | **CtrlFlow:** 13.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (12.4241%), Tech Debt (10.9685%)
**Top Internal Functions/Classes:**
  * `renderAndCommit` **(Compute Cores)** (Impact: 27.2)
  * `manageStart` **(Defensive Guards)** (Impact: 22.6)
  * `create` **(Defensive Guards)** (Impact: 13.1)
  * `handleDestroy` **(Many-Argument Workhorses)** (Impact: 10.6)
  * `handlePresent` **(Compute Cores)** (Impact: 10.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 20 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 73
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 33`, `args: 16`, `func_start: 16`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 1`, `state_mutation: 33`, `dead_code: 2`, `planned_debt: 3`
* *Architecture:* `io: 1`, `api: 9`, `import: 9`
* *Defense:* `safety: 28`, `doc: 28`, `test: 1`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 36.078
  * `Choke Point (Betweenness):` 0.023499 | `Ripple Effect (Closeness):` 0.338402
  * `Imports (Out-Degree: 5):` LayerShellOutput.zig, LockSurface.zig, SceneNodeData.zig, Window.zig, std, util.zig, wayland, wlroots
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `river/OutputManager.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 213.52 | **LOC:** 455 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (25.1941%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `commitOutputState` **(Defensive Guards)** (Impact: 51.2)
  * `handleManagerApply` **(Many-Argument Workhorses)** (Impact: 15.6)
  * `validateConfigCoordinates` **(Compute Cores)** (Impact: 15.6)
  * `handlePowerManagerSetMode` **(Type Conversions)** (Impact: 15.1)
  * `autoLayout` **(Defensive Guards)** (Impact: 9.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 17 instances
* *State Mutation (weighted view):* 59
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 63`, `args: 12`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 25`
* *Architecture:* `api: 5`, `import: 13`
* *Defense:* `safety: 39`, `doc: 4`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.945
  * `Choke Point (Betweenness):` 0.000307 | `Ripple Effect (Closeness):` 0.019608
  * `Imports (Out-Degree: 7):` DragIcon.zig, LockSurface.zig, Output.zig, SceneNodeData.zig, Window.zig, XwaylandOverrideRedirect.zig, build_options, std...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `common/deque.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 205.24 | **LOC:** 435 | **CtrlFlow:** 10.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (12.6246%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Deque` **(Compute Cores)** (Impact: 45.0)
    * *Intent:* /// A contiguous, growable, double-ended queue. /// /// Pushing/popping items from either end of the...
  * `ensureTotalCapacityPrecise` **(Many-Argument Workhorses)** (Impact: 19.8)
    * *Intent:* /// If the current capacity is less than `new_capacity`, this function will /// modify the deque so ...
  * `fuzzAgainstArrayList` **(Defensive Guards)** (Impact: 19.3)
  * `bufferIndex` **(Compute Cores)** (Impact: 5.6)
    * *Intent:* /// Returns the index in `buffer` where the element at the given /// index in the logical deque is s...
  * `growCapacity` **(Compute Cores)** (Impact: 5.5)
    * *Intent:* /// Called when memory growth is necessary. Returns a capacity larger than /// minimum that grows su...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 33
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 46`, `args: 24`, `func_start: 24`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 15`
* *Architecture:* `api: 22`, `concurrency: 1`, `import: 1`
* *Defense:* `safety: 62`, `doc: 68`, `test: 5`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 8.101
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.250949
  * `Imports (Out-Degree: 0):` std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `river/XdgToplevel.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 196.2 | **LOC:** 475 | **CtrlFlow:** 12.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (30.5456%), Tech Debt (10.3629%)
**Top Internal Functions/Classes:**
  * `configure` **(Compute Cores)** (Impact: 24.4)
    * *Intent:* /// Send a configure event, return true if the configure should be tracked /// and current surfaces ...
  * `handleCommit` **(Many-Argument Workhorses)** (Impact: 19.0)
  * `needsConfigure` **(Compute Cores)** (Impact: 16.5)
  * `handleRequestFullscreen` **(Type Conversions)** (Impact: 7.8)
  * `handleAckConfigure` **(Defensive Guards)** (Impact: 7.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 72
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 30`, `args: 19`, `func_start: 19`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 32`, `dead_code: 1`, `planned_debt: 2`
* *Architecture:* `api: 3`, `import: 10`
* *Defense:* `safety: 16`, `doc: 12`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 12.607
  * `Choke Point (Betweenness):` 0.01926 | `Ripple Effect (Closeness):` 0.238235
  * `Imports (Out-Degree: 6):` Output.zig, Seat.zig, Window.zig, XdgDecoration.zig, XdgPopup.zig, std, util.zig, wayland...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `river/KeyboardGroup.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 171.74 | **LOC:** 442 | **CtrlFlow:** 16.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (7.7311%), Tech Debt (17.9302%)
**Top Internal Functions/Classes:**
  * `handleKey` **(Many-Argument Workhorses)** (Impact: 44.9)
  * `processKey` **(Compute Cores)** (Impact: 15.5)
  * `match` **(Compute Cores)** (Impact: 13.6)
  * `unref` **(Many-Argument Workhorses)** (Impact: 10.5)
  * `handleBuiltinBinding` **(Defensive Guards)** (Impact: 7.8)
    * *Intent:* /// Handle any builtin, hardcoded compositor keybindings such as VT switching. /// Returns true if t...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 24
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 39`, `args: 14`, `func_start: 14`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 10`, `planned_debt: 3`, `fragile_debt: 1`
* *Architecture:* `api: 9`, `import: 10`
* *Defense:* `safety: 25`, `doc: 18`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 12.826
  * `Choke Point (Betweenness):` 0.000256 | `Ripple Effect (Closeness):` 0.250247
  * `Imports (Out-Degree: 5):` InputDevice.zig, Keyboard.zig, Seat.zig, XkbBinding.zig, std, util.zig, wayland, wlroots...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `river/Server.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 150.12 | **LOC:** 573 | **CtrlFlow:** 10.8% | **Authorship Centralization:** 87.5%
- **Risk Profile:** Cognitive Load (8.7713%), Tech Debt (10.8358%)
**Top Internal Functions/Classes:**
  * `allowlist` **(Many-Argument Workhorses)** (Impact: 16.3)
    * *Intent:* /// Returns true if the global is allowlisted for security contexts
  * `init` **(Defensive Guards)** (Impact: 15.9)
  * `globalFilter` **(Defensive Guards)** (Impact: 15.2)
  * `handleRequestSetCursorShape` **(Defensive Guards)** (Impact: 13.8)
  * `start` **(Defensive Guards)** (Impact: 7.7)
    * *Intent:* /// Create the socket, start the backend, and setup the environment
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 20
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 30`, `args: 16`, `func_start: 16`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 10`, `planned_debt: 3`
* *Architecture:* `io: 1`, `api: 3`, `import: 25`
* *Defense:* `safety: 77`, `doc: 5`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.642
  * `Choke Point (Betweenness):` 0.010316 | `Ripple Effect (Closeness):` 0.014706
  * `Imports (Out-Degree: 21):` IdleInhibitManager.zig, InputManager.zig, LayerShell.zig, LibinputConfig.zig, LockManager.zig, Output.zig, OutputManager.zig, Scene.zig...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `river/Keyboard.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 134.62 | **LOC:** 251 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (21.2704%), Tech Debt (20.5537%)
**Top Internal Functions/Classes:**
  * `create` **(Defensive Guards)** (Impact: 20.3)
  * `processKey` **(Defensive Guards)** (Impact: 9.3)
  * `setGroup` **(Defensive Guards)** (Impact: 8.1)
  * `setKeymap` **(Defensive Guards)** (Impact: 7.6)
  * `maybeDestroy` **(Defensive Guards)** (Impact: 6.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 40
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 16`, `args: 15`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 18`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `api: 10`, `import: 9`
* *Defense:* `safety: 25`, `doc: 6`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 22.229
  * `Choke Point (Betweenness):` 0.008816 | `Ripple Effect (Closeness):` 0.268283
  * `Imports (Out-Degree: 4):` InputDevice.zig, KeyboardGroup.zig, Seat.zig, std, util.zig, wayland, wlroots, xkbcommon
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `river/InputDevice.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 133.42 | **LOC:** 296 | **CtrlFlow:** 15.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (12.5564%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `init` **(Many-Argument Workhorses)** (Impact: 34.3)
  * `handleRequest` **(Many-Argument Workhorses)** (Impact: 34.2)
  * `deinit` **(Compute Cores)** (Impact: 8.4)
  * `handleRemove` **(Defensive Guards)** (Impact: 6.4)
  * `createObject` **(Defensive Guards)** (Impact: 6.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 19
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 21`, `args: 9`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 9`
* *Architecture:* `api: 5`, `import: 12`
* *Defense:* `safety: 20`, `doc: 3`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 25.53
  * `Choke Point (Betweenness):` 0.052422 | `Ripple Effect (Closeness):` 0.275735
  * `Imports (Out-Degree: 7):` Keyboard.zig, LibinputDevice.zig, Seat.zig, Tablet.zig, XkbKeyboard.zig, c.zig, std, util.zig...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `river/XwaylandWindow.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 120.24 | **LOC:** 347 | **CtrlFlow:** 9.7% | **Authorship Centralization:** 93.3%
- **Risk Profile:** Cognitive Load (14.1105%), Tech Debt (9.8048%)
**Top Internal Functions/Classes:**
  * `configure` **(Compute Cores)** (Impact: 15.2)
    * *Intent:* /// Always returns false as we do not care about frame perfection for Xwayland windows.
  * `handleSetSizeHints` **(State Mutators)** (Impact: 9.4)
  * `handleSetOverrideRedirect` **(Defensive Guards)** (Impact: 5.3)
  * `handleSetDecorations` **(State Mutators)** (Impact: 4.7)
  * `handleRequestMaximize` **(State Mutators)** (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 39
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 6`, `args: 18`, `func_start: 18`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 21`, `planned_debt: 1`
* *Architecture:* `api: 3`, `import: 8`
* *Defense:* `safety: 12`, `doc: 7`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.74
  * `Choke Point (Betweenness):` 0.000348 | `Ripple Effect (Closeness):` 0.236345
  * `Imports (Out-Degree: 4):` Output.zig, Window.zig, XwaylandOverrideRedirect.zig, std, util.zig, wayland, wlroots
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `river/TabletTool.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 106.1 | **LOC:** 271 | **CtrlFlow:** 14.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (10.0567%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `axis` **(Many-Argument Workhorses)** (Impact: 34.8)
  * `passthrough` **(Defensive Guards)** (Impact: 11.3)
    * *Intent:* /// Send a motion event for the surface under the tablet tool's cursor if any. /// Send a proximity_...
  * `tip` **(Many-Argument Workhorses)** (Impact: 9.4)
  * `allowSetCursor` **(Compute Cores)** (Impact: 6.7)
  * `proximity` **(Many-Argument Workhorses)** (Impact: 4.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 12`, `args: 13`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 5`
* *Architecture:* `api: 6`, `import: 6`
* *Defense:* `safety: 11`, `doc: 7`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.652
  * `Choke Point (Betweenness):` 0.000219 | `Ripple Effect (Closeness):` 0.189678
  * `Imports (Out-Degree: 2):` Tablet.zig, std, util.zig, wayland, wlroots
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `river/main.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 105.22 | **LOC:** 295 | **CtrlFlow:** 20.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (16.6437%), Tech Debt (17.2732%)
**Top Internal Functions/Classes:**
  * `main` **(Defensive Guards)** (Impact: 35.3)
  * `logFn` **(Defensive Guards)** (Impact: 11.9)
  * `defaultInitPath` **(Defensive Guards)** (Impact: 9.2)
  * `grepRiverctl` **(Defensive Guards)** (Impact: 8.0)
  * `detectClassic` **(Defensive Guards)** (Impact: 7.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 33`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 6`, `unreferenced_by_name: 2`
* *Architecture:* `io: 5`, `api: 5`, `import: 9`
* *Defense:* `safety: 45`, `doc: 2`, `sync_locks: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.677
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` Server.zig, build_options, builtin, c.zig, flags, process.zig, std, util.zig...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `river/XkbKeyboard.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 97.66 | **LOC:** 208 | **CtrlFlow:** 13.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (14.2817%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `sendState` **(Many-Argument Workhorses)** (Impact: 23.8)
  * `createObject` **(Defensive Guards)** (Impact: 19.2)
  * `handleRequest` **(Many-Argument Workhorses)** (Impact: 14.9)
  * `handleRequestInert` **(State Mutators)** (Impact: 4.3)
  * `init` **(Defensive Guards)** (Impact: 3.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 19
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 14`, `args: 7`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 11`
* *Architecture:* `api: 4`, `import: 10`
* *Defense:* `safety: 13`, `doc: 2`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.304
  * `Choke Point (Betweenness):` 0.01745 | `Ripple Effect (Closeness):` 0.201212
  * `Imports (Out-Degree: 4):` InputDevice.zig, Keyboard.zig, XkbKeymap.zig, std, util.zig, wayland, wlroots, xkbcommon
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `river/XkbBinding.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 87.54 | **LOC:** 229 | **CtrlFlow:** 9.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (13.4678%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `match` **(Many-Argument Workhorses)** (Impact: 27.4)
    * *Intent:* /// Compare binding with given keycode, modifiers and keyboard state
  * `handleRequest` **(Many-Argument Workhorses)** (Impact: 11.1)
  * `handleDestroy` **(Defensive Guards)** (Impact: 7.6)
  * `create` **(Many-Argument Workhorses)** (Impact: 4.4)
  * `handleRequestInert` **(State Mutators)** (Impact: 4.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 12`, `args: 9`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 8`
* *Architecture:* `api: 6`, `import: 8`
* *Defense:* `safety: 10`, `doc: 5`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.966
  * `Choke Point (Betweenness):` 0.00011 | `Ripple Effect (Closeness):` 0.248162
  * `Imports (Out-Degree: 3):` Keyboard.zig, Seat.zig, std, util.zig, wayland, wlroots, xkbcommon
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `river/LockManager.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 87.24 | **LOC:** 246 | **CtrlFlow:** 11.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (10.303%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `maybeLock` **(Defensive Guards)** (Impact: 13.0)
  * `handleLock` **(Many-Argument Workhorses)** (Impact: 12.6)
  * `lockSurfaceFromOutput` **(Type Conversions)** (Impact: 7.6)
  * `handleUnlock` **(I/O & Config Routines)** (Impact: 4.0)
  * `handleDestroy` **(State Mutators)** (Impact: 3.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 26
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 15`, `args: 10`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 12`
* *Architecture:* `api: 4`, `import: 8`
* *Defense:* `safety: 15`, `doc: 12`, `sync_locks: 32`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.945
  * `Choke Point (Betweenness):` 8.8e-05 | `Ripple Effect (Closeness):` 0.019608
  * `Imports (Out-Degree: 3):` LockSurface.zig, Output.zig, build_options, std, util.zig, wayland, wlroots
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `river/InputManager.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 81.36 | **LOC:** 288 | **CtrlFlow:** 6.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (7.6628%), Tech Debt (12.3087%)
**Top Internal Functions/Classes:**
  * `handleRequest` **(Defensive Guards)** (Impact: 18.1)
  * `bind` **(Defensive Guards)** (Impact: 7.6)
  * `init` **(Defensive Guards)** (Impact: 6.1)
  * `handleNewVirtualPointer` **(State Mutators)** (Impact: 6.0)
  * `handleRequestInert` **(State Mutators)** (Impact: 4.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 5
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 12`, `args: 16`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 3`, `planned_debt: 2`
* *Architecture:* `api: 4`, `import: 13`
* *Defense:* `safety: 27`, `doc: 2`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.37
  * `Choke Point (Betweenness):` 0.004748 | `Ripple Effect (Closeness):` 0.248162
  * `Imports (Out-Degree: 7):` InputDevice.zig, InputRelay.zig, Keyboard.zig, PointerConstraint.zig, Seat.zig, TextInput.zig, build_options, std...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `river/LayerShell.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 79.34 | **LOC:** 194 | **CtrlFlow:** 14.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (13.7092%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `handleNewSurface` **(Many-Argument Workhorses)** (Impact: 17.9)
  * `checkExclusiveFocus` **(Defensive Guards)** (Impact: 14.3)
  * `handleRequest` **(Defensive Guards)** (Impact: 13.7)
  * `supported` **(Defensive Guards)** (Impact: 6.1)
  * `bind` **(Defensive Guards)** (Impact: 2.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 13
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 19`, `args: 8`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 5`, `dead_code: 1`
* *Architecture:* `api: 3`, `import: 12`
* *Defense:* `safety: 18`, `doc: 1`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.945
  * `Choke Point (Betweenness):` 0.000732 | `Ripple Effect (Closeness):` 0.019608
  * `Imports (Out-Degree: 8):` LayerShellOutput.zig, LayerShellSeat.zig, LayerSurface.zig, Output.zig, SceneNodeData.zig, Seat.zig, slotmap, std...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `river/Decoration.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 75.46 | **LOC:** 166 | **CtrlFlow:** 10.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (21.4814%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `renderFinish` **(Compute Cores)** (Impact: 10.0)
  * `handleRequest` **(Many-Argument Workhorses)** (Impact: 8.9)
  * `create` **(Many-Argument Workhorses)** (Impact: 6.6)
  * `clientCommit` **(Type Conversions)** (Impact: 6.1)
  * `handleRequestInert` **(State Mutators)** (Impact: 4.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 23
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 9`, `args: 9`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 9`
* *Architecture:* `api: 4`, `import: 8`
* *Defense:* `safety: 12`, `doc: 1`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.052
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.234484
  * `Imports (Out-Degree: 2):` Scene.zig, build_options, std, util.zig, wayland, wlroots
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `river/InputRelay.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 71.44 | **LOC:** 234 | **CtrlFlow:** 12.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (4.9447%), Tech Debt (11.3962%)
**Top Internal Functions/Classes:**
  * `focus` **(Defensive Guards)** (Impact: 15.5)
  * `handleInputMethodCommit` **(Defensive Guards)** (Impact: 10.0)
  * `sendInputMethodState` **(Defensive Guards)** (Impact: 8.7)
  * `newInputMethod` **(Many-Argument Workhorses)** (Impact: 6.3)
  * `disableTextInput` **(Defensive Guards)** (Impact: 4.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 8`, `args: 10`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 4`, `planned_debt: 1`
* *Architecture:* `api: 5`, `import: 7`
* *Defense:* `safety: 15`, `doc: 9`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 16.953
  * `Choke Point (Betweenness):` 0.014368 | `Ripple Effect (Closeness):` 0.268283
  * `Imports (Out-Degree: 4):` InputPopup.zig, Seat.zig, TextInput.zig, std, util.zig, wayland, wlroots
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `common/slotmap.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 70.96 | **LOC:** 272 | **CtrlFlow:** 3.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (5.4636%), Tech Debt (10.3775%)
**Top Internal Functions/Classes:**
  * `SlotMap` **(Compute Cores)** (Impact: 17.0)
  * `getSlot` **(Compute Cores)** (Impact: 5.6)
  * `next` **(Defensive Guards)** (Impact: 4.7)
  * `remove` **(State Mutators)** (Impact: 4.0)
  * `expectIterate` **(Defensive Guards)** (Impact: 4.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 21`, `args: 9`, `func_start: 9`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 8`, `planned_debt: 1`
* *Architecture:* `api: 10`, `import: 1`
* *Defense:* `safety: 91`, `doc: 8`, `test: 7`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 13.595
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.248941
  * `Imports (Out-Degree: 0):` std
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `river/LayerShellOutput.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 69.14 | **LOC:** 181 | **CtrlFlow:** 9.6% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (14.1541%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `sendConfigures` **(Many-Argument Workhorses)** (Impact: 16.4)
  * `manageStart` **(State Mutators)** (Impact: 7.0)
  * `handleRequest` **(Many-Argument Workhorses)** (Impact: 6.8)
  * `handleRequestInert` **(State Mutators)** (Impact: 4.3)
  * `arrange` **(State Mutators)** (Impact: 3.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 9`, `args: 8`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 10`
* *Architecture:* `api: 4`, `import: 7`
* *Defense:* `safety: 8`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 12.441
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.227324
  * `Imports (Out-Degree: 3):` Output.zig, SceneNodeData.zig, std, util.zig, wayland, wlroots
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `river/Window.zig` -> **Isaac Freund** (84.2% isolated ownership) | Magnitude: 584.34
- `river/Seat.zig` -> **Isaac Freund** (92.9% isolated ownership) | Magnitude: 424.4
- `river/Cursor.zig` -> **Isaac Freund** (100.0% isolated ownership) | Magnitude: 316.6
- `river/LibinputDevice.zig` -> **Isaac Freund** (100.0% isolated ownership) | Magnitude: 301.2
- `river/WindowManager.zig` -> **Isaac Freund** (90.9% isolated ownership) | Magnitude: 227.46

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `river/Seat.zig` -> **Severity: 22.046** (Bridge: 0.2412 * Flux: 91.3962%)
- `river/Window.zig` -> **Severity: 9.857** (Bridge: 0.0987 * Flux: 99.8502%)
- `river/SceneNodeData.zig` -> **Severity: 4.664** (Bridge: 0.0532 * Flux: 87.6926%)
- `river/InputDevice.zig` -> **Severity: 3.347** (Bridge: 0.0524 * Flux: 63.8475%)
- `river/Output.zig` -> **Severity: 2.321** (Bridge: 0.0235 * Flux: 98.7568%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `river/util.zig` -> **Severity: 36.365** (Embedded: 0.6497 * Error Risk: 55.9714%)
- `river/LockSurface.zig` -> **Severity: 23.336** (Embedded: 0.3135 * Error Risk: 74.4444%)
- `river/PointerConstraint.zig` -> **Severity: 22.483** (Embedded: 0.2502 * Error Risk: 89.8439%)
- `river/Window.zig` -> **Severity: 22.469** (Embedded: 0.3503 * Error Risk: 64.1347%)
- `river/SceneNodeData.zig` -> **Severity: 21.752** (Embedded: 0.3008 * Error Risk: 72.3122%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `river/SceneNodeData.zig` -> **Severity: 6655.7** (Blast Radius: 66.557 * Doc Risk: 100.0%)
- `river/Seat.zig` -> **Severity: 5490.56** (Blast Radius: 59.897 * Doc Risk: 91.6667%)
- `river/Output.zig` -> **Severity: 3307.151** (Blast Radius: 36.078 * Doc Risk: 91.6667%)
- `river/Window.zig` -> **Severity: 2787.227** (Blast Radius: 39.718 * Doc Risk: 70.1754%)
- `river/LockSurface.zig` -> **Severity: 2542.8** (Blast Radius: 25.428 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
