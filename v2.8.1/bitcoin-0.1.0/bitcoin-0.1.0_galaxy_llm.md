# ARCHITECTURAL_BRIEF: bitcoin-0.1.0
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/trottier/original-bitcoin.git` |
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
| Total Artifacts | 50 |
| Analyzed Artifacts (Scanned) | 33 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 17 |
| Total LOC | 14716 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 66.0% |
| Dominant Lang | CPP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.1842 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.8575 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.8207 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 3 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| CPP | 26 | 14615 | 78.8% |
| PLAINTEXT | 4 | 0 | 12.1% |
| MAKEFILE | 2 | 101 | 6.1% |
| MARKDOWN | 1 | 0 | 3.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Small Flat Repo` (z +0.65; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules 48%, Data / Markup / Trivial 18%, Interface Declarations Files 15%, I/O & Config Routines Files 6%, Compute Cores Files 3%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 28 | 84.8% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 5 | 15.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 17*

**Composition by Extension & Reason:**
- `.bmp`: 9x Excluded (Explicitly Denied Extension: '.bmp')
- `.dll`: 2x Excluded (Explicitly Denied Extension: '.dll')
- `.ico`: 2x Excluded (Explicitly Denied Extension: '.ico')
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.exe`: 1x Excluded (Explicitly Denied Extension: '.exe')
- `.rc`: 1x Unsupported Format (.rc)
- `.fbp`: 1x Unsupported Format (.fbp)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 96.4 | 43.4 | 48.1 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 96.3 | 73.8 | 79.8 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 41.7 | 36.2 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 55.1 | 80.0 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 58.9 | 22.1 | 9.9 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 67.6 | 99.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 17.7 | 4.3 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 92.9 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 91.5 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 2372 | 24 | 89 | `src/uibase.cpp` |
| cleanup | 12 | 5 | 2 | `src/db.cpp` |
| guards | 1233 | 25 | 82 | `src/uint256.h` |
| danger | 142 | 18 | 12 | `src/ui.cpp` |
| concurrency | 1 | 1 | 0 | `src/makefile.vc` |
| connectivity | 294 | 19 | 26 | `src/uibase.h` |
| io | 28 | 7 | 2 | `src/net.cpp` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 0 | 0 | 0 | - |
| serialization | 0 | 0 | 0 | - |
| regex | 0 | 0 | 0 | - |
| events | 9 | 5 | 1 | `src/net.cpp` |
| tests | 1 | 1 | 0 | `src/irc.cpp` |
| docs | 147 | 15 | 14 | `src/uibase.h` |
| debt | 327 | 16 | 36 | `src/main.cpp` |
| mutation | 3649 | 26 | 278 | `src/ui.cpp` |
| dead_code | 282 | 17 | 22 | `src/ui.cpp` |
| credential | 0 | 0 | 0 | - |
| threat | 162 | 8 | 7 | `src/sha.cpp` |
| ml_ai | 0 | 0 | 0 | - |
| ui | 14 | 2 | 0 | `src/uibase.cpp` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **3.8333**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/net.cpp` (Hits: 15)
- `src/irc.cpp` (Hits: 4)
- `src/serialize.h` (Hits: 3)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **headers.h** (`src/headers.h`) — 8 inbound connections
2. **sha.h** (`src/sha.h`) — 3 inbound connections
3. **uibase.h** (`src/uibase.h`) — 2 inbound connections
4. **base58.h** (`src/base58.h`) — 1 inbound connections
5. **bignum.h** (`src/bignum.h`) — 1 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **headers.h** (`src/headers.h`) — 50 outbound dependencies
2. **uibase.h** (`src/uibase.h`) — 28 outbound dependencies
3. **serialize.h** (`src/serialize.h`) — 4 outbound dependencies
4. **bignum.h** (`src/bignum.h`) — 3 outbound dependencies
5. **sha.cpp** (`src/sha.cpp`) — 3 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `EvalScript` **(Many-Argument Workhorses)** (@ `src/script.cpp`) -> Impact: **807.3** | LOC: 763
  * *Intent:* // // Script is a stack machine (like Forth) that evaluates a predicate // returning a bool indicating valid or not. There are no loops. // #define st...
- `ProcessMessage` **(Many-Argument Workhorses)** (@ `src/main.cpp`) -> Impact: **161.8** | LOC: 357
- `GetOpName` **(Compute Cores)** (@ `src/script.h`) -> Impact: **160.8** | LOC: 134
- `CTransaction::ConnectInputs` **(Many-Argument Workhorses)** (@ `src/main.cpp`) -> Impact: **110.0** | LOC: 99
- `CMainFrame::InsertTransaction` **(Many-Argument Workhorses)** (@ `src/ui.cpp`) -> Impact: **109.4** | LOC: 188
- `CTxDetailsDialog::CTxDetailsDialog` **(Many-Argument Workhorses)** (@ `src/ui.cpp`) -> Impact: **86.9** | LOC: 214
  * *Intent:* ////////////////////////////////////////////////////////////////////////////// // // CTxDetailsDialog //
- `HtmlEscape` **(Compute Cores)** (@ `src/ui.cpp`) -> Impact: **62.1** | LOC: 29
- `ThreadSocketHandler2` **(Compute Cores)** (@ `src/net.cpp`) -> Impact: **57.6** | LOC: 219
- `SelectCoins` **(Compute Cores)** (@ `src/main.cpp`) -> Impact: **57.0** | LOC: 100
- `ThreadIRCSeed` **(Compute Cores)** (@ `src/irc.cpp`) -> Impact: **52.1** | LOC: 108

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src` | 30 | 11857.36 | 40.49% | 38.89% |
| `__monolith__` | 3 | 3.0 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/uibase.h` -> **100.0%** Exposure
- `src/market.h` -> **99.9997%** Exposure
- `src/ui.cpp` -> **99.7386%** Exposure
- `src/db.cpp` -> **99.3083%** Exposure
- `src/util.cpp` -> **99.1642%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `src/script.cpp` -> **100.0%** Exposure
- `src/market.cpp` -> **99.9998%** Exposure
- `src/util.cpp` -> **99.9997%** Exposure
- `src/main.cpp` -> **99.999%** Exposure
- `src/uint256.h` -> **99.9986%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/ui.cpp` -> **134** Orphaned Functions | **0** Duplicates
- `src/uibase.h` -> **0** Orphaned Functions | **52** Duplicates
- `src/uibase.cpp` -> **32** Orphaned Functions | **0** Duplicates
- `src/main.cpp` -> **31** Orphaned Functions | **0** Duplicates
- `src/db.cpp` -> **20** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `104` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/serialize.h` (CPP) -> Cumulative Risk: **671.4**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.40)
- **Magnitude:** 720.1 | **LOC:** 1152 | **CtrlFlow:** 9.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.8105%), Tech Debt (97.1025%)
- **Heaviest Functions:** `WriteCompactSize` (Compute Cores, Impact: 13.6), `ReadCompactSize` (Compute Cores, Impact: 11.3), `Unserialize_impl` (Many-Argument Workhorses, Impact: 10.9)

