# ARCHITECTURAL_BRIEF: nx
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_typescript/nx` |
| **Timestamp** | `2026-08-03T19:56:05.944043+00:00` |
| **Scan Duration** | `19.0s` |
| **Git Branch** | `master` |
| **Git Commit** | `557c876e96c1f92f39eb05cb79f0cf06973ee214` |
| **Git Remote** | `https://github.com/nrwl/nx.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 4684 malicious artifacts.

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
| Total Artifacts | 10631 |
| Analyzed Artifacts (Scanned) | 6132 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 4499 |
| Total LOC | 644130 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 57.7% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1483 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.8% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 510 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 4300 | 541666 | 70.1% |
| JSON | 805 | 56005 | 13.1% |
| MARKDOWN | 210 | 0 | 3.4% |
| PLAINTEXT | 169 | 6 | 2.8% |
| RUST | 137 | 25441 | 2.2% |
| XML | 130 | 505 | 2.1% |
| JAVASCRIPT | 117 | 6471 | 1.9% |
| KOTLIN | 93 | 8136 | 1.5% |
| HTML | 90 | 3038 | 1.5% |
| CSS | 37 | 967 | 0.6% |
| CSHARP | 23 | 893 | 0.4% |
| YAML | 7 | 242 | 0.1% |
| SHELL | 5 | 326 | 0.1% |
| BATCH | 3 | 298 | 0.0% |
| GROOVY | 3 | 66 | 0.0% |
| RUBY | 2 | 31 | 0.0% |
| SWIFT | 1 | 39 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.543`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 3916 | 63.9% |
| file_cluster_13 | 1157 | 18.9% |
| file_cluster_4 | 276 | 4.5% |
| file_cluster_0 | 197 | 3.2% |
| file_cluster_2 | 87 | 1.4% |
| file_cluster_17 | 58 | 0.9% |
| file_cluster_16 | 26 | 0.4% |
| Unknown | 6 | 0.1% |
| file_cluster_1 | 4 | 0.1% |
| file_cluster_7 | 3 | 0.0% |
| file_cluster_6 | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 373 | 6.1% |
| Static: Minified & Vendor Opaque Mass | 28 | 0.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 4499*

**Composition by Extension & Reason:**
- `.avif`: 756x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 132x Excluded (Binary Format Detected), 105x Excluded (Unsupported Extension: '.avif')
- `.mdoc`: 497x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 495x Excluded (Explicitly Denied Extension: '.png')
- `.md`: 392x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 377x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Massive Static Asset Blob: 6795 LOC), 2x Excluded (Massive Static Asset Blob: 9787 LOC)
- `.webp`: 253x Excluded (Explicitly Denied Extension: '.webp')
- `.ts`: 203x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 8x Unsupported Format (.undeterminable), 2x Excluded (Machine-Generated Source Code Signature: 1185 LOC)
- `.snap`: 220x Unsupported Format (.snap), 1x Excluded (Saturation: Line 55 exceeds 500 chars), 1x Excluded (Saturation: Line 19 exceeds 500 chars)
- `no_extension`: 122x Unsupported Format (.undeterminable), 28x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 252 LOC)
- `.tsx`: 58x Excluded (Saturation: Line 12 exceeds 500 chars), 34x Excluded (Saturation: Line 15 exceeds 500 chars), 14x Excluded (Saturation: Line 10 exceeds 500 chars)
- `.ts__tmpl__`: 143x Unsupported Format (.undeterminable), 2x Excluded (Saturation: Line 50 exceeds 500 chars)
- `.jpg`: 61x Excluded (Explicitly Denied Extension: '.jpg')
- `.tsx__tmpl__`: 54x Unsupported Format (.undeterminable)
- `.svg`: 53x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js__tmpl__`: 48x Unsupported Format (.undeterminable)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 16.5 | 7.8 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.0 | 20.5 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 9.7 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 6.5 | 0.0 | 0.0 |
| API Exposure | 0.0 | 19.8 | 4.1 | 4.6 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 28.9 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 12.4 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 72.9 | 0.4 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 86.4 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 28.8 | 4.7 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 74.6 | 5.8 | 3.2 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 45.3 | 38.7 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 17.7 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 7.2 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.8 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `packages/nx/src/plugins/js/lock-file/__fixtures__/bun/large-project.bun.lock.ts` (Hits: 2494)
- `packages/nx/src/plugins/js/lock-file/__fixtures__/bun/nextjs-app.bun.lock.ts` (Hits: 619)
- `packages/js/src/utils/assets/copy-assets-handler.spec.ts` (Hits: 214)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **js.rs** (`packages/nx/src/native/plugins/js.rs`) — 199 inbound connections
2. **child_process.rs** (`packages/nx/src/native/pseudo_terminal/child_process.rs`) — 150 inbound connections
3. **tree.ts** (`packages/nx/src/generators/tree.ts`) — 133 inbound connections
4. **mock-project-graph.ts** (`packages/nx/src/internal-testing-utils/mock-project-graph.ts`) — 119 inbound connections
5. **semver.ts** (`packages/devkit/src/utils/semver.ts`) — 103 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.ts** (`nx-dev/ui-icons/src/index.ts`) — 143 outbound dependencies
2. **native-bindings.js** (`packages/nx/src/native/native-bindings.js`) — 82 outbound dependencies
3. **app.rs** (`packages/nx/src/native/tui/app.rs`) — 71 outbound dependencies
4. **server.ts** (`packages/nx/src/daemon/server/server.ts`) — 58 outbound dependencies
5. **tasks_list.rs** (`packages/nx/src/native/tui/components/tasks_list.rs`) — 58 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `from_str` (@ `packages/nx/src/native/tui/components/tasks_list.rs`) -> Impact: **1765.0** | LOC: 1559
- `extractPropertiesFromObjectLiteral` (@ `packages/eslint/src/generators/utils/flat-config/ast-utils.ts`) -> Impact: **1725.7** | LOC: 712
- `describe` (@ `packages/nx/src/utils/params.spec.ts`) -> Impact: **1120.2** | LOC: 2036
- `validateProperty` (@ `packages/nx/src/utils/params.ts`) -> Impact: **1071.0** | LOC: 312
- `runPackageJsonUpdatesConfirmationPrompt` (@ `packages/nx/src/command-line/migrate/migrate.ts`) -> Impact: **1054.2** | LOC: 1185
- `render_cloud_message` (@ `packages/nx/src/native/tui/components/tasks_list.rs`) -> Impact: **1031.1** | LOC: 273
  * *Intent:* // Replace the first cell with a new one containing the NX logo and title
- `describe` (@ `packages/react/src/migrations/update-22-0-0/add-svgr-to-webpack-config.spec.ts`) -> Impact: **982.7** | LOC: 1710
- `describe` (@ `packages/nx/src/utils/package-manager.spec.ts`) -> Impact: **875.1** | LOC: 702
- `run_baseline_if_needed` (@ `packages/nx/src/native/metrics/collector.rs`) -> Impact: **825.0** | LOC: 738
  * *Intent:* /// Establish CPU baselines for all processes when there are processes needing a baseline. /// Uses bulk refresh to keep all process timing in sync (a...
