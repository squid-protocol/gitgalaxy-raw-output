# ARCHITECTURAL_BRIEF: cobol-samples
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/neopragma/cobol-samples.git` |
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
| Total Artifacts | 53 |
| Analyzed Artifacts (Scanned) | 35 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 18 |
| Total LOC | 1522 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 66.0% |
| Dominant Lang | COBOL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2368 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.7013 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 5.7% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 1 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| MARKDOWN | 16 | 0 | 45.7% |
| COBOL | 15 | 1458 | 42.9% |
| SHELL | 3 | 63 | 8.6% |
| BINARY_THREAT | 1 | 1 | 2.9% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.278`
> **Composition Archetype:** `Mainframe / COBOL & Config` (z +1.13; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 51%, Declarative / Non-Code 34%, I/O & Config Routines Files 11%, Interface Declarations Files 3%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 18 | 51.4% |
| Unknown | 1 | 2.9% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 16 | 45.7% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 18*

**Composition by Extension & Reason:**
- `no_extension`: 14x Excluded (Binary Format Detected), 3x Unsupported Format (.undeterminable), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 82.9 | 29.8 | 19.8 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.7 | 73.1 | 79.8 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 43.5 | 4.5 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 2.7 | 2.2 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 4.1 | 1.0 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 77.5 | 97.3 | 100.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 45.6 | 5.5 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 84.2 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 23.7 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 8 | 4 | 1 | `src/main/cobol/DATE1.CBL` |
| cleanup | 4 | 2 | 0 | `src/main/cobol/CPSEQFR.CBL` |
| guards | 0 | 0 | 0 | - |
| danger | 41 | 17 | 3 | `compile` |
| concurrency | 1 | 1 | 0 | `compile` |
| connectivity | 7 | 6 | 1 | `src/main/cobol/REFORMER.CBL` |
| io | 29 | 4 | 3 | `src/main/cobol/CPSEQFR.CBL` |
| crypto | 0 | 0 | 0 | - |
| ipc | 10 | 2 | 0 | `src/main/cobol/MOVEME.CBL` |
| time | 25 | 3 | 0 | `src/main/cobol/DATE1.CBL` |
| serialization | 16 | 5 | 2 | `src/main/cobol/STRINGIT.CBL` |
| regex | 18 | 4 | 1 | `src/main/cobol/STRINGIT.CBL` |
| events | 0 | 0 | 0 | - |
| tests | 0 | 0 | 0 | - |
| docs | 0 | 0 | 0 | - |
| debt | 180 | 13 | 17 | `src/main/cobol/MOVEME.CBL` |
| mutation | 309 | 17 | 30 | `src/main/cobol/MOVEME.CBL` |
| dead_code | 14 | 6 | 1 | `src/main/cobol/NOTBOOL.CBL` |
| credential | 0 | 0 | 0 | - |
| threat | 14 | 8 | 2 | `src/main/cobol/DATE1.CBL` |
| ml_ai | 4 | 1 | 0 | `src/main/cobol/ATTRACT.CBL` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/main/cobol/CPSEQFR.CBL` (Hits: 13)
- `compile` (Hits: 7)
- `src/main/cobol/CPSEQVR.CBL` (Hits: 6)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **DATE1-notes.md** (`DATE1-notes.md`) — 3 inbound connections
2. **DATE2-notes.md** (`DATE2-notes.md`) — 3 inbound connections
3. **COND88-notes.md** (`COND88-notes.md`) — 2 inbound connections
4. **ATTRACT-notes.md** (`ATTRACT-notes.md`) — 1 inbound connections
5. **BRAKES-notes.md** (`BRAKES-notes.md`) — 1 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **README.md** (`README.md`) — 15 outbound dependencies
2. **HOURGLASS-notes.md** (`HOURGLASS-notes.md`) — 2 outbound dependencies
3. **DATE1-notes.md** (`DATE1-notes.md`) — 1 outbound dependencies
4. **DATE2-notes.md** (`DATE2-notes.md`) — 1 outbound dependencies
5. **IFEVAL-notes.md** (`IFEVAL-notes.md`) — 1 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `FILE-CONTROL` **(I/O & Config Routines)** (@ `src/main/cobol/CPSEQVR.CBL`) -> Impact: **13.2** | LOC: 64
- `FILE-CONTROL` **(I/O & Config Routines)** (@ `src/main/cobol/CPSEQFR.CBL`) -> Impact: **10.3** | LOC: 67
- `PRINT-INVOICE-DETAILS` **(I/O & Config Routines)** (@ `src/main/cobol/INVCALC.CBL`) -> Impact: **8.2** | LOC: 44
- `Anonymous_Block` **(Compute Cores)** (@ `compile`) -> Impact: **4.7** | LOC: 9
- `Anonymous_Block` **(Compute Cores)** (@ `compile`) -> Impact: **4.6** | LOC: 7
- `Anonymous_Block` **(Compute Cores)** (@ `compile`) -> Impact: **4.4** | LOC: 3
  * *Intent:* # remove existing output file, if any
- `__global_context__` **(I/O & Config Routines)** (@ `compile`) -> Impact: **4.3** | LOC: 30
- `Anonymous_Block` **(Unclassified)** (@ `compile-all`) -> Impact: **4.3** | LOC: 6
- `Anonymous_Block` **(I/O & Config Routines)** (@ `compile`) -> Impact: **3.4** | LOC: 7
- `ComputeAttraction` **(I/O & Config Routines)** (@ `src/main/cobol/ATTRACT.CBL`) -> Impact: **2.5** | LOC: 9

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Unclassified**: no dominant structural signature (too small or ambiguous)

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src/main/cobol` | 15 | 742.06 | 31.75% | 5.75% |
| `__monolith__` | 20 | 582.4 | 4.53% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/main/cobol/CPSEQVR.CBL` -> **43.507%** Exposure
- `src/main/cobol/CPSEQFR.CBL` -> **42.6996%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `compile` -> **100.0%** Exposure
- `src/main/cobol/COND88.CBL` -> **100.0%** Exposure
- `src/main/cobol/IFEVAL.CBL` -> **100.0%** Exposure
- `src/main/cobol/NOTBOOL.CBL` -> **100.0%** Exposure
- `src/main/cobol/INVCALC.CBL` -> **99.9994%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/main/cobol/CPSEQFR.CBL` -> **1** Orphaned Functions | **0** Duplicates
- `src/main/cobol/CPSEQVR.CBL` -> **1** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `14` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `21` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/main/cobol/INVCALC.CBL` (COBOL) -> Cumulative Risk: **445.49**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +2.15)
- **Magnitude:** 65.24 | **LOC:** 175 | **CtrlFlow:** 7.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9994%), Safety Score (88.5736%)
- **Heaviest Functions:** `PRINT-INVOICE-DETAILS` (I/O & Config Routines, Impact: 8.2), `INVALID-INVOICE-DATA` (Interface Declarations, Impact: 1.1)

### 2. `src/main/cobol/CPSEQVR.CBL` (COBOL) -> Cumulative Risk: **445.04**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `I/O & Config Routines Files` (z +0.00)
- **Magnitude:** 24.54 | **LOC:** 83 | **CtrlFlow:** 13.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (97.2619%), Safety Score (79.888%)
- **Heaviest Functions:** `FILE-CONTROL` (I/O & Config Routines, Impact: 13.2)

### 3. `src/main/cobol/CPSEQFR.CBL` (COBOL) -> Cumulative Risk: **435.33**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `I/O & Config Routines Files` (z -0.09)
- **Magnitude:** 20.66 | **LOC:** 86 | **CtrlFlow:** 8.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (94.7555%), Safety Score (78.5069%)
- **Heaviest Functions:** `FILE-CONTROL` (I/O & Config Routines, Impact: 10.3)

### 4. `compile` (SHELL) -> Cumulative Risk: **430.19**
- **Archetype:** `file_cluster_15` (Distance: N/A IQR)
- **Composition Archetype:** `I/O & Config Routines Files` (z +0.10)
- **Magnitude:** 51.02 | **LOC:** 70 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (97.8179%), Cognitive Load (76.4313%)
- **Heaviest Functions:** `Anonymous_Block` (Compute Cores, Impact: 4.7), `Anonymous_Block` (Compute Cores, Impact: 4.6), `Anonymous_Block` (Compute Cores, Impact: 4.4)

### 5. `src/main/cobol/ATTRACT.CBL` (COBOL) -> Cumulative Risk: **430.09**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `I/O & Config Routines Files` (z +1.65)
- **Magnitude:** 31.7 | **LOC:** 184 | **CtrlFlow:** 4.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.0778%), Safety Score (74.6494%)
- **Heaviest Functions:** `ComputeAttraction` (I/O & Config Routines, Impact: 2.5), `SolicitAttributesOfBody` (I/O & Config Routines, Impact: 2.2), `VerifyAttributesOfBody` (Interface Declarations, Impact: 1.4)

### 6. `src/main/cobol/NOTBOOL.CBL` (COBOL) -> Cumulative Risk: **425.72**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Declarative / Non-Code` (z +0.84)
- **Magnitude:** 103.68 | **LOC:** 185 | **CtrlFlow:** 26.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.478%), Cognitive Load (78.3421%)

