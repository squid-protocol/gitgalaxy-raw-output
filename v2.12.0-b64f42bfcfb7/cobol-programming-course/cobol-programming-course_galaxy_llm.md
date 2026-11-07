# ARCHITECTURAL_BRIEF: cobol-programming-course
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/openmainframeproject/cobol-programming-course.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |
| **Archetype Brains** | trained against engine v2.9.1 (44ffeb1e, 2026-09-19); last measured at engine 49cba5db on language-crucible@v1.7.0 |
| **Function archetypes** | **VALIDATED**, 98.4% agreement with trained state |
| **File archetypes** | **VALIDATED**, 98.7% agreement with trained state |
| **Composition (file)** | **DEGRADED**, 97.4% agreement with trained state -- engine changes since training relabelled 2.6% of crucible files (agreement 97.4%); composition_file inputs disagree with the function model's labels: never read ['Annotated & Test Methods', 'Stateful Encapsulated Methods'], never emitted ['Annotated Framework Methods', 'Tests & Verification'] -- those units drop out and those input columns are always 0.0 (retrain tracked in #4111) |
| **Composition (repo)** | **INVALID**, labels withheld -- not measurable on one corpus; inherits composition_file's measured state; composition_repo reads the composition_file brain labels by name, but none of its 20 inputs (e.g. 'Static: Literature & Documentation') is a label the composition_file brain emits (e.g. 'Annotated Framework Methods Files') -- every input column is 0.0 (retrain tracked in #4111) |

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 125 analyzed artifact(s), 3934 LOC.
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
| Analyzed Artifacts (Scanned) | 125 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 235 |
| Total LOC | 3934 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 34.7% |
| Dominant Lang | COBOL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.9277 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.3007 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.119 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 5 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| MARKDOWN | 44 | 0 | 35.2% |
| JCL | 43 | 680 | 34.4% |
| COBOL | 32 | 2770 | 25.6% |
| YAML | 3 | 90 | 2.4% |
| JSON | 2 | 384 | 1.6% |
| CSV | 1 | 10 | 0.8% |

## 4.1 SOURCE ENCODINGS
All 125 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 47%, Interface Declarations Files 29%, Large Core Modules 18%, Declarative / Non-Code 2%, Large Core Modules (2) 2%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 81 | 64.8% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 44 | 35.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 235*

