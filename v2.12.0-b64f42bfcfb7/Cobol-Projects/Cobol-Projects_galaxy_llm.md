# ARCHITECTURAL_BRIEF: Cobol-Projects
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/dscobol/Cobol-Projects.git` |
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
- **Scope:** 306 analyzed artifact(s), 28268 LOC.
- **Load-bearing artifact:** `OpenCobol/Internal-Sort/cpy/WSFST.cpy` -- 18 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `Mainframe/ZOS/Zowe/Simple_Report/JCL/ALLOCATE.jcl` -- pulls in 5 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `Mainframe/ZOS/ECBAP/cbl/WS81E.cbl` at magnitude 301.3 (structural weight, not risk).
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
| Analyzed Artifacts (Scanned) | 306 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 43 |
| Total LOC | 28268 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 87.7% |
| Dominant Lang | COBOL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7561 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0362 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0864 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 15 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| COBOL | 179 | 23417 | 58.5% |
| PLAINTEXT | 51 | 0 | 16.7% |
| SHELL | 42 | 378 | 13.7% |
| JCL | 24 | 4425 | 7.8% |
| MARKDOWN | 6 | 0 | 2.0% |
| PYTHON | 4 | 48 | 1.3% |

## 4.1 SOURCE ENCODINGS
All 306 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules 32%, Data / Markup / Trivial 25%, Interface Declarations Files 20%, Declarative / Non-Code 18%, Parameter Forwarders Files 2%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 249 | 81.4% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 57 | 18.6% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 43*

**Composition by Extension & Reason:**
- `.sh`: 11x Statistical Anomaly (Z-Score: -15565.38 < -5.00), 2x Statistical Anomaly (Z-Score: -11068.72 < -5.00), 1x Statistical Anomaly (Z-Score: -38048.72 < -5.00)
- `no_extension`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.dat`: 3x Excluded (Unsupported Extension: '.dat')
- `.png`: 1x Excluded (Explicitly Denied Extension: '.png')
- `.txt`: 1x Excluded (Lexical Monotony: High structural repetition detected in 7423 LOC)
- `.csv`: 1x Excluded (Static Asset Blob without Intent: 1002 LOC)
- `.xls`: 1x Excluded (Explicitly Denied Extension: '.xls')
- `.cpy`: 1x Zero-Density Threshold (LOC: 102, Signals: 0)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 94.7 | 16.4 | 9.3 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 71.1 | 48.4 | 57.2 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 68.5 | 4.6 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 7.9 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 11.2 | 0.3 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 66.6 | 91.7 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 23.1 | 0.3 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 70.3 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 28 | 12 | 0 | `OpenCobol/ECBAP/cbl/TABLOAD1.cbl` |
| cleanup | 139 | 102 | 2 | `Mainframe/ZOS/Zowe/Simple_Report/JCL/ALLOCATE.jcl` |
| guards | 15 | 14 | 0 | `pgm_templates/CICS/basecics.cbl` |
| danger | 446 | 192 | 4 | `Mainframe/ZOS/ECBAP/cbl/WS162E.cbl` |
| concurrency | 8 | 4 | 0 | `Mainframe/ZOS/Zowe/Simple_Report/JCL/ALLOCATE.jcl` |
| connectivity | 61 | 18 | 0 | `Mainframe/ZOS/ECBAP/cbl/TABLE1.cbl` |
| io | 907 | 126 | 10 | `Mainframe/ZOS/ECBAP/cbl/WS162E.cbl` |
| crypto | 0 | 0 | 0 | - |
| ipc | 33 | 9 | 0 | `Mainframe/ZOS/ECBAP/cbl/SUB01.cbl` |
| time | 44 | 37 | 1 | `Mainframe/ZOS/ECBAP/cbl/WS120.cbl` |
| serialization | 20 | 14 | 0 | `OpenCobol/ECBAP/cbl/UNSTRNG.cbl` |
| regex | 133 | 42 | 1 | `OpenCobol/ECBAP/cbl/INSPECT1.cbl` |
| events | 20 | 14 | 0 | `Mainframe/MVS/Utilities/jcl/allocate.jcl` |
| tests | 0 | 0 | 0 | - |
| docs | 19 | 9 | 0 | `OpenCobol/ECBAP/cbl/HOSPEDIT.cbl` |
| debt | 1438 | 153 | 10 | `Mainframe/ZOS/ECBAP/cbl/TABLE1.cbl` |
| mutation | 3402 | 212 | 31 | `Mainframe/ZOS/ECBAP/cbl/WS81E.cbl` |
| dead_code | 67 | 25 | 0 | `OpenCobol/dastagg/cbl/CBL0011.cbl` |
| credential | 0 | 0 | 0 | - |
| threat | 34 | 1 | 0 | `Mainframe/ZOS/Normal/cbl/EXE4.cbl` |
| ml_ai | 112 | 17 | 0 | `Mainframe/ZOS/ECBAP/cbl/TABLE2.cbl` |
| ui | 13 | 3 | 0 | `pgm_templates/CICS/basecics.cbl` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `Mainframe/ZOS/ECBAP/cbl/WS162E.cbl` (Hits: 26)
- `OpenCobol/ECBAP/cbl/ws162e.cbl` (Hits: 26)
- `OpenCobol/ECBAP/cbl/HOSPEDIT.cbl` (Hits: 24)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **WSFST.cpy** (`OpenCobol/Internal-Sort/cpy/WSFST.cpy`) — 18 inbound connections
2. **wsfst.cpy** (`Mainframe/ZOS/Zowe/Simple_Report/COPYBOOK/wsfst.cpy`) — 7 inbound connections
3. **WSFST.cpy** (`Mainframe/ZOS/ECBAP/cpy/WSFST.cpy`) — 6 inbound connections
4. **WSDT.cpy** (`Mainframe/ZOS/ECBAP/cpy/WSDT.cpy`) — 5 inbound connections
5. **WSDT.cpy** (`common/cpy/WSDT.cpy`) — 5 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **ALLOCATE.jcl** (`Mainframe/ZOS/Zowe/Simple_Report/JCL/ALLOCATE.jcl`) — 5 outbound dependencies
2. **calctest.cbl** (`pgm_templates/CICS/calctest.cbl`) — 4 outbound dependencies
3. **VSIOINST.JCL** (`Mainframe/MVS/herc01/jcl/VSIOINST.JCL`) — 4 outbound dependencies
4. **allocate.jcl** (`Mainframe/ZOS/Zowe/Initialize/JCL/allocate.jcl`) — 4 outbound dependencies
5. **WS120.cbl** (`Mainframe/ZOS/ECBAP/cbl/WS120.cbl`) — 3 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `2000-Process` **(I/O & Config Routines)** (@ `Mainframe/ZOS/ECBAP/cbl/TABLE1.cbl`) -> Impact: **61.1** | LOC: 322
- `2100-Do-Some-Calculating` **(I/O & Config Routines)** (@ `Mainframe/ZOS/ECBAP/cbl/TABLENA.cbl`) -> Impact: **50.4** | LOC: 288
- `2100-Do-Some-Calculating` **(I/O & Config Routines)** (@ `OpenCobol/ECBAP/cbl/tablena.cbl`) -> Impact: **50.4** | LOC: 288
- `2200-Do-Some-Searching` **(I/O & Config Routines)** (@ `OpenCobol/ECBAP/cbl/tablena.cbl`) -> Impact: **39.4** | LOC: 207
- `2200-Do-Some-Searching` **(I/O & Config Routines)** (@ `OpenCobol/ECBAP/cbl/tablewa.cbl`) -> Impact: **39.4** | LOC: 207
- `2200-Do-Some-Searching` **(I/O & Config Routines)** (@ `Mainframe/ZOS/ECBAP/cbl/TABLENA.cbl`) -> Impact: **39.0** | LOC: 200
- `2200-Do-Some-Searching` **(I/O & Config Routines)** (@ `Mainframe/ZOS/ECBAP/cbl/TABLEWA.cbl`) -> Impact: **39.0** | LOC: 200
- `2120-Calculate-Inst-Price` **(I/O & Config Routines)** (@ `Mainframe/ZOS/ECBAP/cbl/WS81C.cbl`) -> Impact: **36.6** | LOC: 73
- `2120-Calculate-Inst-Price` **(I/O & Config Routines)** (@ `Mainframe/ZOS/ECBAP/cbl/WS81D.cbl`) -> Impact: **36.6** | LOC: 73
- `2120-Calculate-Inst-Price` **(I/O & Config Routines)** (@ `Mainframe/ZOS/ECBAP/cbl/WS81E.cbl`) -> Impact: **36.6** | LOC: 73