### 7. `src/main/cobol/COND88.CBL` (COBOL) -> Cumulative Risk: **384.2**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Declarative / Non-Code` (z +0.58)
- **Magnitude:** 82.42 | **LOC:** 100 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.0199%), Cognitive Load (82.8845%)

### 8. `src/main/cobol/IFEVAL.CBL` (COBOL) -> Cumulative Risk: **383.37**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Declarative / Non-Code` (z +0.71)
- **Magnitude:** 124.9 | **LOC:** 153 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.711%), Cognitive Load (81.3617%)

### 9. `src/main/cobol/REFORMER.CBL` (COBOL) -> Cumulative Risk: **352.83**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Declarative / Non-Code` (z +0.37)
- **Magnitude:** 68.14 | **LOC:** 211 | **CtrlFlow:** 7.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9946%), Safety Score (85.3549%), Cognitive Load (46.3441%)

### 10. `src/main/cobol/MOVEME.CBL` (COBOL) -> Cumulative Risk: **336.44**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Declarative / Non-Code` (z +0.41)
- **Magnitude:** 71.48 | **LOC:** 230 | **CtrlFlow:** 1.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9929%), Safety Score (84.9663%), Cognitive Load (36.8134%)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `TESTIO2.Output.bin` (BINARY_THREAT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.279
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/cobol/IFEVAL.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 124.9 | **LOC:** 153 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (81.3617%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 36 instances
* *State Mutation (weighted view):* 108
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 36`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.279
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/cobol/NOTBOOL.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 103.68 | **LOC:** 185 | **CtrlFlow:** 26.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (78.3421%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 29 instances
* *State Mutation (weighted view):* 87
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 29`, `dead_code: 5`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.279
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/cobol/COND88.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 82.42 | **LOC:** 100 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (82.8845%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 66
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 22`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.279
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/cobol/MOVEME.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 71.48 | **LOC:** 230 | **CtrlFlow:** 1.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (36.8134%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 52
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 80`, `args: 9`, `class_start: 1`
* *Risk/State:* `state_mutation: 46`, `dead_code: 1`
* *Architecture:* `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.279
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/cobol/REFORMER.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 68.14 | **LOC:** 211 | **CtrlFlow:** 7.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (46.3441%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 48
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 27`, `args: 13`, `class_start: 1`
* *Risk/State:* `state_mutation: 30`, `dead_code: 2`
* *Architecture:* `api: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.279
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/cobol/INVCALC.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 65.24 | **LOC:** 175 | **CtrlFlow:** 7.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (54.579%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `PRINT-INVOICE-DETAILS` **(I/O & Config Routines)** (Impact: 8.2)
  * `INVALID-INVOICE-DATA` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 53
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 28`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 39`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.279
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `compile` (SHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 51.02 | **LOC:** 70 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (76.4313%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block` **(Compute Cores)** (Impact: 4.7)
  * `Anonymous_Block` **(Compute Cores)** (Impact: 4.6)
  * `Anonymous_Block` **(Compute Cores)** (Impact: 4.4)
    * *Intent:* # remove existing output file, if any
  * `__global_context__` **(I/O & Config Routines)** (Impact: 4.3)
  * `Anonymous_Block` **(I/O & Config Routines)** (Impact: 3.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 24
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 46`, `args: 8`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 8`
* *Architecture:* `io: 7`, `api: 1`, `import: 1`
* *Defense:* `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.279
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` envvars
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/cobol/ATTRACT.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 31.7 | **LOC:** 184 | **CtrlFlow:** 4.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (19.7816%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ComputeAttraction` **(I/O & Config Routines)** (Impact: 2.5)
  * `SolicitAttributesOfBody` **(I/O & Config Routines)** (Impact: 2.2)
  * `VerifyAttributesOfBody` **(Interface Declarations)** (Impact: 1.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 23
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 40`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 17`, `dead_code: 4`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.279
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/cobol/DATE1.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Drift: 0.0 IQR)
- **Magnitude:** 29.74 | **LOC:** 176 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 13`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 11`
* *Architecture:* `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.279
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/cobol/HEX2TEXT.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 28.7 | **LOC:** 43 | **CtrlFlow:** 5.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (37.2852%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 9`, `args: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 8`
* *Architecture:* `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.279
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/cobol/STRINGIT.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 27.9 | **LOC:** 113 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 19`, `args: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 11`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.279
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/cobol/DATE2.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 26.9 | **LOC:** 180 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 20`, `class_start: 1`
* *Risk/State:* `state_mutation: 8`
* *Architecture:* `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.279
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/cobol/CPSEQVR.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 24.54 | **LOC:** 83 | **CtrlFlow:** 13.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (21.9487%), Tech Debt (43.507%)
**Top Internal Functions/Classes:**
  * `FILE-CONTROL` **(I/O & Config Routines)** (Impact: 13.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 10
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 13`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 6`, `unreferenced_by_name: 1`
* *Architecture:* `io: 6`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.279
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/cobol/CPSEQFR.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 20.66 | **LOC:** 86 | **CtrlFlow:** 8.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.9632%), Tech Debt (42.6996%)
**Top Internal Functions/Classes:**
  * `FILE-CONTROL` **(I/O & Config Routines)** (Impact: 10.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 14`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 3`, `unreferenced_by_name: 1`
* *Architecture:* `io: 13`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.279
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/cobol/BRAKES.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 19.5 | **LOC:** 60 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.279
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/cobol/HELLO.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 16.56 | **LOC:** 44 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.279
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `compile-all` (SHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 11.86 | **LOC:** 14 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (14.1851%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block` **(Unclassified)** (Impact: 4.3)
  * `__global_context__` **(Unclassified)** (Impact: 1.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 6`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 2`
* *Architecture:* `io: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.279
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `run` (SHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1.88 | **LOC:** 8 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__global_context__` **(Unclassified)** (Impact: 1.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `args: 1`
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.279
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `MOVEME-notes.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.7 | **LOC:** 85 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 19.315
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.029412
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `HOURGLASS-notes.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.56 | **LOC:** 78 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 19.315
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.029412
  * `Imports (Out-Degree: 2):` DATE1-notes.md, DATE2-notes.md
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.26 | **LOC:** 63 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 18.279
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` ATTRACT-notes.md, BRAKES-notes.md, COND88-notes.md, CPSEQFR-notes.md, CPSEQVR-notes.md, DATE1-notes.md, DATE2-notes.md, HELLO-notes.md...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `DATE2-notes.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.08 | **LOC:** 54 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 183.449
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.088235
  * `Imports (Out-Degree: 1):` DATE1-notes.md
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `ATTRACT-notes.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.04 | **LOC:** 52 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 19.315
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.029412
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `BRAKES-notes.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 15 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 19.315
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.029412
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/main/cobol/ATTRACT.CBL` -> **Severity: 1827.9** (Blast Radius: 18.279 * Doc Risk: 100.0%)
- `src/main/cobol/CPSEQFR.CBL` -> **Severity: 1827.9** (Blast Radius: 18.279 * Doc Risk: 100.0%)
- `src/main/cobol/CPSEQVR.CBL` -> **Severity: 1827.9** (Blast Radius: 18.279 * Doc Risk: 100.0%)
- `src/main/cobol/INVCALC.CBL` -> **Severity: 1827.9** (Blast Radius: 18.279 * Doc Risk: 100.0%)
- `compile` -> **Severity: 913.95** (Blast Radius: 18.279 * Doc Risk: 50.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
