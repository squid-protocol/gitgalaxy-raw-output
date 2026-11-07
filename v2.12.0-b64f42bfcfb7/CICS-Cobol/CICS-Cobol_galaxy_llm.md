# ARCHITECTURAL_BRIEF: CICS-Cobol
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/mainframe-projects/CICS-Cobol.git` |
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
- **Scope:** 52 analyzed artifact(s), 1543 LOC.
- **Load-bearing artifact:** `QG4CX001.cpy` -- 1 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `CBL0401v01ClausuleCopy.cbl` -- pulls in 1 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `CBL0805v01TableUseIndiceWithSet.cbl` at magnitude 24.48 (structural weight, not risk).
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
| Total Artifacts | 54 |
| Analyzed Artifacts (Scanned) | 52 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 2 |
| Total LOC | 1543 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 96.3% |
| Dominant Lang | COBOL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 0 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| COBOL | 52 | 1543 | 100.0% |

## 4.1 SOURCE ENCODINGS
> 35 file(s) had no BOM, were not UTF-8 and matched no declared code page: decoded by a legacy guess (`--source-encoding` declares the real one).
| Encoding | Decode | Files |
|---|---|---|
| cp1252 | cp1252-fallback | 35 |
| utf-8 | utf-8 | 17 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Interface Declarations Files 81%, Large Core Modules 15%, Data / Markup / Trivial 4%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 52 | 100.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 2*

**Composition by Extension & Reason:**
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 41.1 | 5.7 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 63.9 | 56.9 | 57.8 | 57.8 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 97.1 | 2.6 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 2.4 | 2.4 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 99.9 | 47.8 | 50.0 | 50.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 98.1 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 4 | 1 | 0 | `CBL0301v01DataLayoutRedefine.cbl` |
| cleanup | 0 | 0 | 0 | - |
| guards | 0 | 0 | 0 | - |
| danger | 104 | 51 | 2 | `CBL0605v01GotoStatement.cbl` |
| concurrency | 0 | 0 | 0 | - |
| connectivity | 0 | 0 | 0 | - |
| io | 0 | 0 | 0 | - |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 1 | 1 | 0 | `CBL0201v01VerbosBasicos.cbl` |
| serialization | 5 | 3 | 0 | `CBL0703v01StatementString.cbl` |
| regex | 10 | 4 | 0 | `CBL0701v01StatementInspect.cbl` |
| events | 0 | 0 | 0 | - |
| tests | 0 | 0 | 0 | - |
| docs | 0 | 0 | 0 | - |
| debt | 429 | 51 | 16 | `CBL0301v01DataLayoutRedefine.cbl` |
| mutation | 128 | 46 | 4 | `CBL0206v01MultiplyVerb.cbl` |
| dead_code | 4 | 2 | 0 | `CBL0601v01InOutLineLoop.cbl` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `CBL0101v01EstructuraInicial.COB` (Hits: 0)
- `CBL0102v01DivisionAmbiente.cbl` (Hits: 0)
- `CBL0103v01DivisionData.cbl` (Hits: 0)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **QG4CX001.cpy** (`QG4CX001.cpy`) — 1 inbound connections
2. **CBL0101v01EstructuraInicial.COB** (`CBL0101v01EstructuraInicial.COB`) — 0 inbound connections
3. **CBL0102v01DivisionAmbiente.cbl** (`CBL0102v01DivisionAmbiente.cbl`) — 0 inbound connections
4. **CBL0103v01DivisionData.cbl** (`CBL0103v01DivisionData.cbl`) — 0 inbound connections
5. **CBL0104v01ProcedureDivision.cbl** (`CBL0104v01ProcedureDivision.cbl`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **CBL0401v01ClausuleCopy.cbl** (`CBL0401v01ClausuleCopy.cbl`) — 1 outbound dependencies
2. **CBL0101v01EstructuraInicial.COB** (`CBL0101v01EstructuraInicial.COB`) — 0 outbound dependencies
3. **CBL0102v01DivisionAmbiente.cbl** (`CBL0102v01DivisionAmbiente.cbl`) — 0 outbound dependencies
4. **CBL0103v01DivisionData.cbl** (`CBL0103v01DivisionData.cbl`) — 0 outbound dependencies
5. **CBL0104v01ProcedureDivision.cbl** (`CBL0104v01ProcedureDivision.cbl`) — 0 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `MAIN-PROCEDURE` **(I/O & Config Routines)** (@ `CBL0501v01DeclaracioCondicionIF.cbl`) -> Impact: **9.3** | LOC: 26
- `0000-MAIN` **(I/O & Config Routines)** (@ `CBL0604v01PerformVariying.cbl`) -> Impact: **8.0** | LOC: 19
- `MAIN-PROCEDURE` **(I/O & Config Routines)** (@ `CBL0503v01CondicionSigno.cbl`) -> Impact: **7.3** | LOC: 26
- `0000-MAIN` **(I/O & Config Routines)** (@ `CBL0805v01TableUseIndiceWithSet.cbl`) -> Impact: **6.3** | LOC: 27
- `MAIN-PROCEDURE` **(I/O & Config Routines)** (@ `CBL0508v01CondicionVerb.cbl`) -> Impact: **6.0** | LOC: 21
- `0000-MAIN` **(I/O & Config Routines)** (@ `CBL0804v01TableUseIndice.cbl`) -> Impact: **6.0** | LOC: 20
- `MAIN-PROCEDURE` **(I/O & Config Routines)** (@ `CBL0504v01CondicionClass.cbl`) -> Impact: **5.0** | LOC: 19
- `MAIN-PROCEDURE` **(I/O & Config Routines)** (@ `CBL0502v01CondicionRelacion.cbl`) -> Impact: **4.8** | LOC: 15
- `MAIN-PROCEDURE` **(Interface Declarations)** (@ `CBL0507v01CondicionCombined.cbl`) -> Impact: **3.9** | LOC: 17
- `MAIN-PROCEDURE` **(I/O & Config Routines)** (@ `CBL0505v01CondicionName.cbl`) -> Impact: **3.8** | LOC: 16

*Function archetypes referenced above:*
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Interface Declarations**: signature/entry function exposing API with minimal logic

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `__monolith__` | 52 | 391.3 | 5.75% | 2.59% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `CBL0601v01InOutLineLoop.cbl` -> **97.0688%** Exposure
- `CBL0605v01GotoStatement.cbl` -> **37.7541%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `CBL0503v01CondicionSigno.cbl` -> **99.9254%** Exposure
- `CBL0805v01TableUseIndiceWithSet.cbl` -> **99.9254%** Exposure
- `CBL0502v01CondicionRelacion.cbl` -> **99.1837%** Exposure
- `CBL0807v01TableSearchAll.cbl` -> **98.2014%** Exposure
- `CBL0206v01MultiplyVerb.cbl` -> **96.0834%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `CBL0601v01InOutLineLoop.cbl` -> **3** Orphaned Functions | **0** Duplicates
- `CBL0605v01GotoStatement.cbl` -> **1** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `1` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `CBL0805v01TableUseIndiceWithSet.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.594)
- **Top Global Matches:** file_cluster_11: 6.594, file_cluster_15: 7.447, file_cluster_2: 7.739
- **Magnitude:** 24.48 | **LOC:** 69 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (63.9%), Complexity Load (formerly Cognitive Load) (41.1%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `0000-MAIN` **(I/O & Config Routines)** (Impact: 6.3)
  * `200-TWO-DIMENSION` **(Compute Cores)** (Impact: 3.1)
  * `100-ONE-DIMENSION` **(Interface Declarations)** (Impact: 1.1)
  * `300-MOSTRAR` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 22`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 6`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.921
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0503v01CondicionSigno.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 7.249)
- **Top Global Matches:** file_cluster_9: 7.249, file_cluster_16: 12.709, file_cluster_15: 12.77
- **Magnitude:** 19.88 | **LOC:** 44 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (63.9%), Complexity Load (formerly Cognitive Load) (33.6%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MAIN-PROCEDURE` **(I/O & Config Routines)** (Impact: 7.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 15`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 4`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.921
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0804v01TableUseIndice.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.52)
- **Top Global Matches:** file_cluster_11: 6.52, file_cluster_15: 7.381, file_cluster_2: 7.67
- **Magnitude:** 19.04 | **LOC:** 62 | **CtrlFlow:** 24.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.1%), Guard Balance (formerly Safety Score) (60.6%), Complexity Load (formerly Cognitive Load) (23.9%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `0000-MAIN` **(I/O & Config Routines)** (Impact: 6.0)
  * `200-TWO-DIMENSION` **(Compute Cores)** (Impact: 3.1)
  * `100-ONE-DIMENSION` **(Interface Declarations)** (Impact: 1.1)
  * `300-MOSTRAR` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 7
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 17`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 3`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.921
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0807v01TableSearchAll.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.62)
- **Top Global Matches:** file_cluster_11: 5.62, file_cluster_2: 7.0, file_cluster_15: 7.64
- **Magnitude:** 16.86 | **LOC:** 74 | **CtrlFlow:** 6.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.2%), Guard Balance (formerly Safety Score) (61.2%), Complexity Load (formerly Cognitive Load) (28.7%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `100-ONE-BUSCAR` **(I/O & Config Routines)** (Impact: 3.5)
  * `0000-MAIN` **(Interface Declarations)** (Impact: 1.8)
  * `050-SHOW-BEFORE` **(Interface Declarations)** (Impact: 1.4)
  * `150-SHOW-AFTER` **(Interface Declarations)** (Impact: 1.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 8
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 23`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 4`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.921
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0502v01CondicionRelacion.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.596)
- **Top Global Matches:** file_cluster_2: 6.596, file_cluster_15: 7.652, file_cluster_11: 7.876
- **Magnitude:** 14.26 | **LOC:** 37 | **CtrlFlow:** 13.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.2%), Guard Balance (formerly Safety Score) (61.9%), Complexity Load (formerly Cognitive Load) (21.1%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MAIN-PROCEDURE` **(I/O & Config Routines)** (Impact: 4.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 11`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 3`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.921
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0501v01DeclaracioCondicionIF.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 7.216)
- **Top Global Matches:** file_cluster_9: 7.216, file_cluster_16: 12.77, file_cluster_15: 12.837
- **Magnitude:** 12.98 | **LOC:** 45 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (57.8%), Mutation Surface (formerly State Flux) (50.0%), Complexity Load (formerly Cognitive Load) (12.3%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MAIN-PROCEDURE` **(I/O & Config Routines)** (Impact: 9.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 17`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 1`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.921
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0604v01PerformVariying.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 8.418)
- **Top Global Matches:** file_cluster_9: 8.418, file_cluster_11: 8.545, file_cluster_15: 9.281
- **Magnitude:** 12.58 | **LOC:** 41 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (57.8%), Mutation Surface (formerly State Flux) (50.0%), Complexity Load (formerly Cognitive Load) (11.5%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `0000-MAIN` **(I/O & Config Routines)** (Impact: 8.0)
  * `0100-CONTADOR` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 15`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 1`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.921
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL1001v01ManejoCICS.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.081)
- **Top Global Matches:** file_cluster_11: 5.081, file_cluster_2: 6.319, file_cluster_15: 7.481
- **Magnitude:** 12.02 | **LOC:** 67 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (57.8%), Mutation Surface (formerly State Flux) (50.0%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `2200-CONCATENA-DATOS` **(I/O & Config Routines)** (Impact: 1.4)
  * `0000-PRINCIPAL` **(Interface Declarations)** (Impact: 1.2)
  * `2000-PROCESO` **(Interface Declarations)** (Impact: 1.2)
    * *Intent:* *
  * `1000-INICIO` **(I/O & Config Routines)** (Impact: 1.1)
    * *Intent:* *
  * `2100-PEDIR-DATOS` **(Interface Declarations)** (Impact: 1.1)
    * *Intent:* *
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 16`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 3`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.921
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0207v01DivideVerb.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.455)
- **Top Global Matches:** file_cluster_11: 5.455, file_cluster_2: 6.856, file_cluster_17: 7.824
- **Magnitude:** 10.7 | **LOC:** 61 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.1%), Guard Balance (formerly Safety Score) (60.6%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MAIN-PROCEDURE` **(Interface Declarations)** (Impact: 2.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 30`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 7`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.921
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0508v01CondicionVerb.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.95)
- **Top Global Matches:** file_cluster_2: 6.95, file_cluster_15: 7.884, file_cluster_17: 8.086
- **Magnitude:** 10.52 | **LOC:** 41 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (69.0%), Guard Balance (formerly Safety Score) (58.5%), Complexity Load (formerly Cognitive Load) (16.2%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MAIN-PROCEDURE` **(I/O & Config Routines)** (Impact: 6.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 4
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 14`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 2`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.921
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0206v01MultiplyVerb.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.443)
- **Top Global Matches:** file_cluster_11: 5.443, file_cluster_2: 6.854, file_cluster_17: 7.822
- **Magnitude:** 10.38 | **LOC:** 55 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.1%), Guard Balance (formerly Safety Score) (60.6%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MAIN-PROCEDURE` **(Interface Declarations)** (Impact: 2.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 26`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 7`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.921
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0602v01PerformUntil.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.228)
- **Top Global Matches:** file_cluster_11: 5.228, file_cluster_2: 6.948, file_cluster_15: 7.527
- **Magnitude:** 9.0 | **LOC:** 34 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (69.0%), Guard Balance (formerly Safety Score) (58.5%), Complexity Load (formerly Cognitive Load) (10.0%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MAIN-PROCEDURE` **(Interface Declarations)** (Impact: 3.5)
  * `CONTADOR` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 4
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 12`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 2`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.921
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0603v01PerformTimes.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.228)
- **Top Global Matches:** file_cluster_11: 5.228, file_cluster_2: 6.948, file_cluster_15: 7.527
- **Magnitude:** 9.0 | **LOC:** 34 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (69.0%), Guard Balance (formerly Safety Score) (58.5%), Complexity Load (formerly Cognitive Load) (10.0%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `0000-MAIN` **(Interface Declarations)** (Impact: 3.5)
  * `0100-CONTADOR` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 4
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 12`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 2`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.921
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0806v01TableSearch.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.018)
- **Top Global Matches:** file_cluster_11: 5.018, file_cluster_2: 6.642, file_cluster_15: 7.306
- **Magnitude:** 8.92 | **LOC:** 60 | **CtrlFlow:** 13.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (57.8%), Mutation Surface (formerly State Flux) (50.0%), Complexity Load (formerly Cognitive Load) (10.7%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `100-ONE-DIMENSION` **(Interface Declarations)** (Impact: 3.6)
  * `0000-MAIN` **(Interface Declarations)** (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 15`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 3`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.921
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0601v01InOutLineLoop.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.258)
- **Top Global Matches:** file_cluster_11: 5.258, file_cluster_2: 6.992, file_cluster_15: 7.833
- **Magnitude:** 8.78 | **LOC:** 52 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (97.1%), Guard Balance (formerly Safety Score) (56.4%), Mutation Surface (formerly State Flux) (16.8%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MAIN-PROCEDURE` **(Interface Declarations)** (Impact: 1.4)
  * `A-PARA` **(Interface Declarations)** (Impact: 1.3)
    * *Intent:* * in line
  * `B-PARA` **(Interface Declarations)** (Impact: 1.2)
  * `C-PARA` **(Interface Declarations)** (Impact: 1.1)
  * `D-PARA` **(Interface Declarations)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 17`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 1`, `unreferenced_by_name: 3`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.921
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0203v01MoveVerb.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.345)
- **Top Global Matches:** file_cluster_11: 5.345, file_cluster_2: 6.724, file_cluster_17: 7.729
- **Magnitude:** 8.6 | **LOC:** 42 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (91.7%), Guard Balance (formerly Safety Score) (59.9%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MAIN-PROCEDURE` **(Interface Declarations)** (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 16`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 6`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.921
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0803v01TableUseSubIndice.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.517)
- **Top Global Matches:** file_cluster_11: 5.517, file_cluster_2: 6.961, file_cluster_15: 7.88
- **Magnitude:** 8.5 | **LOC:** 58 | **CtrlFlow:** 5.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (83.2%), Guard Balance (formerly Safety Score) (59.2%), Complexity Load (formerly Cognitive Load) (11.5%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `0000-MAIN` **(Interface Declarations)** (Impact: 2.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 26`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 5`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.921
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0605v01GotoStatement.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 6.541)
- **Top Global Matches:** file_cluster_7: 6.541, file_cluster_12: 8.621, file_cluster_5: 9.759
- **Magnitude:** 8.44 | **LOC:** 43 | **CtrlFlow:** 3.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (60.6%), Debt Markers (formerly Tech Debt) (37.8%), Mutation Surface (formerly State Flux) (16.8%), Complexity Load (formerly Cognitive Load) (6.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `B-PARA` **(Interface Declarations)** (Impact: 2.1)
  * `0000-MAIN` **(Interface Declarations)** (Impact: 1.4)
  * `D-PARA` **(Interface Declarations)** (Impact: 1.2)
  * `C-PARA` **(Interface Declarations)** (Impact: 1.1)
  * `0100-CONTADOR` **(Interface Declarations)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 14`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 1`, `unreferenced_by_name: 1`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.921
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0505v01CondicionName.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.477)
- **Top Global Matches:** file_cluster_2: 6.477, file_cluster_15: 7.658, file_cluster_11: 7.787
- **Magnitude:** 8.26 | **LOC:** 40 | **CtrlFlow:** 8.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (69.0%), Guard Balance (formerly Safety Score) (58.5%), Complexity Load (formerly Cognitive Load) (10.0%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MAIN-PROCEDURE` **(I/O & Config Routines)** (Impact: 3.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 4
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 12`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 2`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.921
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0506v01CondicionNot.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.477)
- **Top Global Matches:** file_cluster_2: 6.477, file_cluster_15: 7.658, file_cluster_11: 7.787
- **Magnitude:** 8.26 | **LOC:** 36 | **CtrlFlow:** 8.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (69.0%), Guard Balance (formerly Safety Score) (58.5%), Complexity Load (formerly Cognitive Load) (10.0%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MAIN-PROCEDURE` **(I/O & Config Routines)** (Impact: 3.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 4
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 12`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 2`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.921
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0304v01ClausuleComp.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.509)
- **Top Global Matches:** file_cluster_11: 5.509, file_cluster_2: 6.976, file_cluster_17: 7.755
- **Magnitude:** 6.96 | **LOC:** 56 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (69.0%), Guard Balance (formerly Safety Score) (58.5%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MAIN-PROCEDURE` **(Interface Declarations)** (Impact: 2.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 19`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 4`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.921
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0303v01ClausuleUse.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.68)
- **Top Global Matches:** file_cluster_11: 5.68, file_cluster_2: 7.159, file_cluster_17: 7.898
- **Magnitude:** 6.8 | **LOC:** 44 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (69.0%), Guard Balance (formerly Safety Score) (58.5%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MAIN-PROCEDURE` **(Interface Declarations)** (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 20`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 4`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.921
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0305v01ClausuleComp-1.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.334)
- **Top Global Matches:** file_cluster_11: 5.334, file_cluster_2: 6.776, file_cluster_17: 7.751
- **Magnitude:** 6.8 | **LOC:** 51 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (69.0%), Guard Balance (formerly Safety Score) (58.5%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MAIN-PROCEDURE` **(Interface Declarations)** (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 16`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 4`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.921
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0306v01ClausuleComp-2.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.334)
- **Top Global Matches:** file_cluster_11: 5.334, file_cluster_2: 6.776, file_cluster_17: 7.751
- **Magnitude:** 6.8 | **LOC:** 51 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (69.0%), Guard Balance (formerly Safety Score) (58.5%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MAIN-PROCEDURE` **(Interface Declarations)** (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 16`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 4`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.921
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CBL0307v01ClausuleComp-3.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.334)
- **Top Global Matches:** file_cluster_11: 5.334, file_cluster_2: 6.776, file_cluster_17: 7.751
- **Magnitude:** 6.8 | **LOC:** 61 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (69.0%), Guard Balance (formerly Safety Score) (58.5%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MAIN-PROCEDURE` **(Interface Declarations)** (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 16`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 4`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 18.921
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `CBL0604v01PerformVariying.cbl` (COBOL) | Magnitude: 12.58 | Delta: **0.127** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 15, branch: 6, debug_prints: 6

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `CBL0101v01EstructuraInicial.COB` -> **Severity: 1892.1** (Blast Radius: 18.921 * Doc Risk: 100.0%)
- `CBL0102v01DivisionAmbiente.cbl` -> **Severity: 1892.1** (Blast Radius: 18.921 * Doc Risk: 100.0%)
- `CBL0103v01DivisionData.cbl` -> **Severity: 1892.1** (Blast Radius: 18.921 * Doc Risk: 100.0%)
- `CBL0104v01ProcedureDivision.cbl` -> **Severity: 1892.1** (Blast Radius: 18.921 * Doc Risk: 100.0%)
- `CBL0105v01DeclararElementoGrupo.cbl` -> **Severity: 1892.1** (Blast Radius: 18.921 * Doc Risk: 100.0%)

## 13. MAINFRAME SYSTEM FACTS (Named Relations & Record Layouts)
> **AI CONTEXT:** Named mainframe relations the structural signal counts flatten -- the call graph (`CALL`/CICS `LINK`·`XCTL`/JCL `EXEC PGM=`), the dataset boundary (`SELECT…ASSIGN` + `OPEN` modes, JCL `DD`→dataset), and record layouts (COBOL DATA DIVISION items, PL/I `DECLARE`d structures). BMS screen maps (every field's position, length and attributes, `screen_field_data`) are the 3270 UI surface. These are the schema of the system: use them to trace which program runs which, which dataset a job binds, and the shape of the records that flow between them. Extracted by the engine (`core/mainframe_boundary.py`) and carried in the master DB (`call_site_data`/`dataset_data`/`record_data`); resolution to files is redone per scan.

- **Coverage:** `51` files carry mainframe facts -- `0` call sites, `10` dataset bindings, `330` record items.

### `CBL0207v01DivideVerb.cbl` (COBOL)
- **Record layouts (11 items):** `WS-NUM1 (1)`, `WS-NUM2 (1)`, `WS-NUM3 (1)`, `WS-NUM4 (1)`, `WS-NUMA (1)`, `WS-NUMB (1)`, `WS-NUMC (1)`, `WS-NUMD (1)`, `WS-NUMT (1)`, `WS-RES1 (1)`, `WS-RES2 (1)`
- **Data moves:** 17 (DIVIDE 17); most-fed items `WS-NUMT`, `WS-NUM2`, `WS-NUM4`, `WS-RES1`, `WS-RES2`, `WS-NUM3`

### `CBL0901v02AccesoSecuencialFiles.cbl` (COBOL)
- **Datasets:** `HOST01.TXT(declared)`, `HOST02.TXT(declared)`, `HOST03.TXT(declared)`
- **Record layouts (20 items):** `WK-CANAL-UI (6)`, `WK-CANAL (5)`, `REG-HOST01⟵HOST001 (3)`, `REG-HOST02⟵HOST002 (3)`, `REG-HOST03⟵HOST003 (3)`
- **Special names:** `DECIMAL-POINT IS COMMA`
- **Keyed files:** `HOST002 INDEXED/SEQUENTIAL key COD-02`, `HOST003 RELATIVE/SEQUENTIAL key COD-03`
- **Data moves:** 1 (MOVE 1)

### `CBL0903v01AccesoDinamico.cbl` (COBOL)
- **Datasets:** `HOST06.TXT(declared)`, `HOST07.TXT(declared)`
- **Record layouts (19 items):** `WK-CANAL-UI (6)`, `WK-CANAL (4)`, `REG-HOST06⟵HOST006 (3)`, `REG-HOST07⟵HOST007 (3)`, `WS-RK-07 (1)`, `EOF-06 (1)`, `EOF-07 (1)`
- **Special names:** `DECIMAL-POINT IS COMMA`
- **Keyed files:** `HOST006 INDEXED/DYNAMIC key COD-06`, `HOST007 RELATIVE/DYNAMIC key WS-RK-07`

### `CBL0206v01MultiplyVerb.cbl` (COBOL)
- **Record layouts (9 items):** `WS-NUM1 (1)`, `WS-NUM2 (1)`, `WS-NUM3 (1)`, `WS-NUM4 (1)`, `WS-NUMA (1)`, `WS-NUMB (1)`, `WS-NUMC (1)`, `WS-NUMD (1)`, `WS-NUMT (1)`
- **Data moves:** 13 (MULTIPLY 13); most-fed items `WS-NUM3`, `WS-NUM4`, `WS-NUMA`, `WS-NUMB`, `WS-NUMC`, `WS-NUMT`

### `CBL0902v01AccesoAleatorio.cbl` (COBOL)
- **Datasets:** `HOST04.TXT(declared)`, `HOST05.TXT(declared)`
- **Record layouts (17 items):** `WK-CANAL-UI (6)`, `WK-CANAL (5)`, `REG-HOST04⟵HOST004 (3)`, `REG-HOST05⟵HOST005 (3)`
- **Special names:** `DECIMAL-POINT IS COMMA`
- **Keyed files:** `HOST004 INDEXED/RANDOM key COD-CANAL`, `HOST005 RELATIVE/RANDOM key COD-05`
- **Data moves:** 1 (MOVE 1)

### `CBL0208v01ComputeVerb.cbl` (COBOL)
- **Record layouts (11 items):** `WS-NUM1 (1)`, `WS-NUM2 (1)`, `WS-NUM3 (1)`, `WS-NUM4 (1)`, `WS-NUMA (1)`, `WS-NUMB (1)`, `WS-NUMC (1)`, `WS-NUMD (1)`, `WS-NUMT (1)`, `WS-RES1 (1)`, `WS-RES2 (1)`
- **Data moves:** 8 (COMPUTE 8); most-fed items `WS-NUM4`, `WS-NUMD`

### `CBL0203v01MoveVerb.cbl` (COBOL)
- **Record layouts (10 items):** `WS-PRESTAMO (4)`, `WS-NOMBRE (1)`, `WS-ID (1)`, `WS-DIRECCION (1)`, `WS-NUMERO (1)`, `WS-CIUDAD (1)`, `WS-POSTAL (1)`
- **Data moves:** 7 (INITIALIZE 3, MOVE 4)

### `CBL0204v01AddVerb.cbl` (COBOL)
- **Record layouts (9 items):** `WS-NUM1 (1)`, `WS-NUM2 (1)`, `WS-NUM3 (1)`, `WS-NUM4 (1)`, `WS-NUMA (1)`, `WS-NUMB (1)`, `WS-NUMC (1)`, `WS-NUMD (1)`, `WS-NUMT (1)`
- **Data moves:** 8 (ADD 8); most-fed items `WS-NUMT`, `WS-NUM3`, `WS-NUM4`

### `CBL0205v01SubtractVerb.cbl` (COBOL)
- **Record layouts (9 items):** `WS-NUM1 (1)`, `WS-NUM2 (1)`, `WS-NUM3 (1)`, `WS-NUM4 (1)`, `WS-NUMA (1)`, `WS-NUMB (1)`, `WS-NUMC (1)`, `WS-NUMD (1)`, `WS-NUMT (1)`
- **Data moves:** 8 (SUBTRACT 8); most-fed items `WS-NUMT`, `WS-NUM3`, `WS-NUM4`

### `CBL0901v01AccesoSecuencial.cbl` (COBOL)
- **Datasets:** `HOST01.TXT(declared)`
- **Record layouts (14 items):** `WK-CANAL-UI (6)`, `WK-CANAL (5)`, `REG-HOST01⟵HOST001 (3)`
- **Data moves:** 1 (MOVE 1)

### `CBL1001v01ManejoCICS.cbl` (COBOL)
- **Record layouts (8 items):** `WX-PREGUNTA-NOMBRE (4)`, `WX-RESPUESTA (1)`, `WX-HOLA (1)`, `WX-SALUDO (1)`, `WX-RESTO-SALUDO (1)`
- **Special names:** `DECIMAL-POINT IS COMMA`
- **Data moves:** 7 (ACCEPT 1, INITIALIZE 2, MOVE 1, STRING 3); most-fed items `WX-RESPUESTA`, `WX-SALUDO`

### `CBL0301v01DataLayoutRedefine.cbl` (COBOL)
- **Record layouts (10 items):** `WS-FECHA (6)`, `WS-NUM1 (1)`, `WS-OLD (1)`, `WS-NEW1 (1)`, `WS-NEW2 (1)`
- **Data moves:** 3 (MOVE 3)

### `CBL0807v01TableSearchAll.cbl` (COBOL)
- **Record layouts (9 items):** `WS-APLICACION (4)`, `WS-REGISTRO (3)`, `WS-TEMA (1)`, `WS-SRCH (1)`
- **Data moves:** 4 (MOVE 4); most-fed items `WS-CODIGO`, `WS-NOMBRE`

### `CBL0804v01TableUseIndice.cbl` (COBOL)
- **Record layouts (9 items):** `WS-TABLE (5)`, `WS-APLICACION (3)`, `WS-TEMA (1)`
- **Data moves:** 3 (MOVE 3)

### `CBL0805v01TableUseIndiceWithSet.cbl` (COBOL)
- **Record layouts (9 items):** `WS-TABLE (5)`, `WS-APLICACION (3)`, `WS-TEMA (1)`
- **Data moves:** 3 (MOVE 3)

### `CBL0302v01DataLayoutRenames.cbl` (COBOL)
- **Record layouts (10 items):** `WS-ARQUITECTURA (5)`, `WS-INTERES (4)`, `WS-TEMA (1)`
- **Data moves:** 1 (MOVE 1)

### `CBL0304v01ClausuleComp.cbl` (COBOL)
- **Record layouts (7 items):** `WS-TEMA (1)`, `WS-TEN (1)`, `WS-TEN1 (1)`, `WS-TEA (1)`, `WS-TEA1 (1)`, `WS-INTERES (1)`, `WS-INTERES1 (1)`
- **Data moves:** 4 (MOVE 4); most-fed items `WS-INTERES1`, `WS-TEA1`, `WS-TEN1`

### `CBL0305v01ClausuleComp-1.cbl` (COBOL)
- **Record layouts (7 items):** `WS-TEMA (1)`, `WS-TEN (1)`, `WS-TEN1 (1)`, `WS-TEA (1)`, `WS-TEA1 (1)`, `WS-INTERES (1)`, `WS-INTERES1 (1)`
- **Data moves:** 4 (MOVE 4)

### `CBL0306v01ClausuleComp-2.cbl` (COBOL)
- **Record layouts (7 items):** `WS-TEMA (1)`, `WS-TEN (1)`, `WS-TEN1 (1)`, `WS-TEA (1)`, `WS-TEA1 (1)`, `WS-INTERES (1)`, `WS-INTERES1 (1)`
- **Data moves:** 4 (MOVE 4)

### `CBL0307v01ClausuleComp-3.cbl` (COBOL)
- **Record layouts (7 items):** `WS-TEMA (1)`, `WS-TEN (1)`, `WS-TEN1 (1)`, `WS-TEA (1)`, `WS-TEA1 (1)`, `WS-INTERES (1)`, `WS-INTERES1 (1)`
- **Data moves:** 4 (MOVE 4)

*(+31 more files with mainframe facts; full detail in `record_data`/`call_site_data`/`dataset_data`.)*

- **Mainframe skeleton completeness:** 67% (mean channel ratio; channel table in the audit report, section 7). Top missing inputs: JCL and PROC libraries (51 gaps).

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 29 call pairs -- scoped 96.6%, unique 0.0%, ambiguous 0.0%, external 3.4%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| cobol | 29 | 96.6% | 0.0% | 0.0% | 3.4% |

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