- `generateJsonExampleForHelper` (@ `nx-dev/feature-package-schema-viewer/src/lib/examples.ts`) -> Impact: **786.1** | LOC: 203

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `generateJsonExampleForHelper` (@ `nx-dev/feature-package-schema-viewer/src/lib/examples.ts`) -> **O(2^N) [Recursive]**
- `Changelog` (@ `nx-dev/nx-dev/pages/changelog.tsx`) -> **O(2^N) [Recursive]**
- `toggleNav` (@ `nx-dev/ui-common/src/lib/headers/documentation-header.tsx`) -> **O(2^N) [Recursive]**
- `describe` (@ `packages/angular-rspack/src/lib/config/create-config.spec.ts`) -> **O(2^N) [Recursive]**
- `executeDevServerBuilder` (@ `packages/angular/src/builders/dev-server/dev-server.impl.ts`) -> **O(2^N) [Recursive]**
- `describe` (@ `packages/angular/src/generators/library/library.spec.ts`) -> **O(2^N) [Recursive]**
- `describe` (@ `packages/devkit/src/utils/replace-project-configuration-with-plugin.spec.ts`) -> **O(2^N) [Recursive]**
- `describe` (@ `packages/docker/src/plugins/plugin.spec.ts`) -> **O(2^N) [Recursive]**
- `describe` (@ `packages/eslint/src/generators/convert-to-flat-config/converters/json-converter.spec.ts`) -> **O(2^N) [Recursive]**
- `describe` (@ `packages/eslint/src/generators/lint-project/lint-project.spec.ts`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `describe` (@ `packages/js/src/utils/assets/copy-assets-handler.spec.ts`) -> DB Complexity: **483**
- `describe` (@ `packages/nx/src/plugins/js/package-json/create-package-json.spec.ts`) -> DB Complexity: **330**
- `native_path_[Truncated]` (@ `mvnw`) -> DB Complexity: **283**
  * *Intent:* # OS specific support.
- `describe` (@ `packages/js/src/plugins/typescript/util.spec.ts`) -> DB Complexity: **244**
- `describe` (@ `packages/js/src/generators/typescript-sync/typescript-sync.spec.ts`) -> DB Complexity: **243**
- `describe` (@ `packages/eslint-plugin/src/rules/dependency-checks.spec.ts`) -> DB Complexity: **215**
- `describe` (@ `e2e/node/src/node-esm-support.test.ts`) -> DB Complexity: **156**
- `describe` (@ `packages/nx/src/utils/package-manager.spec.ts`) -> DB Complexity: **150**
- `describe` (@ `e2e/nx/src/cache.test.ts`) -> DB Complexity: **149**
- `describe` (@ `packages/js/src/utils/assets/copy-assets-handler.spec.ts`) -> DB Complexity: **140**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `packages/nx/src/native/tui/components` | 9 | 6818.58 | 16.04% | 56.65% |
| `packages/nx/src/plugins/js/lock-file/__fixtures__/nextjs` | 4 | 6296.15 | 3.21% | 0.0% |
| `packages/nx/src/native/tui` | 18 | 5494.98 | 14.56% | 36.33% |
| `packages/nx/src/plugins/js/lock-file/__fixtures__/duplicate-package` | 3 | 5236.57 | 2.94% | 0.0% |
| `e2e/dotnet` | 6 | 5033.69 | 4.13% | 0.0% |
| `packages/react-native/src/generators/application/files/app/android/app` | 2 | 5021.9 | 11.68% | 47.9% |
| `packages/nx/src/plugins/js/lock-file/__fixtures__/auxiliary-packages` | 6 | 5018.79 | 4.63% | 0.0% |
| `packages/nx/src/plugins/js/lock-file/__fixtures__/optional` | 5 | 5017.22 | 4.5% | 0.0% |
| `packages/nx/src/native/tasks` | 12 | 2245.16 | 12.15% | 31.08% |
| `packages/nx/src/native/cache` | 7 | 2020.98 | 27.51% | 46.62% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `packages/expo/src/generators/application/files/base/.babelrc.js.template` -> **100.0%** Exposure
- `packages/expo/src/utils/jest/files/jest.resolver.js` -> **100.0%** Exposure
- `packages/nx/src/native/wasi-worker-browser.mjs` -> **100.0%** Exposure
- `scripts/fetch-nx-issues.js` -> **100.0%** Exposure
- `graph/migrate/src/lib/migrate.stories.tsx` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `astro-docs/src/pages/llms.txt.ts` -> **100.0%** Exposure
- `astro-docs/src/plugins/utils/typedoc/theme.ts` -> **100.0%** Exposure
- `astro-docs/src/plugins/utils/typedoc/toc.ts` -> **100.0%** Exposure
- `astro-docs/src/plugins/utils/watch.ts` -> **100.0%** Exposure
- `graph/client/src/app/external-api-impl.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `packages/nx/src/native/tui/tui_state.rs` -> **47** Orphaned Functions | **8** Duplicates
- `packages/nx/src/native/tui/components/tasks_list.rs` -> **46** Orphaned Functions | **0** Duplicates
- `packages/nx/src/native/tui/components/layout_manager.rs` -> **32** Orphaned Functions | **4** Duplicates
- `graph/migrate/src/lib/migrate.stories.tsx` -> **1** Orphaned Functions | **27** Duplicates
- `packages/nx/src/project-graph/error-types.ts` -> **0** Orphaned Functions | **17** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`packages/gradle/batch-runner/src/main/kotlin/dev/nx/gradle/NxBatchRunner.kt`** -> AI Confidence: **99.48%**
2. **`packages/gradle/batch-runner/src/main/kotlin/dev/nx/gradle/runner/BuildListener.kt`** -> AI Confidence: **99.48%**
3. **`packages/gradle/batch-runner/src/main/kotlin/dev/nx/gradle/runner/GradleRunner.kt`** -> AI Confidence: **99.48%**
4. **`packages/gradle/batch-runner/src/main/kotlin/dev/nx/gradle/util/Logger.kt`** -> AI Confidence: **99.48%**
5. **`packages/gradle/project-graph/src/main/kotlin/dev/nx/gradle/NxProjectExtension.kt`** -> AI Confidence: **99.48%**
6. **`packages/gradle/project-graph/src/main/kotlin/dev/nx/gradle/NxProjectReportTask.kt`** -> AI Confidence: **99.48%**
7. **`packages/gradle/project-graph/src/main/kotlin/dev/nx/gradle/NxTaskExtension.kt`** -> AI Confidence: **99.48%**
8. **`packages/gradle/project-graph/src/main/kotlin/dev/nx/gradle/utils/CiTargetsUtils.kt`** -> AI Confidence: **99.48%**
9. **`packages/gradle/project-graph/src/main/kotlin/dev/nx/gradle/utils/NxTracing.kt`** -> AI Confidence: **99.48%**
10. **`packages/gradle/project-graph/src/main/kotlin/dev/nx/gradle/utils/ProjectUtils.kt`** -> AI Confidence: **99.48%**
11. **`packages/gradle/project-graph/src/main/kotlin/dev/nx/gradle/utils/TaskUtils.kt`** -> AI Confidence: **99.48%**
12. **`packages/gradle/project-graph/src/main/kotlin/dev/nx/gradle/utils/parsing/KotlinAstTestParser.kt`** -> AI Confidence: **99.48%**
13. **`packages/gradle/project-graph/src/test/kotlin/dev/nx/gradle/utils/AddTestCiTargetsTest.kt`** -> AI Confidence: **99.48%**
14. **`packages/gradle/project-graph/src/test/kotlin/dev/nx/gradle/utils/ProcessTargetsForProjectTest.kt`** -> AI Confidence: **99.48%**
15. **`packages/gradle/project-graph/src/test/kotlin/dev/nx/gradle/utils/ProcessTaskUtilsTest.kt`** -> AI Confidence: **99.48%**
16. **`packages/maven/batch-runner-adapters/maven3/src/main/kotlin/dev/nx/maven/adapter/maven3/CachingMaven3Invoker.kt`** -> AI Confidence: **99.48%**
17. **`packages/maven/batch-runner-adapters/maven3/src/main/kotlin/dev/nx/maven/adapter/maven3/NxMaven3.kt`** -> AI Confidence: **99.48%**
18. **`packages/maven/batch-runner-adapters/maven4/src/main/kotlin/dev/nx/maven/adapter/maven4/CachingResidentMavenInvoker.kt`** -> AI Confidence: **99.48%**
19. **`packages/maven/batch-runner-adapters/maven4/src/main/kotlin/dev/nx/maven/adapter/maven4/Maven4AdapterInvoker.kt`** -> AI Confidence: **99.48%**
20. **`packages/maven/batch-runner-adapters/maven4/src/main/kotlin/dev/nx/maven/adapter/maven4/NxMaven.kt`** -> AI Confidence: **99.48%**
21. **`packages/maven/batch-runner-adapters/maven4/src/main/kotlin/dev/nx/maven/adapter/maven4/NxMavenFactory.kt`** -> AI Confidence: **99.48%**
22. **`packages/maven/batch-runner/src/main/kotlin/dev/nx/maven/NxMavenBatchRunner.kt`** -> AI Confidence: **99.48%**
23. **`packages/maven/batch-runner/src/main/kotlin/dev/nx/maven/runner/MavenInvokerRunner.kt`** -> AI Confidence: **99.48%**
24. **`packages/maven/maven-plugin/src/main/kotlin/dev/nx/maven/NxProjectAnalyzer.kt`** -> AI Confidence: **99.48%**
25. **`packages/maven/maven-plugin/src/main/kotlin/dev/nx/maven/NxProjectAnalyzerMojo.kt`** -> AI Confidence: **99.48%**
26. **`packages/maven/maven-plugin/src/main/kotlin/dev/nx/maven/buildstate/NxBuildStateApplyMojo.kt`** -> AI Confidence: **99.48%**
27. **`packages/maven/maven-plugin/src/main/kotlin/dev/nx/maven/targets/NxTargetFactory.kt`** -> AI Confidence: **99.48%**
28. **`packages/maven/maven-plugin/src/main/kotlin/dev/nx/maven/utils/MojoAnalyzer.kt`** -> AI Confidence: **99.48%**
29. **`packages/maven/maven-plugin/src/test/kotlin/dev/nx/maven/ExternalDependenciesTest.kt`** -> AI Confidence: **99.48%**
30. **`packages/maven/shared/src/main/kotlin/dev/nx/maven/shared/BuildStateRecorder.kt`** -> AI Confidence: **99.48%**
31. **`packages/react-native/src/generators/application/files/app/android/app/src/main/java/com/__lowerCaseName__/MainApplication.kt.template`** -> AI Confidence: **99.48%**
32. **`e2e/utils/create-project-utils.ts`** -> AI Confidence: **99.39%**
33. **`packages/angular/plugins/component-testing.ts`** -> AI Confidence: **99.39%**
34. **`packages/angular/src/generators/ng-add/migrators/projects/app.migrator.ts`** -> AI Confidence: **99.39%**
35. **`packages/cypress/src/utils/start-dev-server.ts`** -> AI Confidence: **99.39%**
36. **`packages/js/src/executors/release-publish/release-publish.impl.ts`** -> AI Confidence: **99.39%**
37. **`packages/js/src/utils/package-json/update-package-json.ts`** -> AI Confidence: **99.39%**
38. **`packages/nx/src/command-line/init/implementation/angular/standalone-workspace.ts`** -> AI Confidence: **99.39%**
39. **`packages/nx/src/command-line/show/target.ts`** -> AI Confidence: **99.39%**
40. **`packages/nx/src/project-graph/utils/project-configuration/project-nodes-manager.ts`** -> AI Confidence: **99.39%**
41. **`packages/nx/src/project-graph/utils/project-configuration/target-normalization.ts`** -> AI Confidence: **99.39%**
42. **`packages/nx/src/tasks-runner/life-cycles/tui-summary-life-cycle.spec.ts`** -> AI Confidence: **99.39%**
43. **`packages/react/plugins/component-testing/index.ts`** -> AI Confidence: **99.39%**
44. **`packages/react/src/generators/application/lib/create-application-files.ts`** -> AI Confidence: **99.39%**
45. **`packages/storybook/src/generators/configuration/lib/util-functions.ts`** -> AI Confidence: **99.39%**
46. **`packages/vite/src/utils/generator-utils.ts`** -> AI Confidence: **99.39%**
47. **`packages/vitest/src/utils/generator-utils.ts`** -> AI Confidence: **99.39%**
48. **`packages/workspace/src/generators/new/generate-workspace-files.ts`** -> AI Confidence: **99.39%**
49. **`packages/workspace/src/generators/new/new.ts`** -> AI Confidence: **99.39%**
50. **`packages/angular/src/generators/convert-to-rspack/convert-to-rspack.ts`** -> AI Confidence: **99.35%**
51. **`packages/cypress/src/generators/configuration/configuration.ts`** -> AI Confidence: **99.35%**
52. **`packages/nx/src/command-line/init/implementation/utils.ts`** -> AI Confidence: **99.35%**
53. **`packages/nx/src/plugins/js/lock-file/pnpm-parser.ts`** -> AI Confidence: **99.35%**
54. **`packages/rollup/src/plugins/package-json/update-package-json.ts`** -> AI Confidence: **99.35%**
55. **`packages/rspack/src/plugins/utils/apply-base-config.ts`** -> AI Confidence: **99.35%**
56. **`packages/nx/src/native/nx.wasi.cjs`** -> AI Confidence: **99.34%**
57. **`packages/angular/src/generators/convert-to-application-executor/convert-to-application-executor.ts`** -> AI Confidence: **99.34%**
58. **`packages/angular/src/generators/setup-ssr/lib/update-project-config.ts`** -> AI Confidence: **99.34%**
59. **`packages/nx/src/executors/run-commands/run-commands.impl.ts`** -> AI Confidence: **99.34%**
60. **`packages/nx/src/project-graph/utils/project-configuration/target-merging.ts`** -> AI Confidence: **99.34%**
61. **`packages/nx/src/tasks-runner/create-task-graph.ts`** -> AI Confidence: **99.34%**
62. **`packages/rspack/src/plugins/utils/plugins/normalize-options.ts`** -> AI Confidence: **99.34%**
63. **`packages/webpack/src/plugins/nx-webpack-plugin/lib/normalize-options.ts`** -> AI Confidence: **99.34%**
64. **`packages/workspace/src/generators/preset/preset.ts`** -> AI Confidence: **99.34%**
65. **`packages/gradle/batch-runner/src/main/kotlin/dev/nx/gradle/runner/TestListener.kt`** -> AI Confidence: **99.34%**
66. **`packages/gradle/batch-runner/src/test/kotlin/dev/nx/gradle/runner/OutputProcessorTest.kt`** -> AI Confidence: **99.34%**
67. **`packages/gradle/project-graph/src/main/kotlin/dev/nx/gradle/NxProjectGraphReportPlugin.kt`** -> AI Confidence: **99.34%**
68. **`packages/gradle/project-graph/src/test/kotlin/dev/nx/gradle/NxProjectGraphReportPluginTest.kt`** -> AI Confidence: **99.34%**
69. **`packages/gradle/project-graph/src/test/kotlin/dev/nx/gradle/utils/CreateNodeForProjectTest.kt`** -> AI Confidence: **99.34%**
70. **`packages/maven/batch-runner/src/main/kotlin/dev/nx/maven/cli/ArgParser.kt`** -> AI Confidence: **99.34%**
71. **`packages/maven/maven-plugin/src/main/kotlin/dev/nx/maven/buildstate/NxBuildStateRecordMojo.kt`** -> AI Confidence: **99.34%**
72. **`packages/maven/maven-plugin/src/main/kotlin/dev/nx/maven/targets/TestClassDiscovery.kt`** -> AI Confidence: **99.34%**
73. **`packages/maven/maven-plugin/src/main/kotlin/dev/nx/maven/utils/MavenExpressionResolver.kt`** -> AI Confidence: **99.34%**
74. **`packages/maven/shared/src/main/kotlin/dev/nx/maven/shared/BuildStateApplier.kt`** -> AI Confidence: **99.34%**
75. **`packages/maven/shared/src/main/kotlin/dev/nx/maven/shared/BuildStateManager.kt`** -> AI Confidence: **99.34%**
76. **`scripts/copy.js`** -> AI Confidence: **99.32%**
77. **`packages/jest/src/executors/jest/summary.ts`** -> AI Confidence: **99.32%**
78. **`packages/jest/src/utils/config/get-jest-projects.ts`** -> AI Confidence: **99.32%**
79. **`packages/js/src/utils/typescript/plugin.ts`** -> AI Confidence: **99.32%**
80. **`packages/nx/src/migrations/update-16-0-0/update-depends-on-to-tokens.ts`** -> AI Confidence: **99.32%**
81. **`packages/nx/src/utils/git-utils.tree-filter.ts`** -> AI Confidence: **99.32%**
82. **`packages/gradle/batch-runner/src/main/kotlin/dev/nx/gradle/runner/OutputProcessor.kt`** -> AI Confidence: **99.32%**
83. **`packages/maven/batch-runner-adapters/maven4/src/main/kotlin/dev/nx/maven/adapter/maven4/BatchExecutionListener.kt`** -> AI Confidence: **99.32%**
84. **`packages/maven/batch-runner/src/main/kotlin/dev/nx/maven/runner/MavenHomeDiscovery.kt`** -> AI Confidence: **99.32%**
85. **`packages/maven/batch-runner/src/main/kotlin/dev/nx/maven/runner/ProcessBasedMavenExecutor.kt`** -> AI Confidence: **99.32%**
86. **`packages/maven/maven-plugin/src/main/kotlin/dev/nx/maven/GitIgnoreClassifier.kt`** -> AI Confidence: **99.32%**
87. **`packages/maven/shared/src/main/kotlin/dev/nx/maven/shared/PathUtils.kt`** -> AI Confidence: **99.32%**
88. **`astro-docs/src/plugins/plugin.loader.ts`** -> AI Confidence: **99.31%**
89. **`astro-docs/src/plugins/utils/devkit-generation.ts`** -> AI Confidence: **99.31%**
90. **`e2e/utils/command-utils.ts`** -> AI Confidence: **99.31%**
91. **`e2e/utils/ensure-browser-installation.ts`** -> AI Confidence: **99.31%**
92. **`e2e/utils/global-setup.ts`** -> AI Confidence: **99.31%**
93. **`graph/migrate/src/lib/components/migration-card.tsx`** -> AI Confidence: **99.31%**
94. **`graph/ui-project-details/src/lib/project-details/project-details.tsx`** -> AI Confidence: **99.31%**
95. **`graph/ui-project-details/src/lib/show-all-options/show-options-help.tsx`** -> AI Confidence: **99.31%**
96. **`graph/ui-project-details/src/lib/target-configuration-details-header/target-configuration-details-header.tsx`** -> AI Confidence: **99.31%**
97. **`graph/ui-project-details/src/lib/target-configuration-details/target-configuration-details.tsx`** -> AI Confidence: **99.31%**
98. **`nx-dev/feature-package-schema-viewer/src/lib/parameter-view.tsx`** -> AI Confidence: **99.31%**
99. **`nx-dev/nx-dev/pages/changelog.tsx`** -> AI Confidence: **99.31%**
100. **`nx-dev/ui-common/src/lib/sidebar.tsx`** -> AI Confidence: **99.31%**
101. **`nx-dev/ui-fence/src/lib/fence.tsx`** -> AI Confidence: **99.31%**
102. **`packages/angular-rspack/src/lib/config/config-utils/dev-server-config-utils.ts`** -> AI Confidence: **99.31%**
103. **`packages/angular-rspack/src/lib/config/i18n/create-i18n-options.ts`** -> AI Confidence: **99.31%**
104. **`packages/angular-rspack/src/lib/models/normalize-options.ts`** -> AI Confidence: **99.31%**
105. **`packages/angular-rspack/src/lib/plugins/angular-rspack-plugin.ts`** -> AI Confidence: **99.31%**
106. **`packages/angular-rspack/src/lib/plugins/i18n-inline-plugin.ts`** -> AI Confidence: **99.31%**
107. **`packages/angular-rspack/src/lib/plugins/ng-rspack.ts`** -> AI Confidence: **99.31%**
108. **`packages/angular-rspack/src/lib/plugins/prerender-plugin.ts`** -> AI Confidence: **99.31%**
109. **`packages/angular-rspack/src/lib/utils/stats.ts`** -> AI Confidence: **99.31%**
110. **`packages/angular/src/executors/utilities/ng-packagr/stylesheet-processor.ts`** -> AI Confidence: **99.31%**
111. **`packages/angular/src/generators/application/lib/create-files.ts`** -> AI Confidence: **99.31%**
112. **`packages/angular/src/generators/host/host.ts`** -> AI Confidence: **99.31%**
113. **`packages/angular/src/generators/library/lib/normalize-options.ts`** -> AI Confidence: **99.31%**
114. **`packages/angular/src/generators/ng-add/migrators/projects/e2e.migrator.ts`** -> AI Confidence: **99.31%**
115. **`packages/angular/src/generators/ng-add/utilities/workspace.ts`** -> AI Confidence: **99.31%**
116. **`packages/angular/src/generators/ngrx-feature-store/lib/add-imports.ts`** -> AI Confidence: **99.31%**
117. **`packages/angular/src/generators/ngrx/lib/add-imports-to-module.ts`** -> AI Confidence: **99.31%**
118. **`packages/angular/src/generators/remote/lib/update-ssr-setup.ts`** -> AI Confidence: **99.31%**
119. **`packages/angular/src/generators/remote/remote.ts`** -> AI Confidence: **99.31%**
120. **`packages/angular/src/generators/setup-mf/lib/add-remote-to-host.ts`** -> AI Confidence: **99.31%**
121. **`packages/angular/src/generators/setup-ssr/lib/generate-files.ts`** -> AI Confidence: **99.31%**
122. **`packages/angular/src/migrations/update-17-1-0/replace-nguniversal-engines.ts`** -> AI Confidence: **99.31%**
123. **`packages/angular/src/migrations/update-21-5-0/utils/karma-config-comparer.ts`** -> AI Confidence: **99.31%**
124. **`packages/angular/src/migrations/update-22-3-0/update-ssr-webpack-config.ts`** -> AI Confidence: **99.31%**
125. **`packages/angular/src/plugins/plugin.ts`** -> AI Confidence: **99.31%**
126. **`packages/angular/src/utils/nx-devkit/ast-utils.ts`** -> AI Confidence: **99.31%**
127. **`packages/create-nx-workspace/bin/create-nx-workspace.ts`** -> AI Confidence: **99.31%**
128. **`packages/create-nx-workspace/src/create-empty-workspace.ts`** -> AI Confidence: **99.31%**
129. **`packages/create-nx-workspace/src/create-sandbox.ts`** -> AI Confidence: **99.31%**
130. **`packages/create-nx-workspace/src/create-workspace.ts`** -> AI Confidence: **99.31%**
131. **`packages/create-nx-workspace/src/utils/nx/ab-testing.ts`** -> AI Confidence: **99.31%**
132. **`packages/cypress/src/generators/component-configuration/component-configuration.ts`** -> AI Confidence: **99.31%**
133. **`packages/cypress/src/generators/convert-to-inferred/convert-to-inferred.spec.ts`** -> AI Confidence: **99.31%**
134. **`packages/cypress/src/generators/convert-to-inferred/convert-to-inferred.ts`** -> AI Confidence: **99.31%**
135. **`packages/cypress/src/generators/migrate-to-cypress-11/conversion.util.ts`** -> AI Confidence: **99.31%**
136. **`packages/cypress/src/migrations/update-20-8-0/replace-experimental-just-in-time-compile.ts`** -> AI Confidence: **99.31%**
137. **`packages/cypress/src/migrations/update-22-1-0/update-angular-component-testing-support.ts`** -> AI Confidence: **99.31%**
138. **`packages/cypress/src/plugins/plugin.spec.ts`** -> AI Confidence: **99.31%**
139. **`packages/cypress/src/plugins/plugin.ts`** -> AI Confidence: **99.31%**
140. **`packages/detox/src/executors/test/test.impl.ts`** -> AI Confidence: **99.31%**
141. **`packages/detox/src/plugins/plugin.ts`** -> AI Confidence: **99.31%**
142. **`packages/devkit/src/utils/catalog/pnpm-manager.ts`** -> AI Confidence: **99.31%**
143. **`packages/devkit/src/utils/catalog/yarn-manager.ts`** -> AI Confidence: **99.31%**
144. **`packages/devkit/src/utils/package-json.ts`** -> AI Confidence: **99.31%**
145. **`packages/esbuild/src/executors/esbuild/lib/build-esbuild-options.ts`** -> AI Confidence: **99.31%**
146. **`packages/esbuild/src/executors/esbuild/lib/normalize.ts`** -> AI Confidence: **99.31%**
147. **`packages/esbuild/src/generators/configuration/configuration.ts`** -> AI Confidence: **99.31%**
148. **`packages/eslint-plugin/src/resolve-workspace-rules.ts`** -> AI Confidence: **99.31%**
149. **`packages/eslint-plugin/src/rules/dependency-checks.ts`** -> AI Confidence: **99.31%**
150. **`packages/eslint-plugin/src/rules/nx-plugin-checks.ts`** -> AI Confidence: **99.31%**
151. **`packages/eslint-plugin/src/utils/ast-utils.ts`** -> AI Confidence: **99.31%**
152. **`packages/eslint/src/executors/lint/lint.impl.ts`** -> AI Confidence: **99.31%**
153. **`packages/eslint/src/generators/convert-to-flat-config/generator.ts`** -> AI Confidence: **99.31%**
154. **`packages/eslint/src/generators/convert-to-inferred/convert-to-inferred.ts`** -> AI Confidence: **99.31%**
155. **`packages/eslint/src/generators/init/init-migration.ts`** -> AI Confidence: **99.31%**
156. **`packages/eslint/src/generators/init/init.ts`** -> AI Confidence: **99.31%**
157. **`packages/eslint/src/generators/lint-project/lint-project.ts`** -> AI Confidence: **99.31%**
158. **`packages/eslint/src/generators/utils/flat-config/ast-utils.ts`** -> AI Confidence: **99.31%**
159. **`packages/expo/plugins/metro-resolver.ts`** -> AI Confidence: **99.31%**
160. **`packages/expo/plugins/plugin.ts`** -> AI Confidence: **99.31%**
161. **`packages/expo/src/executors/run/run.impl.ts`** -> AI Confidence: **99.31%**
162. **`packages/expo/src/generators/application/lib/add-e2e.ts`** -> AI Confidence: **99.31%**
163. **`packages/gradle/src/executors/gradle/gradle-batch.impl.ts`** -> AI Confidence: **99.31%**
164. **`packages/gradle/src/plugin-v1/nodes.ts`** -> AI Confidence: **99.31%**
165. **`packages/gradle/src/plugin-v1/utils/get-gradle-report.ts`** -> AI Confidence: **99.31%**
166. **`packages/gradle/src/plugin/nodes.ts`** -> AI Confidence: **99.31%**
167. **`packages/jest/src/executors/jest/jest.impl.ts`** -> AI Confidence: **99.31%**
168. **`packages/jest/src/generators/convert-to-inferred/convert-to-inferred.ts`** -> AI Confidence: **99.31%**
169. **`packages/jest/src/migrations/update-22-2-0/convert-jest-config-to-cjs.ts`** -> AI Confidence: **99.31%**
170. **`packages/jest/src/plugins/plugin.ts`** -> AI Confidence: **99.31%**
171. **`packages/js/src/executors/prune-lockfile/prune-lockfile.ts`** -> AI Confidence: **99.31%**
172. **`packages/js/src/executors/verdaccio/verdaccio.impl.ts`** -> AI Confidence: **99.31%**
173. **`packages/js/src/generators/init/init.ts`** -> AI Confidence: **99.31%**
174. **`packages/js/src/generators/library/library.ts`** -> AI Confidence: **99.31%**
175. **`packages/js/src/generators/setup-build/generator.ts`** -> AI Confidence: **99.31%**
176. **`packages/js/src/plugins/typescript/plugin.ts`** -> AI Confidence: **99.31%**
177. **`packages/js/src/utils/buildable-libs-utils.ts`** -> AI Confidence: **99.31%**
178. **`packages/js/src/utils/generate-globs.ts`** -> AI Confidence: **99.31%**
179. **`packages/js/src/utils/typescript/ts-solution-setup.ts`** -> AI Confidence: **99.31%**
180. **`packages/maven/src/executors/maven/maven-batch.impl.ts`** -> AI Confidence: **99.31%**
181. **`packages/maven/src/plugins/maven-analyzer.ts`** -> AI Confidence: **99.31%**
182. **`packages/module-federation/src/plugins/nx-module-federation-plugin/angular/nx-module-federation-dev-server-plugin.ts`** -> AI Confidence: **99.31%**
183. **`packages/module-federation/src/plugins/nx-module-federation-plugin/angular/nx-module-federation-ssr-dev-server-plugin.ts`** -> AI Confidence: **99.31%**
184. **`packages/module-federation/src/plugins/nx-module-federation-plugin/rspack/nx-module-federation-dev-server-plugin.ts`** -> AI Confidence: **99.31%**
185. **`packages/module-federation/src/plugins/nx-module-federation-plugin/rspack/nx-module-federation-ssr-dev-server-plugin.ts`** -> AI Confidence: **99.31%**
186. **`packages/module-federation/src/utils/get-remotes-for-host.ts`** -> AI Confidence: **99.31%**
187. **`packages/module-federation/src/utils/start-remote-proxies.ts`** -> AI Confidence: **99.31%**
188. **`packages/module-federation/src/utils/start-ssr-remote-proxies.ts`** -> AI Confidence: **99.31%**
189. **`packages/next/plugins/component-testing.ts`** -> AI Confidence: **99.31%**
190. **`packages/next/src/executors/server/server.impl.ts`** -> AI Confidence: **99.31%**
191. **`packages/next/src/generators/application/lib/add-e2e.ts`** -> AI Confidence: **99.31%**
192. **`packages/next/src/generators/application/lib/create-application-files.ts`** -> AI Confidence: **99.31%**
193. **`packages/next/src/plugins/plugin.ts`** -> AI Confidence: **99.31%**
194. **`packages/node/src/generators/library/library.ts`** -> AI Confidence: **99.31%**
195. **`packages/nuxt/src/generators/application/lib/add-e2e.ts`** -> AI Confidence: **99.31%**
196. **`packages/nuxt/src/utils/add-linting.ts`** -> AI Confidence: **99.31%**
197. **`packages/nx/bin/init-local.ts`** -> AI Confidence: **99.31%**
198. **`packages/nx/src/adapter/ngcli-adapter.ts`** -> AI Confidence: **99.31%**
199. **`packages/nx/src/ai/set-up-ai-agents/set-up-ai-agents.ts`** -> AI Confidence: **99.31%**
200. **`packages/nx/src/ai/utils.ts`** -> AI Confidence: **99.31%**
201. **`packages/nx/src/analytics/analytics.ts`** -> AI Confidence: **99.31%**
202. **`packages/nx/src/command-line/generate/generate.ts`** -> AI Confidence: **99.31%**
203. **`packages/nx/src/command-line/generate/generator-utils.ts`** -> AI Confidence: **99.31%**
204. **`packages/nx/src/command-line/graph/graph.ts`** -> AI Confidence: **99.31%**
205. **`packages/nx/src/command-line/init/configure-plugins.ts`** -> AI Confidence: **99.31%**
206. **`packages/nx/src/command-line/init/implementation/add-nx-to-monorepo.ts`** -> AI Confidence: **99.31%**
207. **`packages/nx/src/command-line/init/implementation/add-nx-to-npm-repo.ts`** -> AI Confidence: **99.31%**
208. **`packages/nx/src/command-line/init/implementation/angular/index.ts`** -> AI Confidence: **99.31%**
209. **`packages/nx/src/command-line/init/implementation/check-compatible-with-plugins.ts`** -> AI Confidence: **99.31%**
210. **`packages/nx/src/command-line/init/init-v2.ts`** -> AI Confidence: **99.31%**
211. **`packages/nx/src/command-line/migrate/migrate.ts`** -> AI Confidence: **99.31%**
212. **`packages/nx/src/command-line/reset/reset.ts`** -> AI Confidence: **99.31%**
213. **`packages/nx/src/command-line/run/executor-utils.ts`** -> AI Confidence: **99.31%**
214. **`packages/nx/src/command-line/show/project.ts`** -> AI Confidence: **99.31%**
215. **`packages/nx/src/config/nx-json.ts`** -> AI Confidence: **99.31%**
216. **`packages/nx/src/generators/utils/project-configuration.ts`** -> AI Confidence: **99.31%**
217. **`packages/nx/src/hasher/hash-task.ts`** -> AI Confidence: **99.31%**
218. **`packages/nx/src/hasher/native-task-hasher-impl.ts`** -> AI Confidence: **99.31%**
219. **`packages/nx/src/hasher/task-hasher.ts`** -> AI Confidence: **99.31%**
220. **`packages/nx/src/migrations/update-15-0-0/prefix-outputs.ts`** -> AI Confidence: **99.31%**
221. **`packages/nx/src/migrations/update-16-2-0/remove-run-commands-output-path.ts`** -> AI Confidence: **99.31%**
222. **`packages/nx/src/migrations/update-17-0-0/rm-default-collection-npm-scope.ts`** -> AI Confidence: **99.31%**
223. **`packages/nx/src/migrations/update-17-0-0/use-minimal-config-for-tasks-runner-options.ts`** -> AI Confidence: **99.31%**
224. **`packages/nx/src/migrations/update-19-2-4/set-project-name.ts`** -> AI Confidence: **99.31%**
225. **`packages/nx/src/migrations/update-22-0-0/consolidate-release-tag-config.ts`** -> AI Confidence: **99.31%**
226. **`packages/nx/src/nx-cloud/generators/connect-to-nx-cloud/connect-to-nx-cloud.ts`** -> AI Confidence: **99.31%**
227. **`packages/nx/src/plugins/js/lock-file/bun-parser.ts`** -> AI Confidence: **99.31%**
228. **`packages/nx/src/plugins/js/lock-file/npm-parser.ts`** -> AI Confidence: **99.31%**
229. **`packages/nx/src/plugins/js/lock-file/project-graph-pruning.ts`** -> AI Confidence: **99.31%**
230. **`packages/nx/src/plugins/js/lock-file/yarn-parser.ts`** -> AI Confidence: **99.31%**
231. **`packages/nx/src/plugins/js/package-json/create-package-json.ts`** -> AI Confidence: **99.31%**
232. **`packages/nx/src/plugins/js/project-graph/affected/npm-packages.ts`** -> AI Confidence: **99.31%**
233. **`packages/nx/src/plugins/js/project-graph/build-dependencies/explicit-project-dependencies.ts`** -> AI Confidence: **99.31%**
234. **`packages/nx/src/plugins/js/project-graph/build-dependencies/target-project-locator.ts`** -> AI Confidence: **99.31%**
235. **`packages/nx/src/plugins/package-json/create-nodes.ts`** -> AI Confidence: **99.31%**
236. **`packages/nx/src/project-graph/build-project-graph.ts`** -> AI Confidence: **99.31%**
237. **`packages/nx/src/project-graph/nx-deps-cache.ts`** -> AI Confidence: **99.31%**
238. **`packages/nx/src/project-graph/plugins/get-plugins.ts`** -> AI Confidence: **99.31%**
239. **`packages/nx/src/project-graph/plugins/resolve-plugin.ts`** -> AI Confidence: **99.31%**
240. **`packages/nx/src/project-graph/project-graph.ts`** -> AI Confidence: **99.31%**
241. **`packages/nx/src/project-graph/utils/project-configuration-utils.ts`** -> AI Confidence: **99.31%**
242. **`packages/nx/src/tasks-runner/life-cycles/dynamic-run-many-terminal-output-life-cycle.ts`** -> AI Confidence: **99.31%**
243. **`packages/nx/src/tasks-runner/life-cycles/task-history-life-cycle-old.ts`** -> AI Confidence: **99.31%**
244. **`packages/nx/src/tasks-runner/life-cycles/tui-summary-life-cycle.ts`** -> AI Confidence: **99.31%**
245. **`packages/nx/src/tasks-runner/run-command.ts`** -> AI Confidence: **99.31%**
246. **`packages/nx/src/tasks-runner/task-orchestrator.ts`** -> AI Confidence: **99.31%**
247. **`packages/nx/src/utils/analytics-prompt.ts`** -> AI Confidence: **99.31%**
248. **`packages/nx/src/utils/catalog/pnpm-manager.ts`** -> AI Confidence: **99.31%**
249. **`packages/nx/src/utils/catalog/yarn-manager.ts`** -> AI Confidence: **99.31%**
250. **`packages/nx/src/utils/child-process.ts`** -> AI Confidence: **99.31%**
251. **`packages/nx/src/utils/command-line-utils.ts`** -> AI Confidence: **99.31%**
252. **`packages/nx/src/utils/package-json.ts`** -> AI Confidence: **99.31%**
253. **`packages/nx/src/utils/package-manager.ts`** -> AI Confidence: **99.31%**
254. **`packages/nx/src/utils/plugins/local-plugins.ts`** -> AI Confidence: **99.31%**
255. **`packages/nx/src/utils/plugins/output.ts`** -> AI Confidence: **99.31%**
256. **`packages/nx/src/utils/plugins/plugin-capabilities.ts`** -> AI Confidence: **99.31%**
257. **`packages/nx/src/utils/print-help.ts`** -> AI Confidence: **99.31%**
258. **`packages/nx/src/utils/sync-generators.ts`** -> AI Confidence: **99.31%**
259. **`packages/playwright/src/generators/configuration/configuration.ts`** -> AI Confidence: **99.31%**
260. **`packages/plugin/src/generators/lint-checks/generator.ts`** -> AI Confidence: **99.31%**
261. **`packages/plugin/src/generators/migration/migration.ts`** -> AI Confidence: **99.31%**
262. **`packages/react-native/plugins/metro-resolver.ts`** -> AI Confidence: **99.31%**
263. **`packages/react-native/plugins/plugin.ts`** -> AI Confidence: **99.31%**
264. **`packages/react/src/executors/module-federation-dev-server/module-federation-dev-server.impl.ts`** -> AI Confidence: **99.31%**
265. **`packages/react/src/executors/module-federation-ssr-dev-server/module-federation-ssr-dev-server.impl.ts`** -> AI Confidence: **99.31%**
266. **`packages/react/src/executors/module-federation-static-server/module-federation-static-server.impl.ts`** -> AI Confidence: **99.31%**
267. **`packages/react/src/generators/application/lib/add-e2e.ts`** -> AI Confidence: **99.31%**
268. **`packages/react/src/generators/component-story/component-story.ts`** -> AI Confidence: **99.31%**
269. **`packages/react/src/generators/library/lib/add-rollup-build-target.ts`** -> AI Confidence: **99.31%**
270. **`packages/react/src/generators/remote/remote.ts`** -> AI Confidence: **99.31%**
271. **`packages/react/src/generators/setup-ssr/setup-ssr.ts`** -> AI Confidence: **99.31%**
272. **`packages/react/src/generators/stories/stories.ts`** -> AI Confidence: **99.31%**
273. **`packages/react/src/plugins/router-plugin.ts`** -> AI Confidence: **99.31%**
274. **`packages/react/src/utils/ast-utils.ts`** -> AI Confidence: **99.31%**
275. **`packages/react/src/utils/ct-utils.ts`** -> AI Confidence: **99.31%**
276. **`packages/remix/generators.ts`** -> AI Confidence: **99.31%**
277. **`packages/remix/src/generators/application/lib/add-e2e.ts`** -> AI Confidence: **99.31%**
278. **`packages/rollup/src/executors/rollup/rollup.impl.ts`** -> AI Confidence: **99.31%**
279. **`packages/rollup/src/generators/configuration/configuration.ts`** -> AI Confidence: **99.31%**
280. **`packages/rollup/src/plugins/plugin.ts`** -> AI Confidence: **99.31%**
281. **`packages/rspack/src/executors/dev-server/lib/get-dev-server-config.ts`** -> AI Confidence: **99.31%**
282. **`packages/rspack/src/executors/module-federation-dev-server/module-federation-dev-server.impl.ts`** -> AI Confidence: **99.31%**
283. **`packages/rspack/src/executors/module-federation-ssr-dev-server/module-federation-ssr-dev-server.impl.ts`** -> AI Confidence: **99.31%**
284. **`packages/rspack/src/executors/module-federation-static-server/module-federation-static-server.impl.ts`** -> AI Confidence: **99.31%**
285. **`packages/rspack/src/executors/rspack/lib/config.ts`** -> AI Confidence: **99.31%**
286. **`packages/rspack/src/executors/rspack/rspack.impl.ts`** -> AI Confidence: **99.31%**
287. **`packages/rspack/src/generators/configuration/configuration.ts`** -> AI Confidence: **99.31%**
288. **`packages/rspack/src/generators/convert-config-to-rspack-plugin/convert-config-to-rspack-plugin.ts`** -> AI Confidence: **99.31%**
289. **`packages/rspack/src/generators/convert-to-inferred/utils/build-post-target-transformer.ts`** -> AI Confidence: **99.31%**
290. **`packages/rspack/src/generators/convert-to-inferred/utils/serve-post-target-transformer.ts`** -> AI Confidence: **99.31%**
291. **`packages/rspack/src/generators/init/init.ts`** -> AI Confidence: **99.31%**
292. **`packages/rspack/src/plugins/utils/apply-web-config.ts`** -> AI Confidence: **99.31%**
293. **`packages/rspack/src/plugins/utils/plugins/nx-tsconfig-paths-rspack-plugin.ts`** -> AI Confidence: **99.31%**
294. **`packages/rspack/src/plugins/write-index-html-plugin.ts`** -> AI Confidence: **99.31%**
295. **`packages/rspack/src/utils/generator-utils.ts`** -> AI Confidence: **99.31%**
296. **`packages/storybook/src/generators/configuration/configuration.ts`** -> AI Confidence: **99.31%**
297. **`packages/storybook/src/generators/init/init.ts`** -> AI Confidence: **99.31%**
298. **`packages/storybook/src/utils/utilities.ts`** -> AI Confidence: **99.31%**
299. **`packages/vite/plugins/nx-tsconfig-paths.plugin.ts`** -> AI Confidence: **99.31%**
300. **`packages/vite/src/executors/dev-server/dev-server.impl.ts`** -> AI Confidence: **99.31%**
301. **`packages/vite/src/executors/preview-server/preview-server.impl.ts`** -> AI Confidence: **99.31%**
302. **`packages/vite/src/generators/configuration/configuration.ts`** -> AI Confidence: **99.31%**
303. **`packages/vitest/src/executors/test/vitest.impl.ts`** -> AI Confidence: **99.31%**
304. **`packages/vitest/src/generators/configuration/configuration.ts`** -> AI Confidence: **99.31%**
305. **`packages/vitest/src/generators/init/init.ts`** -> AI Confidence: **99.31%**
306. **`packages/vue/src/generators/application/lib/add-e2e.ts`** -> AI Confidence: **99.31%**
307. **`packages/vue/src/generators/component/lib/utils.ts`** -> AI Confidence: **99.31%**
308. **`packages/vue/src/utils/add-linting.ts`** -> AI Confidence: **99.31%**
309. **`packages/web/src/executors/file-server/file-server.impl.ts`** -> AI Confidence: **99.31%**
310. **`packages/webpack/src/executors/dev-server/lib/get-dev-server-config.ts`** -> AI Confidence: **99.31%**
311. **`packages/webpack/src/generators/configuration/configuration.ts`** -> AI Confidence: **99.31%**
312. **`packages/webpack/src/generators/convert-config-to-webpack-plugin/convert-config-to-webpack-plugin.ts`** -> AI Confidence: **99.31%**
313. **`packages/webpack/src/generators/convert-to-inferred/utils/build-post-target-transformer.ts`** -> AI Confidence: **99.31%**
314. **`packages/webpack/src/generators/convert-to-inferred/utils/serve-post-target-transformer.ts`** -> AI Confidence: **99.31%**
315. **`packages/webpack/src/plugins/nx-webpack-plugin/lib/apply-base-config.ts`** -> AI Confidence: **99.31%**
316. **`packages/webpack/src/plugins/nx-webpack-plugin/lib/apply-web-config.ts`** -> AI Confidence: **99.31%**
317. **`packages/webpack/src/plugins/plugin.ts`** -> AI Confidence: **99.31%**
318. **`packages/webpack/src/plugins/write-index-html-plugin.ts`** -> AI Confidence: **99.31%**
319. **`packages/workspace/src/generators/move/lib/update-imports.ts`** -> AI Confidence: **99.31%**
320. **`packages/workspace/src/generators/new/generate-preset.ts`** -> AI Confidence: **99.31%**
321. **`scripts/documentation/package-schemas/package-metadata.ts`** -> AI Confidence: **99.31%**
322. **`scripts/issues-scraper/index.ts`** -> AI Confidence: **99.31%**
323. **`tools/documentation/create-embeddings/src/main.mts`** -> AI Confidence: **99.31%**
324. **`packages/nx/src/native/cache/cache.rs`** -> AI Confidence: **99.31%**
325. **`packages/nx/src/native/cache/file_ops.rs`** -> AI Confidence: **99.31%**
326. **`packages/nx/src/native/db/connection.rs`** -> AI Confidence: **99.31%**
327. **`packages/nx/src/native/db/initialize.rs`** -> AI Confidence: **99.31%**
328. **`packages/nx/src/native/ide/install.rs`** -> AI Confidence: **99.31%**
329. **`packages/nx/src/native/pseudo_terminal/command/unix.rs`** -> AI Confidence: **99.31%**
330. **`packages/nx/src/native/tasks/hash_planner.rs`** -> AI Confidence: **99.31%**
331. **`packages/nx/src/native/tasks/task_history.rs`** -> AI Confidence: **99.31%**
332. **`packages/nx/src/native/tui/components/help_text.rs`** -> AI Confidence: **99.31%**
333. **`packages/nx/src/native/tui/tui_core.rs`** -> AI Confidence: **99.31%**
334. **`packages/nx/src/native/watch/watch_filterer.rs`** -> AI Confidence: **99.31%**
335. **`graph/client/src/assets/release-static/environment.js`** -> AI Confidence: **99.29%**
336. **`jest.preset.js`** -> AI Confidence: **99.29%**
337. **`nx-dev/nx-dev/next-sitemap.config.js`** -> AI Confidence: **99.29%**
338. **`scripts/check-lock-files.js`** -> AI Confidence: **99.29%**
339. **`scripts/check-react-native-changes.js`** -> AI Confidence: **99.29%**
340. **`scripts/commitizen.js`** -> AI Confidence: **99.29%**
341. **`scripts/migrate-to-pnpm-version.js`** -> AI Confidence: **99.29%**
342. **`scripts/run-native-target.js`** -> AI Confidence: **99.29%**
343. **`scripts/submit-plugin.js`** -> AI Confidence: **99.29%**
344. **`scripts/validate-pr-title.js`** -> AI Confidence: **99.29%**
345. **`tools/documentation/create-embeddings/jest.preset.js`** -> AI Confidence: **99.29%**
346. **`e2e/remix/src/remix-ts-solution.test.ts`** -> AI Confidence: **99.29%**
347. **`graph/ui-project-details/src/lib/utils/get-display-header-from-target-configuration.ts`** -> AI Confidence: **99.29%**
348. **`packages/angular-rspack-compiler/src/utils/targets-from-browsers.ts`** -> AI Confidence: **99.29%**
349. **`packages/angular/src/builders/dev-server/schema.d.ts`** -> AI Confidence: **99.29%**
350. **`packages/angular/src/executors/module-federation-dev-server/schema.d.ts`** -> AI Confidence: **99.29%**
351. **`packages/angular/src/generators/library/lib/normalized-schema.ts`** -> AI Confidence: **99.29%**
352. **`packages/angular/src/generators/library/schema.d.ts`** -> AI Confidence: **99.29%**
353. **`packages/angular/src/generators/utils/add-mf-env-to-inputs.ts`** -> AI Confidence: **99.29%**
354. **`packages/angular/src/migrations/update-17-1-0/replace-nguniversal-builders.ts`** -> AI Confidence: **99.29%**
355. **`packages/create-nx-workspace/src/utils/ci/is-ci.ts`** -> AI Confidence: **99.29%**
356. **`packages/detox/src/executors/test/schema.d.ts`** -> AI Confidence: **99.29%**
357. **`packages/devkit/src/utils/replace-project-configuration-with-plugin.ts`** -> AI Confidence: **99.29%**
358. **`packages/expo/src/executors/build-list/build-fragment.d.ts`** -> AI Confidence: **99.29%**
359. **`packages/expo/src/executors/build-list/schema.d.ts`** -> AI Confidence: **99.29%**
360. **`packages/expo/src/executors/export/schema.d.ts`** -> AI Confidence: **99.29%**
361. **`packages/expo/src/executors/start/schema.d.ts`** -> AI Confidence: **99.29%**
362. **`packages/expo/src/migrations/update-21-4-0/update-splash-screen-config.ts`** -> AI Confidence: **99.29%**
363. **`packages/expo/src/utils/resolve-eas.ts`** -> AI Confidence: **99.29%**
364. **`packages/jest/src/executors/jest/schema.d.ts`** -> AI Confidence: **99.29%**
365. **`packages/jest/src/generators/configuration/schema.d.ts`** -> AI Confidence: **99.29%**
366. **`packages/js/src/executors/release-publish/schema.d.ts`** -> AI Confidence: **99.29%**
367. **`packages/js/src/generators/init/schema.d.ts`** -> AI Confidence: **99.29%**
368. **`packages/node/src/generators/application/schema.d.ts`** -> AI Confidence: **99.29%**
369. **`packages/node/src/generators/e2e-project/schema.d.ts`** -> AI Confidence: **99.29%**
370. **`packages/node/src/generators/library/schema.d.ts`** -> AI Confidence: **99.29%**
371. **`packages/nx/src/native/assert-supported-platform.ts`** -> AI Confidence: **99.29%**
372. **`packages/nx/src/plugins/js/lock-file/__fixtures__/duplicate-package/pnpm-lock.yaml.ts`** -> AI Confidence: **99.29%**
373. **`packages/nx/src/plugins/js/lock-file/__fixtures__/optional/yarn.lock.ts`** -> AI Confidence: **99.29%**
374. **`packages/nx/src/plugins/js/lock-file/__fixtures__/pruning/devkit-yargs/pnpm-lock-v6.yaml.ts`** -> AI Confidence: **99.29%**
375. **`packages/nx/src/plugins/js/lock-file/__fixtures__/pruning/devkit-yargs/pnpm-lock-v9.yaml.ts`** -> AI Confidence: **99.29%**
376. **`packages/nx/src/plugins/js/lock-file/__fixtures__/pruning/devkit-yargs/pnpm-lock.yaml.ts`** -> AI Confidence: **99.29%**
377. **`packages/nx/src/plugins/js/lock-file/__fixtures__/pruning/pnpm-lock-v6.yaml.ts`** -> AI Confidence: **99.29%**
378. **`packages/nx/src/plugins/js/lock-file/__fixtures__/pruning/pnpm-lock-v9.yaml.ts`** -> AI Confidence: **99.29%**
379. **`packages/nx/src/plugins/js/lock-file/__fixtures__/pruning/pnpm-lock.yaml.ts`** -> AI Confidence: **99.29%**
380. **`packages/nx/src/plugins/js/project-graph/build-dependencies/strip-source-code.ts`** -> AI Confidence: **99.29%**
381. **`packages/nx/src/tasks-runner/life-cycles/pretty-time.ts`** -> AI Confidence: **99.29%**
382. **`packages/nx/src/utils/git-utils.index-filter.ts`** -> AI Confidence: **99.29%**
383. **`packages/playwright/src/executors/playwright/playwright.impl.ts`** -> AI Confidence: **99.29%**
384. **`packages/plugin/src/generators/plugin/schema.d.ts`** -> AI Confidence: **99.29%**
385. **`packages/react-native/src/generators/init/lib/gitignore-entries.ts`** -> AI Confidence: **99.29%**
386. **`packages/react/babel.ts`** -> AI Confidence: **99.29%**
387. **`packages/react/src/rules/update-module-federation-project.ts`** -> AI Confidence: **99.29%**
388. **`packages/react/src/utils/add-mf-env-to-inputs.ts`** -> AI Confidence: **99.29%**
389. **`packages/remix/src/generators/library/schema.d.ts`** -> AI Confidence: **99.29%**
390. **`packages/rollup/src/generators/configuration/schema.d.ts`** -> AI Confidence: **99.29%**
391. **`packages/storybook/src/generators/convert-to-inferred/lib/serve-post-target-transformer.ts`** -> AI Confidence: **99.29%**
392. **`packages/vite/src/generators/configuration/schema.d.ts`** -> AI Confidence: **99.29%**
393. **`packages/vite/src/generators/init/schema.d.ts`** -> AI Confidence: **99.29%**
394. **`packages/vite/src/generators/vitest/schema.d.ts`** -> AI Confidence: **99.29%**
395. **`packages/vite/src/utils/e2e-web-server-info-utils.ts`** -> AI Confidence: **99.29%**
396. **`packages/vitest/src/generators/configuration/schema.d.ts`** -> AI Confidence: **99.29%**
397. **`packages/vitest/src/generators/init/schema.d.ts`** -> AI Confidence: **99.29%**
398. **`packages/web/src/executors/file-server/schema.d.ts`** -> AI Confidence: **99.29%**
399. **`packages/web/src/generators/application/schema.d.ts`** -> AI Confidence: **99.29%**
400. **`packages/webpack/src/executors/dev-server/schema.d.ts`** -> AI Confidence: **99.29%**
401. **`packages/webpack/src/generators/configuration/schema.d.ts`** -> AI Confidence: **99.29%**
402. **`packages/webpack/src/migrations/update-22-0-0/remove-deprecated-options.ts`** -> AI Confidence: **99.29%**
403. **`packages/workspace/src/generators/move/lib/update-owners-and-conformance.ts`** -> AI Confidence: **99.29%**
404. **`packages/workspace/src/generators/preset/schema.d.ts`** -> AI Confidence: **99.29%**
405. **`scripts/release-docs.ts`** -> AI Confidence: **99.29%**
406. **`tools/eslint-rules/rules/ensure-pnpm-lock-version.ts`** -> AI Confidence: **99.29%**
407. **`packages/react-native/src/generators/application/files/app/android/gradlew.template`** -> AI Confidence: **99.29%**
408. **`packages/gradle/batch-runner/src/main/kotlin/dev/nx/gradle/cli/ArgParser.kt`** -> AI Confidence: **99.29%**
409. **`packages/gradle/project-graph/src/main/kotlin/dev/nx/gradle/dsl/NxDsl.kt`** -> AI Confidence: **99.29%**
410. **`packages/gradle/project-graph/src/main/kotlin/dev/nx/gradle/utils/GitIgnoreClassifier.kt`** -> AI Confidence: **99.29%**
411. **`packages/gradle/project-graph/src/main/kotlin/dev/nx/gradle/utils/ProjectDependencyUtils.kt`** -> AI Confidence: **99.29%**
412. **`packages/gradle/project-graph/src/main/kotlin/dev/nx/gradle/utils/parsing/JavaAstTestParser.kt`** -> AI Confidence: **99.29%**
413. **`packages/gradle/project-graph/src/main/kotlin/dev/nx/gradle/utils/parsing/RegexTestParser.kt`** -> AI Confidence: **99.29%**
414. **`packages/gradle/project-graph/src/main/kotlin/dev/nx/gradle/utils/parsing/TestClassParser.kt`** -> AI Confidence: **99.29%**
415. **`packages/gradle/project-graph/src/main/kotlin/dev/nx/gradle/utils/parsing/TestParsingConstants.kt`** -> AI Confidence: **99.29%**
416. **`packages/gradle/project-graph/src/test/kotlin/dev/nx/gradle/utils/testdata/ConfigurationClass.kt`** -> AI Confidence: **99.29%**
417. **`packages/maven/batch-runner-adapters/maven3/src/main/kotlin/dev/nx/maven/adapter/maven3/BatchExecutionListener.kt`** -> AI Confidence: **99.29%**
418. **`packages/maven/batch-runner/src/main/kotlin/dev/nx/maven/runner/MavenClassRealm.kt`** -> AI Confidence: **99.29%**
419. **`packages/maven/batch-runner/src/main/kotlin/dev/nx/maven/runner/MavenExecutorFactory.kt`** -> AI Confidence: **99.29%**
420. **`packages/maven/batch-runner/src/main/kotlin/dev/nx/maven/runner/ResidentMavenExecutor.kt`** -> AI Confidence: **99.29%**
421. **`packages/maven/batch-runner/src/main/kotlin/dev/nx/maven/utils/TaskGraphUtils.kt`** -> AI Confidence: **99.29%**
422. **`packages/maven/maven-plugin/src/main/kotlin/dev/nx/maven/targets/NxTarget.kt`** -> AI Confidence: **99.29%**
423. **`packages/maven/maven-plugin/src/main/kotlin/dev/nx/maven/utils/PathFormatter.kt`** -> AI Confidence: **99.29%**
424. **`packages/maven/shared/src/main/kotlin/dev/nx/maven/shared/MavenCommandResolver.kt`** -> AI Confidence: **99.29%**
425. **`packages/nx/src/native/utils/ci.rs`** -> AI Confidence: **99.29%**
426. **`packages/react-native/src/generators/application/files/app/android/build.gradle.template`** -> AI Confidence: **99.29%**
427. **`packages/react-native/src/generators/application/files/app/android/settings.gradle.template`** -> AI Confidence: **99.29%**
428. **`packages/js/src/plugins/typescript/util.ts`** -> AI Confidence: **99.25%**
429. **`packages/nx/src/native/native-bindings.js`** -> AI Confidence: **99.24%**
430. **`e2e/nx/src/graph-ts-solution.test.ts`** -> AI Confidence: **99.24%**
431. **`graph/migrate/src/lib/components/migration-timeline.tsx`** -> AI Confidence: **99.24%**
432. **`nx-dev/feature-ai/src/lib/feed-container.tsx`** -> AI Confidence: **99.24%**
433. **`nx-dev/feature-doc-viewer/src/lib/doc-viewer.tsx`** -> AI Confidence: **99.24%**
434. **`nx-dev/feature-package-schema-viewer/src/lib/content.tsx`** -> AI Confidence: **99.24%**
435. **`nx-dev/feature-search/src/lib/algolia-search.tsx`** -> AI Confidence: **99.24%**
436. **`nx-dev/ui-blog/src/lib/blog-details.tsx`** -> AI Confidence: **99.24%**
437. **`nx-dev/ui-common/src/lib/headers/documentation-header.tsx`** -> AI Confidence: **99.24%**
438. **`nx-dev/ui-common/src/lib/headers/header.tsx`** -> AI Confidence: **99.24%**
439. **`nx-dev/ui-courses/src/lib/course-details.tsx`** -> AI Confidence: **99.24%**
440. **`packages/angular-rspack/src/lib/config/config-utils/common-config.ts`** -> AI Confidence: **99.24%**
441. **`packages/angular-rspack/src/lib/config/config-utils/style-config-utils.ts`** -> AI Confidence: **99.24%**
442. **`packages/angular-rspack/src/lib/plugins/index-html-plugin.ts`** -> AI Confidence: **99.24%**
443. **`packages/angular/src/builders/dev-server/dev-server.impl.ts`** -> AI Confidence: **99.24%**
444. **`packages/angular/src/builders/webpack-browser/webpack-browser.impl.ts`** -> AI Confidence: **99.24%**
445. **`packages/angular/src/executors/module-federation-ssr-dev-server/module-federation-ssr-dev-server.impl.ts`** -> AI Confidence: **99.24%**
446. **`packages/angular/src/generators/add-linting/add-linting.ts`** -> AI Confidence: **99.24%**
447. **`packages/angular/src/generators/application/application.ts`** -> AI Confidence: **99.24%**
448. **`packages/create-nx-workspace/src/internal-utils/prompts.ts`** -> AI Confidence: **99.24%**
449. **`packages/devkit/src/generators/plugin-migrations/executor-to-plugin-migrator.ts`** -> AI Confidence: **99.24%**
450. **`packages/esbuild/src/executors/esbuild/esbuild.impl.ts`** -> AI Confidence: **99.24%**
451. **`packages/eslint-plugin/src/rules/enforce-module-boundaries.ts`** -> AI Confidence: **99.24%**
452. **`packages/eslint-plugin/src/utils/project-graph-utils.ts`** -> AI Confidence: **99.24%**
453. **`packages/eslint-plugin/src/utils/runtime-lint-utils.ts`** -> AI Confidence: **99.24%**
454. **`packages/eslint/src/generators/utils/eslint-file.ts`** -> AI Confidence: **99.24%**
455. **`packages/eslint/src/generators/workspace-rule/workspace-rule.ts`** -> AI Confidence: **99.24%**
456. **`packages/expo/src/executors/install/install.impl.ts`** -> AI Confidence: **99.24%**
457. **`packages/expo/src/generators/library/library.ts`** -> AI Confidence: **99.24%**
458. **`packages/js/src/executors/node/node.impl.ts`** -> AI Confidence: **99.24%**
459. **`packages/js/src/executors/swc/swc.impl.ts`** -> AI Confidence: **99.24%**
460. **`packages/maven/src/plugins/nodes.ts`** -> AI Confidence: **99.24%**
461. **`packages/next/src/generators/application/lib/add-linting.ts`** -> AI Confidence: **99.24%**
462. **`packages/node/src/generators/application/application.ts`** -> AI Confidence: **99.24%**
463. **`packages/nuxt/src/generators/application/application.ts`** -> AI Confidence: **99.24%**
464. **`packages/nx/src/command-line/format/format.ts`** -> AI Confidence: **99.24%**
465. **`packages/nx/src/command-line/import/import.ts`** -> AI Confidence: **99.24%**
466. **`packages/nx/src/command-line/init/implementation/add-nx-to-nest.ts`** -> AI Confidence: **99.24%**
467. **`packages/nx/src/command-line/init/implementation/angular/legacy-angular-versions.ts`** -> AI Confidence: **99.24%**
468. **`packages/nx/src/command-line/run/run-one.ts`** -> AI Confidence: **99.24%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `astro-docs/src/assets/concepts/caching/distributed-caching.svg` -> **100.0%** Exposure
### Exploit Generation Surface
- `scripts/migrate-to-pnpm-version.js` -> **100.0%** Exposure
- `astro-docs/src/assets/concepts/caching/distributed-caching.svg` -> **100.0%** Exposure
- `e2e/angular/src/module-federation-host-remote.test.ts` -> **100.0%** Exposure
- `e2e/angular/src/module-federation.rspack.test.ts` -> **100.0%** Exposure
- `e2e/eslint/src/linter.test.ts` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `astro-docs/scripts/vale-changed.mjs` -> **100.0%** Exposure
- `packages/nx/src/command-line/migrate/run-migration-process.js` -> **100.0%** Exposure
- `packages/nx/src/native/wasi-worker.mjs` -> **100.0%** Exposure
- `scripts/jest-mocks/chalk.js` -> **100.0%** Exposure
- `scripts/jest-mocks/prettier.js` -> **100.0%** Exposure
### Raw Memory Manipulation
- `packages/nx/src/lib.rs` -> **0.0001%** Exposure
### Hardcoded Payload Artifacts
- `e2e/utils/global-setup.ts` -> **100.0%** Exposure
- `packages/js/src/plugins/jest/start-local-registry.ts` -> **100.0%** Exposure
- `scripts/local-registry/populate-storage.js` -> **99.9999%** Exposure
### Algorithmic DoS Exposure
- `nx-dev/nx-dev/next.config.js` -> **100.0%** Exposure
- `astro-docs/src/plugins/utils/cnw-generation.ts` -> **100.0%** Exposure
- `astro-docs/src/plugins/utils/core-nx-plugin-generation.ts` -> **100.0%** Exposure
- `astro-docs/src/plugins/utils/typedoc/theme.ts` -> **100.0%** Exposure
- `astro-docs/src/plugins/utils/typedoc/toc.ts` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `210` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `11731` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `packages/rspack/src/plugins/utils/plugins/postcss-cli-resources.ts` (TYPESCRIPT) -> Cumulative Risk: **924.5**
- **Archetype:** `file_cluster_4` (Distance: 11.433 IQR)
- **Magnitude:** 20.76 | **LOC:** 217 | **CtrlFlow:** 57.0% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `resolve` (Impact: 62.3), `PostcssCliResources` (Impact: 41.4), `resolver` (Impact: 10.8)

### 2. `packages/webpack/src/utils/webpack/plugins/postcss-cli-resources.ts` (TYPESCRIPT) -> Cumulative Risk: **924.5**
- **Archetype:** `file_cluster_4` (Distance: 11.461 IQR)
- **Magnitude:** 20.76 | **LOC:** 217 | **CtrlFlow:** 57.6% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `resolve` (Impact: 62.3), `PostcssCliResources` (Impact: 41.4), `resolver` (Impact: 10.8)

### 3. `packages/nx/src/daemon/client/client.ts` (TYPESCRIPT) -> Cumulative Risk: **921.22**
- **Archetype:** `file_cluster_4` (Distance: 13.856 IQR)
- **Magnitude:** 145.37 | **LOC:** 1415 | **CtrlFlow:** 41.0% | **Authorship Centralization:** 52.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `reconnectFileWatcher` (Impact: 173.3), `reconnectProjectGraphListener` (Impact: 165.3), `enabled` (Impact: 61.7)

### 4. `packages/angular-rspack/src/lib/utils/postcss-cli-resources.ts` (TYPESCRIPT) -> Cumulative Risk: **917.69**
- **Archetype:** `file_cluster_4` (Distance: 11.524 IQR)
- **Magnitude:** 13.74 | **LOC:** 241 | **CtrlFlow:** 53.4% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `reject` (Impact: 41.9), `process` (Impact: 11.8), `resolver` (Impact: 10.8)

### 5. `packages/nx/src/tasks-runner/life-cycles/task-history-life-cycle.ts` (TYPESCRIPT) -> Cumulative Risk: **900.53**
- **Archetype:** `file_cluster_4` (Distance: 12.318 IQR)
- **Magnitude:** 16.01 | **LOC:** 129 | **CtrlFlow:** 44.2% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `endCommand` (Impact: 30.7), `printFlakyTasksMessage` (Impact: 19.0), `getTasksHistoryLifeCycle` (Impact: 5.7)

### 6. `packages/nx/src/tasks-runner/life-cycles/task-history-life-cycle-old.ts` (TYPESCRIPT) -> Cumulative Risk: **894.67**
- **Archetype:** `file_cluster_4` (Distance: 12.202 IQR)
- **Magnitude:** 14.02 | **LOC:** 105 | **CtrlFlow:** 47.1% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `endCommand` (Impact: 40.8), `printFlakyTasksMessage` (Impact: 18.6), `endTasks` (Impact: 4.2)

### 7. `nx-dev/ui-common/src/lib/hubspot-form.tsx` (TYPESCRIPT) -> Cumulative Risk: **893.22**
- **Archetype:** `file_cluster_2` (Distance: 13.358 IQR)
- **Magnitude:** 26.37 | **LOC:** 159 | **CtrlFlow:** 65.5% | **Authorship Centralization:** 75.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `initCalendlyIfAvailable` (Impact: 43.5), `createForm` (Impact: 41.2), `findFormElement` (Impact: 26.3)

### 8. `packages/rspack/src/plugins/utils/plugins/rspack-nx-build-coordination-plugin.ts` (TYPESCRIPT) -> Cumulative Risk: **892.22**
- **Archetype:** `file_cluster_4` (Distance: 12.645 IQR)
- **Magnitude:** 18.77 | **LOC:** 115 | **CtrlFlow:** 42.2% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `createFileWatcher` (Impact: 43.2), `constructor` (Impact: 13.8), `buildChangedProjects` (Impact: 11.6)

### 9. `packages/nx/src/tasks-runner/running-tasks/batch-process.ts` (TYPESCRIPT) -> Cumulative Risk: **890.37**
- **Archetype:** `file_cluster_4` (Distance: 13.195 IQR)
- **Magnitude:** 19.86 | **LOC:** 134 | **CtrlFlow:** 45.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `constructor` (Impact: 65.8), `kill` (Impact: 10.6), `getResults` (Impact: 9.6)

### 10. `packages/angular-rspack/src/lib/plugins/ng-rspack.ts` (TYPESCRIPT) -> Cumulative Risk: **887.1**
- **Archetype:** `file_cluster_13` (Distance: 13.172 IQR)
- **Magnitude:** 56.27 | **LOC:** 188 | **CtrlFlow:** 67.2% | **Authorship Centralization:** 75.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `apply` (Impact: 405.8), `constructor` (Impact: 1.3)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `e2e/dotnet/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/nx/src/plugins/js/lock-file/__fixtures__/auxiliary-packages/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/nx/src/plugins/js/lock-file/__fixtures__/duplicate-package/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/nx/src/plugins/js/lock-file/__fixtures__/nextjs/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/nx/src/plugins/js/lock-file/__fixtures__/optional/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-native/src/generators/application/files/app/android/app/debug.keystore` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.115
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/nx/src/native/tui/components/tasks_list.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.68 IQR)
- **Top Global Matches:** file_cluster_8: 13.68, file_cluster_0: 13.804, file_cluster_17: 13.892
- **Magnitude:** 4252.3 | **LOC:** 6606 | **CtrlFlow:** 35.5% | **Authorship Centralization:** 44.4%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 94
- **Risk Profile:** Cognitive Load (23.9131%), Tech Debt (43.5762%)
**Top Internal Functions/Classes:**
  * `from_str` (Impact: 1765.0 | O(N^6) | DB: 94)
  * `render_cloud_message` (Impact: 1031.1 | O(2^N) | DB: 5)
    * *Intent:* // Replace the first cell with a new one containing the NX logo and title
  * `test_batch_completion_ungrouping` (Impact: 72.9 | O(N^5) | DB: 6)
    * *Intent:* // Test various task name lengths: short, 29, 30, 31, and very long
  * `test_expand_collapse_keyboard_interactio` (Impact: 63.1 | O(N^6) | DB: 5)
  * `render_batch_group_row` (Impact: 55.3 | O(N^4) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 403`, `structural_boundaries: 731`, `args: 118`, `func_start: 121`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 65`, `state_mutation: 502`, `dead_code: 1`, `fragile_debt: 5`, `orphaned_logic: 46`
* *Architecture:* `api: 36`, `concurrency: 1`, `import: 18`
* *Defense:* `safety: 485`, `doc: 123`, `test: 126`, `sync_locks: 58`, `immutability_locks: 24`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` parking_lot::Mutex, Serialize, widgets::
        Block, color_eyre::eyre::Result, Row, SelectionEntry, TaskResult, Direction...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/nx/src/native/tui/app.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.175 IQR)
