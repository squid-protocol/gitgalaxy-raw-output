# ARCHITECTURAL_BRIEF: cash-account-cobol
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/IBMStockTrader/cash-account-cobol.git` |
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
- **Scope:** 7 analyzed artifact(s), 384 LOC.
- **Load-bearing artifact:** `COBOL/DCLCASH.cpy` -- 1 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `COBOL/CASH00.cbl` -- pulls in 3 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `COBOL/CASH00.cbl` at magnitude 132.18 (structural weight, not risk).
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
| Total Artifacts | 9 |
| Analyzed Artifacts (Scanned) | 7 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 2 |
| Total LOC | 384 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 77.8% |
| Dominant Lang | COBOL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 1 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| COBOL | 3 | 246 | 42.9% |
| JCL | 3 | 138 | 42.9% |
| MARKDOWN | 1 | 0 | 14.3% |

## 4.1 SOURCE ENCODINGS
All 7 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Micro Repo (<30 files)`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Micro Repo (<30 files)` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules 57%, Declarative / Non-Code 29%, Data / Markup / Trivial 14%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 6 | 85.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1 | 14.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 2*

**Composition by Extension & Reason:**
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 1x Excluded (Explicitly Denied Extension: '.png')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 91.2 | 15.2 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 66.7 | 30.7 | 25.5 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 2.4 | 2.3 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 2.5 | 0.4 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 16.7 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 66.7 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1 | 1 | 0 | `COBOL/CASH00.cbl` |
| cleanup | 1 | 1 | 0 | `COBOL/CASH00.cbl` |
| guards | 9 | 2 | 3 | `COBOL/CASH00.cbl` |
| danger | 9 | 3 | 3 | `DB2-DDL/DB2DDL.jcl` |
| concurrency | 0 | 0 | 0 | - |
| connectivity | 1 | 1 | 0 | `COBOL/CASH00.cbl` |
| io | 38 | 6 | 13 | `COBOL/CASH00.cbl` |
| crypto | 0 | 0 | 0 | - |
| ipc | 18 | 3 | 1 | `COBOL/CASH00.cbl` |
| time | 2 | 1 | 0 | `COBOL/CASH00.cbl` |
| serialization | 0 | 0 | 0 | - |
| regex | 0 | 0 | 0 | - |
| events | 6 | 3 | 2 | `DB2-DDL/DB2BIND.jcl` |
| tests | 2 | 1 | 0 | `COBOL/CASH00.cbl` |
| docs | 0 | 0 | 0 | - |
| debt | 6 | 1 | 0 | `COBOL/CASH00.cbl` |
| mutation | 91 | 4 | 22 | `COBOL/CASH00.cbl` |
| dead_code | 0 | 0 | 0 | - |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `COBOL/CASH00.cbl` (Hits: 17)
- `DB2-DDL/DB2DDL.jcl` (Hits: 13)
- `DB2-DDL/DB2BIND.jcl` (Hits: 5)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **DCLCASH.cpy** (`COBOL/DCLCASH.cpy`) — 1 inbound connections
2. **DCLFRANK.cpy** (`COBOL/DCLFRANK.cpy`) — 1 inbound connections
3. **CASH00.cbl** (`COBOL/CASH00.cbl`) — 0 inbound connections
4. **DB2BIND.jcl** (`DB2-DDL/DB2BIND.jcl`) — 0 inbound connections
5. **DB2DDL.jcl** (`DB2-DDL/DB2DDL.jcl`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **CASH00.cbl** (`COBOL/CASH00.cbl`) — 3 outbound dependencies
2. **DB2BIND.jcl** (`DB2-DDL/DB2BIND.jcl`) — 2 outbound dependencies
3. **DB2DDL.jcl** (`DB2-DDL/DB2DDL.jcl`) — 1 outbound dependencies
4. **README.md** (`README.md`) — 1 outbound dependencies
5. **DCLCASH.cpy** (`COBOL/DCLCASH.cpy`) — 0 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `CASH00` **(I/O & Config Routines)** (@ `COBOL/CASH00.cbl`) -> Impact: **11.4** | LOC: 69
- `CASH-ACCT-CREDIT` **(I/O & Config Routines)** (@ `COBOL/CASH00.cbl`) -> Impact: **4.5** | LOC: 33
- `CASH-ACCT-DEBIT` **(I/O & Config Routines)** (@ `COBOL/CASH00.cbl`) -> Impact: **4.5** | LOC: 32
- `CASH-ACCT-UPDATE` **(I/O & Config Routines)** (@ `COBOL/CASH00.cbl`) -> Impact: **4.0** | LOC: 20
- `CASH-ACCT-DELETE` **(I/O & Config Routines)** (@ `COBOL/CASH00.cbl`) -> Impact: **3.9** | LOC: 18
- `CASH-ACCT-READ` **(I/O & Config Routines)** (@ `COBOL/CASH00.cbl`) -> Impact: **3.8** | LOC: 15
- `CASH-ACCT-ADD` **(I/O & Config Routines)** (@ `COBOL/CASH00.cbl`) -> Impact: **3.6** | LOC: 12
- `BIND` **(I/O & Config Routines)** (@ `DB2-DDL/DB2BIND.jcl`) -> Impact: **3.1** | LOC: 41
  * *Intent:* //DB2BIND JOB (ACCT#),'BIND PROGRAMS',NOTIFY=&SYSUID,CLASS=A, // MSGCLASS=H,MSGLEVEL=(1,1),SCHENV=<wlm-env> //* //* STOCK TRADER BINDS //*
- `CRTABS` **(I/O & Config Routines)** (@ `DB2-DDL/DB2DDL.jcl`) -> Impact: **2.4** | LOC: 27
  * *Intent:* /* //* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> //* CREATE TABLES //* <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< //*
- `CREATE` **(I/O & Config Routines)** (@ `DB2-DDL/DB2DDL.jcl`) -> Impact: **2.2** | LOC: 24
  * *Intent:* //DB2DDL JOB (ACCT#),'DB2 create',NOTIFY=&SYSUID,CLASS=A,MSGCLASS=H, // MSGLEVEL=(1,1),SCHENV=<wlm-env> //JOBLIB DD DSN=SYS1.DSND00A.SDSNLOAD,DISP=SHR...

*Function archetypes referenced above:*
  * **I/O & Config Routines**: dominated by I/O and configuration handling

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `COBOL` | 3 | 133.67 | 30.4% | 0.0% |
| `DB2-DDL` | 2 | 13.88 | 0.0% | 0.0% |
| `VSAM` | 1 | 1.88 | 0.0% | 0.0% |
| `__monolith__` | 1 | 1.0 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `COBOL/CASH00.cbl` -> **99.9999%** Exposure

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
- **Unknown Dependencies:** `7` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `COBOL/CASH00.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 7.377)
- **Top Global Matches:** file_cluster_2: 7.377, file_cluster_12: 7.625, file_cluster_15: 8.11
- **Magnitude:** 132.18 | **LOC:** 270 | **CtrlFlow:** 9.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 127.389; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (91.2%), Guard Balance (formerly Safety Score) (66.7%), Connectivity (formerly Api Exposure) (2.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CASH00` **(I/O & Config Routines)** (Impact: 11.4)
  * `CASH-ACCT-CREDIT` **(I/O & Config Routines)** (Impact: 4.5)
  * `CASH-ACCT-DEBIT` **(I/O & Config Routines)** (Impact: 4.5)
  * `CASH-ACCT-UPDATE` **(I/O & Config Routines)** (Impact: 4.0)
  * `CASH-ACCT-DELETE` **(I/O & Config Routines)** (Impact: 3.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 91
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 19`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 47`
* *Architecture:* `io: 17`, `api: 1`, `import: 3`
* *Defense:* `safety: 6`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 127.389
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` DCLCASH, DCLFRANK, SQLCA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `DB2-DDL/DB2DDL.jcl` (JCL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.844)
- **Top Global Matches:** file_cluster_2: 5.844, file_cluster_17: 7.428, file_cluster_15: 7.545
- **Magnitude:** 9.96 | **LOC:** 104 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 127.389; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (51.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CRTABS` **(I/O & Config Routines)** (Impact: 2.4)
    * *Intent:* /* //* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> //* CREATE TABLES //* <<<<<<<<<<<<<<<<<<<<<<...
  * `CREATE` **(I/O & Config Routines)** (Impact: 2.2)
    * *Intent:* //DB2DDL JOB (ACCT#),'DB2 create',NOTIFY=&SYSUID,CLASS=A,MSGCLASS=H, // MSGLEVEL=(1,1),SCHENV=<wlm-e...
  * `CRINDX` **(I/O & Config Routines)** (Impact: 1.9)
    * *Intent:* /* //* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> //* CREATE INDEXES //* <<<<<<<<<<<<<<<<<<<<<...
  * `CRGRACC` **(I/O & Config Routines)** (Impact: 1.8)
    * *Intent:* //* //* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> //* GRANT DB2 TABLES ACCESSES //* <<<<<<<<<...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *High Risk Execution (weighted view):* 1
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 21`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 4`
* *Architecture:* `io: 13`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 127.389
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` SYS1.DSND00A.SDSNLOAD
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `DB2-DDL/DB2BIND.jcl` (JCL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.763)
- **Top Global Matches:** file_cluster_2: 5.763, file_cluster_17: 7.438, file_cluster_13: 7.644
- **Magnitude:** 3.92 | **LOC:** 47 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 127.389; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (66.5%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `BIND` **(I/O & Config Routines)** (Impact: 3.1)
    * *Intent:* //DB2BIND JOB (ACCT#),'BIND PROGRAMS',NOTIFY=&SYSUID,CLASS=A, // MSGCLASS=H,MSGLEVEL=(1,1),SCHENV=<w...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 7`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 3`
* *Architecture:* `io: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 127.389
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` SYS1.DSND00A.SDSNLOAD, SYSD.STOCK.DBRMLIB
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `VSAM/DEFKSDS.jcl` (JCL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.639)
- **Top Global Matches:** file_cluster_2: 5.639, file_cluster_17: 7.306, file_cluster_11: 7.522
- **Magnitude:** 1.88 | **LOC:** 17 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `STEPNAME` **(I/O & Config Routines)** (Impact: 1.6)
    * *Intent:* //DEFKSDS JOB (P0L1),'STOCK TRADER KSDS',MSGCLASS=A,CLASS=A, // MSGLEVEL=(1,1),REGION=0M,NOTIFY=&SYS...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`, `func_start: 1`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `io: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 127.389
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 1.0 | **LOC:** 7 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 127.389; role: Isolated/Orphan
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 127.389
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` architecture-diagram.png
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `COBOL/DCLFRANK.cpy` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.144)
- **Top Global Matches:** file_cluster_2: 4.144, file_cluster_17: 5.817, file_cluster_13: 7.147
- **Magnitude:** 0.76 | **LOC:** 27 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 181.529; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* `io: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 181.529
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.166667
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `COBOL/DCLCASH.cpy` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.678)
- **Top Global Matches:** file_cluster_2: 4.678, file_cluster_17: 6.17, file_cluster_13: 7.458
- **Magnitude:** 0.73 | **LOC:** 23 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 181.529; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* `io: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 181.529
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.166667
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

*No file sits within 2% of a second archetype -- no mixed-responsibility candidates.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `COBOL/CASH00.cbl` -> **Severity: 12738.9** (Blast Radius: 127.389 * Doc Risk: 100.0%)
- `DB2-DDL/DB2BIND.jcl` -> **Severity: 12738.9** (Blast Radius: 127.389 * Doc Risk: 100.0%)
- `DB2-DDL/DB2DDL.jcl` -> **Severity: 12738.9** (Blast Radius: 127.389 * Doc Risk: 100.0%)
- `VSAM/DEFKSDS.jcl` -> **Severity: 12738.9** (Blast Radius: 127.389 * Doc Risk: 100.0%)

## 13. MAINFRAME SYSTEM FACTS (Named Relations & Record Layouts)
> **AI CONTEXT:** Named mainframe relations the structural signal counts flatten -- the call graph (`CALL`/CICS `LINK`·`XCTL`/JCL `EXEC PGM=`), the dataset boundary (`SELECT…ASSIGN` + `OPEN` modes, JCL `DD`→dataset), and record layouts (COBOL DATA DIVISION items, PL/I `DECLARE`d structures). BMS screen maps (every field's position, length and attributes, `screen_field_data`) are the 3270 UI surface. These are the schema of the system: use them to trace which program runs which, which dataset a job binds, and the shape of the records that flow between them. Extracted by the engine (`core/mainframe_boundary.py`) and carried in the master DB (`call_site_data`/`dataset_data`/`record_data`); resolution to files is redone per scan.

- **Coverage:** `6` files carry mainframe facts -- `11` call sites, `3` dataset bindings, `45` record items.

- **DB2 schemas:** `8` columns of `EXEC SQL DECLARE ... TABLE` (inline or DCLGEN members), full shape in `sql_table_data`.

- **DB2 table access:** `12` embedded SQL statements touching `2` tables (SELECT/INSERT/UPDATE/DELETE, cursors, host variables) in `sql_statement_data`; the program x table read/write matrix is `GalaxyIR.sql_table_access()`.

- **CICS operations:** `1` EXEC CICS operations naming a resource (`1` FILE); verb, direction, VALUE-resolved name and INTO/FROM record in `cics_resource_data`.

### `COBOL/CASH00.cbl` (COBOL)
- **Record layouts (35 items):** `WS-VSAM-RECORD (8)`, `WS-COMMAREA (6)`, `WS-VSAM-KEY (4)`, `BALANCE-GRP (3)`, `CUST-NAME (3)`, `DFHCOMMAREA (2)`, `WS-CALC (1)`, `WS-CURRENCY-KEY (1)`, `WS-MSG (1)`, `WS-ASKTIME (1)`, `WS-DATE (1)`, `WS-TIME (1)` … (+3 more)
- **DB2 table access:** `STOCKTRD.CASHACCOUNTY (read/insert/update/delete)`, `STOCKTRD.FRANKFURT1 (read)`
- **CICS operations:** `FILE HISTORY (write)`
- **Data moves:** 48 (COMPUTE 6, MOVE 42); most-fed items `WS-CALC`, `BALANCE`, `BALANC-RATE`, `WS-BALANCE`, `WS-CURRENCY`, `WS-CURRENCY-KEY`
- **Unit of work:** `0` commit / `0` rollback points; handlers none; `0/0` RESP results tested

### `DB2-DDL/DB2DDL.jcl` (JCL)
- **Calls:** `EXEC PGM IKJEFT01`, `EXEC PGM IKJEFT01 RUN PROGRAM`
- **Datasets:** `JOBLIB→SYS1.DSND00A.SDSNLOAD`
- **Job flow:** `CREATE=IKJEFT01` -> `CRTABS=IKJEFT01` -> `CRGRACC=IKJEFT01` -> `CRINDX=IKJEFT01`

### `DB2-DDL/DB2BIND.jcl` (JCL)
- **Calls:** `EXEC PGM IKJEFT01`, `EXEC PGM IKJEFT01 RUN PROGRAM`
- **Datasets:** `STEPLIB→SYS1.DSND00A.SDSNLOAD`, `DBRMLIB→SYSD.STOCK.DBRMLIB`
- **Job flow:** `BIND=IKJEFT01`

### `COBOL/DCLFRANK.cpy` (COBOL)
- **Record layouts (6 items):** `DCLFRANKFURT1 (6)`
- **DB2 tables declared:** `STOCKTRD.FRANKFURT1 (5 cols)`

### `COBOL/DCLCASH.cpy` (COBOL)
- **Record layouts (4 items):** `DCLCASHACCOUNTY (4)`
- **DB2 tables declared:** `STOCKTRD.CASHACCOUNTY (3 cols)`

### `VSAM/DEFKSDS.jcl` (JCL)
- **Calls:** `EXEC PGM IDCAMS`
- **VSAM defines:** `CLUSTER SYSD.STOCK.HISTORY KEYS(29 0)`
- **Job flow:** `STEPNAME=IDCAMS`

- **Mainframe skeleton completeness:** 50% (mean channel ratio; channel table in the audit report, section 7). Top missing inputs: scheduler export (CA-7 / Control-M / TWS) (3 gaps); CSD extract (DFHCSDUP LIST / CICSPlex SM), or the web / API layer that LINKs it (1 gaps).

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 12 call pairs -- scoped 50.0%, unique 0.0%, ambiguous 0.0%, external 50.0%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| cobol | 6 | 100.0% | 0.0% | 0.0% | 0.0% |
| jcl | 6 | 0.0% | 0.0% | 0.0% | 100.0% |

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
