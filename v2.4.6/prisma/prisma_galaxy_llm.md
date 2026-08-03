# ARCHITECTURAL_BRIEF: prisma
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_typescript/prisma` |
| **Timestamp** | `2026-08-03T19:56:49.186957+00:00` |
| **Scan Duration** | `12.28s` |
| **Git Branch** | `main` |
| **Git Commit** | `ada077ba32b5801d00d32f1434a45aaae7bc09a9` |
| **Git Remote** | `https://github.com/prisma/prisma.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 2881 malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are analyzing software architecture through the lens of GitGalaxy Static Application Security Testing (SAST). GitGalaxy translates the non-visual architecture of repositories into measurable technical metrics.
> 
> **CORE DIRECTIVES:**
> 1. **Measure Risk, Not Quality:** Do not judge. We measure Risk Exposure (e.g., Cognitive Load Exposure). Frame all insights as blameless, objective observations. High risk highlights where the architecture might be drifting into fragile territory, not developer incompetence.
> 2. **The Physical Reality Rule:** Base your analysis strictly on the provided Structural Signatures (regex hit counts). Do not hallucinate meaning.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`.
> 
> **THE STRUCTURAL SIGNATURE LEXICON:**
> * **Structure & Mass:** `branch` (splits), `linear` (paths), `args` (coupling), `func_start` (entry points).
> * **Risk & Volatility:** `danger` (dynamic execution), `flux` (state mutation), `graveyard` (commented-out logic), `safety_neg` (security bypasses).
> * **Architecture & Domain:** `io` (network latency), `concurrency` (async orchestration), `api` (public surface), `import` (dependencies).
> * **Defensive Guardrails:** `safety` (Error handling), `freeze_hits` (immutability), `cleanup` (state destruction).
## 2. THE 13-POINT RISK EXPOSURE ANALYSIS (EQUATIONS & CONTEXT)
> **How the SAST Engine Calculates Risk Exposure (Lower Risk 0 - Higher Risk Exposure 100%):**
> Most scores use a Sigmoid curve based on density (Hits / LOC) to prevent massive files from mathematically hiding their flaws.
> 
> 1. **Cognitive Load Exposure:** Measures the mental effort required for a developer to read and understand the file. `Density(Branches + (Flux * 2) + Async/Danger)` mitigated by `Doc Coverage`.
> 2. **Error & Exception Risk Exposure:** Measures structural integrity and resilience against runtime errors. `Net Exposure = (Danger + Safety_Neg + Flux) - (Safety + Tests + Docs)`.
> 3. **Tech Debt Exposure:** Measures the density of developer-annotated structural stress. `Density(TODOs [1x] + FIXMEs/Hacks [3x] + Empty Stubs [0.5x])`.
> 4. **Verification Risk Exposure:** Evaluates test coverage by comparing a function's structural complexity against the scope of the tests validating it.
> 5. **API Risk Exposure:** Measures the public surface area of a module. `Ratio(API Hits / Total Functions & Classes)`.
> 6. **Concurrency Risk Exposure:** Measures the density of asynchronous operations, threading, and parallel execution logic.
> 7. **State Flux Risk Exposure:** Measures the frequency of data mutation and variable reassignment.
> 8. **Commented Logic (dead code):** Measures the presence of abandoned, commented-out logic blocks.
> 9. **Spec Match Risk Exposure:** Measures how closely code aligns with formal specifications or architectural requirements.
> 10. **Stability:** Measures the recency of edits relative to the repository's entire lifespan.
> 11. **Deep Churn:** Measures the historical volatility and frequency of modification.
> 12. **Documentation Risk Exposure:** Measures the lack of structured documentation and ownership metadata.
> 13. **Indentation Consistency:** Measures formatting alignment (Tabs vs. Spaces). Provided for codebase standardization context, not a functional risk.
> 
> **--- THE SECURITY & VULNERABILITY LENS ---**
> 14. **Obfuscation & Evasion Risk:** Measures the density of obfuscated logic, packed strings, and non-standard encoding.
> 15. **Logic Bomb / Sabotage Risk:** Measures condition-heavy execution leading to destructive OS, memory, or process commands.
> 16. **Injection Surface Risk Exposure:** Measures external network/I/O input flowing directly into dynamic execution contexts (XSS, SQLi, RCE).
> 17. **Memory Corruption Risk Exposure:** Measures the density of raw pointer math and manual memory allocations (Buffer Overflows, UAF).
> 18. **Secrets Risk Exposure:** Measures the presence of hardcoded credentials exposed to logs or globals.
> 
> **--- STRUCTURAL MAGNITUDE (NOT RISK) ---**
> **19. Function Magnitude (Impact Score):** Measures the physical footprint and 'heaviness' of a specific function. `((BranchHits + 1) * (Args + 1) + (0.05 * LOC)) * 10`. This is NOT a risk score.
> **20. File Magnitude (Total Impact):** Measures the total structural impact of a file. `Sum(Function Impacts) + API + Concurrency + Flux + (LOC / 50)`. This is NOT a risk score.

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 4622 |
| Analyzed Artifacts (Scanned) | 3476 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1146 |
| Total LOC | 181871 |
| Volatility Index | 0.003 |
| % Scanned of codebase = | 75.2% |
| Dominant Lang | PLAINTEXT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.839 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2804 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 1.6% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.7765 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 189 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 2570 | 163087 | 73.9% |
| SQLITE | 197 | 831 | 5.7% |
| JSON | 188 | 1314 | 5.4% |
| PLAINTEXT | 188 | 8 | 5.4% |
| MARKDOWN | 152 | 0 | 4.4% |
| JAVASCRIPT | 97 | 1419 | 2.8% |
| YAML | 67 | 15059 | 1.9% |
| SHELL | 6 | 87 | 0.2% |
| BATCH | 6 | 12 | 0.2% |
| DOCKERFILE | 4 | 48 | 0.1% |
| POWERSHELL | 1 | 6 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.273`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 2090 | 60.1% |
| file_cluster_13 | 698 | 20.1% |
| file_cluster_4 | 218 | 6.3% |
| file_cluster_16 | 62 | 1.8% |
| file_cluster_0 | 32 | 0.9% |
| file_cluster_17 | 20 | 0.6% |
| file_cluster_2 | 8 | 0.2% |
| Unknown | 8 | 0.2% |
| file_cluster_9 | 3 | 0.1% |
| file_cluster_1 | 2 | 0.1% |
| file_cluster_12 | 1 | 0.0% |
| file_cluster_7 | 1 | 0.0% |
| file_cluster_5 | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 332 | 9.6% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1146*