- **Top Global Matches:** file_cluster_13: 13.175, file_cluster_8: 13.22, file_cluster_17: 13.401
- **Magnitude:** 1770.18 | **LOC:** 2669 | **CtrlFlow:** 34.8% | **Authorship Centralization:** 44.4%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 27
- **Risk Profile:** Cognitive Load (17.2773%), Tech Debt (8.1456%)
**Top Internal Functions/Classes:**
  * `handle_event` (Impact: 333.9 | O(N^6) | DB: 2)
  * `render_batch_terminal_pane_internal` (Impact: 291.0 | O(N^6) | DB: 27)
  * `handle_key_event` (Impact: 172.1 | O(2^N) | DB: 4)
  * `init` (Impact: 135.6 | O(2^N) | DB: 1)
  * `setup_pane_pty` (Impact: 50.9 | O(N^4) | DB: 2)
    * *Intent:* // TODO: move this to the layout manager?
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 161`, `structural_boundaries: 302`, `args: 114`, `func_start: 86`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 143`, `planned_debt: 2`
* *Architecture:* `io: 2`, `api: 41`, `concurrency: 7`, `import: 43`
* *Defense:* `safety: 191`, `doc: 56`, `sync_locks: 43`, `immutability_locks: 3`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` parking_lot::Mutex, TuiMode, TerminalPaneData, super::tui, selection manager, color_eyre::eyre::Result, TaskResult, super::components::countdown_popup::CountdownPopup...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/nx/src/native/plugins/js/ts_import_locators.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.918 IQR)
- **Top Global Matches:** file_cluster_8: 10.918, file_cluster_16: 11.092, file_cluster_13: 11.224
- **Magnitude:** 1128.58 | **LOC:** 1740 | **CtrlFlow:** 27.2% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (13.2386%), Tech Debt (17.2291%)
**Top Internal Functions/Classes:**
  * `next` (Impact: 515.5 | O(2^N) | DB: 1)
  * `find_specifier_in_import` (Impact: 201.7 | O(N^6) | DB: 3)
  * `find_specifier_in_export` (Impact: 174.9 | O(N^6) | DB: 4)
  * `find_imports_with_ast` (Impact: 79.8 | O(N^6) | DB: 4)
  * `should_find_typeof_import_in_ensure_pack` (Impact: 16.7 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 94`, `structural_boundaries: 251`, `args: 41`, `func_start: 24`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 76`, `state_mutation: 36`, `planned_debt: 1`, `orphaned_logic: 7`
* *Architecture:* `api: 11`, `concurrency: 20`, `import: 28`
* *Defense:* `safety: 94`, `test: 48`, `immutability_locks: 140`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` tracing::trace, swc_common::BytePos, Import, swc_ecma_parser::lexer::Lexer, Default_, super::*, swc_ecma_parser::token::Word::Ident, Function...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/nx/src/native/metrics/collector.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.749 IQR)
- **Top Global Matches:** file_cluster_13: 12.749, file_cluster_8: 12.759, file_cluster_0: 12.84
- **Magnitude:** 1094.88 | **LOC:** 1583 | **CtrlFlow:** 29.6% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 28
- **Risk Profile:** Cognitive Load (10.1714%), Tech Debt (53.3894%)
**Top Internal Functions/Classes:**
  * `run_baseline_if_needed` (Impact: 825.0 | O(2^N) | DB: 28)
    * *Intent:* /// Establish CPU baselines for all processes when there are processes needing a baseline. /// Uses ...
  * `test_concurrent_group_creation_with_subp` (Impact: 39.2 | O(N^6))
    * *Intent:* /// Register the main CLI process for metrics collection #[napi]
  * `test_lock_order_consistency_across_regis` (Impact: 34.4 | O(N^6))
  * `drop` (Impact: 30.6 | O(2^N) | DB: 1)
  * `test_main_cli_subprocesses_cleanup` (Impact: 8.6 | O(N^3))
    * *Intent:* // Wait for the collection thread to finish // When it drops, the channel sender is dropped, signali...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 188`, `args: 51`, `func_start: 43`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 66`, `fragile_debt: 1`, `duplicate_logic: 2`, `orphaned_logic: 10`
