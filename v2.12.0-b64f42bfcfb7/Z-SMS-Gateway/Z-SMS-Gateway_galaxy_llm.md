# ARCHITECTURAL_BRIEF: Z-SMS-Gateway
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/philhp/Z-SMS-Gateway` |
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
- **Scope:** 10 analyzed artifact(s), 1415 LOC.
- **Load-bearing artifact:** `cbl/BALANCE.cbl` -- 1 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `jcl/BUILDZ.jcl` -- pulls in 20 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `cbl/MESSAGES.cbl` at magnitude 201.16 (structural weight, not risk).
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
| Total Artifacts | 13 |
| Analyzed Artifacts (Scanned) | 10 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 3 |
| Total LOC | 1415 |
| Volatility Index | 0.3 |
| % Scanned of codebase = | 76.9% |
| Dominant Lang | COBOL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2188 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.2 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 2 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| COBOL | 4 | 1105 | 40.0% |
| JCL | 4 | 273 | 40.0% |
| MARKDOWN | 1 | 0 | 10.0% |
| CSD | 1 | 37 | 10.0% |

## 4.1 SOURCE ENCODINGS
All 10 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Micro Repo (<30 files)`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Micro Repo (<30 files)` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules 30%, Data / Markup / Trivial 20%, Parameter Forwarders Files 20%, Interface Declarations Files 10%, Many-Argument Workhorses Files 10%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 9 | 90.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1 | 10.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 3*

**Composition by Extension & Reason:**
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rex`: 1x Excluded (Unsupported Extension: '.rex')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 79.4 | 26.9 | 3.6 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 68.4 | 44.9 | 55.7 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 2.4 | 2.4 | 2.4 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 9.1 | 1.3 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 44.3 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 100.0 | 62.4 | 73.7 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 17.8 | 100.0 | 50.5 | 44.3 | 17.8 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 8 | 4 | 1 | `cbl/MESSAGES.cbl` |
| cleanup | 8 | 4 | 2 | `jcl/BUILDZ.jcl` |
| guards | 35 | 5 | 10 | `cbl/BALANCE.cbl` |
| danger | 11 | 4 | 4 | `cbl/SENDSMS.cbl` |
| concurrency | 4 | 1 | 0 | `jcl/BUILDZ.jcl` |
| connectivity | 27 | 5 | 6 | `cbl/BALANCE.cbl` |
| io | 107 | 8 | 17 | `jcl/BUILDZ.jcl` |
| crypto | 0 | 0 | 0 | - |
| ipc | 43 | 3 | 14 | `cbl/BALANCE.cbl` |
| time | 0 | 0 | 0 | - |
| serialization | 29 | 4 | 7 | `cbl/BALANCE.cbl` |
| regex | 7 | 2 | 1 | `cbl/SENDSMS.cbl` |
| events | 3 | 3 | 1 | `jcl/CSDINST.jcl` |
| tests | 0 | 0 | 0 | - |
| docs | 0 | 0 | 0 | - |
| debt | 64 | 4 | 16 | `cbl/MESSAGES.cbl` |
| mutation | 372 | 9 | 75 | `jcl/BUILDZ.jcl` |
| dead_code | 0 | 0 | 0 | - |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 1 | 1 | 0 | `cbl/MESSAGES.cbl` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.1666**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `jcl/BUILDZ.jcl` (Hits: 56)
- `cbl/BALANCE.cbl` (Hits: 17)
- `cbl/HISTORY.cbl` (Hits: 16)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **BALANCE.cbl** (`cbl/BALANCE.cbl`) — 1 inbound connections
2. **HISTORY.cbl** (`cbl/HISTORY.cbl`) — 1 inbound connections
3. **MESSAGES.cbl** (`cbl/MESSAGES.cbl`) — 1 inbound connections
4. **SENDSMS.cbl** (`cbl/SENDSMS.cbl`) — 1 inbound connections
5. **README.md** (`README.md`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **BUILDZ.jcl** (`jcl/BUILDZ.jcl`) — 20 outbound dependencies
2. **ZSMSCSD.csd** (`cics/ZSMSCSD.csd`) — 3 outbound dependencies
3. **CSDINST.jcl** (`jcl/CSDINST.jcl`) — 3 outbound dependencies
4. **BALANCE.cbl** (`cbl/BALANCE.cbl`) — 1 outbound dependencies
5. **HISTORY.cbl** (`cbl/HISTORY.cbl`) — 1 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `BALANCE` **(I/O & Config Routines)** (@ `cbl/BALANCE.cbl`) -> Impact: **38.8** | LOC: 356
- `HISTORY` **(I/O & Config Routines)** (@ `cbl/HISTORY.cbl`) -> Impact: **29.0** | LOC: 280
- `SENDSMS` **(Many-Argument Workhorses)** (@ `cbl/SENDSMS.cbl`) -> Impact: **27.2** | LOC: 145
- `MESSAGES` **(I/O & Config Routines)** (@ `cbl/MESSAGES.cbl`) -> Impact: **23.4** | LOC: 187
- `CHECK-USER-CREDIT` **(I/O & Config Routines)** (@ `cbl/MESSAGES.cbl`) -> Impact: **6.6** | LOC: 51
  * *Intent:* *==========================================================* * CHECK-USER-CREDIT * Checks if the user has enough credit to send SMS * INPUT : WS-RES-U...
- `SAVE-SMS-HISTORY` **(I/O & Config Routines)** (@ `cbl/MESSAGES.cbl`) -> Impact: **5.2** | LOC: 43
  * *Intent:* *==========================================================* * SAVE-SMS-HISTORY * LOGS SENT SMS DATA, INCLUDING STATUS AND MESSAGES ID TO DB2 * INPUT ...
- `SEND-JSON-RESPONSE` **(I/O & Config Routines)** (@ `cbl/MESSAGES.cbl`) -> Impact: **4.8** | LOC: 36
  * *Intent:* *==========================================================* * SEND-JSON-ERROR * ROUTINE TO FORMAT AND SEND JSON ERROR TO THE WEB CLIENT * * INPUT : W...
- `SEND-JSON-ERROR` **(I/O & Config Routines)** (@ `cbl/BALANCE.cbl`) -> Impact: **4.2** | LOC: 25
  * *Intent:* *==========================================================* * SEND-JSON-ERROR * ROUTINE TO FORMAT AND SEND JSON ERROR TO THE WEB CLIENT * * INPUT : W...
- `SEND-JSON-ERROR` **(I/O & Config Routines)** (@ `cbl/HISTORY.cbl`) -> Impact: **4.2** | LOC: 25
  * *Intent:* *==========================================================* * SEND-JSON-ERROR * ROUTINE TO FORMAT AND SEND JSON ERROR TO THE WEB CLIENT * * INPUT : W...
- `8000-DUMP-HEXA` **(I/O & Config Routines)** (@ `cbl/MESSAGES.cbl`) -> Impact: **4.2** | LOC: 23
  * *Intent:* *==========================================================* * 8000-DUMP-HEXA * * PURPOSE: CONVERTS RAW BYTES TO HUMAN-READABLE HEX STRING * * INPUT :...

*Function archetypes referenced above:*
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `cbl` | 4 | 489.5 | 59.69% | 0.0% |
| `jcl` | 4 | 36.66 | 0.9% | 0.0% |
| `cics` | 1 | 13.54 | 0.0% | 0.0% |
| `__monolith__` | 1 | 3.7 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `cbl/MESSAGES.cbl` -> **100.0%** Exposure
- `cbl/SENDSMS.cbl` -> **99.9835%** Exposure
- `cbl/BALANCE.cbl` -> **99.8275%** Exposure
- `cbl/HISTORY.cbl` -> **99.1%** Exposure

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
- **Unknown Dependencies:** `32` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `cbl/MESSAGES.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.478)
- **Top Global Matches:** file_cluster_2: 6.478, file_cluster_15: 7.214, file_cluster_16: 7.755
- **Magnitude:** 201.16 | **LOC:** 540 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 107.474; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (90.3%), Complexity Load (formerly Cognitive Load) (79.4%), Guard Balance (formerly Safety Score) (68.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MESSAGES` **(I/O & Config Routines)** (Impact: 23.4)
  * `CHECK-USER-CREDIT` **(I/O & Config Routines)** (Impact: 6.6)
    * *Intent:* *==========================================================* * CHECK-USER-CREDIT * Checks if the use...
  * `SAVE-SMS-HISTORY` **(I/O & Config Routines)** (Impact: 5.2)
    * *Intent:* *==========================================================* * SAVE-SMS-HISTORY * LOGS SENT SMS DATA...
  * `SEND-JSON-RESPONSE` **(I/O & Config Routines)** (Impact: 4.8)
    * *Intent:* *==========================================================* * SEND-JSON-ERROR * ROUTINE TO FORMAT A...
  * `8000-DUMP-HEXA` **(I/O & Config Routines)** (Impact: 4.2)
    * *Intent:* *==========================================================* * 8000-DUMP-HEXA * * PURPOSE: CONVERTS ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 41 instances
* *State Mutation (weighted view):* 146
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 47`, `args: 1`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 64`
* *Architecture:* `io: 5`, `import: 1`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 107.474
  * `Choke Point (Betweenness):` 0.013889 | `Ripple Effect (Closeness):` 0.111111
  * `Imports (Out-Degree: 1):` SQLCA
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `cbl/BALANCE.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.491)
- **Top Global Matches:** file_cluster_8: 8.491, file_cluster_6: 17.953, file_cluster_3: 20.731
- **Magnitude:** 127.74 | **LOC:** 510 | **CtrlFlow:** 6.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 107.474; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Mutation Surface (formerly State Flux) (99.8%), Complexity Load (formerly Cognitive Load) (59.6%), Guard Balance (formerly Safety Score) (56.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `BALANCE` **(I/O & Config Routines)** (Impact: 38.8)
  * `SEND-JSON-ERROR` **(I/O & Config Routines)** (Impact: 4.2)
    * *Intent:* *==========================================================* * SEND-JSON-ERROR * ROUTINE TO FORMAT A...
  * `SEND-JSON-RESPONSE` **(I/O & Config Routines)** (Impact: 1.8)
    * *Intent:* *==========================================================* * SEND-JSON-ERROR * ROUTINE TO FORMAT A...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 76
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 29`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 44`
* *Architecture:* `io: 17`, `import: 1`
* *Defense:* `safety: 16`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 107.474
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.111111
  * `Imports (Out-Degree: 0):` SQLCA
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `cbl/HISTORY.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 7.543)
- **Top Global Matches:** file_cluster_2: 7.543, file_cluster_15: 8.113, file_cluster_16: 8.447
- **Magnitude:** 89.52 | **LOC:** 457 | **CtrlFlow:** 5.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 107.474; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (63.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (60.0%), Guard Balance (formerly Safety Score) (54.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `HISTORY` **(I/O & Config Routines)** (Impact: 29.0)
  * `SEND-JSON-ERROR` **(I/O & Config Routines)** (Impact: 4.2)
    * *Intent:* *==========================================================* * SEND-JSON-ERROR * ROUTINE TO FORMAT A...
  * `SEND-JSON-RESPONSE` **(I/O & Config Routines)** (Impact: 1.8)
    * *Intent:* *==========================================================* * SEND-JSON-ERROR * ROUTINE TO FORMAT A...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 49
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 24`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 25`
* *Architecture:* `io: 16`, `import: 1`
* *Defense:* `safety: 10`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 107.474
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.111111
  * `Imports (Out-Degree: 0):` SQLCA
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `cbl/SENDSMS.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 6.468)
- **Top Global Matches:** file_cluster_9: 6.468, file_cluster_16: 12.363, file_cluster_15: 12.521
- **Magnitude:** 71.08 | **LOC:** 191 | **CtrlFlow:** 6.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 175.099; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (67.2%), Guard Balance (formerly Safety Score) (60.8%), Complexity Load (formerly Cognitive Load) (47.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SENDSMS` **(Many-Argument Workhorses)** (Impact: 27.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 40
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 26`, `args: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 18`
* *Architecture:* `io: 2`, `api: 1`, `import: 1`
* *Defense:* `safety: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 175.099
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.148148
  * `Imports (Out-Degree: 0):` ZSMSPWD
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `jcl/BUILDZ.jcl` (JCL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.741)
- **Top Global Matches:** file_cluster_15: 6.741, file_cluster_2: 7.601, file_cluster_11: 7.995
- **Magnitude:** 24.18 | **LOC:** 214 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **20**; blast radius 83.746; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (100.0%), Guard Balance (formerly Safety Score) (56.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (17.8%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `COMPILE` **(Parameter Forwarders)** (Impact: 3.0)
    * *Intent:* //SYSUT6 DD UNIT=VIO,SPACE=(CYL,(1,1)) //SYSUT7 DD UNIT=VIO,SPACE=(CYL,(1,1)) //SYSUT8 DD UNIT=VIO,S...
  * `COMPHIST` **(Parameter Forwarders)** (Impact: 3.0)
    * *Intent:* //SYSUT6 DD UNIT=VIO,SPACE=(CYL,(1,1)) //SYSUT7 DD UNIT=VIO,SPACE=(CYL,(1,1)) //SYSUT8 DD UNIT=VIO,S...
  * `COMPBAL` **(Parameter Forwarders)** (Impact: 3.0)
    * *Intent:* //SYSUT6 DD UNIT=VIO,SPACE=(CYL,(1,1)) //SYSUT7 DD UNIT=VIO,SPACE=(CYL,(1,1)) //SYSUT8 DD UNIT=VIO,S...
  * `COMPSMS` **(Parameter Forwarders)** (Impact: 2.9)
    * *Intent:* //IBMUSER JOB 1,NOTIFY=&SYSUID,REGION=0M //*--------------------------------------------------------...
  * `BIND` **(I/O & Config Routines)** (Impact: 2.2)
    * *Intent:* /* //*------------------------------------------------------------------* //* STEP 3 : BIND //*-----...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 139`, `args: 7`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 4`
* *Architecture:* `io: 56`
* *Defense:* `safety: 3`, `sync_locks: 4`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 83.746
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CEE.SCEELKED, CEE.SCEERUN, DFH520.CICS.SDFHCOB, DFH520.CICS.SDFHLOAD, DFH520.CICS.SDFHMAC, DSNB10.SDSNLOAD, DSNB10.SDSNMACS, IBMUSER.CBL...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cics/ZSMSCSD.csd` (CSD | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.166)
- **Top Global Matches:** file_cluster_2: 6.166, file_cluster_13: 6.576, file_cluster_17: 6.642
- **Magnitude:** 13.54 | **LOC:** 70 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 83.746; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (80.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (32.8%), Connectivity (formerly Api Exposure) (9.1%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `BAL` **(State Mutators)** (Impact: 3.2)
  * `MSGS` **(State Mutators)** (Impact: 1.8)
    * *Intent:* *--- TRANSACTION DEFINITIONS ---*
  * `HIST` **(State Mutators)** (Impact: 1.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1`, `args: 13`, `func_start: 3`, `class_start: 3`
* *Risk/State:* None
* *Architecture:* `api: 6`, `import: 9`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 83.746
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` BALANCE, HISTORY, MESSAGES
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `jcl/DDLINST.jcl` (JCL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.755)
- **Top Global Matches:** file_cluster_12: 6.755, file_cluster_15: 7.552, file_cluster_2: 7.576
- **Magnitude:** 6.98 | **LOC:** 75 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 83.746; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (73.7%), Guard Balance (formerly Safety Score) (51.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (44.3%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CREASTEP` **(I/O & Config Routines)** (Impact: 3.9)
    * *Intent:* /* //*------------------------------------------------------------------* //* STEP 2: DDL EXECUTION ...
  * `DROPSTEP` **(Parameter Forwarders)** (Impact: 1.8)
    * *Intent:* //IBMUSER JOB (ACCOUNT),'SQL INSTALL',CLASS=A,MSGCLASS=X,NOTIFY=&SYSUID //*-------------------------...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 6`, `args: 2`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`
* *Architecture:* `io: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 83.746
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` DSNB10.SDSNLOAD
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `jcl/SMSALERT.jcl` (JCL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.36)
- **Top Global Matches:** file_cluster_11: 6.36, file_cluster_2: 7.283, file_cluster_15: 8.101
- **Magnitude:** 4.18 | **LOC:** 21 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 83.746; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (80.3%), Guard Balance (formerly Safety Score) (55.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (43.1%), Complexity Load (formerly Cognitive Load) (3.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `PRODSTEP` **(I/O & Config Routines)** (Impact: 2.5)
    * *Intent:* //IBMUSER JOB (ACCOUNT),'SMS ALERT',CLASS=A,MSGCLASS=X,NOTIFY=&SYSUID //*---------------------------...
  * `SENDSMS` **(Interface Declarations)** (Impact: 1.4)
    * *Intent:* /* //*------------------------------------------------------- //* STEP 2 - ALERTE SMS IF STEP 1 FAIL...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 5`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `io: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 83.746
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` TCPIP.SEZALOAD
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 3.7 | **LOC:** 185 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 83.746
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `jcl/CSDINST.jcl` (JCL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.391)
- **Top Global Matches:** file_cluster_11: 6.391, file_cluster_2: 7.721, file_cluster_13: 8.546
- **Magnitude:** 1.32 | **LOC:** 10 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 83.746; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (17.8%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `UPDATE` **(Interface Declarations)** (Impact: 1.2)
    * *Intent:* //IBMUSER JOB (ACCOUNT),'INSTALL CSD',CLASS=A,MSGCLASS=X,NOTIFY=&SYSUID //*-------------------------...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 4`, `func_start: 1`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `io: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 83.746
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CICS520.DFHCSD, DFH520.CICS.SDFHLOAD, IBMUSER.CICS(ZSMSCSD)
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

*No file sits within 2% of a second archetype -- no mixed-responsibility candidates.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `cbl/BALANCE.cbl` -> Churn: **100.0%** | Cog Load: 59.6054% | Debt: 0.0%
- `cbl/MESSAGES.cbl` -> Churn: **90.31%** | Cog Load: 79.3984% | Debt: 0.0%
- `cbl/HISTORY.cbl` -> Churn: **63.07%** | Cog Load: 52.5341% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `cbl/MESSAGES.cbl` -> **Philippe Dedieu** (100.0% isolated ownership) | Magnitude: 201.16
- `cbl/BALANCE.cbl` -> **Philippe Dedieu** (100.0% isolated ownership) | Magnitude: 127.74
- `cbl/HISTORY.cbl` -> **Philippe Dedieu** (100.0% isolated ownership) | Magnitude: 89.52
- `cbl/SENDSMS.cbl` -> **Philippe Dedieu** (100.0% isolated ownership) | Magnitude: 71.08

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `cbl/MESSAGES.cbl` -> **Severity: 1.389** (Bridge: 0.0139 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `cbl/SENDSMS.cbl` -> **Severity: 9.008** (Embedded: 0.1481 * Error Risk: 60.8027%)
- `cbl/MESSAGES.cbl` -> **Severity: 7.597** (Embedded: 0.1111 * Error Risk: 68.3726%)
- `cbl/BALANCE.cbl` -> **Severity: 6.218** (Embedded: 0.1111 * Error Risk: 55.966%)
- `cbl/HISTORY.cbl` -> **Severity: 6.098** (Embedded: 0.1111 * Error Risk: 54.883%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `cbl/SENDSMS.cbl` -> **Severity: 17509.9** (Blast Radius: 175.099 * Doc Risk: 100.0%)
- `cbl/BALANCE.cbl` -> **Severity: 10747.4** (Blast Radius: 107.474 * Doc Risk: 100.0%)
- `cbl/HISTORY.cbl` -> **Severity: 10747.4** (Blast Radius: 107.474 * Doc Risk: 100.0%)
- `cbl/MESSAGES.cbl` -> **Severity: 10747.4** (Blast Radius: 107.474 * Doc Risk: 100.0%)
- `cics/ZSMSCSD.csd` -> **Severity: 8374.6** (Blast Radius: 83.746 * Doc Risk: 100.0%)

## 13. MAINFRAME SYSTEM FACTS (Named Relations & Record Layouts)
> **AI CONTEXT:** Named mainframe relations the structural signal counts flatten -- the call graph (`CALL`/CICS `LINK`·`XCTL`/JCL `EXEC PGM=`), the dataset boundary (`SELECT…ASSIGN` + `OPEN` modes, JCL `DD`→dataset), and record layouts (COBOL DATA DIVISION items, PL/I `DECLARE`d structures). BMS screen maps (every field's position, length and attributes, `screen_field_data`) are the 3270 UI surface. These are the schema of the system: use them to trace which program runs which, which dataset a job binds, and the shape of the records that flow between them. Extracted by the engine (`core/mainframe_boundary.py`) and carried in the master DB (`call_site_data`/`dataset_data`/`record_data`); resolution to files is redone per scan.

- **Coverage:** `9` files carry mainframe facts -- `14` call sites, `54` dataset bindings, `211` record items.

- **DB2 table access:** `22` embedded SQL statements touching `2` tables (SELECT/INSERT/UPDATE/DELETE, cursors, host variables) in `sql_statement_data`; the program x table read/write matrix is `GalaxyIR.sql_table_access()`.

- **CICS resources:** `17` CSD `DEFINE` records (FILE→DSNAME, TDQUEUE, DB2TRAN→DB2ENTRY→PLAN, MAPSET, LIBRARY, ...), full attributes in `csd_resource_data`.

- **CICS operations:** `10` EXEC CICS operations naming a resource (`10` WEB); verb, direction, VALUE-resolved name and INTO/FROM record in `cics_resource_data`.

### `jcl/BUILDZ.jcl` (JCL)
- **Calls:** `EXEC PGM IGYCRCTL`, `EXEC PGM IEWBLINK`, `EXEC PGM IKJEFT01`
- **Datasets:** `STEPLIB→IGY520.SIGYCOMP`, `STEPLIB→CEE.SCEERUN`, `STEPLIB→DFH520.CICS.SDFHLOAD`, `SYSLIB→DFH520.CICS.SDFHCOB`, `SYSLIB→DFH520.CICS.SDFHMAC`, `SYSLIB→IBMUSER.CBL`, `SYSIN→IBMUSER.CBL(SENDSMS)`, `STEPLIB→IGY520.SIGYCOMP`, `STEPLIB→CEE.SCEERUN`, `STEPLIB→DFH520.CICS.SDFHLOAD`, `STEPLIB→DSNB10.SDSNLOAD`, `STEPLIB→DSNB10.SDSNMACS` … (+36)
- **Job flow:** `COMPSMS=IGYCRCTL` -> `COMPILE=IGYCRCTL` -> `COMPHIST=IGYCRCTL` -> `COMPBAL=IGYCRCTL` -> `LKED=IEWBLINK (cond)` -> `LKED=IEWBLINK (cond)` -> `LKED=IEWBLINK (cond)` -> `BIND=IKJEFT01`; creates `&&OBJBAL`, `&&OBJHIST`, `&&OBJMOD`, `&&OBJSMS`

### `cbl/MESSAGES.cbl` (COBOL)
- **Calls:** `CALL SENDSMS`
- **Record layouts (79 items):** `WS-CONV-DATA (13)`, `DB2-VARS (11)`, `WS-PARSING-RESULTS (9)`, `WS-DEBUG-HEXA (8)`, `WS-SMS-ZONE (6)`, `WS-PARSING-WORK (6)`, `WS-FIELDS (5)`, `WS-BULK-WORK (4)`, `WS-CHARS (3)`, `WS-STATUSTXT (1)`, `WS-JSON-RESPONSE (1)`, `WS-JSON-LEN (1)` … (+11 more)
- **DB2 table access:** `ZSMS_MESSAGES (read/insert)`, `ZSMS_USERS (read/update)`
- **CICS operations:** `WEB ? (read/write)`
- **Data moves:** 79 (ADD 2, COMPUTE 9, INITIALIZE 6, MOVE 42, STRING 15, SUBTRACT 1, UNSTRING 4); most-fed items `WS-JSON-RESPONSE`, `WS-RESP-DISP`, `WS-DISPLAY-HEX`, `WS-RESP`, `WS-SMS-TEL`, `WS-SMS-TXT`
- **Unit of work:** `0` commit / `0` rollback points; handlers none; `1/1` RESP results tested

### `cbl/BALANCE.cbl` (COBOL)
- **Record layouts (60 items):** `DB2-VARS (8)`, `WS-CHARS (5)`, `DB2-VARS (3)`, `WS-STATUSTXT (1)`, `WS-JSON-RESPONSE (1)`, `WS-JSON-LEN (1)`, `WS-PTR (1)`, `WS-USERID-NAME (1)`, `WS-USERID-NAME-LEN (1)`, `WS-USERID-LEN (1)`, `WS-USERID-VAL (1)`, `WS-CREDIT-NAME (1)` … (+35 more)
- **DB2 table access:** `ZSMS_USERS (update/insert/read)`, `ZSMS_MESSAGES (read)`
- **CICS operations:** `WEB ? (write)`
- **Data moves:** 73 (COMPUTE 1, INITIALIZE 1, MOVE 24, STRING 43, SUBTRACT 4); most-fed items `WS-JSON-RESPONSE`, `WS-RESP-DISP`, `D-USER-ID`, `WS-AMOUNT-DISP`, `WS-DELIVERED-DISP`, `WS-MO-DISP`
- **Unit of work:** `0` commit / `0` rollback points; handlers none; `1/6` RESP results tested

### `cbl/HISTORY.cbl` (COBOL)
- **Record layouts (46 items):** `DB2-VARS (12)`, `WS-CHARS (5)`, `WS-STATUSTXT (1)`, `WS-JSON-RESPONSE (1)`, `WS-JSON-LEN (1)`, `WS-PTR (1)`, `WS-USERID-NAME (1)`, `WS-USERID-NAME-LEN (1)`, `WS-USERID-LEN (1)`, `WS-USERID-VAL (1)`, `WS-MSGID-NAME (1)`, `WS-MSGID-NAME-LEN (1)` … (+19 more)
- **DB2 table access:** `ZSMS_MESSAGES (update/read)`
- **CICS operations:** `WEB ? (write)`
- **Data moves:** 56 (COMPUTE 1, INITIALIZE 1, MOVE 13, STRING 39, SUBTRACT 2); most-fed items `WS-JSON-RESPONSE`, `WS-NBSMS-DIS`, `WS-RESP-DISP`, `D-USER-ID`, `WS-RESP-MSGID`, `WS-RESP-TRACKING`
- **Unit of work:** `0` commit / `0` rollback points; handlers none; `1/4` RESP results tested

### `cbl/SENDSMS.cbl` (COBOL)
- **Record layouts (26 items):** `LS-SMS-PARAM (8)`, `WS-CICS-ERRORS (4)`, `WS-EXTRACTION-TOOLS (4)`, `WS-HOST (1)`, `WS-PORT (1)`, `WS-HTTP-STATUS (1)`, `WS-SESSTOKEN (1)`, `WS-RESPONSE-BUFFER (1)`, `WS-RESP-LEN (1)`, `WS-STATUSTEXT (1)`, `WS-SMS-PATH (1)`, `WS-SMS-PATH-LEN (1)` … (+1 more)
- **CICS operations:** `WEB 10.20.0.138 (open)`, `WEB WS-SMS-PATH? (converse)`, `WEB ? (close)`
- **Data moves:** 17 (ADD 3, COMPUTE 2, MOVE 9, UNSTRING 3); most-fed items `LS-OUT-MSGID`, `LS-OUT-NBSMS`, `LS-RETOUR-CODE`, `WS-DISP-CODE`, `WS-OUT-STATUS`, `WS-SMS-PATH-LEN`
- **Unit of work:** `0` commit / `0` rollback points; handlers none; `2/2` RESP results tested

### `cics/ZSMSCSD.csd` (CSD)
- **CSD resources:** `DB2CONN x1`, `DB2ENTRY x3`, `DB2TRAN x3`, `PROGRAM x3`, `TCPIPSERVICE x1`, `TRANSACTION x3`, `URIMAP x3`
- **CICS bindings:** `DB2ENTRY ZSMSENT→MESSAGES`, `DB2ENTRY ZSMSHIS→HISTORY`, `DB2ENTRY ZSMSBAL→BALANCE`, `DB2TRAN ZSMSTRN→ZSMSENT`, `DB2TRAN ZSMSHTRN→ZSMSHIS`, `DB2TRAN ZSMSHBAL→ZSMSBAL`

### `jcl/DDLINST.jcl` (JCL)
- **Calls:** `EXEC PGM DSNUTILB`
- **Datasets:** `STEPLIB→DSNB10.SDSNLOAD`, `STEPLIB→DSNB10.SDSNLOAD`
- **Job flow:** `DROPSTEP=DSNUTILB` -> `CREASTEP=DSNUTILB (cond)`

### `jcl/SMSALERT.jcl` (JCL)
- **Calls:** `EXEC PGM IDCAMS`, `EXEC PGM IKJEFT01`
- **Datasets:** `STEPLIB→TCPIP.SEZALOAD`
- **Job flow:** `PRODSTEP=IDCAMS` -> `SENDSMS=IKJEFT01 (cond)`

### `jcl/CSDINST.jcl` (JCL)
- **Calls:** `EXEC PGM DFHCSDUP`
- **Datasets:** `STEPLIB→DFH520.CICS.SDFHLOAD`, `DFHCSD→CICS520.DFHCSD`, `SYSIN→IBMUSER.CICS(ZSMSCSD)`
- **Job flow:** `UPDATE=DFHCSDUP`

- **Mainframe skeleton completeness:** 95% (mean channel ratio; channel table in the audit report, section 7). Top missing inputs: scheduler export (CA-7 / Control-M / TWS) (4 gaps); CSD extract (DFHCSDUP LIST / CICSPlex SM), or the web / API layer that LINKs it (1 gaps).

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 24 call pairs -- scoped 41.7%, unique 4.2%, ambiguous 0.0%, external 54.2%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| jcl | 13 | 0.0% | 0.0% | 0.0% | 100.0% |
| cobol | 11 | 90.9% | 9.1% | 0.0% | 0.0% |

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