**Composition by Extension & Reason:**
- `.prisma`: 380x Unsupported Format (.prisma), 123x Excluded (Unsupported Extension: '.prisma'), 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 144x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 19x Unsupported Format (.undeterminable)
- `.ts`: 144x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Saturation: Line 22 exceeds 500 chars), 1x Excluded (Machine-Generated Source Code Signature: 128 LOC)
- `.db`: 70x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Binary Format Detected), 1x Excluded (Unsupported Extension: '.db')
- `.json`: 54x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.snap`: 22x Unsupported Format (.snap), 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 1081 LOC)
- `.yml`: 31x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sql`: 17x Excluded: Neighborhood Micro-Mass Limit Exceeded, 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Static Asset Blob without Intent: 1032 LOC)
- `.yaml`: 2x Excluded (Static Asset Blob without Intent: 1072 LOC), 1x Excluded (Static Asset Blob without Intent: 1264 LOC), 1x Excluded (Static Asset Blob without Intent: 2002 LOC)
- `.toml`: 18x Unsupported Format (.toml), 4x Excluded (Unsupported Extension: '.toml')
- `.md`: 14x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 376 LOC), 1x Excluded (Machine-Generated Source Code Signature: 87 LOC)
- `.jsx`: 14x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.tsx`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 3x Excluded (Explicitly Denied Extension: '.png')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 16.7 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 98.7 | 15.3 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 7.5 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 2.2 | 0.0 | 0.0 |
| API Exposure | 0.0 | 19.9 | 3.8 | 4.5 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 26.6 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 7.7 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 0.7 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 70.5 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 21.2 | 6.1 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 71.3 | 4.6 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 22.8 | 0.0 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 6.1 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 98.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 2.9 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.7 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 24.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `packages/migrate/src/__tests__/MigrateDev.test.ts` (Hits: 183)
- `packages/migrate/src/__tests__/DbExecute.test.ts` (Hits: 171)
- `packages/cli/src/bootstrap/__tests__/Bootstrap.vitest.ts` (Hits: 128)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **config.ts** (`packages/cli/src/config.ts`) — 437 inbound connections
2. **providers.ts** (`packages/client/tests/functional/_utils/providers.ts`) — 330 inbound connections
3. **defineMatrix.ts** (`packages/client/tests/functional/_utils/defineMatrix.ts`) — 216 inbound connections
4. **idForProvider.ts** (`packages/client/tests/functional/_utils/idForProvider.ts`) — 181 inbound connections
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

- `matchGrammar` (@ `packages/internals/src/highlight/prism.ts`) -> Impact: **1105.9** | LOC: 170
- `describeIf` (@ `packages/client/tests/functional/relation-load-strategy-unsupported/preview-feature-disabled.ts`) -> Impact: **906.6** | LOC: 511
- `matchGrammar` (@ `packages/client/src/runtime/highlight/prism.ts`) -> Impact: **809.4** | LOC: 150
- `tests` (@ `packages/client/tests/functional/_utils/setupTestSuiteMatrix.ts`) -> Impact: **793.0** | LOC: 248
  * *Intent:* /** * How does this work from a high level? What steps?
- `describeIf` (@ `packages/client/tests/functional/relation-load-strategy/unsupported-queries.ts`) -> Impact: **736.7** | LOC: 281
- `writeUIntLE` (@ `helpers/compile/plugins/fill-plugin/fillers/buffer-small.ts`) -> Impact: **688.1** | LOC: 443
- `interpretNode` (@ `packages/client-engine-runtime/src/interpreter/query-interpreter.ts`) -> Impact: **631.8** | LOC: 235
- `describe` (@ `packages/internals/src/__tests__/engine-commands/validate.test.ts`) -> Impact: **527.8** | LOC: 440
- `getGenerators` (@ `packages/internals/src/get-generators/getGenerators.ts`) -> Impact: **501.1** | LOC: 221
  * *Intent:* /**
- `test` (@ `packages/client/tests/functional/extensions/query.ts`) -> Impact: **494.4** | LOC: 847

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `test` (@ `packages/client/src/__tests__/integration/errors/invalid-input/test.ts`) -> **O(2^N) [Recursive]**
- `test` (@ `packages/client/src/__tests__/integration/errors/union-validation/test.ts`) -> **O(2^N) [Recursive]**
- `test` (@ `packages/client/tests/functional/issues/18970-invalid-date/tests.ts`) -> **O(2^N) [Recursive]**
- `test` (@ `packages/client/tests/functional/query-validation/tests.ts`) -> **O(2^N) [Recursive]**
- `test` (@ `packages/client/tests/functional/query-validation/tests.ts`) -> **O(2^N) [Recursive]**
- `test` (@ `packages/client/tests/functional/query-validation/tests.ts`) -> **O(2^N) [Recursive]**
  * *Intent:* // https://github.com/prisma/prisma/issues/19707
- `test` (@ `packages/client/tests/functional/query-validation/tests.ts`) -> **O(2^N) [Recursive]**
- `test` (@ `packages/client/tests/functional/query-validation/tests.ts`) -> **O(2^N) [Recursive]**
- `test` (@ `packages/client/tests/functional/query-validation/tests.ts`) -> **O(2^N) [Recursive]**
- `describeIf` (@ `packages/client/tests/functional/relation-load-strategy-unsupported/preview-feature-disabled.ts`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `describe` (@ `packages/config/src/__tests__/loadConfigFromFile.test.ts`) -> DB Complexity: **336**
- `describeMatrix` (@ `packages/migrate/src/__tests__/MigrateDev.test.ts`) -> DB Complexity: **297**
- `describe` (@ `packages/migrate/src/__tests__/DbExecute.test.ts`) -> DB Complexity: **288**
- `describeMatrix` (@ `packages/migrate/src/__tests__/DbPull/postgresql-views.test.ts`) -> DB Complexity: **240**
- `describe` (@ `packages/adapter-mssql/src/connection-string.test.ts`) -> DB Complexity: **171**
- `describeMatrix` (@ `packages/migrate/src/__tests__/DbExecute.test.ts`) -> DB Complexity: **117**
- `describe` (@ `packages/cli/src/__tests__/nps.test.ts`) -> DB Complexity: **101**
- `describe` (@ `packages/migrate/src/__tests__/local-clouflare-d1-db-e2e.test.ts`) -> DB Complexity: **101**
  * *Intent:* // We follow the steps in https://www.prisma.io/docs/orm/overview/databases/cloudflare-d1#migration-workflows.
- `describe` (@ `packages/cli/src/bootstrap/__tests__/project-state.vitest.ts`) -> DB Complexity: **93**
- `writeUIntLE` (@ `helpers/compile/plugins/fill-plugin/fillers/buffer-small.ts`) -> DB Complexity: **92**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `__monolith__` | 14 | 5116.8 | 2.82% | 0.0% |
| `packages/config/src/__tests__/fixtures/loadConfigFromFile/env-load-esm` | 2 | 5002.53 | 2.5% | 0.0% |
| `packages/config/src/__tests__/fixtures/loadConfigFromFile/env-load-cjs` | 2 | 5001.26 | 2.5% | 0.0% |
| `packages/client/fixtures/mongo/prisma` | 1 | 5000.0 | 0.0% | 0.0% |
| `packages/client/src/__tests__/integration/happy/browser/prisma` | 1 | 5000.0 | 0.0% | 0.0% |
| `packages/internals/src/__tests__/__fixtures__/dotenv` | 1 | 5000.0 | 0.0% | 0.0% |
| `packages/migrate/src/__tests__/fixtures/schema-only-cockroachdb/prisma` | 1 | 5000.0 | 0.0% | 0.0% |
| `packages/migrate/src/__tests__/fixtures/schema-only-postgresql/prisma` | 1 | 5000.0 | 0.0% | 0.0% |
| `.github/workflows/scripts` | 6 | 431.03 | 23.74% | 66.66% |
| `packages/migrate/src/__tests__` | 20 | 309.33 | 25.05% | 4.98% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `packages/generator-helper/src/__tests__/failing-after-1s-executable` -> **100.0%** Exposure
- `packages/generator-helper/src/__tests__/invalid-executable` -> **100.0%** Exposure
- `packages/migrate/src/__tests__/fixtures/seed-from-prisma-config/seed-sqlite-js/prisma/seed.js` -> **100.0%** Exposure
- `packages/migrate/src/__tests__/fixtures/seed-from-prisma-config/seed-sqlite-skips-deprecated-package-json/prisma/seed-deprecated.js` -> **100.0%** Exposure
- `packages/migrate/src/__tests__/fixtures/seed-from-prisma-config/seed-sqlite-skips-deprecated-package-json/prisma/seed.js` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `.github/workflows/scripts/detect-jobs-to-run.js` -> **100.0%** Exposure
- `helpers/blaze/concat.ts` -> **100.0%** Exposure
- `helpers/blaze/debounce.ts` -> **100.0%** Exposure
- `helpers/blaze/map.ts` -> **100.0%** Exposure
- `helpers/blaze/permutations.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `packages/client/src/__tests__/buffer-small.test.ts` -> **0** Orphaned Functions | **130** Duplicates
- `packages/integration-tests/src/__tests__/integration/mariadb/__scenarios.ts` -> **0** Orphaned Functions | **75** Duplicates
- `packages/integration-tests/src/__tests__/integration/mysql/__scenarios.ts` -> **0** Orphaned Functions | **75** Duplicates
- `packages/integration-tests/src/__tests__/integration/postgresql/__scenarios.ts` -> **0** Orphaned Functions | **75** Duplicates
- `packages/integration-tests/src/__tests__/integration/sqlite/__scenarios.ts` -> **0** Orphaned Functions | **65** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`packages/client/src/runtime/core/errorRendering/applyValidationError.test.ts`** -> AI Confidence: **99.39%**
2. **`packages/client/src/runtime/core/errorRendering/applyValidationError.ts`** -> AI Confidence: **99.35%**
3. **`packages/engines/scripts/postinstall.js`** -> AI Confidence: **99.32%**
4. **`packages/cli/src/Generate.ts`** -> AI Confidence: **99.31%**
5. **`packages/cli/src/bootstrap/Bootstrap.ts`** -> AI Confidence: **99.31%**
6. **`packages/cli/src/postgres/link/Link.ts`** -> AI Confidence: **99.31%**
7. **`packages/client-engine-runtime/src/interpreter/query-interpreter.ts`** -> AI Confidence: **99.31%**
8. **`packages/client/src/runtime/RequestHandler.ts`** -> AI Confidence: **99.31%**
9. **`packages/client/src/runtime/core/engines/client/RemoteExecutor.ts`** -> AI Confidence: **99.31%**
10. **`packages/client/src/runtime/core/engines/common/utils/getErrorMessageWithLink.ts`** -> AI Confidence: **99.31%**
11. **`packages/client/src/runtime/core/jsonProtocol/serializeJsonQuery.ts`** -> AI Confidence: **99.31%**
12. **`packages/client/src/runtime/core/raw-query/rawQueryArgsMapper.ts`** -> AI Confidence: **99.31%**
13. **`packages/client/tests/functional/_utils/getTestSuiteInfo.ts`** -> AI Confidence: **99.31%**
14. **`packages/internals/src/__tests__/engine-commands/validate.test.ts`** -> AI Confidence: **99.31%**
15. **`packages/internals/src/get-generators/getGenerators.ts`** -> AI Confidence: **99.31%**
16. **`packages/migrate/src/commands/DbPull.ts`** -> AI Confidence: **99.31%**
17. **`packages/migrate/src/commands/DbPush.ts`** -> AI Confidence: **99.31%**
18. **`packages/migrate/src/commands/MigrateDiff.ts`** -> AI Confidence: **99.31%**
19. **`eslint-local-rules/index.js`** -> AI Confidence: **99.29%**
20. **`packages/client/default.js`** -> AI Confidence: **99.29%**
21. **`packages/client/extension.js`** -> AI Confidence: **99.29%**
22. **`packages/client/index.js`** -> AI Confidence: **99.29%**
23. **`packages/engines/jest.config.js`** -> AI Confidence: **99.29%**
24. **`packages/fetch-engine/jest.config.js`** -> AI Confidence: **99.29%**
25. **`scripts/only-allow-pnpm.js`** -> AI Confidence: **99.29%**
26. **`.github/workflows/scripts/setup-mysql.sh`** -> AI Confidence: **99.29%**
27. **`docker/mongodb_replica/Dockerfile`** -> AI Confidence: **99.29%**
28. **`docker/postgres_ext/Dockerfile`** -> AI Confidence: **99.29%**
29. **`packages/client/tests/e2e/_utils/standard.dockerfile`** -> AI Confidence: **99.29%**
30. **`packages/adapter-mssql/src/errors.ts`** -> AI Confidence: **99.29%**
31. **`packages/cli/src/utils/prompt/utils/deepExtend.ts`** -> AI Confidence: **99.29%**
32. **`packages/client/tests/e2e/driver-adapters-custom-db-schema/adapter-neon/jestSetup.ts`** -> AI Confidence: **99.29%**
33. **`packages/client/tests/e2e/large-schema-generation/src/generate-schema.ts`** -> AI Confidence: **99.29%**
34. **`packages/client/tests/functional/blog-update/prisma/_schema.ts`** -> AI Confidence: **99.29%**
35. **`packages/client/tests/functional/issues/29331-query-plan-cache-bloat/prisma/_schema.ts`** -> AI Confidence: **99.29%**
36. **`packages/client/tests/functional/relationMode-in-separate-gh-action/prisma/_schema_1_to_1.ts`** -> AI Confidence: **99.29%**
37. **`packages/client/tests/functional/relationMode-in-separate-gh-action/prisma/_schema_m_to_n.ts`** -> AI Confidence: **99.29%**
38. **`packages/internals/src/utils/isCi.ts`** -> AI Confidence: **99.29%**
39. **`scripts/check-engines-override.ts`** -> AI Confidence: **99.29%**
40. **`packages/adapter-mssql/src/mssql.ts`** -> AI Confidence: **99.25%**
41. **`packages/cli/src/Init.ts`** -> AI Confidence: **99.24%**
42. **`packages/cli/src/Studio.ts`** -> AI Confidence: **99.24%**
43. **`packages/cli/src/bootstrap/template-scaffold.ts`** -> AI Confidence: **99.24%**
44. **`packages/client-engine-runtime/src/transaction-manager/transaction-manager.ts`** -> AI Confidence: **99.24%**
45. **`packages/client-generator-js/src/TSClient/Model.ts`** -> AI Confidence: **99.24%**
46. **`packages/client-generator-ts/src/TSClient/Model.ts`** -> AI Confidence: **99.24%**
47. **`packages/client-generator-ts/src/generateClient.ts`** -> AI Confidence: **99.24%**
48. **`packages/client/src/runtime/core/errorRendering/ObjectValue.ts`** -> AI Confidence: **99.24%**
49. **`packages/client/src/runtime/core/extensions/applyAllResultExtensions.ts`** -> AI Confidence: **99.24%**
50. **`packages/client/src/utils/getTestClient.ts`** -> AI Confidence: **99.24%**
51. **`packages/client/tests/functional/_utils/setupTestSuiteMatrix.ts`** -> AI Confidence: **99.24%**
52. **`packages/fetch-engine/src/download.ts`** -> AI Confidence: **99.24%**
53. **`scripts/ci/publish.ts`** -> AI Confidence: **99.24%**
54. **`packages/adapter-d1/src/d1-http.ts`** -> AI Confidence: **99.23%**
55. **`packages/cli/src/__tests__/artificial-panic.test.ts`** -> AI Confidence: **99.23%**
56. **`packages/client/src/runtime/utils/deepCloneArgs.ts`** -> AI Confidence: **99.23%**
57. **`packages/client/tests/e2e/_utils/run.ts`** -> AI Confidence: **99.23%**
58. **`packages/fetch-engine/src/utils.ts`** -> AI Confidence: **99.23%**
59. **`packages/generator-helper/src/GeneratorProcess.ts`** -> AI Confidence: **99.23%**
60. **`packages/get-platform/src/getPlatform.ts`** -> AI Confidence: **99.23%**
61. **`packages/migrate/src/commands/DbExecute.ts`** -> AI Confidence: **99.23%**
62. **`packages/query-plan-executor/src/server/headers.ts`** -> AI Confidence: **99.23%**
63. **`packages/client-engine-runtime/src/parameterization/parameterize-tests/test-fixtures.ts`** -> AI Confidence: **99.2%**
64. **`packages/client/tests/functional/extended-where/validation.ts`** -> AI Confidence: **99.2%**
65. **`packages/client/tests/functional/issues/11233/tests.ts`** -> AI Confidence: **99.2%**
66. **`packages/cli/src/CLI.ts`** -> AI Confidence: **99.18%**
67. **`packages/cli/src/__tests__/Init.vitest.ts`** -> AI Confidence: **99.18%**
68. **`packages/cli/src/__tests__/commands/Format.test.ts`** -> AI Confidence: **99.18%**
69. **`packages/cli/src/bin.ts`** -> AI Confidence: **99.18%**
70. **`packages/cli/src/studio-entry.ts`** -> AI Confidence: **99.18%**
71. **`packages/client-generator-ts/src/TSClient/Count.ts`** -> AI Confidence: **99.18%**
72. **`packages/client/src/__tests__/benchmarks/huge-schema/huge-schema.bench.ts`** -> AI Confidence: **99.18%**
73. **`packages/client/src/runtime/core/errorRendering/throwValidationException.ts`** -> AI Confidence: **99.18%**
74. **`packages/client/src/runtime/core/model/applyAggregates.ts`** -> AI Confidence: **99.18%**
75. **`packages/client/src/runtime/core/types/exported/Extensions.ts`** -> AI Confidence: **99.18%**
76. **`packages/client/tests/functional/_utils/qpe-worker.ts`** -> AI Confidence: **99.18%**
77. **`packages/client/tests/functional/extensions/query.ts`** -> AI Confidence: **99.18%**
78. **`packages/client/tests/functional/typescript/tests.ts`** -> AI Confidence: **99.18%**
79. **`packages/config/src/loadConfigFromFile.ts`** -> AI Confidence: **99.18%**
80. **`packages/fetch-engine/src/__tests__/download.test.ts`** -> AI Confidence: **99.18%**
81. **`packages/integration-tests/src/__tests__/__helpers__/integrationTest.ts`** -> AI Confidence: **99.18%**
82. **`packages/internals/src/__tests__/directoryConfig.test.ts`** -> AI Confidence: **99.18%**
83. **`packages/internals/src/__tests__/handlePanic.test.ts`** -> AI Confidence: **99.18%**
84. **`packages/internals/src/get-generators/utils/getBinaryPathsByVersion.ts`** -> AI Confidence: **99.18%**
85. **`packages/internals/src/resolveBinary.ts`** -> AI Confidence: **99.18%**
86. **`packages/internals/src/utils/handlePanic.ts`** -> AI Confidence: **99.18%**
87. **`packages/migrate/src/SchemaEngineWasm.ts`** -> AI Confidence: **99.18%**
88. **`packages/migrate/src/__tests__/DbExecute.test.ts`** -> AI Confidence: **99.18%**
89. **`packages/migrate/src/bin.ts`** -> AI Confidence: **99.18%**
90. **`packages/ts-builders/src/Method.ts`** -> AI Confidence: **99.18%**
91. **`packages/cli/scripts/preinstall-entry.js`** -> AI Confidence: **99.17%**
92. **`packages/adapter-mariadb/src/errors.ts`** -> AI Confidence: **99.17%**
93. **`packages/client-generator-ts/src/utils/addPreamble.ts`** -> AI Confidence: **99.17%**
94. **`packages/client/src/runtime/highlight/prism.ts`** -> AI Confidence: **99.17%**
95. **`packages/client/tests/functional/issues/22947-sqlite-conccurrent-upsert/prisma/_schema.ts`** -> AI Confidence: **99.17%**
96. **`packages/client/tests/functional/relationMode-in-separate-gh-action/prisma/_schema_1_to_n.ts`** -> AI Confidence: **99.17%**
97. **`packages/internals/src/highlight/prism.ts`** -> AI Confidence: **99.17%**
98. **`packages/migrate/src/__tests__/setup.ts`** -> AI Confidence: **99.17%**
99. **`packages/param-graph/src/serialization.ts`** -> AI Confidence: **99.17%**
100. **`scripts/run-studio.ts`** -> AI Confidence: **99.17%**
101. **`packages/cli/src/SubCommand.ts`** -> AI Confidence: **99.16%**
102. **`packages/client-generator-js/src/TSClient/PrismaClient.ts`** -> AI Confidence: **99.16%**
103. **`packages/client-generator-js/src/TSClient/TSClient.ts`** -> AI Confidence: **99.16%**
104. **`packages/client-generator-js/src/generateClient.ts`** -> AI Confidence: **99.16%**
105. **`packages/client/src/runtime/core/engines/client/ClientEngine.ts`** -> AI Confidence: **99.16%**
106. **`packages/client/src/runtime/core/errorRendering/ArgumentsRenderingTree.ts`** -> AI Confidence: **99.16%**
107. **`packages/client/src/runtime/getPrismaClient.ts`** -> AI Confidence: **99.16%**
108. **`packages/client/src/utils/generateInFolder.ts`** -> AI Confidence: **99.16%**
109. **`packages/client/tests/functional/_utils/setupTestSuiteClient.ts`** -> AI Confidence: **99.16%**
110. **`packages/client/tests/functional/driver-adapters/validate-active-provider/tests.ts`** -> AI Confidence: **99.16%**
111. **`packages/client/tests/functional/tracing/tests.ts`** -> AI Confidence: **99.16%**
112. **`packages/query-plan-executor/src/server/middleware/client-telemetry.ts`** -> AI Confidence: **99.16%**
113. **`packages/ts-builders/src/ConditionalType.test.ts`** -> AI Confidence: **99.16%**
114. **`packages/adapter-planetscale/src/planetscale.ts`** -> AI Confidence: **99.15%**
115. **`packages/cli/src/Version.ts`** -> AI Confidence: **99.15%**
116. **`packages/cli/src/__tests__/incomplete-schemas.test.ts`** -> AI Confidence: **99.15%**
117. **`packages/cli/src/management-api/auth.ts`** -> AI Confidence: **99.15%**
118. **`packages/client-generator-js/src/TSClient/Input.ts`** -> AI Confidence: **99.15%**
119. **`packages/client-generator-js/src/generator.ts`** -> AI Confidence: **99.15%**
120. **`packages/client-generator-ts/src/TSClient/Input.ts`** -> AI Confidence: **99.15%**
121. **`packages/client-generator-ts/src/TSClient/TypeMap.ts`** -> AI Confidence: **99.15%**
122. **`packages/client-generator-ts/src/TSClient/file-generators/PrismaNamespaceFile.ts`** -> AI Confidence: **99.15%**
123. **`packages/client-generator-ts/src/file-extensions.ts`** -> AI Confidence: **99.15%**
124. **`packages/client-generator-ts/src/generator.ts`** -> AI Confidence: **99.15%**
125. **`packages/client/src/runtime/core/model/applyFluent.ts`** -> AI Confidence: **99.15%**
126. **`packages/config/src/__tests__/loadConfigFromFile.test.ts`** -> AI Confidence: **99.15%**
127. **`packages/fetch-engine/src/downloadZip.ts`** -> AI Confidence: **99.15%**
128. **`packages/internals/src/__tests__/engine-commands/formatSchema.test.ts`** -> AI Confidence: **99.15%**
129. **`packages/internals/src/cli/getSchema.ts`** -> AI Confidence: **99.15%**
130. **`packages/internals/src/utils/getGitHubIssueUrl.ts`** -> AI Confidence: **99.15%**
131. **`packages/migrate/src/Migrate.ts`** -> AI Confidence: **99.15%**
132. **`packages/migrate/src/SchemaEngineCLI.ts`** -> AI Confidence: **99.15%**
133. **`packages/migrate/src/commands/DbDrop.ts`** -> AI Confidence: **99.15%**
134. **`packages/migrate/src/commands/MigrateDeploy.ts`** -> AI Confidence: **99.15%**
135. **`packages/migrate/src/commands/MigrateStatus.ts`** -> AI Confidence: **99.15%**
136. **`packages/query-plan-executor/src/logic/app.ts`** -> AI Confidence: **99.15%**
137. **`sandbox/studio/prisma.config.ts`** -> AI Confidence: **99.15%**
138. **`packages/client-engine-runtime/src/interpreter/data-mapper.ts`** -> AI Confidence: **99.13%**
139. **`packages/client-generator-js/src/TSClient/Payload.ts`** -> AI Confidence: **99.13%**
140. **`packages/client-generator-ts/src/TSClient/Payload.ts`** -> AI Confidence: **99.13%**
141. **`packages/client/src/runtime/core/extensions/MergedExtensionsList.ts`** -> AI Confidence: **99.13%**
142. **`packages/client/src/runtime/core/extensions/applyResultExtensions.ts`** -> AI Confidence: **99.13%**
143. **`packages/client/src/runtime/utils/createErrorMessageWithContext.ts`** -> AI Confidence: **99.13%**
144. **`packages/client/src/runtime/utils/validatePrismaClientOptions.ts`** -> AI Confidence: **99.13%**
145. **`packages/client/tests/functional/logging/tests.ts`** -> AI Confidence: **99.13%**
146. **`packages/internals/src/__tests__/engine-commands/getDmmf.test.ts`** -> AI Confidence: **99.13%**
147. **`packages/internals/src/convertCredentials.ts`** -> AI Confidence: **99.13%**
148. **`packages/internals/src/getPackedPackage.ts`** -> AI Confidence: **99.13%**
149. **`packages/migrate/src/__tests__/DbPull/postgresql-extensions.test.ts`** -> AI Confidence: **99.13%**
150. **`packages/migrate/src/__tests__/introspection/introspection.test.ts`** -> AI Confidence: **99.13%**
151. **`packages/client-generator-js/src/utils/buildDebugInitialization.ts`** -> AI Confidence: **99.11%**
152. **`packages/client-generator-ts/src/utils/buildDebugInitialization.ts`** -> AI Confidence: **99.11%**
153. **`packages/client/src/__tests__/integration/errors/client-version-error/test.ts`** -> AI Confidence: **99.11%**
154. **`packages/client/tests/functional/typed-sql/postgres-scalars-nullable/prisma/_schema.ts`** -> AI Confidence: **99.11%**
155. **`eslint.config.cjs`** -> AI Confidence: **99.09%**
156. **`packages/nextjs-monorepo-workaround-plugin/index.js`** -> AI Confidence: **99.09%**
157. **`packages/adapter-libsql/src/conversion.ts`** -> AI Confidence: **99.09%**
158. **`packages/adapter-neon/src/conversion.ts`** -> AI Confidence: **99.09%**
159. **`packages/adapter-planetscale/src/conversion.ts`** -> AI Confidence: **99.09%**
160. **`packages/cli/src/bootstrap/telemetry.ts`** -> AI Confidence: **99.09%**
161. **`packages/cli/src/postgres/link/__tests__/Link.vitest.ts`** -> AI Confidence: **99.09%**
162. **`packages/cli/src/utils/client-output-path.ts`** -> AI Confidence: **99.09%**
163. **`packages/cli/src/utils/printUpdateMessage.ts`** -> AI Confidence: **99.09%**
164. **`packages/client-common/src/index.ts`** -> AI Confidence: **99.09%**
165. **`packages/client-engine-runtime/src/index.ts`** -> AI Confidence: **99.09%**
166. **`packages/client-engine-runtime/src/interpreter/validation.ts`** -> AI Confidence: **99.09%**
167. **`packages/client-generator-js/src/GenericsArgsInfo.ts`** -> AI Confidence: **99.09%**
168. **`packages/client-generator-ts/src/GenericsArgsInfo.ts`** -> AI Confidence: **99.09%**
169. **`packages/client-generator-ts/src/TSClient/TSClient.ts`** -> AI Confidence: **99.09%**
170. **`packages/client-generator-ts/src/TSClient/file-generators/ClassFile.ts`** -> AI Confidence: **99.09%**
171. **`packages/client-generator-ts/src/utils/wasm.ts`** -> AI Confidence: **99.09%**
172. **`packages/client/src/__tests__/benchmarks/huge-schema/builder.ts`** -> AI Confidence: **99.09%**
173. **`packages/client/src/runtime/core/engines/accelerate/HeaderBuilder.ts`** -> AI Confidence: **99.09%**
174. **`packages/client/src/runtime/core/extensions/visitQueryResult.ts`** -> AI Confidence: **99.09%**
175. **`packages/client/src/runtime/core/types/exported/index.ts`** -> AI Confidence: **99.09%**
176. **`packages/client/src/runtime/index.ts`** -> AI Confidence: **99.09%**
177. **`packages/client/tests/e2e/prisma-client-imports-postgres/src/default.ts`** -> AI Confidence: **99.09%**
178. **`packages/client/tests/e2e/prisma-client-imports-postgres/src/no-dep.ts`** -> AI Confidence: **99.09%**
179. **`packages/client/tests/e2e/sqlcommenter-trace-context/src/index.ts`** -> AI Confidence: **99.09%**
180. **`packages/client/tests/functional/0-legacy-ports/aggregations/tests.ts`** -> AI Confidence: **99.09%**
181. **`packages/client/tests/functional/default-selection/prisma/_schema.ts`** -> AI Confidence: **99.09%**
182. **`packages/client/tests/functional/issues/14271/prisma/_schema.ts`** -> AI Confidence: **99.09%**
183. **`packages/client/tests/functional/issues/29331-query-plan-cache-bloat/tests.ts`** -> AI Confidence: **99.09%**
184. **`packages/client/tests/functional/query-validation/tests.ts`** -> AI Confidence: **99.09%**
185. **`packages/client/tests/functional/relation-load-strategy-unsupported/preview-feature-disabled.ts`** -> AI Confidence: **99.09%**
186. **`packages/client/tests/functional/relation-load-strategy-unsupported/unsupported-strategy-for-db.ts`** -> AI Confidence: **99.09%**
187. **`packages/client/tests/functional/tracing-filtered-spans/tests.ts`** -> AI Confidence: **99.09%**
188. **`packages/client/tests/functional/tracing-no-sampling/tests.ts`** -> AI Confidence: **99.09%**
189. **`packages/generator-helper/src/generatorHandler.ts`** -> AI Confidence: **99.09%**
190. **`packages/internals/src/cli/directoryConfig.ts`** -> AI Confidence: **99.09%**
191. **`packages/internals/src/engine-commands/getDmmf.ts`** -> AI Confidence: **99.09%**
192. **`packages/internals/src/engine-commands/mergeSchemas.ts`** -> AI Confidence: **99.09%**
193. **`packages/internals/src/engine-commands/validate.ts`** -> AI Confidence: **99.09%**
194. **`packages/internals/src/index.ts`** -> AI Confidence: **99.09%**
195. **`packages/internals/src/schemaEngineCommands.ts`** -> AI Confidence: **99.09%**
196. **`packages/migrate/src/__tests__/DbPull/sqlite.test.ts`** -> AI Confidence: **99.09%**
197. **`packages/migrate/src/index.ts`** -> AI Confidence: **99.09%**
198. **`packages/migrate/src/utils/promptForMigrationName.ts`** -> AI Confidence: **99.09%**
199. **`packages/param-graph-builder/src/dmmf-traverser.ts`** -> AI Confidence: **99.09%**
200. **`packages/query-plan-executor/src/index.ts`** -> AI Confidence: **99.09%**
201. **`packages/ts-builders/src/IntersectionType.test.ts`** -> AI Confidence: **99.09%**
202. **`packages/ts-builders/src/index.ts`** -> AI Confidence: **99.09%**
203. **`packages/ts-builders/src/stringify.ts`** -> AI Confidence: **99.09%**
204. **`packages/adapter-d1/src/d1-worker.ts`** -> AI Confidence: **99.08%**
205. **`packages/adapter-d1/src/d1.test.ts`** -> AI Confidence: **99.08%**
206. **`packages/cli/src/bootstrap/__tests__/Bootstrap.vitest.ts`** -> AI Confidence: **99.08%**
207. **`packages/cli/src/mcp/MCP.ts`** -> AI Confidence: **99.08%**
208. **`packages/client-runtime-utils/src/errors/index.ts`** -> AI Confidence: **99.08%**
209. **`packages/client/src/__tests__/benchmarks/query-performance/caching.bench.ts`** -> AI Confidence: **99.08%**
210. **`packages/client/src/__tests__/benchmarks/query-performance/query-performance.bench.ts`** -> AI Confidence: **99.08%**
211. **`packages/client/src/runtime/core/model/applyModel.ts`** -> AI Confidence: **99.08%**
212. **`packages/client/src/runtime/core/types/index.ts`** -> AI Confidence: **99.08%**
213. **`packages/client/tests/e2e/prisma-client-imports-mysql/src/default.ts`** -> AI Confidence: **99.08%**
214. **`packages/client/tests/e2e/prisma-client-imports-postgres/src/dep.ts`** -> AI Confidence: **99.08%**
215. **`packages/client/tests/e2e/prisma-client-imports-sqlite/src/default.ts`** -> AI Confidence: **99.08%**
216. **`packages/client/tests/e2e/prisma-client-imports-sqlite/src/dep.ts`** -> AI Confidence: **99.08%**
217. **`packages/client/tests/e2e/prisma-client-imports-sqlite/src/no-dep.ts`** -> AI Confidence: **99.08%**
218. **`packages/client/tests/functional/_utils/setupTestSuiteEnv.ts`** -> AI Confidence: **99.08%**
219. **`packages/client/tests/functional/relation-load-strategy/supported-queries.ts`** -> AI Confidence: **99.08%**
220. **`packages/client/tests/functional/tracing-disabled/tests.ts`** -> AI Confidence: **99.08%**
221. **`packages/client/tests/functional/unixepoch-ms-datetime/tests.ts`** -> AI Confidence: **99.08%**
222. **`packages/driver-adapter-utils/src/index.ts`** -> AI Confidence: **99.08%**
223. **`packages/internals/src/engine-commands/getEnginesInfo.ts`** -> AI Confidence: **99.08%**
224. **`packages/internals/src/engine-commands/index.ts`** -> AI Confidence: **99.08%**
225. **`packages/migrate/src/__tests__/Baseline.test.ts`** -> AI Confidence: **99.08%**
226. **`packages/migrate/src/__tests__/MigrateDev.test.ts`** -> AI Confidence: **99.08%**
227. **`packages/migrate/src/__tests__/rpc.test.ts`** -> AI Confidence: **99.08%**
228. **`packages/migrate/src/commands/MigrateDev.ts`** -> AI Confidence: **99.08%**
229. **`packages/migrate/src/views/handleViewsIO.ts`** -> AI Confidence: **99.08%**
230. **`packages/query-plan-executor/src/server/server.ts`** -> AI Confidence: **99.08%**
231. **`packages/query-plan-executor/src/tracing/span.test.ts`** -> AI Confidence: **99.08%**
232. **`packages/ts-builders/src/ArrayType.test.ts`** -> AI Confidence: **99.08%**
233. **`packages/ts-builders/src/Class.test.ts`** -> AI Confidence: **99.08%**
234. **`packages/ts-builders/src/Interface.test.ts`** -> AI Confidence: **99.08%**
235. **`packages/ts-builders/src/KeyType.test.ts`** -> AI Confidence: **99.08%**
236. **`packages/ts-builders/src/KeyofType.test.ts`** -> AI Confidence: **99.08%**
237. **`packages/ts-builders/src/Method.test.ts`** -> AI Confidence: **99.08%**
238. **`sandbox/tracing/otelSetup.ts`** -> AI Confidence: **99.08%**
239. **`packages/cli/src/__tests__/commands/SubCommand.vitest.ts`** -> AI Confidence: **99.07%**
240. **`packages/cli/src/utils/nps/survey.ts`** -> AI Confidence: **99.07%**
241. **`packages/client-engine-runtime/src/transaction-manager/transaction-manager.test.ts`** -> AI Confidence: **99.07%**
242. **`packages/client-generator-js/src/TSClient/Count.ts`** -> AI Confidence: **99.07%**
243. **`packages/client-generator-ts/src/TSClient/PrismaClient.ts`** -> AI Confidence: **99.07%**
244. **`packages/client-generator-ts/src/typedSql/typedSql.ts`** -> AI Confidence: **99.07%**
245. **`packages/client/src/runtime/core/engines/common/Engine.ts`** -> AI Confidence: **99.07%**
246. **`packages/client/tests/functional/0-legacy-ports/batch-find-unique/tests.ts`** -> AI Confidence: **99.07%**
247. **`packages/client/tests/functional/batching/tests.ts`** -> AI Confidence: **99.07%**
248. **`packages/client/tests/functional/extensions/model.ts`** -> AI Confidence: **99.07%**
249. **`packages/internals/src/engine-commands/getConfig.ts`** -> AI Confidence: **99.07%**
250. **`packages/internals/src/engine-commands/queryEngineCommons.ts`** -> AI Confidence: **99.07%**
251. **`packages/internals/src/sendPanic.ts`** -> AI Confidence: **99.07%**
252. **`packages/migrate/src/__tests__/DbPull/postgresql-views.test.ts`** -> AI Confidence: **99.07%**
253. **`packages/migrate/src/__tests__/DbPush.test.ts`** -> AI Confidence: **99.07%**
254. **`packages/migrate/src/__tests__/MigrateDiff.test.ts`** -> AI Confidence: **99.07%**
255. **`packages/migrate/src/commands/MigrateReset.ts`** -> AI Confidence: **99.07%**
256. **`packages/query-plan-executor/src/tracing/handler.test.ts`** -> AI Confidence: **99.07%**
257. **`packages/query-plan-executor/src/tracing/integration.test.ts`** -> AI Confidence: **99.07%**
258. **`.github/scripts/create-git-tag.mjs`** -> AI Confidence: **99.06%**
259. **`.github/workflows/scripts/auto-close-github-discussions.js`** -> AI Confidence: **99.06%**
260. **`.github/workflows/scripts/detect-jobs-to-run.js`** -> AI Confidence: **99.06%**
261. **`packages/client/scripts/colors.js`** -> AI Confidence: **99.06%**
262. **`packages/client/src/utils/compilerWorker.js`** -> AI Confidence: **99.06%**
263. **`packages/client/tests/e2e/nextjs-schema-not-found/11_monorepo-noServerComponents-noCustomOutput-reExportIndirect/packages/service/next.config.js`** -> AI Confidence: **99.06%**
264. **`packages/client/tests/e2e/nextjs-schema-not-found/12_monorepo-serverComponents-noCustomOutput-reExportIndirect/packages/service/next.config.js`** -> AI Confidence: **99.06%**
265. **`packages/client/tests/e2e/nextjs-schema-not-found/13_monorepo-noServerComponents-customOutput-reExportDirect/packages/service/next.config.js`** -> AI Confidence: **99.06%**
266. **`packages/client/tests/e2e/nextjs-schema-not-found/14_monorepo-serverComponents-customOutput-reExportDirect/packages/service/next.config.js`** -> AI Confidence: **99.06%**
267. **`packages/client/tests/e2e/nextjs-schema-not-found/15_monorepo-noServerComponents-customOutput-reExportIndirect/packages/service/next.config.js`** -> AI Confidence: **99.06%**
268. **`packages/client/tests/e2e/nextjs-schema-not-found/16_monorepo-serverComponents-customOutput-reExportIndirect/packages/service/next.config.js`** -> AI Confidence: **99.06%**
269. **`packages/client/tests/e2e/nextjs-schema-not-found/17_monorepo-noServerComponents-customOutput-reExportIndirect-ts/packages/service/next.config.js`** -> AI Confidence: **99.06%**
270. **`packages/client/tests/e2e/nextjs-schema-not-found/18_monorepo-serverComponents-customOutput-reExportIndirect-ts/packages/service/next.config.js`** -> AI Confidence: **99.06%**
271. **`packages/client/tests/functional/jest.config.js`** -> AI Confidence: **99.06%**
272. **`packages/migrate/src/__tests__/fixtures/seed-from-prisma-config/seed-sqlite-js-extra-args/prisma/seed.js`** -> AI Confidence: **99.06%**
273. **`helpers/compile/plugins/fill-plugin/fillers/buffer-small.ts`** -> AI Confidence: **99.06%**
274. **`packages/adapter-better-sqlite3/src/conversion.ts`** -> AI Confidence: **99.06%**
275. **`packages/adapter-better-sqlite3/src/errors.ts`** -> AI Confidence: **99.06%**
276. **`packages/adapter-d1/src/conversion.ts`** -> AI Confidence: **99.06%**
277. **`packages/adapter-d1/src/errors.ts`** -> AI Confidence: **99.06%**
278. **`packages/adapter-libsql/src/errors.ts`** -> AI Confidence: **99.06%**
279. **`packages/adapter-mariadb/src/conversion.ts`** -> AI Confidence: **99.06%**
280. **`packages/adapter-mssql/src/connection-string.ts`** -> AI Confidence: **99.06%**
281. **`packages/adapter-mssql/src/conversion.ts`** -> AI Confidence: **99.06%**
282. **`packages/adapter-neon/src/errors.ts`** -> AI Confidence: **99.06%**
283. **`packages/adapter-pg/src/conversion.ts`** -> AI Confidence: **99.06%**
284. **`packages/adapter-pg/src/errors.ts`** -> AI Confidence: **99.06%**
285. **`packages/adapter-planetscale/src/errors.ts`** -> AI Confidence: **99.06%**
286. **`packages/adapter-ppg/src/errors.ts`** -> AI Confidence: **99.06%**
287. **`packages/cli/src/bootstrap/completion-output.ts`** -> AI Confidence: **99.06%**
288. **`packages/cli/src/bootstrap/project-state.ts`** -> AI Confidence: **99.06%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `packages/client/src/__tests__/buffer-small.test.ts` -> **97.9998%** Exposure
### Exploit Generation Surface
- `packages/nextjs-monorepo-workaround-plugin/index.js` -> **100.0%** Exposure
- `packages/adapter-neon/src/neon.ts` -> **100.0%** Exposure
- `packages/adapter-pg/src/pg.ts` -> **100.0%** Exposure
- `packages/cli/src/Generate.ts` -> **100.0%** Exposure
- `packages/cli/src/Studio.ts` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `scripts/only-allow-pnpm.js` -> **100.0%** Exposure
- `helpers/compile/plugins/resolvePathsPlugin.ts` -> **100.0%** Exposure
- `packages/adapter-mariadb/src/mariadb.ts` -> **100.0%** Exposure
- `packages/client/src/__tests__/benchmarks/huge-schema/huge-schema.bench.ts` -> **100.0%** Exposure
- `packages/client/src/__tests__/benchmarks/query-performance/qc-loader.ts` -> **100.0%** Exposure
### Hardcoded Payload Artifacts
- `packages/sqlcommenter-query-insights/src/parameterize/tests/security.test.ts` -> **23.958%** Exposure
### Algorithmic DoS Exposure
- `packages/nextjs-monorepo-workaround-plugin/index.js` -> **100.0%** Exposure
- `helpers/compile/plugins/fill-plugin/fillers/buffer-small.ts` -> **100.0%** Exposure
- `helpers/compile/plugins/replaceWithPlugin.ts` -> **100.0%** Exposure
- `packages/adapter-d1/src/d1-http.ts` -> **100.0%** Exposure
- `packages/adapter-mariadb/src/errors.test.ts` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `15` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `3101` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `packages/cli/src/management-api/auth.ts` (TYPESCRIPT) -> Cumulative Risk: **968.02**
- **Archetype:** `file_cluster_4` (Distance: 11.378 IQR)
- **Magnitude:** 17.21 | **LOC:** 144 | **CtrlFlow:** 32.6% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (99.9997%)
- **Heaviest Functions:** `handleCallback` (Impact: 61.6), `login` (Impact: 34.2), `login` (Impact: 3.3)