### 2. `src/ui.cpp` (CPP) -> Cumulative Risk: **641.26**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.10)
- **Magnitude:** 1986.14 | **LOC:** 3229 | **CtrlFlow:** 16.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.993%), Tech Debt (99.7386%), Documentation (92.8205%)
- **Heaviest Functions:** `CMainFrame::InsertTransaction` (Many-Argument Workhorses, Impact: 109.4), `CTxDetailsDialog::CTxDetailsDialog` (Many-Argument Workhorses, Impact: 86.9), `HtmlEscape` (Compute Cores, Impact: 62.1)

### 3. `src/util.cpp` (CPP) -> Cumulative Risk: **639.62**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.02)
- **Magnitude:** 266.46 | **LOC:** 380 | **CtrlFlow:** 24.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9997%), Tech Debt (99.1642%)
- **Heaviest Functions:** `ParseMoney` (Compute Cores, Impact: 43.6), `FormatMoney` (Compute Cores, Impact: 16.2), `strprintf` (Compute Cores, Impact: 15.4)

### 4. `src/db.cpp` (CPP) -> Cumulative Risk: **617.92**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.58)
- **Magnitude:** 360.74 | **LOC:** 609 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.7942%), Tech Debt (99.3083%), Documentation (96.875%)
- **Heaviest Functions:** `CWalletDB::LoadWallet` (Compute Cores, Impact: 31.1), `CRITICAL_BLOCK` (Compute Cores, Impact: 30.4), `CDB::CDB` (Many-Argument Workhorses, Impact: 29.7)

### 5. `src/main.h` (CPP) -> Cumulative Risk: **609.75**
- **Archetype:** `file_cluster_14` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.94)
- **Magnitude:** 622.76 | **LOC:** 1318 | **CtrlFlow:** 10.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.7738%), Safety Score (83.2861%)
- **Heaviest Functions:** `IsNewerThan` (Compute Cores, Impact: 12.7), `ReadFromDisk` (Compute Cores, Impact: 11.4), `ReadFromDisk` (Many-Argument Workhorses, Impact: 11.1)

