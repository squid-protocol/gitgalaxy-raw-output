# ARCHITECTURAL_BRIEF: Cobol-Projects
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/dscobol/Cobol-Projects.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 301 analyzed artifact(s), 28731 LOC.
- **Load-bearing artifact:** `Mainframe/ZOS/Zowe/Simple_Report/COPYBOOK/wsfst.cpy` -- 6 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `Mainframe/ZOS/Zowe/Simple_Report/JCL/ALLOCATE.jcl` -- pulls in 5 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `OpenCobol/ECBAP/cbl/tablena.cbl` at magnitude 332.64 (structural weight, not risk).
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
| Total Artifacts | 349 |
| Analyzed Artifacts (Scanned) | 301 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 48 |
| Total LOC | 28731 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 86.2% |
| Dominant Lang | COBOL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4444 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 2 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| COBOL | 174 | 23880 | 57.8% |
| PLAINTEXT | 51 | 0 | 16.9% |
| SHELL | 42 | 378 | 14.0% |
| JCL | 24 | 4425 | 8.0% |
| MARKDOWN | 6 | 0 | 2.0% |
| PYTHON | 4 | 48 | 1.3% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Mid Flat Project`
> **Architectural Drift Z-Score:** `2.344`
> **Composition Archetype:** `Mid Flat Project` (z +2.34; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules 27%, Declarative / Non-Code 26%, Data / Markup / Trivial 26%, Interface Declarations Files 19%, Large Core Modules (3) 1%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 244 | 81.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 57 | 18.9% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 48*

**Composition by Extension & Reason:**
- `.sh`: 11x Statistical Anomaly (Z-Score: -15565.38 < -5.00), 2x Statistical Anomaly (Z-Score: -11068.72 < -5.00), 1x Statistical Anomaly (Z-Score: -38048.72 < -5.00)
- `no_extension`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.cbl`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.dat`: 3x Excluded (Unsupported Extension: '.dat')
- `.cpy`: 3x Zero-Density Threshold (LOC: 102, Signals: 0)
- `.png`: 1x Excluded (Explicitly Denied Extension: '.png')
- `.txt`: 1x Excluded (Lexical Monotony: High structural repetition detected in 7423 LOC)
- `.csv`: 1x Excluded (Static Asset Blob without Intent: 1002 LOC)
- `.xls`: 1x Excluded (Explicitly Denied Extension: '.xls')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 95.1 | 17.2 | 9.3 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 95.3 | 62.9 | 74.7 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 99.1 | 19.7 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 9.4 | 2.4 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 11.2 | 0.5 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 67.4 | 91.7 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 23.1 | 0.8 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 59.3 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 75.3 | 1.5 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 29 | 13 | 0 | `OpenCobol/ECBAP/cbl/TABLOAD1.cbl` |
| cleanup | 137 | 100 | 2 | `Mainframe/ZOS/Zowe/Simple_Report/JCL/ALLOCATE.jcl` |
| guards | 31 | 19 | 0 | `OpenCobol/ECBAP/cbl/HOSPEDIT.cbl` |
| danger | 438 | 189 | 4 | `Mainframe/ZOS/ECBAP/cbl/WS162E.cbl` |
| concurrency | 8 | 4 | 0 | `Mainframe/ZOS/Zowe/Simple_Report/JCL/ALLOCATE.jcl` |
| connectivity | 123 | 24 | 0 | `Mainframe/ZOS/ECBAP/cbl/TABLE1.cbl` |
| io | 1693 | 124 | 19 | `Mainframe/ZOS/ECBAP/cbl/WS162E.cbl` |
| crypto | 0 | 0 | 0 | - |
| ipc | 38 | 11 | 0 | `Mainframe/ZOS/ECBAP/cbl/SUB01.cbl` |
| time | 123 | 37 | 3 | `Mainframe/ZOS/ECBAP/cbl/WS120.cbl` |
| serialization | 36 | 14 | 0 | `OpenCobol/ECBAP/cbl/TRIM1.cbl` |
| regex | 133 | 41 | 1 | `OpenCobol/ECBAP/cbl/INSPECT1.cbl` |
| events | 20 | 14 | 0 | `Mainframe/MVS/Utilities/jcl/allocate.jcl` |
| tests | 0 | 0 | 0 | - |
| docs | 19 | 9 | 0 | `OpenCobol/ECBAP/cbl/HOSPEDIT.cbl` |
| debt | 1974 | 151 | 11 | `Mainframe/ZOS/ECBAP/cbl/TABLEWA.cbl` |
| mutation | 3425 | 210 | 32 | `Mainframe/ZOS/ECBAP/cbl/WS81E.cbl` |
| dead_code | 196 | 114 | 2 | `pgm_templates/CICS/basecics.cbl` |
| credential | 8 | 7 | 0 | `Mainframe/MVS/herc01/jcl/VSIOINST.JCL` |
| threat | 109 | 32 | 1 | `pgm_templates/CICS/basecics.cbl` |
| ml_ai | 112 | 17 | 0 | `Mainframe/ZOS/ECBAP/cbl/TABLE2.cbl` |
| ui | 13 | 3 | 0 | `pgm_templates/CICS/basecics.cbl` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `Mainframe/ZOS/ECBAP/cbl/WS162E.cbl` (Hits: 49)
- `OpenCobol/ECBAP/cbl/ws162e.cbl` (Hits: 49)
- `OpenCobol/ECBAP/cbl/ws162o.cbl` (Hits: 44)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **wsfst.cpy** (`Mainframe/ZOS/Zowe/Simple_Report/COPYBOOK/wsfst.cpy`) — 6 inbound connections
2. **PATIENT.cpy** (`common/cpy/PATIENT.cpy`) — 3 inbound connections
3. **blue.py** (`Extra-Stuff/Blue/blue.py`) — 0 inbound connections
4. **mvt-convert.py** (`Extra-Stuff/MVT-Convert/mvt-convert.py`) — 0 inbound connections
5. **unnum.py** (`Extra-Stuff/UnNumRight/unnum.py`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **ALLOCATE.jcl** (`Mainframe/ZOS/Zowe/Simple_Report/JCL/ALLOCATE.jcl`) — 5 outbound dependencies
2. **VSIOINST.JCL** (`Mainframe/MVS/herc01/jcl/VSIOINST.JCL`) — 4 outbound dependencies
3. **allocate.jcl** (`Mainframe/ZOS/Zowe/Initialize/JCL/allocate.jcl`) — 4 outbound dependencies
4. **calctest.cbl** (`pgm_templates/CICS/calctest.cbl`) — 4 outbound dependencies
5. **EXE4.jcl** (`Mainframe/ZOS/Normal/jcl/EXE4.jcl`) — 3 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `2000-Process` **(I/O & Config Routines)** (@ `Mainframe/ZOS/ECBAP/cbl/TABLE1.cbl`) -> Impact: **70.1** | LOC: 322
- `2900-Display-The-Tables` **(Compute Cores)** (@ `Mainframe/ZOS/ECBAP/cbl/TABLENA.cbl`) -> Impact: **43.6** | LOC: 193
- `2900-Display-The-Tables` **(Compute Cores)** (@ `Mainframe/ZOS/ECBAP/cbl/TABLEWA.cbl`) -> Impact: **43.6** | LOC: 193
- `2900-Display-The-Tables` **(Compute Cores)** (@ `OpenCobol/ECBAP/cbl/tablena.cbl`) -> Impact: **43.6** | LOC: 193
- `2900-Display-The-Tables` **(Compute Cores)** (@ `OpenCobol/ECBAP/cbl/tablewa.cbl`) -> Impact: **43.6** | LOC: 193
- `2200-Do-Some-Searching` **(I/O & Config Routines)** (@ `OpenCobol/ECBAP/cbl/tablena.cbl`) -> Impact: **39.4** | LOC: 207
- `2200-Do-Some-Searching` **(I/O & Config Routines)** (@ `OpenCobol/ECBAP/cbl/tablewa.cbl`) -> Impact: **39.4** | LOC: 207
- `2200-Do-Some-Searching` **(I/O & Config Routines)** (@ `Mainframe/ZOS/ECBAP/cbl/TABLENA.cbl`) -> Impact: **39.0** | LOC: 200
- `2200-Do-Some-Searching` **(I/O & Config Routines)** (@ `Mainframe/ZOS/ECBAP/cbl/TABLEWA.cbl`) -> Impact: **39.0** | LOC: 200
- `2120-Calculate-Inst-Price` **(I/O & Config Routines)** (@ `Mainframe/ZOS/ECBAP/cbl/WS81C.cbl`) -> Impact: **36.6** | LOC: 73

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **I/O & Config Routines**: dominated by I/O and configuration handling

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `OpenCobol/ECBAP/cbl` | 59 | 3817.72 | 19.67% | 11.25% |
| `Mainframe/ZOS/ECBAP/cbl` | 25 | 2943.16 | 27.22% | 14.38% |
| `OpenCobol/dastagg/cbl` | 28 | 930.26 | 20.19% | 60.8% |
| `Mainframe/ZOS/Normal/cbl` | 16 | 601.56 | 28.36% | 46.1% |
| `OpenCobol/ECBAP/jcl` | 29 | 312.52 | 9.27% | 0.0% |
| `pgm_templates/CICS` | 3 | 277.62 | 59.4% | 40.0% |
| `OpenCobol/prod/cbl` | 11 | 264.2 | 22.85% | 38.59% |
| `Mainframe/MVS/herc03/cbl` | 6 | 148.84 | 30.23% | 49.59% |
| `Mainframe/ZOS/Internal-Sort/cbl` | 5 | 144.94 | 15.34% | 39.17% |
| `OpenCobol/Internal-Sort/cbl` | 5 | 144.94 | 15.34% | 39.17% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `OpenCobol/ECBAP/cbl/ws532.cbl` -> **99.131%** Exposure
- `pgm_templates/Batch/slt_base_ibm_batch.cob` -> **98.9013%** Exposure
- `Mainframe/ZOS/ECBAP/cbl/WS532.cbl` -> **98.7568%** Exposure
- `OpenCobol/ECBAP/cbl/FAVRPT.cbl` -> **98.7568%** Exposure
- `Mainframe/MVS/herc03/cbl/cbl0001.cbl` -> **96.2229%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `OpenCobol/ECBAP/cbl/FAHR2CEL.cbl` -> **100.0%** Exposure
- `OpenCobol/ECBAP/cbl/INTEG1.cbl` -> **100.0%** Exposure
- `pgm_templates/CICS/calctest.cbl` -> **100.0%** Exposure
- `Mainframe/MVS/herc03/cbl/BDS0704.cbl` -> **99.9999%** Exposure
- `pgm_templates/CICS/basecics.cbl` -> **99.9998%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `OpenCobol/dastagg/cbl/CBL0008.cbl` -> **5** Orphaned Functions | **0** Duplicates
- `OpenCobol/dastagg/cbl/CBL0009.cbl` -> **5** Orphaned Functions | **0** Duplicates
- `OpenCobol/dastagg/cbl/CBL0010.cbl` -> **5** Orphaned Functions | **0** Duplicates
- `OpenCobol/dastagg/cbl/CBL0011.cbl` -> **5** Orphaned Functions | **0** Duplicates
- `OpenCobol/dastagg/cbl/CBL0012.cbl` -> **5** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `OpenCobol/ECBAP/cbl/ws81c.cbl` -> **75.3102%** Exposure
- `Mainframe/ZOS/ECBAP/cbl/WS81C.cbl` -> **73.5779%** Exposure
- `OpenCobol/ECBAP/cbl/ws81d.cbl` -> **61.0229%** Exposure
- `Mainframe/ZOS/ECBAP/cbl/WS81D.cbl` -> **59.2107%** Exposure
- `Mainframe/ZOS/ECBAP/cbl/WS81E.cbl` -> **49.6269%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `112` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `OpenCobol/ECBAP/cbl/tablena.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 332.64 | **LOC:** 1244 | **CtrlFlow:** 10.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (95.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.6%), Complexity Load (formerly Cognitive Load) (29.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `2900-Display-The-Tables` **(Compute Cores)** (Impact: 43.6)
  * `2200-Do-Some-Searching` **(I/O & Config Routines)** (Impact: 39.4)
  * `WS-Show-Number` **(I/O & Config Routines)** (Impact: 14.5)
  * `WS-Company-Counter` **(I/O & Config Routines)** (Impact: 11.4)
  * `WS-Company-Total` **(I/O & Config Routines)** (Impact: 8.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 35 instances
* *State Mutation (weighted view):* 142
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 113`, `structural_boundaries: 332`, `args: 28`, `func_start: 21`, `class_start: 1`
* *Risk/State:* `state_mutation: 72`, `unreferenced_by_name: 1`
* *Architecture:* `api: 14`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.962
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Mainframe/ZOS/ECBAP/cbl/TABLENA.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 331.96 | **LOC:** 1235 | **CtrlFlow:** 11.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (95.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.8%), Complexity Load (formerly Cognitive Load) (29.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `2900-Display-The-Tables` **(Compute Cores)** (Impact: 43.6)
  * `2200-Do-Some-Searching` **(I/O & Config Routines)** (Impact: 39.0)
  * `WS-Show-Number` **(I/O & Config Routines)** (Impact: 14.5)
  * `WS-Company-Counter` **(I/O & Config Routines)** (Impact: 11.4)
  * `WS-Company-Total` **(I/O & Config Routines)** (Impact: 8.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 35 instances
* *State Mutation (weighted view):* 142
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 113`, `structural_boundaries: 331`, `args: 28`, `func_start: 21`, `class_start: 1`
* *Risk/State:* `state_mutation: 72`, `unreferenced_by_name: 1`
* *Architecture:* `api: 14`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.962
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Mainframe/ZOS/ECBAP/cbl/WS81E.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 303.2 | **LOC:** 710 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `2120-Calculate-Inst-Price` **(I/O & Config Routines)** (Impact: 36.6)
  * `5100-Read-RFPIN` **(I/O & Config Routines)** (Impact: 6.7)
  * `2110-Move-Fixed-Fields` **(I/O & Config Routines)** (Impact: 6.2)
  * `2130-Calculate-Shipping` **(I/O & Config Routines)** (Impact: 5.6)
  * `2100-Create-RFP` **(I/O & Config Routines)** (Impact: 4.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 45 instances
* *State Mutation (weighted view):* 176
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 79`, `func_start: 29`, `class_start: 1`
* *Risk/State:* `state_mutation: 86`, `dead_code: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 40`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.962
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `OpenCobol/ECBAP/cbl/ws81e.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 303.2 | **LOC:** 702 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `2120-Calculate-Inst-Price` **(I/O & Config Routines)** (Impact: 36.6)
  * `5100-Read-RFPIN` **(I/O & Config Routines)** (Impact: 6.7)
  * `2110-Move-Fixed-Fields` **(I/O & Config Routines)** (Impact: 6.2)
  * `2130-Calculate-Shipping` **(I/O & Config Routines)** (Impact: 5.6)
  * `2100-Create-RFP` **(I/O & Config Routines)** (Impact: 4.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 45 instances
* *State Mutation (weighted view):* 176
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 79`, `func_start: 29`, `class_start: 1`
* *Risk/State:* `state_mutation: 86`, `dead_code: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 40`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.962
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Mainframe/ZOS/ECBAP/cbl/WS81D.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 283.06 | **LOC:** 626 | **CtrlFlow:** 12.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (85.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `2120-Calculate-Inst-Price` **(I/O & Config Routines)** (Impact: 36.6)
  * `5100-Read-RFPIN` **(I/O & Config Routines)** (Impact: 6.7)
  * `2110-Move-Fixed-Fields` **(I/O & Config Routines)** (Impact: 6.2)
  * `2130-Calculate-Shipping` **(I/O & Config Routines)** (Impact: 5.6)
  * `2100-Create-RFP` **(I/O & Config Routines)** (Impact: 4.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 43 instances
* *State Mutation (weighted view):* 162
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 73`, `func_start: 28`, `class_start: 1`
* *Risk/State:* `state_mutation: 76`, `dead_code: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 30`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.962
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `OpenCobol/ECBAP/cbl/ws81d.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 282.8 | **LOC:** 627 | **CtrlFlow:** 12.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (85.9%), Complexity Load (formerly Cognitive Load) (80.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `2120-Calculate-Inst-Price` **(I/O & Config Routines)** (Impact: 36.6)
  * `5100-Read-RFPIN` **(I/O & Config Routines)** (Impact: 6.7)
  * `2110-Move-Fixed-Fields` **(I/O & Config Routines)** (Impact: 6.2)
  * `2130-Calculate-Shipping` **(I/O & Config Routines)** (Impact: 5.6)
  * `2100-Create-RFP` **(I/O & Config Routines)** (Impact: 4.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 43 instances
* *State Mutation (weighted view):* 162
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 73`, `func_start: 28`, `class_start: 1`
* *Risk/State:* `state_mutation: 76`, `dead_code: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 30`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.962
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `OpenCobol/ECBAP/cbl/tablewa.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 266.66 | **LOC:** 1198 | **CtrlFlow:** 9.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (82.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.7%), Complexity Load (formerly Cognitive Load) (20.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `2900-Display-The-Tables` **(Compute Cores)** (Impact: 43.6)
  * `2200-Do-Some-Searching` **(I/O & Config Routines)** (Impact: 39.4)
  * `WS-Show-Number` **(I/O & Config Routines)** (Impact: 7.8)
  * `WS-Company-Total` **(I/O & Config Routines)** (Impact: 7.2)
  * `WS-Company-Total` **(I/O & Config Routines)** (Impact: 6.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 23 instances
* *State Mutation (weighted view):* 99
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 94`, `structural_boundaries: 300`, `args: 34`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `state_mutation: 53`, `unreferenced_by_name: 1`
* *Architecture:* `api: 14`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.962
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Mainframe/ZOS/ECBAP/cbl/TABLEWA.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 265.98 | **LOC:** 1189 | **CtrlFlow:** 9.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (83.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.9%), Complexity Load (formerly Cognitive Load) (20.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `2900-Display-The-Tables` **(Compute Cores)** (Impact: 43.6)
  * `2200-Do-Some-Searching` **(I/O & Config Routines)** (Impact: 39.0)
  * `WS-Show-Number` **(I/O & Config Routines)** (Impact: 7.8)
  * `WS-Company-Total` **(I/O & Config Routines)** (Impact: 7.2)
  * `WS-Company-Total` **(I/O & Config Routines)** (Impact: 6.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 23 instances
* *State Mutation (weighted view):* 99
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 94`, `structural_boundaries: 300`, `args: 34`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `state_mutation: 53`, `unreferenced_by_name: 1`
* *Architecture:* `api: 14`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.962
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Mainframe/ZOS/ECBAP/cbl/WS162E.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 261.78 | **LOC:** 696 | **CtrlFlow:** 8.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 2.962; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (39.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `6135-Display-Ins-Type-Messages` **(Stateful Encapsulated Methods)** (Impact: 10.1)
  * `1015-Load-Type` **(I/O & Config Routines)** (Impact: 7.0)
  * `WS-OutFile-Patient-NAME` **(I/O & Config Routines)** (Impact: 6.9)
  * `5000-Read-INFILE` **(I/O & Config Routines)** (Impact: 6.7)
  * `1019-Verify-Type-Table` **(Interface Declarations)** (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 37 instances
* *State Mutation (weighted view):* 159
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 82`, `func_start: 30`, `class_start: 1`
* *Risk/State:* `state_mutation: 85`, `fragile_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 49`, `import: 8`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.962
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` PATIENT, WSDT, WSFST
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `OpenCobol/ECBAP/cbl/ws162e.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 261.78 | **LOC:** 696 | **CtrlFlow:** 8.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 2.962; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (39.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `6135-Display-Ins-Type-Messages` **(Stateful Encapsulated Methods)** (Impact: 10.1)
  * `1015-Load-Type` **(I/O & Config Routines)** (Impact: 7.0)
  * `WS-OutFile-Patient-NAME` **(I/O & Config Routines)** (Impact: 6.9)
  * `5000-Read-INFILE` **(I/O & Config Routines)** (Impact: 6.7)
  * `1019-Verify-Type-Table` **(Interface Declarations)** (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 37 instances
* *State Mutation (weighted view):* 159
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 82`, `func_start: 30`, `class_start: 1`
* *Risk/State:* `state_mutation: 85`, `fragile_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 49`, `import: 8`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.962
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` PATIENT, WSDT, WSFST
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Mainframe/ZOS/ECBAP/cbl/TABLE1.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 212.24 | **LOC:** 639 | **CtrlFlow:** 14.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 2.962; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.2%), Complexity Load (formerly Cognitive Load) (39.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `2000-Process` **(I/O & Config Routines)** (Impact: 70.1)
  * `1015-Load-Type` **(I/O & Config Routines)** (Impact: 7.0)
  * `1099-Verify-Type-Table` **(Interface Declarations)** (Impact: 4.7)
  * `1010-Load-Type-Table` **(I/O & Config Routines)** (Impact: 2.4)
  * `1100-Load-Other-Tables` **(I/O & Config Routines)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 88
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 220`, `args: 4`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 48`, `dead_code: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 7`, `api: 24`, `import: 1`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.962
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` WSFST
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Mainframe/ZOS/ECBAP/cbl/WS81C.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 204.94 | **LOC:** 508 | **CtrlFlow:** 11.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `2120-Calculate-Inst-Price` **(I/O & Config Routines)** (Impact: 36.6)
  * `5100-Read-RFPIN` **(I/O & Config Routines)** (Impact: 6.7)
  * `2110-Move-Fixed-Fields` **(I/O & Config Routines)** (Impact: 6.2)
  * `2130-Calculate-Shipping` **(I/O & Config Routines)** (Impact: 5.6)
  * `6000-Write-Proposal` **(Interface Declarations)** (Impact: 3.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 114
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 47`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `state_mutation: 60`, `dead_code: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 32`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.962
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `OpenCobol/ECBAP/cbl/ws81c.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 204.72 | **LOC:** 523 | **CtrlFlow:** 11.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `2120-Calculate-Inst-Price` **(I/O & Config Routines)** (Impact: 36.6)
  * `5100-Read-RFPIN` **(I/O & Config Routines)** (Impact: 6.7)
  * `2110-Move-Fixed-Fields` **(I/O & Config Routines)** (Impact: 6.2)
  * `2130-Calculate-Shipping` **(I/O & Config Routines)** (Impact: 5.6)
  * `6000-Write-Proposal` **(Interface Declarations)** (Impact: 3.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 114
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 47`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `state_mutation: 60`, `dead_code: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 32`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.962
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `OpenCobol/ECBAP/cbl/HOSPEDIT.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 174.36 | **LOC:** 488 | **CtrlFlow:** 5.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.9%), Complexity Load (formerly Cognitive Load) (65.1%), Dead Code Surface (formerly Dead Code) (5.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `100-MAINLINE` **(I/O & Config Routines)** (Impact: 20.9)
  * `WS-OUTPUT-REC` **(I/O & Config Routines)** (Impact: 3.9)
  * `INS-TYPE-O` **(I/O & Config Routines)** (Impact: 2.6)
  * `200-CLEANUP` **(I/O & Config Routines)** (Impact: 2.0)
  * `000-HOUSEKEEPING` **(I/O & Config Routines)** (Impact: 1.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 26 instances
* *State Mutation (weighted view):* 124
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 30`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 72`, `dead_code: 1`
* *Architecture:* `io: 38`
* *Defense:* `doc: 3`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.962
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `OpenCobol/ECBAP/cbl/ws172a.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 163.28 | **LOC:** 416 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 2.962; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (67.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `2120-Calculate-Grades` **(I/O & Config Routines)** (Impact: 9.4)
  * `R1-Student-Name` **(I/O & Config Routines)** (Impact: 8.8)
  * `5000-Read-STCOURS` **(I/O & Config Routines)** (Impact: 6.7)
  * `2110-Print-Stdt-Total-Report` **(I/O & Config Routines)** (Impact: 4.0)
  * `6200-Write-ERRFILE` **(I/O & Config Routines)** (Impact: 3.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 26 instances
* *State Mutation (weighted view):* 101
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 51`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `state_mutation: 49`, `unreferenced_by_name: 1`
* *Architecture:* `io: 38`, `import: 4`
* *Defense:* `safety: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.962
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` WSDT, WSFST
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Mainframe/ZOS/ECBAP/cbl/WS172A.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 163.26 | **LOC:** 416 | **CtrlFlow:** 9.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 2.962; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (67.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `2120-Calculate-Grades` **(I/O & Config Routines)** (Impact: 9.4)
  * `R1-Student-Name` **(I/O & Config Routines)** (Impact: 8.8)
  * `5000-Read-STCOURS` **(I/O & Config Routines)** (Impact: 6.7)
  * `2110-Print-Stdt-Total-Report` **(I/O & Config Routines)** (Impact: 4.0)
  * `6200-Write-ERRFILE` **(I/O & Config Routines)** (Impact: 3.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 26 instances
* *State Mutation (weighted view):* 101
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 51`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `state_mutation: 49`, `unreferenced_by_name: 1`
* *Architecture:* `io: 38`, `import: 4`
* *Defense:* `safety: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.962
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` WSDT, WSFST
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pgm_templates/CICS/basecics.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 157.82 | **LOC:** 336 | **CtrlFlow:** 10.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (95.1%), Guard Balance (formerly Safety Score) (90.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `WCM-A-HOURLY-WAGE` **(I/O & Config Routines)** (Impact: 16.2)
  * `0000-MAINLINE` **(I/O & Config Routines)** (Impact: 6.8)
  * `5500-COMPUTE-RESULTS` **(I/O & Config Routines)** (Impact: 6.3)
  * `1000-RECIEVE-MAP` **(I/O & Config Routines)** (Impact: 6.2)
  * `0500-NORMAL-PROCESSING` **(Interface Declarations)** (Impact: 2.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 99
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 21`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `state_mutation: 61`, `dead_code: 2`, `unreferenced_by_name: 5`
* *Architecture:* `api: 1`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.962
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Mainframe/ZOS/ECBAP/cbl/WS120.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 144.3 | **LOC:** 387 | **CtrlFlow:** 7.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 2.962; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (36.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `2112-Check-Deductible` **(I/O & Config Routines)** (Impact: 10.1)
  * `5100-Read-INSClaim` **(I/O & Config Routines)** (Impact: 6.7)
  * `2120-Move-Fixed-Fields` **(Stateful Encapsulated Methods)** (Impact: 5.8)
  * `2111-Check-Benefit-Date` **(I/O & Config Routines)** (Impact: 3.8)
  * `2100-Process-Claims` **(I/O & Config Routines)** (Impact: 3.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 87
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 44`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `state_mutation: 43`, `unreferenced_by_name: 1`
* *Architecture:* `io: 32`, `import: 4`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.962
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CLAIMREC, WSDT, WSFST
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Mainframe/ZOS/ECBAP/cbl/WS193.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 144.3 | **LOC:** 387 | **CtrlFlow:** 7.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 2.962; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (36.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `2112-Check-Deductible` **(I/O & Config Routines)** (Impact: 10.1)
  * `5100-Read-INSClaim` **(I/O & Config Routines)** (Impact: 6.7)
  * `2120-Move-Fixed-Fields` **(Stateful Encapsulated Methods)** (Impact: 5.8)
  * `2111-Check-Benefit-Date` **(I/O & Config Routines)** (Impact: 3.8)
  * `2100-Process-Claims` **(I/O & Config Routines)** (Impact: 3.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 87
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 44`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `state_mutation: 43`, `unreferenced_by_name: 1`
* *Architecture:* `io: 32`, `import: 4`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.962
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CLAIMREC, WSDT, WSFST
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `OpenCobol/ECBAP/cbl/ws120.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 144.3 | **LOC:** 387 | **CtrlFlow:** 7.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 2.962; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (36.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `2112-Check-Deductible` **(I/O & Config Routines)** (Impact: 10.1)
  * `5100-Read-INSClaim` **(I/O & Config Routines)** (Impact: 6.7)
  * `2120-Move-Fixed-Fields` **(Stateful Encapsulated Methods)** (Impact: 5.8)
  * `2111-Check-Benefit-Date` **(I/O & Config Routines)** (Impact: 3.8)
  * `2100-Process-Claims` **(I/O & Config Routines)** (Impact: 3.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 87
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 44`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `state_mutation: 43`, `unreferenced_by_name: 1`
* *Architecture:* `io: 32`, `import: 4`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.962
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CLAIMREC, WSDT, WSFST
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `OpenCobol/ECBAP/cbl/TABLE1.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 130.98 | **LOC:** 449 | **CtrlFlow:** 11.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 2.962; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (70.8%), Complexity Load (formerly Cognitive Load) (31.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `2000-Process` **(I/O & Config Routines)** (Impact: 35.8)
  * `1015-Load-Type` **(I/O & Config Routines)** (Impact: 7.0)
  * `1099-Verify-Type-Table` **(Interface Declarations)** (Impact: 4.7)
  * `1010-Load-Type-Table` **(Interface Declarations)** (Impact: 2.3)
  * `0000-Mainline` **(Interface Declarations)** (Impact: 1.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 55
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 154`, `args: 4`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 25`, `unreferenced_by_name: 1`
* *Architecture:* `io: 6`, `api: 14`, `import: 1`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.962
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` WSFST
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `OpenCobol/ECBAP/cbl/ws162o.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 130.12 | **LOC:** 483 | **CtrlFlow:** 6.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 2.962; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (70.4%), Complexity Load (formerly Cognitive Load) (25.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `1015-Load-Type` **(I/O & Config Routines)** (Impact: 7.0)
  * `5100-Read-INFILE` **(I/O & Config Routines)** (Impact: 6.7)
  * `1099-Verify-Type-Table` **(Interface Declarations)** (Impact: 4.7)
  * `2100-Process-INFile-Records` **(I/O & Config Routines)** (Impact: 4.2)
  * `FD-OutFile-Patient-Record` **(Interface Declarations)** (Impact: 3.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 56
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 76`, `func_start: 32`, `class_start: 1`
* *Risk/State:* `state_mutation: 32`, `unreferenced_by_name: 2`
* *Architecture:* `io: 44`, `import: 9`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.962
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` PATIENT, WSDT, WSFST
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pgm_templates/CICS/calctest.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 117.76 | **LOC:** 240 | **CtrlFlow:** 10.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 2.962; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (93.9%), Complexity Load (formerly Cognitive Load) (83.1%), Debt Markers (formerly Tech Debt) (15.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `WCM-A-HOURLY-WAGE` **(I/O & Config Routines)** (Impact: 23.9)
  * `WCM-A-LAST-NAME` **(I/O & Config Routines)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 88
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 7`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 50`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.962
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AVDEFN, CICSERC, DFHAID, WAGEMAP
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `OpenCobol/ECBAP/cbl/tabldna.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 111.3 | **LOC:** 366 | **CtrlFlow:** 11.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 2.962; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.5%), Complexity Load (formerly Cognitive Load) (49.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `2200-Do-Some-Searching` **(I/O & Config Routines)** (Impact: 12.2)
  * `1013-Load-Employees` **(I/O & Config Routines)** (Impact: 6.8)
  * `1113-Load-Students` **(I/O & Config Routines)** (Impact: 6.8)
  * `1019-Verify-Emp-Table` **(Interface Declarations)** (Impact: 4.7)
  * `1119-Verify-Student-Table` **(Interface Declarations)** (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 55
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 66`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `state_mutation: 31`, `unreferenced_by_name: 1`
* *Architecture:* `io: 8`, `import: 2`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.962
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` WSFST
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `OpenCobol/ECBAP/cbl/ws182.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 109.2 | **LOC:** 390 | **CtrlFlow:** 4.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 2.962; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.7%), Guard Balance (formerly Safety Score) (77.2%), Complexity Load (formerly Cognitive Load) (38.5%), Debt Markers (formerly Tech Debt) (11.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `5000-Read-ACCTREC` **(I/O & Config Routines)** (Impact: 6.7)
  * `2000-Process` **(I/O & Config Routines)** (Impact: 5.8)
  * `2910-Print-Detail-Line` **(I/O & Config Routines)** (Impact: 4.8)
  * `6100-Write-R1` **(Interface Declarations)** (Impact: 3.4)
  * `6130-Write-R1-Footer` **(I/O & Config Routines)** (Impact: 3.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 63
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 43`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `state_mutation: 47`, `dead_code: 2`, `unreferenced_by_name: 1`
* *Architecture:* `io: 34`, `import: 3`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.962
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` WSDT, WSFST
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

- `Mainframe/MVS/Utilities/jcl/allocate.jcl` -> **Severity: 296.2** (Blast Radius: 2.962 * Doc Risk: 100.0%)
- `Mainframe/MVS/herc01/jcl/VSIOINST.JCL` -> **Severity: 296.2** (Blast Radius: 2.962 * Doc Risk: 100.0%)
- `Mainframe/MVS/herc01/jcl/VSTEST01.JCL` -> **Severity: 296.2** (Blast Radius: 2.962 * Doc Risk: 100.0%)
- `Mainframe/MVS/herc03/jcl/BDS0702.jcl` -> **Severity: 296.2** (Blast Radius: 2.962 * Doc Risk: 100.0%)
- `Mainframe/MVS/herc03/jcl/BDS0704.jcl` -> **Severity: 296.2** (Blast Radius: 2.962 * Doc Risk: 100.0%)

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
