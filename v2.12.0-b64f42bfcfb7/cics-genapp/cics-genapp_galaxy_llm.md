# ARCHITECTURAL_BRIEF: cics-genapp
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/cicsdev/cics-genapp.git` |
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
- **Scope:** 132 analyzed artifact(s), 10616 LOC.
- **Load-bearing artifact:** `base/src/lgcmarea.cpy` -- 25 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `base/Installation.md` -- pulls in 7 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `base/src/lgipdb01.cbl` at magnitude 437.08 (structural weight, not risk).
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
| Total Artifacts | 139 |
| Analyzed Artifacts (Scanned) | 132 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 7 |
| Total LOC | 10616 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 95.0% |
| Dominant Lang | COBOL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3957 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3327 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 3.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.675 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 4 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| COBOL | 44 | 6794 | 33.3% |
| PLAINTEXT | 41 | 0 | 31.1% |
| JCL | 29 | 3070 | 22.0% |
| MARKDOWN | 14 | 0 | 10.6% |
| REXX | 2 | 173 | 1.5% |
| SHELL | 1 | 17 | 0.8% |
| BMS | 1 | 562 | 0.8% |

## 4.1 SOURCE ENCODINGS
All 132 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 46%, Large Core Modules 33%, Declarative / Non-Code 8%, Interface Declarations Files 7%, Parameter Forwarders Files 3%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 77 | 58.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 55 | 41.7% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 7*

**Composition by Extension & Reason:**
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 1x Excluded (Machine-Generated Source Code Signature: 82 LOC)
- `.evbind`: 1x Excluded (Unsupported Extension: '.evbind')
- `.jpg`: 1x Excluded (Explicitly Denied Extension: '.jpg')
- `.txt`: 1x Excluded (Lexical Monotony: High structural repetition detected in 24204 LOC)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 99.3 | 35.1 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 80.3 | 31.7 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 39.7 | 6.1 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 4.2 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 6.4 | 1.0 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 89.1 | 1.8 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 42.4 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 9.9 | 0.3 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 50.0 | 39.6 | 50.0 | 50.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 99.0 | 1.3 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 25 | 7 | 0 | `base/src/lgcmarea.cpy` |
| cleanup | 54 | 8 | 0 | `base/src/lgsetup.cbl` |
| guards | 96 | 28 | 2 | `base/src/lgipdb01.cbl` |
| danger | 146 | 35 | 2 | `base/src/lgtestp1.cbl` |
| concurrency | 12 | 5 | 0 | `base/cntl/asmmap.jcl` |
| connectivity | 35 | 29 | 1 | `base/src/ssmap.bms` |
| io | 409 | 40 | 6 | `base/src/lgsetup.cbl` |
| crypto | 0 | 0 | 0 | - |
| ipc | 239 | 32 | 7 | `base/src/lgipdb01.cbl` |
| time | 44 | 22 | 2 | `base/src/lgacdb01.cbl` |
| serialization | 25 | 1 | 0 | `base/src/lgwebst5.cbl` |
| regex | 4 | 1 | 0 | `base/src/lgtestc1.cbl` |
| events | 49 | 39 | 1 | `base/src/lgtestc1.cbl` |
| tests | 0 | 0 | 0 | - |
| docs | 0 | 0 | 0 | - |
| debt | 65 | 17 | 1 | `base/src/lgwebst5.cbl` |
| mutation | 2994 | 64 | 70 | `base/src/ssmap.bms` |
| dead_code | 36 | 28 | 1 | `base/src/ssmap.bms` |
| credential | 1 | 1 | 0 | `base/src/lgacdb01.cbl` |
| threat | 0 | 0 | 0 | - |
| ml_ai | 2 | 1 | 0 | `base/src/lgicvs01.cbl` |
| ui | 339 | 10 | 0 | `base/src/ssmap.bms` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `base/src/lgsetup.cbl` (Hits: 81)
- `base/src/lgwebst5.cbl` (Hits: 45)
- `base/cntl/db2cre.jcl` (Hits: 32)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **lgcmarea.cpy** (`base/src/lgcmarea.cpy`) — 25 inbound connections
2. **lgstsq.cbl** (`base/src/lgstsq.cbl`) — 20 inbound connections
3. **lgpolicy.cpy** (`base/src/lgpolicy.cpy`) — 10 inbound connections
4. **lgapol01.cbl** (`base/src/lgapol01.cbl`) — 4 inbound connections
5. **lgdpol01.cbl** (`base/src/lgdpol01.cbl`) — 4 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **Installation.md** (`base/Installation.md`) — 7 outbound dependencies
2. **README.md** (`base/README.md`) — 5 outbound dependencies
3. **README.md** (`README.md`) — 3 outbound dependencies
4. **Architecture.md** (`base/Architecture.md`) — 3 outbound dependencies
5. **lgacdb01.cbl** (`base/src/lgacdb01.cbl`) — 3 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `A-GAIN` **(I/O & Config Routines)** (@ `base/src/lgtestp4.cbl`) -> Impact: **24.0** | LOC: 199
- `UPDATE-POLICY-DB2-INFO` **(I/O & Config Routines)** (@ `base/src/lgupdb01.cbl`) -> Impact: **22.5** | LOC: 110
  * *Intent:* *================================================================* * 1) Use SELECT FOR UPDATE to obtain a lock on the row in the * * policy table, che...
- `MAINLINE` **(I/O & Config Routines)** (@ `base/src/lgapdb01.cbl`) -> Impact: **20.2** | LOC: 105
  * *Intent:* *----------------------------------------------------------------*
- `MAINLINE` **(I/O & Config Routines)** (@ `base/src/lgicvs01.cbl`) -> Impact: **19.6** | LOC: 133
  * *Intent:* *---------------------------------------------------------------*
- `A-GAIN` **(I/O & Config Routines)** (@ `base/src/lgtestp1.cbl`) -> Impact: **18.0** | LOC: 204
- `A-GAIN` **(I/O & Config Routines)** (@ `base/src/lgtestp2.cbl`) -> Impact: **18.0** | LOC: 191
- `A-GAIN` **(I/O & Config Routines)** (@ `base/src/lgtestp3.cbl`) -> Impact: **18.0** | LOC: 187
- `GET-ENDOW-DB2-INFO` **(I/O & Config Routines)** (@ `base/src/lgipdb01.cbl`) -> Impact: **16.3** | LOC: 106
  * *Intent:* *----------------------------------------------------------------* *================================================================* * Use Select on ...
- `A-GAIN` **(I/O & Config Routines)** (@ `base/src/lgtestc1.cbl`) -> Impact: **15.5** | LOC: 159
- `MAINLINE` **(I/O & Config Routines)** (@ `base/src/lgipdb01.cbl`) -> Impact: **15.1** | LOC: 81
  * *Intent:* *----------------------------------------------------------------*

*Function archetypes referenced above:*
  * **I/O & Config Routines**: dominated by I/O and configuration handling

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `base/src` | 47 | 3258.58 | 55.86% | 10.07% |
| `base/cntl` | 30 | 264.92 | 0.0% | 0.0% |
| `base/exec` | 3 | 113.04 | 25.35% | 0.0% |
| `base/wsim` | 39 | 79.64 | 0.0% | 0.0% |
| `base` | 6 | 11.94 | 0.0% | 0.0% |
| `base/bin` | 1 | 6.24 | 0.0% | 0.0% |
| `__monolith__` | 3 | 3.78 | 0.0% | 0.0% |
| `base/data` | 2 | 2.0 | 0.0% | 0.0% |
| `base/event-bindings` | 1 | 1.0 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `base/src/lgicus01.cbl` -> **39.7315%** Exposure
- `base/src/lgupol01.cbl` -> **31.204%** Exposure
- `base/src/lgicdb01.cbl` -> **25.3211%** Exposure
- `base/src/lgucdb01.cbl` -> **25.3211%** Exposure
- `base/src/lgipol01.cbl` -> **21.7467%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `base/exec/cust1.rexx` -> **100.0%** Exposure
- `base/src/lgapvs01.cbl` -> **100.0%** Exposure
- `base/src/lgipdb01.cbl` -> **100.0%** Exposure
- `base/src/lgtestp1.cbl` -> **100.0%** Exposure
- `base/src/lgtestp2.cbl` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `base/src/lgicdb01.cbl` -> **2** Orphaned Functions | **0** Duplicates
- `base/src/lgicus01.cbl` -> **2** Orphaned Functions | **0** Duplicates
- `base/src/lgucdb01.cbl` -> **2** Orphaned Functions | **0** Duplicates
- `base/src/lgupdb01.cbl` -> **2** Orphaned Functions | **0** Duplicates
- `base/src/lgupol01.cbl` -> **2** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `base/src/lgacdb01.cbl` -> **99.0093%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `71` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `base/src/lgipdb01.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 7.685)
- **Top Global Matches:** file_cluster_9: 7.685, file_cluster_2: 7.895, file_cluster_15: 8.181
- **Magnitude:** 437.08 | **LOC:** 1031 | **CtrlFlow:** 8.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 7.753; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.7%), Guard Balance (formerly Safety Score) (67.7%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `GET-ENDOW-DB2-INFO` **(I/O & Config Routines)** (Impact: 16.3)
    * *Intent:* *----------------------------------------------------------------* *================================...
  * `MAINLINE` **(I/O & Config Routines)** (Impact: 15.1)
    * *Intent:* *----------------------------------------------------------------*
  * `GET-MOTOR-DB2-INFO` **(I/O & Config Routines)** (Impact: 13.7)
    * *Intent:* *================================================================* * Use Select on join of Policy an...
  * `GET-HOUSE-DB2-INFO` **(I/O & Config Routines)** (Impact: 13.2)
    * *Intent:* *================================================================* * Use Select on join of Policy an...
  * `GET-Commercial-DB2-INFO-1` **(I/O & Config Routines)** (Impact: 11.5)
    * *Intent:* *================================================================* * Use Select on join of Policy an...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 83 instances
* *State Mutation (weighted view):* 313
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 43`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `state_mutation: 147`, `unreferenced_by_name: 1`
* *Architecture:* `io: 18`, `api: 1`, `import: 3`
* *Defense:* `safety: 16`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.753
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.021204
  * `Imports (Out-Degree: 3):` LGCMAREA, LGPOLICY, SQLCA
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `base/src/lgwebst5.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.546)
- **Top Global Matches:** file_cluster_11: 6.546, file_cluster_2: 6.723, file_cluster_15: 7.794
- **Magnitude:** 238.64 | **LOC:** 803 | **CtrlFlow:** 0.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (85.8%), Guard Balance (formerly Safety Score) (62.6%), Concurrency Surface (formerly Concurrency) (13.0%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MAINLINE` **(I/O & Config Routines)** (Impact: 14.0)
    * *Intent:* *---------------------------------------------------------------*
  * `Tran-Rate-Interval` **(I/O & Config Routines)** (Impact: 3.5)
  * `Tran-Rate-Counts` **(I/O & Config Routines)** (Impact: 2.0)
  * `A-EXIT` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 201
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 75`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 199`, `unreferenced_by_name: 1`
* *Architecture:* `io: 45`, `api: 1`, `concurrency: 1`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `base/src/lgtestp1.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 6.627)
- **Top Global Matches:** file_cluster_7: 6.627, file_cluster_12: 8.179, file_cluster_5: 9.764
- **Magnitude:** 190.58 | **LOC:** 319 | **CtrlFlow:** 5.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 5.675; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (98.8%), Guard Balance (formerly Safety Score) (80.3%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `A-GAIN` **(I/O & Config Routines)** (Impact: 18.0)
  * `NO-ADD` **(I/O & Config Routines)** (Impact: 4.5)
  * `MAINLINE` **(I/O & Config Routines)** (Impact: 3.0)
    * *Intent:* *---------------------------------------------------------------*
  * `CLEARIT` **(I/O & Config Routines)** (Impact: 1.5)
  * `ERROR-OUT` **(I/O & Config Routines)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 25 instances
* *State Mutation (weighted view):* 151
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 7`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 101`
* *Architecture:* `import: 2`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` LGCMAREA, SSMAP
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `base/src/lgapdb01.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.651)
- **Top Global Matches:** file_cluster_2: 6.651, file_cluster_11: 6.694, file_cluster_15: 7.245
- **Magnitude:** 186.96 | **LOC:** 596 | **CtrlFlow:** 6.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 8.445; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (77.1%), Guard Balance (formerly Safety Score) (63.0%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MAINLINE` **(I/O & Config Routines)** (Impact: 20.2)
    * *Intent:* *----------------------------------------------------------------*
  * `INSERT-POLICY` **(I/O & Config Routines)** (Impact: 8.1)
    * *Intent:* *----------------------------------------------------------------* *================================...
  * `INSERT-ENDOW` **(I/O & Config Routines)** (Impact: 7.0)
    * *Intent:* *================================================================* * Issue INSERT on endowment table...
  * `WRITE-ERROR-MESSAGE` **(I/O & Config Routines)** (Impact: 5.7)
    * *Intent:* *================================================================* * Procedure to write error messag...
  * `INSERT-MOTOR` **(I/O & Config Routines)** (Impact: 4.0)
    * *Intent:* *================================================================* * Issue INSERT on motor table usi...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 29 instances
* *State Mutation (weighted view):* 124
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 28`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 66`, `unreferenced_by_name: 1`
* *Architecture:* `io: 11`, `api: 1`, `import: 3`
* *Defense:* `safety: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.445
  * `Choke Point (Betweenness):` 0.000352 | `Ripple Effect (Closeness):` 0.021204
  * `Imports (Out-Degree: 4):` LGCMAREA, LGPOLICY, SQLCA
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `base/src/lgtestp4.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 11.087)
- **Top Global Matches:** file_cluster_4: 11.087, file_cluster_7: 11.964, file_cluster_12: 12.334
- **Magnitude:** 185.98 | **LOC:** 319 | **CtrlFlow:** 7.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 5.675; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (97.9%), Guard Balance (formerly Safety Score) (77.5%), Debt Markers (formerly Tech Debt) (10.7%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `A-GAIN` **(I/O & Config Routines)** (Impact: 24.0)
  * `NO-ADD` **(I/O & Config Routines)** (Impact: 4.5)
  * `MAINLINE` **(I/O & Config Routines)** (Impact: 3.3)
    * *Intent:* *---------------------------------------------------------------*
  * `CLEARIT` **(I/O & Config Routines)** (Impact: 1.5)
  * `ERROR-OUT` **(I/O & Config Routines)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 140
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 7`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 100`, `unreferenced_by_name: 1`
* *Architecture:* `import: 2`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` LGCMAREA, SSMAP
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `base/src/lgtestp2.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 6.601)
- **Top Global Matches:** file_cluster_7: 6.601, file_cluster_12: 8.319, file_cluster_5: 9.787
- **Magnitude:** 179.08 | **LOC:** 301 | **CtrlFlow:** 6.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 5.675; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (98.9%), Guard Balance (formerly Safety Score) (80.2%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `A-GAIN` **(I/O & Config Routines)** (Impact: 18.0)
  * `NO-ADD` **(I/O & Config Routines)** (Impact: 4.5)
  * `MAINLINE` **(I/O & Config Routines)** (Impact: 2.8)
    * *Intent:* *---------------------------------------------------------------*
  * `CLEARIT` **(I/O & Config Routines)** (Impact: 1.5)
  * `ERROR-OUT` **(I/O & Config Routines)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 25 instances
* *State Mutation (weighted view):* 140
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 7`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 90`
* *Architecture:* `import: 2`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` LGCMAREA, SSMAP
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `base/src/lgupdb01.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.11)
- **Top Global Matches:** file_cluster_4: 8.11, file_cluster_6: 11.13, file_cluster_11: 12.114
- **Magnitude:** 174.88 | **LOC:** 536 | **CtrlFlow:** 10.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 8.104; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (84.3%), Guard Balance (formerly Safety Score) (62.0%), Debt Markers (formerly Tech Debt) (13.2%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `UPDATE-POLICY-DB2-INFO` **(I/O & Config Routines)** (Impact: 22.5)
    * *Intent:* *================================================================* * 1) Use SELECT FOR UPDATE to obt...
  * `CLOSE-PCURSOR` **(I/O & Config Routines)** (Impact: 6.0)
  * `UPDATE-MOTOR-DB2-INFO` **(I/O & Config Routines)** (Impact: 5.8)
    * *Intent:* *================================================================* * Update row in Motor table which...
  * `WRITE-ERROR-MESSAGE` **(I/O & Config Routines)** (Impact: 5.7)
    * *Intent:* *================================================================* * Procedure to write error messag...
  * `UPDATE-ENDOW-DB2-INFO` **(I/O & Config Routines)** (Impact: 5.6)
    * *Intent:* *================================================================* * Update row in Endowment table w...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 25 instances
* *State Mutation (weighted view):* 108
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 32`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `state_mutation: 58`, `unreferenced_by_name: 2`
* *Architecture:* `io: 14`, `api: 1`, `import: 3`
* *Defense:* `safety: 12`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.104
  * `Choke Point (Betweenness):` 0.000294 | `Ripple Effect (Closeness):` 0.017448
  * `Imports (Out-Degree: 4):` LGCMAREA, LGPOLICY, SQLCA
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `base/src/lgtestp3.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 6.602)
- **Top Global Matches:** file_cluster_7: 6.602, file_cluster_12: 8.353, file_cluster_5: 9.797
- **Magnitude:** 172.22 | **LOC:** 300 | **CtrlFlow:** 6.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 5.675; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (98.9%), Guard Balance (formerly Safety Score) (79.6%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `A-GAIN` **(I/O & Config Routines)** (Impact: 18.0)
  * `NO-ADD` **(I/O & Config Routines)** (Impact: 4.5)
  * `MAINLINE` **(I/O & Config Routines)** (Impact: 3.0)
    * *Intent:* *---------------------------------------------------------------*
  * `CLEARIT` **(I/O & Config Routines)** (Impact: 1.5)
  * `ERROR-OUT` **(I/O & Config Routines)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 23 instances
* *State Mutation (weighted view):* 133
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 7`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 87`
* *Architecture:* `import: 2`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` LGCMAREA, SSMAP
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `base/src/lgtestc1.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 6.903)
- **Top Global Matches:** file_cluster_7: 6.903, file_cluster_12: 7.435, file_cluster_5: 9.688
- **Magnitude:** 163.04 | **LOC:** 348 | **CtrlFlow:** 5.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 5.675; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (99.3%), Guard Balance (formerly Safety Score) (72.4%), Concurrency Surface (formerly Concurrency) (36.2%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `A-GAIN` **(I/O & Config Routines)** (Impact: 15.5)
  * `WRITE-GENACNTL` **(I/O & Config Routines)** (Impact: 8.2)
    * *Intent:* *--------------------------------------------------------------*
  * `MAINLINE` **(I/O & Config Routines)** (Impact: 2.8)
    * *Intent:* *---------------------------------------------------------------*
  * `CLEARIT` **(I/O & Config Routines)** (Impact: 1.5)
  * `ERROR-OUT` **(I/O & Config Routines)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 21 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 115
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 10`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 73`
* *Architecture:* `io: 7`, `concurrency: 2`, `import: 2`
* *Defense:* `safety: 4`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` LGCMAREA, SSMAP
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `base/src/lgupvs01.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 7.016)
- **Top Global Matches:** file_cluster_11: 7.016, file_cluster_2: 7.617, file_cluster_15: 7.798
- **Magnitude:** 111.54 | **LOC:** 207 | **CtrlFlow:** 6.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 7.398; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (89.3%), Guard Balance (formerly Safety Score) (71.6%), Debt Markers (formerly Tech Debt) (13.2%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MAINLINE` **(I/O & Config Routines)** (Impact: 12.5)
    * *Intent:* *---------------------------------------------------------------*
  * `WRITE-ERROR-MESSAGE` **(I/O & Config Routines)** (Impact: 5.7)
    * *Intent:* *---------------------------------------------------------------*
  * `A-EXIT` **(Interface Declarations)** (Impact: 1.1)
    * *Intent:* *---------------------------------------------------------------*
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 88
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 15`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 34`, `unreferenced_by_name: 1`
* *Architecture:* `io: 2`, `api: 1`, `import: 1`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.398
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.015903
  * `Imports (Out-Degree: 2):` LGCMAREA
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `base/src/lgapvs01.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.895)
- **Top Global Matches:** file_cluster_11: 6.895, file_cluster_2: 7.493, file_cluster_15: 7.696
- **Magnitude:** 101.42 | **LOC:** 189 | **CtrlFlow:** 6.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 7.47; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (85.6%), Guard Balance (formerly Safety Score) (71.9%), Debt Markers (formerly Tech Debt) (14.0%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MAINLINE` **(I/O & Config Routines)** (Impact: 10.7)
    * *Intent:* *---------------------------------------------------------------*
  * `WRITE-ERROR-MESSAGE` **(I/O & Config Routines)** (Impact: 5.7)
    * *Intent:* *---------------------------------------------------------------*
  * `A-EXIT` **(Interface Declarations)** (Impact: 1.1)
    * *Intent:* *---------------------------------------------------------------*
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 24 instances
* *State Mutation (weighted view):* 80
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 14`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 32`, `unreferenced_by_name: 1`
* *Architecture:* `io: 2`, `api: 1`, `import: 1`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.47
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.018321
  * `Imports (Out-Degree: 2):` LGCMAREA
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `base/src/lgacdb01.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.138)
- **Top Global Matches:** file_cluster_11: 6.138, file_cluster_2: 6.393, file_cluster_15: 7.211
- **Magnitude:** 90.56 | **LOC:** 329 | **CtrlFlow:** 5.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 7.138; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Credential Material (formerly Secrets Risk) (99.0%), Complexity Load (formerly Cognitive Load) (76.0%), Guard Balance (formerly Safety Score) (61.4%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `INSERT-CUSTOMER` **(I/O & Config Routines)** (Impact: 8.7)
    * *Intent:* *================================================================*
  * `MAINLINE` **(I/O & Config Routines)** (Impact: 6.2)
    * *Intent:* *----------------------------------------------------------------*
  * `WRITE-ERROR-MESSAGE` **(I/O & Config Routines)** (Impact: 5.7)
    * *Intent:* *================================================================* *================================...
  * `Obtain-CUSTOMER-Number` **(I/O & Config Routines)** (Impact: 3.6)
    * *Intent:* *----------------------------------------------------------------*
  * `MAINLINE-EXIT` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 60
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 17`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 30`, `unreferenced_by_name: 1`
* *Architecture:* `io: 6`, `api: 1`, `import: 3`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.138
  * `Choke Point (Betweenness):` 0.000235 | `Ripple Effect (Closeness):` 0.010178
  * `Imports (Out-Degree: 5):` LGCMAREA, LGPOLICY, SQLCA
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `base/exec/cust1.rexx` (REXX | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.455)
- **Top Global Matches:** file_cluster_2: 4.455, file_cluster_17: 6.066, file_cluster_15: 6.561
- **Magnitude:** 89.34 | **LOC:** 149 | **CtrlFlow:** 14.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (68.1%), Complexity Load (formerly Cognitive Load) (64.1%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 5 instances
* *Amplified Cascading Flux:* 9 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 72
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 16`
* *Risk/State:* `high_risk_execution: 5`, `state_mutation: 54`
* *Architecture:* None
* *Defense:* `safety: 10`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `base/src/lgicvs01.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 7.951)
- **Top Global Matches:** file_cluster_9: 7.951, file_cluster_11: 8.124, file_cluster_2: 8.719
- **Magnitude:** 88.3 | **LOC:** 231 | **CtrlFlow:** 6.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (90.2%), Concurrency Surface (formerly Concurrency) (89.1%), Guard Balance (formerly Safety Score) (60.6%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MAINLINE` **(I/O & Config Routines)** (Impact: 19.6)
    * *Intent:* *---------------------------------------------------------------*
  * `A-EXIT` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 13 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 51
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 11`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 25`, `unreferenced_by_name: 1`
* *Architecture:* `io: 6`, `api: 1`, `concurrency: 2`
* *Defense:* `safety: 4`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `base/src/lgupol01.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.292)
- **Top Global Matches:** file_cluster_11: 6.292, file_cluster_2: 7.215, file_cluster_15: 7.37
- **Magnitude:** 85.74 | **LOC:** 202 | **CtrlFlow:** 10.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **1**; blast radius 8.57; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (90.8%), Guard Balance (formerly Safety Score) (70.6%), Debt Markers (formerly Tech Debt) (31.2%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MAINLINE` **(I/O & Config Routines)** (Impact: 13.1)
    * *Intent:* *----------------------------------------------------------------*
  * `WRITE-ERROR-MESSAGE` **(I/O & Config Routines)** (Impact: 5.7)
    * *Intent:* *================================================================* * Procedure to write error messag...
  * `UPDATE-POLICY-DB2-INFO` **(Interface Declarations)** (Impact: 1.4)
    * *Intent:* *----------------------------------------------------------------* *================================...
  * `END-PROGRAM` **(I/O & Config Routines)** (Impact: 1.1)
    * *Intent:* * Return to caller
  * `MAINLINE-EXIT` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 60
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 13`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 22`, `unreferenced_by_name: 2`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.57
  * `Choke Point (Betweenness):` 0.000396 | `Ripple Effect (Closeness):` 0.022901
  * `Imports (Out-Degree: 3):` LGCMAREA
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `base/src/lgicdb01.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.384)
- **Top Global Matches:** file_cluster_11: 6.384, file_cluster_2: 6.828, file_cluster_15: 7.202
- **Magnitude:** 74.42 | **LOC:** 246 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 7.138; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (85.4%), Guard Balance (formerly Safety Score) (64.2%), Debt Markers (formerly Tech Debt) (25.3%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `GET-CUSTOMER-INFO` **(I/O & Config Routines)** (Impact: 8.0)
    * *Intent:* *----------------------------------------------------------------*
  * `MAINLINE` **(I/O & Config Routines)** (Impact: 5.7)
    * *Intent:* *----------------------------------------------------------------*
  * `WRITE-ERROR-MESSAGE` **(I/O & Config Routines)** (Impact: 5.7)
    * *Intent:* *================================================================* * Procedure to write error messag...
  * `MAINLINE-END` **(I/O & Config Routines)** (Impact: 1.1)
    * *Intent:* *----------------------------------------------------------------* * END PROGRAM and return to calle...
  * `MAINLINE-EXIT` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 49
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 15`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 23`, `unreferenced_by_name: 2`
* *Architecture:* `io: 3`, `api: 1`, `import: 3`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.010178
  * `Imports (Out-Degree: 3):` LGCMAREA, LGPOLICY, SQLCA
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `base/src/lgdpdb01.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.192)
- **Top Global Matches:** file_cluster_11: 6.192, file_cluster_2: 6.719, file_cluster_15: 7.377
- **Magnitude:** 73.62 | **LOC:** 246 | **CtrlFlow:** 6.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 8.445; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (90.3%), Guard Balance (formerly Safety Score) (66.0%), Debt Markers (formerly Tech Debt) (15.0%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MAINLINE` **(I/O & Config Routines)** (Impact: 8.2)
    * *Intent:* *----------------------------------------------------------------*
  * `WRITE-ERROR-MESSAGE` **(I/O & Config Routines)** (Impact: 5.7)
    * *Intent:* *================================================================* * Procedure to write error messag...
  * `DELETE-POLICY-DB2-INFO` **(I/O & Config Routines)** (Impact: 3.0)
    * *Intent:* *----------------------------------------------------------------* *================================...
  * `MAINLINE-EXIT` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 52
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 15`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 22`, `unreferenced_by_name: 1`
* *Architecture:* `io: 5`, `api: 1`, `import: 2`
* *Defense:* `safety: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.445
  * `Choke Point (Betweenness):` 0.000294 | `Ripple Effect (Closeness):` 0.021204
  * `Imports (Out-Degree: 3):` LGCMAREA, SQLCA
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `base/src/lgacdb02.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.943)
- **Top Global Matches:** file_cluster_11: 5.943, file_cluster_2: 6.469, file_cluster_15: 7.177
- **Magnitude:** 64.62 | **LOC:** 226 | **CtrlFlow:** 6.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 6.889; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (85.7%), Guard Balance (formerly Safety Score) (64.0%), Debt Markers (formerly Tech Debt) (15.4%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MAINLINE` **(I/O & Config Routines)** (Impact: 7.1)
    * *Intent:* *----------------------------------------------------------------*
  * `WRITE-ERROR-MESSAGE` **(I/O & Config Routines)** (Impact: 5.7)
    * *Intent:* *================================================================* * Procedure to write error messag...
  * `INSERT-CUSTOMER-PASSWORD` **(I/O & Config Routines)** (Impact: 3.2)
    * *Intent:* *----------------------------------------------------------------* *================================...
  * `MAINLINE-EXIT` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 15`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 18`, `dead_code: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 2`, `api: 1`, `import: 2`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.889
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.01145
  * `Imports (Out-Degree: 2):` LGPOLICY, SQLCA
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `base/src/lgdpol01.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.296)
- **Top Global Matches:** file_cluster_11: 6.296, file_cluster_2: 7.336, file_cluster_15: 7.498
- **Magnitude:** 59.02 | **LOC:** 187 | **CtrlFlow:** 7.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **1**; blast radius 9.776; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (90.9%), Guard Balance (formerly Safety Score) (65.6%), Debt Markers (formerly Tech Debt) (18.1%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MAINLINE` **(I/O & Config Routines)** (Impact: 8.8)
    * *Intent:* *----------------------------------------------------------------*
  * `WRITE-ERROR-MESSAGE` **(I/O & Config Routines)** (Impact: 5.7)
    * *Intent:* *================================================================* * Procedure to write error messag...
  * `DELETE-POLICY-DB2-INFO` **(Interface Declarations)** (Impact: 1.4)
    * *Intent:* *----------------------------------------------------------------*
  * `MAINLINE-EXIT` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 39
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 13`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 15`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.776
  * `Choke Point (Betweenness):` 0.000533 | `Ripple Effect (Closeness):` 0.030534
  * `Imports (Out-Degree: 3):` LGCMAREA
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `base/src/lgipvs01.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 7.619)
- **Top Global Matches:** file_cluster_11: 7.619, file_cluster_9: 7.724, file_cluster_2: 8.293
- **Magnitude:** 57.82 | **LOC:** 150 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (81.4%), Guard Balance (formerly Safety Score) (65.2%), Debt Markers (formerly Tech Debt) (16.8%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MAINLINE` **(I/O & Config Routines)** (Impact: 10.5)
    * *Intent:* *---------------------------------------------------------------*
  * `A-EXIT` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 43
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 10`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 19`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 1`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `base/src/lgucdb01.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.017)
- **Top Global Matches:** file_cluster_11: 6.017, file_cluster_2: 6.459, file_cluster_15: 7.148
- **Magnitude:** 57.22 | **LOC:** 223 | **CtrlFlow:** 5.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 7.625; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (72.0%), Guard Balance (formerly Safety Score) (59.8%), Debt Markers (formerly Tech Debt) (25.3%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `WRITE-ERROR-MESSAGE` **(I/O & Config Routines)** (Impact: 5.7)
    * *Intent:* *================================================================* * Procedure to write error messag...
  * `UPDATE-CUSTOMER-INFO` **(I/O & Config Routines)** (Impact: 5.5)
    * *Intent:* *----------------------------------------------------------------* *================================...
  * `MAINLINE` **(I/O & Config Routines)** (Impact: 4.0)
    * *Intent:* *----------------------------------------------------------------*
  * `END-PROGRAM` **(I/O & Config Routines)** (Impact: 1.1)
    * *Intent:* * Return to caller
  * `MAINLINE-EXIT` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 36
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 15`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 20`, `unreferenced_by_name: 2`
* *Architecture:* `io: 4`, `api: 1`, `import: 3`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.625
  * `Choke Point (Betweenness):` 0.000176 | `Ripple Effect (Closeness):` 0.010178
  * `Imports (Out-Degree: 4):` LGCMAREA, LGPOLICY, SQLCA
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `base/cntl/db2cre.jcl` (JCL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.832)
- **Top Global Matches:** file_cluster_2: 4.832, file_cluster_17: 6.865, file_cluster_15: 7.125
- **Magnitude:** 53.42 | **LOC:** 1241 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `INSERT` **(I/O & Config Routines)** (Impact: 4.5)
    * *Intent:* /* //* //********************************************************************
  * `CREATE` **(I/O & Config Routines)** (Impact: 4.0)
    * *Intent:* //GENADB2 JOB 241901,'Db2 create',NOTIFY=&SYSUID, // CLASS=A,MSGCLASS=H //* //* (C) Copyright IBM Co...
  * `CRTABS` **(I/O & Config Routines)** (Impact: 3.4)
    * *Intent:* /* //* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> //* CREATE TABLES AND INDEXES //* <<<<<<<<<<...
  * `CRTABS` **(I/O & Config Routines)** (Impact: 3.1)
    * *Intent:* /* //* //* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> //* CREATE Commercial TABLE //* <<<<<<<<...
  * `CRTABS` **(I/O & Config Routines)** (Impact: 2.9)
    * *Intent:* /* //* //* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> //* CREATE policy TABLE //* <<<<<<<<<<<<...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 8 instances
* *High Risk Execution (weighted view):* 2
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 52`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 10`
* *Architecture:* `io: 32`
* *Defense:* `safety: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.675
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `base/src/lgucus01.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.677)
- **Top Global Matches:** file_cluster_11: 6.677, file_cluster_12: 7.124, file_cluster_2: 7.535
- **Magnitude:** 50.92 | **LOC:** 173 | **CtrlFlow:** 5.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 6.881; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (84.7%), Guard Balance (formerly Safety Score) (65.4%), Debt Markers (formerly Tech Debt) (18.9%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `WRITE-ERROR-MESSAGE` **(I/O & Config Routines)** (Impact: 5.7)
    * *Intent:* *================================================================* * Procedure to write error messag...
  * `MAINLINE` **(I/O & Config Routines)** (Impact: 4.7)
    * *Intent:* *----------------------------------------------------------------*
  * `UPDATE-CUSTOMER-INFO` **(Interface Declarations)** (Impact: 1.4)
    * *Intent:* *----------------------------------------------------------------*
  * `END-PROGRAM` **(I/O & Config Routines)** (Impact: 1.1)
    * *Intent:* * Return to caller
  * `MAINLINE-EXIT` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 34
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 13`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 14`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.881
  * `Choke Point (Betweenness):` 0.000137 | `Ripple Effect (Closeness):` 0.007634
  * `Imports (Out-Degree: 3):` LGCMAREA
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `base/src/lgicus01.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.008)
- **Top Global Matches:** file_cluster_11: 6.008, file_cluster_2: 6.626, file_cluster_15: 7.169
- **Magnitude:** 50.82 | **LOC:** 167 | **CtrlFlow:** 5.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 6.881; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (87.2%), Guard Balance (formerly Safety Score) (64.2%), Debt Markers (formerly Tech Debt) (39.7%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `WRITE-ERROR-MESSAGE` **(I/O & Config Routines)** (Impact: 5.6)
    * *Intent:* *================================================================* * Procedure to write error messag...
  * `MAINLINE` **(I/O & Config Routines)** (Impact: 4.7)
    * *Intent:* *----------------------------------------------------------------*
  * `GET-CUSTOMER-INFO` **(I/O & Config Routines)** (Impact: 1.4)
    * *Intent:* *----------------------------------------------------------------*
  * `MAINLINE-END` **(I/O & Config Routines)** (Impact: 1.1)
    * *Intent:* *----------------------------------------------------------------* * END PROGRAM and return to calle...
  * `MAINLINE-EXIT` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 34
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 13`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 16`, `unreferenced_by_name: 2`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.881
  * `Choke Point (Betweenness):` 0.000108 | `Ripple Effect (Closeness):` 0.007634
  * `Imports (Out-Degree: 4):` LGCMAREA, LGPOLICY
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `base/src/lgacus01.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.954)
- **Top Global Matches:** file_cluster_11: 5.954, file_cluster_2: 6.66, file_cluster_15: 7.224
- **Magnitude:** 50.4 | **LOC:** 180 | **CtrlFlow:** 5.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 6.881; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (87.7%), Guard Balance (formerly Safety Score) (64.4%), Debt Markers (formerly Tech Debt) (19.0%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `WRITE-ERROR-MESSAGE` **(I/O & Config Routines)** (Impact: 5.7)
    * *Intent:* *================================================================* * Procedure to write error messag...
  * `MAINLINE` **(I/O & Config Routines)** (Impact: 5.3)
    * *Intent:* *----------------------------------------------------------------*
  * `INSERT-CUSTOMER` **(I/O & Config Routines)** (Impact: 1.4)
    * *Intent:* *----------------------------------------------------------------* *--------------------------------...
  * `MAINLINE-EXIT` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 34
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 13`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 16`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.881
  * `Choke Point (Betweenness):` 0.000225 | `Ripple Effect (Closeness):` 0.007634
  * `Imports (Out-Degree: 4):` LGCMAREA, LGPOLICY
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `base/cntl/cobol.jcl` (JCL) | Magnitude: 43.92 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: core_var_decl: 52, design_upper_case: 52, structural_boundaries: 48, func_start: 34
- `base/src/lgipvs01.cbl` (COBOL) | Magnitude: 57.82 | Delta: **0.105** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 111, state_mutation: 19, structural_boundaries: 10, reflection_metaprogramming: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `base/src/lgapdb01.cbl` (COBOL) | Magnitude: 186.96 | Delta: **0.043** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 408, state_mutation: 66, reflection_metaprogramming: 31, structural_boundaries: 28

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `base/src/lgastat1.cbl` (COBOL) | Magnitude: 44.52 | Delta: **0.058** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 106, state_mutation: 14, structural_boundaries: 9, reflection_metaprogramming: 9

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `base/src/lgapol01.cbl` -> **Severity: 0.053** (Bridge: 0.0005 * Flux: 99.9994%)
- `base/src/lgdpol01.cbl` -> **Severity: 0.053** (Bridge: 0.0005 * Flux: 99.9998%)
- `base/src/lgipol01.cbl` -> **Severity: 0.053** (Bridge: 0.0005 * Flux: 99.9909%)
- `base/src/lgupol01.cbl` -> **Severity: 0.04** (Bridge: 0.0004 * Flux: 100.0%)
- `base/src/lgapdb01.cbl` -> **Severity: 0.035** (Bridge: 0.0004 * Flux: 99.9942%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `base/src/lgstsq.cbl` -> **Severity: 10.303** (Embedded: 0.159 * Error Risk: 64.7832%)
- `base/src/lgdpol01.cbl` -> **Severity: 2.002** (Embedded: 0.0305 * Error Risk: 65.5799%)
- `base/src/lgapol01.cbl` -> **Severity: 1.962** (Embedded: 0.0305 * Error Risk: 64.2712%)
- `base/src/lgipol01.cbl` -> **Severity: 1.879** (Embedded: 0.0305 * Error Risk: 61.5523%)
- `base/src/lgupol01.cbl` -> **Severity: 1.617** (Embedded: 0.0229 * Error Risk: 70.5974%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `base/src/lgstsq.cbl` -> **Severity: 2613.25** (Blast Radius: 52.265 * Doc Risk: 50.0%)
- `base/src/lgapol01.cbl` -> **Severity: 488.8** (Blast Radius: 9.776 * Doc Risk: 50.0%)
- `base/src/lgdpol01.cbl` -> **Severity: 488.8** (Blast Radius: 9.776 * Doc Risk: 50.0%)
- `base/src/lgipol01.cbl` -> **Severity: 488.8** (Blast Radius: 9.776 * Doc Risk: 50.0%)
- `base/src/lgupol01.cbl` -> **Severity: 428.5** (Blast Radius: 8.57 * Doc Risk: 50.0%)

## 13. MAINFRAME SYSTEM FACTS (Named Relations & Record Layouts)
> **AI CONTEXT:** Named mainframe relations the structural signal counts flatten -- the call graph (`CALL`/CICS `LINK`·`XCTL`/JCL `EXEC PGM=`), the dataset boundary (`SELECT…ASSIGN` + `OPEN` modes, JCL `DD`→dataset), and record layouts (COBOL DATA DIVISION items, PL/I `DECLARE`d structures). BMS screen maps (every field's position, length and attributes, `screen_field_data`) are the 3270 UI surface. These are the schema of the system: use them to trace which program runs which, which dataset a job binds, and the shape of the records that flow between them. Extracted by the engine (`core/mainframe_boundary.py`) and carried in the master DB (`call_site_data`/`dataset_data`/`record_data`); resolution to files is redone per scan.

- **Coverage:** `74` files carry mainframe facts -- `160` call sites, `101` dataset bindings, `1543` record items.

- **DB2 table access:** `37` embedded SQL statements touching `7` tables (SELECT/INSERT/UPDATE/DELETE, cursors, host variables) in `sql_statement_data`; the program x table read/write matrix is `GalaxyIR.sql_table_access()`.

- **CICS resources:** `197` CSD `DEFINE` records (FILE→DSNAME, TDQUEUE, DB2TRAN→DB2ENTRY→PLAN, MAPSET, LIBRARY, ...), full attributes in `csd_resource_data`.

- **CICS operations:** `94` EXEC CICS operations naming a resource (`2` CONTAINER, `9` FILE, `52` MAP, `31` QUEUE); verb, direction, VALUE-resolved name and INTO/FROM record in `cics_resource_data`.

- **CICS task control:** `5` commands (`2` DEQ, `2` ENQ, `1` START); child transid (or its STRING-built pattern), channel, CHILD/REQID token and timing in `cics_task_data`.

### `base/src/lgwebst5.cbl` (COBOL)
- **Calls:** `START TRANSID SSST`
- **Record layouts (218 items):** `SYMBLIST (81)`, `WS-HEADER (6)`, `DFHCOMMAREA (5)`, `WS-HHMMSS (4)`, `WS-OLDV (4)`, `COUNTVAL (1)`, `COUNTSUCCESS (1)`, `COUNTERRORS (1)`, `COUNTINQ (1)`, `COUNTADD (1)`, `COUNTUPD (1)`, `COUNTDEL (1)` … (+111 more)
- **CICS operations:** `QUEUE WS-TSQname? (delete/read/write)`, `QUEUE WS-TSQNAME? (delete/write)`
- **CICS task control:** `START SSST`
- **Data moves:** 275 (COMPUTE 100, INITIALIZE 1, MOVE 124, STRING 50); most-fed items `COUNTERRORS`, `COUNTSUCCESS`, `WS-TSQNAME`, `NRATEVAL`, `COUNTADD`, `COUNTINQ`
- **Unit of work:** `0` commit / `0` rollback points; handlers none; `1/46` RESP results tested

### `base/src/ssmap.bms` (BMS)
- **Screen maps:** `SSMAPC1 (12 named / 41 fields)`, `SSMAPP1 (15 named / 52 fields)`, `SSMAPP2 (13 named / 45 fields)`, `SSMAPP3 (12 named / 42 fields)`, `SSMAPP4 (22 named / 66 fields)`, `SSMAPP5 (10 named / 33 fields)`

### `base/src/lgipdb01.cbl` (COBOL)
- **Calls:** `LINK LGSTSQ`
- **COMMAREA passed:** `LINK LGSTSQ ← ERROR-MSG LENGTH(LENGTH OF ERROR-MSG)`, `LINK LGSTSQ ← CA-ERROR-MSG LENGTH(LENGTH OF CA-ERROR-MSG)`
- **Record layouts (75 items):** `DB2-OUT-INTEGERS (23)`, `ERROR-MSG (13)`, `WS-HEADER (8)`, `TSAREA (7)`, `DB2-IN-INTEGERS (4)`, `CA-ERROR-MSG (3)`, `WS-COMMAREA-LENGTHS (3)`, `ABS-TIME (1)`, `TIME1 (1)`, `DATE1 (1)`, `MINUS-ONE (1)`, `END-POLICY-POS (1)` … (+9 more)
- **DB2 table access:** `POLICY (read)`, `COMMERCIAL (read)`, `ENDOWMENT (read)`, `HOUSE (read)`, `MOTOR (read)`
- **Data moves:** 146 (ADD 13, INITIALIZE 11, MOVE 122); most-fed items `WS-REQUIRED-CA-LEN`, `CA-POLICY-COMMON`, `CA-COMMERCIAL`, `DB2-B-CRIMEPERIL`, `DB2-B-CRIMEPREMIUM`, `DB2-B-FIREPERIL`
- **Unit of work:** `0` commit / `0` rollback points; handlers none; `0/0` RESP results tested

### `base/src/lgsetup.cbl` (COBOL)
- **Record layouts (88 items):** `WRITE-MSG (8)`, `DFHCOMMAREA (5)`, `WS-RECV (3)`, `FILLER (3)`, `FILLER (3)`, `FILLER (3)`, `CA-AREA (3)`, `READ-MSG (2)`, `STSQ (2)`, `WS-FLAG-TSQE (1)`, `WS-FLAG-TSQH (1)`, `WS-FLAG-TSQL (1)` … (+53 more)
- **CICS operations:** `QUEUE GENAERRS (delete)`, `QUEUE GENASTRT (delete)`, `QUEUE GENASTAT (delete)`, `QUEUE GENACNTL (delete/write)`
- **Data moves:** 4 (MOVE 3, SUBTRACT 1); most-fed items `LASTCUSTNUM`, `WRITE-MSG-HIGH`, `WRITE-MSG-LOW`
- **Unit of work:** `0` commit / `0` rollback points; handlers none; `0/82` RESP results tested

### `base/src/lgapdb01.cbl` (COBOL)
- **Calls:** `LINK LGAPVS01`, `LINK LGSTSQ`
- **COMMAREA passed:** `LINK LGAPVS01 ← DFHCOMMAREA LENGTH(32500)`, `LINK LGSTSQ ← ERROR-MSG LENGTH(LENGTH OF ERROR-MSG)`, `LINK LGSTSQ ← CA-ERROR-MSG LENGTH(LENGTH OF CA-ERROR-MSG)`
- **Record layouts (63 items):** `DB2-IN-INTEGERS (26)`, `ERROR-MSG (13)`, `WS-HEADER (8)`, `CA-ERROR-MSG (3)`, `WS-COMMAREA-LENGTHS (3)`, `WS-VARY-FIELD (3)`, `DB2-OUT-INTEGERS (2)`, `ABS-TIME (1)`, `TIME1 (1)`, `DATE1 (1)`, `LGAPVS01 (1)`, `DFHCOMMAREA (1)`
- **DB2 table access:** `POLICY (insert/read)`, `ENDOWMENT (insert)`, `HOUSE (insert)`, `MOTOR (insert)`, `COMMERCIAL (insert)`
- **Data moves:** 65 (ADD 5, INITIALIZE 3, MOVE 55, SUBTRACT 2); most-fed items `WS-REQUIRED-CA-LEN`, `CA-DATA`, `WS-VARY-LEN`, `CA-POLICY-NUM`, `DB2-B-CRIMEPERIL-INT`, `DB2-B-CRIMEPREMIUM-INT`
- **Unit of work:** `0` commit / `0` rollback points; handlers none; `0/0` RESP results tested

### `base/src/lgtestc1.cbl` (COBOL)
- **Calls:** `LINK LGICUS01`, `LINK LGACUS01`, `LINK LGUCUS01`, `RETURN TRANSID SSC1`
- **COMMAREA passed:** `LINK LGICUS01 ← COMM-AREA LENGTH(32500)`, `LINK LGACUS01 ← COMM-AREA LENGTH(32500)`, `LINK LGUCUS01 ← COMM-AREA LENGTH(32500)`, `RETURN TRANSID SSC1 ← COMM-AREA`
- **Record layouts (21 items):** `WRITE-MSG (7)`, `FILLER (3)`, `READ-MSG (2)`, `STSQ (2)`, `WS-RESP (1)`, `WS-ITEM-COUNT (1)`, `WS-FLAG-TSQH (1)`, `WS-CUST-HIGH (1)`, `F24 (1)`, `MSGEND (1)`, `COMM-AREA (1)`
- **CICS operations:** `MAP SSMAPC1 (read/write)`, `QUEUE GENACNTL (read/write)`
- **CICS task control:** `ENQ GENACNTL`, `DEQ GENACNTL`
- **Data moves:** 73 (ADD 1, INITIALIZE 7, MOVE 65); most-fed items `CA-CUSTOMER-NUM`, `CA-DOB`, `CA-EMAIL-ADDRESS`, `CA-FIRST-NAME`, `CA-HOUSE-NAME`, `CA-HOUSE-NUM`
- **Unit of work:** `0` commit / `1` rollback points; handlers `MAPFAIL->ENDIT`; `2/6` RESP results tested

### `base/src/lgtestp1.cbl` (COBOL)
- **Calls:** `LINK LGIPOL01`, `LINK LGAPOL01`, `LINK LGDPOL01`, `LINK LGUPOL01`, `RETURN TRANSID SSP1`
- **COMMAREA passed:** `LINK LGIPOL01 ← COMM-AREA LENGTH(32500)`, `LINK LGAPOL01 ← COMM-AREA LENGTH(32500)`, `LINK LGDPOL01 ← COMM-AREA LENGTH(32500)`, `LINK LGUPOL01 ← COMM-AREA LENGTH(32500)`, `RETURN TRANSID SSP1 ← COMM-AREA`
- **Record layouts (2 items):** `MSGEND (1)`, `COMM-AREA (1)`
- **CICS operations:** `MAP SSMAPP1 (read/write)`
- **Data moves:** 101 (INITIALIZE 7, MOVE 94); most-fed items `CA-CUSTOMER-NUM`, `CA-POLICY-NUM`, `CA-EXPIRY-DATE`, `CA-ISSUE-DATE`, `CA-M-ACCIDENTS`, `CA-M-CC`
- **Unit of work:** `0` commit / `2` rollback points; handlers `MAPFAIL->ENDIT`; `0/0` RESP results tested

### `base/src/lgtestp4.cbl` (COBOL)
- **Calls:** `LINK LGIPOL01`, `LINK LGAPOL01`, `LINK LGDPOL01`, `RETURN TRANSID SSP4`
- **COMMAREA passed:** `LINK LGIPOL01 ← COMM-AREA LENGTH(32500)`, `LINK LGAPOL01 ← COMM-AREA LENGTH(32500)`, `LINK LGDPOL01 ← COMM-AREA LENGTH(32500)`, `RETURN TRANSID SSP4 ← COMM-AREA`
- **Record layouts (2 items):** `MSGEND (1)`, `COMM-AREA (1)`
- **CICS operations:** `MAP SSMAPP4 (read/write)`
- **Data moves:** 100 (INITIALIZE 7, MOVE 93); most-fed items `CA-CUSTOMER-NUM`, `CA-POLICY-NUM`, `CA-B-POSTCODE`, `ENP4CNOI`, `ENP4PNOI`, `CA-B-ADDRESS`
- **Unit of work:** `0` commit / `2` rollback points; handlers `MAPFAIL->ENDIT`; `0/0` RESP results tested

### `base/src/lgupdb01.cbl` (COBOL)
- **Calls:** `LINK LGUPVS01`, `LINK LGSTSQ`
- **COMMAREA passed:** `LINK LGUPVS01 ← DFHCOMMAREA LENGTH(225)`, `LINK LGSTSQ ← ERROR-MSG LENGTH(LENGTH OF ERROR-MSG)`, `LINK LGSTSQ ← CA-ERROR-MSG LENGTH(LENGTH OF CA-ERROR-MSG)`
- **Record layouts (52 items):** `ERROR-MSG (13)`, `DB2-IN-INTEGERS (13)`, `WS-HEADER (9)`, `CA-ERROR-MSG (3)`, `WS-COMMAREA-LENGTHS (3)`, `WS-VARY-FIELD (3)`, `WS-ABSTIME (1)`, `WS-TIME (1)`, `WS-DATE (1)`, `IND-BROKERID (1)`, `IND-BROKERSREF (1)`, `IND-PAYMENT (1)` … (+2 more)
- **DB2 table access:** `POLICY (read/update)`, `ENDOWMENT (update)`, `HOUSE (update)`, `MOTOR (update)`
- **Data moves:** 53 (INITIALIZE 3, MOVE 50); most-fed items `CA-DATA`, `DB2-BROKERID-INT`, `DB2-CUSTOMERNUM-INT`, `DB2-E-SUMASSURED-INT`, `DB2-E-TERM-SINT`, `DB2-H-BEDROOMS-SINT`
- **Unit of work:** `0` commit / `1` rollback points; handlers none; `0/0` RESP results tested

### `base/src/lgtestp2.cbl` (COBOL)
- **Calls:** `LINK LGIPOL01`, `LINK LGAPOL01`, `LINK LGDPOL01`, `LINK LGUPOL01`, `RETURN TRANSID SSP2`
- **COMMAREA passed:** `LINK LGIPOL01 ← COMM-AREA LENGTH(32500)`, `LINK LGAPOL01 ← COMM-AREA LENGTH(32500)`, `LINK LGDPOL01 ← COMM-AREA LENGTH(32500)`, `LINK LGUPOL01 ← COMM-AREA LENGTH(32500)`, `RETURN TRANSID SSP2 ← COMM-AREA`
- **Record layouts (2 items):** `MSGEND (1)`, `COMM-AREA (1)`
- **CICS operations:** `MAP SSMAPP2 (read/write)`
- **Data moves:** 90 (INITIALIZE 7, MOVE 83); most-fed items `CA-CUSTOMER-NUM`, `CA-POLICY-NUM`, `ENP2FNMI`, `CA-E-EQUITIES`, `CA-E-FUND-NAME`, `CA-E-LIFE-ASSURED`
- **Unit of work:** `0` commit / `2` rollback points; handlers `MAPFAIL->ENDIT`; `0/0` RESP results tested

### `base/src/lgtestp3.cbl` (COBOL)
- **Calls:** `LINK LGIPOL01`, `LINK LGAPOL01`, `LINK LGDPOL01`, `LINK LGUPOL01`, `RETURN TRANSID SSP3`
- **COMMAREA passed:** `LINK LGIPOL01 ← COMM-AREA LENGTH(32500)`, `LINK LGAPOL01 ← COMM-AREA LENGTH(32500)`, `LINK LGDPOL01 ← COMM-AREA LENGTH(32500)`, `LINK LGUPOL01 ← COMM-AREA LENGTH(32500)`, `RETURN TRANSID SSP3 ← COMM-AREA`
- **Record layouts (2 items):** `MSGEND (1)`, `COMM-AREA (1)`
- **CICS operations:** `MAP SSMAPP3 (read/write)`
- **Data moves:** 87 (INITIALIZE 7, MOVE 80); most-fed items `CA-CUSTOMER-NUM`, `CA-POLICY-NUM`, `CA-EXPIRY-DATE`, `CA-H-BEDROOMS`, `CA-H-HOUSE-NAME`, `CA-H-HOUSE-NUMBER`
- **Unit of work:** `0` commit / `2` rollback points; handlers `MAPFAIL->ENDIT`; `0/0` RESP results tested

### `base/cntl/cobol.jcl` (JCL)
- **Calls:** `EXEC PGM IGYCRCTL`, `EXEC PGM IEBGENER`, `EXEC PGM HEWL`
- **Datasets:** `STEPLIB→<COBOLHLQ>.SIGYCOMP`, `STEPLIB→<CICSHLQ>.SDFHLOAD`, `STEPLIB→<DB2HLQ>.SDSNEXIT`, `STEPLIB→<DB2HLQ>.SDSNLOAD`, `SYSLIB→<CICSHLQ>.SDFHCOB`, `SYSLIB→<CICSHLQ>.SDFHMAC`, `SYSLIB→<CICSHLQ>.SDFHSAMP`, `SYSLIB→<DB2HLQ>.SDSNSAMP`, `SYSLIB→<DB2HLQ>.SDSNMACS`, `SYSLIB→<MAPCOPX>`, `SYSLIB→<SOURCEX>`, `SYSIN→<SOURCEX>(&MEM)` … (+8)
- **Job flow:** `LGACDB01=PROC DB2PROC` -> `LGACDB02=PROC DB2PROC` -> `LGACUS01=PROC DB2PROC` -> `LGACVS01=PROC DB2PROC` -> `LGAPDB01=PROC DB2PROC` -> `LGAPOL01=PROC DB2PROC` -> `LGAPVS01=PROC DB2PROC` -> `LGASTAT1=PROC DB2PROC` -> `LGDPDB01=PROC DB2PROC` -> `LGDPOL01=PROC DB2PROC`; creates `&&COPYLINK`, `&&LOADSET`

### `base/src/lgupvs01.cbl` (COBOL)
- **Calls:** `LINK LGSTSQ`
- **COMMAREA passed:** `LINK LGSTSQ ← ERROR-MSG LENGTH(LENGTH OF ERROR-MSG)`, `LINK LGSTSQ ← CA-ERROR-MSG LENGTH(LENGTH OF CA-ERROR-MSG)`
- **Record layouts (58 items):** `WF-POLICY-INFO (27)`, `ERROR-MSG (15)`, `CA-ERROR-MSG (3)`, `WS-RESP (1)`, `WS-RESP2 (1)`, `WS-COMM-LEN (1)`, `WS-STARTCODE (1)`, `WS-SYSID (1)`, `WS-COMMAREA-LEN (1)`, `WS-COMMAREA-LENF (1)`, `WS-FILEIN (1)`, `WS-ABSTIME (1)` … (+4 more)
- **CICS operations:** `FILE KSDSPOLY (read/update)`
- **Data moves:** 34 (MOVE 34); most-fed items `CA-DATA`, `WF-POLICY-NUM`, `WS-RESP2`, `EM-CUSNUM`, `EM-DATE`, `EM-RESP2RC`
- **Unit of work:** `0` commit / `0` rollback points; handlers none; `2/2` RESP results tested

### `base/src/lgicvs01.cbl` (COBOL)
- **Record layouts (51 items):** `WRITE-MSG (8)`, `DFHCOMMAREA (5)`, `WS-RECV (3)`, `FILLER (3)`, `FILLER (3)`, `FILLER (3)`, `CA-AREA (3)`, `READ-MSG (2)`, `STSQ (2)`, `WS-FLAG-TSQE (1)`, `WS-FLAG-TSQH (1)`, `WS-FLAG-TSQL (1)` … (+16 more)
- **CICS operations:** `QUEUE GENACNTL (read/write)`, `FILE KSDSCUST (read)`
- **CICS task control:** `ENQ GENACNTL`, `DEQ GENACNTL`
- **Data moves:** 28 (COMPUTE 4, MOVE 23, SUBTRACT 1); most-fed items `WS-RANDOM-NUMBER`, `WRITE-MSG-HIGH`, `WS-COMMAREA`, `COMMA-DATA-H`, `COMMA-DATA-HIGH`, `WRITE-MSG-LOW`
- **Unit of work:** `0` commit / `0` rollback points; handlers none; `3/10` RESP results tested

### `base/src/lgapvs01.cbl` (COBOL)
- **Calls:** `LINK LGSTSQ`
- **COMMAREA passed:** `LINK LGSTSQ ← ERROR-MSG LENGTH(LENGTH OF ERROR-MSG)`, `LINK LGSTSQ ← CA-ERROR-MSG LENGTH(LENGTH OF CA-ERROR-MSG)`
- **Record layouts (56 items):** `WF-POLICY-INFO (27)`, `ERROR-MSG (15)`, `CA-ERROR-MSG (3)`, `WS-RESP (1)`, `WS-RESP2 (1)`, `WS-COMM-LEN (1)`, `WS-STARTCODE (1)`, `WS-SYSID (1)`, `WS-COMMAREA-LEN (1)`, `WS-ABSTIME (1)`, `WS-TIME (1)`, `WS-DATE (1)` … (+2 more)
- **CICS operations:** `FILE KSDSPOLY (write)`
- **Data moves:** 32 (MOVE 32); most-fed items `CA-DATA`, `EM-CUSNUM`, `EM-DATE`, `EM-POLNUM`, `EM-RESP2RC`, `EM-RESPRC`
- **Unit of work:** `0` commit / `0` rollback points; handlers none; `1/1` RESP results tested

### `base/cntl/cdef123.jcl` (JCL)
- **Calls:** `EXEC PGM DFHCSDUP`
- **Datasets:** `STEPLIB→<CICSHLQ>.SDFHLOAD`, `DFHCSD→<CSDNAME>`
- **CSD resources:** `ENQMODEL x1`, `FILE x2`, `PROGRAM x56`, `TRANSACTION x23`
- **CICS bindings:** `FILE KSDSCUST→<USRHLQ>.GENAPP.KSDSCUST`, `FILE KSDSPOLY→<USRHLQ>.GENAPP.KSDSPOLY`
- **Job flow:** `CSDDEFS=DFHCSDUP`

### `base/src/lgacdb01.cbl` (COBOL)
- **Calls:** `LINK LGACVS01`, `LINK LGACDB02`, `LINK LGSTSQ`
- **COMMAREA passed:** `LINK LGACVS01 ← DFHCOMMAREA LENGTH(225)`, `LINK LGACDB02 ← CDB2AREA LENGTH(32500)`, `LINK LGSTSQ ← ERROR-MSG LENGTH(LENGTH OF ERROR-MSG)`, `LINK LGSTSQ ← CA-ERROR-MSG LENGTH(LENGTH OF CA-ERROR-MSG)`
- **Record layouts (49 items):** `ERROR-MSG (11)`, `WS-HEADER (8)`, `CDB2AREA (8)`, `CA-ERROR-MSG (3)`, `WS-COMMAREA-LENGTHS (3)`, `DB2-OUT-INTEGERS (2)`, `WS-RESP (1)`, `LASTCUSTNUM (1)`, `GENACOUNT (1)`, `GENAPOOL (1)`, `WS-ABSTIME (1)`, `WS-TIME (1)` … (+8 more)
- **DB2 table access:** `CUSTOMER (insert)`
- **Data moves:** 28 (ADD 2, INITIALIZE 3, MOVE 23); most-fed items `CA-DATA`, `WS-REQUIRED-CA-LEN`, `CA-CUSTOMER-NUM`, `D2-CUSTOMER-NUM`, `DB2-CUSTOMERNUM-INT`, `EM-DATE`
- **Unit of work:** `0` commit / `0` rollback points; handlers none; `1/1` RESP results tested

### `base/cntl/db2cre.jcl` (JCL)
- **Calls:** `EXEC PGM IKJEFT01`, `EXEC PGM IKJEFT01 RUN PROGRAM`
- **Datasets:** `JOBLIB→<DB2HLQ>.SDSNLOAD`, `STEPLIB→<DB2HLQ>.SDSNLOAD`
- **Job flow:** `CREATE=IKJEFT01` -> `CRTABS=IKJEFT01 (cond)` -> `CRTABS=IKJEFT01 (cond)` -> `CRTABS=IKJEFT01 (cond)` -> `CRTABS=IKJEFT01 (cond)` -> `CRTABS=IKJEFT01 (cond)` -> `CRTABS=IKJEFT01 (cond)` -> `CRTABS=IKJEFT01 (cond)` -> `CRGRACC=IKJEFT01 (cond)` -> `INSERT=IKJEFT01`

### `base/src/lgcmarea.cpy` (COBOL)
- **Record layouts (85 items):** `CA-POLICY-REQUEST (64)`, `CA-CUSTOMER-REQUEST (12)`, `CA-CUSTSECR-REQUEST (5)`, `CA-REQUEST-ID (1)`, `CA-RETURN-CODE (1)`, `CA-CUSTOMER-NUM (1)`, `CA-REQUEST-SPECIFIC (1)`

### `base/src/lgpolicy.cpy` (COBOL)
- **Record layouts (85 items):** `DB2-COMMERCIAL (17)`, `WS-POLICY-LENGTHS (14)`, `DB2-CUSTOMER (10)`, `DB2-POLICY (10)`, `DB2-ENDOWMENT (10)`, `DB2-MOTOR (10)`, `DB2-HOUSE (7)`, `DB2-CLAIM (7)`

*(+54 more files with mainframe facts; full detail in `record_data`/`call_site_data`/`dataset_data`.)*

- **Mainframe skeleton completeness:** 99% (mean channel ratio; channel table in the audit report, section 7). Top missing inputs: scheduler export (CA-7 / Control-M / TWS) (29 gaps); application programs (source or load-module list) (6 gaps).

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 196 call pairs -- scoped 39.8%, unique 0.0%, ambiguous 0.0%, external 60.2%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| jcl | 113 | 0.0% | 0.0% | 0.0% | 100.0% |
| cobol | 78 | 100.0% | 0.0% | 0.0% | 0.0% |
| shell | 5 | 0.0% | 0.0% | 0.0% | 100.0% |

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