### 6. `src/util.h` (CPP) -> Cumulative Risk: **608.55**
- **Archetype:** `file_cluster_14` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.65)
- **Magnitude:** 210.5 | **LOC:** 400 | **CtrlFlow:** 15.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9749%), Safety Score (86.7314%)
- **Heaviest Functions:** `OutputDebugStringF` (Compute Cores, Impact: 18.7), `HexStr` (Generic / Templated Code, Impact: 8.5), `HexNumStr` (Generic / Templated Code, Impact: 6.5)

### 7. `src/market.cpp` (CPP) -> Cumulative Risk: **604.32**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.17)
- **Magnitude:** 122.42 | **LOC:** 265 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9998%), Tech Debt (90.7158%)
- **Heaviest Functions:** `AddAtomsAndPropagate` (Many-Argument Workhorses, Impact: 18.4), `CUser::AddAtom` (Compute Cores, Impact: 15.5), `CReview::AcceptReview` (I/O & Config Routines, Impact: 7.8)

### 8. `src/bignum.h` (CPP) -> Cumulative Risk: **603.33**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.23)
- **Magnitude:** 399.58 | **LOC:** 499 | **CtrlFlow:** 15.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9917%), Safety Score (90.0492%)
- **Heaviest Functions:** `setint64` (Compute Cores, Impact: 15.8), `SetHex` (Compute Cores, Impact: 12.8), `setuint64` (Compute Cores, Impact: 9.8)

### 9. `src/script.cpp` (CPP) -> Cumulative Risk: **591.06**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.42)
- **Magnitude:** 1494.26 | **LOC:** 1128 | **CtrlFlow:** 43.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Cognitive Load (96.3739%)
- **Heaviest Functions:** `EvalScript` (Many-Argument Workhorses, Impact: 807.3), `Solver` (Compute Cores, Impact: 34.2), `SignatureHash` (Many-Argument Workhorses, Impact: 32.1)