*Function archetypes referenced above:*
  * **I/O & Config Routines**: dominated by I/O and configuration handling

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `OpenCobol/ECBAP/cbl` | 59 | 3391.62 | 18.83% | 0.5% |
| `Mainframe/ZOS/ECBAP/cbl` | 25 | 2635.34 | 24.82% | 0.39% |
| `OpenCobol/dastagg/cbl` | 28 | 899.76 | 19.31% | 30.72% |
| `Mainframe/ZOS/Normal/cbl` | 16 | 591.72 | 26.87% | 9.85% |
| `OpenCobol/ECBAP/jcl` | 29 | 312.52 | 9.27% | 0.0% |
| `pgm_templates/CICS` | 3 | 281.02 | 59.27% | 7.11% |
| `OpenCobol/prod/cbl` | 11 | 250.6 | 22.61% | 0.0% |
| `Mainframe/ZOS/Internal-Sort/cbl` | 5 | 142.24 | 13.63% | 0.0% |
| `OpenCobol/Internal-Sort/cbl` | 5 | 142.24 | 13.63% | 0.0% |
| `Mainframe/MVS/herc03/cbl` | 6 | 136.44 | 30.23% | 11.42% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `Mainframe/MVS/herc03/cbl/cbl0001.cbl` -> **68.5397%** Exposure
- `Mainframe/ZOS/Normal/cbl/ODS000C.cbl` -> **68.5397%** Exposure
- `OpenCobol/dastagg/cbl/CBL0001.cbl` -> **68.5397%** Exposure
- `OpenCobol/dastagg/cbl/CBL0002.cbl` -> **68.5397%** Exposure
- `OpenCobol/dastagg/cbl/ODS0002.cbl` -> **68.5397%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `OpenCobol/ECBAP/cbl/FAHR2CEL.cbl` -> **100.0%** Exposure
- `OpenCobol/ECBAP/cbl/INTEG1.cbl` -> **100.0%** Exposure
- `pgm_templates/CICS/calctest.cbl` -> **100.0%** Exposure
- `Mainframe/MVS/herc03/cbl/BDS0704.cbl` -> **99.9999%** Exposure
- `pgm_templates/CICS/basecics.cbl` -> **99.9998%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `OpenCobol/dastagg/cbl/CBL0008.cbl` -> **4** Orphaned Functions | **0** Duplicates
- `OpenCobol/dastagg/cbl/CBL0009.cbl` -> **4** Orphaned Functions | **0** Duplicates
- `OpenCobol/dastagg/cbl/CBL0010.cbl` -> **4** Orphaned Functions | **0** Duplicates
- `OpenCobol/dastagg/cbl/CBL0011.cbl` -> **4** Orphaned Functions | **0** Duplicates
- `OpenCobol/dastagg/cbl/CBL0012.cbl` -> **4** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `113` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `Mainframe/ZOS/ECBAP/cbl/WS81E.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 7.578)
- **Top Global Matches:** file_cluster_11: 7.578, file_cluster_2: 8.067, file_cluster_15: 8.279
- **Magnitude:** 301.3 | **LOC:** 710 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (63.4%), Complexity Load (formerly Cognitive Load) (49.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `2120-Calculate-Inst-Price` **(I/O & Config Routines)** (Impact: 36.6)
  * `5100-Read-RFPIN` **(I/O & Config Routines)** (Impact: 6.8)
  * `2110-Move-Fixed-Fields` **(I/O & Config Routines)** (Impact: 6.2)
  * `2130-Calculate-Shipping` **(I/O & Config Routines)** (Impact: 5.6)
  * `2100-Create-RFP` **(I/O & Config Routines)** (Impact: 4.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 45 instances
* *State Mutation (weighted view):* 176
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 76`, `func_start: 27`, `class_start: 1`
* *Risk/State:* `state_mutation: 86`
* *Architecture:* `io: 18`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `OpenCobol/ECBAP/cbl/ws81e.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 7.576)
- **Top Global Matches:** file_cluster_11: 7.576, file_cluster_2: 8.069, file_cluster_15: 8.277
- **Magnitude:** 301.3 | **LOC:** 702 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (63.4%), Complexity Load (formerly Cognitive Load) (49.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `2120-Calculate-Inst-Price` **(I/O & Config Routines)** (Impact: 36.6)
  * `5100-Read-RFPIN` **(I/O & Config Routines)** (Impact: 6.8)
  * `2110-Move-Fixed-Fields` **(I/O & Config Routines)** (Impact: 6.2)
  * `2130-Calculate-Shipping` **(I/O & Config Routines)** (Impact: 5.6)
  * `2100-Create-RFP` **(I/O & Config Routines)** (Impact: 4.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 45 instances
* *State Mutation (weighted view):* 176
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 76`, `func_start: 27`, `class_start: 1`
* *Risk/State:* `state_mutation: 86`
* *Architecture:* `io: 18`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Mainframe/ZOS/ECBAP/cbl/WS81D.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 7.611)
- **Top Global Matches:** file_cluster_11: 7.611, file_cluster_2: 8.135, file_cluster_15: 8.316
- **Magnitude:** 281.26 | **LOC:** 626 | **CtrlFlow:** 12.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (78.5%), Guard Balance (formerly Safety Score) (64.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `2120-Calculate-Inst-Price` **(I/O & Config Routines)** (Impact: 36.6)
  * `5100-Read-RFPIN` **(I/O & Config Routines)** (Impact: 6.8)
  * `2110-Move-Fixed-Fields` **(I/O & Config Routines)** (Impact: 6.2)
  * `2130-Calculate-Shipping` **(I/O & Config Routines)** (Impact: 5.6)
  * `2100-Create-RFP` **(I/O & Config Routines)** (Impact: 4.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 43 instances
* *State Mutation (weighted view):* 162
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 70`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `state_mutation: 76`
* *Architecture:* `io: 12`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `OpenCobol/ECBAP/cbl/ws81d.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 7.613)
- **Top Global Matches:** file_cluster_11: 7.613, file_cluster_2: 8.147, file_cluster_15: 8.318
- **Magnitude:** 281.0 | **LOC:** 627 | **CtrlFlow:** 12.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (80.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `2120-Calculate-Inst-Price` **(I/O & Config Routines)** (Impact: 36.6)
  * `5100-Read-RFPIN` **(I/O & Config Routines)** (Impact: 6.8)
  * `2110-Move-Fixed-Fields` **(I/O & Config Routines)** (Impact: 6.2)
  * `2130-Calculate-Shipping` **(I/O & Config Routines)** (Impact: 5.6)
  * `2100-Create-RFP` **(I/O & Config Routines)** (Impact: 4.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 43 instances
* *State Mutation (weighted view):* 162
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 70`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `state_mutation: 76`
* *Architecture:* `io: 12`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Mainframe/ZOS/ECBAP/cbl/WS162E.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.301)
- **Top Global Matches:** file_cluster_11: 6.301, file_cluster_2: 6.839, file_cluster_15: 7.298
- **Magnitude:** 255.78 | **LOC:** 696 | **CtrlFlow:** 7.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 2.616; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (63.1%), Complexity Load (formerly Cognitive Load) (39.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `6135-Display-Ins-Type-Messages` **(Stateful Encapsulated Methods)** (Impact: 10.1)
  * `2110-Move-Static-Fields` **(I/O & Config Routines)** (Impact: 7.2)
  * `1015-Load-Type` **(I/O & Config Routines)** (Impact: 7.1)
  * `5000-Read-INFILE` **(I/O & Config Routines)** (Impact: 6.8)
  * `2181-Validate-INS-Type` **(I/O & Config Routines)** (Impact: 4.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 37 instances
* *State Mutation (weighted view):* 159
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 72`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `state_mutation: 85`, `fragile_debt: 1`
* *Architecture:* `io: 26`, `import: 8`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` PATIENT, WSDT, WSFST
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `OpenCobol/ECBAP/cbl/ws162e.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.342)
- **Top Global Matches:** file_cluster_11: 6.342, file_cluster_2: 6.886, file_cluster_15: 7.333
- **Magnitude:** 255.78 | **LOC:** 696 | **CtrlFlow:** 7.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 2.616; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (63.1%), Complexity Load (formerly Cognitive Load) (39.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `6135-Display-Ins-Type-Messages` **(Stateful Encapsulated Methods)** (Impact: 10.1)
  * `2110-Move-Static-Fields` **(I/O & Config Routines)** (Impact: 7.2)
  * `1015-Load-Type` **(I/O & Config Routines)** (Impact: 7.1)
  * `5000-Read-INFILE` **(I/O & Config Routines)** (Impact: 6.8)
  * `2181-Validate-INS-Type` **(I/O & Config Routines)** (Impact: 4.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 37 instances
* *State Mutation (weighted view):* 159
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 72`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `state_mutation: 85`, `fragile_debt: 1`
* *Architecture:* `io: 26`, `import: 8`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` PATIENT, WSDT, WSFST
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `OpenCobol/ECBAP/cbl/tablena.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 9.438)
- **Top Global Matches:** file_cluster_6: 9.438, file_cluster_8: 11.665, file_cluster_4: 16.019
- **Magnitude:** 243.4 | **LOC:** 1244 | **CtrlFlow:** 9.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (57.0%), Complexity Load (formerly Cognitive Load) (29.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `2100-Do-Some-Calculating` **(I/O & Config Routines)** (Impact: 50.4)
  * `2200-Do-Some-Searching` **(I/O & Config Routines)** (Impact: 39.4)
  * `2300-Do-Some-Searching-All` **(Interface Declarations)** (Impact: 4.1)
  * `2900-Display-The-Tables` **(Interface Declarations)** (Impact: 2.1)
  * `1100-Load-WS-Tables` **(I/O & Config Routines)** (Impact: 1.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 30 instances
* *State Mutation (weighted view):* 124
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 153`, `args: 1`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `state_mutation: 64`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Mainframe/ZOS/ECBAP/cbl/TABLENA.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 9.436)
- **Top Global Matches:** file_cluster_6: 9.436, file_cluster_8: 11.663, file_cluster_4: 16.018
- **Magnitude:** 242.72 | **LOC:** 1235 | **CtrlFlow:** 9.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (57.1%), Complexity Load (formerly Cognitive Load) (29.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `2100-Do-Some-Calculating` **(I/O & Config Routines)** (Impact: 50.4)
  * `2200-Do-Some-Searching` **(I/O & Config Routines)** (Impact: 39.0)
  * `2300-Do-Some-Searching-All` **(Interface Declarations)** (Impact: 4.0)
  * `2900-Display-The-Tables` **(Interface Declarations)** (Impact: 2.1)
  * `1100-Load-WS-Tables` **(I/O & Config Routines)** (Impact: 1.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 30 instances
* *State Mutation (weighted view):* 124
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 152`, `args: 1`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `state_mutation: 64`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Mainframe/ZOS/ECBAP/cbl/WS81C.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.131)
- **Top Global Matches:** file_cluster_4: 8.131, file_cluster_11: 8.428, file_cluster_2: 9.007
- **Magnitude:** 203.14 | **LOC:** 508 | **CtrlFlow:** 11.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.7%), Guard Balance (formerly Safety Score) (62.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `2120-Calculate-Inst-Price` **(I/O & Config Routines)** (Impact: 36.6)
  * `5100-Read-RFPIN` **(I/O & Config Routines)** (Impact: 6.8)
  * `2110-Move-Fixed-Fields` **(I/O & Config Routines)** (Impact: 6.2)
  * `2130-Calculate-Shipping` **(I/O & Config Routines)** (Impact: 5.6)
  * `6000-Write-Proposal` **(Interface Declarations)** (Impact: 3.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 114
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 44`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `state_mutation: 60`
* *Architecture:* `io: 12`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `OpenCobol/ECBAP/cbl/ws81c.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.127)
- **Top Global Matches:** file_cluster_4: 8.127, file_cluster_11: 8.43, file_cluster_2: 9.019
- **Magnitude:** 202.92 | **LOC:** 523 | **CtrlFlow:** 11.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.6%), Guard Balance (formerly Safety Score) (62.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `2120-Calculate-Inst-Price` **(I/O & Config Routines)** (Impact: 36.6)
  * `5100-Read-RFPIN` **(I/O & Config Routines)** (Impact: 6.8)
  * `2110-Move-Fixed-Fields` **(I/O & Config Routines)** (Impact: 6.2)
  * `2130-Calculate-Shipping` **(I/O & Config Routines)** (Impact: 5.6)
  * `6000-Write-Proposal` **(Interface Declarations)** (Impact: 3.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 114
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 44`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `state_mutation: 60`
* *Architecture:* `io: 12`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Mainframe/ZOS/ECBAP/cbl/TABLE1.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.033)
- **Top Global Matches:** file_cluster_4: 9.033, file_cluster_6: 9.466, file_cluster_11: 14.398
- **Magnitude:** 201.22 | **LOC:** 639 | **CtrlFlow:** 12.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 2.616; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (57.6%), Complexity Load (formerly Cognitive Load) (37.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `2000-Process` **(I/O & Config Routines)** (Impact: 61.1)
  * `1015-Load-Type` **(I/O & Config Routines)** (Impact: 7.0)
  * `1099-Verify-Type-Table` **(I/O & Config Routines)** (Impact: 2.8)
  * `1010-Load-Type-Table` **(I/O & Config Routines)** (Impact: 2.4)
  * `1100-Load-Other-Tables` **(I/O & Config Routines)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 88
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 189`, `args: 4`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 48`, `dead_code: 1`
* *Architecture:* `io: 3`, `api: 24`, `import: 1`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` WSFST
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `OpenCobol/ECBAP/cbl/tablewa.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 9.493)
- **Top Global Matches:** file_cluster_6: 9.493, file_cluster_8: 11.731, file_cluster_4: 16.031
- **Magnitude:** 178.32 | **LOC:** 1198 | **CtrlFlow:** 7.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (82.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (54.8%), Complexity Load (formerly Cognitive Load) (18.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `2200-Do-Some-Searching` **(I/O & Config Routines)** (Impact: 39.4)
  * `2100-Do-Some-Calculating` **(I/O & Config Routines)** (Impact: 29.2)
  * `2300-Do-Some-Searching-All` **(Interface Declarations)** (Impact: 4.0)
  * `2900-Display-The-Tables` **(Interface Declarations)** (Impact: 2.1)
  * `1100-Load-WS-Tables` **(I/O & Config Routines)** (Impact: 1.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 81
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 62`, `structural_boundaries: 144`, `args: 7`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `state_mutation: 45`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Mainframe/ZOS/ECBAP/cbl/TABLEWA.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 9.494)
- **Top Global Matches:** file_cluster_6: 9.494, file_cluster_8: 11.732, file_cluster_4: 16.032
- **Magnitude:** 177.64 | **LOC:** 1189 | **CtrlFlow:** 7.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (83.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (54.9%), Complexity Load (formerly Cognitive Load) (18.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `2200-Do-Some-Searching` **(I/O & Config Routines)** (Impact: 39.0)
  * `2100-Do-Some-Calculating` **(I/O & Config Routines)** (Impact: 29.2)
  * `2300-Do-Some-Searching-All` **(Interface Declarations)** (Impact: 3.9)
  * `2900-Display-The-Tables` **(Interface Declarations)** (Impact: 2.1)
  * `1100-Load-WS-Tables` **(I/O & Config Routines)** (Impact: 1.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 81
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 62`, `structural_boundaries: 144`, `args: 7`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `state_mutation: 45`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `OpenCobol/ECBAP/cbl/HOSPEDIT.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.66)
- **Top Global Matches:** file_cluster_6: 8.66, file_cluster_4: 9.881, file_cluster_12: 15.804
- **Magnitude:** 169.76 | **LOC:** 488 | **CtrlFlow:** 5.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (65.0%), Complexity Load (formerly Cognitive Load) (63.4%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `100-MAINLINE` **(I/O & Config Routines)** (Impact: 23.4)
  * `000-HOUSEKEEPING` **(I/O & Config Routines)** (Impact: 4.2)
  * `HOSPEDIT` **(I/O & Config Routines)** (Impact: 2.4)
  * `200-CLEANUP` **(I/O & Config Routines)** (Impact: 2.0)
  * `000-EXIT` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 126
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 18`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 72`
* *Architecture:* `io: 24`
* *Defense:* `doc: 3`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `OpenCobol/ECBAP/cbl/ws172a.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.042)
- **Top Global Matches:** file_cluster_11: 6.042, file_cluster_2: 6.716, file_cluster_15: 7.126
- **Magnitude:** 160.48 | **LOC:** 416 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 2.616; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (63.4%), Complexity Load (formerly Cognitive Load) (43.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `2120-Calculate-Grades` **(I/O & Config Routines)** (Impact: 9.4)
  * `2110-Print-Stdt-Detail-Report` **(I/O & Config Routines)** (Impact: 8.9)
  * `5000-Read-STCOURS` **(I/O & Config Routines)** (Impact: 6.8)
  * `2110-Print-Stdt-Total-Report` **(I/O & Config Routines)** (Impact: 4.0)
  * `6200-Write-ERRFILE` **(I/O & Config Routines)** (Impact: 3.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 26 instances
* *State Mutation (weighted view):* 101
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 47`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `state_mutation: 49`
* *Architecture:* `io: 14`, `import: 4`
* *Defense:* `safety: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` WSDT, WSFST
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Mainframe/ZOS/ECBAP/cbl/WS172A.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.038)
- **Top Global Matches:** file_cluster_11: 6.038, file_cluster_2: 6.707, file_cluster_15: 7.124
- **Magnitude:** 160.46 | **LOC:** 416 | **CtrlFlow:** 9.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 2.616; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (63.5%), Complexity Load (formerly Cognitive Load) (44.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `2120-Calculate-Grades` **(I/O & Config Routines)** (Impact: 9.4)
  * `2110-Print-Stdt-Detail-Report` **(I/O & Config Routines)** (Impact: 8.9)
  * `5000-Read-STCOURS` **(I/O & Config Routines)** (Impact: 6.8)
  * `2110-Print-Stdt-Total-Report` **(I/O & Config Routines)** (Impact: 4.0)
  * `6200-Write-ERRFILE` **(I/O & Config Routines)** (Impact: 3.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 26 instances
* *State Mutation (weighted view):* 101
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 47`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `state_mutation: 49`
* *Architecture:* `io: 14`, `import: 4`
* *Defense:* `safety: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` WSDT, WSFST
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pgm_templates/CICS/basecics.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.266)
- **Top Global Matches:** file_cluster_2: 6.266, file_cluster_11: 6.521, file_cluster_15: 6.866
- **Magnitude:** 156.12 | **LOC:** 336 | **CtrlFlow:** 10.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (66.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `5000-VALIDATE-FIELD` **(I/O & Config Routines)** (Impact: 16.6)
  * `0000-MAINLINE` **(I/O & Config Routines)** (Impact: 6.8)
  * `5500-COMPUTE-RESULTS` **(I/O & Config Routines)** (Impact: 6.3)
  * `1000-RECIEVE-MAP` **(I/O & Config Routines)** (Impact: 6.2)
  * `0500-NORMAL-PROCESSING` **(Interface Declarations)** (Impact: 2.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 99
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 21`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `state_mutation: 61`, `dead_code: 2`, `unreferenced_by_name: 3`
* *Architecture:* `api: 1`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Mainframe/ZOS/ECBAP/cbl/WS120.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.118)
- **Top Global Matches:** file_cluster_11: 6.118, file_cluster_2: 6.794, file_cluster_15: 7.251
- **Magnitude:** 143.3 | **LOC:** 387 | **CtrlFlow:** 7.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 2.616; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (62.0%), Complexity Load (formerly Cognitive Load) (36.3%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `2112-Check-Deductible` **(I/O & Config Routines)** (Impact: 10.1)
  * `5100-Read-INSClaim` **(I/O & Config Routines)** (Impact: 6.8)
  * `2120-Move-Fixed-Fields` **(Stateful Encapsulated Methods)** (Impact: 5.8)
  * `2111-Check-Benefit-Date` **(I/O & Config Routines)** (Impact: 3.8)
  * `2100-Process-Claims` **(I/O & Config Routines)** (Impact: 3.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 87
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 41`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `state_mutation: 43`
* *Architecture:* `io: 14`, `import: 4`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` CLAIMREC, WSDT, WSFST
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Mainframe/ZOS/ECBAP/cbl/WS193.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.118)
- **Top Global Matches:** file_cluster_11: 6.118, file_cluster_2: 6.794, file_cluster_15: 7.251
- **Magnitude:** 143.3 | **LOC:** 387 | **CtrlFlow:** 7.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 2.616; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (62.0%), Complexity Load (formerly Cognitive Load) (36.3%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `2112-Check-Deductible` **(I/O & Config Routines)** (Impact: 10.1)
  * `5100-Read-INSClaim` **(I/O & Config Routines)** (Impact: 6.8)
  * `2120-Move-Fixed-Fields` **(Stateful Encapsulated Methods)** (Impact: 5.8)
  * `2111-Check-Benefit-Date` **(I/O & Config Routines)** (Impact: 3.8)
  * `2100-Process-Claims` **(I/O & Config Routines)** (Impact: 3.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 87
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 41`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `state_mutation: 43`
* *Architecture:* `io: 14`, `import: 4`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` CLAIMREC, WSDT, WSFST
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `OpenCobol/ECBAP/cbl/ws120.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.115)
- **Top Global Matches:** file_cluster_11: 6.115, file_cluster_2: 6.795, file_cluster_15: 7.248
- **Magnitude:** 143.3 | **LOC:** 387 | **CtrlFlow:** 7.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 2.616; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (62.0%), Complexity Load (formerly Cognitive Load) (36.3%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `2112-Check-Deductible` **(I/O & Config Routines)** (Impact: 10.1)
  * `5100-Read-INSClaim` **(I/O & Config Routines)** (Impact: 6.8)
  * `2120-Move-Fixed-Fields` **(Stateful Encapsulated Methods)** (Impact: 5.8)
  * `2111-Check-Benefit-Date` **(I/O & Config Routines)** (Impact: 3.8)
  * `2100-Process-Claims` **(I/O & Config Routines)** (Impact: 3.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 87
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 41`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `state_mutation: 43`
* *Architecture:* `io: 14`, `import: 4`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` CLAIMREC, WSDT, WSFST
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `OpenCobol/ECBAP/cbl/TABLE1.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.042)
- **Top Global Matches:** file_cluster_4: 9.042, file_cluster_6: 9.509, file_cluster_11: 14.138
- **Magnitude:** 126.98 | **LOC:** 449 | **CtrlFlow:** 10.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 2.616; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (56.8%), Complexity Load (formerly Cognitive Load) (30.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `2000-Process` **(I/O & Config Routines)** (Impact: 31.8)
  * `1015-Load-Type` **(I/O & Config Routines)** (Impact: 7.0)
  * `1099-Verify-Type-Table` **(Interface Declarations)** (Impact: 4.7)
  * `1010-Load-Type-Table` **(Interface Declarations)** (Impact: 2.3)
  * `0000-Mainline` **(Interface Declarations)** (Impact: 1.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 55
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 139`, `args: 4`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 25`
* *Architecture:* `io: 3`, `api: 14`, `import: 1`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` WSFST
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `OpenCobol/ECBAP/cbl/ws162o.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.491)
- **Top Global Matches:** file_cluster_11: 6.491, file_cluster_2: 7.182, file_cluster_15: 7.54
- **Magnitude:** 125.12 | **LOC:** 483 | **CtrlFlow:** 6.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 2.616; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (56.8%), Complexity Load (formerly Cognitive Load) (25.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `1015-Load-Type` **(I/O & Config Routines)** (Impact: 7.0)
  * `5100-Read-INFILE` **(I/O & Config Routines)** (Impact: 6.8)
  * `2100-Process-INFile-Records` **(I/O & Config Routines)** (Impact: 4.2)
  * `6000-Write-OutFile-Patient` **(I/O & Config Routines)** (Impact: 3.6)
  * `6200-Write-ErrFile` **(Interface Declarations)** (Impact: 3.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 56
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 69`, `func_start: 29`, `class_start: 1`
* *Risk/State:* `state_mutation: 32`
* *Architecture:* `io: 21`, `import: 9`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` PATIENT, WSDT, WSFST
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pgm_templates/CICS/calctest.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 6.436)
- **Top Global Matches:** file_cluster_1: 6.436, file_cluster_3: 48.33, file_cluster_8: 70.12
- **Magnitude:** 122.86 | **LOC:** 240 | **CtrlFlow:** 10.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 2.616; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (83.1%), Guard Balance (formerly Safety Score) (70.6%), Connectivity (formerly Api Exposure) (2.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CALCTEST` **(I/O & Config Routines)** (Impact: 30.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 88
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 50`
* *Architecture:* `api: 1`, `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AVDEFN, CICSERC, DFHAID, WAGEMAP
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `OpenCobol/ECBAP/cbl/tabldna.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.718)
- **Top Global Matches:** file_cluster_11: 6.718, file_cluster_2: 7.38, file_cluster_15: 7.493
- **Magnitude:** 107.5 | **LOC:** 366 | **CtrlFlow:** 10.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 2.616; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.7%), Guard Balance (formerly Safety Score) (59.4%), Complexity Load (formerly Cognitive Load) (51.1%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `2200-Do-Some-Searching` **(I/O & Config Routines)** (Impact: 12.2)
  * `1013-Load-Employees` **(I/O & Config Routines)** (Impact: 7.0)
  * `1113-Load-Students` **(I/O & Config Routines)** (Impact: 7.0)
  * `1019-Verify-Emp-Table` **(I/O & Config Routines)** (Impact: 2.7)
  * `1119-Verify-Student-Table` **(I/O & Config Routines)** (Impact: 2.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 55
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 51`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `state_mutation: 31`
* *Architecture:* `io: 6`, `import: 2`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` WSFST
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `OpenCobol/dastagg/cbl/BDS1005.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.292)
- **Top Global Matches:** file_cluster_2: 6.292, file_cluster_15: 6.616, file_cluster_16: 7.576
- **Magnitude:** 107.3 | **LOC:** 223 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (67.0%), Complexity Load (formerly Cognitive Load) (62.7%), Debt Markers (formerly Tech Debt) (16.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ProcessOneTransaction` **(Compute Cores)** (Impact: 7.5)
  * `ApplySubtractFromStock` **(I/O & Config Routines)** (Impact: 5.6)
  * `Begin` **(I/O & Config Routines)** (Impact: 5.0)
  * `SetInitialStatus` **(I/O & Config Routines)** (Impact: 3.4)
  * `ApplyInsertion` **(I/O & Config Routines)** (Impact: 3.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 61
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 28`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 21`, `fragile_debt: 1`
* *Architecture:* `io: 7`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

*No file sits within 2% of a second archetype -- no mixed-responsibility candidates.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `Mainframe/ZOS/ECBAP/cbl/SUB01.cbl` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 91.6827%)
- `Mainframe/ZOS/Normal/cbl/BDS0704.cbl` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 99.9704%)
- `Mainframe/ZOS/Normal/cbl/BDS0801.cbl` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 99.9952%)
- `Mainframe/ZOS/Normal/cbl/BDS0802.cbl` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 99.7515%)
- `Mainframe/ZOS/Normal/cbl/BDS0803.cbl` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 97.4581%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `Mainframe/ZOS/Normal/cbl/BDS0801.cbl` -> **Severity: 0.21** (Embedded: 0.003 * Error Risk: 69.8657%)
- `Mainframe/ZOS/ECBAP/cbl/SUB03.cbl` -> **Severity: 0.204** (Embedded: 0.004 * Error Risk: 50.7142%)
- `OpenCobol/ECBAP/cbl/SUB03.cbl` -> **Severity: 0.204** (Embedded: 0.004 * Error Risk: 50.7142%)
- `Mainframe/ZOS/Zowe/Simple_Report/COBOL/prtrpt1.cbl` -> **Severity: 0.197** (Embedded: 0.003 * Error Risk: 65.3653%)
- `Mainframe/ZOS/Normal/cbl/BDS0704.cbl` -> **Severity: 0.194** (Embedded: 0.003 * Error Risk: 64.5062%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `Mainframe/ZOS/ECBAP/cbl/SUB03.cbl` -> **Severity: 673.0** (Blast Radius: 6.73 * Doc Risk: 100.0%)
- `OpenCobol/ECBAP/cbl/SUB03.cbl` -> **Severity: 673.0** (Blast Radius: 6.73 * Doc Risk: 100.0%)
- `Mainframe/MVS/herc03/cbl/cbl0001.cbl` -> **Severity: 484.0** (Blast Radius: 4.84 * Doc Risk: 100.0%)
- `Mainframe/ZOS/ECBAP/cbl/SUB01.cbl` -> **Severity: 484.0** (Blast Radius: 4.84 * Doc Risk: 100.0%)
- `Mainframe/ZOS/ECBAP/cbl/WS63.cbl` -> **Severity: 484.0** (Blast Radius: 4.84 * Doc Risk: 100.0%)

## 13. MAINFRAME SYSTEM FACTS (Named Relations & Record Layouts)
> **AI CONTEXT:** Named mainframe relations the structural signal counts flatten -- the call graph (`CALL`/CICS `LINK`·`XCTL`/JCL `EXEC PGM=`), the dataset boundary (`SELECT…ASSIGN` + `OPEN` modes, JCL `DD`→dataset), and record layouts (COBOL DATA DIVISION items, PL/I `DECLARE`d structures). BMS screen maps (every field's position, length and attributes, `screen_field_data`) are the 3270 UI surface. These are the schema of the system: use them to trace which program runs which, which dataset a job binds, and the shape of the records that flow between them. Extracted by the engine (`core/mainframe_boundary.py`) and carried in the master DB (`call_site_data`/`dataset_data`/`record_data`); resolution to files is redone per scan.

- **Coverage:** `184` files carry mainframe facts -- `39` call sites, `257` dataset bindings, `8279` record items.

- **CICS operations:** `8` EXEC CICS operations naming a resource (`8` MAP); verb, direction, VALUE-resolved name and INTO/FROM record in `cics_resource_data`.

### `Mainframe/ZOS/ECBAP/cbl/WS81E.cbl` (COBOL)
- **Datasets:** `RFPIN(INPUT)`, `PROPOSAL(OUTPUT)`, `BADRFP(OUTPUT)`, `PROPRPT(OUTPUT)`
- **Record layouts (230 items):** `PRP-RECORD⟵PROPOSAL (24)`, `R1-COLUMN-HEADER2 (20)`, `R1-COLUMN-HEADER3 (20)`, `R1-DETAIL-LINE (20)`, `RFP-RECORD⟵RFPIN (19)`, `BRFP-RECORD⟵BADRFP (19)`, `WS-RPF-STORAGE (16)`, `R1-PAGE-HEADER (14)`, `WS-FILE-STATUS (13)`, `WS-RPF-PRICE-LIST (12)`, `R1-COLUMN-HEADER1 (11)`, `CURRENT-DATE-AND-TIME (10)` … (+8 more)
- **Data moves:** 123 (ADD 13, COMPUTE 53, INITIALIZE 2, MOVE 51, WRITE 4); most-fed items `WS-RFP-P1`, `PRINT-LINE`, `WS-RFP-P2`, `PRP-COST-PER-INSTRUMENT`, `WS-RFP-P3`, `WS-RFP-TOTAL-PROP`

### `OpenCobol/ECBAP/cbl/ws81e.cbl` (COBOL)
- **Datasets:** `../../../COMMON/DATA/ECBAP/FAVRFP.DAT.TXT(INPUT)`, `../../../COMMON/DATA/ECBAP/PROPOSAL.DAT.TXT(OUTPUT)`, `../../../COMMON/DATA/ECBAP/BADRFP.DAT.TXT(OUTPUT)`, `../SPOOL/PROP-REPORT.RPT(OUTPUT)`
- **Record layouts (230 items):** `PRP-RECORD⟵PROPOSAL (24)`, `R1-COLUMN-HEADER2 (20)`, `R1-COLUMN-HEADER3 (20)`, `R1-DETAIL-LINE (20)`, `RFP-RECORD⟵RFPIN (19)`, `BRFP-RECORD⟵BADRFP (19)`, `WS-RPF-STORAGE (16)`, `R1-PAGE-HEADER (14)`, `WS-FILE-STATUS (13)`, `WS-RPF-PRICE-LIST (12)`, `R1-COLUMN-HEADER1 (11)`, `CURRENT-DATE-AND-TIME (10)` … (+8 more)
- **Data moves:** 123 (ADD 13, COMPUTE 53, INITIALIZE 2, MOVE 51, WRITE 4); most-fed items `WS-RFP-P1`, `PRINT-LINE`, `WS-RFP-P2`, `PRP-COST-PER-INSTRUMENT`, `WS-RFP-P3`, `WS-RFP-TOTAL-PROP`

### `Mainframe/ZOS/ECBAP/cbl/TABLENA.cbl` (COBOL)
- **Record layouts (272 items):** `WS-3DI-HOLD (61)`, `WS-STATE-HOLD (52)`, `WS-3DS-HOLD (36)`, `WS-3DS-TABLE-STORAGE (14)`, `WS-ST-CRS-HOLD (11)`, `WS-3DI-TABLE-STORAGE (11)`, `WS-2D-TABLE-STORAGE (10)`, `WS-2DN-TABLE-STORAGE (10)`, `WS-STD-CRS-TABLE-STORAGE (10)`, `WS-COMPANY-STORAGE (8)`, `WS-STATE-TABLE-STORAGE (7)`, `WS-1DN-HOLD (6)` … (+7 more)
- **Data moves:** 82 (ADD 6, COMPUTE 38, DIVIDE 4, INITIALIZE 24, MOVE 10); most-fed items `WS-SHOW-NUMBER`, `WS-COMPANY-TOTAL`, `WS-AVERAGE-DISPLAY`, `WS-DIVISION-TOTAL`, `WS-REGION-TOTAL`, `WS-HOLD-HIGH-VALUE`

### `OpenCobol/ECBAP/cbl/tablena.cbl` (COBOL)
- **Record layouts (272 items):** `WS-3DI-HOLD (61)`, `WS-STATE-HOLD (52)`, `WS-3DS-HOLD (36)`, `WS-3DS-TABLE-STORAGE (14)`, `WS-ST-CRS-HOLD (11)`, `WS-3DI-TABLE-STORAGE (11)`, `WS-2D-TABLE-STORAGE (10)`, `WS-2DN-TABLE-STORAGE (10)`, `WS-STD-CRS-TABLE-STORAGE (10)`, `WS-COMPANY-STORAGE (8)`, `WS-STATE-TABLE-STORAGE (7)`, `WS-1DN-HOLD (6)` … (+7 more)
- **Data moves:** 82 (ADD 6, COMPUTE 38, DIVIDE 4, INITIALIZE 24, MOVE 10); most-fed items `WS-SHOW-NUMBER`, `WS-COMPANY-TOTAL`, `WS-AVERAGE-DISPLAY`, `WS-DIVISION-TOTAL`, `WS-REGION-TOTAL`, `WS-HOLD-HIGH-VALUE`

### `Mainframe/ZOS/ECBAP/cbl/TABLEWA.cbl` (COBOL)
- **Record layouts (272 items):** `WS-3DI-HOLD (61)`, `WS-STATE-HOLD (52)`, `WS-3DS-HOLD (36)`, `WS-3DS-TABLE-STORAGE (14)`, `WS-ST-CRS-HOLD (11)`, `WS-3DI-TABLE-STORAGE (11)`, `WS-2D-TABLE-STORAGE (10)`, `WS-2DN-TABLE-STORAGE (10)`, `WS-STD-CRS-TABLE-STORAGE (10)`, `WS-COMPANY-STORAGE (8)`, `WS-STATE-TABLE-STORAGE (7)`, `WS-1DN-HOLD (6)` … (+7 more)
- **Data moves:** 44 (COMPUTE 28, INITIALIZE 6, MOVE 10); most-fed items `WS-SHOW-NUMBER`, `WS-COMPANY-TOTAL`, `WS-AVERAGE-DISPLAY`, `WS-DIVISION-TOTAL`, `WS-REGION-TOTAL`, `WS-1D-TABLE-SETUP`

### `OpenCobol/ECBAP/cbl/tablewa.cbl` (COBOL)
- **Record layouts (272 items):** `WS-3DI-HOLD (61)`, `WS-STATE-HOLD (52)`, `WS-3DS-HOLD (36)`, `WS-3DS-TABLE-STORAGE (14)`, `WS-ST-CRS-HOLD (11)`, `WS-3DI-TABLE-STORAGE (11)`, `WS-2D-TABLE-STORAGE (10)`, `WS-2DN-TABLE-STORAGE (10)`, `WS-STD-CRS-TABLE-STORAGE (10)`, `WS-COMPANY-STORAGE (8)`, `WS-STATE-TABLE-STORAGE (7)`, `WS-1DN-HOLD (6)` … (+7 more)
- **Data moves:** 44 (COMPUTE 28, INITIALIZE 6, MOVE 10); most-fed items `WS-SHOW-NUMBER`, `WS-COMPANY-TOTAL`, `WS-AVERAGE-DISPLAY`, `WS-DIVISION-TOTAL`, `WS-REGION-TOTAL`, `WS-1D-TABLE-SETUP`

### `Mainframe/ZOS/ECBAP/cbl/WS81D.cbl` (COBOL)
- **Datasets:** `RFPIN(INPUT)`, `PROPOSAL(OUTPUT)`, `PROPRPT(OUTPUT)`
- **Record layouts (195 items):** `PRP-RECORD⟵PROPOSAL (24)`, `R1-COLUMN-HEADER2 (20)`, `R1-COLUMN-HEADER3 (20)`, `R1-DETAIL-LINE (20)`, `RFP-RECORD⟵RFPIN (19)`, `WS-RPF-STORAGE (15)`, `R1-PAGE-HEADER (14)`, `WS-RPF-PRICE-LIST (12)`, `R1-COLUMN-HEADER1 (11)`, `WS-FILE-STATUS (10)`, `CURRENT-DATE-AND-TIME (10)`, `R1-COUNTERS (6)` … (+4 more)
- **Data moves:** 112 (ADD 11, COMPUTE 51, INITIALIZE 2, MOVE 44, WRITE 4); most-fed items `WS-RFP-P1`, `PRINT-LINE`, `WS-RFP-P2`, `PRP-COST-PER-INSTRUMENT`, `WS-RFP-P3`, `PRP-ARTIST-ACCT-NO`

### `OpenCobol/ECBAP/cbl/ws81d.cbl` (COBOL)
- **Datasets:** `../../../COMMON/DATA/ECBAP/FAVRFP.DAT.TXT(INPUT)`, `../../../COMMON/DATA/ECBAP/PROPOSAL.DAT.TXT(OUTPUT)`, `../SPOOL/PROP-REPORT.RPT(OUTPUT)`
- **Record layouts (195 items):** `PRP-RECORD⟵PROPOSAL (24)`, `R1-COLUMN-HEADER2 (20)`, `R1-COLUMN-HEADER3 (20)`, `R1-DETAIL-LINE (20)`, `RFP-RECORD⟵RFPIN (19)`, `WS-RPF-STORAGE (15)`, `R1-PAGE-HEADER (14)`, `WS-RPF-PRICE-LIST (12)`, `R1-COLUMN-HEADER1 (11)`, `WS-FILE-STATUS (10)`, `CURRENT-DATE-AND-TIME (10)`, `R1-COUNTERS (6)` … (+4 more)
- **Data moves:** 112 (ADD 11, COMPUTE 51, INITIALIZE 2, MOVE 44, WRITE 4); most-fed items `WS-RFP-P1`, `PRINT-LINE`, `WS-RFP-P2`, `PRP-COST-PER-INSTRUMENT`, `WS-RFP-P3`, `PRP-ARTIST-ACCT-NO`

### `Mainframe/ZOS/ECBAP/cbl/WS162E.cbl` (COBOL)
- **Datasets:** `HOSPIN(INPUT)`, `RPTFILE(OUTPUT)`, `HOSPOUT(OUTPUT)`, `HOSPERR(OUTPUT)`, `INSTYPE(INPUT)`
- **Record layouts (200 items):** `R1-DETAIL-LINE (28)`, `R1-COLUMN-HEADER2 (26)`, `R1-COLUMN-HEADER3 (26)`, `WS-OUTFILE-RECORD (18)`, `R1-PAGE-HEADER (14)`, `R1-COLUMN-HEADER1 (14)`, `WS-TYPE-TABLE-STORAGE (11)`, `WS-PROGRAM-STORAGE (7)`, `R1-FOOTER-TYPE-PRINT-LINE (7)`, `WS-FILE-COUNTERS (6)`, `R1-COUNTERS (6)`, `EOJ-DISPLAY-MESSAGES (5)` … (+11 more)
- **Data moves:** 94 (ADD 13, COMPUTE 8, MOVE 63, STRING 6, WRITE 4); most-fed items `R1-PRINT-LINE`, `R1-PATIENT-PHONE`, `R1-PATIENT-AMT-PDAY`, `R1-PATIENT-COPAY`, `WS-DAILY-AMT`, `WS-DAILY-CO-PAY`

### `OpenCobol/ECBAP/cbl/ws162e.cbl` (COBOL)
- **Datasets:** `../../../COMMON/DATA/ECBAP/HOSPIN.DAT.TXT(INPUT)`, `../../../COMMON/DATA/ECBAP/HRPTFILE.DAT.TXT(OUTPUT)`, `../../../COMMON/DATA/ECBAP/HOUTFILE.DAT.TXT(OUTPUT)`, `../../../COMMON/DATA/ECBAP/HERRFILE.DAT.TXT(OUTPUT)`, `../../../COMMON/DATA/ECBAP/HINSTYPE.DAT.TXT(INPUT)`
- **Record layouts (200 items):** `R1-DETAIL-LINE (28)`, `R1-COLUMN-HEADER2 (26)`, `R1-COLUMN-HEADER3 (26)`, `WS-OUTFILE-RECORD (18)`, `R1-PAGE-HEADER (14)`, `R1-COLUMN-HEADER1 (14)`, `WS-TYPE-TABLE-STORAGE (11)`, `WS-PROGRAM-STORAGE (7)`, `R1-FOOTER-TYPE-PRINT-LINE (7)`, `WS-FILE-COUNTERS (6)`, `R1-COUNTERS (6)`, `EOJ-DISPLAY-MESSAGES (5)` … (+11 more)
- **Data moves:** 94 (ADD 13, COMPUTE 8, MOVE 63, STRING 6, WRITE 4); most-fed items `R1-PRINT-LINE`, `R1-PATIENT-PHONE`, `R1-PATIENT-AMT-PDAY`, `R1-PATIENT-COPAY`, `WS-DAILY-AMT`, `WS-DAILY-CO-PAY`

### `OpenCobol/ECBAP/cbl/HOSPEDIT.cbl` (COBOL)
- **Datasets:** `../../../COMMON/DATA/ECBAP/HOSPIN.DAT.TXT(INPUT)`, `../../../COMMON/DATA/ECBAP/HRPTFILE.DAT.TXT(OUTPUT)`, `../../../COMMON/DATA/ECBAP/HOUTFILE.DAT.TXT(OUTPUT)`, `../../../COMMON/DATA/ECBAP/HERRFILE.DAT.TXT(OUTPUT)`, `../../../COMMON/DATA/ECBAP/HINSTYPE.DAT.TXT(INPUT)`
- **Record layouts (208 items):** `WS-INPUT-REC (23)`, `R1-COLUMN-HEADER2 (20)`, `R1-COLUMN-HEADER3 (20)`, `R1-DETAIL-LINE (20)`, `R1-COLUMN-HEADER1 (19)`, `WS-OUTPUT-REC (18)`, `COUNTERS-AND-ACCUMULATORS (15)`, `R1-PAGE-HEADER (14)`, `FILE-STATUS-CODES (13)`, `WS-INS-TYPE-TABLE (7)`, `R1-COUNTERS (6)`, `EOJ-PRINT-LINE (4)` … (+14 more)
- **Data moves:** 77 (ACCEPT 1, ADD 19, COMPUTE 3, INITIALIZE 2, MOVE 47, READ 4, WRITE 1); most-fed items `RPT-REC`, `EOJ-PRINT-NUMBER`, `PAT-TOTAL-AMT-NET`, `PATIENT-AMT-PER-DAY-O`, `BED-IDENTITY-O`, `CURR-DATE-O`

### `Mainframe/ZOS/ECBAP/cbl/WS81C.cbl` (COBOL)
- **Datasets:** `RFPIN(INPUT)`, `PROPOSAL(OUTPUT)`, `PROPRPT(OUTPUT)`
- **Record layouts (183 items):** `PRP-RECORD⟵PROPOSAL (24)`, `R1-COLUMN-HEADER2 (20)`, `R1-COLUMN-HEADER3 (20)`, `R1-DETAIL-LINE (20)`, `RFP-RECORD⟵RFPIN (19)`, `R1-PAGE-HEADER (14)`, `WS-RPF-PRICE-LIST (12)`, `R1-COLUMN-HEADER1 (11)`, `WS-FILE-STATUS (10)`, `CURRENT-DATE-AND-TIME (10)`, `R1-COUNTERS (5)`, `EOJ-DISPLAY-MESSAGES (5)` … (+4 more)
- **Data moves:** 104 (ADD 3, COMPUTE 51, INITIALIZE 2, MOVE 44, WRITE 4); most-fed items `WS-RFP-P1`, `PRINT-LINE`, `WS-RFP-P2`, `PRP-COST-PER-INSTRUMENT`, `WS-RFP-P3`, `PRP-ARTIST-ACCT-NO`

### `OpenCobol/ECBAP/cbl/ws81c.cbl` (COBOL)
- **Datasets:** `../../../COMMON/DATA/ECBAP/FAVRFP.DAT.TXT(INPUT)`, `../../../COMMON/DATA/ECBAP/PROPOSAL.DAT.TXT(OUTPUT)`, `../SPOOL/PROP-REPORT.RPT(OUTPUT)`
- **Record layouts (183 items):** `PRP-RECORD⟵PROPOSAL (24)`, `R1-COLUMN-HEADER2 (20)`, `R1-COLUMN-HEADER3 (20)`, `R1-DETAIL-LINE (20)`, `RFP-RECORD⟵RFPIN (19)`, `R1-PAGE-HEADER (14)`, `WS-RPF-PRICE-LIST (12)`, `R1-COLUMN-HEADER1 (11)`, `WS-FILE-STATUS (10)`, `CURRENT-DATE-AND-TIME (10)`, `R1-COUNTERS (5)`, `EOJ-DISPLAY-MESSAGES (5)` … (+4 more)
- **Data moves:** 104 (ADD 3, COMPUTE 51, INITIALIZE 2, MOVE 44, WRITE 4); most-fed items `WS-RFP-P1`, `PRINT-LINE`, `WS-RFP-P2`, `PRP-COST-PER-INSTRUMENT`, `WS-RFP-P3`, `PRP-ARTIST-ACCT-NO`

### `Mainframe/ZOS/ECBAP/cbl/TABLE2.cbl` (COBOL)
- **Record layouts (190 items):** `WS-3D-HOLD (61)`, `WS-TT-HOLD (36)`, `WS-THREE-DIM-TABLE-STORAGE (11)`, `WS-TWO-DIM-TABLE-STORAGE (8)`, `WS-TWO-DIM-NUM-TABLE-STORAGE (8)`, `WS-TWO-DIM-HNUM-TABLE-STORAGE (8)`, `WS-3D-INDEX-TABLE-STORAGE (8)`, `WS-FUNCTION-STORAGE (6)`, `WS-STN-HOLD (6)`, `WS-DT-HOLD (6)`, `WS-DTN-HOLD (6)`, `WS-DTHN-HOLD (6)` … (+6 more)
- **Data moves:** 38 (COMPUTE 25, INITIALIZE 3, MOVE 10); most-fed items `WS-DTN-L2-B`, `MAX-SALARY`, `TOTAL-PAYROLL`, `WS-COMPANY-TOTAL`, `WS-DIVISION-TOTAL`, `AVG-SALARY`

### `Mainframe/ZOS/ECBAP/cbl/TABLE3.cbl` (COBOL)
- **Record layouts (190 items):** `WS-3D-HOLD (61)`, `WS-TT-HOLD (36)`, `WS-THREE-DIM-TABLE-STORAGE (11)`, `WS-TWO-DIM-TABLE-STORAGE (8)`, `WS-TWO-DIM-NUM-TABLE-STORAGE (8)`, `WS-TWO-DIM-HNUM-TABLE-STORAGE (8)`, `WS-3D-INDEX-TABLE-STORAGE (8)`, `WS-FUNCTION-STORAGE (6)`, `WS-STN-HOLD (6)`, `WS-DT-HOLD (6)`, `WS-DTN-HOLD (6)`, `WS-DTHN-HOLD (6)` … (+6 more)
- **Data moves:** 8 (MOVE 8); most-fed items `WS-3D-TABLE-SETUP`, `WS-DT-TABLE-SETUP`, `WS-DTHN-TABLE-SETUP`, `WS-DTN-TABLE-SETUP`, `WS-ST-TABLE-SETUP`, `WS-STF-A-TAB`

### `Mainframe/ZOS/ECBAP/cbl/WS120.cbl` (COBOL)
- **Datasets:** `INSCLAIM(INPUT)`, `INSRPT(OUTPUT)`
- **Record layouts (134 items):** `R1-COLUMN-HEADER2 (20)`, `R1-COLUMN-HEADER3 (20)`, `R1-DETAIL-LINE (20)`, `R1-COLUMN-HEADER1 (19)`, `R1-PAGE-HEADER (14)`, `R1-COUNTERS (6)`, `WS-CLAIM-COUNTERS (6)`, `EOJ-DISPLAY-MESSAGES (5)`, `R1-FOOTER1 (4)`, `R1-FOOTER2 (4)`, `R1-FOOTER3 (4)`, `WS-CLAIM-FLAGS (4)` … (+5 more)
- **Data moves:** 53 (ADD 6, COMPUTE 8, MOVE 27, STRING 5, SUBTRACT 2, WRITE 5); most-fed items `PRINT-LINE`, `R1-INSURED-POLICY-NO`, `WS-CLAIM-DEDUCTIBLE-AMT`, `WS-CLAIM-PAID-AMT`, `WS-CLAIM-COPAY-AMT`, `WS-DAYS-DIFF`

### `Mainframe/ZOS/ECBAP/cbl/WS182.cbl` (COBOL)
- **Datasets:** `ACCTREC(INPUT)`, `RPTFILE(OUTPUT)`
- **Record layouts (134 items):** `R1-PAGE-HEADER (17)`, `R1-DETAIL-LINE1 (15)`, `R1-COLUMN-HEADER1 (14)`, `R1-COLUMN-HEADER2 (14)`, `FD-ACCOUNT-RECORD⟵ACCTREC (12)`, `R1-CB-LINE1 (10)`, `WS-PROGRAM-STORAGE (7)`, `R1-STORAGE (7)`, `R1-FOOTER-TYPE-PRINT-LINE (7)`, `EOJ-DISPLAY-MESSAGES (5)`, `WS-CB-HOLD-STORAGE (4)`, `R1-FOOTER1 (4)` … (+7 more)
- **Data moves:** 53 (ADD 8, COMPUTE 5, INITIALIZE 1, MOVE 36, STRING 3); most-fed items `FD-REPORT-RECORD`, `R1-SALARY-ACCUM`, `R1-FT-AVG-SALARY`, `R1-NAME-COMBINED`, `R1-PRINT-LINE`, `R1-CB-STATE`

### `Mainframe/ZOS/ECBAP/cbl/WS193.cbl` (COBOL)
- **Datasets:** `INSCLAIM(INPUT)`, `INSRPT(OUTPUT)`
- **Record layouts (134 items):** `R1-COLUMN-HEADER2 (20)`, `R1-COLUMN-HEADER3 (20)`, `R1-DETAIL-LINE (20)`, `R1-COLUMN-HEADER1 (19)`, `R1-PAGE-HEADER (14)`, `R1-COUNTERS (6)`, `WS-CLAIM-COUNTERS (6)`, `EOJ-DISPLAY-MESSAGES (5)`, `R1-FOOTER1 (4)`, `R1-FOOTER2 (4)`, `R1-FOOTER3 (4)`, `WS-CLAIM-FLAGS (4)` … (+5 more)
- **Data moves:** 53 (ADD 6, COMPUTE 8, MOVE 27, STRING 5, SUBTRACT 2, WRITE 5); most-fed items `PRINT-LINE`, `R1-INSURED-POLICY-NO`, `WS-CLAIM-DEDUCTIBLE-AMT`, `WS-CLAIM-PAID-AMT`, `WS-CLAIM-COPAY-AMT`, `WS-DAYS-DIFF`

### `OpenCobol/ECBAP/cbl/ws120.cbl` (COBOL)
- **Datasets:** `../../../COMMON/DATA/ECBAP/INSCLAIM.DAT.TXT(INPUT)`, `../SPOOL/INSCLAIM-REPORT.RPT(OUTPUT)`
- **Record layouts (134 items):** `R1-COLUMN-HEADER2 (20)`, `R1-COLUMN-HEADER3 (20)`, `R1-DETAIL-LINE (20)`, `R1-COLUMN-HEADER1 (19)`, `R1-PAGE-HEADER (14)`, `R1-COUNTERS (6)`, `WS-CLAIM-COUNTERS (6)`, `EOJ-DISPLAY-MESSAGES (5)`, `R1-FOOTER1 (4)`, `R1-FOOTER2 (4)`, `R1-FOOTER3 (4)`, `WS-CLAIM-FLAGS (4)` … (+5 more)
- **Data moves:** 53 (ADD 6, COMPUTE 8, MOVE 27, STRING 5, SUBTRACT 2, WRITE 5); most-fed items `PRINT-LINE`, `R1-INSURED-POLICY-NO`, `WS-CLAIM-DEDUCTIBLE-AMT`, `WS-CLAIM-PAID-AMT`, `WS-CLAIM-COPAY-AMT`, `WS-DAYS-DIFF`

### `OpenCobol/ECBAP/cbl/ws182.cbl` (COBOL)
- **Datasets:** `../../../COMMON/DATA/ECBAP/ACCTREC.SORT.DAT.TXT(INPUT)`, `../SPOOL/PRES-CB1-REPORT.RPT(OUTPUT)`
- **Record layouts (133 items):** `R1-PAGE-HEADER (17)`, `R1-DETAIL-LINE1 (15)`, `R1-COLUMN-HEADER1 (14)`, `R1-COLUMN-HEADER2 (14)`, `FD-ACCOUNT-RECORD⟵ACCTREC (11)`, `R1-CB-LINE1 (10)`, `WS-PROGRAM-STORAGE (7)`, `R1-STORAGE (7)`, `R1-FOOTER-TYPE-PRINT-LINE (7)`, `EOJ-DISPLAY-MESSAGES (5)`, `WS-CB-HOLD-STORAGE (4)`, `R1-FOOTER1 (4)` … (+7 more)
- **Data moves:** 54 (ADD 8, COMPUTE 5, INITIALIZE 2, MOVE 36, STRING 3); most-fed items `FD-REPORT-RECORD`, `R1-SALARY-ACCUM`, `R1-FT-AVG-SALARY`, `R1-NAME-COMBINED`, `R1-PRINT-LINE`, `R1-CB-STATE`

*(+164 more files with mainframe facts; full detail in `record_data`/`call_site_data`/`dataset_data`.)*

- **Mainframe skeleton completeness:** 50% (mean channel ratio; channel table in the audit report, section 7). Top missing inputs: JCL and PROC libraries (122 gaps); scheduler export (CA-7 / Control-M / TWS) (24 gaps); BMS map sources (8 gaps).

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 1164 call pairs -- scoped 83.8%, unique 0.0%, ambiguous 0.6%, external 15.6%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| cobol | 988 | 98.6% | 0.0% | 0.5% | 0.9% |
| shell | 112 | 0.0% | 0.0% | 0.0% | 100.0% |
| jcl | 37 | 2.7% | 0.0% | 5.4% | 91.9% |
| python | 27 | 0.0% | 0.0% | 0.0% | 100.0% |

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