**Composition by Extension & Reason:**
- `.png`: 219x Excluded (Explicitly Denied Extension: '.png')
- `.jpg`: 5x Excluded (Explicitly Denied Extension: '.jpg')
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Binary Format Detected)
- `.tex`: 4x Excluded (Unsupported Extension: '.tex')
- `.gif`: 2x Excluded (Explicitly Denied Extension: '.gif')
- `.xlsx`: 1x Excluded (Explicitly Denied Extension: '.xlsx')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 65.6 | 8.7 | 3.9 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 71.7 | 27.1 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 15.7 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 2.5 | 2.3 | 2.4 | 2.4 |
| Connectivity (formerly API Exposure) | 0.0 | 3.5 | 0.3 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 31.1 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 7.8 | 0.2 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 90.1 | 100.0 | 100.0 |
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
| io | 418 | 57 | 10 | `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB22.cbl` |
| crypto | 0 | 0 | 0 | - |
| ipc | 35 | 4 | 0 | `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB22.cbl` |
| time | 14 | 13 | 1 | `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/COBOL.cobol` |
| serialization | 0 | 0 | 0 | - |
| regex | 1 | 1 | 0 | `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/ADDAMT.cobol` |
| events | 3 | 3 | 0 | `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB21.cbl` |
| tests | 0 | 0 | 0 | - |
| docs | 12 | 2 | 0 | `.github/ISSUE_TEMPLATE/bug_report.yml` |
| debt | 54 | 16 | 2 | `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/PAYROL00.cobol` |
| mutation | 738 | 65 | 18 | `COBOL Programming Course #3 - Advanced Topics/Labs/jclproc/DB2CBL.jcl` |
| dead_code | 75 | 21 | 3 | `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0033.cobol` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB22.cbl` (Hits: 21)
- `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB23.cbl` (Hits: 21)
- `COBOL Programming Course #3 - Advanced Topics/Labs/jclproc/DB2CBL.jcl` (Hits: 16)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **CONTRIBUTING.md** (`CONTRIBUTING.md`) — 3 inbound connections
2. **CBL0001.cobol** (`COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0001.cobol`) — 2 inbound connections
3. **DBRMLIB.jcl** (`COBOL Programming Course #3 - Advanced Topics/Labs/jcl/DBRMLIB.jcl`) — 2 inbound connections
4. **COMMITTERS.csv** (`COMMITTERS.csv`) — 2 inbound connections
5. **CODE_OF_CONDUCT.md** (`CODE_OF_CONDUCT.md`) — 1 inbound connections

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
| `COBOL Programming Course #2 - Learning COBOL/Labs/cbl` | 23 | 491.64 | 12.44% | 45.92% |
| `COBOL Programming Course #3 - Advanced Topics/Labs/cbl` | 3 | 164.1 | 59.37% | 14.73% |
| `COBOL Programming Course #3 - Advanced Topics/Challenges/Debugging/cbl` | 2 | 122.96 | 29.11% | 33.85% |
| `COBOL Programming Course #2 - Learning COBOL/Labs/jcl` | 23 | 106.7 | 3.39% | 0.0% |
| `COBOL Programming Course #2 - Learning COBOL` | 2 | 76.72 | 0.0% | 0.0% |
| `__monolith__` | 15 | 65.28 | 0.0% | 0.0% |
| `COBOL Programming Course #4 - Testing/Labs/cbl` | 2 | 50.48 | 30.78% | 0.0% |
| `.github/ISSUE_TEMPLATE` | 3 | 44.3 | 1.77% | 33.33% |
| `COBOL Programming Course #4 - Testing/Labs/tests` | 2 | 42.62 | 6.72% | 0.0% |
| `COBOL Programming Course #3 - Advanced Topics` | 2 | 27.72 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0033.cobol` -> **100.0%** Exposure
- `.github/ISSUE_TEMPLATE/bug_report.yml` -> **99.9925%** Exposure
- `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/SRCHSER.cobol` -> **95.9316%** Exposure
- `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/SRCHBIN.cobol` -> **95.5022%** Exposure
- `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0004.cobol` -> **72.6763%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `COBOL Programming Course #4 - Testing/Labs/cbl/EMPPAY.CBL` -> **100.0%** Exposure
- `COBOL Programming Course #3 - Advanced Topics/Challenges/Debugging/cbl/CBL0106.cbl` -> **99.9318%** Exposure
- `COBOL Programming Course #3 - Advanced Topics/Challenges/Debugging/cbl/CBL0106C.cbl` -> **99.924%** Exposure
- `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB22.cbl` -> **99.7546%** Exposure
- `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB23.cbl` -> **99.6123%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0033.cobol` -> **14** Orphaned Functions | **0** Duplicates
- `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0004.cobol` -> **4** Orphaned Functions | **0** Duplicates
- `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0005.cobol` -> **4** Orphaned Functions | **0** Duplicates
- `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0008.cobol` -> **4** Orphaned Functions | **0** Duplicates
- `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0009.cobol` -> **4** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `101` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `COBOL Programming Course #2 - Learning COBOL/COBOL Programming Course #2 - Learning COBOL.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 75.72 | **LOC:** 3786 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.432
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB22.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.38)
- **Top Global Matches:** file_cluster_12: 7.38, file_cluster_11: 8.045, file_cluster_15: 8.869
- **Magnitude:** 65.34 | **LOC:** 202 | **CtrlFlow:** 10.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 11.899; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Complexity Load (formerly Cognitive Load) (65.6%), Guard Balance (formerly Safety Score) (57.0%), Debt Markers (formerly Tech Debt) (13.4%)
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
* *Structure:* `branch: 17`, `structural_boundaries: 26`, `args: 3`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 15`, `unreferenced_by_name: 1`
* *Architecture:* `io: 21`, `import: 1`
* *Defense:* `safety: 7`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 11.899
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.008065
  * `Imports (Out-Degree: 0):` SQLCA
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB23.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.38)
- **Top Global Matches:** file_cluster_12: 7.38, file_cluster_11: 8.058, file_cluster_15: 8.882
- **Magnitude:** 63.22 | **LOC:** 189 | **CtrlFlow:** 10.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 11.899; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Complexity Load (formerly Cognitive Load) (63.7%), Guard Balance (formerly Safety Score) (56.5%), Debt Markers (formerly Tech Debt) (13.5%)
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
* *Structure:* `branch: 17`, `structural_boundaries: 26`, `args: 3`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 13`, `unreferenced_by_name: 1`
* *Architecture:* `io: 21`, `import: 1`
* *Defense:* `safety: 7`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 11.899
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.008065
  * `Imports (Out-Degree: 0):` SQLCA
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `COBOL Programming Course #3 - Advanced Topics/Challenges/Debugging/cbl/CBL0106C.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.683)
- **Top Global Matches:** file_cluster_11: 5.683, file_cluster_2: 5.89, file_cluster_15: 7.005
- **Magnitude:** 62.74 | **LOC:** 205 | **CtrlFlow:** 4.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (62.6%), Debt Markers (formerly Tech Debt) (33.1%), Complexity Load (formerly Cognitive Load) (29.1%)
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
* *Structure:* `branch: 8`, `structural_boundaries: 17`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 24`, `unreferenced_by_name: 3`
* *Architecture:* `io: 12`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.432
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #3 - Advanced Topics/Challenges/Debugging/cbl/CBL0106.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.674)
- **Top Global Matches:** file_cluster_11: 5.674, file_cluster_2: 5.861, file_cluster_15: 6.992
- **Magnitude:** 60.22 | **LOC:** 196 | **CtrlFlow:** 4.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 11.899; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (60.6%), Debt Markers (formerly Tech Debt) (34.6%), Complexity Load (formerly Cognitive Load) (29.1%)
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
* *Structure:* `branch: 7`, `structural_boundaries: 15`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `state_mutation: 23`, `unreferenced_by_name: 3`
* *Architecture:* `io: 12`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 11.899
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.008065
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `COBOL Programming Course #4 - Testing/Labs/cbl/EMPPAY.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.814)
- **Top Global Matches:** file_cluster_11: 5.814, file_cluster_2: 6.719, file_cluster_15: 7.376
- **Magnitude:** 38.82 | **LOC:** 55 | **CtrlFlow:** 11.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 11.899; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (71.7%), Complexity Load (formerly Cognitive Load) (61.6%), Test Surface (formerly Verification) (2.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `PAYMENT-WEEKLY` **(I/O & Config Routines)** (Impact: 5.5)
  * `PAYMENT-MONTHLY` **(I/O & Config Routines)** (Impact: 3.4)
  * `SHOW-OUTPUT` **(Interface Declarations)** (Impact: 1.4)
  * `EMPPAY` **(Interface Declarations)** (Impact: 1.3)
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
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 11.899
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.008065
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB21.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 7.182)
- **Top Global Matches:** file_cluster_11: 7.182, file_cluster_12: 7.441, file_cluster_15: 8.331
- **Magnitude:** 35.54 | **LOC:** 145 | **CtrlFlow:** 7.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 11.899; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.7%), Guard Balance (formerly Safety Score) (55.1%), Complexity Load (formerly Cognitive Load) (48.8%), Debt Markers (formerly Tech Debt) (17.3%)
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
* *Structure:* `branch: 8`, `structural_boundaries: 19`, `args: 3`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 10`, `unreferenced_by_name: 1`
* *Architecture:* `io: 11`, `import: 1`
* *Defense:* `safety: 4`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 11.899
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.008065
  * `Imports (Out-Degree: 0):` SQLCA
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0033.cobol` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.267)
- **Top Global Matches:** file_cluster_12: 7.267, file_cluster_11: 7.282, file_cluster_2: 8.267
- **Magnitude:** 35.24 | **LOC:** 131 | **CtrlFlow:** 4.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 11.899; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Mutation Surface (formerly State Flux) (88.0%), Guard Balance (formerly Safety Score) (55.9%), Complexity Load (formerly Cognitive Load) (18.8%)
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
* *Structure:* `branch: 4`, `structural_boundaries: 17`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 7`, `unreferenced_by_name: 14`
* *Architecture:* `io: 4`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.899
  * `Choke Point (Betweenness):` 6.6e-05 | `Ripple Effect (Closeness):` 0.008065
  * `Imports (Out-Degree: 1):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0011.cobol` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.662)
