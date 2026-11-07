# ARCHITECTURAL_BRIEF: node-sql-parser
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `N/A` |
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
- **Scope:** 57 analyzed artifact(s), 4492 LOC.
- **Load-bearing artifact:** `package/lib/util.js` -- 34 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `package/lib/expr.js` -- pulls in 19 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `package/lib/util.js` at magnitude 386.0 (structural weight, not risk).
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
| Total Artifacts | 92 |
| Analyzed Artifacts (Scanned) | 57 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 35 |
| Total LOC | 4492 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 62.0% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.1654 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.5107 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 63.2% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.385 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 1 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 38 | 3974 | 66.7% |
| TYPESCRIPT | 17 | 518 | 29.8% |
| MARKDOWN | 1 | 0 | 1.8% |
| PLAINTEXT | 1 | 0 | 1.8% |

## 4.1 SOURCE ENCODINGS
All 57 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 32%, Large Core Modules (2) 25%, Parameter Forwarders Files 21%, Compute Cores Files 18%, Large Core Modules (3) 4%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 55 | 96.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 3.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 35*

**Composition by Extension & Reason:**
- `.js`: 16x Excluded (Saturation: Line 1 exceeds 500 chars), 1x Excluded (Saturation: Line 5 exceeds 500 chars)
- `.map`: 16x Excluded (Saturation: Line 1 exceeds 500 chars)
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ts`: 1x Excluded (Machine-Generated Source Code Signature: 2114 LOC)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 89.8 | 38.1 | 33.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 68.0 | 36.5 | 43.6 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 99.6 | 2.2 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 15.1 | 2.4 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 23.2 | 1.7 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 67.3 | 96.1 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 22.4 | 0.4 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 64.1 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 0 | 0 | 0 | - |
| cleanup | 0 | 0 | 0 | - |
| guards | 447 | 38 | 15 | `package/lib/util.js` |
| danger | 60 | 17 | 3 | `package/types.d.ts` |
| concurrency | 6 | 4 | 0 | `package/types.d.ts` |
| connectivity | 91 | 18 | 1 | `package/types.d.ts` |
| io | 11 | 2 | 0 | `package/types.d.ts` |
| crypto | 0 | 0 | 0 | - |
| ipc | 1 | 1 | 0 | `package/lib/tables.js` |
| time | 0 | 0 | 0 | - |
| serialization | 2 | 1 | 0 | `package/lib/util.js` |
| regex | 2 | 2 | 0 | `package/lib/parser.js` |
| events | 35 | 6 | 0 | `package/lib/command.js` |
| tests | 0 | 0 | 0 | - |
| docs | 11 | 9 | 1 | `package/lib/util.js` |
| debt | 0 | 0 | 0 | - |
| mutation | 1076 | 39 | 58 | `package/lib/create.js` |
| dead_code | 20 | 3 | 0 | `package/lib/parser.js` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **5.5**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `package/types.d.ts` (Hits: 8)
- `package/lib/limit.js` (Hits: 3)
- `package/README.md` (Hits: 0)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **util.js** (`package/lib/util.js`) — 34 inbound connections
2. **expr.js** (`package/lib/expr.js`) — 29 inbound connections
3. **column.js** (`package/lib/column.js`) — 17 inbound connections
4. **tables.js** (`package/lib/tables.js`) — 13 inbound connections
5. **collate.js** (`package/lib/collate.js`) — 6 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **expr.js** (`package/lib/expr.js`) — 19 outbound dependencies
2. **union.js** (`package/lib/union.js`) — 18 outbound dependencies
3. **create.js** (`package/lib/create.js`) — 11 outbound dependencies
4. **alter.js** (`package/lib/alter.js`) — 7 outbound dependencies
5. **command.js** (`package/lib/command.js`) — 7 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `literalToSQL` **(Compute Cores)** (@ `package/lib/util.js`) -> Impact: **52.3** | LOC: 84
- `identifierToSql` **(Defensive Guards)** (@ `package/lib/util.js`) -> Impact: **41.5** | LOC: 29
- `alterExprToSQL` **(Compute Cores)** (@ `package/lib/alter.js`) -> Impact: **34.1** | LOC: 59
- `createToSQL` **(Compute Cores)** (@ `package/lib/create.js`) -> Impact: **26.4** | LOC: 48
- `commonCmdToSQL` **(Compute Cores)** (@ `package/lib/command.js`) -> Impact: **25.8** | LOC: 36
- `tableToSQL` **(Compute Cores)** (@ `package/lib/tables.js`) -> Impact: **25.5** | LOC: 58
- `columnIdentifierToSql` **(Compute Cores)** (@ `package/lib/util.js`) -> Impact: **25.2** | LOC: 24
- `funcToSQL` **(Defensive Guards)** (@ `package/lib/func.js`) -> Impact: **25.0** | LOC: 48
- `binaryToSQL` **(Defensive Guards)** (@ `package/lib/binary.js`) -> Impact: **22.7** | LOC: 30
- `castToSQL` **(Defensive Guards)** (@ `package/lib/func.js`) -> Impact: **22.3** | LOC: 51

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `package/lib` | 38 | 2936.08 | 54.88% | 2.62% |
| `package` | 4 | 16.1 | 2.6% | 5.33% |
| `package/umd` | 15 | 8.7 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `package/lib/parser.js` -> **99.6112%** Exposure
- `package/types.d.ts` -> **21.3362%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `package/lib/aggregation.js` -> **100.0%** Exposure
- `package/lib/binary.js` -> **100.0%** Exposure
- `package/lib/case.js` -> **100.0%** Exposure
- `package/lib/column.js` -> **100.0%** Exposure
- `package/lib/constrain.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `package/lib/parser.js` -> **7** Orphaned Functions | **0** Duplicates
- `package/types.d.ts` -> **6** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `3` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `package/lib/util.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.28)
- **Top Global Matches:** file_cluster_4: 7.28, file_cluster_6: 8.318, file_cluster_15: 13.912
- **Magnitude:** 386.0 | **LOC:** 461 | **CtrlFlow:** 29.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **34** in-repo importer(s); it depends on **2**; blast radius 163.285; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (65.7%), Guard Balance (formerly Safety Score) (58.3%)
- **Documentation Coverage:** 88.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `literalToSQL` **(Compute Cores)** (Impact: 52.3)
  * `identifierToSql` **(Defensive Guards)** (Impact: 41.5)
  * `columnIdentifierToSql` **(Compute Cores)** (Impact: 25.2)
  * `createValueExpr` **(Defensive Guards)** (Impact: 12.8)
    * *Intent:* /** */
  * `autoIncrementToSQL` **(Defensive Guards)** (Impact: 12.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 38 instances
* *State Mutation (weighted view):* 139
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 125`, `structural_boundaries: 93`, `args: 32`, `func_start: 25`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 63`, `dead_code: 7`
* *Architecture:* `import: 2`
* *Defense:* `safety: 37`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 163.285
  * `Choke Point (Betweenness):` 0.01974 | `Ripple Effect (Closeness):` 0.609023
  * `Imports (Out-Degree: 2):` collate, column
  * `Imported By (In-Degree: 34):` (Excluded from Brief to save tokens)

### `package/lib/create.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.161)
- **Top Global Matches:** file_cluster_4: 7.161, file_cluster_9: 8.751, file_cluster_12: 8.884
- **Magnitude:** 355.3 | **LOC:** 496 | **CtrlFlow:** 19.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **11**; blast radius 6.7; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.3%), Complexity Load (formerly Cognitive Load) (62.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createToSQL` **(Compute Cores)** (Impact: 26.4)
  * `createTableToSQL` **(Compute Cores)** (Impact: 15.0)
  * `createTriggerToSQL` **(Compute Cores)** (Impact: 13.1)
  * `createDomainToSQL` **(Compute Cores)** (Impact: 12.8)
  * `createDefinitionToSQL` **(Compute Cores)** (Impact: 12.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 54 instances
* *State Mutation (weighted view):* 166
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 96`, `structural_boundaries: 69`, `args: 30`, `func_start: 21`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 58`
* *Architecture:* `import: 11`
* *Defense:* `safety: 15`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.7
  * `Choke Point (Betweenness):` 0.005259 | `Ripple Effect (Closeness):` 0.220408
  * `Imports (Out-Degree: 11):` alter, column, command, constrain, expr, func, index-definition, tables...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/lib/tables.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.67)
- **Top Global Matches:** file_cluster_4: 6.67, file_cluster_9: 10.771, file_cluster_15: 10.879
- **Magnitude:** 238.96 | **LOC:** 279 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **6**; blast radius 42.808; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (72.8%), Guard Balance (formerly Safety Score) (64.1%)
- **Documentation Coverage:** 84.6154% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `tableToSQL` **(Compute Cores)** (Impact: 25.5)
  * `tablesToSQL` **(Defensive Guards)** (Impact: 22.0)
    * *Intent:* /** */
  * `tableHintToSQL` **(Compute Cores)** (Impact: 12.6)
  * `tableOptionToSQL` **(Compute Cores)** (Impact: 11.1)
  * `temporalTableOptionToSQL` **(Compute Cores)** (Impact: 9.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 37 instances
* *State Mutation (weighted view):* 119
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 45`, `args: 18`, `func_start: 12`
* *Risk/State:* `state_mutation: 45`
* *Architecture:* `import: 6`
* *Defense:* `safety: 17`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 42.808
  * `Choke Point (Betweenness):` 0.009885 | `Ripple Effect (Closeness):` 0.379391
  * `Imports (Out-Degree: 6):` binary, column, expr, insert, interval, util
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `package/lib/command.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.65)
- **Top Global Matches:** file_cluster_4: 6.65, file_cluster_15: 8.14, file_cluster_12: 9.661
- **Magnitude:** 227.72 | **LOC:** 307 | **CtrlFlow:** 18.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **7**; blast radius 5.152; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (68.7%), Guard Balance (formerly Safety Score) (64.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `commonCmdToSQL` **(Compute Cores)** (Impact: 25.8)
  * `declareToSQL` **(Compute Cores)** (Impact: 11.8)
  * `grantAndRevokeToSQL` **(Compute Cores)** (Impact: 10.3)
  * `ifToSQL` **(Compute Cores)** (Impact: 8.1)
  * `raiseToSQL` **(Defensive Guards)** (Impact: 7.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 33 instances
* *State Mutation (weighted view):* 116
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 41`, `args: 26`, `func_start: 17`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 50`
* *Architecture:* `import: 7`
* *Defense:* `safety: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.152
  * `Choke Point (Betweenness):` 0.011152 | `Ripple Effect (Closeness):` 0.218329
  * `Imports (Out-Degree: 7):` column, create, expr, sql, tables, union, util
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/lib/column.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.502)
- **Top Global Matches:** file_cluster_15: 6.502, file_cluster_9: 7.876, file_cluster_12: 8.064
- **Magnitude:** 226.66 | **LOC:** 265 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **17** in-repo importer(s); it depends on **6**; blast radius 114.57; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (71.0%), Guard Balance (formerly Safety Score) (60.8%)
- **Documentation Coverage:** 93.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `columnToSQL` **(Defensive Guards)** (Impact: 21.9)
  * `columnOption` **(Compute Cores)** (Impact: 13.6)
  * `columnDataType` **(Compute Cores)** (Impact: 11.2)
  * `columnRefToSQL` **(Defensive Guards)** (Impact: 10.2)
  * `arrayIndexToSQL` **(Defensive Guards)** (Impact: 9.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 32 instances
* *State Mutation (weighted view):* 114
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 39`, `args: 23`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 50`
* *Architecture:* `import: 6`
* *Defense:* `safety: 28`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 114.57
  * `Choke Point (Betweenness):` 0.045843 | `Ripple Effect (Closeness):` 0.413265
  * `Imports (Out-Degree: 6):` collate, constrain, expr, func, tables, util
  * `Imported By (In-Degree: 17):` (Excluded from Brief to save tokens)

### `package/lib/func.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.061)
- **Top Global Matches:** file_cluster_4: 6.061, file_cluster_15: 10.018, file_cluster_6: 10.977
- **Magnitude:** 190.8 | **LOC:** 246 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **5**; blast radius 27.203; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (89.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (62.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `funcToSQL` **(Defensive Guards)** (Impact: 25.0)
  * `castToSQL` **(Defensive Guards)** (Impact: 22.3)
  * `arrayDimensionToSymbol` **(Compute Cores)** (Impact: 10.8)
  * `anyValueFuncToSQL` **(Compute Cores)** (Impact: 3.6)
  * `jsonObjectArgToSQL` **(Compute Cores)** (Impact: 3.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 31 instances
* *State Mutation (weighted view):* 103
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 32`, `args: 15`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 41`
* *Architecture:* `import: 5`
* *Defense:* `safety: 18`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 27.203
  * `Choke Point (Betweenness):` 0.005969 | `Ripple Effect (Closeness):` 0.321429
  * `Imports (Out-Degree: 5):` collate, column, expr, over, util
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/lib/alter.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.158)
- **Top Global Matches:** file_cluster_4: 6.158, file_cluster_6: 10.458, file_cluster_15: 10.581
- **Magnitude:** 151.5 | **LOC:** 211 | **CtrlFlow:** 22.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **7**; blast radius 11.856; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (83.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (60.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `alterExprToSQL` **(Compute Cores)** (Impact: 34.1)
  * `alterToSQL` **(Compute Cores)** (Impact: 15.2)
  * `alterExprPartition` **(Compute Cores)** (Impact: 7.5)
  * `alterArgsToSQL` **(Compute Cores)** (Impact: 7.3)
  * `alterViewToSQL` **(Compute Cores)** (Impact: 6.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 63
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 33`, `args: 15`, `func_start: 11`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 23`
* *Architecture:* `import: 7`
* *Defense:* `safety: 9`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.856
  * `Choke Point (Betweenness):` 0.011747 | `Ripple Effect (Closeness):` 0.304511
  * `Imports (Out-Degree: 7):` column, create, expr, index-definition, select, tables, util
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/lib/select.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.681)
- **Top Global Matches:** file_cluster_12: 7.681, file_cluster_9: 8.557, file_cluster_7: 10.052
- **Magnitude:** 112.82 | **LOC:** 138 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **7**; blast radius 14.748; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (68.7%), Guard Balance (formerly Safety Score) (66.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 75.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `selectToSQL` **(Defensive Guards)** (Impact: 18.5)
  * `selectIntoToSQL` **(Defensive Guards)** (Impact: 10.9)
  * `distinctToSQL` **(Defensive Guards)** (Impact: 6.2)
  * `forXmlToSQL` **(Compute Cores)** (Impact: 4.8)
    * *Intent:* */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 70
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 13`, `args: 6`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 26`
* *Architecture:* `import: 7`
* *Defense:* `safety: 16`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 14.748
  * `Choke Point (Betweenness):` 0.02113 | `Ripple Effect (Closeness):` 0.312741
  * `Imports (Out-Degree: 7):` collate, column, expr, limit, tables, util, with
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `package/lib/expr.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 8.756)
- **Top Global Matches:** file_cluster_15: 8.756, file_cluster_12: 9.042, file_cluster_9: 9.303
- **Magnitude:** 104.06 | **LOC:** 149 | **CtrlFlow:** 23.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **29** in-repo importer(s); it depends on **19**; blast radius 149.853; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (64.4%), Guard Balance (formerly Safety Score) (53.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `orderOrPartitionByToSQL` **(Defensive Guards)** (Impact: 13.0)
  * `exprToSQL` **(Defensive Guards)** (Impact: 9.4)
  * `unaryToSQL` **(Defensive Guards)** (Impact: 9.0)
  * `expr_list` **(Callbacks & Closures)** (Impact: 7.6)
  * `varToSQL` **(Compute Cores)** (Impact: 6.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 26`, `args: 14`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 18`
* *Architecture:* `api: 1`, `import: 19`
* *Defense:* `safety: 17`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 149.853
  * `Choke Point (Betweenness):` 0.285564 | `Ripple Effect (Closeness):` 0.525974
  * `Imports (Out-Degree: 19):` aggregation, alter, array-struct, assign, binary, case, collate, column...
  * `Imported By (In-Degree: 29):` (Excluded from Brief to save tokens)

### `package/lib/index-definition.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.352)
- **Top Global Matches:** file_cluster_15: 7.352, file_cluster_12: 7.561, file_cluster_9: 8.2
- **Magnitude:** 102.1 | **LOC:** 106 | **CtrlFlow:** 24.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **2**; blast radius 11.515; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (76.5%), Guard Balance (formerly Safety Score) (68.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `indexOptionToSQL` **(Compute Cores)** (Impact: 20.3)
  * `indexTypeAndOptionToSQL` **(Defensive Guards)** (Impact: 9.5)
  * `indexTypeToSQL` **(Parameter Forwarders)** (Impact: 3.2)
  * `indexOptionListToSQL` **(Parameter Forwarders)** (Impact: 3.0)
  * `indexDefinitionToSQL` **(Parameter Forwarders)** (Impact: 2.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 62
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 17`, `args: 8`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 24`
* *Architecture:* `import: 2`
* *Defense:* `safety: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.515
  * `Choke Point (Betweenness):` 0.00436 | `Ripple Effect (Closeness):` 0.231429
  * `Imports (Out-Degree: 2):` expr, util
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/lib/parser.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.828)
- **Top Global Matches:** file_cluster_12: 6.828, file_cluster_15: 7.062, file_cluster_16: 9.087
- **Magnitude:** 91.44 | **LOC:** 88 | **CtrlFlow:** 37.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 3.75; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.6%), Complexity Load (formerly Cognitive Load) (81.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `whiteListCheck` **(Defensive Guards)** (Impact: 21.4)
  * `parse` **(Defensive Guards)** (Impact: 12.6)
  * `columnsToSQL` **(Defensive Guards)** (Impact: 6.3)
  * `_interopRequireDefault` **(Compute Cores)** (Impact: 5.7)
  * `astify` **(Parameter Forwarders)** (Impact: 3.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 19`, `args: 12`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 9`, `unreferenced_by_name: 7`
* *Architecture:* `import: 5`
* *Defense:* `safety: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.75
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` column, expr, parser.all, sql, util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/lib/insert.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.923)
- **Top Global Matches:** file_cluster_15: 5.923, file_cluster_10: 7.739, file_cluster_2: 8.228
- **Magnitude:** 77.1 | **LOC:** 120 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **6**; blast radius 19.33; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (60.7%), Guard Balance (formerly Safety Score) (54.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 83.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `insertToSQL` **(Defensive Guards)** (Impact: 8.5)
  * `conflictActionToSQL` **(Compute Cores)** (Impact: 6.6)
  * `partitionToSQL` **(Defensive Guards)** (Impact: 6.4)
  * `conflictTargetToSQL` **(Compute Cores)** (Impact: 6.2)
  * `valuesToSQL` **(Defensive Guards)** (Impact: 4.8)
    * *Intent:* /** */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 39
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 16`, `args: 10`, `func_start: 6`
* *Risk/State:* `state_mutation: 17`
* *Architecture:* `import: 6`
* *Defense:* `safety: 13`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 19.33
  * `Choke Point (Betweenness):` 0.010498 | `Ripple Effect (Closeness):` 0.312741
  * `Imports (Out-Degree: 6):` column, expr, tables, union, update, util
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `package/lib/show.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 6.933)
- **Top Global Matches:** file_cluster_9: 6.933, file_cluster_15: 7.341, file_cluster_16: 9.103
- **Magnitude:** 65.76 | **LOC:** 89 | **CtrlFlow:** 29.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **4**; blast radius 11.338; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (72.2%), Guard Balance (formerly Safety Score) (54.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `showToSQL` **(Compute Cores)** (Impact: 18.8)
  * `showGrantsForUser` **(Compute Cores)** (Impact: 9.2)
  * `showLikeAndWhereToSQL` **(Defensive Guards)** (Impact: 4.8)
  * `showEventToSQL` **(Parameter Forwarders)** (Impact: 3.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 28
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 20`, `args: 7`, `func_start: 4`
* *Risk/State:* `state_mutation: 10`
* *Architecture:* `import: 4`
* *Defense:* `safety: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.338
  * `Choke Point (Betweenness):` 0.001878 | `Ripple Effect (Closeness):` 0.300557
  * `Imports (Out-Degree: 4):` expr, limit, tables, util
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/lib/binary.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 8.441)
- **Top Global Matches:** file_cluster_9: 8.441, file_cluster_12: 12.515, file_cluster_16: 14.19
- **Magnitude:** 47.68 | **LOC:** 50 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **3**; blast radius 16.518; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (88.9%), Guard Balance (formerly Safety Score) (53.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `binaryToSQL` **(Defensive Guards)** (Impact: 22.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 24
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 10`, `args: 3`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 8`
* *Architecture:* `import: 3`
* *Defense:* `safety: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 16.518
  * `Choke Point (Betweenness):` 8.1e-05 | `Ripple Effect (Closeness):` 0.300557
  * `Imports (Out-Degree: 3):` collate, expr, util
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/lib/aggregation.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 6.73)
- **Top Global Matches:** file_cluster_9: 6.73, file_cluster_15: 12.93, file_cluster_16: 13.135
- **Magnitude:** 42.9 | **LOC:** 42 | **CtrlFlow:** 45.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 10.454; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (69.0%), Guard Balance (formerly Safety Score) (54.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `aggrToSQL` **(Compute Cores)** (Impact: 18.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 24
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 3`, `args: 3`, `func_start: 1`
* *Risk/State:* `state_mutation: 8`
* *Architecture:* `import: 3`
* *Defense:* `safety: 9`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 10.454
  * `Choke Point (Betweenness):` 0.002413 | `Ripple Effect (Closeness):` 0.292948
  * `Imports (Out-Degree: 3):` expr, over, util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/union.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 10.359)
- **Top Global Matches:** file_cluster_9: 10.359, file_cluster_15: 11.43, file_cluster_16: 12.156
- **Magnitude:** 41.68 | **LOC:** 85 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **18**; blast radius 18.732; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (57.1%), Guard Balance (formerly Safety Score) (51.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `multipleToSQL` **(Defensive Guards)** (Impact: 9.0)
  * `unionToSQL` **(Compute Cores)** (Impact: 8.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 23
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 9`, `args: 4`, `func_start: 2`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `import: 18`
* *Defense:* `safety: 10`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 18.732
  * `Choke Point (Betweenness):` 0.122416 | `Ripple Effect (Closeness):` 0.317025
  * `Imports (Out-Degree: 18):` alter, analyze, command, comment, create, delete, exec, explain...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `package/lib/array-struct.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.583)
- **Top Global Matches:** file_cluster_15: 7.583, file_cluster_9: 8.001, file_cluster_10: 8.538
- **Magnitude:** 37.14 | **LOC:** 63 | **CtrlFlow:** 29.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 10.454; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Complexity Load (formerly Cognitive Load) (57.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (45.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `arrayStructValueToSQL` **(Compute Cores)** (Impact: 9.2)
  * `arrayExprListToSQL` **(Defensive Guards)** (Impact: 7.7)
  * `arrayStructExprToSQL` **(Defensive Guards)** (Impact: 5.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 14
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 9`, `args: 6`, `func_start: 3`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* `import: 4`
* *Defense:* `safety: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 10.454
  * `Choke Point (Betweenness):` 0.001824 | `Ripple Effect (Closeness):` 0.292948
  * `Imports (Out-Degree: 4):` column, expr, limit, util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/constrain.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 6.47)
- **Top Global Matches:** file_cluster_9: 6.47, file_cluster_15: 12.527, file_cluster_16: 12.616
- **Magnitude:** 36.86 | **LOC:** 49 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **3**; blast radius 20.499; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (79.6%), Guard Balance (formerly Safety Score) (52.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `constraintDefinitionToSQL` **(Defensive Guards)** (Impact: 9.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 26
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 4`, `args: 3`, `func_start: 1`
* *Risk/State:* `state_mutation: 12`
* *Architecture:* `import: 3`
* *Defense:* `safety: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 20.499
  * `Choke Point (Betweenness):` 0.00322 | `Ripple Effect (Closeness):` 0.262987
  * `Imports (Out-Degree: 3):` column, index-definition, util
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/lib/update.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 9.056)
- **Top Global Matches:** file_cluster_12: 9.056, file_cluster_7: 9.818, file_cluster_5: 10.678
- **Magnitude:** 36.74 | **LOC:** 62 | **CtrlFlow:** 24.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **6**; blast radius 9.818; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (64.5%), Guard Balance (formerly Safety Score) (56.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setToSQL` **(Defensive Guards)** (Impact: 12.5)
    * *Intent:* /** */
  * `updateToSQL` **(Parameter Forwarders)** (Impact: 2.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 21
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 6`, `args: 4`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 7`
* *Architecture:* `import: 6`
* *Defense:* `safety: 11`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.818
  * `Choke Point (Betweenness):` 0.003062 | `Ripple Effect (Closeness):` 0.229137
  * `Imports (Out-Degree: 6):` column, expr, limit, tables, util, with
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `package/lib/window.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.269)
- **Top Global Matches:** file_cluster_15: 5.269, file_cluster_10: 7.313, file_cluster_2: 7.76
- **Magnitude:** 36.54 | **LOC:** 84 | **CtrlFlow:** 14.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **3**; blast radius 14.858; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (46.6%), Complexity Load (formerly Cognitive Load) (33.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `constructArgsList` **(Compute Cores)** (Impact: 4.8)
  * `windowFrameExprToSQL` **(Defensive Guards)** (Impact: 4.7)
  * `asWindowSpecToSQL` **(Defensive Guards)** (Impact: 3.2)
  * `windowSpecificationToSQL` **(Parameter Forwarders)** (Impact: 1.9)
  * `namedWindowExprToSQL` **(Parameter Forwarders)** (Impact: 1.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 11`, `args: 9`, `func_start: 7`
* *Risk/State:* `state_mutation: 7`
* *Architecture:* `import: 3`
* *Defense:* `safety: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 14.858
  * `Choke Point (Betweenness):` 0.002413 | `Ripple Effect (Closeness):` 0.296703
  * `Imports (Out-Degree: 3):` expr, over, util
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/lib/case.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.731)
- **Top Global Matches:** file_cluster_15: 6.731, file_cluster_10: 6.779, file_cluster_2: 7.373
- **Magnitude:** 35.76 | **LOC:** 39 | **CtrlFlow:** 28.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 10.454; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (78.2%), Guard Balance (formerly Safety Score) (57.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `caseToSQL` **(Compute Cores)** (Impact: 8.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 3`, `args: 3`, `func_start: 1`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `import: 1`
* *Defense:* `safety: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 10.454
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.292948
  * `Imports (Out-Degree: 1):` expr
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/sql.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.315)
- **Top Global Matches:** file_cluster_15: 7.315, file_cluster_10: 7.462, file_cluster_2: 8.389
- **Magnitude:** 27.94 | **LOC:** 43 | **CtrlFlow:** 38.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **1**; blast radius 5.173; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.2%), Complexity Load (formerly Cognitive Load) (53.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (40.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `goToSQL` **(Defensive Guards)** (Impact: 6.0)
  * `checkSupported` **(Compute Cores)** (Impact: 5.9)
  * `toSQL` **(Defensive Guards)** (Impact: 3.2)
  * `astToSQL` **(Defensive Guards)** (Impact: 3.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 8`, `args: 7`, `func_start: 4`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `import: 1`
* *Defense:* `safety: 11`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.173
  * `Choke Point (Betweenness):` 0.001715 | `Ripple Effect (Closeness):` 0.168926
  * `Imports (Out-Degree: 1):` union
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/lib/collate.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.063)
- **Top Global Matches:** file_cluster_10: 7.063, file_cluster_15: 7.645, file_cluster_2: 7.86
- **Magnitude:** 26.62 | **LOC:** 37 | **CtrlFlow:** 30.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **2**; blast radius 107.175; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (76.1%), Guard Balance (formerly Safety Score) (50.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `collateToSQL` **(Defensive Guards)** (Impact: 7.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 3`, `args: 3`, `func_start: 1`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* `import: 2`
* *Defense:* `safety: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 107.175
  * `Choke Point (Betweenness):` 0.008558 | `Ripple Effect (Closeness):` 0.345416
  * `Imports (Out-Degree: 2):` expr, util
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `package/lib/delete.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 8.234)
- **Top Global Matches:** file_cluster_7: 8.234, file_cluster_12: 9.12, file_cluster_5: 9.907
- **Magnitude:** 24.76 | **LOC:** 44 | **CtrlFlow:** 23.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 4.635; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (71.5%), Guard Balance (formerly Safety Score) (60.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `deleteToSQL` **(Defensive Guards)** (Impact: 6.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 17
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 2`, `args: 3`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 9`
* *Architecture:* `import: 6`
* *Defense:* `safety: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.635
  * `Choke Point (Betweenness):` 0.000395 | `Ripple Effect (Closeness):` 0.216288
  * `Imports (Out-Degree: 6):` column, expr, limit, tables, util, with
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/limit.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.462)
- **Top Global Matches:** file_cluster_15: 6.462, file_cluster_10: 7.851, file_cluster_11: 8.805
- **Magnitude:** 22.18 | **LOC:** 45 | **CtrlFlow:** 29.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **2**; blast radius 13.104; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (91.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (38.8%), Complexity Load (formerly Cognitive Load) (35.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `limitToSQL` **(Compute Cores)** (Impact: 5.9)
  * `limitOffsetToSQL` **(Defensive Guards)** (Impact: 4.6)
  * `composePrefixValSuffix` **(Parameter Forwarders)** (Impact: 3.0)
  * `fetchOffsetToSQL` **(Parameter Forwarders)** (Impact: 1.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 9`, `args: 6`, `func_start: 4`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `io: 3`, `import: 2`
* *Defense:* `safety: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.248848
  * `Imports (Out-Degree: 2):` expr, util
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `package/lib/case.js` (JAVASCRIPT) | Magnitude: 35.76 | Delta: **0.048** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 35, branch: 11, state_mutation: 9, safety: 8
- `package/lib/explain.js` (JAVASCRIPT) | Magnitude: 8.32 | Delta: **0.058** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 23, safety: 8, branch: 7, args: 3
- `package/lib/interval.js` (JAVASCRIPT) | Magnitude: 8.46 | Delta: **0.098** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 25, safety: 8, branch: 7, args: 3

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `package/lib/expr.js` -> **Severity: 28.554** (Bridge: 0.2856 * Flux: 99.9925%)
- `package/lib/union.js` -> **Severity: 12.239** (Bridge: 0.1224 * Flux: 99.9807%)
- `package/lib/column.js` -> **Severity: 4.584** (Bridge: 0.0458 * Flux: 100.0%)
- `package/lib/select.js` -> **Severity: 2.113** (Bridge: 0.0211 * Flux: 100.0%)
- `package/lib/util.js` -> **Severity: 1.974** (Bridge: 0.0197 * Flux: 99.998%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `package/lib/util.js` -> **Severity: 35.484** (Embedded: 0.609 * Error Risk: 58.2644%)
- `package/lib/expr.js` -> **Severity: 28.33** (Embedded: 0.526 * Error Risk: 53.8613%)
- `package/lib/column.js` -> **Severity: 25.112** (Embedded: 0.4133 * Error Risk: 60.7642%)
- `package/lib/tables.js` -> **Severity: 24.311** (Embedded: 0.3794 * Error Risk: 64.08%)
- `package/lib/select.js` -> **Severity: 20.645** (Embedded: 0.3127 * Error Risk: 66.012%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `package/lib/expr.js` -> **Severity: 14985.3** (Blast Radius: 149.853 * Doc Risk: 100.0%)
- `package/lib/util.js` -> **Severity: 14369.08** (Blast Radius: 163.285 * Doc Risk: 88.0%)
- `package/lib/collate.js` -> **Severity: 10717.5** (Blast Radius: 107.175 * Doc Risk: 100.0%)
- `package/lib/column.js` -> **Severity: 10693.196** (Blast Radius: 114.57 * Doc Risk: 93.3333%)
- `package/lib/tables.js` -> **Severity: 3622.216** (Blast Radius: 42.808 * Doc Risk: 84.6154%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 558 call pairs -- scoped 18.6%, unique 0.0%, ambiguous 0.0%, external 81.4%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| javascript | 558 | 18.6% | 0.0% | 0.0% | 81.4% |

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
