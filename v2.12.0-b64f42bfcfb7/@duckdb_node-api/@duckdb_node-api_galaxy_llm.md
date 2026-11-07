# ARCHITECTURAL_BRIEF: @duckdb_node-api
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
- **Scope:** 147 analyzed artifact(s), 8678 LOC.
- **Load-bearing artifact:** `package/lib/values/index.js` -- 25 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `package/lib/duckdb.d.ts` -- pulls in 33 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `package/lib/DuckDBVector.js` at magnitude 1764.4 (structural weight, not risk).
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
| Total Artifacts | 149 |
| Analyzed Artifacts (Scanned) | 147 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 2 |
| Total LOC | 8678 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 98.7% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.452 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3132 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 3.4% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.5484 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 11 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 73 | 7293 | 49.7% |
| TYPESCRIPT | 72 | 1385 | 49.0% |
| MARKDOWN | 1 | 0 | 0.7% |
| PLAINTEXT | 1 | 0 | 0.7% |

## 4.1 SOURCE ENCODINGS
All 147 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 28%, State Mutators Files 20%, Declarative / Non-Code 13%, Interface Declarations Files 9%, Parameter Forwarders Files 9%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 145 | 98.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 1.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 2*

**Composition by Extension & Reason:**
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ts`: 1x Excluded (Saturation: Line 2 exceeds 500 chars)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 99.2 | 17.2 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 78.8 | 26.6 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 33.6 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 11.5 | 2.4 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 26.4 | 9.1 | 3.5 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 9.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 36.7 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 11.2 | 0.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 79.7 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 65 | 7 | 0 | `package/lib/DuckDBVector.js` |
| cleanup | 0 | 0 | 0 | - |
| guards | 490 | 73 | 6 | `package/lib/DuckDBType.d.ts` |
| danger | 208 | 48 | 1 | `package/lib/DuckDBVector.js` |
| concurrency | 217 | 18 | 2 | `package/lib/DuckDBConnection.js` |
| connectivity | 1018 | 139 | 15 | `package/lib/DuckDBType.js` |
| io | 22 | 4 | 0 | `package/lib/DuckDBConnection.d.ts` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 10 | 5 | 0 | `package/lib/DuckDBValueConverters.js` |
| serialization | 1 | 1 | 0 | `package/lib/conversion/stringFromDecimal.js` |
| regex | 2 | 1 | 0 | `package/lib/conversion/dateTimeStringConversion.js` |
| events | 10 | 2 | 0 | `package/lib/values/DuckDBBitValue.js` |
| tests | 0 | 0 | 0 | - |
| docs | 42 | 16 | 1 | `package/lib/DuckDBResultReader.d.ts` |
| debt | 235 | 3 | 0 | `package/lib/DuckDBVector.js` |
| mutation | 1792 | 77 | 17 | `package/lib/DuckDBVector.js` |
| dead_code | 501 | 62 | 7 | `package/lib/DuckDBPreparedStatement.d.ts` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 0 | 0 | 0 | - |
| ui | 2 | 1 | 0 | `package/lib/DuckDBExtractedStatements.js` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `package/lib/DuckDBConnection.d.ts` (Hits: 18)
- `package/lib/DuckDBInstance.d.ts` (Hits: 2)
- `package/lib/DuckDBInstanceCache.d.ts` (Hits: 1)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **index.js** (`package/lib/values/index.js`) — 25 inbound connections
2. **DuckDBType.js** (`package/lib/DuckDBType.js`) — 20 inbound connections
3. **DuckDBDataChunk.js** (`package/lib/DuckDBDataChunk.js`) — 17 inbound connections
4. **DuckDBTypeId.js** (`package/lib/DuckDBTypeId.js`) — 14 inbound connections
5. **DuckDBValueConverter.js** (`package/lib/DuckDBValueConverter.js`) — 13 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **duckdb.d.ts** (`package/lib/duckdb.d.ts`) — 33 outbound dependencies
2. **duckdb.js** (`package/lib/duckdb.js`) — 33 outbound dependencies
3. **index.d.ts** (`package/lib/values/index.d.ts`) — 20 outbound dependencies
4. **index.js** (`package/lib/values/index.js`) — 20 outbound dependencies
5. **DuckDBValue.d.ts** (`package/lib/values/DuckDBValue.d.ts`) — 19 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `createValue` **(Defensive Guards)** (@ `package/lib/createValue.js`) -> Impact: **220.2** | LOC: 213
- `create` **(Many-Argument Workhorses)** (@ `package/lib/DuckDBVector.js`) -> Impact: **138.8** | LOC: 136
- `typeForValue` **(Defensive Guards)** (@ `package/lib/typeForValue.js`) -> Impact: **73.6** | LOC: 86
- `asType` **(Compute Cores)** (@ `package/lib/DuckDBLogicalType.js`) -> Impact: **46.2** | LOC: 85
- `create` **(Compute Cores)** (@ `package/lib/DuckDBLogicalType.js`) -> Impact: **26.5** | LOC: 20
- `getDuckDBIntervalString` **(Defensive Guards)** (@ `package/lib/conversion/dateTimeStringConversion.js`) -> Impact: **17.3** | LOC: 26
- `stringFromDecimal` **(Defensive Guards)** (@ `package/lib/conversion/stringFromDecimal.js`) -> Impact: **17.1** | LOC: 23
  * *Intent:* /** * Convert a scaled decimal value to a string, possibly using locale-specific formatting. */
- `setItemValid` **(Defensive Guards)** (@ `package/lib/DuckDBVector.js`) -> Impact: **17.0** | LOC: 28
- `flush` **(I/O & Config Routines)** (@ `package/lib/DuckDBVector.js`) -> Impact: **16.4** | LOC: 48
- `formatFractionalPart` **(Defensive Guards)** (@ `package/lib/conversion/stringFromDecimal.js`) -> Impact: **16.4** | LOC: 9
  * *Intent:* // Format the fractional part of a decimal value // Note that we must handle minimumFractionDigits and maximumFractionDigits ourselves, and that // we...

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `package/lib` | 93 | 5294.11 | 18.74% | 28.83% |
| `package/lib/values` | 42 | 549.99 | 14.0% | 44.71% |
| `package/lib/conversion` | 10 | 282.27 | 15.92% | 31.03% |
| `package` | 2 | 25.16 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `package/lib/DuckDBAppender.d.ts` -> **100.0%** Exposure
- `package/lib/DuckDBConnection.d.ts` -> **100.0%** Exposure
- `package/lib/DuckDBDataChunk.d.ts` -> **100.0%** Exposure
- `package/lib/DuckDBLogicalType.d.ts` -> **100.0%** Exposure
- `package/lib/DuckDBPreparedStatement.d.ts` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `package/lib/DuckDBTypeId.js` -> **100.0%** Exposure
- `package/lib/index.js` -> **100.0%** Exposure
- `package/lib/values/DuckDBBitValue.js` -> **100.0%** Exposure
- `package/lib/DuckDBDataChunk.js` -> **99.9999%** Exposure
- `package/lib/DuckDBPreparedStatementWeakRefCollection.js` -> **99.9994%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `package/lib/DuckDBVector.js` -> **0** Orphaned Functions | **146** Duplicates
- `package/lib/DuckDBType.d.ts` -> **10** Orphaned Functions | **84** Duplicates
- `package/lib/DuckDBPreparedStatement.d.ts` -> **58** Orphaned Functions | **0** Duplicates
- `package/lib/DuckDBAppender.d.ts` -> **44** Orphaned Functions | **0** Duplicates
- `package/lib/DuckDBResult.d.ts` -> **44** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `64` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `package/lib/DuckDBVector.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 10.803)
- **Top Global Matches:** file_cluster_12: 10.803, file_cluster_15: 11.887, file_cluster_11: 12.647
- **Magnitude:** 1764.4 | **LOC:** 2526 | **CtrlFlow:** 13.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **6**; blast radius 27.211; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Mutation Surface (formerly State Flux) (99.2%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (78.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `create` **(Many-Argument Workhorses)** (Impact: 138.8)
  * `setItemValid` **(Defensive Guards)** (Impact: 17.0)
  * `flush` **(I/O & Config Routines)** (Impact: 16.4)
  * `getBytesFromBigNum` **(Defensive Guards)** (Impact: 12.7)
  * `setItem` **(Defensive Guards)** (Impact: 11.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 79 instances
* *State Mutation (weighted view):* 449
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 334`, `structural_boundaries: 455`, `args: 380`, `func_start: 377`, `class_start: 42`
* *Risk/State:* `safety_bypasses: 42`, `state_mutation: 291`, `dead_code: 15`, `duplicate_logic: 146`
* *Architecture:* `api: 83`, `import: 6`
* *Defense:* `safety: 30`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 27.211
  * `Choke Point (Betweenness):` 0.020635 | `Ripple Effect (Closeness):` 0.101963
  * `Imports (Out-Degree: 23):` DuckDBLogicalType, DuckDBType, DuckDBTypeId, values, node-bindings, os
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `package/lib/DuckDBType.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.035)
- **Top Global Matches:** file_cluster_11: 6.035, file_cluster_15: 6.275, file_cluster_12: 8.237
- **Magnitude:** 748.0 | **LOC:** 931 | **CtrlFlow:** 7.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **20** in-repo importer(s); it depends on **5**; blast radius 28.828; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (61.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ENUM` **(Compute Cores)** (Impact: 12.8)
  * `DECIMAL` **(Defensive Guards)** (Impact: 8.4)
  * `constructor` **(Defensive Guards)** (Impact: 6.7)
  * `constructor` **(Defensive Guards)** (Impact: 6.7)
  * `constructor` **(Parameter Forwarders)** (Impact: 4.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 52 instances
* *State Mutation (weighted view):* 222
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 70`, `structural_boundaries: 270`, `args: 182`, `func_start: 177`, `class_start: 40`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 118`
* *Architecture:* `api: 163`, `import: 5`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 28.828
  * `Choke Point (Betweenness):` 0.005883 | `Ripple Effect (Closeness):` 0.174722
  * `Imports (Out-Degree: 4):` DuckDBLogicalType, DuckDBTypeId, sql, values, node-bindings
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `package/lib/DuckDBLogicalType.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.276)
- **Top Global Matches:** file_cluster_15: 7.276, file_cluster_11: 7.473, file_cluster_4: 7.71
- **Magnitude:** 288.36 | **LOC:** 329 | **CtrlFlow:** 31.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **3**; blast radius 15.926; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Connectivity (formerly Api Exposure) (82.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (60.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `asType` **(Compute Cores)** (Impact: 46.2)
  * `create` **(Compute Cores)** (Impact: 26.5)
  * `createStruct` **(Defensive Guards)** (Impact: 7.6)
  * `createUnion` **(Defensive Guards)** (Impact: 7.6)
  * `alias` **(State Mutators)** (Impact: 4.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 74
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 102`, `structural_boundaries: 108`, `args: 47`, `func_start: 46`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 30`
* *Architecture:* `api: 24`, `import: 3`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 15.926
  * `Choke Point (Betweenness):` 0.000914 | `Ripple Effect (Closeness):` 0.163899
  * `Imports (Out-Degree: 2):` DuckDBType, DuckDBTypeId, node-bindings
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `package/lib/DuckDBPreparedStatement.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.87)
- **Top Global Matches:** file_cluster_15: 6.87, file_cluster_11: 7.013, file_cluster_12: 7.711
- **Magnitude:** 270.78 | **LOC:** 220 | **CtrlFlow:** 24.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **10**; blast radius 15.322; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Concurrency Surface (formerly Concurrency) (99.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (50.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `bind` **(Defensive Guards)** (Impact: 14.6)
  * `bindValue` **(State Mutators)** (Impact: 6.2)
  * `bindArray` **(Defensive Guards)** (Impact: 4.2)
  * `bindList` **(Defensive Guards)** (Impact: 4.2)
  * `bindStruct` **(Defensive Guards)** (Impact: 4.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 10
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 37`, `args: 61`, `func_start: 60`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 4`
* *Architecture:* `api: 57`, `concurrency: 20`, `import: 10`
* *Defense:* `safety: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 15.322
  * `Choke Point (Betweenness):` 0.014649 | `Ripple Effect (Closeness):` 0.061021
  * `Imports (Out-Degree: 9):` DuckDBLogicalType, DuckDBMaterializedResult, DuckDBPendingResult, DuckDBResult, DuckDBResultReader, DuckDBType, createValue, typeForValue...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `package/lib/createValue.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 8.721)
- **Top Global Matches:** file_cluster_1: 8.721, file_cluster_3: 48.693, file_cluster_8: 70.379
- **Magnitude:** 228.64 | **LOC:** 223 | **CtrlFlow:** 55.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **3**; blast radius 5.779; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (31.3%), Complexity Load (formerly Cognitive Load) (31.0%), Connectivity (formerly Api Exposure) (15.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createValue` **(Defensive Guards)** (Impact: 220.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 124`, `structural_boundaries: 45`, `args: 8`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 1`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `safety: 58`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.779
  * `Choke Point (Betweenness):` 0.000413 | `Ripple Effect (Closeness):` 0.046143
  * `Imports (Out-Degree: 3):` DuckDBTypeId, values, node-bindings
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/lib/DuckDBConnection.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.25)
- **Top Global Matches:** file_cluster_15: 6.25, file_cluster_11: 7.291, file_cluster_12: 7.427
- **Magnitude:** 226.14 | **LOC:** 209 | **CtrlFlow:** 14.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **9**; blast radius 9.862; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (92.4%), Mutation Surface (formerly State Flux) (84.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 94.2308% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getTableNames` **(Compute Cores)** (Impact: 11.0)
  * `run` **(Defensive Guards)** (Impact: 8.8)
  * `createAppender` **(Defensive Guards)** (Impact: 8.2)
  * `runUntilLast` **(Defensive Guards)** (Impact: 5.0)
  * `stream` **(Defensive Guards)** (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 6 instances
* *Concurrency (weighted view):* 80
* *State Mutation (weighted view):* 21
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 71`, `args: 32`, `func_start: 31`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 9`
* *Architecture:* `api: 19`, `concurrency: 60`, `import: 9`
* *Defense:* `safety: 13`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.862
  * `Choke Point (Betweenness):` 0.011148 | `Ripple Effect (Closeness):` 0.039628
  * `Imports (Out-Degree: 8):` DuckDBAppender, DuckDBClientContext, DuckDBExtractedStatements, DuckDBInstance, DuckDBMaterializedResult, DuckDBPreparedStatement, DuckDBPreparedStatementWeakRefCollection, DuckDBResultReader...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `package/lib/DuckDBDataChunk.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.549)
- **Top Global Matches:** file_cluster_15: 5.549, file_cluster_12: 5.962, file_cluster_11: 6.783
- **Magnitude:** 214.56 | **LOC:** 224 | **CtrlFlow:** 16.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **17** in-repo importer(s); it depends on **2**; blast radius 24.963; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (80.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (67.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `appendToColumnsObject` **(Defensive Guards)** (Impact: 7.7)
  * `rowCount` **(State Mutators)** (Impact: 6.0)
  * `appendToRowObjects` **(Defensive Guards)** (Impact: 5.9)
  * `setColumnValues` **(Defensive Guards)** (Impact: 5.7)
  * `create` **(Compute Cores)** (Impact: 5.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 91
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 45`, `args: 41`, `func_start: 32`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 37`
* *Architecture:* `api: 15`, `import: 2`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 24.963
  * `Choke Point (Betweenness):` 0.015124 | `Ripple Effect (Closeness):` 0.134496
  * `Imports (Out-Degree: 1):` DuckDBVector, node-bindings
  * `Imported By (In-Degree: 17):` (Excluded from Brief to save tokens)

### `package/lib/DuckDBResult.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.401)
- **Top Global Matches:** file_cluster_11: 5.401, file_cluster_15: 6.165, file_cluster_12: 7.231
- **Magnitude:** 205.88 | **LOC:** 230 | **CtrlFlow:** 14.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **13**; blast radius 18.126; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.5%), Connectivity (formerly Api Exposure) (93.6%), Complexity Load (formerly Cognitive Load) (81.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `deduplicatedColumnNames` **(I/O & Config Routines)** (Impact: 5.8)
  * `fetchAllChunks` **(Defensive Guards)** (Impact: 4.5)
  * `fetchChunk` **(Interface Declarations)** (Impact: 3.2)
  * `yieldConvertedRows` **(Parameter Forwarders)** (Impact: 3.1)
  * `yieldConvertedRowObjects` **(Parameter Forwarders)** (Impact: 3.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 14 instances
* *Concurrency (weighted view):* 43
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 67`, `args: 44`, `func_start: 43`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 16`
* *Architecture:* `api: 29`, `concurrency: 38`, `import: 13`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 18.126
  * `Choke Point (Betweenness):` 0.010769 | `Ripple Effect (Closeness):` 0.088373
  * `Imports (Out-Degree: 12):` DuckDBDataChunk, DuckDBLogicalType, JSDuckDBValueConverter, JsonDuckDBValueConverter, convertColumnsFromChunks, convertColumnsObjectFromChunks, convertRowObjectsFromChunks, convertRowsFromChunks...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `package/lib/DuckDBAppender.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.394)
- **Top Global Matches:** file_cluster_15: 6.394, file_cluster_12: 6.632, file_cluster_11: 6.882
- **Magnitude:** 168.36 | **LOC:** 150 | **CtrlFlow:** 24.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **6**; blast radius 5.098; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (51.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `appendValue` **(State Mutators)** (Impact: 5.3)
  * `appendList` **(Defensive Guards)** (Impact: 3.6)
  * `appendStruct` **(Defensive Guards)** (Impact: 3.6)
  * `appendArray` **(Defensive Guards)** (Impact: 3.6)
  * `columnType` **(Parameter Forwarders)** (Impact: 3.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 7
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 5`, `args: 45`, `func_start: 44`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3`
* *Architecture:* `api: 45`, `import: 6`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.098
  * `Choke Point (Betweenness):` 0.003997 | `Ripple Effect (Closeness):` 0.038052
  * `Imports (Out-Degree: 5):` DuckDBLogicalType, DuckDBType, createValue, typeForValue, values, node-bindings
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `package/lib/conversion/dateTimeStringConversion.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.453)
- **Top Global Matches:** file_cluster_15: 5.453, file_cluster_2: 8.027, file_cluster_16: 8.122
- **Magnitude:** 167.58 | **LOC:** 239 | **CtrlFlow:** 11.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); blast radius 55.887; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Connectivity (formerly Api Exposure) (82.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (57.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getDuckDBIntervalString` **(Defensive Guards)** (Impact: 17.3)
  * `getAbsoluteOffsetStringFromParts` **(Defensive Guards)** (Impact: 12.8)
  * `getDuckDBTimestampStringFromMicroseconds` **(Defensive Guards)** (Impact: 9.8)
  * `getDuckDBDateStringFromDays` **(Compute Cores)** (Impact: 5.4)
  * `getTimezoneOffsetString` **(Type Conversions)** (Impact: 4.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 53
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 31`, `args: 21`, `func_start: 21`
* *Risk/State:* `state_mutation: 31`
* *Architecture:* `api: 20`
* *Defense:* `safety: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 55.887
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.144618
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `package/lib/DuckDBValueConverters.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.632)
- **Top Global Matches:** file_cluster_15: 6.632, file_cluster_2: 7.765, file_cluster_11: 8.001
- **Magnitude:** 165.96 | **LOC:** 215 | **CtrlFlow:** 17.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **2**; blast radius 7.173; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (94.6%), Connectivity (formerly Api Exposure) (80.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (44.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `objectFromStructValue` **(Defensive Guards)** (Impact: 8.5)
  * `objectArrayFromMapValue` **(Defensive Guards)** (Impact: 6.5)
  * `objectFromUnionValue` **(Defensive Guards)** (Impact: 6.5)
  * `arrayFromListValue` **(Defensive Guards)** (Impact: 6.3)
  * `arrayFromArrayValue` **(Defensive Guards)** (Impact: 6.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 28
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 28`, `args: 28`, `func_start: 25`
* *Risk/State:* `state_mutation: 26`
* *Architecture:* `api: 25`, `import: 2`
* *Defense:* `safety: 26`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.173
  * `Choke Point (Betweenness):` 0.005451 | `Ripple Effect (Closeness):` 0.063204
  * `Imports (Out-Degree: 3):` DuckDBType, values
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `package/lib/DuckDBResultReader.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.585)
- **Top Global Matches:** file_cluster_11: 5.585, file_cluster_15: 6.16, file_cluster_12: 6.936
- **Magnitude:** 137.82 | **LOC:** 204 | **CtrlFlow:** 6.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **10**; blast radius 10.048; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.8%), Connectivity (formerly Api Exposure) (95.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (55.9%)
- **Documentation Coverage:** 85.7143% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fetchChunks` **(Defensive Guards)** (Impact: 10.6)
  * `value` **(Defensive Guards)** (Impact: 8.2)
    * *Intent:* /** * Returns the value for the given column and row. Both are zero-indexed. * * Will return an erro...
  * `updateChunkSizeRuns` **(Defensive Guards)** (Impact: 5.1)
  * `constructor` **(State Mutators)** (Impact: 1.8)
  * `columnName` **(Parameter Forwarders)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 28
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 41`, `args: 39`, `func_start: 39`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 16`
* *Architecture:* `api: 33`, `concurrency: 4`, `import: 10`
* *Defense:* `safety: 3`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 10.048
  * `Choke Point (Betweenness):` 0.00739 | `Ripple Effect (Closeness):` 0.073973
  * `Imports (Out-Degree: 10):` JSDuckDBValueConverter, JsonDuckDBValueConverter, convertColumnsFromChunks, convertColumnsObjectFromChunks, convertRowObjectsFromChunks, convertRowsFromChunks, getColumnsFromChunks, getColumnsObjectFromChunks...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `package/lib/values/DuckDBBitValue.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.508)
- **Top Global Matches:** file_cluster_12: 6.508, file_cluster_15: 6.818, file_cluster_11: 7.3
- **Magnitude:** 103.52 | **LOC:** 104 | **CtrlFlow:** 13.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); blast radius 6.359; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (88.8%), Guard Balance (formerly Safety Score) (65.2%), Connectivity (formerly Api Exposure) (57.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fromLengthAndPredicate` **(Compute Cores)** (Impact: 10.2)
  * `bitValue` **(Defensive Guards)** (Impact: 9.2)
  * `toString` **(Type Conversions)** (Impact: 3.4)
  * `getBit` **(Parameter Forwarders)** (Impact: 3.0)
  * `toBools` **(Interface Declarations)** (Impact: 2.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 53
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 27`, `args: 17`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 21`
* *Architecture:* `api: 7`
* *Defense:* `safety: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 6.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.15259
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `package/lib/typeForValue.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 6.448)
- **Top Global Matches:** file_cluster_1: 6.448, file_cluster_3: 48.35, file_cluster_8: 70.149
- **Magnitude:** 80.42 | **LOC:** 92 | **CtrlFlow:** 52.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **2**; blast radius 5.779; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (39.4%), Mutation Surface (formerly State Flux) (34.5%), Guard Balance (formerly Safety Score) (32.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `typeForValue` **(Defensive Guards)** (Impact: 73.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 4
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 27`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `safety: 22`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.779
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.046143
  * `Imports (Out-Degree: 2):` DuckDBType, values
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/lib/DuckDBTypeId.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 5.783)
- **Top Global Matches:** file_cluster_12: 5.783, file_cluster_7: 6.505, file_cluster_2: 6.676
- **Magnitude:** 60.92 | **LOC:** 48 | **CtrlFlow:** 2.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **14** in-repo importer(s); blast radius 27.415; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (78.8%), Complexity Load (formerly Cognitive Load) (61.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 43
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 1`, `args: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 41`
* *Architecture:* `api: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 27.415
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.165753
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `package/lib/DuckDBScalarFunction.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.772)
- **Top Global Matches:** file_cluster_12: 6.772, file_cluster_10: 7.259, file_cluster_15: 7.952
- **Magnitude:** 57.06 | **LOC:** 84 | **CtrlFlow:** 26.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **5**; blast radius 4.05; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (87.4%), Guard Balance (formerly Safety Score) (55.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (46.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `create` **(Compute Cores)** (Impact: 12.7)
  * `setMainFunction` **(Callbacks & Closures)** (Impact: 3.2)
  * `setBindFunction` **(Callbacks & Closures)** (Impact: 3.1)
  * `setName` **(State Mutators)** (Impact: 3.0)
  * `setReturnType` **(State Mutators)** (Impact: 3.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 6`, `args: 15`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3`
* *Architecture:* `api: 4`, `import: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.05
  * `Choke Point (Betweenness):` 0.000157 | `Ripple Effect (Closeness):` 0.024462
  * `Imports (Out-Degree: 4):` DuckDBBindInfo, DuckDBDataChunk, DuckDBFunctionInfo, DuckDBVector, node-bindings
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/lib/DuckDBPendingResult.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.747)
- **Top Global Matches:** file_cluster_12: 6.747, file_cluster_15: 8.601, file_cluster_11: 8.937
- **Magnitude:** 54.88 | **LOC:** 61 | **CtrlFlow:** 30.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **4**; blast radius 5.866; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (98.9%), Mutation Surface (formerly State Flux) (98.8%), Connectivity (formerly Api Exposure) (75.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `runTask` **(Compute Cores)** (Impact: 12.8)
  * `runAllTasks` **(Defensive Guards)** (Impact: 2.2)
  * `getResult` **(Interface Declarations)** (Impact: 2.1)
  * `readUntil` **(Parameter Forwarders)** (Impact: 1.7)
  * `constructor` **(State Mutators)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 10
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 18`, `args: 9`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 6`
* *Architecture:* `api: 9`, `concurrency: 12`, `import: 4`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.866
  * `Choke Point (Betweenness):` 0.001512 | `Ripple Effect (Closeness):` 0.053134
  * `Imports (Out-Degree: 3):` DuckDBResultReader, createResult, sleep, node-bindings
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `package/lib/conversion/stringFromDecimal.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.489)
- **Top Global Matches:** file_cluster_15: 7.489, file_cluster_9: 8.175, file_cluster_16: 8.931
- **Magnitude:** 52.68 | **LOC:** 81 | **CtrlFlow:** 37.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 10.598; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (34.1%), Mutation Surface (formerly State Flux) (28.5%), Complexity Load (formerly Cognitive Load) (18.8%)
- **Documentation Coverage:** 80.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `stringFromDecimal` **(Defensive Guards)** (Impact: 17.1)
    * *Intent:* /** * Convert a scaled decimal value to a string, possibly using locale-specific formatting. */
  * `formatFractionalPart` **(Defensive Guards)** (Impact: 16.4)
    * *Intent:* // Format the fractional part of a decimal value // Note that we must handle minimumFractionDigits a...
  * `formatWholePart` **(Defensive Guards)** (Impact: 7.3)
    * *Intent:* // Helper function to format whole part of a decimal value. // Note that we explicitly omit 'minimum...
  * `getDecimalSeparator` **(Defensive Guards)** (Impact: 4.5)
    * *Intent:* /* * Get the decimal separator for a given locale. * Somewhat expensive, so use getCachedDecimalSepa...
  * `getCachedDecimalSeparator` **(Parameter Forwarders)** (Impact: 3.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 11`, `args: 6`, `func_start: 5`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `api: 1`
* *Defense:* `safety: 13`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.598
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.116305
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/conversion/stringFromBlob.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 6.454)
- **Top Global Matches:** file_cluster_9: 6.454, file_cluster_15: 8.717, file_cluster_16: 9.872
- **Magnitude:** 45.32 | **LOC:** 46 | **CtrlFlow:** 31.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 6.168; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (60.9%), Guard Balance (formerly Safety Score) (56.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 66.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `stringFromBlobStringConcat` **(Defensive Guards)** (Impact: 10.6)
  * `stringFromBlobArrayJoin` **(Defensive Guards)** (Impact: 10.6)
  * `stringFromBlob` **(Parameter Forwarders)** (Impact: 3.3)
    * *Intent:* /** Matches BLOB-to-VARCHAR conversion behavior of DuckDB. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 17
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 5`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 7`
* *Architecture:* `api: 3`
* *Defense:* `safety: 4`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 6.168
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.113536
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/lib/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.958)
- **Top Global Matches:** file_cluster_12: 8.958, file_cluster_10: 8.988, file_cluster_7: 9.778
- **Magnitude:** 34.92 | **LOC:** 42 | **CtrlFlow:** 68.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 3.465; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (99.2%), Guard Balance (formerly Safety Score) (65.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ownKeys` **(Callbacks & Closures)** (Impact: 6.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 17`, `args: 10`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 9`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.465
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` duckdb
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/lib/duckdb.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 22.127)
- **Top Global Matches:** file_cluster_12: 22.127, file_cluster_5: 22.437, file_cluster_10: 22.776
- **Magnitude:** 33.08 | **LOC:** 55 | **CtrlFlow:** 25.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **33**; blast radius 9.354; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Complexity Load (formerly Cognitive Load) (94.9%), Guard Balance (formerly Safety Score) (56.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 13
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 10`, `args: 8`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 5`
* *Architecture:* `api: 4`, `import: 33`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.354
  * `Choke Point (Betweenness):` 0.006708 | `Ripple Effect (Closeness):` 0.013699
  * `Imports (Out-Degree: 32):` DuckDBAppender, DuckDBBindInfo, DuckDBClientContext, DuckDBConnection, DuckDBDataChunk, DuckDBExtractedStatements, DuckDBFunctionInfo, DuckDBInstance...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/lib/values/DuckDBTimeTZValue.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.224)
- **Top Global Matches:** file_cluster_12: 6.224, file_cluster_11: 8.142, file_cluster_15: 8.333
- **Magnitude:** 33.04 | **LOC:** 66 | **CtrlFlow:** 11.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **2**; blast radius 6.359; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.5%), Connectivity (formerly Api Exposure) (66.7%), Guard Balance (formerly Safety Score) (58.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 83.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fromParts` **(Parameter Forwarders)** (Impact: 3.0)
  * `constructor` **(State Mutators)** (Impact: 2.2)
  * `toParts` **(Interface Declarations)** (Impact: 2.1)
  * `fromMicrosAndOffset` **(Type Conversions)** (Impact: 2.0)
  * `timeTZValue` **(Parameter Forwarders)** (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 10
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 9`, `args: 8`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 6`
* *Architecture:* `api: 8`, `import: 2`
* *Defense:* `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.359
  * `Choke Point (Betweenness):` 0.000274 | `Ripple Effect (Closeness):` 0.15259
  * `Imports (Out-Degree: 1):` dateTimeStringConversion, node-bindings
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `package/lib/values/DuckDBDecimalValue.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 5.924)
- **Top Global Matches:** file_cluster_12: 5.924, file_cluster_7: 7.692, file_cluster_11: 8.942
- **Magnitude:** 32.62 | **LOC:** 45 | **CtrlFlow:** 19.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **2**; blast radius 8.392; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Connectivity (formerly Api Exposure) (63.2%), Guard Balance (formerly Safety Score) (57.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 75.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `decimalValue` **(Defensive Guards)** (Impact: 4.3)
  * `fromDouble` **(Parameter Forwarders)** (Impact: 4.2)
  * `constructor` **(State Mutators)** (Impact: 2.2)
    * *Intent:* /** */
  * `toDouble` **(Interface Declarations)** (Impact: 2.1)
  * `toString` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 8`, `args: 6`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 6`
* *Architecture:* `api: 6`, `import: 2`
* *Defense:* `safety: 2`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 8.392
  * `Choke Point (Betweenness):` 0.00274 | `Ripple Effect (Closeness):` 0.157816
  * `Imports (Out-Degree: 1):` stringFromDecimal, node-bindings
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `package/lib/values/DuckDBTimestampValue.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 5.793)
- **Top Global Matches:** file_cluster_12: 5.793, file_cluster_7: 7.903, file_cluster_11: 8.375
- **Magnitude:** 31.82 | **LOC:** 42 | **CtrlFlow:** 19.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **3**; blast radius 9.062; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.2%), Connectivity (formerly Api Exposure) (77.4%), Guard Balance (formerly Safety Score) (55.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `timestampValue` **(Defensive Guards)** (Impact: 3.1)
  * `fromParts` **(Parameter Forwarders)** (Impact: 3.0)
  * `isFinite` **(Interface Declarations)** (Impact: 2.1)
  * `toParts` **(Interface Declarations)** (Impact: 2.1)
  * `constructor` **(State Mutators)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 9`, `args: 7`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 5`
* *Architecture:* `api: 9`, `import: 3`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.062
  * `Choke Point (Betweenness):` 0.000368 | `Ripple Effect (Closeness):` 0.156858
  * `Imports (Out-Degree: 2):` dateTimeStringConversion, DuckDBTimestampMillisecondsValue, node-bindings
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `package/lib/DuckDBInstance.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.054)
- **Top Global Matches:** file_cluster_12: 7.054, file_cluster_7: 7.901, file_cluster_5: 9.249
- **Magnitude:** 31.0 | **LOC:** 31 | **CtrlFlow:** 23.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **4**; blast radius 10.983; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (96.6%), Mutation Surface (formerly State Flux) (96.1%), Connectivity (formerly Api Exposure) (73.5%), Guard Balance (formerly Safety Score) (57.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `create` **(Parameter Forwarders)** (Impact: 3.7)
  * `connect` **(Interface Declarations)** (Impact: 2.1)
  * `closeSync` **(State Mutators)** (Impact: 2.1)
  * `fromCache` **(Parameter Forwarders)** (Impact: 1.9)
  * `constructor` **(State Mutators)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 7
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 8`, `args: 6`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3`
* *Architecture:* `api: 7`, `concurrency: 5`, `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 10.983
  * `Choke Point (Betweenness):` 0.006046 | `Ripple Effect (Closeness):` 0.046233
  * `Imports (Out-Degree: 3):` DuckDBConnection, DuckDBInstanceCache, createConfig, node-bindings
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `package/lib/createResult.js` (JAVASCRIPT) | Magnitude: 10.44 | Delta: **0.129** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: branch: 7, indent_spaces: 7, structural_boundaries: 4, core_var_decl: 4
- `package/lib/values/index.js` (JAVASCRIPT) | Magnitude: 27.72 | Delta: **0.199** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: import: 20, branch: 14, indent_spaces: 9, structural_boundaries: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `package/lib/index.js` (JAVASCRIPT) | Magnitude: 34.92 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: branch: 28, indent_spaces: 26, structural_boundaries: 17, core_var_decl: 11
- `package/lib/duckdb.js` (JAVASCRIPT) | Magnitude: 33.08 | Delta: **0.31** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: import: 33, branch: 14, structural_boundaries: 10, indent_spaces: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `package/lib/values/DuckDBUnionValue.d.ts` (TYPESCRIPT) | Magnitude: 0.34 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 6, indent_spaces: 4, args: 3, func_start: 3
- `package/lib/getColumnsFromChunks.d.ts` (TYPESCRIPT) | Magnitude: 0.13 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 4, import: 2, args: 1, func_start: 1
- `package/lib/getRowsFromChunks.d.ts` (TYPESCRIPT) | Magnitude: 0.13 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 4, import: 2, args: 1, func_start: 1
- `package/lib/values/DuckDBBlobValue.d.ts` (TYPESCRIPT) | Magnitude: 0.39 | Delta: **0.099** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: structural_boundaries: 5, args: 4, func_start: 4, indent_spaces: 4
- `package/lib/duckdb.d.ts` (TYPESCRIPT) | Magnitude: 2.43 | Delta: **0.207** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 33, api: 33, import: 33, io: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `package/lib/values/DuckDBUUIDValue.d.ts` (TYPESCRIPT) | Magnitude: 0.5 | Delta: **0.137** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 8, args: 6, func_start: 6, unreferenced_by_name: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `package/lib/values/DuckDBArrayValue.d.ts` (TYPESCRIPT) | Magnitude: 0.31 | Delta: **0.112** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 6, immutability_locks: 4, args: 3, func_start: 3
- `package/lib/values/DuckDBListValue.d.ts` (TYPESCRIPT) | Magnitude: 0.31 | Delta: **0.112** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 6, immutability_locks: 4, args: 3, func_start: 3
- `package/lib/values/DuckDBValue.d.ts` (TYPESCRIPT) | Magnitude: 0.82 | Delta: **0.151** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 21, import: 19, api: 1, core_var_decl: 1
- `package/lib/values/index.d.ts` (TYPESCRIPT) | Magnitude: 1.77 | Delta: **0.152** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 20, api: 20, import: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `package/lib/DuckDBMaterializedResult.js` (JAVASCRIPT) | Magnitude: 21.28 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 8, branch: 7, api: 6

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `package/lib/values/index.js` -> **Severity: 4.509** (Bridge: 0.0451 * Flux: 99.9254%)
- `package/lib/DuckDBVector.js` -> **Severity: 2.047** (Bridge: 0.0206 * Flux: 99.217%)
- `package/lib/DuckDBDataChunk.js` -> **Severity: 1.512** (Bridge: 0.0151 * Flux: 99.9999%)
- `package/lib/DuckDBResult.js` -> **Severity: 1.071** (Bridge: 0.0108 * Flux: 99.4961%)
- `package/lib/DuckDBConnection.js` -> **Severity: 0.936** (Bridge: 0.0111 * Flux: 83.9965%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `package/lib/DuckDBTypeId.js` -> **Severity: 13.065** (Embedded: 0.1658 * Error Risk: 78.8229%)
- `package/lib/DuckDBType.js` -> **Severity: 10.724** (Embedded: 0.1747 * Error Risk: 61.3763%)
- `package/lib/values/index.js` -> **Severity: 10.51** (Embedded: 0.1936 * Error Risk: 54.2752%)
- `package/lib/values/DuckDBBitValue.js` -> **Severity: 9.95** (Embedded: 0.1526 * Error Risk: 65.2058%)
- `package/lib/DuckDBLogicalType.js` -> **Severity: 9.889** (Embedded: 0.1639 * Error Risk: 60.3373%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `package/lib/conversion/dateTimeStringConversion.js` -> **Severity: 5588.7** (Blast Radius: 55.887 * Doc Risk: 100.0%)
- `package/lib/sql.js` -> **Severity: 3125.6** (Blast Radius: 31.256 * Doc Risk: 100.0%)
- `package/lib/DuckDBType.js` -> **Severity: 2882.8** (Blast Radius: 28.828 * Doc Risk: 100.0%)
- `package/lib/DuckDBVector.js` -> **Severity: 2721.1** (Blast Radius: 27.211 * Doc Risk: 100.0%)
- `package/lib/conversion/displayStringForDuckDBValue.js` -> **Severity: 2508.8** (Blast Radius: 25.088 * Doc Risk: 100.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 1353 call pairs -- scoped 52.6%, unique 0.0%, ambiguous 4.8%, external 42.6%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| javascript | 1351 | 52.7% | 0.0% | 4.8% | 42.5% |
| typescript | 2 | 0.0% | 0.0% | 0.0% | 100.0% |

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
