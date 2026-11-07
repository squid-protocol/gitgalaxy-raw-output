# ARCHITECTURAL_BRIEF: aws-mainframe-modernization-carddemo
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/aws-samples/aws-mainframe-modernization-carddemo` |
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
- **Scope:** 240 analyzed artifact(s), 41272 LOC.
- **Load-bearing artifact:** `app/cpy/COCOM01Y.cpy` -- 21 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `samples/proc/BLDCIDB2.prc` -- pulls in 20 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `app/cbl/COACTUPC.cbl` at magnitude 2166.16 (structural weight, not risk).
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
| Total Artifacts | 329 |
| Analyzed Artifacts (Scanned) | 240 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 89 |
| Total LOC | 41272 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 72.9% |
| Dominant Lang | COBOL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4706 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0909 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.3312 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 48 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| COBOL | 109 | 32562 | 45.4% |
| JCL | 62 | 2200 | 25.8% |
| BMS | 21 | 5324 | 8.8% |
| HLASM | 12 | 151 | 5.0% |
| PLAINTEXT | 11 | 0 | 4.6% |
| SHELL | 9 | 297 | 3.8% |
| MARKDOWN | 6 | 0 | 2.5% |
| DB2_SQL | 6 | 53 | 2.5% |
| CSD | 4 | 685 | 1.7% |

## 4.1 SOURCE ENCODINGS
All 240 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 27%, Large Core Modules 27%, Interface Declarations Files 19%, Data / Markup / Trivial 17%, Parameter Forwarders Files 4%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 223 | 92.9% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 17 | 7.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 89*

**Composition by Extension & Reason:**
- `no_extension`: 30x Excluded: Neighborhood Micro-Mass Limit Exceeded, 15x Unsupported Format (.undeterminable), 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ps`: 12x Excluded (Unsupported Extension: '.PS')
- `.png`: 11x Excluded (Explicitly Denied Extension: '.png')
- `.ctl`: 8x Excluded (Unsupported Extension: '.ctl')
- `.zip`: 2x Excluded (Explicitly Denied Extension: '.zip')
- `.dat`: 1x Excluded (Unsupported Extension: '.dat')
- `.init`: 1x Excluded (Unsupported Extension: '.INIT')
- `.ca7`: 1x Excluded (Unsupported Extension: '.ca7')
- `.controlm`: 1x Excluded (Unsupported Extension: '.controlm')
- `.drawio`: 1x Excluded (Unsupported Extension: '.drawio')
- `.awk`: 1x Unsupported Format (.awk)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 93.7 | 15.1 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 95.3 | 20.6 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 37.8 | 1.3 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 13.0 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 42.2 | 1.5 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 14.0 | 0.2 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 23.8 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 90.0 | 1.3 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 61.4 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 757 | 54 | 8 | `app/app-authorization-ims-db2-mq/cpy-bms/COPAU00.cpy` |
| cleanup | 104 | 44 | 1 | `app/app-transaction-type-db2/cbl/COTRTLIC.cbl` |
| guards | 198 | 44 | 3 | `app/asm/COBDATFT.asm` |
| danger | 368 | 55 | 2 | `app/cbl/COACTUPC.cbl` |
| concurrency | 62 | 28 | 1 | `samples/jcl/IMSMQCMP.jcl` |
| connectivity | 159 | 71 | 2 | `app/csd/CARDDEMO.CSD` |
| io | 930 | 109 | 13 | `app/cbl/CBSTM03A.CBL` |
| crypto | 0 | 0 | 0 | - |
| ipc | 202 | 48 | 2 | `app/app-transaction-type-db2/cbl/COTRTLIC.cbl` |
| time | 90 | 38 | 1 | `app/cbl/CBIMPORT.cbl` |
| serialization | 137 | 26 | 1 | `app/cbl/COACTUPC.cbl` |
| regex | 83 | 18 | 0 | `app/cbl/COACTUPC.cbl` |
| events | 107 | 79 | 1 | `app/app-vsam-mq/cbl/COACCT01.cbl` |
| tests | 0 | 0 | 0 | - |
| docs | 18 | 9 | 0 | `app/app-transaction-type-db2/cbl/COTRTLIC.cbl` |
| debt | 487 | 40 | 4 | `app/cbl/CBEXPORT.cbl` |
| mutation | 12537 | 153 | 156 | `app/cbl/COACTUPC.cbl` |
| dead_code | 78 | 26 | 1 | `app/cbl/COACTUPC.cbl` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 4 | 2 | 0 | `scripts/upld_module.sh` |
| ui | 1269 | 42 | 3 | `app/bms/COACTUP.bms` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `app/cbl/CBSTM03A.CBL` (Hits: 97)
- `samples/proc/BLDCIDB2.prc` (Hits: 43)
- `app/app-transaction-type-db2/jcl/CREADB21.jcl` (Hits: 30)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **COCOM01Y.cpy** (`app/cpy/COCOM01Y.cpy`) — 21 inbound connections
2. **COTTL01Y.cpy** (`app/cpy/COTTL01Y.cpy`) — 21 inbound connections
3. **CSDAT01Y.cpy** (`app/cpy/CSDAT01Y.cpy`) — 21 inbound connections
4. **CSMSG01Y.cpy** (`app/cpy/CSMSG01Y.cpy`) — 21 inbound connections
5. **CSUSR01Y.cpy** (`app/cpy/CSUSR01Y.cpy`) — 14 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **BLDCIDB2.prc** (`samples/proc/BLDCIDB2.prc`) — 20 outbound dependencies
2. **COACTUPC.cbl** (`app/cbl/COACTUPC.cbl`) — 18 outbound dependencies
3. **CARDDEMO.CSD** (`app/csd/CARDDEMO.CSD`) — 18 outbound dependencies
4. **COTRTUPC.cbl** (`app/app-transaction-type-db2/cbl/COTRTUPC.cbl`) — 16 outbound dependencies
5. **COTRTLIC.cbl** (`app/app-transaction-type-db2/cbl/COTRTLIC.cbl`) — 15 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `1100-RECEIVE-MAP` **(I/O & Config Routines)** (@ `app/cbl/COACTUPC.cbl`) -> Impact: **117.3** | LOC: 387
- `3300-SETUP-SCREEN-ATTRS` **(I/O & Config Routines)** (@ `app/cbl/COACTUPC.cbl`) -> Impact: **116.5** | LOC: 451
- `0000-MAIN` **(I/O & Config Routines)** (@ `app/app-transaction-type-db2/cbl/COTRTLIC.cbl`) -> Impact: **61.0** | LOC: 400
- `VALIDATE-INPUT-DATA-FIELDS` **(I/O & Config Routines)** (@ `app/cbl/COTRN02C.cbl`) -> Impact: **56.1** | LOC: 203
  * *Intent:* *----------------------------------------------------------------* * VALIDATE-INPUT-DATA-FIELDS *-----------------------------------------------------...
- `3300-SETUP-SCREEN-ATTRS` **(I/O & Config Routines)** (@ `app/cbl/COCRDUPC.cbl`) -> Impact: **47.5** | LOC: 151
- `PROCESS-ENTER-KEY` **(I/O & Config Routines)** (@ `app/cbl/CORPT00C.cbl`) -> Impact: **41.5** | LOC: 249
  * *Intent:* *----------------------------------------------------------------* * PROCESS-ENTER-KEY *--------------------------------------------------------------...
- `3300-SETUP-SCREEN-ATTRS` **(I/O & Config Routines)** (@ `app/app-transaction-type-db2/cbl/COTRTUPC.cbl`) -> Impact: **38.8** | LOC: 95
- `0000-MAIN` **(I/O & Config Routines)** (@ `app/cbl/COCRDLIC.cbl`) -> Impact: **38.2** | LOC: 305
- `0000-MAIN` **(I/O & Config Routines)** (@ `app/app-transaction-type-db2/cbl/COTRTUPC.cbl`) -> Impact: **36.6** | LOC: 213
- `YYYY-STORE-PFKEY` **(I/O & Config Routines)** (@ `app/cpy/CSSTRPFY.cpy`) -> Impact: **33.1** | LOC: 63
  * *Intent:* * All Rights Reserved. * * Licensed under the Apache License, Version 2.0 (the "License"). * You may not use this file except in compliance with the L...

