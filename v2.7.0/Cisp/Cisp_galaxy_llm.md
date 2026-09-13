# ARCHITECTURAL_BRIEF: Cisp
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/lauryndbrown/Cisp` |
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
| Total Artifacts | 51 |
| Analyzed Artifacts (Scanned) | 7 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 44 |
| Total LOC | 839 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 13.7% |
| Dominant Lang | COBOL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 0 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| COBOL | 6 | 824 | 85.7% |
| BATCH | 1 | 15 | 14.3% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 7 | 100.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 44*

**Composition by Extension & Reason:**
- `.dll`: 29x Excluded (Explicitly Denied Extension: '.dll')
- `.lisp`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.exe`: 3x Excluded (Explicitly Denied Extension: '.exe')
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 1x Excluded (Machine-Generated Source Code Signature: 83 LOC)
- `.data`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 92.4 | 52.5 | 54.8 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 97.8 | 74.5 | 84.6 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 88.5 | 44.9 | 30.3 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 13.5 | 2.4 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 3.3 | 2.0 | 2.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 85.5 | 99.9 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 85.7 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 50.0 | 42.9 | 50.0 | 50.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 6 | 3 | 2 | `recursion.cbl` |
| cleanup | 12 | 6 | 2 | `recursion.cbl` |
| guards | 0 | 0 | 0 | - |
| danger | 7 | 6 | 1 | `cisp-error.cbl` |
| concurrency | 0 | 0 | 0 | - |
| connectivity | 5 | 5 | 1 | `cisp-error.cbl` |
| io | 43 | 5 | 14 | `recursion.cbl` |
| crypto | 0 | 0 | 0 | - |
| ipc | 31 | 5 | 8 | `lisp.cbl` |
| time | 0 | 0 | 0 | - |
| serialization | 19 | 4 | 4 | `tokenizer.cbl` |
| regex | 0 | 0 | 0 | - |
| events | 0 | 0 | 0 | - |
| tests | 0 | 0 | 0 | - |
| docs | 0 | 0 | 0 | - |
| debt | 43 | 5 | 14 | `lisp.cbl` |
| mutation | 209 | 7 | 56 | `tokenizer.cbl` |
| dead_code | 14 | 6 | 3 | `tokenizer.cbl` |
| credential | 0 | 0 | 0 | - |
| threat | 5 | 2 | 2 | `recursion.cbl` |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **1.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `recursion.cbl` (Hits: 15)
- `tokenizer.cbl` (Hits: 14)
- `logger.cbl` (Hits: 8)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
No file in this repository is imported by another file that GitGalaxy could resolve, so there is no blast-radius ranking to report. That is itself a finding: either the codebase genuinely has no internal dependency structure (a collection of scripts, documents or configuration rather than a coupled system), or its import style is one the engine does not resolve for this language. Do not infer that any file is load-bearing from this section.


### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
No file in this repository declares an import that GitGalaxy resolved, so there is no coupling ranking to report. See the note above -- the same caveat applies.


## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `MAIN-PROCEDURE` (@ `lisp.cbl`) -> Impact: **11.2** | LOC: 25
- `MAIN-PROCEDURE` (@ `recursion.cbl`) -> Impact: **11.2** | LOC: 25
- `FORMAT-LISP-PROCEDURE` (@ `tokenizer.cbl`) -> Impact: **8.8** | LOC: 36
- `FILE-HANDLING-PROCEDURE` (@ `tokenizer.cbl`) -> Impact: **8.2** | LOC: 24
- `CALC-LISP-LENGTH` (@ `tokenizer.cbl`) -> Impact: **8.0** | LOC: 19
- `EVALUATE-CURRENT-COMMAND` (@ `lisp.cbl`) -> Impact: **7.5** | LOC: 10
- `EVALUATE-CURRENT-VALUES` (@ `lisp.cbl`) -> Impact: **7.0** | LOC: 21
- `MAIN-PROCEDURE` (@ `logger.cbl`) -> Impact: **6.5** | LOC: 11
- `FORMAT-PAREN-SPACE-PROCEDURE` (@ `tokenizer.cbl`) -> Impact: **6.5** | LOC: 10
- `FILE-CONTROL` (@ `tokenizer.cbl`) -> Impact: **6.1** | LOC: 61

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `__monolith__` | 6 | 589.38 | 61.22% | 52.38% |
| `bin` | 1 | 15.3 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `logger.cbl` -> **88.5488%** Exposure
- `cisp.cbl` -> **82.2336%** Exposure
- `cisp-error.cbl` -> **56.9001%** Exposure
- `recursion.cbl` -> **30.2941%** Exposure
- `tokenizer.cbl` -> **29.658%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `tokenizer.cbl` -> **100.0%** Exposure
- `lisp.cbl` -> **99.9999%** Exposure
- `recursion.cbl` -> **99.9992%** Exposure
- `cisp.cbl` -> **99.931%** Exposure
- `logger.cbl` -> **99.9137%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tokenizer.cbl` -> **4** Orphaned Functions | **0** Duplicates
- `recursion.cbl` -> **3** Orphaned Functions | **0** Duplicates
- `cisp.cbl` -> **2** Orphaned Functions | **0** Duplicates
- `lisp.cbl` -> **2** Orphaned Functions | **0** Duplicates
- `logger.cbl` -> **2** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `32` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `0` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `tokenizer.cbl` (COBOL) -> Cumulative Risk: **524.67**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 265.8 | **LOC:** 306 | **CtrlFlow:** 15.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (97.7753%), Verification (80.0%)
- **Heaviest Functions:** `FORMAT-LISP-PROCEDURE` (Impact: 8.8), `FILE-HANDLING-PROCEDURE` (Impact: 8.2), `CALC-LISP-LENGTH` (Impact: 8.0)

### 2. `logger.cbl` (COBOL) -> Cumulative Risk: **478.69**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 28.6 | **LOC:** 62 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9137%), Tech Debt (88.5488%), Safety Score (79.576%)
- **Heaviest Functions:** `MAIN-PROCEDURE` (Impact: 6.5), `FILE-CONTROL` (Impact: 1.9), `LOG-INIT-PROCEDURE` (Impact: 1.4)

### 3. `lisp.cbl` (COBOL) -> Cumulative Risk: **465.35**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 121.56 | **LOC:** 193 | **CtrlFlow:** 17.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9999%), Cognitive Load (92.4269%), Safety Score (91.1314%)
- **Heaviest Functions:** `MAIN-PROCEDURE` (Impact: 11.2), `EVALUATE-CURRENT-COMMAND` (Impact: 7.5), `EVALUATE-CURRENT-VALUES` (Impact: 7.0)

### 4. `cisp.cbl` (COBOL) -> Cumulative Risk: **463.4**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 28.74 | **LOC:** 79 | **CtrlFlow:** 3.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.931%), Tech Debt (82.2336%), Safety Score (80.0631%)
- **Heaviest Functions:** `FILE-CONTROL` (Impact: 4.5), `READ-CMD-LINE-PROCEDURE` (Impact: 1.5), `MAIN-PROCEDURE` (Impact: 1.4)

### 5. `recursion.cbl` (COBOL) -> Cumulative Risk: **460.0**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 122.8 | **LOC:** 229 | **CtrlFlow:** 7.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9992%), Safety Score (88.4401%), Cognitive Load (86.2773%)
- **Heaviest Functions:** `MAIN-PROCEDURE` (Impact: 11.2), `PRINT-CALL-STACK-PROCEDURE` (Impact: 4.8), `FILE-CONTROL` (Impact: 4.0)

### 6. `cisp-error.cbl` (COBOL) -> Cumulative Risk: **416.09**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 21.88 | **LOC:** 68 | **CtrlFlow:** 7.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (98.6166%), Safety Score (84.5887%), Tech Debt (56.9001%)
- **Heaviest Functions:** `MAIN-PROCEDURE` (Impact: 3.2), `THROW-ERROR-PROCEDURE` (Impact: 2.5), `CLOSE-OPEN-FILES-PROCEDURE` (Impact: 2.5)

### 7. `bin/cisp.bat` (BATCH) -> Cumulative Risk: **2.3**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 15.3 | **LOC:** 16 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Verification (2.2977%)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `tokenizer.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 265.8 | **LOC:** 306 | **CtrlFlow:** 15.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (64.8148%), Tech Debt (29.658%)
**Top Internal Functions/Classes:**
  * `FORMAT-LISP-PROCEDURE` (Impact: 8.8)
  * `FILE-HANDLING-PROCEDURE` (Impact: 8.2)
  * `CALC-LISP-LENGTH` (Impact: 8.0)
  * `FORMAT-PAREN-SPACE-PROCEDURE` (Impact: 6.5)
  * `FILE-CONTROL` (Impact: 6.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 49 instances
* *State Mutation (weighted view):* 182
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 53`, `args: 9`, `func_start: 21`, `class_start: 1`
* *Risk/State:* `state_mutation: 84`, `unreferenced_by_name: 4`
* *Architecture:* `io: 14`, `api: 1`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 142.857
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `recursion.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 122.8 | **LOC:** 229 | **CtrlFlow:** 7.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (86.2773%), Tech Debt (30.2941%)
**Top Internal Functions/Classes:**
  * `MAIN-PROCEDURE` (Impact: 11.2)
  * `PRINT-CALL-STACK-PROCEDURE` (Impact: 4.8)
  * `FILE-CONTROL` (Impact: 4.0)
  * `IS-STACK-EMPTY-PROCEDURE` (Impact: 3.3)
  * `POP-CALL-STACK-PROCEDURE` (Impact: 2.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 74
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 32`, `args: 16`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `state_mutation: 56`, `unreferenced_by_name: 3`
* *Architecture:* `io: 15`, `api: 1`
* *Defense:* `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 142.857
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lisp.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 121.56 | **LOC:** 193 | **CtrlFlow:** 17.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (92.4269%), Tech Debt (26.6607%)
**Top Internal Functions/Classes:**
  * `MAIN-PROCEDURE` (Impact: 11.2)
  * `EVALUATE-CURRENT-COMMAND` (Impact: 7.5)
  * `EVALUATE-CURRENT-VALUES` (Impact: 7.0)
  * `INIT-RECURSION-OBJECT-PROCEDURE` (Impact: 3.9)
  * `APPLY-VALUE-TO-EXPRESSION` (Impact: 2.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 17 instances
* *State Mutation (weighted view):* 69
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 42`, `args: 15`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `state_mutation: 35`, `unreferenced_by_name: 2`
* *Architecture:* `api: 1`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 142.857
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cisp.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 28.74 | **LOC:** 79 | **CtrlFlow:** 3.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.733%), Tech Debt (82.2336%)
**Top Internal Functions/Classes:**
  * `FILE-CONTROL` (Impact: 4.5)
  * `READ-CMD-LINE-PROCEDURE` (Impact: 1.5)
  * `MAIN-PROCEDURE` (Impact: 1.4)
  * `TOKENIZE-LISP-PROCEDURE` (Impact: 1.4)
  * `EVALUTE-LISP-PROCEDURE` (Impact: 1.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 15`, `args: 14`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 15`, `unreferenced_by_name: 2`
* *Architecture:* `io: 4`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 142.857
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `logger.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 28.6 | **LOC:** 62 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (54.8333%), Tech Debt (88.5488%)
**Top Internal Functions/Classes:**
  * `MAIN-PROCEDURE` (Impact: 6.5)
  * `FILE-CONTROL` (Impact: 1.9)
  * `LOG-INIT-PROCEDURE` (Impact: 1.4)
  * `LOG-CLOSE-PROCEDURE` (Impact: 1.4)
  * `LOG-WRITE-TO-PROCEDURE` (Impact: 1.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 13
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 14`, `args: 2`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 11`, `unreferenced_by_name: 2`
* *Architecture:* `io: 8`, `api: 1`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 142.857
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cisp-error.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 21.88 | **LOC:** 68 | **CtrlFlow:** 7.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (20.256%), Tech Debt (56.9001%)
**Top Internal Functions/Classes:**
  * `MAIN-PROCEDURE` (Impact: 3.2)
  * `THROW-ERROR-PROCEDURE` (Impact: 2.5)
  * `CLOSE-OPEN-FILES-PROCEDURE` (Impact: 2.5)
  * `WS-LOG-RECORD-FUNCTION-NAME` (Impact: 1.4)
  * `LOG-ERROR-PROCEDURE` (Impact: 1.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Rce:* 1 instances
* *Amplified Cascading Flux:* 1 instances
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 14`, `args: 8`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 7`, `unreferenced_by_name: 1`
* *Architecture:* `io: 2`, `api: 1`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 142.857
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bin/cisp.bat` (BATCH | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 15.3 | **LOC:** 16 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 142.857
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

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `cisp-error.cbl` -> **Severity: 7142.85** (Blast Radius: 142.857 * Doc Risk: 50.0%)
- `cisp.cbl` -> **Severity: 7142.85** (Blast Radius: 142.857 * Doc Risk: 50.0%)
- `lisp.cbl` -> **Severity: 7142.85** (Blast Radius: 142.857 * Doc Risk: 50.0%)
- `logger.cbl` -> **Severity: 7142.85** (Blast Radius: 142.857 * Doc Risk: 50.0%)
- `recursion.cbl` -> **Severity: 7142.85** (Blast Radius: 142.857 * Doc Risk: 50.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
