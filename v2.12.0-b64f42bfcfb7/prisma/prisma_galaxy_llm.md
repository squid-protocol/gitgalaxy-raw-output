# ARCHITECTURAL_BRIEF: prisma
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/prisma/prisma.git` |
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
- **Scope:** 3726 analyzed artifact(s), 206825 LOC.
- **Load-bearing artifact:** `packages/client/tests/functional/_utils/providers.ts` -- 346 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `packages/internals/src/index.ts` -- pulls in 74 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `.npmrc` at magnitude 5000.0 (structural weight, not risk).
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
| Total Artifacts | 4622 |
| Analyzed Artifacts (Scanned) | 3726 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 896 |
| Total LOC | 206825 |
| Volatility Index | 0.002 |
| % Scanned of codebase = | 80.6% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.8439 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1817 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 2.5% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 5.6223 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 354 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 2695 | 184460 | 72.3% |
| JSON | 236 | 1735 | 6.3% |
| PLAINTEXT | 189 | 8 | 5.1% |
| SQLITE | 177 | 536 | 4.8% |
| MARKDOWN | 159 | 0 | 4.3% |
| JAVASCRIPT | 121 | 2023 | 3.2% |
| YAML | 91 | 17492 | 2.4% |
| POSTGRESQL | 41 | 418 | 1.1% |
| SHELL | 6 | 87 | 0.2% |
| BATCH | 6 | 12 | 0.2% |
| DOCKERFILE | 4 | 48 | 0.1% |
| POWERSHELL | 1 | 6 | 0.0% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 3718 |
| unknown | unknown | 8 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 45%, Declarative / Non-Code 27%, Callbacks & Closures Files 6%, Parameter Forwarders Files 5%, Large Core Modules (2) 4%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 3378 | 90.7% |
| Unknown | 8 | 0.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 340 | 9.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 896*

**Composition by Extension & Reason:**
- `.prisma`: 381x Unsupported Format (.prisma), 127x Excluded (Unsupported Extension: '.prisma')
- `no_extension`: 143x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 19x Unsupported Format (.undeterminable)
- `.db`: 70x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Binary Format Detected), 1x Excluded (Unsupported Extension: '.db')
- `.snap`: 23x Unsupported Format (.snap), 8x Excluded (Unsupported Extension: '.snap'), 1x Excluded (Machine-Generated Source Code Signature: 1081 LOC)
- `.ts`: 26x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Saturation: Line 22 exceeds 500 chars), 1x Excluded (Machine-Generated Source Code Signature: 23 LOC)
- `.yaml`: 2x Excluded (Static Asset Blob without Intent: 1072 LOC), 1x Excluded (Static Asset Blob without Intent: 1264 LOC), 1x Excluded (Static Asset Blob without Intent: 2002 LOC)
- `.toml`: 18x Unsupported Format (.toml), 4x Excluded (Unsupported Extension: '.toml')
- `.md`: 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 3x Excluded (Explicitly Denied Extension: '.png')
- `.sql`: 1x Excluded (Static Asset Blob without Intent: 1032 LOC), 1x Excluded (Static Asset Blob without Intent: 1028 LOC), 1x Excluded (Static Asset Blob without Intent: 1026 LOC)
- `.lock`: 2x Unsupported Format (.lock)
- `.1c`: 2x Unsupported Format (.1c)
- `.so`: 2x Excluded (Explicitly Denied Extension: '.so')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 10.9 | 5.6 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 87.7 | 19.1 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 1.5 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 1.9 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 15.4 | 3.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 25.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 10.7 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 94.2 | 0.3 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 18.5 | 5.7 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 76.8 | 4.7 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 29.5 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1092 | 399 | 1 | `packages/client/src/__tests__/buffer-small.test.ts` |
| cleanup | 97 | 50 | 0 | `packages/adapter-pg/src/__tests__/pg.test.ts` |
| guards | 5265 | 855 | 3 | `packages/migrate/src/__tests__/DbExecute.test.ts` |
| danger | 2533 | 600 | 2 | `packages/client/src/__tests__/buffer-small.test.ts` |
| concurrency | 13697 | 977 | 9 | `packages/client/tests/functional/interactive-transactions/tests.ts` |
| connectivity | 5027 | 1952 | 3 | `packages/internals/src/index.ts` |
| io | 5558 | 635 | 3 | `packages/migrate/src/__tests__/DbExecute.test.ts` |
| crypto | 20 | 20 | 0 | `helpers/compile/plugins/fill-plugin/fillPlugin.ts` |
| ipc | 32 | 19 | 0 | `packages/client/tests/functional/_utils/setupTestSuiteMatrix.ts` |
| time | 458 | 186 | 0 | `packages/cli/src/bootstrap/Bootstrap.ts` |
| serialization | 337 | 137 | 0 | `packages/sqlcommenter-query-insights/src/parameterize/tests/security.test.ts` |
| regex | 551 | 187 | 0 | `packages/adapter-mariadb/src/errors.ts` |
| events | 889 | 245 | 0 | `packages/client/tests/functional/relationMode-in-separate-gh-action/tests_m-to-n.ts` |
| tests | 12530 | 662 | 6 | `packages/client/src/__tests__/buffer-small.test.ts` |
| docs | 1807 | 534 | 1 | `.github/workflows/test-template.yml` |
| debt | 1444 | 396 | 1 | `scripts/ci/publish.ts` |
| mutation | 23054 | 1988 | 14 | `packages/client/src/__tests__/buffer-small.test.ts` |
| dead_code | 452 | 230 | 0 | `packages/migrate/src/__tests__/__helpers__/captureStdout.ts` |
| credential | 28 | 17 | 0 | `.github/workflows/scripts/setup-mysql.sh` |
| threat | 17 | 7 | 0 | `packages/client/src/__tests__/buffer-small.test.ts` |
| ml_ai | 223 | 48 | 0 | `packages/client/src/__tests__/benchmarks/query-performance/seed-data.ts` |
| ui | 56 | 18 | 0 | `helpers/blaze/pipe.ts` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `packages/migrate/src/__tests__/DbExecute.test.ts` (Hits: 206)
- `packages/migrate/src/__tests__/MigrateDev.test.ts` (Hits: 184)
- `packages/config/src/__tests__/loadConfigFromFile.test.ts` (Hits: 159)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **providers.ts** (`packages/client/tests/functional/_utils/providers.ts`) — 346 inbound connections
2. **defineMatrix.ts** (`packages/client/tests/functional/_utils/defineMatrix.ts`) — 219 inbound connections
3. **idForProvider.ts** (`packages/client/tests/functional/_utils/idForProvider.ts`) — 184 inbound connections
4. **executeSteps.ts** (`packages/client/tests/e2e/_utils/executeSteps.ts`) — 89 inbound connections
5. **getTestClient.ts** (`packages/client/src/utils/getTestClient.ts`) — 69 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.ts** (`packages/internals/src/index.ts`) — 74 outbound dependencies
2. **getPrismaClient.ts** (`packages/client/src/runtime/getPrismaClient.ts`) — 43 outbound dependencies
3. **index.ts** (`packages/ts-builders/src/index.ts`) — 37 outbound dependencies
4. **bin.ts** (`packages/cli/src/bin.ts`) — 32 outbound dependencies
5. **Studio.ts** (`packages/cli/src/Studio.ts`) — 27 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `writeUIntLE` **(Many-Argument Workhorses)** (@ `helpers/compile/plugins/fill-plugin/fillers/buffer-small.ts`) -> Impact: **232.2** | LOC: 443
- `run` **(Many-Argument Workhorses)** (@ `packages/cli/src/bootstrap/Bootstrap.ts`) -> Impact: **220.7** | LOC: 392
- `getPrismaClient` **(Defensive Guards)** (@ `packages/client/src/runtime/getPrismaClient.ts`) -> Impact: **176.9** | LOC: 767
- `mapValue` **(Many-Argument Workhorses)** (@ `packages/client-engine-runtime/src/interpreter/data-mapper.ts`) -> Impact: **148.7** | LOC: 157
- `parse` **(Many-Argument Workhorses)** (@ `packages/cli/src/Init.ts`) -> Impact: **145.6** | LOC: 418
- `testIf` **(Callbacks & Closures)** (@ `packages/client/src/__tests__/buffer-small.test.ts`) -> Impact: **145.1** | LOC: 2194
- `mapDriverError` **(Compute Cores)** (@ `packages/adapter-mssql/src/errors.ts`) -> Impact: **135.8** | LOC: 170
- `parse` **(Many-Argument Workhorses)** (@ `packages/cli/src/Generate.ts`) -> Impact: **111.5** | LOC: 229
- `interpretNode` **(Many-Argument Workhorses)** (@ `packages/client-engine-runtime/src/interpreter/query-interpreter.ts`) -> Impact: **107.0** | LOC: 235
- `shouldSkipSuiteConfig` **(Many-Argument Workhorses)** (@ `packages/client/tests/functional/_utils/getTestSuitePlan.ts`) -> Impact: **106.0** | LOC: 111

*Function archetypes referenced above:*
  * **Callbacks & Closures**: built around closures/callbacks (handlers, async continuations)
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `packages/migrate/src/__tests__` | 20 | 7078.26 | 15.7% | 0.0% |
| `__monolith__` | 18 | 5166.08 | 0.28% | 0.0% |
| `packages/config/src/__tests__/fixtures/loadConfigFromFile/env-load-esm` | 2 | 5000.03 | 9.41% | 0.0% |
| `packages/config/src/__tests__/fixtures/loadConfigFromFile/env-load-cjs` | 2 | 5000.01 | 1.79% | 0.0% |
| `packages/client/fixtures/mongo/prisma` | 1 | 5000.0 | 0.0% | 0.0% |
| `packages/client/src/__tests__/integration/happy/browser/prisma` | 1 | 5000.0 | 0.0% | 0.0% |
| `packages/internals/src/__tests__/__fixtures__/dotenv` | 1 | 5000.0 | 0.0% | 0.0% |
| `packages/migrate/src/__tests__/fixtures/schema-only-cockroachdb/prisma` | 1 | 5000.0 | 0.0% | 0.0% |
| `packages/migrate/src/__tests__/fixtures/schema-only-postgresql/prisma` | 1 | 5000.0 | 0.0% | 0.0% |
| `packages/client/tests/functional/composites/object` | 14 | 3052.81 | 8.7% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `packages/type-benchmark-tests/lots-of-relations/client-options.bench.ts` -> **100.0%** Exposure
- `packages/type-benchmark-tests/basic/client-options.bench.ts` -> **99.9999%** Exposure
- `packages/ts-builders/src/Import.ts` -> **99.9636%** Exposure
- `packages/migrate/src/__tests__/__helpers__/captureStdout.ts` -> **99.9447%** Exposure
- `packages/client/src/runtime/core/model/applyModelsAndClientExtensions.ts` -> **99.1392%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `.github/workflows/scripts/detect-jobs-to-run.js` -> **100.0%** Exposure
- `packages/client/src/utils/compilerWorker.js` -> **100.0%** Exposure
- `packages/migrate/src/__tests__/fixtures/seed-from-prisma-config/seed-sqlite-js-extra-args/prisma/seed.js` -> **100.0%** Exposure
- `helpers/blaze/concat.ts` -> **100.0%** Exposure
- `helpers/blaze/map.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `packages/type-benchmark-tests/lots-of-relations/client-options.bench.ts` -> **0** Orphaned Functions | **22** Duplicates
- `packages/client/src/runtime/core/compositeProxy/createCompositeProxy.test.ts` -> **1** Orphaned Functions | **19** Duplicates
- `packages/client/tests/functional/extensions/query.ts` -> **1** Orphaned Functions | **17** Duplicates
- `packages/client/tests/functional/extensions/model.ts` -> **0** Orphaned Functions | **16** Duplicates
- `packages/client/src/runtime/core/extensions/applyResultExtensions.test.ts` -> **0** Orphaned Functions | **15** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `packages/adapter-mariadb/src/credentials.test.ts` -> **99.9995%** Exposure
- `packages/migrate/src/__tests__/fixtures/sqlite-d1/prisma.config.ts` -> **99.9954%** Exposure
- `packages/sqlcommenter-query-insights/src/parameterize/tests/security.test.ts` -> **23.958%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `14` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `3280` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.144
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/client/fixtures/mongo/prisma/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.144
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/client/src/__tests__/integration/happy/browser/prisma/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.144
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/config/src/__tests__/fixtures/loadConfigFromFile/env-load-cjs/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.144
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/config/src/__tests__/fixtures/loadConfigFromFile/env-load-esm/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.144
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/internals/src/__tests__/__fixtures__/dotenv/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.144
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/migrate/src/__tests__/fixtures/schema-only-cockroachdb/prisma/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.144
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/migrate/src/__tests__/fixtures/schema-only-postgresql/prisma/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.144
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/client/tests/functional/fluent-api/tests.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 5.998)
- **Top Global Matches:** file_cluster_0: 5.998, file_cluster_10: 6.524, file_cluster_2: 7.901
- **Magnitude:** 2584.51 | **LOC:** 764 | **CtrlFlow:** 5.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.144; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (39.5%), Complexity Load (formerly Cognitive Load) (26.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Concurrency (weighted view):* 90
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 113`, `args: 39`, `func_start: 26`
* *Risk/State:* `state_mutation: 2`, `planned_debt: 1`
* *Architecture:* `concurrency: 70`, `import: 4`
* *Defense:* `safety: 36`, `doc: 1`, `test: 74`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.144
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` _matrix, client, faker, expect-type
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/client/tests/functional/logging/tests.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.333)
- **Top Global Matches:** file_cluster_10: 5.333, file_cluster_2: 7.206, file_cluster_13: 7.406
- **Magnitude:** 2468.8 | **LOC:** 272 | **CtrlFlow:** 25.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.144; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (49.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 25 instances
* *Concurrency (weighted view):* 41
* *State Mutation (weighted view):* 76
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 35`, `args: 15`, `func_start: 4`
* *Risk/State:* `state_mutation: 26`
* *Architecture:* `io: 3`, `concurrency: 21`, `import: 5`
* *Defense:* `safety: 19`, `test: 42`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.144
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` providers, types, _matrix, client, faker
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/migrate/src/__tests__/MigrateDiff.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.435)
- **Top Global Matches:** file_cluster_10: 5.435, file_cluster_2: 7.514, file_cluster_12: 7.723
- **Magnitude:** 1942.02 | **LOC:** 927 | **CtrlFlow:** 0.8% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.144; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (52.0%), Complexity Load (formerly Cognitive Load) (50.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 123 instances
* *Amplified Cascading Flux:* 2 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 756
* *State Mutation (weighted view):* 182
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 177`, `args: 74`, `func_start: 39`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 2`, `state_mutation: 178`
* *Architecture:* `io: 29`, `concurrency: 141`, `import: 11`
* *Defense:* `safety: 22`, `test: 125`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.144
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` MigrateDiff, setupCockroach, setupMSSQL, setupMysql, setupPostgres, conditionalTests, context, promises...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/client/tests/functional/0-legacy-ports/query-raw/tests.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 5.772)
- **Top Global Matches:** file_cluster_7: 5.772, file_cluster_12: 6.173, file_cluster_5: 8.412
- **Magnitude:** 1279.91 | **LOC:** 307 | **CtrlFlow:** 8.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.144; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (58.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 16 instances
* *Amplified Cascading Flux:* 13 instances
* *Concurrency (weighted view):* 109
* *State Mutation (weighted view):* 42
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 44`, `args: 16`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 16`, `planned_debt: 2`
* *Architecture:* `io: 3`, `concurrency: 29`, `import: 4`
* *Defense:* `test: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.144
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` providers, _matrix, client, copycat
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/client/src/__tests__/buffer-small.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.365)
- **Top Global Matches:** file_cluster_4: 9.365, file_cluster_12: 11.001, file_cluster_10: 12.32
- **Magnitude:** 1095.14 | **LOC:** 6236 | **CtrlFlow:** 2.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.144; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.8%), Guard Balance (formerly Safety Score) (52.0%), Complexity Load (formerly Cognitive Load) (14.5%), Dead Code Surface (formerly Dead Code) (7.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testIf` **(Callbacks & Closures)** (Impact: 145.1)
  * `writeToFill` **(Many-Argument Workhorses)** (Impact: 35.4)
    * *Intent:* // This is mostly accurate. Except write() won't write partial bytes to the // string while fill() b...
  * `testBufs` **(Many-Argument Workhorses)** (Impact: 9.4)
  * `receiver` **(Compute Cores)** (Impact: 5.3)
    * *Intent:* // eslint-disable-next-line no-inner-declarations
  * `deepStrictEqualValues` **(State Mutators)** (Impact: 3.7)
    * *Intent:* // Buffer
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 194 instances
* *State Mutation (weighted view):* 787
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 127`, `structural_boundaries: 690`, `args: 662`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 108`, `state_mutation: 399`, `dead_code: 1`, `fragile_debt: 5`, `unreferenced_by_name: 2`
* *Architecture:* `import: 6`
* *Defense:* `safety: 61`, `doc: 3`, `test: 803`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.144
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` buffer-small, assert, buffer, crypto
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/migrate/src/__tests__/DbExecute.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.585)
- **Top Global Matches:** file_cluster_10: 7.585, file_cluster_12: 8.701, file_cluster_7: 10.383
- **Magnitude:** 1077.38 | **LOC:** 966 | **CtrlFlow:** 1.2% | **Authorship Centralization:** 60.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.144; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (97.1%), Complexity Load (formerly Cognitive Load) (50.0%), Guard Balance (formerly Safety Score) (39.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testIf` **(Callbacks & Closures)** (Impact: 3.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 152 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 946
* *State Mutation (weighted view):* 113
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 228`, `args: 89`, `func_start: 55`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 111`, `planned_debt: 2`
* *Architecture:* `io: 206`, `concurrency: 186`, `import: 12`
* *Defense:* `safety: 91`, `test: 136`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.144
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` DbExecute, setupCockroach, setupMSSQL, setupMysql, setupPostgres, conditionalTests, context, node:child_process...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `helpers/compile/plugins/fill-plugin/fillers/buffer-small.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.484)
- **Top Global Matches:** file_cluster_4: 7.484, file_cluster_12: 9.426, file_cluster_15: 11.309
- **Magnitude:** 832.32 | **LOC:** 707 | **CtrlFlow:** 23.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 0.266; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (97.4%), Guard Balance (formerly Safety Score) (65.2%), Connectivity (formerly Api Exposure) (52.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `writeUIntLE` **(Many-Argument Workhorses)** (Impact: 232.2)
  * `indexOf` **(Many-Argument Workhorses)** (Impact: 46.1)
  * `toString` **(Compute Cores)** (Impact: 39.7)
  * `write` **(Defensive Guards)** (Impact: 29.9)
  * `stringToBuffer` **(Compute Cores)** (Impact: 29.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 60 instances
* *State Mutation (weighted view):* 185
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 135`, `structural_boundaries: 111`, `args: 141`, `func_start: 59`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 65`, `planned_debt: 1`
* *Architecture:* `api: 19`, `import: 3`
* *Defense:* `safety: 17`, `doc: 1`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000268
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `scripts/ci/publish.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.182)
- **Top Global Matches:** file_cluster_4: 8.182, file_cluster_12: 8.995, file_cluster_15: 10.065
- **Magnitude:** 828.52 | **LOC:** 982 | **CtrlFlow:** 20.1% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 0.144; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (85.7%), Debt Markers (formerly Tech Debt) (74.4%)
- **Documentation Coverage:** 82.6087% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `publishPackages` **(Many-Argument Workhorses)** (Impact: 50.9)
  * `publish` **(I/O & Config Routines)** (Impact: 50.8)
    * *Intent:* // TODO: name this to main
  * `run` **(Many-Argument Workhorses)** (Impact: 14.7)
    * *Intent:* /** * Runs a command and pipes the stdout & stderr to the current process. */
  * `getCurrentPatchForPatchVersions` **(Callbacks & Closures)** (Impact: 14.2)
    * *Intent:* // This function gets the current "patchMajorMinor" (major and minor of the patch branch), // and fi...
  * `getAllVersionsPublishedFor` **(Compute Cores)** (Impact: 14.0)
    * *Intent:* /** */
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 37 instances
* *Amplified Cascading Flux:* 70 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 282
* *State Mutation (weighted view):* 220
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 148`, `structural_boundaries: 182`, `args: 74`, `func_start: 46`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 1`, `state_mutation: 80`, `planned_debt: 15`, `duplicate_logic: 4`
* *Architecture:* `io: 34`, `api: 4`, `concurrency: 97`, `import: 12`
* *Defense:* `safety: 18`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.144
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` package.json, slugify, webhook, arg, batching-toposort, execa, globby, colors...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/client/tests/functional/0-legacy-ports/batch-find-unique/tests.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.748)
- **Top Global Matches:** file_cluster_10: 4.748, file_cluster_13: 4.779, file_cluster_2: 5.722
- **Magnitude:** 752.02 | **LOC:** 175 | **CtrlFlow:** 15.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.144; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (67.1%), Guard Balance (formerly Safety Score) (48.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (12.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 32
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 29`, `args: 6`, `func_start: 1`
* *Risk/State:* `state_mutation: 2`, `planned_debt: 1`
* *Architecture:* `concurrency: 12`, `import: 7`
* *Defense:* `safety: 1`, `test: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.144
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` providers, waitFor, types, _matrix, client, internals, copycat
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/client/tests/functional/0-legacy-ports/execute-raw/tests.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.497)
- **Top Global Matches:** file_cluster_10: 4.497, file_cluster_13: 4.97, file_cluster_2: 5.445
- **Magnitude:** 748.96 | **LOC:** 240 | **CtrlFlow:** 5.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.144; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (54.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 21 instances
* *Amplified Cascading Flux:* 11 instances
* *Concurrency (weighted view):* 132
* *State Mutation (weighted view):* 38
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 42`, `args: 12`, `func_start: 5`
* *Risk/State:* `state_mutation: 16`
* *Architecture:* `io: 3`, `concurrency: 27`, `import: 4`
* *Defense:* `test: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.144
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` providers, _matrix, client, copycat
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/client/tests/functional/issues/11233/tests.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.598)
- **Top Global Matches:** file_cluster_12: 6.598, file_cluster_7: 7.692, file_cluster_10: 8.107
- **Magnitude:** 742.8 | **LOC:** 109 | **CtrlFlow:** 35.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.144; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (45.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 4 instances
* *Concurrency (weighted view):* 24
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 20`, `args: 3`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 4`, `planned_debt: 2`
* *Architecture:* `io: 2`, `concurrency: 4`, `import: 3`
* *Defense:* `safety: 6`, `test: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.144
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` providers, _matrix, client
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/migrate/src/__tests__/DbPush.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.993)
- **Top Global Matches:** file_cluster_10: 6.993, file_cluster_12: 7.801, file_cluster_2: 9.17
- **Magnitude:** 720.38 | **LOC:** 447 | **CtrlFlow:** 0.9% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.144; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (62.7%), Complexity Load (formerly Cognitive Load) (50.0%), Guard Balance (formerly Safety Score) (38.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 37 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 263
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 100`, `args: 42`, `func_start: 20`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 2`, `state_mutation: 24`
* *Architecture:* `io: 43`, `concurrency: 78`, `import: 7`
* *Defense:* `safety: 26`, `test: 68`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.144
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` DbPush, setupMongo, setupPostgres, conditionalTests, context, path, prompts
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/migrate/src/__tests__/MigrateDev.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.902)
- **Top Global Matches:** file_cluster_10: 6.902, file_cluster_12: 8.948, file_cluster_15: 9.212
- **Magnitude:** 698.78 | **LOC:** 1795 | **CtrlFlow:** 2.1% | **Authorship Centralization:** 61.5%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 0.144; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (49.0%), Guard Balance (formerly Safety Score) (37.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (36.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `clearPromptInjection` **(Compute Cores)** (Impact: 6.3)
    * *Intent:* // Sanity check to ensure no prompt injections remain enqueued between // test cases. Having those w...
  * `testIf` **(Callbacks & Closures)** (Impact: 3.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 77 instances
* *Amplified Cascading Flux:* 1 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 614
* *State Mutation (weighted view):* 52
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 270`, `args: 94`, `func_start: 59`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 2`, `state_mutation: 50`, `planned_debt: 3`
* *Architecture:* `io: 184`, `concurrency: 229`, `import: 13`
* *Defense:* `safety: 80`, `test: 225`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.144
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` DbExecute, MigrateDev, MigrateReset, setupCockroach, setupMSSQL, setupMysql, setupPostgres, conditionalTests...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/cli/src/bootstrap/Bootstrap.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.563)
- **Top Global Matches:** file_cluster_4: 6.563, file_cluster_6: 9.726, file_cluster_16: 12.437
- **Magnitude:** 693.72 | **LOC:** 630 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **19**; blast radius 0.211; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (96.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 83.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run` **(Many-Argument Workhorses)** (Impact: 220.7)
  * `parse` **(Many-Argument Workhorses)** (Impact: 26.6)
  * `runInit` **(Many-Argument Workhorses)** (Impact: 19.0)
  * `scaffoldTemplate` **(Stateful Encapsulated Methods)** (Impact: 11.5)
  * `manualInstallAndReturn` **(Defensive Guards)** (Impact: 5.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 32 instances
* *Amplified Cascading Flux:* 47 instances
* *Concurrency (weighted view):* 217
* *State Mutation (weighted view):* 161
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 102`, `structural_boundaries: 105`, `args: 10`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `state_mutation: 67`
* *Architecture:* `io: 24`, `api: 4`, `concurrency: 57`, `import: 22`
* *Defense:* `safety: 35`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.211
  * `Choke Point (Betweenness):` 5e-06 | `Ripple Effect (Closeness):` 0.000614
  * `Imports (Out-Degree: 9):` Generate, Init, Link, local-setup, management-api, completion-output, project-state, telemetry...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/client/tests/functional/composites/object/upsert-update.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.026)
- **Top Global Matches:** file_cluster_12: 6.026, file_cluster_7: 7.121, file_cluster_5: 7.44
- **Magnitude:** 682.34 | **LOC:** 644 | **CtrlFlow:** 1.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.144; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (97.9%), Guard Balance (formerly Safety Score) (50.7%), Complexity Load (formerly Cognitive Load) (12.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Concurrency (weighted view):* 45
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 43`, `args: 18`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 1`, `planned_debt: 1`
* *Architecture:* `io: 1`, `concurrency: 35`, `import: 3`
* *Defense:* `doc: 2`, `test: 34`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.144
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` _matrix, client, faker
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/client/tests/functional/composites/object/update.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.178)
- **Top Global Matches:** file_cluster_12: 6.178, file_cluster_7: 6.95, file_cluster_5: 7.204
- **Magnitude:** 680.94 | **LOC:** 569 | **CtrlFlow:** 1.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.144; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.0%), Guard Balance (formerly Safety Score) (50.8%), Complexity Load (formerly Cognitive Load) (14.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Concurrency (weighted view):* 45
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 43`, `args: 18`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 1`, `planned_debt: 1`
* *Architecture:* `io: 1`, `concurrency: 35`, `import: 3`
* *Defense:* `test: 34`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.144
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` _matrix, client, faker
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/client/tests/functional/composites/object/updateMany.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 3.851)
- **Top Global Matches:** file_cluster_10: 3.851, file_cluster_2: 5.353, file_cluster_13: 6.292
- **Magnitude:** 676.34 | **LOC:** 339 | **CtrlFlow:** 3.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.144; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (44.7%), Complexity Load (formerly Cognitive Load) (29.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Concurrency (weighted view):* 45
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 43`, `args: 18`, `func_start: 14`
* *Risk/State:* `state_mutation: 1`, `planned_debt: 1`
* *Architecture:* `io: 1`, `concurrency: 35`, `import: 3`
* *Defense:* `test: 34`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.144
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` _matrix, client, faker
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `packages/client/tests/functional/extensions/client.ts` (TYPESCRIPT) | Magnitude: 29.42 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 264, structural_boundaries: 81, test: 42, args: 37
- `packages/client/tests/functional/extensions/itx.ts` (TYPESCRIPT) | Magnitude: 65.2 | Delta: **0.058** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 259, structural_boundaries: 81, concurrency: 42, args: 30
- `packages/client/tests/e2e/accelerate-types/src/index.ts` (TYPESCRIPT) | Magnitude: 5.4 | Delta: **0.063** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 8, concurrency: 3, import: 3
- `packages/client/tests/functional/fluent-api-null/tests.ts` (TYPESCRIPT) | Magnitude: 423.24 | Delta: **0.076** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 480, structural_boundaries: 145, concurrency: 96, test: 94
- `packages/client/src/runtime/utils/fromEntries.ts` (TYPESCRIPT) | Magnitude: 3.96 | Delta: **0.081** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 5, structural_boundaries: 4, args: 2, func_start: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `packages/client/src/__tests__/integration/happy/modify-client/test.ts` (TYPESCRIPT) | Magnitude: 163.06 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 71, structural_boundaries: 34, concurrency: 15, test: 13
- `packages/client/src/runtime/utils/createErrorMessageWithContext.test.ts` (TYPESCRIPT) | Magnitude: 13.36 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 314, test: 41, structural_boundaries: 32, args: 27
- `packages/client/tests/functional/_utils/setupTestSuiteClient.ts` (TYPESCRIPT) | Magnitude: 154.96 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 237, structural_boundaries: 61, import: 35, io: 31
- `packages/driver-adapter-utils/src/binder.ts` (TYPESCRIPT) | Magnitude: 76.26 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 121, structural_boundaries: 59, core_var_decl: 24, args: 22
- `packages/client/src/__tests__/integration/happy/referentialActions-onDelete-cascade-mysql/test.ts` (TYPESCRIPT) | Magnitude: 123.52 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 51, structural_boundaries: 22, concurrency: 17, test: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `packages/instrumentation-contract/src/global.ts` (TYPESCRIPT) | Magnitude: 13.26 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 11, core_var_decl: 8, branch: 5
- `packages/client/src/runtime/core/errors/PrismaClientError.ts` (TYPESCRIPT) | Magnitude: 13.46 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 14, api: 8, structural_boundaries: 6, branch: 2
- `sandbox/driver-adapters/src/test.ts` (TYPESCRIPT) | Magnitude: 108.48 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 211, concurrency: 72, structural_boundaries: 66, debug_prints: 20
- `packages/client/src/runtime/core/errorRendering/FormattedString.ts` (TYPESCRIPT) | Magnitude: 17.58 | Delta: **0.089** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 12, args: 7, api: 6
- `packages/client/tests/e2e/prisma-client-mutually-exclusive-options/src/accelerate-adapter.ts` (TYPESCRIPT) | Magnitude: 4.16 | Delta: **0.124** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 8, import: 4, core_var_decl: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `packages/client/src/__tests__/integration/happy/scalar-list/test.ts` (TYPESCRIPT) | Magnitude: 74.38 | Delta: **0.075** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 84, structural_boundaries: 21, concurrency: 18, core_var_decl: 9
- `packages/cli/src/utils/nps/status.ts` (TYPESCRIPT) | Magnitude: 18.96 | Delta: **0.103** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 15, branch: 6, concurrency: 5
- `packages/fetch-engine/src/downloadZip.ts` (TYPESCRIPT) | Magnitude: 69.96 | Delta: **0.104** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 104, structural_boundaries: 43, core_var_decl: 22, concurrency: 21
- `packages/client/src/__tests__/integration/errors/referentialActions-onDelete-default-foreign-key-error-postgresql/test.ts` (TYPESCRIPT) | Magnitude: 123.52 | Delta: **0.106** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 51, structural_boundaries: 20, concurrency: 15, state_mutation: 5
- `packages/internals/src/panic.ts` (TYPESCRIPT) | Magnitude: 39.3 | Delta: **0.14** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 13, api: 12, core_var_decl: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `packages/client/tests/functional/driver-adapters/validate-active-provider/tests.ts` (TYPESCRIPT) | Magnitude: 134.16 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 70, structural_boundaries: 24, import: 12, decorators: 11
- `packages/client/tests/functional/default-selection/prisma/_schema.ts` (TYPESCRIPT) | Magnitude: 1.85 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 43, structural_boundaries: 9, branch: 8, state_mutation: 8
- `packages/client/tests/functional/issues/15264-uint-id-overflow/prisma/_schema.ts` (TYPESCRIPT) | Magnitude: 1.11 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 4, state_mutation: 2, decorators: 2
- `packages/client/tests/e2e/nextjs-schema-not-found/11_monorepo-noServerComponents-noCustomOutput-reExportIndirect/packages/db/index.js` (JAVASCRIPT) | Magnitude: 15.64 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: decorators: 2, import: 2, core_var_decl: 2, design_snake_case: 2
- `packages/client/tests/e2e/nextjs-schema-not-found/12_monorepo-serverComponents-noCustomOutput-reExportIndirect/packages/db/index.js` (JAVASCRIPT) | Magnitude: 15.64 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: decorators: 2, import: 2, core_var_decl: 2, design_snake_case: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `packages/migrate/src/__tests__/fixtures/introspection/mysql/setup.sql` (SQLITE) | Magnitude: 0.01 | Delta: **0.067** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 23, safety_bypasses: 6, class_start: 3, safety: 3
- `packages/cli/src/utils/simpleDebounce.ts` (TYPESCRIPT) | Magnitude: 36.44 | Delta: **0.07** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 9, core_var_decl: 6, args: 4
- `packages/client/src/runtime/core/types/exported/Public.ts` (TYPESCRIPT) | Magnitude: 22.38 | Delta: **0.097** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: structural_boundaries: 23, generics: 10, indent_spaces: 9, api: 6
- `packages/get-platform/src/logger.ts` (TYPESCRIPT) | Magnitude: 10.7 | Delta: **0.164** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 6, indent_spaces: 6, api: 4, args: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `packages/migrate/src/utils/printIntrospectedSchema.ts` (TYPESCRIPT) | Magnitude: 0.5 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 9, structural_boundaries: 6, io: 6, import: 3
- `packages/cli/src/bootstrap/telemetry.ts` (TYPESCRIPT) | Magnitude: 77.34 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 64, structural_boundaries: 36, branch: 25, safety: 22
- `packages/migrate/src/utils/setupMysql.ts` (TYPESCRIPT) | Magnitude: 29.36 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 45, structural_boundaries: 18, io: 15, concurrency: 12
- `scripts/check-engines-override.ts` (TYPESCRIPT) | Magnitude: 11.98 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 9, branch: 4, io: 3, core_var_decl: 3
- `packages/client-generator-ts/src/utils/wasm.ts` (TYPESCRIPT) | Magnitude: 103.76 | Delta: **0.031** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 85, structural_boundaries: 51, core_var_decl: 22, design_camel_case: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `packages/client-generator-ts/src/TSClient/Enum.ts` (TYPESCRIPT) | Magnitude: 17.26 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: structural_boundaries: 24, indent_spaces: 19, args: 6, func_start: 5
- `packages/adapter-pg/src/pg.ts` (TYPESCRIPT) | Magnitude: 234.6 | Delta: **0.141** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 231, structural_boundaries: 92, concurrency: 47, branch: 46
- `packages/client-generator-ts/src/TSClient/TSClient.ts` (TYPESCRIPT) | Magnitude: 13.62 | Delta: **0.222** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 40, structural_boundaries: 30, import: 16, args: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `packages/client/src/runtime/core/types/index.ts` (TYPESCRIPT) | Magnitude: 22.24 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 14, api: 7, import: 7, explicit_casts: 5
- `packages/client-runtime-utils/src/errors/index.ts` (TYPESCRIPT) | Magnitude: 20.64 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 7, api: 7, import: 7
- `packages/sqlcommenter/src/index.ts` (TYPESCRIPT) | Magnitude: 22.46 | Delta: **0.057** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 20, doc: 15, immutability_locks: 11, indent_spaces: 11
- `packages/internals/src/built-in-provider.ts` (TYPESCRIPT) | Magnitude: 13.08 | Delta: **0.06** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 2, structural_boundaries: 1, api: 1, doc: 1
- `packages/ts-builders/src/index.ts` (TYPESCRIPT) | Magnitude: 52.74 | Delta: **0.08** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 37, api: 37, import: 37

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `packages/client-engine-runtime/src/events.ts` (TYPESCRIPT) | Magnitude: 14.12 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 4, structural_boundaries: 3, api: 1, immutability_locks: 1
- `packages/migrate/src/__tests__/fixtures/seed-from-prisma-config/seed-sqlite-js-extra-args/prisma.config.ts` (TYPESCRIPT) | Magnitude: 0.02 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 7, structural_boundaries: 2, state_mutation: 2, import: 2
- `packages/client-engine-runtime/src/parameterization/parameterize-tests/tagged-values.test.ts` (TYPESCRIPT) | Magnitude: 16.82 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 84, structural_boundaries: 13, core_var_decl: 7, test: 5
- `packages/instrumentation-contract/helpers/build.ts` (TYPESCRIPT) | Magnitude: 15.24 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 7, structural_boundaries: 3, safety: 1, decorators: 1
- `packages/migrate/src/__tests__/fixtures/seed-from-prisma-config/seed-sqlite-js/prisma.config.ts` (TYPESCRIPT) | Magnitude: 0.02 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 7, structural_boundaries: 2, branch: 1, api: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `packages/client-generator-ts/src/TSClient/PrismaClient.ts` (TYPESCRIPT) | Magnitude: 83.3 | Delta: **0.039** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 241, structural_boundaries: 77, generics: 29, core_var_decl: 23
- `packages/client/tests/functional/too-many-instances-of-prisma-client/tests.ts` (TYPESCRIPT) | Magnitude: 20.18 | Delta: **0.106** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 11, args: 5, closures: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `packages/adapter-mariadb/src/mariadb.test.ts` (TYPESCRIPT) | Magnitude: 92.05 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 78, structural_boundaries: 23, args: 14, test: 13
- `packages/client/tests/functional/extensions/pdp.ts` (TYPESCRIPT) | Magnitude: 143.04 | Delta: **0.059** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 353, structural_boundaries: 109, args: 53, safety_bypasses: 41
- `packages/client/src/__tests__/integration/errors/connection-limit-mysql/test.ts` (TYPESCRIPT) | Magnitude: 31.8 | Delta: **0.085** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 9, concurrency: 6, args: 5
- `packages/adapter-neon/src/__tests__/neon.test.ts` (TYPESCRIPT) | Magnitude: 108.75 | Delta: **0.09** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 57, structural_boundaries: 21, concurrency: 16, core_var_decl: 16
- `helpers/compile/plugins/fill-plugin/fillers/events.ts` (TYPESCRIPT) | Magnitude: 18.38 | Delta: **0.15** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 10, args: 4, api: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `packages/internals/src/__tests__/getSchema.test.ts` (TYPESCRIPT) | Magnitude: 66.2 | Delta: **0.057** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 79, io: 30, structural_boundaries: 24, concurrency: 18
- `packages/client-generator-ts/src/TSClient/Output.ts` (TYPESCRIPT) | Magnitude: 75.8 | Delta: **0.095** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 51, structural_boundaries: 30, branch: 21, core_var_decl: 17
- `packages/client-generator-js/src/TSClient/Output.ts` (TYPESCRIPT) | Magnitude: 80.76 | Delta: **0.103** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 54, structural_boundaries: 30, branch: 22, core_var_decl: 18
- `packages/schema-files-loader/src/loadSchemaFiles.ts` (TYPESCRIPT) | Magnitude: 32.92 | Delta: **0.153** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 37, structural_boundaries: 23, concurrency: 12, core_var_decl: 10
- `packages/client-generator-ts/tests/utils/buildGetWasmModule.test.ts` (TYPESCRIPT) | Magnitude: 20.28 | Delta: **0.154** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 59, structural_boundaries: 25, core_var_decl: 14, branch: 6

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `packages/cli/src/Studio.ts` -> Churn: **76.85%** | Cog Load: 57.6547% | Debt: 8.996%
- `packages/cli/src/Init.ts` -> Churn: **68.52%** | Cog Load: 85.4577% | Debt: 8.1584%
- `packages/client/tests/functional/_utils/setupTestSuiteClient.ts` -> Churn: **66.92%** | Cog Load: 59.9455% | Debt: 0.0%
- `packages/client/src/runtime/core/engines/client/ClientEngine.ts` -> Churn: **59.26%** | Cog Load: 87.9754% | Debt: 13.1536%
- `packages/cli/src/CLI.ts` -> Churn: **55.57%** | Cog Load: 89.481% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `packages/client/tests/functional/0-legacy-ports/batch-find-unique/tests.ts` -> **Oleksii (Alexey) Orlenko** (100.0% isolated ownership) | Magnitude: 752.02
- `packages/cli/src/bootstrap/Bootstrap.ts` -> **Kristof Siket** (100.0% isolated ownership) | Magnitude: 693.72
- `packages/client/tests/functional/extended-where/validation.ts` -> **Alberto Schiabel** (100.0% isolated ownership) | Magnitude: 623.6
- `packages/client/src/__tests__/benchmarks/query-performance/query-performance.bench.ts` -> **Oleksii Orlenko** (100.0% isolated ownership) | Magnitude: 545.4
- `packages/client/tests/functional/extensions/query.ts` -> **Alberto Schiabel** (100.0% isolated ownership) | Magnitude: 502.16

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `packages/client/src/runtime/getPrismaClient.ts` -> **Severity: 0.809** (Bridge: 0.0085 * Flux: 95.116%)
- `packages/client/src/runtime/core/engines/client/ClientEngine.ts` -> **Severity: 0.201** (Bridge: 0.0022 * Flux: 92.2%)
- `packages/client-engine-runtime/src/interpreter/query-interpreter.ts` -> **Severity: 0.095** (Bridge: 0.0012 * Flux: 81.3017%)
- `packages/client/src/runtime/RequestHandler.ts` -> **Severity: 0.055** (Bridge: 0.0009 * Flux: 60.0935%)
- `packages/client/src/runtime/core/jsonProtocol/serializeJsonQuery.ts` -> **Severity: 0.053** (Bridge: 0.0007 * Flux: 73.3365%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `packages/client/tests/functional/_utils/setupTestSuiteEnv.ts` -> **Severity: 4.042** (Embedded: 0.0715 * Error Risk: 56.5619%)
- `packages/client/tests/functional/_utils/types.ts` -> **Severity: 4.022** (Embedded: 0.0741 * Error Risk: 54.2752%)
- `packages/client/tests/functional/_utils/setupTestSuiteMatrix.ts` -> **Severity: 4.01** (Embedded: 0.0693 * Error Risk: 57.8318%)
- `packages/migrate/src/commands/DbExecute.ts` -> **Severity: 3.693** (Embedded: 0.0532 * Error Risk: 69.3456%)
- `helpers/blaze/map.ts` -> **Severity: 3.666** (Embedded: 0.0458 * Error Risk: 80.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `packages/client/tests/functional/_utils/providers.ts` -> **Severity: 5522.0** (Blast Radius: 55.22 * Doc Risk: 100.0%)
- `packages/client/tests/functional/_utils/idForProvider.ts` -> **Severity: 1136.7** (Blast Radius: 11.367 * Doc Risk: 100.0%)
- `packages/client/tests/e2e/_utils/executeSteps.ts` -> **Severity: 973.5** (Blast Radius: 9.735 * Doc Risk: 100.0%)
- `packages/client/tests/functional/_utils/defineMatrix.ts` -> **Severity: 898.525** (Blast Radius: 35.941 * Doc Risk: 25.0%)
- `packages/client/tests/functional/_utils/setupTestSuiteMatrix.ts` -> **Severity: 712.89** (Blast Radius: 7.921 * Doc Risk: 90.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 851 literal sites + 5 sites through wrappers = 856
- **`panics_and_aborts`:** 941 literal sites + 10 sites through wrappers = 951

- `onGenericD1HttpError` (function, panics_and_aborts, primitive): 3 call sites in 1 files -- `packages/adapter-d1/src/d1-http.ts`
- `bufferPolyfillDoesNotImplement` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `helpers/compile/plugins/fill-plugin/fillers/buffer-small.ts`
- `onError` (function, debug_prints, primitive): 2 call sites in 1 files -- `packages/adapter-d1/src/d1-http.ts`
- `onError` (function, debug_prints, primitive): 2 call sites in 1 files -- `packages/adapter-d1/src/d1-worker.ts`
- `onError` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `packages/adapter-d1/src/d1-http.ts`
- `onError` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `packages/adapter-d1/src/d1-worker.ts`
- `one` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `sandbox/driver-adapters/src/test.ts`
- `runGenerate` (function, debug_prints, primitive): 1 call sites in 1 files -- `packages/type-benchmark-tests/test.ts`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 12200 call pairs -- scoped 25.6%, unique 0.0%, ambiguous 21.9%, external 52.5%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| typescript | 11874 | 26.1% | 0.0% | 21.9% | 52.0% |
| javascript | 301 | 8.6% | 0.0% | 22.6% | 68.8% |
| shell | 24 | 0.0% | 0.0% | 0.0% | 100.0% |
| postgresql | 1 | 100.0% | 0.0% | 0.0% | 0.0% |

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
