# ARCHITECTURAL_BRIEF: cobol-unit-test
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/neopragma/cobol-unit-test` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 43 analyzed artifact(s), 5502 LOC.
- **Load-bearing artifact:** `src/main/cobol/copy/DFHEIBLK.CPY` -- 2 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `padder.py` -- pulls in 2 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `src/main/cobol/ZUTZCPC.CBL` at magnitude 2097.4 (structural weight, not risk).
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
| Total Artifacts | 81 |
| Analyzed Artifacts (Scanned) | 43 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 38 |
| Total LOC | 5502 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 53.1% |
| Dominant Lang | COBOL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 2 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| COBOL | 27 | 5054 | 62.8% |
| PLAINTEXT | 6 | 0 | 14.0% |
| SHELL | 5 | 206 | 11.6% |
| BATCH | 3 | 216 | 7.0% |
| MARKDOWN | 1 | 0 | 2.3% |
| PYTHON | 1 | 26 | 2.3% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Small Flat Repo`
> **Architectural Drift Z-Score:** `1.795`
> **Composition Archetype:** `Small Flat Repo` (z +1.79; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules 47%, Declarative / Non-Code 21%, Data / Markup / Trivial 19%, Interface Declarations Files 7%, Large Core Modules (2) 2%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 36 | 83.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 7 | 16.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 38*

**Composition by Extension & Reason:**
- `no_extension`: 33x Unsupported Format (.undeterminable), 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Binary Format Detected)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 89.3 | 27.2 | 9.8 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.5 | 51.7 | 70.2 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 37.9 | 22.8 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 6.6 | 2.4 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 7.7 | 1.0 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 53.4 | 70.8 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 95.9 | 2.9 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 68.1 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 2.8 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 29 | 8 | 1 | `src/main/cobol/ZUTZCPC.CBL` |
| cleanup | 21 | 9 | 2 | `src/main/cobol/ZUTZCPC.CBL` |
| guards | 2 | 1 | 0 | `padder.py` |
| danger | 62 | 18 | 2 | `run-ut` |
| concurrency | 2 | 2 | 0 | `compile` |
| connectivity | 15 | 8 | 1 | `run-ut` |
| io | 223 | 15 | 9 | `src/main/cobol/ZUTZCPC.CBL` |
| crypto | 0 | 0 | 0 | - |
| ipc | 43 | 12 | 3 | `convert-bad.cbl` |
| time | 1 | 1 | 0 | `src/main/cobol/INVDATE.CBL` |
| serialization | 205 | 11 | 4 | `src/main/cobol/ZUTZCPC.CBL` |
| regex | 41 | 2 | 0 | `src/main/cobol/ZUTZCPC.CBL` |
| events | 0 | 0 | 0 | - |
| tests | 36 | 2 | 0 | `src/main/cobol/ZUTZCPC.CBL` |
| docs | 0 | 0 | 0 | - |
| debt | 147 | 18 | 8 | `run-examples` |
| mutation | 1092 | 25 | 21 | `src/main/cobol/ZUTZCPC.CBL` |
| dead_code | 69 | 24 | 4 | `src/main/cobol/ZUTZCPC.CBL` |
| credential | 36 | 1 | 0 | `src/main/cobol/ZUTZCPC.CBL` |
| threat | 50 | 14 | 2 | `src/main/cobol/ZUTZCPC.CBL` |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/main/cobol/ZUTZCPC.CBL` (Hits: 132)
- `run-ut` (Hits: 10)
- `src/main/cobol/CARD1.CBL` (Hits: 10)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **DFHEIBLK.CPY** (`src/main/cobol/copy/DFHEIBLK.CPY`) — 2 inbound connections
2. **output.txt** (`src/test/resources/output.txt`) — 2 inbound connections
3. **README.md** (`README.md`) — 0 inbound connections
4. **compile** (`compile`) — 0 inbound connections
5. **integration-tests** (`integration-tests`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **padder.py** (`padder.py`) — 2 outbound dependencies
2. **compile** (`compile`) — 1 outbound dependencies
3. **run-ut** (`run-ut`) — 1 outbound dependencies
4. **convert-bad.cbl** (`convert-bad.cbl`) — 1 outbound dependencies
5. **convert-bad2.cbl** (`convert-bad2.cbl`) — 1 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `4200-PROCESS-KEYWORDS` **(I/O & Config Routines)** (@ `src/main/cobol/ZUTZCPC.CBL`) -> Impact: **26.6** | LOC: 71
- `4900-PROCESS-MOCK-FILE-SPEC` **(I/O & Config Routines)** (@ `src/main/cobol/ZUTZCPC.CBL`) -> Impact: **23.2** | LOC: 165
- `DEFAULT-CICS-STATEMENT-VALUES` **(I/O & Config Routines)** (@ `src/main/cobol/ZUTZCPC.CBL`) -> Impact: **18.5** | LOC: 904
- `UT-ASSERT-ACCESSES` **(I/O & Config Routines)** (@ `src/main/cobol/copy/ZUTZCPD.CPY`) -> Impact: **18.1** | LOC: 83
- `5060-PARSE-HAPPENED-SPEC` **(I/O & Config Routines)** (@ `src/main/cobol/ZUTZCPC.CBL`) -> Impact: **15.7** | LOC: 54
- `UT-LOOKUP-MOCK` **(I/O & Config Routines)** (@ `src/main/cobol/copy/ZUTZCPD.CPY`) -> Impact: **13.9** | LOC: 39
- `2200-IDENTIFY-CARD-TYPE` **(I/O & Config Routines)** (@ `src/main/cobol/CARD1.CBL`) -> Impact: **13.3** | LOC: 26
- `2200-IDENTIFY-CARD-TYPE` **(I/O & Config Routines)** (@ `src/main/cobol/CARD2.CBL`) -> Impact: **13.3** | LOC: 26
- `5020-VERIFY-CALL-MOCK` **(I/O & Config Routines)** (@ `src/main/cobol/ZUTZCPC.CBL`) -> Impact: **12.9** | LOC: 98
- `9425-WRITE-TEST-LINE` **(I/O & Config Routines)** (@ `src/main/cobol/ZUTZCPC.CBL`) -> Impact: **12.8** | LOC: 36

*Function archetypes referenced above:*
  * **I/O & Config Routines**: dominated by I/O and configuration handling

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src/main/cobol` | 20 | 2556.72 | 30.38% | 66.55% |
| `__monolith__` | 9 | 264.74 | 31.63% | 0.0% |
| `src/test/cobol` | 2 | 59.0 | 12.38% | 0.0% |
| `win` | 3 | 49.32 | 0.0% | 0.0% |
| `src/main/cobol/copy` | 3 | 12.01 | 21.03% | 11.28% |
| `src/test/resources` | 6 | 6.0 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/main/cobol/MOCKDEMO.CBL` -> **99.9797%** Exposure
- `src/main/cobol/PARADEMO.CBL` -> **99.9797%** Exposure
- `src/main/cobol/CALLDEMO.CBL` -> **99.8499%** Exposure
- `src/main/cobol/CICSDEMO.CBL` -> **98.9013%** Exposure
- `src/main/cobol/FILEDEMO.CBL` -> **98.9013%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `compile` -> **100.0%** Exposure
- `src/main/cobol/CARD2.CBL` -> **100.0%** Exposure
- `src/main/cobol/ZUTZCPC.CBL` -> **100.0%** Exposure
- `src/main/cobol/copy/ZUTZCPD.CPY` -> **100.0%** Exposure
- `src/main/cobol/VIZZBUZZ.CBL` -> **99.9998%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/main/cobol/MOCKDEMO.CBL` -> **5** Orphaned Functions | **0** Duplicates
- `src/main/cobol/PARADEMO.CBL` -> **5** Orphaned Functions | **0** Duplicates
- `src/main/cobol/CALLDEMO.CBL` -> **4** Orphaned Functions | **0** Duplicates
- `src/main/cobol/copy/ZUTZCPD.CPY` -> **4** Orphaned Functions | **0** Duplicates
- `src/main/cobol/CICSDEMO.CBL` -> **3** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `src/main/cobol/ZUTZCPC.CBL` -> **100.0%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `6` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `13` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/main/cobol/ZUTZCPC.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 2097.4 | **LOC:** 4427 | **CtrlFlow:** 10.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Credential Material (formerly Secrets Risk) (100.0%), Guard Balance (formerly Safety Score) (92.8%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `4200-PROCESS-KEYWORDS` **(I/O & Config Routines)** (Impact: 26.6)
  * `4900-PROCESS-MOCK-FILE-SPEC` **(I/O & Config Routines)** (Impact: 23.2)
  * `DEFAULT-CICS-STATEMENT-VALUES` **(I/O & Config Routines)** (Impact: 18.5)
  * `5060-PARSE-HAPPENED-SPEC` **(I/O & Config Routines)** (Impact: 15.7)
  * `5020-VERIFY-CALL-MOCK` **(I/O & Config Routines)** (Impact: 12.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 314 instances
* *State Mutation (weighted view):* 1413
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 346`, `structural_boundaries: 472`, `func_start: 112`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 785`, `dead_code: 15`, `unreferenced_by_name: 2`
* *Architecture:* `io: 132`, `api: 2`
* *Defense:* `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.552
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/cobol/CONVER2.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 62.22 | **LOC:** 153 | **CtrlFlow:** 9.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 21.552; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.2%), Complexity Load (formerly Cognitive Load) (47.4%), Debt Markers (formerly Tech Debt) (23.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `1000-PROCESS-INPUT` **(I/O & Config Routines)** (Impact: 4.7)
  * `2200-LOOKUP-STATE-NAME` **(I/O & Config Routines)** (Impact: 3.5)
  * `2100-CONVERT-TEXT-FIELD-1` **(I/O & Config Routines)** (Impact: 3.4)
  * `0500-INITIALIZE` **(Interface Declarations)** (Impact: 2.5)
  * `2300-CONVERT-TEXT-FIELD-2` **(I/O & Config Routines)** (Impact: 2.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 34
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 23`, `args: 3`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `state_mutation: 14`, `unreferenced_by_name: 1`
* *Architecture:* `io: 6`, `import: 1`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.552
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` OUTPUT
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/cobol/CONVERT.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 60.66 | **LOC:** 176 | **CtrlFlow:** 8.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 21.552; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (79.7%), Complexity Load (formerly Cognitive Load) (34.2%), Debt Markers (formerly Tech Debt) (19.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `1000-PROCESS-INPUT` **(I/O & Config Routines)** (Impact: 4.8)
  * `2300-CONVERT-TEXT-FIELD-2` **(I/O & Config Routines)** (Impact: 3.9)
  * `2200-LOOKUP-STATE-NAME` **(I/O & Config Routines)** (Impact: 3.6)
  * `2100-CONVERT-TEXT-FIELD-1` **(I/O & Config Routines)** (Impact: 3.5)
  * `0500-INITIALIZE` **(Interface Declarations)** (Impact: 2.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 32
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 24`, `args: 3`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `state_mutation: 14`, `unreferenced_by_name: 1`
* *Architecture:* `io: 8`, `import: 1`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.552
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` OUTPUT
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `compile` (SHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 60.36 | **LOC:** 77 | **CtrlFlow:** 20.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 21.552; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.8%), Complexity Load (formerly Cognitive Load) (76.4%), Connectivity (formerly Api Exposure) (3.2%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Anonymous_Block` **(Compute Cores)** (Impact: 4.7)
  * `Anonymous_Block` **(Compute Cores)** (Impact: 4.6)
  * `Anonymous_Block` **(Compute Cores)** (Impact: 4.4)
    * *Intent:* # remove existing output file, if any
  * `__global_context__` **(I/O & Config Routines)** (Impact: 4.3)
  * `Anonymous_Block` **(I/O & Config Routines)** (Impact: 3.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 30
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 52`, `args: 8`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 10`
* *Architecture:* `io: 9`, `api: 1`, `import: 1`
* *Defense:* `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.552
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` envvars
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/test/cobol/CONVERT-TEST.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 56.12 | **LOC:** 144 | **CtrlFlow:** 12.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 21.552; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (85.3%), Complexity Load (formerly Cognitive Load) (24.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `2000-COMPARE-RECORDS` **(I/O & Config Routines)** (Impact: 11.9)
  * `1000-COMPARE-FILES` **(I/O & Config Routines)** (Impact: 5.3)
  * `0500-INITIALIZE` **(Interface Declarations)** (Impact: 2.6)
  * `0000-MAIN` **(Interface Declarations)** (Impact: 1.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 33
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 22`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 11`, `unreferenced_by_name: 1`
* *Architecture:* `io: 6`, `import: 2`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.552
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` OUTPUT
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/cobol/CARD1.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 52.78 | **LOC:** 134 | **CtrlFlow:** 14.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.5%), Complexity Load (formerly Cognitive Load) (79.4%), Debt Markers (formerly Tech Debt) (25.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `2200-IDENTIFY-CARD-TYPE` **(I/O & Config Routines)** (Impact: 13.3)
  * `9100-OPEN-FILES` **(I/O & Config Routines)** (Impact: 2.6)
  * `2000-IDENTIFY-CARD-TYPES` **(Interface Declarations)** (Impact: 2.3)
  * `9400-CLOSE-FILES` **(I/O & Config Routines)** (Impact: 1.2)
  * `9200-READ-INPUT-FILE` **(I/O & Config Routines)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 28
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 17`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 10`, `unreferenced_by_name: 1`
* *Architecture:* `io: 10`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.552
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/cobol/FIZZBUZZ.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 51.7 | **LOC:** 104 | **CtrlFlow:** 12.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.7%), Complexity Load (formerly Cognitive Load) (85.6%), Debt Markers (formerly Tech Debt) (60.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `1000-PROCESS-NUMBER` **(I/O & Config Routines)** (Impact: 10.6)
  * `0000-MAIN` **(Interface Declarations)** (Impact: 3.6)
  * `0500-INITIALIZE` **(Interface Declarations)** (Impact: 1.4)
  * `2000-DIVIDE` **(I/O & Config Routines)** (Impact: 1.3)
  * `9999-END` **(I/O & Config Routines)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 32
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 18`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 12`, `unreferenced_by_name: 2`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.552
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `convert-bad.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 51.18 | **LOC:** 135 | **CtrlFlow:** 10.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 21.552; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (85.4%), Complexity Load (formerly Cognitive Load) (52.1%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 34
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 13`, `args: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 14`
* *Architecture:* `io: 6`, `import: 1`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 21.552
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` output
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `convert-bad2.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 51.18 | **LOC:** 180 | **CtrlFlow:** 10.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 21.552; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (85.4%), Complexity Load (formerly Cognitive Load) (52.1%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 34
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 13`, `args: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 14`
* *Architecture:* `io: 6`, `import: 1`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 21.552
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` output
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `run-ut` (SHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 51.1 | **LOC:** 101 | **CtrlFlow:** 12.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 21.552; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.5%), Complexity Load (formerly Cognitive Load) (49.7%), Connectivity (formerly Api Exposure) (7.7%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run_unit_tests` **(I/O & Config Routines)** (Impact: 6.7)
    * *Intent:* #!/bin/bash #================================================================================ # Run ...
  * `__global_context__` **(Many-Argument Workhorses)** (Impact: 6.3)
  * `Anonymous_Block` **(Compute Cores)** (Impact: 4.7)
  * `show_help` **(I/O & Config Routines)** (Impact: 2.6)
  * `Anonymous_Block` **(Interface Declarations)** (Impact: 2.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 21
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 49`, `args: 9`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 7`
* *Architecture:* `io: 10`, `api: 5`, `import: 1`
* *Defense:* `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.552
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` envvars
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/cobol/CARD3.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 48.46 | **LOC:** 149 | **CtrlFlow:** 11.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.5%), Guard Balance (formerly Safety Score) (76.4%), Complexity Load (formerly Cognitive Load) (52.5%), Debt Markers (formerly Tech Debt) (22.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `2200-IDENTIFY-CARD-TYPE` **(I/O & Config Routines)** (Impact: 12.4)
  * `9100-OPEN-FILES` **(I/O & Config Routines)** (Impact: 2.6)
  * `2000-IDENTIFY-CARD-TYPES` **(Interface Declarations)** (Impact: 2.2)
  * `2290-POPULATE-MESSAGE` **(Interface Declarations)** (Impact: 1.4)
  * `9400-CLOSE-FILES` **(I/O & Config Routines)** (Impact: 1.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 23
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 26`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 9`, `unreferenced_by_name: 1`
* *Architecture:* `io: 10`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.552
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/cobol/CARD2.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 44.36 | **LOC:** 62 | **CtrlFlow:** 22.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.0%), Complexity Load (formerly Cognitive Load) (78.2%), Debt Markers (formerly Tech Debt) (62.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `2200-IDENTIFY-CARD-TYPE` **(I/O & Config Routines)** (Impact: 13.3)
  * `9999-END` **(I/O & Config Routines)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 28
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 8`, `args: 1`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 10`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.552
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/cobol/VIZZBUZZ.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 42.32 | **LOC:** 87 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (89.0%), Debt Markers (formerly Tech Debt) (78.4%), Complexity Load (formerly Cognitive Load) (63.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `1000-PROCESS-NUMBER` **(I/O & Config Routines)** (Impact: 7.9)
  * `0000-MAIN` **(Interface Declarations)** (Impact: 3.6)
  * `0500-INITIALIZE` **(Interface Declarations)** (Impact: 1.2)
  * `2000-DIVIDE` **(I/O & Config Routines)** (Impact: 1.2)
  * `9999-END` **(I/O & Config Routines)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 26
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 16`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 10`, `unreferenced_by_name: 2`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.552
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/cobol/INVDATE.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 32.38 | **LOC:** 59 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 21.552; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (92.4%), Complexity Load (formerly Cognitive Load) (89.3%), Guard Balance (formerly Safety Score) (86.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `2000-NEXT-INVOICE-DATE` **(I/O & Config Routines)** (Impact: 5.5)
  * `2100-HANDLE-FEBRUARY` **(I/O & Config Routines)** (Impact: 3.5)
  * `0000-MAIN` **(Interface Declarations)** (Impact: 1.2)
  * `0500-INITIALIZE` **(I/O & Config Routines)** (Impact: 1.1)
  * `1000-PROCESS-INVOICES` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 10`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 6`, `unreferenced_by_name: 2`
* *Architecture:* `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.552
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` DATETIME
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `padder.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 22.12 | **LOC:** 41 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 21.552; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Guard Balance (formerly Safety Score) (72.0%), Complexity Load (formerly Cognitive Load) (31.9%), Connectivity (formerly Api Exposure) (3.5%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(Defensive Guards)** (Impact: 9.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 3 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 11
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 4`, `args: 1`, `func_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 5`
* *Architecture:* `io: 4`, `api: 1`, `import: 1`
* *Defense:* `safety: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.552
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` getopt, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `win/run-ut.cmd` (BATCH | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 17.32 | **LOC:** 183 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.552
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `win/compile.cmd` (BATCH | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 16.66 | **LOC:** 138 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.552
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `prepare` (SHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 16.18 | **LOC:** 36 | **CtrlFlow:** 5.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.2%), Guard Balance (formerly Safety Score) (76.9%), Complexity Load (formerly Cognitive Load) (16.2%), Connectivity (formerly Api Exposure) (7.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Anonymous_Block` **(Unclassified)** (Impact: 2.4)
  * `__global_context__` **(Unclassified)** (Impact: 2.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 8
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 7`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `api: 3`
* *Defense:* `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.552
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `win/setenv.cmd` (BATCH | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 15.34 | **LOC:** 49 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.552
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/cobol/CALLDEMO.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 11.74 | **LOC:** 43 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.8%), Mutation Surface (formerly State Flux) (91.7%), Guard Balance (formerly Safety Score) (70.2%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `1000-BASIC-CALL` **(State Mutators)** (Impact: 1.4)
  * `2000-CLASSIC-CALL` **(State Mutators)** (Impact: 1.3)
  * `3000-DYNAMIC-CALL` **(State Mutators)** (Impact: 1.3)
  * `9999-END` **(I/O & Config Routines)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 6`, `args: 6`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 6`, `unreferenced_by_name: 4`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.552
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/cobol/SAMPLE.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 10.92 | **LOC:** 27 | **CtrlFlow:** 9.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (92.4%), Mutation Surface (formerly State Flux) (91.7%), Guard Balance (formerly Safety Score) (70.2%), Complexity Load (formerly Cognitive Load) (13.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `2000-SPEAK` **(I/O & Config Routines)** (Impact: 3.4)
  * `9999-END` **(I/O & Config Routines)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 6`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 2`, `unreferenced_by_name: 2`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.552
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/cobol/copy/ZUTZCPD.CPY` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 10.38 | **LOC:** 279 | **CtrlFlow:** 20.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (92.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (63.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `UT-ASSERT-ACCESSES` **(I/O & Config Routines)** (Impact: 18.1)
  * `UT-LOOKUP-MOCK` **(I/O & Config Routines)** (Impact: 13.9)
  * `UT-SET-MOCK` **(I/O & Config Routines)** (Impact: 6.8)
  * `UT-COMPARE` **(I/O & Config Routines)** (Impact: 5.7)
  * `UT-REVERSE-RESULT` **(I/O & Config Routines)** (Impact: 4.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 37 instances
* *State Mutation (weighted view):* 127
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 49`, `func_start: 13`
* *Risk/State:* `state_mutation: 53`, `unreferenced_by_name: 4`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.552
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `run-examples` (SHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 8.52 | **LOC:** 73 | **CtrlFlow:** 7.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Dead Code Surface (formerly Dead Code) (95.9%), Complexity Load (formerly Cognitive Load) (6.4%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__global_context__` **(Unclassified)** (Impact: 7.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`
* *Risk/State:* `dead_code: 5`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.552
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/cobol/MOCKDEMO.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 8.34 | **LOC:** 64 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Guard Balance (formerly Safety Score) (62.6%), Mutation Surface (formerly State Flux) (31.0%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `0100-OPEN-INPUT` **(I/O & Config Routines)** (Impact: 1.1)
  * `0200-READ-INPUT-FILE` **(I/O & Config Routines)** (Impact: 1.1)
  * `1000-PARA-A` **(I/O & Config Routines)** (Impact: 1.1)
  * `2000-PARA-B` **(I/O & Config Routines)** (Impact: 1.1)
  * `9999-END` **(I/O & Config Routines)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 7`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 2`, `unreferenced_by_name: 5`
* *Architecture:* `io: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.552
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/cobol/PARADEMO.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 8.34 | **LOC:** 64 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Guard Balance (formerly Safety Score) (62.6%), Mutation Surface (formerly State Flux) (31.0%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `0100-OPEN-INPUT` **(I/O & Config Routines)** (Impact: 1.1)
  * `0200-READ-INPUT-FILE` **(I/O & Config Routines)** (Impact: 1.1)
  * `1000-PARA-A` **(I/O & Config Routines)** (Impact: 1.1)
  * `2000-PARA-B` **(I/O & Config Routines)** (Impact: 1.1)
  * `9999-END` **(I/O & Config Routines)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 7`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 2`, `unreferenced_by_name: 5`
* *Architecture:* `io: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.552
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

- `src/main/cobol/CALLDEMO.CBL` -> **Severity: 2155.2** (Blast Radius: 21.552 * Doc Risk: 100.0%)
- `src/main/cobol/CARD1.CBL` -> **Severity: 2155.2** (Blast Radius: 21.552 * Doc Risk: 100.0%)
- `src/main/cobol/CARD2.CBL` -> **Severity: 2155.2** (Blast Radius: 21.552 * Doc Risk: 100.0%)
- `src/main/cobol/CARD2D.CBL` -> **Severity: 2155.2** (Blast Radius: 21.552 * Doc Risk: 100.0%)
- `src/main/cobol/CARD3.CBL` -> **Severity: 2155.2** (Blast Radius: 21.552 * Doc Risk: 100.0%)

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
