# ARCHITECTURAL_BRIEF: cobol-programming-course
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/openmainframeproject/cobol-programming-course.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 121 analyzed artifact(s), 3844 LOC.
- **Load-bearing artifact:** `CONTRIBUTING.md` -- 3 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `COBOL Programming Course #3 - Advanced Topics/Labs/jclproc/DB2CBL.jcl` -- pulls in 10 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `COBOL Programming Course #2 - Learning COBOL/COBOL Programming Course #2 - Learning COBOL.md` at magnitude 75.72 (structural weight, not risk).
- **How to read this brief:** section 11 ranks artifacts by structural magnitude with a blast-radius line each; section 7 has the full dependency graph. The surface vectors in section 6 describe what is present in a file, not the probability of a defect -- Appendix A has the equations and the validation record behind that distinction.

## 1.5 SYSTEM ROLE & PHILOSOPHY
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
> *(Section 2, the structural-surface lexicon and its equations, is now **Appendix A** at the end of this brief -- the findings come first.)*

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 360 |
| Analyzed Artifacts (Scanned) | 121 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 239 |
| Total LOC | 3844 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 33.6% |
| Dominant Lang | COBOL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.335 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2855 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.2857 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 3 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| MARKDOWN | 43 | 0 | 35.5% |
| JCL | 43 | 680 | 35.5% |
| COBOL | 32 | 2770 | 26.4% |
| JSON | 2 | 384 | 1.7% |
| CSV | 1 | 10 | 0.8% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Small Flat Repo`
> **Architectural Drift Z-Score:** `2.372`
> **Composition Archetype:** `Small Flat Repo` (z +2.37; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 45%, Interface Declarations Files 29%, Large Core Modules 17%, Declarative / Non-Code 4%, Large Core Modules (2) 2%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 78 | 64.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 43 | 35.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 239*

**Composition by Extension & Reason:**
- `.png`: 219x Excluded (Explicitly Denied Extension: '.png')
- `.jpg`: 5x Excluded (Explicitly Denied Extension: '.jpg')
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Binary Format Detected)
- `.tex`: 4x Excluded (Unsupported Extension: '.tex')
- `.yml`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.gif`: 2x Excluded (Explicitly Denied Extension: '.gif')
- `.md`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.xlsx`: 1x Excluded (Explicitly Denied Extension: '.xlsx')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 65.6 | 9.0 | 3.9 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 95.8 | 36.8 | 31.3 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 22.9 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 2.5 | 2.3 | 2.4 | 2.4 |
| Connectivity (formerly API Exposure) | 0.0 | 3.5 | 0.3 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 32.3 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 7.9 | 0.4 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 88.5 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1 | 1 | 0 | `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0014.cobol` |
| cleanup | 47 | 25 | 2 | `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB22.cbl` |
| guards | 20 | 5 | 0 | `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB22.cbl` |
| danger | 57 | 39 | 1 | `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB22.cbl` |
| concurrency | 7 | 4 | 0 | `COBOL Programming Course #2 - Learning COBOL/Labs/jclproc/IGYWCL.jcl` |
| connectivity | 6 | 6 | 0 | `COBOL Programming Course #2 - Learning COBOL/Labs/jclproc/IGYWC.jcl` |
| io | 600 | 57 | 19 | `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0033.cobol` |
| crypto | 0 | 0 | 0 | - |
| ipc | 35 | 4 | 0 | `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB22.cbl` |
| time | 53 | 14 | 3 | `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0004.cobol` |
| serialization | 0 | 0 | 0 | - |
| regex | 1 | 1 | 0 | `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/ADDAMT.cobol` |
| events | 3 | 3 | 0 | `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB21.cbl` |
| tests | 0 | 0 | 0 | - |
| docs | 0 | 0 | 0 | - |
| debt | 52 | 15 | 1 | `COBOL Programming Course #4 - Testing/Labs/cbl/DEPTPAY.CBL` |
| mutation | 738 | 65 | 18 | `COBOL Programming Course #3 - Advanced Topics/Labs/jclproc/DB2CBL.jcl` |
| dead_code | 94 | 24 | 4 | `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0033.cobol` |
| credential | 0 | 0 | 0 | - |
| threat | 32 | 4 | 0 | `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB22.cbl` |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0033.cobol` (Hits: 28)
- `COBOL Programming Course #3 - Advanced Topics/Challenges/Debugging/cbl/CBL0106.cbl` (Hits: 23)
- `COBOL Programming Course #3 - Advanced Topics/Challenges/Debugging/cbl/CBL0106C.cbl` (Hits: 23)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **CONTRIBUTING.md** (`CONTRIBUTING.md`) — 3 inbound connections
2. **DBRMLIB.jcl** (`COBOL Programming Course #3 - Advanced Topics/Labs/jcl/DBRMLIB.jcl`) — 2 inbound connections
3. **COMMITTERS.csv** (`COMMITTERS.csv`) — 2 inbound connections
4. **CODE_OF_CONDUCT.md** (`CODE_OF_CONDUCT.md`) — 1 inbound connections
5. **GOVERNANCE.md** (`GOVERNANCE.md`) — 1 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **DB2CBL.jcl** (`COBOL Programming Course #3 - Advanced Topics/Labs/jclproc/DB2CBL.jcl`) — 10 outbound dependencies
2. **README.md** (`README.md`) — 7 outbound dependencies
3. **IGYWCL.jcl** (`COBOL Programming Course #2 - Learning COBOL/Labs/jclproc/IGYWCL.jcl`) — 7 outbound dependencies
4. **IGYWCLG.jcl** (`COBOL Programming Course #2 - Learning COBOL/Labs/jclproc/IGYWCLG.jcl`) — 7 outbound dependencies
5. **DB2SETUP.jcl** (`COBOL Programming Course #3 - Advanced Topics/Labs/jcl/DB2SETUP.jcl`) — 5 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `LIST-ALL` **(Defensive Guards)** (@ `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB21.cbl`) -> Impact: **6.0** | LOC: 19
  * *Intent:* ***************************************************** * LIST ALL CLIENTS * *****************************************************...