### 2. `packages/adapter-neon/src/neon.ts` (TYPESCRIPT) -> Cumulative Risk: **871.23**
- **Archetype:** `file_cluster_4` (Distance: 13.052 IQR)
- **Magnitude:** 50.66 | **LOC:** 329 | **CtrlFlow:** 31.8% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `performIO` (Impact: 62.6), `startTransaction` (Impact: 49.8), `performIO` (Impact: 19.0)

### 3. `packages/generator-helper/src/GeneratorProcess.ts` (TYPESCRIPT) -> Cumulative Risk: **868.71**
- **Archetype:** `file_cluster_4` (Distance: 13.668 IQR)
- **Magnitude:** 61.03 | **LOC:** 278 | **CtrlFlow:** 44.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `reject` (Impact: 372.1), `constructor` (Impact: 11.7)

### 4. `packages/client/src/runtime/getPrismaClient.ts` (TYPESCRIPT) -> Cumulative Risk: **867.99**
- **Archetype:** `file_cluster_13` (Distance: 13.508 IQR)
- **Magnitude:** 29.4 | **LOC:** 1070 | **CtrlFlow:** 38.9% | **Authorship Centralization:** 45.5%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `callback` (Impact: 82.2), `debug` (Impact: 14.1), `_createItxClient` (Impact: 10.1)

