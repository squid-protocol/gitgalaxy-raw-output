# ARCHITECTURAL_BRIEF: cobol-unit-test
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/neopragma/cobol-unit-test` |
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
- **Scope:** 43 analyzed artifact(s), 5502 LOC.
- **Load-bearing artifact:** `src/main/cobol/copy/DFHEIBLK.CPY` -- 2 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `padder.py` -- pulls in 2 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `src/main/cobol/ZUTZCPC.CBL` at magnitude 1966.7 (structural weight, not risk).
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
| Modularity | 0.6667 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.25 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 0 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| COBOL | 27 | 5054 | 62.8% |
| PLAINTEXT | 6 | 0 | 14.0% |
| SHELL | 5 | 206 | 11.6% |
| BATCH | 3 | 216 | 7.0% |
| MARKDOWN | 1 | 0 | 2.3% |
| PYTHON | 1 | 26 | 2.3% |

## 4.1 SOURCE ENCODINGS
All 43 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules 49%, Data / Markup / Trivial 19%, Declarative / Non-Code 16%, Interface Declarations Files 12%, Large Core Modules (2) 2%
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
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 83.5 | 39.4 | 54.3 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 99.6 | 26.2 | 12.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 6.6 | 2.4 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 7.7 | 1.0 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 53.4 | 70.8 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 14.6 | 0.6 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 70.8 | 100.0 | 100.0 |
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
| io | 91 | 15 | 4 | `src/main/cobol/ZUTZCPC.CBL` |
| crypto | 0 | 0 | 0 | - |
| ipc | 23 | 11 | 3 | `convert-bad.cbl` |
| time | 0 | 0 | 0 | - |
| serialization | 73 | 11 | 2 | `src/main/cobol/ZUTZCPC.CBL` |
| regex | 23 | 2 | 0 | `src/main/cobol/ZUTZCPC.CBL` |
| events | 0 | 0 | 0 | - |
| tests | 5 | 2 | 0 | `src/main/cobol/ZUTZCPC.CBL` |
| docs | 0 | 0 | 0 | - |
| debt | 132 | 17 | 8 | `run-examples` |
| mutation | 1020 | 25 | 21 | `src/main/cobol/ZUTZCPC.CBL` |
| dead_code | 43 | 21 | 4 | `src/main/cobol/ZUTZCPC.CBL` |
| credential | 23 | 1 | 0 | `src/main/cobol/ZUTZCPC.CBL` |
| threat | 0 | 0 | 0 | - |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/main/cobol/ZUTZCPC.CBL` (Hits: 32)
- `run-ut` (Hits: 10)
- `compile` (Hits: 9)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **DFHEIBLK.CPY** (`src/main/cobol/copy/DFHEIBLK.CPY`) — 2 inbound connections
2. **CARD2.CBL** (`src/main/cobol/CARD2.CBL`) — 1 inbound connections
3. **CARD3.CBL** (`src/main/cobol/CARD3.CBL`) — 1 inbound connections
4. **CICSDEMO.CBL** (`src/main/cobol/CICSDEMO.CBL`) — 1 inbound connections
5. **SUBPROG.CBL** (`src/main/cobol/SUBPROG.CBL`) — 1 inbound connections

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
- `UT-ASSERT-ACCESSES` **(I/O & Config Routines)** (@ `src/main/cobol/copy/ZUTZCPD.CPY`) -> Impact: **18.1** | LOC: 83
- `CONVERT-BAD2` **(I/O & Config Routines)** (@ `convert-bad2.cbl`) -> Impact: **16.9** | LOC: 119
- `5060-PARSE-HAPPENED-SPEC` **(I/O & Config Routines)** (@ `src/main/cobol/ZUTZCPC.CBL`) -> Impact: **15.7** | LOC: 54
- `CONVERT-BAD` **(I/O & Config Routines)** (@ `convert-bad.cbl`) -> Impact: **14.7** | LOC: 74
- `UT-LOOKUP-MOCK` **(I/O & Config Routines)** (@ `src/main/cobol/copy/ZUTZCPD.CPY`) -> Impact: **13.9** | LOC: 39
- `2200-IDENTIFY-CARD-TYPE` **(I/O & Config Routines)** (@ `src/main/cobol/CARD1.CBL`) -> Impact: **13.3** | LOC: 26
- `2200-IDENTIFY-CARD-TYPE` **(I/O & Config Routines)** (@ `src/main/cobol/CARD2.CBL`) -> Impact: **13.3** | LOC: 26
- `5020-VERIFY-CALL-MOCK` **(I/O & Config Routines)** (@ `src/main/cobol/ZUTZCPC.CBL`) -> Impact: **12.9** | LOC: 98

