# ARCHITECTURAL_BRIEF: cics-async-api-credit-card-application-example
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/cicsdev/cics-async-api-credit-card-application-example` |
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
- **Scope:** 21 analyzed artifact(s), 736 LOC.
- **Load-bearing artifact:** `src/CRDTCHK.cbl` -- 1 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `README.md` -- pulls in 1 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `src/ASYNCPNT.cbl` at magnitude 78.56 (structural weight, not risk).
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
| Total Artifacts | 61 |
| Analyzed Artifacts (Scanned) | 21 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 40 |
| Total LOC | 736 |
| Volatility Index | 0.048 |
| % Scanned of codebase = | 34.4% |
| Dominant Lang | COBOL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3163 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.2222 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 2 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| COBOL | 10 | 736 | 47.6% |
| XML | 8 | 0 | 38.1% |
| MARKDOWN | 3 | 0 | 14.3% |

## 4.1 SOURCE ENCODINGS
All 21 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Micro Repo (<30 files)`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Micro Repo (<30 files)` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 52%, Large Core Modules 48%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 18 | 85.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 3 | 14.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 40*

**Composition by Extension & Reason:**
- `.program`: 10x Excluded (Unsupported Extension: '.program')
- `.transaction`: 9x Excluded (Unsupported Extension: '.transaction')
- `no_extension`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.tcpipservice')
- `.urimap`: 4x Excluded (Unsupported Extension: '.urimap')
- `.wsbind`: 2x Excluded (Unsupported Extension: '.wsbind'), 2x Excluded (Binary Format Detected)
- `.prefs`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.webservice`: 2x Excluded (Unsupported Extension: '.webservice')
- `.png`: 1x Excluded (Explicitly Denied Extension: '.png')
- `.pipeline`: 1x Excluded (Unsupported Extension: '.pipeline')
- `.library`: 1x Excluded (Unsupported Extension: '.library')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 93.2 | 26.5 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 59.6 | 21.9 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 2.4 | 2.3 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 3.4 | 1.6 | 2.3 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 24.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 37.0 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 55.6 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 0 | 0 | 0 | - |
| cleanup | 0 | 0 | 0 | - |
| guards | 0 | 0 | 0 | - |
| danger | 0 | 0 | 0 | - |
| concurrency | 22 | 7 | 2 | `src/ASYNCPNT.cbl` |
| connectivity | 10 | 10 | 1 | `src/ASYNCPNT.cbl` |
| io | 0 | 0 | 0 | - |
| crypto | 0 | 0 | 0 | - |
| ipc | 51 | 10 | 5 | `src/ASYNCPNT.cbl` |
| time | 0 | 0 | 0 | - |
| serialization | 0 | 0 | 0 | - |
| regex | 0 | 0 | 0 | - |
| events | 2 | 2 | 0 | `src/ASYNCPNT.cbl` |
| tests | 0 | 0 | 0 | - |
| docs | 0 | 0 | 0 | - |
| debt | 0 | 0 | 0 | - |
| mutation | 52 | 7 | 6 | `src/ASYNCPNT.cbl` |
| dead_code | 0 | 0 | 0 | - |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 0 | 0 | 0 | - |
| ui | 2 | 2 | 0 | `src/ASYNCPNT.cbl` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `MAINTAINERS.md` (Hits: 0)
- `README.md` (Hits: 0)
- `doc/Async vs Sequential processing.md` (Hits: 0)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **CRDTCHK.cbl** (`src/CRDTCHK.cbl`) — 1 inbound connections
2. **CSSTATUS.cbl** (`src/CSSTATUS.cbl`) — 1 inbound connections
3. **GETADDR.cbl** (`src/GETADDR.cbl`) — 1 inbound connections
4. **GETNAME.cbl** (`src/GETNAME.cbl`) — 1 inbound connections
5. **GETPOL.cbl** (`src/GETPOL.cbl`) — 1 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **README.md** (`README.md`) — 1 outbound dependencies
2. **Async vs Sequential processing.md** (`doc/Async vs Sequential processing.md`) — 1 outbound dependencies
3. **MAINTAINERS.md** (`MAINTAINERS.md`) — 0 outbound dependencies
4. **cics.xml** (`etc/CICS_bundles/cics-async-creditcardapplication-pipeline/META-INF/cics.xml`) — 0 outbound dependencies
5. **basicsoap11provider.xml** (`etc/CICS_bundles/cics-async-creditcardapplication-pipeline/basicsoap11provider.xml`) — 0 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `MAINLINE` **(I/O & Config Routines)** (@ `src/ASYNCPNT.cbl`) -> Impact: **8.0** | LOC: 191
- `MAINLINE` **(I/O & Config Routines)** (@ `src/SEQPNT.cbl`) -> Impact: **8.0** | LOC: 148
- `MAINLINE` **(I/O & Config Routines)** (@ `src/CSSTATS2.cbl`) -> Impact: **5.0** | LOC: 39
- `MAINLINE` **(I/O & Config Routines)** (@ `src/CSSTATUS.cbl`) -> Impact: **5.0** | LOC: 39
- `MAINLINE` **(I/O & Config Routines)** (@ `src/GETADDR.cbl`) -> Impact: **5.0** | LOC: 42
- `MAINLINE` **(I/O & Config Routines)** (@ `src/CRDTCHK.cbl`) -> Impact: **4.7** | LOC: 33
- `MAINLINE` **(I/O & Config Routines)** (@ `src/GETNAME.cbl`) -> Impact: **4.5** | LOC: 30
- `GET-INPUT-ACCOUNT-NUMBER` **(I/O & Config Routines)** (@ `src/ASYNCPNT.cbl`) -> Impact: **4.2** | LOC: 25
  * *Intent:* * Check for a terminal or web service invocation and * populate the account number