### 5. `packages/client/src/runtime/core/engines/client/ClientEngine.ts` (TYPESCRIPT) -> Cumulative Risk: **854.86**
- **Archetype:** `file_cluster_4` (Distance: 12.403 IQR)
- **Magnitude:** 36.76 | **LOC:** 774 | **CtrlFlow:** 38.7% | **Authorship Centralization:** 40.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `ensureStarted` (Impact: 71.6), `constructor` (Impact: 57.5), `transformRequestError` (Impact: 19.3)

### 6. `packages/client-generator-ts/src/TSClient/Model.ts` (TYPESCRIPT) -> Cumulative Risk: **852.62**
- **Archetype:** `file_cluster_13` (Distance: 12.605 IQR)
- **Magnitude:** 101.57 | **LOC:** 983 | **CtrlFlow:** 45.4% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.9956%)
- **Heaviest Functions:** `argsTypes` (Impact: 196.6), `toTS` (Impact: 113.8), `getAggregationTypes` (Impact: 92.2)

### 7. `packages/client/src/__tests__/benchmarks/query-performance/seed-data.ts` (TYPESCRIPT) -> Cumulative Risk: **849.37**
- **Archetype:** `file_cluster_8` (Distance: 11.759 IQR)
- **Magnitude:** 57.82 | **LOC:** 855 | **CtrlFlow:** 41.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `seedDatabase` (Impact: 105.3), `generateUser` (Impact: 30.0), `generateCategory` (Impact: 9.2)