*Function archetypes referenced above:*
  * **I/O & Config Routines**: dominated by I/O and configuration handling

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src/main/cobol` | 20 | 2440.02 | 30.28% | 45.68% |
| `__monolith__` | 9 | 266.34 | 31.63% | 0.0% |
| `src/test/cobol` | 2 | 59.2 | 12.38% | 0.0% |
| `win` | 3 | 49.32 | 0.0% | 0.0% |
| `src/main/cobol/copy` | 3 | 12.01 | 21.03% | 9.81% |
| `src/test/resources` | 6 | 6.0 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/main/cobol/CALLDEMO.CBL` -> **99.593%** Exposure
- `src/main/cobol/MOCKDEMO.CBL` -> **99.593%** Exposure
- `src/main/cobol/PARADEMO.CBL` -> **99.593%** Exposure
- `src/main/cobol/SUBPROG.CBL` -> **97.0688%** Exposure
- `src/main/cobol/CICSDEMO.CBL` -> **81.7574%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `compile` -> **100.0%** Exposure
- `src/main/cobol/CARD2.CBL` -> **100.0%** Exposure
- `src/main/cobol/copy/ZUTZCPD.CPY` -> **100.0%** Exposure
- `src/main/cobol/VIZZBUZZ.CBL` -> **99.9998%** Exposure
- `src/main/cobol/ZUTZCPC.CBL` -> **99.9998%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/main/cobol/CALLDEMO.CBL` -> **4** Orphaned Functions | **0** Duplicates
- `src/main/cobol/MOCKDEMO.CBL` -> **4** Orphaned Functions | **0** Duplicates
- `src/main/cobol/PARADEMO.CBL` -> **4** Orphaned Functions | **0** Duplicates
- `src/main/cobol/copy/ZUTZCPD.CPY` -> **4** Orphaned Functions | **0** Duplicates
- `src/main/cobol/SUBPROG.CBL` -> **3** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `src/main/cobol/ZUTZCPC.CBL` -> **99.9976%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `6` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `13` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/main/cobol/ZUTZCPC.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 7.421)
- **Top Global Matches:** file_cluster_2: 7.421, file_cluster_11: 7.524, file_cluster_15: 7.598
- **Magnitude:** 1966.7 | **LOC:** 4427 | **CtrlFlow:** 10.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Credential Material (formerly Secrets Risk) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `4200-PROCESS-KEYWORDS` **(I/O & Config Routines)** (Impact: 26.6)
  * `4900-PROCESS-MOCK-FILE-SPEC` **(I/O & Config Routines)** (Impact: 23.2)
  * `5060-PARSE-HAPPENED-SPEC` **(I/O & Config Routines)** (Impact: 15.7)
  * `5020-VERIFY-CALL-MOCK` **(I/O & Config Routines)** (Impact: 12.9)
  * `9425-WRITE-TEST-LINE` **(I/O & Config Routines)** (Impact: 12.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 295 instances
* *State Mutation (weighted view):* 1303
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 342`, `structural_boundaries: 401`, `func_start: 111`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 713`, `dead_code: 5`, `unreferenced_by_name: 2`
* *Architecture:* `io: 32`, `api: 2`
* *Defense:* `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.003
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/cobol/CONVERT.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.72)
- **Top Global Matches:** file_cluster_11: 5.72, file_cluster_2: 6.317, file_cluster_15: 6.907
- **Magnitude:** 60.86 | **LOC:** 176 | **CtrlFlow:** 8.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 21.003; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (60.0%), Complexity Load (formerly Cognitive Load) (34.2%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `1000-PROCESS-INPUT` **(I/O & Config Routines)** (Impact: 4.8)
  * `2300-CONVERT-TEXT-FIELD-2` **(I/O & Config Routines)** (Impact: 3.9)
  * `2200-LOOKUP-STATE-NAME` **(I/O & Config Routines)** (Impact: 3.6)
  * `2100-CONVERT-TEXT-FIELD-1` **(I/O & Config Routines)** (Impact: 3.5)
  * `0500-INITIALIZE` **(I/O & Config Routines)** (Impact: 2.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 32
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 22`, `args: 3`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `state_mutation: 14`
* *Architecture:* `io: 4`, `import: 1`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.003
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` OUTPUT
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `compile` (SHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 7.695)
- **Top Global Matches:** file_cluster_7: 7.695, file_cluster_14: 8.672, file_cluster_12: 10.494
- **Magnitude:** 60.36 | **LOC:** 77 | **CtrlFlow:** 20.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 21.003; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.0%), Complexity Load (formerly Cognitive Load) (76.4%), Connectivity (formerly Api Exposure) (3.2%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `show_help` **(Interface Declarations)** (Impact: 1.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 30
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 52`, `args: 8`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 10`
* *Architecture:* `io: 9`, `api: 1`, `import: 1`
* *Defense:* `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.003
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` envvars
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/cobol/CONVER2.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.651)
- **Top Global Matches:** file_cluster_11: 5.651, file_cluster_2: 6.593, file_cluster_15: 7.054
- **Magnitude:** 60.12 | **LOC:** 153 | **CtrlFlow:** 9.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 21.003; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (62.2%), Complexity Load (formerly Cognitive Load) (47.4%), Test Surface (formerly Verification) (2.4%)
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
* *Structure:* `branch: 11`, `structural_boundaries: 22`, `args: 3`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `state_mutation: 14`
* *Architecture:* `io: 4`, `import: 1`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.003
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` OUTPUT
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/cobol/CARD1.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.273)
- **Top Global Matches:** file_cluster_11: 6.273, file_cluster_2: 6.415, file_cluster_15: 6.915
- **Magnitude:** 56.48 | **LOC:** 134 | **CtrlFlow:** 14.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (78.5%), Guard Balance (formerly Safety Score) (61.1%), Debt Markers (formerly Tech Debt) (17.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `2200-IDENTIFY-CARD-TYPE` **(I/O & Config Routines)** (Impact: 13.3)
  * `CARD1` **(I/O & Config Routines)** (Impact: 3.4)
  * `9100-OPEN-FILES` **(I/O & Config Routines)** (Impact: 2.9)
  * `2000-IDENTIFY-CARD-TYPES` **(Interface Declarations)** (Impact: 2.3)
  * `9400-CLOSE-FILES` **(I/O & Config Routines)** (Impact: 1.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 28
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 16`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 10`, `unreferenced_by_name: 1`
* *Architecture:* `io: 4`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.003
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/test/cobol/CONVERT-TEST.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.689)
- **Top Global Matches:** file_cluster_11: 6.689, file_cluster_2: 7.159, file_cluster_15: 7.478
- **Magnitude:** 56.32 | **LOC:** 144 | **CtrlFlow:** 12.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 21.003; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (62.8%), Complexity Load (formerly Cognitive Load) (24.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `2000-COMPARE-RECORDS` **(I/O & Config Routines)** (Impact: 11.9)
  * `1000-COMPARE-FILES` **(I/O & Config Routines)** (Impact: 5.3)
  * `0500-INITIALIZE` **(I/O & Config Routines)** (Impact: 2.7)
  * `0000-MAIN` **(Interface Declarations)** (Impact: 1.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 33
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 21`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 11`
* *Architecture:* `io: 4`, `import: 2`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.003
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` OUTPUT
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `convert-bad2.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 6.583)
- **Top Global Matches:** file_cluster_9: 6.583, file_cluster_16: 12.294, file_cluster_15: 12.365
- **Magnitude:** 53.08 | **LOC:** 180 | **CtrlFlow:** 10.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 21.003; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (62.9%), Complexity Load (formerly Cognitive Load) (52.1%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CONVERT-BAD2` **(I/O & Config Routines)** (Impact: 16.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 34
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 11`, `args: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 14`
* *Architecture:* `io: 4`, `import: 1`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.003
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` output
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/cobol/CARD3.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.026)
- **Top Global Matches:** file_cluster_11: 6.026, file_cluster_2: 6.566, file_cluster_15: 7.014
- **Magnitude:** 52.16 | **LOC:** 149 | **CtrlFlow:** 11.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 38.856; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.5%), Guard Balance (formerly Safety Score) (58.3%), Complexity Load (formerly Cognitive Load) (51.5%), Debt Markers (formerly Tech Debt) (16.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `2200-IDENTIFY-CARD-TYPE` **(I/O & Config Routines)** (Impact: 12.4)
  * `CARD3` **(I/O & Config Routines)** (Impact: 3.4)
  * `9100-OPEN-FILES` **(I/O & Config Routines)** (Impact: 2.9)
  * `2000-IDENTIFY-CARD-TYPES` **(Interface Declarations)** (Impact: 2.2)
  * `2290-POPULATE-MESSAGE` **(Interface Declarations)** (Impact: 1.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 23
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 25`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 9`, `unreferenced_by_name: 1`
* *Architecture:* `io: 4`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 38.856
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.02381
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/main/cobol/FIZZBUZZ.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.985)
- **Top Global Matches:** file_cluster_11: 5.985, file_cluster_2: 6.432, file_cluster_15: 6.838
- **Magnitude:** 51.8 | **LOC:** 104 | **CtrlFlow:** 12.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (85.6%), Guard Balance (formerly Safety Score) (64.8%), Debt Markers (formerly Tech Debt) (21.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `1000-PROCESS-NUMBER` **(I/O & Config Routines)** (Impact: 10.6)
  * `0000-MAIN` **(I/O & Config Routines)** (Impact: 3.7)
  * `0500-INITIALIZE` **(Interface Declarations)** (Impact: 1.4)
  * `2000-DIVIDE` **(I/O & Config Routines)** (Impact: 1.3)
  * `9999-END` **(I/O & Config Routines)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 32
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 16`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 12`, `unreferenced_by_name: 1`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.003
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `run-ut` (SHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Centroid distance: 6.977)
- **Top Global Matches:** file_cluster_14: 6.977, file_cluster_7: 9.72, file_cluster_5: 12.848
- **Magnitude:** 51.1 | **LOC:** 101 | **CtrlFlow:** 12.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 21.003; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.5%), Complexity Load (formerly Cognitive Load) (49.7%), Connectivity (formerly Api Exposure) (7.7%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run_unit_tests` **(I/O & Config Routines)** (Impact: 6.7)
    * *Intent:* #!/bin/bash #================================================================================ # Run ...
  * `show_help` **(I/O & Config Routines)** (Impact: 2.6)
  * `show_version` **(I/O & Config Routines)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 21
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 49`, `args: 9`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 7`
* *Architecture:* `io: 10`, `api: 5`, `import: 1`
* *Defense:* `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.003
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` envvars
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `convert-bad.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 6.523)
- **Top Global Matches:** file_cluster_9: 6.523, file_cluster_16: 12.29, file_cluster_15: 12.364
- **Magnitude:** 50.88 | **LOC:** 135 | **CtrlFlow:** 10.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 21.003; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (62.9%), Complexity Load (formerly Cognitive Load) (52.1%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CONVERT-BAD` **(I/O & Config Routines)** (Impact: 14.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 34
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 11`, `args: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 14`
* *Architecture:* `io: 4`, `import: 1`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.003
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` output
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/cobol/CARD2.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.386)
- **Top Global Matches:** file_cluster_15: 6.386, file_cluster_2: 7.681, file_cluster_16: 7.951
- **Magnitude:** 44.06 | **LOC:** 62 | **CtrlFlow:** 22.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 38.856; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (78.2%), Guard Balance (formerly Safety Score) (67.8%), Debt Markers (formerly Tech Debt) (37.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `2200-IDENTIFY-CARD-TYPE` **(I/O & Config Routines)** (Impact: 13.3)
  * `CARD2` **(Parameter Forwarders)** (Impact: 1.7)
  * `9999-END` **(I/O & Config Routines)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 26
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 8`, `args: 1`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 10`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 38.856
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.02381
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/main/cobol/VIZZBUZZ.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.672)
- **Top Global Matches:** file_cluster_11: 5.672, file_cluster_2: 6.633, file_cluster_15: 6.965
- **Magnitude:** 42.32 | **LOC:** 87 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (64.7%), Complexity Load (formerly Cognitive Load) (63.3%), Debt Markers (formerly Tech Debt) (27.2%)
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
* *Structure:* `branch: 9`, `structural_boundaries: 15`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 10`, `unreferenced_by_name: 1`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.003
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/cobol/INVDATE.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.168)
- **Top Global Matches:** file_cluster_11: 5.168, file_cluster_2: 6.185, file_cluster_15: 6.816
- **Magnitude:** 32.48 | **LOC:** 59 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 21.003; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (89.3%), Guard Balance (formerly Safety Score) (62.6%), Debt Markers (formerly Tech Debt) (37.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `2000-NEXT-INVOICE-DATE` **(I/O & Config Routines)** (Impact: 5.5)
  * `2100-HANDLE-FEBRUARY` **(I/O & Config Routines)** (Impact: 3.5)
  * `0000-MAIN` **(Interface Declarations)** (Impact: 1.3)
  * `0500-INITIALIZE` **(I/O & Config Routines)** (Impact: 1.1)
  * `1000-PROCESS-INVOICES` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 10`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 6`, `unreferenced_by_name: 1`
* *Architecture:* `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.003
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` DATETIME
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `padder.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 7.545)
- **Top Global Matches:** file_cluster_9: 7.545, file_cluster_15: 13.034, file_cluster_16: 13.155
- **Magnitude:** 22.12 | **LOC:** 41 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 21.003; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Guard Balance (formerly Safety Score) (55.0%), Complexity Load (formerly Cognitive Load) (31.9%), Connectivity (formerly Api Exposure) (3.5%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.003
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` getopt, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `win/run-ut.cmd` (BATCH | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.087)
- **Top Global Matches:** file_cluster_2: 2.087, file_cluster_17: 4.988, file_cluster_13: 6.253
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.003
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `win/compile.cmd` (BATCH | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.026)
- **Top Global Matches:** file_cluster_2: 2.026, file_cluster_17: 4.958, file_cluster_13: 6.232
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.003
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `prepare` (SHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.514)
- **Top Global Matches:** file_cluster_2: 4.514, file_cluster_17: 5.828, file_cluster_13: 6.449
- **Magnitude:** 16.18 | **LOC:** 36 | **CtrlFlow:** 5.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.2%), Guard Balance (formerly Safety Score) (55.7%), Complexity Load (formerly Cognitive Load) (16.2%), Connectivity (formerly Api Exposure) (7.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 8
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 7`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `api: 3`
* *Defense:* `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.003
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `win/setenv.cmd` (BATCH | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.052)
- **Top Global Matches:** file_cluster_2: 2.052, file_cluster_17: 4.908, file_cluster_13: 6.249
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.003
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/cobol/CALLDEMO.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.923)
- **Top Global Matches:** file_cluster_11: 5.923, file_cluster_2: 6.969, file_cluster_15: 7.505
- **Magnitude:** 12.84 | **LOC:** 43 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.6%), Mutation Surface (formerly State Flux) (91.7%), Guard Balance (formerly Safety Score) (54.3%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `1000-BASIC-CALL` **(State Mutators)** (Impact: 1.4)
  * `2000-CLASSIC-CALL` **(State Mutators)** (Impact: 1.3)
  * `3000-DYNAMIC-CALL` **(State Mutators)** (Impact: 1.3)
  * `9999-END` **(I/O & Config Routines)** (Impact: 1.1)
  * `CALLDEMO` **(Interface Declarations)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 6`, `args: 6`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 6`, `unreferenced_by_name: 4`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.003
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/cobol/SAMPLE.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.073)
- **Top Global Matches:** file_cluster_2: 5.073, file_cluster_15: 6.443, file_cluster_11: 6.628
- **Magnitude:** 10.92 | **LOC:** 27 | **CtrlFlow:** 9.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (91.7%), Guard Balance (formerly Safety Score) (54.3%), Debt Markers (formerly Tech Debt) (37.8%), Complexity Load (formerly Cognitive Load) (13.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `2000-SPEAK` **(I/O & Config Routines)** (Impact: 3.4)
  * `9999-END` **(I/O & Config Routines)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 6`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 2`, `unreferenced_by_name: 1`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.003
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/cobol/copy/ZUTZCPD.CPY` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.783)
- **Top Global Matches:** file_cluster_2: 6.783, file_cluster_11: 6.93, file_cluster_15: 7.088
- **Magnitude:** 10.38 | **LOC:** 279 | **CtrlFlow:** 20.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.2%), Complexity Load (formerly Cognitive Load) (63.1%)
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
* *Structure:* `branch: 50`, `structural_boundaries: 36`, `func_start: 13`
* *Risk/State:* `state_mutation: 53`, `unreferenced_by_name: 4`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.003
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/cobol/SUBPROG.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.14)
- **Top Global Matches:** file_cluster_15: 6.14, file_cluster_2: 6.41, file_cluster_11: 6.907
- **Magnitude:** 9.94 | **LOC:** 27 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 38.856; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (97.1%), Guard Balance (formerly Safety Score) (52.1%), Mutation Surface (formerly State Flux) (50.0%), Connectivity (formerly Api Exposure) (3.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SUBPROG` **(Parameter Forwarders)** (Impact: 2.2)
  * `1000-RETURN-VALUE-A` **(I/O & Config Routines)** (Impact: 1.1)
  * `1000-RETURN-VALUE-B` **(I/O & Config Routines)** (Impact: 1.1)
  * `9999-END` **(I/O & Config Routines)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 8`, `args: 1`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 3`, `unreferenced_by_name: 3`
* *Architecture:* `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 38.856
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.02381
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `run-examples` (SHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.806)
- **Top Global Matches:** file_cluster_2: 4.806, file_cluster_17: 6.622, file_cluster_15: 7.638
- **Magnitude:** 8.52 | **LOC:** 73 | **CtrlFlow:** 7.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Dead Code Surface (formerly Dead Code) (14.6%), Complexity Load (formerly Cognitive Load) (6.4%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`
* *Risk/State:* `dead_code: 1`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.003
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/cobol/MOCKDEMO.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.963)
- **Top Global Matches:** file_cluster_2: 4.963, file_cluster_17: 6.813, file_cluster_11: 6.843
- **Magnitude:** 8.34 | **LOC:** 64 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.6%), Guard Balance (formerly Safety Score) (51.4%), Mutation Surface (formerly State Flux) (31.0%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `0100-OPEN-INPUT` **(I/O & Config Routines)** (Impact: 1.1)
  * `0200-READ-INPUT-FILE` **(I/O & Config Routines)** (Impact: 1.1)
  * `1000-PARA-A` **(I/O & Config Routines)** (Impact: 1.1)
  * `2000-PARA-B` **(I/O & Config Routines)** (Impact: 1.1)
  * `9999-END` **(I/O & Config Routines)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 7`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 2`, `unreferenced_by_name: 4`
* *Architecture:* `io: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.003
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `src/main/cobol/ZUTZCPC.CBL` (COBOL) | Magnitude: 1966.7 | Delta: **0.103** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 3320, state_mutation: 713, structural_boundaries: 401, branch: 342

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/main/cobol/CARD2.CBL` -> **Severity: 1.613** (Embedded: 0.0238 * Error Risk: 67.762%)
- `src/main/cobol/CARD3.CBL` -> **Severity: 1.387** (Embedded: 0.0238 * Error Risk: 58.257%)
- `src/main/cobol/SUBPROG.CBL` -> **Severity: 1.241** (Embedded: 0.0238 * Error Risk: 52.1415%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/main/cobol/CARD2.CBL` -> **Severity: 3885.6** (Blast Radius: 38.856 * Doc Risk: 100.0%)
- `src/main/cobol/CARD3.CBL` -> **Severity: 3885.6** (Blast Radius: 38.856 * Doc Risk: 100.0%)
- `src/main/cobol/SUBPROG.CBL` -> **Severity: 3885.6** (Blast Radius: 38.856 * Doc Risk: 100.0%)
- `src/main/cobol/CICSDEMO.CBL` -> **Severity: 2993.0** (Blast Radius: 29.93 * Doc Risk: 100.0%)
- `src/main/cobol/CALLDEMO.CBL` -> **Severity: 2100.3** (Blast Radius: 21.003 * Doc Risk: 100.0%)

## 13. MAINFRAME SYSTEM FACTS (Named Relations & Record Layouts)
> **AI CONTEXT:** Named mainframe relations the structural signal counts flatten -- the call graph (`CALL`/CICS `LINK`·`XCTL`/JCL `EXEC PGM=`), the dataset boundary (`SELECT…ASSIGN` + `OPEN` modes, JCL `DD`→dataset), and record layouts (COBOL DATA DIVISION items, PL/I `DECLARE`d structures). BMS screen maps (every field's position, length and attributes, `screen_field_data`) are the 3270 UI surface. These are the schema of the system: use them to trace which program runs which, which dataset a job binds, and the shape of the records that flow between them. Extracted by the engine (`core/mainframe_boundary.py`) and carried in the master DB (`call_site_data`/`dataset_data`/`record_data`); resolution to files is redone per scan.

- **Coverage:** `27` files carry mainframe facts -- `22` call sites, `24` dataset bindings, `935` record items.

- **CICS operations:** `2` EXEC CICS operations naming a resource (`2` FILE); verb, direction, VALUE-resolved name and INTO/FROM record in `cics_resource_data`.

### `src/main/cobol/ZUTZCPC.CBL` (COBOL)
- **Datasets:** `SRCPRG(INPUT)`, `UTSTCFG(INPUT)`, `TESTPRG(OUTPUT)`, `UTESTS(INPUT)`
- **Record layouts (522 items):** `ERROR-MESSAGES (108)`, `FILLER (71)`, `FILLER (69)`, `FILLER (42)`, `MOCKS (39)`, `FILLER (21)`, `FILLER (19)`, `FILLER (17)`, `ORIGINAL-LINE⟵ORIGINAL-SOURCE (16)`, `INSPECT-REPLACING-FIELDS (15)`, `VALID-FILE-OPERATIONS (13)`, `FILLER (11)` … (+29 more)
- **Data moves:** 558 (ADD 13, COMPUTE 23, INITIALIZE 14, MOVE 304, STRING 193, SUBTRACT 7, WRITE 4); most-fed items `GENERATED-SOURCE-STATEMENT`, `TEST-LINE`, `RAW-VALUE`, `INITIALIZATION-STATEMENT`, `KEYWORD-OFFSET`, `KEYWORD-SEARCH-LIMIT`

### `src/main/cobol/copy/ZUTZCWS.CPY` (COBOL)
- **Record layouts (96 items):** `UT-MOCKS (45)`, `UT-FIELDS (38)`, `UT-FILES (11)`, `FILLER (1)`, `FILLER (1)`

### `src/main/cobol/CONVERT.CBL` (COBOL)
- **Calls:** `CALL C$TOUPPER`, `CALL C$JUSTIFY`
- **Datasets:** `INPUT-FILENAME(INPUT)`, `OUTPUT-FILENAME(INPUT/OUTPUT)`
- **Record layouts (25 items):** `INPUT-VALUES (6)`, `STATE-VALUES (4)`, `STATE-TABLE (4)`, `ARG-VALUES (3)`, `WS-FILE-STATUS (2)`, `EOF (2)`, `INPUT-RECORD⟵INPUT-FILE (1)`, `OUTPUT-RECORD⟵OUTPUT-FILE (1)`, `ARGS (1)`, `TO-UPPER-CASE (1)`
- **Data moves:** 19 (ACCEPT 1, MOVE 11, UNSTRING 6, WRITE 1); most-fed items `STATE-CODE-IN`, `TO-UPPER-CASE`, `DECIMAL-OUT-1`, `DECIMAL-VALUE-1`, `INPUT-FILENAME`, `OUTPUT-FILENAME`

### `src/main/cobol/copy/ZUTZCPD.CPY` (COBOL)
- **Data moves:** 51 (ADD 8, MOVE 21, STRING 22); most-fed items `UT-DISPLAY-MESSAGE`, `UT-TEST-CASE-NUMBER`, `RETURN-CODE`, `UT-ACTUAL-ACCESSES-FMT`, `UT-EXPECTED-ACCESSES-FMT`, `UT-LABEL-EXPECTED-ACCESS-PL`

### `src/main/cobol/CONVER2.CBL` (COBOL)
- **Calls:** `CALL C$TOUPPER`, `CALL C$JUSTIFY`
- **Datasets:** `INPUT-FILENAME(INPUT)`, `OUTPUT-FILENAME(OUTPUT)`
- **Record layouts (25 items):** `INPUT-VALUES (6)`, `STATE-VALUES (4)`, `STATE-TABLE (4)`, `ARG-VALUES (3)`, `WS-FILE-STATUS (2)`, `EOF (2)`, `INPUT-RECORD⟵INPUT-FILE (1)`, `OUTPUT-RECORD⟵OUTPUT-FILE (1)`, `ARGS (1)`, `TO-UPPER-CASE (1)`
- **Data moves:** 18 (ACCEPT 1, MOVE 11, UNSTRING 6); most-fed items `STATE-CODE-IN`, `TO-UPPER-CASE`, `DECIMAL-OUT-1`, `DECIMAL-VALUE-1`, `INPUT-FILENAME`, `OUTPUT-FILENAME`

### `convert-bad.cbl` (COBOL)
- **Calls:** `CALL C$TOUPPER`, `CALL C$JUSTIFY`
- **Datasets:** `INPUT-FILENAME(INPUT)`, `OUTPUT-FILENAME(INPUT/OUTPUT)`
- **Record layouts (22 items):** `INPUT-VALUES (5)`, `STATE-VALUES (4)`, `STATE-TABLE (4)`, `ARG-VALUES (3)`, `EOF (2)`, `INPUT-RECORD⟵INPUT-FILE (1)`, `OUTPUT-RECORD⟵OUTPUT-FILE (1)`, `ARGS (1)`, `TO-UPPER-CASE (1)`
- **Data moves:** 19 (ACCEPT 1, MOVE 11, UNSTRING 6, WRITE 1); most-fed items `STATE-CODE-IN`, `TO-UPPER-CASE`, `DECIMAL-OUT-1`, `DECIMAL-VALUE-1`, `INPUT-FILENAME`, `OUTPUT-FILENAME`

### `convert-bad2.cbl` (COBOL)
- **Calls:** `CALL C$TOUPPER`, `CALL C$JUSTIFY`
- **Datasets:** `INPUT-FILENAME(INPUT)`, `OUTPUT-FILENAME(INPUT/OUTPUT)`
- **Record layouts (22 items):** `INPUT-VALUES (5)`, `STATE-VALUES (4)`, `STATE-TABLE (4)`, `ARG-VALUES (3)`, `EOF (2)`, `INPUT-RECORD⟵INPUT-FILE (1)`, `OUTPUT-RECORD⟵OUTPUT-FILE (1)`, `ARGS (1)`, `TO-UPPER-CASE (1)`
- **Data moves:** 19 (ACCEPT 1, MOVE 11, UNSTRING 6, WRITE 1); most-fed items `STATE-CODE-IN`, `TO-UPPER-CASE`, `DECIMAL-OUT-1`, `DECIMAL-VALUE-1`, `INPUT-FILENAME`, `OUTPUT-FILENAME`

### `src/main/cobol/CARD1.CBL` (COBOL)
- **Datasets:** `INPUT-FILENAME(INPUT)`, `OUTPUT-FILENAME(OUTPUT)`
- **Record layouts (25 items):** `WS-RECORD-AREAS (8)`, `WS-FILE-STATUS (6)`, `ARG-VALUES (3)`, `WS-MESSAGE (3)`, `WS-ALL-FILE-STATUS (2)`, `INPUT-RECORD⟵INPUT-FILE (1)`, `OUTPUT-RECORD⟵OUTPUT-FILE (1)`, `ARGS (1)`
- **Data moves:** 13 (ACCEPT 1, MOVE 9, UNSTRING 2, WRITE 1); most-fed items `INPUT-FILENAME`, `OUT-ACCOUNT-NUMBER`, `OUT-MESSAGE`, `OUTPUT-FILENAME`, `OUTPUT-RECORD`

### `src/main/cobol/CARD3.CBL` (COBOL)
- **Datasets:** `INPUT-FILENAME(INPUT)`, `OUTPUT-FILENAME(OUTPUT)`
- **Record layouts (31 items):** `WS-MESSAGE (9)`, `WS-RECORD-AREAS (8)`, `WS-FILE-STATUS (6)`, `ARG-VALUES (3)`, `WS-ALL-FILE-STATUS (2)`, `INPUT-RECORD⟵INPUT-FILE (1)`, `OUTPUT-RECORD⟵OUTPUT-FILE (1)`, `ARGS (1)`
- **Data moves:** 6 (ACCEPT 1, MOVE 2, UNSTRING 2, WRITE 1); most-fed items `INPUT-FILENAME`, `OUT-ACCOUNT-NUMBER`, `OUT-MESSAGE`, `OUTPUT-FILENAME`, `OUTPUT-RECORD`

### `src/main/cobol/FIZZBUZZ.CBL` (COBOL)
- **Record layouts (18 items):** `FILLER (7)`, `FILLER (5)`, `ARGUMENTS (3)`, `RETURN-VALUE (2)`, `ARGS (1)`
- **Data moves:** 19 (ACCEPT 1, DIVIDE 4, MOVE 12, UNSTRING 2); most-fed items `THE-QUOTIENT`, `THE-REMAINDER`, `CURRENT-RESULT`, `ENDING-NUMBER`, `STARTING-NUMBER`

### `src/main/cobol/VIZZBUZZ.CBL` (COBOL)
- **Record layouts (18 items):** `FILLER (7)`, `FILLER (5)`, `ARGUMENTS (3)`, `RETURN-VALUE (2)`, `ARGS (1)`
- **Data moves:** 17 (ACCEPT 1, DIVIDE 4, MOVE 10, UNSTRING 2); most-fed items `THE-QUOTIENT`, `THE-REMAINDER`, `CURRENT-RESULT`, `ENDING-NUMBER`, `STARTING-NUMBER`

### `src/main/cobol/copy/DFHEIBLK.CPY` (COBOL)
- **Record layouts (32 items):** `DFHEIBLK (32)`

### `src/test/cobol/CONVERT-TEST.CBL` (COBOL)
- **Datasets:** `EXPECTED-RESULT-FILENAME(INPUT)`, `ACTUAL-RESULT-FILENAME(INPUT)`
- **Record layouts (16 items):** `ARG-VALUES (3)`, `TEST-STATUS (3)`, `EOF-EXPECTED (2)`, `EOF-ACTUAL (2)`, `EXPECTED-RESULT-RECORD⟵EXPECTED-RESULT-FILE (1)`, `ACTUAL-RESULT-RECORD⟵ACTUAL-RESULT-FILE (1)`, `ARGS (1)`, `EXPECTED-LINE-NUMBER (1)`, `ACTUAL-LINE-NUMBER (1)`, `STATUS-MESSAGE (1)`
- **Data moves:** 8 (ACCEPT 1, ADD 2, MOVE 3, UNSTRING 2); most-fed items `ACTUAL-RESULT-FILENAME`, `EXPECTED-RESULT-FILENAME`

### `src/main/cobol/CARD2.CBL` (COBOL)
- **Record layouts (11 items):** `WS-PARAMETERS (8)`, `WS-MESSAGE (3)`
- **Data moves:** 10 (MOVE 10); most-fed items `OUT-ACCOUNT-NUMBER`, `OUT-MESSAGE`

### `src/main/cobol/MOCKDEMO.CBL` (COBOL)
- **Datasets:** `INPUT-FILENAME(INPUT)`, `OUTPUT-FILENAME(declared)`
- **Record layouts (12 items):** `WS-FILE-STATUS (4)`, `WS-RECORD-AREAS (3)`, `WS-TEST-AREAS (3)`, `INPUT-RECORD⟵INPUT-FILE (1)`, `OUTPUT-RECORD⟵OUTPUT-FILE (1)`
- **Data moves:** 2 (MOVE 2)

### `src/main/cobol/PARADEMO.CBL` (COBOL)
- **Datasets:** `INPUT-FILENAME(INPUT)`, `OUTPUT-FILENAME(declared)`
- **Record layouts (12 items):** `WS-FILE-STATUS (4)`, `WS-RECORD-AREAS (3)`, `WS-TEST-AREAS (3)`, `INPUT-RECORD⟵INPUT-FILE (1)`, `OUTPUT-RECORD⟵OUTPUT-FILE (1)`
- **Data moves:** 2 (MOVE 2)

### `src/main/cobol/FILEDEMO.CBL` (COBOL)
- **Datasets:** `INPUT-FILENAME(INPUT)`, `OUTPUT-FILENAME(declared)`
- **Record layouts (9 items):** `WS-FILE-STATUS (4)`, `WS-RECORD-AREAS (3)`, `INPUT-RECORD⟵INPUT-FILE (1)`, `OUTPUT-RECORD⟵OUTPUT-FILE (1)`

### `src/main/cobol/CALLDEMO.CBL` (COBOL)
- **Calls:** `CALL NOTREALNAME`, `CALL WS-SUBPROGRAM-NAME`
- **Record layouts (3 items):** `WS-ALPHA (1)`, `WS-OMEGA (1)`, `WS-SUBPROGRAM-NAME (1)`
- **Data moves:** 6 (MOVE 6)

### `src/main/cobol/INVDATE.CBL` (COBOL)
- **Record layouts (3 items):** `WS-NEXT-INVOICE-DATE (1)`, `WS-QUOTIENT (1)`, `WS-REMAINDER (1)`
- **Data moves:** 9 (DIVIDE 4, MOVE 5); most-fed items `WS-NEXT-INVOICE-DATE`, `WS-QUOTIENT`, `WS-REMAINDER`

### `src/main/cobol/CARD2D.CBL` (COBOL)
- **Calls:** `CALL CARD2`
- **Record layouts (8 items):** `WS-PARAMETERS (8)`

*(+7 more files with mainframe facts; full detail in `record_data`/`call_site_data`/`dataset_data`.)*

- **Mainframe skeleton completeness:** 22% (mean channel ratio; channel table in the audit report, section 7). Top missing inputs: JCL and PROC libraries (19 gaps); application programs (source or load-module list) (17 gaps); copybook libraries (6 gaps).

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 343 call pairs -- scoped 89.5%, unique 1.2%, ambiguous 0.0%, external 9.3%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| cobol | 315 | 95.6% | 1.3% | 0.0% | 3.2% |
| shell | 20 | 25.0% | 0.0% | 0.0% | 75.0% |
| python | 8 | 12.5% | 0.0% | 0.0% | 87.5% |

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
