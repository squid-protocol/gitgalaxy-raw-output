# ARCHITECTURAL_BRIEF: mikro-orm
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/mikro-orm/mikro-orm.git` |
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
- **Scope:** 1710 analyzed artifact(s), 204254 LOC.
- **Load-bearing artifact:** `tests/helpers.ts` -- 213 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `packages/core/src/EntityManager.ts` -- pulls in 29 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `tests/features/entity-manager/EntityManager.sqlite.test.ts` at magnitude 3641.68 (structural weight, not risk).
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
| Total Artifacts | 2384 |
| Analyzed Artifacts (Scanned) | 1710 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 674 |
| Total LOC | 204254 |
| Volatility Index | 0.021 |
| % Scanned of codebase = | 71.7% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7131 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3489 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 13.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.5437 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 47 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 1557 | 201975 | 91.1% |
| JSON | 63 | 605 | 3.7% |
| MARKDOWN | 42 | 0 | 2.5% |
| PLAINTEXT | 22 | 0 | 1.3% |
| JAVASCRIPT | 15 | 628 | 0.9% |
| YAML | 7 | 722 | 0.4% |
| SQLITE | 2 | 185 | 0.1% |
| DB2_SQL | 1 | 40 | 0.1% |
| POSTGRESQL | 1 | 99 | 0.1% |

## 4.1 SOURCE ENCODINGS
All 1710 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 40%, State Mutators Files 14%, Data / Markup / Trivial 11%, Parameter Forwarders Files 7%, Callbacks & Closures Files 7%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 1646 | 96.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 64 | 3.7% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 674*

**Composition by Extension & Reason:**
- `.md`: 298x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 4853 LOC), 1x Excluded (Lexical Monotony: High structural repetition detected in 3532 LOC)
- `.snap`: 175x Excluded (Unsupported Extension: '.snap')
- `.html`: 36x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 31x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.svg`: 31x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 20x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.jpg`: 19x Excluded (Explicitly Denied Extension: '.jpg')
- `.ts`: 15x Unsupported Format (.undeterminable), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 12x Excluded (Explicitly Denied Extension: '.png')
- `.css`: 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.lock`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.lock')
- `.patch`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 98.8 | 21.3 | 9.2 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 80.4 | 43.2 | 49.5 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 1.3 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 4.3 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 8.7 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 72.9 | 100.0 | 100.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 8.5 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 64.6 | 0.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 1.0 | 0.5 | 0.3 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 83.4 | 11.3 | 11.4 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 43.3 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1920 | 265 | 2 | `packages/sql/src/AbstractSqlDriver.ts` |
| cleanup | 1477 | 1091 | 1 | `tests/features/table-per-type-inheritance/table-per-type-inheritance.test.ts` |
| guards | 5357 | 579 | 6 | `packages/sql/src/query/QueryBuilder.ts` |
| danger | 4924 | 533 | 6 | `packages/sql/src/AbstractSqlDriver.ts` |
| concurrency | 24481 | 1235 | 28 | `tests/features/entity-manager/EntityManager.postgre.test.ts` |
| connectivity | 3209 | 632 | 5 | `packages/core/src/typings.ts` |
| io | 2853 | 374 | 3 | `packages/sql/src/query/QueryBuilder.ts` |
| crypto | 9 | 9 | 0 | `tests/features/custom-types/GH6434.test.ts` |
| ipc | 9 | 5 | 0 | `tests/features/table-per-type-inheritance/table-per-type-inheritance.test.ts` |
| time | 712 | 195 | 1 | `tests/features/mikro-kysely-plugin.test.ts` |
| serialization | 92 | 49 | 0 | `packages/core/src/utils/DataloaderUtils.ts` |
| regex | 459 | 117 | 0 | `packages/sql/src/dialects/postgresql/PostgreSqlSchemaHelper.ts` |
| events | 2097 | 269 | 2 | `tests/features/entity-manager/EntityManager.mysql.test.ts` |
| tests | 29396 | 1106 | 39 | `tests/features/entity-manager/EntityManager.postgre.test.ts` |
| docs | 2451 | 290 | 2 | `packages/core/src/typings.ts` |
| debt | 398 | 124 | 0 | `tests/defineEntity.test.ts` |
| mutation | 39218 | 1448 | 47 | `tests/features/entity-manager/EntityManager.mysql.test.ts` |
| dead_code | 671 | 311 | 1 | `packages/core/src/utils/Utils.ts` |
| credential | 4 | 4 | 0 | `tests/Connection.test.ts` |
| threat | 0 | 0 | 0 | - |
| ml_ai | 191 | 49 | 0 | `tests/features/query-builder/query-builder-select.test.ts` |
| ui | 173 | 49 | 0 | `packages/core/src/EntityManager.ts` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **1.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `packages/sql/src/query/QueryBuilder.ts` (Hits: 102)
- `packages/sql/src/query/QueryBuilderHelper.ts` (Hits: 87)
- `packages/sql/src/AbstractSqlDriver.ts` (Hits: 75)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **helpers.ts** (`tests/helpers.ts`) — 213 inbound connections
2. **bootstrap.ts** (`tests/bootstrap.ts`) — 134 inbound connections
3. **Utils.ts** (`packages/core/src/utils/Utils.ts`) — 110 inbound connections
4. **typings.ts** (`packages/core/src/typings.ts`) — 89 inbound connections
5. **index.ts** (`tests/entities-sql/index.ts`) — 53 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **EntityManager.ts** (`packages/core/src/EntityManager.ts`) — 29 outbound dependencies
2. **Configuration.ts** (`packages/core/src/utils/Configuration.ts`) — 28 outbound dependencies
3. **typings.ts** (`packages/core/src/typings.ts`) — 26 outbound dependencies
4. **index.ts** (`packages/core/src/types/index.ts`) — 25 outbound dependencies
5. **bootstrap.ts** (`tests/bootstrap.ts`) — 24 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `isSimpleRegExp` **(Many-Argument Workhorses)** (@ `packages/sql/src/query/QueryBuilderHelper.ts`) -> Impact: **258.5** | LOC: 983
  * *Intent:* /** * Checks whether the RE can be rewritten to simple LIKE query */
- `getEntityHydrator` **(Many-Argument Workhorses)** (@ `packages/core/src/hydration/ObjectHydrator.ts`) -> Impact: **216.1** | LOC: 482
  * *Intent:* /** */
- `initCustomType` **(Many-Argument Workhorses)** (@ `packages/core/src/metadata/MetadataDiscovery.ts`) -> Impact: **207.5** | LOC: 169
- `nativeInsertMany` **(Many-Argument Workhorses)** (@ `packages/sql/src/AbstractSqlDriver.ts`) -> Impact: **182.1** | LOC: 199
- `convertException` **(Compute Cores)** (@ `packages/oracledb/src/OracleExceptionConverter.ts`) -> Impact: **175.2** | LOC: 138
  * *Intent:* /** */