* *Architecture:* `api: 12`, `concurrency: 12`, `import: 23`
* *Defense:* `safety: 140`, `doc: 84`, `test: 54`, `sync_locks: 34`, `immutability_locks: 5`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` parking_lot::Mutex, ProcessMetadata, CollectorConfig, IndividualTaskRegistration, DashSet, std::sync::Arc, ThreadsafeFunctionCallMode, GroupInfo...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/nx/src/native/tui/inline_app.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.726 IQR)
- **Top Global Matches:** file_cluster_13: 12.726, file_cluster_8: 12.822, file_cluster_0: 12.977
- **Magnitude:** 1052.08 | **LOC:** 1775 | **CtrlFlow:** 31.5% | **Authorship Centralization:** 60.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (14.8768%), Tech Debt (19.9282%)
**Top Internal Functions/Classes:**
  * `handle_event` (Impact: 281.6 | O(N^6) | DB: 2)
  * `render_inline_status` (Impact: 133.1 | O(N^6) | DB: 13)
  * `render_scrollback_above_tui` (Impact: 100.8 | O(2^N) | DB: 2)
  * `handle_interactive_key` (Impact: 81.2 | O(N^4) | DB: 2)
  * `handle_action` (Impact: 45.6 | O(N^6) | DB: 2)
    * *Intent:* // Show status message in bottom chrome
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 105`, `structural_boundaries: 228`, `args: 61`, `func_start: 46`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 69`, `planned_debt: 1`, `orphaned_logic: 6`
* *Architecture:* `api: 3`, `concurrency: 25`, `import: 39`
* *Defense:* `safety: 128`, `doc: 73`, `test: 34`, `sync_locks: 26`, `immutability_locks: 2`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` TaskTarget, parking_lot::Mutex, arboard::Clipboard, Borders, TuiMode, super::tui, crate::native::tui::theme::THEME, color_eyre::eyre::Result...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/nx/src/plugins/js/lock-file/__fixtures__/pnpm-regression/pnpm-lock.yaml.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.22%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.419 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.277 IQR)
- **Top Global Matches:** file_cluster_8: 11.419, file_cluster_0: 11.53, file_cluster_7: 11.979
- **Magnitude:** 987.51 | **LOC:** 16458 | **CtrlFlow:** 75.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (4.9259%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 632`, `structural_boundaries: 205`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 2`
* *Architecture:* `io: 182`, `api: 22`, `concurrency: 62`, `import: 16`
* *Defense:* `safety: 13`, `doc: 347`, `immutability_locks: 8`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` core@7.24.0):
    resolution: integrity: sha512-OxBdcnF04bpdQdR3i4giHZNZQn7cm8RQKcSwA17wAAqEELo1ZOwp5FFgeptWUQXFyT9kwHo10aqqauYkRZPCAg==
    engines: node:, core@7.24.5), core@7.24.5), core@7.24.0), 2SkOrRk4pNBPg5IPZ+dOxcmkK5IyuBcxiNPyyYowPGUReyBvrvZs7IlQ==
    engines: node:, core@7.24.0)
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/nx/src/native/pseudo_terminal/pseudo_terminal.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.906 IQR)
- **Top Global Matches:** file_cluster_13: 12.906, file_cluster_4: 12.923, file_cluster_0: 13.147
- **Magnitude:** 928.58 | **LOC:** 386 | **CtrlFlow:** 36.6% | **Authorship Centralization:** 60.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 24
- **Risk Profile:** Cognitive Load (73.8707%), Tech Debt (10.1892%)
**Top Internal Functions/Classes:**
  * `new` (Impact: 455.1 | O(2^N) | DB: 24)
  * `run_command` (Impact: 319.0 | O(N^6) | DB: 10)
  * `get_directory` (Impact: 15.6 | O(N^4))
  * `command_builder` (Impact: 11.2 | O(N^3) | DB: 2)
  * `can_run_commands` (Impact: 7.7 | O(N^3) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 109`, `args: 14`, `func_start: 6`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 64`, `orphaned_logic: 1`
* *Architecture:* `io: 6`, `api: 15`, `concurrency: 32`, `import: 15`
* *Defense:* `safety: 52`, `test: 1`, `sync_locks: 7`, `immutability_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` parking_lot::Mutex, process_killer::ProcessKiller, sync::
        Arc, tty::IsTty, crossterm::
    terminal, RwLock, napi::bindgen_prelude::*, unbounded...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/nx/src/native/tasks/hash_planner.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.24 IQR)
- **Top Global Matches:** file_cluster_17: 12.24, file_cluster_8: 12.262, file_cluster_13: 12.332
- **Magnitude:** 735.3 | **LOC:** 553 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (15.7604%), Tech Debt (19.505%)
**Top Internal Functions/Classes:**
  * `get_plans_internal` (Impact: 238.9 | O(2^N) | DB: 2)
  * `gather_dependency_input` (Impact: 124.2 | O(N^6) | DB: 2)
  * `gather_self_inputs` (Impact: 73.7 | O(N^6))
  * `gather_project_inputs` (Impact: 50.2 | O(N^6) | DB: 1)
  * `find_external_dependency_node_name` (Impact: 49.0 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 84`, `args: 29`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 36`, `dead_code: 1`, `planned_debt: 3`, `orphaned_logic: 2`
* *Architecture:* `api: 5`, `import: 12`
* *Defense:* `safety: 66`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` tracing::trace, get_inputs, crate::native::tasks::
    dep_outputs::get_dep_output, NxJson, get_inputs_for_dependency, types::Task, napi::bindgen_prelude::External, std::sync::Arc...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/nx/src/native/telemetry/service.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.022 IQR)