### 8. `packages/adapter-pg/src/pg.ts` (TYPESCRIPT) -> Cumulative Risk: **847.53**
- **Archetype:** `file_cluster_4` (Distance: 13.679 IQR)
- **Magnitude:** 61.54 | **LOC:** 338 | **CtrlFlow:** 43.8% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `startTransaction` (Impact: 49.8), `performIO` (Impact: 46.2), `queryRaw` (Impact: 42.0)

### 9. `packages/client-generator-js/src/TSClient/Model.ts` (TYPESCRIPT) -> Cumulative Risk: **830.33**
- **Archetype:** `file_cluster_13` (Distance: 12.377 IQR)
- **Magnitude:** 96.94 | **LOC:** 960 | **CtrlFlow:** 45.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.9815%)
- **Heaviest Functions:** `argsTypes` (Impact: 196.6), `toTS` (Impact: 113.8), `getAggregationTypes` (Impact: 92.2)

### 10. `packages/client-engine-runtime/src/interpreter/query-interpreter.ts` (TYPESCRIPT) -> Cumulative Risk: **829.15**
- **Archetype:** `file_cluster_4` (Distance: 11.865 IQR)
- **Magnitude:** 123.51 | **LOC:** 607 | **CtrlFlow:** 46.8% | **Authorship Centralization:** 75.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `interpretNode` (Impact: 631.8), `attachChildrenToParents` (Impact: 59.3), `inferKeyCasts` (Impact: 38.2)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.166
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/client/fixtures/mongo/prisma/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.166
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/client/src/__tests__/integration/happy/browser/prisma/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.166
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/config/src/__tests__/fixtures/loadConfigFromFile/env-load-cjs/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.166
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/config/src/__tests__/fixtures/loadConfigFromFile/env-load-esm/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.166
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/internals/src/__tests__/__fixtures__/dotenv/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.166
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/migrate/src/__tests__/fixtures/schema-only-cockroachdb/prisma/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.166
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/migrate/src/__tests__/fixtures/schema-only-postgresql/prisma/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.166
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `.github/workflows/scripts/auto-close-github-discussions.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.939 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 5.468 IQR)
- **Top Global Matches:** file_cluster_8: 9.939, file_cluster_17: 10.342, file_cluster_4: 10.466
- **Magnitude:** 307.98 | **LOC:** 267 | **CtrlFlow:** 65.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (25.5132%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `run` (Impact: 278.5 | O(N^6) | DB: 12)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 20`, `args: 19`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 1`, `state_mutation: 12`
* *Architecture:* `concurrency: 13`, `import: 2`
* *Defense:* `safety: 10`, `immutability_locks: 29`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.166
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` graphql, rest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/client/src/runtime/core/errorRendering/applyValidationError.test.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.452 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.324 IQR)
- **Top Global Matches:** file_cluster_8: 10.452, file_cluster_7: 11.171, file_cluster_1: 11.272
- **Magnitude:** 159.35 | **LOC:** 3621 | **CtrlFlow:** 71.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (7.5402%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 316.7 | O(N^4))
  * `describe` (Impact: 305.5 | O(N^4))
  * `describe` (Impact: 201.0 | O(N^4))
  * `describe` (Impact: 199.7 | O(N^4))
  * `describe` (Impact: 138.2 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 305`, `structural_boundaries: 120`, `args: 153`, `func_start: 221`
* *Risk/State:* `duplicate_logic: 14`
* *Architecture:* `io: 3`, `import: 9`
* *Defense:* `safety: 39`, `test: 150`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.166
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` serializeJsonQuery, colors, ValidationError, JsApi, ArgumentsRenderingTree, applyValidationError, base, ts-builders...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/client/src/__tests__/buffer-small.test.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.952 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.985 IQR)
- **Top Global Matches:** file_cluster_8: 10.952, file_cluster_17: 11.578, file_cluster_7: 11.58
- **Magnitude:** 152.77 | **LOC:** 6236 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 22
- **Risk Profile:** Cognitive Load (4.8655%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test` (Impact: 194.0 | O(2^N) | DB: 22)
    * *Intent:* ;[NaN, 1.01].forEach((offset) => {
  * `test` (Impact: 92.3 | O(2^N) | DB: 9)
  * `test` (Impact: 83.8 | O(2^N) | DB: 3)
  * `test` (Impact: 73.7 | O(2^N) | DB: 2)
  * `test` (Impact: 66.5 | O(2^N) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 121`, `structural_boundaries: 664`, `args: 928`, `func_start: 922`
* *Risk/State:* `safety_bypasses: 100`, `state_mutation: 208`, `dead_code: 2`, `fragile_debt: 4`, `duplicate_logic: 130`
* *Architecture:* `import: 5`
* *Defense:* `safety: 60`, `doc: 3`, `test: 786`, `immutability_locks: 645`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.166
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` buffer-small, buffer, assert, crypto
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/internals/src/highlight/prism.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.986 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 5.061 IQR)
- **Top Global Matches:** file_cluster_13: 11.986, file_cluster_4: 11.987, file_cluster_11: 12.024
- **Magnitude:** 147.52 | **LOC:** 517 | **CtrlFlow:** 72.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (68.1523%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `matchGrammar` (Impact: 1105.9 | O(N^3) | DB: 14)
  * `DFS` (Impact: 108.4 | O(2^N))
  * `deepClone` (Impact: 78.3 | O(2^N) | DB: 1)
  * `insertBefore` (Impact: 57.6 | O(N^4))
  * `encode` (Impact: 30.6 | O(2^N))
    * *Intent:* /** * Prism: Lightweight, robust, elegant syntax highlighting * MIT license http://www.opensource.or...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 231`, `structural_boundaries: 86`, `args: 20`, `func_start: 17`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 48`
* *Architecture:* `api: 10`, `concurrency: 13`, `import: 4`
* *Defense:* `safety: 18`, `doc: 8`, `immutability_locks: 22`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.166
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` theme
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/client/tests/functional/query-validation/tests.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.972 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.793 IQR)
- **Top Global Matches:** file_cluster_8: 9.972, file_cluster_4: 10.636, file_cluster_7: 10.739
- **Magnitude:** 131.23 | **LOC:** 495 | **CtrlFlow:** 63.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (43.0103%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test` (Impact: 335.4 | O(2^N))
  * `test` (Impact: 230.4 | O(2^N))
  * `test` (Impact: 192.1 | O(2^N))
  * `test` (Impact: 148.9 | O(2^N))
  * `test` (Impact: 148.6 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 112`, `structural_boundaries: 64`, `args: 36`, `func_start: 17`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 1`, `planned_debt: 1`, `duplicate_logic: 16`
* *Architecture:* `io: 1`, `concurrency: 50`, `import: 3`
* *Defense:* `safety: 15`, `test: 50`, `immutability_locks: 33`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.166
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` _matrix, _common, client
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/client-engine-runtime/src/interpreter/query-interpreter.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.865 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.103 IQR)
- **Top Global Matches:** file_cluster_4: 11.865, file_cluster_13: 12.232, file_cluster_17: 12.313
- **Magnitude:** 123.51 | **LOC:** 607 | **CtrlFlow:** 46.8% | **Authorship Centralization:** 75.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 30
- **Risk Profile:** Cognitive Load (98.6239%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `interpretNode` (Impact: 631.8 | O(2^N) | DB: 30)
  * `attachChildrenToParents` (Impact: 59.3 | O(N^2) | DB: 2)
  * `inferKeyCasts` (Impact: 38.2 | O(N^2) | DB: 1)
  * `evalFieldOperation` (Impact: 34.6 | O(N^2))
  * `evaluateProcessingParameters` (Impact: 23.1 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 152`, `structural_boundaries: 173`, `args: 49`, `func_start: 32`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 100`
* *Architecture:* `io: 6`, `api: 7`, `concurrency: 199`, `import: 19`
* *Defense:* `safety: 25`, `immutability_locks: 71`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.306
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` generators, serialize-sql, sqlcommenter, events, sql-commenter, schema, render-query, validation...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `packages/client/src/runtime/highlight/prism.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.074 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 5.144 IQR)
- **Top Global Matches:** file_cluster_4: 12.074, file_cluster_13: 12.1, file_cluster_11: 12.114
- **Magnitude:** 118.14 | **LOC:** 497 | **CtrlFlow:** 72.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (82.02%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `matchGrammar` (Impact: 809.4 | O(N^2) | DB: 14)
  * `DFS` (Impact: 108.4 | O(2^N))
  * `deepClone` (Impact: 78.3 | O(2^N) | DB: 1)
  * `insertBefore` (Impact: 57.6 | O(N^4))
  * `encode` (Impact: 30.6 | O(2^N))
    * *Intent:* /** * Prism: Lightweight, robust, elegant syntax highlighting * MIT license http://www.opensource.or...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 226`, `structural_boundaries: 87`, `args: 20`, `func_start: 17`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 51`
* *Architecture:* `api: 10`, `concurrency: 13`, `import: 4`
* *Defense:* `safety: 18`, `doc: 6`, `immutability_locks: 20`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.166
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` theme
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/client/tests/functional/extensions/query.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_2` (Drift: 11.147 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.487 IQR)
- **Top Global Matches:** file_cluster_2: 11.147, file_cluster_8: 11.351, file_cluster_16: 11.478
- **Magnitude:** 115.21 | **LOC:** 2098 | **CtrlFlow:** 23.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (62.8695%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test` (Impact: 494.4 | O(N^5))
  * `testIf` (Impact: 48.3 | O(N^4) | DB: 4)
    * *Intent:* // TODO: skipped for PlanetScale adapter because of https://github.com/prisma/team-orm/issues/495 //...
  * `test` (Impact: 41.2 | O(N^4))
  * `async` (Impact: 37.9 | O(2^N) | DB: 2)
  * `async` (Impact: 36.8 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 124`, `structural_boundaries: 409`, `args: 524`, `func_start: 523`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 39`, `planned_debt: 4`, `duplicate_logic: 27`, `orphaned_logic: 2`
* *Architecture:* `io: 4`, `concurrency: 240`, `import: 9`
* *Defense:* `safety: 24`, `doc: 1`, `test: 120`, `immutability_locks: 211`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.166
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` expect-type, _matrix, internals, providers, types, client, wait, waitFor...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `.github/workflows/scripts/detect-jobs-to-run.js` (JAVASCRIPT | Tier 0 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.013 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.958 IQR)
- **Top Global Matches:** file_cluster_17: 13.013, file_cluster_4: 13.263, file_cluster_13: 13.304
- **Magnitude:** 107.38 | **LOC:** 62 | **CtrlFlow:** 68.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 20
- **Risk Profile:** Cognitive Load (59.2775%), Tech Debt (99.9837%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 56.5 | O(N^2) | DB: 20)
  * `main` (Impact: 1.9 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 8`, `args: 9`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 45`, `duplicate_logic: 2`
* *Architecture:* `io: 3`, `concurrency: 3`, `import: 2`
* *Defense:* `safety: 1`, `doc: 2`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.166
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` fs, consumers
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/internals/src/highlight/types.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_2` (Drift: 8.992 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.488 IQR)
- **Top Global Matches:** file_cluster_2: 8.992, file_cluster_16: 9.185, file_cluster_8: 9.237
- **Magnitude:** 106.99 | **LOC:** 40 | **CtrlFlow:** 58.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (26.8941%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 19`, `args: 13`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.166
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `helpers/compile/plugins/fill-plugin/fillers/buffer-small.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.146 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.089 IQR)
- **Top Global Matches:** file_cluster_8: 13.146, file_cluster_17: 13.151, file_cluster_11: 13.235
- **Magnitude:** 103.63 | **LOC:** 707 | **CtrlFlow:** 57.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 92
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (8.206%)
**Top Internal Functions/Classes:**
  * `writeUIntLE` (Impact: 688.1 | O(2^N) | DB: 92)
  * `stringToBuffer` (Impact: 29.4 | O(N^1) | DB: 2)
  * `initReadMethods` (Impact: 16.5 | O(N^1) | DB: 4)
  * `assertUnsigned` (Impact: 8.4 | O(N^1))
  * `assertBounds` (Impact: 7.2 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 142`, `structural_boundaries: 105`, `args: 206`, `func_start: 190`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 244`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `api: 7`, `import: 3`
* *Defense:* `safety: 21`, `doc: 1`, `immutability_locks: 51`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.237
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/client-generator-ts/src/TSClient/Model.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.605 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.948 IQR)
- **Top Global Matches:** file_cluster_13: 12.605, file_cluster_17: 12.639, file_cluster_8: 12.702
- **Magnitude:** 101.57 | **LOC:** 983 | **CtrlFlow:** 45.4% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 44
- **Risk Profile:** Cognitive Load (75.1882%), Tech Debt (20.7969%)
**Top Internal Functions/Classes:**
  * `argsTypes` (Impact: 196.6 | O(2^N) | DB: 31)
  * `toTS` (Impact: 113.8 | O(N^3) | DB: 6)
  * `getAggregationTypes` (Impact: 92.2 | O(N^4) | DB: 18)
  * `toTS` (Impact: 81.6 | O(2^N) | DB: 44)
  * `buildFluentWrapperDefinition` (Impact: 80.8 | O(N^3) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 166`, `structural_boundaries: 200`, `args: 59`, `func_start: 36`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 308`, `duplicate_logic: 4`
* *Architecture:* `io: 1`, `api: 10`, `concurrency: 21`, `import: 20`
* *Defense:* `safety: 25`, `doc: 15`, `immutability_locks: 81`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.166
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` dmmf, constants, TSClient, helpers, indent-string, SelectIncludeOmit, utils, ts-builders...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/client/tests/functional/relation-load-strategy-unsupported/preview-feature-disabled.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.538 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.209 IQR)
- **Top Global Matches:** file_cluster_8: 10.538, file_cluster_4: 10.984, file_cluster_7: 11.264
- **Magnitude:** 100.57 | **LOC:** 523 | **CtrlFlow:** 55.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (57.597%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describeIf` (Impact: 906.6 | O(2^N) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 72`, `args: 35`, `func_start: 17`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* `concurrency: 84`, `import: 3`
* *Defense:* `safety: 16`, `test: 60`, `immutability_locks: 1`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.166
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` _matrix, client, providers
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/client-generator-js/src/TSClient/Model.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.377 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.869 IQR)
- **Top Global Matches:** file_cluster_13: 12.377, file_cluster_8: 12.477, file_cluster_16: 12.481
- **Magnitude:** 96.94 | **LOC:** 960 | **CtrlFlow:** 45.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 41
- **Risk Profile:** Cognitive Load (53.2775%), Tech Debt (21.1157%)
**Top Internal Functions/Classes:**
  * `argsTypes` (Impact: 196.6 | O(2^N) | DB: 31)
  * `toTS` (Impact: 113.8 | O(N^3) | DB: 6)
  * `getAggregationTypes` (Impact: 92.2 | O(N^4) | DB: 18)
  * `toTS` (Impact: 81.5 | O(2^N) | DB: 41)
  * `buildFluentWrapperDefinition` (Impact: 80.8 | O(N^3) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 163`, `structural_boundaries: 195`, `args: 52`, `func_start: 34`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 273`, `duplicate_logic: 4`
* *Architecture:* `io: 1`, `api: 11`, `concurrency: 21`, `import: 21`
* *Defense:* `safety: 22`, `doc: 16`, `immutability_locks: 81`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.166
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` dmmf, constants, TSClient, helpers, indent-string, SelectIncludeOmit, utils, ts-builders...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/client/src/runtime/highlight/types.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.099 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 2.36 IQR)
- **Top Global Matches:** file_cluster_8: 7.099, file_cluster_7: 8.223, file_cluster_1: 8.45
- **Magnitude:** 95.86 | **LOC:** 38 | **CtrlFlow:** 58.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (29.5836%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 18`, `args: 12`, `func_start: 1`, `class_start: 2`
* *Risk/State:* None
* *Architecture:* `api: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.166
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/client/tests/functional/_utils/setupTestSuiteMatrix.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.266 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 6.037 IQR)
- **Top Global Matches:** file_cluster_13: 11.266, file_cluster_4: 11.315, file_cluster_8: 11.467
- **Magnitude:** 84.56 | **LOC:** 316 | **CtrlFlow:** 44.1% | **Authorship Centralization:** 71.4%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (49.8254%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `tests` (Impact: 793.0 | O(2^N) | DB: 16)
    * *Intent:* /** * How does this work from a high level? What steps?
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 57`, `args: 35`, `func_start: 26`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 10`
* *Architecture:* `io: 6`, `api: 2`, `concurrency: 36`, `import: 14`
* *Defense:* `safety: 18`, `doc: 2`, `test: 1`, `immutability_locks: 27`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.093
  * `Choke Point (Betweenness):` 0.002277 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` types, promises, checkMissingProviders, getPrismaClient, getTestSuitePlan, getTestSuiteInfo, qpe-worker, node:worker_threads...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/client/tests/functional/relation-load-strategy/unsupported-queries.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.884 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.083 IQR)
- **Top Global Matches:** file_cluster_8: 9.884, file_cluster_4: 10.587, file_cluster_7: 10.677
- **Magnitude:** 77.5 | **LOC:** 302 | **CtrlFlow:** 61.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (42.9969%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describeIf` (Impact: 736.7 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 45`, `args: 19`, `func_start: 9`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `concurrency: 32`, `import: 4`
* *Defense:* `safety: 8`, `test: 30`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.166
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` _common, client, _matrix, providers
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `packages/migrate/src/__tests__/fixtures/schema-only-cockroachdb/invalid-url.config.ts` (TYPESCRIPT) | Magnitude: 1.57 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 4, structural_boundaries: 3, io: 3, branch: 2
- `packages/client/tests/e2e/typed-sql/src/index.ts` (TYPESCRIPT) | Magnitude: 0.57 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 9, structural_boundaries: 5, decorators: 4, immutability_locks: 4
- `packages/client/tests/functional/_utils/getTestSuiteInfo.ts` (TYPESCRIPT) | Magnitude: 32.18 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 182, branch: 58, structural_boundaries: 55, immutability_locks: 46
- `packages/query-plan-executor/src/logic/adapter.ts` (TYPESCRIPT) | Magnitude: 13.41 | Delta: **0.043 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 70, structural_boundaries: 30, branch: 22, args: 22
- `packages/migrate/src/CLI.ts` (TYPESCRIPT) | Magnitude: 10.38 | Delta: **0.056 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 45, structural_boundaries: 16, state_mutation: 15, branch: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `packages/client-generator-ts/src/TSClient/NullTypes.ts` (TYPESCRIPT) | Magnitude: 2.05 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 8, events: 6, listeners: 6, api: 5
- `eslint.config.cjs` (JAVASCRIPT) | Magnitude: 25.1 | Delta: **0.216 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 140, doc: 45, decorators: 28, events: 26

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `packages/client/tests/e2e/_utils/standard.cmd.sh` (SHELL) | Magnitude: 2.74 | Delta: **0.416 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 32, io: 19, safety_bypasses: 17, reflection_metaprogramming: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `packages/get-platform/src/getPlatform.ts` (TYPESCRIPT) | Magnitude: 36.0 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 337, structural_boundaries: 118, branch: 96, immutability_locks: 58
- `packages/internals/src/highlight/prism.ts` (TYPESCRIPT) | Magnitude: 147.52 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 254, branch: 231, structural_boundaries: 86, state_mutation: 48
- `packages/client/tests/functional/dataproxy-engine/version/tests.ts` (TYPESCRIPT) | Magnitude: 0.59 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: args: 11, indent_spaces: 11, func_start: 9, safety_bypasses: 8
- `packages/migrate/src/utils/spinner.ts` (TYPESCRIPT) | Magnitude: 1.38 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 14, args: 9, doc: 9
- `packages/client-generator-js/src/GenericsArgsInfo.ts` (TYPESCRIPT) | Magnitude: 12.26 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 63, state_mutation: 52, structural_boundaries: 19, branch: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `packages/param-graph/src/types.ts` (TYPESCRIPT) | Magnitude: 2.15 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 21, indent_spaces: 14, structural_boundaries: 12, branch: 7
- `helpers/blaze/permutations.ts` (TYPESCRIPT) | Magnitude: 1.29 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 9, structural_boundaries: 4, lazy_evaluation: 4, branch: 3
- `packages/ts-builders/src/GenericParameter.test.ts` (TYPESCRIPT) | Magnitude: 1.48 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 14, args: 8, func_start: 8, test: 8
- `packages/client-engine-runtime/src/utils.ts` (TYPESCRIPT) | Magnitude: 10.97 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 91, branch: 63, structural_boundaries: 47, safety: 16
- `helpers/blaze/matrix.ts` (TYPESCRIPT) | Magnitude: 1.14 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 15, generics: 6, import: 6, indent_spaces: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `packages/client/src/runtime/utils/deserializeRawParameters.ts` (TYPESCRIPT) | Magnitude: 7.13 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 51, structural_boundaries: 20, branch: 19, safety: 11
- `packages/client-engine-runtime/src/interpreter/in-memory-processing.ts` (TYPESCRIPT) | Magnitude: 8.25 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 78, branch: 31, structural_boundaries: 27, state_mutation: 21
- `packages/client/tests/functional/relationMode-17255-same-actions/_matrix.ts` (TYPESCRIPT) | Magnitude: 1.65 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 11, branch: 9, immutability_locks: 4
- `packages/client-generator-js/src/typedSql/buildDbEnums.ts` (TYPESCRIPT) | Magnitude: 5.89 | Delta: **0.038 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 51, structural_boundaries: 27, state_mutation: 19, args: 13
- `helpers/compile/plugins/fill-plugin/fillers/events.ts` (TYPESCRIPT) | Magnitude: 2.94 | Delta: **0.054 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 18, indent_spaces: 18, structural_boundaries: 9, args: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `packages/client/tests/functional/_utils/relationMode/conditionalError.ts` (TYPESCRIPT) | Magnitude: 5.17 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 36, structural_boundaries: 23, generics: 22, ui_framework: 17
- `packages/migrate/src/SchemaEngine.ts` (TYPESCRIPT) | Magnitude: 2.16 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 21, doc: 20, concurrency: 18, args: 17
- `packages/client/tests/functional/_utils/defineMatrix.ts` (TYPESCRIPT) | Magnitude: 1.9 | Delta: **0.066 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 29, ui_framework: 20, generics: 20, indent_spaces: 20
- `helpers/blaze/pipe.ts` (TYPESCRIPT) | Magnitude: 6.01 | Delta: **0.066 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 170, generics: 105, ui_framework: 75, structural_boundaries: 38
- `packages/client/src/runtime/core/types/exported/FieldRef.ts` (TYPESCRIPT) | Magnitude: 1.41 | Delta: **0.074 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: immutability_locks: 4, indent_spaces: 4, structural_boundaries: 2, class_start: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `packages/client/src/__tests__/benchmarks/query-performance/caching.bench.ts` (TYPESCRIPT) | Magnitude: 7.83 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 150, structural_boundaries: 38, concurrency: 30, args: 20
- `packages/client/tests/e2e/large-schema-generation/_steps.ts` (TYPESCRIPT) | Magnitude: 1.59 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 10, concurrency: 8, args: 3
- `packages/client/tests/e2e/unsupported-edge-error/_steps.ts` (TYPESCRIPT) | Magnitude: 2.29 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 15, concurrency: 11, args: 4
- `packages/client-common/src/QueryEngine.ts` (TYPESCRIPT) | Magnitude: 1.78 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 32, structural_boundaries: 12, args: 8, func_start: 8
- `packages/client/tests/e2e/prisma-client-imports-sqlite/_steps.ts` (TYPESCRIPT) | Magnitude: 3.09 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 16, concurrency: 14, branch: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `packages/client/tests/e2e/typed-sql-query-compiler-adapter-libsql/prisma/sql/filterTrackingEvents.sql` (SQLITE) | Magnitude: 5.2 | Delta: **0.065 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 6, io: 3, args: 2, doc: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `packages/client/src/runtime/core/request/UserArgs.ts` (TYPESCRIPT) | Magnitude: 1.15 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 2, safety_bypasses: 1, api: 1, doc: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `packages/client/tests/e2e/browser-enum/tests/main.ts` (TYPESCRIPT) | Magnitude: 0.32 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 5, indent_spaces: 4, args: 2, func_start: 2
- `packages/client/src/__tests__/integration/happy/rfc3339/test.ts` (TYPESCRIPT) | Magnitude: 1.73 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 7, concurrency: 6, args: 4
- `packages/client/src/runtime/core/engines/common/utils/getInteractiveTransactionId.ts` (TYPESCRIPT) | Magnitude: 0.94 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, indent_spaces: 4, branch: 3, safety: 2
- `packages/client-common/src/Dictionary.ts` (TYPESCRIPT) | Magnitude: 0.44 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 9, structural_boundaries: 6, generics: 4, immutability_locks: 4
- `packages/client/src/runtime/core/engines/common/errors/engine-not-found/binaryTargetsWasIncorrectlyPinned.ts` (TYPESCRIPT) | Magnitude: 0.37 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 6, import: 4, indent_spaces: 2, args: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `packages/client/tests/e2e/ts-version/5.4/prisma.config.ts` (TYPESCRIPT) | Magnitude: 1.36 | Delta: **0.081 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 3, branch: 1, structural_boundaries: 1, api: 1
- `packages/client/tests/e2e/ts-version/5.5/prisma.config.ts` (TYPESCRIPT) | Magnitude: 1.36 | Delta: **0.081 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 3, branch: 1, structural_boundaries: 1, api: 1
- `packages/client/tests/e2e/ts-version/5.6/prisma.config.ts` (TYPESCRIPT) | Magnitude: 1.36 | Delta: **0.081 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 3, branch: 1, structural_boundaries: 1, api: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `packages/cli/src/bin.ts` -> Churn: **62.73%** | Cog Load: 12.7711% | Debt: 96.2141%
- `packages/client/src/runtime/core/engines/client/ClientEngine.ts` -> Churn: **54.26%** | Cog Load: 100.0% | Debt: 24.3274%
- `packages/cli/src/CLI.ts` -> Churn: **53.02%** | Cog Load: 63.8767% | Debt: 0.0%
- `packages/client/src/runtime/getPrismaClient.ts` -> Churn: **52.08%** | Cog Load: 48.9119% | Debt: 94.7907%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `packages/client/tests/functional/query-validation/tests.ts` -> **Alberto Schiabel** (100.0% isolated ownership) | Magnitude: 131.23
- `packages/client/tests/functional/extensions/query.ts` -> **Alberto Schiabel** (100.0% isolated ownership) | Magnitude: 115.21
- `packages/client/tests/functional/relation-load-strategy-unsupported/preview-feature-disabled.ts` -> **Alberto Schiabel** (100.0% isolated ownership) | Magnitude: 100.57
- `packages/client-generator-js/src/TSClient/Model.ts` -> **Prismo** (100.0% isolated ownership) | Magnitude: 96.94
- `packages/client/tests/functional/relation-load-strategy/unsupported-queries.ts` -> **Alberto Schiabel** (100.0% isolated ownership) | Magnitude: 77.5

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `packages/client/src/runtime/getPrismaClient.ts` -> **Severity: 0.286** (Bridge: 0.0029 * Flux: 99.9434%)
- `packages/client/src/runtime/RequestHandler.ts` -> **Severity: 0.036** (Bridge: 0.0004 * Flux: 99.4049%)
- `packages/migrate/src/Migrate.ts` -> **Severity: 0.023** (Bridge: 0.0002 * Flux: 100.0%)
- `packages/migrate/src/commands/DbPush.ts` -> **Severity: 0.017** (Bridge: 0.0002 * Flux: 95.4978%)
- `packages/client/src/runtime/core/extensions/MergedExtensionsList.ts` -> **Severity: 0.013** (Bridge: 0.0001 * Flux: 100.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `helpers/compile/plugins/fill-plugin/fillers/fs.ts` -> **Severity: 562.0** (Blast Radius: 5.62 * Doc Risk: 100.0%)
- `packages/ts-builders/src/BasicBuilder.ts` -> **Severity: 527.529** (Blast Radius: 19.789 * Doc Risk: 26.6577%)
- `packages/cli/src/config.ts` -> **Severity: 407.802** (Blast Radius: 61.17 * Doc Risk: 6.6667%)
- `packages/client/src/utils/getTestClient.ts` -> **Severity: 392.982** (Blast Radius: 10.315 * Doc Risk: 38.0981%)
- `packages/param-graph-builder/src/param-graph-builder.ts` -> **Severity: 388.4** (Blast Radius: 3.884 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