- `GET-INPUT-ACCOUNT-NUMBER` **(I/O & Config Routines)** (@ `src/SEQPNT.cbl`) -> Impact: **4.2** | LOC: 25
  * *Intent:* * Check for a terminal or web service invocation and * populate the account number
- `PRINT-TEXT-TO-SCREEN` **(I/O & Config Routines)** (@ `src/ASYNCPNT.cbl`) -> Impact: **2.5** | LOC: 9
  * *Intent:* * For terminal based invocations, update with progress status

*Function archetypes referenced above:*
  * **I/O & Config Routines**: dominated by I/O and configuration handling

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src` | 12 | 252.16 | 39.76% | 0.0% |
| `etc/CICS_bundles/cics-async-creditcardapplication-webservices` | 2 | 21.04 | 0.0% | 0.0% |
| `etc/CICS_bundles/cics-async-creditcardapplication-pipeline/META-INF` | 1 | 10.52 | 0.0% | 0.0% |
| `etc/CICS_bundles/cics-async-creditcardapplication-pipeline` | 1 | 10.52 | 0.0% | 0.0% |
| `etc/CICS_bundles/cics-async-creditcardapplication-resources/META-INF` | 1 | 10.52 | 0.0% | 0.0% |
| `etc/CICS_bundles/cics-async-creditcardapplication-webservices/META-INF` | 1 | 10.52 | 0.0% | 0.0% |
| `__monolith__` | 2 | 2.56 | 0.0% | 0.0% |
| `doc` | 1 | 1.72 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `src/GETADDR.cbl` -> **99.9768%** Exposure
- `src/CRDTCHK.cbl` -> **99.1837%** Exposure
- `src/CSSTATUS.cbl` -> **99.1837%** Exposure
- `src/GETNAME.cbl` -> **99.1837%** Exposure
- `src/CSSTATS2.cbl` -> **98.6166%** Exposure

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
- **Unknown Dependencies:** `2` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/ASYNCPNT.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.706)
- **Top Global Matches:** file_cluster_2: 5.706, file_cluster_17: 7.139, file_cluster_15: 7.313
- **Magnitude:** 78.56 | **LOC:** 416 | **CtrlFlow:** 1.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (80.0%), Complexity Load (formerly Cognitive Load) (79.3%), Guard Balance (formerly Safety Score) (54.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MAINLINE` **(I/O & Config Routines)** (Impact: 8.0)
  * `GET-INPUT-ACCOUNT-NUMBER` **(I/O & Config Routines)** (Impact: 4.2)
    * *Intent:* * Check for a terminal or web service invocation and * populate the account number
  * `PRINT-TEXT-TO-SCREEN` **(I/O & Config Routines)** (Impact: 2.5)
    * *Intent:* * For terminal based invocations, update with progress status
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 35
* *State Mutation (weighted view):* 23
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 21`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 17`
* *Architecture:* `api: 1`, `concurrency: 10`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 43.774
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/SEQPNT.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.596)
- **Top Global Matches:** file_cluster_2: 5.596, file_cluster_17: 6.9, file_cluster_15: 7.07
- **Magnitude:** 42.66 | **LOC:** 345 | **CtrlFlow:** 1.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (90.4%), Guard Balance (formerly Safety Score) (55.3%), Complexity Load (formerly Cognitive Load) (42.7%), Connectivity (formerly Api Exposure) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MAINLINE` **(I/O & Config Routines)** (Impact: 8.0)
  * `GET-INPUT-ACCOUNT-NUMBER` **(I/O & Config Routines)** (Impact: 4.2)
    * *Intent:* * Check for a terminal or web service invocation and * populate the account number
  * `PRINT-TEXT-TO-SCREEN` **(I/O & Config Routines)** (Impact: 2.5)
    * *Intent:* * For terminal based invocations, update with progress status
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 23
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 21`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 17`
* *Architecture:* `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 43.774
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/GETADDR.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.765)
- **Top Global Matches:** file_cluster_2: 5.765, file_cluster_17: 7.06, file_cluster_15: 7.328
- **Magnitude:** 27.04 | **LOC:** 106 | **CtrlFlow:** 3.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 51.216; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (98.6%), Complexity Load (formerly Cognitive Load) (93.2%), Guard Balance (formerly Safety Score) (59.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MAINLINE` **(I/O & Config Routines)** (Impact: 5.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 4 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 14
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 8`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* `api: 1`, `concurrency: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 51.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.05
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/CRDTCHK.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.804)
- **Top Global Matches:** file_cluster_2: 5.804, file_cluster_17: 7.059, file_cluster_15: 7.313
- **Magnitude:** 21.56 | **LOC:** 94 | **CtrlFlow:** 4.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 51.216; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.2%), Concurrency Surface (formerly Concurrency) (98.8%), Complexity Load (formerly Cognitive Load) (83.8%), Guard Balance (formerly Safety Score) (56.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MAINLINE` **(I/O & Config Routines)** (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 8`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 1`, `concurrency: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 51.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.05
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/CSSTATS2.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.789)
- **Top Global Matches:** file_cluster_2: 5.789, file_cluster_17: 7.082, file_cluster_15: 7.361
- **Magnitude:** 18.08 | **LOC:** 109 | **CtrlFlow:** 3.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.6%), Complexity Load (formerly Cognitive Load) (68.5%), Guard Balance (formerly Safety Score) (56.1%), Concurrency Surface (formerly Concurrency) (50.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MAINLINE` **(I/O & Config Routines)** (Impact: 5.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 8`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 1`, `concurrency: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 43.774
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/CSSTATUS.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.939)
- **Top Global Matches:** file_cluster_2: 5.939, file_cluster_17: 6.966, file_cluster_15: 7.251
- **Magnitude:** 15.94 | **LOC:** 104 | **CtrlFlow:** 4.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 51.216; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.2%), Complexity Load (formerly Cognitive Load) (64.6%), Guard Balance (formerly Safety Score) (56.4%), Connectivity (formerly Api Exposure) (3.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MAINLINE` **(I/O & Config Routines)** (Impact: 5.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 8`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 51.216
  * `Choke Point (Betweenness):` 0.005263 | `Ripple Effect (Closeness):` 0.05
  * `Imports (Out-Degree: 2):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/GETNAME.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.51)
- **Top Global Matches:** file_cluster_2: 5.51, file_cluster_17: 6.834, file_cluster_15: 7.088
- **Magnitude:** 15.32 | **LOC:** 95 | **CtrlFlow:** 4.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 51.216; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.2%), Guard Balance (formerly Safety Score) (56.4%), Complexity Load (formerly Cognitive Load) (45.0%), Connectivity (formerly Api Exposure) (3.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MAINLINE` **(I/O & Config Routines)** (Impact: 4.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 8`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 51.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.05
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `etc/CICS_bundles/cics-async-creditcardapplication-pipeline/META-INF/cics.xml` (XML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Centroid distance: 0.0)
- **Magnitude:** 10.52 | **LOC:** 9 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 43.774
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `etc/CICS_bundles/cics-async-creditcardapplication-pipeline/basicsoap11provider.xml` (XML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Centroid distance: 0.0)
- **Magnitude:** 10.52 | **LOC:** 33 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 43.774
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `etc/CICS_bundles/cics-async-creditcardapplication-resources/META-INF/cics.xml` (XML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Centroid distance: 0.0)
- **Magnitude:** 10.52 | **LOC:** 27 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 43.774
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `etc/CICS_bundles/cics-async-creditcardapplication-webservices/ASYNCPNT.wsdl` (XML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Centroid distance: 0.0)
- **Magnitude:** 10.52 | **LOC:** 168 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 43.774
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `etc/CICS_bundles/cics-async-creditcardapplication-webservices/META-INF/cics.xml` (XML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Centroid distance: 0.0)
- **Magnitude:** 10.52 | **LOC:** 13 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 43.774
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `etc/CICS_bundles/cics-async-creditcardapplication-webservices/SEQPNT.wsdl` (XML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Centroid distance: 0.0)
- **Magnitude:** 10.52 | **LOC:** 168 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 43.774
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ASYNCPNT.wsdl` (XML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Centroid distance: 0.0)
- **Magnitude:** 10.52 | **LOC:** 168 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 43.774
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/SEQPNT.wsdl` (XML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Centroid distance: 0.0)
- **Magnitude:** 10.52 | **LOC:** 168 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 43.774
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/UPDCSDB.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.774)
- **Top Global Matches:** file_cluster_2: 5.774, file_cluster_17: 6.927, file_cluster_11: 7.354
- **Magnitude:** 4.12 | **LOC:** 70 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 51.216; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (28.2%), Connectivity (formerly Api Exposure) (3.3%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MAINLINE` **(I/O & Config Routines)** (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 8`, `func_start: 1`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`, `concurrency: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 51.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.05
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/GETPOL.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.525)
- **Top Global Matches:** file_cluster_2: 6.525, file_cluster_17: 7.434, file_cluster_11: 7.778
- **Magnitude:** 3.92 | **LOC:** 60 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 65.541; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (28.2%), Connectivity (formerly Api Exposure) (3.4%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MAINLINE` **(I/O & Config Routines)** (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 8`, `func_start: 1`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`, `concurrency: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 65.541
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.066667
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/GETSPND.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.525)
- **Top Global Matches:** file_cluster_2: 6.525, file_cluster_17: 7.434, file_cluster_11: 7.778
- **Magnitude:** 3.92 | **LOC:** 56 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 65.541; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (28.2%), Connectivity (formerly Api Exposure) (3.4%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MAINLINE` **(I/O & Config Routines)** (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 8`, `func_start: 1`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`, `concurrency: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 65.541
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.066667
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `doc/Async vs Sequential processing.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 1.72 | **LOC:** 86 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 43.774; role: Isolated/Orphan
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 43.774
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` credit
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 1.56 | **LOC:** 78 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 43.774; role: Isolated/Orphan
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 43.774
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` LICENSE
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `MAINTAINERS.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 1.0 | **LOC:** 6 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 43.774
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

- `src/CSSTATUS.cbl` -> **Severity: 0.522** (Bridge: 0.0053 * Flux: 99.1837%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/GETADDR.cbl` -> **Severity: 2.98** (Embedded: 0.05 * Error Risk: 59.6015%)
- `src/CRDTCHK.cbl` -> **Severity: 2.82** (Embedded: 0.05 * Error Risk: 56.3934%)
- `src/CSSTATUS.cbl` -> **Severity: 2.82** (Embedded: 0.05 * Error Risk: 56.3934%)
- `src/GETNAME.cbl` -> **Severity: 2.82** (Embedded: 0.05 * Error Risk: 56.3934%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/GETPOL.cbl` -> **Severity: 6554.1** (Blast Radius: 65.541 * Doc Risk: 100.0%)
- `src/GETSPND.cbl` -> **Severity: 6554.1** (Blast Radius: 65.541 * Doc Risk: 100.0%)
- `src/CRDTCHK.cbl` -> **Severity: 5121.6** (Blast Radius: 51.216 * Doc Risk: 100.0%)
- `src/CSSTATUS.cbl` -> **Severity: 5121.6** (Blast Radius: 51.216 * Doc Risk: 100.0%)
- `src/GETADDR.cbl` -> **Severity: 5121.6** (Blast Radius: 51.216 * Doc Risk: 100.0%)

## 13. MAINFRAME SYSTEM FACTS (Named Relations & Record Layouts)
> **AI CONTEXT:** Named mainframe relations the structural signal counts flatten -- the call graph (`CALL`/CICS `LINK`·`XCTL`/JCL `EXEC PGM=`), the dataset boundary (`SELECT…ASSIGN` + `OPEN` modes, JCL `DD`→dataset), and record layouts (COBOL DATA DIVISION items, PL/I `DECLARE`d structures). BMS screen maps (every field's position, length and attributes, `screen_field_data`) are the 3270 UI surface. These are the schema of the system: use them to trace which program runs which, which dataset a job binds, and the shape of the records that flow between them. Extracted by the engine (`core/mainframe_boundary.py`) and carried in the master DB (`call_site_data`/`dataset_data`/`record_data`); resolution to files is redone per scan.

- **Coverage:** `10` files carry mainframe facts -- `14` call sites, `0` dataset bindings, `224` record items.

- **CICS operations:** `37` EXEC CICS operations naming a resource (`10` CHANNEL, `27` CONTAINER); verb, direction, VALUE-resolved name and INTO/FROM record in `cics_resource_data`.

- **CICS task control:** `17` commands (`5` DELAY, `5` FETCH CHILD, `7` RUN); child transid (or its STRING-built pattern), channel, CHILD/REQID token and timing in `cics_task_data`.

### `src/ASYNCPNT.cbl` (COBOL)
- **Calls:** `RUN TRANSID CREDIT-CHECK-TRAN`, `RUN TRANSID GET-ADDR-TRAN`, `RUN TRANSID CSSTATUS-TRAN`, `RUN TRANSID GET-NAME-TRAN`, `RUN TRANSID DB-CACHE-TRAN`
- **Record layouts (87 items):** `PRINT-LINE (26)`, `CONTAINER-NAMES (8)`, `TRANSIDS (8)`, `CHILD-TOKENS (8)`, `RETURN-CHANNELS (8)`, `RETURN-DATA (7)`, `PROG-NAMES (6)`, `READ-INPUT (4)`, `ACCOUNT-NUMBER-IN (2)`, `APPLICATION-SUCCESS (1)`, `APPLICATION-FAILED (1)`, `READ-INPUT-LENGTH (1)` … (+7 more)
- **CICS operations:** `CONTAINER INPUTCONTAINER (write)`, `CHANNEL MYCHANNEL (pass)`, `CONTAINER CREDITCHECKCONT (read)`, `CONTAINER GETNAMECONTAINER (read)`, `CONTAINER GETVIPSTATUS (read)`, `CONTAINER GETADDRCONTAINER (read)`, `CONTAINER GETPOSTCODE (read)`, `CONTAINER ASYNCPNT (read/write)`
- **CICS task control:** `RUN ICCK`, `RUN GETA`, `RUN STUS`, `RUN GETN`, `FETCH CHILD`, `RUN UPDB`
- **Compiler options:** `TRUNC(STD)`
- **Data moves:** 15 (MOVE 15); most-fed items `ACCOUNT-NUM`, `APPLICATION-RESULT`, `CUST-NO-IN`, `RESULT-TEXT`
- **Unit of work:** `0` commit / `0` rollback points; handlers none; `0/9` RESP results tested

### `src/SEQPNT.cbl` (COBOL)
- **Calls:** `LINK CREDIT-CHECK`, `LINK GET-NAME`, `LINK GET-ADDR`, `LINK CSSTATUS`, `LINK DB-CACHE`
- **Record layouts (61 items):** `PRINT-LINE (26)`, `CONTAINER-NAMES (8)`, `RETURN-DATA (7)`, `PROG-NAMES (6)`, `READ-INPUT (4)`, `ACCOUNT-NUMBER-IN (2)`, `APPLICATION-SUCCESS (1)`, `APPLICATION-FAILED (1)`, `READ-INPUT-LENGTH (1)`, `IS-TERMINAL-BASED (1)`, `START-CODE (1)`, `MYCHANNEL (1)` … (+2 more)
- **CICS operations:** `CONTAINER INPUTCONTAINER (write)`, `CHANNEL MYCHANNEL (pass)`, `CONTAINER CREDITCHECKCONT (read)`, `CONTAINER GETNAMECONTAINER (read)`, `CONTAINER GETADDRCONTAINER (read)`, `CONTAINER GETPOSTCODE (read)`, `CONTAINER GETVIPSTATUS (read)`, `CONTAINER SEQPNT (read/write)`
- **Compiler options:** `TRUNC(STD)`
- **Data moves:** 15 (MOVE 15); most-fed items `ACCOUNT-NUM`, `APPLICATION-RESULT`, `CUST-NO-IN`, `RESULT-TEXT`
- **Unit of work:** `0` commit / `0` rollback points; handlers none; `0/14` RESP results tested

### `src/CSSTATS2.cbl` (COBOL)
- **Calls:** `RUN TRANSID GET-POLICY-TRAN`, `RUN TRANSID GET-SPEND-TRAN`
- **Record layouts (18 items):** `CONTAINER-NAMES (3)`, `PROG-NAMES (3)`, `TRANSIDS (3)`, `CHILD-TOKENS (3)`, `ACCOUNT-NUMBER-IN (2)`, `RETURN-DATA (2)`, `COMMAND-RESP (1)`, `COMMAND-RESP2 (1)`
- **CICS operations:** `CONTAINER INPUTCONTAINER (read)`, `CONTAINER GETVIPSTATUS (write)`
- **CICS task control:** `RUN GETP`, `RUN SPND`
- **Compiler options:** `TRUNC(STD)`
- **Data moves:** 2 (MOVE 2)
- **Unit of work:** `0` commit / `0` rollback points; handlers none; `0/2` RESP results tested

### `src/GETADDR.cbl` (COBOL)
- **Record layouts (13 items):** `CONTAINER-NAMES (4)`, `RETURN-DATA (3)`, `ACCOUNT-NUMBER-IN (2)`, `PROG-NAMES (2)`, `COMMAND-RESP (1)`, `COMMAND-RESP2 (1)`
- **CICS operations:** `CONTAINER INPUTCONTAINER (read)`, `CONTAINER GETADDRCONTAINER (write)`, `CONTAINER GETPOSTCODE (write)`
- **CICS task control:** `DELAY`
- **Compiler options:** `TRUNC(STD)`
- **Data moves:** 4 (MOVE 4)
- **Unit of work:** `0` commit / `0` rollback points; handlers none; `0/3` RESP results tested

### `src/CSSTATUS.cbl` (COBOL)
- **Calls:** `LINK GETPOL`, `LINK GETSPND`
- **Record layouts (13 items):** `CONTAINER-NAMES (3)`, `PROG-NAMES (3)`, `ACCOUNT-NUMBER-IN (2)`, `RETURN-DATA (2)`, `OK (1)`, `COMMAND-RESP (1)`, `COMMAND-RESP2 (1)`
- **CICS operations:** `CONTAINER INPUTCONTAINER (read)`, `CONTAINER GETVIPSTATUS (write)`
- **Compiler options:** `TRUNC(STD)`
- **Data moves:** 2 (MOVE 2)
- **Unit of work:** `0` commit / `0` rollback points; handlers none; `0/2` RESP results tested

### `src/CRDTCHK.cbl` (COBOL)
- **Record layouts (11 items):** `CONTAINER-NAMES (3)`, `ACCOUNT-NUMBER-IN (2)`, `RETURN-DATA (2)`, `PROG-NAMES (2)`, `COMMAND-RESP (1)`, `COMMAND-RESP2 (1)`
- **CICS operations:** `CONTAINER INPUTCONTAINER (read)`, `CONTAINER CREDITCHECKCONT (write)`
- **CICS task control:** `DELAY`
- **Compiler options:** `TRUNC(STD)`
- **Data moves:** 2 (MOVE 2)
- **Unit of work:** `0` commit / `0` rollback points; handlers none; `0/2` RESP results tested

### `src/GETNAME.cbl` (COBOL)
- **Record layouts (11 items):** `CONTAINER-NAMES (3)`, `ACCOUNT-NUMBER-IN (2)`, `RETURN-DATA (2)`, `PROG-NAMES (2)`, `COMMAND-RESP (1)`, `COMMAND-RESP2 (1)`
- **CICS operations:** `CONTAINER INPUTCONTAINER (read)`, `CONTAINER GETNAMECONTAINER (write)`
- **Compiler options:** `TRUNC(STD)`
- **Data moves:** 2 (MOVE 2)
- **Unit of work:** `0` commit / `0` rollback points; handlers none; `0/2` RESP results tested

### `src/UPDCSDB.cbl` (COBOL)
- **Record layouts (10 items):** `CONTAINER-NAMES (4)`, `ACCOUNT-NUMBER-IN (2)`, `PROG-NAMES (2)`, `COMMAND-RESP (1)`, `COMMAND-RESP2 (1)`
- **CICS task control:** `DELAY`
- **Compiler options:** `TRUNC(STD)`

### `src/GETPOL.cbl` (COBOL)
- **CICS task control:** `DELAY`
- **Compiler options:** `TRUNC(STD)`

### `src/GETSPND.cbl` (COBOL)
- **CICS task control:** `DELAY`
- **Compiler options:** `TRUNC(STD)`

- **Mainframe skeleton completeness:** 90% (mean channel ratio; channel table in the audit report, section 7). Top missing inputs: CSD extract (DFHCSDUP LIST / CICSPlex SM), or the web / API layer that LINKs it (3 gaps).

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 6 call pairs -- scoped 100.0%, unique 0.0%, ambiguous 0.0%, external 0.0%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| cobol | 6 | 100.0% | 0.0% | 0.0% | 0.0% |

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