- **Top Global Matches:** file_cluster_8: 13.022, file_cluster_16: 13.03, file_cluster_13: 13.061
- **Magnitude:** 730.0 | **LOC:** 669 | **CtrlFlow:** 32.7% | **Authorship Centralization:** 80.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 24
- **Risk Profile:** Cognitive Load (16.8149%), Tech Debt (17.0432%)
**Top Internal Functions/Classes:**
  * `background_sender` (Impact: 137.9 | O(N^6) | DB: 24)
  * `send_batches` (Impact: 76.4 | O(N^5) | DB: 3)
  * `log_page_view` (Impact: 61.6 | O(N^5))
  * `new` (Impact: 55.2 | O(2^N) | DB: 2)
  * `sanitize_params` (Impact: 55.1 | O(N^5) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 134`, `args: 34`, `func_start: 18`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 95`, `duplicate_logic: 2`
* *Architecture:* `io: 1`, `api: 34`, `concurrency: 14`, `import: 7`
* *Defense:* `safety: 94`, `doc: 29`, `sync_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` reqwest::Client, napi::bindgen_prelude::*, parking_lot::Mutex, std::time::Duration, ClientBuilder, std::collections::HashMap, super::constants::*, Sender...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/nx/src/plugins/js/lock-file/__fixtures__/nextjs/pnpm-lock-v6.yaml.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.2%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.88 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.156 IQR)
- **Top Global Matches:** file_cluster_8: 10.88, file_cluster_0: 11.058, file_cluster_7: 11.446
- **Magnitude:** 653.64 | **LOC:** 10421 | **CtrlFlow:** 71.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (4.5748%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 420`, `structural_boundaries: 168`, `func_start: 3`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `io: 136`, `api: 12`, `concurrency: 24`, `import: 14`
* *Defense:* `safety: 14`, `doc: 288`, `immutability_locks: 5`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` core@7.21.3), core@7.21.3), KFL5EWDjlJuMsUGRFb8fQgQ==
    engines: node:
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/nx/src/native/cache/cache.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.914 IQR)
- **Top Global Matches:** file_cluster_0: 11.914, file_cluster_8: 12.0, file_cluster_13: 12.025
- **Magnitude:** 638.14 | **LOC:** 470 | **CtrlFlow:** 50.6% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (16.0996%), Tech Debt (8.5834%)
**Top Internal Functions/Classes:**
  * `put` (Impact: 115.4 | O(N^4) | DB: 3)
  * `get` (Impact: 85.1 | O(2^N) | DB: 1)
  * `check_cache_fs_in_sync` (Impact: 74.6 | O(N^6) | DB: 3)
  * `copy_files_from_cache` (Impact: 69.3 | O(N^5) | DB: 3)
  * `apply_remote_cache_results` (Impact: 56.4 | O(N^4) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 80`, `args: 23`, `func_start: 15`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 15`, `planned_debt: 1`
* *Architecture:* `io: 5`, `api: 21`, `concurrency: 1`, `import: 14`
* *Defense:* `safety: 69`, `sync_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` regex::Regex, std::fs::create_dir_all, read_to_string, PathBuf, std::time::Instant, napi::bindgen_prelude::External, std::sync::Arc, sysinfo::Disks...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/nx/src/plugins/js/lock-file/__fixtures__/nextjs/pnpm-lock.yaml.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.2%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.64 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.077 IQR)
- **Top Global Matches:** file_cluster_8: 10.64, file_cluster_0: 11.022, file_cluster_7: 11.233
- **Magnitude:** 632.39 | **LOC:** 10285 | **CtrlFlow:** 70.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (4.8432%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 406`, `structural_boundaries: 171`, `func_start: 3`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `io: 137`, `api: 12`, `concurrency: 24`, `import: 14`
* *Defense:* `safety: 12`, `doc: 245`, `immutability_locks: 5`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` : 7.8.3_@babel+core@7.20.5, KFL5EWDjlJuMsUGRFb8fQgQ==
    engines: node:, : 7.18.9_@babel+core@7.20.5
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/nx/src/native/tui/components/task_selection_manager.rs` (RUST | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.047 IQR)
- **Top Global Matches:** file_cluster_8: 13.047, file_cluster_0: 13.148, file_cluster_7: 13.297
- **Magnitude:** 568.3 | **LOC:** 931 | **CtrlFlow:** 31.3% | **Authorship Centralization:** 75.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (11.4901%), Tech Debt (22.27%)
**Top Internal Functions/Classes:**
  * `handle_in_progress_task_finished` (Impact: 171.0 | O(2^N) | DB: 7)
  * `previous` (Impact: 37.5 | O(N^5) | DB: 1)
  * `get_selected_task_index` (Impact: 37.3 | O(N^5) | DB: 2)
  * `next` (Impact: 37.0 | O(N^5) | DB: 1)
  * `ensure_selected_visible` (Impact: 30.9 | O(N^4) | DB: 1)
    * *Intent:* /// Scroll up by the specified number of lines
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 101`, `args: 25`, `func_start: 39`, `class_start: 5`
* *Risk/State:* `state_mutation: 49`, `orphaned_logic: 6`
* *Architecture:* `api: 38`
* *Defense:* `safety: 124`, `doc: 75`, `test: 21`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` super::*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/gradle/batch-runner/src/test/kotlin/dev/nx/gradle/runner/OutputProcessorTest.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.086 IQR)
- **Top Global Matches:** file_cluster_8: 9.086, file_cluster_0: 9.761, file_cluster_16: 9.925
- **Magnitude:** 550.15 | **LOC:** 446 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.9817%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `args: 19`, `func_start: 19`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 1`
* *Architecture:* `import: 6`
* *Defense:* `safety: 7`, `test: 61`, `immutability_locks: 102`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` org.junit.jupiter.api.Assertions.*, org.junit.jupiter.api.Nested, org.junit.jupiter.api.Test, dev.nx.gradle.data.TaskResult, dev.nx.gradle.data.GradleTask, java.io.ByteArrayOutputStream
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/nx/src/native/db/initialize.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.311 IQR)
- **Top Global Matches:** file_cluster_8: 11.311, file_cluster_13: 11.455, file_cluster_0: 11.611
- **Magnitude:** 542.2 | **LOC:** 506 | **CtrlFlow:** 57.8% | **Authorship Centralization:** 80.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (6.8031%), Tech Debt (28.2878%)
**Top Internal Functions/Classes:**
  * `initialize_db` (Impact: 198.3 | O(2^N) | DB: 3)
  * `diagnose_filesystem_issue` (Impact: 65.1 | O(N^5))
    * *Intent:* /// Diagnose specific filesystem issues when setting journal mode fails
  * `set_journal_mode` (Impact: 56.5 | O(N^5))
  * `create_io_error` (Impact: 33.0 | O(N^4) | DB: 3)
    * *Intent:* /// Creates a user-friendly error message for filesystem IO errors with specific guidance based on e...
  * `create_all_tables` (Impact: 27.9 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 49`, `args: 26`, `func_start: 19`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 11`, `dead_code: 1`, `planned_debt: 1`, `orphaned_logic: 4`
* *Architecture:* `io: 5`, `api: 4`, `import: 13`
* *Defense:* `safety: 48`, `doc: 17`, `test: 6`, `sync_locks: 8`, `immutability_locks: 7`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::sync::OnceLock, crate::native::db::connection::NxDbConnection, crate::native::tasks::running_tasks_service::SCHEMA, tracing::debug, super::*, write, std::path::Path, std::fs::File...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/maven/maven-plugin/src/main/kotlin/dev/nx/maven/targets/NxTargetFactory.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.626 IQR)
- **Top Global Matches:** file_cluster_8: 12.626, file_cluster_13: 12.757, file_cluster_16: 12.779
- **Magnitude:** 522.84 | **LOC:** 734 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 77.8%
- **Algorithmic:** O(N^3) | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (44.0959%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `createSimpleGoalTarget` (Impact: 42.4 | O(N^2) | DB: 8)
  * `createCiPhaseTarget` (Impact: 41.1 | O(N^1) | DB: 7)
  * `createPhaseBatchTarget` (Impact: 40.4 | O(N^3) | DB: 13)
  * `createIndividualGoalTargets` (Impact: 38.7 | O(N^3) | DB: 3)
  * `createRegularPhaseTarget` (Impact: 28.7 | O(N^1) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 85`, `args: 52`, `func_start: 20`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 146`
* *Architecture:* `io: 2`, `api: 2`, `import: 16`
* *Defense:* `safety: 16`, `doc: 5`, `immutability_locks: 106`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.148
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` org.apache.maven.plugin.descriptor.MojoDescriptor, org.apache.maven.plugin.descriptor.PluginDescriptor, org.apache.maven.execution.MavenSession, org.apache.maven.model.PluginExecution, dev.nx.maven.GitIgnoreClassifier, org.apache.maven.project.MavenProject, java.io.File, org.apache.maven.model.Plugin...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/dotnet/analyzer/Program.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.219 IQR)
- **Top Global Matches:** file_cluster_8: 11.219, file_cluster_13: 11.38, file_cluster_17: 11.469
- **Magnitude:** 518.08 | **LOC:** 164 | **CtrlFlow:** 40.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (38.7611%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 29`, `args: 3`, `func_start: 27`
* *Risk/State:* `state_mutation: 31`
* *Architecture:* `import: 6`
* *Defense:* `safety: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` MsbuildAnalyzer, Microsoft.Build.Locator, System.Text.Json, MsbuildAnalyzer.Models, MsbuildAnalyzer.Utilities, System.Text.Json.Serialization
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/nx/src/native/tui/tui.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.175 IQR)
- **Top Global Matches:** file_cluster_13: 13.175, file_cluster_4: 13.218, file_cluster_16: 13.264
- **Magnitude:** 511.94 | **LOC:** 629 | **CtrlFlow:** 35.6% | **Authorship Centralization:** 57.1%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 22
- **Risk Profile:** Cognitive Load (39.5725%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `start` (Impact: 186.1 | O(2^N) | DB: 4)
  * `restore_terminal` (Impact: 93.1 | O(N^4) | DB: 22)
    * *Intent:* /// Stop the event loop task. /// /// This properly yields to the tokio runtime, allowing the inner ...
  * `new_with_mode` (Impact: 32.8 | O(N^5) | DB: 6)
  * `terminal` (Impact: 17.8 | O(2^N))
  * `inline_tui_unsupported_reason` (Impact: 14.5 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 76`, `args: 25`, `func_start: 21`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 41`
* *Architecture:* `io: 8`, `api: 29`, `concurrency: 37`, `import: 10`
* *Defense:* `safety: 39`, `doc: 63`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::native::tui::theme::THEME, color_eyre::eyre::Result, LeaveAlternateScreen, KeyEvent, tokio_util::sync::CancellationToken, std::
    env, KeyEventKind, crossterm::
    cursor...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/nx/src/native/tui/tui_state.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.797 IQR)
- **Top Global Matches:** file_cluster_0: 12.797, file_cluster_13: 12.836, file_cluster_16: 12.929
- **Magnitude:** 504.0 | **LOC:** 1002 | **CtrlFlow:** 9.9% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (11.4615%), Tech Debt (99.9998%)
**Top Internal Functions/Classes:**
  * `new` (Impact: 24.1 | O(2^N) | DB: 1)
    * *Intent:* /// Create a new TuiState with the given tasks and configuration
  * `get_focused_item_id` (Impact: 18.0 | O(N^4))
    * *Intent:* /// Get the item ID (task or batch) that should be shown in inline mode /// Priority: focused pane i...
  * `call_done_callback` (Impact: 14.5 | O(N^3))
    * *Intent:* /// Call the done callback if it exists /// Can be called multiple times safely /// If is_forced_shu...
  * `complete_batch_metadata` (Impact: 11.3 | O(N^3) | DB: 1)
    * *Intent:* /// Update batch as completed
  * `should_quit` (Impact: 10.7 | O(N^3))
    * *Intent:* // === Quit Management Methods === /// Check if the application should quit
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 136`, `args: 22`, `func_start: 83`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 44`, `planned_debt: 1`, `duplicate_logic: 8`, `orphaned_logic: 47`
* *Architecture:* `api: 72`, `concurrency: 27`, `import: 25`
* *Defense:* `safety: 122`, `doc: 82`, `test: 62`, `sync_locks: 6`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` parking_lot::Mutex, std::sync::Arc, ThreadsafeFunctionCallMode, super::config::TuiConfig, crate::native::tui::config, TaskGraph, napi::Status, RunMode...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `packages/angular/src/generators/setup-ssr/lib/add-dependencies.ts` (TYPESCRIPT) | Magnitude: 1.87 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 37, branch: 7, decorators: 7, immutability_locks: 5
- `packages/remix/src/utils/get-default-export-name.ts` (TYPESCRIPT) | Magnitude: 1.02 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 5, branch: 4, api: 3, safety: 2
- `packages/angular/src/builders/utilities/buildable-libs.ts` (TYPESCRIPT) | Magnitude: 1.48 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 23, branch: 9, structural_boundaries: 6, safety: 4
- `packages/react/src/migrations/update-21-0-0/update-babel-loose.ts` (TYPESCRIPT) | Magnitude: 1.79 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 25, structural_boundaries: 12, branch: 10, args: 4
- `packages/angular/src/generators/move/move-impl.ts` (TYPESCRIPT) | Magnitude: 0.54 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 6, indent_spaces: 6, import: 3, concurrency: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `packages/eslint-plugin/src/configs/typescript.ts` (TYPESCRIPT) | Magnitude: 1.49 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 30, doc: 21, decorators: 18, structural_boundaries: 10
- `graph/client-e2e/src/plugins/index.js` (JAVASCRIPT) | Magnitude: 4.04 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: api: 2, structural_boundaries: 1, args: 1, func_start: 1
- `packages/eslint-plugin/src/flat-configs/typescript.ts` (TYPESCRIPT) | Magnitude: 0.8 | Delta: **0.055 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 37, doc: 19, decorators: 16, structural_boundaries: 13
- `packages/eslint-plugin/src/configs/react-typescript.ts` (TYPESCRIPT) | Magnitude: 1.67 | Delta: **0.09 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 34, doc: 7, decorators: 6, events: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `packages/module-federation/src/plugins/nx-module-federation-plugin/angular/nx-module-federation-plugin.ts` (TYPESCRIPT) | Magnitude: 26.29 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 80, state_mutation: 39, branch: 31, structural_boundaries: 20
- `packages/eslint-plugin/angular.ts` (TYPESCRIPT) | Magnitude: 1.72 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 6, indent_spaces: 5, import: 3, api: 2
- `packages/eslint-plugin/typescript.ts` (TYPESCRIPT) | Magnitude: 1.72 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 6, indent_spaces: 5, import: 3, api: 2
- `packages/expo/src/generators/application/lib/add-eas-scripts.ts` (TYPESCRIPT) | Magnitude: 0.69 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 6, branch: 4, args: 3
- `packages/react/src/generators/library/lib/install-common-dependencies.ts` (TYPESCRIPT) | Magnitude: 5.39 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 60, branch: 13, decorators: 11, state_mutation: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `packages/nx/src/native/utils/git.rs` (RUST) | Magnitude: 62.96 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 14, safety: 11, branch: 9
- `packages/nx/src/native/tasks/task_hasher.rs` (RUST) | Magnitude: 414.3 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 430, structural_boundaries: 93, branch: 63, generics: 60
- `packages/js/src/utils/typescript/configuration.ts` (TYPESCRIPT) | Magnitude: 5.53 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 71, structural_boundaries: 21, generics: 15, branch: 9
- `packages/gradle/project-graph/src/main/kotlin/dev/nx/gradle/data/GradleNodeReport.kt` (KOTLIN) | Magnitude: 15.2 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: decorators: 4, generics: 4, immutability_locks: 4, indent_spaces: 4
- `packages/create-nx-workspace/src/internal-utils/yargs-options.ts` (TYPESCRIPT) | Magnitude: 5.81 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 69, structural_boundaries: 33, generics: 16, api: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `graph/ui-code-block/src/lib/json-code-block.tsx` (TYPESCRIPT) | Magnitude: 10.6 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 74, structural_boundaries: 21, ui_framework: 15, args: 11
- `packages/react-native/src/utils/find-all-npm-dependencies.ts` (TYPESCRIPT) | Magnitude: 1.88 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 5, args: 3, state_mutation: 3
- `packages/eslint/src/generators/convert-to-inferred/convert-to-inferred.ts` (TYPESCRIPT) | Magnitude: 10.04 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 146, branch: 34, structural_boundaries: 32, args: 14
- `packages/devkit/src/generators/executor-options-utils.ts` (TYPESCRIPT) | Magnitude: 4.56 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 35, branch: 10, args: 9, generics: 8
- `packages/eslint/src/generators/convert-to-flat-config/converters/json-converter.ts` (TYPESCRIPT) | Magnitude: 26.84 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 348, state_mutation: 100, branch: 63, structural_boundaries: 48

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `packages/expo/src/generators/application/files/nx-welcome/unclaimed/src/app/App.tsx.template` (TYPESCRIPT) | Magnitude: 116.9 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 716, ui_framework: 148, generics: 145, structural_boundaries: 18
- `nx-dev/ui-common/src/lib/webinar-notifier.tsx` (TYPESCRIPT) | Magnitude: 1.23 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 109, ui_framework: 24, structural_boundaries: 12, branch: 10
- `nx-dev/ui-markdoc/src/lib/tags/stackblitz-button.component.tsx` (TYPESCRIPT) | Magnitude: 0.5 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 35, ui_framework: 10, structural_boundaries: 5, io: 3
- `nx-dev/ui-common/src/lib/hubspot-form.tsx` (TYPESCRIPT) | Magnitude: 26.37 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 125, state_mutation: 101, branch: 36, ui_framework: 27
- `nx-dev/ui-video-courses/src/lib/course-hero.tsx` (TYPESCRIPT) | Magnitude: 0.89 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 22, ui_framework: 8, structural_boundaries: 5, import: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `packages/rollup/src/plugins/postcss/loaders/stylus-loader.ts` (TYPESCRIPT) | Magnitude: 9.89 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 59, state_mutation: 19, structural_boundaries: 13, args: 9
- `packages/angular/src/generators/ng-add/migrators/projects/app.migrator.ts` (TYPESCRIPT) | Magnitude: 95.06 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 482, state_mutation: 402, branch: 135, structural_boundaries: 50
- `packages/angular-rspack/src/lib/plugins/angular-rspack-plugin.ts` (TYPESCRIPT) | Magnitude: 52.36 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 332, branch: 80, encapsulation: 70, concurrency: 63
- `packages/react/src/generators/host/host.ts` (TYPESCRIPT) | Magnitude: 14.68 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 164, structural_boundaries: 41, branch: 35, concurrency: 31
- `packages/angular-rspack/src/lib/utils/index-file/add-event-dispatch-contract.ts` (TYPESCRIPT) | Magnitude: 1.36 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 7, concurrency: 4, branch: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `packages/nx/src/utils/call-sites.ts` (TYPESCRIPT) | Magnitude: 0.56 | Delta: **0.278 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 4, immutability_locks: 3, args: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `packages/dotnet/analyzer/Models/NxJsonConfig.cs` (CSHARP) | Magnitude: 17.6 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 6, state_mutation: 3, structural_boundaries: 2, api: 2
- `packages/dotnet/analyzer/Models/Target.cs` (CSHARP) | Magnitude: 25.26 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 30, structural_boundaries: 11, api: 10, branch: 9
- `packages/dotnet/analyzer/Models/PluginOptions.cs` (CSHARP) | Magnitude: 32.24 | Delta: **0.117 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 27, api: 9, state_mutation: 8, indent_spaces: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `packages/angular/src/migrations/update-21-5-0/remove-default-karma-configuration-files.ts` (TYPESCRIPT) | Magnitude: 21.49 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 55, branch: 21, state_mutation: 12, immutability_locks: 9
- `packages/js/src/utils/assets/assets.ts` (TYPESCRIPT) | Magnitude: 2.85 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 47, structural_boundaries: 13, branch: 7, args: 7
- `packages/nx/src/plugins/js/index.ts` (TYPESCRIPT) | Magnitude: 13.8 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 189, structural_boundaries: 42, branch: 34, immutability_locks: 31
- `packages/storybook/src/migrations/update-22-1-0/migrate-to-storybook-10.spec.ts` (TYPESCRIPT) | Magnitude: 0.67 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 32, structural_boundaries: 12, args: 10, func_start: 10
- `packages/gradle/project-graph/src/main/kotlin/dev/nx/gradle/utils/parsing/RegexTestParser.kt` (KOTLIN) | Magnitude: 120.42 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 56, branch: 38, state_mutation: 27, immutability_locks: 17

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `packages/nx/src/tasks-runner/task-orchestrator.ts` -> Churn: **63.82%** | Cog Load: 99.9974% | Debt: 8.05%
- `packages/create-nx-workspace/src/create-workspace.ts` -> Churn: **62.92%** | Cog Load: 64.6422% | Debt: 0.0%
- `packages/nx/src/command-line/migrate/migrate.ts` -> Churn: **62.92%** | Cog Load: 98.3733% | Debt: 8.2392%
- `packages/nx/src/daemon/client/client.ts` -> Churn: **60.35%** | Cog Load: 100.0% | Debt: 28.9578%
- `packages/nx/src/daemon/server/server.ts` -> Churn: **55.46%** | Cog Load: 62.8739% | Debt: 14.3599%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `packages/gradle/batch-runner/src/test/kotlin/dev/nx/gradle/runner/OutputProcessorTest.kt` -> **Louie Weng** (100.0% isolated ownership) | Magnitude: 550.15
- `packages/dotnet/analyzer/Program.cs` -> **Craigory Coppola** (100.0% isolated ownership) | Magnitude: 518.08
- `packages/nx/src/native/cache/http_remote_cache.rs` -> **Sander Boelhouwers** (100.0% isolated ownership) | Magnitude: 411.54
- `packages/nx/src/native/cache/file_ops.rs` -> **Craigory Coppola** (100.0% isolated ownership) | Magnitude: 401.42
- `packages/nx/src/native/tui/components/layout_manager.rs` -> **Craigory Coppola** (100.0% isolated ownership) | Magnitude: 385.88

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `packages/nx/src/project-graph/plugins/loaded-nx-plugin.ts` -> **Severity: 0.028** (Bridge: 0.0003 * Flux: 100.0%)
- `packages/nx/src/project-graph/build-project-graph.ts` -> **Severity: 0.021** (Bridge: 0.0003 * Flux: 63.7138%)
- `packages/nx/src/project-graph/project-graph-builder.ts` -> **Severity: 0.018** (Bridge: 0.0002 * Flux: 99.9999%)
- `packages/nx/src/command-line/graph/graph.ts` -> **Severity: 0.016** (Bridge: 0.0003 * Flux: 55.7463%)
- `packages/nx/src/tasks-runner/pseudo-terminal.ts` -> **Severity: 0.013** (Bridge: 0.0001 * Flux: 99.998%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `packages/nx/src/devkit-exports.ts` -> **Severity: 1810.3** (Blast Radius: 18.103 * Doc Risk: 100.0%)
- `packages/nx/src/utils/workspace-root.ts` -> **Severity: 1628.023** (Blast Radius: 17.317 * Doc Risk: 94.013%)
- `packages/nx/src/native/pseudo_terminal/child_process.rs` -> **Severity: 1395.3** (Blast Radius: 13.953 * Doc Risk: 100.0%)
- `packages/devkit/src/utils/semver.ts` -> **Severity: 742.1** (Blast Radius: 7.421 * Doc Risk: 100.0%)
- `packages/nx/src/devkit-internals.ts` -> **Severity: 410.0** (Blast Radius: 4.1 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