- `nativeUpdateMany` **(Many-Argument Workhorses)** (@ `packages/sql/src/AbstractSqlDriver.ts`) -> Impact: **159.9** | LOC: 209
- `mapJoinedProps` **(Many-Argument Workhorses)** (@ `packages/sql/src/AbstractSqlDriver.ts`) -> Impact: **154.5** | LOC: 205
- `getFieldsForJoinedLoad` **(Many-Argument Workhorses)** (@ `packages/sql/src/AbstractSqlDriver.ts`) -> Impact: **150.6** | LOC: 211
- `findChildren` **(Many-Argument Workhorses)** (@ `packages/core/src/entity/EntityLoader.ts`) -> Impact: **141.8** | LOC: 190
- `assignProperty` **(Many-Argument Workhorses)** (@ `packages/core/src/entity/EntityAssigner.ts`) -> Impact: **140.9** | LOC: 124

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `tests/issues` | 400 | 42724.38 | 23.84% | 0.0% |
| `tests/features/entity-manager` | 7 | 15089.65 | 49.91% | 0.0% |
| `tests/features/schema-generator` | 89 | 11842.57 | 16.08% | 0.0% |
| `tests/features/embeddables` | 89 | 9924.11 | 25.01% | 0.0% |
| `tests` | 33 | 6022.85 | 13.31% | 0.0% |
| `tests/features` | 22 | 5165.68 | 23.97% | 0.0% |
| `packages/sql/src/query` | 11 | 4968.56 | 26.57% | 0.0% |
| `tests/features/polymorphic-relations` | 11 | 4825.15 | 36.04% | 0.0% |
| `tests/features/custom-types` | 46 | 4703.6 | 29.88% | 0.0% |
| `packages/core/src/utils` | 20 | 4289.58 | 35.75% | 17.1% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `packages/core/src/types/Type.ts` -> **99.9999%** Exposure
- `.github/ISSUE_TEMPLATE/bug_report.yml` -> **99.9993%** Exposure
- `.github/workflows/tests.yml` -> **99.9972%** Exposure
- `packages/core/src/entity/BaseEntity.ts` -> **99.9653%** Exposure
- `packages/core/src/cache/FileCacheAdapter.ts` -> **99.391%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `packages/core/src/hydration/ObjectHydrator.ts` -> **100.0%** Exposure
- `packages/core/src/logging/DefaultLogger.ts` -> **100.0%** Exposure
- `packages/core/src/metadata/MetadataDiscovery.ts` -> **100.0%** Exposure
- `packages/core/src/utils/AbstractMigrator.ts` -> **100.0%** Exposure
- `packages/core/src/utils/AbstractSchemaGenerator.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `packages/core/src/utils/Utils.ts` -> **39** Orphaned Functions | **0** Duplicates
- `tests/defineEntity.test.ts` -> **6** Orphaned Functions | **33** Duplicates
- `tests/features/decorators/legacy/decorators.test.ts` -> **4** Orphaned Functions | **16** Duplicates
- `tests/features/decorators/es/decorators.sqlite.test.ts` -> **3** Orphaned Functions | **16** Duplicates
- `.github/workflows/tests.yml` -> **0** Orphaned Functions | **16** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `tests/database/seeder/user.seeder.ts` -> **99.9995%** Exposure
- `tests/issues/GH1150.test.ts` -> **99.6651%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `3252` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `tests/features/entity-manager/EntityManager.sqlite.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.341)
- **Top Global Matches:** file_cluster_12: 7.341, file_cluster_7: 8.091, file_cluster_10: 8.459
- **Magnitude:** 3641.68 | **LOC:** 1813 | **CtrlFlow:** 1.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.246; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (50.0%), Guard Balance (formerly Safety Score) (41.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (19.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 178 instances
* *Amplified Cascading Flux:* 12 instances
* *Concurrency (weighted view):* 1277
* *State Mutation (weighted view):* 172
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 423`, `args: 98`, `func_start: 67`
* *Risk/State:* `safety_bypasses: 39`, `state_mutation: 148`, `dead_code: 1`
* *Architecture:* `io: 4`, `concurrency: 387`, `import: 8`
* *Defense:* `safety: 32`, `test: 497`, `sync_locks: 15`, `immutability_locks: 8`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.246
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` bootstrap.js, Author4.js, index.js, core, libsql, sql, sqlite, promises
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/sql/src/AbstractSqlDriver.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 13.771)
- **Top Global Matches:** file_cluster_6: 13.771, file_cluster_8: 16.677, file_cluster_4: 18.661
- **Magnitude:** 2908.38 | **LOC:** 3023 | **CtrlFlow:** 31.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **9**; blast radius 1.383; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Concurrency Surface (formerly Concurrency) (98.4%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (78.1%)
- **Documentation Coverage:** 70.3704% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `nativeInsertMany` **(Many-Argument Workhorses)** (Impact: 182.1)
  * `nativeUpdateMany` **(Many-Argument Workhorses)** (Impact: 159.9)
  * `mapJoinedProps` **(Many-Argument Workhorses)** (Impact: 154.5)
  * `getFieldsForJoinedLoad` **(Many-Argument Workhorses)** (Impact: 150.6)
  * `buildFields` **(Many-Argument Workhorses)** (Impact: 101.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 21 instances
* *Amplified Cascading Flux:* 190 instances
* *Concurrency (weighted view):* 186
* *State Mutation (weighted view):* 584
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 762`, `structural_boundaries: 497`, `args: 195`, `func_start: 68`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 222`, `state_mutation: 204`, `planned_debt: 1`
* *Architecture:* `io: 75`, `api: 12`, `concurrency: 81`, `import: 9`
* *Defense:* `safety: 112`, `doc: 22`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.383
  * `Choke Point (Betweenness):` 0.000298 | `Ripple Effect (Closeness):` 0.014395
  * `Imports (Out-Degree: 12):` AbstractSqlConnection.js, AbstractSqlPlatform.js, PivotCollectionPersister.js, SqlEntityManager.js, NativeQueryBuilder.js, QueryBuilder.js, enums.js, typings.js...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `tests/features/entity-manager/EntityManager.mssql.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 7.15)
- **Top Global Matches:** file_cluster_7: 7.15, file_cluster_12: 7.691, file_cluster_5: 9.037
- **Magnitude:** 2870.77 | **LOC:** 1608 | **CtrlFlow:** 0.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.246; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (50.0%), Guard Balance (formerly Safety Score) (43.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (19.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 162 instances
* *Amplified Cascading Flux:* 9 instances
* *Concurrency (weighted view):* 1119
* *State Mutation (weighted view):* 161
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 335`, `args: 82`, `func_start: 56`
* *Risk/State:* `safety_bypasses: 57`, `state_mutation: 143`
* *Architecture:* `io: 5`, `concurrency: 309`, `import: 5`
* *Defense:* `safety: 37`, `test: 435`, `sync_locks: 15`, `immutability_locks: 4`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.246
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` bootstrap.js, index.js, mssql, node:perf_hooks, uuid
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/features/entity-manager/EntityManager.mysql.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 8.416)
- **Top Global Matches:** file_cluster_7: 8.416, file_cluster_12: 8.657, file_cluster_5: 9.986
- **Magnitude:** 2406.0 | **LOC:** 3205 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.246; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (49.9%), Guard Balance (formerly Safety Score) (44.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (19.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `saveBook` **(Callbacks & Closures)** (Impact: 2.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 298 instances
* *Amplified Cascading Flux:* 9 instances
* *Concurrency (weighted view):* 2029
* *State Mutation (weighted view):* 319
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 612`, `args: 169`, `func_start: 104`
* *Risk/State:* `safety_bypasses: 117`, `state_mutation: 301`
* *Architecture:* `io: 8`, `concurrency: 539`, `import: 9`
* *Defense:* `safety: 54`, `test: 879`, `sync_locks: 25`, `immutability_locks: 5`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.246
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` bootstrap.js, index.js, Author2Subscriber.js, EverythingSubscriber.js, FlushSubscriber.js, Test2Subscriber.js, mysql, node:util...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/features/entity-manager/EntityManager.postgre.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.505)
- **Top Global Matches:** file_cluster_12: 8.505, file_cluster_7: 9.876, file_cluster_5: 9.939
- **Magnitude:** 2309.4 | **LOC:** 3100 | **CtrlFlow:** 1.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.246; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (49.9%), Guard Balance (formerly Safety Score) (42.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (26.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `saveUser` **(Generic / Templated Code)** (Impact: 3.4)
  * `createBooksWithTags` **(I/O & Config Routines)** (Impact: 2.0)
  * `afterFlush` **(Parameter Forwarders)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 276 instances
* *Amplified Cascading Flux:* 25 instances
* *Concurrency (weighted view):* 1947
* *State Mutation (weighted view):* 302
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 651`, `args: 192`, `func_start: 110`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 74`, `state_mutation: 252`, `dead_code: 2`
* *Architecture:* `io: 13`, `concurrency: 567`, `import: 8`
* *Defense:* `safety: 67`, `test: 819`, `sync_locks: 17`, `immutability_locks: 5`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.246
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` bootstrap.js, index.js, Test2Subscriber.js, knex-compat, postgresql, knex, node:perf_hooks, uuid
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/core/src/metadata/MetadataDiscovery.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.014)
- **Top Global Matches:** file_cluster_6: 8.014, file_cluster_4: 11.914, file_cluster_8: 16.124
- **Magnitude:** 2269.6 | **LOC:** 2429 | **CtrlFlow:** 30.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **18**; blast radius 0.668; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (74.0%), Complexity Load (formerly Cognitive Load) (74.0%)
- **Documentation Coverage:** 77.2152% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `initCustomType` **(Many-Argument Workhorses)** (Impact: 207.5)
  * `initEmbeddables` **(Many-Argument Workhorses)** (Impact: 78.3)
  * `initSingleTableInheritance` **(Many-Argument Workhorses)** (Impact: 57.5)
  * `initPolymorphicRelation` **(Many-Argument Workhorses)** (Impact: 49.1)
  * `definePivotTableEntity` **(Many-Argument Workhorses)** (Impact: 46.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 286 instances
* *Concurrency (weighted view):* 25
* *State Mutation (weighted view):* 926
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 587`, `structural_boundaries: 507`, `args: 205`, `func_start: 77`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 59`, `state_mutation: 354`
* *Architecture:* `io: 21`, `api: 4`, `concurrency: 10`, `import: 18`
* *Defense:* `safety: 115`, `doc: 16`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.668
  * `Choke Point (Betweenness):` 0.000727 | `Ripple Effect (Closeness):` 0.07205
  * `Imports (Out-Degree: 19):` BaseEntity.js, enums.js, errors.js, Logger.js, colors.js, NamingStrategy.js, Platform.js, index.js...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `tests/features/entity-manager/EntityManager.mongo.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 8.236)
- **Top Global Matches:** file_cluster_7: 8.236, file_cluster_12: 8.837, file_cluster_5: 9.834
- **Magnitude:** 2247.94 | **LOC:** 2598 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.246; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (50.0%), Guard Balance (formerly Safety Score) (47.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (27.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `failHandler` **(Parameter Forwarders)** (Impact: 1.5)
  * `failHandler` **(Callbacks & Closures)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 287 instances
* *Amplified Cascading Flux:* 7 instances
* *Concurrency (weighted view):* 1893
* *State Mutation (weighted view):* 308
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 511`, `args: 127`, `func_start: 99`
* *Risk/State:* `safety_bypasses: 120`, `state_mutation: 294`, `fragile_debt: 2`
* *Architecture:* `io: 2`, `concurrency: 458`, `import: 7`
* *Defense:* `safety: 19`, `test: 742`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.246
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` bootstrap.js, FooBar.js, FooBaz.js, index.js, AuthorRepository.js, legacy, mongodb
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/sql/src/query/QueryBuilder.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 11.095)
- **Top Global Matches:** file_cluster_5: 11.095, file_cluster_4: 12.74, file_cluster_12: 13.573
- **Magnitude:** 2172.0 | **LOC:** 4266 | **CtrlFlow:** 29.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **10**; blast radius 1.444; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (91.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (59.5%)
- **Documentation Coverage:** 44.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `prepareFields` **(Many-Argument Workhorses)** (Impact: 97.7)
  * `joinReference` **(Many-Argument Workhorses)** (Impact: 82.1)
  * `execute` **(Defensive Guards)** (Impact: 55.1)
    * *Intent:* /** * Executes this QB and returns the raw results, mapped to the property names (unless disabled vi...
  * `processReturningStatement` **(Many-Argument Workhorses)** (Impact: 47.4)
  * `resolveNestedPath` **(Defensive Guards)** (Impact: 44.2)
    * *Intent:* /** * Resolves nested paths like `a.books.title` to their actual field references. * Auto-joins rela...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 8 instances
* *Amplified Cascading Flux:* 118 instances
* *Concurrency (weighted view):* 83
* *State Mutation (weighted view):* 376
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 863`, `structural_boundaries: 963`, `args: 265`, `func_start: 177`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 208`, `state_mutation: 140`
* *Architecture:* `io: 102`, `api: 42`, `concurrency: 43`, `import: 10`
* *Defense:* `safety: 135`, `doc: 99`, `immutability_locks: 44`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.444
  * `Choke Point (Betweenness):` 0.00029 | `Ripple Effect (Closeness):` 0.015488
  * `Imports (Out-Degree: 14):` AbstractSqlConnection.js, AbstractSqlDriver.js, AbstractSqlPlatform.js, SqlEntityManager.js, typings.js, CriteriaNodeFactory.js, NativeQueryBuilder.js, QueryBuilderHelper.js...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `packages/core/src/EntityManager.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 9.716)
- **Top Global Matches:** file_cluster_5: 9.716, file_cluster_12: 12.104, file_cluster_4: 12.33
- **Magnitude:** 2048.94 | **LOC:** 2902 | **CtrlFlow:** 22.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **29** in-repo importer(s); it depends on **29**; blast radius 9.198; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.8%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (70.4%)
- **Documentation Coverage:** 9.2437% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `upsertMany` **(Many-Argument Workhorses)** (Impact: 130.8)
    * *Intent:* * * ```ts * const author = await em.upsertMany(Author, [ * ]); * ``` * * Depending on the driver sup...
  * `autoJoinRefsForFilters` **(Many-Argument Workhorses)** (Impact: 80.2)
    * *Intent:* /** * When filters are active on M:1 or 1:1 relations, we need to ref join them eagerly as they migh...
  * `upsert` **(Many-Argument Workhorses)** (Impact: 78.9)
    * *Intent:* * ``` * * The entity data needs to contain either the primary key, or any other unique property. Let...
  * `preparePopulate` **(Many-Argument Workhorses)** (Impact: 62.6)
  * `applyFilters` **(Many-Argument Workhorses)** (Impact: 37.4)
    * *Intent:* /** */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 57 instances
* *Amplified Cascading Flux:* 138 instances
* *Concurrency (weighted view):* 455
* *State Mutation (weighted view):* 446
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 452`, `structural_boundaries: 576`, `args: 145`, `func_start: 94`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 114`, `state_mutation: 170`
* *Architecture:* `api: 28`, `concurrency: 170`, `import: 29`
* *Defense:* `safety: 79`, `doc: 105`, `sync_locks: 3`, `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.198
  * `Choke Point (Betweenness):` 0.002705 | `Ripple Effect (Closeness):` 0.09616
  * `Imports (Out-Degree: 29):` CacheAdapter.js, Connection.js, IDatabaseDriver.js, EntityAssigner.js, EntityFactory.js, EntityLoader.js, EntityRepository.js, Reference.js...
  * `Imported By (In-Degree: 29):` (Excluded from Brief to save tokens)

### `tests/features/polymorphic-relations/polymorphic-loading-strategies.sqlite.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.632)
- **Top Global Matches:** file_cluster_10: 6.632, file_cluster_13: 7.723, file_cluster_12: 7.968
- **Magnitude:** 1554.95 | **LOC:** 748 | **CtrlFlow:** 2.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.246; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (46.8%), Guard Balance (formerly Safety Score) (40.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (11.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 33 instances
* *Concurrency (weighted view):* 247
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 139`, `args: 68`, `func_start: 25`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 21`
* *Architecture:* `io: 7`, `concurrency: 82`, `import: 2`
* *Defense:* `safety: 3`, `test: 143`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.246
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` legacy, sqlite
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/features/table-per-type-inheritance/table-per-type-inheritance.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 8.612)
- **Top Global Matches:** file_cluster_10: 8.612, file_cluster_12: 9.254, file_cluster_15: 9.572
- **Magnitude:** 1508.56 | **LOC:** 3455 | **CtrlFlow:** 3.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.246; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (60.0%), Complexity Load (formerly Cognitive Load) (48.5%), Guard Balance (formerly Safety Score) (43.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `onFlush` **(Compute Cores)** (Impact: 6.6)
  * `onFlush` **(Compute Cores)** (Impact: 5.0)
  * `onFlush` **(Type Conversions)** (Impact: 4.8)
  * `onFlush` **(Type Conversions)** (Impact: 4.8)
  * `onFlush` **(Type Conversions)** (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 171 instances
* *Amplified Cascading Flux:* 8 instances
* *Concurrency (weighted view):* 1302
* *State Mutation (weighted view):* 115
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 820`, `args: 222`, `func_start: 88`, `class_start: 130`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 99`, `duplicate_logic: 2`, `unreferenced_by_name: 3`
* *Architecture:* `io: 10`, `concurrency: 447`, `import: 7`
* *Defense:* `safety: 43`, `test: 426`, `immutability_locks: 1`, `cleanup: 58`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.246
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` bootstrap.js, core, legacy, mongodb, sqlite
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/features/read-replicas.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 8.06)
- **Top Global Matches:** file_cluster_10: 8.06, file_cluster_12: 8.348, file_cluster_13: 9.252
- **Magnitude:** 1442.52 | **LOC:** 310 | **CtrlFlow:** 8.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.246; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (50.0%), Guard Balance (formerly Safety Score) (39.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 41 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 271
* *State Mutation (weighted view):* 37
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 87`, `args: 22`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 33`
* *Architecture:* `io: 1`, `concurrency: 66`, `import: 8`
* *Defense:* `safety: 16`, `test: 76`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.246
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` bootstrap.js, index.js, Author2Subscriber.js, EverythingSubscriber.js, FlushSubscriber.js, Test2Subscriber.js, core, mysql
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/sql/src/query/QueryBuilderHelper.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.513)
- **Top Global Matches:** file_cluster_6: 8.513, file_cluster_8: 12.769, file_cluster_4: 14.932
- **Magnitude:** 1363.86 | **LOC:** 1525 | **CtrlFlow:** 24.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **6**; blast radius 0.357; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (71.7%), Guard Balance (formerly Safety Score) (61.1%)
- **Documentation Coverage:** 89.5833% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `isSimpleRegExp` **(Many-Argument Workhorses)** (Impact: 258.5)
    * *Intent:* /** * Checks whether the RE can be rewritten to simple LIKE query */
  * `mapper` **(Many-Argument Workhorses)** (Impact: 136.4)
  * `createJoinExpression` **(Many-Argument Workhorses)** (Impact: 84.0)
  * `processObjectSubCondition` **(Many-Argument Workhorses)** (Impact: 78.2)
  * `getQueryOrderFromObject` **(Many-Argument Workhorses)** (Impact: 42.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 92 instances
* *State Mutation (weighted view):* 297
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 302`, `structural_boundaries: 323`, `args: 107`, `func_start: 52`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 38`, `state_mutation: 113`
* *Architecture:* `io: 87`, `api: 17`, `import: 6`
* *Defense:* `safety: 65`, `doc: 5`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.357
  * `Choke Point (Betweenness):` 8e-06 | `Ripple Effect (Closeness):` 0.011681
  * `Imports (Out-Degree: 8):` AbstractSqlDriver.js, AbstractSqlPlatform.js, typings.js, NativeQueryBuilder.js, enums.js, core
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/core/src/unit-of-work/UnitOfWork.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 10.133)
- **Top Global Matches:** file_cluster_4: 10.133, file_cluster_5: 11.175, file_cluster_12: 12.182
- **Magnitude:** 1328.76 | **LOC:** 1677 | **CtrlFlow:** 30.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **23**; blast radius 1.035; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (98.5%), Guard Balance (formerly Safety Score) (64.5%), Complexity Load (formerly Cognitive Load) (61.1%)
- **Documentation Coverage:** 49.4253% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `remove` **(Many-Argument Workhorses)** (Impact: 35.8)
    * *Intent:* /** Marks an entity for removal, cascading to related entities. */
  * `register` **(Defensive Guards)** (Impact: 33.7)
    * *Intent:* /** */
  * `normalizeEntityData` **(Many-Argument Workhorses)** (Impact: 33.4)
    * *Intent:* /** * Entity data can wary in its shape, e.g. we might get a deep relation graph with joined strateg...
  * `getById` **(Many-Argument Workhorses)** (Impact: 33.2)
    * *Intent:* /** * Returns entity from the identity map. For composite keys, you need to pass an array of PKs in ...
  * `createTPTChangeSets` **(Many-Argument Workhorses)** (Impact: 32.7)
    * *Intent:* /** * For TPT inheritance, creates separate changesets for each table in the hierarchy. * Uses the s...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 8 instances
* *Amplified Cascading Flux:* 104 instances
* *Concurrency (weighted view):* 102
* *State Mutation (weighted view):* 331
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 392`, `structural_boundaries: 334`, `args: 102`, `func_start: 65`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 48`, `state_mutation: 123`, `planned_debt: 2`
* *Architecture:* `api: 21`, `concurrency: 62`, `import: 23`
* *Defense:* `safety: 42`, `doc: 29`, `sync_locks: 1`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.035
  * `Choke Point (Betweenness):` 0.000687 | `Ripple Effect (Closeness):` 0.071135
  * `Imports (Out-Degree: 23):` EntityManager.js, Connection.js, IDatabaseDriver.js, Collection.js, EntityHelper.js, EntityIdentifier.js, Reference.js, wrap.js...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `tests/features/entity-manager/EntityManager.mongo2.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 7.235)
- **Top Global Matches:** file_cluster_7: 7.235, file_cluster_12: 7.359, file_cluster_5: 9.252
- **Magnitude:** 1213.84 | **LOC:** 409 | **CtrlFlow:** 2.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.246; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (50.0%), Guard Balance (formerly Safety Score) (45.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (11.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 71 instances
* *Amplified Cascading Flux:* 6 instances
* *Concurrency (weighted view):* 473
* *State Mutation (weighted view):* 57
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 133`, `args: 31`, `func_start: 19`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 45`
* *Architecture:* `io: 1`, `concurrency: 118`, `import: 5`
* *Defense:* `safety: 13`, `test: 103`, `sync_locks: 10`, `immutability_locks: 3`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.246
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` bootstrap.js, FooBar.js, index.js, legacy, mongodb
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/EntityManager.oracledb.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.35)
- **Top Global Matches:** file_cluster_12: 8.35, file_cluster_7: 9.015, file_cluster_10: 9.886
- **Magnitude:** 1082.18 | **LOC:** 1410 | **CtrlFlow:** 0.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.246; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (50.0%), Guard Balance (formerly Safety Score) (41.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (11.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createBooksWithTags` **(I/O & Config Routines)** (Impact: 2.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 132 instances
* *Amplified Cascading Flux:* 5 instances
* *Concurrency (weighted view):* 942
* *State Mutation (weighted view):* 114
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 334`, `args: 93`, `func_start: 50`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 104`
* *Architecture:* `io: 17`, `concurrency: 282`, `import: 7`
* *Defense:* `safety: 36`, `test: 361`, `sync_locks: 16`, `immutability_locks: 4`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.246
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` bootstrap.js, index.js, Test2Subscriber.js, legacy, oracledb, node:perf_hooks, uuid
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/EntityManager.oracledb2.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.459)
- **Top Global Matches:** file_cluster_12: 8.459, file_cluster_5: 9.756, file_cluster_7: 9.764
- **Magnitude:** 1059.6 | **LOC:** 1541 | **CtrlFlow:** 1.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.246; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (50.0%), Guard Balance (formerly Safety Score) (42.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (11.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `saveUser` **(Generic / Templated Code)** (Impact: 3.4)
  * `createBooksWithTags` **(I/O & Config Routines)** (Impact: 2.0)
  * `constructor` **(State Mutators)** (Impact: 1.6)
  * `afterFlush` **(Parameter Forwarders)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 125 instances
* *Amplified Cascading Flux:* 6 instances
* *Concurrency (weighted view):* 875
* *State Mutation (weighted view):* 149
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 301`, `args: 89`, `func_start: 49`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 40`, `state_mutation: 137`, `unreferenced_by_name: 2`
* *Architecture:* `io: 12`, `concurrency: 250`, `import: 7`
* *Defense:* `safety: 29`, `test: 420`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.246
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` bootstrap.js, index.js, Test2Subscriber.js, legacy, oracledb, uuid
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/features/entity-generator/advanced-index-options.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.955)
- **Top Global Matches:** file_cluster_10: 4.955, file_cluster_13: 6.451, file_cluster_2: 6.722
- **Magnitude:** 1056.39 | **LOC:** 401 | **CtrlFlow:** 4.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.246; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (41.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (11.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (1.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 144`, `args: 21`, `func_start: 16`
* *Risk/State:* None
* *Architecture:* `io: 2`, `concurrency: 126`, `import: 11`
* *Defense:* `safety: 9`, `test: 40`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.246
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` legacy, entity-generator, mariadb, mssql, mysql, postgresql, sql
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/features/reflection/TsMorphMetadataProvider.sqlite.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.579)
- **Top Global Matches:** file_cluster_5: 7.579, file_cluster_12: 7.86, file_cluster_7: 9.003
- **Magnitude:** 1033.71 | **LOC:** 189 | **CtrlFlow:** 14.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **6**; blast radius 0.822; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (34.4%), Connectivity (formerly Api Exposure) (33.7%), Complexity Load (formerly Cognitive Load) (31.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 31
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 57`, `args: 12`, `func_start: 7`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 6`
* *Architecture:* `io: 14`, `api: 3`, `concurrency: 16`, `import: 7`
* *Defense:* `safety: 21`, `test: 42`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.822
  * `Choke Point (Betweenness):` 5e-06 | `Ripple Effect (Closeness):` 0.002389
  * `Imports (Out-Degree: 2):` FooBar.js, index.js, core, reflection, sqlite, node:url
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `packages/core/src/entity/EntityLoader.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 12.717)
- **Top Global Matches:** file_cluster_6: 12.717, file_cluster_8: 14.463, file_cluster_4: 18.596
- **Magnitude:** 1029.84 | **LOC:** 1207 | **CtrlFlow:** 29.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **15**; blast radius 3.395; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.7%), Mutation Surface (formerly State Flux) (99.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.6%)
- **Documentation Coverage:** 81.4815% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `findChildren` **(Many-Argument Workhorses)** (Impact: 141.8)
  * `populate` **(Many-Argument Workhorses)** (Impact: 64.8)
    * *Intent:* /** * Loads specified relations in batch. * This will execute one query for each relation, that will...
  * `populateField` **(Many-Argument Workhorses)** (Impact: 63.1)
  * `populateMany` **(Many-Argument Workhorses)** (Impact: 61.8)
    * *Intent:* /** * preload everything in one call (this will update already existing references in IM) */
  * `lookupEagerLoadedRelationships` **(Many-Argument Workhorses)** (Impact: 58.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 11 instances
* *Amplified Cascading Flux:* 65 instances
* *Concurrency (weighted view):* 96
* *State Mutation (weighted view):* 198
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 278`, `structural_boundaries: 238`, `args: 94`, `func_start: 27`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 56`, `state_mutation: 68`
* *Architecture:* `api: 2`, `concurrency: 41`, `import: 15`
* *Defense:* `safety: 34`, `doc: 23`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.395
  * `Choke Point (Betweenness):` 7.8e-05 | `Ripple Effect (Closeness):` 0.080732
  * `Imports (Out-Degree: 15):` EntityManager.js, IDatabaseDriver.js, enums.js, errors.js, Logger.js, MetadataStorage.js, Platform.js, typings.js...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `tests/features/transactions/transaction-propagation.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 8.49)
- **Top Global Matches:** file_cluster_10: 8.49, file_cluster_12: 8.493, file_cluster_7: 9.028
- **Magnitude:** 1004.36 | **LOC:** 1691 | **CtrlFlow:** 2.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.246; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (49.9%), Guard Balance (formerly Safety Score) (48.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (12.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `onCreate` **(Callbacks & Closures)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 98 instances
* *Amplified Cascading Flux:* 6 instances
* *Concurrency (weighted view):* 925
* *State Mutation (weighted view):* 52
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 523`, `args: 203`, `func_start: 67`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 38`, `state_mutation: 40`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `concurrency: 435`, `import: 4`
* *Defense:* `safety: 24`, `test: 172`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.246
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` bootstrap.js, helpers.js, core, legacy
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/features/transactions/transaction-propagation.mongo.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 8.519)
- **Top Global Matches:** file_cluster_10: 8.519, file_cluster_12: 8.559, file_cluster_7: 9.046
- **Magnitude:** 996.44 | **LOC:** 1646 | **CtrlFlow:** 0.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.246; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (49.9%), Guard Balance (formerly Safety Score) (48.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (12.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `onCreate` **(Callbacks & Closures)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 95 instances
* *Amplified Cascading Flux:* 7 instances
* *Concurrency (weighted view):* 917
* *State Mutation (weighted view):* 53
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 494`, `args: 198`, `func_start: 68`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 37`, `state_mutation: 39`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `concurrency: 442`, `import: 3`
* *Defense:* `safety: 18`, `test: 174`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.246
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` helpers.js, legacy, mongodb
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/sql/src/dialects/postgresql/PostgreSqlSchemaHelper.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.526)
- **Top Global Matches:** file_cluster_4: 5.526, file_cluster_6: 8.817, file_cluster_12: 12.583
- **Magnitude:** 965.68 | **LOC:** 1073 | **CtrlFlow:** 27.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **6**; blast radius 0.367; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (91.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.0%)
- **Documentation Coverage:** 93.6709% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getAllColumns` **(Many-Argument Workhorses)** (Impact: 98.0)
  * `createTableColumn` **(Compute Cores)** (Impact: 42.2)
  * `getAlterNativeEnumSQL` **(Many-Argument Workhorses)** (Impact: 35.5)
  * `getAllForeignKeys` **(Many-Argument Workhorses)** (Impact: 35.3)
  * `getPreAlterTable` **(Compute Cores)** (Impact: 33.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 75 instances
* *Concurrency (weighted view):* 48
* *State Mutation (weighted view):* 239
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 240`, `structural_boundaries: 182`, `args: 87`, `func_start: 50`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 89`
* *Architecture:* `io: 16`, `api: 31`, `concurrency: 33`, `import: 6`
* *Defense:* `safety: 30`, `doc: 5`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.367
  * `Choke Point (Betweenness):` 1.1e-05 | `Ripple Effect (Closeness):` 0.001625
  * `Imports (Out-Degree: 6):` AbstractSqlConnection.js, DatabaseSchema.js, DatabaseTable.js, SchemaHelper.js, typings.js, core
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `tests/features/query-builder/query-builder-fields-type.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.857)
- **Top Global Matches:** file_cluster_0: 7.857, file_cluster_10: 8.931, file_cluster_5: 9.697
- **Magnitude:** 958.41 | **LOC:** 394 | **CtrlFlow:** 3.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.246; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (42.9%), Complexity Load (formerly Cognitive Load) (15.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (11.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 172`, `args: 55`, `func_start: 26`
* *Risk/State:* `safety_bypasses: 3`
* *Architecture:* `io: 9`, `concurrency: 52`, `import: 5`
* *Defense:* `safety: 1`, `test: 53`, `immutability_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.246
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` bootstrap.js, index.js, mysql, sql, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/core/src/utils/EntityComparator.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 9.845)
- **Top Global Matches:** file_cluster_6: 9.845, file_cluster_4: 12.031, file_cluster_5: 16.566
- **Magnitude:** 951.6 | **LOC:** 1067 | **CtrlFlow:** 20.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **10**; blast radius 2.724; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (63.4%)
- **Documentation Coverage:** 41.4634% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getPropertySnapshot` **(Many-Argument Workhorses)** (Impact: 83.7)
  * `getEmbeddedPropertySnapshot` **(Many-Argument Workhorses)** (Impact: 56.3)
  * `getResultMapper` **(Compute Cores)** (Impact: 56.1)
    * *Intent:* /** */
  * `mapEntityProperties` **(Compute Cores)** (Impact: 48.0)
  * `getPropertyComparator` **(Many-Argument Workhorses)** (Impact: 37.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 129 instances
* *State Mutation (weighted view):* 435
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 174`, `structural_boundaries: 206`, `args: 85`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 38`, `state_mutation: 177`
* *Architecture:* `io: 16`, `api: 8`, `import: 10`
* *Defense:* `safety: 26`, `doc: 17`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.724
  * `Choke Point (Betweenness):` 0.000172 | `Ripple Effect (Closeness):` 0.081104
  * `Imports (Out-Degree: 10):` EntityIdentifier.js, PolymorphicRef.js, enums.js, Platform.js, JsonType.js, typings.js, Configuration.js, RawQueryFragment.js...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `tests/features/filters/GH6760.test.ts` (TYPESCRIPT) | Magnitude: 59.26 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 87, structural_boundaries: 39, decorators: 15, args: 11
- `tests/issues/GHx29.test.ts` (TYPESCRIPT) | Magnitude: 49.3 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 47, structural_boundaries: 18, decorators: 13, args: 9
- `tests/features/single-table-inheritance/GH4351.test.ts` (TYPESCRIPT) | Magnitude: 238.66 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 63, structural_boundaries: 28, decorators: 16, core_var_decl: 12
- `tests/issues/GH893.test.ts` (TYPESCRIPT) | Magnitude: 46.12 | Delta: **0.047** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 37, structural_boundaries: 20, args: 8, concurrency: 8
- `tests/entities-schema/FooBaz4.ts` (TYPESCRIPT) | Magnitude: 4.34 | Delta: **0.047** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: structural_boundaries: 7, indent_spaces: 7, api: 3, import: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `tests/issues/GH4755.test.ts` (TYPESCRIPT) | Magnitude: 198.25 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 44, structural_boundaries: 19, decorators: 15, branch: 5
- `tests/features/transactions/transaction-propagation.test.ts` (TYPESCRIPT) | Magnitude: 1004.36 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 1301, structural_boundaries: 523, concurrency: 435, core_var_decl: 353
- `tests/issues/GH302.test.ts` (TYPESCRIPT) | Magnitude: 47.12 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 50, structural_boundaries: 16, test: 10, decorators: 10
- `tests/features/embeddables/GH3134.test.ts` (TYPESCRIPT) | Magnitude: 51.38 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 49, structural_boundaries: 15, concurrency: 9, decorators: 9
- `tests/features/unit-of-work/GH4863.test.ts` (TYPESCRIPT) | Magnitude: 121.18 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 42, structural_boundaries: 19, concurrency: 13, decorators: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `tests/issues/GH2489.test.ts` (TYPESCRIPT) | Magnitude: 35.14 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 48, structural_boundaries: 19, args: 9, branch: 6
- `packages/core/src/types/EnumType.ts` (TYPESCRIPT) | Magnitude: 13.84 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 12, indent_spaces: 12, api: 4, branch: 3
- `tests/features/custom-types/GH6726.test.ts` (TYPESCRIPT) | Magnitude: 45.54 | Delta: **0.052** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 44, structural_boundaries: 22, decorators: 9, concurrency: 8
- `tests/issues/GH3429.test.ts` (TYPESCRIPT) | Magnitude: 26.26 | Delta: **0.109** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 42, structural_boundaries: 14, decorators: 11, concurrency: 7
- `packages/core/src/types/UnknownType.ts` (TYPESCRIPT) | Magnitude: 13.94 | Delta: **0.123** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 16, indent_spaces: 12, api: 5, args: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `tests/features/raw-queries/GHx6.test.ts` (TYPESCRIPT) | Magnitude: 341.39 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 166, structural_boundaries: 52, concurrency: 32, args: 31
- `tests/features/upsert/upsert.test.ts` (TYPESCRIPT) | Magnitude: 331.28 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 645, structural_boundaries: 180, concurrency: 143, test: 136
- `tests/issues/GH5559.test.ts` (TYPESCRIPT) | Magnitude: 221.2 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 91, structural_boundaries: 24, decorators: 15, concurrency: 12
- `tests/issues/GH1657.test.ts` (TYPESCRIPT) | Magnitude: 40.56 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 57, structural_boundaries: 17, args: 10, decorators: 10
- `tests/features/balanced-strategy.postgre.test.ts` (TYPESCRIPT) | Magnitude: 75.84 | Delta: **0.031** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 124, structural_boundaries: 31, core_var_decl: 25, design_snake_case: 25

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `tests/helpers.ts` (TYPESCRIPT) | Magnitude: 6.58 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 7, indent_spaces: 4, api: 3, test_skip: 3
- `tests/entities-sql/Label2.ts` (TYPESCRIPT) | Magnitude: 6.92 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 9, indent_spaces: 9, decorators: 6, import: 4
- `tests/features/dataloader/GH6031.test.ts` (TYPESCRIPT) | Magnitude: 49.5 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 35, structural_boundaries: 14, concurrency: 9, decorators: 9
- `tests/issues/GH4759.test.ts` (TYPESCRIPT) | Magnitude: 38.8 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 68, structural_boundaries: 18, decorators: 13, args: 9
- `tests/features/embeddables/GH2165.test.ts` (TYPESCRIPT) | Magnitude: 43.92 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 47, structural_boundaries: 15, decorators: 11, state_mutation: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `tests/features/reflection/entities-compiled/Author.js` (JAVASCRIPT) | Magnitude: 26.34 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 38, reflection_metaprogramming: 19, structural_boundaries: 15, branch: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `packages/sql/src/dialects/postgresql/BasePostgreSqlPlatform.ts` (TYPESCRIPT) | Magnitude: 226.3 | Delta: **0.072** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 390, structural_boundaries: 147, args: 63, branch: 60
- `tests/issues/GH6715.test.ts` (TYPESCRIPT) | Magnitude: 67.62 | Delta: **0.077** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 44, structural_boundaries: 24, concurrency: 11, args: 8
- `tests/features/query-builder/query-builder-pivot.test.ts` (TYPESCRIPT) | Magnitude: 33.3 | Delta: **0.088** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 414, listeners: 55, test: 45, core_var_decl: 28
- `tests/features/custom-types/GH6477.test.ts` (TYPESCRIPT) | Magnitude: 109.22 | Delta: **0.092** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 141, structural_boundaries: 62, test: 36, concurrency: 34
- `packages/core/src/types/Uint8ArrayType.ts` (TYPESCRIPT) | Magnitude: 18.28 | Delta: **0.13** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 17, api: 5, branch: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `packages/migrations-mongodb/src/index.ts` (TYPESCRIPT) | Magnitude: 22.16 | Delta: **0.105** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 9, api: 8, import: 8, doc: 1
- `packages/migrations/src/index.ts` (TYPESCRIPT) | Magnitude: 1.11 | Delta: **0.105** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 9, api: 8, import: 8, doc: 1
- `tests/entities-schema/index.ts` (TYPESCRIPT) | Magnitude: 23.68 | Delta: **0.157** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 9, api: 9, import: 9
- `tests/features/reflection/entities-compiled/index.d.ts` (TYPESCRIPT) | Magnitude: 1.18 | Delta: **0.157** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 9, api: 9, import: 9
- `tests/features/reflection/entities/index.ts` (TYPESCRIPT) | Magnitude: 23.68 | Delta: **0.157** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 9, api: 9, import: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `tests/features/entity-generator/AmbiguousFks.mysql.test.ts` (TYPESCRIPT) | Magnitude: 47.78 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 157, structural_boundaries: 16, core_var_decl: 15, state_mutation: 11
- `packages/core/src/metadata/index.ts` (TYPESCRIPT) | Magnitude: 19.12 | Delta: **0.055** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 7, api: 6, import: 6
- `packages/core/src/unit-of-work/index.ts` (TYPESCRIPT) | Magnitude: 19.12 | Delta: **0.075** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 6, api: 6, import: 6
- `packages/sql/src/dialects/sqlite/index.ts` (TYPESCRIPT) | Magnitude: 19.12 | Delta: **0.075** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 6, api: 6, import: 6
- `tests/entities/index.ts` (TYPESCRIPT) | Magnitude: 19.12 | Delta: **0.075** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 6, api: 6, import: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `tests/issues/GH755.test.ts` (TYPESCRIPT) | Magnitude: 35.92 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 9, test: 3, core_var_decl: 3
- `packages/core/src/types/TimeType.ts` (TYPESCRIPT) | Magnitude: 21.18 | Delta: **0.039** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 14, api: 6, args: 5
- `packages/core/src/utils/Cursor.ts` (TYPESCRIPT) | Magnitude: 125.66 | Delta: **0.069** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 146, structural_boundaries: 63, branch: 33, generics: 19
- `packages/core/src/utils/RequestContext.ts` (TYPESCRIPT) | Magnitude: 30.84 | Delta: **0.08** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 40, structural_boundaries: 17, core_var_decl: 10, args: 8
- `tests/issues/GH7436.test.ts` (TYPESCRIPT) | Magnitude: 272.4 | Delta: **0.11** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 109, structural_boundaries: 35, core_var_decl: 23, concurrency: 22

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `tests/issues/GH557.test.ts` (TYPESCRIPT) | Magnitude: 45.84 | Delta: **0.053** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 51, structural_boundaries: 14, decorators: 13, args: 7
- `tests/features/migrations/Migrator.mssql.test.ts` (TYPESCRIPT) | Magnitude: 16.57 | Delta: **0.055** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 388, structural_boundaries: 156, concurrency: 126, core_var_decl: 87
- `tests/features/migrations/Migrator.mongo.test.ts` (TYPESCRIPT) | Magnitude: 14.02 | Delta: **0.064** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 294, structural_boundaries: 150, concurrency: 117, core_var_decl: 69
- `tests/features/unit-of-work/GH4245.test.ts` (TYPESCRIPT) | Magnitude: 21.66 | Delta: **0.096** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 38, structural_boundaries: 15, test: 9, concurrency: 7
- `tests/features/custom-types/ArrayType.test.ts` (TYPESCRIPT) | Magnitude: 15.28 | Delta: **0.113** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: structural_boundaries: 12, indent_spaces: 10, test: 6, args: 3

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `packages/sql/src/AbstractSqlDriver.ts` -> Churn: **78.14%** | Cog Load: 69.1066% | Debt: 7.7329%
- `packages/core/src/metadata/MetadataDiscovery.ts` -> Churn: **74.01%** | Cog Load: 73.9776% | Debt: 0.0%
- `packages/sql/src/dialects/postgresql/PostgreSqlSchemaHelper.ts` -> Churn: **66.44%** | Cog Load: 76.0192% | Debt: 0.0%
- `packages/core/src/entity/EntityLoader.ts` -> Churn: **63.4%** | Cog Load: 55.8466% | Debt: 0.0%
- `packages/core/src/utils/EntityComparator.ts` -> Churn: **63.4%** | Cog Load: 58.7143% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `tests/features/entity-manager/EntityManager.sqlite.test.ts` -> **Martin Adámek** (100.0% isolated ownership) | Magnitude: 3641.68
- `packages/sql/src/AbstractSqlDriver.ts` -> **Martin Adámek** (100.0% isolated ownership) | Magnitude: 2908.38
- `tests/features/entity-manager/EntityManager.mssql.test.ts` -> **Martin Adámek** (100.0% isolated ownership) | Magnitude: 2870.77
- `tests/features/entity-manager/EntityManager.mysql.test.ts` -> **Martin Adámek** (100.0% isolated ownership) | Magnitude: 2406.0
- `tests/features/entity-manager/EntityManager.postgre.test.ts` -> **Martin Adámek** (100.0% isolated ownership) | Magnitude: 2309.4

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `packages/core/src/utils/Utils.ts` -> **Severity: 0.448** (Bridge: 0.0045 * Flux: 100.0%)
- `packages/core/src/MikroORM.ts` -> **Severity: 0.39** (Bridge: 0.0039 * Flux: 99.7332%)
- `packages/core/src/typings.ts` -> **Severity: 0.337** (Bridge: 0.0052 * Flux: 65.0994%)
- `packages/core/src/EntityManager.ts` -> **Severity: 0.27** (Bridge: 0.0027 * Flux: 99.8282%)
- `packages/core/src/platforms/Platform.ts` -> **Severity: 0.235** (Bridge: 0.0029 * Flux: 82.2493%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `packages/core/src/utils/Utils.ts` -> **Severity: 8.864** (Embedded: 0.1388 * Error Risk: 63.8475%)
- `tests/helpers.ts` -> **Severity: 7.264** (Embedded: 0.1432 * Error Risk: 50.7142%)
- `packages/core/src/utils/clone.ts` -> **Severity: 7.237** (Embedded: 0.0943 * Error Risk: 76.7428%)
- `packages/core/src/typings.ts` -> **Severity: 6.708** (Embedded: 0.111 * Error Risk: 60.4573%)
- `packages/core/src/entity/Reference.ts` -> **Severity: 6.639** (Embedded: 0.1017 * Error Risk: 65.2761%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `tests/helpers.ts` -> **Severity: 4373.3** (Blast Radius: 43.733 * Doc Risk: 100.0%)
- `packages/core/src/typings.ts` -> **Severity: 2215.488** (Blast Radius: 51.897 * Doc Risk: 42.6901%)
- `tests/bootstrap.ts` -> **Severity: 1646.0** (Blast Radius: 16.46 * Doc Risk: 100.0%)
- `packages/core/src/utils/Utils.ts` -> **Severity: 1533.055** (Blast Radius: 34.292 * Doc Risk: 44.7059%)
- `tests/entities-sql/Test2.ts` -> **Severity: 938.3** (Blast Radius: 9.383 * Doc Risk: 100.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 12705 call pairs -- scoped 36.0%, unique 0.0%, ambiguous 37.4%, external 26.6%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| typescript | 12676 | 36.0% | 0.0% | 37.4% | 26.5% |
| javascript | 29 | 3.4% | 0.0% | 37.9% | 58.6% |

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