- `GET-ALL` **(Defensive Guards)** (@ `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB22.cbl`) -> Impact: **6.0** | LOC: 19
  * *Intent:* *
- `GET-SPECIFIC` **(Defensive Guards)** (@ `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB22.cbl`) -> Impact: **6.0** | LOC: 19
  * *Intent:* *
- `GET-ALL` **(Defensive Guards)** (@ `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB23.cbl`) -> Impact: **6.0** | LOC: 19
- `GET-SPECIFIC` **(Defensive Guards)** (@ `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB23.cbl`) -> Impact: **6.0** | LOC: 19
- `PAYMENT-WEEKLY` **(I/O & Config Routines)** (@ `COBOL Programming Course #4 - Testing/Labs/cbl/EMPPAY.CBL`) -> Impact: **5.5** | LOC: 10
- `SQL-ERROR-HANDLING` **(Defensive Guards)** (@ `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB21.cbl`) -> Impact: **4.7** | LOC: 13
- `SQL-ERROR-HANDLING` **(Defensive Guards)** (@ `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB22.cbl`) -> Impact: **4.7** | LOC: 13
- `SQL-ERROR-HANDLING` **(Defensive Guards)** (@ `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB23.cbl`) -> Impact: **4.7** | LOC: 13
- `COBOL` **(Compute Cores)** (@ `COBOL Programming Course #3 - Advanced Topics/Labs/jclproc/DB2CBL.jcl`) -> Impact: **4.4** | LOC: 32
  * *Intent:* //DB2CBL PROC MBR='DB2CBL' //******************************************************************** //* Copyright Contributors to the COBOL Programming ...

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **I/O & Config Routines**: dominated by I/O and configuration handling

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `COBOL Programming Course #2 - Learning COBOL/Labs/cbl` | 23 | 544.54 | 12.44% | 68.32% |
| `COBOL Programming Course #3 - Advanced Topics/Labs/cbl` | 3 | 166.1 | 59.37% | 34.54% |
| `COBOL Programming Course #3 - Advanced Topics/Challenges/Debugging/cbl` | 2 | 122.96 | 29.11% | 56.09% |
| `COBOL Programming Course #2 - Learning COBOL/Labs/jcl` | 23 | 106.7 | 3.39% | 0.0% |
| `COBOL Programming Course #2 - Learning COBOL` | 2 | 76.72 | 0.0% | 0.0% |
| `__monolith__` | 15 | 65.28 | 0.0% | 0.0% |
| `COBOL Programming Course #4 - Testing/Labs/cbl` | 2 | 47.98 | 30.78% | 0.0% |
| `COBOL Programming Course #4 - Testing/Labs/tests` | 2 | 42.62 | 6.72% | 0.0% |
| `COBOL Programming Course #3 - Advanced Topics` | 2 | 27.72 | 0.0% | 0.0% |
| `COBOL Programming Course #3 - Advanced Topics/Labs/jcl` | 11 | 24.92 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0033.cobol` -> **99.9887%** Exposure
- `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/SRCHSER.cobol` -> **99.7504%** Exposure
- `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/SRCHBIN.cobol` -> **99.708%** Exposure
- `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0001.cobol` -> **96.2229%** Exposure
- `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0002.cobol` -> **96.2229%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `COBOL Programming Course #4 - Testing/Labs/cbl/EMPPAY.CBL` -> **100.0%** Exposure
- `COBOL Programming Course #3 - Advanced Topics/Challenges/Debugging/cbl/CBL0106.cbl` -> **99.9318%** Exposure
- `COBOL Programming Course #3 - Advanced Topics/Challenges/Debugging/cbl/CBL0106C.cbl` -> **99.924%** Exposure
- `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB22.cbl` -> **99.7546%** Exposure
- `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB23.cbl` -> **99.6123%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0033.cobol` -> **9** Orphaned Functions | **0** Duplicates
- `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0008.cobol` -> **5** Orphaned Functions | **0** Duplicates
- `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0009.cobol` -> **5** Orphaned Functions | **0** Duplicates
- `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0010.cobol` -> **5** Orphaned Functions | **0** Duplicates
- `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0011.cobol` -> **5** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `98` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `COBOL Programming Course #2 - Learning COBOL/COBOL Programming Course #2 - Learning COBOL.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 75.72 | **LOC:** 3786 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.825
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB22.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 66.34 | **LOC:** 202 | **CtrlFlow:** 10.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Guard Balance (formerly Safety Score) (72.8%), Complexity Load (formerly Cognitive Load) (65.6%), Debt Markers (formerly Tech Debt) (28.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `GET-ALL` **(Defensive Guards)** (Impact: 6.0)
    * *Intent:* *
  * `GET-SPECIFIC` **(Defensive Guards)** (Impact: 6.0)
    * *Intent:* *
  * `SQL-ERROR-HANDLING` **(Defensive Guards)** (Impact: 4.7)
  * `PROCESS-INPUT` **(I/O & Config Routines)** (Impact: 4.3)
    * *Intent:* *
  * `PROG-START` **(I/O & Config Routines)** (Impact: 3.4)
    * *Intent:* *------------------
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 9 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 33
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 27`, `args: 3`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 15`, `unreferenced_by_name: 2`
* *Architecture:* `io: 22`
* *Defense:* `safety: 7`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.825
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB23.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 64.22 | **LOC:** 189 | **CtrlFlow:** 10.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Guard Balance (formerly Safety Score) (71.5%), Complexity Load (formerly Cognitive Load) (63.7%), Debt Markers (formerly Tech Debt) (29.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `GET-ALL` **(Defensive Guards)** (Impact: 6.0)
  * `GET-SPECIFIC` **(Defensive Guards)** (Impact: 6.0)
  * `SQL-ERROR-HANDLING` **(Defensive Guards)** (Impact: 4.7)
  * `PROCESS-INPUT` **(I/O & Config Routines)** (Impact: 4.3)
  * `PROG-START` **(I/O & Config Routines)** (Impact: 3.4)
    * *Intent:* *------------------
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 9 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 31
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 27`, `args: 3`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 13`, `unreferenced_by_name: 2`
* *Architecture:* `io: 22`
* *Defense:* `safety: 7`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.825
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #3 - Advanced Topics/Challenges/Debugging/cbl/CBL0106C.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 62.74 | **LOC:** 205 | **CtrlFlow:** 4.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (84.1%), Debt Markers (formerly Tech Debt) (54.9%), Complexity Load (formerly Cognitive Load) (29.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `IS-OVERLIMIT` **(I/O & Config Routines)** (Impact: 3.8)
    * *Intent:* *
  * `WRITE-OVERLIMIT` **(I/O & Config Routines)** (Impact: 3.5)
    * *Intent:* *
  * `READ-NEXT-RECORD` **(Interface Declarations)** (Impact: 2.5)
    * *Intent:* *
  * `READ-RECORD` **(I/O & Config Routines)** (Impact: 2.2)
    * *Intent:* *
  * `IS-STATE-VIRGINIA` **(I/O & Config Routines)** (Impact: 2.2)
    * *Intent:* *
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 40
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 18`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 24`, `unreferenced_by_name: 4`
* *Architecture:* `io: 23`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.825
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #3 - Advanced Topics/Challenges/Debugging/cbl/CBL0106.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 60.22 | **LOC:** 196 | **CtrlFlow:** 4.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (80.6%), Debt Markers (formerly Tech Debt) (57.3%), Complexity Load (formerly Cognitive Load) (29.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `WRITE-OVERLIMIT` **(I/O & Config Routines)** (Impact: 3.5)
    * *Intent:* *
  * `READ-NEXT-RECORD` **(Interface Declarations)** (Impact: 2.5)
    * *Intent:* *
  * `IS-OVERLIMIT` **(I/O & Config Routines)** (Impact: 2.4)
    * *Intent:* *
  * `READ-RECORD` **(I/O & Config Routines)** (Impact: 2.2)
    * *Intent:* *
  * `IS-STATE-VIRGINIA` **(I/O & Config Routines)** (Impact: 2.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 39
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 16`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `state_mutation: 23`, `unreferenced_by_name: 4`
* *Architecture:* `io: 23`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.825
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #4 - Testing/Labs/cbl/EMPPAY.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 37.52 | **LOC:** 55 | **CtrlFlow:** 11.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.8%), Complexity Load (formerly Cognitive Load) (61.6%), Test Surface (formerly Verification) (2.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `PAYMENT-WEEKLY` **(I/O & Config Routines)** (Impact: 5.5)
  * `PAYMENT-MONTHLY` **(I/O & Config Routines)** (Impact: 3.4)
  * `SHOW-OUTPUT` **(Interface Declarations)** (Impact: 1.4)
  * `INITIALIZATION` **(I/O & Config Routines)** (Impact: 1.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 25
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 16`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 11`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.825
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB21.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 35.54 | **LOC:** 145 | **CtrlFlow:** 7.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.7%), Guard Balance (formerly Safety Score) (69.1%), Complexity Load (formerly Cognitive Load) (48.8%), Debt Markers (formerly Tech Debt) (45.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `LIST-ALL` **(Defensive Guards)** (Impact: 6.0)
    * *Intent:* ***************************************************** * LIST ALL CLIENTS * *************************...
  * `SQL-ERROR-HANDLING` **(Defensive Guards)** (Impact: 4.7)
  * `PRINT-A-LINE` **(I/O & Config Routines)** (Impact: 1.4)
  * `PROG-START` **(Interface Declarations)** (Impact: 1.1)
    * *Intent:* *------------------ ***************************************************** * MAIN PROGRAM ROUTINE * *...
  * `PROG-END` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 4 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 20`, `args: 3`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 10`, `unreferenced_by_name: 2`
* *Architecture:* `io: 12`
* *Defense:* `safety: 4`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.825
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0033.cobol` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 35.24 | **LOC:** 131 | **CtrlFlow:** 4.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Mutation Surface (formerly State Flux) (88.0%), Guard Balance (formerly Safety Score) (71.9%), Complexity Load (formerly Cognitive Load) (18.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `2300-READ-NEXT-RECORDS` **(Interface Declarations)** (Impact: 3.2)
    * *Intent:* *THRU or THROUGH list the start and end of which *paragraphs will be executed in a sequential order ...
  * `2100-READ-TEN-RECORDS` **(Interface Declarations)** (Impact: 2.2)
    * *Intent:* *notice that because of GO TO, this command will *never be executed *
  * `4000-READ-RECORD` **(I/O & Config Routines)** (Impact: 2.2)
    * *Intent:* *
  * `5000-WRITE-RECORD` **(I/O & Config Routines)** (Impact: 1.4)
    * *Intent:* *
  * `2000-READ-FIRST-RECORD` **(Interface Declarations)** (Impact: 1.2)
    * *Intent:* *The prefix "1000" is increased thoughout the code and *is used as a programming technique to better...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 19`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 7`, `unreferenced_by_name: 9`
* *Architecture:* `io: 28`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.825
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0011.cobol` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 33.06 | **LOC:** 174 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (93.3%), Debt Markers (formerly Tech Debt) (79.3%), Guard Balance (formerly Safety Score) (69.2%), Complexity Load (formerly Cognitive Load) (17.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `READ-NEXT-RECORD` **(Interface Declarations)** (Impact: 2.4)
    * *Intent:* *
  * `READ-RECORD` **(I/O & Config Routines)** (Impact: 2.2)
    * *Intent:* *
  * `WRITE-HEADERS` **(I/O & Config Routines)** (Impact: 1.5)
    * *Intent:* *
  * `WRITE-RECORD` **(I/O & Config Routines)** (Impact: 1.4)
    * *Intent:* *
  * `WRITE-TLIMIT-TBALANCE` **(I/O & Config Routines)** (Impact: 1.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 14`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 16`, `dead_code: 1`, `unreferenced_by_name: 5`
* *Architecture:* `io: 21`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.825
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0012.cobol` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 32.96 | **LOC:** 169 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (94.4%), Debt Markers (formerly Tech Debt) (81.5%), Guard Balance (formerly Safety Score) (69.8%), Complexity Load (formerly Cognitive Load) (18.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `READ-NEXT-RECORD` **(Interface Declarations)** (Impact: 2.4)
    * *Intent:* *
  * `READ-RECORD` **(I/O & Config Routines)** (Impact: 2.2)
    * *Intent:* *
  * `WRITE-HEADERS` **(I/O & Config Routines)** (Impact: 1.5)
    * *Intent:* *
  * `WRITE-RECORD` **(I/O & Config Routines)** (Impact: 1.4)
    * *Intent:* *
  * `WRITE-TLIMIT-TBALANCE` **(I/O & Config Routines)** (Impact: 1.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 14`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 16`, `dead_code: 1`, `unreferenced_by_name: 5`
* *Architecture:* `io: 21`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.825
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0008.cobol` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 31.92 | **LOC:** 195 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (91.9%), Debt Markers (formerly Tech Debt) (80.2%), Guard Balance (formerly Safety Score) (68.6%), Complexity Load (formerly Cognitive Load) (16.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `READ-NEXT-RECORD` **(Interface Declarations)** (Impact: 2.4)
    * *Intent:* *
  * `READ-RECORD` **(I/O & Config Routines)** (Impact: 2.2)
    * *Intent:* *
  * `WRITE-HEADERS` **(I/O & Config Routines)** (Impact: 1.5)
    * *Intent:* *
  * `WRITE-RECORD` **(I/O & Config Routines)** (Impact: 1.3)
    * *Intent:* * The COMPUTE verb assigns the value of the arithmetic * expression to the TLIMIT and TBALANCE data ...
  * `WRITE-TLIMIT-TBALANCE` **(I/O & Config Routines)** (Impact: 1.2)
    * *Intent:* *
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 17
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 14`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 15`, `unreferenced_by_name: 5`
* *Architecture:* `io: 21`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.825
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0009.cobol` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 31.92 | **LOC:** 195 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (91.9%), Debt Markers (formerly Tech Debt) (80.2%), Guard Balance (formerly Safety Score) (68.6%), Complexity Load (formerly Cognitive Load) (16.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `READ-NEXT-RECORD` **(Interface Declarations)** (Impact: 2.4)
    * *Intent:* *
  * `READ-RECORD` **(I/O & Config Routines)** (Impact: 2.2)
    * *Intent:* *
  * `WRITE-HEADERS` **(I/O & Config Routines)** (Impact: 1.5)
    * *Intent:* *
  * `WRITE-RECORD` **(I/O & Config Routines)** (Impact: 1.3)
    * *Intent:* * The COMPUTE verb assigns the value of the arithmetic * expression to the TLIMIT and TBALANCE data ...
  * `WRITE-TLIMIT-TBALANCE` **(I/O & Config Routines)** (Impact: 1.2)
    * *Intent:* *
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 17
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 14`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 15`, `unreferenced_by_name: 5`
* *Architecture:* `io: 21`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.825
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0010.cobol` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 31.92 | **LOC:** 184 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (91.9%), Debt Markers (formerly Tech Debt) (80.2%), Guard Balance (formerly Safety Score) (68.6%), Complexity Load (formerly Cognitive Load) (16.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `READ-NEXT-RECORD` **(Interface Declarations)** (Impact: 2.4)
    * *Intent:* *
  * `READ-RECORD` **(I/O & Config Routines)** (Impact: 2.2)
    * *Intent:* *
  * `WRITE-HEADERS` **(I/O & Config Routines)** (Impact: 1.5)
    * *Intent:* *
  * `WRITE-RECORD` **(I/O & Config Routines)** (Impact: 1.3)
    * *Intent:* *
  * `WRITE-TLIMIT-TBALANCE` **(I/O & Config Routines)** (Impact: 1.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 17
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 14`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 15`, `unreferenced_by_name: 5`
* *Architecture:* `io: 21`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.825
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL006A.cobol` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 30.5 | **LOC:** 173 | **CtrlFlow:** 2.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (93.8%), Debt Markers (formerly Tech Debt) (75.0%), Guard Balance (formerly Safety Score) (69.6%), Complexity Load (formerly Cognitive Load) (13.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `READ-NEXT-RECORD` **(Interface Declarations)** (Impact: 2.5)
    * *Intent:* *
  * `READ-RECORD` **(I/O & Config Routines)** (Impact: 2.2)
    * *Intent:* *
  * `IS-STATE-NEWYORK` **(I/O & Config Routines)** (Impact: 2.2)
    * *Intent:* * * CHANGE 3: Updated paragraph name and logic to check for New York * Original paragraph: IS-STATE-...
  * `WRITE-HEADERS` **(I/O & Config Routines)** (Impact: 1.5)
    * *Intent:* *
  * `WRITE-RECORD` **(I/O & Config Routines)** (Impact: 1.3)
    * *Intent:* * Boolean logic -- when the conditional expression * USA-STATE = 'New York' is true, the program * c...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 14`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 12`, `unreferenced_by_name: 4`
* *Architecture:* `io: 19`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.825
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBLC1.cobol` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 30.5 | **LOC:** 171 | **CtrlFlow:** 2.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (93.8%), Debt Markers (formerly Tech Debt) (75.0%), Guard Balance (formerly Safety Score) (69.6%), Complexity Load (formerly Cognitive Load) (13.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `READ-NEXT-RECORD` **(Interface Declarations)** (Impact: 2.5)
    * *Intent:* *
  * `READ-RECORD` **(I/O & Config Routines)** (Impact: 2.2)
    * *Intent:* *
  * `IS-STATE-NEWYORK` **(I/O & Config Routines)** (Impact: 2.2)
    * *Intent:* * * CHANGE 3: Updated paragraph name and logic to check for New York * Original paragraph: IS-STATE-...
  * `WRITE-HEADERS` **(I/O & Config Routines)** (Impact: 1.5)
    * *Intent:* *
  * `WRITE-RECORD` **(I/O & Config Routines)** (Impact: 1.3)
    * *Intent:* * Boolean logic -- when the conditional expression * USA-STATE = 'New York' is true, the program * c...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 14`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 12`, `unreferenced_by_name: 4`
* *Architecture:* `io: 19`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.825
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0006.cobol` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 30.4 | **LOC:** 164 | **CtrlFlow:** 2.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (93.8%), Debt Markers (formerly Tech Debt) (75.0%), Guard Balance (formerly Safety Score) (69.6%), Complexity Load (formerly Cognitive Load) (13.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `READ-NEXT-RECORD` **(Interface Declarations)** (Impact: 2.4)
    * *Intent:* *
  * `READ-RECORD` **(I/O & Config Routines)** (Impact: 2.2)
    * *Intent:* *
  * `IS-STATE-VIRGINIA` **(I/O & Config Routines)** (Impact: 2.2)
    * *Intent:* *
  * `WRITE-HEADERS` **(I/O & Config Routines)** (Impact: 1.5)
    * *Intent:* *
  * `WRITE-RECORD` **(I/O & Config Routines)** (Impact: 1.3)
    * *Intent:* * Boolean logic -- when the conditional expression * USA-STATE = 'Virginia' is true, the program * c...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 14`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 12`, `unreferenced_by_name: 4`
* *Architecture:* `io: 19`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.825
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0007.cobol` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 30.3 | **LOC:** 160 | **CtrlFlow:** 2.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (93.8%), Debt Markers (formerly Tech Debt) (75.0%), Guard Balance (formerly Safety Score) (69.6%), Complexity Load (formerly Cognitive Load) (13.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `READ-NEXT-RECORD` **(Interface Declarations)** (Impact: 2.4)
    * *Intent:* *
  * `READ-RECORD` **(I/O & Config Routines)** (Impact: 2.2)
    * *Intent:* *
  * `IS-STATE-VIRGINIA` **(I/O & Config Routines)** (Impact: 2.1)
    * *Intent:* *
  * `WRITE-HEADERS` **(I/O & Config Routines)** (Impact: 1.5)
    * *Intent:* *
  * `WRITE-RECORD` **(I/O & Config Routines)** (Impact: 1.3)
    * *Intent:* * When the current value of USA-STATE equals 'Virginia' * the conditional data-name STATE is TRUE. *...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 14`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 12`, `unreferenced_by_name: 4`
* *Architecture:* `io: 19`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.825
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #4 - Testing/Labs/tests/emppay.cut` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 27.42 | **LOC:** 25 | **CtrlFlow:** 4.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (79.8%), Complexity Load (formerly Cognitive Load) (13.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 4`
* *Risk/State:* `state_mutation: 8`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.825
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #3 - Advanced Topics/COBOL Programming Course #3 - Advanced Topics.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 26.72 | **LOC:** 1336 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.825
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0004.cobol` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 26.3 | **LOC:** 164 | **CtrlFlow:** 1.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (89.3%), Debt Markers (formerly Tech Debt) (80.4%), Guard Balance (formerly Safety Score) (68.0%), Complexity Load (formerly Cognitive Load) (15.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `READ-NEXT-RECORD` **(I/O & Config Routines)** (Impact: 2.6)
    * *Intent:* *
  * `READ-RECORD` **(I/O & Config Routines)** (Impact: 2.2)
    * *Intent:* *
  * `WRITE-HEADERS` **(I/O & Config Routines)** (Impact: 1.5)
    * *Intent:* *OPEN-FILES-END -- consists of an empty paragraph suffixed by *-END that ends the past one and serve...
  * `WRITE-RECORD` **(I/O & Config Routines)** (Impact: 1.3)
    * *Intent:* *
  * `CLOSE-STOP` **(Interface Declarations)** (Impact: 1.2)
    * *Intent:* *
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 13
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 13`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 11`, `dead_code: 1`, `unreferenced_by_name: 4`
* *Architecture:* `io: 19`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.825
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0005.cobol` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 26.3 | **LOC:** 164 | **CtrlFlow:** 1.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (89.3%), Debt Markers (formerly Tech Debt) (80.4%), Guard Balance (formerly Safety Score) (68.0%), Complexity Load (formerly Cognitive Load) (15.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `READ-NEXT-RECORD` **(I/O & Config Routines)** (Impact: 2.6)
    * *Intent:* *
  * `READ-RECORD` **(I/O & Config Routines)** (Impact: 2.2)
    * *Intent:* *
  * `WRITE-HEADERS` **(I/O & Config Routines)** (Impact: 1.5)
    * *Intent:* *OPEN-FILES-END -- consists of an empty paragraph suffixed by *-END that ends the past one and serve...
  * `WRITE-RECORD` **(I/O & Config Routines)** (Impact: 1.3)
    * *Intent:* *
  * `CLOSE-STOP` **(Interface Declarations)** (Impact: 1.2)
    * *Intent:* *
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 13
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 13`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 11`, `dead_code: 1`, `unreferenced_by_name: 4`
* *Architecture:* `io: 19`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.825
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #4 - Testing/COBOL Programming Course #4 - Testing.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 23.44 | **LOC:** 1172 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.825
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/SRCHSER.cobol` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 22.16 | **LOC:** 73 | **CtrlFlow:** 13.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.8%), Mutation Surface (formerly State Flux) (98.8%), Guard Balance (formerly Safety Score) (74.4%), Complexity Load (formerly Cognitive Load) (24.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SEARCH-RECORD` **(Compute Cores)** (Impact: 4.3)
    * *Intent:* *
  * `LOAD-TABLES` **(Interface Declarations)** (Impact: 3.4)
    * *Intent:* *
  * `READ-RECORD` **(I/O & Config Routines)** (Impact: 2.2)
    * *Intent:* *
  * `OPEN-FILES` **(I/O & Config Routines)** (Impact: 1.1)
    * *Intent:* *------------------
  * `CLOSE-STOP` **(Interface Declarations)** (Impact: 1.1)
    * *Intent:* *
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 14`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 3`, `unreferenced_by_name: 4`
* *Architecture:* `io: 7`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.825
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `zowe.schema.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 22.0 | **LOC:** 350 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.825
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/PAYROL00.cobol` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 21.5 | **LOC:** 61 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (91.7%), Guard Balance (formerly Safety Score) (70.2%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 12`, `class_start: 1`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.825
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `COBOL Programming Course #3 - Advanced Topics/Labs/jcl/DBRMLIB.jcl` -> **Severity: 2112.6** (Blast Radius: 21.126 * Doc Risk: 100.0%)
- `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/ADDAMT.cobol` -> **Severity: 782.5** (Blast Radius: 7.825 * Doc Risk: 100.0%)
- `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0001.cobol` -> **Severity: 782.5** (Blast Radius: 7.825 * Doc Risk: 100.0%)
- `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0002.cobol` -> **Severity: 782.5** (Blast Radius: 7.825 * Doc Risk: 100.0%)
- `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0004.cobol` -> **Severity: 782.5** (Blast Radius: 7.825 * Doc Risk: 100.0%)

## APPENDIX A. STRUCTURAL SURFACE LEXICON (EQUATIONS & CONTEXT)
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

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with high Structural Magnitude combined with a wide Blast Radius, severe Z-Scores (Architectural Drift), or extreme spikes in individual surface vectors (like Mutation Surface or Complexity Load). Do NOT sum the surface vectors together or treat any total of them as a score -- they are independently scaled meters in different units (#3112). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