*Function archetypes referenced above:*
  * **I/O & Config Routines**: dominated by I/O and configuration handling

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `app/cbl` | 31 | 11061.26 | 69.16% | 2.74% |
| `app/app-authorization-ims-db2-mq/cbl` | 8 | 2067.84 | 51.91% | 6.86% |
| `app/app-transaction-type-db2/cbl` | 3 | 1939.9 | 74.96% | 9.93% |
| `app/app-vsam-mq/cbl` | 2 | 561.18 | 61.59% | 0.0% |
| `app/jcl` | 38 | 193.24 | 0.0% | 0.0% |
| `app/app-authorization-ims-db2-mq/ims` | 8 | 110.3 | 0.0% | 0.0% |
| `app/csd` | 1 | 86.9 | 0.0% | 0.0% |
| `app/catlg` | 1 | 79.14 | 0.0% | 0.0% |
| `samples/proc` | 4 | 49.48 | 1.24% | 0.0% |
| `samples/jcl` | 9 | 48.76 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `app/asm/MVSWAIT.asm` -> **37.7541%** Exposure
- `app/maclib/ASMWAIT.mac` -> **37.7541%** Exposure
- `app/asm/COBDATFT.asm` -> **29.7202%** Exposure
- `app/cbl/CSUTLDTC.cbl` -> **23.4296%** Exposure
- `app/cbl/COACTVWC.cbl` -> **18.179%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl` -> **100.0%** Exposure
- `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl` -> **100.0%** Exposure
- `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl` -> **100.0%** Exposure
- `app/app-transaction-type-db2/cbl/COTRTLIC.cbl` -> **100.0%** Exposure
- `app/app-vsam-mq/cbl/COACCT01.cbl` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `app/cbl/COCRDLIC.cbl` -> **5** Orphaned Functions | **0** Duplicates
- `app/cbl/COCRDSLC.cbl` -> **5** Orphaned Functions | **0** Duplicates
- `app/cbl/COACTUPC.cbl` -> **4** Orphaned Functions | **0** Duplicates
- `app/cbl/COACTVWC.cbl` -> **2** Orphaned Functions | **2** Duplicates
- `app/app-transaction-type-db2/cbl/COTRTLIC.cbl` -> **3** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `510` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `app/cbl/COACTUPC.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.699)
- **Top Global Matches:** file_cluster_4: 8.699, file_cluster_12: 8.78, file_cluster_11: 10.163
- **Magnitude:** 2166.16 | **LOC:** 4237 | **CtrlFlow:** 12.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **18**; blast radius 3.353; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (91.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `1100-RECEIVE-MAP` **(I/O & Config Routines)** (Impact: 117.3)
  * `3300-SETUP-SCREEN-ATTRS` **(I/O & Config Routines)** (Impact: 116.5)
  * `2000-DECIDE-ACTION` **(I/O & Config Routines)** (Impact: 24.1)
  * `0000-MAIN` **(I/O & Config Routines)** (Impact: 23.4)
  * `1200-EDIT-MAP-INPUTS` **(I/O & Config Routines)** (Impact: 23.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 384 instances
* *State Mutation (weighted view):* 1468
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 403`, `structural_boundaries: 155`, `func_start: 85`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 52`, `state_mutation: 700`, `dead_code: 10`, `unreferenced_by_name: 4`
* *Architecture:* `io: 11`, `api: 1`, `import: 56`
* *Defense:* `safety: 14`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.353
  * `Choke Point (Betweenness):` 0.000118 | `Ripple Effect (Closeness):` 0.004184
  * `Imports (Out-Degree: 16):` COACTUP, COCOM01Y, COTTL01Y, CSDAT01Y, CSLKPCDY, CSMSG01Y, CSMSG02Y, CSSETATY...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `app/app-transaction-type-db2/cbl/COTRTLIC.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.041)
- **Top Global Matches:** file_cluster_4: 8.041, file_cluster_12: 11.015, file_cluster_6: 11.846
- **Magnitude:** 1129.84 | **LOC:** 2099 | **CtrlFlow:** 13.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **15**; blast radius 4.55; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (93.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `0000-MAIN` **(I/O & Config Routines)** (Impact: 61.0)
  * `8000-READ-FORWARD` **(I/O & Config Routines)** (Impact: 27.1)
  * `2500-SETUP-MESSAGE` **(I/O & Config Routines)** (Impact: 22.9)
  * `2400-SETUP-SCREEN-ATTRS` **(I/O & Config Routines)** (Impact: 22.1)
  * `2300-SCREEN-ARRAY-INIT` **(I/O & Config Routines)** (Impact: 19.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 219 instances
* *State Mutation (weighted view):* 759
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 216`, `structural_boundaries: 120`, `func_start: 57`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 321`, `unreferenced_by_name: 3`
* *Architecture:* `io: 25`, `api: 1`, `import: 15`
* *Defense:* `safety: 3`, `doc: 2`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.55
  * `Choke Point (Betweenness):` 0.000141 | `Ripple Effect (Closeness):` 0.004184
  * `Imports (Out-Degree: 13):` COCOM01Y, COTRTLI, COTTL01Y, CSDAT01Y, CSDB2RPY, CSDB2RWY, CSMSG01Y, CSSTRPFY...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `app/cbl/COCRDUPC.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.076)
- **Top Global Matches:** file_cluster_4: 8.076, file_cluster_12: 9.606, file_cluster_11: 11.19
- **Magnitude:** 800.58 | **LOC:** 1561 | **CtrlFlow:** 14.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **13**; blast radius 3.353; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (91.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `3300-SETUP-SCREEN-ATTRS` **(I/O & Config Routines)** (Impact: 47.5)
  * `0000-MAIN` **(I/O & Config Routines)** (Impact: 29.9)
  * `2000-DECIDE-ACTION` **(I/O & Config Routines)** (Impact: 24.1)
  * `1100-RECEIVE-MAP` **(I/O & Config Routines)** (Impact: 15.9)
  * `3200-SETUP-SCREEN-VARS` **(I/O & Config Routines)** (Impact: 14.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 113 instances
* *State Mutation (weighted view):* 509
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 170`, `structural_boundaries: 66`, `func_start: 45`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 283`, `dead_code: 3`, `unreferenced_by_name: 1`
* *Architecture:* `io: 4`, `api: 1`, `import: 13`
* *Defense:* `safety: 7`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.353
  * `Choke Point (Betweenness):` 4.3e-05 | `Ripple Effect (Closeness):` 0.004184
  * `Imports (Out-Degree: 11):` COCOM01Y, COCRDUP, COTTL01Y, CSDAT01Y, CSMSG01Y, CSMSG02Y, CSSTRPFY, CSUSR01Y...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.834)
- **Top Global Matches:** file_cluster_4: 7.834, file_cluster_2: 8.573, file_cluster_15: 8.836
- **Magnitude:** 766.84 | **LOC:** 1033 | **CtrlFlow:** 13.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **14**; blast radius 3.872; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `PROCESS-ENTER-KEY` **(I/O & Config Routines)** (Impact: 20.9)
    * *Intent:* *****************************************************************
  * `MAIN-PARA` **(I/O & Config Routines)** (Impact: 19.0)
    * *Intent:* *****************************************************************
  * `POPULATE-AUTH-LIST` **(I/O & Config Routines)** (Impact: 14.2)
    * *Intent:* *****************************************************************
  * `INITIALIZE-AUTH-DATA` **(I/O & Config Routines)** (Impact: 12.8)
    * *Intent:* *****************************************************************
  * `PROCESS-PAGE-FORWARD` **(I/O & Config Routines)** (Impact: 12.0)
    * *Intent:* *****************************************************************
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 161 instances
* *State Mutation (weighted view):* 590
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 104`, `structural_boundaries: 57`, `args: 3`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `state_mutation: 268`, `dead_code: 1`
* *Architecture:* `io: 9`, `api: 1`, `import: 14`
* *Defense:* `safety: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.872
  * `Choke Point (Betweenness):` 0.000116 | `Ripple Effect (Closeness):` 0.004184
  * `Imports (Out-Degree: 12):` CIPAUDTY, CIPAUSMY, COCOM01Y, COPAU00, COTTL01Y, CSDAT01Y, CSMSG01Y, CSMSG02Y...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `app/app-transaction-type-db2/cbl/COTRTUPC.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.072)
- **Top Global Matches:** file_cluster_4: 8.072, file_cluster_12: 10.2, file_cluster_11: 11.678
- **Magnitude:** 740.12 | **LOC:** 1703 | **CtrlFlow:** 15.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **16**; blast radius 4.848; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (89.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (67.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `3300-SETUP-SCREEN-ATTRS` **(I/O & Config Routines)** (Impact: 38.8)
  * `0000-MAIN` **(I/O & Config Routines)** (Impact: 36.6)
  * `2000-DECIDE-ACTION` **(I/O & Config Routines)** (Impact: 29.2)
  * `3250-SETUP-INFOMSG` **(I/O & Config Routines)** (Impact: 21.8)
  * `3200-SETUP-SCREEN-VARS` **(I/O & Config Routines)** (Impact: 18.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 94 instances
* *State Mutation (weighted view):* 399
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 195`, `structural_boundaries: 97`, `func_start: 63`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 211`, `unreferenced_by_name: 1`
* *Architecture:* `io: 14`, `api: 1`, `import: 16`
* *Defense:* `safety: 6`, `doc: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.848
  * `Choke Point (Betweenness):` 0.000246 | `Ripple Effect (Closeness):` 0.008368
  * `Imports (Out-Degree: 13):` COCOM01Y, COTRTUP, COTTL01Y, CSDAT01Y, CSMSG01Y, CSMSG02Y, CSSETATY, CSSTRPFY...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `app/cbl/COCRDLIC.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.913)
- **Top Global Matches:** file_cluster_4: 7.913, file_cluster_6: 10.433, file_cluster_12: 12.109
- **Magnitude:** 719.06 | **LOC:** 1460 | **CtrlFlow:** 13.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **11**; blast radius 3.353; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (92.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (70.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `0000-MAIN` **(I/O & Config Routines)** (Impact: 38.2)
  * `9000-READ-FORWARD` **(I/O & Config Routines)** (Impact: 28.9)
  * `1250-SETUP-ARRAY-ATTRIBS` **(I/O & Config Routines)** (Impact: 27.2)
  * `9100-READ-BACKWARDS` **(I/O & Config Routines)** (Impact: 19.4)
  * `1300-SETUP-SCREEN-ATTRS` **(I/O & Config Routines)** (Impact: 18.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 81 instances
* *State Mutation (weighted view):* 459
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 150`, `structural_boundaries: 78`, `func_start: 39`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 297`, `dead_code: 7`, `unreferenced_by_name: 5`
* *Architecture:* `io: 12`, `api: 1`, `import: 11`
* *Defense:* `safety: 10`, `doc: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.353
  * `Choke Point (Betweenness):` 3.5e-05 | `Ripple Effect (Closeness):` 0.004184
  * `Imports (Out-Degree: 10):` COCOM01Y, COCRDLI, COTTL01Y, CSDAT01Y, CSMSG01Y, CSSTRPFY, CSUSR01Y, CVACT02Y...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `app/cbl/COTRN00C.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.307)
- **Top Global Matches:** file_cluster_4: 7.307, file_cluster_2: 9.568, file_cluster_15: 9.67
- **Magnitude:** 681.08 | **LOC:** 700 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **8**; blast radius 3.353; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `PROCESS-ENTER-KEY` **(I/O & Config Routines)** (Impact: 27.2)
    * *Intent:* *----------------------------------------------------------------* * PROCESS-ENTER-KEY *------------...
  * `POPULATE-TRAN-DATA` **(I/O & Config Routines)** (Impact: 16.2)
    * *Intent:* *----------------------------------------------------------------* * POPULATE-TRAN-DATA *-----------...
  * `INITIALIZE-TRAN-DATA` **(I/O & Config Routines)** (Impact: 15.8)
    * *Intent:* *----------------------------------------------------------------* * INITIALIZE-TRAN-DATA *---------...
  * `PROCESS-PAGE-FORWARD` **(I/O & Config Routines)** (Impact: 15.5)
    * *Intent:* *----------------------------------------------------------------* * PROCESS-PAGE-FORWARD *---------...
  * `PROCESS-PAGE-BACKWARD` **(I/O & Config Routines)** (Impact: 14.2)
    * *Intent:* *----------------------------------------------------------------* * PROCESS-PAGE-BACKWARD *--------...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 164 instances
* *State Mutation (weighted view):* 525
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 104`, `structural_boundaries: 60`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `state_mutation: 197`, `dead_code: 1`
* *Architecture:* `io: 4`, `api: 1`, `import: 8`
* *Defense:* `safety: 6`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.353
  * `Choke Point (Betweenness):` 2.5e-05 | `Ripple Effect (Closeness):` 0.004184
  * `Imports (Out-Degree: 6):` COCOM01Y, COTRN00, COTTL01Y, CSDAT01Y, CSMSG01Y, CVTRA05Y, DFHAID, DFHBMSCA
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `app/cbl/COUSR00C.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.321)
- **Top Global Matches:** file_cluster_4: 7.321, file_cluster_2: 9.581, file_cluster_15: 9.683
- **Magnitude:** 667.82 | **LOC:** 696 | **CtrlFlow:** 19.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **8**; blast radius 3.353; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (77.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `PROCESS-ENTER-KEY` **(I/O & Config Routines)** (Impact: 27.2)
    * *Intent:* *----------------------------------------------------------------* * PROCESS-ENTER-KEY *------------...
  * `POPULATE-USER-DATA` **(I/O & Config Routines)** (Impact: 15.9)
    * *Intent:* *----------------------------------------------------------------* * POPULATE-USER-DATA *-----------...
  * `INITIALIZE-USER-DATA` **(I/O & Config Routines)** (Impact: 15.8)
    * *Intent:* *----------------------------------------------------------------* * INITIALIZE-USER-DATA *---------...
  * `PROCESS-PAGE-FORWARD` **(I/O & Config Routines)** (Impact: 15.5)
    * *Intent:* *----------------------------------------------------------------* * PROCESS-PAGE-FORWARD *---------...
  * `PROCESS-PAGE-BACKWARD` **(I/O & Config Routines)** (Impact: 14.2)
    * *Intent:* *----------------------------------------------------------------* * PROCESS-PAGE-BACKWARD *--------...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 160 instances
* *State Mutation (weighted view):* 512
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 105`, `structural_boundaries: 59`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `state_mutation: 192`
* *Architecture:* `io: 4`, `api: 1`, `import: 8`
* *Defense:* `safety: 6`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.353
  * `Choke Point (Betweenness):` 2.3e-05 | `Ripple Effect (Closeness):` 0.004184
  * `Imports (Out-Degree: 6):` COCOM01Y, COTTL01Y, COUSR00, CSDAT01Y, CSMSG01Y, CSUSR01Y, DFHAID, DFHBMSCA
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `app/cbl/COTRN02C.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.394)
- **Top Global Matches:** file_cluster_4: 7.394, file_cluster_15: 9.004, file_cluster_2: 9.113
- **Magnitude:** 562.38 | **LOC:** 784 | **CtrlFlow:** 15.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **10**; blast radius 3.353; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (93.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `VALIDATE-INPUT-DATA-FIELDS` **(I/O & Config Routines)** (Impact: 56.1)
    * *Intent:* *----------------------------------------------------------------* * VALIDATE-INPUT-DATA-FIELDS *---...
  * `MAIN-PARA` **(I/O & Config Routines)** (Impact: 16.6)
  * `PROCESS-ENTER-KEY` **(I/O & Config Routines)** (Impact: 10.2)
    * *Intent:* *----------------------------------------------------------------* * PROCESS-ENTER-KEY *------------...
  * `VALIDATE-INPUT-KEY-FIELDS` **(I/O & Config Routines)** (Impact: 8.9)
    * *Intent:* *----------------------------------------------------------------* * VALIDATE-INPUT-KEY-FIELDS *----...
  * `WRITE-TRANSACT-FILE` **(I/O & Config Routines)** (Impact: 8.0)
    * *Intent:* *----------------------------------------------------------------* * WRITE-TRANSACT-FILE *----------...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 111 instances
* *State Mutation (weighted view):* 407
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 97`, `structural_boundaries: 84`, `args: 2`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `state_mutation: 185`
* *Architecture:* `io: 6`, `api: 1`, `import: 10`
* *Defense:* `safety: 11`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.353
  * `Choke Point (Betweenness):` 4.3e-05 | `Ripple Effect (Closeness):` 0.004184
  * `Imports (Out-Degree: 9):` COCOM01Y, COTRN02, COTTL01Y, CSDAT01Y, CSMSG01Y, CVACT01Y, CVACT03Y, CVTRA05Y...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.73)
- **Top Global Matches:** file_cluster_11: 6.73, file_cluster_2: 7.787, file_cluster_15: 7.859
- **Magnitude:** 488.62 | **LOC:** 1027 | **CtrlFlow:** 8.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **14**; blast radius 3.872; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (92.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `6000-MAKE-DECISION` **(I/O & Config Routines)** (Impact: 23.8)
    * *Intent:* * * ------------------------------------------------------------- *
  * `8400-UPDATE-SUMMARY` **(I/O & Config Routines)** (Impact: 10.6)
    * *Intent:* * * ------------------------------------------------------------- *
  * `8500-INSERT-AUTH` **(I/O & Config Routines)** (Impact: 8.5)
    * *Intent:* * * ------------------------------------------------------------- *
  * `3100-READ-REQUEST-MQ` **(I/O & Config Routines)** (Impact: 7.3)
    * *Intent:* * * ------------------------------------------------------------- *
  * `5100-READ-XREF-RECORD` **(I/O & Config Routines)** (Impact: 7.2)
    * *Intent:* * * ------------------------------------------------------------- *
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 49 instances
* *State Mutation (weighted view):* 326
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 68`, `args: 8`, `func_start: 43`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 228`, `unreferenced_by_name: 2`
* *Architecture:* `io: 17`, `api: 1`, `concurrency: 1`, `import: 16`
* *Defense:* `safety: 8`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.872
  * `Choke Point (Betweenness):` 8.9e-05 | `Ripple Effect (Closeness):` 0.004184
  * `Imports (Out-Degree: 8):` CCPAUERY, CCPAURLY, CCPAURQY, CIPAUDTY, CIPAUSMY, CMQGMOV, CMQMDV, CMQODV...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `app/cbl/CBTRN02C.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.465)
- **Top Global Matches:** file_cluster_2: 6.465, file_cluster_11: 6.604, file_cluster_15: 6.859
- **Magnitude:** 401.88 | **LOC:** 732 | **CtrlFlow:** 16.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 5.907; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (67.8%), Complexity Load (formerly Cognitive Load) (67.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `1000-DALYTRAN-GET-NEXT` **(I/O & Config Routines)** (Impact: 10.2)
    * *Intent:* *---------------------------------------------------------------*
  * `2700-UPDATE-TCATBAL` **(I/O & Config Routines)** (Impact: 9.8)
    * *Intent:* *---------------------------------------------------------------*
  * `CBTRN02C` **(I/O & Config Routines)** (Impact: 9.1)
    * *Intent:* *****************************************************************
  * `1500-B-LOOKUP-ACCT` **(I/O & Config Routines)** (Impact: 8.5)
  * `2700-A-CREATE-TCATBAL-REC` **(I/O & Config Routines)** (Impact: 6.1)
    * *Intent:* *---------------------------------------------------------------*
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 51 instances
* *State Mutation (weighted view):* 238
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 100`, `structural_boundaries: 140`, `args: 2`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `state_mutation: 136`
* *Architecture:* `io: 16`, `import: 5`
* *Defense:* `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.907
  * `Choke Point (Betweenness):` 8.8e-05 | `Ripple Effect (Closeness):` 0.004184
  * `Imports (Out-Degree: 5):` CVACT01Y, CVACT03Y, CVTRA01Y, CVTRA05Y, CVTRA06Y
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `app/cbl/COCRDSLC.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.112)
- **Top Global Matches:** file_cluster_4: 8.112, file_cluster_12: 8.619, file_cluster_11: 9.706
- **Magnitude:** 391.64 | **LOC:** 888 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **13**; blast radius 3.353; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (91.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `0000-MAIN` **(I/O & Config Routines)** (Impact: 25.2)
  * `1300-SETUP-SCREEN-ATTRS` **(I/O & Config Routines)** (Impact: 18.9)
  * `1200-SETUP-SCREEN-VARS` **(I/O & Config Routines)** (Impact: 11.1)
  * `9100-GETCARD-BYACCTCARD` **(I/O & Config Routines)** (Impact: 8.9)
  * `2220-EDIT-CARD` **(I/O & Config Routines)** (Impact: 8.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 55 instances
* *State Mutation (weighted view):* 248
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 42`, `func_start: 34`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 138`, `dead_code: 1`, `unreferenced_by_name: 5`
* *Architecture:* `io: 4`, `api: 1`, `import: 13`
* *Defense:* `safety: 6`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.353
  * `Choke Point (Betweenness):` 4.3e-05 | `Ripple Effect (Closeness):` 0.004184
  * `Imports (Out-Degree: 11):` COCOM01Y, COCRDSL, COTTL01Y, CSDAT01Y, CSMSG01Y, CSMSG02Y, CSSTRPFY, CSUSR01Y...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `app/cbl/COACTVWC.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.134)
- **Top Global Matches:** file_cluster_12: 7.134, file_cluster_11: 8.135, file_cluster_2: 8.868
- **Magnitude:** 383.26 | **LOC:** 942 | **CtrlFlow:** 8.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **15**; blast radius 3.353; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (87.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (67.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `0000-MAIN` **(I/O & Config Routines)** (Impact: 23.6)
  * `1200-SETUP-SCREEN-VARS` **(I/O & Config Routines)** (Impact: 11.8)
  * `1300-SETUP-SCREEN-ATTRS` **(I/O & Config Routines)** (Impact: 10.6)
  * `9200-GETCARDXREF-BYACCT` **(I/O & Config Routines)** (Impact: 8.4)
  * `9300-GETACCTDATA-BYACCT` **(I/O & Config Routines)** (Impact: 8.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 46 instances
* *State Mutation (weighted view):* 245
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 43`, `func_start: 35`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 153`, `dead_code: 4`, `duplicate_logic: 2`, `unreferenced_by_name: 2`
* *Architecture:* `io: 6`, `api: 1`, `import: 15`
* *Defense:* `safety: 8`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.353
  * `Choke Point (Betweenness):` 5.2e-05 | `Ripple Effect (Closeness):` 0.004184
  * `Imports (Out-Degree: 13):` COACTVW, COCOM01Y, COTTL01Y, CSDAT01Y, CSMSG01Y, CSMSG02Y, CSSTRPFY, CSUSR01Y...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `app/cbl/CBSTM03A.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.75)
- **Top Global Matches:** file_cluster_12: 6.75, file_cluster_11: 8.146, file_cluster_2: 8.828
- **Magnitude:** 382.78 | **LOC:** 925 | **CtrlFlow:** 7.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 5.907; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.8%), Complexity Load (formerly Cognitive Load) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `0000-START` **(I/O & Config Routines)** (Impact: 8.9)
  * `8500-READTRNX-READ` **(I/O & Config Routines)** (Impact: 8.5)
    * *Intent:* *---------------------------------------------------------------*
  * `4000-TRNXFILE-GET` **(I/O & Config Routines)** (Impact: 8.1)
  * `CBSTM03A` **(I/O & Config Routines)** (Impact: 7.7)
    * *Intent:* *****************************************************************
  * `8100-TRNXFILE-OPEN` **(I/O & Config Routines)** (Impact: 6.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 40 instances
* *State Mutation (weighted view):* 263
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 100`, `args: 13`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 14`, `high_risk_execution: 4`, `state_mutation: 183`
* *Architecture:* `io: 97`, `api: 1`, `import: 4`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.907
  * `Choke Point (Betweenness):` 8.8e-05 | `Ripple Effect (Closeness):` 0.004184
  * `Imports (Out-Degree: 5):` COSTM01, CUSTREC, CVACT01Y, CVACT03Y
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `app/app-authorization-ims-db2-mq/cbl/COPAUS1C.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 7.458)
- **Top Global Matches:** file_cluster_2: 7.458, file_cluster_9: 7.609, file_cluster_15: 7.707
- **Magnitude:** 370.62 | **LOC:** 605 | **CtrlFlow:** 13.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **10**; blast radius 3.872; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (80.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `READ-AUTH-RECORD` **(I/O & Config Routines)** (Impact: 15.1)
  * `MAIN-PARA` **(I/O & Config Routines)** (Impact: 13.5)
  * `POPULATE-AUTH-DETAILS` **(I/O & Config Routines)** (Impact: 11.4)
  * `MARK-AUTH-FRAUD` **(I/O & Config Routines)** (Impact: 8.8)
  * `UPDATE-AUTH-DETAILS` **(I/O & Config Routines)** (Impact: 7.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 75 instances
* *State Mutation (weighted view):* 270
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 42`, `args: 4`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 120`
* *Architecture:* `io: 7`, `api: 1`, `import: 10`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.872
  * `Choke Point (Betweenness):` 7.2e-05 | `Ripple Effect (Closeness):` 0.004184
  * `Imports (Out-Degree: 9):` CIPAUDTY, CIPAUSMY, COCOM01Y, COPAU01, COTTL01Y, CSDAT01Y, CSMSG01Y, CSMSG02Y...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `app/cbl/CORPT00C.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.13)
- **Top Global Matches:** file_cluster_4: 7.13, file_cluster_6: 10.015, file_cluster_2: 12.103
- **Magnitude:** 363.46 | **LOC:** 650 | **CtrlFlow:** 10.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **8**; blast radius 3.353; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (90.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `PROCESS-ENTER-KEY` **(I/O & Config Routines)** (Impact: 41.5)
    * *Intent:* *----------------------------------------------------------------* * PROCESS-ENTER-KEY *------------...
  * `SUBMIT-JOB-TO-INTRDR` **(I/O & Config Routines)** (Impact: 12.4)
    * *Intent:* *----------------------------------------------------------------* * SUBMIT-JOB-TO-INTRDR *---------...
  * `MAIN-PARA` **(I/O & Config Routines)** (Impact: 11.0)
  * `WIRTE-JOBSUB-TDQ` **(I/O & Config Routines)** (Impact: 5.0)
    * *Intent:* *----------------------------------------------------------------* * WIRTE-JOBSUB-TDQ *-------------...
  * `SEND-TRNRPT-SCREEN` **(I/O & Config Routines)** (Impact: 4.2)
    * *Intent:* *----------------------------------------------------------------* * SEND-TRNRPT-SCREEN *-----------...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 63 instances
* *State Mutation (weighted view):* 270
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 48`, `args: 2`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 144`
* *Architecture:* `io: 9`, `api: 1`, `import: 8`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.353
  * `Choke Point (Betweenness):` 3.4e-05 | `Ripple Effect (Closeness):` 0.004184
  * `Imports (Out-Degree: 7):` COCOM01Y, CORPT00, COTTL01Y, CSDAT01Y, CSMSG01Y, CVTRA05Y, DFHAID, DFHBMSCA
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `app/cbl/CBACT04C.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.698)
- **Top Global Matches:** file_cluster_11: 6.698, file_cluster_15: 6.762, file_cluster_2: 6.977
- **Magnitude:** 337.14 | **LOC:** 653 | **CtrlFlow:** 15.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 5.907; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (66.1%), Complexity Load (formerly Cognitive Load) (61.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CBACT04C` **(Compute Cores)** (Impact: 15.4)
    * *Intent:* *****************************************************************
  * `1000-TCATBALF-GET-NEXT` **(I/O & Config Routines)** (Impact: 10.2)
    * *Intent:* *---------------------------------------------------------------*
  * `1200-GET-INTEREST-RATE` **(I/O & Config Routines)** (Impact: 8.3)
    * *Intent:* *---------------------------------------------------------------*
  * `1300-B-WRITE-TX` **(I/O & Config Routines)** (Impact: 7.2)
    * *Intent:* *---------------------------------------------------------------*
  * `1100-GET-ACCT-DATA` **(I/O & Config Routines)** (Impact: 7.0)
    * *Intent:* *---------------------------------------------------------------*
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 40 instances
* *State Mutation (weighted view):* 191
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 86`, `structural_boundaries: 130`, `args: 3`, `func_start: 22`, `class_start: 1`
* *Risk/State:* `state_mutation: 111`
* *Architecture:* `io: 13`, `api: 1`, `import: 5`
* *Defense:* `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.907
  * `Choke Point (Betweenness):` 8.8e-05 | `Ripple Effect (Closeness):` 0.004184
  * `Imports (Out-Degree: 5):` CVACT01Y, CVACT03Y, CVTRA01Y, CVTRA02Y, CVTRA05Y
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `app/cbl/CBTRN03C.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.104)
- **Top Global Matches:** file_cluster_11: 6.104, file_cluster_2: 6.753, file_cluster_15: 7.031
- **Magnitude:** 330.9 | **LOC:** 650 | **CtrlFlow:** 15.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **5**; blast radius 8.621; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (66.3%), Complexity Load (formerly Cognitive Load) (60.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CBTRN03C` **(I/O & Config Routines)** (Impact: 11.9)
    * *Intent:* *****************************************************************
  * `0550-DATEPARM-READ` **(I/O & Config Routines)** (Impact: 10.2)
    * *Intent:* * Read the date parameter file.
  * `1000-TRANFILE-GET-NEXT` **(I/O & Config Routines)** (Impact: 10.2)
    * *Intent:* ***************************************************************** * I/O ROUTINES TO ACCESS A KSDS, V...
  * `1111-WRITE-REPORT-REC` **(I/O & Config Routines)** (Impact: 5.8)
    * *Intent:* *---------------------------------------------------------------*
  * `0000-TRANFILE-OPEN` **(I/O & Config Routines)** (Impact: 5.8)
    * *Intent:* *---------------------------------------------------------------*
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 36 instances
* *State Mutation (weighted view):* 188
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 146`, `args: 2`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 116`
* *Architecture:* `io: 13`, `import: 5`
* *Defense:* `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.621
  * `Choke Point (Betweenness):` 0.000176 | `Ripple Effect (Closeness):` 0.008368
  * `Imports (Out-Degree: 5):` CVACT03Y, CVTRA03Y, CVTRA04Y, CVTRA05Y, CVTRA07Y
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `app/cbl/COBIL00C.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.47)
- **Top Global Matches:** file_cluster_4: 7.47, file_cluster_2: 9.074, file_cluster_11: 9.196
- **Magnitude:** 330.7 | **LOC:** 573 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **10**; blast radius 3.353; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (77.0%), Guard Balance (formerly Safety Score) (71.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `PROCESS-ENTER-KEY` **(I/O & Config Routines)** (Impact: 22.6)
    * *Intent:* *----------------------------------------------------------------* * PROCESS-ENTER-KEY *------------...
  * `MAIN-PARA` **(I/O & Config Routines)** (Impact: 15.6)
  * `WRITE-TRANSACT-FILE` **(I/O & Config Routines)** (Impact: 7.9)
    * *Intent:* *----------------------------------------------------------------* * WRITE-TRANSACT-FILE *----------...
  * `READ-ACCTDAT-FILE` **(I/O & Config Routines)** (Impact: 6.5)
    * *Intent:* *----------------------------------------------------------------* * READ-ACCTDAT-FILE *------------...
  * `READ-CXACAIX-FILE` **(I/O & Config Routines)** (Impact: 6.5)
    * *Intent:* *----------------------------------------------------------------* * READ-CXACAIX-FILE *------------...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 61 instances
* *State Mutation (weighted view):* 231
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 57`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `state_mutation: 109`
* *Architecture:* `io: 7`, `api: 1`, `import: 10`
* *Defense:* `safety: 13`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.353
  * `Choke Point (Betweenness):` 3.4e-05 | `Ripple Effect (Closeness):` 0.004184
  * `Imports (Out-Degree: 8):` COBIL00, COCOM01Y, COTTL01Y, CSDAT01Y, CSMSG01Y, CVACT01Y, CVACT03Y, CVTRA05Y...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `app/cbl/CBTRN01C.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.502)
- **Top Global Matches:** file_cluster_2: 6.502, file_cluster_11: 6.704, file_cluster_15: 6.87
- **Magnitude:** 310.3 | **LOC:** 495 | **CtrlFlow:** 16.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 3.193; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.6%), Complexity Load (formerly Cognitive Load) (66.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `1000-DALYTRAN-GET-NEXT` **(I/O & Config Routines)** (Impact: 10.2)
    * *Intent:* ***************************************************************** * READS FILE * *******************...
  * `MAIN-PARA` **(I/O & Config Routines)** (Impact: 9.2)
  * `0000-DALYTRAN-OPEN` **(I/O & Config Routines)** (Impact: 5.8)
    * *Intent:* *---------------------------------------------------------------*
  * `0100-CUSTFILE-OPEN` **(I/O & Config Routines)** (Impact: 5.8)
    * *Intent:* *---------------------------------------------------------------*
  * `0200-XREFFILE-OPEN` **(I/O & Config Routines)** (Impact: 5.8)
    * *Intent:* *---------------------------------------------------------------*
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 66 instances
* *State Mutation (weighted view):* 201
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 105`, `args: 2`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `state_mutation: 69`
* *Architecture:* `io: 12`, `import: 6`
* *Defense:* `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.193
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` CVACT01Y, CVACT02Y, CVACT03Y, CVCUS01Y, CVTRA05Y, CVTRA06Y
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `app/app-vsam-mq/cbl/COACCT01.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.706)
- **Top Global Matches:** file_cluster_2: 5.706, file_cluster_15: 6.46, file_cluster_17: 7.226
- **Magnitude:** 299.8 | **LOC:** 621 | **CtrlFlow:** 8.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **7**; blast radius 4.55; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.7%), Complexity Load (formerly Cognitive Load) (61.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `4000-PROCESS-REQUEST-REPLY` **(I/O & Config Routines)** (Impact: 10.6)
  * `3000-GET-REQUEST` **(I/O & Config Routines)** (Impact: 7.8)
  * `1000-CONTROL` **(I/O & Config Routines)** (Impact: 6.2)
  * `4100-PUT-REPLY` **(I/O & Config Routines)** (Impact: 5.9)
  * `9000-ERROR` **(I/O & Config Routines)** (Impact: 5.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 36 instances
* *State Mutation (weighted view):* 213
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 41`, `args: 9`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `state_mutation: 141`
* *Architecture:* `io: 2`, `api: 1`, `concurrency: 1`, `import: 7`
* *Defense:* `safety: 4`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.55
  * `Choke Point (Betweenness):` 1.8e-05 | `Ripple Effect (Closeness):` 0.004184
  * `Imports (Out-Degree: 1):` CMQGMOV, CMQMDV, CMQODV, CMQPMOV, CMQTML, CMQV, CVACT01Y
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `app/cbl/COUSR02C.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.732)
- **Top Global Matches:** file_cluster_11: 6.732, file_cluster_2: 6.742, file_cluster_15: 6.911
- **Magnitude:** 289.96 | **LOC:** 415 | **CtrlFlow:** 14.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **8**; blast radius 3.353; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.4%), Complexity Load (formerly Cognitive Load) (75.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `UPDATE-USER-INFO` **(I/O & Config Routines)** (Impact: 18.4)
    * *Intent:* *----------------------------------------------------------------* * UPDATE-USER-INFO *-------------...
  * `MAIN-PARA` **(I/O & Config Routines)** (Impact: 17.9)
  * `PROCESS-ENTER-KEY` **(I/O & Config Routines)** (Impact: 7.5)
    * *Intent:* *----------------------------------------------------------------* * PROCESS-ENTER-KEY *------------...
  * `READ-USER-SEC-FILE` **(I/O & Config Routines)** (Impact: 6.7)
    * *Intent:* *----------------------------------------------------------------* * READ-USER-SEC-FILE *-----------...
  * `UPDATE-USER-SEC-FILE` **(I/O & Config Routines)** (Impact: 6.7)
    * *Intent:* *----------------------------------------------------------------* * UPDATE-USER-SEC-FILE *---------...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 64 instances
* *State Mutation (weighted view):* 216
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 43`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 88`
* *Architecture:* `io: 2`, `api: 1`, `import: 8`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.353
  * `Choke Point (Betweenness):` 2.3e-05 | `Ripple Effect (Closeness):` 0.004184
  * `Imports (Out-Degree: 6):` COCOM01Y, COTTL01Y, COUSR02, CSDAT01Y, CSMSG01Y, CSUSR01Y, DFHAID, DFHBMSCA
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `app/app-vsam-mq/cbl/CODATE01.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.515)
- **Top Global Matches:** file_cluster_2: 5.515, file_cluster_15: 6.511, file_cluster_17: 7.051
- **Magnitude:** 261.38 | **LOC:** 525 | **CtrlFlow:** 8.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 4.55; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.9%), Complexity Load (formerly Cognitive Load) (61.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `3000-GET-REQUEST` **(I/O & Config Routines)** (Impact: 7.8)
  * `1000-CONTROL` **(I/O & Config Routines)** (Impact: 6.2)
  * `4100-PUT-REPLY` **(I/O & Config Routines)** (Impact: 5.9)
  * `9000-ERROR` **(I/O & Config Routines)** (Impact: 5.8)
  * `2400-OPEN-OUTPUT-QUEUE` **(I/O & Config Routines)** (Impact: 5.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 31 instances
* *State Mutation (weighted view):* 185
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 37`, `args: 9`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `state_mutation: 123`
* *Architecture:* `api: 1`, `concurrency: 1`, `import: 6`
* *Defense:* `safety: 2`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.55
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004184
  * `Imports (Out-Degree: 0):` CMQGMOV, CMQMDV, CMQODV, CMQPMOV, CMQTML, CMQV
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `app/cbl/CBACT01C.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.018)
- **Top Global Matches:** file_cluster_11: 6.018, file_cluster_2: 6.674, file_cluster_15: 7.028
- **Magnitude:** 224.16 | **LOC:** 431 | **CtrlFlow:** 11.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 5.907; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.7%), Complexity Load (formerly Cognitive Load) (63.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `1000-ACCTFILE-GET-NEXT` **(I/O & Config Routines)** (Impact: 10.7)
    * *Intent:* ***************************************************************** * I/O ROUTINES TO ACCESS A KSDS, V...
  * `0000-ACCTFILE-OPEN` **(I/O & Config Routines)** (Impact: 5.8)
    * *Intent:* *---------------------------------------------------------------*
  * `2000-OUTFILE-OPEN` **(I/O & Config Routines)** (Impact: 5.8)
  * `3000-ARRFILE-OPEN` **(I/O & Config Routines)** (Impact: 5.8)
    * *Intent:* *---------------------------------------------------------------*
  * `4000-VBRFILE-OPEN` **(I/O & Config Routines)** (Impact: 5.8)
    * *Intent:* *---------------------------------------------------------------*
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 40 instances
* *State Mutation (weighted view):* 149
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 94`, `args: 3`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `state_mutation: 69`
* *Architecture:* `io: 14`, `import: 2`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.907
  * `Choke Point (Betweenness):` 7e-05 | `Ripple Effect (Closeness):` 0.004184
  * `Imports (Out-Degree: 3):` CODATECN, CVACT01Y
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `app/cbl/COUSR03C.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.431)
- **Top Global Matches:** file_cluster_11: 6.431, file_cluster_2: 6.503, file_cluster_15: 6.735
- **Magnitude:** 209.22 | **LOC:** 360 | **CtrlFlow:** 13.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **8**; blast radius 3.353; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.5%), Guard Balance (formerly Safety Score) (73.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MAIN-PARA` **(I/O & Config Routines)** (Impact: 17.8)
  * `PROCESS-ENTER-KEY` **(I/O & Config Routines)** (Impact: 7.4)
    * *Intent:* *----------------------------------------------------------------* * PROCESS-ENTER-KEY *------------...
  * `READ-USER-SEC-FILE` **(I/O & Config Routines)** (Impact: 6.7)
    * *Intent:* *----------------------------------------------------------------* * READ-USER-SEC-FILE *-----------...
  * `DELETE-USER-SEC-FILE` **(I/O & Config Routines)** (Impact: 6.6)
    * *Intent:* *----------------------------------------------------------------* * DELETE-USER-SEC-FILE *---------...
  * `DELETE-USER-INFO` **(I/O & Config Routines)** (Impact: 6.0)
    * *Intent:* *----------------------------------------------------------------* * DELETE-USER-INFO *-------------...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 42 instances
* *State Mutation (weighted view):* 149
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 38`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 65`
* *Architecture:* `io: 3`, `api: 1`, `import: 8`
* *Defense:* `safety: 4`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.353
  * `Choke Point (Betweenness):` 2.3e-05 | `Ripple Effect (Closeness):` 0.004184
  * `Imports (Out-Degree: 6):` COCOM01Y, COTTL01Y, COUSR03, CSDAT01Y, CSMSG01Y, CSUSR01Y, DFHAID, DFHBMSCA
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `app/cbl/COUSR02C.cbl` (COBOL) | Magnitude: 289.96 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 303, state_mutation: 88, branch: 44, structural_boundaries: 43
- `app/cbl/CBACT04C.cbl` (COBOL) | Magnitude: 337.14 | Delta: **0.064** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 552, structural_boundaries: 130, state_mutation: 111, branch: 86
- `app/cbl/COUSR03C.cbl` (COBOL) | Magnitude: 209.22 | Delta: **0.072** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 251, state_mutation: 65, structural_boundaries: 38, branch: 34
- `app/cbl/COTRN01C.cbl` (COBOL) | Magnitude: 165.02 | Delta: **0.106** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 231, state_mutation: 60, structural_boundaries: 27, branch: 25

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `app/cbl/COACTUPC.cbl` (COBOL) | Magnitude: 2166.16 | Delta: **0.081** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 3368, state_mutation: 700, branch: 403, structural_boundaries: 155

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `app/cpy/CSUTLDPY.cpy` (COBOL) | Magnitude: 13.97 | Delta: **0.137** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 289, state_mutation: 69, branch: 46, structural_boundaries: 18

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `app/app-transaction-type-db2/cbl/COTRTUPC.cbl` -> **Severity: 0.025** (Bridge: 0.0002 * Flux: 99.9971%)
- `app/cbl/CBTRN03C.cbl` -> **Severity: 0.018** (Bridge: 0.0002 * Flux: 99.9989%)
- `app/app-transaction-type-db2/cbl/COTRTLIC.cbl` -> **Severity: 0.014** (Bridge: 0.0001 * Flux: 100.0%)
- `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl` -> **Severity: 0.012** (Bridge: 0.0001 * Flux: 100.0%)
- `app/cbl/COACTUPC.cbl` -> **Severity: 0.012** (Bridge: 0.0001 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `app/cpy/CSSTRPFY.cpy` -> **Severity: 2.613** (Embedded: 0.0308 * Error Risk: 84.8191%)
- `app/cbl/CSUTLDTC.cbl` -> **Severity: 0.999** (Embedded: 0.0149 * Error Risk: 66.8519%)
- `app/cbl/COMEN01C.cbl` -> **Severity: 0.957** (Embedded: 0.0126 * Error Risk: 76.2671%)
- `app/cpy/CSSETATY.cpy` -> **Severity: 0.701** (Embedded: 0.0131 * Error Risk: 53.6364%)
- `app/cbl/COADM01C.cbl` -> **Severity: 0.575** (Embedded: 0.0084 * Error Risk: 68.669%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `app/maclib/ASMWAIT.mac` -> **Severity: 1017.5** (Blast Radius: 10.175 * Doc Risk: 100.0%)
- `app/cbl/CBTRN03C.cbl` -> **Severity: 862.1** (Blast Radius: 8.621 * Doc Risk: 100.0%)
- `app/asm/MVSWAIT.asm` -> **Severity: 821.4** (Blast Radius: 8.214 * Doc Risk: 100.0%)
- `app/cbl/CSUTLDTC.cbl` -> **Severity: 678.2** (Blast Radius: 6.782 * Doc Risk: 100.0%)
- `app/app-authorization-ims-db2-mq/cbl/CBPAUP0C.cbl` -> **Severity: 590.7** (Blast Radius: 5.907 * Doc Risk: 100.0%)

## 13. MAINFRAME SYSTEM FACTS (Named Relations & Record Layouts)
> **AI CONTEXT:** Named mainframe relations the structural signal counts flatten -- the call graph (`CALL`/CICS `LINK`·`XCTL`/JCL `EXEC PGM=`), the dataset boundary (`SELECT…ASSIGN` + `OPEN` modes, JCL `DD`→dataset), and record layouts (COBOL DATA DIVISION items, PL/I `DECLARE`d structures). BMS screen maps (every field's position, length and attributes, `screen_field_data`) are the 3270 UI surface. These are the schema of the system: use them to trace which program runs which, which dataset a job binds, and the shape of the records that flow between them. Extracted by the engine (`core/mainframe_boundary.py`) and carried in the master DB (`call_site_data`/`dataset_data`/`record_data`); resolution to files is redone per scan.

- **Coverage:** `202` files carry mainframe facts -- `282` call sites, `371` dataset bindings, `11262` record items.

- **DB2 schemas:** `31` columns of `EXEC SQL DECLARE ... TABLE` (inline or DCLGEN members), full shape in `sql_table_data`.

- **DB2 table access:** `22` embedded SQL statements touching `3` tables (SELECT/INSERT/UPDATE/DELETE, cursors, host variables) in `sql_statement_data`; the program x table read/write matrix is `GalaxyIR.sql_table_access()`.

- **CICS resources:** `134` CSD `DEFINE` records (FILE→DSNAME, TDQUEUE, DB2TRAN→DB2ENTRY→PLAN, MAPSET, LIBRARY, ...), full attributes in `csd_resource_data`.

- **CICS operations:** `107` EXEC CICS operations naming a resource (`58` FILE, `47` MAP, `2` QUEUE); verb, direction, VALUE-resolved name and INTO/FROM record in `cics_resource_data`.

- **CICS task control:** `3` commands (`3` RETRIEVE); child transid (or its STRING-built pattern), channel, CHILD/REQID token and timing in `cics_task_data`.

### `app/cbl/COACTUPC.cbl` (COBOL)
- **Calls:** `XCTL CDEMO-TO-PROGRAM`, `RETURN TRANSID LIT-THISTRANID`
- **COMMAREA passed:** `XCTL CDEMO-TO-PROGRAM ← CARDDEMO-COMMAREA`, `RETURN TRANSID CAUP ← WS-COMMAREA LENGTH(LENGTH OF WS-COMMAREA)`
- **Record layouts (578 items):** `WS-MISC-STORAGE (376)`, `WS-THIS-PROGCOMMAREA (162)`, `WS-LITERALS (31)`, `DFHCOMMAREA (2)`, `LIT-ALL-ALPHA-FROM (1)`, `LIT-ALL-ALPHANUM-FROM (1)`, `LIT-ALL-NUM-FROM (1)`, `LIT-ALPHA-SPACES-TO (1)`, `LIT-ALPHANUM-SPACES-TO (1)`, `LIT-NUM-SPACES-TO (1)`, `WS-COMMAREA (1)`
- **CICS operations:** `MAP CACTUPA (read/write)`, `FILE CXACAIX (read)`, `FILE ACCTDAT (read/update)`, `FILE CUSTDAT (read/update)`
- **Data moves:** 751 (COMPUTE 5, INITIALIZE 14, MOVE 620, STRING 112); most-fed items `WS-EDIT-ALPHANUM-ONLY`, `WS-RETURN-MSG`, `WS-EDIT-CURRENCY-9-2-F`, `ERROR-RESP`, `ERROR-RESP2`, `WS-EDIT-SIGNED-NUMBER-9V2-X`
- **Unit of work:** `1` commit / `1` rollback points; handlers `ABEND->ABEND-ROUTINE`, `ABEND->CANCEL`; `7/10` RESP results tested

### `app/app-authorization-ims-db2-mq/cpy-bms/COPAU00.cpy` (COBOL)
- **Record layouts (748 items):** `COPAU0AI (374)`, `COPAU0AO (374)`

### `app/cpy-bms/COTRN00.CPY` (COBOL)
- **Record layouts (712 items):** `COTRN0AI (356)`, `COTRN0AO (356)`

### `app/cpy-bms/COUSR00.CPY` (COBOL)
- **Record layouts (712 items):** `COUSR0AI (356)`, `COUSR0AO (356)`

### `app/cpy-bms/COACTUP.CPY` (COBOL)
- **Record layouts (652 items):** `CACTUPAI (326)`, `CACTUPAO (326)`

### `app/cpy-bms/COCRDLI.CPY` (COBOL)
- **Record layouts (544 items):** `CCRDLIAI (272)`, `CCRDLIAO (272)`

### `app/app-transaction-type-db2/cbl/COTRTLIC.cbl` (COBOL)
- **Calls:** `XCTL CDEMO-TO-PROGRAM`, `XCTL LIT-ADDTPGM`, `RETURN TRANSID LIT-THISTRANID`
- **COMMAREA passed:** `XCTL CDEMO-TO-PROGRAM ← CARDDEMO-COMMAREA`, `XCTL COTRTUPC ← CARDDEMO-COMMAREA`, `RETURN TRANSID CTLI ← WS-COMMAREA LENGTH(LENGTH OF WS-COMMAREA)`
- **Record layouts (251 items):** `WS-MISC-STORAGE (141)`, `WS-THIS-PROGCOMMAREA (33)`, `WS-CONSTANTS (23)`, `FILLER (23)`, `FILLER (22)`, `DFHCOMMAREA (2)`, `LIT-ALL-ALPHA-FROM (1)`, `LIT-ALL-ALPHANUM-FROM (1)`, `LIT-ALL-NUM-FROM (1)`, `LIT-ALPHA-SPACES-TO (1)`, `LIT-ALPHANUM-SPACES-TO (1)`, `LIT-NUM-SPACES-TO (1)` … (+1 more)
- **DB2 table access:** `CARDDEMO.TRANSACTION_TYPE (read/update/delete)`
- **CICS operations:** `MAP CTRTLIA (read/write)`
- **Data moves:** 226 (ADD 3, COMPUTE 9, INITIALIZE 19, MOVE 186, STRING 7, SUBTRACT 2); most-fed items `WS-DISP-SQLCODE`, `WS-START-KEY`, `CDEMO-LAST-MAP`, `CDEMO-FROM-PROGRAM`, `CDEMO-LAST-MAPSET`, `CDEMO-FROM-TRANID`
- **Unit of work:** `3` commit / `0` rollback points; handlers none; `0/2` RESP results tested

### `app/app-transaction-type-db2/cpy-bms/COTRTLI.cpy` (COBOL)
- **Record layouts (484 items):** `CTRTLIAI (242)`, `CTRTLIAO (242)`

### `app/cpy-bms/COACTVW.CPY` (COBOL)
- **Record layouts (448 items):** `CACTVWAI (224)`, `CACTVWAO (224)`

### `app/cbl/CBSTM03A.CBL` (COBOL)
- **Calls:** `CALL CBSTM03B`, `CALL CEE3ABD`
- **Datasets:** `STMTFILE(OUTPUT)`, `HTMLFILE(OUTPUT)`
- **Record layouts (168 items):** `STATEMENT-LINES (62)`, `HTML-LINES (46)`, `WS-M03B-AREA (13)`, `TIOT-ENTRY (10)`, `WS-TRNX-TABLE (6)`, `COMP-VARIABLES (5)`, `MISC-VARIABLES (5)`, `TIOT-BLOCK (4)`, `WS-TRN-TBL-CNTR (3)`, `PSA-BLOCK (3)`, `TCB-BLOCK (3)`, `COMP3-VARIABLES (2)` … (+6 more)
- **Data moves:** 229 (ADD 3, COMPUTE 2, INITIALIZE 3, MOVE 79, STRING 48, WRITE 94); most-fed items `FD-HTMLFILE-REC`, `FD-STMTFILE-REC`, `ST-ADD3`, `HTML-ADDR-LN`, `HTML-BSIC-LN`, `HTML-TRAN-LN`

### `app/cbl/COCRDUPC.cbl` (COBOL)
- **Calls:** `XCTL CDEMO-TO-PROGRAM`, `RETURN TRANSID LIT-THISTRANID`
- **COMMAREA passed:** `XCTL CDEMO-TO-PROGRAM ← CARDDEMO-COMMAREA`, `RETURN TRANSID CCUP ← WS-COMMAREA LENGTH(LENGTH OF WS-COMMAREA)`
- **Record layouts (179 items):** `WS-MISC-STORAGE (111)`, `WS-THIS-PROGCOMMAREA (42)`, `WS-LITERALS (23)`, `DFHCOMMAREA (2)`, `WS-COMMAREA (1)`
- **CICS operations:** `MAP CCRDUPA (read/write)`, `FILE CARDDAT (read/update)`
- **Data moves:** 219 (INITIALIZE 13, MOVE 201, STRING 5); most-fed items `ACCTSIDA OF CCRDUPAI`, `CARDSIDA OF CCRDUPAI`, `CRDNAMEA OF CCRDUPAI`, `CRDSTCDA OF CCRDUPAI`, `EXPMONA OF CCRDUPAI`, `EXPYEARA OF CCRDUPAI`
- **Unit of work:** `1` commit / `0` rollback points; handlers `ABEND->ABEND-ROUTINE`, `ABEND->CANCEL`; `3/6` RESP results tested

### `app/app-authorization-ims-db2-mq/cbl/COPAUS0C.cbl` (COBOL)
- **Calls:** `RETURN TRANSID WS-CICS-TRANID`, `XCTL CDEMO-TO-PROGRAM`
- **COMMAREA passed:** `RETURN TRANSID CPVS ← CARDDEMO-COMMAREA`, `XCTL CDEMO-TO-PROGRAM ← CARDDEMO-COMMAREA`
- **Record layouts (86 items):** `WS-VARIABLES (33)`, `WS-SWITCHES (32)`, `WS-IMS-VARIABLES (17)`, `DFHCOMMAREA (2)`, `PENDING-AUTH-SUMMARY (1)`, `PENDING-AUTH-DETAILS (1)`
- **CICS operations:** `MAP COPAU0A (read/write)`, `FILE CXACAIX (read)`, `FILE ACCTDAT (read)`, `FILE CUSTDAT (read)`
- **Data moves:** 298 (COMPUTE 3, INITIALIZE 1, MOVE 237, STRING 57); most-fed items `WS-MESSAGE`, `WS-REAS-CD-DIS`, `WS-RESP-CD-DIS`, `CDEMO-CPVS-AUTH-KEYS`, `CDEMO-CPVS-PAU-SEL-FLG`, `CDEMO-CPVS-PAU-SELECTED`
- **IMS DL/I:** `GNP PAUTDTL1`, `GU PAUTSUM0`, `SCHD PSB-NAME`, `TERM`
- **Unit of work:** `1` commit / `0` rollback points; handlers none; `3/4` RESP results tested

### `app/cbl/COCRDLIC.cbl` (COBOL)
- **Calls:** `XCTL LIT-MENUPGM`, `XCTL CCARD-NEXT-PROG`, `RETURN TRANSID LIT-THISTRANID`
- **COMMAREA passed:** `XCTL COMEN01C ← CARDDEMO-COMMAREA`, `XCTL CCARD-NEXT-PROG ← CARDDEMO-COMMAREA`, `RETURN TRANSID CCLI ← WS-COMMAREA LENGTH(LENGTH OF WS-COMMAREA)`
- **Record layouts (129 items):** `WS-MISC-STORAGE (79)`, `WS-THIS-PROGCOMMAREA (27)`, `WS-CONSTANTS (20)`, `DFHCOMMAREA (2)`, `WS-COMMAREA (1)`
- **CICS operations:** `MAP CCRDLIA (read/write)`, `FILE CARDDAT (browse/read)`
- **Data moves:** 237 (ADD 3, COMPUTE 1, INITIALIZE 8, MOVE 222, SUBTRACT 3); most-fed items `CDEMO-LAST-MAP`, `CDEMO-FROM-PROGRAM`, `CDEMO-LAST-MAPSET`, `WS-EDIT-SELECT`, `CDEMO-FROM-TRANID`, `CCARD-NEXT-MAP`
- **Unit of work:** `0` commit / `0` rollback points; handlers none; `4/8` RESP results tested

### `app/app-authorization-ims-db2-mq/cbl/COPAUA0C.cbl` (COBOL)
- **Calls:** `CALL MQOPEN`, `CALL MQGET`, `CALL MQPUT1`, `CALL MQCLOSE`
- **Record layouts (116 items):** `WS-VARIABLES (40)`, `WS-SWITCHES (36)`, `WS-IMS-VARIABLES (17)`, `DFHCOMMAREA (2)`, `W01-HCONN-REQUEST (1)`, `W01-HOBJ-REQUEST (1)`, `W01-BUFFLEN (1)`, `W01-DATALEN (1)`, `W01-GET-BUFFER (1)`, `W02-HCONN-REPLY (1)`, `W02-BUFFLEN (1)`, `W02-DATALEN (1)` … (+13 more)
- **CICS operations:** `FILE CCXREF (read)`, `FILE ACCTDAT (read)`, `FILE CUSTDAT (read)`, `QUEUE CSSL (write)`
- **CICS task control:** `RETRIEVE`
- **MQ queues:** `<trigger> (get)`, `<reply_to> (put)`
- **Data moves:** 211 (ADD 6, COMPUTE 16, INITIALIZE 1, MOVE 158, STRING 12, UNSTRING 18); most-fed items `WS-CODE-DISPLAY`, `ERR-CODE-1`, `ERR-EVENT-KEY`, `ERR-CODE-2`, `W02-PUT-BUFFER`, `IMS-RETURN-CODE`
- **IMS DL/I:** `SCHD PSB-NAME`, `TERM`, `GU PAUTSUM0`, `REPL PAUTSUM0`, `ISRT PAUTSUM0`, `ISRT PAUTSUM0,PAUTDTL1`
- **Unit of work:** `1` commit / `0` rollback points; handlers none; `4/7` RESP results tested

### `app/app-authorization-ims-db2-mq/cpy-bms/COPAU01.cpy` (COBOL)
- **Record layouts (328 items):** `COPAU1AI (164)`, `COPAU1AO (164)`

### `app/app-transaction-type-db2/cbl/COTRTUPC.cbl` (COBOL)
- **Calls:** `XCTL CDEMO-TO-PROGRAM`, `RETURN TRANSID LIT-THISTRANID`
- **COMMAREA passed:** `XCTL CDEMO-TO-PROGRAM ← CARDDEMO-COMMAREA`, `RETURN TRANSID CTTU ← WS-COMMAREA LENGTH(LENGTH OF WS-COMMAREA)`
- **Record layouts (146 items):** `WS-MISC-STORAGE (89)`, `WS-THIS-PROGCOMMAREA (30)`, `WS-LITERALS (18)`, `DFHCOMMAREA (2)`, `LIT-ALL-ALPHA-FROM (1)`, `LIT-ALL-ALPHANUM-FROM (1)`, `LIT-ALL-NUM-FROM (1)`, `LIT-ALPHA-SPACES-TO (1)`, `LIT-ALPHANUM-SPACES-TO (1)`, `LIT-NUM-SPACES-TO (1)`, `WS-COMMAREA (1)`
- **DB2 table access:** `CARDDEMO.TRANSACTION_TYPE (read/update/insert/delete)`
- **CICS operations:** `MAP CTRTUPA (read/write)`
- **Data moves:** 154 (COMPUTE 5, INITIALIZE 13, MOVE 100, STRING 36); most-fed items `WS-RETURN-MSG`, `INFOMSGA OF CTRTUPAI`, `DCL-TR-TYPE`, `TRTYPCDA OF CTRTUPAI`, `WS-DISP-SQLCODE`, `ABEND-CULPRIT`
- **Unit of work:** `4` commit / `0` rollback points; handlers `ABEND->ABEND-ROUTINE`, `ABEND->CANCEL`; `0/3` RESP results tested

### `app/app-vsam-mq/cbl/COACCT01.cbl` (COBOL)
- **Calls:** `CALL MQOPEN`, `CALL MQGET`, `CALL MQPUT`, `CALL MQCLOSE`
- **Record layouts (99 items):** `WS-ACCT-RESPONSE (23)`, `MQ-ERR-DISPLAY (10)`, `WS-VARIABLES (10)`, `WS-CICS-RESP-CDS (5)`, `QUEUE-INFO (5)`, `WS-DATE-TIME (4)`, `REQUEST-MSG-COPY (4)`, `WS-MQ-MSG-FLAG (2)`, `WS-RESP-QUEUE-STS (2)`, `WS-ERR-QUEUE-STS (2)`, `WS-REPLY-QUEUE-STS (2)`, `MQ-QUEUE (1)` … (+29 more)
- **CICS operations:** `FILE ACCTDAT (read)`
- **CICS task control:** `RETRIEVE`
- **MQ queues:** `<trigger> (get)`, `CARD.DEMO.REPLY.ACCT (put)`, `CARD.DEMO.ERROR (put)`
- **Data moves:** 161 (ADD 1, COMPUTE 24, INITIALIZE 3, MOVE 121, STRING 12); most-fed items `MQ-APPL-CONDITION-CODE`, `MQ-APPL-REASON-CODE`, `MQ-OPTIONS`, `MQ-APPL-QUEUE-NAME`, `MQPMO-OPTIONS`, `MQ-HOBJ`
- **Unit of work:** `1` commit / `0` rollback points; handlers none; `2/2` RESP results tested

### `app/cbl/COTRN02C.cbl` (COBOL)
- **Calls:** `RETURN TRANSID WS-TRANID`, `CALL CSUTLDTC`, `XCTL CDEMO-TO-PROGRAM`
- **COMMAREA passed:** `RETURN TRANSID CT02 ← CARDDEMO-COMMAREA`, `XCTL CDEMO-TO-PROGRAM ← CARDDEMO-COMMAREA`
- **Record layouts (43 items):** `WS-VARIABLES (24)`, `CSUTLDTC-PARM (17)`, `DFHCOMMAREA (2)`
- **CICS operations:** `MAP COTRN2A (read/write)`, `FILE CXACAIX (read)`, `FILE CCXREF (read)`, `FILE TRANSACT (browse/read/write)`
- **Data moves:** 210 (ADD 1, COMPUTE 4, INITIALIZE 1, MOVE 200, STRING 4); most-fed items `CARDNINI OF COTRN2AI`, `ACTIDINI OF COTRN2AI`, `CSUTLDTC-DATE`, `CSUTLDTC-DATE-FORMAT`, `TRNAMTI OF COTRN2AI`, `WS-MESSAGE`
- **Unit of work:** `0` commit / `0` rollback points; handlers none; `5/6` RESP results tested

### `app/cbl/CBTRN02C.cbl` (COBOL)
- **Calls:** `CALL CEE3ABD`
- **Datasets:** `DALYTRAN(INPUT)`, `TRANFILE(OUTPUT)`, `XREFFILE(INPUT)`, `DALYREJS(OUTPUT)`, `ACCTFILE(I-O)`, `TCATBALF(I-O)`
- **Record layouts (92 items):** `FILLER (15)`, `COBOL-TS (9)`, `FD-TRAN-CAT-BAL-RECORD⟵TCATBAL-FILE (6)`, `WS-COUNTERS (4)`, `FD-TRAN-RECORD⟵DALYTRAN-FILE (3)`, `FD-TRANFILE-REC⟵TRANSACT-FILE (3)`, `FD-XREFFILE-REC⟵XREF-FILE (3)`, `FD-REJS-RECORD⟵DALYREJS-FILE (3)`, `FD-ACCTFILE-REC⟵ACCOUNT-FILE (3)`, `DALYTRAN-STATUS (3)`, `TRANFILE-STATUS (3)`, `XREFFILE-STATUS (3)` … (+15 more)
- **Keyed files:** `TRANSACT-FILE INDEXED/RANDOM key FD-TRANS-ID`, `XREF-FILE INDEXED/RANDOM key FD-XREF-CARD-NUM`, `ACCOUNT-FILE INDEXED/RANDOM key FD-ACCT-ID`, `TCATBAL-FILE INDEXED/RANDOM key FD-TRAN-CAT-KEY`
- **Data moves:** 151 (ADD 7, COMPUTE 3, INITIALIZE 1, MOVE 131, READ 4, REWRITE 2, WRITE 3); most-fed items `IO-STATUS`, `WS-TEMP-BAL`, `FD-TRAN-CAT-BAL-RECORD`, `IO-STATUS-04`, `TRAN-CAT-BAL`, `ACCT-CURR-BAL`

### `app/cbl/COACTVWC.cbl` (COBOL)
- **Calls:** `XCTL CDEMO-TO-PROGRAM`, `RETURN TRANSID LIT-THISTRANID`
- **COMMAREA passed:** `XCTL CDEMO-TO-PROGRAM ← CARDDEMO-COMMAREA`, `RETURN TRANSID CAVW ← WS-COMMAREA LENGTH(LENGTH OF WS-COMMAREA)`
- **Record layouts (96 items):** `WS-MISC-STORAGE (59)`, `WS-LITERALS (30)`, `WS-THIS-PROGCOMMAREA (4)`, `DFHCOMMAREA (2)`, `WS-COMMAREA (1)`
- **CICS operations:** `MAP CACTVWA (read/write)`, `FILE CXACAIX (read)`, `FILE ACCTDAT (read)`, `FILE CUSTDAT (read)`
- **Data moves:** 144 (INITIALIZE 5, MOVE 113, STRING 26); most-fed items `WS-RETURN-MSG`, `ERROR-RESP`, `ERROR-RESP2`, `ACCTSIDC OF CACTVWAO`, `ACSTSSNO OF CACTVWAO`, `CCARD-ERROR-MSG`
- **Unit of work:** `0` commit / `0` rollback points; handlers `ABEND->ABEND-ROUTINE`, `ABEND->CANCEL`; `3/6` RESP results tested

*(+182 more files with mainframe facts; full detail in `record_data`/`call_site_data`/`dataset_data`.)*

- **Mainframe skeleton completeness:** 95% (mean channel ratio; channel table in the audit report, section 7). Top missing inputs: scheduler export (CA-7 / Control-M / TWS) (56 gaps); application programs (source or load-module list) (22 gaps); JCL and PROC libraries (1 gaps).

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 1221 call pairs -- scoped 77.3%, unique 1.3%, ambiguous 5.0%, external 16.4%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| cobol | 1003 | 93.9% | 1.5% | 0.0% | 4.6% |
| jcl | 161 | 1.2% | 0.0% | 37.9% | 60.9% |
| shell | 56 | 0.0% | 0.0% | 0.0% | 100.0% |
| hlasm | 1 | 0.0% | 100.0% | 0.0% | 0.0% |

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
