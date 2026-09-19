# ARCHITECTURAL_BRIEF: prisma
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/prisma/prisma.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 3694 analyzed artifact(s), 204246 LOC.
- **Load-bearing artifact:** `packages/cli/src/config.ts` -- 433 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `packages/internals/src/index.ts` -- pulls in 74 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `packages/client/tests/functional/query-validation/tests.ts` at magnitude 7138.28 (structural weight, not risk).
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
| Analyzed Artifacts (Scanned) | 3694 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 928 |
| Total LOC | 204246 |
| Volatility Index | 0.002 |
| % Scanned of codebase = | 79.9% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.8433 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2662 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 1.5% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.3336 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 200 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 2692 | 184314 | 72.9% |
| JSON | 236 | 1735 | 6.4% |
| SQLITE | 218 | 954 | 5.9% |
| PLAINTEXT | 188 | 8 | 5.1% |
| MARKDOWN | 155 | 0 | 4.2% |
| JAVASCRIPT | 121 | 2023 | 3.3% |
| YAML | 67 | 15059 | 1.8% |
| SHELL | 6 | 87 | 0.2% |
| BATCH | 6 | 12 | 0.2% |
| DOCKERFILE | 4 | 48 | 0.1% |
| POWERSHELL | 1 | 6 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Hub-Coupled Monorepo`
> **Architectural Drift Z-Score:** `7.332`
> **Composition Archetype:** `Hub-Coupled Monorepo` (z +7.33; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 44%, Declarative / Non-Code 27%, Callbacks & Closures Files 6%, Parameter Forwarders Files 5%, Large Core Modules (2) 4%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 3351 | 90.7% |
| Unknown | 8 | 0.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 335 | 9.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 928*

**Composition by Extension & Reason:**
- `.prisma`: 380x Unsupported Format (.prisma), 127x Excluded (Unsupported Extension: '.prisma'), 1x Excluded (Monolithic Amalgamation: 30273 LOC exceeds safe regex boundaries)
- `no_extension`: 144x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 19x Unsupported Format (.undeterminable)
- `.db`: 70x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Binary Format Detected), 1x Excluded (Unsupported Extension: '.db')
- `.snap`: 22x Unsupported Format (.snap), 8x Excluded (Unsupported Extension: '.snap'), 1x Excluded (Machine-Generated Source Code Signature: 1081 LOC)
- `.ts`: 26x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Saturation: Line 22 exceeds 500 chars), 1x Excluded (Machine-Generated Source Code Signature: 128 LOC)
- `.yml`: 31x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 2x Excluded (Static Asset Blob without Intent: 1072 LOC), 1x Excluded (Static Asset Blob without Intent: 1264 LOC), 1x Excluded (Static Asset Blob without Intent: 2002 LOC)
- `.toml`: 18x Unsupported Format (.toml), 4x Excluded (Unsupported Extension: '.toml')
- `.md`: 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 376 LOC), 1x Excluded (Machine-Generated Source Code Signature: 87 LOC)
- `.json`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 3x Excluded (Explicitly Denied Extension: '.png')
- `.sql`: 1x Excluded (Static Asset Blob without Intent: 1032 LOC), 1x Excluded (Static Asset Blob without Intent: 1028 LOC), 1x Excluded (Static Asset Blob without Intent: 1026 LOC)
- `.lock`: 2x Unsupported Format (.lock)
- `.1c`: 2x Unsupported Format (.1c)
- `.so`: 2x Excluded (Explicitly Denied Extension: '.so')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 12.5 | 5.6 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.7 | 21.5 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 1.6 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 2.0 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 15.5 | 3.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 25.2 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 11.0 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 0.8 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 19.7 | 5.9 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 71.8 | 4.5 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 29.4 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 24.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1076 | 383 | 1 | `packages/client/src/__tests__/buffer-small.test.ts` |
| cleanup | 90 | 49 | 0 | `packages/adapter-pg/src/__tests__/pg.test.ts` |
| guards | 5183 | 851 | 3 | `packages/migrate/src/__tests__/DbExecute.test.ts` |
| danger | 2539 | 595 | 2 | `packages/client/src/__tests__/buffer-small.test.ts` |
| concurrency | 13678 | 968 | 9 | `packages/client/tests/functional/interactive-transactions/tests.ts` |
| connectivity | 5022 | 1937 | 3 | `packages/internals/src/index.ts` |
| io | 5539 | 632 | 3 | `packages/migrate/src/__tests__/DbExecute.test.ts` |
| crypto | 0 | 0 | 0 | - |
| ipc | 32 | 19 | 0 | `packages/client/tests/functional/_utils/setupTestSuiteMatrix.ts` |
| time | 460 | 188 | 0 | `packages/cli/src/bootstrap/Bootstrap.ts` |
| serialization | 337 | 137 | 0 | `packages/sqlcommenter-query-insights/src/parameterize/tests/security.test.ts` |
| regex | 546 | 185 | 0 | `packages/adapter-mariadb/src/errors.ts` |
| events | 878 | 239 | 0 | `packages/client/tests/functional/relationMode-in-separate-gh-action/tests_m-to-n.ts` |
| tests | 12517 | 660 | 6 | `packages/client/src/__tests__/buffer-small.test.ts` |
| docs | 1637 | 511 | 1 | `packages/integration-tests/src/__tests__/__helpers__/integrationTest.ts` |
| debt | 1282 | 377 | 1 | `scripts/ci/publish.ts` |
| mutation | 22972 | 1977 | 14 | `packages/client/src/__tests__/buffer-small.test.ts` |
| dead_code | 592 | 297 | 0 | `packages/client/tests/functional/_utils/getTestSuitePlan.ts` |
| credential | 26 | 15 | 0 | `.github/workflows/scripts/setup-mysql.sh` |
| threat | 227 | 67 | 0 | `helpers/compile/plugins/fill-plugin/fillers/buffer-small.ts` |
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

1. **config.ts** (`packages/cli/src/config.ts`) — 433 inbound connections
2. **providers.ts** (`packages/client/tests/functional/_utils/providers.ts`) — 346 inbound connections
3. **defineMatrix.ts** (`packages/client/tests/functional/_utils/defineMatrix.ts`) — 219 inbound connections
4. **idForProvider.ts** (`packages/client/tests/functional/_utils/idForProvider.ts`) — 184 inbound connections
5. **colors.js** (`packages/client/scripts/colors.js`) — 92 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.ts** (`packages/internals/src/index.ts`) — 74 outbound dependencies
2. **getPrismaClient.ts** (`packages/client/src/runtime/getPrismaClient.ts`) — 43 outbound dependencies
3. **index.ts** (`packages/ts-builders/src/index.ts`) — 37 outbound dependencies
4. **bin.ts** (`packages/cli/src/bin.ts`) — 32 outbound dependencies
5. **Studio.ts** (`packages/cli/src/Studio.ts`) — 27 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `run` **(Many-Argument Workhorses)** (@ `packages/cli/src/bootstrap/Bootstrap.ts`) -> Impact: **252.4** | LOC: 392
- `writeUIntLE` **(Many-Argument Workhorses)** (@ `helpers/compile/plugins/fill-plugin/fillers/buffer-small.ts`) -> Impact: **240.2** | LOC: 443
- `getPrismaClient` **(Defensive Guards)** (@ `packages/client/src/runtime/getPrismaClient.ts`) -> Impact: **198.2** | LOC: 767
- `testIf` **(Callbacks & Closures)** (@ `packages/client/src/__tests__/buffer-small.test.ts`) -> Impact: **188.9** | LOC: 2194
- `parse` **(Many-Argument Workhorses)** (@ `packages/cli/src/Init.ts`) -> Impact: **156.0** | LOC: 418
- `mapValue` **(Many-Argument Workhorses)** (@ `packages/client-engine-runtime/src/interpreter/data-mapper.ts`) -> Impact: **148.7** | LOC: 157
- `mapDriverError` **(Compute Cores)** (@ `packages/adapter-mssql/src/errors.ts`) -> Impact: **135.8** | LOC: 170
- `parse` **(Many-Argument Workhorses)** (@ `packages/cli/src/Generate.ts`) -> Impact: **115.5** | LOC: 229
- `interpretNode` **(Many-Argument Workhorses)** (@ `packages/client-engine-runtime/src/interpreter/query-interpreter.ts`) -> Impact: **112.2** | LOC: 235
- `parse` **(Many-Argument Workhorses)** (@ `packages/migrate/src/commands/MigrateDiff.ts`) -> Impact: **108.0** | LOC: 200

*Function archetypes referenced above:*
  * **Callbacks & Closures**: built around closures/callbacks (handlers, async continuations)
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `packages/migrate/src/__tests__` | 20 | 10565.73 | 29.41% | 0.0% |
| `packages/migrate/src/__tests__/DbPull` | 11 | 7999.17 | 96.94% | 0.0% |
| `packages/client/tests/functional/query-validation` | 2 | 7154.48 | 24.07% | 0.0% |
| `packages/client/tests/functional/relation-load-strategy-unsupported` | 3 | 6064.0 | 33.24% | 0.0% |
| `__monolith__` | 17 | 5158.56 | 0.45% | 0.0% |
| `packages/config/src/__tests__/fixtures/loadConfigFromFile/env-load-esm` | 2 | 5000.03 | 9.41% | 0.0% |
| `packages/config/src/__tests__/fixtures/loadConfigFromFile/env-load-cjs` | 2 | 5000.01 | 1.79% | 0.0% |
| `packages/client/fixtures/mongo/prisma` | 1 | 5000.0 | 0.0% | 0.0% |
| `packages/client/src/__tests__/integration/happy/browser/prisma` | 1 | 5000.0 | 0.0% | 0.0% |
| `packages/internals/src/__tests__/__fixtures__/dotenv` | 1 | 5000.0 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `packages/ts-builders/src/Import.ts` -> **99.9719%** Exposure
- `packages/type-benchmark-tests/lots-of-relations/client-options.bench.ts` -> **99.9711%** Exposure
- `packages/migrate/src/__tests__/__helpers__/captureStdout.ts` -> **99.9665%** Exposure
- `packages/type-benchmark-tests/basic/client-options.bench.ts` -> **99.9555%** Exposure
- `packages/client/src/runtime/core/model/applyModelsAndClientExtensions.ts` -> **99.3992%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `.github/workflows/scripts/detect-jobs-to-run.js` -> **100.0%** Exposure
- `packages/client/src/utils/compilerWorker.js` -> **100.0%** Exposure
- `packages/migrate/src/__tests__/fixtures/seed-from-prisma-config/seed-sqlite-js-extra-args/prisma/seed.js` -> **100.0%** Exposure
- `helpers/blaze/concat.ts` -> **100.0%** Exposure
- `helpers/blaze/map.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `packages/client/src/runtime/core/compositeProxy/createCompositeProxy.test.ts` -> **1** Orphaned Functions | **19** Duplicates
- `packages/client/tests/functional/extensions/query.ts` -> **1** Orphaned Functions | **17** Duplicates
- `packages/client/tests/functional/extensions/model.ts` -> **0** Orphaned Functions | **16** Duplicates
- `packages/client/src/runtime/core/extensions/applyResultExtensions.test.ts` -> **0** Orphaned Functions | **15** Duplicates
- `packages/type-benchmark-tests/lots-of-relations/client-options.bench.ts` -> **1** Orphaned Functions | **11** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `packages/sqlcommenter-query-insights/src/parameterize/tests/security.test.ts` -> **23.958%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `12` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `3283` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `packages/client/tests/functional/query-validation/tests.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 7138.28 | **LOC:** 495 | **CtrlFlow:** 27.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.157; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.9%), Complexity Load (formerly Cognitive Load) (42.5%), Guard Balance (formerly Safety Score) (30.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (17.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 112`, `structural_boundaries: 71`, `args: 36`, `func_start: 33`
* *Risk/State:* `safety_bypasses: 2`, `planned_debt: 1`
* *Architecture:* `io: 1`, `concurrency: 50`, `import: 3`
* *Defense:* `safety: 8`, `test: 50`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` _common, _matrix, client
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/client/tests/functional/relation-load-strategy-unsupported/preview-feature-disabled.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 5665.6 | **LOC:** 523 | **CtrlFlow:** 19.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.157; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (57.1%), Guard Balance (formerly Safety Score) (25.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (17.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 84
* *State Mutation (weighted view):* 5
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 72`, `args: 35`, `func_start: 32`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `concurrency: 64`, `import: 3`
* *Defense:* `safety: 16`, `test: 60`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` providers, _matrix, client
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/client/fixtures/mongo/prisma/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/client/src/__tests__/integration/happy/browser/prisma/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/config/src/__tests__/fixtures/loadConfigFromFile/env-load-cjs/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/config/src/__tests__/fixtures/loadConfigFromFile/env-load-esm/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/internals/src/__tests__/__fixtures__/dotenv/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/migrate/src/__tests__/fixtures/schema-only-cockroachdb/prisma/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/migrate/src/__tests__/fixtures/schema-only-postgresql/prisma/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/migrate/src/__tests__/DbPull/sqlite.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 4299.11 | **LOC:** 654 | **CtrlFlow:** 15.6% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.157; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (92.6%), Guard Balance (formerly Safety Score) (48.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 31 instances
* *Amplified Cascading Flux:* 10 instances
* *Concurrency (weighted view):* 207
* *State Mutation (weighted view):* 64
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 61`, `args: 20`, `func_start: 17`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 44`, `planned_debt: 1`
* *Architecture:* `io: 26`, `concurrency: 52`, `import: 3`
* *Defense:* `safety: 10`, `test: 56`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` DbPull, conditionalTests, context
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/client/tests/functional/relation-load-strategy/unsupported-queries.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 3434.98 | **LOC:** 302 | **CtrlFlow:** 27.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.157; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.9%), Complexity Load (formerly Cognitive Load) (42.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (17.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (4.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 45`, `args: 19`, `func_start: 16`
* *Risk/State:* None
* *Architecture:* `concurrency: 32`, `import: 4`
* *Defense:* `safety: 8`, `test: 30`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` providers, _common, _matrix, client
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/migrate/src/__tests__/MigrateDiff.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 2926.65 | **LOC:** 927 | **CtrlFlow:** 2.2% | **Authorship Centralization:** 42.9%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.157; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (62.2%), Complexity Load (formerly Cognitive Load) (50.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 123 instances
* *Amplified Cascading Flux:* 18 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 756
* *State Mutation (weighted view):* 214
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 177`, `args: 74`, `func_start: 39`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 2`, `state_mutation: 178`
* *Architecture:* `io: 29`, `concurrency: 141`, `import: 11`
* *Defense:* `safety: 22`, `test: 125`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` MigrateDiff, setupCockroach, setupMSSQL, setupMysql, setupPostgres, conditionalTests, context, promises...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/client/tests/functional/fluent-api/tests.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 2584.51 | **LOC:** 764 | **CtrlFlow:** 5.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.157; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (26.4%), Guard Balance (formerly Safety Score) (22.1%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` _matrix, client, faker, expect-type
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/client/tests/functional/logging/tests.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 2468.8 | **LOC:** 272 | **CtrlFlow:** 25.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.157; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (48.7%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` providers, types, _matrix, client, faker
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/client/tests/functional/0-legacy-ports/aggregations/tests.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 2088.54 | **LOC:** 380 | **CtrlFlow:** 12.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.157; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.8%), Complexity Load (formerly Cognitive Load) (24.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 42`, `args: 20`, `func_start: 18`
* *Risk/State:* None
* *Architecture:* `concurrency: 36`, `import: 3`
* *Defense:* `safety: 5`, `test: 31`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` _matrix, client, copycat
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/cli/src/__tests__/Init.vitest.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 1779.51 | **LOC:** 526 | **CtrlFlow:** 6.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.157; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (98.2%), Mutation Surface (formerly State Flux) (81.6%), Guard Balance (formerly Safety Score) (21.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 34 instances
* *Amplified Cascading Flux:* 6 instances
* *Concurrency (weighted view):* 215
* *State Mutation (weighted view):* 42
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 68`, `args: 22`, `func_start: 22`
* *Risk/State:* `state_mutation: 30`
* *Architecture:* `io: 81`, `api: 3`, `concurrency: 45`, `import: 9`
* *Defense:* `safety: 4`, `test: 134`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Init, config, get-platform, config, fs, path, config, strip-ansi
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/client/tests/functional/extended-where/validation.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1739.6 | **LOC:** 99 | **CtrlFlow:** 67.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.157; role: Isolated/Orphan
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (53.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (17.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 36
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 23`, `args: 8`, `func_start: 4`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* `concurrency: 6`, `import: 3`
* *Defense:* `safety: 2`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` _matrix, client, expect-type
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/client/tests/functional/0-legacy-ports/query-raw/tests.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 1692.22 | **LOC:** 307 | **CtrlFlow:** 12.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.157; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (74.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 16 instances
* *Amplified Cascading Flux:* 13 instances
* *Concurrency (weighted view):* 109
* *State Mutation (weighted view):* 42
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 44`, `args: 16`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 16`, `planned_debt: 2`
* *Architecture:* `io: 3`, `concurrency: 29`, `import: 4`
* *Defense:* `test: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` providers, _matrix, client, copycat
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/client/tests/functional/0-legacy-ports/batch-find-unique/tests.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 1360.54 | **LOC:** 175 | **CtrlFlow:** 30.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.157; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (81.5%), Guard Balance (formerly Safety Score) (45.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (12.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 32
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 29`, `args: 6`, `func_start: 1`
* *Risk/State:* `state_mutation: 2`, `planned_debt: 1`
* *Architecture:* `concurrency: 12`, `import: 7`
* *Defense:* `safety: 1`, `test: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` providers, waitFor, types, _matrix, client, internals, copycat
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/migrate/src/__tests__/DbPush.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 1320.55 | **LOC:** 447 | **CtrlFlow:** 3.6% | **Authorship Centralization:** 45.5%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.157; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (85.0%), Complexity Load (formerly Cognitive Load) (50.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (30.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 37 instances
* *Amplified Cascading Flux:* 5 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 263
* *State Mutation (weighted view):* 34
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 100`, `args: 42`, `func_start: 20`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 2`, `state_mutation: 24`
* *Architecture:* `io: 43`, `concurrency: 78`, `import: 7`
* *Defense:* `safety: 26`, `test: 68`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` DbPush, setupMongo, setupPostgres, conditionalTests, context, path, prompts
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/migrate/src/__tests__/MigrateResolve.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 1201.19 | **LOC:** 263 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.157; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (57.1%), Complexity Load (formerly Cognitive Load) (50.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 43 instances
* *Amplified Cascading Flux:* 20 instances
* *Concurrency (weighted view):* 266
* *State Mutation (weighted view):* 75
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 60`, `args: 21`, `func_start: 16`
* *Risk/State:* `state_mutation: 35`
* *Architecture:* `io: 16`, `concurrency: 51`, `import: 3`
* *Defense:* `safety: 11`, `test: 44`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` MigrateResolve, conditionalTests, context
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/client/src/__tests__/buffer-small.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1142.94 | **LOC:** 6236 | **CtrlFlow:** 3.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.157; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.9%), Guard Balance (formerly Safety Score) (56.2%), Complexity Load (formerly Cognitive Load) (15.5%), Dead Code Surface (formerly Dead Code) (7.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testIf` **(Callbacks & Closures)** (Impact: 188.9)
  * `writeToFill` **(Many-Argument Workhorses)** (Impact: 35.4)
    * *Intent:* // This is mostly accurate. Except write() won't write partial bytes to the // string while fill() b...
  * `testBufs` **(Many-Argument Workhorses)** (Impact: 9.4)
  * `receiver` **(Compute Cores)** (Impact: 5.3)
    * *Intent:* // eslint-disable-next-line no-inner-declarations
  * `deepStrictEqualValues` **(State Mutators)** (Impact: 3.7)
    * *Intent:* // Buffer
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 196 instances
* *State Mutation (weighted view):* 791
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 161`, `structural_boundaries: 690`, `args: 662`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 108`, `state_mutation: 399`, `dead_code: 3`, `fragile_debt: 5`, `unreferenced_by_name: 2`
* *Architecture:* `import: 6`
* *Defense:* `safety: 61`, `doc: 3`, `test: 803`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` buffer-small, assert, buffer, crypto
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/migrate/src/__tests__/DbExecute.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 1107.38 | **LOC:** 966 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 60.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.157; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.4%), Complexity Load (formerly Cognitive Load) (50.0%), Guard Balance (formerly Safety Score) (26.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testIf` **(Callbacks & Closures)** (Impact: 3.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 152 instances
* *Amplified Cascading Flux:* 16 instances
* *Concurrency (weighted view):* 946
* *State Mutation (weighted view):* 143
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 228`, `args: 89`, `func_start: 55`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 111`, `planned_debt: 2`
* *Architecture:* `io: 206`, `concurrency: 186`, `import: 12`
* *Defense:* `safety: 91`, `test: 136`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` DbExecute, setupCockroach, setupMSSQL, setupMysql, setupPostgres, conditionalTests, context, node:child_process...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/ci/publish.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 876.72 | **LOC:** 982 | **CtrlFlow:** 21.9% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 0.157; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (85.8%), Guard Balance (formerly Safety Score) (83.9%)
- **Documentation Coverage:** 82.6087% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `publishPackages` **(Many-Argument Workhorses)** (Impact: 61.5)
  * `publish` **(I/O & Config Routines)** (Impact: 55.8)
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
* *Structure:* `branch: 161`, `structural_boundaries: 182`, `args: 74`, `func_start: 46`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 1`, `state_mutation: 80`, `dead_code: 1`, `planned_debt: 15`, `unreferenced_by_name: 1`
* *Architecture:* `io: 34`, `api: 4`, `concurrency: 97`, `import: 12`
* *Defense:* `safety: 18`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` package.json, slugify, webhook, arg, batching-toposort, execa, globby, colors...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `packages/cli/src/Studio.ts` -> Churn: **71.82%** | Cog Load: 67.4826% | Debt: 9.3837%
- `packages/cli/src/Init.ts` -> Churn: **63.2%** | Cog Load: 87.005% | Debt: 8.4593%
- `packages/client/tests/functional/_utils/setupTestSuiteClient.ts` -> Churn: **61.73%** | Cog Load: 60.2906% | Debt: 0.0%
- `packages/client/src/runtime/core/engines/client/ClientEngine.ts` -> Churn: **54.66%** | Cog Load: 88.8047% | Debt: 13.5972%
- `packages/cli/src/CLI.ts` -> Churn: **53.42%** | Cog Load: 89.8365% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `packages/client/tests/functional/query-validation/tests.ts` -> **Alberto Schiabel** (100.0% isolated ownership) | Magnitude: 7138.28
- `packages/client/tests/functional/relation-load-strategy-unsupported/preview-feature-disabled.ts` -> **Alberto Schiabel** (100.0% isolated ownership) | Magnitude: 5665.6
- `packages/client/tests/functional/relation-load-strategy/unsupported-queries.ts` -> **Alberto Schiabel** (100.0% isolated ownership) | Magnitude: 3434.98
- `packages/cli/src/__tests__/Init.vitest.ts` -> **jacek-prisma** (100.0% isolated ownership) | Magnitude: 1779.51
- `packages/client/tests/functional/extended-where/validation.ts` -> **Alberto Schiabel** (100.0% isolated ownership) | Magnitude: 1739.6

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `packages/client/src/runtime/getPrismaClient.ts` -> **Severity: 0.243** (Bridge: 0.0025 * Flux: 95.5913%)
- `packages/client/src/utils/getTestClient.ts` -> **Severity: 0.03** (Bridge: 0.0006 * Flux: 47.0906%)
- `packages/client/src/runtime/core/jsonProtocol/serializeJsonQuery.ts` -> **Severity: 0.022** (Bridge: 0.0003 * Flux: 73.3365%)
- `packages/client/src/runtime/RequestHandler.ts` -> **Severity: 0.021** (Bridge: 0.0003 * Flux: 60.0935%)
- `packages/integration-tests/src/__tests__/__helpers__/integrationTest.ts` -> **Severity: 0.015** (Bridge: 0.0002 * Flux: 98.4507%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `packages/client/tests/functional/_utils/idForProvider.ts` -> **Severity: 3.829** (Embedded: 0.0498 * Error Risk: 76.8525%)
- `packages/client/scripts/colors.js` -> **Severity: 3.26** (Embedded: 0.0459 * Error Risk: 71.058%)
- `packages/client/tests/functional/_utils/setupTestSuiteMatrix.ts` -> **Severity: 2.496** (Embedded: 0.033 * Error Risk: 75.733%)
- `packages/client/tests/functional/_utils/setupTestSuiteEnv.ts` -> **Severity: 2.326** (Embedded: 0.0335 * Error Risk: 69.4661%)
- `packages/client/src/runtime/utils/waitForBatch.ts` -> **Severity: 2.323** (Embedded: 0.0281 * Error Risk: 82.6806%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `packages/client/tests/functional/_utils/providers.ts` -> **Severity: 5297.3** (Blast Radius: 52.973 * Doc Risk: 100.0%)
- `packages/client/tests/functional/_utils/idForProvider.ts` -> **Severity: 2399.1** (Blast Radius: 23.991 * Doc Risk: 100.0%)
- `packages/client/scripts/colors.js` -> **Severity: 1177.6** (Blast Radius: 11.776 * Doc Risk: 100.0%)
- `packages/client/tests/e2e/_utils/executeSteps.ts` -> **Severity: 1061.6** (Blast Radius: 10.616 * Doc Risk: 100.0%)
- `packages/ts-builders/src/Writer.ts` -> **Severity: 660.599** (Blast Radius: 19.818 * Doc Risk: 33.3333%)

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