- **Top Global Matches:** file_cluster_11: 5.662, file_cluster_2: 5.924, file_cluster_15: 7.124
- **Magnitude:** 33.06 | **LOC:** 174 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 11.899; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (93.3%), Debt Markers (formerly Tech Debt) (57.4%), Guard Balance (formerly Safety Score) (55.5%), Complexity Load (formerly Cognitive Load) (17.7%)
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
* *Structure:* `branch: 2`, `structural_boundaries: 13`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 16`, `dead_code: 1`, `unreferenced_by_name: 4`
* *Architecture:* `io: 11`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 11.899
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.008065
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0012.cobol` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.649)
- **Top Global Matches:** file_cluster_11: 5.649, file_cluster_2: 5.926, file_cluster_15: 7.116
- **Magnitude:** 32.96 | **LOC:** 169 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 11.899; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (94.4%), Debt Markers (formerly Tech Debt) (59.8%), Guard Balance (formerly Safety Score) (55.7%), Complexity Load (formerly Cognitive Load) (18.5%)
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
* *Structure:* `branch: 2`, `structural_boundaries: 13`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 16`, `dead_code: 1`, `unreferenced_by_name: 4`
* *Architecture:* `io: 11`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 11.899
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.008065
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0008.cobol` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.644)
- **Top Global Matches:** file_cluster_11: 5.644, file_cluster_2: 5.912, file_cluster_15: 7.114
- **Magnitude:** 31.92 | **LOC:** 195 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 11.899; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (91.9%), Debt Markers (formerly Tech Debt) (58.3%), Guard Balance (formerly Safety Score) (55.3%), Complexity Load (formerly Cognitive Load) (16.9%)
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
* *Structure:* `branch: 2`, `structural_boundaries: 13`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 15`, `unreferenced_by_name: 4`
* *Architecture:* `io: 11`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 11.899
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.008065
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0009.cobol` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.644)
- **Top Global Matches:** file_cluster_11: 5.644, file_cluster_2: 5.912, file_cluster_15: 7.114
- **Magnitude:** 31.92 | **LOC:** 195 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 11.899; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (91.9%), Debt Markers (formerly Tech Debt) (58.3%), Guard Balance (formerly Safety Score) (55.3%), Complexity Load (formerly Cognitive Load) (16.9%)
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
* *Structure:* `branch: 2`, `structural_boundaries: 13`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 15`, `unreferenced_by_name: 4`
* *Architecture:* `io: 11`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 11.899
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.008065
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0010.cobol` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.644)
- **Top Global Matches:** file_cluster_11: 5.644, file_cluster_2: 5.912, file_cluster_15: 7.114
- **Magnitude:** 31.92 | **LOC:** 184 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 11.899; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (91.9%), Debt Markers (formerly Tech Debt) (58.3%), Guard Balance (formerly Safety Score) (55.3%), Complexity Load (formerly Cognitive Load) (16.9%)
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
* *Structure:* `branch: 2`, `structural_boundaries: 13`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 15`, `unreferenced_by_name: 4`
* *Architecture:* `io: 11`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 11.899
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.008065
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL006A.cobol` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.546)
- **Top Global Matches:** file_cluster_11: 5.546, file_cluster_2: 5.903, file_cluster_15: 7.105
- **Magnitude:** 30.5 | **LOC:** 173 | **CtrlFlow:** 2.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 11.899; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (93.8%), Guard Balance (formerly Safety Score) (55.5%), Debt Markers (formerly Tech Debt) (47.5%), Complexity Load (formerly Cognitive Load) (13.2%)
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
* *Structure:* `branch: 3`, `structural_boundaries: 13`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 12`, `unreferenced_by_name: 3`
* *Architecture:* `io: 10`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 11.899
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.008065
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBLC1.cobol` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.546)
- **Top Global Matches:** file_cluster_11: 5.546, file_cluster_2: 5.903, file_cluster_15: 7.105
- **Magnitude:** 30.5 | **LOC:** 171 | **CtrlFlow:** 2.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (93.8%), Guard Balance (formerly Safety Score) (55.5%), Debt Markers (formerly Tech Debt) (47.5%), Complexity Load (formerly Cognitive Load) (13.2%)
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
* *Structure:* `branch: 3`, `structural_boundaries: 13`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 12`, `unreferenced_by_name: 3`
* *Architecture:* `io: 10`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.432
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0006.cobol` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.546)
- **Top Global Matches:** file_cluster_11: 5.546, file_cluster_2: 5.902, file_cluster_15: 7.105
- **Magnitude:** 30.4 | **LOC:** 164 | **CtrlFlow:** 2.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 11.899; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (93.8%), Guard Balance (formerly Safety Score) (55.5%), Debt Markers (formerly Tech Debt) (47.5%), Complexity Load (formerly Cognitive Load) (13.2%)
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
* *Structure:* `branch: 3`, `structural_boundaries: 13`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 12`, `unreferenced_by_name: 3`
* *Architecture:* `io: 10`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 11.899
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.008065
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0007.cobol` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.546)
- **Top Global Matches:** file_cluster_11: 5.546, file_cluster_2: 5.9, file_cluster_15: 7.106
- **Magnitude:** 30.3 | **LOC:** 160 | **CtrlFlow:** 2.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 11.899; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (93.8%), Guard Balance (formerly Safety Score) (55.5%), Debt Markers (formerly Tech Debt) (47.5%), Complexity Load (formerly Cognitive Load) (13.2%)
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
* *Structure:* `branch: 3`, `structural_boundaries: 13`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 12`, `unreferenced_by_name: 3`
* *Architecture:* `io: 10`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 11.899
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.008065
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `COBOL Programming Course #4 - Testing/Labs/tests/emppay.cut` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.265)
- **Top Global Matches:** file_cluster_2: 2.265, file_cluster_17: 4.553, file_cluster_13: 5.508
- **Magnitude:** 27.42 | **LOC:** 25 | **CtrlFlow:** 4.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (58.5%), Complexity Load (formerly Cognitive Load) (13.4%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.432
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #3 - Advanced Topics/COBOL Programming Course #3 - Advanced Topics.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 26.72 | **LOC:** 1336 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.432
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0004.cobol` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.837)
- **Top Global Matches:** file_cluster_11: 5.837, file_cluster_2: 6.37, file_cluster_15: 7.301
- **Magnitude:** 26.3 | **LOC:** 164 | **CtrlFlow:** 1.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 11.899; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (89.3%), Debt Markers (formerly Tech Debt) (72.7%), Guard Balance (formerly Safety Score) (54.8%), Complexity Load (formerly Cognitive Load) (15.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `READ-NEXT-RECORD` **(Interface Declarations)** (Impact: 2.6)
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
* *Structure:* `branch: 2`, `structural_boundaries: 12`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 11`, `unreferenced_by_name: 4`
* *Architecture:* `io: 9`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 11.899
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.008065
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0005.cobol` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.837)
- **Top Global Matches:** file_cluster_11: 5.837, file_cluster_2: 6.37, file_cluster_15: 7.301
- **Magnitude:** 26.3 | **LOC:** 164 | **CtrlFlow:** 1.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 11.899; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (89.3%), Debt Markers (formerly Tech Debt) (72.7%), Guard Balance (formerly Safety Score) (54.8%), Complexity Load (formerly Cognitive Load) (15.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `READ-NEXT-RECORD` **(Interface Declarations)** (Impact: 2.6)
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
* *Structure:* `branch: 2`, `structural_boundaries: 12`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 11`, `unreferenced_by_name: 4`
* *Architecture:* `io: 9`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 11.899
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.008065
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `COBOL Programming Course #4 - Testing/COBOL Programming Course #4 - Testing.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 23.44 | **LOC:** 1172 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.432
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/SRCHSER.cobol` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.933)
- **Top Global Matches:** file_cluster_11: 5.933, file_cluster_15: 6.857, file_cluster_2: 6.966
- **Magnitude:** 22.16 | **LOC:** 73 | **CtrlFlow:** 13.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 11.899; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.8%), Debt Markers (formerly Tech Debt) (95.9%), Guard Balance (formerly Safety Score) (56.1%), Complexity Load (formerly Cognitive Load) (24.7%)
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
* *Structure:* `branch: 7`, `structural_boundaries: 13`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 3`, `unreferenced_by_name: 3`
* *Architecture:* `io: 2`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 11.899
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.008065
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `zowe.schema.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.276)
- **Top Global Matches:** file_cluster_2: 2.276, file_cluster_17: 4.996, file_cluster_13: 6.343
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.432
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/SRCHBIN.cobol` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.138)
- **Top Global Matches:** file_cluster_11: 5.138, file_cluster_2: 6.404, file_cluster_15: 7.132
- **Magnitude:** 21.18 | **LOC:** 74 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 11.899; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.6%), Debt Markers (formerly Tech Debt) (95.5%), Guard Balance (formerly Safety Score) (56.1%), Complexity Load (formerly Cognitive Load) (22.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `LOAD-TABLES` **(Interface Declarations)** (Impact: 3.4)
    * *Intent:* *
  * `SEARCH-RECORD` **(Interface Declarations)** (Impact: 3.3)
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
* *Structure:* `branch: 6`, `structural_boundaries: 13`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 3`, `unreferenced_by_name: 3`
* *Architecture:* `io: 2`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 11.899
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.008065
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0033.cobol` (COBOL) | Magnitude: 35.24 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 82, func_start: 18, structural_boundaries: 17, unreferenced_by_name: 14

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0033.cobol` -> **Severity: 0.006** (Bridge: 0.0001 * Flux: 87.9769%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0001.cobol` -> **Severity: 0.896** (Embedded: 0.0161 * Error Risk: 55.5328%)
- `COBOL Programming Course #4 - Testing/Labs/cbl/EMPPAY.CBL` -> **Severity: 0.578** (Embedded: 0.0081 * Error Risk: 71.699%)
- `COBOL Programming Course #3 - Advanced Topics/Challenges/Debugging/cbl/CBL0106.cbl` -> **Severity: 0.489** (Embedded: 0.0081 * Error Risk: 60.6098%)
- `COBOL Programming Course #4 - Testing/Labs/cbl/DEPTPAY.CBL` -> **Severity: 0.488** (Embedded: 0.0081 * Error Risk: 60.5532%)
- `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB22.cbl` -> **Severity: 0.46** (Embedded: 0.0081 * Error Risk: 57.0156%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0001.cobol` -> **Severity: 1736.6** (Blast Radius: 17.366 * Doc Risk: 100.0%)
- `COBOL Programming Course #3 - Advanced Topics/Labs/jcl/DBRMLIB.jcl` -> **Severity: 1736.6** (Blast Radius: 17.366 * Doc Risk: 100.0%)
- `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/HELLO.cobol` -> **Severity: 1654.4** (Blast Radius: 16.544 * Doc Risk: 100.0%)
- `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/ADDAMT.cobol` -> **Severity: 1189.9** (Blast Radius: 11.899 * Doc Risk: 100.0%)
- `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0002.cobol` -> **Severity: 1189.9** (Blast Radius: 11.899 * Doc Risk: 100.0%)

## 13. MAINFRAME SYSTEM FACTS (Named Relations & Record Layouts)
> **AI CONTEXT:** Named mainframe relations the structural signal counts flatten -- the call graph (`CALL`/CICS `LINK`·`XCTL`/JCL `EXEC PGM=`), the dataset boundary (`SELECT…ASSIGN` + `OPEN` modes, JCL `DD`→dataset), and record layouts (COBOL DATA DIVISION items, PL/I `DECLARE`d structures). BMS screen maps (every field's position, length and attributes, `screen_field_data`) are the 3270 UI surface. These are the schema of the system: use them to trace which program runs which, which dataset a job binds, and the shape of the records that flow between them. Extracted by the engine (`core/mainframe_boundary.py`) and carried in the master DB (`call_site_data`/`dataset_data`/`record_data`); resolution to files is redone per scan.

- **Coverage:** `73` files carry mainframe facts -- `48` call sites, `129` dataset bindings, `1209` record items.

- **DB2 schemas:** `30` columns of `EXEC SQL DECLARE ... TABLE` (inline or DCLGEN members), full shape in `sql_table_data`.

- **DB2 table access:** `25` embedded SQL statements touching `1` tables (SELECT/INSERT/UPDATE/DELETE, cursors, host variables) in `sql_statement_data`; the program x table read/write matrix is `GalaxyIR.sql_table_access()`.

### `COBOL Programming Course #3 - Advanced Topics/Challenges/Debugging/cbl/CBL0106C.cbl` (COBOL)
- **Datasets:** `PRTLINE(OUTPUT)`, `ACCTREC(INPUT)`
- **Record layouts (82 items):** `ACCT-FIELDS⟵ACCT-REC (12)`, `HEADER-2 (10)`, `WS-CURRENT-DATE-DATA (10)`, `PRINT-REC⟵PRINT-LINE (9)`, `HEADER-3 (9)`, `HEADER-4 (9)`, `OVERLIMIT (7)`, `FILLER (5)`, `CLIENTS-PER-STATE (4)`, `OVERLIMIT-STATUS (4)`, `HEADER-1 (3)`
- **Data moves:** 29 (ADD 2, MOVE 22, WRITE 5); most-fed items `PRINT-REC`, `ACCT-BALANCE-O`, `ACCT-LIMIT-O`, `ACCT-NO-O`, `DISP-SUB1`, `HDR-DAY`

### `COBOL Programming Course #3 - Advanced Topics/Challenges/Debugging/cbl/CBL0106.cbl` (COBOL)
- **Datasets:** `PRTLINE(OUTPUT)`, `ACCTREC(INPUT)`
- **Record layouts (81 items):** `ACCT-FIELDS⟵ACCT-REC (12)`, `HEADER-2 (10)`, `WS-CURRENT-DATE-DATA (10)`, `PRINT-REC⟵PRINT-LINE (9)`, `HEADER-3 (9)`, `HEADER-4 (9)`, `OVERLIMIT (7)`, `FILLER (4)`, `CLIENTS-PER-STATE (4)`, `OVERLIMIT-STATUS (4)`, `HEADER-1 (3)`
- **Data moves:** 28 (ADD 2, MOVE 21, WRITE 5); most-fed items `PRINT-REC`, `ACCT-BALANCE-O`, `ACCT-LIMIT-O`, `ACCT-NO-O`, `DISP-SUB1`, `HDR-DAY`

### `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0011.cobol` (COBOL)
- **Datasets:** `PRTLINE(OUTPUT)`, `ACCTREC(INPUT)`
- **Record layouts (81 items):** `ACCT-FIELDS⟵ACCT-REC (12)`, `HEADER-2 (10)`, `WS-CURRENT-DATE-DATA (10)`, `PRINT-REC⟵PRINT-LINE (9)`, `HEADER-3 (9)`, `HEADER-4 (9)`, `TRAILER-2 (8)`, `TRAILER-1 (6)`, `TLIMIT-TBALANCE (3)`, `HEADER-1 (3)`, `FLAGS (2)`
- **Data moves:** 24 (COMPUTE 4, MOVE 14, WRITE 6); most-fed items `PRINT-REC`, `TBALANCE`, `TLIMIT`, `ACCT-BALANCE-O`, `ACCT-LIMIT-O`, `ACCT-NO-O`

### `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0008.cobol` (COBOL)
- **Datasets:** `PRTLINE(OUTPUT)`, `ACCTREC(INPUT)`
- **Record layouts (81 items):** `ACCT-FIELDS⟵ACCT-REC (12)`, `HEADER-2 (10)`, `WS-CURRENT-DATE-DATA (10)`, `PRINT-REC⟵PRINT-LINE (9)`, `HEADER-3 (9)`, `HEADER-4 (9)`, `TRAILER-2 (8)`, `TRAILER-1 (6)`, `TLIMIT-TBALANCE (3)`, `HEADER-1 (3)`, `FLAGS (2)`
- **Data moves:** 23 (COMPUTE 4, MOVE 13, WRITE 6); most-fed items `PRINT-REC`, `TBALANCE`, `TLIMIT`, `ACCT-BALANCE-O`, `ACCT-LIMIT-O`, `ACCT-NO-O`

### `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0009.cobol` (COBOL)
- **Datasets:** `PRTLINE(OUTPUT)`, `ACCTREC(INPUT)`
- **Record layouts (81 items):** `ACCT-FIELDS⟵ACCT-REC (12)`, `HEADER-2 (10)`, `WS-CURRENT-DATE-DATA (10)`, `PRINT-REC⟵PRINT-LINE (9)`, `HEADER-3 (9)`, `HEADER-4 (9)`, `TRAILER-2 (8)`, `TRAILER-1 (6)`, `TLIMIT-TBALANCE (3)`, `HEADER-1 (3)`, `FLAGS (2)`
- **Data moves:** 23 (COMPUTE 4, MOVE 13, WRITE 6); most-fed items `PRINT-REC`, `TBALANCE`, `TLIMIT`, `ACCT-BALANCE-O`, `ACCT-LIMIT-O`, `ACCT-NO-O`

### `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0010.cobol` (COBOL)
- **Datasets:** `PRTLINE(OUTPUT)`, `ACCTREC(INPUT)`
- **Record layouts (81 items):** `ACCT-FIELDS⟵ACCT-REC (12)`, `HEADER-2 (10)`, `WS-CURRENT-DATE-DATA (10)`, `PRINT-REC⟵PRINT-LINE (9)`, `HEADER-3 (9)`, `HEADER-4 (9)`, `TRAILER-2 (8)`, `TRAILER-1 (6)`, `TLIMIT-TBALANCE (3)`, `HEADER-1 (3)`, `FLAGS (2)`
- **Data moves:** 23 (COMPUTE 4, MOVE 13, WRITE 6); most-fed items `PRINT-REC`, `TBALANCE`, `TLIMIT`, `ACCT-BALANCE-O`, `ACCT-LIMIT-O`, `ACCT-NO-O`

### `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0012.cobol` (COBOL)
- **Datasets:** `PRTLINE(OUTPUT)`, `ACCTREC(INPUT)`
- **Record layouts (76 items):** `ACCT-FIELDS⟵ACCT-REC (12)`, `HEADER-2 (10)`, `PRINT-REC⟵PRINT-LINE (9)`, `HEADER-3 (9)`, `HEADER-4 (9)`, `TRAILER-2 (8)`, `TRAILER-1 (6)`, `WS-CURRENT-DATE-DATA (5)`, `TLIMIT-TBALANCE (3)`, `HEADER-1 (3)`, `FLAGS (2)`
- **Data moves:** 24 (COMPUTE 4, MOVE 14, WRITE 6); most-fed items `PRINT-REC`, `TBALANCE`, `TLIMIT`, `ACCT-BALANCE-O`, `ACCT-LIMIT-O`, `ACCT-NO-O`

### `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0007.cobol` (COBOL)
- **Datasets:** `PRTLINE(OUTPUT)`, `ACCTREC(INPUT)`
- **Record layouts (69 items):** `ACCT-FIELDS⟵ACCT-REC (13)`, `HEADER-2 (10)`, `WS-CURRENT-DATE-DATA (10)`, `PRINT-REC⟵PRINT-LINE (9)`, `HEADER-3 (9)`, `HEADER-4 (9)`, `CLIENTS-PER-STATE (4)`, `HEADER-1 (3)`, `FLAGS (2)`
- **Data moves:** 17 (ADD 1, MOVE 11, WRITE 5); most-fed items `PRINT-REC`, `ACCT-BALANCE-O`, `ACCT-LIMIT-O`, `ACCT-NO-O`, `HDR-DAY`, `HDR-MO`

### `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0006.cobol` (COBOL)
- **Datasets:** `PRTLINE(OUTPUT)`, `ACCTREC(INPUT)`
- **Record layouts (68 items):** `ACCT-FIELDS⟵ACCT-REC (12)`, `HEADER-2 (10)`, `WS-CURRENT-DATE-DATA (10)`, `PRINT-REC⟵PRINT-LINE (9)`, `HEADER-3 (9)`, `HEADER-4 (9)`, `CLIENTS-PER-STATE (4)`, `HEADER-1 (3)`, `FLAGS (2)`
- **Data moves:** 17 (ADD 1, MOVE 11, WRITE 5); most-fed items `PRINT-REC`, `ACCT-BALANCE-O`, `ACCT-LIMIT-O`, `ACCT-NO-O`, `HDR-DAY`, `HDR-MO`

### `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL006A.cobol` (COBOL)
- **Datasets:** `PRTLINE(OUTPUT)`, `ACCTREC(INPUT)`
- **Record layouts (68 items):** `ACCT-FIELDS⟵ACCT-REC (12)`, `HEADER-2 (10)`, `WS-CURRENT-DATE-DATA (10)`, `PRINT-REC⟵PRINT-LINE (9)`, `HEADER-3 (9)`, `HEADER-4 (9)`, `CLIENTS-PER-STATE (4)`, `HEADER-1 (3)`, `FLAGS (2)`
- **Data moves:** 17 (ADD 1, MOVE 11, WRITE 5); most-fed items `PRINT-REC`, `ACCT-BALANCE-O`, `ACCT-LIMIT-O`, `ACCT-NO-O`, `HDR-DAY`, `HDR-MO`

### `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBLC1.cobol` (COBOL)
- **Datasets:** `PRTLINE(OUTPUT)`, `ACCTREC(INPUT)`
- **Record layouts (68 items):** `ACCT-FIELDS⟵ACCT-REC (12)`, `HEADER-2 (10)`, `WS-CURRENT-DATE-DATA (10)`, `PRINT-REC⟵PRINT-LINE (9)`, `HEADER-3 (9)`, `HEADER-4 (9)`, `CLIENTS-PER-STATE (4)`, `HEADER-1 (3)`, `FLAGS (2)`
- **Data moves:** 17 (ADD 1, MOVE 11, WRITE 5); most-fed items `PRINT-REC`, `ACCT-BALANCE-O`, `ACCT-LIMIT-O`, `ACCT-NO-O`, `HDR-DAY`, `HDR-MO`

### `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0004.cobol` (COBOL)
- **Datasets:** `PRTLINE(OUTPUT)`, `ACCTREC(INPUT)`
- **Record layouts (64 items):** `ACCT-FIELDS⟵ACCT-REC (12)`, `HEADER-2 (10)`, `WS-CURRENT-DATE-DATA (10)`, `PRINT-REC⟵PRINT-LINE (9)`, `HEADER-3 (9)`, `HEADER-4 (9)`, `HEADER-1 (3)`, `FLAGS (2)`
- **Data moves:** 15 (MOVE 11, WRITE 4); most-fed items `PRINT-REC`, `ACCT-BALANCE-O`, `ACCT-LIMIT-O`, `ACCT-NO-O`, `HDR-DAY`, `HDR-MO`

### `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0005.cobol` (COBOL)
- **Datasets:** `PRTLINE(OUTPUT)`, `ACCTREC(INPUT)`
- **Record layouts (64 items):** `ACCT-FIELDS⟵ACCT-REC (12)`, `HEADER-2 (10)`, `WS-CURRENT-DATE-DATA (10)`, `PRINT-REC⟵PRINT-LINE (9)`, `HEADER-3 (9)`, `HEADER-4 (9)`, `HEADER-1 (3)`, `FLAGS (2)`
- **Data moves:** 15 (MOVE 11, WRITE 4); most-fed items `PRINT-REC`, `ACCT-BALANCE-O`, `ACCT-LIMIT-O`, `ACCT-NO-O`, `HDR-DAY`, `HDR-MO`

### `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB22.cbl` (COBOL)
- **Calls:** `CALL DSNTIAR`
- **Datasets:** `REPORT(OUTPUT)`, `RECIN(INPUT)`
- **Record layouts (30 items):** `CUSTOMER-RECORD (11)`, `REPREC⟵REPOUT (7)`, `IOAREA (3)`, `ERROR-MESSAGE (3)`, `INPUT-SWITCH (2)`, `INREC⟵RECIN (1)`, `ERROR-TEXT-LEN (1)`, `ERROR-TEXT-HBOUND (1)`, `UD-ERROR-MESSAGE (1)`
- **DB2 tables declared:** `Z#####T (10 cols)`
- **DB2 table access:** `Z#####T (read)`
- **Data moves:** 15 (MOVE 13, READ 2); most-fed items `ACCT-BALANCE-O`, `ACCT-COMMENT-O`, `ACCT-FIRSTN-O`, `ACCT-LASTN-O`, `ACCT-LIMIT-O`, `ACCT-NO-O`

### `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB23.cbl` (COBOL)
- **Calls:** `CALL DSNTIAR`
- **Datasets:** `REPORT(OUTPUT)`, `CARDIN(INPUT)`
- **Record layouts (28 items):** `CUSTOMER-RECORD (11)`, `REPREC⟵REPOUT (5)`, `IOAREA (3)`, `ERROR-MESSAGE (3)`, `INPUT-SWITCH (2)`, `CARDREC⟵CARDIN (1)`, `ERROR-TEXT-LEN (1)`, `ERROR-TEXT-HBOUND (1)`, `UD-ERROR-MESSAGE (1)`
- **DB2 tables declared:** `Z#####T (10 cols)`
- **DB2 table access:** `Z#####T (read)`
- **Data moves:** 13 (MOVE 11, READ 2); most-fed items `ACCT-ADDR3-O`, `ACCT-FIRSTN-O`, `ACCT-LASTN-O`, `ACCT-NO-O`

### `COBOL Programming Course #3 - Advanced Topics/Labs/jclproc/DB2CBL.jcl` (JCL)
- **Calls:** `EXEC PGM IGYCRCTL`, `EXEC PGM IEWBLINK`, `EXEC PGM IKJEFT01`
- **Datasets:** `STEPLIB→IGY630.SIGYCOMP`, `STEPLIB→DSNC10.DBCG.SDSNEXIT`, `STEPLIB→DSNC10.SDSNLOAD`, `STEPLIB→CEE.SCEERUN`, `STEPLIB→CEE.SCEERUN2`, `SYSIN→&SYSUID..CBL(&MBR)`, `DBRMLIB→&SYSUID..DBRMLIB(&MBR)`, `SYSLIB→CEE.SCEELKED`, `SYSLIB→DSNC10.SDSNLOAD`, `SYSLMOD→&SYSUID..LOAD(&MBR)`, `STEPLIB→DSNC10.SDSNLOAD`, `DBRMLIB→&SYSUID..DBRMLIB`

### `COBOL Programming Course #3 - Advanced Topics/Labs/cbl/CBLDB21.cbl` (COBOL)
- **Calls:** `CALL DSNTIAR`
- **Datasets:** `REPORT(OUTPUT)`
- **Record layouts (24 items):** `CUSTOMER-RECORD (11)`, `REPREC⟵REPOUT (7)`, `ERROR-MESSAGE (3)`, `ERROR-TEXT-LEN (1)`, `ERROR-TEXT-HBOUND (1)`, `UD-ERROR-MESSAGE (1)`
- **DB2 tables declared:** `Z#####T (10 cols)`
- **DB2 table access:** `Z#####T (read)`
- **Data moves:** 10 (MOVE 10); most-fed items `ACCT-BALANCE-O`, `ACCT-COMMENT-O`, `ACCT-FIRSTN-O`, `ACCT-LASTN-O`, `ACCT-LIMIT-O`, `ACCT-NO-O`

### `COBOL Programming Course #2 - Learning COBOL/Labs/jclproc/IGYWCLG.jcl` (JCL)
- **Calls:** `EXEC PGM IGYCRCTL`, `EXEC PGM IEWBLINK`
- **Datasets:** `STEPLIB→IGY630.SIGYCOMP`, `STEPLIB→CEE.SCEERUN`, `STEPLIB→CEE.SCEERUN2`, `SYSIN→&SYSUID..CBL(&SRC)`, `SYSLIB→CEE.SCEELKEX`, `SYSLIB→CEE.SCEELKED`, `SYSLMOD→&SYSUID..LOAD(&SRC)`, `STEPLIB→CEE.SCEERUN`, `STEPLIB→CEE.SCEERUN2`

### `COBOL Programming Course #2 - Learning COBOL/Labs/jclproc/IGYWCL.jcl` (JCL)
- **Calls:** `EXEC PGM IGYCRCTL`, `EXEC PGM IEWBLINK`
- **Datasets:** `STEPLIB→IGY630.SIGYCOMP`, `STEPLIB→CEE.SCEERUN`, `STEPLIB→CEE.SCEERUN2`, `SYSIN→&SYSUID..CBL(&SRC)`, `SYSLIB→CEE.SCEELKEX`, `SYSLIB→CEE.SCEELKED`, `SYSLMOD→&SYSUID..LOAD(&SRC)`

### `COBOL Programming Course #2 - Learning COBOL/Labs/cbl/CBL0033.cobol` (COBOL)
- **Calls:** `CALL HELLO`
- **Datasets:** `PRTLINE(OUTPUT)`, `ACCTREC(INPUT)`
- **Record layouts (22 items):** `ACCT-FIELDS⟵ACCT-REC (12)`, `PRINT-REC⟵PRINT-LINE (7)`, `FLAGS (2)`, `COUNTER (1)`
- **Data moves:** 7 (MOVE 7); most-fed items `ACCT-BALANCE-O`, `ACCT-LIMIT-O`, `ACCT-NO-O`, `COMMENTS-O`, `FIRST-NAME-O`, `LAST-NAME-O`

*(+53 more files with mainframe facts; full detail in `record_data`/`call_site_data`/`dataset_data`.)*

- **Mainframe skeleton completeness:** 93% (mean channel ratio; channel table in the audit report, section 7). Top missing inputs: scheduler export (CA-7 / Control-M / TWS) (37 gaps); JCL and PROC libraries (4 gaps); application programs (source or load-module list) (1 gaps).

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 161 call pairs -- scoped 52.8%, unique 1.9%, ambiguous 0.0%, external 45.3%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| cobol | 87 | 95.4% | 1.1% | 0.0% | 3.4% |
| jcl | 74 | 2.7% | 2.7% | 0.0% | 94.6% |

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