### 10. `src/uint256.h` (CPP) -> Cumulative Risk: **588.93**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Parameter Forwarders Files` (z +0.66)
- **Magnitude:** 712.56 | **LOC:** 751 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9986%), Safety Score (96.2869%)
- **Heaviest Functions:** `SetHex` (Compute Cores, Impact: 17.2), `Testuint256AdHoc` (Compute Cores, Impact: 13.0), `operator<<=` (Compute Cores, Impact: 9.3)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/main.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1997.3 | **LOC:** 2661 | **CtrlFlow:** 23.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (60.7667%), Tech Debt (51.4996%)
**Top Internal Functions/Classes:**
  * `ProcessMessage` **(Many-Argument Workhorses)** (Impact: 161.8)
  * `CTransaction::ConnectInputs` **(Many-Argument Workhorses)** (Impact: 110.0)
  * `SelectCoins` **(Compute Cores)** (Impact: 57.0)
  * `CTransaction::AcceptTransaction` **(Many-Argument Workhorses)** (Impact: 43.6)
  * `BitcoinMiner` **(I/O & Config Routines)** (Impact: 39.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 208 instances
* *State Mutation (weighted view):* 681
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 444`, `structural_boundaries: 185`, `args: 93`, `func_start: 98`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 265`, `dead_code: 5`, `planned_debt: 1`, `unreferenced_by_name: 31`
* *Architecture:* `io: 1`, `import: 2`
* *Defense:* `safety: 7`, `doc: 25`, `immutability_locks: 56`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 20.934
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` headers.h, sha.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ui.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1986.14 | **LOC:** 3229 | **CtrlFlow:** 16.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (71.9616%), Tech Debt (99.7386%)
**Top Internal Functions/Classes:**
  * `CMainFrame::InsertTransaction` **(Many-Argument Workhorses)** (Impact: 109.4)
  * `CTxDetailsDialog::CTxDetailsDialog` **(Many-Argument Workhorses)** (Impact: 86.9)
    * *Intent:* ////////////////////////////////////////////////////////////////////////////// // // CTxDetailsDialo...
  * `HtmlEscape` **(Compute Cores)** (Impact: 62.1)
  * `CMyApp::OnInit2` **(I/O & Config Routines)** (Impact: 44.8)
  * `CViewProductDialog::UpdateProductDisplay` **(Compute Cores)** (Impact: 31.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 210 instances
* *State Mutation (weighted view):* 754
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 406`, `structural_boundaries: 264`, `args: 89`, `func_start: 195`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 25`, `high_risk_execution: 1`, `state_mutation: 334`, `dead_code: 1`, `planned_debt: 2`, `unreferenced_by_name: 134`
* *Architecture:* `io: 2`, `api: 1`, `import: 2`
* *Defense:* `safety: 15`, `doc: 26`, `immutability_locks: 67`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 20.934
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` crtdbg.h, headers.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/script.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1494.26 | **LOC:** 1128 | **CtrlFlow:** 43.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (96.3739%), Tech Debt (13.3964%)
**Top Internal Functions/Classes:**
  * `EvalScript` **(Many-Argument Workhorses)** (Impact: 807.3)
    * *Intent:* // // Script is a stack machine (like Forth) that evaluates a predicate // returning a bool indicati...
  * `Solver` **(Compute Cores)** (Impact: 34.2)
  * `SignatureHash` **(Many-Argument Workhorses)** (Impact: 32.1)
    * *Intent:* #undef top
  * `foreach` **(Compute Cores)** (Impact: 31.5)
  * `Solver` **(Many-Argument Workhorses)** (Impact: 29.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 135 instances
* *State Mutation (weighted view):* 407
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 376`, `structural_boundaries: 81`, `args: 25`, `func_start: 18`
* *Risk/State:* `state_mutation: 137`, `dead_code: 1`, `unreferenced_by_name: 5`
* *Architecture:* `import: 1`
* *Defense:* `safety: 3`, `doc: 1`, `immutability_locks: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 20.934
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` headers.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/net.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 726.88 | **LOC:** 1068 | **CtrlFlow:** 19.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (50.6885%), Tech Debt (31.9556%)
**Top Internal Functions/Classes:**
  * `ThreadSocketHandler2` **(Compute Cores)** (Impact: 57.6)
  * `ThreadOpenConnections2` **(Compute Cores)** (Impact: 38.6)
  * `foreach` **(Compute Cores)** (Impact: 36.5)
  * `StartNode` **(Compute Cores)** (Impact: 32.7)
  * `GetMyExternalIP2` **(Many-Argument Workhorses)** (Impact: 24.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 70 instances
* *State Mutation (weighted view):* 233
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 147`, `structural_boundaries: 86`, `args: 55`, `func_start: 42`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 93`, `dead_code: 3`, `planned_debt: 1`, `unreferenced_by_name: 8`
* *Architecture:* `io: 15`, `import: 2`
* *Defense:* `safety: 4`, `doc: 5`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 20.934
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` headers.h, winsock2.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/serialize.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 720.1 | **LOC:** 1152 | **CtrlFlow:** 9.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (61.0741%), Tech Debt (97.1025%)
**Top Internal Functions/Classes:**
  * `WriteCompactSize` **(Compute Cores)** (Impact: 13.6)
  * `ReadCompactSize` **(Compute Cores)** (Impact: 11.3)
  * `Unserialize_impl` **(Many-Argument Workhorses)** (Impact: 10.9)
  * `GetSizeOfCompactSize` **(Compute Cores)** (Impact: 10.2)
    * *Intent:* // // Compact size // size < 253 -- 1 byte // size <= USHRT_MAX -- 3 bytes (253 + 2 bytes) // size <...
  * `main` **(State Mutators)** (Impact: 9.8)
    * *Intent:* // n=1024000 8 seconds // n=2048000 16 seconds // n=4096000 32 seconds // stringstream: // n=1000 1 ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 46 instances
* *State Mutation (weighted view):* 235
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 588`, `args: 157`, `func_start: 168`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 143`, `dead_code: 1`, `duplicate_logic: 20`
* *Architecture:* `io: 3`, `api: 21`, `import: 4`
* *Defense:* `safety: 3`, `doc: 1`, `immutability_locks: 106`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 29.683
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.148897
  * `Imports (Out-Degree: 0):` is_fundamental.hpp, iostream, map, vector
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/uint256.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 712.56 | **LOC:** 751 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (73.4874%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `SetHex` **(Compute Cores)** (Impact: 17.2)
  * `Testuint256AdHoc` **(Compute Cores)** (Impact: 13.0)
  * `operator<<=` **(Compute Cores)** (Impact: 9.3)
  * `operator>>=` **(Compute Cores)** (Impact: 9.3)
  * `operator<` **(Compute Cores)** (Impact: 9.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 94 instances
* *State Mutation (weighted view):* 329
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 276`, `args: 15`, `func_start: 140`, `class_start: 3`
* *Risk/State:* `state_mutation: 141`
* *Architecture:* `api: 11`, `import: 2`
* *Defense:* `doc: 2`, `immutability_locks: 255`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 29.683
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.148897
  * `Imports (Out-Degree: 0):` limits.h, string
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/main.h` (CPP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 622.76 | **LOC:** 1318 | **CtrlFlow:** 10.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (52.2774%), Tech Debt (46.6008%)
**Top Internal Functions/Classes:**
  * `IsNewerThan` **(Compute Cores)** (Impact: 12.7)
  * `ReadFromDisk` **(Compute Cores)** (Impact: 11.4)
  * `ReadFromDisk` **(Many-Argument Workhorses)** (Impact: 11.1)
  * `CheckTransaction` **(Interface Declarations)** (Impact: 10.2)
  * `operator==` **(Compute Cores)** (Impact: 9.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 57 instances
* *State Mutation (weighted view):* 262
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 98`, `structural_boundaries: 159`, `args: 73`, `func_start: 113`, `class_start: 24`
* *Risk/State:* `state_mutation: 148`, `duplicate_logic: 9`
* *Architecture:* `api: 25`
* *Defense:* `doc: 1`, `immutability_locks: 111`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 29.683
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.148897
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/uibase.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 415.92 | **LOC:** 1807 | **CtrlFlow:** 0.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (34.9252%), Tech Debt (50.9269%)
**Top Internal Functions/Classes:**
  * `CSendDialogBase::CSendDialogBase` **(Many-Argument Workhorses)** (Impact: 12.4)
  * `CAboutDialogBase::CAboutDialogBase` **(Many-Argument Workhorses)** (Impact: 11.3)
  * `CEditProductDialogBase::CEditProductDialogBase` **(Many-Argument Workhorses)** (Impact: 9.3)
  * `CYourAddressDialogBase::CYourAddressDialogBase` **(Many-Argument Workhorses)** (Impact: 8.5)
  * `CMainFrameBase::CMainFrameBase` **(Many-Argument Workhorses)** (Impact: 6.1)
    * *Intent:* // Distributed under the MIT/X11 software license, see the accompanying // file license.txt or http:...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 264
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `args: 400`, `func_start: 32`
* *Risk/State:* `state_mutation: 256`, `unreferenced_by_name: 32`
* *Architecture:* `import: 1`
* *Defense:* `doc: 3`, `immutability_locks: 48`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 20.934
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` uibase.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/bignum.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 399.58 | **LOC:** 499 | **CtrlFlow:** 15.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.414%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `setint64` **(Compute Cores)** (Impact: 15.8)
  * `SetHex` **(Compute Cores)** (Impact: 12.8)
  * `setuint64` **(Compute Cores)** (Impact: 9.8)
  * `setuint256` **(Compute Cores)** (Impact: 9.8)
  * `SetCompact` **(Compute Cores)** (Impact: 6.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 45 instances
* *State Mutation (weighted view):* 159
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 82`, `args: 54`, `func_start: 67`, `class_start: 3`
* *Risk/State:* `state_mutation: 69`
* *Architecture:* `api: 27`, `import: 3`
* *Defense:* `immutability_locks: 68`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 29.683
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.148897
  * `Imports (Out-Degree: 0):` bn.h, stdexcept, vector
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/script.h` (CPP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 381.52 | **LOC:** 598 | **CtrlFlow:** 30.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (47.8004%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `GetOpName` **(Compute Cores)** (Impact: 160.8)
  * `GetOp` **(Many-Argument Workhorses)** (Impact: 30.6)
  * `operator<<` **(Compute Cores)** (Impact: 8.1)
  * `FindAndDelete` **(Compute Cores)** (Impact: 7.9)
  * `push_int64` **(Compute Cores)** (Impact: 7.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 62
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 146`, `structural_boundaries: 164`, `args: 31`, `func_start: 48`, `class_start: 2`
* *Risk/State:* `state_mutation: 22`, `dead_code: 2`
* *Architecture:* `api: 7`
* *Defense:* `safety: 2`, `doc: 1`, `immutability_locks: 32`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 29.683
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.148897
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/net.h` (CPP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 364.16 | **LOC:** 857 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (36.3584%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `operator<` **(Compute Cores)** (Impact: 12.8)
  * `AdvertStartPublish` **(Many-Argument Workhorses)** (Impact: 11.9)
    * *Intent:* // // Templates for the publish and subscription system. // The object being published as T& obj nee...
  * `IsValid` **(I/O & Config Routines)** (Impact: 11.4)
  * `AdvertStopPublish` **(Many-Argument Workhorses)** (Impact: 9.5)
  * `CInv` **(Compute Cores)** (Impact: 9.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 26 instances
* *State Mutation (weighted view):* 129
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 143`, `args: 58`, `func_start: 57`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 77`, `dead_code: 3`
* *Architecture:* `api: 26`
* *Defense:* `safety: 10`, `doc: 1`, `immutability_locks: 67`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 29.683
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.148897
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/db.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 360.74 | **LOC:** 609 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (53.1648%), Tech Debt (99.3083%)
**Top Internal Functions/Classes:**
  * `CWalletDB::LoadWallet` **(Compute Cores)** (Impact: 31.1)
    * *Intent:* // // CWalletDB //
  * `CRITICAL_BLOCK` **(Compute Cores)** (Impact: 30.4)
  * `CDB::CDB` **(Many-Argument Workhorses)** (Impact: 29.7)
  * `CTxDB::ReadOwnerTxes` **(Many-Argument Workhorses)** (Impact: 26.2)
  * `CTxDB::LoadBlockIndex` **(I/O & Config Routines)** (Impact: 19.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 29 instances
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 102
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 46`, `args: 13`, `func_start: 32`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 44`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 20`
* *Architecture:* `io: 2`, `api: 1`, `import: 1`
* *Defense:* `safety: 9`, `doc: 6`, `immutability_locks: 10`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 20.934
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` headers.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/uibase.h` (CPP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 0.0 IQR)
- **Magnitude:** 266.9 | **LOC:** 721 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `OnClose` **(Interface Declarations)** (Impact: 1.5)
    * *Intent:* // Virtual event handlers, overide them in your derived class
  * `OnIdle` **(Interface Declarations)** (Impact: 1.5)
  * `OnMouseEvents` **(Interface Declarations)** (Impact: 1.5)
  * `OnPaint` **(Interface Declarations)** (Impact: 1.5)
  * `OnMenuFileExit` **(Interface Declarations)** (Impact: 1.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 250`, `func_start: 117`, `class_start: 16`
* *Risk/State:* `duplicate_logic: 52`
* *Architecture:* `api: 81`, `import: 28`
* *Defense:* `doc: 51`, `immutability_locks: 48`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 47.477
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.173611
  * `Imports (Out-Degree: 0):` bitmap.h, button.h, checkbox.h, choice.h, colour.h, combobox.h, dialog.h, font.h...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/util.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 266.46 | **LOC:** 380 | **CtrlFlow:** 24.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (67.3777%), Tech Debt (99.1642%)
**Top Internal Functions/Classes:**
  * `ParseMoney` **(Compute Cores)** (Impact: 43.6)
  * `FormatMoney` **(Compute Cores)** (Impact: 16.2)
  * `strprintf` **(Compute Cores)** (Impact: 15.4)
  * `AddTimeData` **(Compute Cores)** (Impact: 13.7)
  * `my_snprintf` **(Many-Argument Workhorses)** (Impact: 9.7)
    * *Intent:* // Safer snprintf // - prints up to limit-1 characters // - output string is always null terminated ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 35 instances
* *State Mutation (weighted view):* 106
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 28`, `args: 20`, `func_start: 17`, `class_start: 2`
* *Risk/State:* `state_mutation: 36`, `planned_debt: 1`, `unreferenced_by_name: 12`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `doc: 2`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 20.934
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` headers.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/util.h` (CPP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 210.5 | **LOC:** 400 | **CtrlFlow:** 15.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (83.1145%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `OutputDebugStringF` **(Compute Cores)** (Impact: 18.7)
  * `HexStr` **(Generic / Templated Code)** (Impact: 8.5)
  * `HexNumStr` **(Generic / Templated Code)** (Impact: 6.5)
  * `Hash` **(Many-Argument Workhorses)** (Impact: 3.4)
  * `atoi64` **(Interface Declarations)** (Impact: 3.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 32 instances
* *State Mutation (weighted view):* 98
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 71`, `args: 29`, `func_start: 31`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 34`, `dead_code: 1`
* *Architecture:* `io: 1`, `api: 20`
* *Defense:* `safety: 4`, `immutability_locks: 41`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 29.683
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.148897
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/irc.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 174.64 | **LOC:** 289 | **CtrlFlow:** 27.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (39.0566%), Tech Debt (13.7145%)
**Top Internal Functions/Classes:**
  * `ThreadIRCSeed` **(Compute Cores)** (Impact: 52.1)
  * `RecvLine` **(Compute Cores)** (Impact: 22.5)
  * `RecvUntil` **(Many-Argument Workhorses)** (Impact: 18.7)
  * `RecvLineIRC` **(Compute Cores)** (Impact: 9.8)
  * `Send` **(Compute Cores)** (Impact: 7.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 41
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 32`, `args: 12`, `func_start: 9`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 15`, `unreferenced_by_name: 1`
* *Architecture:* `io: 4`, `import: 1`
* *Defense:* `test: 1`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 20.934
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` headers.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/db.h` (CPP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 170.26 | **LOC:** 421 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.7539%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ReadAtCursor` **(Many-Argument Workhorses)** (Impact: 26.5)
  * `Write` **(Many-Argument Workhorses)** (Impact: 7.3)
  * `Read` **(Type Conversions)** (Impact: 6.6)
  * `Erase` **(Compute Cores)** (Impact: 5.2)
  * `TxnBegin` **(Interface Declarations)** (Impact: 4.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 19
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 82`, `args: 48`, `func_start: 33`, `class_start: 15`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 11`
* *Architecture:* `api: 34`, `import: 1`
* *Defense:* `immutability_locks: 46`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 29.683
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.148897
  * `Imports (Out-Degree: 0):` db_cxx.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/market.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 122.42 | **LOC:** 265 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (33.7983%), Tech Debt (90.7158%)
**Top Internal Functions/Classes:**
  * `AddAtomsAndPropagate` **(Many-Argument Workhorses)** (Impact: 18.4)
  * `CUser::AddAtom` **(Compute Cores)** (Impact: 15.5)
  * `CReview::AcceptReview` **(I/O & Config Routines)** (Impact: 7.8)
  * `AdvertInsert` **(Compute Cores)** (Impact: 5.6)
  * `CProduct::CheckProduct` **(I/O & Config Routines)** (Impact: 5.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 56
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 19`, `args: 7`, `func_start: 9`
* *Risk/State:* `state_mutation: 20`, `dead_code: 1`, `unreferenced_by_name: 6`
* *Architecture:* `import: 1`
* *Defense:* `doc: 8`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 20.934
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` headers.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/base58.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 118.42 | **LOC:** 202 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.447%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `DecodeBase58` **(Compute Cores)** (Impact: 23.0)
  * `EncodeBase58` **(Compute Cores)** (Impact: 10.5)
  * `DecodeBase58Check` **(Compute Cores)** (Impact: 7.8)
  * `AddressToHash160` **(Compute Cores)** (Impact: 7.6)
  * `DecodeBase58` **(Parameter Forwarders)** (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 50
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 33`, `args: 6`, `func_start: 13`
* *Risk/State:* `state_mutation: 18`
* *Architecture:* `api: 1`
* *Defense:* `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 29.683
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.148897
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/sha.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 84.64 | **LOC:** 555 | **CtrlFlow:** 3.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (96.4416%), Tech Debt (40.4784%)
**Top Internal Functions/Classes:**
  * `SHA512::Transform` **(Many-Argument Workhorses)** (Impact: 12.4)
    * *Intent:* #endif // #if CRYPTOPP_BOOL_SSE2_ASM_AVAILABLE
  * `SHA256::Transform` **(Compute Cores)** (Impact: 4.7)
    * *Intent:* // for SHA256 #define S0(x) (rotrFixed(x,2)^rotrFixed(x,13)^rotrFixed(x,22)) #define S1(x) (rotrFixe...
  * `SHA1::Transform` **(Many-Argument Workhorses)** (Impact: 3.6)
    * *Intent:* #define f1(x,y,z) (z^(x&(y^z))) #define f2(x,y,z) (x^y^z) #define f3(x,y,z) ((x&y)|(z&(x|y))) #defin...
  * `SHA384::InitState` **(Interface Declarations)** (Impact: 1.9)
    * *Intent:* */ #undef S0 #undef S1 #undef s0 #undef s1 #undef R // *********************************************...
  * `SHA512::InitState` **(Interface Declarations)** (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 45
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 88`, `args: 103`, `func_start: 9`
* *Risk/State:* `state_mutation: 41`, `dead_code: 1`, `unreferenced_by_name: 8`
* *Architecture:* `import: 3`
* *Defense:* `safety: 1`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 20.934
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` assert.h, memory.h, sha.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/key.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 64.32 | **LOC:** 157 | **CtrlFlow:** 13.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (14.6865%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Sign` **(Parameter Forwarders)** (Impact: 4.3)
  * `Verify` **(Parameter Forwarders)** (Impact: 4.3)
  * `Sign` **(Compute Cores)** (Impact: 4.0)
  * `Verify` **(Compute Cores)** (Impact: 3.8)
  * `GetPrivKey` **(I/O & Config Routines)** (Impact: 3.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 20`, `args: 8`, `func_start: 14`, `class_start: 2`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `api: 7`
* *Defense:* `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 29.683
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.148897
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/ui.h` (CPP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 52.2 | **LOC:** 419 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (2.3916%), Tech Debt (88.7095%)
**Top Internal Functions/Classes:**
  * `CGetTextFromUserDialog` **(Many-Argument Workhorses)** (Impact: 6.2)
    * *Intent:* /** Constructor */
  * `OnKeyDown` **(Compute Cores)** (Impact: 6.0)
  * `OnKeyDown` **(Interface Declarations)** (Impact: 1.5)
  * `OnKeyDown` **(Interface Declarations)** (Impact: 1.5)
    * *Intent:* // Event handlers
  * `OnKeyDown` **(Interface Declarations)** (Impact: 1.5)
    * *Intent:* // Event handlers
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 149`, `args: 16`, `func_start: 13`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 2`, `duplicate_logic: 5`
* *Architecture:* `api: 17`
* *Defense:* `doc: 14`, `immutability_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 29.683
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.148897
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/sha.h` (CPP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 0.0 IQR)
- **Magnitude:** 43.5 | **LOC:** 178 | **CtrlFlow:** 19.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.3497%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ByteReverse` **(I/O & Config Routines)** (Impact: 4.7)
  * `ByteReverse` **(Compute Cores)** (Impact: 4.4)
    * *Intent:* #ifdef WORD64_AVAILABLE
  * `ByteReverse` **(I/O & Config Routines)** (Impact: 3.0)
  * `rotlFixed` **(Generic / Templated Code)** (Impact: 2.0)
    * *Intent:* #endif
  * `rotrFixed` **(Generic / Templated Code)** (Impact: 2.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 59`, `args: 10`, `func_start: 13`, `class_start: 5`
* *Risk/State:* `state_mutation: 3`, `dead_code: 1`
* *Architecture:* `api: 5`, `import: 1`
* *Defense:* `safety: 2`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 56.374
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.183824
  * `Imports (Out-Degree: 0):` stdlib.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/market.h` (CPP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 42.58 | **LOC:** 183 | **CtrlFlow:** 5.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (22.2814%), Tech Debt (99.9997%)
**Top Internal Functions/Classes:**
  * `IMPLEMENT_SERIALIZE` **(State Mutators)** (Impact: 4.1)
  * `SetNull` **(I/O & Config Routines)** (Impact: 1.4)
  * `CReview` **(I/O & Config Routines)** (Impact: 1.4)
  * `CProduct` **(I/O & Config Routines)** (Impact: 1.3)
  * `GetAtomCount` **(I/O & Config Routines)** (Impact: 1.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 17
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 17`, `args: 5`, `func_start: 13`, `class_start: 6`
* *Risk/State:* `state_mutation: 13`, `duplicate_logic: 7`
* *Architecture:* `api: 5`
* *Defense:* `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 29.683
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.148897
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/makefile` (MAKEFILE | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 19.84 | **LOC:** 84 | **CtrlFlow:** 5.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.1307%), Tech Debt (70.3784%)
**Top Internal Functions/Classes:**
  * `obj/ui_res.o` **(I/O & Config Routines)** (Impact: 1.4)
  * `all` **(I/O & Config Routines)** (Impact: 1.1)
  * `headers.h.gch` **(I/O & Config Routines)** (Impact: 1.1)
  * `obj/util.o` **(I/O & Config Routines)** (Impact: 1.1)
  * `obj/script.o` **(I/O & Config Routines)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 13`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 1`, `dead_code: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 20.934
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/uint256.h` -> **Severity: 14.337** (Embedded: 0.1489 * Error Risk: 96.2869%)
- `src/bignum.h` -> **Severity: 13.408** (Embedded: 0.1489 * Error Risk: 90.0492%)
- `src/base58.h` -> **Severity: 13.232** (Embedded: 0.1489 * Error Risk: 88.864%)
- `src/util.h` -> **Severity: 12.914** (Embedded: 0.1489 * Error Risk: 86.7314%)
- `src/serialize.h` -> **Severity: 12.523** (Embedded: 0.1489 * Error Risk: 84.1048%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/sha.h` -> **Severity: 5637.4** (Blast Radius: 56.374 * Doc Risk: 100.0%)
- `src/uibase.h` -> **Severity: 4747.7** (Blast Radius: 47.477 * Doc Risk: 100.0%)
- `src/base58.h` -> **Severity: 2968.3** (Blast Radius: 29.683 * Doc Risk: 100.0%)
- `src/bignum.h` -> **Severity: 2968.3** (Blast Radius: 29.683 * Doc Risk: 100.0%)
- `src/db.h` -> **Severity: 2968.3** (Blast Radius: 29.683 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
