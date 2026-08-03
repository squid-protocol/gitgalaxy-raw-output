# ARCHITECTURAL_BRIEF: TypeScript
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_typescript/TypeScript` |
| **Timestamp** | `2026-08-03T19:53:18.717622+00:00` |
| **Scan Duration** | `205.29s` |
| **Git Branch** | `main` |
| **Git Commit** | `7b8cb3bdf82f400642b73173f941335775d6f730` |
| **Git Remote** | `https://github.com/microsoft/TypeScript.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 37532 malicious artifacts.

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
| Total Artifacts | 81366 |
| Analyzed Artifacts (Scanned) | 49847 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 31519 |
| Total LOC | 2155730 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 61.3% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2234 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 37 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 19998 | 488696 | 40.1% |
| JAVASCRIPT | 17532 | 1530495 | 35.2% |
| PLAINTEXT | 9861 | 11 | 19.8% |
| JSON | 2423 | 136295 | 4.9% |
| MARKDOWN | 29 | 0 | 0.1% |
| YAML | 2 | 227 | 0.0% |
| SHELL | 2 | 6 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.005`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 30021 | 60.2% |
| file_cluster_9 | 3065 | 6.1% |
| file_cluster_13 | 2482 | 5.0% |
| file_cluster_16 | 1300 | 2.6% |
| file_cluster_4 | 970 | 1.9% |
| file_cluster_0 | 684 | 1.4% |
| file_cluster_2 | 428 | 0.9% |
| file_cluster_17 | 377 | 0.8% |
| file_cluster_11 | 313 | 0.6% |
| file_cluster_6 | 119 | 0.2% |
| file_cluster_7 | 80 | 0.2% |
| file_cluster_15 | 71 | 0.1% |
| file_cluster_12 | 42 | 0.1% |
| file_cluster_1 | 5 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 9889 | 19.8% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 31519*

**Composition by Extension & Reason:**
- `.symbols`: 13942x Excluded (Unsupported Extension: '.symbols'), 74x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.types`: 13942x Excluded (Unsupported Extension: '.types'), 74x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ts`: 875x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 225x Excluded: Neighborhood Micro-Mass Limit Exceeded, 6x Excluded (Binary Format Detected)
- `.map`: 538x Excluded (Unsupported Extension: '.map'), 263x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 64x Excluded (Saturation: Line 1 exceeds 500 chars)
- `.js`: 85x Excluded (Saturation: Line 94 exceeds 500 chars), 82x Excluded (Saturation: Line 95 exceeds 500 chars), 80x Excluded (Saturation: Line 89 exceeds 500 chars)
- `.baseline`: 458x Excluded (Unsupported Extension: '.baseline'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 89x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Lexical Monotony: High structural repetition detected in 3072 LOC), 1x Excluded (Machine-Generated Source Code Signature: 56 LOC)
- `.md`: 72x Excluded (Lexical Monotony: High structural repetition detected in 2354 LOC), 4x Excluded (Lexical Monotony: High structural repetition detected in 2216 LOC), 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.diff`: 24x Excluded (Unsupported Extension: '.diff')
- `.yml`: 18x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 8560 LOC)
- `.lcl`: 13x Unsupported Format (.lcl)
- `.yaml`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mjs`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 10.1 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 26.1 | 8.3 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 0.4 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 0.6 | 0.0 | 0.0 |
| API Exposure | 0.0 | 20.9 | 2.4 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 4.4 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 0.3 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 6.2 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 67.2 | 80.0 | 100.0 |
| Instability Exposure | 0.0 | 1.3 | 0.1 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 2.6 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 1.0 | 0.0 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 5.8 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 4.4 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tests/baselines/reference/reuseProgramStructure/should-not-reuse-ambient-module-declarations-from-non-modified-files.js` (Hits: 651)
- `src/testRunner/unittests/tsserver/projectReferenceCompileOnSave.ts` (Hits: 296)
- `src/testRunner/unittests/services/convertToAsyncFunction.ts` (Hits: 271)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **module.ts** (`src/compiler/transformers/module/module.ts`) — 83 inbound connections
2. **package.json** (`package.json`) — 68 inbound connections
3. **path.ts** (`src/compiler/path.ts`) — 45 inbound connections
4. **utils.cjs** (`scripts/eslint/rules/utils.cjs`) — 40 inbound connections
5. **core.ts** (`src/compiler/core.ts`) — 30 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **tests.ts** (`src/testRunner/tests.ts`) — 233 outbound dependencies
2. **ts.ts** (`src/compiler/_namespaces/ts.ts`) — 75 outbound dependencies
3. **nodeFactory.ts** (`src/compiler/factory/nodeFactory.ts`) — 75 outbound dependencies
4. **ts.codefix.ts** (`src/services/_namespaces/ts.codefix.ts`) — 74 outbound dependencies
5. **program.ts** (`src/compiler/program.ts`) — 71 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `log` (@ `src/compiler/debug.ts`) -> Impact: **4418.1** | LOC: 1067
- `getTokenPosOfNode` (@ `src/compiler/utilities.ts`) -> Impact: **3623.8** | LOC: 1357
- `transformConstructorBodyWorker` (@ `src/compiler/transformers/classFields.ts`) -> Impact: **3145.9** | LOC: 749
  * *Intent:* // 13.15.2 RS: Evaluation // AssignmentExpression : LeftHandSideExpression `=` AssignmentExpression // 1. If |LeftHandSideExpression| is neither an |O...
- `transformModule` (@ `src/compiler/transformers/module/module.ts`) -> Impact: **3084.2** | LOC: 1205
  * *Intent:* /** @internal */
- `createSourceFileAndAssertInvariants` (@ `src/harness/harnessIO.ts`) -> Impact: **2639.2** | LOC: 1131
- `getModuleInstanceStateForAliasTarget` (@ `src/compiler/binder.ts`) -> Impact: **2495.8** | LOC: 1197
- `createCacheableExportInfoMap` (@ `src/services/exportInfoMap.ts`) -> Impact: **2264.7** | LOC: 493
- `getJSSyntacticDiagnosticsForFile` (@ `src/compiler/program.ts`) -> Impact: **2188.8** | LOC: 935
- `emitHelpers` (@ `src/compiler/emitter.ts`) -> Impact: **2183.5** | LOC: 1110
- `run` (@ `tests/baselines/reference/enumLiteralsSubtypeReduction.js`) -> Impact: **2107.4** | LOC: 1028

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `watch` (@ `Herebyfile.mjs`) -> **O(2^N) [Recursive]**
- `emitAsNamespace` (@ `scripts/dtsBundler.mjs`) -> **O(2^N) [Recursive]**
- `next` (@ `tests/baselines/reference/awaitUsingDeclarations.1(target=es2015).js`) -> **O(2^N) [Recursive]**
- `next` (@ `tests/baselines/reference/awaitUsingDeclarations.1(target=es2017).js`) -> **O(2^N) [Recursive]**
- `next` (@ `tests/baselines/reference/awaitUsingDeclarations.1(target=es2022).js`) -> **O(2^N) [Recursive]**
- `next` (@ `tests/baselines/reference/awaitUsingDeclarations.1(target=es5).js`) -> **O(2^N) [Recursive]**
- `next` (@ `tests/baselines/reference/awaitUsingDeclarations.2(target=es2015).js`) -> **O(2^N) [Recursive]**
- `next` (@ `tests/baselines/reference/awaitUsingDeclarations.2(target=es2017).js`) -> **O(2^N) [Recursive]**
- `next` (@ `tests/baselines/reference/awaitUsingDeclarations.2(target=es2022).js`) -> **O(2^N) [Recursive]**
- `next` (@ `tests/baselines/reference/awaitUsingDeclarations.2(target=es5).js`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `describe` (@ `src/testRunner/unittests/services/convertToAsyncFunction.ts`) -> DB Complexity: **817**
- `describe` (@ `src/testRunner/unittests/tsserver/configuredProjects.ts`) -> DB Complexity: **532**
- `describe` (@ `src/testRunner/unittests/tsserver/projectReferenceCompileOnSave.ts`) -> DB Complexity: **486**
- `describe` (@ `src/testRunner/unittests/tsserver/typingsInstaller.ts`) -> DB Complexity: **454**
- `getEncodedRootLength` (@ `src/compiler/path.ts`) -> DB Complexity: **451**
  * *Intent:* /** * Determines whether a path starts with a relative path component (i.e. `.` or `..`). * * @internal */
- `describe` (@ `src/testRunner/unittests/tscWatch/programUpdates.ts`) -> DB Complexity: **399**
- `describe` (@ `src/testRunner/unittests/tsserver/externalProjects.ts`) -> DB Complexity: **368**
- `describe` (@ `src/testRunner/unittests/tsserver/compileOnSave.ts`) -> DB Complexity: **360**
- `describe` (@ `src/testRunner/unittests/tsserver/projects.ts`) -> DB Complexity: **331**
- `verifyImportFixModuleSpecifiers` (@ `src/harness/fourslashImpl.ts`) -> DB Complexity: **289**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `tests/baselines/reference` | 24172 | 645949.28 | 8.8% | 0.0% |
| `tests/baselines/reference/tsserver/projectReferences` | 67 | 22088.55 | 5.54% | 0.0% |
| `tests/baselines/reference/tsserver/declarationFileMaps` | 21 | 13035.06 | 6.07% | 0.0% |
| `tests/cases/compiler` | 6331 | 11624.33 | 6.71% | 0.0% |
| `tests/cases/fourslash` | 6317 | 10572.14 | 3.16% | 0.0% |
| `tests/baselines/reference/tsserver/fourslashServer` | 238 | 9466.74 | 5.84% | 0.0% |
| `tests/baselines/reference/tsserver/completionsIncomplete` | 5 | 9288.79 | 5.46% | 0.0% |
| `tests/baselines/reference/tsserver/projectReferenceCompileOnSave` | 45 | 8235.46 | 5.62% | 0.0% |
| `tests/baselines/reference/transpile` | 390 | 6681.43 | 6.99% | 0.0% |
| `src/compiler` | 38 | 6664.43 | 21.32% | 14.57% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `src/compiler/factory/nodeTests.ts` -> **100.0%** Exposure
- `src/harness/fakesHosts.ts` -> **100.0%** Exposure
- `src/lib/es2015.core.d.ts` -> **100.0%** Exposure
- `src/lib/es2016.array.include.d.ts` -> **100.0%** Exposure
- `src/lib/es2017.object.d.ts` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `scripts/failed-tests.cjs` -> **100.0%** Exposure
- `scripts/regenerate-unicode-identifier-parts.mjs` -> **100.0%** Exposure
- `src/harness/collectionsImpl.ts` -> **100.0%** Exposure
- `src/harness/compilerImpl.ts` -> **100.0%** Exposure
- `src/harness/documentsUtil.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tests/baselines/reference/privacyAccessorDeclFile(target=es2015).js` -> **0** Orphaned Functions | **250** Duplicates
- `tests/baselines/reference/privacyFunctionReturnTypeDeclFile.js` -> **1** Orphaned Functions | **249** Duplicates
- `tests/cases/compiler/privacyAccessorDeclFile.ts` -> **0** Orphaned Functions | **250** Duplicates
- `tests/cases/compiler/resolvingClassDeclarationWhenInBaseTypeResolution.ts` -> **249** Orphaned Functions | **0** Duplicates
- `tests/baselines/reference/privacyAccessorDeclFile(target=es5).js` -> **10** Orphaned Functions | **238** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`tests/baselines/reference/tsserver/fourslashServer/goToSource15_bundler.js`** -> AI Confidence: **99.32%**
2. **`tests/baselines/reference/tsserver/fourslashServer/goToSource7_conditionallyMinified.js`** -> AI Confidence: **99.32%**
3. **`tests/cases/fourslash/importNameCodeFix_require.ts`** -> AI Confidence: **99.32%**
4. **`scripts/dtsBundler.mjs`** -> AI Confidence: **99.31%**
5. **`tests/baselines/reference/jsDeclarationsExportForms(target=es2015).js`** -> AI Confidence: **99.31%**
6. **`tests/baselines/reference/jsDeclarationsExportForms(target=es5).js`** -> AI Confidence: **99.31%**
7. **`src/compiler/factory/nodeFactory.ts`** -> AI Confidence: **99.31%**
8. **`src/compiler/moduleNameResolver.ts`** -> AI Confidence: **99.31%**
9. **`src/compiler/parser.ts`** -> AI Confidence: **99.31%**
10. **`src/compiler/program.ts`** -> AI Confidence: **99.31%**
11. **`src/compiler/sys.ts`** -> AI Confidence: **99.31%**
12. **`src/compiler/transformers/module/system.ts`** -> AI Confidence: **99.31%**
13. **`src/harness/compilerImpl.ts`** -> AI Confidence: **99.31%**
14. **`src/harness/fakesHosts.ts`** -> AI Confidence: **99.31%**
15. **`src/harness/fourslashImpl.ts`** -> AI Confidence: **99.31%**
16. **`src/harness/harnessIO.ts`** -> AI Confidence: **99.31%**
17. **`src/services/codefixes/convertToEsModule.ts`** -> AI Confidence: **99.31%**
18. **`src/services/completions.ts`** -> AI Confidence: **99.31%**
19. **`src/services/findAllReferences.ts`** -> AI Confidence: **99.31%**
20. **`src/services/importTracker.ts`** -> AI Confidence: **99.31%**
21. **`src/services/refactors/convertImport.ts`** -> AI Confidence: **99.31%**
22. **`src/services/services.ts`** -> AI Confidence: **99.31%**
23. **`src/testRunner/projectsRunner.ts`** -> AI Confidence: **99.31%**
24. **`src/testRunner/unittests/helpers/tsserver.ts`** -> AI Confidence: **99.31%**
25. **`src/testRunner/unittests/helpers/virtualFileSystemWithWatch.ts`** -> AI Confidence: **99.31%**
26. **`src/tsserver/nodeServer.ts`** -> AI Confidence: **99.31%**
27. **`.gulp.js`** -> AI Confidence: **99.29%**
28. **`tests/baselines/reference/ES5For-of12(target=es2015).js`** -> AI Confidence: **99.29%**
29. **`tests/baselines/reference/ES5For-of29(target=es2015).js`** -> AI Confidence: **99.29%**
30. **`tests/baselines/reference/ES5For-of35(target=es2015).js`** -> AI Confidence: **99.29%**
31. **`tests/baselines/reference/ES5For-of37(target=es2015).js`** -> AI Confidence: **99.29%**
32. **`tests/baselines/reference/ES5For-ofTypeCheck12(target=es2015).js`** -> AI Confidence: **99.29%**
33. **`tests/baselines/reference/ES5For-ofTypeCheck13(target=es2015).js`** -> AI Confidence: **99.29%**
34. **`tests/baselines/reference/ambientWithStatements(alwaysstrict=false).js`** -> AI Confidence: **99.29%**
35. **`tests/baselines/reference/ambientWithStatements(alwaysstrict=true).js`** -> AI Confidence: **99.29%**
36. **`tests/baselines/reference/arrayIterationLibES5TargetDifferent(nolib=false,target=es2015).js`** -> AI Confidence: **99.29%**
37. **`tests/baselines/reference/arrayIterationLibES5TargetDifferent(nolib=false,target=esnext).js`** -> AI Confidence: **99.29%**
38. **`tests/baselines/reference/arrayIterationLibES5TargetDifferent(nolib=true,target=es2015).js`** -> AI Confidence: **99.29%**
39. **`tests/baselines/reference/arrayIterationLibES5TargetDifferent(nolib=true,target=esnext).js`** -> AI Confidence: **99.29%**
40. **`tests/baselines/reference/asiBreak.js`** -> AI Confidence: **99.29%**
41. **`tests/baselines/reference/asiContinue.js`** -> AI Confidence: **99.29%**
42. **`tests/baselines/reference/assertionFunctionsCanNarrowByDiscriminant.js`** -> AI Confidence: **99.29%**
43. **`tests/baselines/reference/assignmentCompatFunctionsWithOptionalArgs.js`** -> AI Confidence: **99.29%**
44. **`tests/baselines/reference/binaryArithmeticControlFlowGraphNotTooLarge.js`** -> AI Confidence: **99.29%**
45. **`tests/baselines/reference/blockScopedFunctionDeclarationES5(target=es2015).js`** -> AI Confidence: **99.29%**
46. **`tests/baselines/reference/blockScopedFunctionDeclarationES5(target=es5).js`** -> AI Confidence: **99.29%**
47. **`tests/baselines/reference/blockScopedFunctionDeclarationES6.js`** -> AI Confidence: **99.29%**
48. **`tests/baselines/reference/blockScopedFunctionDeclarationStrictES5(target=es2015).js`** -> AI Confidence: **99.29%**
49. **`tests/baselines/reference/blockScopedFunctionDeclarationStrictES5(target=es5).js`** -> AI Confidence: **99.29%**
50. **`tests/baselines/reference/blockScopedFunctionDeclarationStrictES6.js`** -> AI Confidence: **99.29%**
51. **`tests/baselines/reference/blockScopedSameNameFunctionDeclarationES5(target=es2015).js`** -> AI Confidence: **99.29%**
52. **`tests/baselines/reference/blockScopedSameNameFunctionDeclarationES5(target=es5).js`** -> AI Confidence: **99.29%**
53. **`tests/baselines/reference/blockScopedSameNameFunctionDeclarationES6.js`** -> AI Confidence: **99.29%**
54. **`tests/baselines/reference/blockScopedSameNameFunctionDeclarationStrictES5(target=es2015).js`** -> AI Confidence: **99.29%**
55. **`tests/baselines/reference/blockScopedSameNameFunctionDeclarationStrictES5(target=es5).js`** -> AI Confidence: **99.29%**
56. **`tests/baselines/reference/blockScopedSameNameFunctionDeclarationStrictES6.js`** -> AI Confidence: **99.29%**
57. **`tests/baselines/reference/breakInIterationOrSwitchStatement1.js`** -> AI Confidence: **99.29%**
58. **`tests/baselines/reference/breakInIterationOrSwitchStatement2.js`** -> AI Confidence: **99.29%**
59. **`tests/baselines/reference/breakInIterationOrSwitchStatement3.js`** -> AI Confidence: **99.29%**
60. **`tests/baselines/reference/breakNotInIterationOrSwitchStatement1.js`** -> AI Confidence: **99.29%**
61. **`tests/baselines/reference/breakNotInIterationOrSwitchStatement2.js`** -> AI Confidence: **99.29%**
62. **`tests/baselines/reference/breakTarget1.js`** -> AI Confidence: **99.29%**
63. **`tests/baselines/reference/breakTarget2.js`** -> AI Confidence: **99.29%**
64. **`tests/baselines/reference/breakTarget3.js`** -> AI Confidence: **99.29%**
65. **`tests/baselines/reference/breakTarget4.js`** -> AI Confidence: **99.29%**
66. **`tests/baselines/reference/breakTarget5.js`** -> AI Confidence: **99.29%**
67. **`tests/baselines/reference/breakTarget6.js`** -> AI Confidence: **99.29%**
68. **`tests/baselines/reference/callChain.3.js`** -> AI Confidence: **99.29%**
69. **`tests/baselines/reference/callChain.js`** -> AI Confidence: **99.29%**
70. **`tests/baselines/reference/callChainInference.js`** -> AI Confidence: **99.29%**
71. **`tests/baselines/reference/callWithSpread5.js`** -> AI Confidence: **99.29%**
72. **`tests/baselines/reference/capturedLetConstInLoop7.js`** -> AI Confidence: **99.29%**
73. **`tests/baselines/reference/capturedLetConstInLoop7_ES6.js`** -> AI Confidence: **99.29%**
74. **`tests/baselines/reference/capturedLetConstInLoop8.js`** -> AI Confidence: **99.29%**
75. **`tests/baselines/reference/capturedLetConstInLoop8_ES6.js`** -> AI Confidence: **99.29%**
76. **`tests/baselines/reference/catch.js`** -> AI Confidence: **99.29%**
77. **`tests/baselines/reference/catchClauseWithInitializer1.js`** -> AI Confidence: **99.29%**
78. **`tests/baselines/reference/catchClauseWithTypeAnnotation.js`** -> AI Confidence: **99.29%**
79. **`tests/baselines/reference/cf.js`** -> AI Confidence: **99.29%**
80. **`tests/baselines/reference/circularOptionalityRemoval.js`** -> AI Confidence: **99.29%**
81. **`tests/baselines/reference/classStaticBlock8.js`** -> AI Confidence: **99.29%**
82. **`tests/baselines/reference/commentLeadingCloseBrace.js`** -> AI Confidence: **99.29%**
83. **`tests/baselines/reference/commentOnIfStatement1.js`** -> AI Confidence: **99.29%**
84. **`tests/baselines/reference/conditionalEqualityOnLiteralObjects.js`** -> AI Confidence: **99.29%**
85. **`tests/baselines/reference/config/commandLineParsing/parseBuildOptions/errors on missing argument.js`** -> AI Confidence: **99.29%**
86. **`tests/baselines/reference/config/commandLineParsing/parseCommandLine/Handles did you mean for misspelt flags.js`** -> AI Confidence: **99.29%**
87. **`tests/baselines/reference/config/commandLineParsing/parseCommandLine/Parse empty options of --jsx.js`** -> AI Confidence: **99.29%**
88. **`tests/baselines/reference/config/commandLineParsing/parseCommandLine/Parse empty options of --module.js`** -> AI Confidence: **99.29%**
89. **`tests/baselines/reference/config/commandLineParsing/parseCommandLine/Parse empty options of --moduleResolution.js`** -> AI Confidence: **99.29%**
90. **`tests/baselines/reference/config/commandLineParsing/parseCommandLine/Parse empty options of --newLine.js`** -> AI Confidence: **99.29%**
91. **`tests/baselines/reference/config/commandLineParsing/parseCommandLine/Parse empty options of --target.js`** -> AI Confidence: **99.29%**
92. **`tests/baselines/reference/config/commandLineParsing/parseCommandLine/errors on missing argument to --fallbackPolling.js`** -> AI Confidence: **99.29%**
93. **`tests/baselines/reference/config/convertCompilerOptionsFromJson/Convert incorrect option of jsx to compiler-options with json api.js`** -> AI Confidence: **99.29%**
94. **`tests/baselines/reference/config/convertCompilerOptionsFromJson/Convert incorrect option of jsx to compiler-options with jsonSourceFile api.js`** -> AI Confidence: **99.29%**
95. **`tests/baselines/reference/config/convertCompilerOptionsFromJson/Convert incorrect option of module to compiler-options with json api.js`** -> AI Confidence: **99.29%**
96. **`tests/baselines/reference/config/convertCompilerOptionsFromJson/Convert incorrect option of module to compiler-options with jsonSourceFile api.js`** -> AI Confidence: **99.29%**
97. **`tests/baselines/reference/config/convertCompilerOptionsFromJson/Convert incorrect option of module-resolution to compiler-options with json api.js`** -> AI Confidence: **99.29%**
98. **`tests/baselines/reference/config/convertCompilerOptionsFromJson/Convert incorrect option of module-resolution to compiler-options with jsonSourceFile api.js`** -> AI Confidence: **99.29%**
99. **`tests/baselines/reference/config/convertCompilerOptionsFromJson/Convert incorrect option of newLine to compiler-options with json api.js`** -> AI Confidence: **99.29%**
100. **`tests/baselines/reference/config/convertCompilerOptionsFromJson/Convert incorrect option of newLine to compiler-options with jsonSourceFile api.js`** -> AI Confidence: **99.29%**
101. **`tests/baselines/reference/config/convertCompilerOptionsFromJson/Convert incorrect option of target to compiler-options with json api.js`** -> AI Confidence: **99.29%**
102. **`tests/baselines/reference/config/convertCompilerOptionsFromJson/Convert incorrect option of target to compiler-options with jsonSourceFile api.js`** -> AI Confidence: **99.29%**
103. **`tests/baselines/reference/config/convertCompilerOptionsFromJson/Convert tsconfig options when there are multiple invalid strings with jsonSourceFile api.js`** -> AI Confidence: **99.29%**
104. **`tests/baselines/reference/config/matchFiles/and exclusions with json api.js`** -> AI Confidence: **99.29%**
105. **`tests/baselines/reference/config/matchFiles/and exclusions with jsonSourceFile api.js`** -> AI Confidence: **99.29%**
106. **`tests/baselines/reference/config/matchFiles/question matches only a single character with json api.js`** -> AI Confidence: **99.29%**
107. **`tests/baselines/reference/config/matchFiles/question matches only a single character with jsonSourceFile api.js`** -> AI Confidence: **99.29%**
108. **`tests/baselines/reference/config/matchFiles/with wildcard excludes with json api.js`** -> AI Confidence: **99.29%**
109. **`tests/baselines/reference/config/matchFiles/with wildcard excludes with jsonSourceFile api.js`** -> AI Confidence: **99.29%**
110. **`tests/baselines/reference/config/tsconfigParsing/returns error when tsconfig have excludes with json api.js`** -> AI Confidence: **99.29%**
111. **`tests/baselines/reference/config/tsconfigParsing/returns error when tsconfig have excludes with jsonSourceFile api.js`** -> AI Confidence: **99.29%**
112. **`tests/baselines/reference/constDeclarations-errors.js`** -> AI Confidence: **99.29%**
113. **`tests/baselines/reference/constDeclarations.js`** -> AI Confidence: **99.29%**
114. **`tests/baselines/reference/constEnum4.js`** -> AI Confidence: **99.29%**
115. **`tests/baselines/reference/constEnums.js`** -> AI Confidence: **99.29%**
116. **`tests/baselines/reference/contextualTypeLogicalOr.js`** -> AI Confidence: **99.29%**
117. **`tests/baselines/reference/continueInIterationStatement1.js`** -> AI Confidence: **99.29%**
118. **`tests/baselines/reference/continueInIterationStatement2.js`** -> AI Confidence: **99.29%**
119. **`tests/baselines/reference/continueInIterationStatement3.js`** -> AI Confidence: **99.29%**
120. **`tests/baselines/reference/continueNotInIterationStatement1.js`** -> AI Confidence: **99.29%**
121. **`tests/baselines/reference/continueNotInIterationStatement2.js`** -> AI Confidence: **99.29%**
122. **`tests/baselines/reference/continueNotInIterationStatement3.js`** -> AI Confidence: **99.29%**
123. **`tests/baselines/reference/continueStatementInternalComments.js`** -> AI Confidence: **99.29%**
124. **`tests/baselines/reference/continueTarget1.js`** -> AI Confidence: **99.29%**
125. **`tests/baselines/reference/continueTarget2.js`** -> AI Confidence: **99.29%**
126. **`tests/baselines/reference/continueTarget3.js`** -> AI Confidence: **99.29%**
127. **`tests/baselines/reference/continueTarget4.js`** -> AI Confidence: **99.29%**
128. **`tests/baselines/reference/continueTarget5.js`** -> AI Confidence: **99.29%**
129. **`tests/baselines/reference/continueTarget6.js`** -> AI Confidence: **99.29%**
130. **`tests/baselines/reference/controlFlowAliasingCatchVariables(useunknownincatchvariables=false).js`** -> AI Confidence: **99.29%**
131. **`tests/baselines/reference/controlFlowAliasingCatchVariables(useunknownincatchvariables=true).js`** -> AI Confidence: **99.29%**
132. **`tests/baselines/reference/controlFlowAnalysisOnBareThisKeyword.js`** -> AI Confidence: **99.29%**
133. **`tests/baselines/reference/controlFlowBreakContinueWithLabel.js`** -> AI Confidence: **99.29%**
134. **`tests/baselines/reference/controlFlowElementAccess2.js`** -> AI Confidence: **99.29%**
135. **`tests/baselines/reference/controlFlowForInStatement2.js`** -> AI Confidence: **99.29%**
136. **`tests/baselines/reference/controlFlowInitializedDestructuringVariables.js`** -> AI Confidence: **99.29%**
137. **`tests/baselines/reference/controlFlowInstanceOfGuardPrimitives.js`** -> AI Confidence: **99.29%**
138. **`tests/baselines/reference/controlFlowManyCallExpressionStatementsPerf.js`** -> AI Confidence: **99.29%**
139. **`tests/baselines/reference/controlFlowManyConsecutiveConditionsNoTimeout.js`** -> AI Confidence: **99.29%**
140. **`tests/baselines/reference/controlFlowNullTypeAndLiteral.js`** -> AI Confidence: **99.29%**
141. **`tests/baselines/reference/controlFlowOptionalChain.js`** -> AI Confidence: **99.29%**
142. **`tests/baselines/reference/controlFlowOptionalChain2.js`** -> AI Confidence: **99.29%**
143. **`tests/baselines/reference/controlFlowStringIndex.js`** -> AI Confidence: **99.29%**
144. **`tests/baselines/reference/controlFlowWithTemplateLiterals.js`** -> AI Confidence: **99.29%**
145. **`tests/baselines/reference/declFileForInterfaceWithOptionalFunction.js`** -> AI Confidence: **99.29%**
146. **`tests/baselines/reference/declFileOptionalInterfaceMethod.js`** -> AI Confidence: **99.29%**
147. **`tests/baselines/reference/declarationEmitDestructuring2.js`** -> AI Confidence: **99.29%**
148. **`tests/baselines/reference/declarationEmitDestructuring3.js`** -> AI Confidence: **99.29%**
149. **`tests/baselines/reference/declarationEmitDestructuring4.js`** -> AI Confidence: **99.29%**
150. **`tests/baselines/reference/declarationEmitDestructuring5.js`** -> AI Confidence: **99.29%**
151. **`tests/baselines/reference/declarationEmitDestructuringOptionalBindingParametersInOverloads.js`** -> AI Confidence: **99.29%**
152. **`tests/baselines/reference/declarationEmitDestructuringWithOptionalBindingParameters.js`** -> AI Confidence: **99.29%**
153. **`tests/baselines/reference/defaultKeywordWithoutExport2.js`** -> AI Confidence: **99.29%**
154. **`tests/baselines/reference/definiteAssignmentAssertionsWithObjectShortHand.js`** -> AI Confidence: **99.29%**
155. **`tests/baselines/reference/destructureCatchClause(strict=false,useunknownincatchvariables=false).js`** -> AI Confidence: **99.29%**
156. **`tests/baselines/reference/destructureCatchClause(strict=false,useunknownincatchvariables=true).js`** -> AI Confidence: **99.29%**
157. **`tests/baselines/reference/destructureCatchClause(strict=true,useunknownincatchvariables=false).js`** -> AI Confidence: **99.29%**
158. **`tests/baselines/reference/destructureCatchClause(strict=true,useunknownincatchvariables=true).js`** -> AI Confidence: **99.29%**
159. **`tests/baselines/reference/destructureOptionalParameter.js`** -> AI Confidence: **99.29%**
160. **`tests/baselines/reference/destructuringArrayBindingPatternAndAssignment5SiblingInitializer.js`** -> AI Confidence: **99.29%**
161. **`tests/baselines/reference/destructuringCatch.js`** -> AI Confidence: **99.29%**
162. **`tests/baselines/reference/destructuringObjectBindingPatternAndAssignment9SiblingInitializer.js`** -> AI Confidence: **99.29%**
163. **`tests/baselines/reference/destructuringParameterDeclaration2.js`** -> AI Confidence: **99.29%**
164. **`tests/baselines/reference/destructuringParameterDeclaration6.js`** -> AI Confidence: **99.29%**
165. **`tests/baselines/reference/destructuringParameterDeclaration8.js`** -> AI Confidence: **99.29%**
166. **`tests/baselines/reference/destructuringTypeGuardFlow.js`** -> AI Confidence: **99.29%**
167. **`tests/baselines/reference/discriminableUnionWithIntersectedMembers.js`** -> AI Confidence: **99.29%**
168. **`tests/baselines/reference/discriminantNarrowingCouldBeCircular.js`** -> AI Confidence: **99.29%**
169. **`tests/baselines/reference/discriminantOrderIndependence.js`** -> AI Confidence: **99.29%**
170. **`tests/baselines/reference/discriminantPropertyCheck.js`** -> AI Confidence: **99.29%**
171. **`tests/baselines/reference/discriminantsAndNullOrUndefined.js`** -> AI Confidence: **99.29%**
172. **`tests/baselines/reference/discriminantsAndPrimitives.js`** -> AI Confidence: **99.29%**
173. **`tests/baselines/reference/discriminatedUnionTypes2.js`** -> AI Confidence: **99.29%**
174. **`tests/baselines/reference/discriminatedUnionTypes3.js`** -> AI Confidence: **99.29%**
175. **`tests/baselines/reference/doWhileBreakStatements.js`** -> AI Confidence: **99.29%**
176. **`tests/baselines/reference/doWhileContinueStatements.js`** -> AI Confidence: **99.29%**
177. **`tests/baselines/reference/doYouNeedToChangeYourTargetLibraryES2016Plus.js`** -> AI Confidence: **99.29%**
178. **`tests/baselines/reference/doubleUnderscoreLabels.js`** -> AI Confidence: **99.29%**
179. **`tests/baselines/reference/duplicateLabel1.js`** -> AI Confidence: **99.29%**
180. **`tests/baselines/reference/duplicateLabel2.js`** -> AI Confidence: **99.29%**
181. **`tests/baselines/reference/duplicateLabel3.js`** -> AI Confidence: **99.29%**
182. **`tests/baselines/reference/duplicateLabel4.js`** -> AI Confidence: **99.29%**
183. **`tests/baselines/reference/elementAccessChain.2.js`** -> AI Confidence: **99.29%**
184. **`tests/baselines/reference/elementAccessChain.3.js`** -> AI Confidence: **99.29%**
185. **`tests/baselines/reference/elementAccessChain.js`** -> AI Confidence: **99.29%**
186. **`tests/baselines/reference/elidedEmbeddedStatementsReplacedWithSemicolon.js`** -> AI Confidence: **99.29%**
187. **`tests/baselines/reference/emitter.noCatchBinding.es2019.js`** -> AI Confidence: **99.29%**
188. **`tests/baselines/reference/enumNumbering1.js`** -> AI Confidence: **99.29%**
189. **`tests/baselines/reference/equalityStrictNulls.js`** -> AI Confidence: **99.29%**
190. **`tests/baselines/reference/equalityWithEnumTypes.js`** -> AI Confidence: **99.29%**
191. **`tests/baselines/reference/equalityWithtNullishCoalescingAssignment(strict=false).js`** -> AI Confidence: **99.29%**
192. **`tests/baselines/reference/equalityWithtNullishCoalescingAssignment(strict=true).js`** -> AI Confidence: **99.29%**
193. **`tests/baselines/reference/errorOnEnumReferenceInCondition.js`** -> AI Confidence: **99.29%**
194. **`tests/baselines/reference/es2016IntlAPIs.js`** -> AI Confidence: **99.29%**
195. **`tests/baselines/reference/es2018ObjectAssign.js`** -> AI Confidence: **99.29%**
196. **`tests/baselines/reference/es5-asyncFunctionSwitchStatements(target=es2015).js`** -> AI Confidence: **99.29%**
197. **`tests/baselines/reference/exhaustiveSwitchCheckCircularity.js`** -> AI Confidence: **99.29%**
198. **`tests/baselines/reference/expr.js`** -> AI Confidence: **99.29%**
199. **`tests/baselines/reference/expressionWithJSDocTypeArguments.js`** -> AI Confidence: **99.29%**
200. **`tests/baselines/reference/extractConstant/extractConstant_CaseClauseExpression.js`** -> AI Confidence: **99.29%**
201. **`tests/baselines/reference/extractConstant/extractConstant_PropertyName_Keyword.js`** -> AI Confidence: **99.29%**
202. **`tests/baselines/reference/extractConstant/extractConstant_PropertyName_PrivateIdentifierKeyword.js`** -> AI Confidence: **99.29%**
203. **`tests/baselines/reference/fallFromLastCase1.js`** -> AI Confidence: **99.29%**
204. **`tests/baselines/reference/fallFromLastCase2.js`** -> AI Confidence: **99.29%**
205. **`tests/baselines/reference/firstMatchRegExpMatchArray.js`** -> AI Confidence: **99.29%**
206. **`tests/baselines/reference/for-of-excess-declarations.js`** -> AI Confidence: **99.29%**
207. **`tests/baselines/reference/for-of2.js`** -> AI Confidence: **99.29%**
208. **`tests/baselines/reference/for-of58.js`** -> AI Confidence: **99.29%**
209. **`tests/baselines/reference/forBreakStatements.js`** -> AI Confidence: **99.29%**
210. **`tests/baselines/reference/forContinueStatements.js`** -> AI Confidence: **99.29%**
211. **`tests/baselines/reference/forInStrictNullChecksNoError.js`** -> AI Confidence: **99.29%**
212. **`tests/baselines/reference/functionCall11.js`** -> AI Confidence: **99.29%**
213. **`tests/baselines/reference/functionCall12.js`** -> AI Confidence: **99.29%**
214. **`tests/baselines/reference/functionCall14.js`** -> AI Confidence: **99.29%**
215. **`tests/baselines/reference/functionCall15.js`** -> AI Confidence: **99.29%**
216. **`tests/baselines/reference/functionCall16.js`** -> AI Confidence: **99.29%**
217. **`tests/baselines/reference/functionCall17.js`** -> AI Confidence: **99.29%**
218. **`tests/baselines/reference/functionCall8.js`** -> AI Confidence: **99.29%**
219. **`tests/baselines/reference/functionCall9.js`** -> AI Confidence: **99.29%**
220. **`tests/baselines/reference/functionOverloadErrorsSyntax.js`** -> AI Confidence: **99.29%**
221. **`tests/baselines/reference/generatorES6_5.js`** -> AI Confidence: **99.29%**
222. **`tests/baselines/reference/generatorImplicitAny.js`** -> AI Confidence: **99.29%**
223. **`tests/baselines/reference/homomorphicMappedTypeIntersectionAssignability.js`** -> AI Confidence: **99.29%**
224. **`tests/baselines/reference/identicalTypesNoDifferByCheckOrder.js`** -> AI Confidence: **99.29%**
225. **`tests/baselines/reference/ifDoWhileStatements.js`** -> AI Confidence: **99.29%**
226. **`tests/baselines/reference/ifStatementInternalComments.js`** -> AI Confidence: **99.29%**
227. **`tests/baselines/reference/inKeywordTypeguard(strict=false).js`** -> AI Confidence: **99.29%**
228. **`tests/baselines/reference/inKeywordTypeguard(strict=true).js`** -> AI Confidence: **99.29%**
229. **`tests/baselines/reference/initializedDestructuringAssignmentTypes.js`** -> AI Confidence: **99.29%**
230. **`tests/baselines/reference/instanceofOperatorWithRHSHasSymbolHasInstance.js`** -> AI Confidence: **99.29%**
231. **`tests/baselines/reference/instanceofWithPrimitiveUnion.js`** -> AI Confidence: **99.29%**
232. **`tests/baselines/reference/interfaceWithOptionalProperty.js`** -> AI Confidence: **99.29%**
233. **`tests/baselines/reference/intersectionAsWeakTypeSource.js`** -> AI Confidence: **99.29%**
234. **`tests/baselines/reference/intersectionNarrowing.js`** -> AI Confidence: **99.29%**
235. **`tests/baselines/reference/intersectionOfUnionNarrowing.js`** -> AI Confidence: **99.29%**
236. **`tests/baselines/reference/invalidDoWhileBreakStatements.js`** -> AI Confidence: **99.29%**
237. **`tests/baselines/reference/invalidDoWhileContinueStatements.js`** -> AI Confidence: **99.29%**
238. **`tests/baselines/reference/invalidSwitchBreakStatement.js`** -> AI Confidence: **99.29%**
239. **`tests/baselines/reference/invalidSwitchContinueStatement.js`** -> AI Confidence: **99.29%**
240. **`tests/baselines/reference/invalidTryStatements.js`** -> AI Confidence: **99.29%**
241. **`tests/baselines/reference/iteratorsAndStrictNullChecks.js`** -> AI Confidence: **99.29%**
242. **`tests/baselines/reference/jsDeclarationsJson(target=es2015).js`** -> AI Confidence: **99.29%**
243. **`tests/baselines/reference/jsDeclarationsOptionalTypeLiteralProps2.js`** -> AI Confidence: **99.29%**
244. **`tests/baselines/reference/jsdocCatchClauseWithTypeAnnotation.js`** -> AI Confidence: **99.29%**
245. **`tests/baselines/reference/jsxNestedWithinTernaryParsesCorrectly.js`** -> AI Confidence: **99.29%**
246. **`tests/baselines/reference/literalTypes1.js`** -> AI Confidence: **99.29%**
247. **`tests/baselines/reference/literalTypes3.js`** -> AI Confidence: **99.29%**
248. **`tests/baselines/reference/logicalAndOperatorStrictMode.js`** -> AI Confidence: **99.29%**
249. **`tests/baselines/reference/logicalAssignment2(target=es2015).js`** -> AI Confidence: **99.29%**
250. **`tests/baselines/reference/logicalAssignment2(target=es2020).js`** -> AI Confidence: **99.29%**
251. **`tests/baselines/reference/logicalAssignment2(target=es2021).js`** -> AI Confidence: **99.29%**
252. **`tests/baselines/reference/logicalAssignment2(target=esnext).js`** -> AI Confidence: **99.29%**
253. **`tests/baselines/reference/logicalAssignment3(target=es2015).js`** -> AI Confidence: **99.29%**
254. **`tests/baselines/reference/logicalAssignment3(target=es2020).js`** -> AI Confidence: **99.29%**
255. **`tests/baselines/reference/logicalAssignment3(target=es2021).js`** -> AI Confidence: **99.29%**
256. **`tests/baselines/reference/logicalAssignment3(target=esnext).js`** -> AI Confidence: **99.29%**
257. **`tests/baselines/reference/logicalAssignment4(target=es2015).js`** -> AI Confidence: **99.29%**
258. **`tests/baselines/reference/logicalAssignment4(target=es2020).js`** -> AI Confidence: **99.29%**
259. **`tests/baselines/reference/logicalAssignment4(target=es2021).js`** -> AI Confidence: **99.29%**
260. **`tests/baselines/reference/logicalAssignment4(target=esnext).js`** -> AI Confidence: **99.29%**
261. **`tests/baselines/reference/logicalAssignment6(target=es2015).js`** -> AI Confidence: **99.29%**
262. **`tests/baselines/reference/logicalAssignment6(target=es2020).js`** -> AI Confidence: **99.29%**
263. **`tests/baselines/reference/logicalAssignment6(target=es2021).js`** -> AI Confidence: **99.29%**
264. **`tests/baselines/reference/logicalAssignment6(target=esnext).js`** -> AI Confidence: **99.29%**
265. **`tests/baselines/reference/logicalAssignment7(target=es2015).js`** -> AI Confidence: **99.29%**
266. **`tests/baselines/reference/logicalAssignment7(target=es2020).js`** -> AI Confidence: **99.29%**
267. **`tests/baselines/reference/logicalAssignment7(target=es2021).js`** -> AI Confidence: **99.29%**
268. **`tests/baselines/reference/logicalAssignment7(target=esnext).js`** -> AI Confidence: **99.29%**
269. **`tests/baselines/reference/logicalAssignment8(target=es2015).js`** -> AI Confidence: **99.29%**
270. **`tests/baselines/reference/logicalAssignment8(target=es2020).js`** -> AI Confidence: **99.29%**
271. **`tests/baselines/reference/logicalAssignment8(target=es2021).js`** -> AI Confidence: **99.29%**
272. **`tests/baselines/reference/logicalAssignment8(target=esnext).js`** -> AI Confidence: **99.29%**
273. **`tests/baselines/reference/missingCloseParenStatements(alwaysstrict=false).js`** -> AI Confidence: **99.29%**
274. **`tests/baselines/reference/missingCloseParenStatements(alwaysstrict=true).js`** -> AI Confidence: **99.29%**
275. **`tests/baselines/reference/modularizeLibrary_Dom.iterable.js`** -> AI Confidence: **99.29%**
276. **`tests/baselines/reference/modularizeLibrary_Worker.iterable.js`** -> AI Confidence: **99.29%**
277. **`tests/baselines/reference/nanEquality.js`** -> AI Confidence: **99.29%**
278. **`tests/baselines/reference/narrowExceptionVariableInCatchClause.js`** -> AI Confidence: **99.29%**
279. **`tests/baselines/reference/narrowFromAnyWithInstanceof.js`** -> AI Confidence: **99.29%**
280. **`tests/baselines/reference/narrowFromAnyWithTypePredicate.js`** -> AI Confidence: **99.29%**
281. **`tests/baselines/reference/narrowUnknownByTypeofObject.js`** -> AI Confidence: **99.29%**
282. **`tests/baselines/reference/narrowingByDiscriminantInLoop.js`** -> AI Confidence: **99.29%**
283. **`tests/baselines/reference/narrowingMutualSubtypes.js`** -> AI Confidence: **99.29%**
284. **`tests/baselines/reference/narrowingOfQualifiedNames.js`** -> AI Confidence: **99.29%**
285. **`tests/baselines/reference/narrowingOrderIndependent.js`** -> AI Confidence: **99.29%**
286. **`tests/baselines/reference/narrowingTruthyObject.js`** -> AI Confidence: **99.29%**
287. **`tests/baselines/reference/narrowingTypeofFunction.js`** -> AI Confidence: **99.29%**
288. **`tests/baselines/reference/narrowingTypeofObject.js`** -> AI Confidence: **99.29%**
289. **`tests/baselines/reference/narrowingTypeofUndefined1.js`** -> AI Confidence: **99.29%**
290. **`tests/baselines/reference/narrowingTypeofUndefined2.js`** -> AI Confidence: **99.29%**
291. **`tests/baselines/reference/narrowingUnionToNeverAssigment.js`** -> AI Confidence: **99.29%**
292. **`tests/baselines/reference/narrowingUnionWithBang.js`** -> AI Confidence: **99.29%**
293. **`tests/baselines/reference/narrowingWithNonNullExpression.js`** -> AI Confidence: **99.29%**
294. **`tests/baselines/reference/nestedIfStatement.js`** -> AI Confidence: **99.29%**
295. **`tests/baselines/reference/neverNullishThroughParentheses.js`** -> AI Confidence: **99.29%**
296. **`tests/baselines/reference/newTargetNarrowing.js`** -> AI Confidence: **99.29%**
297. **`tests/baselines/reference/noCatchBlock.js`** -> AI Confidence: **99.29%**
298. **`tests/baselines/reference/noImplicitReturnsWithProtectedBlocks2.js`** -> AI Confidence: **99.29%**
299. **`tests/baselines/reference/noPropertyAccessFromIndexSignature1.js`** -> AI Confidence: **99.29%**
300. **`tests/baselines/reference/noUnusedLocals_selfReference_skipsBlockLocations.js`** -> AI Confidence: **99.29%**
301. **`tests/baselines/reference/nonNullReferenceMatching.js`** -> AI Confidence: **99.29%**
302. **`tests/baselines/reference/nonObjectUnionNestedExcessPropertyCheck.js`** -> AI Confidence: **99.29%**
303. **`tests/baselines/reference/normalizedIntersectionTooComplex.js`** -> AI Confidence: **99.29%**
304. **`tests/baselines/reference/nullishCoalescingOperator1.js`** -> AI Confidence: **99.29%**
305. **`tests/baselines/reference/nullishCoalescingOperator12.js`** -> AI Confidence: **99.29%**
306. **`tests/baselines/reference/nullishCoalescingOperator2.js`** -> AI Confidence: **99.29%**
307. **`tests/baselines/reference/nullishCoalescingOperator3.js`** -> AI Confidence: **99.29%**
308. **`tests/baselines/reference/nullishCoalescingOperator4.js`** -> AI Confidence: **99.29%**
309. **`tests/baselines/reference/nullishCoalescingOperator5.js`** -> AI Confidence: **99.29%**
310. **`tests/baselines/reference/nullishCoalescingOperator6.js`** -> AI Confidence: **99.29%**
311. **`tests/baselines/reference/nullishCoalescingOperator7.js`** -> AI Confidence: **99.29%**
312. **`tests/baselines/reference/nullishCoalescingOperator8.js`** -> AI Confidence: **99.29%**
313. **`tests/baselines/reference/nullishCoalescingOperator_es2020.js`** -> AI Confidence: **99.29%**
314. **`tests/baselines/reference/nullishCoalescingOperator_not_strict.js`** -> AI Confidence: **99.29%**
315. **`tests/baselines/reference/objectLiteralPropertyImplicitlyAny.js`** -> AI Confidence: **99.29%**
316. **`tests/baselines/reference/objectSpreadRepeatedComplexity.js`** -> AI Confidence: **99.29%**
317. **`tests/baselines/reference/omitTypeHelperModifiers01.js`** -> AI Confidence: **99.29%**
318. **`tests/baselines/reference/omittedExpressionForOfLoop.js`** -> AI Confidence: **99.29%**
319. **`tests/baselines/reference/optionalBindingParameters1.js`** -> AI Confidence: **99.29%**
320. **`tests/baselines/reference/optionalBindingParameters2.js`** -> AI Confidence: **99.29%**
321. **`tests/baselines/reference/optionalBindingParametersInOverloads1.js`** -> AI Confidence: **99.29%**
322. **`tests/baselines/reference/optionalBindingParametersInOverloads2.js`** -> AI Confidence: **99.29%**
323. **`tests/baselines/reference/optionalChainWithInstantiationExpression2(target=es2019).js`** -> AI Confidence: **99.29%**
324. **`tests/baselines/reference/optionalChainWithInstantiationExpression2(target=es2020).js`** -> AI Confidence: **99.29%**
325. **`tests/baselines/reference/optionalChainingInTypeAssertions(target=es2015).js`** -> AI Confidence: **99.29%**
326. **`tests/baselines/reference/optionalChainingInTypeAssertions(target=esnext).js`** -> AI Confidence: **99.29%**
327. **`tests/baselines/reference/optionalChainingInference.js`** -> AI Confidence: **99.29%**
328. **`tests/baselines/reference/optionalParameterInDestructuringWithInitializer.js`** -> AI Confidence: **99.29%**
329. **`tests/baselines/reference/optionalProperties01.js`** -> AI Confidence: **99.29%**
330. **`tests/baselines/reference/optionalProperties02.js`** -> AI Confidence: **99.29%**
331. **`tests/baselines/reference/optionalPropertiesSyntax.js`** -> AI Confidence: **99.29%**
332. **`tests/baselines/reference/overloadingStaticFunctionsInFunctions.js`** -> AI Confidence: **99.29%**
333. **`tests/baselines/reference/overloadsAndTypeArgumentArity.js`** -> AI Confidence: **99.29%**
334. **`tests/baselines/reference/overloadsAndTypeArgumentArityErrors.js`** -> AI Confidence: **99.29%**
335. **`tests/baselines/reference/parentheses.js`** -> AI Confidence: **99.29%**
336. **`tests/baselines/reference/parser509693.js`** -> AI Confidence: **99.29%**
337. **`tests/baselines/reference/parserArrowFunctionExpression7.js`** -> AI Confidence: **99.29%**
338. **`tests/baselines/reference/parserCatchClauseWithTypeAnnotation1.js`** -> AI Confidence: **99.29%**
339. **`tests/baselines/reference/parserConditionalExpression1.js`** -> AI Confidence: **99.29%**
340. **`tests/baselines/reference/parserConstructorAmbiguity4.js`** -> AI Confidence: **99.29%**
341. **`tests/baselines/reference/parserDoStatement2.js`** -> AI Confidence: **99.29%**
342. **`tests/baselines/reference/parserES5ForOfStatement10(target=es2015).js`** -> AI Confidence: **99.29%**
343. **`tests/baselines/reference/parserES5ForOfStatement11(target=es2015).js`** -> AI Confidence: **99.29%**
344. **`tests/baselines/reference/parserES5ForOfStatement12(target=es2015).js`** -> AI Confidence: **99.29%**
345. **`tests/baselines/reference/parserErrorRecovery_SwitchStatement1.js`** -> AI Confidence: **99.29%**
346. **`tests/baselines/reference/parserForOfStatement10.js`** -> AI Confidence: **99.29%**
347. **`tests/baselines/reference/parserForOfStatement11.js`** -> AI Confidence: **99.29%**
348. **`tests/baselines/reference/parserForOfStatement12.js`** -> AI Confidence: **99.29%**
349. **`tests/baselines/reference/parserForStatement3.js`** -> AI Confidence: **99.29%**
350. **`tests/baselines/reference/parserForStatement4.js`** -> AI Confidence: **99.29%**
351. **`tests/baselines/reference/parserForStatement5.js`** -> AI Confidence: **99.29%**
352. **`tests/baselines/reference/parserForStatement6.js`** -> AI Confidence: **99.29%**
353. **`tests/baselines/reference/parserForStatement7.js`** -> AI Confidence: **99.29%**
354. **`tests/baselines/reference/parserForStatement8.js`** -> AI Confidence: **99.29%**
355. **`tests/baselines/reference/parserFuzz1.js`** -> AI Confidence: **99.29%**
356. **`tests/baselines/reference/parserGenericsInInterfaceDeclaration1.js`** -> AI Confidence: **99.29%**
357. **`tests/baselines/reference/parserIfStatement2.js`** -> AI Confidence: **99.29%**
358. **`tests/baselines/reference/parserIndexSignature3.js`** -> AI Confidence: **99.29%**
359. **`tests/baselines/reference/parserMethodSignature10.js`** -> AI Confidence: **99.29%**
360. **`tests/baselines/reference/parserMethodSignature12.js`** -> AI Confidence: **99.29%**
361. **`tests/baselines/reference/parserMethodSignature2.js`** -> AI Confidence: **99.29%**
362. **`tests/baselines/reference/parserMethodSignature4.js`** -> AI Confidence: **99.29%**
363. **`tests/baselines/reference/parserMethodSignature6.js`** -> AI Confidence: **99.29%**
364. **`tests/baselines/reference/parserMethodSignature8.js`** -> AI Confidence: **99.29%**
365. **`tests/baselines/reference/parserMissingToken1.js`** -> AI Confidence: **99.29%**
366. **`tests/baselines/reference/parserOptionalTypeMembers1.js`** -> AI Confidence: **99.29%**
367. **`tests/baselines/reference/parserPropertySignature10.js`** -> AI Confidence: **99.29%**
368. **`tests/baselines/reference/parserPropertySignature12.js`** -> AI Confidence: **99.29%**
369. **`tests/baselines/reference/parserPropertySignature2.js`** -> AI Confidence: **99.29%**
370. **`tests/baselines/reference/parserPropertySignature4.js`** -> AI Confidence: **99.29%**
371. **`tests/baselines/reference/parserPropertySignature6.js`** -> AI Confidence: **99.29%**
372. **`tests/baselines/reference/parserPropertySignature8.js`** -> AI Confidence: **99.29%**
373. **`tests/baselines/reference/parserPublicBreak1.js`** -> AI Confidence: **99.29%**
374. **`tests/baselines/reference/parserRealSource13.js`** -> AI Confidence: **99.29%**
375. **`tests/baselines/reference/parserRegularExpression1.js`** -> AI Confidence: **99.29%**
376. **`tests/baselines/reference/parserRegularExpression3.js`** -> AI Confidence: **99.29%**
377. **`tests/baselines/reference/parserRegularExpression4.js`** -> AI Confidence: **99.29%**
378. **`tests/baselines/reference/parserRegularExpression5.js`** -> AI Confidence: **99.29%**
379. **`tests/baselines/reference/parserRegularExpressionDivideAmbiguity3.js`** -> AI Confidence: **99.29%**
380. **`tests/baselines/reference/parserSbp_7.9_A9_T3.js`** -> AI Confidence: **99.29%**
381. **`tests/baselines/reference/parserStrictMode13.js`** -> AI Confidence: **99.29%**
382. **`tests/baselines/reference/parserTernaryAndCommaOperators1.js`** -> AI Confidence: **99.29%**
383. **`tests/baselines/reference/parserUnterminatedGeneric2.js`** -> AI Confidence: **99.29%**
384. **`tests/baselines/reference/parser_breakInIterationOrSwitchStatement1.js`** -> AI Confidence: **99.29%**
385. **`tests/baselines/reference/parser_breakInIterationOrSwitchStatement2.js`** -> AI Confidence: **99.29%**
386. **`tests/baselines/reference/parser_breakInIterationOrSwitchStatement3.js`** -> AI Confidence: **99.29%**
387. **`tests/baselines/reference/parser_breakNotInIterationOrSwitchStatement1.js`** -> AI Confidence: **99.29%**
388. **`tests/baselines/reference/parser_breakNotInIterationOrSwitchStatement2.js`** -> AI Confidence: **99.29%**
389. **`tests/baselines/reference/parser_breakTarget1.js`** -> AI Confidence: **99.29%**
390. **`tests/baselines/reference/parser_breakTarget2.js`** -> AI Confidence: **99.29%**
391. **`tests/baselines/reference/parser_breakTarget3.js`** -> AI Confidence: **99.29%**
392. **`tests/baselines/reference/parser_breakTarget4.js`** -> AI Confidence: **99.29%**
393. **`tests/baselines/reference/parser_breakTarget5.js`** -> AI Confidence: **99.29%**
394. **`tests/baselines/reference/parser_breakTarget6.js`** -> AI Confidence: **99.29%**
395. **`tests/baselines/reference/parser_continueInIterationStatement1.js`** -> AI Confidence: **99.29%**
396. **`tests/baselines/reference/parser_continueInIterationStatement2.js`** -> AI Confidence: **99.29%**
397. **`tests/baselines/reference/parser_continueInIterationStatement3.js`** -> AI Confidence: **99.29%**
398. **`tests/baselines/reference/parser_continueNotInIterationStatement1.js`** -> AI Confidence: **99.29%**
399. **`tests/baselines/reference/parser_continueNotInIterationStatement2.js`** -> AI Confidence: **99.29%**
400. **`tests/baselines/reference/parser_continueNotInIterationStatement3.js`** -> AI Confidence: **99.29%**
401. **`tests/baselines/reference/parser_continueTarget1.js`** -> AI Confidence: **99.29%**
402. **`tests/baselines/reference/parser_continueTarget2.js`** -> AI Confidence: **99.29%**
403. **`tests/baselines/reference/parser_continueTarget3.js`** -> AI Confidence: **99.29%**
404. **`tests/baselines/reference/parser_continueTarget4.js`** -> AI Confidence: **99.29%**
405. **`tests/baselines/reference/parser_continueTarget5.js`** -> AI Confidence: **99.29%**
406. **`tests/baselines/reference/parser_continueTarget6.js`** -> AI Confidence: **99.29%**
407. **`tests/baselines/reference/parser_duplicateLabel1.js`** -> AI Confidence: **99.29%**
408. **`tests/baselines/reference/parser_duplicateLabel2.js`** -> AI Confidence: **99.29%**
409. **`tests/baselines/reference/parser_duplicateLabel3.js`** -> AI Confidence: **99.29%**
410. **`tests/baselines/reference/parser_duplicateLabel4.js`** -> AI Confidence: **99.29%**
411. **`tests/baselines/reference/plainJSTypeErrors.js`** -> AI Confidence: **99.29%**
412. **`tests/baselines/reference/predicateSemantics.js`** -> AI Confidence: **99.29%**
413. **`tests/baselines/reference/prettyContextNotDebugAssertion.js`** -> AI Confidence: **99.29%**
414. **`tests/baselines/reference/printerApi/printsFileCorrectly.default.js`** -> AI Confidence: **99.29%**
415. **`tests/baselines/reference/printerApi/printsFileCorrectly.removeComments.js`** -> AI Confidence: **99.29%**
416. **`tests/baselines/reference/printerApi/printsNodeCorrectly.binaryAmpersandAmpersandExpressionWithLeftBinaryQuestionQuestionExpression.js`** -> AI Confidence: **99.29%**
417. **`tests/baselines/reference/printerApi/printsNodeCorrectly.binaryAmpersandAmpersandExpressionWithLeftConditionalExpression.js`** -> AI Confidence: **99.29%**
418. **`tests/baselines/reference/printerApi/printsNodeCorrectly.binaryAmpersandAmpersandExpressionWithRightBinaryQuestionQuestionExpression.js`** -> AI Confidence: **99.29%**
419. **`tests/baselines/reference/printerApi/printsNodeCorrectly.binaryBarBarExpressionWithLeftBinaryQuestionQuestionExpression.js`** -> AI Confidence: **99.29%**
420. **`tests/baselines/reference/printerApi/printsNodeCorrectly.binaryBarBarExpressionWithLeftConditionalExpression.js`** -> AI Confidence: **99.29%**
421. **`tests/baselines/reference/printerApi/printsNodeCorrectly.binaryBarBarExpressionWithRightBinaryQuestionQuestionExpression.js`** -> AI Confidence: **99.29%**
422. **`tests/baselines/reference/printerApi/printsNodeCorrectly.binaryCommaExpressionWithLeftBinaryQuestionQuestionExpression.js`** -> AI Confidence: **99.29%**
423. **`tests/baselines/reference/printerApi/printsNodeCorrectly.binaryCommaExpressionWithRightBinaryQuestionQuestionExpression.js`** -> AI Confidence: **99.29%**
424. **`tests/baselines/reference/printerApi/printsNodeCorrectly.binaryEqualsEqualsExpressionWithLeftBinaryQuestionQuestionExpression.js`** -> AI Confidence: **99.29%**
425. **`tests/baselines/reference/printerApi/printsNodeCorrectly.binaryEqualsEqualsExpressionWithRightBinaryQuestionQuestionExpression.js`** -> AI Confidence: **99.29%**
426. **`tests/baselines/reference/propertyAccessChain.2.js`** -> AI Confidence: **99.29%**
427. **`tests/baselines/reference/propertyAccessChain.3.js`** -> AI Confidence: **99.29%**
428. **`tests/baselines/reference/propertyAccessChain.js`** -> AI Confidence: **99.29%**
429. **`tests/baselines/reference/propertyAccessExpressionInnerComments.js`** -> AI Confidence: **99.29%**
430. **`tests/baselines/reference/reachabilityChecks2.js`** -> AI Confidence: **99.29%**
431. **`tests/baselines/reference/reachabilityChecks8.js`** -> AI Confidence: **99.29%**
432. **`tests/baselines/reference/recursiveArrayNotCircular.js`** -> AI Confidence: **99.29%**
433. **`tests/baselines/reference/recursiveExcessPropertyChecks.js`** -> AI Confidence: **99.29%**
434. **`tests/baselines/reference/redeclareParameterInCatchBlock.js`** -> AI Confidence: **99.29%**
435. **`tests/baselines/reference/regularExpressionAnnexB.js`** -> AI Confidence: **99.29%**
436. **`tests/baselines/reference/regularExpressionGroupNameSuggestions.js`** -> AI Confidence: **99.29%**
437. **`tests/baselines/reference/regularExpressionScanning(target=es2015).js`** -> AI Confidence: **99.29%**
438. **`tests/baselines/reference/regularExpressionScanning(target=es5).js`** -> AI Confidence: **99.29%**
439. **`tests/baselines/reference/regularExpressionScanning(target=esnext).js`** -> AI Confidence: **99.29%**
440. **`tests/baselines/reference/regularExpressionWithNonBMPFlags.js`** -> AI Confidence: **99.29%**
441. **`tests/baselines/reference/requiredInitializedParameter1.js`** -> AI Confidence: **99.29%**
442. **`tests/baselines/reference/restParamAsOptional.js`** -> AI Confidence: **99.29%**
443. **`tests/baselines/reference/restParameters.js`** -> AI Confidence: **99.29%**
444. **`tests/baselines/reference/restParamsWithNonRestParams.js`** -> AI Confidence: **99.29%**
445. **`tests/baselines/reference/scopingInCatchBlocks.js`** -> AI Confidence: **99.29%**
446. **`tests/baselines/reference/sourceMap-SkippedNode.js`** -> AI Confidence: **99.29%**
447. **`tests/baselines/reference/sourceMapValidationDestructuringForObjectBindingPattern2.js`** -> AI Confidence: **99.29%**
448. **`tests/baselines/reference/sourceMapValidationDestructuringForObjectBindingPatternDefaultValues2.js`** -> AI Confidence: **99.29%**
449. **`tests/baselines/reference/sourceMapValidationDestructuringForOfObjectBindingPattern2(target=es2015).js`** -> AI Confidence: **99.29%**
450. **`tests/baselines/reference/sourceMapValidationDestructuringForOfObjectBindingPatternDefaultValues2(target=es2015).js`** -> AI Confidence: **99.29%**
451. **`tests/baselines/reference/sourceMapValidationDo.js`** -> AI Confidence: **99.29%**
452. **`tests/baselines/reference/sourceMapValidationFor.js`** -> AI Confidence: **99.29%**
453. **`tests/baselines/reference/sourceMapValidationIfElse.js`** -> AI Confidence: **99.29%**
454. **`tests/baselines/reference/sourceMapValidationSwitch.js`** -> AI Confidence: **99.29%**
455. **`tests/baselines/reference/sourceMapValidationTryCatchFinally.js`** -> AI Confidence: **99.29%**
456. **`tests/baselines/reference/specializedSignatureWithOptional.js`** -> AI Confidence: **99.29%**
457. **`tests/baselines/reference/spreadObjectPermutations(exactoptionalpropertytypes=false).js`** -> AI Confidence: **99.29%**
458. **`tests/baselines/reference/spreadObjectPermutations(exactoptionalpropertytypes=true).js`** -> AI Confidence: **99.29%**
459. **`tests/baselines/reference/spreadOfObjectLiteralAssignableToIndexSignature.js`** -> AI Confidence: **99.29%**
460. **`tests/baselines/reference/standaloneBreak.js`** -> AI Confidence: **99.29%**
461. **`tests/baselines/reference/staticIndexSignature4.js`** -> AI Confidence: **99.29%**
462. **`tests/baselines/reference/staticsInAFunction.js`** -> AI Confidence: **99.29%**
463. **`tests/baselines/reference/strictSubtypeAndNarrowing.js`** -> AI Confidence: **99.29%**
464. **`tests/baselines/reference/stringLiteralMatchedInSwitch01.js`** -> AI Confidence: **99.29%**
465. **`tests/baselines/reference/stringLiteralsWithSwitchStatements01.js`** -> AI Confidence: **99.29%**
466. **`tests/baselines/reference/stringLiteralsWithSwitchStatements03.js`** -> AI Confidence: **99.29%**
467. **`tests/baselines/reference/stringLiteralsWithSwitchStatements04.js`** -> AI Confidence: **99.29%**
468. **`tests/baselines/reference/switchBreakStatements.js`** -> AI Confidence: **99.29%**
469. **`tests/baselines/reference/switchCaseCircularRefeference.js`** -> AI Confidence: **99.29%**
470. **`tests/baselines/reference/switchCaseInternalComments.js`** -> AI Confidence: **99.29%**
471. **`tests/baselines/reference/switchCases.js`** -> AI Confidence: **99.29%**
472. **`tests/baselines/reference/switchCasesExpressionTypeMismatch.js`** -> AI Confidence: **99.29%**
473. **`tests/baselines/reference/switchStatements.js`** -> AI Confidence: **99.29%**
474. **`tests/baselines/reference/switchStatementsWithMultipleDefaults.js`** -> AI Confidence: **99.29%**
475. **`tests/baselines/reference/switchStatementsWithMultipleDefaults1.js`** -> AI Confidence: **99.29%**
476. **`tests/baselines/reference/switchWithConstrainedTypeVariable.js`** -> AI Confidence: **99.29%**
477. **`tests/baselines/reference/symbolType1.js`** -> AI Confidence: **99.29%**
478. **`tests/baselines/reference/symbolType11.js`** -> AI Confidence: **99.29%**
479. **`tests/baselines/reference/templateStringInSwitchAndCase.js`** -> AI Confidence: **99.29%**
480. **`tests/baselines/reference/templateStringInSwitchAndCaseES6.js`** -> AI Confidence: **99.29%**
481. **`tests/baselines/reference/templateStringInWhile.js`** -> AI Confidence: **99.29%**
482. **`tests/baselines/reference/templateStringInWhileES6.js`** -> AI Confidence: **99.29%**
483. **`tests/baselines/reference/truthinessCallExpressionCoercion2.js`** -> AI Confidence: **99.29%**
484. **`tests/baselines/reference/truthinessPromiseCoercion.js`** -> AI Confidence: **99.29%**
485. **`tests/baselines/reference/tryCatchFinally.js`** -> AI Confidence: **99.29%**
486. **`tests/baselines/reference/tryStatementInternalComments.js`** -> AI Confidence: **99.29%**
487. **`tests/baselines/reference/tryStatements.js`** -> AI Confidence: **99.29%**
488. **`tests/baselines/reference/tsbuild/commandLine/help.js`** -> AI Confidence: **99.29%**
489. **`tests/baselines/reference/tsbuild/noEmit/multiFile/dts-errors-without-dts-enabled.js`** -> AI Confidence: **99.29%**
490. **`tests/baselines/reference/tsbuild/noEmit/multiFile/semantic-errors.js`** -> AI Confidence: **99.29%**
491. **`tests/baselines/reference/tsbuild/noEmit/multiFile/syntax-errors-with-incremental-discrepancies.js`** -> AI Confidence: **99.29%**
492. **`tests/baselines/reference/tsbuild/noEmit/multiFile/syntax-errors.js`** -> AI Confidence: **99.29%**
493. **`tests/baselines/reference/tsbuildWatch/noEmit/multiFile/does-not-go-in-loop-when-watching-when-no-files-are-emitted.js`** -> AI Confidence: **99.29%**
494. **`tests/baselines/reference/tsbuildWatch/noEmit/multiFile/dts-errors-without-dts-enabled.js`** -> AI Confidence: **99.29%**
495. **`tests/baselines/reference/tsbuildWatch/noEmit/multiFile/semantic-errors.js`** -> AI Confidence: **99.29%**
496. **`tests/baselines/reference/tsbuildWatch/noEmit/multiFile/syntax-errors.js`** -> AI Confidence: **99.29%**
497. **`tests/baselines/reference/tsbuildWatch/noEmit/outFile/does-not-go-in-loop-when-watching-when-no-files-are-emitted.js`** -> AI Confidence: **99.29%**
498. **`tests/baselines/reference/tsbuildWatch/noEmit/outFile/semantic-errors.js`** -> AI Confidence: **99.29%**
499. **`tests/baselines/reference/tsbuildWatch/noEmit/outFile/syntax-errors.js`** -> AI Confidence: **99.29%**
500. **`tests/baselines/reference/tsc/commandLine/adds-color-when-FORCE_COLOR-is-set.js`** -> AI Confidence: **99.29%**
501. **`tests/baselines/reference/tsc/commandLine/does-not-add-color-when-NO_COLOR-is-set-even-if-FORCE_COLOR-is-set.js`** -> AI Confidence: **99.29%**
502. **`tests/baselines/reference/tsc/commandLine/does-not-add-color-when-NO_COLOR-is-set.js`** -> AI Confidence: **99.29%**
503. **`tests/baselines/reference/tsc/commandLine/help-all.js`** -> AI Confidence: **99.29%**
504. **`tests/baselines/reference/tsc/commandLine/help.js`** -> AI Confidence: **99.29%**
505. **`tests/baselines/reference/tsc/commandLine/show-help-with-ExitStatus.DiagnosticsPresent_OutputsSkipped-when-host-can't-provide-terminal-width.js`** -> AI Confidence: **99.29%**
506. **`tests/baselines/reference/tsc/commandLine/show-help-with-ExitStatus.DiagnosticsPresent_OutputsSkipped.js`** -> AI Confidence: **99.29%**
507. **`tests/baselines/reference/tsc/forceConsistentCasingInFileNames/with-type-ref-from-file.js`** -> AI Confidence: **99.29%**
508. **`tests/baselines/reference/tsc/ignoreConfig/without-any-options-when-config-file-absent-with---ignoreConfig.js`** -> AI Confidence: **99.29%**
509. **`tests/baselines/reference/tsc/ignoreConfig/without-any-options-when-config-file-absent.js`** -> AI Confidence: **99.29%**
510. **`tests/baselines/reference/tsc/noEmit/multiFile/syntax-errors-with-incremental-discrepancies.js`** -> AI Confidence: **99.29%**
511. **`tests/baselines/reference/tsc/noEmitOnError/multiFile/when-declarationMap-changes-discrepancies.js`** -> AI Confidence: **99.29%**
512. **`tests/baselines/reference/tscWatch/consoleClearing/when-preserveWatchOutput-is-true-in-config-file/createWatchOfConfigFile.js`** -> AI Confidence: **99.29%**
513. **`tests/baselines/reference/tscWatch/consoleClearing/when-preserveWatchOutput-is-true-in-config-file/when-createWatchProgram-is-invoked-with-configFileParseResult-on-WatchCompilerHostOfConfigFile.js`** -> AI Confidence: **99.29%**
514. **`tests/baselines/reference/tscWatch/consoleClearing/with---diagnostics.js`** -> AI Confidence: **99.29%**
515. **`tests/baselines/reference/tscWatch/consoleClearing/with---extendedDiagnostics.js`** -> AI Confidence: **99.29%**
516. **`tests/baselines/reference/tscWatch/consoleClearing/with---preserveWatchOutput.js`** -> AI Confidence: **99.29%**
517. **`tests/baselines/reference/tscWatch/consoleClearing/without---diagnostics-or---extendedDiagnostics.js`** -> AI Confidence: **99.29%**
518. **`tests/baselines/reference/tscWatch/noEmit/multiFile/dts-errors-without-dts-enabled.js`** -> AI Confidence: **99.29%**
519. **`tests/baselines/reference/tscWatch/noEmit/multiFile/semantic-errors.js`** -> AI Confidence: **99.29%**
520. **`tests/baselines/reference/tscWatch/noEmit/multiFile/syntax-errors.js`** -> AI Confidence: **99.29%**
521. **`tests/baselines/reference/tscWatch/noEmit/outFile/semantic-errors.js`** -> AI Confidence: **99.29%**
522. **`tests/baselines/reference/tscWatch/noEmit/outFile/syntax-errors.js`** -> AI Confidence: **99.29%**
523. **`tests/baselines/reference/tscWatch/programUpdates/Proper-errors-document-is-not-contained-in-project.js`** -> AI Confidence: **99.29%**
524. **`tests/baselines/reference/tscWatch/programUpdates/Updates-diagnostics-when-'--noUnusedLabels'-changes.js`** -> AI Confidence: **99.29%**
525. **`tests/baselines/reference/tscWatch/programUpdates/updates-emit-on-jsx-option-add.js`** -> AI Confidence: **99.29%**
526. **`tests/baselines/reference/tscWatch/programUpdates/updates-emit-on-jsx-option-change.js`** -> AI Confidence: **99.29%**
527. **`tests/baselines/reference/tscWatch/programUpdates/updates-errors-when-ambient-modules-of-program-changes.js`** -> AI Confidence: **99.29%**
528. **`tests/baselines/reference/tscWatch/programUpdates/updates-errors-when-noErrorTruncation-changes.js`** -> AI Confidence: **99.29%**
529. **`tests/baselines/reference/tscWatch/programUpdates/updates-errors-when-strictNullChecks-changes.js`** -> AI Confidence: **99.29%**
530. **`tests/baselines/reference/tscWatch/programUpdates/when-creating-extensionless-file.js`** -> AI Confidence: **99.29%**
531. **`tests/baselines/reference/tscWatch/programUpdates/when-skipLibCheck-and-skipDefaultLibCheck-changes.js`** -> AI Confidence: **99.29%**
532. **`tests/baselines/reference/tscWatch/resolutionCache/when-types-in-compiler-option-are-global-and-installed-at-later-point.js`** -> AI Confidence: **99.29%**
533. **`tests/baselines/reference/tscWatch/resolutionCache/works-when-installing-something-in-node_modules-or-@types-when-there-is-no-notification-from-fs-for-index-file.js`** -> AI Confidence: **99.29%**
534. **`tests/baselines/reference/tscWatch/watchApi/extraFileExtensions-are-supported.js`** -> AI Confidence: **99.29%**
535. **`tests/baselines/reference/tscWatch/watchApi/without-timesouts-on-host-program-gets-updated.js`** -> AI Confidence: **99.29%**
536. **`tests/baselines/reference/tscWatch/watchEnvironment/watchDirectories/uses-non-recursive-dynamic-polling-when-renaming-file-in-subfolder.js`** -> AI Confidence: **99.29%**
537. **`tests/baselines/reference/tscWatch/watchEnvironment/watchDirectories/uses-non-recursive-watchDirectory-when-renaming-file-in-subfolder.js`** -> AI Confidence: **99.29%**
538. **`tests/baselines/reference/tscWatch/watchEnvironment/watchDirectories/uses-watchFile-when-renaming-file-in-subfolder.js`** -> AI Confidence: **99.29%**
539. **`tests/baselines/reference/tsserver/autoImportProvider/Does-not-create-an-auto-import-provider-if-there-are-too-many-dependencies.js`** -> AI Confidence: **99.29%**
540. **`tests/baselines/reference/tsserver/compileOnSave/emit-with-richRepsonse-as-false.js`** -> AI Confidence: **99.29%**
541. **`tests/baselines/reference/tsserver/compileOnSave/emit-with-richRepsonse-as-true.js`** -> AI Confidence: **99.29%**
542. **`tests/baselines/reference/tsserver/compileOnSave/emit-with-richRepsonse-as-undefined.js`** -> AI Confidence: **99.29%**
543. **`tests/baselines/reference/tsserver/compileOnSave/should-not-emit-js-files-in-external-projects.js`** -> AI Confidence: **99.29%**
544. **`tests/baselines/reference/tsserver/compileOnSave/use-projectRoot-as-current-directory.js`** -> AI Confidence: **99.29%**
545. **`tests/baselines/reference/tsserver/configFileSearch/should-stop-at-projectRootPath-if-given.js`** -> AI Confidence: **99.29%**
546. **`tests/baselines/reference/tsserver/configFileSearch/should-use-projectRootPath-when-searching-for-inferred-project-again-2.js`** -> AI Confidence: **99.29%**
547. **`tests/baselines/reference/tsserver/configFileSearch/should-use-projectRootPath-when-searching-for-inferred-project-again.js`** -> AI Confidence: **99.29%**
548. **`tests/baselines/reference/tsserver/configFileSearch/tsconfig-for-the-file-does-not-exist.js`** -> AI Confidence: **99.29%**
549. **`tests/baselines/reference/tsserver/configFileSearch/when-projectRootPath-is-not-present.js`** -> AI Confidence: **99.29%**
550. **`tests/baselines/reference/tsserver/configFileSearch/when-projectRootPath-is-present-but-file-is-not-from-project-root.js`** -> AI Confidence: **99.29%**
551. **`tests/baselines/reference/tsserver/configuredProjects/add-and-then-remove-a-config-file-in-a-folder-with-loose-files.js`** -> AI Confidence: **99.29%**
552. **`tests/baselines/reference/tsserver/configuredProjects/add-and-then-remove-a-config-file-when-parent-folder-has-config-file.js`** -> AI Confidence: **99.29%**
553. **`tests/baselines/reference/tsserver/configuredProjects/add-and-then-remove-a-config-file-with-sibling-jsconfig-file.js`** -> AI Confidence: **99.29%**
554. **`tests/baselines/reference/tsserver/configuredProjects/should-not-close-configured-project-after-closing-last-open-file,-but-should-be-closed-on-next-file-open-if-its-not-the-file-from-same-project.js`** -> AI Confidence: **99.29%**
555. **`tests/baselines/reference/tsserver/configuredProjects/when-file-name-starts-with-caret.js`** -> AI Confidence: **99.29%**
556. **`tests/baselines/reference/tsserver/declarationFileMaps/findAllReferencesFull-definition-is-in-mapped-file.js`** -> AI Confidence: **99.29%**
557. **`tests/baselines/reference/tsserver/declarationFileMaps/getEditsForFileRename-when-referencing-project-doesnt-include-file-and-its-renamed.js`** -> AI Confidence: **99.29%**
558. **`tests/baselines/reference/tsserver/dynamicFiles/chat-block-with-imports.js`** -> AI Confidence: **99.29%**
559. **`tests/baselines/reference/tsserver/dynamicFiles/dynamic-file-with-projectRootPath-with-useInferredProjectPerProjectRoot.js`** -> AI Confidence: **99.29%**
560. **`tests/baselines/reference/tsserver/dynamicFiles/dynamic-file-with-reference-paths-without-external-project.js`** -> AI Confidence: **99.29%**
561. **`tests/baselines/reference/tsserver/dynamicFiles/opening-and-closing-untitled-files-when-projectRootPath-is-different-from-currentDirectory.js`** -> AI Confidence: **99.29%**
562. **`tests/baselines/reference/tsserver/dynamicFiles/opening-untitled-files-without-inferred-project-per-projectRootPath.js`** -> AI Confidence: **99.29%**
563. **`tests/baselines/reference/tsserver/dynamicFiles/opening-untitled-files.js`** -> AI Confidence: **99.29%**
564. **`tests/baselines/reference/tsserver/dynamicFiles/untitled-can-convert-positions-to-locations.js`** -> AI Confidence: **99.29%**
565. **`tests/baselines/reference/tsserver/dynamicFiles/untitled.js`** -> AI Confidence: **99.29%**
566. **`tests/baselines/reference/tsserver/dynamicFiles/walkThroughSnippet.js`** -> AI Confidence: **99.29%**
567. **`tests/baselines/reference/tsserver/dynamicFiles/when-changing-scriptKind-of-the-untitled-files.js`** -> AI Confidence: **99.29%**
568. **`tests/baselines/reference/tsserver/events/projectLanguageServiceState/language-service-disabled-events-are-triggered.js`** -> AI Confidence: **99.29%**
569. **`tests/baselines/reference/tsserver/externalProjects/correctly-handling-add-or-remove-tsconfig---1-with-lazyConfiguredProjectsFromExternalProject.js`** -> AI Confidence: **99.29%**
570. **`tests/baselines/reference/tsserver/externalProjects/correctly-handling-add-or-remove-tsconfig---2-with-lazyConfiguredProjectsFromExternalProject.js`** -> AI Confidence: **99.29%**
571. **`tests/baselines/reference/tsserver/externalProjects/correctly-handling-add-or-remove-tsconfig---2.js`** -> AI Confidence: **99.29%**
572. **`tests/baselines/reference/tsserver/externalProjects/deleting-config-file-opened-from-the-external-project-works-with-lazyConfiguredProjectsFromExternalProject.js`** -> AI Confidence: **99.29%**
573. **`tests/baselines/reference/tsserver/externalProjects/deleting-config-file-opened-from-the-external-project-works.js`** -> AI Confidence: **99.29%**
574. **`tests/baselines/reference/tsserver/externalProjects/handles-creation-of-external-project-with-jsconfig-before-jsconfig-creation-watcher-is-invoked.js`** -> AI Confidence: **99.29%**
575. **`tests/baselines/reference/tsserver/externalProjects/when-file-name-starts-with-caret.js`** -> AI Confidence: **99.29%**
576. **`tests/baselines/reference/tsserver/formatSettings/works-when-extends-is-specified-with-a-case-insensitive-file-system.js`** -> AI Confidence: **99.29%**
577. **`tests/baselines/reference/tsserver/fourslashServer/autoImportPackageJsonFilterExistingImport2.js`** -> AI Confidence: **99.29%**
578. **`tests/baselines/reference/tsserver/fourslashServer/autoImportPackageJsonFilterExistingImport3.js`** -> AI Confidence: **99.29%**
579. **`tests/baselines/reference/tsserver/fourslashServer/completionsServerCommitCharacters.js`** -> AI Confidence: **99.29%**
580. **`tests/baselines/reference/tsserver/fourslashServer/documentHighlights01.js`** -> AI Confidence: **99.29%**
581. **`tests/baselines/reference/tsserver/fourslashServer/documentHighlights02.js`** -> AI Confidence: **99.29%**
582. **`tests/baselines/reference/tsserver/fourslashServer/fixExtractToInnerFunctionDuplicaton.js`** -> AI Confidence: **99.29%**
583. **`tests/baselines/reference/tsserver/fourslashServer/format01.js`** -> AI Confidence: **99.29%**
584. **`tests/baselines/reference/tsserver/fourslashServer/formatBracketInSwitchCase.js`** -> AI Confidence: **99.29%**
585. **`tests/baselines/reference/tsserver/fourslashServer/formatOnEnter.js`** -> AI Confidence: **99.29%**
586. **`tests/baselines/reference/tsserver/fourslashServer/formatTrimRemainingRange.js`** -> AI Confidence: **99.29%**
587. **`tests/baselines/reference/tsserver/fourslashServer/formatonkey01.js`** -> AI Confidence: **99.29%**
588. **`tests/baselines/reference/tsserver/fourslashServer/getOutliningSpansForComments.js`** -> AI Confidence: **99.29%**
589. **`tests/baselines/reference/tsserver/fourslashServer/getOutliningSpansForRegions.js`** -> AI Confidence: **99.29%**
590. **`tests/baselines/reference/tsserver/fourslashServer/getOutliningSpansForRegionsNoSingleLineFolds.js`** -> AI Confidence: **99.29%**
591. **`tests/baselines/reference/tsserver/fourslashServer/goToSource13_nodenext.js`** -> AI Confidence: **99.29%**
592. **`tests/baselines/reference/tsserver/fourslashServer/goToSource14_unresolvedRequireDestructuring.js`** -> AI Confidence: **99.29%**
593. **`tests/baselines/reference/tsserver/fourslashServer/implementation01.js`** -> AI Confidence: **99.29%**
594. **`tests/baselines/reference/tsserver/fourslashServer/jsdocCallbackTagRename01.js`** -> AI Confidence: **99.29%**
595. **`tests/baselines/reference/tsserver/fourslashServer/jsdocParamTagSpecialKeywords.js`** -> AI Confidence: **99.29%**
596. **`tests/baselines/reference/tsserver/fourslashServer/jsdocTypedefTag1.js`** -> AI Confidence: **99.29%**
597. **`tests/baselines/reference/tsserver/fourslashServer/jsdocTypedefTag2.js`** -> AI Confidence: **99.29%**
598. **`tests/baselines/reference/tsserver/fourslashServer/jsdocTypedefTagRename02.js`** -> AI Confidence: **99.29%**
599. **`tests/baselines/reference/tsserver/fourslashServer/jsdocTypedefTagRename03.js`** -> AI Confidence: **99.29%**
600. **`tests/baselines/reference/tsserver/fourslashServer/nodeNextPathCompletions.js`** -> AI Confidence: **99.29%**
601. **`tests/baselines/reference/tsserver/fourslashServer/occurrences01.js`** -> AI Confidence: **99.29%**
602. **`tests/baselines/reference/tsserver/fourslashServer/occurrences02.js`** -> AI Confidence: **99.29%**
603. **`tests/baselines/reference/tsserver/fourslashServer/pasteEdits_pasteComments.js`** -> AI Confidence: **99.29%**
604. **`tests/baselines/reference/tsserver/fourslashServer/pasteEdits_pasteIntoSameFile.js`** -> AI Confidence: **99.29%**
605. **`tests/baselines/reference/tsserver/fourslashServer/pasteEdits_rangeSelection0.js`** -> AI Confidence: **99.29%**
606. **`tests/baselines/reference/tsserver/fourslashServer/pathCompletionsPackageJsonImportsSrcNoDistWildcard2.js`** -> AI Confidence: **99.29%**
607. **`tests/baselines/reference/tsserver/fourslashServer/pathCompletionsPackageJsonImportsSrcNoDistWildcard3.js`** -> AI Confidence: **99.29%**
608. **`tests/baselines/reference/tsserver/fourslashServer/quickinfoVerbosityServer.js`** -> AI Confidence: **99.29%**
609. **`tests/baselines/reference/tsserver/fourslashServer/referenceToEmptyObject.js`** -> AI Confidence: **99.29%**
610. **`tests/baselines/reference/tsserver/fourslashServer/referencesInEmptyFile.js`** -> AI Confidence: **99.29%**
611. **`tests/baselines/reference/tsserver/fourslashServer/referencesInEmptyFileWithMultipleProjects.js`** -> AI Confidence: **99.29%**
612. **`tests/baselines/reference/tsserver/fourslashServer/referencesInStringLiteralValueWithMultipleProjects.js`** -> AI Confidence: **99.29%**
613. **`tests/baselines/reference/tsserver/fourslashServer/referencesToNonPropertyNameStringLiteral.js`** -> AI Confidence: **99.29%**
614. **`tests/baselines/reference/tsserver/fourslashServer/referencesToStringLiteralValue.js`** -> AI Confidence: **99.29%**
615. **`tests/baselines/reference/tsserver/fourslashServer/rename01.js`** -> AI Confidence: **99.29%**
616. **`tests/baselines/reference/tsserver/fourslashServer/renameNamedImport.js`** -> AI Confidence: **99.29%**
617. **`tests/baselines/reference/tsserver/fourslashServer/renameNamespaceImport.js`** -> AI Confidence: **99.29%**
618. **`tests/baselines/reference/tsserver/fourslashServer/semanticClassificationJs1.js`** -> AI Confidence: **99.29%**
619. **`tests/baselines/reference/tsserver/fourslashServer/signatureHelp01.js`** -> AI Confidence: **99.29%**
620. **`tests/baselines/reference/tsserver/fourslashServer/tsconfigComputedPropertyError.js`** -> AI Confidence: **99.29%**
621. **`tests/baselines/reference/tsserver/fourslashServer/tsxIncrementalServer.js`** -> AI Confidence: **99.29%**
622. **`tests/baselines/reference/tsserver/fourslashServer/typeReferenceOnServer.js`** -> AI Confidence: **99.29%**
623. **`tests/baselines/reference/tsserver/getApplicableRefactors/returns-the-affected-range-of-text-for-'move-to-file'-and-'move-to-new-file'-refactors.js`** -> AI Confidence: **99.29%**
624. **`tests/baselines/reference/tsserver/getApplicableRefactors/returns-the-affected-range-of-text-for-extract-type-refactor.js`** -> AI Confidence: **99.29%**
625. **`tests/baselines/reference/tsserver/getApplicableRefactors/works-when-taking-position.js`** -> AI Confidence: **99.29%**
626. **`tests/baselines/reference/tsserver/inferredProjects/inferred-projects-per-project-root-with-case-insensitive-system.js`** -> AI Confidence: **99.29%**
627. **`tests/baselines/reference/tsserver/inferredProjects/inferred-projects-per-project-root-with-case-sensitive-system.js`** -> AI Confidence: **99.29%**
628. **`tests/baselines/reference/tsserver/inferredProjects/regression-test---should-infer-typeAcquisition-for-inferred-projects-when-set-undefined.js`** -> AI Confidence: **99.29%**
629. **`tests/baselines/reference/tsserver/inferredProjects/should-still-retain-configured-project-created-while-opening-the-file.js`** -> AI Confidence: **99.29%**
630. **`tests/baselines/reference/tsserver/navTo/should-not-include-type-symbols.js`** -> AI Confidence: **99.29%**
631. **`tests/baselines/reference/tsserver/navTo/should-work-with-Deprecated.js`** -> AI Confidence: **99.29%**
632. **`tests/baselines/reference/tsserver/packageJsonInfo/detects-new-package.json-files-that-are-added,-caches-them,-and-watches-them.js`** -> AI Confidence: **99.29%**
633. **`tests/baselines/reference/tsserver/packageJsonInfo/finds-multiple-package.json-files-when-present.js`** -> AI Confidence: **99.29%**
634. **`tests/baselines/reference/tsserver/packageJsonInfo/finds-package.json-on-demand,-watches-for-deletion,-and-removes-them-from-cache.js`** -> AI Confidence: **99.29%**
635. **`tests/baselines/reference/tsserver/packageJsonInfo/handles-empty-package.json.js`** -> AI Confidence: **99.29%**
636. **`tests/baselines/reference/tsserver/packageJsonInfo/handles-errors-in-json-parsing-of-package.json.js`** -> AI Confidence: **99.29%**
637. **`tests/baselines/reference/tsserver/partialSemanticServer/should-not-include-referenced-files-from-unopened-files.js`** -> AI Confidence: **99.29%**
638. **`tests/baselines/reference/tsserver/partialSemanticServer/syntactic-diagnostics-are-returned-with-no-error.js`** -> AI Confidence: **99.29%**
639. **`tests/baselines/reference/tsserver/plugins/when-plugins-use-LS-to-get-program-and-update-is-pending.js`** -> AI Confidence: **99.29%**
640. **`tests/baselines/reference/tsserver/projectErrors/configFileDiagnostic-events-are-not-generated-when-the-config-file-does-not-include-file-opened-and-config-file-has-errors.js`** -> AI Confidence: **99.29%**
641. **`tests/baselines/reference/tsserver/projectErrors/configured-projects---diagnostics-for-missing-files.js`** -> AI Confidence: **99.29%**
642. **`tests/baselines/reference/tsserver/projectErrors/diagnostics-after-noUnusedLabels-changes.js`** -> AI Confidence: **99.29%**
643. **`tests/baselines/reference/tsserver/projectErrors/document-is-not-contained-in-project.js`** -> AI Confidence: **99.29%**
644. **`tests/baselines/reference/tsserver/projectErrors/external-project---diagnostics-for-missing-files.js`** -> AI Confidence: **99.29%**
645. **`tests/baselines/reference/tsserver/projectErrors/for-external-project.js`** -> AI Confidence: **99.29%**
646. **`tests/baselines/reference/tsserver/projectErrors/for-inferred-project.js`** -> AI Confidence: **99.29%**
647. **`tests/baselines/reference/tsserver/projectErrors/reports-errors-correctly-when-file-referenced-by-inferred-project-root,-is-opened-right-after-closing-the-root-file.js`** -> AI Confidence: **99.29%**
648. **`tests/baselines/reference/tsserver/projectReferences/with-dts-file-next-to-ts-file.js`** -> AI Confidence: **99.29%**
649. **`tests/baselines/reference/tsserver/projects/regression-test-for-crash-in-acquireOrUpdateDocument.js`** -> AI Confidence: **99.29%**
650. **`tests/baselines/reference/tsserver/projects/syntax-tree-cache-handles-changes-in-project-settings.js`** -> AI Confidence: **99.29%**
651. **`tests/baselines/reference/tsserver/refactors/use-formatting-options.js`** -> AI Confidence: **99.29%**
652. **`tests/baselines/reference/tsserver/regionDiagnostics/diagnostics-for-select-nodes-in-a-single-file.js`** -> AI Confidence: **99.29%**
653. **`tests/baselines/reference/tsserver/regionDiagnostics/region-diagnostics-is-skipped-for-@ts-nocheck-file.js`** -> AI Confidence: **99.29%**
654. **`tests/baselines/reference/tsserver/regionDiagnostics/region-diagnostics-is-skipped-for-small-file.js`** -> AI Confidence: **99.29%**
655. **`tests/baselines/reference/tsserver/rename/works-with-prefixText-and-suffixText-when-enabled.js`** -> AI Confidence: **99.29%**
656. **`tests/baselines/reference/tsserver/resolutionCache/disable-suggestion-diagnostics.js`** -> AI Confidence: **99.29%**
657. **`tests/baselines/reference/tsserver/resolutionCache/suggestion-diagnostics.js`** -> AI Confidence: **99.29%**
658. **`tests/baselines/reference/tsserver/resolutionCache/suppressed-diagnostic-events.js`** -> AI Confidence: **99.29%**
659. **`tests/baselines/reference/tsserver/resolutionCache/when-resolution-fails-in-global-typings-location-with-currentDirectory-at-root.js`** -> AI Confidence: **99.29%**
660. **`tests/baselines/reference/tsserver/resolutionCache/when-resolution-fails-in-global-typings-location.js`** -> AI Confidence: **99.29%**
661. **`tests/baselines/reference/tsserver/skipLibCheck/jsonly-inferred-project.js`** -> AI Confidence: **99.29%**
662. **`tests/baselines/reference/tsserver/skipLibCheck/reports-semantic-error-with-tscheck.js`** -> AI Confidence: **99.29%**
663. **`tests/baselines/reference/tsserver/syntacticServer/should-not-include-referenced-files-from-unopened-files.js`** -> AI Confidence: **99.29%**
664. **`tests/baselines/reference/tsserver/telemetry/detects-whether-language-service-was-disabled.js`** -> AI Confidence: **99.29%**
665. **`tests/baselines/reference/tsserver/telemetry/does-not-expose-paths.js`** -> AI Confidence: **99.29%**
666. **`tests/baselines/reference/tsserver/telemetry/does-nothing-for-inferred-project.js`** -> AI Confidence: **99.29%**
667. **`tests/baselines/reference/tsserver/telemetry/even-for-project-with-ts-check-in-config.js`** -> AI Confidence: **99.29%**
668. **`tests/baselines/reference/tsserver/telemetry/not-for-ts-file.js`** -> AI Confidence: **99.29%**
669. **`tests/baselines/reference/tsserver/telemetry/only-sends-an-event-once.js`** -> AI Confidence: **99.29%**
670. **`tests/baselines/reference/tsserver/telemetry/sends-event-for-inferred-project.js`** -> AI Confidence: **99.29%**
671. **`tests/baselines/reference/tsserver/telemetry/sends-telemetry-for-file-sizes.js`** -> AI Confidence: **99.29%**
672. **`tests/baselines/reference/tsserver/telemetry/sends-telemetry-for-typeAcquisition-settings.js`** -> AI Confidence: **99.29%**
673. **`tests/baselines/reference/tsserver/telemetry/works-with-external-project.js`** -> AI Confidence: **99.29%**
674. **`tests/baselines/reference/tsserver/typeAquisition/does-not-depend-on-extension.js`** -> AI Confidence: **99.29%**
675. **`tests/baselines/reference/tsserver/typingsInstaller/configured-projects-discover-from-bower_components.js`** -> AI Confidence: **99.29%**
676. **`tests/baselines/reference/tsserver/typingsInstaller/configured-projects.js`** -> AI Confidence: **99.29%**
677. **`tests/baselines/reference/tsserver/typingsInstaller/discover-from-bower.js`** -> AI Confidence: **99.29%**
678. **`tests/baselines/reference/tsserver/typingsInstaller/discover-from-node_modules-empty-types-has-import.js`** -> AI Confidence: **99.29%**
679. **`tests/baselines/reference/tsserver/typingsInstaller/discover-from-node_modules-empty-types.js`** -> AI Confidence: **99.29%**
680. **`tests/baselines/reference/tsserver/typingsInstaller/discover-from-node_modules-explicit-types.js`** -> AI Confidence: **99.29%**
681. **`tests/baselines/reference/tsserver/typingsInstaller/discover-from-node_modules.js`** -> AI Confidence: **99.29%**
682. **`tests/baselines/reference/tsserver/typingsInstaller/discover-typings-should-search-only-2-levels-deep.js`** -> AI Confidence: **99.29%**
683. **`tests/baselines/reference/tsserver/typingsInstaller/discover-typings-should-support-scoped-packages.js`** -> AI Confidence: **99.29%**
684. **`tests/baselines/reference/tsserver/typingsInstaller/expired-cache-entry-lockFile3.js`** -> AI Confidence: **99.29%**
685. **`tests/baselines/reference/tsserver/typingsInstaller/expired-cache-entry.js`** -> AI Confidence: **99.29%**
686. **`tests/baselines/reference/tsserver/typingsInstaller/external-projects-autoDiscovery.js`** -> AI Confidence: **99.29%**
687. **`tests/baselines/reference/tsserver/typingsInstaller/external-projects-duplicate-package.js`** -> AI Confidence: **99.29%**
688. **`tests/baselines/reference/tsserver/typingsInstaller/external-projects-no-auto-typings.js`** -> AI Confidence: **99.29%**
689. **`tests/baselines/reference/tsserver/typingsInstaller/external-projects-no-type-acquisition-with-enable-false.js`** -> AI Confidence: **99.29%**
690. **`tests/baselines/reference/tsserver/typingsInstaller/external-projects-no-type-acquisition-with-js-ts-files.js`** -> AI Confidence: **99.29%**
691. **`tests/baselines/reference/tsserver/typingsInstaller/external-projects-no-type-acquisition.js`** -> AI Confidence: **99.29%**
692. **`tests/baselines/reference/tsserver/typingsInstaller/external-projects-type-acquisition-with-disableFilenameBasedTypeAcquisition.js`** -> AI Confidence: **99.29%**
693. **`tests/baselines/reference/tsserver/typingsInstaller/external-projects-type-acquisition.js`** -> AI Confidence: **99.29%**
694. **`tests/baselines/reference/tsserver/typingsInstaller/external-projects.js`** -> AI Confidence: **99.29%**
695. **`tests/baselines/reference/tsserver/typingsInstaller/inferred-projects-with-disableFilenameBasedTypeAcquisition.js`** -> AI Confidence: **99.29%**
696. **`tests/baselines/reference/tsserver/typingsInstaller/inferred-projects.js`** -> AI Confidence: **99.29%**
697. **`tests/baselines/reference/tsserver/typingsInstaller/multiple-projects.js`** -> AI Confidence: **99.29%**
698. **`tests/baselines/reference/tsserver/typingsInstaller/non-expired-cache-entry-lockFile3.js`** -> AI Confidence: **99.29%**
699. **`tests/baselines/reference/tsserver/typingsInstaller/non-expired-cache-entry.js`** -> AI Confidence: **99.29%**
700. **`tests/baselines/reference/tsserver/typingsInstaller/progress-notification-for-error.js`** -> AI Confidence: **99.29%**
701. **`tests/baselines/reference/tsserver/typingsInstaller/projectRootPath-is-provided-for-inferred-project.js`** -> AI Confidence: **99.29%**
702. **`tests/baselines/reference/tsserver/typingsInstaller/redo-resolutions-pointing-to-js-on-typing-install.js`** -> AI Confidence: **99.29%**
703. **`tests/baselines/reference/tsserver/typingsInstaller/scoped-name-discovery.js`** -> AI Confidence: **99.29%**
704. **`tests/baselines/reference/tsserver/typingsInstaller/should-not-initialize-invaalid-package-names.js`** -> AI Confidence: **99.29%**
705. **`tests/baselines/reference/tsserver/typingsInstaller/throttle-delayed-run-install-requests.js`** -> AI Confidence: **99.29%**
706. **`tests/baselines/reference/tsserver/typingsInstaller/throttle-delayed-typings-to-install.js`** -> AI Confidence: **99.29%**
707. **`tests/baselines/reference/tsserver/typingsInstaller/throttle-scheduled-run-install-requests-with-defer-refreshed.js`** -> AI Confidence: **99.29%**
708. **`tests/baselines/reference/tsserver/typingsInstaller/throttle-scheduled-run-install-requests-with-defer-while-queuing-again.js`** -> AI Confidence: **99.29%**
709. **`tests/baselines/reference/tsserver/typingsInstaller/throttle-scheduled-run-install-requests-with-defer.js`** -> AI Confidence: **99.29%**
710. **`tests/baselines/reference/tsserver/typingsInstaller/throttle-scheduled-run-install-requests-without-reaching-limit.js`** -> AI Confidence: **99.29%**
711. **`tests/baselines/reference/tsserver/watchEnvironment/watching-files-with-network-style-paths.js`** -> AI Confidence: **99.29%**
712. **`tests/baselines/reference/tsxAttributeInvalidNames.js`** -> AI Confidence: **99.29%**
713. **`tests/baselines/reference/tsxAttributeResolution6.js`** -> AI Confidence: **99.29%**
714. **`tests/baselines/reference/tsxAttributeResolution7.js`** -> AI Confidence: **99.29%**
715. **`tests/baselines/reference/tsxStatelessFunctionComponentOverload1.js`** -> AI Confidence: **99.29%**
716. **`tests/baselines/reference/typeFromPropertyAssignment36.js`** -> AI Confidence: **99.29%**
717. **`tests/baselines/reference/typeGuardConstructorClassAndNumber.js`** -> AI Confidence: **99.29%**
718. **`tests/baselines/reference/typeGuardConstructorNarrowAny.js`** -> AI Confidence: **99.29%**
719. **`tests/baselines/reference/typeGuardConstructorNarrowPrimitivesInUnion.js`** -> AI Confidence: **99.29%**
720. **`tests/baselines/reference/typeGuardConstructorPrimitiveTypes.js`** -> AI Confidence: **99.29%**
721. **`tests/baselines/reference/typeGuardIntersectionTypes.js`** -> AI Confidence: **99.29%**
722. **`tests/baselines/reference/typeGuardNarrowsIndexedAccessOfKnownProperty2.js`** -> AI Confidence: **99.29%**
723. **`tests/baselines/reference/typeGuardNarrowsIndexedAccessOfKnownProperty3.js`** -> AI Confidence: **99.29%**
724. **`tests/baselines/reference/typeGuardNarrowsIndexedAccessOfKnownProperty5.js`** -> AI Confidence: **99.29%**
725. **`tests/baselines/reference/typeGuardNarrowsIndexedAccessOfKnownProperty6.js`** -> AI Confidence: **99.29%**
726. **`tests/baselines/reference/typeGuardNarrowsPrimitiveIntersection.js`** -> AI Confidence: **99.29%**
727. **`tests/baselines/reference/typeGuardTautologicalConsistiency.js`** -> AI Confidence: **99.29%**
728. **`tests/baselines/reference/typeGuardTypeOfUndefined.js`** -> AI Confidence: **99.29%**
729. **`tests/baselines/reference/typeGuardsInDoStatement.js`** -> AI Confidence: **99.29%**
730. **`tests/baselines/reference/typeGuardsInForStatement.js`** -> AI Confidence: **99.29%**
731. **`tests/baselines/reference/typeGuardsInWhileStatement.js`** -> AI Confidence: **99.29%**
732. **`tests/baselines/reference/typeGuardsWithAny.js`** -> AI Confidence: **99.29%**
733. **`tests/baselines/reference/typeInterfaceDeclarationsInBlockStatements1.js`** -> AI Confidence: **99.29%**
734. **`tests/baselines/reference/typePredicatesCanNarrowByDiscriminant.js`** -> AI Confidence: **99.29%**
735. **`tests/baselines/reference/typePredicatesInUnion.js`** -> AI Confidence: **99.29%**
736. **`tests/baselines/reference/typePredicatesInUnion_noMatch.js`** -> AI Confidence: **99.29%**
737. **`tests/baselines/reference/uncalledFunctionChecksInConditional.js`** -> AI Confidence: **99.29%**
738. **`tests/baselines/reference/uncalledFunctionChecksInConditionalPerf.js`** -> AI Confidence: **99.29%**
739. **`tests/baselines/reference/undefinedAsDiscriminantWithUnknown(strictnullchecks=false).js`** -> AI Confidence: **99.29%**
740. **`tests/baselines/reference/undefinedAsDiscriminantWithUnknown(strictnullchecks=true).js`** -> AI Confidence: **99.29%**
741. **`tests/baselines/reference/unionReductionMutualSubtypes.js`** -> AI Confidence: **99.29%**
742. **`tests/baselines/reference/unionRelationshipCheckPasses.js`** -> AI Confidence: **99.29%**
743. **`tests/baselines/reference/unionTypeCallSignatures5.js`** -> AI Confidence: **99.29%**
744. **`tests/baselines/reference/unknownType2.js`** -> AI Confidence: **99.29%**
745. **`tests/baselines/reference/unusedParameterInCatchClause.js`** -> AI Confidence: **99.29%**
746. **`tests/baselines/reference/unusedVariablesWithUnderscoreInForOfLoop.js`** -> AI Confidence: **99.29%**
747. **`tests/baselines/reference/unusedVariablesinForLoop2.js`** -> AI Confidence: **99.29%**
748. **`tests/baselines/reference/unusedVariablesinForLoop3.js`** -> AI Confidence: **99.29%**
749. **`tests/baselines/reference/useUnknownInCatchVariables01.js`** -> AI Confidence: **99.29%**
750. **`tests/baselines/reference/usingDeclarations.1(target=es2022).js`** -> AI Confidence: **99.29%**
751. **`tests/baselines/reference/usingDeclarations.17.js`** -> AI Confidence: **99.29%**
752. **`tests/baselines/reference/usingDeclarationsInFor(target=esnext).js`** -> AI Confidence: **99.29%**
753. **`tests/baselines/reference/usingDeclarationsInForIn.js`** -> AI Confidence: **99.29%**
754. **`tests/baselines/reference/usingDeclarationsInForOf.1(target=esnext).js`** -> AI Confidence: **99.29%**
755. **`tests/baselines/reference/usingDeclarationsInForOf.2.js`** -> AI Confidence: **99.29%**
756. **`tests/baselines/reference/usingDeclarationsInForOf.3.js`** -> AI Confidence: **99.29%**
757. **`tests/baselines/reference/usingDeclarationsInForOf.4.js`** -> AI Confidence: **99.29%**
758. **`tests/baselines/reference/voidAsOperator.js`** -> AI Confidence: **99.29%**
759. **`tests/baselines/reference/voidIsInitialized.js`** -> AI Confidence: **99.29%**
760. **`tests/baselines/reference/weakTypeAndPrimitiveNarrowing.js`** -> AI Confidence: **99.29%**
761. **`tests/baselines/reference/webworkerIterable.js`** -> AI Confidence: **99.29%**
762. **`tests/baselines/reference/whileBreakStatements.js`** -> AI Confidence: **99.29%**
763. **`tests/baselines/reference/whileContinueStatements.js`** -> AI Confidence: **99.29%**
764. **`tests/baselines/reference/whileStatementInnerComments.js`** -> AI Confidence: **99.29%**
765. **`src/compiler/factory/utilitiesPublic.ts`** -> AI Confidence: **99.29%**
766. **`src/compiler/programDiagnostics.ts`** -> AI Confidence: **99.29%**
767. **`src/compiler/transformers/esDecorators.ts`** -> AI Confidence: **99.29%**
768. **`src/lib/es2017.date.d.ts`** -> AI Confidence: **99.29%**
769. **`src/lib/es2020.date.d.ts`** -> AI Confidence: **99.29%**
770. **`src/services/codefixes/fixSpelling.ts`** -> AI Confidence: **99.29%**
771. **`src/services/preProcess.ts`** -> AI Confidence: **99.29%**
772. **`src/tsc/tsc.ts`** -> AI Confidence: **99.29%**
773. **`tests/baselines/reference/extractConstant/extractConstant_BlockScopeMismatch.ts`** -> AI Confidence: **99.29%**
774. **`tests/baselines/reference/extractConstant/extractConstant_BlockScopes_NoDependencies.ts`** -> AI Confidence: **99.29%**
775. **`tests/baselines/reference/extractConstant/extractConstant_CaseClauseExpression.ts`** -> AI Confidence: **99.29%**
776. **`tests/baselines/reference/extractConstant/extractConstant_PropertyName_Keyword.ts`** -> AI Confidence: **99.29%**
777. **`tests/baselines/reference/extractConstant/extractConstant_PropertyName_PrivateIdentifierKeyword.ts`** -> AI Confidence: **99.29%**
778. **`tests/baselines/reference/extractConstant/extractConstant_StatementInsertionPosition1.ts`** -> AI Confidence: **99.29%**
779. **`tests/baselines/reference/extractConstant/extractConstant_StatementInsertionPosition2.ts`** -> AI Confidence: **99.29%**
780. **`tests/baselines/reference/extractConstant/extractConstant_StatementInsertionPosition3.ts`** -> AI Confidence: **99.29%**
781. **`tests/baselines/reference/extractConstant/extractConstant_StatementInsertionPosition4.ts`** -> AI Confidence: **99.29%**
782. **`tests/baselines/reference/mapCodeNestedLabeledInsertion.mapCode.ts`** -> AI Confidence: **99.29%**
783. **`tests/cases/compiler/SystemModuleForStatementNoInitializer.ts`** -> AI Confidence: **99.29%**
784. **`tests/cases/compiler/argumentsAsPropertyName2.ts`** -> AI Confidence: **99.29%**
785. **`tests/cases/compiler/asiBreak.ts`** -> AI Confidence: **99.29%**
786. **`tests/cases/compiler/assignmentCompatFunctionsWithOptionalArgs.ts`** -> AI Confidence: **99.29%**
787. **`tests/cases/compiler/asyncFunctionWithForStatementNoInitializer.ts`** -> AI Confidence: **99.29%**
788. **`tests/cases/compiler/binaryArithmeticControlFlowGraphNotTooLarge.ts`** -> AI Confidence: **99.29%**
789. **`tests/cases/compiler/blockScopedBindingUsedBeforeDef.ts`** -> AI Confidence: **99.29%**
790. **`tests/cases/compiler/blockScopedBindingsReassignedInLoop2.ts`** -> AI Confidence: **99.29%**
791. **`tests/cases/compiler/blockScopedBindingsReassignedInLoop3.ts`** -> AI Confidence: **99.29%**
792. **`tests/cases/compiler/blockScopedBindingsReassignedInLoop5.ts`** -> AI Confidence: **99.29%**
793. **`tests/cases/compiler/blockScopedFunctionDeclarationES5.ts`** -> AI Confidence: **99.29%**
794. **`tests/cases/compiler/blockScopedFunctionDeclarationES6.ts`** -> AI Confidence: **99.29%**
795. **`tests/cases/compiler/blockScopedFunctionDeclarationStrictES5.ts`** -> AI Confidence: **99.29%**
796. **`tests/cases/compiler/blockScopedFunctionDeclarationStrictES6.ts`** -> AI Confidence: **99.29%**
797. **`tests/cases/compiler/blockScopedSameNameFunctionDeclarationES5.ts`** -> AI Confidence: **99.29%**
798. **`tests/cases/compiler/blockScopedSameNameFunctionDeclarationES6.ts`** -> AI Confidence: **99.29%**
799. **`tests/cases/compiler/blockScopedSameNameFunctionDeclarationStrictES5.ts`** -> AI Confidence: **99.29%**
800. **`tests/cases/compiler/blockScopedSameNameFunctionDeclarationStrictES6.ts`** -> AI Confidence: **99.29%**
801. **`tests/cases/compiler/breakInIterationOrSwitchStatement2.ts`** -> AI Confidence: **99.29%**
802. **`tests/cases/compiler/breakNotInIterationOrSwitchStatement2.ts`** -> AI Confidence: **99.29%**
803. **`tests/cases/compiler/breakTarget2.ts`** -> AI Confidence: **99.29%**
804. **`tests/cases/compiler/breakTarget3.ts`** -> AI Confidence: **99.29%**
805. **`tests/cases/compiler/breakTarget4.ts`** -> AI Confidence: **99.29%**
806. **`tests/cases/compiler/breakTarget5.ts`** -> AI Confidence: **99.29%**
807. **`tests/cases/compiler/breakTarget6.ts`** -> AI Confidence: **99.29%**
808. **`tests/cases/compiler/capturedLetConstInLoop7.ts`** -> AI Confidence: **99.29%**
809. **`tests/cases/compiler/capturedLetConstInLoop7_ES6.ts`** -> AI Confidence: **99.29%**
810. **`tests/cases/compiler/capturedLetConstInLoop8.ts`** -> AI Confidence: **99.29%**
811. **`tests/cases/compiler/capturedLetConstInLoop8_ES6.ts`** -> AI Confidence: **99.29%**
812. **`tests/cases/compiler/catch.ts`** -> AI Confidence: **99.29%**
813. **`tests/cases/compiler/cf.ts`** -> AI Confidence: **99.29%**
814. **`tests/cases/compiler/circularOptionalityRemoval.ts`** -> AI Confidence: **99.29%**
815. **`tests/cases/compiler/commentOnIfStatement1.ts`** -> AI Confidence: **99.29%**
816. **`tests/cases/compiler/conditionalEqualityOnLiteralObjects.ts`** -> AI Confidence: **99.29%**
817. **`tests/cases/compiler/constDeclarations-errors.ts`** -> AI Confidence: **99.29%**
818. **`tests/cases/compiler/constDeclarations.ts`** -> AI Confidence: **99.29%**
819. **`tests/cases/compiler/contextualTypeLogicalOr.ts`** -> AI Confidence: **99.29%**
820. **`tests/cases/compiler/continueInIterationStatement1.ts`** -> AI Confidence: **99.29%**
821. **`tests/cases/compiler/continueInIterationStatement2.ts`** -> AI Confidence: **99.29%**
822. **`tests/cases/compiler/continueNotInIterationStatement2.ts`** -> AI Confidence: **99.29%**
823. **`tests/cases/compiler/continueNotInIterationStatement3.ts`** -> AI Confidence: **99.29%**
824. **`tests/cases/compiler/continueStatementInternalComments.ts`** -> AI Confidence: **99.29%**
825. **`tests/cases/compiler/continueTarget2.ts`** -> AI Confidence: **99.29%**
826. **`tests/cases/compiler/continueTarget3.ts`** -> AI Confidence: **99.29%**
827. **`tests/cases/compiler/continueTarget4.ts`** -> AI Confidence: **99.29%**
828. **`tests/cases/compiler/continueTarget5.ts`** -> AI Confidence: **99.29%**
829. **`tests/cases/compiler/continueTarget6.ts`** -> AI Confidence: **99.29%**
830. **`tests/cases/compiler/controlFlowBreakContinueWithLabel.ts`** -> AI Confidence: **99.29%**
831. **`tests/cases/compiler/controlFlowCaching.ts`** -> AI Confidence: **99.29%**
832. **`tests/cases/compiler/controlFlowFinallyNoCatchAssignments.ts`** -> AI Confidence: **99.29%**
833. **`tests/cases/compiler/controlFlowForStatementContinueIntoIncrementor1.ts`** -> AI Confidence: **99.29%**
834. **`tests/cases/compiler/controlFlowJavascript.ts`** -> AI Confidence: **99.29%**
835. **`tests/cases/compiler/controlFlowManyCallExpressionStatementsPerf.ts`** -> AI Confidence: **99.29%**
836. **`tests/cases/compiler/controlFlowNullTypeAndLiteral.ts`** -> AI Confidence: **99.29%**
837. **`tests/cases/compiler/declFileForInterfaceWithOptionalFunction.ts`** -> AI Confidence: **99.29%**
838. **`tests/cases/compiler/declarationEmitDestructuringOptionalBindingParametersInOverloads.ts`** -> AI Confidence: **99.29%**
839. **`tests/cases/compiler/declarationEmitDestructuringWithOptionalBindingParameters.ts`** -> AI Confidence: **99.29%**
840. **`tests/cases/compiler/defaultOfAnyInStrictNullChecks.ts`** -> AI Confidence: **99.29%**
841. **`tests/cases/compiler/destructureCatchClause.ts`** -> AI Confidence: **99.29%**
842. **`tests/cases/compiler/destructuringAssignmentWithDefault.ts`** -> AI Confidence: **99.29%**
843. **`tests/cases/compiler/discriminateWithOptionalProperty4.ts`** -> AI Confidence: **99.29%**
844. **`tests/cases/compiler/doYouNeedToChangeYourTargetLibraryES2016Plus.ts`** -> AI Confidence: **99.29%**
845. **`tests/cases/compiler/doubleUnderscoreLabels.ts`** -> AI Confidence: **99.29%**
846. **`tests/cases/compiler/downlevelLetConst17.ts`** -> AI Confidence: **99.29%**
847. **`tests/cases/compiler/duplicateLabel1.ts`** -> AI Confidence: **99.29%**
848. **`tests/cases/compiler/duplicateLabel2.ts`** -> AI Confidence: **99.29%**
849. **`tests/cases/compiler/duplicateLabel3.ts`** -> AI Confidence: **99.29%**
850. **`tests/cases/compiler/duplicateLabel4.ts`** -> AI Confidence: **99.29%**
851. **`tests/cases/compiler/emptyThenWarning.ts`** -> AI Confidence: **99.29%**
852. **`tests/cases/compiler/emptyThenWithoutWarning.ts`** -> AI Confidence: **99.29%**
853. **`tests/cases/compiler/errorOnEnumReferenceInCondition.ts`** -> AI Confidence: **99.29%**
854. **`tests/cases/compiler/es5-asyncFunctionDoStatements.ts`** -> AI Confidence: **99.29%**
855. **`tests/cases/compiler/es5-asyncFunctionSwitchStatements.ts`** -> AI Confidence: **99.29%**
856. **`tests/cases/compiler/exhaustiveSwitchCheckCircularity.ts`** -> AI Confidence: **99.29%**
857. **`tests/cases/compiler/expandoFunctionNestedAssigments.ts`** -> AI Confidence: **99.29%**
858. **`tests/cases/compiler/expr.ts`** -> AI Confidence: **99.29%**
859. **`tests/cases/compiler/externalModuleImmutableBindings.ts`** -> AI Confidence: **99.29%**
860. **`tests/cases/compiler/fallFromLastCase1.ts`** -> AI Confidence: **99.29%**
861. **`tests/cases/compiler/fallFromLastCase2.ts`** -> AI Confidence: **99.29%**
862. **`tests/cases/compiler/firstMatchRegExpMatchArray.ts`** -> AI Confidence: **99.29%**
863. **`tests/cases/compiler/forInStrictNullChecksNoError.ts`** -> AI Confidence: **99.29%**
864. **`tests/cases/compiler/forLoopWithDestructuringDoesNotElideFollowingStatement.ts`** -> AI Confidence: **99.29%**
865. **`tests/cases/compiler/functionCall11.ts`** -> AI Confidence: **99.29%**
866. **`tests/cases/compiler/functionCall12.ts`** -> AI Confidence: **99.29%**
867. **`tests/cases/compiler/functionCall14.ts`** -> AI Confidence: **99.29%**
868. **`tests/cases/compiler/functionCall15.ts`** -> AI Confidence: **99.29%**
869. **`tests/cases/compiler/functionCall16.ts`** -> AI Confidence: **99.29%**
870. **`tests/cases/compiler/functionCall17.ts`** -> AI Confidence: **99.29%**
871. **`tests/cases/compiler/functionCall8.ts`** -> AI Confidence: **99.29%**
872. **`tests/cases/compiler/functionCall9.ts`** -> AI Confidence: **99.29%**
873. **`tests/cases/compiler/generatorES6_5.ts`** -> AI Confidence: **99.29%**
874. **`tests/cases/compiler/homomorphicMappedTypeIntersectionAssignability.ts`** -> AI Confidence: **99.29%**
875. **`tests/cases/compiler/ifStatementInternalComments.ts`** -> AI Confidence: **99.29%**
876. **`tests/cases/compiler/inKeywordTypeguard.ts`** -> AI Confidence: **99.29%**
877. **`tests/cases/compiler/initializedDestructuringAssignmentTypes.ts`** -> AI Confidence: **99.29%**
878. **`tests/cases/compiler/instanceofWithPrimitiveUnion.ts`** -> AI Confidence: **99.29%**
879. **`tests/cases/compiler/iteratorsAndStrictNullChecks.ts`** -> AI Confidence: **99.29%**
880. **`tests/cases/compiler/jsFileCompilationLetBeingRenamed.ts`** -> AI Confidence: **99.29%**
881. **`tests/cases/compiler/jsFileCompilationOptionalParameter.ts`** -> AI Confidence: **99.29%**
882. **`tests/cases/compiler/jsxNestedWithinTernaryParsesCorrectly.tsx`** -> AI Confidence: **99.29%**
883. **`tests/cases/compiler/letConstInCaseClauses.ts`** -> AI Confidence: **99.29%**
884. **`tests/cases/compiler/letDeclarations-es5.ts`** -> AI Confidence: **99.29%**
885. **`tests/cases/compiler/letDeclarations.ts`** -> AI Confidence: **99.29%**
886. **`tests/cases/compiler/letInLetConstDeclOfForOfAndForIn_ES5.ts`** -> AI Confidence: **99.29%**
887. **`tests/cases/compiler/letInLetConstDeclOfForOfAndForIn_ES6.ts`** -> AI Confidence: **99.29%**
888. **`tests/cases/compiler/missingCloseParenStatements.ts`** -> AI Confidence: **99.29%**
889. **`tests/cases/compiler/modularizeLibrary_Dom.iterable.ts`** -> AI Confidence: **99.29%**
890. **`tests/cases/compiler/modularizeLibrary_Worker.iterable.ts`** -> AI Confidence: **99.29%**
891. **`tests/cases/compiler/narrowByClauseExpressionInSwitchTrue10.ts`** -> AI Confidence: **99.29%**
892. **`tests/cases/compiler/narrowByClauseExpressionInSwitchTrue2.ts`** -> AI Confidence: **99.29%**
893. **`tests/cases/compiler/narrowByClauseExpressionInSwitchTrue4.ts`** -> AI Confidence: **99.29%**
894. **`tests/cases/compiler/narrowByClauseExpressionInSwitchTrue6.ts`** -> AI Confidence: **99.29%**
895. **`tests/cases/compiler/narrowByClauseExpressionInSwitchTrue7.ts`** -> AI Confidence: **99.29%**
896. **`tests/cases/compiler/narrowByClauseExpressionInSwitchTrue8.ts`** -> AI Confidence: **99.29%**
897. **`tests/cases/compiler/narrowSwitchOptionalChainContainmentEvolvingArrayNoCrash1.ts`** -> AI Confidence: **99.29%**
898. **`tests/cases/compiler/narrowUnknownByTypeofObject.ts`** -> AI Confidence: **99.29%**
899. **`tests/cases/compiler/narrowingOrderIndependent.ts`** -> AI Confidence: **99.29%**
900. **`tests/cases/compiler/narrowingTruthyObject.ts`** -> AI Confidence: **99.29%**
901. **`tests/cases/compiler/narrowingTypeofParenthesized1.ts`** -> AI Confidence: **99.29%**
902. **`tests/cases/compiler/narrowingTypeofUndefined1.ts`** -> AI Confidence: **99.29%**
903. **`tests/cases/compiler/narrowingWithNonNullExpression.ts`** -> AI Confidence: **99.29%**
904. **`tests/cases/compiler/nestedBlockScopedBindings1.ts`** -> AI Confidence: **99.29%**
905. **`tests/cases/compiler/nestedBlockScopedBindings10.ts`** -> AI Confidence: **99.29%**
906. **`tests/cases/compiler/nestedBlockScopedBindings15.ts`** -> AI Confidence: **99.29%**
907. **`tests/cases/compiler/nestedIfStatement.ts`** -> AI Confidence: **99.29%**
908. **`tests/cases/compiler/neverNullishThroughParentheses.ts`** -> AI Confidence: **99.29%**
909. **`tests/cases/compiler/noCatchBlock.ts`** -> AI Confidence: **99.29%**
910. **`tests/cases/compiler/noUnusedLocals_writeOnly.ts`** -> AI Confidence: **99.29%**
911. **`tests/cases/compiler/normalizedIntersectionTooComplex.ts`** -> AI Confidence: **99.29%**
912. **`tests/cases/compiler/objectLiteralPropertyImplicitlyAny.ts`** -> AI Confidence: **99.29%**
913. **`tests/cases/compiler/omittedExpressionForOfLoop.ts`** -> AI Confidence: **99.29%**
914. **`tests/cases/compiler/overloadingStaticFunctionsInFunctions.ts`** -> AI Confidence: **99.29%**
915. **`tests/cases/compiler/parenthesizedJSDocCastDoesNotNarrow.ts`** -> AI Confidence: **99.29%**
916. **`tests/cases/compiler/parseInvalidNullableTypes.ts`** -> AI Confidence: **99.29%**
917. **`tests/cases/compiler/potentiallyUnassignedVariableInCatch.ts`** -> AI Confidence: **99.29%**
918. **`tests/cases/compiler/predicateSemantics.ts`** -> AI Confidence: **99.29%**
919. **`tests/cases/compiler/prettyContextNotDebugAssertion.ts`** -> AI Confidence: **99.29%**
920. **`tests/cases/compiler/propertyAccessExpressionInnerComments.ts`** -> AI Confidence: **99.29%**
921. **`tests/cases/compiler/reachabilityChecks8.ts`** -> AI Confidence: **99.29%**
922. **`tests/cases/compiler/redeclareParameterInCatchBlock.ts`** -> AI Confidence: **99.29%**
923. **`tests/cases/compiler/regularExpressionAnnexB.ts`** -> AI Confidence: **99.29%**
924. **`tests/cases/compiler/regularExpressionGroupNameSuggestions.ts`** -> AI Confidence: **99.29%**
925. **`tests/cases/compiler/regularExpressionScanning.ts`** -> AI Confidence: **99.29%**
926. **`tests/cases/compiler/regularExpressionWithNonBMPFlags.ts`** -> AI Confidence: **99.29%**
927. **`tests/cases/compiler/requiredInitializedParameter1.ts`** -> AI Confidence: **99.29%**
928. **`tests/cases/compiler/restParamAsOptional.ts`** -> AI Confidence: **99.29%**
929. **`tests/cases/compiler/restParameters.ts`** -> AI Confidence: **99.29%**
930. **`tests/cases/compiler/restParamsWithNonRestParams.ts`** -> AI Confidence: **99.29%**
931. **`tests/cases/compiler/scopingInCatchBlocks.ts`** -> AI Confidence: **99.29%**
932. **`tests/cases/compiler/selfReferencingSpreadInLoop.ts`** -> AI Confidence: **99.29%**
933. **`tests/cases/compiler/sourceMap-SkippedNode.ts`** -> AI Confidence: **99.29%**
934. **`tests/cases/compiler/sourceMapValidationDestructuringForArrayBindingPattern.ts`** -> AI Confidence: **99.29%**
935. **`tests/cases/compiler/sourceMapValidationDestructuringForArrayBindingPattern2.ts`** -> AI Confidence: **99.29%**
936. **`tests/cases/compiler/sourceMapValidationDestructuringForObjectBindingPattern2.ts`** -> AI Confidence: **99.29%**
937. **`tests/cases/compiler/sourceMapValidationDestructuringForObjectBindingPatternDefaultValues2.ts`** -> AI Confidence: **99.29%**
938. **`tests/cases/compiler/sourceMapValidationDestructuringForOfArrayBindingPattern.ts`** -> AI Confidence: **99.29%**
939. **`tests/cases/compiler/sourceMapValidationDestructuringForOfArrayBindingPattern2.ts`** -> AI Confidence: **99.29%**
940. **`tests/cases/compiler/sourceMapValidationDestructuringForOfObjectBindingPattern2.ts`** -> AI Confidence: **99.29%**
941. **`tests/cases/compiler/sourceMapValidationDestructuringForOfObjectBindingPatternDefaultValues2.ts`** -> AI Confidence: **99.29%**
942. **`tests/cases/compiler/sourceMapValidationDo.ts`** -> AI Confidence: **99.29%**
943. **`tests/cases/compiler/sourceMapValidationFor.ts`** -> AI Confidence: **99.29%**
944. **`tests/cases/compiler/sourceMapValidationIfElse.ts`** -> AI Confidence: **99.29%**
945. **`tests/cases/compiler/sourceMapValidationSwitch.ts`** -> AI Confidence: **99.29%**
946. **`tests/cases/compiler/sourceMapValidationTryCatchFinally.ts`** -> AI Confidence: **99.29%**
947. **`tests/cases/compiler/staticsInAFunction.ts`** -> AI Confidence: **99.29%**
948. **`tests/cases/compiler/strictNullEmptyDestructuring.ts`** -> AI Confidence: **99.29%**
949. **`tests/cases/compiler/strictNullLogicalAndOr.ts`** -> AI Confidence: **99.29%**
950. **`tests/cases/compiler/strictOptionalProperties1.ts`** -> AI Confidence: **99.29%**
951. **`tests/cases/compiler/switchCaseCircularRefeference.ts`** -> AI Confidence: **99.29%**
952. **`tests/cases/compiler/switchCaseInternalComments.ts`** -> AI Confidence: **99.29%**
953. **`tests/cases/compiler/switchCases.ts`** -> AI Confidence: **99.29%**
954. **`tests/cases/compiler/switchCasesExpressionTypeMismatch.ts`** -> AI Confidence: **99.29%**
955. **`tests/cases/compiler/switchStatementsWithMultipleDefaults.ts`** -> AI Confidence: **99.29%**
956. **`tests/cases/compiler/switchStatementsWithMultipleDefaults1.ts`** -> AI Confidence: **99.29%**
957. **`tests/cases/compiler/truthinessCallExpressionCoercion2.ts`** -> AI Confidence: **99.29%**
958. **`tests/cases/compiler/tryCatchFinally.ts`** -> AI Confidence: **99.29%**
959. **`tests/cases/compiler/tryStatementInternalComments.ts`** -> AI Confidence: **99.29%**
960. **`tests/cases/compiler/typeGuardConstructorClassAndNumber.ts`** -> AI Confidence: **99.29%**
961. **`tests/cases/compiler/typeGuardConstructorNarrowAny.ts`** -> AI Confidence: **99.29%**
962. **`tests/cases/compiler/typeGuardConstructorNarrowPrimitivesInUnion.ts`** -> AI Confidence: **99.29%**
963. **`tests/cases/compiler/typeGuardConstructorPrimitiveTypes.ts`** -> AI Confidence: **99.29%**
964. **`tests/cases/compiler/typeGuardNarrowsIndexedAccessOfKnownProperty2.ts`** -> AI Confidence: **99.29%**
965. **`tests/cases/compiler/typeGuardNarrowsIndexedAccessOfKnownProperty5.ts`** -> AI Confidence: **99.29%**
966. **`tests/cases/compiler/uncalledFunctionChecksInConditional2.ts`** -> AI Confidence: **99.29%**
967. **`tests/cases/compiler/uncalledFunctionChecksInConditionalPerf.ts`** -> AI Confidence: **99.29%**
968. **`tests/cases/compiler/underscoreTest1.ts`** -> AI Confidence: **99.29%**
969. **`tests/cases/compiler/unionRelationshipCheckPasses.ts`** -> AI Confidence: **99.29%**
970. **`tests/cases/compiler/unusedParameterInCatchClause.ts`** -> AI Confidence: **99.29%**
971. **`tests/cases/compiler/unusedSwitchStatement.ts`** -> AI Confidence: **99.29%**
972. **`tests/cases/compiler/unusedVariablesWithUnderscoreInForOfLoop.ts`** -> AI Confidence: **99.29%**
973. **`tests/cases/compiler/unusedVariablesinForLoop2.ts`** -> AI Confidence: **99.29%**
974. **`tests/cases/compiler/unusedVariablesinForLoop3.ts`** -> AI Confidence: **99.29%**
975. **`tests/cases/compiler/useUnknownInCatchVariables01.ts`** -> AI Confidence: **99.29%**
976. **`tests/cases/compiler/voidAsOperator.ts`** -> AI Confidence: **99.29%**
977. **`tests/cases/compiler/voidIsInitialized.ts`** -> AI Confidence: **99.29%**
978. **`tests/cases/compiler/webworkerIterable.ts`** -> AI Confidence: **99.29%**
979. **`tests/cases/compiler/whileStatementInnerComments.ts`** -> AI Confidence: **99.29%**
980. **`tests/cases/compiler/yieldExpressionInFlowLoop.ts`** -> AI Confidence: **99.29%**
981. **`tests/cases/conformance/controlFlow/controlFlowAliasing.ts`** -> AI Confidence: **99.29%**
982. **`tests/cases/conformance/controlFlow/controlFlowAliasingCatchVariables.ts`** -> AI Confidence: **99.29%**
983. **`tests/cases/conformance/controlFlow/controlFlowBinaryAndExpression.ts`** -> AI Confidence: **99.29%**
984. **`tests/cases/conformance/controlFlow/controlFlowCommaOperator.ts`** -> AI Confidence: **99.29%**
985. **`tests/cases/conformance/controlFlow/controlFlowComputedPropertyNames.ts`** -> AI Confidence: **99.29%**
986. **`tests/cases/conformance/controlFlow/controlFlowConditionalExpression.ts`** -> AI Confidence: **99.29%**
987. **`tests/cases/conformance/controlFlow/controlFlowDeleteOperator.ts`** -> AI Confidence: **99.29%**
988. **`tests/cases/conformance/controlFlow/controlFlowDestructuringDeclaration.ts`** -> AI Confidence: **99.29%**
989. **`tests/cases/conformance/controlFlow/controlFlowDoWhileStatement.ts`** -> AI Confidence: **99.29%**
990. **`tests/cases/conformance/controlFlow/controlFlowElementAccess.ts`** -> AI Confidence: **99.29%**
991. **`tests/cases/conformance/controlFlow/controlFlowForInStatement.ts`** -> AI Confidence: **99.29%**
992. **`tests/cases/conformance/controlFlow/controlFlowForOfStatement.ts`** -> AI Confidence: **99.29%**
993. **`tests/cases/conformance/controlFlow/controlFlowForStatement.ts`** -> AI Confidence: **99.29%**
994. **`tests/cases/conformance/controlFlow/controlFlowInstanceOfGuardPrimitives.ts`** -> AI Confidence: **99.29%**
995. **`tests/cases/conformance/controlFlow/controlFlowIteration.ts`** -> AI Confidence: **99.29%**
996. **`tests/cases/conformance/controlFlow/controlFlowNoIntermediateErrors.ts`** -> AI Confidence: **99.29%**
997. **`tests/cases/conformance/controlFlow/controlFlowNullishCoalesce.ts`** -> AI Confidence: **99.29%**
998. **`tests/cases/conformance/controlFlow/controlFlowOptionalChain.ts`** -> AI Confidence: **99.29%**
999. **`tests/cases/conformance/controlFlow/controlFlowOptionalChain3.tsx`** -> AI Confidence: **99.29%**
1000. **`tests/cases/conformance/controlFlow/controlFlowTruthiness.ts`** -> AI Confidence: **99.29%**
1001. **`tests/cases/conformance/controlFlow/controlFlowWhileStatement.ts`** -> AI Confidence: **99.29%**
1002. **`tests/cases/conformance/controlFlow/definiteAssignmentAssertionsWithObjectShortHand.ts`** -> AI Confidence: **99.29%**
1003. **`tests/cases/conformance/controlFlow/switchWithConstrainedTypeVariable.ts`** -> AI Confidence: **99.29%**
1004. **`tests/cases/conformance/controlFlow/typeGuardsTypeParameters.ts`** -> AI Confidence: **99.29%**
1005. **`tests/cases/conformance/emitter/es2019/noCatchBinding/emitter.noCatchBinding.es2019.ts`** -> AI Confidence: **99.29%**
1006. **`tests/cases/conformance/es2016/es2016IntlAPIs.ts`** -> AI Confidence: **99.29%**
1007. **`tests/cases/conformance/es2018/usePromiseFinally.ts`** -> AI Confidence: **99.29%**
1008. **`tests/cases/conformance/es2018/useRegexpGroups.ts`** -> AI Confidence: **99.29%**
1009. **`tests/cases/conformance/es2021/logicalAssignment/logicalAssignment4.ts`** -> AI Confidence: **99.29%**
1010. **`tests/cases/conformance/es2021/logicalAssignment/logicalAssignment6.ts`** -> AI Confidence: **99.29%**
1011. **`tests/cases/conformance/es2021/logicalAssignment/logicalAssignment7.ts`** -> AI Confidence: **99.29%**
1012. **`tests/cases/conformance/es2021/logicalAssignment/logicalAssignment8.ts`** -> AI Confidence: **99.29%**
1013. **`tests/cases/conformance/es2021/logicalAssignment/logicalAssignment9.ts`** -> AI Confidence: **99.29%**
1014. **`tests/cases/conformance/es6/Symbols/symbolType1.ts`** -> AI Confidence: **99.29%**
1015. **`tests/cases/conformance/es6/Symbols/symbolType11.ts`** -> AI Confidence: **99.29%**
1016. **`tests/cases/conformance/es6/destructuring/destructuringCatch.ts`** -> AI Confidence: **99.29%**
1017. **`tests/cases/conformance/es6/destructuring/destructuringControlFlow.ts`** -> AI Confidence: **99.29%**
1018. **`tests/cases/conformance/es6/destructuring/destructuringObjectBindingPatternAndAssignment9SiblingInitializer.ts`** -> AI Confidence: **99.29%**
1019. **`tests/cases/conformance/es6/destructuring/destructuringParameterDeclaration6.ts`** -> AI Confidence: **99.29%**
1020. **`tests/cases/conformance/es6/destructuring/destructuringParameterDeclaration8.ts`** -> AI Confidence: **99.29%**
1021. **`tests/cases/conformance/es6/destructuring/optionalBindingParameters1.ts`** -> AI Confidence: **99.29%**
1022. **`tests/cases/conformance/es6/destructuring/optionalBindingParameters2.ts`** -> AI Confidence: **99.29%**
1023. **`tests/cases/conformance/es6/destructuring/optionalBindingParametersInOverloads1.ts`** -> AI Confidence: **99.29%**
1024. **`tests/cases/conformance/es6/destructuring/optionalBindingParametersInOverloads2.ts`** -> AI Confidence: **99.29%**
1025. **`tests/cases/conformance/es6/for-ofStatements/for-of-excess-declarations.ts`** -> AI Confidence: **99.29%**
1026. **`tests/cases/conformance/es6/for-ofStatements/for-of2.ts`** -> AI Confidence: **99.29%**
1027. **`tests/cases/conformance/es6/for-ofStatements/for-of5.ts`** -> AI Confidence: **99.29%**
1028. **`tests/cases/conformance/es6/for-ofStatements/for-of51.ts`** -> AI Confidence: **99.29%**
1029. **`tests/cases/conformance/es6/for-ofStatements/for-of52.ts`** -> AI Confidence: **99.29%**
1030. **`tests/cases/conformance/es6/for-ofStatements/for-of55.ts`** -> AI Confidence: **99.29%**
1031. **`tests/cases/conformance/es6/for-ofStatements/for-of6.ts`** -> AI Confidence: **99.29%**
1032. **`tests/cases/conformance/es6/for-ofStatements/for-of7.ts`** -> AI Confidence: **99.29%**
1033. **`tests/cases/conformance/es6/newTarget/newTargetNarrowing.ts`** -> AI Confidence: **99.29%**
1034. **`tests/cases/conformance/es6/templates/templateStringInSwitchAndCase.ts`** -> AI Confidence: **99.29%**
1035. **`tests/cases/conformance/es6/templates/templateStringInSwitchAndCaseES6.ts`** -> AI Confidence: **99.29%**
1036. **`tests/cases/conformance/es6/templates/templateStringInWhile.ts`** -> AI Confidence: **99.29%**
1037. **`tests/cases/conformance/es6/templates/templateStringInWhileES6.ts`** -> AI Confidence: **99.29%**
1038. **`tests/cases/conformance/esnext/logicalAssignment/logicalAssignment11.ts`** -> AI Confidence: **99.29%**
1039. **`tests/cases/conformance/expressions/binaryOperators/logicalAndOperator/logicalAndOperatorStrictMode.ts`** -> AI Confidence: **99.29%**
1040. **`tests/cases/conformance/expressions/nullishCoalescingOperator/nullishCoalescingOperator12.ts`** -> AI Confidence: **99.29%**
1041. **`tests/cases/conformance/expressions/nullishCoalescingOperator/nullishCoalescingOperator5.ts`** -> AI Confidence: **99.29%**
1042. **`tests/cases/conformance/expressions/nullishCoalescingOperator/nullishCoalescingOperator6.ts`** -> AI Confidence: **99.29%**
1043. **`tests/cases/conformance/expressions/nullishCoalescingOperator/nullishCoalescingOperator7.ts`** -> AI Confidence: **99.29%**
1044. **`tests/cases/conformance/expressions/nullishCoalescingOperator/nullishCoalescingOperator8.ts`** -> AI Confidence: **99.29%**
1045. **`tests/cases/conformance/expressions/nullishCoalescingOperator/nullishCoalescingOperatorInAsyncGenerator.ts`** -> AI Confidence: **99.29%**
1046. **`tests/cases/conformance/expressions/nullishCoalescingOperator/nullishCoalescingOperator_es2020.ts`** -> AI Confidence: **99.29%**
1047. **`tests/cases/conformance/expressions/optionalChaining/callChain/callChain.3.ts`** -> AI Confidence: **99.29%**
1048. **`tests/cases/conformance/expressions/optionalChaining/delete/deleteChain.ts`** -> AI Confidence: **99.29%**
1049. **`tests/cases/conformance/expressions/optionalChaining/elementAccessChain/elementAccessChain.3.ts`** -> AI Confidence: **99.29%**
1050. **`tests/cases/conformance/expressions/optionalChaining/elementAccessChain/elementAccessChain.ts`** -> AI Confidence: **99.29%**
1051. **`tests/cases/conformance/expressions/optionalChaining/optionalChainingInLoop.ts`** -> AI Confidence: **99.29%**
1052. **`tests/cases/conformance/expressions/optionalChaining/optionalChainingInTypeAssertions.ts`** -> AI Confidence: **99.29%**
1053. **`tests/cases/conformance/expressions/optionalChaining/propertyAccessChain/propertyAccessChain.3.ts`** -> AI Confidence: **99.29%**
1054. **`tests/cases/conformance/expressions/propertyAccess/propertyAccessWidening.ts`** -> AI Confidence: **99.29%**
1055. **`tests/cases/conformance/expressions/typeGuards/typeGuardNesting.ts`** -> AI Confidence: **99.29%**
1056. **`tests/cases/conformance/expressions/typeGuards/typeGuardOfFormTypeOfPrimitiveSubtype.ts`** -> AI Confidence: **99.29%**
1057. **`tests/cases/conformance/expressions/typeGuards/typeGuardTautologicalConsistiency.ts`** -> AI Confidence: **99.29%**
1058. **`tests/cases/conformance/expressions/typeGuards/typeGuardTypeOfUndefined.ts`** -> AI Confidence: **99.29%**
1059. **`tests/cases/conformance/expressions/typeGuards/typeGuardsInDoStatement.ts`** -> AI Confidence: **99.29%**
1060. **`tests/cases/conformance/expressions/typeGuards/typeGuardsInForStatement.ts`** -> AI Confidence: **99.29%**
1061. **`tests/cases/conformance/expressions/typeGuards/typeGuardsInWhileStatement.ts`** -> AI Confidence: **99.29%**
1062. **`tests/cases/conformance/expressions/typeGuards/typeGuardsWithAny.ts`** -> AI Confidence: **99.29%**
1063. **`tests/cases/conformance/functions/functionOverloadErrorsSyntax.ts`** -> AI Confidence: **99.29%**
1064. **`tests/cases/conformance/jsdoc/declarations/jsDeclarationsOptionalTypeLiteralProps2.ts`** -> AI Confidence: **99.29%**
1065. **`tests/cases/conformance/jsdoc/jsdocBindingInUnreachableCode.ts`** -> AI Confidence: **99.29%**
1066. **`tests/cases/conformance/jsdoc/jsdocCatchClauseWithTypeAnnotation.ts`** -> AI Confidence: **99.29%**
1067. **`tests/cases/conformance/jsdoc/thisPrototypeMethodCompoundAssignment.ts`** -> AI Confidence: **99.29%**
1068. **`tests/cases/conformance/jsdoc/thisPrototypeMethodCompoundAssignmentJs.ts`** -> AI Confidence: **99.29%**
1069. **`tests/cases/conformance/jsdoc/typedefOnStatements.ts`** -> AI Confidence: **99.29%**
1070. **`tests/cases/conformance/parser/ecmascript5/ArrowFunctionExpressions/parserArrowFunctionExpression7.ts`** -> AI Confidence: **99.29%**
1071. **`tests/cases/conformance/parser/ecmascript5/CatchClauses/parserCatchClauseWithTypeAnnotation1.ts`** -> AI Confidence: **99.29%**
1072. **`tests/cases/conformance/parser/ecmascript5/ErrorRecovery/SwitchStatements/parserErrorRecovery_SwitchStatement1.ts`** -> AI Confidence: **99.29%**
1073. **`tests/cases/conformance/parser/ecmascript5/ErrorRecovery/parserFuzz1.ts`** -> AI Confidence: **99.29%**
1074. **`tests/cases/conformance/parser/ecmascript5/ErrorRecovery/parserPublicBreak1.ts`** -> AI Confidence: **99.29%**
1075. **`tests/cases/conformance/parser/ecmascript5/Expressions/parserConditionalExpression1.ts`** -> AI Confidence: **99.29%**
1076. **`tests/cases/conformance/parser/ecmascript5/Generics/parserConstructorAmbiguity4.ts`** -> AI Confidence: **99.29%**
1077. **`tests/cases/conformance/parser/ecmascript5/MissingTokens/parserMissingToken1.ts`** -> AI Confidence: **99.29%**
1078. **`tests/cases/conformance/parser/ecmascript5/RegressionTests/parserTernaryAndCommaOperators1.ts`** -> AI Confidence: **99.29%**
1079. **`tests/cases/conformance/parser/ecmascript5/RegularExpressions/parserRegularExpression1.ts`** -> AI Confidence: **99.29%**
1080. **`tests/cases/conformance/parser/ecmascript5/RegularExpressions/parserRegularExpression3.ts`** -> AI Confidence: **99.29%**
1081. **`tests/cases/conformance/parser/ecmascript5/RegularExpressions/parserRegularExpression4.ts`** -> AI Confidence: **99.29%**
1082. **`tests/cases/conformance/parser/ecmascript5/RegularExpressions/parserRegularExpression5.ts`** -> AI Confidence: **99.29%**
1083. **`tests/cases/conformance/parser/ecmascript5/RegularExpressions/parserRegularExpressionDivideAmbiguity3.ts`** -> AI Confidence: **99.29%**
1084. **`tests/cases/conformance/parser/ecmascript5/Statements/BreakStatements/parser_breakInIterationOrSwitchStatement1.ts`** -> AI Confidence: **99.29%**
1085. **`tests/cases/conformance/parser/ecmascript5/Statements/BreakStatements/parser_breakInIterationOrSwitchStatement2.ts`** -> AI Confidence: **99.29%**
1086. **`tests/cases/conformance/parser/ecmascript5/Statements/BreakStatements/parser_breakInIterationOrSwitchStatement3.ts`** -> AI Confidence: **99.29%**
1087. **`tests/cases/conformance/parser/ecmascript5/Statements/BreakStatements/parser_breakNotInIterationOrSwitchStatement1.ts`** -> AI Confidence: **99.29%**
1088. **`tests/cases/conformance/parser/ecmascript5/Statements/BreakStatements/parser_breakNotInIterationOrSwitchStatement2.ts`** -> AI Confidence: **99.29%**
1089. **`tests/cases/conformance/parser/ecmascript5/Statements/BreakStatements/parser_breakTarget1.ts`** -> AI Confidence: **99.29%**
1090. **`tests/cases/conformance/parser/ecmascript5/Statements/BreakStatements/parser_breakTarget2.ts`** -> AI Confidence: **99.29%**
1091. **`tests/cases/conformance/parser/ecmascript5/Statements/BreakStatements/parser_breakTarget3.ts`** -> AI Confidence: **99.29%**
1092. **`tests/cases/conformance/parser/ecmascript5/Statements/BreakStatements/parser_breakTarget4.ts`** -> AI Confidence: **99.29%**
1093. **`tests/cases/conformance/parser/ecmascript5/Statements/BreakStatements/parser_breakTarget5.ts`** -> AI Confidence: **99.29%**
1094. **`tests/cases/conformance/parser/ecmascript5/Statements/BreakStatements/parser_breakTarget6.ts`** -> AI Confidence: **99.29%**
1095. **`tests/cases/conformance/parser/ecmascript5/Statements/ContinueStatements/parser_continueInIterationStatement1.ts`** -> AI Confidence: **99.29%**
1096. **`tests/cases/conformance/parser/ecmascript5/Statements/ContinueStatements/parser_continueInIterationStatement2.ts`** -> AI Confidence: **99.29%**
1097. **`tests/cases/conformance/parser/ecmascript5/Statements/ContinueStatements/parser_continueInIterationStatement3.ts`** -> AI Confidence: **99.29%**
1098. **`tests/cases/conformance/parser/ecmascript5/Statements/ContinueStatements/parser_continueNotInIterationStatement1.ts`** -> AI Confidence: **99.29%**
1099. **`tests/cases/conformance/parser/ecmascript5/Statements/ContinueStatements/parser_continueNotInIterationStatement2.ts`** -> AI Confidence: **99.29%**
1100. **`tests/cases/conformance/parser/ecmascript5/Statements/ContinueStatements/parser_continueNotInIterationStatement3.ts`** -> AI Confidence: **99.29%**
1101. **`tests/cases/conformance/parser/ecmascript5/Statements/ContinueStatements/parser_continueTarget1.ts`** -> AI Confidence: **99.29%**
1102. **`tests/cases/conformance/parser/ecmascript5/Statements/ContinueStatements/parser_continueTarget2.ts`** -> AI Confidence: **99.29%**
1103. **`tests/cases/conformance/parser/ecmascript5/Statements/ContinueStatements/parser_continueTarget3.ts`** -> AI Confidence: **99.29%**
1104. **`tests/cases/conformance/parser/ecmascript5/Statements/ContinueStatements/parser_continueTarget4.ts`** -> AI Confidence: **99.29%**
1105. **`tests/cases/conformance/parser/ecmascript5/Statements/ContinueStatements/parser_continueTarget5.ts`** -> AI Confidence: **99.29%**
1106. **`tests/cases/conformance/parser/ecmascript5/Statements/ContinueStatements/parser_continueTarget6.ts`** -> AI Confidence: **99.29%**
1107. **`tests/cases/conformance/parser/ecmascript5/Statements/LabeledStatements/parser_duplicateLabel1.ts`** -> AI Confidence: **99.29%**
1108. **`tests/cases/conformance/parser/ecmascript5/Statements/LabeledStatements/parser_duplicateLabel2.ts`** -> AI Confidence: **99.29%**
1109. **`tests/cases/conformance/parser/ecmascript5/Statements/LabeledStatements/parser_duplicateLabel3.ts`** -> AI Confidence: **99.29%**
1110. **`tests/cases/conformance/parser/ecmascript5/Statements/LabeledStatements/parser_duplicateLabel4.ts`** -> AI Confidence: **99.29%**
1111. **`tests/cases/conformance/parser/ecmascript5/Statements/parserBreakStatement1.d.ts`** -> AI Confidence: **99.29%**
1112. **`tests/cases/conformance/parser/ecmascript5/Statements/parserContinueStatement1.d.ts`** -> AI Confidence: **99.29%**
1113. **`tests/cases/conformance/parser/ecmascript5/Statements/parserDoStatement1.d.ts`** -> AI Confidence: **99.29%**
1114. **`tests/cases/conformance/parser/ecmascript5/Statements/parserDoStatement2.ts`** -> AI Confidence: **99.29%**
1115. **`tests/cases/conformance/parser/ecmascript5/Statements/parserES5ForOfStatement10.ts`** -> AI Confidence: **99.29%**
1116. **`tests/cases/conformance/parser/ecmascript5/Statements/parserES5ForOfStatement11.ts`** -> AI Confidence: **99.29%**
1117. **`tests/cases/conformance/parser/ecmascript5/Statements/parserES5ForOfStatement12.ts`** -> AI Confidence: **99.29%**
1118. **`tests/cases/conformance/parser/ecmascript5/Statements/parserES5ForOfStatement13.ts`** -> AI Confidence: **99.29%**
1119. **`tests/cases/conformance/parser/ecmascript5/Statements/parserES5ForOfStatement14.ts`** -> AI Confidence: **99.29%**
1120. **`tests/cases/conformance/parser/ecmascript5/Statements/parserES5ForOfStatement9.ts`** -> AI Confidence: **99.29%**
1121. **`tests/cases/conformance/parser/ecmascript5/Statements/parserForInStatement8.ts`** -> AI Confidence: **99.29%**
1122. **`tests/cases/conformance/parser/ecmascript5/Statements/parserForStatement3.ts`** -> AI Confidence: **99.29%**
1123. **`tests/cases/conformance/parser/ecmascript5/Statements/parserForStatement9.ts`** -> AI Confidence: **99.29%**
1124. **`tests/cases/conformance/parser/ecmascript5/StrictMode/parserStrictMode13.ts`** -> AI Confidence: **99.29%**
1125. **`tests/cases/conformance/parser/ecmascript5/parserOptionalTypeMembers1.ts`** -> AI Confidence: **99.29%**
1126. **`tests/cases/conformance/parser/ecmascript5/parserParenthesizedVariableAndFunctionInTernary.ts`** -> AI Confidence: **99.29%**
1127. **`tests/cases/conformance/parser/ecmascript5/parserParenthesizedVariableAndParenthesizedFunctionInTernary.ts`** -> AI Confidence: **99.29%**
1128. **`tests/cases/conformance/parser/ecmascript5/parserRealSource13.ts`** -> AI Confidence: **99.29%**
1129. **`tests/cases/conformance/parser/ecmascript5/parserSbp_7.9_A9_T3.ts`** -> AI Confidence: **99.29%**
1130. **`tests/cases/conformance/parser/ecmascript6/Iterators/parserForOfStatement10.ts`** -> AI Confidence: **99.29%**
1131. **`tests/cases/conformance/parser/ecmascript6/Iterators/parserForOfStatement11.ts`** -> AI Confidence: **99.29%**
1132. **`tests/cases/conformance/parser/ecmascript6/Iterators/parserForOfStatement12.ts`** -> AI Confidence: **99.29%**
1133. **`tests/cases/conformance/parser/ecmascript6/Iterators/parserForOfStatement13.ts`** -> AI Confidence: **99.29%**
1134. **`tests/cases/conformance/parser/ecmascript6/Iterators/parserForOfStatement14.ts`** -> AI Confidence: **99.29%**
1135. **`tests/cases/conformance/parser/ecmascript6/Iterators/parserForOfStatement25.ts`** -> AI Confidence: **99.29%**
1136. **`tests/cases/conformance/salsa/circularMultipleAssignmentDeclaration.ts`** -> AI Confidence: **99.29%**
1137. **`tests/cases/conformance/salsa/plainJSTypeErrors.ts`** -> AI Confidence: **99.29%**
1138. **`tests/cases/conformance/salsa/typeFromJSConstructor.ts`** -> AI Confidence: **99.29%**
1139. **`tests/cases/conformance/salsa/typeFromPropertyAssignment36.ts`** -> AI Confidence: **99.29%**
1140. **`tests/cases/conformance/statements/breakStatements/doWhileBreakStatements.ts`** -> AI Confidence: **99.29%**
1141. **`tests/cases/conformance/statements/breakStatements/forBreakStatements.ts`** -> AI Confidence: **99.29%**
1142. **`tests/cases/conformance/statements/breakStatements/invalidDoWhileBreakStatements.ts`** -> AI Confidence: **99.29%**
1143. **`tests/cases/conformance/statements/breakStatements/invalidSwitchBreakStatement.ts`** -> AI Confidence: **99.29%**
1144. **`tests/cases/conformance/statements/breakStatements/switchBreakStatements.ts`** -> AI Confidence: **99.29%**
1145. **`tests/cases/conformance/statements/breakStatements/whileBreakStatements.ts`** -> AI Confidence: **99.29%**
1146. **`tests/cases/conformance/statements/continueStatements/doWhileContinueStatements.ts`** -> AI Confidence: **99.29%**
1147. **`tests/cases/conformance/statements/continueStatements/forContinueStatements.ts`** -> AI Confidence: **99.29%**
1148. **`tests/cases/conformance/statements/continueStatements/invalidDoWhileContinueStatements.ts`** -> AI Confidence: **99.29%**
1149. **`tests/cases/conformance/statements/continueStatements/invalidSwitchContinueStatement.ts`** -> AI Confidence: **99.29%**
1150. **`tests/cases/conformance/statements/continueStatements/whileContinueStatements.ts`** -> AI Confidence: **99.29%**
1151. **`tests/cases/conformance/statements/for-inStatements/for-inStatementsArray.ts`** -> AI Confidence: **99.29%**
1152. **`tests/cases/conformance/statements/for-ofStatements/ES5For-of12.ts`** -> AI Confidence: **99.29%**
1153. **`tests/cases/conformance/statements/for-ofStatements/ES5For-of18.ts`** -> AI Confidence: **99.29%**
1154. **`tests/cases/conformance/statements/for-ofStatements/ES5For-of19.ts`** -> AI Confidence: **99.29%**
1155. **`tests/cases/conformance/statements/for-ofStatements/ES5For-of20.ts`** -> AI Confidence: **99.29%**
1156. **`tests/cases/conformance/statements/for-ofStatements/ES5For-of21.ts`** -> AI Confidence: **99.29%**
1157. **`tests/cases/conformance/statements/for-ofStatements/ES5For-of28.ts`** -> AI Confidence: **99.29%**
1158. **`tests/cases/conformance/statements/for-ofStatements/ES5For-of29.ts`** -> AI Confidence: **99.29%**
1159. **`tests/cases/conformance/statements/for-ofStatements/ES5For-of35.ts`** -> AI Confidence: **99.29%**
1160. **`tests/cases/conformance/statements/for-ofStatements/ES5For-of36.ts`** -> AI Confidence: **99.29%**
1161. **`tests/cases/conformance/statements/for-ofStatements/ES5For-of37.ts`** -> AI Confidence: **99.29%**
1162. **`tests/cases/conformance/statements/for-ofStatements/ES5For-ofTypeCheck12.ts`** -> AI Confidence: **99.29%**
1163. **`tests/cases/conformance/statements/for-ofStatements/ES5For-ofTypeCheck13.ts`** -> AI Confidence: **99.29%**
1164. **`tests/cases/conformance/statements/tryStatements/catchClauseWithTypeAnnotation.ts`** -> AI Confidence: **99.29%**
1165. **`tests/cases/conformance/statements/tryStatements/invalidTryStatements.ts`** -> AI Confidence: **99.29%**
1166. **`tests/cases/conformance/statements/tryStatements/tryStatements.ts`** -> AI Confidence: **99.29%**
1167. **`tests/cases/conformance/types/intersection/intersectionNarrowing.ts`** -> AI Confidence: **99.29%**
1168. **`tests/cases/conformance/types/literal/literalTypes1.ts`** -> AI Confidence: **99.29%**
1169. **`tests/cases/conformance/types/literal/literalTypes3.ts`** -> AI Confidence: **99.29%**
1170. **`tests/cases/conformance/types/literal/stringLiteralsWithSwitchStatements03.ts`** -> AI Confidence: **99.29%**
1171. **`tests/cases/conformance/types/literal/stringLiteralsWithSwitchStatements04.ts`** -> AI Confidence: **99.29%**
1172. **`tests/cases/conformance/types/objectTypeLiteral/callSignatures/callSignaturesWithOptionalParameters2.ts`** -> AI Confidence: **99.29%**
1173. **`tests/cases/conformance/types/rest/objectRestCatchES5.ts`** -> AI Confidence: **99.29%**
1174. **`tests/cases/conformance/types/spread/objectSpreadRepeatedComplexity.ts`** -> AI Confidence: **99.29%**
1175. **`tests/cases/conformance/types/spread/objectSpreadRepeatedNullCheckPerf.ts`** -> AI Confidence: **99.29%**
1176. **`tests/cases/conformance/types/stringLiteral/stringLiteralTypesInUnionTypes04.ts`** -> AI Confidence: **99.29%**
1177. **`tests/cases/conformance/types/typeRelationships/comparable/equalityStrictNulls.ts`** -> AI Confidence: **99.29%**
1178. **`tests/cases/conformance/types/typeRelationships/comparable/equalityWithEnumTypes.ts`** -> AI Confidence: **99.29%**
1179. **`tests/cases/conformance/types/typeRelationships/comparable/equalityWithtNullishCoalescingAssignment.ts`** -> AI Confidence: **99.29%**
1180. **`tests/cases/conformance/types/union/unionTypeCallSignatures3.ts`** -> AI Confidence: **99.29%**
1181. **`tests/cases/fourslash/addMemberInDeclarationFile.ts`** -> AI Confidence: **99.29%**
1182. **`tests/cases/fourslash/codeFixAddConvertToUnknownForNonOverlappingTypes1.ts`** -> AI Confidence: **99.29%**
1183. **`tests/cases/fourslash/codeFixAddConvertToUnknownForNonOverlappingTypes2.ts`** -> AI Confidence: **99.29%**
1184. **`tests/cases/fourslash/codeFixAddConvertToUnknownForNonOverlappingTypes3.ts`** -> AI Confidence: **99.29%**
1185. **`tests/cases/fourslash/codeFixAddConvertToUnknownForNonOverlappingTypes4.ts`** -> AI Confidence: **99.29%**
1186. **`tests/cases/fourslash/codeFixAddConvertToUnknownForNonOverlappingTypes5.ts`** -> AI Confidence: **99.29%**
1187. **`tests/cases/fourslash/codeFixAddConvertToUnknownForNonOverlappingTypes6.ts`** -> AI Confidence: **99.29%**
1188. **`tests/cases/fourslash/codeFixAddConvertToUnknownForNonOverlappingTypes7.ts`** -> AI Confidence: **99.29%**
1189. **`tests/cases/fourslash/codeFixAddConvertToUnknownForNonOverlappingTypes8.ts`** -> AI Confidence: **99.29%**
1190. **`tests/cases/fourslash/codeFixAddMissingConstInForInLoop1.ts`** -> AI Confidence: **99.29%**
1191. **`tests/cases/fourslash/codeFixAddMissingConstInForInLoop2.ts`** -> AI Confidence: **99.29%**
1192. **`tests/cases/fourslash/codeFixAddMissingConstInForLoopWithArrayDestructuring1.ts`** -> AI Confidence: **99.29%**
1193. **`tests/cases/fourslash/codeFixAddMissingConstInForLoopWithArrayDestructuring2.ts`** -> AI Confidence: **99.29%**
1194. **`tests/cases/fourslash/codeFixAddMissingConstInForLoopWithObjectDestructuring1.ts`** -> AI Confidence: **99.29%**
1195. **`tests/cases/fourslash/codeFixAddMissingConstInForLoopWithObjectDestructuring2.ts`** -> AI Confidence: **99.29%**
1196. **`tests/cases/fourslash/codeFixAddMissingConstInForOfLoop1.ts`** -> AI Confidence: **99.29%**
1197. **`tests/cases/fourslash/codeFixAddMissingConstInForOfLoop2.ts`** -> AI Confidence: **99.29%**
1198. **`tests/cases/fourslash/codeFixAddOptionalParam1.ts`** -> AI Confidence: **99.29%**
1199. **`tests/cases/fourslash/codeFixAddOptionalParam10.ts`** -> AI Confidence: **99.29%**
1200. **`tests/cases/fourslash/codeFixAddOptionalParam16.ts`** -> AI Confidence: **99.29%**
1201. **`tests/cases/fourslash/codeFixAddOptionalParam2.ts`** -> AI Confidence: **99.29%**
1202. **`tests/cases/fourslash/codeFixAddOptionalParam3.ts`** -> AI Confidence: **99.29%**
1203. **`tests/cases/fourslash/codeFixAddOptionalParam4.ts`** -> AI Confidence: **99.29%**
1204. **`tests/cases/fourslash/codeFixAddOptionalParam5.ts`** -> AI Confidence: **99.29%**
1205. **`tests/cases/fourslash/codeFixAddOptionalParam7.ts`** -> AI Confidence: **99.29%**
1206. **`tests/cases/fourslash/codeFixAddOptionalParam8.ts`** -> AI Confidence: **99.29%**
1207. **`tests/cases/fourslash/codeFixAddOptionalParam9.ts`** -> AI Confidence: **99.29%**
1208. **`tests/cases/fourslash/codeFixAddOptionalParam_all.ts`** -> AI Confidence: **99.29%**
1209. **`tests/cases/fourslash/codeFixChangeJSDocSyntax1.ts`** -> AI Confidence: **99.29%**
1210. **`tests/cases/fourslash/codeFixChangeJSDocSyntax10.ts`** -> AI Confidence: **99.29%**
1211. **`tests/cases/fourslash/codeFixChangeJSDocSyntax11.ts`** -> AI Confidence: **99.29%**
1212. **`tests/cases/fourslash/codeFixChangeJSDocSyntax14.ts`** -> AI Confidence: **99.29%**
1213. **`tests/cases/fourslash/codeFixChangeJSDocSyntax18.ts`** -> AI Confidence: **99.29%**
1214. **`tests/cases/fourslash/codeFixChangeJSDocSyntax19.ts`** -> AI Confidence: **99.29%**
1215. **`tests/cases/fourslash/codeFixChangeJSDocSyntax27.ts`** -> AI Confidence: **99.29%**
1216. **`tests/cases/fourslash/codeFixChangeJSDocSyntax28.ts`** -> AI Confidence: **99.29%**
1217. **`tests/cases/fourslash/codeFixChangeJSDocSyntax5.ts`** -> AI Confidence: **99.29%**
1218. **`tests/cases/fourslash/codeFixChangeJSDocSyntax6.ts`** -> AI Confidence: **99.29%**
1219. **`tests/cases/fourslash/codeFixConstToLet3.ts`** -> AI Confidence: **99.29%**
1220. **`tests/cases/fourslash/codeFixDeleteUnmatchedParameterJS1.ts`** -> AI Confidence: **99.29%**
1221. **`tests/cases/fourslash/codeFixDeleteUnmatchedParameterJS2.ts`** -> AI Confidence: **99.29%**
1222. **`tests/cases/fourslash/codeFixDeleteUnmatchedParameterJS3.ts`** -> AI Confidence: **99.29%**
1223. **`tests/cases/fourslash/codeFixDeleteUnmatchedParameterJS4.ts`** -> AI Confidence: **99.29%**
1224. **`tests/cases/fourslash/codeFixDisableJsDiagnosticsInFile8.ts`** -> AI Confidence: **99.29%**
1225. **`tests/cases/fourslash/codeFixInferFromUsageConstructorFunctionJS.ts`** -> AI Confidence: **99.29%**
1226. **`tests/cases/fourslash/codeFixInferFromUsageEmptyTypePriority.ts`** -> AI Confidence: **99.29%**
1227. **`tests/cases/fourslash/codeFixInferFromUsageOptionalParam.ts`** -> AI Confidence: **99.29%**
1228. **`tests/cases/fourslash/codeFixInferFromUsageOptionalParam2.ts`** -> AI Confidence: **99.29%**
1229. **`tests/cases/fourslash/codeFixInferFromUsageUnifyAnonymousType.ts`** -> AI Confidence: **99.29%**
1230. **`tests/cases/fourslash/codeFixRenameUnmatchedParameterJS1.ts`** -> AI Confidence: **99.29%**
1231. **`tests/cases/fourslash/codeFixRenameUnmatchedParameterJS2.ts`** -> AI Confidence: **99.29%**
1232. **`tests/cases/fourslash/codeFixRenameUnmatchedParameterJS3.ts`** -> AI Confidence: **99.29%**
1233. **`tests/cases/fourslash/codeFixSpellingPrivatePropertyName.ts`** -> AI Confidence: **99.29%**
1234. **`tests/cases/fourslash/codeFixSpellingPrivatePropertyNameNotInScope.ts`** -> AI Confidence: **99.29%**
1235. **`tests/cases/fourslash/codeFixSpellingPropertyNameStartsWithHash.ts`** -> AI Confidence: **99.29%**
1236. **`tests/cases/fourslash/codeFixSpellingVsMissingMember.ts`** -> AI Confidence: **99.29%**
1237. **`tests/cases/fourslash/codeFixSpelling_optionalChain.ts`** -> AI Confidence: **99.29%**
1238. **`tests/cases/fourslash/codeFixUnreachableCode_if.ts`** -> AI Confidence: **99.29%**
1239. **`tests/cases/fourslash/codeFixUnusedIdentifier_destructure_allUnused_for.ts`** -> AI Confidence: **99.29%**
1240. **`tests/cases/fourslash/codeFixUnusedIdentifier_destructuring_elements2.ts`** -> AI Confidence: **99.29%**
1241. **`tests/cases/fourslash/codeFixUnusedIdentifier_destructuring_elements3.ts`** -> AI Confidence: **99.29%**
1242. **`tests/cases/fourslash/codeFixUnusedIdentifier_destructuring_elements4.ts`** -> AI Confidence: **99.29%**
1243. **`tests/cases/fourslash/codeFixUnusedIdentifier_destructuring_elements5.ts`** -> AI Confidence: **99.29%**
1244. **`tests/cases/fourslash/codeFixUnusedIdentifier_destructuring_elements6.ts`** -> AI Confidence: **99.29%**
1245. **`tests/cases/fourslash/codeFixUnusedIdentifier_parameter1.ts`** -> AI Confidence: **99.29%**
1246. **`tests/cases/fourslash/codeFixUnusedIdentifier_parameter2.ts`** -> AI Confidence: **99.29%**
1247. **`tests/cases/fourslash/codeFixUnusedIdentifier_parameter3.ts`** -> AI Confidence: **99.29%**
1248. **`tests/cases/fourslash/codeFixUnusedIdentifier_parameter4.ts`** -> AI Confidence: **99.29%**
1249. **`tests/cases/fourslash/codeFixUnusedIdentifier_parameter5.ts`** -> AI Confidence: **99.29%**
1250. **`tests/cases/fourslash/codeFixUnusedIdentifier_parameter6.ts`** -> AI Confidence: **99.29%**
1251. **`tests/cases/fourslash/codeFixUnusedIdentifier_parameterInGetAccessor.ts`** -> AI Confidence: **99.29%**
1252. **`tests/cases/fourslash/codeFixUnusedIdentifier_super2.ts`** -> AI Confidence: **99.29%**
1253. **`tests/cases/fourslash/codeFixUnusedIdentifier_typeParameter1.ts`** -> AI Confidence: **99.29%**
1254. **`tests/cases/fourslash/codeFixUnusedIdentifier_typeParameter2.ts`** -> AI Confidence: **99.29%**
1255. **`tests/cases/fourslash/codeFixUnusedIdentifier_typeParameter3.ts`** -> AI Confidence: **99.29%**
1256. **`tests/cases/fourslash/codeFixUnusedIdentifier_typeParameter4.ts`** -> AI Confidence: **99.29%**
1257. **`tests/cases/fourslash/codeFixUnusedIdentifier_typeParameter5.ts`** -> AI Confidence: **99.29%**
1258. **`tests/cases/fourslash/codeFixUnusedLabel.ts`** -> AI Confidence: **99.29%**
1259. **`tests/cases/fourslash/codeFixUnusedLabel_all.ts`** -> AI Confidence: **99.29%**
1260. **`tests/cases/fourslash/codeFixWrapDecoratorInParentheses01.ts`** -> AI Confidence: **99.29%**
1261. **`tests/cases/fourslash/completionAfterQuestionDot.ts`** -> AI Confidence: **99.29%**
1262. **`tests/cases/fourslash/completionAutoInsertQuestionDot.ts`** -> AI Confidence: **99.29%**
1263. **`tests/cases/fourslash/completionListAtEndOfWordInArrowFunction02.ts`** -> AI Confidence: **99.29%**
1264. **`tests/cases/fourslash/completionListAtEndOfWordInArrowFunction03.ts`** -> AI Confidence: **99.29%**
1265. **`tests/cases/fourslash/completionListInNestedNamespaceName.ts`** -> AI Confidence: **99.29%**
1266. **`tests/cases/fourslash/completionListInUnclosedTypeArguments.ts`** -> AI Confidence: **99.29%**
1267. **`tests/cases/fourslash/completionListInvalidMemberNames.ts`** -> AI Confidence: **99.29%**
1268. **`tests/cases/fourslash/completionOfAwaitPromise6.ts`** -> AI Confidence: **99.29%**
1269. **`tests/cases/fourslash/completionWritingSpreadLikeArgument.ts`** -> AI Confidence: **99.29%**
1270. **`tests/cases/fourslash/completionsClassPropertiesAssignment.ts`** -> AI Confidence: **99.29%**
1271. **`tests/cases/fourslash/completionsDefaultExport.ts`** -> AI Confidence: **99.29%**
1272. **`tests/cases/fourslash/completionsDefaultKeywordWhenDefaultExportAvailable.ts`** -> AI Confidence: **99.29%**
1273. **`tests/cases/fourslash/completionsImport_filteredByPackageJson_ambient.ts`** -> AI Confidence: **99.29%**
1274. **`tests/cases/fourslash/completionsIsPossiblyTypeArgumentPosition.ts`** -> AI Confidence: **99.29%**
1275. **`tests/cases/fourslash/completionsOverridingMethod9.ts`** -> AI Confidence: **99.29%**
1276. **`tests/cases/fourslash/completionsWithStringReplacementMode.ts`** -> AI Confidence: **99.29%**
1277. **`tests/cases/fourslash/declarationExpressions.ts`** -> AI Confidence: **99.29%**
1278. **`tests/cases/fourslash/docCommentTemplateFunctionExpression.ts`** -> AI Confidence: **99.29%**
1279. **`tests/cases/fourslash/docCommentTemplateInSingleLineComment.ts`** -> AI Confidence: **99.29%**
1280. **`tests/cases/fourslash/docCommentTemplateInsideFunctionDeclaration.ts`** -> AI Confidence: **99.29%**
1281. **`tests/cases/fourslash/docCommentTemplatePrototypeMethod.ts`** -> AI Confidence: **99.29%**
1282. **`tests/cases/fourslash/docCommentTemplateRegex.ts`** -> AI Confidence: **99.29%**
1283. **`tests/cases/fourslash/docCommentTemplateVariableStatements01.ts`** -> AI Confidence: **99.29%**
1284. **`tests/cases/fourslash/docCommentTemplateVariableStatements02.ts`** -> AI Confidence: **99.29%**
1285. **`tests/cases/fourslash/exhaustiveCaseCompletions1.ts`** -> AI Confidence: **99.29%**
1286. **`tests/cases/fourslash/exhaustiveCaseCompletions2.ts`** -> AI Confidence: **99.29%**
1287. **`tests/cases/fourslash/exhaustiveCaseCompletions3.ts`** -> AI Confidence: **99.29%**
1288. **`tests/cases/fourslash/exhaustiveCaseCompletions4.ts`** -> AI Confidence: **99.29%**
1289. **`tests/cases/fourslash/exhaustiveCaseCompletions5.ts`** -> AI Confidence: **99.29%**
1290. **`tests/cases/fourslash/exhaustiveCaseCompletions6.ts`** -> AI Confidence: **99.29%**
1291. **`tests/cases/fourslash/exhaustiveCaseCompletions7.ts`** -> AI Confidence: **99.29%**
1292. **`tests/cases/fourslash/exhaustiveCaseCompletions8.ts`** -> AI Confidence: **99.29%**
1293. **`tests/cases/fourslash/extract-const3.ts`** -> AI Confidence: **99.29%**
1294. **`tests/cases/fourslash/extract-method11.ts`** -> AI Confidence: **99.29%**
1295. **`tests/cases/fourslash/extract-method31.ts`** -> AI Confidence: **99.29%**
1296. **`tests/cases/fourslash/fixNaNEquality1.ts`** -> AI Confidence: **99.29%**
1297. **`tests/cases/fourslash/fixNaNEquality2.ts`** -> AI Confidence: **99.29%**
1298. **`tests/cases/fourslash/fixNaNEquality3.ts`** -> AI Confidence: **99.29%**
1299. **`tests/cases/fourslash/fixNaNEquality4.ts`** -> AI Confidence: **99.29%**
1300. **`tests/cases/fourslash/fixNaNEquality5.ts`** -> AI Confidence: **99.29%**
1301. **`tests/cases/fourslash/formatCatch.ts`** -> AI Confidence: **99.29%**
1302. **`tests/cases/fourslash/formatControlFlowConstructs.ts`** -> AI Confidence: **99.29%**
1303. **`tests/cases/fourslash/formatDebuggerStatement.ts`** -> AI Confidence: **99.29%**
1304. **`tests/cases/fourslash/formatDocumentWithTrivia.ts`** -> AI Confidence: **99.29%**
1305. **`tests/cases/fourslash/formatIfTryCatchBlocks.ts`** -> AI Confidence: **99.29%**
1306. **`tests/cases/fourslash/formatIfWithEmptyCondition.ts`** -> AI Confidence: **99.29%**
1307. **`tests/cases/fourslash/formatOnEnterOpenBraceAddNewLine.ts`** -> AI Confidence: **99.29%**
1308. **`tests/cases/fourslash/formatOnOpenCurlyBraceRemoveNewLine.ts`** -> AI Confidence: **99.29%**
1309. **`tests/cases/fourslash/formatOnSemiColonAfterBreak.ts`** -> AI Confidence: **99.29%**
1310. **`tests/cases/fourslash/formatOnTypeOpenCurlyWithBraceCompletion.ts`** -> AI Confidence: **99.29%**
1311. **`tests/cases/fourslash/formatRemoveNewLineAfterOpenBrace.ts`** -> AI Confidence: **99.29%**
1312. **`tests/cases/fourslash/formatSelectionDocCommentInBlock.ts`** -> AI Confidence: **99.29%**
1313. **`tests/cases/fourslash/formatSelectionWithTrivia.ts`** -> AI Confidence: **99.29%**
1314. **`tests/cases/fourslash/formatSelectionWithTrivia3.ts`** -> AI Confidence: **99.29%**
1315. **`tests/cases/fourslash/formatSelectionWithTrivia4.ts`** -> AI Confidence: **99.29%**
1316. **`tests/cases/fourslash/formatSelectionWithTrivia5.ts`** -> AI Confidence: **99.29%**
1317. **`tests/cases/fourslash/formatSelectionWithTrivia7.ts`** -> AI Confidence: **99.29%**
1318. **`tests/cases/fourslash/formatTryCatch.ts`** -> AI Confidence: **99.29%**
1319. **`tests/cases/fourslash/formatTryFinally.ts`** -> AI Confidence: **99.29%**
1320. **`tests/cases/fourslash/formattingDoubleLessThan.ts`** -> AI Confidence: **99.29%**
1321. **`tests/cases/fourslash/formattingElseInsideAFunction.ts`** -> AI Confidence: **99.29%**
1322. **`tests/cases/fourslash/formattingExpressionsInIfCondition.ts`** -> AI Confidence: **99.29%**
1323. **`tests/cases/fourslash/formattingForOfKeyword.ts`** -> AI Confidence: **99.29%**
1324. **`tests/cases/fourslash/formattingInMultilineComments.ts`** -> AI Confidence: **99.29%**
1325. **`tests/cases/fourslash/formattingOnNestedDoWhileByEnter.ts`** -> AI Confidence: **99.29%**
1326. **`tests/cases/fourslash/formattingOnStatementsWithNoSemicolon.ts`** -> AI Confidence: **99.29%**
1327. **`tests/cases/fourslash/formattingQMark.ts`** -> AI Confidence: **99.29%**
1328. **`tests/cases/fourslash/formattingSpaceBetweenOptionalChaining.ts`** -> AI Confidence: **99.29%**
1329. **`tests/cases/fourslash/getJavaScriptQuickInfo2.ts`** -> AI Confidence: **99.29%**
1330. **`tests/cases/fourslash/getJavaScriptQuickInfo3.ts`** -> AI Confidence: **99.29%**
1331. **`tests/cases/fourslash/getJavaScriptQuickInfo4.ts`** -> AI Confidence: **99.29%**
1332. **`tests/cases/fourslash/getJavaScriptQuickInfo5.ts`** -> AI Confidence: **99.29%**
1333. **`tests/cases/fourslash/getMatchingBraces.ts`** -> AI Confidence: **99.29%**
1334. **`tests/cases/fourslash/getMatchingBracesAdjacentBraces.ts`** -> AI Confidence: **99.29%**
1335. **`tests/cases/fourslash/importNameCodeFix_require_namedAndDefault.ts`** -> AI Confidence: **99.29%**
1336. **`tests/cases/fourslash/incompleteFunctionCallCodefixTypeParameterNarrowed.ts`** -> AI Confidence: **99.29%**
1337. **`tests/cases/fourslash/incrementalEditInvocationExpressionAboveInterfaceDeclaration.ts`** -> AI Confidence: **99.29%**
1338. **`tests/cases/fourslash/indentationInAmdIife.ts`** -> AI Confidence: **99.29%**
1339. **`tests/cases/fourslash/indentationInArrays.ts`** -> AI Confidence: **99.29%**
1340. **`tests/cases/fourslash/indentationInAssignment.ts`** -> AI Confidence: **99.29%**
1341. **`tests/cases/fourslash/indentationInAsyncExpressions.ts`** -> AI Confidence: **99.29%**
1342. **`tests/cases/fourslash/indentationInClassExpression.ts`** -> AI Confidence: **99.29%**
1343. **`tests/cases/fourslash/indentationInComments.ts`** -> AI Confidence: **99.29%**
1344. **`tests/cases/fourslash/indentationInObject.ts`** -> AI Confidence: **99.29%**
1345. **`tests/cases/fourslash/insertSecondTryCatchBlock.ts`** -> AI Confidence: **99.29%**
1346. **`tests/cases/fourslash/isInMultiLineCommentInJsxText.ts`** -> AI Confidence: **99.29%**
1347. **`tests/cases/fourslash/isInMultiLineCommentInTemplateLiteral.ts`** -> AI Confidence: **99.29%**
1348. **`tests/cases/fourslash/jsDocFunctionSignatures2.ts`** -> AI Confidence: **99.29%**
1349. **`tests/cases/fourslash/jsDocPropertyDescription11.ts`** -> AI Confidence: **99.29%**
1350. **`tests/cases/fourslash/jsDocPropertyDescription6.ts`** -> AI Confidence: **99.29%**
1351. **`tests/cases/fourslash/jsDocPropertyDescription9.ts`** -> AI Confidence: **99.29%**
1352. **`tests/cases/fourslash/jsSpecialAssignmentMerging.ts`** -> AI Confidence: **99.29%**
1353. **`tests/cases/fourslash/jsSpecialAssignmentMerging2.ts`** -> AI Confidence: **99.29%**
1354. **`tests/cases/fourslash/jsxAttributeSnippetCompletionAfterTypeArgs.ts`** -> AI Confidence: **99.29%**
1355. **`tests/cases/fourslash/jsxAttributeSnippetCompletionClosed.ts`** -> AI Confidence: **99.29%**
1356. **`tests/cases/fourslash/jsxAttributeSnippetCompletionUnclosed.ts`** -> AI Confidence: **99.29%**
1357. **`tests/cases/fourslash/mapCodeNestedForInsertion.ts`** -> AI Confidence: **99.29%**
1358. **`tests/cases/fourslash/mapCodeNestedForOfInsertion.ts`** -> AI Confidence: **99.29%**
1359. **`tests/cases/fourslash/mapCodeNestedForOfReplacement.ts`** -> AI Confidence: **99.29%**
1360. **`tests/cases/fourslash/mapCodeNestedForReplacement.ts`** -> AI Confidence: **99.29%**
1361. **`tests/cases/fourslash/mapCodeNestedIfInsertion.ts`** -> AI Confidence: **99.29%**
1362. **`tests/cases/fourslash/mapCodeNestedIfReplace.ts`** -> AI Confidence: **99.29%**
1363. **`tests/cases/fourslash/mapCodeNestedLabeledInsertion.ts`** -> AI Confidence: **99.29%**
1364. **`tests/cases/fourslash/mapCodeNestedLabeledReplace.ts`** -> AI Confidence: **99.29%**
1365. **`tests/cases/fourslash/mapCodeNestedWhileInsertion.ts`** -> AI Confidence: **99.29%**
1366. **`tests/cases/fourslash/mapCodeNestedWhileReplace.ts`** -> AI Confidence: **99.29%**
1367. **`tests/cases/fourslash/multilineCommentBeforeOpenBrace.ts`** -> AI Confidence: **99.29%**
1368. **`tests/cases/fourslash/navigateItemsConst.ts`** -> AI Confidence: **99.29%**
1369. **`tests/cases/fourslash/navigateItemsExports.ts`** -> AI Confidence: **99.29%**
1370. **`tests/cases/fourslash/navigateItemsImports.ts`** -> AI Confidence: **99.29%**
1371. **`tests/cases/fourslash/navigationItemsComputedProperties.ts`** -> AI Confidence: **99.29%**
1372. **`tests/cases/fourslash/navigationItemsExactMatch.ts`** -> AI Confidence: **99.29%**
1373. **`tests/cases/fourslash/navigationItemsPrefixMatch.ts`** -> AI Confidence: **99.29%**
1374. **`tests/cases/fourslash/navigationItemsSubStringMatch.ts`** -> AI Confidence: **99.29%**
1375. **`tests/cases/fourslash/pathCompletionsPackageJsonExportsBundlerNoNodeCondition.ts`** -> AI Confidence: **99.29%**
1376. **`tests/cases/fourslash/pathCompletionsPackageJsonImportsBundlerNoNodeCondition.ts`** -> AI Confidence: **99.29%**
1377. **`tests/cases/fourslash/preserveSpace.ts`** -> AI Confidence: **99.29%**
1378. **`tests/cases/fourslash/quickInfoDisplayPartsIife.ts`** -> AI Confidence: **99.29%**
1379. **`tests/cases/fourslash/quickInfoForContextuallyTypedArrowFunctionInSuperCall.ts`** -> AI Confidence: **99.29%**
1380. **`tests/cases/fourslash/quickInfoForContextuallyTypedFunctionInTaggedTemplateExpression1.ts`** -> AI Confidence: **99.29%**
1381. **`tests/cases/fourslash/quickInfoForObjectBindingElementPropertyName03.ts`** -> AI Confidence: **99.29%**
1382. **`tests/cases/fourslash/quickInfoInOptionalChain.ts`** -> AI Confidence: **99.29%**
1383. **`tests/cases/fourslash/quickInfoJsDocNonDiscriminatedUnionSharedProp.ts`** -> AI Confidence: **99.29%**
1384. **`tests/cases/fourslash/quickInfoOnElementAccessInWriteLocation1.ts`** -> AI Confidence: **99.29%**
1385. **`tests/cases/fourslash/quickInfoOnElementAccessInWriteLocation2.ts`** -> AI Confidence: **99.29%**
1386. **`tests/cases/fourslash/quickInfoOnElementAccessInWriteLocation3.ts`** -> AI Confidence: **99.29%**
1387. **`tests/cases/fourslash/quickInfoOnPropertyAccessInWriteLocation1.ts`** -> AI Confidence: **99.29%**
1388. **`tests/cases/fourslash/quickInfoOnPropertyAccessInWriteLocation2.ts`** -> AI Confidence: **99.29%**
1389. **`tests/cases/fourslash/quickInfoOnPropertyAccessInWriteLocation3.ts`** -> AI Confidence: **99.29%**
1390. **`tests/cases/fourslash/refactorConvertParamsToDestructuredObject_restParamInference.ts`** -> AI Confidence: **99.29%**
1391. **`tests/cases/fourslash/refactorConvertParamsToDestructuredObject_shorthandProperty.ts`** -> AI Confidence: **99.29%**
1392. **`tests/cases/fourslash/refactorConvertParamsToDestructuredObject_templateLiteral.ts`** -> AI Confidence: **99.29%**
1393. **`tests/cases/fourslash/refactorConvertParamsToDestructuredObject_tupleRestParam.ts`** -> AI Confidence: **99.29%**
1394. **`tests/cases/fourslash/refactorConvertParamsToDestructuredObject_typedRestParam.ts`** -> AI Confidence: **99.29%**
1395. **`tests/cases/fourslash/refactorConvertStringOrTemplateLiteral_TemplateString13.ts`** -> AI Confidence: **99.29%**
1396. **`tests/cases/fourslash/refactorConvertToOptionalChainExpression_AccessThenCall.ts`** -> AI Confidence: **99.29%**
1397. **`tests/cases/fourslash/refactorConvertToOptionalChainExpression_BinaryExpression.ts`** -> AI Confidence: **99.29%**
1398. **`tests/cases/fourslash/refactorConvertToOptionalChainExpression_BinaryExpressionPartialSpan.ts`** -> AI Confidence: **99.29%**
1399. **`tests/cases/fourslash/refactorConvertToOptionalChainExpression_ComparisonOperator.ts`** -> AI Confidence: **99.29%**
1400. **`tests/cases/fourslash/refactorConvertToOptionalChainExpression_ConditionalInitialIdentifier.ts`** -> AI Confidence: **99.29%**
1401. **`tests/cases/fourslash/refactorConvertToOptionalChainExpression_ConditionalPartialSPan.ts`** -> AI Confidence: **99.29%**
1402. **`tests/cases/fourslash/refactorConvertToOptionalChainExpression_ConditionalWithBinaryCondition1.ts`** -> AI Confidence: **99.29%**
1403. **`tests/cases/fourslash/refactorConvertToOptionalChainExpression_ElementAccessExpression1.ts`** -> AI Confidence: **99.29%**
1404. **`tests/cases/fourslash/refactorConvertToOptionalChainExpression_ElementAccessExpression2.ts`** -> AI Confidence: **99.29%**
1405. **`tests/cases/fourslash/refactorConvertToOptionalChainExpression_EmptySpanBinaryExpression.ts`** -> AI Confidence: **99.29%**
1406. **`tests/cases/fourslash/refactorConvertToOptionalChainExpression_EmptySpanCallArgument.ts`** -> AI Confidence: **99.29%**
1407. **`tests/cases/fourslash/refactorConvertToOptionalChainExpression_EmptySpanConditional.ts`** -> AI Confidence: **99.29%**
1408. **`tests/cases/fourslash/refactorConvertToOptionalChainExpression_EmptySpanVarKeyword.ts`** -> AI Confidence: **99.29%**
1409. **`tests/cases/fourslash/refactorConvertToOptionalChainExpression_EmptySpanVariableStatementBinary.ts`** -> AI Confidence: **99.29%**
1410. **`tests/cases/fourslash/refactorConvertToOptionalChainExpression_EmptySpanVariableStatementConditional.ts`** -> AI Confidence: **99.29%**
1411. **`tests/cases/fourslash/refactorConvertToOptionalChainExpression_InFunctionCall.ts`** -> AI Confidence: **99.29%**
1412. **`tests/cases/fourslash/refactorConvertToOptionalChainExpression_InIfStatement.ts`** -> AI Confidence: **99.29%**
1413. **`tests/cases/fourslash/refactorConvertToOptionalChainExpression_NoInitialIdentifier.ts`** -> AI Confidence: **99.29%**
1414. **`tests/cases/fourslash/refactorConvertToOptionalChainExpression_SemicolonNotSelected.ts`** -> AI Confidence: **99.29%**
1415. **`tests/cases/fourslash/refactorConvertToOptionalChainExpression_SparseAccess.ts`** -> AI Confidence: **99.29%**
1416. **`tests/cases/fourslash/refactorConvertToOptionalChainExpression_SubexpressionWithPrefix1.ts`** -> AI Confidence: **99.29%**
1417. **`tests/cases/fourslash/refactorConvertToOptionalChainExpression_SubexpressionWithSuffix1.ts`** -> AI Confidence: **99.29%**
1418. **`tests/cases/fourslash/refactorConvertToOptionalChainExpression_SubexpressionWithSuffix2.ts`** -> AI Confidence: **99.29%**
1419. **`tests/cases/fourslash/refactorConvertToOptionalChainExpression_SubexpressionsWithPrefix2.ts`** -> AI Confidence: **99.29%**
1420. **`tests/cases/fourslash/renameDefaultKeyword.ts`** -> AI Confidence: **99.29%**
1421. **`tests/cases/fourslash/server/brace01.ts`** -> AI Confidence: **99.29%**
1422. **`tests/cases/fourslash/server/formatBracketInSwitchCase.ts`** -> AI Confidence: **99.29%**
1423. **`tests/cases/fourslash/server/navto01.ts`** -> AI Confidence: **99.29%**
1424. **`tests/cases/fourslash/signatureHelpFilteredTriggers01.ts`** -> AI Confidence: **99.29%**
1425. **`tests/cases/fourslash/signatureHelpFilteredTriggers02.ts`** -> AI Confidence: **99.29%**
1426. **`tests/cases/fourslash/signatureHelpForNonlocalTypeDoesNotUseImportType.ts`** -> AI Confidence: **99.29%**
1427. **`tests/cases/fourslash/signatureHelpWithTriggers01.ts`** -> AI Confidence: **99.29%**
1428. **`tests/cases/fourslash/smartIndentReturn.ts`** -> AI Confidence: **99.29%**
1429. **`tests/cases/fourslash/spaceAfterStatementConditions.ts`** -> AI Confidence: **99.29%**
1430. **`tests/cases/fourslash/stringCompletionsUnterminated.ts`** -> AI Confidence: **99.29%**
1431. **`tests/cases/fourslash/stringCompletionsUnterminated2.ts`** -> AI Confidence: **99.29%**
1432. **`tests/cases/fourslash/switchIndenting.ts`** -> AI Confidence: **99.29%**
1433. **`tests/cases/fourslash/textChangesPreserveNewlines9.ts`** -> AI Confidence: **99.29%**
1434. **`tests/cases/fourslash/tsxQuickInfo4.ts`** -> AI Confidence: **99.29%**
1435. **`tests/cases/fourslash/tsxQuickInfo7.ts`** -> AI Confidence: **99.29%**
1436. **`tests/cases/fourslash/unusedLabelAfterEdit.ts`** -> AI Confidence: **99.29%**
1437. **`tests/cases/fourslash/unusedMethodInClass4.ts`** -> AI Confidence: **99.29%**
1438. **`tests/cases/fourslash/unusedParameterInFunction1.ts`** -> AI Confidence: **99.29%**
1439. **`tests/cases/fourslash/unusedParameterInFunction2.ts`** -> AI Confidence: **99.29%**
1440. **`tests/cases/fourslash/unusedTypeParametersInFunction2.ts`** -> AI Confidence: **99.29%**
1441. **`tests/cases/fourslash/unusedTypeParametersInLambda2.ts`** -> AI Confidence: **99.29%**
1442. **`tests/cases/fourslash/unusedTypeParametersInLambda3.ts`** -> AI Confidence: **99.29%**
1443. **`tests/cases/fourslash/unusedTypeParametersInMethod2.ts`** -> AI Confidence: **99.29%**
1444. **`tests/cases/fourslash/unusedTypeParametersInMethods1.ts`** -> AI Confidence: **99.29%**
1445. **`tests/cases/fourslash/unusedVariableInBlocks.ts`** -> AI Confidence: **99.29%**
1446. **`tests/cases/fourslash/unusedVariableInClass1.ts`** -> AI Confidence: **99.29%**
1447. **`tests/cases/fourslash/unusedVariableInClass2.ts`** -> AI Confidence: **99.29%**
1448. **`tests/cases/fourslash/unusedVariableInClass3.ts`** -> AI Confidence: **99.29%**
1449. **`tests/cases/fourslash/unusedVariableInClass4.ts`** -> AI Confidence: **99.29%**
1450. **`tests/cases/fourslash/unusedVariableInForLoop1FS.ts`** -> AI Confidence: **99.29%**
1451. **`tests/cases/fourslash/unusedVariableInForLoop5FSAddUnderscore.ts`** -> AI Confidence: **99.29%**
1452. **`tests/cases/fourslash/unusedVariableInForLoop6FS.ts`** -> AI Confidence: **99.29%**
1453. **`tests/cases/fourslash/unusedVariableInForLoop6FSAddUnderscore.ts`** -> AI Confidence: **99.29%**
1454. **`tests/cases/fourslash/unusedVariableInForLoop7FS.ts`** -> AI Confidence: **99.29%**
1455. **`tests/cases/fourslash/unusedVariableInNamespace1.ts`** -> AI Confidence: **99.29%**
1456. **`tests/cases/fourslash/unusedVariableInNamespace2.ts`** -> AI Confidence: **99.29%**
1457. **`tests/cases/fourslash/unusedVariableInNamespace3.ts`** -> AI Confidence: **99.29%**
1458. **`tests/cases/fourslash/whiteSpaceTrimming.ts`** -> AI Confidence: **99.29%**
1459. **`tests/cases/fourslash/yieldKeywordFormatting.ts`** -> AI Confidence: **99.29%**
1460. **`src/testRunner/parallel/host.ts`** -> AI Confidence: **99.25%**
1461. **`scripts/failed-tests.cjs`** -> AI Confidence: **99.23%**
1462. **`tests/baselines/reference/tsserver/typingsInstaller/pick-typing-names-from-nonrelative-unresolved-imports.js`** -> AI Confidence: **99.23%**
1463. **`tests/baselines/reference/esModuleInteropDefaultImports.js`** -> AI Confidence: **99.2%**
1464. **`tests/baselines/reference/tsserver/resolutionCache/when-resolution-is-succeeds-in-global-typings-location-with-import-from-the-cache-file-failing-with-currentDirectory-at-root.js`** -> AI Confidence: **99.2%**
1465. **`tests/baselines/reference/tsserver/resolutionCache/when-resolution-is-succeeds-in-global-typings-location-with-import-from-the-cache-file-failing.js`** -> AI Confidence: **99.2%**
1466. **`src/services/refactors/extractSymbol.ts`** -> AI Confidence: **99.2%**
1467. **`src/testRunner/unittests/tsserver/jsdocTag.ts`** -> AI Confidence: **99.2%**
1468. **`Herebyfile.mjs`** -> AI Confidence: **99.18%**
1469. **`tests/baselines/reference/declarationFileForTsJsImport(module=node18).js`** -> AI Confidence: **99.18%**
1470. **`tests/baselines/reference/declarationFileForTsJsImport(module=node20).js`** -> AI Confidence: **99.18%**
1471. **`tests/baselines/reference/declarationFileForTsJsImport(module=nodenext).js`** -> AI Confidence: **99.18%**
1472. **`tests/baselines/reference/modulePreserve4.js`** -> AI Confidence: **99.18%**
1473. **`tests/baselines/reference/nodeModulesAllowJsConditionalPackageExports(module=node16).js`** -> AI Confidence: **99.18%**
1474. **`tests/baselines/reference/nodeModulesAllowJsConditionalPackageExports(module=node18).js`** -> AI Confidence: **99.18%**
1475. **`tests/baselines/reference/nodeModulesAllowJsConditionalPackageExports(module=node20).js`** -> AI Confidence: **99.18%**
1476. **`tests/baselines/reference/nodeModulesAllowJsConditionalPackageExports(module=nodenext).js`** -> AI Confidence: **99.18%**
1477. **`tests/baselines/reference/nodeModulesConditionalPackageExports(module=node16).js`** -> AI Confidence: **99.18%**
1478. **`tests/baselines/reference/nodeModulesConditionalPackageExports(module=node18).js`** -> AI Confidence: **99.18%**
1479. **`tests/baselines/reference/nodeModulesConditionalPackageExports(module=node20).js`** -> AI Confidence: **99.18%**
1480. **`tests/baselines/reference/nodeModulesConditionalPackageExports(module=nodenext).js`** -> AI Confidence: **99.18%**
1481. **`tests/baselines/reference/tsc/projectReferences/default-import-interop-uses-referenced-project-settings.js`** -> AI Confidence: **99.18%**
1482. **`src/harness/harnessLanguageService.ts`** -> AI Confidence: **99.18%**
1483. **`src/testRunner/unittests/helpers/monorepoSymlinkedSiblingPackages.ts`** -> AI Confidence: **99.18%**
1484. **`src/testRunner/unittests/helpers/noEmit.ts`** -> AI Confidence: **99.18%**
1485. **`src/testRunner/unittests/services/organizeImports.ts`** -> AI Confidence: **99.18%**
1486. **`src/testRunner/unittests/services/transpile.ts`** -> AI Confidence: **99.18%**
1487. **`src/testRunner/unittests/tsserver/completions.ts`** -> AI Confidence: **99.18%**
1488. **`src/testRunner/unittests/tsserver/documentRegistry.ts`** -> AI Confidence: **99.18%**
1489. **`src/testRunner/unittests/tsserver/inferredProjects.ts`** -> AI Confidence: **99.18%**
1490. **`tests/cases/fourslash/getEditsForFileRename_directory.ts`** -> AI Confidence: **99.18%**
1491. **`tests/cases/fourslash/getEditsForFileRename_directory_down.ts`** -> AI Confidence: **99.18%**
1492. **`tests/cases/fourslash/getEditsForFileRename_directory_up.ts`** -> AI Confidence: **99.18%**
1493. **`scripts/eslint/rules/js-extensions.cjs`** -> AI Confidence: **99.17%**
1494. **`tests/baselines/reference/ES5For-of35(target=es5).js`** -> AI Confidence: **99.17%**
1495. **`tests/baselines/reference/ES5For-of36(target=es5).js`** -> AI Confidence: **99.17%**
1496. **`tests/baselines/reference/ES5For-of37(target=es5).js`** -> AI Confidence: **99.17%**
1497. **`tests/baselines/reference/anonymousDefaultExportsUmd.js`** -> AI Confidence: **99.17%**
1498. **`tests/baselines/reference/asyncFunctionTempVariableScoping(target=es5).js`** -> AI Confidence: **99.17%**
1499. **`tests/baselines/reference/asyncMultiFile_es5(target=es2015).js`** -> AI Confidence: **99.17%**
1500. **`tests/baselines/reference/asyncMultiFile_es5(target=es5).js`** -> AI Confidence: **99.17%**
1501. **`tests/baselines/reference/asyncMultiFile_es6.js`** -> AI Confidence: **99.17%**
1502. **`tests/baselines/reference/blockScopedBindingsInDownlevelGenerator(target=es5).js`** -> AI Confidence: **99.17%**
1503. **`tests/baselines/reference/callSignaturesWithOptionalParameters2.js`** -> AI Confidence: **99.17%**
1504. **`tests/baselines/reference/callWithSpread2.js`** -> AI Confidence: **99.17%**
1505. **`tests/baselines/reference/classPropertyInferenceFromBroaderTypeConst.js`** -> AI Confidence: **99.17%**
1506. **`tests/baselines/reference/commentsAfterCaseClauses1.js`** -> AI Confidence: **99.17%**
1507. **`tests/baselines/reference/commentsAfterCaseClauses2.js`** -> AI Confidence: **99.17%**
1508. **`tests/baselines/reference/commentsAfterCaseClauses3.js`** -> AI Confidence: **99.17%**
1509. **`tests/baselines/reference/conditionalExpressionNewLine10.js`** -> AI Confidence: **99.17%**
1510. **`tests/baselines/reference/conditionalExpressionNewLine8.js`** -> AI Confidence: **99.17%**
1511. **`tests/baselines/reference/conditionalExpressionNewLine9.js`** -> AI Confidence: **99.17%**
1512. **`tests/baselines/reference/constDeclarations-invalidContexts(alwaysstrict=false).js`** -> AI Confidence: **99.17%**
1513. **`tests/baselines/reference/constDeclarations-invalidContexts(alwaysstrict=true).js`** -> AI Confidence: **99.17%**
1514. **`tests/baselines/reference/controlFlowAliasedDiscriminants.js`** -> AI Confidence: **99.17%**
1515. **`tests/baselines/reference/controlFlowDestructuringLoop.js`** -> AI Confidence: **99.17%**
1516. **`tests/baselines/reference/controlFlowDoWhileStatement.js`** -> AI Confidence: **99.17%**
1517. **`tests/baselines/reference/controlFlowForCompoundAssignmentToThisMember.js`** -> AI Confidence: **99.17%**
1518. **`tests/baselines/reference/controlFlowInOperator.js`** -> AI Confidence: **99.17%**
1519. **`tests/baselines/reference/controlFlowIteration.js`** -> AI Confidence: **99.17%**
1520. **`tests/baselines/reference/controlFlowNullishCoalesce.js`** -> AI Confidence: **99.17%**
1521. **`tests/baselines/reference/controlFlowTypeofObject.js`** -> AI Confidence: **99.17%**
1522. **`tests/baselines/reference/controlFlowWithIncompleteTypes.js`** -> AI Confidence: **99.17%**
1523. **`tests/baselines/reference/decoratorMetadata-jsdoc(target=es2015).js`** -> AI Confidence: **99.17%**
1524. **`tests/baselines/reference/decoratorOnClassProperty13.js`** -> AI Confidence: **99.17%**
1525. **`tests/baselines/reference/defaultExportsGetExportedUmd.js`** -> AI Confidence: **99.17%**
1526. **`tests/baselines/reference/deleteChain.js`** -> AI Confidence: **99.17%**
1527. **`tests/baselines/reference/discriminatedUnionTypes1.js`** -> AI Confidence: **99.17%**
1528. **`tests/baselines/reference/doNotElaborateAssignabilityToTypeParameters(target=es5).js`** -> AI Confidence: **99.17%**
1529. **`tests/baselines/reference/emptyAnonymousObjectNarrowing(strictnullchecks=false).js`** -> AI Confidence: **99.17%**
1530. **`tests/baselines/reference/emptyAnonymousObjectNarrowing(strictnullchecks=true).js`** -> AI Confidence: **99.17%**
1531. **`tests/baselines/reference/enumsWithMultipleDeclarations1.js`** -> AI Confidence: **99.17%**
1532. **`tests/baselines/reference/enumsWithMultipleDeclarations2.js`** -> AI Confidence: **99.17%**
1533. **`tests/baselines/reference/equalityWithIntersectionTypes01.js`** -> AI Confidence: **99.17%**
1534. **`tests/baselines/reference/equalityWithUnionTypes01.js`** -> AI Confidence: **99.17%**
1535. **`tests/baselines/reference/es5-asyncFunction(target=es5).js`** -> AI Confidence: **99.17%**
1536. **`tests/baselines/reference/es5-asyncFunctionDoStatements(target=es2015).js`** -> AI Confidence: **99.17%**
1537. **`tests/baselines/reference/es5-asyncFunctionNestedLoops(target=es2015).js`** -> AI Confidence: **99.17%**
1538. **`tests/baselines/reference/esModuleInteropImportDefaultWhenAllNamedAreDefaultAlias.js`** -> AI Confidence: **99.17%**
1539. **`tests/baselines/reference/externalModuleImmutableBindings.js`** -> AI Confidence: **99.17%**
1540. **`tests/baselines/reference/functionInIfStatementInModule.js`** -> AI Confidence: **99.17%**
1541. **`tests/baselines/reference/genericDefaults.js`** -> AI Confidence: **99.17%**
1542. **`tests/baselines/reference/impliedNodeFormatEmit1(module=umd).js`** -> AI Confidence: **99.17%**
1543. **`tests/baselines/reference/invalidContinueInDownlevelAsync.js`** -> AI Confidence: **99.17%**
1544. **`tests/baselines/reference/invalidForBreakStatements.js`** -> AI Confidence: **99.17%**
1545. **`tests/baselines/reference/invalidForContinueStatements.js`** -> AI Confidence: **99.17%**
1546. **`tests/baselines/reference/invalidWhileBreakStatements.js`** -> AI Confidence: **99.17%**
1547. **`tests/baselines/reference/invalidWhileContinueStatements.js`** -> AI Confidence: **99.17%**
1548. **`tests/baselines/reference/logicalAssignment1(target=es2015).js`** -> AI Confidence: **99.17%**
1549. **`tests/baselines/reference/logicalAssignment1(target=es2020).js`** -> AI Confidence: **99.17%**
1550. **`tests/baselines/reference/logicalAssignment1(target=es2021).js`** -> AI Confidence: **99.17%**
1551. **`tests/baselines/reference/logicalAssignment1(target=esnext).js`** -> AI Confidence: **99.17%**
1552. **`tests/baselines/reference/logicalAssignment11(target=es2015).js`** -> AI Confidence: **99.17%**
1553. **`tests/baselines/reference/logicalAssignment11(target=es2020).js`** -> AI Confidence: **99.17%**
1554. **`tests/baselines/reference/logicalAssignment11(target=esnext).js`** -> AI Confidence: **99.17%**
1555. **`tests/baselines/reference/logicalAssignment9.js`** -> AI Confidence: **99.17%**
1556. **`tests/baselines/reference/mappedTypes6.js`** -> AI Confidence: **99.17%**
1557. **`tests/baselines/reference/multipleExportDefault1.js`** -> AI Confidence: **99.17%**
1558. **`tests/baselines/reference/multipleExportDefault2.js`** -> AI Confidence: **99.17%**
1559. **`tests/baselines/reference/narrowByEquality.js`** -> AI Confidence: **99.17%**
1560. **`tests/baselines/reference/narrowingIntersection.js`** -> AI Confidence: **99.17%**
1561. **`tests/baselines/reference/nestedExcessPropertyChecking.js`** -> AI Confidence: **99.17%**
1562. **`tests/baselines/reference/noImplicitReturnsWithProtectedBlocks1.js`** -> AI Confidence: **99.17%**
1563. **`tests/baselines/reference/noImplicitReturnsWithProtectedBlocks3.js`** -> AI Confidence: **99.17%**
1564. **`tests/baselines/reference/nullishCoalescingAssignmentVsPrivateFieldsJsEmit1.js`** -> AI Confidence: **99.17%**
1565. **`tests/baselines/reference/nullishCoalescingOperatorInAsyncGenerator(target=esnext).js`** -> AI Confidence: **99.17%**
1566. **`tests/baselines/reference/objectBindingPatternKeywordIdentifiers02.js`** -> AI Confidence: **99.17%**
1567. **`tests/baselines/reference/objectBindingPatternKeywordIdentifiers04.js`** -> AI Confidence: **99.17%**
1568. **`tests/baselines/reference/optionalChainWithInstantiationExpression1(target=es2019).js`** -> AI Confidence: **99.17%**
1569. **`tests/baselines/reference/optionalChainingInLoop(target=es2015).js`** -> AI Confidence: **99.17%**
1570. **`tests/baselines/reference/parserRealSource12.js`** -> AI Confidence: **99.17%**
1571. **`tests/baselines/reference/potentiallyUnassignedVariableInCatch.js`** -> AI Confidence: **99.17%**
1572. **`tests/baselines/reference/primitiveUnionDetection.js`** -> AI Confidence: **99.17%**
1573. **`tests/baselines/reference/privateNameFieldUnaryMutation.js`** -> AI Confidence: **99.17%**
1574. **`tests/baselines/reference/privateNameInInExpression(target=es2022).js`** -> AI Confidence: **99.17%**
1575. **`tests/baselines/reference/privateNameInInExpression(target=esnext).js`** -> AI Confidence: **99.17%**
1576. **`tests/baselines/reference/promiseDefinitionTest(target=es5).js`** -> AI Confidence: **99.17%**
1577. **`tests/baselines/reference/reachabilityCheckWithEmptyDefault.js`** -> AI Confidence: **99.17%**
1578. **`tests/baselines/reference/reachabilityChecks5.js`** -> AI Confidence: **99.17%**
1579. **`tests/baselines/reference/reachabilityChecks6.js`** -> AI Confidence: **99.17%**
1580. **`tests/baselines/reference/recursiveNamedLambdaCall.js`** -> AI Confidence: **99.17%**
1581. **`tests/baselines/reference/recursiveTypeReferences2.js`** -> AI Confidence: **99.17%**
1582. **`tests/baselines/reference/requireOfJsonFileWithModuleNodeResolutionEmitUmd.js`** -> AI Confidence: **99.17%**
1583. **`tests/baselines/reference/reservedWords.js`** -> AI Confidence: **99.17%**
1584. **`tests/baselines/reference/sourceMapValidationDestructuringForArrayBindingPatternDefaultValues2(target=es5).js`** -> AI Confidence: **99.17%**
1585. **`tests/baselines/reference/sourceMapValidationDestructuringForOfObjectBindingPatternDefaultValues2(target=es5).js`** -> AI Confidence: **99.17%**
1586. **`tests/baselines/reference/strictOptionalProperties2.js`** -> AI Confidence: **99.17%**
1587. **`tests/baselines/reference/switchAssignmentCompat.js`** -> AI Confidence: **99.17%**
1588. **`tests/baselines/reference/symbolType8.js`** -> AI Confidence: **99.17%**
1589. **`tests/baselines/reference/templateStringInEqualityChecks.js`** -> AI Confidence: **99.17%**
1590. **`tests/baselines/reference/templateStringInEqualityChecksES6.js`** -> AI Confidence: **99.17%**
1591. **`tests/baselines/reference/transpile/Rename dependencies - UMD.js`** -> AI Confidence: **99.17%**
1592. **`tests/baselines/reference/tsbuild/resolveJsonModule/files-containing-json-file-non-composite.js`** -> AI Confidence: **99.17%**
1593. **`tests/baselines/reference/tsbuild/resolveJsonModule/include-and-files-non-composite.js`** -> AI Confidence: **99.17%**
1594. **`tests/baselines/reference/tsbuild/resolveJsonModule/include-of-json-along-with-other-include-and-file-name-matches-ts-file-non-composite.js`** -> AI Confidence: **99.17%**
1595. **`tests/baselines/reference/tsbuild/resolveJsonModule/include-of-json-along-with-other-include-non-composite.js`** -> AI Confidence: **99.17%**
1596. **`tests/baselines/reference/tsbuild/resolveJsonModule/include-only-non-composite.js`** -> AI Confidence: **99.17%**
1597. **`tests/baselines/reference/tsbuild/resolveJsonModule/include-only-with-json-without-rootDir-but-outside-configDirectory-non-composite.js`** -> AI Confidence: **99.17%**
1598. **`tests/baselines/reference/tsbuild/resolveJsonModule/sourcemap-non-composite.js`** -> AI Confidence: **99.17%**
1599. **`tests/baselines/reference/tsbuild/resolveJsonModule/without-outDir-non-composite.js`** -> AI Confidence: **99.17%**
1600. **`tests/baselines/reference/tscWatch/moduleResolution/package-json-file-is-edited.js`** -> AI Confidence: **99.17%**
1601. **`tests/baselines/reference/tscWatch/programUpdates/Reports-errors-when-the-config-file-changes.js`** -> AI Confidence: **99.17%**
1602. **`tests/baselines/reference/tscWatch/programUpdates/change-module-to-none.js`** -> AI Confidence: **99.17%**
1603. **`tests/baselines/reference/tscWatch/symlinks/monorepo-style-sibling-packages-symlinked-Linux.js`** -> AI Confidence: **99.17%**
1604. **`tests/baselines/reference/tscWatch/symlinks/monorepo-style-sibling-packages-symlinked-package1-built-Linux.js`** -> AI Confidence: **99.17%**
1605. **`tests/baselines/reference/tscWatch/symlinks/monorepo-style-sibling-packages-symlinked.js`** -> AI Confidence: **99.17%**
1606. **`tests/baselines/reference/tscWatch/watchApi/verify-that-module-resolution-with-json-extension-works-when-returned-without-extension.js`** -> AI Confidence: **99.17%**
1607. **`tests/baselines/reference/tsserver/autoImportProvider/Responds-to-automatic-changes-in-node_modules.js`** -> AI Confidence: **99.17%**
1608. **`tests/baselines/reference/tsserver/autoImportProvider/projects-already-inside-node_modules.js`** -> AI Confidence: **99.17%**
1609. **`tests/baselines/reference/tsserver/cachingFileSystemInformation/npm-install-works-when-timeout-occurs-after-installation.js`** -> AI Confidence: **99.17%**
1610. **`tests/baselines/reference/tsserver/cachingFileSystemInformation/npm-install-works-when-timeout-occurs-inbetween-installation.js`** -> AI Confidence: **99.17%**
1611. **`tests/baselines/reference/tsserver/cancellationT/is-attached-to-request.js`** -> AI Confidence: **99.17%**
1612. **`tests/baselines/reference/tsserver/configFileSearch/tsconfig-for-the-file-exists.js`** -> AI Confidence: **99.17%**
1613. **`tests/baselines/reference/tsserver/configuredProjects/Open-ref-of-configured-project-when-open-file-gets-added-to-the-project-as-part-of-configured-file-update-buts-its-open-file-references-are-all-closed-when-the-update-happens.js`** -> AI Confidence: **99.17%**
1614. **`tests/baselines/reference/tsserver/configuredProjects/Open-ref-of-configured-project-when-open-file-gets-added-to-the-project-as-part-of-configured-file-update.js`** -> AI Confidence: **99.17%**
1615. **`tests/baselines/reference/tsserver/configuredProjects/add-and-then-remove-a-config-file-when-parent-folder-has-config-file-and-file-from-first-config-is-not-open.js`** -> AI Confidence: **99.17%**
1616. **`tests/baselines/reference/tsserver/configuredProjects/add-and-then-remove-a-config-file-with-sibling-jsconfig-file-and-file-from-first-config-is-not-open.js`** -> AI Confidence: **99.17%**
1617. **`tests/baselines/reference/tsserver/configuredProjects/add-new-files-to-a-configured-project-without-file-list.js`** -> AI Confidence: **99.17%**
1618. **`tests/baselines/reference/tsserver/configuredProjects/can-correctly-update-configured-project-when-set-of-root-files-has-changed-(new-file-on-disk).js`** -> AI Confidence: **99.17%**
1619. **`tests/baselines/reference/tsserver/configuredProjects/should-be-tolerated-without-crashing-the-server.js`** -> AI Confidence: **99.17%**
1620. **`tests/baselines/reference/tsserver/configuredProjects/should-properly-handle-module-resolution-changes-in-config-file.js`** -> AI Confidence: **99.17%**
1621. **`tests/baselines/reference/tsserver/configuredProjects/should-tolerate-invalid-include-files-that-start-in-subDirectory.js`** -> AI Confidence: **99.17%**
1622. **`tests/baselines/reference/tsserver/documentRegistry/works-when-reusing-orphan-script-info-with-different-scriptKind.js`** -> AI Confidence: **99.17%**
1623. **`tests/baselines/reference/tsserver/externalProjects/can-handle-tsconfig-file-name-with-difference-casing-with-lazyConfiguredProjectsFromExternalProject.js`** -> AI Confidence: **99.17%**
1624. **`tests/baselines/reference/tsserver/externalProjects/can-handle-tsconfig-file-name-with-difference-casing.js`** -> AI Confidence: **99.17%**
1625. **`tests/baselines/reference/tsserver/externalProjects/correctly-handling-add-or-remove-tsconfig---1.js`** -> AI Confidence: **99.17%**
1626. **`tests/baselines/reference/tsserver/externalProjects/external-project-that-included-config-files.js`** -> AI Confidence: **99.17%**
1627. **`tests/baselines/reference/tsserver/externalProjects/language-service-disabled-state-is-updated-in-external-projects.js`** -> AI Confidence: **99.17%**
1628. **`tests/baselines/reference/tsserver/fourslashServer/autoImportCrossPackage_pathsAndSymlink.js`** -> AI Confidence: **99.17%**
1629. **`tests/baselines/reference/tsserver/fourslashServer/autoImportCrossProject_symlinks_stripSrc.js`** -> AI Confidence: **99.17%**
1630. **`tests/baselines/reference/tsserver/fourslashServer/autoImportCrossProject_symlinks_toDist.js`** -> AI Confidence: **99.17%**
1631. **`tests/baselines/reference/tsserver/fourslashServer/autoImportCrossProject_symlinks_toSrc.js`** -> AI Confidence: **99.17%**
1632. **`tests/baselines/reference/tsserver/fourslashServer/autoImportPackageJsonFilterExistingImport1.js`** -> AI Confidence: **99.17%**
1633. **`tests/baselines/reference/tsserver/fourslashServer/autoImportProvider1.js`** -> AI Confidence: **99.17%**
1634. **`tests/baselines/reference/tsserver/fourslashServer/autoImportProvider_pnpm.js`** -> AI Confidence: **99.17%**
1635. **`tests/baselines/reference/tsserver/fourslashServer/configurePlugin.js`** -> AI Confidence: **99.17%**
1636. **`tests/baselines/reference/tsserver/fourslashServer/formatSpaceBetweenFunctionAndArrayIndex.js`** -> AI Confidence: **99.17%**
1637. **`tests/baselines/reference/tsserver/fourslashServer/jsdocCallbackTagNavigateTo.js`** -> AI Confidence: **99.17%**
1638. **`tests/baselines/reference/tsserver/fourslashServer/ngProxy4.js`** -> AI Confidence: **99.17%**
1639. **`tests/baselines/reference/tsserver/fourslashServer/pathCompletionsPackageJsonImportsSrcNoDistWildcard6.js`** -> AI Confidence: **99.17%**
1640. **`tests/baselines/reference/tsserver/getMoveToRefactoringFileSuggestions/suggests-only-.ts-file-for-a-.ts-filepath.js`** -> AI Confidence: **99.17%**
1641. **`tests/baselines/reference/tsserver/inferredProjects/inferred-projects-per-project-root.js`** -> AI Confidence: **99.17%**
1642. **`tests/baselines/reference/tsserver/inferredProjects/should-support-files-without-extensions.js`** -> AI Confidence: **99.17%**
1643. **`tests/baselines/reference/tsserver/inferredProjects/should-use-only-one-inferred-project-if-useOneInferredProject-is-set.js`** -> AI Confidence: **99.17%**
1644. **`tests/baselines/reference/tsserver/languageService/should-work-correctly-on-case-sensitive-file-systems.js`** -> AI Confidence: **99.17%**
1645. **`tests/baselines/reference/tsserver/maxNodeModuleJsDepth/should-be-set-to-2-if-the-project-has-js-root-files.js`** -> AI Confidence: **99.17%**
1646. **`tests/baselines/reference/tsserver/openfile/project-root-is-used-with-case-sensitive-system.js`** -> AI Confidence: **99.17%**
1647. **`tests/baselines/reference/tsserver/openfile/uses-existing-project-even-if-project-refresh-is-pending.js`** -> AI Confidence: **99.17%**
1648. **`tests/baselines/reference/tsserver/pasteEdits/should-not-error.js`** -> AI Confidence: **99.17%**
1649. **`tests/baselines/reference/tsserver/pluginsAsync/project-is-closed-before-plugins-are-loaded.js`** -> AI Confidence: **99.17%**
1650. **`tests/baselines/reference/tsserver/projectErrors/configFileDiagnostic-events-are-not-generated-when-the-config-file-does-not-include-file-opened-and-doesnt-contain-any-errors.js`** -> AI Confidence: **99.17%**
1651. **`tests/baselines/reference/tsserver/projectErrors/configured-projects---diagnostics-for-corrupted-config-1.js`** -> AI Confidence: **99.17%**
1652. **`tests/baselines/reference/tsserver/projectErrors/configured-projects---diagnostics-for-corrupted-config-2.js`** -> AI Confidence: **99.17%**
1653. **`tests/baselines/reference/tsserver/projectErrors/when-opening-new-file-that-doesnt-exist-on-disk-yet-with-projectRoot.js`** -> AI Confidence: **99.17%**
1654. **`tests/baselines/reference/tsserver/projectErrors/when-opening-new-file-that-doesnt-exist-on-disk-yet-without-projectRoot.js`** -> AI Confidence: **99.17%**
1655. **`tests/baselines/reference/tsserver/projectReferences/disables-looking-into-the-child-project-if-disableReferencedProjectLoad-is-set.js`** -> AI Confidence: **99.17%**
1656. **`tests/baselines/reference/tsserver/projects/File-in-multiple-projects-at-opened-and-closed-correctly.js`** -> AI Confidence: **99.17%**
1657. **`tests/baselines/reference/tsserver/projects/assert-when-removing-project.js`** -> AI Confidence: **99.17%**
1658. **`tests/baselines/reference/tsserver/projects/correctly-migrate-files-between-projects.js`** -> AI Confidence: **99.17%**
1659. **`tests/baselines/reference/tsserver/projects/does-not-look-beyond-node_modules-folders-for-default-configured-projects.js`** -> AI Confidence: **99.17%**
1660. **`tests/baselines/reference/tsserver/projects/ignores-files-excluded-by-a-legacy-safe-type-list.js`** -> AI Confidence: **99.17%**
1661. **`tests/baselines/reference/tsserver/projects/js-file-opened-is-in-configured-project-that-will-be-removed.js`** -> AI Confidence: **99.17%**
1662. **`tests/baselines/reference/tsserver/projects/loading-files-with-correct-priority.js`** -> AI Confidence: **99.17%**
1663. **`tests/baselines/reference/tsserver/refactors/handles-canonicalization-of-tsconfig-path.js`** -> AI Confidence: **99.17%**
1664. **`tests/baselines/reference/tsserver/refactors/handles-moving-statements-to-a-TS-file-that-is-not-included-in-the-TS-project.js`** -> AI Confidence: **99.17%**
1665. **`tests/baselines/reference/tsserver/refactors/handles-moving-statements-to-a-non-TS-file.js`** -> AI Confidence: **99.17%**
1666. **`tests/baselines/reference/tsserver/regionDiagnostics/diagnostics-for-select-nodes-and-whole-file-for-multiple-files.js`** -> AI Confidence: **99.17%**
1667. **`tests/baselines/reference/tsserver/reload/should-work-with-temp-file.js`** -> AI Confidence: **99.17%**
1668. **`tests/baselines/reference/tsserver/rename/rename-behavior-is-based-on-file-of-rename-initiation.js`** -> AI Confidence: **99.17%**
1669. **`tests/baselines/reference/tsserver/resolutionCache/when-watching-node_modules-as-part-of-wild-card-directories-in-config-project.js`** -> AI Confidence: **99.17%**
1670. **`tests/baselines/reference/tsserver/resolutionCache/when-watching-node_modules-in-inferred-project-for-failed-lookup-closed-script-infos.js`** -> AI Confidence: **99.17%**
1671. **`tests/baselines/reference/tsserver/skipLibCheck/reports-semantic-error-in-configured-js-project-with-tscheck.js`** -> AI Confidence: **99.17%**
1672. **`tests/baselines/reference/tsserver/skipLibCheck/reports-semantic-error-in-configured-project-with-tscheck.js`** -> AI Confidence: **99.17%**
1673. **`tests/baselines/reference/tsserver/symLinks/monorepo-style-sibling-packages-symlinked-Linux-canUseWatchEvents.js`** -> AI Confidence: **99.17%**
1674. **`tests/baselines/reference/tsserver/symLinks/monorepo-style-sibling-packages-symlinked-Linux.js`** -> AI Confidence: **99.17%**
1675. **`tests/baselines/reference/tsserver/symLinks/monorepo-style-sibling-packages-symlinked-canUseWatchEvents.js`** -> AI Confidence: **99.17%**
1676. **`tests/baselines/reference/tsserver/symLinks/monorepo-style-sibling-packages-symlinked.js`** -> AI Confidence: **99.17%**
1677. **`tests/baselines/reference/tsserver/telemetry/counts-files-by-extension.js`** -> AI Confidence: **99.17%**
1678. **`tests/baselines/reference/tsserver/typingsInstaller/progress-notification.js`** -> AI Confidence: **99.17%**
1679. **`tests/baselines/reference/tsserver/typingsInstaller/should-handle-node-core-modules.js`** -> AI Confidence: **99.17%**
1680. **`tests/baselines/reference/tsserver/typingsInstaller/telemetry-events.js`** -> AI Confidence: **99.17%**
1681. **`tests/baselines/reference/tsserver/watchEnvironment/perVolumeCasing-and-new-file-addition.js`** -> AI Confidence: **99.17%**
1682. **`tests/baselines/reference/tsserver/watchEnvironment/project-with-ascii-file-names-with-i.js`** -> AI Confidence: **99.17%**
1683. **`tests/baselines/reference/tsserver/watchEnvironment/project-with-ascii-file-names.js`** -> AI Confidence: **99.17%**
1684. **`tests/baselines/reference/tsserver/watchEnvironment/project-with-unicode-file-names.js`** -> AI Confidence: **99.17%**
1685. **`tests/baselines/reference/tsxReactEmitEntities.js`** -> AI Confidence: **99.17%**
1686. **`tests/baselines/reference/typeAliasDeclarationEmit3.js`** -> AI Confidence: **99.17%**
1687. **`tests/baselines/reference/typeAnnotationBestCommonTypeInArrayLiteral.js`** -> AI Confidence: **99.17%**
1688. **`tests/baselines/reference/typeFromPrivatePropertyAssignment.js`** -> AI Confidence: **99.17%**
1689. **`tests/baselines/reference/typeGuardEnums.js`** -> AI Confidence: **99.17%**
1690. **`tests/baselines/reference/typeGuardNarrowsIndexedAccessOfKnownProperty11.js`** -> AI Confidence: **99.17%**
1691. **`tests/baselines/reference/typeGuardNarrowsIndexedAccessOfKnownProperty12.js`** -> AI Confidence: **99.17%**
1692. **`tests/baselines/reference/typeGuardOfFormNotExpr.js`** -> AI Confidence: **99.17%**
1693. **`tests/baselines/reference/typeGuardOfFormTypeOfFunction.js`** -> AI Confidence: **99.17%**
1694. **`tests/baselines/reference/typeParameterLeak.js`** -> AI Confidence: **99.17%**
1695. **`tests/baselines/reference/typePredicatesOptionalChaining1.js`** -> AI Confidence: **99.17%**
1696. **`tests/baselines/reference/typedefOnStatements.js`** -> AI Confidence: **99.17%**
1697. **`tests/baselines/reference/umdDependencyComment2.js`** -> AI Confidence: **99.17%**
1698. **`tests/baselines/reference/umdDependencyCommentName1.js`** -> AI Confidence: **99.17%**
1699. **`tests/baselines/reference/umdDependencyCommentName2.js`** -> AI Confidence: **99.17%**
1700. **`tests/baselines/reference/umdNamedAmdMode.js`** -> AI Confidence: **99.17%**
1701. **`tests/baselines/reference/uncalledFunctionChecksInConditional2.js`** -> AI Confidence: **99.17%**
1702. **`tests/baselines/reference/underscoreTest1.js`** -> AI Confidence: **99.17%**
1703. **`tests/baselines/reference/unionTypeCallSignatures3.js`** -> AI Confidence: **99.17%**
1704. **`tests/baselines/reference/unusedSwitchStatement.js`** -> AI Confidence: **99.17%**
1705. **`tests/baselines/reference/usingDeclarations.1(target=es2015).js`** -> AI Confidence: **99.17%**
1706. **`tests/baselines/reference/usingDeclarations.1(target=es2017).js`** -> AI Confidence: **99.17%**
1707. **`tests/baselines/reference/usingDeclarationsInFor(target=es2015).js`** -> AI Confidence: **99.17%**
1708. **`tests/baselines/reference/usingDeclarationsInFor(target=es2017).js`** -> AI Confidence: **99.17%**
1709. **`tests/baselines/reference/usingDeclarationsInFor(target=es2022).js`** -> AI Confidence: **99.17%**
1710. **`tests/baselines/reference/usingDeclarationsInForOf.1(target=es2015).js`** -> AI Confidence: **99.17%**
1711. **`tests/baselines/reference/usingDeclarationsInForOf.1(target=es2017).js`** -> AI Confidence: **99.17%**
1712. **`tests/baselines/reference/usingDeclarationsInForOf.1(target=es2022).js`** -> AI Confidence: **99.17%**
1713. **`tests/baselines/reference/yieldInForInInDownlevelGenerator(target=es5).js`** -> AI Confidence: **99.17%**
1714. **`src/compiler/binder.ts`** -> AI Confidence: **99.17%**
1715. **`src/compiler/semver.ts`** -> AI Confidence: **99.17%**
1716. **`src/compiler/transformers/classFields.ts`** -> AI Confidence: **99.17%**
1717. **`src/compiler/transformers/declarations/diagnostics.ts`** -> AI Confidence: **99.17%**
1718. **`src/compiler/transformers/destructuring.ts`** -> AI Confidence: **99.17%**
1719. **`src/lib/es2020.string.d.ts`** -> AI Confidence: **99.17%**
1720. **`src/lib/es2022.error.d.ts`** -> AI Confidence: **99.17%**
1721. **`src/lib/es2024.arraybuffer.d.ts`** -> AI Confidence: **99.17%**
1722. **`src/lib/es2025.intl.d.ts`** -> AI Confidence: **99.17%**
1723. **`src/lib/esnext.typedarrays.d.ts`** -> AI Confidence: **99.17%**
1724. **`src/server/typingInstallerAdapter.ts`** -> AI Confidence: **99.17%**
1725. **`src/services/codefixes/fixAddVoidToPromise.ts`** -> AI Confidence: **99.17%**
1726. **`src/services/formatting/smartIndenter.ts`** -> AI Confidence: **99.17%**
1727. **`src/services/inlayHints.ts`** -> AI Confidence: **99.17%**
1728. **`src/services/smartSelection.ts`** -> AI Confidence: **99.17%**
1729. **`src/typingsInstallerCore/typingsInstaller.ts`** -> AI Confidence: **99.17%**
1730. **`tests/baselines/reference/mapCodeNestedForInsertion.mapCode.ts`** -> AI Confidence: **99.17%**
1731. **`tests/baselines/reference/mapCodeNestedForOfInsertion.mapCode.ts`** -> AI Confidence: **99.17%**
1732. **`tests/baselines/reference/mapCodeNestedIfInsertion.mapCode.ts`** -> AI Confidence: **99.17%**
1733. **`tests/baselines/reference/mapCodeNestedLabeledReplace.mapCode.ts`** -> AI Confidence: **99.17%**
1734. **`tests/baselines/reference/mapCodeNestedWhileInsertion.mapCode.ts`** -> AI Confidence: **99.17%**
1735. **`tests/cases/compiler/ambientWithStatements.ts`** -> AI Confidence: **99.17%**
1736. **`tests/cases/compiler/blockScopedBindingsReassignedInLoop6.ts`** -> AI Confidence: **99.17%**
1737. **`tests/cases/compiler/capturedLetConstInLoop6.ts`** -> AI Confidence: **99.17%**
1738. **`tests/cases/compiler/capturedLetConstInLoop6_ES6.ts`** -> AI Confidence: **99.17%**
1739. **`tests/cases/compiler/capturedLetConstInLoop9.ts`** -> AI Confidence: **99.17%**
1740. **`tests/cases/compiler/capturedLetConstInLoop9_ES6.ts`** -> AI Confidence: **99.17%**
1741. **`tests/cases/compiler/commentsAfterCaseClauses1.ts`** -> AI Confidence: **99.17%**
1742. **`tests/cases/compiler/commentsAfterCaseClauses2.ts`** -> AI Confidence: **99.17%**
1743. **`tests/cases/compiler/commentsAfterCaseClauses3.ts`** -> AI Confidence: **99.17%**
1744. **`tests/cases/compiler/conditionalExpressionNewLine10.ts`** -> AI Confidence: **99.17%**
1745. **`tests/cases/compiler/conditionalExpressionNewLine8.ts`** -> AI Confidence: **99.17%**
1746. **`tests/cases/compiler/conditionalExpressionNewLine9.ts`** -> AI Confidence: **99.17%**
1747. **`tests/cases/compiler/conflictMarkerDiff3Trivia1.ts`** -> AI Confidence: **99.17%**
1748. **`tests/cases/compiler/conflictMarkerDiff3Trivia2.ts`** -> AI Confidence: **99.17%**
1749. **`tests/cases/compiler/constDeclarations-invalidContexts.ts`** -> AI Confidence: **99.17%**
1750. **`tests/cases/compiler/controlFlowForCompoundAssignmentToThisMember.ts`** -> AI Confidence: **99.17%**
1751. **`tests/cases/compiler/controlFlowNoImplicitAny.ts`** -> AI Confidence: **99.17%**
1752. **`tests/cases/compiler/controlFlowWithIncompleteTypes.ts`** -> AI Confidence: **99.17%**
1753. **`tests/cases/compiler/destructuringAssignmentWithExportedName.ts`** -> AI Confidence: **99.17%**
1754. **`tests/cases/compiler/destructuringTypeGuardFlow.ts`** -> AI Confidence: **99.17%**
1755. **`tests/cases/compiler/es5-asyncFunctionWhileStatements.ts`** -> AI Confidence: **99.17%**
1756. **`tests/cases/compiler/flowInFinally1.ts`** -> AI Confidence: **99.17%**
1757. **`tests/cases/compiler/invalidContinueInDownlevelAsync.ts`** -> AI Confidence: **99.17%**
1758. **`tests/cases/compiler/letDeclarations-invalidContexts.ts`** -> AI Confidence: **99.17%**
1759. **`tests/cases/compiler/nanEquality.ts`** -> AI Confidence: **99.17%**
1760. **`tests/cases/compiler/narrowByClauseExpressionInSwitchTrue5.ts`** -> AI Confidence: **99.17%**
1761. **`tests/cases/compiler/narrowingTypeofFunction.ts`** -> AI Confidence: **99.17%**
1762. **`tests/cases/compiler/narrowingUnionToNeverAssigment.ts`** -> AI Confidence: **99.17%**
1763. **`tests/cases/compiler/narrowingUnionWithBang.ts`** -> AI Confidence: **99.17%**
1764. **`tests/cases/compiler/nestedBlockScopedBindings2.ts`** -> AI Confidence: **99.17%**
1765. **`tests/cases/compiler/nestedBlockScopedBindings3.ts`** -> AI Confidence: **99.17%**
1766. **`tests/cases/compiler/nestedBlockScopedBindings5.ts`** -> AI Confidence: **99.17%**
1767. **`tests/cases/compiler/nestedBlockScopedBindings6.ts`** -> AI Confidence: **99.17%**
1768. **`tests/cases/compiler/noUnusedLocals_selfReference_skipsBlockLocations.ts`** -> AI Confidence: **99.17%**
1769. **`tests/cases/compiler/nonNullableTypes1.ts`** -> AI Confidence: **99.17%**
1770. **`tests/cases/compiler/reachabilityChecks5.ts`** -> AI Confidence: **99.17%**
1771. **`tests/cases/compiler/reachabilityChecks6.ts`** -> AI Confidence: **99.17%**
1772. **`tests/cases/compiler/reachabilityChecks9.ts`** -> AI Confidence: **99.17%**
1773. **`tests/cases/compiler/recursiveNamedLambdaCall.ts`** -> AI Confidence: **99.17%**
1774. **`tests/cases/compiler/reservedWords.ts`** -> AI Confidence: **99.17%**
1775. **`tests/cases/compiler/sourceMapValidationDestructuringForArrayBindingPatternDefaultValues.ts`** -> AI Confidence: **99.17%**
1776. **`tests/cases/compiler/sourceMapValidationDestructuringForArrayBindingPatternDefaultValues2.ts`** -> AI Confidence: **99.17%**
1777. **`tests/cases/compiler/sourceMapValidationDestructuringForOfArrayBindingPatternDefaultValues.ts`** -> AI Confidence: **99.17%**
1778. **`tests/cases/compiler/sourceMapValidationDestructuringForOfArrayBindingPatternDefaultValues2.ts`** -> AI Confidence: **99.17%**
1779. **`tests/cases/compiler/switchAssignmentCompat.ts`** -> AI Confidence: **99.17%**
1780. **`tests/cases/compiler/tryCatchFinallyControlFlow.ts`** -> AI Confidence: **99.17%**
1781. **`tests/cases/compiler/typeGuardNarrowsIndexedAccessOfKnownProperty3.ts`** -> AI Confidence: **99.17%**
1782. **`tests/cases/compiler/uncalledFunctionChecksInConditional.ts`** -> AI Confidence: **99.17%**
1783. **`tests/cases/compiler/unreachableFlowAfterFinally.ts`** -> AI Confidence: **99.17%**
1784. **`tests/cases/compiler/unusedLocalsInForInOrOf1.ts`** -> AI Confidence: **99.17%**
1785. **`tests/cases/compiler/weakTypeAndPrimitiveNarrowing.ts`** -> AI Confidence: **99.17%**
1786. **`tests/cases/conformance/controlFlow/controlFlowInOperator.ts`** -> AI Confidence: **99.17%**
1787. **`tests/cases/conformance/controlFlow/controlFlowOptionalChain2.ts`** -> AI Confidence: **99.17%**
1788. **`tests/cases/conformance/controlFlow/controlFlowTypeofObject.ts`** -> AI Confidence: **99.17%**
1789. **`tests/cases/conformance/es2021/logicalAssignment/logicalAssignment2.ts`** -> AI Confidence: **99.17%**
1790. **`tests/cases/conformance/es6/Symbols/symbolType8.ts`** -> AI Confidence: **99.17%**
1791. **`tests/cases/conformance/es6/destructuring/objectBindingPatternKeywordIdentifiers02.ts`** -> AI Confidence: **99.17%**
1792. **`tests/cases/conformance/es6/destructuring/objectBindingPatternKeywordIdentifiers04.ts`** -> AI Confidence: **99.17%**
1793. **`tests/cases/conformance/es6/templates/templateStringInEqualityChecks.ts`** -> AI Confidence: **99.17%**
1794. **`tests/cases/conformance/es6/templates/templateStringInEqualityChecksES6.ts`** -> AI Confidence: **99.17%**
1795. **`tests/cases/conformance/expressions/nullishCoalescingOperator/nullishCoalescingAssignmentVsPrivateFieldsJsEmit1.ts`** -> AI Confidence: **99.17%**
1796. **`tests/cases/conformance/expressions/nullishCoalescingOperator/nullishCoalescingOperator1.ts`** -> AI Confidence: **99.17%**
1797. **`tests/cases/conformance/expressions/nullishCoalescingOperator/nullishCoalescingOperator4.ts`** -> AI Confidence: **99.17%**
1798. **`tests/cases/conformance/expressions/optionalChaining/privateIdentifierChain/privateIdentifierChain.1.ts`** -> AI Confidence: **99.17%**
1799. **`tests/cases/conformance/expressions/typeGuards/typeGuardOfFormNotExpr.ts`** -> AI Confidence: **99.17%**
1800. **`tests/cases/conformance/jsdoc/assertionsAndNonReturningFunctions.ts`** -> AI Confidence: **99.17%**
1801. **`tests/cases/conformance/parser/ecmascript6/ShorthandPropertyAssignment/parserShorthandPropertyAssignment1.ts`** -> AI Confidence: **99.17%**
1802. **`tests/cases/conformance/statements/breakStatements/invalidForBreakStatements.ts`** -> AI Confidence: **99.17%**
1803. **`tests/cases/conformance/statements/breakStatements/invalidWhileBreakStatements.ts`** -> AI Confidence: **99.17%**
1804. **`tests/cases/conformance/statements/continueStatements/invalidForContinueStatements.ts`** -> AI Confidence: **99.17%**
1805. **`tests/cases/conformance/statements/continueStatements/invalidWhileContinueStatements.ts`** -> AI Confidence: **99.17%**
1806. **`tests/cases/conformance/statements/ifDoWhileStatements/ifDoWhileStatements.ts`** -> AI Confidence: **99.17%**
1807. **`tests/cases/conformance/statements/switchStatements/switchStatements.ts`** -> AI Confidence: **99.17%**
1808. **`tests/cases/conformance/types/any/narrowExceptionVariableInCatchClause.ts`** -> AI Confidence: **99.17%**
1809. **`tests/cases/conformance/types/keyof/keyofAndForIn.ts`** -> AI Confidence: **99.17%**
1810. **`tests/cases/conformance/types/literal/literalTypesAndDestructuring.ts`** -> AI Confidence: **99.17%**
1811. **`tests/cases/conformance/types/literal/stringLiteralsWithSwitchStatements01.ts`** -> AI Confidence: **99.17%**
1812. **`tests/cases/conformance/types/objectTypeLiteral/methodSignatures/methodSignaturesWithOverloads2.ts`** -> AI Confidence: **99.17%**
1813. **`tests/cases/conformance/types/rest/objectRestForOf.ts`** -> AI Confidence: **99.17%**
1814. **`tests/cases/conformance/types/unknown/unknownType2.ts`** -> AI Confidence: **99.17%**
1815. **`tests/cases/fourslash/codeFixAddOptionalParam13.ts`** -> AI Confidence: **99.17%**
1816. **`tests/cases/fourslash/codeFixAddOptionalParam17.ts`** -> AI Confidence: **99.17%**
1817. **`tests/cases/fourslash/completionsObjectLiteralExpressions1.ts`** -> AI Confidence: **99.17%**
1818. **`tests/cases/fourslash/findAllRefsReExports.ts`** -> AI Confidence: **99.17%**
1819. **`tests/cases/fourslash/fixNaNEquality_all.ts`** -> AI Confidence: **99.17%**
1820. **`tests/cases/fourslash/formatColonAndQMark.ts`** -> AI Confidence: **99.17%**
1821. **`tests/cases/fourslash/formatConflictDiff3Marker1.ts`** -> AI Confidence: **99.17%**
1822. **`tests/cases/fourslash/formattingOnClosingBracket.ts`** -> AI Confidence: **99.17%**
1823. **`tests/cases/fourslash/formattingOnDoWhileNoSemicolon.ts`** -> AI Confidence: **99.17%**
1824. **`tests/cases/fourslash/formattingOnInvalidCodes.ts`** -> AI Confidence: **99.17%**
1825. **`tests/cases/fourslash/refactorConvertToOptionalChainExpression_EmptySpanConditionalReturnKeyword.ts`** -> AI Confidence: **99.17%**
1826. **`tests/cases/fourslash/refactorConvertToOptionalChainExpression_EmptySpanConditionalReturnStatement.ts`** -> AI Confidence: **99.17%**
1827. **`tests/cases/fourslash/refactorConvertToOptionalChainExpression_ReturnStatementConditional.ts`** -> AI Confidence: **99.17%**
1828. **`tests/baselines/reference/emit(jsx=preserve).js`** -> AI Confidence: **99.16%**
1829. **`tests/baselines/reference/emit(jsx=react).js`** -> AI Confidence: **99.16%**
1830. **`src/services/codefixes/importFixes.ts`** -> AI Confidence: **99.16%**
1831. **`src/testRunner/unittests/tsserver/cachingFileSystemInformation.ts`** -> AI Confidence: **99.16%**
1832. **`src/testRunner/unittests/helpers/typingsInstaller.ts`** -> AI Confidence: **99.15%**
1833. **`src/testRunner/unittests/tsserver/getEditsForFileRename.ts`** -> AI Confidence: **99.15%**
1834. **`tests/baselines/reference/exportNamespace9.js`** -> AI Confidence: **99.13%**
1835. **`tests/baselines/reference/jsxRuntimePragma(jsx=preserve).js`** -> AI Confidence: **99.13%**
1836. **`tests/baselines/reference/jsxRuntimePragma(jsx=react).js`** -> AI Confidence: **99.13%**
1837. **`tests/baselines/reference/jsxRuntimePragma(jsx=react-jsx).js`** -> AI Confidence: **99.13%**
1838. **`tests/baselines/reference/jsxRuntimePragma(jsx=react-jsxdev).js`** -> AI Confidence: **99.13%**
1839. **`tests/baselines/reference/tsserver/moduleResolution/alternateResult.js`** -> AI Confidence: **99.13%**
1840. **`src/harness/vfsUtil.ts`** -> AI Confidence: **99.13%**
1841. **`src/services/stringCompletions.ts`** -> AI Confidence: **99.13%**
1842. **`src/testRunner/compilerRunner.ts`** -> AI Confidence: **99.13%**
1843. **`src/testRunner/runner.ts`** -> AI Confidence: **99.13%**
1844. **`src/testRunner/unittests/helpers/tsc.ts`** -> AI Confidence: **99.13%**
1845. **`tests/baselines/reference/awaitUsingDeclarations.3(target=es5).js`** -> AI Confidence: **99.11%**
1846. **`tests/baselines/reference/awaitUsingDeclarationsInFor(target=es2015).js`** -> AI Confidence: **99.11%**
1847. **`tests/baselines/reference/awaitUsingDeclarationsInFor(target=es5).js`** -> AI Confidence: **99.11%**
1848. **`tests/baselines/reference/awaitUsingDeclarationsInForOf.1(target=es2015).js`** -> AI Confidence: **99.11%**
1849. **`tests/baselines/reference/callChain.2.js`** -> AI Confidence: **99.11%**
1850. **`tests/baselines/reference/decoratorInAmbientContext.js`** -> AI Confidence: **99.11%**
1851. **`tests/baselines/reference/decoratorOnClassAccessor4(target=es2015).js`** -> AI Confidence: **99.11%**
1852. **`tests/baselines/reference/decoratorOnClassAccessor5(target=es2015).js`** -> AI Confidence: **99.11%**
1853. **`tests/baselines/reference/decoratorOnClassAccessor6(target=es2015).js`** -> AI Confidence: **99.11%**
1854. **`tests/baselines/reference/decoratorOnClassMethod1(target=es2015).js`** -> AI Confidence: **99.11%**
1855. **`tests/baselines/reference/decoratorOnClassMethod10(target=es2015).js`** -> AI Confidence: **99.11%**
1856. **`tests/baselines/reference/decoratorOnClassMethod13.js`** -> AI Confidence: **99.11%**
1857. **`tests/baselines/reference/decoratorOnClassMethod2(target=es2015).js`** -> AI Confidence: **99.11%**
1858. **`tests/baselines/reference/decoratorOnClassMethod3(target=es2015).js`** -> AI Confidence: **99.11%**
1859. **`tests/baselines/reference/decoratorOnClassMethod4.js`** -> AI Confidence: **99.11%**
1860. **`tests/baselines/reference/decoratorOnClassMethod7.js`** -> AI Confidence: **99.11%**
1861. **`tests/baselines/reference/decoratorOnClassMethod8(target=es2015).js`** -> AI Confidence: **99.11%**
1862. **`tests/baselines/reference/decoratorOnClassMethodOverload2(target=es2015).js`** -> AI Confidence: **99.11%**
1863. **`tests/baselines/reference/decoratorOnClassProperty1(target=es2015).js`** -> AI Confidence: **99.11%**
1864. **`tests/baselines/reference/decoratorOnClassProperty2(target=es2015).js`** -> AI Confidence: **99.11%**
1865. **`tests/baselines/reference/decoratorOnClassProperty3(target=es2015).js`** -> AI Confidence: **99.11%**
1866. **`tests/baselines/reference/decoratorOnClassProperty6(target=es2015).js`** -> AI Confidence: **99.11%**
1867. **`tests/baselines/reference/decoratorOnClassProperty7(target=es2015).js`** -> AI Confidence: **99.11%**
1868. **`tests/baselines/reference/decoratorWithNegativeLiteralTypeNoCrash(target=es2015).js`** -> AI Confidence: **99.11%**
1869. **`tests/baselines/reference/defaultExportInAwaitExpression01.js`** -> AI Confidence: **99.11%**
1870. **`tests/baselines/reference/destructuringArrayBindingPatternAndAssignment4(target=es5).js`** -> AI Confidence: **99.11%**
1871. **`tests/baselines/reference/destructuringAssignmentWithExportedName.js`** -> AI Confidence: **99.11%**
1872. **`tests/baselines/reference/es5-asyncFunctionWhileStatements(target=es2015).js`** -> AI Confidence: **99.11%**
1873. **`tests/baselines/reference/generatorTypeCheck59.js`** -> AI Confidence: **99.11%**
1874. **`tests/baselines/reference/importCallExpressionNestedES20152(target=es5).js`** -> AI Confidence: **99.11%**
1875. **`tests/baselines/reference/importCallExpressionNestedES20202(target=es5).js`** -> AI Confidence: **99.11%**
1876. **`tests/baselines/reference/importCallExpressionNestedUMD2(target=es5).js`** -> AI Confidence: **99.11%**
1877. **`tests/baselines/reference/metadataOfStringLiteral.js`** -> AI Confidence: **99.11%**
1878. **`tests/baselines/reference/missingDecoratorType(target=es2015).js`** -> AI Confidence: **99.11%**
1879. **`tests/baselines/reference/mixedTypeEnumComparison.js`** -> AI Confidence: **99.11%**
1880. **`tests/baselines/reference/moduleNodeDefaultImports(module=node16).js`** -> AI Confidence: **99.11%**
1881. **`tests/baselines/reference/moduleNodeDefaultImports(module=node18).js`** -> AI Confidence: **99.11%**
1882. **`tests/baselines/reference/moduleNodeDefaultImports(module=node20).js`** -> AI Confidence: **99.11%**
1883. **`tests/baselines/reference/moduleNodeDefaultImports(module=nodenext).js`** -> AI Confidence: **99.11%**
1884. **`tests/baselines/reference/narrowingTypeofDiscriminant.js`** -> AI Confidence: **99.11%**
1885. **`tests/baselines/reference/numericEnumMappedType.js`** -> AI Confidence: **99.11%**
1886. **`tests/baselines/reference/paramsOnlyHaveLiteralTypesWhenAppropriatelyContextualized.js`** -> AI Confidence: **99.11%**
1887. **`tests/baselines/reference/sourceMap-Comments(target=es2015).js`** -> AI Confidence: **99.11%**
1888. **`tests/baselines/reference/sourceMapValidationDestructuringForArrayBindingPattern2(target=es2015).js`** -> AI Confidence: **99.11%**
1889. **`tests/baselines/reference/strictOptionalProperties1.js`** -> AI Confidence: **99.11%**
1890. **`tests/baselines/reference/transformApi/transformsCorrectly.transformAddDecoratedNode.js`** -> AI Confidence: **99.11%**
1891. **`tests/baselines/reference/transformApi/transformsCorrectly.transformSyntheticCommentOnStaticFieldInClassDeclaration.js`** -> AI Confidence: **99.11%**
1892. **`tests/baselines/reference/tsbuild/resolveJsonModule/include-only-with-json-not-in-rootDir-non-composite.js`** -> AI Confidence: **99.11%**
1893. **`tests/baselines/reference/tsbuild/resolveJsonModule/include-only-without-outDir-non-composite.js`** -> AI Confidence: **99.11%**
1894. **`tests/baselines/reference/tsbuildWatch/noEmit/outFile/dts-errors-without-dts-enabled.js`** -> AI Confidence: **99.11%**
1895. **`tests/baselines/reference/tscWatch/moduleResolution/package-json-file-is-edited-when-package-json-with-type-module-exists.js`** -> AI Confidence: **99.11%**
1896. **`tests/baselines/reference/tscWatch/noEmit/outFile/dts-errors-without-dts-enabled.js`** -> AI Confidence: **99.11%**
1897. **`tests/baselines/reference/tscWatch/symlinks/monorepo-style-sibling-packages-symlinked-package1-built.js`** -> AI Confidence: **99.11%**
1898. **`tests/baselines/reference/tscWatch/watchEnvironment/fsEvent-for-change-is-repeated.js`** -> AI Confidence: **99.11%**
1899. **`tests/baselines/reference/tsserver/exportMapCache/does-not-invalidate-the-cache-when-referenced-project-changes-inconsequentially.js`** -> AI Confidence: **99.11%**
1900. **`tests/baselines/reference/tsserver/fourslashServer/importCompletions_importsMap4.js`** -> AI Confidence: **99.11%**
1901. **`tests/baselines/reference/tsserver/fourslashServer/importCompletions_importsMap5.js`** -> AI Confidence: **99.11%**
1902. **`tests/baselines/reference/tsserver/fourslashServer/openFileWithSyntaxKind.js`** -> AI Confidence: **99.11%**
1903. **`tests/baselines/reference/tsserver/fourslashServer/packageJsonImportsFailedLookups.js`** -> AI Confidence: **99.11%**
1904. **`tests/baselines/reference/tsserver/fourslashServer/rewriteRelativeImportExtensionsProjectReferences1.js`** -> AI Confidence: **99.11%**
1905. **`tests/baselines/reference/tsserver/projects/should-disable-features-when-the-files-are-too-large.js`** -> AI Confidence: **99.11%**
1906. **`tests/baselines/reference/tsserver/typingsInstaller/malformed-packagejson.js`** -> AI Confidence: **99.11%**
1907. **`tests/baselines/reference/tsserver/watchEnvironment/uses-dynamic-polling-when-file-is-added-to-subfolder.js`** -> AI Confidence: **99.11%**
1908. **`tests/baselines/reference/tsserver/watchEnvironment/uses-watchFile-when-file-is-added-to-subfolder.js`** -> AI Confidence: **99.11%**
1909. **`tests/baselines/reference/tsserver/watchEnvironment/watching-npm-install-in-codespaces-where-workspaces-folder-is-hosted-at-root.js`** -> AI Confidence: **99.11%**
1910. **`tests/baselines/reference/uncaughtCompilerError1.js`** -> AI Confidence: **99.11%**
1911. **`tests/baselines/reference/usingDeclarations.2(target=es2015).js`** -> AI Confidence: **99.11%**
1912. **`tests/baselines/reference/usingDeclarations.2(target=es2017).js`** -> AI Confidence: **99.11%**
1913. **`tests/baselines/reference/usingDeclarations.2(target=es2022).js`** -> AI Confidence: **99.11%**
1914. **`tests/baselines/reference/usingDeclarations.3(target=es2015).js`** -> AI Confidence: **99.11%**
1915. **`tests/baselines/reference/usingDeclarations.3(target=es2017).js`** -> AI Confidence: **99.11%**
1916. **`tests/baselines/reference/usingDeclarations.3(target=es2022).js`** -> AI Confidence: **99.11%**
1917. **`src/services/suggestionDiagnostics.ts`** -> AI Confidence: **99.11%**
1918. **`tests/cases/compiler/downlevelLetConst18.ts`** -> AI Confidence: **99.11%**
1919. **`tests/cases/compiler/emptyAnonymousObjectNarrowing.ts`** -> AI Confidence: **99.11%**
1920. **`tests/cases/compiler/optionalPropertiesSyntax.ts`** -> AI Confidence: **99.11%**
1921. **`tests/cases/compiler/sourceMap-Comments.ts`** -> AI Confidence: **99.11%**
1922. **`tests/cases/compiler/sourceMapValidationDestructuringForObjectBindingPatternDefaultValues.ts`** -> AI Confidence: **99.11%**
1923. **`tests/cases/compiler/sourceMapValidationDestructuringForOfObjectBindingPatternDefaultValues.ts`** -> AI Confidence: **99.11%**
1924. **`tests/cases/compiler/typePredicatesOptionalChaining1.ts`** -> AI Confidence: **99.11%**
1925. **`tests/cases/conformance/expressions/optionalChaining/propertyAccessChain/propertyAccessChain.ts`** -> AI Confidence: **99.11%**
1926. **`tests/cases/fourslash/extract-method47.ts`** -> AI Confidence: **99.11%**
1927. **`scripts/eslint/rules/argument-trivia.cjs`** -> AI Confidence: **99.09%**
1928. **`scripts/eslint/rules/no-array-mutating-method-expressions.cjs`** -> AI Confidence: **99.09%**
1929. **`scripts/eslint/rules/no-direct-import.cjs`** -> AI Confidence: **99.09%**
1930. **`scripts/eslint/tests/js-extensions.cjs`** -> AI Confidence: **99.09%**
1931. **`tests/baselines/reference/ambientShorthand_reExport.js`** -> AI Confidence: **99.09%**
1932. **`tests/baselines/reference/assertionFunctionWildcardImport1.js`** -> AI Confidence: **99.09%**
1933. **`tests/baselines/reference/bundlerImportTsExtensions(allowimportingtsextensions=false,noemit=false).js`** -> AI Confidence: **99.09%**
1934. **`tests/baselines/reference/bundlerImportTsExtensions(allowimportingtsextensions=true,noemit=false).js`** -> AI Confidence: **99.09%**
1935. **`tests/baselines/reference/chained2.js`** -> AI Confidence: **99.09%**
1936. **`tests/baselines/reference/declarationsIndirectGeneratedAliasReference.js`** -> AI Confidence: **99.09%**
1937. **`tests/baselines/reference/emitDecoratorMetadata_isolatedModules(module=commonjs).js`** -> AI Confidence: **99.09%**
1938. **`tests/baselines/reference/esModuleInterop.js`** -> AI Confidence: **99.09%**
1939. **`tests/baselines/reference/exportAsNamespace4(module=amd).js`** -> AI Confidence: **99.09%**
1940. **`tests/baselines/reference/exportAsNamespace4(module=commonjs).js`** -> AI Confidence: **99.09%**
1941. **`tests/baselines/reference/exportAsNamespace4(module=umd).js`** -> AI Confidence: **99.09%**
1942. **`tests/baselines/reference/exportDefault.js`** -> AI Confidence: **99.09%**
1943. **`tests/baselines/reference/exportNamespace1.js`** -> AI Confidence: **99.09%**
1944. **`tests/baselines/reference/exportNamespace2.js`** -> AI Confidence: **99.09%**
1945. **`tests/baselines/reference/exportNamespace3.js`** -> AI Confidence: **99.09%**
1946. **`tests/baselines/reference/exportStarForValues4.js`** -> AI Confidence: **99.09%**
1947. **`tests/baselines/reference/exportStarForValues9.js`** -> AI Confidence: **99.09%**
1948. **`tests/baselines/reference/exportStarFromEmptyModule(target=es2015).js`** -> AI Confidence: **99.09%**
1949. **`tests/baselines/reference/exportStarFromEmptyModule(target=es5).js`** -> AI Confidence: **99.09%**
1950. **`tests/baselines/reference/exportStarNotElided.js`** -> AI Confidence: **99.09%**
1951. **`tests/baselines/reference/importEquals1.js`** -> AI Confidence: **99.09%**
1952. **`tests/baselines/reference/legacyNodeModulesExportsSpecifierGenerationConditions.js`** -> AI Confidence: **99.09%**
1953. **`tests/baselines/reference/nodeModules1(module=node16).js`** -> AI Confidence: **99.09%**
1954. **`tests/baselines/reference/nodeModules1(module=node18).js`** -> AI Confidence: **99.09%**
1955. **`tests/baselines/reference/nodeModules1(module=node20).js`** -> AI Confidence: **99.09%**
1956. **`tests/baselines/reference/nodeModules1(module=nodenext).js`** -> AI Confidence: **99.09%**
1957. **`tests/baselines/reference/nodeModulesAllowJs1(module=node16).js`** -> AI Confidence: **99.09%**
1958. **`tests/baselines/reference/nodeModulesAllowJs1(module=node18).js`** -> AI Confidence: **99.09%**
1959. **`tests/baselines/reference/nodeModulesAllowJs1(module=node20).js`** -> AI Confidence: **99.09%**
1960. **`tests/baselines/reference/nodeModulesAllowJs1(module=nodenext).js`** -> AI Confidence: **99.09%**
1961. **`tests/baselines/reference/nodeModulesCJSEmit1(module=node18).js`** -> AI Confidence: **99.09%**
1962. **`tests/baselines/reference/nodeModulesCJSEmit1(module=node20).js`** -> AI Confidence: **99.09%**
1963. **`tests/baselines/reference/nodeModulesCJSEmit1(module=nodenext).js`** -> AI Confidence: **99.09%**
1964. **`tests/baselines/reference/pathMappingBasedModuleResolution_rootImport_aliasWithRoot_differentRootTypes.js`** -> AI Confidence: **99.09%**
1965. **`tests/baselines/reference/project/nonRelative/node/consume.js`** -> AI Confidence: **99.09%**
1966. **`tests/baselines/reference/requireAsFunctionInExternalModule.js`** -> AI Confidence: **99.09%**
1967. **`tests/baselines/reference/tsc/moduleResolution/pnpm-style-layout.js`** -> AI Confidence: **99.09%**
1968. **`tests/baselines/reference/tscWatch/moduleResolution/ambient-module-names-are-resolved-correctly.js`** -> AI Confidence: **99.09%**
1969. **`tests/baselines/reference/tscWatch/moduleResolution/late-discovered-dependency-symlink.js`** -> AI Confidence: **99.09%**
1970. **`tests/baselines/reference/tsserver/completions/works-when-files-are-included-from-two-different-drives-of-windows.js`** -> AI Confidence: **99.09%**
1971. **`tests/baselines/reference/tsserver/fourslashServer/completionsImport_addToNamedWithDifferentCacheValue.js`** -> AI Confidence: **99.09%**
1972. **`tests/baselines/reference/tsserver/inferredProjects/when-existing-inferred-project-has-no-root-files.js`** -> AI Confidence: **99.09%**
1973. **`tests/baselines/reference/tsserver/maxNodeModuleJsDepth/handles-resolutions-when-currentNodeModulesDepth-changes-when-referencing-file-from-another-file.js`** -> AI Confidence: **99.09%**
1974. **`tests/baselines/reference/tsserver/resolutionCache/avoid-unnecessary-lookup-invalidation-on-save.js`** -> AI Confidence: **99.09%**
1975. **`tests/baselines/reference/tsserver/resolutionCache/when-resolution-is-succeeds-in-global-typings-location-with-import-from-the-cache-file-with-currentDirectory-at-root.js`** -> AI Confidence: **99.09%**
1976. **`tests/baselines/reference/tsserver/resolutionCache/when-resolution-is-succeeds-in-global-typings-location-with-import-from-the-cache-file.js`** -> AI Confidence: **99.09%**
1977. **`tests/baselines/reference/tsserver/symLinks/when-not-symlink-but-differs-in-casing.js`** -> AI Confidence: **99.09%**
1978. **`tests/baselines/reference/tsserver/syntacticServer/files-go-to-inferred-project-and-semantic-operations-fail.js`** -> AI Confidence: **99.09%**
1979. **`tests/baselines/reference/untypedModuleImport.js`** -> AI Confidence: **99.09%**
1980. **`src/compiler/_namespaces/ts.ts`** -> AI Confidence: **99.09%**
1981. **`src/compiler/tracing.ts`** -> AI Confidence: **99.09%**
1982. **`src/harness/harnessUtils.ts`** -> AI Confidence: **99.09%**
1983. **`src/harness/projectServiceStateLogger.ts`** -> AI Confidence: **99.09%**
1984. **`src/server/_namespaces/ts.server.ts`** -> AI Confidence: **99.09%**
1985. **`src/server/editorServices.ts`** -> AI Confidence: **99.09%**
1986. **`src/server/project.ts`** -> AI Confidence: **99.09%**
1987. **`src/server/scriptInfo.ts`** -> AI Confidence: **99.09%**
1988. **`src/server/scriptVersionCache.ts`** -> AI Confidence: **99.09%**
1989. **`src/services/_namespaces/ts.codefix.ts`** -> AI Confidence: **99.09%**
1990. **`src/services/_namespaces/ts.refactor.ts`** -> AI Confidence: **99.09%**
1991. **`src/services/_namespaces/ts.ts`** -> AI Confidence: **99.09%**
1992. **`src/services/codefixes/addMissingResolutionModeImportAttribute.ts`** -> AI Confidence: **99.09%**
1993. **`src/services/codefixes/fixMissingTypeAnnotationOnExports.ts`** -> AI Confidence: **99.09%**
1994. **`src/testRunner/tests.ts`** -> AI Confidence: **99.09%**
1995. **`src/testRunner/transpileRunner.ts`** -> AI Confidence: **99.09%**
1996. **`src/testRunner/unittests/services/preProcessFile.ts`** -> AI Confidence: **99.09%**
1997. **`src/testRunner/unittests/tsbuild/moduleResolution.ts`** -> AI Confidence: **99.09%**
1998. **`src/testRunner/unittests/tsbuild/moduleSpecifiers.ts`** -> AI Confidence: **99.09%**
1999. **`src/testRunner/unittests/tsbuild/sample.ts`** -> AI Confidence: **99.09%**
2000. **`src/testRunner/unittests/tsc/declarationEmit.ts`** -> AI Confidence: **99.09%**
2001. **`src/testRunner/unittests/tsc/moduleResolution.ts`** -> AI Confidence: **99.09%**
2002. **`src/testRunner/unittests/tsc/projectReferences.ts`** -> AI Confidence: **99.09%**
2003. **`src/testRunner/unittests/tscWatch/emitAndErrorUpdates.ts`** -> AI Confidence: **99.09%**
2004. **`src/testRunner/unittests/tscWatch/forceConsistentCasingInFileNames.ts`** -> AI Confidence: **99.09%**
2005. **`src/testRunner/unittests/tscWatch/moduleResolution.ts`** -> AI Confidence: **99.09%**
2006. **`src/testRunner/unittests/tscWatch/programUpdates.ts`** -> AI Confidence: **99.09%**
2007. **`src/testRunner/unittests/tscWatch/projectsWithReferences.ts`** -> AI Confidence: **99.09%**
2008. **`src/testRunner/unittests/tscWatch/resolutionCache.ts`** -> AI Confidence: **99.09%**
2009. **`src/testRunner/unittests/tsserver/auxiliaryProject.ts`** -> AI Confidence: **99.09%**
2010. **`src/testRunner/unittests/tsserver/forceConsistentCasingInFileNames.ts`** -> AI Confidence: **99.09%**
2011. **`src/testRunner/unittests/tsserver/moduleResolution.ts`** -> AI Confidence: **99.09%**
2012. **`tests/cases/compiler/es6ExportEqualsInterop.ts`** -> AI Confidence: **99.09%**
2013. **`tests/cases/compiler/esModuleInteropDefaultImports.ts`** -> AI Confidence: **99.09%**
2014. **`tests/cases/compiler/pathMappingBasedModuleResolution_rootImport_aliasWithRoot_differentRootTypes.ts`** -> AI Confidence: **99.09%**
2015. **`tests/cases/compiler/ramdaToolsNoInfinite2.ts`** -> AI Confidence: **99.09%**
2016. **`tests/cases/conformance/externalModules/rewriteRelativeImportExtensions/emit.ts`** -> AI Confidence: **99.09%**
2017. **`tests/cases/conformance/jsdoc/declarations/jsDeclarationsExportForms.ts`** -> AI Confidence: **99.09%**
2018. **`tests/cases/conformance/moduleResolution/allowImportingTsExtensions.ts`** -> AI Confidence: **99.09%**
2019. **`tests/cases/conformance/moduleResolution/bundler/bundlerImportTsExtensions.ts`** -> AI Confidence: **99.09%**
2020. **`tests/cases/conformance/node/allowJs/nodeModulesAllowJs1.ts`** -> AI Confidence: **99.09%**
2021. **`tests/cases/conformance/node/nodeModules1.ts`** -> AI Confidence: **99.09%**
2022. **`tests/cases/fourslash/getEditsForFileRename_preservePathEnding.ts`** -> AI Confidence: **99.09%**
2023. **`tests/baselines/reference/bundledDtsLateExportRenaming.js`** -> AI Confidence: **99.08%**
2024. **`tests/baselines/reference/bundlerRelative1(module=esnext).js`** -> AI Confidence: **99.08%**
2025. **`tests/baselines/reference/bundlerRelative1(module=preserve).js`** -> AI Confidence: **99.08%**
2026. **`tests/baselines/reference/exportAssignTypes.js`** -> AI Confidence: **99.08%**
2027. **`tests/baselines/reference/nodeModulesDeclarationEmitDynamicImportWithPackageExports(module=node18).js`** -> AI Confidence: **99.08%**
2028. **`tests/baselines/reference/nodeModulesDeclarationEmitDynamicImportWithPackageExports(module=node20).js`** -> AI Confidence: **99.08%**
2029. **`tests/baselines/reference/nodeModulesDeclarationEmitDynamicImportWithPackageExports(module=nodenext).js`** -> AI Confidence: **99.08%**
2030. **`tests/baselines/reference/privacyImport.js`** -> AI Confidence: **99.08%**
2031. **`tests/baselines/reference/privacyImportParseErrors.js`** -> AI Confidence: **99.08%**
2032. **`tests/baselines/reference/ramdaToolsNoInfinite2.js`** -> AI Confidence: **99.08%**
2033. **`tests/baselines/reference/tsserver/completionsIncomplete/works-with-PackageJsonAutoImportProvider.js`** -> AI Confidence: **99.08%**
2034. **`src/harness/_namespaces/ts.ts`** -> AI Confidence: **99.08%**
2035. **`src/services/_namespaces/ts.formatting.ts`** -> AI Confidence: **99.08%**
2036. **`src/testRunner/_namespaces/ts.ts`** -> AI Confidence: **99.08%**
2037. **`src/testRunner/unittests/helpers/alternateResult.ts`** -> AI Confidence: **99.08%**
2038. **`src/testRunner/unittests/helpers/forceConsistentCasingInFileNames.ts`** -> AI Confidence: **99.08%**
2039. **`src/testRunner/unittests/helpers/libraryResolution.ts`** -> AI Confidence: **99.08%**
2040. **`src/testRunner/unittests/programApi.ts`** -> AI Confidence: **99.08%**
2041. **`src/testRunner/unittests/reuseProgramStructure.ts`** -> AI Confidence: **99.08%**
2042. **`src/testRunner/unittests/tsbuild/declarationEmit.ts`** -> AI Confidence: **99.08%**
2043. **`src/testRunner/unittests/tsbuild/emitDeclarationOnly.ts`** -> AI Confidence: **99.08%**
2044. **`src/testRunner/unittests/tsbuild/inferredTypeFromTransitiveModule.ts`** -> AI Confidence: **99.08%**
2045. **`src/testRunner/unittests/tsbuild/javascriptProjectEmit.ts`** -> AI Confidence: **99.08%**
2046. **`src/testRunner/unittests/tsbuild/roots.ts`** -> AI Confidence: **99.08%**
2047. **`src/testRunner/unittests/tsbuildWatch/moduleResolution.ts`** -> AI Confidence: **99.08%**
2048. **`src/testRunner/unittests/tsbuildWatch/programUpdates.ts`** -> AI Confidence: **99.08%**
2049. **`src/testRunner/unittests/tsc/forceConsistentCasingInFileNames.ts`** -> AI Confidence: **99.08%**
2050. **`src/testRunner/unittests/tsc/incremental.ts`** -> AI Confidence: **99.08%**
2051. **`src/testRunner/unittests/tscWatch/sourceOfProjectReferenceRedirect.ts`** -> AI Confidence: **99.08%**
2052. **`src/testRunner/unittests/tscWatch/watchApi.ts`** -> AI Confidence: **99.08%**
2053. **`src/testRunner/unittests/tscWatch/watchEnvironment.ts`** -> AI Confidence: **99.08%**
2054. **`src/testRunner/unittests/tsserver/compileOnSave.ts`** -> AI Confidence: **99.08%**
2055. **`src/testRunner/unittests/tsserver/configuredProjects.ts`** -> AI Confidence: **99.08%**
2056. **`src/testRunner/unittests/tsserver/projectReferences.ts`** -> AI Confidence: **99.08%**
2057. **`src/testRunner/unittests/tsserver/projects.ts`** -> AI Confidence: **99.08%**
2058. **`src/testRunner/unittests/tsserver/resolutionCache.ts`** -> AI Confidence: **99.08%**
2059. **`src/testRunner/unittests/tsserver/typeOnlyImportChains.ts`** -> AI Confidence: **99.08%**
2060. **`src/testRunner/unittests/tsserver/typingsInstaller.ts`** -> AI Confidence: **99.08%**
2061. **`src/testRunner/unittests/tsserver/watchEnvironment.ts`** -> AI Confidence: **99.08%**
2062. **`tests/cases/compiler/privacyImport.ts`** -> AI Confidence: **99.08%**
2063. **`tests/cases/compiler/privacyImportParseErrors.ts`** -> AI Confidence: **99.08%**
2064. **`tests/cases/conformance/externalModules/exportAssignTypes.ts`** -> AI Confidence: **99.08%**
2065. **`tests/cases/conformance/moduleResolution/bundler/bundlerRelative1.ts`** -> AI Confidence: **99.08%**
2066. **`tests/cases/conformance/node/allowJs/nodeModulesAllowJsConditionalPackageExports.ts`** -> AI Confidence: **99.08%**
2067. **`tests/cases/conformance/node/nodeModulesConditionalPackageExports.ts`** -> AI Confidence: **99.08%**
2068. **`tests/cases/conformance/node/nodeModulesImportAttributesTypeModeDeclarationEmitErrors.ts`** -> AI Confidence: **99.08%**
2069. **`tests/cases/conformance/node/nodeModulesImportTypeModeDeclarationEmitErrors1.ts`** -> AI Confidence: **99.08%**
2070. **`tests/cases/fourslash/getEditsForFileRename_renameFromIndex.ts`** -> AI Confidence: **99.08%**
2071. **`tests/cases/fourslash/nodeModulesImportCompletions1.ts`** -> AI Confidence: **99.08%**
2072. **`tests/cases/projects/NoModule/decl.ts`** -> AI Confidence: **99.08%**
2073. **`eslint.config.mjs`** -> AI Confidence: **99.07%**
2074. **`tests/baselines/reference/es6ExportEqualsInterop.js`** -> AI Confidence: **99.07%**
2075. **`tests/baselines/reference/tsserver/resolutionCache/relative-module-name-from-files-in-different-folders.js`** -> AI Confidence: **99.07%**
2076. **`src/testRunner/unittests/helpers/demoProjectReferences.ts`** -> AI Confidence: **99.07%**
2077. **`src/testRunner/unittests/helpers/sampleProjectReferences.ts`** -> AI Confidence: **99.07%**
2078. **`src/testRunner/unittests/moduleResolution.ts`** -> AI Confidence: **99.07%**
2079. **`src/testRunner/unittests/services/languageService.ts`** -> AI Confidence: **99.07%**
2080. **`src/testRunner/unittests/transform.ts`** -> AI Confidence: **99.07%**
2081. **`src/testRunner/unittests/tsbuild/commandLine.ts`** -> AI Confidence: **99.07%**
2082. **`src/testRunner/unittests/tsbuild/fileDelete.ts`** -> AI Confidence: **99.07%**
2083. **`src/testRunner/unittests/tsbuild/resolveJsonModule.ts`** -> AI Confidence: **99.07%**
2084. **`src/testRunner/unittests/tsc/cancellationToken.ts`** -> AI Confidence: **99.07%**
2085. **`src/testRunner/unittests/tsc/projectReferencesConfig.ts`** -> AI Confidence: **99.07%**
2086. **`src/testRunner/unittests/tscWatch/emit.ts`** -> AI Confidence: **99.07%**
2087. **`src/testRunner/unittests/tscWatch/incremental.ts`** -> AI Confidence: **99.07%**
2088. **`src/testRunner/unittests/tsserver/codeFix.ts`** -> AI Confidence: **99.07%**
2089. **`src/testRunner/unittests/tsserver/events/projectUpdatedInBackground.ts`** -> AI Confidence: **99.07%**
2090. **`src/testRunner/unittests/tsserver/exportMapCache.ts`** -> AI Confidence: **99.07%**
2091. **`src/testRunner/unittests/tsserver/externalProjects.ts`** -> AI Confidence: **99.07%**
2092. **`src/testRunner/unittests/tsserver/maxNodeModuleJsDepth.ts`** -> AI Confidence: **99.07%**
2093. **`src/testRunner/unittests/tsserver/projectErrors.ts`** -> AI Confidence: **99.07%**
2094. **`src/testRunner/unittests/tsserver/projectReferenceErrors.ts`** -> AI Confidence: **99.07%**
2095. **`src/testRunner/unittests/tsserver/rename.ts`** -> AI Confidence: **99.07%**
2096. **`src/testRunner/unittests/tsserver/symLinks.ts`** -> AI Confidence: **99.07%**
2097. **`tests/cases/conformance/nonjsExtensions/declarationFileForTsJsImport.ts`** -> AI Confidence: **99.07%**
2098. **`scripts/configurePrerelease.mjs`** -> AI Confidence: **99.06%**
2099. **`scripts/eslint/rules/debug-assert.cjs`** -> AI Confidence: **99.06%**
2100. **`scripts/eslint/rules/jsdoc-format.cjs`** -> AI Confidence: **99.06%**
2101. **`scripts/eslint/rules/no-in-operator.cjs`** -> AI Confidence: **99.06%**
2102. **`scripts/eslint/rules/no-keywords.cjs`** -> AI Confidence: **99.06%**
2103. **`scripts/eslint/rules/only-arrow-functions.cjs`** -> AI Confidence: **99.06%**
2104. **`scripts/run-sequence.mjs`** -> AI Confidence: **99.06%**
2105. **`tests/baselines/reference/APISample_jsdoc.js`** -> AI Confidence: **99.06%**
2106. **`tests/baselines/reference/APISample_linter.js`** -> AI Confidence: **99.06%**
2107. **`tests/baselines/reference/APISample_transform.js`** -> AI Confidence: **99.06%**
2108. **`tests/baselines/reference/ES3For-ofTypeCheck1(target=es2015).js`** -> AI Confidence: **99.06%**
2109. **`tests/baselines/reference/ES3For-ofTypeCheck2(target=es2015).js`** -> AI Confidence: **99.06%**
2110. **`tests/baselines/reference/ES3For-ofTypeCheck4(target=es2015).js`** -> AI Confidence: **99.06%**
2111. **`tests/baselines/reference/ES5For-of1(target=es2015).js`** -> AI Confidence: **99.06%**
2112. **`tests/baselines/reference/ES5For-of10(target=es2015).js`** -> AI Confidence: **99.06%**
2113. **`tests/baselines/reference/ES5For-of11(target=es2015).js`** -> AI Confidence: **99.06%**
2114. **`tests/baselines/reference/ES5For-of12(target=es5).js`** -> AI Confidence: **99.06%**
2115. **`tests/baselines/reference/ES5For-of14(target=es2015).js`** -> AI Confidence: **99.06%**
2116. **`tests/baselines/reference/ES5For-of15(target=es2015).js`** -> AI Confidence: **99.06%**
2117. **`tests/baselines/reference/ES5For-of18(target=es2015).js`** -> AI Confidence: **99.06%**
2118. **`tests/baselines/reference/ES5For-of19(alwaysstrict=false,target=es2015).js`** -> AI Confidence: **99.06%**
2119. **`tests/baselines/reference/ES5For-of19(alwaysstrict=true,target=es2015).js`** -> AI Confidence: **99.06%**
2120. **`tests/baselines/reference/ES5For-of21(target=es2015).js`** -> AI Confidence: **99.06%**
2121. **`tests/baselines/reference/ES5For-of26(target=es2015).js`** -> AI Confidence: **99.06%**
2122. **`tests/baselines/reference/ES5For-of26(target=es5).js`** -> AI Confidence: **99.06%**
2123. **`tests/baselines/reference/ES5For-of27(target=es2015).js`** -> AI Confidence: **99.06%**
2124. **`tests/baselines/reference/ES5For-of27(target=es5).js`** -> AI Confidence: **99.06%**
2125. **`tests/baselines/reference/ES5For-of28(target=es2015).js`** -> AI Confidence: **99.06%**
2126. **`tests/baselines/reference/ES5For-of28(target=es5).js`** -> AI Confidence: **99.06%**
2127. **`tests/baselines/reference/ES5For-of29(target=es5).js`** -> AI Confidence: **99.06%**
2128. **`tests/baselines/reference/ES5For-of31(target=es2015).js`** -> AI Confidence: **99.06%**
2129. **`tests/baselines/reference/ES5For-of31(target=es5).js`** -> AI Confidence: **99.06%**
2130. **`tests/baselines/reference/ES5For-of33(target=es2015).js`** -> AI Confidence: **99.06%**
2131. **`tests/baselines/reference/ES5For-of33(target=es5).js`** -> AI Confidence: **99.06%**
2132. **`tests/baselines/reference/ES5For-of34(target=es5).js`** -> AI Confidence: **99.06%**
2133. **`tests/baselines/reference/ES5For-of36(target=es2015).js`** -> AI Confidence: **99.06%**
2134. **`tests/baselines/reference/ES5For-of9(target=es2015).js`** -> AI Confidence: **99.06%**
2135. **`tests/baselines/reference/ES5For-ofTypeCheck1(target=es2015).js`** -> AI Confidence: **99.06%**
2136. **`tests/baselines/reference/ES5For-ofTypeCheck12(target=es5).js`** -> AI Confidence: **99.06%**
2137. **`tests/baselines/reference/ES5For-ofTypeCheck14(target=es2015).js`** -> AI Confidence: **99.06%**
2138. **`tests/baselines/reference/ES5For-ofTypeCheck2(target=es2015).js`** -> AI Confidence: **99.06%**
2139. **`tests/baselines/reference/ES5For-ofTypeCheck4(target=es2015).js`** -> AI Confidence: **99.06%**
2140. **`tests/baselines/reference/FunctionDeclaration7.js`** -> AI Confidence: **99.06%**
2141. **`tests/baselines/reference/SystemModuleForStatementNoInitializer.js`** -> AI Confidence: **99.06%**
2142. **`tests/baselines/reference/accessorInAmbientContextES5(target=es2015).js`** -> AI Confidence: **99.06%**
2143. **`tests/baselines/reference/accessorInAmbientContextES5(target=es5).js`** -> AI Confidence: **99.06%**
2144. **`tests/baselines/reference/allowImportClausesToMergeWithTypes.js`** -> AI Confidence: **99.06%**
2145. **`tests/baselines/reference/allowSyntheticDefaultImports10.js`** -> AI Confidence: **99.06%**
2146. **`tests/baselines/reference/allowSyntheticDefaultImports9.js`** -> AI Confidence: **99.06%**
2147. **`tests/baselines/reference/ambientConstLiterals.js`** -> AI Confidence: **99.06%**
2148. **`tests/baselines/reference/ambientShorthand.js`** -> AI Confidence: **99.06%**
2149. **`tests/baselines/reference/amdDependencyCommentName4.js`** -> AI Confidence: **99.06%**
2150. **`tests/baselines/reference/amdImportAsPrimaryExpression.js`** -> AI Confidence: **99.06%**
2151. **`tests/baselines/reference/anonymousDefaultExportsAmd.js`** -> AI Confidence: **99.06%**
2152. **`tests/baselines/reference/anonymousDefaultExportsCommonjs.js`** -> AI Confidence: **99.06%**
2153. **`tests/baselines/reference/anyAndUnknownHaveFalsyComponents.js`** -> AI Confidence: **99.06%**
2154. **`tests/baselines/reference/arbitraryModuleNamespaceIdentifiers_module(module=commonjs).js`** -> AI Confidence: **99.06%**
2155. **`tests/baselines/reference/arbitraryModuleNamespaceIdentifiers_module(module=node16).js`** -> AI Confidence: **99.06%**
2156. **`tests/baselines/reference/arbitraryModuleNamespaceIdentifiers_module(module=node18).js`** -> AI Confidence: **99.06%**
2157. **`tests/baselines/reference/arbitraryModuleNamespaceIdentifiers_module(module=node20).js`** -> AI Confidence: **99.06%**
2158. **`tests/baselines/reference/arbitraryModuleNamespaceIdentifiers_module(module=nodenext).js`** -> AI Confidence: **99.06%**
2159. **`tests/baselines/reference/arbitraryModuleNamespaceIdentifiers_module(module=none).js`** -> AI Confidence: **99.06%**
2160. **`tests/baselines/reference/arbitraryModuleNamespaceIdentifiers_module(module=umd).js`** -> AI Confidence: **99.06%**
2161. **`tests/baselines/reference/argumentsAsPropertyName.js`** -> AI Confidence: **99.06%**
2162. **`tests/baselines/reference/arrayDestructuringInSwitch1.js`** -> AI Confidence: **99.06%**
2163. **`tests/baselines/reference/arrayDestructuringInSwitch2.js`** -> AI Confidence: **99.06%**
2164. **`tests/baselines/reference/arrayEvery.js`** -> AI Confidence: **99.06%**
2165. **`tests/baselines/reference/arrayIterationLibES5TargetDifferent(nolib=false,target=es5).js`** -> AI Confidence: **99.06%**
2166. **`tests/baselines/reference/arrayIterationLibES5TargetDifferent(nolib=true,target=es5).js`** -> AI Confidence: **99.06%**
2167. **`tests/baselines/reference/arrayconcat.js`** -> AI Confidence: **99.06%**
2168. **`tests/baselines/reference/assertionFunctionWildcardImport2.js`** -> AI Confidence: **99.06%**
2169. **`tests/baselines/reference/assignFromNumberInterface2.js`** -> AI Confidence: **99.06%**
2170. **`tests/baselines/reference/assignFromStringInterface2.js`** -> AI Confidence: **99.06%**
2171. **`tests/baselines/reference/assignToEnum.js`** -> AI Confidence: **99.06%**
2172. **`tests/baselines/reference/asyncArrowFunction11_es5(target=es2015).js`** -> AI Confidence: **99.06%**
2173. **`tests/baselines/reference/asyncArrowFunction11_es5(target=es5).js`** -> AI Confidence: **99.06%**
2174. **`tests/baselines/reference/asyncEnum_es5(target=es2015).js`** -> AI Confidence: **99.06%**
2175. **`tests/baselines/reference/asyncEnum_es5(target=es5).js`** -> AI Confidence: **99.06%**
2176. **`tests/baselines/reference/asyncEnum_es6.js`** -> AI Confidence: **99.06%**
2177. **`tests/baselines/reference/asyncFunctionNoReturnType.js`** -> AI Confidence: **99.06%**
2178. **`tests/baselines/reference/asyncFunctionReturnExpressionErrorSpans.js`** -> AI Confidence: **99.06%**
2179. **`tests/baselines/reference/asyncFunctionTempVariableScoping(target=es2015).js`** -> AI Confidence: **99.06%**
2180. **`tests/baselines/reference/asyncFunctionWithForStatementNoInitializer.js`** -> AI Confidence: **99.06%**
2181. **`tests/baselines/reference/asyncFunctionsAcrossFiles.js`** -> AI Confidence: **99.06%**
2182. **`tests/baselines/reference/asyncFunctionsAndStrictNullChecks.js`** -> AI Confidence: **99.06%**
2183. **`tests/baselines/reference/asyncIIFE.js`** -> AI Confidence: **99.06%**
2184. **`tests/baselines/reference/asyncImportNestedYield.js`** -> AI Confidence: **99.06%**
2185. **`tests/baselines/reference/asyncImportedPromise_es5(target=es5).js`** -> AI Confidence: **99.06%**
2186. **`tests/baselines/reference/augmentExportEquals3.js`** -> AI Confidence: **99.06%**
2187. **`tests/baselines/reference/augmentExportEquals3_1.js`** -> AI Confidence: **99.06%**
2188. **`tests/baselines/reference/augmentExportEquals4.js`** -> AI Confidence: **99.06%**
2189. **`tests/baselines/reference/augmentExportEquals4_1.js`** -> AI Confidence: **99.06%**
2190. **`tests/baselines/reference/autoAccessor1(target=es2015).js`** -> AI Confidence: **99.06%**
2191. **`tests/baselines/reference/autoAccessor3(target=es2015).js`** -> AI Confidence: **99.06%**
2192. **`tests/baselines/reference/autoAccessor4(target=es2015).js`** -> AI Confidence: **99.06%**
2193. **`tests/baselines/reference/autoAccessor5(target=es2015).js`** -> AI Confidence: **99.06%**
2194. **`tests/baselines/reference/autoAccessor5(target=es5).js`** -> AI Confidence: **99.06%**
2195. **`tests/baselines/reference/autoAccessor6(target=es2015,usedefineforclassfields=false).js`** -> AI Confidence: **99.06%**
2196. **`tests/baselines/reference/autoAccessor6(target=es2015,usedefineforclassfields=true).js`** -> AI Confidence: **99.06%**
2197. **`tests/baselines/reference/autoAccessor7(target=es2015,usedefineforclassfields=false).js`** -> AI Confidence: **99.06%**
2198. **`tests/baselines/reference/autoAccessor7(target=es2015,usedefineforclassfields=true).js`** -> AI Confidence: **99.06%**
2199. **`tests/baselines/reference/autoAccessorExperimentalDecorators(target=es2022).js`** -> AI Confidence: **99.06%**
2200. **`tests/baselines/reference/autoAccessorExperimentalDecorators(target=esnext).js`** -> AI Confidence: **99.06%**
2201. **`tests/baselines/reference/autonumberingInEnums.js`** -> AI Confidence: **99.06%**
2202. **`tests/baselines/reference/awaitUsingDeclarations.1(target=es2015).js`** -> AI Confidence: **99.06%**
2203. **`tests/baselines/reference/awaitUsingDeclarations.1(target=es2017).js`** -> AI Confidence: **99.06%**
2204. **`tests/baselines/reference/awaitUsingDeclarations.1(target=es2022).js`** -> AI Confidence: **99.06%**
2205. **`tests/baselines/reference/awaitUsingDeclarations.1(target=es5).js`** -> AI Confidence: **99.06%**
2206. **`tests/baselines/reference/awaitUsingDeclarations.17.js`** -> AI Confidence: **99.06%**
2207. **`tests/baselines/reference/awaitUsingDeclarations.2(target=es2015).js`** -> AI Confidence: **99.06%**
2208. **`tests/baselines/reference/awaitUsingDeclarations.2(target=es2017).js`** -> AI Confidence: **99.06%**
2209. **`tests/baselines/reference/awaitUsingDeclarations.2(target=es2022).js`** -> AI Confidence: **99.06%**
2210. **`tests/baselines/reference/awaitUsingDeclarations.2(target=es5).js`** -> AI Confidence: **99.06%**
2211. **`tests/baselines/reference/awaitUsingDeclarations.3(target=es2015).js`** -> AI Confidence: **99.06%**
2212. **`tests/baselines/reference/awaitUsingDeclarations.3(target=es2017).js`** -> AI Confidence: **99.06%**
2213. **`tests/baselines/reference/awaitUsingDeclarations.3(target=es2022).js`** -> AI Confidence: **99.06%**
2214. **`tests/baselines/reference/awaitUsingDeclarationsInFor(target=es2017).js`** -> AI Confidence: **99.06%**
2215. **`tests/baselines/reference/awaitUsingDeclarationsInFor(target=es2022).js`** -> AI Confidence: **99.06%**
2216. **`tests/baselines/reference/awaitUsingDeclarationsInFor(target=esnext).js`** -> AI Confidence: **99.06%**
2217. **`tests/baselines/reference/awaitUsingDeclarationsInForAwaitOf(target=es2015).js`** -> AI Confidence: **99.06%**
2218. **`tests/baselines/reference/awaitUsingDeclarationsInForAwaitOf(target=es2017).js`** -> AI Confidence: **99.06%**
2219. **`tests/baselines/reference/awaitUsingDeclarationsInForAwaitOf(target=es2022).js`** -> AI Confidence: **99.06%**
2220. **`tests/baselines/reference/awaitUsingDeclarationsInForAwaitOf(target=es5).js`** -> AI Confidence: **99.06%**
2221. **`tests/baselines/reference/awaitUsingDeclarationsInForAwaitOf.3(target=es5).js`** -> AI Confidence: **99.06%**
2222. **`tests/baselines/reference/awaitUsingDeclarationsInForIn.js`** -> AI Confidence: **99.06%**
2223. **`tests/baselines/reference/awaitUsingDeclarationsInForOf.1(target=es2017).js`** -> AI Confidence: **99.06%**
2224. **`tests/baselines/reference/awaitUsingDeclarationsInForOf.1(target=es2022).js`** -> AI Confidence: **99.06%**
2225. **`tests/baselines/reference/awaitUsingDeclarationsInForOf.1(target=es5).js`** -> AI Confidence: **99.06%**
2226. **`tests/baselines/reference/awaitUsingDeclarationsInForOf.1(target=esnext).js`** -> AI Confidence: **99.06%**
2227. **`tests/baselines/reference/awaitUsingDeclarationsInForOf.2.js`** -> AI Confidence: **99.06%**
2228. **`tests/baselines/reference/awaitUsingDeclarationsInForOf.3.js`** -> AI Confidence: **99.06%**
2229. **`tests/baselines/reference/awaitUsingDeclarationsInForOf.4.js`** -> AI Confidence: **99.06%**
2230. **`tests/baselines/reference/awaitUsingDeclarationsInForOf.5(target=es5).js`** -> AI Confidence: **99.06%**
2231. **`tests/baselines/reference/awaitUsingDeclarationsWithImportHelpers.js`** -> AI Confidence: **99.06%**
2232. **`tests/baselines/reference/await_unaryExpression_es6.js`** -> AI Confidence: **99.06%**
2233. **`tests/baselines/reference/await_unaryExpression_es6_3.js`** -> AI Confidence: **99.06%**
2234. **`tests/baselines/reference/bigintMissingES2019.js`** -> AI Confidence: **99.06%**
2235. **`tests/baselines/reference/bigintMissingES2020.js`** -> AI Confidence: **99.06%**
2236. **`tests/baselines/reference/bigintMissingESNext.js`** -> AI Confidence: **99.06%**
2237. **`tests/baselines/reference/bindingPatternContextualTypeDoesNotCauseWidening.js`** -> AI Confidence: **99.06%**
2238. **`tests/baselines/reference/blockScopedBindingUsedBeforeDef.js`** -> AI Confidence: **99.06%**
2239. **`tests/baselines/reference/blockScopedBindingsInDownlevelGenerator(target=es2015).js`** -> AI Confidence: **99.06%**
2240. **`tests/baselines/reference/blockScopedBindingsReassignedInLoop2.js`** -> AI Confidence: **99.06%**
2241. **`tests/baselines/reference/blockScopedBindingsReassignedInLoop3.js`** -> AI Confidence: **99.06%**
2242. **`tests/baselines/reference/blockScopedBindingsReassignedInLoop5.js`** -> AI Confidence: **99.06%**
2243. **`tests/baselines/reference/blockScopedBindingsReassignedInLoop6.js`** -> AI Confidence: **99.06%**
2244. **`tests/baselines/reference/blockScopedFunctionDeclarationInStrictClass(target=es2015).js`** -> AI Confidence: **99.06%**
2245. **`tests/baselines/reference/blockScopedFunctionDeclarationInStrictModule.js`** -> AI Confidence: **99.06%**
2246. **`tests/baselines/reference/breakInIterationOrSwitchStatement4.js`** -> AI Confidence: **99.06%**
2247. **`tests/baselines/reference/callbackTagNestedParameter.js`** -> AI Confidence: **99.06%**
2248. **`tests/baselines/reference/capturedLetConstInLoop11.js`** -> AI Confidence: **99.06%**
2249. **`tests/baselines/reference/capturedLetConstInLoop11_ES6.js`** -> AI Confidence: **99.06%**
2250. **`tests/baselines/reference/capturedLetConstInLoop6.js`** -> AI Confidence: **99.06%**
2251. **`tests/baselines/reference/capturedLetConstInLoop6_ES6.js`** -> AI Confidence: **99.06%**
2252. **`tests/baselines/reference/capturedLetConstInLoop9.js`** -> AI Confidence: **99.06%**
2253. **`tests/baselines/reference/capturedLetConstInLoop9_ES6.js`** -> AI Confidence: **99.06%**
2254. **`tests/baselines/reference/castOfAwait.js`** -> AI Confidence: **99.06%**
2255. **`tests/baselines/reference/checkJsdocTypeTagOnExportAssignment1.js`** -> AI Confidence: **99.06%**
2256. **`tests/baselines/reference/checkJsdocTypeTagOnExportAssignment2.js`** -> AI Confidence: **99.06%**
2257. **`tests/baselines/reference/checkJsdocTypeTagOnExportAssignment3.js`** -> AI Confidence: **99.06%**
2258. **`tests/baselines/reference/checkJsdocTypeTagOnExportAssignment4.js`** -> AI Confidence: **99.06%**
2259. **`tests/baselines/reference/checkJsdocTypeTagOnExportAssignment5.js`** -> AI Confidence: **99.06%**
2260. **`tests/baselines/reference/checkJsdocTypeTagOnExportAssignment6.js`** -> AI Confidence: **99.06%**
2261. **`tests/baselines/reference/checkJsdocTypeTagOnExportAssignment7.js`** -> AI Confidence: **99.06%**
2262. **`tests/baselines/reference/checkJsdocTypeTagOnExportAssignment8.js`** -> AI Confidence: **99.06%**
2263. **`tests/baselines/reference/checkJsxNotSetError.js`** -> AI Confidence: **99.06%**
2264. **`tests/baselines/reference/checkSwitchStatementIfCaseTypeIsString.js`** -> AI Confidence: **99.06%**
2265. **`tests/baselines/reference/circularlyConstrainedMappedTypeContainingConditionalNoInfiniteInstantiationDepth.js`** -> AI Confidence: **99.06%**
2266. **`tests/baselines/reference/classMethodWithKeywordName1.js`** -> AI Confidence: **99.06%**
2267. **`tests/baselines/reference/classNameReferencesInStaticElements.js`** -> AI Confidence: **99.06%**
2268. **`tests/baselines/reference/classPropertyErrorOnNameOnly.js`** -> AI Confidence: **99.06%**
2269. **`tests/baselines/reference/classStaticBlock11(target=es2015).js`** -> AI Confidence: **99.06%**
2270. **`tests/baselines/reference/classStaticBlock12.js`** -> AI Confidence: **99.06%**
2271. **`tests/baselines/reference/classStaticBlock13(target=es2015).js`** -> AI Confidence: **99.06%**
2272. **`tests/baselines/reference/classStaticBlock17.js`** -> AI Confidence: **99.06%**
2273. **`tests/baselines/reference/classStaticBlock24(module=umd).js`** -> AI Confidence: **99.06%**
2274. **`tests/baselines/reference/classStaticBlock6(target=es5).js`** -> AI Confidence: **99.06%**
2275. **`tests/baselines/reference/classWithOptionalParameter.js`** -> AI Confidence: **99.06%**
2276. **`tests/baselines/reference/classWithStaticFieldInParameterInitializer(target=es5).js`** -> AI Confidence: **99.06%**
2277. **`tests/baselines/reference/coAndContraVariantInferences3.js`** -> AI Confidence: **99.06%**
2278. **`tests/baselines/reference/collisionCodeGenEnumWithEnumMemberConflict.js`** -> AI Confidence: **99.06%**
2279. **`tests/baselines/reference/collisionCodeGenModuleWithEnumMemberConflict.js`** -> AI Confidence: **99.06%**
2280. **`tests/baselines/reference/commentInNamespaceDeclarationWithIdentifierPathName.js`** -> AI Confidence: **99.06%**
2281. **`tests/baselines/reference/commentOnDecoratedClassDeclaration.js`** -> AI Confidence: **99.06%**
2282. **`tests/baselines/reference/comparabilityTypeParametersRelatedByUnion.js`** -> AI Confidence: **99.06%**
2283. **`tests/baselines/reference/computedEnumMemberSyntacticallyString(isolatedmodules=false).js`** -> AI Confidence: **99.06%**
2284. **`tests/baselines/reference/computedEnumMemberSyntacticallyString(isolatedmodules=true).js`** -> AI Confidence: **99.06%**
2285. **`tests/baselines/reference/computedPropertyNames46_ES5(target=es2015).js`** -> AI Confidence: **99.06%**
2286. **`tests/baselines/reference/computedPropertyNames46_ES6.js`** -> AI Confidence: **99.06%**
2287. **`tests/baselines/reference/computedPropertyNames47_ES5(target=es2015).js`** -> AI Confidence: **99.06%**
2288. **`tests/baselines/reference/computedPropertyNames47_ES6.js`** -> AI Confidence: **99.06%**
2289. **`tests/baselines/reference/computedPropertyNames48_ES5(target=es2015).js`** -> AI Confidence: **99.06%**
2290. **`tests/baselines/reference/computedPropertyNames48_ES6.js`** -> AI Confidence: **99.06%**
2291. **`tests/baselines/reference/conditionalExpression1.js`** -> AI Confidence: **99.06%**
2292. **`tests/baselines/reference/conditionalExpressionNewLine1.js`** -> AI Confidence: **99.06%**
2293. **`tests/baselines/reference/conditionalExpressionNewLine2.js`** -> AI Confidence: **99.06%**
2294. **`tests/baselines/reference/conditionalExpressionNewLine3.js`** -> AI Confidence: **99.06%**
2295. **`tests/baselines/reference/conditionalExpressionNewLine4.js`** -> AI Confidence: **99.06%**
2296. **`tests/baselines/reference/conditionalExpressionNewLine5.js`** -> AI Confidence: **99.06%**
2297. **`tests/baselines/reference/conditionalExpressionNewLine6.js`** -> AI Confidence: **99.06%**
2298. **`tests/baselines/reference/conditionalExpressionNewLine7.js`** -> AI Confidence: **99.06%**
2299. **`tests/baselines/reference/conditionalExpressions2.js`** -> AI Confidence: **99.06%**
2300. **`tests/baselines/reference/conditionalOperatorConditionIsBooleanType.js`** -> AI Confidence: **99.06%**
2301. **`tests/baselines/reference/conditionalOperatorConditionIsNumberType.js`** -> AI Confidence: **99.06%**
2302. **`tests/baselines/reference/conditionalOperatorConditionIsObjectType.js`** -> AI Confidence: **99.06%**
2303. **`tests/baselines/reference/conditionalOperatorConditoinIsAnyType.js`** -> AI Confidence: **99.06%**
2304. **`tests/baselines/reference/conditionalOperatorConditoinIsStringType.js`** -> AI Confidence: **99.06%**
2305. **`tests/baselines/reference/conditionalTypeVarianceBigArrayConstraintsPerformance.js`** -> AI Confidence: **99.06%**
2306. **`tests/baselines/reference/conditionalTypesASI.js`** -> AI Confidence: **99.06%**
2307. **`tests/baselines/reference/conditionalTypesExcessProperties.js`** -> AI Confidence: **99.06%**
2308. **`tests/baselines/reference/conflictMarkerDiff3Trivia1.js`** -> AI Confidence: **99.06%**
2309. **`tests/baselines/reference/conflictMarkerDiff3Trivia2.js`** -> AI Confidence: **99.06%**
2310. **`tests/baselines/reference/conflictingDeclarationsImportFromNamespace1.js`** -> AI Confidence: **99.06%**
2311. **`tests/baselines/reference/conflictingDeclarationsImportFromNamespace2.js`** -> AI Confidence: **99.06%**
2312. **`tests/baselines/reference/constDeclarations-access2.js`** -> AI Confidence: **99.06%**
2313. **`tests/baselines/reference/constDeclarations-access4.js`** -> AI Confidence: **99.06%**
2314. **`tests/baselines/reference/constDeclarations-scopes(alwaysstrict=false).js`** -> AI Confidence: **99.06%**
2315. **`tests/baselines/reference/constDeclarations-scopes(alwaysstrict=true).js`** -> AI Confidence: **99.06%**
2316. **`tests/baselines/reference/constDeclarations-validContexts(alwaysstrict=false).js`** -> AI Confidence: **99.06%**
2317. **`tests/baselines/reference/constDeclarations-validContexts(alwaysstrict=true).js`** -> AI Confidence: **99.06%**
2318. **`tests/baselines/reference/constEnumNamespaceReferenceCausesNoImport(isolatedmodules=false).js`** -> AI Confidence: **99.06%**
2319. **`tests/baselines/reference/constEnumNamespaceReferenceCausesNoImport(isolatedmodules=true).js`** -> AI Confidence: **99.06%**
2320. **`tests/baselines/reference/constEnumNamespaceReferenceCausesNoImport2.js`** -> AI Confidence: **99.06%**
2321. **`tests/baselines/reference/constEnumSyntheticNodesComments.js`** -> AI Confidence: **99.06%**
2322. **`tests/baselines/reference/constantEnumAssert.js`** -> AI Confidence: **99.06%**
2323. **`tests/baselines/reference/constructableDecoratorOnClass01.js`** -> AI Confidence: **99.06%**
2324. **`tests/baselines/reference/constructorOverloadsWithOptionalParameters.js`** -> AI Confidence: **99.06%**
2325. **`tests/baselines/reference/constructorWithParameterPropertiesAndPrivateFields.es2015.js`** -> AI Confidence: **99.06%**
2326. **`tests/baselines/reference/contextualExpressionTypecheckingDoesntBlowStack(target=es2015).js`** -> AI Confidence: **99.06%**
2327. **`tests/baselines/reference/contextualReturnTypeOfIIFE.js`** -> AI Confidence: **99.06%**
2328. **`tests/baselines/reference/contextualSigInstantiationRestParams.js`** -> AI Confidence: **99.06%**
2329. **`tests/baselines/reference/contextuallyTypedByDiscriminableUnion.js`** -> AI Confidence: **99.06%**
2330. **`tests/baselines/reference/continueInIterationStatement4.js`** -> AI Confidence: **99.06%**
2331. **`tests/baselines/reference/continueInLoopsWithCapturedBlockScopedBindings1(target=es2015).js`** -> AI Confidence: **99.06%**
2332. **`tests/baselines/reference/continueLabel.js`** -> AI Confidence: **99.06%**
2333. **`tests/baselines/reference/continueNotInIterationStatement4.js`** -> AI Confidence: **99.06%**
2334. **`tests/baselines/reference/controlFlowAliasing.js`** -> AI Confidence: **99.06%**
2335. **`tests/baselines/reference/controlFlowBinaryAndExpression.js`** -> AI Confidence: **99.06%**
2336. **`tests/baselines/reference/controlFlowBinaryOrExpression.js`** -> AI Confidence: **99.06%**
2337. **`tests/baselines/reference/controlFlowCommaExpressionAssertionWithinTernary.js`** -> AI Confidence: **99.06%**
2338. **`tests/baselines/reference/controlFlowCommaOperator.js`** -> AI Confidence: **99.06%**
2339. **`tests/baselines/reference/controlFlowElementAccess.js`** -> AI Confidence: **99.06%**
2340. **`tests/baselines/reference/controlFlowFinallyNoCatchAssignments.js`** -> AI Confidence: **99.06%**
2341. **`tests/baselines/reference/controlFlowForCatchAndFinally.js`** -> AI Confidence: **99.06%**
2342. **`tests/baselines/reference/controlFlowForInStatement.js`** -> AI Confidence: **99.06%**
2343. **`tests/baselines/reference/controlFlowForIndexSignatures.js`** -> AI Confidence: **99.06%**
2344. **`tests/baselines/reference/controlFlowForStatement.js`** -> AI Confidence: **99.06%**
2345. **`tests/baselines/reference/controlFlowIfStatement.js`** -> AI Confidence: **99.06%**
2346. **`tests/baselines/reference/controlFlowJavascript.js`** -> AI Confidence: **99.06%**
2347. **`tests/baselines/reference/controlFlowNoImplicitAny.js`** -> AI Confidence: **99.06%**
2348. **`tests/baselines/reference/controlFlowTruthiness.js`** -> AI Confidence: **99.06%**
2349. **`tests/baselines/reference/controlFlowWhileStatement.js`** -> AI Confidence: **99.06%**
2350. **`tests/baselines/reference/convertToAsyncFunction/convertToAsyncFunction_Conditionals.js`** -> AI Confidence: **99.06%**
2351. **`tests/baselines/reference/curiousNestedConditionalEvaluationResult.js`** -> AI Confidence: **99.06%**
2352. **`tests/baselines/reference/customTransforms/before+decorators.js`** -> AI Confidence: **99.06%**
2353. **`tests/baselines/reference/declFileEnums.js`** -> AI Confidence: **99.06%**
2354. **`tests/baselines/reference/declarationEmitAliasExportStar.js`** -> AI Confidence: **99.06%**
2355. **`tests/baselines/reference/declarationEmitAmdModuleNameDirective.js`** -> AI Confidence: **99.06%**
2356. **`tests/baselines/reference/declarationEmitCastReusesTypeNode5(strictnullchecks=false).js`** -> AI Confidence: **99.06%**
2357. **`tests/baselines/reference/declarationEmitCastReusesTypeNode5(strictnullchecks=true).js`** -> AI Confidence: **99.06%**
2358. **`tests/baselines/reference/declarationEmitComputedNameConstEnumAlias.js`** -> AI Confidence: **99.06%**
2359. **`tests/baselines/reference/declarationEmitDefaultExport5.js`** -> AI Confidence: **99.06%**
2360. **`tests/baselines/reference/declarationEmitDefaultExportWithTempVarName.js`** -> AI Confidence: **99.06%**
2361. **`tests/baselines/reference/declarationEmitDefaultExportWithTempVarNameWithBundling.js`** -> AI Confidence: **99.06%**
2362. **`tests/baselines/reference/declarationEmitExpressionInExtends6.js`** -> AI Confidence: **99.06%**
2363. **`tests/baselines/reference/declarationEmitInferredDefaultExportType.js`** -> AI Confidence: **99.06%**
2364. **`tests/baselines/reference/declarationEmitMappedTypeTemplateTypeofSymbol.js`** -> AI Confidence: **99.06%**
2365. **`tests/baselines/reference/declarationEmitMethodDeclaration.js`** -> AI Confidence: **99.06%**
2366. **`tests/baselines/reference/declarationEmitOfTypeofAliasedExport.js`** -> AI Confidence: **99.06%**
2367. **`tests/baselines/reference/declarationEmitOptionalMappedTypePropertyNoStrictNullChecks4.js`** -> AI Confidence: **99.06%**
2368. **`tests/baselines/reference/declarationEmitOptionalMethod.js`** -> AI Confidence: **99.06%**
2369. **`tests/baselines/reference/declarationEmitPrivateAsync.js`** -> AI Confidence: **99.06%**
2370. **`tests/baselines/reference/declarationEmitPromise.js`** -> AI Confidence: **99.06%**
2371. **`tests/baselines/reference/declarationEmitRetainedAnnotationRetainsImportInOutput.js`** -> AI Confidence: **99.06%**
2372. **`tests/baselines/reference/declarationEmitToDeclarationDirWithCompositeOption.js`** -> AI Confidence: **99.06%**
2373. **`tests/baselines/reference/declarationEmitToDeclarationDirWithDeclarationOption.js`** -> AI Confidence: **99.06%**
2374. **`tests/baselines/reference/declarationEmitToDeclarationDirWithoutCompositeAndDeclarationOptions.js`** -> AI Confidence: **99.06%**
2375. **`tests/baselines/reference/declarationEmitTypeofDefaultExport.js`** -> AI Confidence: **99.06%**
2376. **`tests/baselines/reference/declarationEmitWithComposite.js`** -> AI Confidence: **99.06%**
2377. **`tests/baselines/reference/declarationEmitWithDefaultAsComputedName(target=es2015).js`** -> AI Confidence: **99.06%**
2378. **`tests/baselines/reference/declarationEmitWithDefaultAsComputedName2(target=es2015).js`** -> AI Confidence: **99.06%**
2379. **`tests/baselines/reference/declarationEmitWithDefaultAsComputedName2(target=es5).js`** -> AI Confidence: **99.06%**
2380. **`tests/baselines/reference/declarationFileForJsonImport(resolvejsonmodule=false).js`** -> AI Confidence: **99.06%**
2381. **`tests/baselines/reference/declarationFileForJsonImport(resolvejsonmodule=true).js`** -> AI Confidence: **99.06%**
2382. **`tests/baselines/reference/decoratedBlockScopedClass1(target=es2015).js`** -> AI Confidence: **99.06%**
2383. **`tests/baselines/reference/decoratedBlockScopedClass1(target=es5).js`** -> AI Confidence: **99.06%**
2384. **`tests/baselines/reference/decoratedBlockScopedClass2(target=es2015).js`** -> AI Confidence: **99.06%**
2385. **`tests/baselines/reference/decoratedBlockScopedClass2(target=es5).js`** -> AI Confidence: **99.06%**
2386. **`tests/baselines/reference/decoratedBlockScopedClass3(target=es2015).js`** -> AI Confidence: **99.06%**
2387. **`tests/baselines/reference/decoratedBlockScopedClass3(target=es5).js`** -> AI Confidence: **99.06%**
2388. **`tests/baselines/reference/decoratedClassExportsCommonJS1.js`** -> AI Confidence: **99.06%**
2389. **`tests/baselines/reference/decoratedClassExportsCommonJS2.js`** -> AI Confidence: **99.06%**
2390. **`tests/baselines/reference/decoratedClassExportsSystem1.js`** -> AI Confidence: **99.06%**
2391. **`tests/baselines/reference/decoratedClassExportsSystem2.js`** -> AI Confidence: **99.06%**
2392. **`tests/baselines/reference/decoratedClassFromExternalModule.js`** -> AI Confidence: **99.06%**
2393. **`tests/baselines/reference/decoratedDefaultExportsGetExportedAmd.js`** -> AI Confidence: **99.06%**
2394. **`tests/baselines/reference/decoratedDefaultExportsGetExportedCommonjs.js`** -> AI Confidence: **99.06%**
2395. **`tests/baselines/reference/decoratedDefaultExportsGetExportedSystem.js`** -> AI Confidence: **99.06%**
2396. **`tests/baselines/reference/decoratedDefaultExportsGetExportedUmd.js`** -> AI Confidence: **99.06%**
2397. **`tests/baselines/reference/decoratorCallGeneric.js`** -> AI Confidence: **99.06%**
2398. **`tests/baselines/reference/decoratorChecksFunctionBodies(target=es2015).js`** -> AI Confidence: **99.06%**
2399. **`tests/baselines/reference/decoratorChecksFunctionBodies(target=es5).js`** -> AI Confidence: **99.06%**
2400. **`tests/baselines/reference/decoratorInstantiateModulesInFunctionBodies(target=es2015).js`** -> AI Confidence: **99.06%**
2401. **`tests/baselines/reference/decoratorInstantiateModulesInFunctionBodies(target=es5).js`** -> AI Confidence: **99.06%**
2402. **`tests/baselines/reference/decoratorMetadata(target=es2015).js`** -> AI Confidence: **99.06%**
2403. **`tests/baselines/reference/decoratorMetadata(target=es5).js`** -> AI Confidence: **99.06%**
2404. **`tests/baselines/reference/decoratorMetadata-jsdoc(target=es5).js`** -> AI Confidence: **99.06%**
2405. **`tests/baselines/reference/decoratorMetadataConditionalType.js`** -> AI Confidence: **99.06%**
2406. **`tests/baselines/reference/decoratorMetadataElidedImport(module=commonjs).js`** -> AI Confidence: **99.06%**
2407. **`tests/baselines/reference/decoratorMetadataElidedImport(module=esnext).js`** -> AI Confidence: **99.06%**
2408. **`tests/baselines/reference/decoratorMetadataElidedImportOnDeclare(module=commonjs).js`** -> AI Confidence: **99.06%**
2409. **`tests/baselines/reference/decoratorMetadataElidedImportOnDeclare(module=esnext).js`** -> AI Confidence: **99.06%**
2410. **`tests/baselines/reference/decoratorMetadataGenericTypeVariable.js`** -> AI Confidence: **99.06%**
2411. **`tests/baselines/reference/decoratorMetadataGenericTypeVariableDefault.js`** -> AI Confidence: **99.06%**
2412. **`tests/baselines/reference/decoratorMetadataGenericTypeVariableInScope.js`** -> AI Confidence: **99.06%**
2413. **`tests/baselines/reference/decoratorMetadataNoLibIsolatedModulesTypes.js`** -> AI Confidence: **99.06%**
2414. **`tests/baselines/reference/decoratorMetadataNoStrictNull.js`** -> AI Confidence: **99.06%**
2415. **`tests/baselines/reference/decoratorMetadataPromise.js`** -> AI Confidence: **99.06%**
2416. **`tests/baselines/reference/decoratorMetadataTypeOnlyExport.js`** -> AI Confidence: **99.06%**
2417. **`tests/baselines/reference/decoratorMetadataTypeOnlyImport.js`** -> AI Confidence: **99.06%**
2418. **`tests/baselines/reference/decoratorMetadataWithTypeOnlyImport(target=es2015).js`** -> AI Confidence: **99.06%**
2419. **`tests/baselines/reference/decoratorMetadataWithTypeOnlyImport(target=es5).js`** -> AI Confidence: **99.06%**
2420. **`tests/baselines/reference/decoratorMetadataWithTypeOnlyImport2.js`** -> AI Confidence: **99.06%**
2421. **`tests/baselines/reference/decoratorOnClass1(target=es2015).js`** -> AI Confidence: **99.06%**
2422. **`tests/baselines/reference/decoratorOnClass1(target=es5).js`** -> AI Confidence: **99.06%**
2423. **`tests/baselines/reference/decoratorOnClass1.es6.js`** -> AI Confidence: **99.06%**
2424. **`tests/baselines/reference/decoratorOnClass2(target=es2015).js`** -> AI Confidence: **99.06%**
2425. **`tests/baselines/reference/decoratorOnClass2(target=es5).js`** -> AI Confidence: **99.06%**
2426. **`tests/baselines/reference/decoratorOnClass2.es6.js`** -> AI Confidence: **99.06%**
2427. **`tests/baselines/reference/decoratorOnClass3(target=es2015).js`** -> AI Confidence: **99.06%**
2428. **`tests/baselines/reference/decoratorOnClass3(target=es5).js`** -> AI Confidence: **99.06%**
2429. **`tests/baselines/reference/decoratorOnClass3.es6.js`** -> AI Confidence: **99.06%**
2430. **`tests/baselines/reference/decoratorOnClass4(target=es2015).js`** -> AI Confidence: **99.06%**
2431. **`tests/baselines/reference/decoratorOnClass4(target=es5).js`** -> AI Confidence: **99.06%**
2432. **`tests/baselines/reference/decoratorOnClass4.es6.js`** -> AI Confidence: **99.06%**
2433. **`tests/baselines/reference/decoratorOnClass5(target=es2015).js`** -> AI Confidence: **99.06%**
2434. **`tests/baselines/reference/decoratorOnClass5(target=es5).js`** -> AI Confidence: **99.06%**
2435. **`tests/baselines/reference/decoratorOnClass5.es6.js`** -> AI Confidence: **99.06%**
2436. **`tests/baselines/reference/decoratorOnClass6.es6.js`** -> AI Confidence: **99.06%**
2437. **`tests/baselines/reference/decoratorOnClass7.es6.js`** -> AI Confidence: **99.06%**
2438. **`tests/baselines/reference/decoratorOnClass8(target=es2015).js`** -> AI Confidence: **99.06%**
2439. **`tests/baselines/reference/decoratorOnClass8(target=es5).js`** -> AI Confidence: **99.06%**
2440. **`tests/baselines/reference/decoratorOnClass8.es6.js`** -> AI Confidence: **99.06%**
2441. **`tests/baselines/reference/decoratorOnClass9(target=es2015).js`** -> AI Confidence: **99.06%**
2442. **`tests/baselines/reference/decoratorOnClass9(target=es5).js`** -> AI Confidence: **99.06%**
2443. **`tests/baselines/reference/decoratorOnClassAccessor1(target=es2015).js`** -> AI Confidence: **99.06%**
2444. **`tests/baselines/reference/decoratorOnClassAccessor1(target=es5).js`** -> AI Confidence: **99.06%**
2445. **`tests/baselines/reference/decoratorOnClassAccessor1.es6.js`** -> AI Confidence: **99.06%**
2446. **`tests/baselines/reference/decoratorOnClassAccessor2(target=es2015).js`** -> AI Confidence: **99.06%**
2447. **`tests/baselines/reference/decoratorOnClassAccessor2(target=es5).js`** -> AI Confidence: **99.06%**
2448. **`tests/baselines/reference/decoratorOnClassAccessor3(target=es2015).js`** -> AI Confidence: **99.06%**
2449. **`tests/baselines/reference/decoratorOnClassAccessor3(target=es5).js`** -> AI Confidence: **99.06%**
2450. **`tests/baselines/reference/decoratorOnClassAccessor4(target=es5).js`** -> AI Confidence: **99.06%**
2451. **`tests/baselines/reference/decoratorOnClassAccessor5(target=es5).js`** -> AI Confidence: **99.06%**
2452. **`tests/baselines/reference/decoratorOnClassAccessor6(target=es5).js`** -> AI Confidence: **99.06%**
2453. **`tests/baselines/reference/decoratorOnClassConstructor2(target=es5).js`** -> AI Confidence: **99.06%**
2454. **`tests/baselines/reference/decoratorOnClassConstructor3(target=es5).js`** -> AI Confidence: **99.06%**
2455. **`tests/baselines/reference/decoratorOnClassConstructor4(target=es2015).js`** -> AI Confidence: **99.06%**
2456. **`tests/baselines/reference/decoratorOnClassConstructor4(target=es5).js`** -> AI Confidence: **99.06%**
2457. **`tests/baselines/reference/decoratorOnClassConstructorParameter1(target=es2015).js`** -> AI Confidence: **99.06%**
2458. **`tests/baselines/reference/decoratorOnClassConstructorParameter1(target=es5).js`** -> AI Confidence: **99.06%**
2459. **`tests/baselines/reference/decoratorOnClassConstructorParameter4(target=es2015).js`** -> AI Confidence: **99.06%**
2460. **`tests/baselines/reference/decoratorOnClassConstructorParameter4(target=es5).js`** -> AI Confidence: **99.06%**
2461. **`tests/baselines/reference/decoratorOnClassMethod1(target=es5).js`** -> AI Confidence: **99.06%**
2462. **`tests/baselines/reference/decoratorOnClassMethod1.es6.js`** -> AI Confidence: **99.06%**
2463. **`tests/baselines/reference/decoratorOnClassMethod10(target=es5).js`** -> AI Confidence: **99.06%**
2464. **`tests/baselines/reference/decoratorOnClassMethod11(target=es2015).js`** -> AI Confidence: **99.06%**
2465. **`tests/baselines/reference/decoratorOnClassMethod11(target=es5).js`** -> AI Confidence: **99.06%**
2466. **`tests/baselines/reference/decoratorOnClassMethod12(target=es2015).js`** -> AI Confidence: **99.06%**
2467. **`tests/baselines/reference/decoratorOnClassMethod12(target=es5).js`** -> AI Confidence: **99.06%**
2468. **`tests/baselines/reference/decoratorOnClassMethod14.js`** -> AI Confidence: **99.06%**
2469. **`tests/baselines/reference/decoratorOnClassMethod15.js`** -> AI Confidence: **99.06%**
2470. **`tests/baselines/reference/decoratorOnClassMethod16.js`** -> AI Confidence: **99.06%**
2471. **`tests/baselines/reference/decoratorOnClassMethod17.js`** -> AI Confidence: **99.06%**
2472. **`tests/baselines/reference/decoratorOnClassMethod18.js`** -> AI Confidence: **99.06%**
2473. **`tests/baselines/reference/decoratorOnClassMethod19(target=es2015).js`** -> AI Confidence: **99.06%**
2474. **`tests/baselines/reference/decoratorOnClassMethod19(target=es2022).js`** -> AI Confidence: **99.06%**
2475. **`tests/baselines/reference/decoratorOnClassMethod19(target=esnext).js`** -> AI Confidence: **99.06%**
2476. **`tests/baselines/reference/decoratorOnClassMethod2(target=es5).js`** -> AI Confidence: **99.06%**
2477. **`tests/baselines/reference/decoratorOnClassMethod3(target=es5).js`** -> AI Confidence: **99.06%**
2478. **`tests/baselines/reference/decoratorOnClassMethod5.js`** -> AI Confidence: **99.06%**
2479. **`tests/baselines/reference/decoratorOnClassMethod6.js`** -> AI Confidence: **99.06%**
2480. **`tests/baselines/reference/decoratorOnClassMethod8(target=es5).js`** -> AI Confidence: **99.06%**
2481. **`tests/baselines/reference/decoratorOnClassMethodOverload2(target=es5).js`** -> AI Confidence: **99.06%**
2482. **`tests/baselines/reference/decoratorOnClassMethodParameter1(target=es2015).js`** -> AI Confidence: **99.06%**
2483. **`tests/baselines/reference/decoratorOnClassMethodParameter1(target=es5).js`** -> AI Confidence: **99.06%**
2484. **`tests/baselines/reference/decoratorOnClassMethodParameter1.es6.js`** -> AI Confidence: **99.06%**
2485. **`tests/baselines/reference/decoratorOnClassMethodParameter2(target=es2015).js`** -> AI Confidence: **99.06%**
2486. **`tests/baselines/reference/decoratorOnClassMethodParameter2(target=es5).js`** -> AI Confidence: **99.06%**
2487. **`tests/baselines/reference/decoratorOnClassMethodParameter3.js`** -> AI Confidence: **99.06%**
2488. **`tests/baselines/reference/decoratorOnClassMethodThisParameter(target=es2015).js`** -> AI Confidence: **99.06%**
2489. **`tests/baselines/reference/decoratorOnClassMethodThisParameter(target=es5).js`** -> AI Confidence: **99.06%**
2490. **`tests/baselines/reference/decoratorOnClassProperty1(target=es5).js`** -> AI Confidence: **99.06%**
2491. **`tests/baselines/reference/decoratorOnClassProperty1.es6.js`** -> AI Confidence: **99.06%**
2492. **`tests/baselines/reference/decoratorOnClassProperty10(target=es2015).js`** -> AI Confidence: **99.06%**
2493. **`tests/baselines/reference/decoratorOnClassProperty10(target=es5).js`** -> AI Confidence: **99.06%**
2494. **`tests/baselines/reference/decoratorOnClassProperty11(target=es2015).js`** -> AI Confidence: **99.06%**
2495. **`tests/baselines/reference/decoratorOnClassProperty11(target=es5).js`** -> AI Confidence: **99.06%**
2496. **`tests/baselines/reference/decoratorOnClassProperty12(target=es2015).js`** -> AI Confidence: **99.06%**
2497. **`tests/baselines/reference/decoratorOnClassProperty12(target=es5).js`** -> AI Confidence: **99.06%**
2498. **`tests/baselines/reference/decoratorOnClassProperty2(target=es5).js`** -> AI Confidence: **99.06%**
2499. **`tests/baselines/reference/decoratorOnClassProperty3(target=es5).js`** -> AI Confidence: **99.06%**
2500. **`tests/baselines/reference/decoratorOnClassProperty6(target=es5).js`** -> AI Confidence: **99.06%**
2501. **`tests/baselines/reference/decoratorOnClassProperty7(target=es5).js`** -> AI Confidence: **99.06%**
2502. **`tests/baselines/reference/decoratorOnEnum.js`** -> AI Confidence: **99.06%**
2503. **`tests/baselines/reference/decoratorOnEnum2.js`** -> AI Confidence: **99.06%**
2504. **`tests/baselines/reference/decoratorReferenceOnOtherProperty.js`** -> AI Confidence: **99.06%**
2505. **`tests/baselines/reference/decoratorReferences.js`** -> AI Confidence: **99.06%**
2506. **`tests/baselines/reference/decoratorWithNegativeLiteralTypeNoCrash(target=es5).js`** -> AI Confidence: **99.06%**
2507. **`tests/baselines/reference/deeplyNestedConditionalTypes.js`** -> AI Confidence: **99.06%**
2508. **`tests/baselines/reference/defaultDeclarationEmitShadowedNamedCorrectly.js`** -> AI Confidence: **99.06%**
2509. **`tests/baselines/reference/defaultExportInAwaitExpression02.js`** -> AI Confidence: **99.06%**
2510. **`tests/baselines/reference/defaultExportWithOverloads01(target=es2015).js`** -> AI Confidence: **99.06%**
2511. **`tests/baselines/reference/defaultExportWithOverloads01(target=es5).js`** -> AI Confidence: **99.06%**
2512. **`tests/baselines/reference/defaultExportsGetExportedAmd.js`** -> AI Confidence: **99.06%**
2513. **`tests/baselines/reference/defaultExportsGetExportedCommonjs.js`** -> AI Confidence: **99.06%**
2514. **`tests/baselines/reference/defaultIsNotVisibleInLocalScope.js`** -> AI Confidence: **99.06%**
2515. **`tests/baselines/reference/defaultKeywordWithoutExport1.js`** -> AI Confidence: **99.06%**
2516. **`tests/baselines/reference/defaultNamedExportWithType2.js`** -> AI Confidence: **99.06%**
2517. **`tests/baselines/reference/defaultNamedExportWithType4.js`** -> AI Confidence: **99.06%**
2518. **`tests/baselines/reference/defaultOfAnyInStrictNullChecks.js`** -> AI Confidence: **99.06%**
2519. **`tests/baselines/reference/defaultParameterAddsUndefinedWithStrictNullChecks.js`** -> AI Confidence: **99.06%**
2520. **`tests/baselines/reference/dependentDestructuredVariables.js`** -> AI Confidence: **99.06%**
2521. **`tests/baselines/reference/derivedInterfaceCallSignature.js`** -> AI Confidence: **99.06%**
2522. **`tests/baselines/reference/destructureOfVariableSameAsShorthand.js`** -> AI Confidence: **99.06%**
2523. **`tests/baselines/reference/destructuringAssignmentWithDefault.js`** -> AI Confidence: **99.06%**
2524. **`tests/baselines/reference/destructuringAssignmentWithStrictNullChecks.js`** -> AI Confidence: **99.06%**
2525. **`tests/baselines/reference/destructuringControlFlowNoCrash.js`** -> AI Confidence: **99.06%**
2526. **`tests/baselines/reference/destructuringInVariableDeclarations5.js`** -> AI Confidence: **99.06%**
2527. **`tests/baselines/reference/destructuringInVariableDeclarations6.js`** -> AI Confidence: **99.06%**
2528. **`tests/baselines/reference/destructuringObjectAssignmentPatternWithNestedSpread(target=es2015).js`** -> AI Confidence: **99.06%**
2529. **`tests/baselines/reference/destructuringObjectAssignmentPatternWithNestedSpread(target=es5).js`** -> AI Confidence: **99.06%**
2530. **`tests/baselines/reference/destructuringObjectBindingPatternAndAssignment5.js`** -> AI Confidence: **99.06%**
2531. **`tests/baselines/reference/destructuringParameterDeclaration1ES5.js`** -> AI Confidence: **99.06%**
2532. **`tests/baselines/reference/destructuringParameterDeclaration1ES5iterable.js`** -> AI Confidence: **99.06%**
2533. **`tests/baselines/reference/destructuringParameterDeclaration3ES5iterable(target=es5).js`** -> AI Confidence: **99.06%**
2534. **`tests/baselines/reference/destructuringParameterDeclaration7ES5iterable(target=es5).js`** -> AI Confidence: **99.06%**
2535. **`tests/baselines/reference/destructuringParameterProperties5.js`** -> AI Confidence: **99.06%**
2536. **`tests/baselines/reference/destructuringUnspreadableIntoRest.js`** -> AI Confidence: **99.06%**
2537. **`tests/baselines/reference/destructuringVariableDeclaration1ES5iterable(target=es5).js`** -> AI Confidence: **99.06%**
2538. **`tests/baselines/reference/destructuringWithConstraint.js`** -> AI Confidence: **99.06%**
2539. **`tests/baselines/reference/discriminantElementAccessCheck.js`** -> AI Confidence: **99.06%**
2540. **`tests/baselines/reference/doNotElaborateAssignabilityToTypeParameters(target=es2015).js`** -> AI Confidence: **99.06%**
2541. **`tests/baselines/reference/doWhileLoop.js`** -> AI Confidence: **99.06%**
2542. **`tests/baselines/reference/doubleUnderscoreExportStarConflict.js`** -> AI Confidence: **99.06%**
2543. **`tests/baselines/reference/downlevelIterationDeprecated(downleveliteration=true).js`** -> AI Confidence: **99.06%**
2544. **`tests/baselines/reference/downlevelLetConst17(target=es2015).js`** -> AI Confidence: **99.06%**
2545. **`tests/baselines/reference/downlevelLetConst17(target=es5).js`** -> AI Confidence: **99.06%**
2546. **`tests/baselines/reference/duplicateDefaultExport.js`** -> AI Confidence: **99.06%**
2547. **`tests/baselines/reference/duplicateIdentifierInCatchBlock.js`** -> AI Confidence: **99.06%**
2548. **`tests/baselines/reference/duplicateObjectLiteralProperty_computedName2.js`** -> AI Confidence: **99.06%**
2549. **`tests/baselines/reference/duplicatePackage_referenceTypes.js`** -> AI Confidence: **99.06%**
2550. **`tests/baselines/reference/duplicatePackage_subModule.js`** -> AI Confidence: **99.06%**
2551. **`tests/baselines/reference/dynamicImportInDefaultExportExpression.js`** -> AI Confidence: **99.06%**
2552. **`tests/baselines/reference/dynamicImportTrailingComma.js`** -> AI Confidence: **99.06%**
2553. **`tests/baselines/reference/dynamicImportWithNestedThis_es2015.js`** -> AI Confidence: **99.06%**
2554. **`tests/baselines/reference/dynamicImportWithNestedThis_es5(target=es2015).js`** -> AI Confidence: **99.06%**
2555. **`tests/baselines/reference/dynamicImportWithNestedThis_es5(target=es5).js`** -> AI Confidence: **99.06%**
2556. **`tests/baselines/reference/elidedJSImport2(module=commonjs).js`** -> AI Confidence: **99.06%**
2557. **`tests/baselines/reference/emitDecoratorMetadata_object(target=es2015).js`** -> AI Confidence: **99.06%**
2558. **`tests/baselines/reference/emitDecoratorMetadata_object(target=es5).js`** -> AI Confidence: **99.06%**
2559. **`tests/baselines/reference/emitDecoratorMetadata_restArgs(target=es2015).js`** -> AI Confidence: **99.06%**
2560. **`tests/baselines/reference/emitDecoratorMetadata_restArgs(target=es5).js`** -> AI Confidence: **99.06%**
2561. **`tests/baselines/reference/emitDefaultParametersFunction(target=es5).js`** -> AI Confidence: **99.06%**
2562. **`tests/baselines/reference/emitDefaultParametersFunctionProperty(target=es5).js`** -> AI Confidence: **99.06%**
2563. **`tests/baselines/reference/emitHelpersWithLocalCollisions(module=amd).js`** -> AI Confidence: **99.06%**
2564. **`tests/baselines/reference/emitHelpersWithLocalCollisions(module=commonjs).js`** -> AI Confidence: **99.06%**
2565. **`tests/baselines/reference/emitHelpersWithLocalCollisions(module=es2020).js`** -> AI Confidence: **99.06%**
2566. **`tests/baselines/reference/emitHelpersWithLocalCollisions(module=es2022).js`** -> AI Confidence: **99.06%**
2567. **`tests/baselines/reference/emitHelpersWithLocalCollisions(module=es6).js`** -> AI Confidence: **99.06%**
2568. **`tests/baselines/reference/emitHelpersWithLocalCollisions(module=esnext).js`** -> AI Confidence: **99.06%**
2569. **`tests/baselines/reference/emitHelpersWithLocalCollisions(module=node16).js`** -> AI Confidence: **99.06%**
2570. **`tests/baselines/reference/emitHelpersWithLocalCollisions(module=node18).js`** -> AI Confidence: **99.06%**
2571. **`tests/baselines/reference/emitHelpersWithLocalCollisions(module=node20).js`** -> AI Confidence: **99.06%**
2572. **`tests/baselines/reference/emitHelpersWithLocalCollisions(module=nodenext).js`** -> AI Confidence: **99.06%**
2573. **`tests/baselines/reference/emitHelpersWithLocalCollisions(module=none).js`** -> AI Confidence: **99.06%**
2574. **`tests/baselines/reference/emitHelpersWithLocalCollisions(module=preserve).js`** -> AI Confidence: **99.06%**
2575. **`tests/baselines/reference/emitHelpersWithLocalCollisions(module=system).js`** -> AI Confidence: **99.06%**
2576. **`tests/baselines/reference/emitHelpersWithLocalCollisions(module=umd).js`** -> AI Confidence: **99.06%**
2577. **`tests/baselines/reference/emitModuleCommonJS(module=commonjs).js`** -> AI Confidence: **99.06%**
2578. **`tests/baselines/reference/emitModuleCommonJS(module=nodenext).js`** -> AI Confidence: **99.06%**
2579. **`tests/baselines/reference/emitter.asyncGenerators.classMethods.es2015.js`** -> AI Confidence: **99.06%**
2580. **`tests/baselines/reference/emitter.asyncGenerators.classMethods.es5(target=es2015).js`** -> AI Confidence: **99.06%**
2581. **`tests/baselines/reference/emitter.asyncGenerators.classMethods.es5(target=es5).js`** -> AI Confidence: **99.06%**
2582. **`tests/baselines/reference/emitter.asyncGenerators.functionDeclarations.es2015.js`** -> AI Confidence: **99.06%**
2583. **`tests/baselines/reference/emitter.asyncGenerators.functionDeclarations.es5(target=es2015).js`** -> AI Confidence: **99.06%**
2584. **`tests/baselines/reference/emitter.asyncGenerators.functionDeclarations.es5(target=es5).js`** -> AI Confidence: **99.06%**
2585. **`tests/baselines/reference/emitter.asyncGenerators.functionExpressions.es2015.js`** -> AI Confidence: **99.06%**
2586. **`tests/baselines/reference/emitter.asyncGenerators.functionExpressions.es5(target=es2015).js`** -> AI Confidence: **99.06%**
2587. **`tests/baselines/reference/emitter.asyncGenerators.functionExpressions.es5(target=es5).js`** -> AI Confidence: **99.06%**
2588. **`tests/baselines/reference/emitter.asyncGenerators.objectLiteralMethods.es2015.js`** -> AI Confidence: **99.06%**
2589. **`tests/baselines/reference/emitter.asyncGenerators.objectLiteralMethods.es5(target=es2015).js`** -> AI Confidence: **99.06%**
2590. **`tests/baselines/reference/emitter.asyncGenerators.objectLiteralMethods.es5(target=es5).js`** -> AI Confidence: **99.06%**
2591. **`tests/baselines/reference/emitter.forAwait(target=es2015).js`** -> AI Confidence: **99.06%**
2592. **`tests/baselines/reference/emitter.forAwait(target=es2017).js`** -> AI Confidence: **99.06%**
2593. **`tests/baselines/reference/emitter.forAwait(target=es5).js`** -> AI Confidence: **99.06%**
2594. **`tests/baselines/reference/emptyAssignmentPatterns02_ES5iterable(target=es5).js`** -> AI Confidence: **99.06%**
2595. **`tests/baselines/reference/emptyAssignmentPatterns04_ES5iterable(target=es5).js`** -> AI Confidence: **99.06%**
2596. **`tests/baselines/reference/emptyEnum.js`** -> AI Confidence: **99.06%**
2597. **`tests/baselines/reference/emptyModuleName.js`** -> AI Confidence: **99.06%**
2598. **`tests/baselines/reference/emptyThenWarning.js`** -> AI Confidence: **99.06%**
2599. **`tests/baselines/reference/emptyThenWithoutWarning.js`** -> AI Confidence: **99.06%**
2600. **`tests/baselines/reference/emptyVariableDeclarationBindingPatterns01_ES5iterable(target=es5).js`** -> AI Confidence: **99.06%**
2601. **`tests/baselines/reference/emptyVariableDeclarationBindingPatterns02_ES5iterable(target=es5).js`** -> AI Confidence: **99.06%**
2602. **`tests/baselines/reference/enumBasics1.js`** -> AI Confidence: **99.06%**
2603. **`tests/baselines/reference/enumBasics2.js`** -> AI Confidence: **99.06%**
2604. **`tests/baselines/reference/enumClassification.js`** -> AI Confidence: **99.06%**
2605. **`tests/baselines/reference/enumCodeGenNewLines1.js`** -> AI Confidence: **99.06%**
2606. **`tests/baselines/reference/enumConstantMemberWithString.js`** -> AI Confidence: **99.06%**
2607. **`tests/baselines/reference/enumConstantMemberWithStringEmitDeclaration.js`** -> AI Confidence: **99.06%**
2608. **`tests/baselines/reference/enumConstantMemberWithTemplateLiterals.js`** -> AI Confidence: **99.06%**
2609. **`tests/baselines/reference/enumConstantMemberWithTemplateLiteralsEmitDeclaration.js`** -> AI Confidence: **99.06%**
2610. **`tests/baselines/reference/enumConstantMembers.js`** -> AI Confidence: **99.06%**
2611. **`tests/baselines/reference/enumErrorOnConstantBindingWithInitializer.js`** -> AI Confidence: **99.06%**
2612. **`tests/baselines/reference/enumIdentifierLiterals.js`** -> AI Confidence: **99.06%**
2613. **`tests/baselines/reference/enumLiteralTypes3.js`** -> AI Confidence: **99.06%**
2614. **`tests/baselines/reference/enumLiteralsSubtypeReduction.js`** -> AI Confidence: **99.06%**
2615. **`tests/baselines/reference/enumNegativeLiteral1.js`** -> AI Confidence: **99.06%**
2616. **`tests/baselines/reference/enumPropertyAccessBeforeInitalisation.js`** -> AI Confidence: **99.06%**
2617. **`tests/baselines/reference/enumUsedBeforeDeclaration.js`** -> AI Confidence: **99.06%**
2618. **`tests/baselines/reference/enumWithBigint.js`** -> AI Confidence: **99.06%**
2619. **`tests/baselines/reference/enumWithComputedMember.js`** -> AI Confidence: **99.06%**
2620. **`tests/baselines/reference/enumWithInfinityProperty.js`** -> AI Confidence: **99.06%**
2621. **`tests/baselines/reference/enumWithNaNProperty.js`** -> AI Confidence: **99.06%**
2622. **`tests/baselines/reference/enumWithNegativeInfinityProperty.js`** -> AI Confidence: **99.06%**
2623. **`tests/baselines/reference/enumWithParenthesizedInitializer1.js`** -> AI Confidence: **99.06%**
2624. **`tests/baselines/reference/enumWithPrimitiveName.js`** -> AI Confidence: **99.06%**
2625. **`tests/baselines/reference/enumWithQuotedElementName1.js`** -> AI Confidence: **99.06%**
2626. **`tests/baselines/reference/enumWithQuotedElementName2.js`** -> AI Confidence: **99.06%**
2627. **`tests/baselines/reference/enumWithUnicodeEscape1.js`** -> AI Confidence: **99.06%**
2628. **`tests/baselines/reference/enumWithoutInitializerAfterComputedMember.js`** -> AI Confidence: **99.06%**
2629. **`tests/baselines/reference/enumsWithMultipleDeclarations3.js`** -> AI Confidence: **99.06%**
2630. **`tests/baselines/reference/errorConstructorSubtypes.js`** -> AI Confidence: **99.06%**
2631. **`tests/baselines/reference/errorForConflictingExportEqualsValue.js`** -> AI Confidence: **99.06%**
2632. **`tests/baselines/reference/errorHandlingInInstanceOf.js`** -> AI Confidence: **99.06%**
2633. **`tests/baselines/reference/errorRecoveryWithDotFollowedByNamespaceKeyword.js`** -> AI Confidence: **99.06%**
2634. **`tests/baselines/reference/es2022IntlAPIs.js`** -> AI Confidence: **99.06%**
2635. **`tests/baselines/reference/es5-asyncFunction(target=es2015).js`** -> AI Confidence: **99.06%**
2636. **`tests/baselines/reference/es5-asyncFunctionDoStatements(target=es5).js`** -> AI Confidence: **99.06%**
2637. **`tests/baselines/reference/es5-asyncFunctionForInStatements(target=es5).js`** -> AI Confidence: **99.06%**
2638. **`tests/baselines/reference/es5-asyncFunctionForOfStatements(target=es2015).js`** -> AI Confidence: **99.06%**
2639. **`tests/baselines/reference/es5-asyncFunctionForOfStatements(target=es5).js`** -> AI Confidence: **99.06%**
2640. **`tests/baselines/reference/es5-asyncFunctionForStatements(target=es2015).js`** -> AI Confidence: **99.06%**
2641. **`tests/baselines/reference/es5-asyncFunctionForStatements(target=es5).js`** -> AI Confidence: **99.06%**
2642. **`tests/baselines/reference/es5-asyncFunctionIfStatements(target=es2015).js`** -> AI Confidence: **99.06%**
2643. **`tests/baselines/reference/es5-asyncFunctionIfStatements(target=es5).js`** -> AI Confidence: **99.06%**
2644. **`tests/baselines/reference/es5-asyncFunctionLongObjectLiteral(target=es5).js`** -> AI Confidence: **99.06%**
2645. **`tests/baselines/reference/es5-asyncFunctionNestedLoops(target=es5).js`** -> AI Confidence: **99.06%**
2646. **`tests/baselines/reference/es5-asyncFunctionSwitchStatements(target=es5).js`** -> AI Confidence: **99.06%**
2647. **`tests/baselines/reference/es5-asyncFunctionTryStatements(target=es2015).js`** -> AI Confidence: **99.06%**
2648. **`tests/baselines/reference/es5-asyncFunctionWhileStatements(target=es5).js`** -> AI Confidence: **99.06%**
2649. **`tests/baselines/reference/es5-commonjs2(target=es2015).js`** -> AI Confidence: **99.06%**
2650. **`tests/baselines/reference/es5-commonjs2(target=es5).js`** -> AI Confidence: **99.06%**
2651. **`tests/baselines/reference/es5-importHelpersAsyncFunctions(target=es2015).js`** -> AI Confidence: **99.06%**
2652. **`tests/baselines/reference/es5-importHelpersAsyncFunctions(target=es5).js`** -> AI Confidence: **99.06%**
2653. **`tests/baselines/reference/es5-oldStyleOctalLiteralInEnums(target=es2015).js`** -> AI Confidence: **99.06%**
2654. **`tests/baselines/reference/es5-oldStyleOctalLiteralInEnums(target=es5).js`** -> AI Confidence: **99.06%**
2655. **`tests/baselines/reference/es5-umd2(target=es2015).js`** -> AI Confidence: **99.06%**
2656. **`tests/baselines/reference/es5-umd3(target=es2015).js`** -> AI Confidence: **99.06%**
2657. **`tests/baselines/reference/es5-umd3(target=es5).js`** -> AI Confidence: **99.06%**
2658. **`tests/baselines/reference/es5ExportDefaultExpression(target=es2015).js`** -> AI Confidence: **99.06%**
2659. **`tests/baselines/reference/es5ExportDefaultExpression(target=es5).js`** -> AI Confidence: **99.06%**
2660. **`tests/baselines/reference/es5ExportDefaultFunctionDeclaration(target=es2015).js`** -> AI Confidence: **99.06%**
2661. **`tests/baselines/reference/es5ExportDefaultFunctionDeclaration(target=es5).js`** -> AI Confidence: **99.06%**
2662. **`tests/baselines/reference/es5ExportDefaultFunctionDeclaration2(target=es2015).js`** -> AI Confidence: **99.06%**
2663. **`tests/baselines/reference/es5ExportDefaultFunctionDeclaration2(target=es5).js`** -> AI Confidence: **99.06%**
2664. **`tests/baselines/reference/es6-umd2.js`** -> AI Confidence: **99.06%**
2665. **`tests/baselines/reference/es6ExportDefaultExpression.js`** -> AI Confidence: **99.06%**
2666. **`tests/baselines/reference/es6ExportDefaultFunctionDeclaration.js`** -> AI Confidence: **99.06%**
2667. **`tests/baselines/reference/es6ExportDefaultFunctionDeclaration2.js`** -> AI Confidence: **99.06%**
2668. **`tests/baselines/reference/es6ImportDefaultBindingFollowedWithNamespaceBindingDts.js`** -> AI Confidence: **99.06%**
2669. **`tests/baselines/reference/es6ImportDefaultBindingFollowedWithNamespaceBindingInEs5(target=es2015).js`** -> AI Confidence: **99.06%**
2670. **`tests/baselines/reference/es6ImportDefaultBindingFollowedWithNamespaceBindingInEs5(target=es5).js`** -> AI Confidence: **99.06%**
2671. **`tests/baselines/reference/es6ImportDefaultBindingFollowedWithNamespaceBindingWithExport.js`** -> AI Confidence: **99.06%**
2672. **`tests/baselines/reference/es6ImportEqualsExportModuleCommonJsError.js`** -> AI Confidence: **99.06%**
2673. **`tests/baselines/reference/es6ImportNameSpaceImport.js`** -> AI Confidence: **99.06%**
2674. **`tests/baselines/reference/es6ImportNameSpaceImportAmd.js`** -> AI Confidence: **99.06%**
2675. **`tests/baselines/reference/es6ImportNameSpaceImportDts.js`** -> AI Confidence: **99.06%**
2676. **`tests/baselines/reference/es6ImportNameSpaceImportInEs5(target=es2015).js`** -> AI Confidence: **99.06%**
2677. **`tests/baselines/reference/es6ImportNameSpaceImportInEs5(target=es5).js`** -> AI Confidence: **99.06%**
2678. **`tests/baselines/reference/es6ImportNameSpaceImportWithExport.js`** -> AI Confidence: **99.06%**
2679. **`tests/baselines/reference/es6modulekindWithES5Target11(target=es2015).js`** -> AI Confidence: **99.06%**
2680. **`tests/baselines/reference/es6modulekindWithES5Target11(target=es5).js`** -> AI Confidence: **99.06%**
2681. **`tests/baselines/reference/es6modulekindWithES5Target3(target=es2015).js`** -> AI Confidence: **99.06%**
2682. **`tests/baselines/reference/es6modulekindWithES5Target3(target=es5).js`** -> AI Confidence: **99.06%**
2683. **`tests/baselines/reference/esDecorators-classDeclaration-commonjs-classNamespaceMerge.js`** -> AI Confidence: **99.06%**
2684. **`tests/baselines/reference/esDecorators-classDeclaration-commonjs.js`** -> AI Confidence: **99.06%**
2685. **`tests/baselines/reference/esDecoratorsMetadata1(target=es2015).js`** -> AI Confidence: **99.06%**
2686. **`tests/baselines/reference/esDecoratorsMetadata1(target=es2022).js`** -> AI Confidence: **99.06%**
2687. **`tests/baselines/reference/esDecoratorsMetadata2(target=es2015).js`** -> AI Confidence: **99.06%**
2688. **`tests/baselines/reference/esDecoratorsMetadata2(target=es2022).js`** -> AI Confidence: **99.06%**
2689. **`tests/baselines/reference/esDecoratorsMetadata3(target=es2015).js`** -> AI Confidence: **99.06%**
2690. **`tests/baselines/reference/esDecoratorsMetadata3(target=es2022).js`** -> AI Confidence: **99.06%**
2691. **`tests/baselines/reference/esDecoratorsMetadata4(target=es2015).js`** -> AI Confidence: **99.06%**
2692. **`tests/baselines/reference/esDecoratorsMetadata4(target=es2022).js`** -> AI Confidence: **99.06%**
2693. **`tests/baselines/reference/esDecoratorsMetadata5.js`** -> AI Confidence: **99.06%**
2694. **`tests/baselines/reference/esModuleInteropDefaultMemberMustBeSyntacticallyDefaultExport.js`** -> AI Confidence: **99.06%**
2695. **`tests/baselines/reference/esModuleInteropImportCall.js`** -> AI Confidence: **99.06%**
2696. **`tests/baselines/reference/esModuleInteropImportNamespace.js`** -> AI Confidence: **99.06%**
2697. **`tests/baselines/reference/esModuleInteropNamedDefaultImports.js`** -> AI Confidence: **99.06%**
2698. **`tests/baselines/reference/esModuleInteropPrettyErrorRelatedInformation.js`** -> AI Confidence: **99.06%**
2699. **`tests/baselines/reference/esModuleInteropUsesExportStarWhenDefaultPlusNames.js`** -> AI Confidence: **99.06%**
2700. **`tests/baselines/reference/esModuleInteropWithExportStar(target=es2015).js`** -> AI Confidence: **99.06%**
2701. **`tests/baselines/reference/esModuleInteropWithExportStar(target=es5).js`** -> AI Confidence: **99.06%**
2702. **`tests/baselines/reference/esModuleIntersectionCrash.js`** -> AI Confidence: **99.06%**
2703. **`tests/baselines/reference/esnextmodulekindWithES5Target11(target=es2015).js`** -> AI Confidence: **99.06%**
2704. **`tests/baselines/reference/esnextmodulekindWithES5Target11(target=es5).js`** -> AI Confidence: **99.06%**
2705. **`tests/baselines/reference/esnextmodulekindWithES5Target3(target=es2015).js`** -> AI Confidence: **99.06%**
2706. **`tests/baselines/reference/esnextmodulekindWithES5Target3(target=es5).js`** -> AI Confidence: **99.06%**
2707. **`tests/baselines/reference/evolvingArrayResolvedAssert.js`** -> AI Confidence: **99.06%**
2708. **`tests/baselines/reference/exactSpellingSuggestion.js`** -> AI Confidence: **99.06%**
2709. **`tests/baselines/reference/excessPropertyCheckWithMultipleDiscriminants.js`** -> AI Confidence: **99.06%**
2710. **`tests/baselines/reference/exhaustiveSwitchImplicitReturn.js`** -> AI Confidence: **99.06%**
2711. **`tests/baselines/reference/exhaustiveSwitchStatements1.js`** -> AI Confidence: **99.06%**
2712. **`tests/baselines/reference/experimentalDecoratorMetadataUnresolvedTypeObjectInEmit.js`** -> AI Confidence: **99.06%**
2713. **`tests/baselines/reference/exportAndImport-es5(target=es2015).js`** -> AI Confidence: **99.06%**
2714. **`tests/baselines/reference/exportAndImport-es5(target=es5).js`** -> AI Confidence: **99.06%**
2715. **`tests/baselines/reference/exportAndImport-es5-amd(target=es2015).js`** -> AI Confidence: **99.06%**
2716. **`tests/baselines/reference/exportAndImport-es5-amd(target=es5).js`** -> AI Confidence: **99.06%**
2717. **`tests/baselines/reference/exportAsNamespace1(module=amd).js`** -> AI Confidence: **99.06%**
2718. **`tests/baselines/reference/exportAsNamespace1(module=commonjs).js`** -> AI Confidence: **99.06%**
2719. **`tests/baselines/reference/exportAsNamespace1(module=umd).js`** -> AI Confidence: **99.06%**
2720. **`tests/baselines/reference/exportAsNamespace2(module=amd).js`** -> AI Confidence: **99.06%**
2721. **`tests/baselines/reference/exportAsNamespace2(module=commonjs).js`** -> AI Confidence: **99.06%**
2722. **`tests/baselines/reference/exportAsNamespace2(module=umd).js`** -> AI Confidence: **99.06%**
2723. **`tests/baselines/reference/exportAsNamespace3(module=amd).js`** -> AI Confidence: **99.06%**
2724. **`tests/baselines/reference/exportAsNamespace3(module=commonjs).js`** -> AI Confidence: **99.06%**
2725. **`tests/baselines/reference/exportAsNamespace3(module=umd).js`** -> AI Confidence: **99.06%**
2726. **`tests/baselines/reference/exportAsNamespace_augment.js`** -> AI Confidence: **99.06%**
2727. **`tests/baselines/reference/exportAsNamespace_exportAssignment.js`** -> AI Confidence: **99.06%**
2728. **`tests/baselines/reference/exportAssignmentImportMergeNoCrash.js`** -> AI Confidence: **99.06%**
2729. **`tests/baselines/reference/exportClassNameWithObjectUMD(target=es2015).js`** -> AI Confidence: **99.06%**
2730. **`tests/baselines/reference/exportClassNameWithObjectUMD(target=es5).js`** -> AI Confidence: **99.06%**
2731. **`tests/baselines/reference/exportDeclarationsInAmbientNamespaces.js`** -> AI Confidence: **99.06%**
2732. **`tests/baselines/reference/exportDefaultAlias_excludesEverything.js`** -> AI Confidence: **99.06%**
2733. **`tests/baselines/reference/exportDefaultAsyncFunction.js`** -> AI Confidence: **99.06%**
2734. **`tests/baselines/reference/exportDefaultClassAndValue.js`** -> AI Confidence: **99.06%**
2735. **`tests/baselines/reference/exportDefaultDuplicateCrash.js`** -> AI Confidence: **99.06%**
2736. **`tests/baselines/reference/exportDefaultExpressionComments.js`** -> AI Confidence: **99.06%**
2737. **`tests/baselines/reference/exportDefaultFunctionInNamespace.js`** -> AI Confidence: **99.06%**
2738. **`tests/baselines/reference/exportDefaultInterfaceClassAndFunctionOverloads.js`** -> AI Confidence: **99.06%**
2739. **`tests/baselines/reference/exportDefaultInterfaceClassAndValue.js`** -> AI Confidence: **99.06%**
2740. **`tests/baselines/reference/exportDefaultMarksIdentifierAsUsed.js`** -> AI Confidence: **99.06%**
2741. **`tests/baselines/reference/exportDefaultMissingName.js`** -> AI Confidence: **99.06%**
2742. **`tests/baselines/reference/exportDefaultProperty.js`** -> AI Confidence: **99.06%**
2743. **`tests/baselines/reference/exportDefaultProperty2.js`** -> AI Confidence: **99.06%**
2744. **`tests/baselines/reference/exportDefaultQualifiedNameNoError.js`** -> AI Confidence: **99.06%**
2745. **`tests/baselines/reference/exportDefaultStripsFreshness.js`** -> AI Confidence: **99.06%**
2746. **`tests/baselines/reference/exportDefaultTypeClassAndValue.js`** -> AI Confidence: **99.06%**
2747. **`tests/baselines/reference/exportEqualsDefaultProperty.js`** -> AI Confidence: **99.06%**
2748. **`tests/baselines/reference/exportEqualsUmd.js`** -> AI Confidence: **99.06%**
2749. **`tests/baselines/reference/exportNamespace11.js`** -> AI Confidence: **99.06%**
2750. **`tests/baselines/reference/exportNamespace12.js`** -> AI Confidence: **99.06%**
2751. **`tests/baselines/reference/exportNonInitializedVariablesInIfThenStatementNoCrash1(module=commonjs).js`** -> AI Confidence: **99.06%**
2752. **`tests/baselines/reference/exportNonInitializedVariablesInIfThenStatementNoCrash1(module=esnext).js`** -> AI Confidence: **99.06%**
2753. **`tests/baselines/reference/exportNonInitializedVariablesInIfThenStatementNoCrash1(module=system).js`** -> AI Confidence: **99.06%**
2754. **`tests/baselines/reference/exportStar(target=es2015).js`** -> AI Confidence: **99.06%**
2755. **`tests/baselines/reference/exportStar(target=es5).js`** -> AI Confidence: **99.06%**
2756. **`tests/baselines/reference/exportStar-amd(target=es2015).js`** -> AI Confidence: **99.06%**
2757. **`tests/baselines/reference/exportStar-amd(target=es5).js`** -> AI Confidence: **99.06%**
2758. **`tests/baselines/reference/exportStarForValues.js`** -> AI Confidence: **99.06%**
2759. **`tests/baselines/reference/exportStarForValues2.js`** -> AI Confidence: **99.06%**
2760. **`tests/baselines/reference/exportStarForValues3.js`** -> AI Confidence: **99.06%**
2761. **`tests/baselines/reference/exportStarForValues5.js`** -> AI Confidence: **99.06%**
2762. **`tests/baselines/reference/exportStarForValues7.js`** -> AI Confidence: **99.06%**
2763. **`tests/baselines/reference/exportStarForValues8.js`** -> AI Confidence: **99.06%**
2764. **`tests/baselines/reference/exportTypeMergedWithExportStarAsNamespace.js`** -> AI Confidence: **99.06%**
2765. **`tests/baselines/reference/exportsAndImports4(target=es2015).js`** -> AI Confidence: **99.06%**
2766. **`tests/baselines/reference/exportsAndImports4(target=es5).js`** -> AI Confidence: **99.06%**
2767. **`tests/baselines/reference/exportsAndImports4-amd(target=es2015).js`** -> AI Confidence: **99.06%**
2768. **`tests/baselines/reference/exportsAndImports4-amd(target=es5).js`** -> AI Confidence: **99.06%**
2769. **`tests/baselines/reference/exportsAndImports4-es6.js`** -> AI Confidence: **99.06%**
2770. **`tests/baselines/reference/exportsAndImportsWithUnderscores1(target=es2015).js`** -> AI Confidence: **99.06%**
2771. **`tests/baselines/reference/exportsAndImportsWithUnderscores1(target=es5).js`** -> AI Confidence: **99.06%**
2772. **`tests/baselines/reference/exportsAndImportsWithUnderscores2(target=es2015).js`** -> AI Confidence: **99.06%**
2773. **`tests/baselines/reference/exportsAndImportsWithUnderscores2(target=es5).js`** -> AI Confidence: **99.06%**
2774. **`tests/baselines/reference/exportsAndImportsWithUnderscores3(target=es2015).js`** -> AI Confidence: **99.06%**
2775. **`tests/baselines/reference/exportsAndImportsWithUnderscores3(target=es5).js`** -> AI Confidence: **99.06%**
2776. **`tests/baselines/reference/expressionsForbiddenInParameterInitializers.js`** -> AI Confidence: **99.06%**
2777. **`tests/baselines/reference/extractConstant/extractConstant_BlockScopeMismatch.js`** -> AI Confidence: **99.06%**
2778. **`tests/baselines/reference/extractConstant/extractConstant_StatementInsertionPosition1.js`** -> AI Confidence: **99.06%**
2779. **`tests/baselines/reference/extractConstant/extractConstant_StatementInsertionPosition2.js`** -> AI Confidence: **99.06%**
2780. **`tests/baselines/reference/extractConstant/extractConstant_StatementInsertionPosition3.js`** -> AI Confidence: **99.06%**
2781. **`tests/baselines/reference/extractConstant/extractConstant_StatementInsertionPosition4.js`** -> AI Confidence: **99.06%**
2782. **`tests/baselines/reference/extractFunction/extractFunction22.js`** -> AI Confidence: **99.06%**
2783. **`tests/baselines/reference/flowAfterFinally1.js`** -> AI Confidence: **99.06%**
2784. **`tests/baselines/reference/flowControlTypeGuardThenSwitch.js`** -> AI Confidence: **99.06%**
2785. **`tests/baselines/reference/flowInFinally1.js`** -> AI Confidence: **99.06%**
2786. **`tests/baselines/reference/for-inStatementsAsyncIdentifier.js`** -> AI Confidence: **99.06%**
2787. **`tests/baselines/reference/for-inStatementsDestructuring(target=es2015).js`** -> AI Confidence: **99.06%**
2788. **`tests/baselines/reference/for-inStatementsDestructuring(target=es5).js`** -> AI Confidence: **99.06%**
2789. **`tests/baselines/reference/for-inStatementsDestructuring2.js`** -> AI Confidence: **99.06%**
2790. **`tests/baselines/reference/for-inStatementsDestructuring3.js`** -> AI Confidence: **99.06%**
2791. **`tests/baselines/reference/for-inStatementsDestructuring4.js`** -> AI Confidence: **99.06%**
2792. **`tests/baselines/reference/for-of1.js`** -> AI Confidence: **99.06%**
2793. **`tests/baselines/reference/for-of10.js`** -> AI Confidence: **99.06%**
2794. **`tests/baselines/reference/for-of11.js`** -> AI Confidence: **99.06%**
2795. **`tests/baselines/reference/for-of12.js`** -> AI Confidence: **99.06%**
2796. **`tests/baselines/reference/for-of13.js`** -> AI Confidence: **99.06%**
2797. **`tests/baselines/reference/for-of29.js`** -> AI Confidence: **99.06%**
2798. **`tests/baselines/reference/for-of3.js`** -> AI Confidence: **99.06%**
2799. **`tests/baselines/reference/for-of32.js`** -> AI Confidence: **99.06%**
2800. **`tests/baselines/reference/for-of4.js`** -> AI Confidence: **99.06%**
2801. **`tests/baselines/reference/for-of5.js`** -> AI Confidence: **99.06%**
2802. **`tests/baselines/reference/for-of50.js`** -> AI Confidence: **99.06%**
2803. **`tests/baselines/reference/for-of52.js`** -> AI Confidence: **99.06%**
2804. **`tests/baselines/reference/for-of6.js`** -> AI Confidence: **99.06%**
2805. **`tests/baselines/reference/for-of7.js`** -> AI Confidence: **99.06%**
2806. **`tests/baselines/reference/for-of8.js`** -> AI Confidence: **99.06%**
2807. **`tests/baselines/reference/for-of9.js`** -> AI Confidence: **99.06%**
2808. **`tests/baselines/reference/for.js`** -> AI Confidence: **99.06%**
2809. **`tests/baselines/reference/forAwaitForUnion.js`** -> AI Confidence: **99.06%**
2810. **`tests/baselines/reference/forAwaitPerIterationBindingDownlevel(target=es2015).js`** -> AI Confidence: **99.06%**
2811. **`tests/baselines/reference/forAwaitPerIterationBindingDownlevel(target=es5).js`** -> AI Confidence: **99.06%**
2812. **`tests/baselines/reference/forIn2.js`** -> AI Confidence: **99.06%**
2813. **`tests/baselines/reference/forInBreakStatements.js`** -> AI Confidence: **99.06%**
2814. **`tests/baselines/reference/forInContinueStatements.js`** -> AI Confidence: **99.06%**
2815. **`tests/baselines/reference/forInModule.js`** -> AI Confidence: **99.06%**
2816. **`tests/baselines/reference/forLoopEndingMultilineComments.js`** -> AI Confidence: **99.06%**
2817. **`tests/baselines/reference/forLoopWithDestructuringDoesNotElideFollowingStatement.js`** -> AI Confidence: **99.06%**
2818. **`tests/baselines/reference/forOfStringConstituents.js`** -> AI Confidence: **99.06%**
2819. **`tests/baselines/reference/forStatementInnerComments.js`** -> AI Confidence: **99.06%**
2820. **`tests/baselines/reference/forStatementsMultipleValidDecl.js`** -> AI Confidence: **99.06%**
2821. **`tests/baselines/reference/forwardRefInEnum.js`** -> AI Confidence: **99.06%**
2822. **`tests/baselines/reference/functionOverloads12.js`** -> AI Confidence: **99.06%**
2823. **`tests/baselines/reference/functionParameterObjectRestAndInitializers.js`** -> AI Confidence: **99.06%**
2824. **`tests/baselines/reference/functionWithMultipleReturnStatements.js`** -> AI Confidence: **99.06%**
2825. **`tests/baselines/reference/functionsWithImplicitReturnTypeAssignableToUndefined(strictnullchecks=false).js`** -> AI Confidence: **99.06%**
2826. **`tests/baselines/reference/functionsWithImplicitReturnTypeAssignableToUndefined(strictnullchecks=true).js`** -> AI Confidence: **99.06%**
2827. **`tests/baselines/reference/generatorNoImplicitReturns.js`** -> AI Confidence: **99.06%**
2828. **`tests/baselines/reference/generatorOverloads1.js`** -> AI Confidence: **99.06%**
2829. **`tests/baselines/reference/generatorOverloads5.js`** -> AI Confidence: **99.06%**
2830. **`tests/baselines/reference/generatorTransformFinalLabel(target=es2015).js`** -> AI Confidence: **99.06%**
2831. **`tests/baselines/reference/generatorTransformFinalLabel(target=es5).js`** -> AI Confidence: **99.06%**
2832. **`tests/baselines/reference/generatorTypeCheck39.js`** -> AI Confidence: **99.06%**
2833. **`tests/baselines/reference/generatorTypeCheck61.js`** -> AI Confidence: **99.06%**
2834. **`tests/baselines/reference/genericFunctionsWithOptionalParameters1.js`** -> AI Confidence: **99.06%**
2835. **`tests/baselines/reference/genericFunctionsWithOptionalParameters2.js`** -> AI Confidence: **99.06%**
2836. **`tests/baselines/reference/genericInferenceDefaultTypeParameterJsxReact.js`** -> AI Confidence: **99.06%**
2837. **`tests/baselines/reference/genericInstanceOf.js`** -> AI Confidence: **99.06%**
2838. **`tests/baselines/reference/genericObjectSpreadResultInSwitch.js`** -> AI Confidence: **99.06%**
2839. **`tests/baselines/reference/ifElseWithStatements1.js`** -> AI Confidence: **99.06%**
2840. **`tests/baselines/reference/implementArrayInterface.js`** -> AI Confidence: **99.06%**
2841. **`tests/baselines/reference/implicitAnyInCatch.js`** -> AI Confidence: **99.06%**
2842. **`tests/baselines/reference/importAttributes7.js`** -> AI Confidence: **99.06%**
2843. **`tests/baselines/reference/importCallExpressionAsyncES5AMD(target=es5).js`** -> AI Confidence: **99.06%**
2844. **`tests/baselines/reference/importCallExpressionAsyncES5CJS(target=es5).js`** -> AI Confidence: **99.06%**
2845. **`tests/baselines/reference/importCallExpressionAsyncES5System(target=es5).js`** -> AI Confidence: **99.06%**
2846. **`tests/baselines/reference/importCallExpressionAsyncES5UMD(target=es5).js`** -> AI Confidence: **99.06%**
2847. **`tests/baselines/reference/importCallExpressionES5UMD(target=es5).js`** -> AI Confidence: **99.06%**
2848. **`tests/baselines/reference/importCallExpressionGrammarError.js`** -> AI Confidence: **99.06%**
2849. **`tests/baselines/reference/importCallExpressionInAMD2.js`** -> AI Confidence: **99.06%**
2850. **`tests/baselines/reference/importCallExpressionInCJS3.js`** -> AI Confidence: **99.06%**
2851. **`tests/baselines/reference/importCallExpressionInExportEqualsAMD.js`** -> AI Confidence: **99.06%**
2852. **`tests/baselines/reference/importCallExpressionInExportEqualsCJS.js`** -> AI Confidence: **99.06%**
2853. **`tests/baselines/reference/importCallExpressionInExportEqualsUMD.js`** -> AI Confidence: **99.06%**
2854. **`tests/baselines/reference/importCallExpressionInScriptContext2.js`** -> AI Confidence: **99.06%**
2855. **`tests/baselines/reference/importCallExpressionInUMD1.js`** -> AI Confidence: **99.06%**
2856. **`tests/baselines/reference/importCallExpressionInUMD2.js`** -> AI Confidence: **99.06%**
2857. **`tests/baselines/reference/importCallExpressionInUMD3.js`** -> AI Confidence: **99.06%**
2858. **`tests/baselines/reference/importCallExpressionInUMD5.js`** -> AI Confidence: **99.06%**
2859. **`tests/baselines/reference/importCallExpressionNestedAMD.js`** -> AI Confidence: **99.06%**
2860. **`tests/baselines/reference/importCallExpressionNestedAMD2(target=es2015).js`** -> AI Confidence: **99.06%**
2861. **`tests/baselines/reference/importCallExpressionNestedAMD2(target=es5).js`** -> AI Confidence: **99.06%**
2862. **`tests/baselines/reference/importCallExpressionNestedCJS.js`** -> AI Confidence: **99.06%**
2863. **`tests/baselines/reference/importCallExpressionNestedCJS2(target=es2015).js`** -> AI Confidence: **99.06%**
2864. **`tests/baselines/reference/importCallExpressionNestedCJS2(target=es5).js`** -> AI Confidence: **99.06%**
2865. **`tests/baselines/reference/importCallExpressionNestedES2015.js`** -> AI Confidence: **99.06%**
2866. **`tests/baselines/reference/importCallExpressionNestedES20152(target=es2015).js`** -> AI Confidence: **99.06%**
2867. **`tests/baselines/reference/importCallExpressionNestedES2020.js`** -> AI Confidence: **99.06%**
2868. **`tests/baselines/reference/importCallExpressionNestedES20202(target=es2015).js`** -> AI Confidence: **99.06%**
2869. **`tests/baselines/reference/importCallExpressionNestedSystem.js`** -> AI Confidence: **99.06%**
2870. **`tests/baselines/reference/importCallExpressionNestedSystem2(target=es2015).js`** -> AI Confidence: **99.06%**
2871. **`tests/baselines/reference/importCallExpressionNestedSystem2(target=es5).js`** -> AI Confidence: **99.06%**
2872. **`tests/baselines/reference/importCallExpressionNestedUMD.js`** -> AI Confidence: **99.06%**
2873. **`tests/baselines/reference/importCallExpressionNestedUMD2(target=es2015).js`** -> AI Confidence: **99.06%**
2874. **`tests/baselines/reference/importCallExpressionWithTypeArgument.js`** -> AI Confidence: **99.06%**
2875. **`tests/baselines/reference/importDeferNamespace(module=commonjs).js`** -> AI Confidence: **99.06%**
2876. **`tests/baselines/reference/importDeferNamespace(module=nodenext).js`** -> AI Confidence: **99.06%**
2877. **`tests/baselines/reference/importEquals2.js`** -> AI Confidence: **99.06%**
2878. **`tests/baselines/reference/importEquals3.js`** -> AI Confidence: **99.06%**
2879. **`tests/baselines/reference/importHelpersNoEmitHelpersExportDefault(target=es2015).js`** -> AI Confidence: **99.06%**
2880. **`tests/baselines/reference/importHelpersNoEmitHelpersExportDefault(target=es5).js`** -> AI Confidence: **99.06%**
2881. **`tests/baselines/reference/importHelpersWithImportOrExportDefault(esmoduleinterop=false,module=amd).js`** -> AI Confidence: **99.06%**
2882. **`tests/baselines/reference/importHelpersWithImportOrExportDefault(esmoduleinterop=false,module=commonjs).js`** -> AI Confidence: **99.06%**
2883. **`tests/baselines/reference/importHelpersWithImportOrExportDefault(esmoduleinterop=false,module=system).js`** -> AI Confidence: **99.06%**
2884. **`tests/baselines/reference/importHelpersWithImportOrExportDefault(esmoduleinterop=true,module=amd).js`** -> AI Confidence: **99.06%**
2885. **`tests/baselines/reference/importHelpersWithImportOrExportDefault(esmoduleinterop=true,module=commonjs).js`** -> AI Confidence: **99.06%**
2886. **`tests/baselines/reference/importHelpersWithImportOrExportDefault(esmoduleinterop=true,module=system).js`** -> AI Confidence: **99.06%**
2887. **`tests/baselines/reference/importMeta(module=commonjs,target=es5).js`** -> AI Confidence: **99.06%**
2888. **`tests/baselines/reference/importMeta(module=system,target=es5).js`** -> AI Confidence: **99.06%**
2889. **`tests/baselines/reference/importsImplicitlyReadonly.js`** -> AI Confidence: **99.06%**
2890. **`tests/baselines/reference/inKeywordAndIntersection.js`** -> AI Confidence: **99.06%**
2891. **`tests/baselines/reference/inKeywordAndUnknown.js`** -> AI Confidence: **99.06%**
2892. **`tests/baselines/reference/indexerAsOptional.js`** -> AI Confidence: **99.06%**
2893. **`tests/baselines/reference/indexingTypesWithNever.js`** -> AI Confidence: **99.06%**
2894. **`tests/baselines/reference/inferredFunctionReturnTypeIsEmptyType.js`** -> AI Confidence: **99.06%**
2895. **`tests/baselines/reference/inferredIndexerOnNamespaceImport.js`** -> AI Confidence: **99.06%**
2896. **`tests/baselines/reference/inheritSameNamePropertiesWithDifferentOptionality.js`** -> AI Confidence: **99.06%**
2897. **`tests/baselines/reference/inlineConditionalHasSimilarAssignability.js`** -> AI Confidence: **99.06%**
2898. **`tests/baselines/reference/inlineJsxFactoryDeclarations.js`** -> AI Confidence: **99.06%**
2899. **`tests/baselines/reference/inlineJsxFactoryWithFragmentIsError.js`** -> AI Confidence: **99.06%**
2900. **`tests/baselines/reference/instanceofNarrowReadonlyArray.js`** -> AI Confidence: **99.06%**
2901. **`tests/baselines/reference/instanceofWithStructurallyIdenticalTypes.js`** -> AI Confidence: **99.06%**
2902. **`tests/baselines/reference/intersectionMemberOfUnionNarrowsCorrectly.js`** -> AI Confidence: **99.06%**
2903. **`tests/baselines/reference/invalidForInBreakStatements.js`** -> AI Confidence: **99.06%**
2904. **`tests/baselines/reference/invalidForInContinueStatements.js`** -> AI Confidence: **99.06%**
2905. **`tests/baselines/reference/invalidOptionalChainFromNewExpression.js`** -> AI Confidence: **99.06%**
2906. **`tests/baselines/reference/invalidSyntaxNamespaceImportWithCommonjs.js`** -> AI Confidence: **99.06%**
2907. **`tests/baselines/reference/invalidTaggedTemplateEscapeSequences(target=es2015).js`** -> AI Confidence: **99.06%**
2908. **`tests/baselines/reference/isArray.js`** -> AI Confidence: **99.06%**
2909. **`tests/baselines/reference/isolatedDeclarationErrorsDefault.js`** -> AI Confidence: **99.06%**
2910. **`tests/baselines/reference/isolatedDeclarationErrorsEnums.js`** -> AI Confidence: **99.06%**
2911. **`tests/baselines/reference/isolatedModulesExportDeclarationType.js`** -> AI Confidence: **99.06%**
2912. **`tests/baselines/reference/isolatedModulesImportExportElision(target=es5).js`** -> AI Confidence: **99.06%**
2913. **`tests/baselines/reference/jsDeclarationsCrossfileMerge(target=es2015).js`** -> AI Confidence: **99.06%**
2914. **`tests/baselines/reference/jsDeclarationsCrossfileMerge(target=es5).js`** -> AI Confidence: **99.06%**
2915. **`tests/baselines/reference/jsDeclarationsExportFormsErr(target=es2015).js`** -> AI Confidence: **99.06%**
2916. **`tests/baselines/reference/jsDeclarationsExportFormsErr(target=es5).js`** -> AI Confidence: **99.06%**
2917. **`tests/baselines/reference/jsDeclarationsFunctionWithDefaultAssignedMember.js`** -> AI Confidence: **99.06%**
2918. **`tests/baselines/reference/jsDeclarationsJson(target=es5).js`** -> AI Confidence: **99.06%**
2919. **`tests/baselines/reference/jsDeclarationsNestedParams.js`** -> AI Confidence: **99.06%**
2920. **`tests/baselines/reference/jsDeclarationsOptionalTypeLiteralProps1.js`** -> AI Confidence: **99.06%**
2921. **`tests/baselines/reference/jsDeclarationsPackageJson(target=es2015).js`** -> AI Confidence: **99.06%**
2922. **`tests/baselines/reference/jsDeclarationsPackageJson(target=es5).js`** -> AI Confidence: **99.06%**
2923. **`tests/baselines/reference/jsDeclarationsReactComponents(target=es2015).js`** -> AI Confidence: **99.06%**
2924. **`tests/baselines/reference/jsDeclarationsReexportAliases(target=es2015).js`** -> AI Confidence: **99.06%**
2925. **`tests/baselines/reference/jsFileCompilationLetBeingRenamed.js`** -> AI Confidence: **99.06%**
2926. **`tests/baselines/reference/jsFileCompilationRestParamJsDocFunction.js`** -> AI Confidence: **99.06%**
2927. **`tests/baselines/reference/jsxChildrenSingleChildConfusableWithMultipleChildrenNoError.js`** -> AI Confidence: **99.06%**
2928. **`tests/baselines/reference/jsxElementTypeLiteral.js`** -> AI Confidence: **99.06%**
2929. **`tests/baselines/reference/jsxElementTypeLiteralWithGeneric.js`** -> AI Confidence: **99.06%**
2930. **`tests/baselines/reference/jsxEmptyExpressionNotCountedAsChild(jsx=react).js`** -> AI Confidence: **99.06%**
2931. **`tests/baselines/reference/jsxExcessPropsAndAssignability.js`** -> AI Confidence: **99.06%**
2932. **`tests/baselines/reference/jsxImportInAttribute.js`** -> AI Confidence: **99.06%**
2933. **`tests/baselines/reference/jsxIntrinsicUnions.js`** -> AI Confidence: **99.06%**
2934. **`tests/baselines/reference/jsxNamespaceReexports.js`** -> AI Confidence: **99.06%**
2935. **`tests/baselines/reference/jsxPropsAsIdentifierNames.js`** -> AI Confidence: **99.06%**
2936. **`tests/baselines/reference/keyofModuleObjectHasCorrectKeys.js`** -> AI Confidence: **99.06%**
2937. **`tests/baselines/reference/keywordField.js`** -> AI Confidence: **99.06%**
2938. **`tests/baselines/reference/labeledStatementWithLabel.js`** -> AI Confidence: **99.06%**
2939. **`tests/baselines/reference/labeledStatementWithLabel_es2015.js`** -> AI Confidence: **99.06%**
2940. **`tests/baselines/reference/labeledStatementWithLabel_strict.js`** -> AI Confidence: **99.06%**
2941. **`tests/baselines/reference/letConstInCaseClauses(target=es2015).js`** -> AI Confidence: **99.06%**
2942. **`tests/baselines/reference/letConstInCaseClauses(target=es5).js`** -> AI Confidence: **99.06%**
2943. **`tests/baselines/reference/localVariablesReturnedFromCatchBlocks.js`** -> AI Confidence: **99.06%**
2944. **`tests/baselines/reference/logicalAndOperatorWithEveryType.js`** -> AI Confidence: **99.06%**
2945. **`tests/baselines/reference/logicalAndOperatorWithTypeParameters.js`** -> AI Confidence: **99.06%**
2946. **`tests/baselines/reference/logicalAssignment10(target=es2015).js`** -> AI Confidence: **99.06%**
2947. **`tests/baselines/reference/logicalAssignment10(target=es2020).js`** -> AI Confidence: **99.06%**
2948. **`tests/baselines/reference/logicalAssignment10(target=es2021).js`** -> AI Confidence: **99.06%**
2949. **`tests/baselines/reference/logicalAssignment10(target=esnext).js`** -> AI Confidence: **99.06%**
2950. **`tests/baselines/reference/logicalAssignment5(target=es2015).js`** -> AI Confidence: **99.06%**
2951. **`tests/baselines/reference/logicalAssignment5(target=es2020).js`** -> AI Confidence: **99.06%**
2952. **`tests/baselines/reference/logicalAssignment5(target=es2021).js`** -> AI Confidence: **99.06%**
2953. **`tests/baselines/reference/logicalAssignment5(target=esnext).js`** -> AI Confidence: **99.06%**
2954. **`tests/baselines/reference/logicalOrExpressionIsContextuallyTyped.js`** -> AI Confidence: **99.06%**
2955. **`tests/baselines/reference/logicalOrOperatorWithEveryType.js`** -> AI Confidence: **99.06%**
2956. **`tests/baselines/reference/logicalOrOperatorWithTypeParameters.js`** -> AI Confidence: **99.06%**
2957. **`tests/baselines/reference/mappedTypeCircularReferenceInAccessor.js`** -> AI Confidence: **99.06%**
2958. **`tests/baselines/reference/mappedTypeNoTypeNoCrash.js`** -> AI Confidence: **99.06%**
2959. **`tests/baselines/reference/mappedTypeOverlappingStringEnumKeys.js`** -> AI Confidence: **99.06%**
2960. **`tests/baselines/reference/mappedTypeWithAsClauseAndLateBoundProperty2.js`** -> AI Confidence: **99.06%**
2961. **`tests/baselines/reference/memberFunctionsWithPublicOverloads.js`** -> AI Confidence: **99.06%**
2962. **`tests/baselines/reference/memberFunctionsWithPublicPrivateOverloads.js`** -> AI Confidence: **99.06%**
2963. **`tests/baselines/reference/mergeMultipleInterfacesReexported.js`** -> AI Confidence: **99.06%**
2964. **`tests/baselines/reference/mergedDeclarations2.js`** -> AI Confidence: **99.06%**
2965. **`tests/baselines/reference/mergedDeclarations7.js`** -> AI Confidence: **99.06%**
2966. **`tests/baselines/reference/mergedEnumDeclarationCodeGen.js`** -> AI Confidence: **99.06%**
2967. **`tests/baselines/reference/mergedModuleDeclarationCodeGen2.js`** -> AI Confidence: **99.06%**
2968. **`tests/baselines/reference/mergedModuleDeclarationCodeGen3.js`** -> AI Confidence: **99.06%**
2969. **`tests/baselines/reference/metadataImportType.js`** -> AI Confidence: **99.06%**
2970. **`tests/baselines/reference/metadataOfClassFromAlias(strict=false,target=es2015).js`** -> AI Confidence: **99.06%**
2971. **`tests/baselines/reference/metadataOfClassFromAlias(strict=false,target=es5).js`** -> AI Confidence: **99.06%**
2972. **`tests/baselines/reference/metadataOfClassFromAlias(strict=true,target=es2015).js`** -> AI Confidence: **99.06%**
2973. **`tests/baselines/reference/metadataOfClassFromAlias(strict=true,target=es5).js`** -> AI Confidence: **99.06%**
2974. **`tests/baselines/reference/metadataOfClassFromAlias2(target=es2015).js`** -> AI Confidence: **99.06%**
2975. **`tests/baselines/reference/metadataOfClassFromAlias2(target=es5).js`** -> AI Confidence: **99.06%**
2976. **`tests/baselines/reference/metadataOfClassFromModule(target=es2015).js`** -> AI Confidence: **99.06%**
2977. **`tests/baselines/reference/metadataOfClassFromModule(target=es5).js`** -> AI Confidence: **99.06%**
2978. **`tests/baselines/reference/metadataOfEventAlias(target=es2015).js`** -> AI Confidence: **99.06%**
2979. **`tests/baselines/reference/metadataOfEventAlias(target=es5).js`** -> AI Confidence: **99.06%**
2980. **`tests/baselines/reference/metadataOfUnion.js`** -> AI Confidence: **99.06%**
2981. **`tests/baselines/reference/metadataOfUnionWithNull(strictnullchecks=false).js`** -> AI Confidence: **99.06%**
2982. **`tests/baselines/reference/metadataOfUnionWithNull(strictnullchecks=true).js`** -> AI Confidence: **99.06%**
2983. **`tests/baselines/reference/metadataReferencedWithinFilteredUnion(strictnullchecks=false,target=es2015).js`** -> AI Confidence: **99.06%**
2984. **`tests/baselines/reference/metadataReferencedWithinFilteredUnion(strictnullchecks=false,target=es5).js`** -> AI Confidence: **99.06%**
2985. **`tests/baselines/reference/metadataReferencedWithinFilteredUnion(strictnullchecks=true,target=es2015).js`** -> AI Confidence: **99.06%**
2986. **`tests/baselines/reference/metadataReferencedWithinFilteredUnion(strictnullchecks=true,target=es5).js`** -> AI Confidence: **99.06%**
2987. **`tests/baselines/reference/methodSignaturesWithOverloads.js`** -> AI Confidence: **99.06%**
2988. **`tests/baselines/reference/methodSignaturesWithOverloads2.js`** -> AI Confidence: **99.06%**
2989. **`tests/baselines/reference/missingDecoratorType(target=es5).js`** -> AI Confidence: **99.06%**
2990. **`tests/baselines/reference/moduleAugmentationDoesInterfaceMergeOfReexport.js`** -> AI Confidence: **99.06%**
2991. **`tests/baselines/reference/moduleAugmentationDoesNamespaceEnumMergeOfReexport.js`** -> AI Confidence: **99.06%**
2992. **`tests/baselines/reference/moduleAugmentationDoesNamespaceMergeOfReexport.js`** -> AI Confidence: **99.06%**
2993. **`tests/baselines/reference/moduleAugmentationEnumClassMergeOfReexportIsError.js`** -> AI Confidence: **99.06%**
2994. **`tests/baselines/reference/moduleMergeConstructor.js`** -> AI Confidence: **99.06%**
2995. **`tests/baselines/reference/moduleNoEmit.js`** -> AI Confidence: **99.06%**
2996. **`tests/baselines/reference/moduleNoneDynamicImport(target=es2015).js`** -> AI Confidence: **99.06%**
2997. **`tests/baselines/reference/modulePrologueUmd.js`** -> AI Confidence: **99.06%**
2998. **`tests/baselines/reference/moduleResolution/reused-program-keeps-errors.js`** -> AI Confidence: **99.06%**
2999. **`tests/baselines/reference/moduleResolution/two-files-used-in-program-differ-only-in-casing-(tripleslash-references).js`** -> AI Confidence: **99.06%**
3000. **`tests/baselines/reference/moduleResolutionWithModule(module=commonjs,moduleresolution=node16).js`** -> AI Confidence: **99.06%**
3001. **`tests/baselines/reference/moduleResolutionWithModule(module=commonjs,moduleresolution=nodenext).js`** -> AI Confidence: **99.06%**
3002. **`tests/baselines/reference/moduleResolutionWithModule(module=node16,moduleresolution=node16).js`** -> AI Confidence: **99.06%**
3003. **`tests/baselines/reference/moduleResolutionWithModule(module=node16,moduleresolution=nodenext).js`** -> AI Confidence: **99.06%**
3004. **`tests/baselines/reference/moduleResolutionWithModule(module=node18,moduleresolution=node16).js`** -> AI Confidence: **99.06%**
3005. **`tests/baselines/reference/moduleResolutionWithModule(module=node18,moduleresolution=nodenext).js`** -> AI Confidence: **99.06%**
3006. **`tests/baselines/reference/moduleResolutionWithModule(module=node20,moduleresolution=node16).js`** -> AI Confidence: **99.06%**
3007. **`tests/baselines/reference/moduleResolutionWithModule(module=node20,moduleresolution=nodenext).js`** -> AI Confidence: **99.06%**
3008. **`tests/baselines/reference/moduleResolutionWithModule(module=nodenext,moduleresolution=node16).js`** -> AI Confidence: **99.06%**
3009. **`tests/baselines/reference/moduleResolutionWithModule(module=nodenext,moduleresolution=nodenext).js`** -> AI Confidence: **99.06%**
3010. **`tests/baselines/reference/moduleResolutionWithSuffixes_one_jsonModule.js`** -> AI Confidence: **99.06%**
3011. **`tests/baselines/reference/moduleSameValueDuplicateExportedBindings1.js`** -> AI Confidence: **99.06%**
3012. **`tests/baselines/reference/moduleSameValueDuplicateExportedBindings2.js`** -> AI Confidence: **99.06%**
3013. **`tests/baselines/reference/moduleWithTryStatement1.js`** -> AI Confidence: **99.06%**
3014. **`tests/baselines/reference/multiCallOverloads.js`** -> AI Confidence: **99.06%**
3015. **`tests/baselines/reference/multiline.js`** -> AI Confidence: **99.06%**
3016. **`tests/baselines/reference/multipleDefaultExports01(target=es2015).js`** -> AI Confidence: **99.06%**
3017. **`tests/baselines/reference/multipleDefaultExports01(target=es5).js`** -> AI Confidence: **99.06%**
3018. **`tests/baselines/reference/multipleDefaultExports02(target=es2015).js`** -> AI Confidence: **99.06%**
3019. **`tests/baselines/reference/multipleDefaultExports02(target=es5).js`** -> AI Confidence: **99.06%**
3020. **`tests/baselines/reference/multipleDefaultExports04(target=es2015).js`** -> AI Confidence: **99.06%**
3021. **`tests/baselines/reference/multipleDefaultExports04(target=es5).js`** -> AI Confidence: **99.06%**
3022. **`tests/baselines/reference/multipleExportDefault3.js`** -> AI Confidence: **99.06%**
3023. **`tests/baselines/reference/multipleExportDefault4.js`** -> AI Confidence: **99.06%**
3024. **`tests/baselines/reference/multipleExportDefault5.js`** -> AI Confidence: **99.06%**
3025. **`tests/baselines/reference/multipleExportDefault6.js`** -> AI Confidence: **99.06%**
3026. **`tests/baselines/reference/namespaceMemberAccess.js`** -> AI Confidence: **99.06%**
3027. **`tests/baselines/reference/namespaceMergedWithFunctionWithOverloadsUsage.js`** -> AI Confidence: **99.06%**
3028. **`tests/baselines/reference/narrowByInstanceof.js`** -> AI Confidence: **99.06%**
3029. **`tests/baselines/reference/narrowCommaOperatorNestedWithinLHS.js`** -> AI Confidence: **99.06%**
3030. **`tests/baselines/reference/narrowedImports.js`** -> AI Confidence: **99.06%**
3031. **`tests/baselines/reference/narrowingByTypeofInSwitch.js`** -> AI Confidence: **99.06%**
3032. **`tests/baselines/reference/narrowingConstrainedTypeVariable.js`** -> AI Confidence: **99.06%**
3033. **`tests/baselines/reference/narrowingDestructuring.js`** -> AI Confidence: **99.06%**
3034. **`tests/baselines/reference/narrowingGenericTypeFromInstanceof01.js`** -> AI Confidence: **99.06%**
3035. **`tests/baselines/reference/narrowingOfDottedNames.js`** -> AI Confidence: **99.06%**
3036. **`tests/baselines/reference/narrowingPlainJsNoCrash1.js`** -> AI Confidence: **99.06%**
3037. **`tests/baselines/reference/narrowingRestGenericCall.js`** -> AI Confidence: **99.06%**
3038. **`tests/baselines/reference/narrowingUnionToUnion.js`** -> AI Confidence: **99.06%**
3039. **`tests/baselines/reference/nestedBlockScopedBindings10.js`** -> AI Confidence: **99.06%**
3040. **`tests/baselines/reference/nestedBlockScopedBindings15.js`** -> AI Confidence: **99.06%**
3041. **`tests/baselines/reference/nestedBlockScopedBindings16.js`** -> AI Confidence: **99.06%**
3042. **`tests/baselines/reference/nestedBlockScopedBindings2.js`** -> AI Confidence: **99.06%**
3043. **`tests/baselines/reference/nestedBlockScopedBindings3.js`** -> AI Confidence: **99.06%**
3044. **`tests/baselines/reference/nestedBlockScopedBindings5.js`** -> AI Confidence: **99.06%**
3045. **`tests/baselines/reference/nestedBlockScopedBindings6.js`** -> AI Confidence: **99.06%**
3046. **`tests/baselines/reference/nestedFreshLiteral.js`** -> AI Confidence: **99.06%**
3047. **`tests/baselines/reference/nestedLoopTypeGuards.js`** -> AI Confidence: **99.06%**
3048. **`tests/baselines/reference/nestedObjectRest.js`** -> AI Confidence: **99.06%**
3049. **`tests/baselines/reference/nestedSuperCallEmit(target=es5).js`** -> AI Confidence: **99.06%**
3050. **`tests/baselines/reference/neverAsDiscriminantType(strict=false).js`** -> AI Confidence: **99.06%**
3051. **`tests/baselines/reference/neverAsDiscriminantType(strict=true).js`** -> AI Confidence: **99.06%**
3052. **`tests/baselines/reference/neverReturningFunctions1.js`** -> AI Confidence: **99.06%**
3053. **`tests/baselines/reference/newAbstractInstance2.js`** -> AI Confidence: **99.06%**
3054. **`tests/baselines/reference/noCrashOnImportShadowing.js`** -> AI Confidence: **99.06%**
3055. **`tests/baselines/reference/noCrashOnNoLib.js`** -> AI Confidence: **99.06%**
3056. **`tests/baselines/reference/noImplicitReturnsInAsync1.js`** -> AI Confidence: **99.06%**
3057. **`tests/baselines/reference/noImplicitReturnsInAsync2.js`** -> AI Confidence: **99.06%**
3058. **`tests/baselines/reference/noImplicitUseStrict_umd.js`** -> AI Confidence: **99.06%**
3059. **`tests/baselines/reference/noUncheckedIndexAccess.js`** -> AI Confidence: **99.06%**
3060. **`tests/baselines/reference/nodeAllowJsPackageSelfName(module=node16).js`** -> AI Confidence: **99.06%**
3061. **`tests/baselines/reference/nodeAllowJsPackageSelfName(module=node18).js`** -> AI Confidence: **99.06%**
3062. **`tests/baselines/reference/nodeAllowJsPackageSelfName(module=node20).js`** -> AI Confidence: **99.06%**
3063. **`tests/baselines/reference/nodeAllowJsPackageSelfName(module=nodenext).js`** -> AI Confidence: **99.06%**
3064. **`tests/baselines/reference/nodeModulesImportHelpersCollisions3(module=node16,target=es2015).js`** -> AI Confidence: **99.06%**
3065. **`tests/baselines/reference/nodeModulesImportHelpersCollisions3(module=node16,target=es5).js`** -> AI Confidence: **99.06%**
3066. **`tests/baselines/reference/nodeModulesImportHelpersCollisions3(module=node18,target=es2015).js`** -> AI Confidence: **99.06%**
3067. **`tests/baselines/reference/nodeModulesImportHelpersCollisions3(module=node18,target=es5).js`** -> AI Confidence: **99.06%**
3068. **`tests/baselines/reference/nodeModulesImportHelpersCollisions3(module=node20,target=es2015).js`** -> AI Confidence: **99.06%**
3069. **`tests/baselines/reference/nodeModulesImportHelpersCollisions3(module=node20,target=es5).js`** -> AI Confidence: **99.06%**
3070. **`tests/baselines/reference/nodeModulesImportHelpersCollisions3(module=nodenext,target=es2015).js`** -> AI Confidence: **99.06%**
3071. **`tests/baselines/reference/nodeModulesImportHelpersCollisions3(module=nodenext,target=es5).js`** -> AI Confidence: **99.06%**
3072. **`tests/baselines/reference/nodeModulesImportResolutionIntoExport(module=node16).js`** -> AI Confidence: **99.06%**
3073. **`tests/baselines/reference/nodeModulesImportResolutionIntoExport(module=node18).js`** -> AI Confidence: **99.06%**
3074. **`tests/baselines/reference/nodeModulesImportResolutionIntoExport(module=node20).js`** -> AI Confidence: **99.06%**
3075. **`tests/baselines/reference/nodeModulesImportResolutionIntoExport(module=nodenext).js`** -> AI Confidence: **99.06%**
3076. **`tests/baselines/reference/nodeModulesImportResolutionNoCycle(module=node16).js`** -> AI Confidence: **99.06%**
3077. **`tests/baselines/reference/nodeModulesImportResolutionNoCycle(module=node18).js`** -> AI Confidence: **99.06%**
3078. **`tests/baselines/reference/nodeModulesImportResolutionNoCycle(module=node20).js`** -> AI Confidence: **99.06%**
3079. **`tests/baselines/reference/nodeModulesImportResolutionNoCycle(module=nodenext).js`** -> AI Confidence: **99.06%**
3080. **`tests/baselines/reference/nodeModulesResolveJsonModule(module=node16).js`** -> AI Confidence: **99.06%**
3081. **`tests/baselines/reference/nodeModulesResolveJsonModule(module=node18).js`** -> AI Confidence: **99.06%**
3082. **`tests/baselines/reference/nodeModulesResolveJsonModule(module=node20).js`** -> AI Confidence: **99.06%**
3083. **`tests/baselines/reference/nodeModulesResolveJsonModule(module=nodenext).js`** -> AI Confidence: **99.06%**
3084. **`tests/baselines/reference/nodeModulesTripleSlashReferenceModeDeclarationEmit6(module=node16).js`** -> AI Confidence: **99.06%**
3085. **`tests/baselines/reference/nodeModulesTripleSlashReferenceModeDeclarationEmit6(module=node18).js`** -> AI Confidence: **99.06%**
3086. **`tests/baselines/reference/nodeModulesTripleSlashReferenceModeDeclarationEmit6(module=node20).js`** -> AI Confidence: **99.06%**
3087. **`tests/baselines/reference/nodeModulesTripleSlashReferenceModeDeclarationEmit6(module=nodenext).js`** -> AI Confidence: **99.06%**
3088. **`tests/baselines/reference/nodePackageSelfName(module=node16).js`** -> AI Confidence: **99.06%**
3089. **`tests/baselines/reference/nodePackageSelfName(module=node18).js`** -> AI Confidence: **99.06%**
3090. **`tests/baselines/reference/nodePackageSelfName(module=node20).js`** -> AI Confidence: **99.06%**
3091. **`tests/baselines/reference/nodePackageSelfName(module=nodenext).js`** -> AI Confidence: **99.06%**
3092. **`tests/baselines/reference/nodePackageSelfNameScoped(module=node16).js`** -> AI Confidence: **99.06%**
3093. **`tests/baselines/reference/nodePackageSelfNameScoped(module=node18).js`** -> AI Confidence: **99.06%**
3094. **`tests/baselines/reference/nodePackageSelfNameScoped(module=node20).js`** -> AI Confidence: **99.06%**
3095. **`tests/baselines/reference/nodePackageSelfNameScoped(module=nodenext).js`** -> AI Confidence: **99.06%**
3096. **`tests/baselines/reference/nonNullFullInference.js`** -> AI Confidence: **99.06%**
3097. **`tests/baselines/reference/nonNullableAndObjectIntersections(strict=false).js`** -> AI Confidence: **99.06%**
3098. **`tests/baselines/reference/nonNullableAndObjectIntersections(strict=true).js`** -> AI Confidence: **99.06%**
3099. **`tests/baselines/reference/nonNullableTypes1.js`** -> AI Confidence: **99.06%**
3100. **`tests/baselines/reference/nonPrimitiveAccessProperty.js`** -> AI Confidence: **99.06%**
3101. **`tests/baselines/reference/nonPrimitiveNarrow.js`** -> AI Confidence: **99.06%**
3102. **`tests/baselines/reference/nonPrimitiveStrictNull.js`** -> AI Confidence: **99.06%**
3103. **`tests/baselines/reference/nongenericConditionalNotPartiallyComputed.js`** -> AI Confidence: **99.06%**
3104. **`tests/baselines/reference/nullOrUndefinedTypeGuardIsOrderIndependent.js`** -> AI Confidence: **99.06%**
3105. **`tests/baselines/reference/nullishCoalescingOperator10.js`** -> AI Confidence: **99.06%**
3106. **`tests/baselines/reference/nullishCoalescingOperator11.js`** -> AI Confidence: **99.06%**
3107. **`tests/baselines/reference/nullishCoalescingOperatorInAsyncGenerator(target=es2015).js`** -> AI Confidence: **99.06%**
3108. **`tests/baselines/reference/nullishCoalescingOperatorInAsyncGenerator(target=es5).js`** -> AI Confidence: **99.06%**
3109. **`tests/baselines/reference/nullishCoalescingOperatorInParameterBindingPattern(target=esnext).js`** -> AI Confidence: **99.06%**
3110. **`tests/baselines/reference/nullishCoalescingOperatorInParameterInitializer(target=es2015).js`** -> AI Confidence: **99.06%**
3111. **`tests/baselines/reference/nullishCoalescingOperatorInParameterInitializer(target=es5).js`** -> AI Confidence: **99.06%**
3112. **`tests/baselines/reference/nullishCoalescingOperatorInParameterInitializer(target=esnext).js`** -> AI Confidence: **99.06%**
3113. **`tests/baselines/reference/numericLiteralTypes3.js`** -> AI Confidence: **99.06%**
3114. **`tests/baselines/reference/objectAssignLikeNonUnionResult.js`** -> AI Confidence: **99.06%**
3115. **`tests/baselines/reference/objectBindingPatternKeywordIdentifiers01.js`** -> AI Confidence: **99.06%**
3116. **`tests/baselines/reference/objectBindingPatternKeywordIdentifiers03.js`** -> AI Confidence: **99.06%**
3117. **`tests/baselines/reference/objectBindingPattern_restElementWithPropertyName.js`** -> AI Confidence: **99.06%**
3118. **`tests/baselines/reference/objectLiteralEnumPropertyNames.js`** -> AI Confidence: **99.06%**
3119. **`tests/baselines/reference/objectLiteralNormalization.js`** -> AI Confidence: **99.06%**
3120. **`tests/baselines/reference/objectRest2.js`** -> AI Confidence: **99.06%**
3121. **`tests/baselines/reference/objectRestCatchES5.js`** -> AI Confidence: **99.06%**
3122. **`tests/baselines/reference/objectRestForOf.js`** -> AI Confidence: **99.06%**
3123. **`tests/baselines/reference/objectRestPropertyMustBeLast.js`** -> AI Confidence: **99.06%**
3124. **`tests/baselines/reference/objectRestReadonly.js`** -> AI Confidence: **99.06%**
3125. **`tests/baselines/reference/operationsAvailableOnPromisedType(target=es2015).js`** -> AI Confidence: **99.06%**
3126. **`tests/baselines/reference/operationsAvailableOnPromisedType(target=es5).js`** -> AI Confidence: **99.06%**
3127. **`tests/baselines/reference/optionalChainWithInstantiationExpression1(target=es2020).js`** -> AI Confidence: **99.06%**
3128. **`tests/baselines/reference/optionalChainingInLoop(target=es5).js`** -> AI Confidence: **99.06%**
3129. **`tests/baselines/reference/optionalMethods.js`** -> AI Confidence: **99.06%**
3130. **`tests/baselines/reference/optionalTupleElements1.js`** -> AI Confidence: **99.06%**
3131. **`tests/baselines/reference/outFilerootDirModuleNamesAmd.js`** -> AI Confidence: **99.06%**
3132. **`tests/baselines/reference/overloadAssignmentCompat.js`** -> AI Confidence: **99.06%**
3133. **`tests/baselines/reference/overloadModifiersMustAgree.js`** -> AI Confidence: **99.06%**
3134. **`tests/baselines/reference/overloadReturnTypes.js`** -> AI Confidence: **99.06%**
3135. **`tests/baselines/reference/parameterDecoratorsEmitCrash.js`** -> AI Confidence: **99.06%**
3136. **`tests/baselines/reference/parameterInitializerBeforeDestructuringEmit.js`** -> AI Confidence: **99.06%**
3137. **`tests/baselines/reference/parameterInitializersForwardReferencing(target=es5).js`** -> AI Confidence: **99.06%**
3138. **`tests/baselines/reference/parenthesizedAsyncArrowFunction.js`** -> AI Confidence: **99.06%**
3139. **`tests/baselines/reference/parseEntityNameWithReservedWord.js`** -> AI Confidence: **99.06%**
3140. **`tests/baselines/reference/parseIncompleteBinaryExpression1.js`** -> AI Confidence: **99.06%**
3141. **`tests/baselines/reference/parseInvalidNullableTypes.js`** -> AI Confidence: **99.06%**
3142. **`tests/baselines/reference/parser509667.js`** -> AI Confidence: **99.06%**
3143. **`tests/baselines/reference/parser512097.js`** -> AI Confidence: **99.06%**
3144. **`tests/baselines/reference/parserAmbiguityWithBinaryOperator1.js`** -> AI Confidence: **99.06%**
3145. **`tests/baselines/reference/parserAmbiguityWithBinaryOperator2.js`** -> AI Confidence: **99.06%**
3146. **`tests/baselines/reference/parserAmbiguityWithBinaryOperator3.js`** -> AI Confidence: **99.06%**
3147. **`tests/baselines/reference/parserAmbiguityWithBinaryOperator4.js`** -> AI Confidence: **99.06%**
3148. **`tests/baselines/reference/parserArrowFunctionExpression11.js`** -> AI Confidence: **99.06%**
3149. **`tests/baselines/reference/parserArrowFunctionExpression14.js`** -> AI Confidence: **99.06%**
3150. **`tests/baselines/reference/parserArrowFunctionExpression15.js`** -> AI Confidence: **99.06%**
3151. **`tests/baselines/reference/parserArrowFunctionExpression16.js`** -> AI Confidence: **99.06%**
3152. **`tests/baselines/reference/parserArrowFunctionExpression17.js`** -> AI Confidence: **99.06%**
3153. **`tests/baselines/reference/parserArrowFunctionExpression2.js`** -> AI Confidence: **99.06%**
3154. **`tests/baselines/reference/parserArrowFunctionExpression3.js`** -> AI Confidence: **99.06%**
3155. **`tests/baselines/reference/parserArrowFunctionExpression6.js`** -> AI Confidence: **99.06%**
3156. **`tests/baselines/reference/parserArrowFunctionExpression9.js`** -> AI Confidence: **99.06%**
3157. **`tests/baselines/reference/parserComputedPropertyName16.js`** -> AI Confidence: **99.06%**
3158. **`tests/baselines/reference/parserComputedPropertyName26.js`** -> AI Confidence: **99.06%**
3159. **`tests/baselines/reference/parserComputedPropertyName30.js`** -> AI Confidence: **99.06%**
3160. **`tests/baselines/reference/parserComputedPropertyName34.js`** -> AI Confidence: **99.06%**
3161. **`tests/baselines/reference/parserComputedPropertyName40.js`** -> AI Confidence: **99.06%**
3162. **`tests/baselines/reference/parserES5ComputedPropertyName6(target=es2015).js`** -> AI Confidence: **99.06%**
3163. **`tests/baselines/reference/parserES5ComputedPropertyName6(target=es5).js`** -> AI Confidence: **99.06%**
3164. **`tests/baselines/reference/parserES5ForOfStatement10(target=es5).js`** -> AI Confidence: **99.06%**
3165. **`tests/baselines/reference/parserES5ForOfStatement11(target=es5).js`** -> AI Confidence: **99.06%**
3166. **`tests/baselines/reference/parserES5ForOfStatement12(target=es5).js`** -> AI Confidence: **99.06%**
3167. **`tests/baselines/reference/parserES5ForOfStatement13(target=es2015).js`** -> AI Confidence: **99.06%**
3168. **`tests/baselines/reference/parserES5ForOfStatement14(target=es2015).js`** -> AI Confidence: **99.06%**
3169. **`tests/baselines/reference/parserES5ForOfStatement15(target=es2015).js`** -> AI Confidence: **99.06%**
3170. **`tests/baselines/reference/parserES5ForOfStatement16(target=es2015).js`** -> AI Confidence: **99.06%**
3171. **`tests/baselines/reference/parserES5ForOfStatement17(target=es2015).js`** -> AI Confidence: **99.06%**
3172. **`tests/baselines/reference/parserES5ForOfStatement17(target=es5).js`** -> AI Confidence: **99.06%**
3173. **`tests/baselines/reference/parserES5ForOfStatement18(target=es2015).js`** -> AI Confidence: **99.06%**
3174. **`tests/baselines/reference/parserES5ForOfStatement19(target=es2015).js`** -> AI Confidence: **99.06%**
3175. **`tests/baselines/reference/parserES5ForOfStatement19(target=es5).js`** -> AI Confidence: **99.06%**
3176. **`tests/baselines/reference/parserES5ForOfStatement2(target=es2015).js`** -> AI Confidence: **99.06%**
3177. **`tests/baselines/reference/parserES5ForOfStatement20(target=es2015).js`** -> AI Confidence: **99.06%**
3178. **`tests/baselines/reference/parserES5ForOfStatement20(target=es5).js`** -> AI Confidence: **99.06%**
3179. **`tests/baselines/reference/parserES5ForOfStatement21(target=es2015).js`** -> AI Confidence: **99.06%**
3180. **`tests/baselines/reference/parserES5ForOfStatement3(target=es2015).js`** -> AI Confidence: **99.06%**
3181. **`tests/baselines/reference/parserES5ForOfStatement4(target=es2015).js`** -> AI Confidence: **99.06%**
3182. **`tests/baselines/reference/parserES5ForOfStatement5(target=es2015).js`** -> AI Confidence: **99.06%**
3183. **`tests/baselines/reference/parserES5ForOfStatement6(target=es2015).js`** -> AI Confidence: **99.06%**
3184. **`tests/baselines/reference/parserES5ForOfStatement7(target=es2015).js`** -> AI Confidence: **99.06%**
3185. **`tests/baselines/reference/parserES5ForOfStatement8(target=es2015).js`** -> AI Confidence: **99.06%**
3186. **`tests/baselines/reference/parserES5ForOfStatement9(target=es2015).js`** -> AI Confidence: **99.06%**
3187. **`tests/baselines/reference/parserEnum5.js`** -> AI Confidence: **99.06%**
3188. **`tests/baselines/reference/parserEnum6.js`** -> AI Confidence: **99.06%**
3189. **`tests/baselines/reference/parserEnum7.js`** -> AI Confidence: **99.06%**
3190. **`tests/baselines/reference/parserEnumDeclaration1.js`** -> AI Confidence: **99.06%**
3191. **`tests/baselines/reference/parserEnumDeclaration4.js`** -> AI Confidence: **99.06%**
3192. **`tests/baselines/reference/parserEnumDeclaration5.js`** -> AI Confidence: **99.06%**
3193. **`tests/baselines/reference/parserEnumDeclaration6.js`** -> AI Confidence: **99.06%**
3194. **`tests/baselines/reference/parserErrorRecoveryIfStatement1.js`** -> AI Confidence: **99.06%**
3195. **`tests/baselines/reference/parserErrorRecoveryIfStatement2.js`** -> AI Confidence: **99.06%**
3196. **`tests/baselines/reference/parserErrorRecoveryIfStatement3.js`** -> AI Confidence: **99.06%**
3197. **`tests/baselines/reference/parserErrorRecoveryIfStatement4.js`** -> AI Confidence: **99.06%**
3198. **`tests/baselines/reference/parserErrorRecoveryIfStatement5.js`** -> AI Confidence: **99.06%**
3199. **`tests/baselines/reference/parserErrorRecoveryIfStatement6.js`** -> AI Confidence: **99.06%**
3200. **`tests/baselines/reference/parserExportAssignment9.js`** -> AI Confidence: **99.06%**
3201. **`tests/baselines/reference/parserForInStatement2.js`** -> AI Confidence: **99.06%**
3202. **`tests/baselines/reference/parserForInStatement3.js`** -> AI Confidence: **99.06%**
3203. **`tests/baselines/reference/parserForInStatement4.js`** -> AI Confidence: **99.06%**
3204. **`tests/baselines/reference/parserForInStatement5.js`** -> AI Confidence: **99.06%**
3205. **`tests/baselines/reference/parserForInStatement6.js`** -> AI Confidence: **99.06%**
3206. **`tests/baselines/reference/parserForInStatement7.js`** -> AI Confidence: **99.06%**
3207. **`tests/baselines/reference/parserForInStatement8(target=es2015).js`** -> AI Confidence: **99.06%**
3208. **`tests/baselines/reference/parserForInStatement8(target=es5).js`** -> AI Confidence: **99.06%**
3209. **`tests/baselines/reference/parserForOfStatement13.js`** -> AI Confidence: **99.06%**
3210. **`tests/baselines/reference/parserForOfStatement14.js`** -> AI Confidence: **99.06%**
3211. **`tests/baselines/reference/parserForOfStatement15.js`** -> AI Confidence: **99.06%**
3212. **`tests/baselines/reference/parserForOfStatement16.js`** -> AI Confidence: **99.06%**
3213. **`tests/baselines/reference/parserForOfStatement17.js`** -> AI Confidence: **99.06%**
3214. **`tests/baselines/reference/parserForOfStatement18.js`** -> AI Confidence: **99.06%**
3215. **`tests/baselines/reference/parserForOfStatement19.js`** -> AI Confidence: **99.06%**
3216. **`tests/baselines/reference/parserForOfStatement2.js`** -> AI Confidence: **99.06%**
3217. **`tests/baselines/reference/parserForOfStatement20.js`** -> AI Confidence: **99.06%**
3218. **`tests/baselines/reference/parserForOfStatement21.js`** -> AI Confidence: **99.06%**
3219. **`tests/baselines/reference/parserForOfStatement22.js`** -> AI Confidence: **99.06%**
3220. **`tests/baselines/reference/parserForOfStatement24.js`** -> AI Confidence: **99.06%**
3221. **`tests/baselines/reference/parserForOfStatement25.js`** -> AI Confidence: **99.06%**
3222. **`tests/baselines/reference/parserForOfStatement3.js`** -> AI Confidence: **99.06%**
3223. **`tests/baselines/reference/parserForOfStatement4.js`** -> AI Confidence: **99.06%**
3224. **`tests/baselines/reference/parserForOfStatement5.js`** -> AI Confidence: **99.06%**
3225. **`tests/baselines/reference/parserForOfStatement6.js`** -> AI Confidence: **99.06%**
3226. **`tests/baselines/reference/parserForOfStatement7.js`** -> AI Confidence: **99.06%**
3227. **`tests/baselines/reference/parserForOfStatement8.js`** -> AI Confidence: **99.06%**
3228. **`tests/baselines/reference/parserForOfStatement9.js`** -> AI Confidence: **99.06%**
3229. **`tests/baselines/reference/parserForStatement9.js`** -> AI Confidence: **99.06%**
3230. **`tests/baselines/reference/parserFunctionDeclaration7.js`** -> AI Confidence: **99.06%**
3231. **`tests/baselines/reference/parserInterfaceKeywordInEnum.js`** -> AI Confidence: **99.06%**
3232. **`tests/baselines/reference/parserInterfaceKeywordInEnum1.js`** -> AI Confidence: **99.06%**
3233. **`tests/baselines/reference/parserNotRegex1.js`** -> AI Confidence: **99.06%**
3234. **`tests/baselines/reference/parserParenthesizedVariableAndFunctionInTernary.js`** -> AI Confidence: **99.06%**
3235. **`tests/baselines/reference/parserParenthesizedVariableAndParenthesizedFunctionInTernary.js`** -> AI Confidence: **99.06%**
3236. **`tests/baselines/reference/parserRealSource7.js`** -> AI Confidence: **99.06%**
3237. **`tests/baselines/reference/parserRealSource8.js`** -> AI Confidence: **99.06%**
3238. **`tests/baselines/reference/parserRealSource9.js`** -> AI Confidence: **99.06%**
3239. **`tests/baselines/reference/parserS12.11_A3_T4.js`** -> AI Confidence: **99.06%**
3240. **`tests/baselines/reference/parserS7.2_A1.5_T2.js`** -> AI Confidence: **99.06%**
3241. **`tests/baselines/reference/parserS7.6_A4.2_T1.js`** -> AI Confidence: **99.06%**
3242. **`tests/baselines/reference/parserShorthandPropertyAssignment1.js`** -> AI Confidence: **99.06%**
3243. **`tests/baselines/reference/parserUnicode1.js`** -> AI Confidence: **99.06%**
3244. **`tests/baselines/reference/parserUsingConstructorAsIdentifier.js`** -> AI Confidence: **99.06%**
3245. **`tests/baselines/reference/parser_breakInIterationOrSwitchStatement4.js`** -> AI Confidence: **99.06%**
3246. **`tests/baselines/reference/parser_continueInIterationStatement4.js`** -> AI Confidence: **99.06%**
3247. **`tests/baselines/reference/parser_continueLabel.js`** -> AI Confidence: **99.06%**
3248. **`tests/baselines/reference/parser_continueNotInIterationStatement4.js`** -> AI Confidence: **99.06%**
3249. **`tests/baselines/reference/parserindenter.js`** -> AI Confidence: **99.06%**
3250. **`tests/baselines/reference/partiallyDiscriminantedUnions.js`** -> AI Confidence: **99.06%**
3251. **`tests/baselines/reference/plainJSGrammarErrors2.js`** -> AI Confidence: **99.06%**
3252. **`tests/baselines/reference/prefixUnaryOperatorsOnExportedVariables(target=es2015).js`** -> AI Confidence: **99.06%**
3253. **`tests/baselines/reference/prefixUnaryOperatorsOnExportedVariables(target=es5).js`** -> AI Confidence: **99.06%**
3254. **`tests/baselines/reference/preserveConstEnums.js`** -> AI Confidence: **99.06%**
3255. **`tests/baselines/reference/primtiveTypesAreIdentical.js`** -> AI Confidence: **99.06%**
3256. **`tests/baselines/reference/printerApi/printsFileCorrectly.templateLiteral.js`** -> AI Confidence: **99.06%**
3257. **`tests/baselines/reference/printerApi/printsNodeCorrectly.classWithOptionalMethodAndProperty.js`** -> AI Confidence: **99.06%**
3258. **`tests/baselines/reference/privateIdentifierChain.1.js`** -> AI Confidence: **99.06%**
3259. **`tests/baselines/reference/privateNameAccessors.js`** -> AI Confidence: **99.06%**
3260. **`tests/baselines/reference/privateNameAndAny.js`** -> AI Confidence: **99.06%**
3261. **`tests/baselines/reference/privateNameAndObjectRestSpread.js`** -> AI Confidence: **99.06%**
3262. **`tests/baselines/reference/privateNameBadAssignment.js`** -> AI Confidence: **99.06%**
3263. **`tests/baselines/reference/privateNameCircularReference.js`** -> AI Confidence: **99.06%**
3264. **`tests/baselines/reference/privateNameComputedPropertyName1(target=es2015).js`** -> AI Confidence: **99.06%**
3265. **`tests/baselines/reference/privateNameComputedPropertyName2(target=es2015).js`** -> AI Confidence: **99.06%**
3266. **`tests/baselines/reference/privateNameComputedPropertyName3(target=es2015).js`** -> AI Confidence: **99.06%**
3267. **`tests/baselines/reference/privateNameConstructorSignature.js`** -> AI Confidence: **99.06%**
3268. **`tests/baselines/reference/privateNameDeclarationMerging.js`** -> AI Confidence: **99.06%**
3269. **`tests/baselines/reference/privateNameEnum.js`** -> AI Confidence: **99.06%**
3270. **`tests/baselines/reference/privateNameField.js`** -> AI Confidence: **99.06%**
3271. **`tests/baselines/reference/privateNameFieldAccess.js`** -> AI Confidence: **99.06%**
3272. **`tests/baselines/reference/privateNameFieldAssignment.js`** -> AI Confidence: **99.06%**
3273. **`tests/baselines/reference/privateNameFieldCallExpression.js`** -> AI Confidence: **99.06%**
3274. **`tests/baselines/reference/privateNameFieldDerivedClasses.js`** -> AI Confidence: **99.06%**
3275. **`tests/baselines/reference/privateNameFieldParenthesisLeftAssignment.js`** -> AI Confidence: **99.06%**
3276. **`tests/baselines/reference/privateNameHashCharName.js`** -> AI Confidence: **99.06%**
3277. **`tests/baselines/reference/privateNameInLhsReceiverExpression.js`** -> AI Confidence: **99.06%**
3278. **`tests/baselines/reference/privateNameMethod.js`** -> AI Confidence: **99.06%**
3279. **`tests/baselines/reference/privateNameMethodAssignment.js`** -> AI Confidence: **99.06%**
3280. **`tests/baselines/reference/privateNameMethodCallExpression.js`** -> AI Confidence: **99.06%**
3281. **`tests/baselines/reference/privateNameMethodInStaticFieldInit.js`** -> AI Confidence: **99.06%**
3282. **`tests/baselines/reference/privateNameNestedClassFieldShadowing.js`** -> AI Confidence: **99.06%**
3283. **`tests/baselines/reference/privateNameNestedClassMethodShadowing.js`** -> AI Confidence: **99.06%**
3284. **`tests/baselines/reference/privateNameReadonly.js`** -> AI Confidence: **99.06%**
3285. **`tests/baselines/reference/privateNameSetterExprReturnValue.js`** -> AI Confidence: **99.06%**
3286. **`tests/baselines/reference/privateNameSetterNoGetter.js`** -> AI Confidence: **99.06%**
3287. **`tests/baselines/reference/privateNameStaticAccessors.js`** -> AI Confidence: **99.06%**
3288. **`tests/baselines/reference/privateNameStaticAccessorsCallExpression.js`** -> AI Confidence: **99.06%**
3289. **`tests/baselines/reference/privateNameStaticFieldAccess.js`** -> AI Confidence: **99.06%**
3290. **`tests/baselines/reference/privateNameStaticFieldAssignment.js`** -> AI Confidence: **99.06%**
3291. **`tests/baselines/reference/privateNameStaticFieldCallExpression.js`** -> AI Confidence: **99.06%**
3292. **`tests/baselines/reference/privateNameStaticFieldClassExpression.js`** -> AI Confidence: **99.06%**
3293. **`tests/baselines/reference/privateNameStaticFieldDerivedClasses.js`** -> AI Confidence: **99.06%**
3294. **`tests/baselines/reference/privateNameStaticFieldUnaryMutation.js`** -> AI Confidence: **99.06%**
3295. **`tests/baselines/reference/privateNameStaticMethod.js`** -> AI Confidence: **99.06%**
3296. **`tests/baselines/reference/privateNameStaticMethodAssignment.js`** -> AI Confidence: **99.06%**
3297. **`tests/baselines/reference/privateNameStaticMethodCallExpression.js`** -> AI Confidence: **99.06%**
3298. **`tests/baselines/reference/privateNameStaticMethodInStaticFieldInit.js`** -> AI Confidence: **99.06%**
3299. **`tests/baselines/reference/privateNamesAndGenericClasses-2.js`** -> AI Confidence: **99.06%**
3300. **`tests/baselines/reference/privateNamesAndStaticFields.js`** -> AI Confidence: **99.06%**
3301. **`tests/baselines/reference/privateNamesInNestedClasses-2.js`** -> AI Confidence: **99.06%**
3302. **`tests/baselines/reference/privateNamesInterfaceExtendingClass.js`** -> AI Confidence: **99.06%**
3303. **`tests/baselines/reference/privateNamesNoDelete.js`** -> AI Confidence: **99.06%**
3304. **`tests/baselines/reference/privateNamesUnique-3.js`** -> AI Confidence: **99.06%**
3305. **`tests/baselines/reference/privateStaticNameShadowing.js`** -> AI Confidence: **99.06%**
3306. **`tests/baselines/reference/privateWriteOnlyAccessorRead.js`** -> AI Confidence: **99.06%**
3307. **`tests/baselines/reference/project/emitDecoratorMetadataCommonJSISolatedModules/amd/main.js`** -> AI Confidence: **99.06%**
3308. **`tests/baselines/reference/project/emitDecoratorMetadataCommonJSISolatedModules/node/main.js`** -> AI Confidence: **99.06%**
3309. **`tests/baselines/reference/project/emitDecoratorMetadataCommonJSISolatedModulesNoResolve/amd/main.js`** -> AI Confidence: **99.06%**
3310. **`tests/baselines/reference/project/emitDecoratorMetadataCommonJSISolatedModulesNoResolve/node/main.js`** -> AI Confidence: **99.06%**
3311. **`tests/baselines/reference/project/emitDecoratorMetadataSystemJS/amd/main.js`** -> AI Confidence: **99.06%**
3312. **`tests/baselines/reference/project/emitDecoratorMetadataSystemJS/node/main.js`** -> AI Confidence: **99.06%**
3313. **`tests/baselines/reference/project/emitDecoratorMetadataSystemJSISolatedModules/amd/main.js`** -> AI Confidence: **99.06%**
3314. **`tests/baselines/reference/project/emitDecoratorMetadataSystemJSISolatedModules/node/main.js`** -> AI Confidence: **99.06%**
3315. **`tests/baselines/reference/project/emitDecoratorMetadataSystemJSISolatedModulesNoResolve/amd/main.js`** -> AI Confidence: **99.06%**
3316. **`tests/baselines/reference/project/emitDecoratorMetadataSystemJSISolatedModulesNoResolve/node/main.js`** -> AI Confidence: **99.06%**
3317. **`tests/baselines/reference/project/nodeModulesImportHigher/amd/importHigher/root.js`** -> AI Confidence: **99.06%**
3318. **`tests/baselines/reference/project/nodeModulesImportHigher/node/importHigher/root.js`** -> AI Confidence: **99.06%**
3319. **`tests/baselines/reference/project/nodeModulesMaxDepthExceeded/amd/maxDepthExceeded/built/root.js`** -> AI Confidence: **99.06%**
3320. **`tests/baselines/reference/project/nodeModulesMaxDepthExceeded/node/maxDepthExceeded/built/root.js`** -> AI Confidence: **99.06%**
3321. **`tests/baselines/reference/project/nodeModulesMaxDepthIncreased/amd/maxDepthIncreased/root.js`** -> AI Confidence: **99.06%**
3322. **`tests/baselines/reference/project/nodeModulesMaxDepthIncreased/node/maxDepthIncreased/root.js`** -> AI Confidence: **99.06%**
3323. **`tests/baselines/reference/project/nonRelative/amd/consume.js`** -> AI Confidence: **99.06%**
3324. **`tests/baselines/reference/promiseDefinitionTest(target=es2015).js`** -> AI Confidence: **99.06%**
3325. **`tests/baselines/reference/promiseTry.js`** -> AI Confidence: **99.06%**
3326. **`tests/baselines/reference/promises.js`** -> AI Confidence: **99.06%**
3327. **`tests/baselines/reference/propTypeValidatorInference.js`** -> AI Confidence: **99.06%**
3328. **`tests/baselines/reference/propagateNonInferrableType.js`** -> AI Confidence: **99.06%**
3329. **`tests/baselines/reference/propertiesAndIndexersForNumericNames.js`** -> AI Confidence: **99.06%**
3330. **`tests/baselines/reference/propertyAccessWidening.js`** -> AI Confidence: **99.06%**
3331. **`tests/baselines/reference/propertyNamesOfReservedWords.js`** -> AI Confidence: **99.06%**
3332. **`tests/baselines/reference/propertyOverridesAccessors4(target=es5).js`** -> AI Confidence: **99.06%**
3333. **`tests/baselines/reference/propertyWrappedInTry.js`** -> AI Confidence: **99.06%**
3334. **`tests/baselines/reference/reExportDefaultExport(target=es2015).js`** -> AI Confidence: **99.06%**
3335. **`tests/baselines/reference/reExportDefaultExport(target=es5).js`** -> AI Confidence: **99.06%**
3336. **`tests/baselines/reference/reExportJsFromTs.js`** -> AI Confidence: **99.06%**
3337. **`tests/baselines/reference/reachabilityChecks1.js`** -> AI Confidence: **99.06%**
3338. **`tests/baselines/reference/reachabilityChecks11.js`** -> AI Confidence: **99.06%**
3339. **`tests/baselines/reference/reachabilityChecks3.js`** -> AI Confidence: **99.06%**
3340. **`tests/baselines/reference/reachabilityChecks4.js`** -> AI Confidence: **99.06%**
3341. **`tests/baselines/reference/reactNamespaceImportPresevation.js`** -> AI Confidence: **99.06%**
3342. **`tests/baselines/reference/reactSFCAndFunctionResolvable.js`** -> AI Confidence: **99.06%**
3343. **`tests/baselines/reference/reactTagNameComponentWithPropsNoOOM.js`** -> AI Confidence: **99.06%**
3344. **`tests/baselines/reference/readonlyArraysAndTuples2.js`** -> AI Confidence: **99.06%**
3345. **`tests/baselines/reference/recursiveConditionalCrash1.js`** -> AI Confidence: **99.06%**
3346. **`tests/baselines/reference/recursiveConditionalEvaluationNonInfinite.js`** -> AI Confidence: **99.06%**
3347. **`tests/baselines/reference/recursiveReturns.js`** -> AI Confidence: **99.06%**
3348. **`tests/baselines/reference/reexportDefaultIsCallable.js`** -> AI Confidence: **99.06%**
3349. **`tests/baselines/reference/reexportMissingDefault.js`** -> AI Confidence: **99.06%**
3350. **`tests/baselines/reference/reexportMissingDefault1.js`** -> AI Confidence: **99.06%**
3351. **`tests/baselines/reference/reexportMissingDefault2.js`** -> AI Confidence: **99.06%**
3352. **`tests/baselines/reference/reexportMissingDefault4.js`** -> AI Confidence: **99.06%**
3353. **`tests/baselines/reference/reexportMissingDefault6.js`** -> AI Confidence: **99.06%**
3354. **`tests/baselines/reference/reexportMissingDefault8.js`** -> AI Confidence: **99.06%**
3355. **`tests/baselines/reference/regexpExecAndMatchTypeUsages(strict=false).js`** -> AI Confidence: **99.06%**
3356. **`tests/baselines/reference/regexpExecAndMatchTypeUsages(strict=true).js`** -> AI Confidence: **99.06%**
3357. **`tests/baselines/reference/requiredInitializedParameter3.js`** -> AI Confidence: **99.06%**
3358. **`tests/baselines/reference/reservedWords2.js`** -> AI Confidence: **99.06%**
3359. **`tests/baselines/reference/reservedWords3.js`** -> AI Confidence: **99.06%**
3360. **`tests/baselines/reference/restElementAssignable.js`** -> AI Confidence: **99.06%**
3361. **`tests/baselines/reference/restElementWithNullInitializer(target=es5).js`** -> AI Confidence: **99.06%**
3362. **`tests/baselines/reference/restElementWithNumberPropertyName(target=es2015).js`** -> AI Confidence: **99.06%**
3363. **`tests/baselines/reference/restElementWithNumberPropertyName(target=es5).js`** -> AI Confidence: **99.06%**
3364. **`tests/baselines/reference/restIntersection.js`** -> AI Confidence: **99.06%**
3365. **`tests/baselines/reference/restParameterInDownlevelGenerator(target=es2015).js`** -> AI Confidence: **99.06%**
3366. **`tests/baselines/reference/restParameterInDownlevelGenerator(target=es5).js`** -> AI Confidence: **99.06%**
3367. **`tests/baselines/reference/restParameterTypeInstantiation.js`** -> AI Confidence: **99.06%**
3368. **`tests/baselines/reference/restParameterWithBindingPattern3.js`** -> AI Confidence: **99.06%**
3369. **`tests/baselines/reference/restPropertyWithBindingPattern(target=es2015).js`** -> AI Confidence: **99.06%**
3370. **`tests/baselines/reference/restPropertyWithBindingPattern(target=es5).js`** -> AI Confidence: **99.06%**
3371. **`tests/baselines/reference/reuseProgramStructure/fetches-imports-after-npm-install.js`** -> AI Confidence: **99.06%**
3372. **`tests/baselines/reference/reuseProgramStructure/should-not-reuse-ambient-module-declarations-from-non-modified-files.js`** -> AI Confidence: **99.06%**
3373. **`tests/baselines/reference/reverseMappedTypeAssignableToIndex.js`** -> AI Confidence: **99.06%**
3374. **`tests/baselines/reference/scannerS7.2_A1.5_T2.js`** -> AI Confidence: **99.06%**
3375. **`tests/baselines/reference/scannerS7.6_A4.2_T1.js`** -> AI Confidence: **99.06%**
3376. **`tests/baselines/reference/scannertest1.js`** -> AI Confidence: **99.06%**
3377. **`tests/baselines/reference/selfReferencingSpreadInLoop.js`** -> AI Confidence: **99.06%**
3378. **`tests/baselines/reference/selfReferencingTypeReferenceInference.js`** -> AI Confidence: **99.06%**
3379. **`tests/baselines/reference/selfReferentialDefaultNoStackOverflow.js`** -> AI Confidence: **99.06%**
3380. **`tests/baselines/reference/signatureLengthMismatchWithOptionalParameters.js`** -> AI Confidence: **99.06%**
3381. **`tests/baselines/reference/singletonLabeledTuple.js`** -> AI Confidence: **99.06%**
3382. **`tests/baselines/reference/sourceMap-Comments(target=es5).js`** -> AI Confidence: **99.06%**
3383. **`tests/baselines/reference/sourceMapValidationDecorators(target=es2015).js`** -> AI Confidence: **99.06%**
3384. **`tests/baselines/reference/sourceMapValidationDecorators(target=es5).js`** -> AI Confidence: **99.06%**
3385. **`tests/baselines/reference/sourceMapValidationDestructuringForArrayBindingPattern2(target=es5).js`** -> AI Confidence: **99.06%**
3386. **`tests/baselines/reference/sourceMapValidationDestructuringForArrayBindingPatternDefaultValues(target=es5).js`** -> AI Confidence: **99.06%**
3387. **`tests/baselines/reference/sourceMapValidationDestructuringForArrayBindingPatternDefaultValues2(target=es2015).js`** -> AI Confidence: **99.06%**
3388. **`tests/baselines/reference/sourceMapValidationDestructuringForOfArrayBindingPattern2(target=es2015).js`** -> AI Confidence: **99.06%**
3389. **`tests/baselines/reference/sourceMapValidationDestructuringForOfArrayBindingPattern2(target=es5).js`** -> AI Confidence: **99.06%**
3390. **`tests/baselines/reference/sourceMapValidationDestructuringForOfArrayBindingPatternDefaultValues(target=es5).js`** -> AI Confidence: **99.06%**
3391. **`tests/baselines/reference/sourceMapValidationDestructuringForOfArrayBindingPatternDefaultValues2(target=es2015).js`** -> AI Confidence: **99.06%**
3392. **`tests/baselines/reference/sourceMapValidationDestructuringForOfArrayBindingPatternDefaultValues2(target=es5).js`** -> AI Confidence: **99.06%**
3393. **`tests/baselines/reference/sourceMapValidationDestructuringForOfObjectBindingPattern2(target=es5).js`** -> AI Confidence: **99.06%**
3394. **`tests/baselines/reference/sourceMapValidationDestructuringForOfObjectBindingPatternDefaultValues(target=es5).js`** -> AI Confidence: **99.06%**
3395. **`tests/baselines/reference/sourceMapValidationDestructuringParametertArrayBindingPatternDefaultValues(target=es5).js`** -> AI Confidence: **99.06%**
3396. **`tests/baselines/reference/sourceMapValidationDestructuringParametertArrayBindingPatternDefaultValues2(target=es5).js`** -> AI Confidence: **99.06%**
3397. **`tests/baselines/reference/sourceMapValidationDestructuringVariableStatementArrayBindingPatternDefaultValues3(target=es5).js`** -> AI Confidence: **99.06%**
3398. **`tests/baselines/reference/sourceMapValidationEnums.js`** -> AI Confidence: **99.06%**
3399. **`tests/baselines/reference/sourceMapValidationForIn.js`** -> AI Confidence: **99.06%**
3400. **`tests/baselines/reference/sourceMapValidationStatements.js`** -> AI Confidence: **99.06%**
3401. **`tests/baselines/reference/sourceMapValidationWhile.js`** -> AI Confidence: **99.06%**
3402. **`tests/baselines/reference/spellingSuggestionJSXAttribute.js`** -> AI Confidence: **99.06%**
3403. **`tests/baselines/reference/spreadBooleanRespectsFreshness.js`** -> AI Confidence: **99.06%**
3404. **`tests/baselines/reference/spreadExpressionContextualTypeWithNamespace.js`** -> AI Confidence: **99.06%**
3405. **`tests/baselines/reference/spreadIdenticalTypesRemoved.js`** -> AI Confidence: **99.06%**
3406. **`tests/baselines/reference/spreadUnionPropOverride.js`** -> AI Confidence: **99.06%**
3407. **`tests/baselines/reference/spyComparisonChecking.js`** -> AI Confidence: **99.06%**
3408. **`tests/baselines/reference/stackDepthLimitCastingType.js`** -> AI Confidence: **99.06%**
3409. **`tests/baselines/reference/staticAutoAccessors(target=es2017).js`** -> AI Confidence: **99.06%**
3410. **`tests/baselines/reference/staticAutoAccessorsWithDecorators(target=es2017).js`** -> AI Confidence: **99.06%**
3411. **`tests/baselines/reference/staticAutoAccessorsWithDecorators(target=es2022).js`** -> AI Confidence: **99.06%**
3412. **`tests/baselines/reference/staticInitializersAndLegacyClassDecorators.js`** -> AI Confidence: **99.06%**
3413. **`tests/baselines/reference/strictModeEnumMemberNameReserved.js`** -> AI Confidence: **99.06%**
3414. **`tests/baselines/reference/strictModeReservedWord2.js`** -> AI Confidence: **99.06%**
3415. **`tests/baselines/reference/strictNullEmptyDestructuring(target=es2015).js`** -> AI Confidence: **99.06%**
3416. **`tests/baselines/reference/strictNullEmptyDestructuring(target=es5).js`** -> AI Confidence: **99.06%**
3417. **`tests/baselines/reference/strictNullLogicalAndOr.js`** -> AI Confidence: **99.06%**
3418. **`tests/baselines/reference/strictTypeofUnionNarrowing.js`** -> AI Confidence: **99.06%**
3419. **`tests/baselines/reference/stringEnumInElementAccess01.js`** -> AI Confidence: **99.06%**
3420. **`tests/baselines/reference/stringEnumLiteralTypes3.js`** -> AI Confidence: **99.06%**
3421. **`tests/baselines/reference/stringLiteralCheckedInIf01.js`** -> AI Confidence: **99.06%**
3422. **`tests/baselines/reference/stringLiteralCheckedInIf02.js`** -> AI Confidence: **99.06%**
3423. **`tests/baselines/reference/stringLiteralTypesOverloads01.js`** -> AI Confidence: **99.06%**
3424. **`tests/baselines/reference/stringLiteralTypesOverloads02.js`** -> AI Confidence: **99.06%**
3425. **`tests/baselines/reference/substitutionTypePassedToExtends.js`** -> AI Confidence: **99.06%**
3426. **`tests/baselines/reference/substitutionTypesCompareCorrectlyInRestrictiveInstances.js`** -> AI Confidence: **99.06%**
3427. **`tests/baselines/reference/substitutionTypesInIndexedAccessTypes.js`** -> AI Confidence: **99.06%**
3428. **`tests/baselines/reference/subtypesOfTypeParameterWithConstraints3.js`** -> AI Confidence: **99.06%**
3429. **`tests/baselines/reference/subtypingWithObjectMembers2.js`** -> AI Confidence: **99.06%**
3430. **`tests/baselines/reference/subtypingWithObjectMembers3.js`** -> AI Confidence: **99.06%**
3431. **`tests/baselines/reference/switchCaseWithIntersectionTypes01.js`** -> AI Confidence: **99.06%**
3432. **`tests/baselines/reference/switchCaseWithUnionTypes01.js`** -> AI Confidence: **99.06%**
3433. **`tests/baselines/reference/switchFallThroughs.js`** -> AI Confidence: **99.06%**
3434. **`tests/baselines/reference/symbolProperty53.js`** -> AI Confidence: **99.06%**
3435. **`tests/baselines/reference/symbolType10.js`** -> AI Confidence: **99.06%**
3436. **`tests/baselines/reference/symbolType12.js`** -> AI Confidence: **99.06%**
3437. **`tests/baselines/reference/symbolType13.js`** -> AI Confidence: **99.06%**
3438. **`tests/baselines/reference/symbolType17.js`** -> AI Confidence: **99.06%**
3439. **`tests/baselines/reference/symbolType18.js`** -> AI Confidence: **99.06%**
3440. **`tests/baselines/reference/symbolType19.js`** -> AI Confidence: **99.06%**
3441. **`tests/baselines/reference/symbolType4.js`** -> AI Confidence: **99.06%**
3442. **`tests/baselines/reference/symbolType5.js`** -> AI Confidence: **99.06%**
3443. **`tests/baselines/reference/symbolType6.js`** -> AI Confidence: **99.06%**
3444. **`tests/baselines/reference/symbolType7.js`** -> AI Confidence: **99.06%**
3445. **`tests/baselines/reference/symbolType9.js`** -> AI Confidence: **99.06%**
3446. **`tests/baselines/reference/symlinkedWorkspaceDependenciesNoDirectLinkGeneratesDeepNonrelativeName.js`** -> AI Confidence: **99.06%**
3447. **`tests/baselines/reference/symlinkedWorkspaceDependenciesNoDirectLinkGeneratesNonrelativeName.js`** -> AI Confidence: **99.06%**
3448. **`tests/baselines/reference/symlinkedWorkspaceDependenciesNoDirectLinkOptionalGeneratesNonrelativeName.js`** -> AI Confidence: **99.06%**
3449. **`tests/baselines/reference/symlinkedWorkspaceDependenciesNoDirectLinkPeerGeneratesNonrelativeName.js`** -> AI Confidence: **99.06%**
3450. **`tests/baselines/reference/systemModule8.js`** -> AI Confidence: **99.06%**
3451. **`tests/baselines/reference/taggedTemplateChain.js`** -> AI Confidence: **99.06%**
3452. **`tests/baselines/reference/targetEs6DecoratorMetadataImportNotElided(target=es2015).js`** -> AI Confidence: **99.06%**
3453. **`tests/baselines/reference/templateLiteralEscapeSequence.js`** -> AI Confidence: **99.06%**
3454. **`tests/baselines/reference/templateLiteralsAndDecoratorMetadata.js`** -> AI Confidence: **99.06%**
3455. **`tests/baselines/reference/templateStringInConditional.js`** -> AI Confidence: **99.06%**
3456. **`tests/baselines/reference/templateStringInConditionalES6.js`** -> AI Confidence: **99.06%**
3457. **`tests/baselines/reference/templateStringWithEmbeddedConditional.js`** -> AI Confidence: **99.06%**
3458. **`tests/baselines/reference/templateStringWithEmbeddedConditionalES6.js`** -> AI Confidence: **99.06%**
3459. **`tests/baselines/reference/templateStringsArrayTypeNotDefinedES5Mode(target=es5).js`** -> AI Confidence: **99.06%**
3460. **`tests/baselines/reference/thisAndSuperInStaticMembers3(target=es5).js`** -> AI Confidence: **99.06%**
3461. **`tests/baselines/reference/thisAndSuperInStaticMembers4(target=es5).js`** -> AI Confidence: **99.06%**
3462. **`tests/baselines/reference/thisAssignmentInNamespaceDeclaration1.js`** -> AI Confidence: **99.06%**
3463. **`tests/baselines/reference/thisKeyword.js`** -> AI Confidence: **99.06%**
3464. **`tests/baselines/reference/thisMethodCall.js`** -> AI Confidence: **99.06%**
3465. **`tests/baselines/reference/thisTypeInObjectLiterals2(target=es2015).js`** -> AI Confidence: **99.06%**
3466. **`tests/baselines/reference/thisTypeInObjectLiterals2(target=es5).js`** -> AI Confidence: **99.06%**
3467. **`tests/baselines/reference/thisTypeSyntacticContext.js`** -> AI Confidence: **99.06%**
3468. **`tests/baselines/reference/this_inside-enum-should-not-be-allowed.js`** -> AI Confidence: **99.06%**
3469. **`tests/baselines/reference/throwInEnclosingStatements.js`** -> AI Confidence: **99.06%**
3470. **`tests/baselines/reference/topLevelVarHoistingCommonJS.js`** -> AI Confidence: **99.06%**
3471. **`tests/baselines/reference/trailingCommasInBindingPatterns.js`** -> AI Confidence: **99.06%**
3472. **`tests/baselines/reference/transformApi/transformsCorrectly.rewrittenNamespace.js`** -> AI Confidence: **99.06%**
3473. **`tests/baselines/reference/transformApi/transformsCorrectly.rewrittenNamespaceFollowingClass.js`** -> AI Confidence: **99.06%**
3474. **`tests/baselines/reference/transformApi/transformsCorrectly.synthesizedClassAndNamespaceCombination.js`** -> AI Confidence: **99.06%**
3475. **`tests/baselines/reference/transformApi/transformsCorrectly.transformAddCommentToImport.js`** -> AI Confidence: **99.06%**
3476. **`tests/baselines/reference/transformApi/transformsCorrectly.transformAddCommentToNamespace.js`** -> AI Confidence: **99.06%**
3477. **`tests/baselines/reference/transformApi/transformsCorrectly.transformParameterProperty.js`** -> AI Confidence: **99.06%**
3478. **`tests/baselines/reference/transformApi/transformsCorrectly.transformSyntheticCommentOnStaticFieldInClassExpression.js`** -> AI Confidence: **99.06%**
3479. **`tests/baselines/reference/transformApi/transformsCorrectly.transformTaggedTemplateLiteral.js`** -> AI Confidence: **99.06%**
3480. **`tests/baselines/reference/transformApi/transformsCorrectly.transformUpdateModuleMember.js`** -> AI Confidence: **99.06%**
3481. **`tests/baselines/reference/transformNestedGeneratorsWithTry(target=es2015).js`** -> AI Confidence: **99.06%**
3482. **`tests/baselines/reference/transformNestedGeneratorsWithTry(target=es5).js`** -> AI Confidence: **99.06%**
3483. **`tests/baselines/reference/transpile/Correctly serialize metadata when transpile with CommonJS option (verbatimModuleSyntax=true).js`** -> AI Confidence: **99.06%**
3484. **`tests/baselines/reference/transpile/Correctly serialize metadata when transpile with CommonJS option (verbatimModuleSyntax=true).oldTranspile.js`** -> AI Confidence: **99.06%**
3485. **`tests/baselines/reference/transpile/Correctly serialize metadata when transpile with CommonJS option.js`** -> AI Confidence: **99.06%**
3486. **`tests/baselines/reference/transpile/Correctly serialize metadata when transpile with CommonJS option.oldTranspile.js`** -> AI Confidence: **99.06%**
3487. **`tests/baselines/reference/transpile/Correctly serialize metadata when transpile with System option.js`** -> AI Confidence: **99.06%**
3488. **`tests/baselines/reference/transpile/Correctly serialize metadata when transpile with System option.oldTranspile.js`** -> AI Confidence: **99.06%**
3489. **`tests/baselines/reference/transpile/Export star as ns conflict does not crash (verbatimModuleSyntax=true).js`** -> AI Confidence: **99.06%**
3490. **`tests/baselines/reference/transpile/Export star as ns conflict does not crash (verbatimModuleSyntax=true).oldTranspile.js`** -> AI Confidence: **99.06%**
3491. **`tests/baselines/reference/transpile/Export star as ns conflict does not crash.js`** -> AI Confidence: **99.06%**
3492. **`tests/baselines/reference/transpile/Export star as ns conflict does not crash.oldTranspile.js`** -> AI Confidence: **99.06%**
3493. **`tests/baselines/reference/truthinessCallExpressionCoercion.js`** -> AI Confidence: **99.06%**
3494. **`tests/baselines/reference/truthinessCallExpressionCoercion1.js`** -> AI Confidence: **99.06%**
3495. **`tests/baselines/reference/truthinessCallExpressionCoercion3.js`** -> AI Confidence: **99.06%**
3496. **`tests/baselines/reference/tryCatchFinallyControlFlow.js`** -> AI Confidence: **99.06%**
3497. **`tests/baselines/reference/tsbuild/declarationEmit/outFile/reports-dts-generation-errors-with-incremental.js`** -> AI Confidence: **99.06%**
3498. **`tests/baselines/reference/tsbuild/declarationEmit/outFile/reports-dts-generation-errors.js`** -> AI Confidence: **99.06%**
3499. **`tests/baselines/reference/tsbuild/fileDelete/outFile/deleted-file-without-composite.js`** -> AI Confidence: **99.06%**
3500. **`tests/baselines/reference/tsbuild/moduleResolution/impliedNodeFormat-differs-between-projects-for-shared-file.js`** -> AI Confidence: **99.06%**
3501. **`tests/baselines/reference/tsbuild/noEmit/multiFile/dts-errors-with-declaration-enable-changes.js`** -> AI Confidence: **99.06%**
3502. **`tests/baselines/reference/tsbuild/noEmit/multiFile/dts-errors.js`** -> AI Confidence: **99.06%**
3503. **`tests/baselines/reference/tsbuild/noEmitOnError/outFile/semantic-errors-with-declaration.js`** -> AI Confidence: **99.06%**
3504. **`tests/baselines/reference/tsbuild/noEmitOnError/outFile/semantic-errors.js`** -> AI Confidence: **99.06%**
3505. **`tests/baselines/reference/tsbuild/noEmitOnError/outFile/syntax-errors-with-declaration.js`** -> AI Confidence: **99.06%**
3506. **`tests/baselines/reference/tsbuild/noEmitOnError/outFile/syntax-errors.js`** -> AI Confidence: **99.06%**
3507. **`tests/baselines/reference/tsbuild/resolveJsonModule/files-containing-json-file.js`** -> AI Confidence: **99.06%**
3508. **`tests/baselines/reference/tsbuild/resolveJsonModule/include-and-files.js`** -> AI Confidence: **99.06%**
3509. **`tests/baselines/reference/tsbuild/resolveJsonModule/include-of-json-along-with-other-include-and-file-name-matches-ts-file.js`** -> AI Confidence: **99.06%**
3510. **`tests/baselines/reference/tsbuild/resolveJsonModule/include-of-json-along-with-other-include.js`** -> AI Confidence: **99.06%**
3511. **`tests/baselines/reference/tsbuild/resolveJsonModule/sourcemap.js`** -> AI Confidence: **99.06%**
3512. **`tests/baselines/reference/tsbuildWatch/noEmit/multiFile/dts-errors.js`** -> AI Confidence: **99.06%**
3513. **`tests/baselines/reference/tsbuildWatch/noEmit/outFile/dts-errors.js`** -> AI Confidence: **99.06%**
3514. **`tests/baselines/reference/tsbuildWatch/noEmitOnError/multiFile/noEmitOnError-with-declaration.js`** -> AI Confidence: **99.06%**
3515. **`tests/baselines/reference/tsbuildWatch/noEmitOnError/multiFile/noEmitOnError.js`** -> AI Confidence: **99.06%**
3516. **`tests/baselines/reference/tsbuildWatch/noEmitOnError/outFile/noEmitOnError-with-declaration.js`** -> AI Confidence: **99.06%**
3517. **`tests/baselines/reference/tsbuildWatch/noEmitOnError/outFile/noEmitOnError.js`** -> AI Confidence: **99.06%**
3518. **`tests/baselines/reference/tsbuildWatch/programUpdates/works-when-noUnusedParameters-changes-to-false.js`** -> AI Confidence: **99.06%**
3519. **`tests/baselines/reference/tsbuildWatch/watchEnvironment/same-file-in-multiple-projects-with-single-watcher-per-file.js`** -> AI Confidence: **99.06%**
3520. **`tests/baselines/reference/tsc/declarationEmit/multiFile/reports-dts-generation-errors.js`** -> AI Confidence: **99.06%**
3521. **`tests/baselines/reference/tsc/declarationEmit/outFile/reports-dts-generation-errors.js`** -> AI Confidence: **99.06%**
3522. **`tests/baselines/reference/tsc/declarationEmit/when-pkg-references-sibling-package-through-indirect-symlink-moduleCaseChange.js`** -> AI Confidence: **99.06%**
3523. **`tests/baselines/reference/tsc/declarationEmit/when-pkg-references-sibling-package-through-indirect-symlink.js`** -> AI Confidence: **99.06%**
3524. **`tests/baselines/reference/tsc/projectReferences/when-project-contains-invalid-project-reference.js`** -> AI Confidence: **99.06%**
3525. **`tests/baselines/reference/tscWatch/emit/emit-file-content/file-is-deleted-and-created-as-part-of-change.js`** -> AI Confidence: **99.06%**
3526. **`tests/baselines/reference/tscWatch/emit/emit-with-outFile-or-out-setting/config-does-not-have-out-or-outFile.js`** -> AI Confidence: **99.06%**
3527. **`tests/baselines/reference/tscWatch/forceConsistentCasingInFileNames/package-json-is-looked-up-for-file.js`** -> AI Confidence: **99.06%**
3528. **`tests/baselines/reference/tscWatch/forceConsistentCasingInFileNames/when-Windows-style-drive-root-is-lowercase.js`** -> AI Confidence: **99.06%**
3529. **`tests/baselines/reference/tscWatch/forceConsistentCasingInFileNames/when-Windows-style-drive-root-is-uppercase.js`** -> AI Confidence: **99.06%**
3530. **`tests/baselines/reference/tscWatch/forceConsistentCasingInFileNames/when-both-file-symlink-target-and-import-match-disk.js`** -> AI Confidence: **99.06%**
3531. **`tests/baselines/reference/tscWatch/forceConsistentCasingInFileNames/when-file-symlink-target-matches-disk-but-import-does-not.js`** -> AI Confidence: **99.06%**
3532. **`tests/baselines/reference/tscWatch/forceConsistentCasingInFileNames/when-import,-file-symlink-target,-and-disk-are-all-different.js`** -> AI Confidence: **99.06%**
3533. **`tests/baselines/reference/tscWatch/forceConsistentCasingInFileNames/when-import-and-file-symlink-target-agree-but-do-not-match-disk.js`** -> AI Confidence: **99.06%**
3534. **`tests/baselines/reference/tscWatch/forceConsistentCasingInFileNames/when-import-matches-disk-but-file-symlink-target-does-not.js`** -> AI Confidence: **99.06%**
3535. **`tests/baselines/reference/tscWatch/forceConsistentCasingInFileNames/with-nodeNext-resolution.js`** -> AI Confidence: **99.06%**
3536. **`tests/baselines/reference/tscWatch/incremental/importHelpers-backing-types-removed-watch.js`** -> AI Confidence: **99.06%**
3537. **`tests/baselines/reference/tscWatch/libraryResolution/without-config-with-redirection.js`** -> AI Confidence: **99.06%**
3538. **`tests/baselines/reference/tscWatch/libraryResolution/without-config.js`** -> AI Confidence: **99.06%**
3539. **`tests/baselines/reference/tscWatch/moduleResolution/watches-for-changes-to-package-json-main-fields.js`** -> AI Confidence: **99.06%**
3540. **`tests/baselines/reference/tscWatch/noEmit/multiFile/dts-errors.js`** -> AI Confidence: **99.06%**
3541. **`tests/baselines/reference/tscWatch/noEmit/outFile/dts-errors.js`** -> AI Confidence: **99.06%**
3542. **`tests/baselines/reference/tscWatch/noEmitOnError/multiFile/noEmitOnError.js`** -> AI Confidence: **99.06%**
3543. **`tests/baselines/reference/tscWatch/noEmitOnError/outFile/noEmitOnError-with-declaration.js`** -> AI Confidence: **99.06%**
3544. **`tests/baselines/reference/tscWatch/noEmitOnError/outFile/noEmitOnError.js`** -> AI Confidence: **99.06%**
3545. **`tests/baselines/reference/tscWatch/nodeNextWatch/esm-mode-file-is-edited.js`** -> AI Confidence: **99.06%**
3546. **`tests/baselines/reference/tscWatch/programUpdates/Configure-file-diagnostics-events-are-generated-when-the-config-file-has-errors.js`** -> AI Confidence: **99.06%**
3547. **`tests/baselines/reference/tscWatch/programUpdates/Options-Diagnostic-locations-reported-correctly-with-changes-in-configFile-contents-when-options-change.js`** -> AI Confidence: **99.06%**
3548. **`tests/baselines/reference/tscWatch/programUpdates/Updates-diagnostics-when-'--allowArbitraryExtensions'-changes.js`** -> AI Confidence: **99.06%**
3549. **`tests/baselines/reference/tscWatch/programUpdates/add-new-files-to-a-configured-program-without-file-list.js`** -> AI Confidence: **99.06%**
3550. **`tests/baselines/reference/tscWatch/programUpdates/add-the-missing-module-file-for-inferred-project-should-remove-the-module-not-found-error.js`** -> AI Confidence: **99.06%**
3551. **`tests/baselines/reference/tscWatch/programUpdates/can-correctly-update-configured-project-when-set-of-root-files-has-changed-(new-file-in-list-of-files).js`** -> AI Confidence: **99.06%**
3552. **`tests/baselines/reference/tscWatch/programUpdates/can-correctly-update-configured-project-when-set-of-root-files-has-changed-(new-file-on-disk).js`** -> AI Confidence: **99.06%**
3553. **`tests/baselines/reference/tscWatch/programUpdates/can-correctly-update-configured-project-when-set-of-root-files-has-changed-through-include.js`** -> AI Confidence: **99.06%**
3554. **`tests/baselines/reference/tscWatch/programUpdates/can-handle-tsconfig-file-name-with-difference-casing.js`** -> AI Confidence: **99.06%**
3555. **`tests/baselines/reference/tscWatch/programUpdates/correctly-handles-changes-in-lib-section-of-config-file.js`** -> AI Confidence: **99.06%**
3556. **`tests/baselines/reference/tscWatch/programUpdates/extended-source-files-are-watched.js`** -> AI Confidence: **99.06%**
3557. **`tests/baselines/reference/tscWatch/programUpdates/file-in-files-is-deleted.js`** -> AI Confidence: **99.06%**
3558. **`tests/baselines/reference/tscWatch/programUpdates/handle-recreated-files-correctly.js`** -> AI Confidence: **99.06%**
3559. **`tests/baselines/reference/tscWatch/programUpdates/handles-the-missing-files---that-were-added-to-program-because-they-were-added-with-tripleSlashRefs.js`** -> AI Confidence: **99.06%**
3560. **`tests/baselines/reference/tscWatch/programUpdates/if-config-file-doesnt-have-errors,-they-are-not-reported.js`** -> AI Confidence: **99.06%**
3561. **`tests/baselines/reference/tscWatch/programUpdates/non-existing-directories-listed-in-config-file-input-array-should-be-tolerated-without-crashing-the-server.js`** -> AI Confidence: **99.06%**
3562. **`tests/baselines/reference/tscWatch/programUpdates/rename-a-module-file-and-rename-back-should-restore-the-states-for-configured-projects.js`** -> AI Confidence: **99.06%**
3563. **`tests/baselines/reference/tscWatch/programUpdates/rename-a-module-file-and-rename-back-should-restore-the-states-for-inferred-projects.js`** -> AI Confidence: **99.06%**
3564. **`tests/baselines/reference/tscWatch/programUpdates/reports-errors-correctly-with-isolatedModules.js`** -> AI Confidence: **99.06%**
3565. **`tests/baselines/reference/tscWatch/programUpdates/should-handle-non-existing-directories-in-config-file.js`** -> AI Confidence: **99.06%**
3566. **`tests/baselines/reference/tscWatch/programUpdates/should-not-trigger-recompilation-because-of-program-emit/when-outDir-is-specified.js`** -> AI Confidence: **99.06%**
3567. **`tests/baselines/reference/tscWatch/programUpdates/should-not-trigger-recompilation-because-of-program-emit/without-outDir-or-outFile-is-specified.js`** -> AI Confidence: **99.06%**
3568. **`tests/baselines/reference/tscWatch/programUpdates/should-reflect-change-in-config-file.js`** -> AI Confidence: **99.06%**
3569. **`tests/baselines/reference/tscWatch/programUpdates/should-support-files-without-extensions.js`** -> AI Confidence: **99.06%**
3570. **`tests/baselines/reference/tscWatch/programUpdates/shouldnt-report-error-about-unused-function-incorrectly-when-file-changes-from-global-to-module.js`** -> AI Confidence: **99.06%**
3571. **`tests/baselines/reference/tscWatch/programUpdates/types-should-load-from-config-file-path-if-config-exists.js`** -> AI Confidence: **99.06%**
3572. **`tests/baselines/reference/tscWatch/programUpdates/types-should-not-load-from-config-file-path-if-config-exists-but-does-not-specifies-typeRoots.js`** -> AI Confidence: **99.06%**
3573. **`tests/baselines/reference/tscWatch/programUpdates/updates-diagnostics-and-emit-for-decorators.js`** -> AI Confidence: **99.06%**
3574. **`tests/baselines/reference/tscWatch/programUpdates/updates-errors-correctly-when-declaration-emit-is-disabled-in-compiler-options.js`** -> AI Confidence: **99.06%**
3575. **`tests/baselines/reference/tscWatch/programUpdates/updates-errors-in-lib-file/when-module-file-with-global-definitions-changes/with-default-options.js`** -> AI Confidence: **99.06%**
3576. **`tests/baselines/reference/tscWatch/programUpdates/updates-errors-in-lib-file/when-module-file-with-global-definitions-changes/with-skipDefaultLibCheck.js`** -> AI Confidence: **99.06%**
3577. **`tests/baselines/reference/tscWatch/programUpdates/updates-errors-in-lib-file/when-module-file-with-global-definitions-changes/with-skipLibCheck.js`** -> AI Confidence: **99.06%**
3578. **`tests/baselines/reference/tscWatch/programUpdates/updates-errors-in-lib-file/when-non-module-file-changes/with-default-options.js`** -> AI Confidence: **99.06%**
3579. **`tests/baselines/reference/tscWatch/programUpdates/updates-errors-in-lib-file/when-non-module-file-changes/with-skipDefaultLibCheck.js`** -> AI Confidence: **99.06%**
3580. **`tests/baselines/reference/tscWatch/programUpdates/updates-errors-in-lib-file/when-non-module-file-changes/with-skipLibCheck.js`** -> AI Confidence: **99.06%**
3581. **`tests/baselines/reference/tscWatch/programUpdates/updates-moduleResolution-when-resolveJsonModule-changes.js`** -> AI Confidence: **99.06%**
3582. **`tests/baselines/reference/tscWatch/programUpdates/watched-files-when-file-is-deleted-and-new-file-is-added-as-part-of-change.js`** -> AI Confidence: **99.06%**
3583. **`tests/baselines/reference/tscWatch/programUpdates/when-changing-`allowImportingTsExtensions`-of-config-file-2.js`** -> AI Confidence: **99.06%**
3584. **`tests/baselines/reference/tscWatch/programUpdates/when-changing-`allowImportingTsExtensions`-of-config-file.js`** -> AI Confidence: **99.06%**
3585. **`tests/baselines/reference/tscWatch/programUpdates/when-changing-checkJs-of-config-file.js`** -> AI Confidence: **99.06%**
3586. **`tests/baselines/reference/tscWatch/programUpdates/when-changing-noUncheckedSideEffectImports-of-config-file.js`** -> AI Confidence: **99.06%**
3587. **`tests/baselines/reference/tscWatch/programUpdates/works-correctly-when-config-file-is-changed-but-its-content-havent.js`** -> AI Confidence: **99.06%**
3588. **`tests/baselines/reference/tscWatch/resolutionCache/caching-works.js`** -> AI Confidence: **99.06%**
3589. **`tests/baselines/reference/tscWatch/resolutionCache/ignores-changes-in-node_modules-that-start-with-dot/watch-with-configFile.js`** -> AI Confidence: **99.06%**
3590. **`tests/baselines/reference/tscWatch/resolutionCache/ignores-changes-in-node_modules-that-start-with-dot/watch-without-configFile.js`** -> AI Confidence: **99.06%**
3591. **`tests/baselines/reference/tscWatch/resolutionCache/loads-missing-files-from-disk.js`** -> AI Confidence: **99.06%**
3592. **`tests/baselines/reference/tscWatch/resolutionCache/scoped-package-installation.js`** -> AI Confidence: **99.06%**
3593. **`tests/baselines/reference/tscWatch/resolutionCache/should-compile-correctly-when-resolved-module-goes-missing-and-then-comes-back.js`** -> AI Confidence: **99.06%**
3594. **`tests/baselines/reference/tscWatch/resolutionCache/works-when-included-file-with-ambient-module-changes.js`** -> AI Confidence: **99.06%**
3595. **`tests/baselines/reference/tscWatch/resolutionCache/works-when-module-resolution-changes-to-ambient-module.js`** -> AI Confidence: **99.06%**
3596. **`tests/baselines/reference/tscWatch/resolutionCache/works-when-renaming-node_modules-folder-that-already-contains-@types-folder.js`** -> AI Confidence: **99.06%**
3597. **`tests/baselines/reference/tscWatch/watchApi/host-implements-does-not-implement-hasInvalidatedResolutions.js`** -> AI Confidence: **99.06%**
3598. **`tests/baselines/reference/tscWatch/watchApi/host-implements-hasInvalidatedResolutions.js`** -> AI Confidence: **99.06%**
3599. **`tests/baselines/reference/tscWatch/watchApi/multiFile/verifies-that-noEmit-is-handled-on-createSemanticDiagnosticsBuilderProgram.js`** -> AI Confidence: **99.06%**
3600. **`tests/baselines/reference/tscWatch/watchApi/verify-that-the-error-count-is-correctly-passed-down-to-the-watch-status-reporter.js`** -> AI Confidence: **99.06%**
3601. **`tests/baselines/reference/tscWatch/watchApi/when-watching-referenced-project-when-there-is-no-config-file-name.js`** -> AI Confidence: **99.06%**
3602. **`tests/baselines/reference/tscWatch/watchApi/when-watching-referenced-project-with-extends-when-there-is-no-config-file-name.js`** -> AI Confidence: **99.06%**
3603. **`tests/baselines/reference/tscWatch/watchEnvironment/fsWatch/fsWatchWithTimestamp-false-useFsEventsOnParentDirectory.js`** -> AI Confidence: **99.06%**
3604. **`tests/baselines/reference/tscWatch/watchEnvironment/fsWatch/fsWatchWithTimestamp-false.js`** -> AI Confidence: **99.06%**
3605. **`tests/baselines/reference/tscWatch/watchEnvironment/fsWatch/fsWatchWithTimestamp-true-useFsEventsOnParentDirectory.js`** -> AI Confidence: **99.06%**
3606. **`tests/baselines/reference/tscWatch/watchEnvironment/fsWatch/fsWatchWithTimestamp-true.js`** -> AI Confidence: **99.06%**
3607. **`tests/baselines/reference/tscWatch/watchEnvironment/fsWatch/when-using-file-watching-thats-on-inode-when-rename-event-ends-with-tilde.js`** -> AI Confidence: **99.06%**
3608. **`tests/baselines/reference/tscWatch/watchEnvironment/fsWatch/when-using-file-watching-thats-on-inode-when-rename-occurs-when-file-is-still-on-the-disk.js`** -> AI Confidence: **99.06%**
3609. **`tests/baselines/reference/tscWatch/watchEnvironment/fsWatch/when-using-file-watching-thats-on-inode.js`** -> AI Confidence: **99.06%**
3610. **`tests/baselines/reference/tscWatch/watchEnvironment/fsWatch/when-using-file-watching-thats-when-rename-occurs-when-file-is-still-on-the-disk.js`** -> AI Confidence: **99.06%**
3611. **`tests/baselines/reference/tscWatch/watchEnvironment/watchDirectories/when-there-are-symlinks-to-folders-in-recursive-folders-with-synchronousWatchDirectory.js`** -> AI Confidence: **99.06%**
3612. **`tests/baselines/reference/tscWatch/watchEnvironment/watchDirectories/when-there-are-symlinks-to-folders-in-recursive-folders.js`** -> AI Confidence: **99.06%**
3613. **`tests/baselines/reference/tscWatch/watchEnvironment/watchDirectories/with-non-synchronous-watch-directory-renaming-a-file.js`** -> AI Confidence: **99.06%**
3614. **`tests/baselines/reference/tscWatch/watchEnvironment/watchDirectories/with-non-synchronous-watch-directory.js`** -> AI Confidence: **99.06%**
3615. **`tests/baselines/reference/tscWatch/watchEnvironment/watchFile/using-dynamic-priority-polling.js`** -> AI Confidence: **99.06%**
3616. **`tests/baselines/reference/tscWatch/watchEnvironment/watchFile/using-fixed-chunk-size-polling.js`** -> AI Confidence: **99.06%**
3617. **`tests/baselines/reference/tsconfigMapOptionsAreCaseInsensitive.js`** -> AI Confidence: **99.06%**
3618. **`tests/baselines/reference/tslibNotFoundDifferentModules.js`** -> AI Confidence: **99.06%**
3619. **`tests/baselines/reference/tsserver/autoImportProvider/Auto-importable-file-is-in-inferred-project-until-imported.js`** -> AI Confidence: **99.06%**
3620. **`tests/baselines/reference/tsserver/autoImportProvider/Closes-AutoImportProviderProject-when-host-project-closes.js`** -> AI Confidence: **99.06%**
3621. **`tests/baselines/reference/tsserver/autoImportProvider/Does-not-close-when-root-files-are-redirects-that-dont-actually-exist.js`** -> AI Confidence: **99.06%**
3622. **`tests/baselines/reference/tsserver/autoImportProvider/Does-not-schedule-ensureProjectForOpenFiles-on-AutoImportProviderProject-creation.js`** -> AI Confidence: **99.06%**
3623. **`tests/baselines/reference/tsserver/autoImportProvider/Recovers-from-an-unparseable-package_json.js`** -> AI Confidence: **99.06%**
3624. **`tests/baselines/reference/tsserver/autoImportProvider/Responds-to-manual-changes-in-node_modules.js`** -> AI Confidence: **99.06%**
3625. **`tests/baselines/reference/tsserver/autoImportProvider/Responds-to-package_json-changes.js`** -> AI Confidence: **99.06%**
3626. **`tests/baselines/reference/tsserver/autoImportProvider/Reuses-autoImportProvider-when-program-structure-is-unchanged.js`** -> AI Confidence: **99.06%**
3627. **`tests/baselines/reference/tsserver/autoImportProvider/without-dependencies-listed.js`** -> AI Confidence: **99.06%**
3628. **`tests/baselines/reference/tsserver/auxiliaryProject/does-not-remove-scrips-from-InferredProject.js`** -> AI Confidence: **99.06%**
3629. **`tests/baselines/reference/tsserver/cachingFileSystemInformation/when-node_modules-dont-receive-event-for-the-@types-file-addition.js`** -> AI Confidence: **99.06%**
3630. **`tests/baselines/reference/tsserver/cachingFileSystemInformation/works-using-legacy-resolution-logic.js`** -> AI Confidence: **99.06%**
3631. **`tests/baselines/reference/tsserver/cancellationT/Geterr-is-cancellable.js`** -> AI Confidence: **99.06%**
3632. **`tests/baselines/reference/tsserver/compileOnSave/dtsFileChange-in-global-file-with-composite.js`** -> AI Confidence: **99.06%**
3633. **`tests/baselines/reference/tsserver/compileOnSave/dtsFileChange-in-global-file-with-decorator-emit.js`** -> AI Confidence: **99.06%**
3634. **`tests/baselines/reference/tsserver/compileOnSave/dtsFileChange-in-global-file-with-dts-emit.js`** -> AI Confidence: **99.06%**
3635. **`tests/baselines/reference/tsserver/compileOnSave/dtsFileChange-in-global-file.js`** -> AI Confidence: **99.06%**
3636. **`tests/baselines/reference/tsserver/compileOnSave/dtsFileChange-in-module-file.js`** -> AI Confidence: **99.06%**
3637. **`tests/baselines/reference/tsserver/compileOnSave/line-endings.js`** -> AI Confidence: **99.06%**
3638. **`tests/baselines/reference/tsserver/completions/in-project-reference-setup-with-path-mapping-without-includeCompletionsForModuleExports.js`** -> AI Confidence: **99.06%**
3639. **`tests/baselines/reference/tsserver/completions/in-project-where-there-are-no-imports-but-has-project-references-setup.js`** -> AI Confidence: **99.06%**
3640. **`tests/baselines/reference/tsserver/configuredProjects/creating-new-file-and-then-open-it-after-watcher-is-invoked,-ask-errors-on-it-after-old-one-without-file-being-in-config.js`** -> AI Confidence: **99.06%**
3641. **`tests/baselines/reference/tsserver/configuredProjects/creating-new-file-and-then-open-it-after-watcher-is-invoked,-ask-errors-on-it-before-old-one-without-file-being-in-config.js`** -> AI Confidence: **99.06%**
3642. **`tests/baselines/reference/tsserver/configuredProjects/creating-new-file-and-then-open-it-before-watcher-is-invoked,-ask-errors-on-it-after-old-one-without-file-being-in-config.js`** -> AI Confidence: **99.06%**
3643. **`tests/baselines/reference/tsserver/configuredProjects/creating-new-file-and-then-open-it-before-watcher-is-invoked,-ask-errors-on-it-after-old-one.js`** -> AI Confidence: **99.06%**
3644. **`tests/baselines/reference/tsserver/configuredProjects/creating-new-file-and-then-open-it-before-watcher-is-invoked,-ask-errors-on-it-before-old-one-without-file-being-in-config.js`** -> AI Confidence: **99.06%**
3645. **`tests/baselines/reference/tsserver/configuredProjects/creating-new-file-and-then-open-it-before-watcher-is-invoked,-ask-errors-on-it-before-old-one.js`** -> AI Confidence: **99.06%**
3646. **`tests/baselines/reference/tsserver/configuredProjects/files-are-properly-detached-when-language-service-is-disabled.js`** -> AI Confidence: **99.06%**
3647. **`tests/baselines/reference/tsserver/configuredProjects/files-explicitly-excluded-in-config-file.js`** -> AI Confidence: **99.06%**
3648. **`tests/baselines/reference/tsserver/configuredProjects/handle-recreated-files-correctly.js`** -> AI Confidence: **99.06%**
3649. **`tests/baselines/reference/tsserver/configuredProjects/open-file-become-a-part-of-configured-project-if-it-is-referenced-from-root-file.js`** -> AI Confidence: **99.06%**
3650. **`tests/baselines/reference/tsserver/configuredProjects/should-be-able-to-handle-@types-if-input-file-list-is-empty.js`** -> AI Confidence: **99.06%**
3651. **`tests/baselines/reference/tsserver/configuredProjects/should-be-tolerated-without-crashing-the-server-when-reading-tsconfig-file-fails.js`** -> AI Confidence: **99.06%**
3652. **`tests/baselines/reference/tsserver/configuredProjects/should-ignore-non-existing-files-specified-in-the-config-file.js`** -> AI Confidence: **99.06%**
3653. **`tests/baselines/reference/tsserver/configuredProjects/should-stop-watching-the-extended-configs-of-closed-projects.js`** -> AI Confidence: **99.06%**
3654. **`tests/baselines/reference/tsserver/configuredProjects/syntactic-features-work-even-if-language-service-is-disabled.js`** -> AI Confidence: **99.06%**
3655. **`tests/baselines/reference/tsserver/configuredProjects/when-default-configured-project-does-not-contain-the-file.js`** -> AI Confidence: **99.06%**
3656. **`tests/baselines/reference/tsserver/declarationFileMaps/does-not-jump-to-source-if-inlined-sources.js`** -> AI Confidence: **99.06%**
3657. **`tests/baselines/reference/tsserver/declarationFileMaps/findAllReferences-starting-at-definition.js`** -> AI Confidence: **99.06%**
3658. **`tests/baselines/reference/tsserver/declarationFileMaps/findAllReferences-target-does-not-exist.js`** -> AI Confidence: **99.06%**
3659. **`tests/baselines/reference/tsserver/declarationFileMaps/getDefinitionAndBoundSpan.js`** -> AI Confidence: **99.06%**
3660. **`tests/baselines/reference/tsserver/declarationFileMaps/getEditsForFileRename.js`** -> AI Confidence: **99.06%**
3661. **`tests/baselines/reference/tsserver/declarationFileMaps/goToDefinition-target-does-not-exist.js`** -> AI Confidence: **99.06%**
3662. **`tests/baselines/reference/tsserver/declarationFileMaps/goToDefinition.js`** -> AI Confidence: **99.06%**
3663. **`tests/baselines/reference/tsserver/declarationFileMaps/goToImplementation.js`** -> AI Confidence: **99.06%**
3664. **`tests/baselines/reference/tsserver/declarationFileMaps/goToType.js`** -> AI Confidence: **99.06%**
3665. **`tests/baselines/reference/tsserver/declarationFileMaps/navigateTo.js`** -> AI Confidence: **99.06%**
3666. **`tests/baselines/reference/tsserver/declarationFileMaps/renameLocations-starting-at-definition.js`** -> AI Confidence: **99.06%**
3667. **`tests/baselines/reference/tsserver/declarationFileMaps/renameLocations-target-does-not-exist.js`** -> AI Confidence: **99.06%**
3668. **`tests/baselines/reference/tsserver/documentRegistry/Caches-the-source-file-if-script-info-is-orphan.js`** -> AI Confidence: **99.06%**
3669. **`tests/baselines/reference/tsserver/events/largeFileReferenced/when-large-js-file-is-included-by-module-resolution.js`** -> AI Confidence: **99.06%**
3670. **`tests/baselines/reference/tsserver/events/projectLanguageServiceState/large-file-size-is-determined-correctly.js`** -> AI Confidence: **99.06%**
3671. **`tests/baselines/reference/tsserver/events/projectUpdatedInBackground/when-event-handler-is-set-in-the-session-and-should-always-return-the-file-itself-if---isolatedModules-is-specified.js`** -> AI Confidence: **99.06%**
3672. **`tests/baselines/reference/tsserver/events/projectUpdatedInBackground/when-event-handler-is-set-in-the-session-and-should-always-return-the-file-itself-if---out-or---outFile-is-specified.js`** -> AI Confidence: **99.06%**
3673. **`tests/baselines/reference/tsserver/events/projectUpdatedInBackground/when-event-handler-is-set-in-the-session-and-should-be-up-to-date-with-deleted-files.js`** -> AI Confidence: **99.06%**
3674. **`tests/baselines/reference/tsserver/events/projectUpdatedInBackground/when-event-handler-is-set-in-the-session-and-should-be-up-to-date-with-newly-created-files.js`** -> AI Confidence: **99.06%**
3675. **`tests/baselines/reference/tsserver/events/projectUpdatedInBackground/when-event-handler-is-set-in-the-session-and-should-detect-non-existing-code-file.js`** -> AI Confidence: **99.06%**
3676. **`tests/baselines/reference/tsserver/events/projectUpdatedInBackground/when-event-handler-is-set-in-the-session-and-should-return-all-files-if-a-global-file-changed-shape.js`** -> AI Confidence: **99.06%**
3677. **`tests/baselines/reference/tsserver/events/projectUpdatedInBackground/when-event-handler-is-set-in-the-session-and-should-work-fine-for-files-with-circular-references.js`** -> AI Confidence: **99.06%**
3678. **`tests/baselines/reference/tsserver/events/projectUpdatedInBackground/when-event-handler-is-set-in-the-session-and-when-adding-new-file.js`** -> AI Confidence: **99.06%**
3679. **`tests/baselines/reference/tsserver/events/projectUpdatedInBackground/with-noGetErrOnBackgroundUpdate-and-should-always-return-the-file-itself-if---isolatedModules-is-specified.js`** -> AI Confidence: **99.06%**
3680. **`tests/baselines/reference/tsserver/events/projectUpdatedInBackground/with-noGetErrOnBackgroundUpdate-and-should-always-return-the-file-itself-if---out-or---outFile-is-specified.js`** -> AI Confidence: **99.06%**
3681. **`tests/baselines/reference/tsserver/events/projectUpdatedInBackground/with-noGetErrOnBackgroundUpdate-and-should-be-up-to-date-with-deleted-files.js`** -> AI Confidence: **99.06%**
3682. **`tests/baselines/reference/tsserver/events/projectUpdatedInBackground/with-noGetErrOnBackgroundUpdate-and-should-be-up-to-date-with-newly-created-files.js`** -> AI Confidence: **99.06%**
3683. **`tests/baselines/reference/tsserver/events/projectUpdatedInBackground/with-noGetErrOnBackgroundUpdate-and-should-detect-non-existing-code-file.js`** -> AI Confidence: **99.06%**
3684. **`tests/baselines/reference/tsserver/events/projectUpdatedInBackground/with-noGetErrOnBackgroundUpdate-and-should-return-all-files-if-a-global-file-changed-shape.js`** -> AI Confidence: **99.06%**
3685. **`tests/baselines/reference/tsserver/events/projectUpdatedInBackground/with-noGetErrOnBackgroundUpdate-and-should-work-fine-for-files-with-circular-references.js`** -> AI Confidence: **99.06%**
3686. **`tests/baselines/reference/tsserver/events/projectUpdatedInBackground/with-noGetErrOnBackgroundUpdate-and-when-adding-new-file.js`** -> AI Confidence: **99.06%**
3687. **`tests/baselines/reference/tsserver/events/projectUpdatedInBackground/without-noGetErrOnBackgroundUpdate-and-should-always-return-the-file-itself-if---isolatedModules-is-specified.js`** -> AI Confidence: **99.06%**
3688. **`tests/baselines/reference/tsserver/events/projectUpdatedInBackground/without-noGetErrOnBackgroundUpdate-and-should-always-return-the-file-itself-if---out-or---outFile-is-specified.js`** -> AI Confidence: **99.06%**
3689. **`tests/baselines/reference/tsserver/events/projectUpdatedInBackground/without-noGetErrOnBackgroundUpdate-and-should-be-up-to-date-with-deleted-files.js`** -> AI Confidence: **99.06%**
3690. **`tests/baselines/reference/tsserver/events/projectUpdatedInBackground/without-noGetErrOnBackgroundUpdate-and-should-be-up-to-date-with-newly-created-files.js`** -> AI Confidence: **99.06%**
3691. **`tests/baselines/reference/tsserver/events/projectUpdatedInBackground/without-noGetErrOnBackgroundUpdate-and-should-detect-non-existing-code-file.js`** -> AI Confidence: **99.06%**
3692. **`tests/baselines/reference/tsserver/events/projectUpdatedInBackground/without-noGetErrOnBackgroundUpdate-and-should-detect-removed-code-file.js`** -> AI Confidence: **99.06%**
3693. **`tests/baselines/reference/tsserver/events/projectUpdatedInBackground/without-noGetErrOnBackgroundUpdate-and-should-return-all-files-if-a-global-file-changed-shape.js`** -> AI Confidence: **99.06%**
3694. **`tests/baselines/reference/tsserver/events/projectUpdatedInBackground/without-noGetErrOnBackgroundUpdate-and-should-work-fine-for-files-with-circular-references.js`** -> AI Confidence: **99.06%**
3695. **`tests/baselines/reference/tsserver/events/projectUpdatedInBackground/without-noGetErrOnBackgroundUpdate-and-when---outFile-is-set.js`** -> AI Confidence: **99.06%**
3696. **`tests/baselines/reference/tsserver/events/projectUpdatedInBackground/without-noGetErrOnBackgroundUpdate-and-when-adding-new-file.js`** -> AI Confidence: **99.06%**
3697. **`tests/baselines/reference/tsserver/events/projectUpdatedInBackground/without-noGetErrOnBackgroundUpdate-and-when-both-options-are-not-set.js`** -> AI Confidence: **99.06%**
3698. **`tests/baselines/reference/tsserver/exportMapCache/caches-auto-imports-in-the-same-file.js`** -> AI Confidence: **99.06%**
3699. **`tests/baselines/reference/tsserver/exportMapCache/does-not-invalidate-the-cache-when-package.json-is-changed-inconsequentially.js`** -> AI Confidence: **99.06%**
3700. **`tests/baselines/reference/tsserver/exportMapCache/does-not-invalidate-the-cache-when-referenced-project-changes-inconsequentially-referencedInProject.js`** -> AI Confidence: **99.06%**
3701. **`tests/baselines/reference/tsserver/exportMapCache/does-not-store-transient-symbols-through-program-updates.js`** -> AI Confidence: **99.06%**
3702. **`tests/baselines/reference/tsserver/exportMapCache/invalidates-the-cache-when-files-are-deleted.js`** -> AI Confidence: **99.06%**
3703. **`tests/baselines/reference/tsserver/exportMapCache/invalidates-the-cache-when-new-files-are-added.js`** -> AI Confidence: **99.06%**
3704. **`tests/baselines/reference/tsserver/exportMapCache/invalidates-the-cache-when-package.json-change-results-in-AutoImportProvider-change.js`** -> AI Confidence: **99.06%**
3705. **`tests/baselines/reference/tsserver/exportMapCache/invalidates-the-cache-when-referenced-project-changes-signatures-referencedInProject.js`** -> AI Confidence: **99.06%**
3706. **`tests/baselines/reference/tsserver/exportMapCache/invalidates-the-cache-when-referenced-project-changes-signatures.js`** -> AI Confidence: **99.06%**
3707. **`tests/baselines/reference/tsserver/extends/configDir-template.js`** -> AI Confidence: **99.06%**
3708. **`tests/baselines/reference/tsserver/extends/resolves-the-symlink-path.js`** -> AI Confidence: **99.06%**
3709. **`tests/baselines/reference/tsserver/externalProjects/can-correctly-update-external-project-when-set-of-root-files-has-changed.js`** -> AI Confidence: **99.06%**
3710. **`tests/baselines/reference/tsserver/externalProjects/correctly-handles-changes-in-lib-section-of-config-file.js`** -> AI Confidence: **99.06%**
3711. **`tests/baselines/reference/tsserver/externalProjects/does-not-crash-if-external-file-does-not-exist.js`** -> AI Confidence: **99.06%**
3712. **`tests/baselines/reference/tsserver/externalProjects/external-project-for-dynamic-file.js`** -> AI Confidence: **99.06%**
3713. **`tests/baselines/reference/tsserver/externalProjects/external-project-with-included-config-file-opened-after-configured-project-and-then-closed.js`** -> AI Confidence: **99.06%**
3714. **`tests/baselines/reference/tsserver/externalProjects/external-project-with-included-config-file-opened-after-configured-project.js`** -> AI Confidence: **99.06%**
3715. **`tests/baselines/reference/tsserver/externalProjects/handles-loads-existing-configured-projects-of-external-projects-when-lazyConfiguredProjectsFromExternalProject-is-disabled.js`** -> AI Confidence: **99.06%**
3716. **`tests/baselines/reference/tsserver/externalProjects/load-global-plugins.js`** -> AI Confidence: **99.06%**
3717. **`tests/baselines/reference/tsserver/externalProjects/remove-not-listed-external-projects.js`** -> AI Confidence: **99.06%**
3718. **`tests/baselines/reference/tsserver/externalProjects/should-handle-non-existing-directories-in-config-file.js`** -> AI Confidence: **99.06%**
3719. **`tests/baselines/reference/tsserver/externalProjects/should-not-close-external-project-with-no-open-files.js`** -> AI Confidence: **99.06%**
3720. **`tests/baselines/reference/tsserver/findAllReferences/does-not-try-to-open-a-file-in-a-project-that-was-updated-and-no-longer-has-the-file.js`** -> AI Confidence: **99.06%**
3721. **`tests/baselines/reference/tsserver/forceConsistentCasingInFileNames/when-both-directory-symlink-target-and-import-match-disk-with-target-and-link-open.js`** -> AI Confidence: **99.06%**
3722. **`tests/baselines/reference/tsserver/forceConsistentCasingInFileNames/when-both-file-symlink-target-and-import-match-disk-with-link-open.js`** -> AI Confidence: **99.06%**
3723. **`tests/baselines/reference/tsserver/forceConsistentCasingInFileNames/when-both-file-symlink-target-and-import-match-disk-with-target-and-link-open.js`** -> AI Confidence: **99.06%**
3724. **`tests/baselines/reference/tsserver/forceConsistentCasingInFileNames/when-both-file-symlink-target-and-import-match-disk-with-target-open.js`** -> AI Confidence: **99.06%**
3725. **`tests/baselines/reference/tsserver/forceConsistentCasingInFileNames/when-directory-symlink-target-matches-disk-but-import-does-not-with-target-and-link-open.js`** -> AI Confidence: **99.06%**
3726. **`tests/baselines/reference/tsserver/forceConsistentCasingInFileNames/when-file-symlink-target-matches-disk-but-import-does-not-with-link-open.js`** -> AI Confidence: **99.06%**
3727. **`tests/baselines/reference/tsserver/forceConsistentCasingInFileNames/when-file-symlink-target-matches-disk-but-import-does-not-with-target-and-link-open.js`** -> AI Confidence: **99.06%**
3728. **`tests/baselines/reference/tsserver/forceConsistentCasingInFileNames/when-file-symlink-target-matches-disk-but-import-does-not-with-target-open.js`** -> AI Confidence: **99.06%**
3729. **`tests/baselines/reference/tsserver/forceConsistentCasingInFileNames/when-import,-directory-symlink-target,-and-disk-are-all-different-with-link-open.js`** -> AI Confidence: **99.06%**
3730. **`tests/baselines/reference/tsserver/forceConsistentCasingInFileNames/when-import,-directory-symlink-target,-and-disk-are-all-different-with-target-and-link-open.js`** -> AI Confidence: **99.06%**
3731. **`tests/baselines/reference/tsserver/forceConsistentCasingInFileNames/when-import,-directory-symlink-target,-and-disk-are-all-different-with-target-open.js`** -> AI Confidence: **99.06%**
3732. **`tests/baselines/reference/tsserver/forceConsistentCasingInFileNames/when-import,-file-symlink-target,-and-disk-are-all-different-with-target-and-link-open.js`** -> AI Confidence: **99.06%**
3733. **`tests/baselines/reference/tsserver/forceConsistentCasingInFileNames/when-import-and-directory-symlink-target-agree-but-do-not-match-disk-with-link-open.js`** -> AI Confidence: **99.06%**
3734. **`tests/baselines/reference/tsserver/forceConsistentCasingInFileNames/when-import-and-directory-symlink-target-agree-but-do-not-match-disk-with-target-and-link-open.js`** -> AI Confidence: **99.06%**
3735. **`tests/baselines/reference/tsserver/forceConsistentCasingInFileNames/when-import-and-directory-symlink-target-agree-but-do-not-match-disk-with-target-open.js`** -> AI Confidence: **99.06%**
3736. **`tests/baselines/reference/tsserver/forceConsistentCasingInFileNames/when-import-and-file-symlink-target-agree-but-do-not-match-disk-with-target-and-link-open.js`** -> AI Confidence: **99.06%**
3737. **`tests/baselines/reference/tsserver/forceConsistentCasingInFileNames/when-import-matches-disk-but-directory-symlink-target-does-not-with-link-open.js`** -> AI Confidence: **99.06%**
3738. **`tests/baselines/reference/tsserver/forceConsistentCasingInFileNames/when-import-matches-disk-but-directory-symlink-target-does-not-with-target-and-link-open.js`** -> AI Confidence: **99.06%**
3739. **`tests/baselines/reference/tsserver/forceConsistentCasingInFileNames/when-import-matches-disk-but-directory-symlink-target-does-not-with-target-open.js`** -> AI Confidence: **99.06%**
3740. **`tests/baselines/reference/tsserver/forceConsistentCasingInFileNames/when-import-matches-disk-but-file-symlink-target-does-not-with-target-and-link-open.js`** -> AI Confidence: **99.06%**
3741. **`tests/baselines/reference/tsserver/fourslashServer/autoImportCrossProject_baseUrl_toDist.js`** -> AI Confidence: **99.06%**
3742. **`tests/baselines/reference/tsserver/fourslashServer/autoImportCrossProject_paths_sharedOutDir.js`** -> AI Confidence: **99.06%**
3743. **`tests/baselines/reference/tsserver/fourslashServer/autoImportCrossProject_paths_stripSrc.js`** -> AI Confidence: **99.06%**
3744. **`tests/baselines/reference/tsserver/fourslashServer/autoImportCrossProject_paths_toDist.js`** -> AI Confidence: **99.06%**
3745. **`tests/baselines/reference/tsserver/fourslashServer/autoImportCrossProject_paths_toSrc.js`** -> AI Confidence: **99.06%**
3746. **`tests/baselines/reference/tsserver/fourslashServer/autoImportNodeModuleSymlinkRenamed.js`** -> AI Confidence: **99.06%**
3747. **`tests/baselines/reference/tsserver/fourslashServer/autoImportProvider2.js`** -> AI Confidence: **99.06%**
3748. **`tests/baselines/reference/tsserver/fourslashServer/autoImportProvider4.js`** -> AI Confidence: **99.06%**
3749. **`tests/baselines/reference/tsserver/fourslashServer/autoImportProvider5.js`** -> AI Confidence: **99.06%**
3750. **`tests/baselines/reference/tsserver/fourslashServer/autoImportProvider9.js`** -> AI Confidence: **99.06%**
3751. **`tests/baselines/reference/tsserver/fourslashServer/autoImportProvider_importsMap2.js`** -> AI Confidence: **99.06%**
3752. **`tests/baselines/reference/tsserver/fourslashServer/autoImportProvider_importsMap3.js`** -> AI Confidence: **99.06%**
3753. **`tests/baselines/reference/tsserver/fourslashServer/autoImportProvider_importsMap4.js`** -> AI Confidence: **99.06%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `src/testRunner/unittests/paths.ts` -> **100.0%** Exposure
- `src/compiler/watch.ts` -> **0.2793%** Exposure
- `src/compiler/executeCommandLine.ts` -> **0.0204%** Exposure
- `src/testRunner/unittests/services/languageService.ts` -> **0.0128%** Exposure
- `src/harness/harnessUtils.ts` -> **0.0008%** Exposure
### Exploit Generation Surface
- `Herebyfile.mjs` -> **100.0%** Exposure
- `scripts/dtsBundler.mjs` -> **100.0%** Exposure
- `scripts/failed-tests.cjs` -> **100.0%** Exposure
- `scripts/generateLocalizedDiagnosticMessages.mjs` -> **100.0%** Exposure
- `tests/baselines/reference/APISample_jsdoc.js` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `.gulp.js` -> **100.0%** Exposure
- `scripts/addPackageJsonGitHead.mjs` -> **100.0%** Exposure
- `scripts/failed-tests.cjs` -> **100.0%** Exposure
- `scripts/generateLocalizedDiagnosticMessages.mjs` -> **100.0%** Exposure
- `tests/baselines/reference/asyncAwaitNestedClasses_es5(target=es5).js` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `Herebyfile.mjs` -> **100.0%** Exposure
- `scripts/dtsBundler.mjs` -> **100.0%** Exposure
- `scripts/eslint/rules/jsdoc-format.cjs` -> **100.0%** Exposure
- `scripts/eslint/rules/no-array-mutating-method-expressions.cjs` -> **100.0%** Exposure
- `scripts/eslint/rules/no-direct-import.cjs` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `5287` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/server/utilities.ts` (TYPESCRIPT) -> Cumulative Risk: **931.04**
- **Archetype:** `file_cluster_4` (Distance: 13.983 IQR)
- **Magnitude:** 14.67 | **LOC:** 85 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `schedule` (Impact: 16.6), `run` (Impact: 14.0), `scheduleCollect` (Impact: 10.7)

### 2. `src/testRunner/unittests/helpers/virtualFileSystemWithWatch.ts` (TYPESCRIPT) -> Cumulative Risk: **921.17**
- **Archetype:** `file_cluster_17` (Distance: 14.455 IQR)
- **Magnitude:** 292.75 | **LOC:** 1405 | **CtrlFlow:** 57.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `diffFsEntry` (Impact: 248.9), `readDirectory` (Impact: 86.8), `reloadFS` (Impact: 84.7)

### 3. `src/harness/vfsUtil.ts` (TYPESCRIPT) -> Cumulative Risk: **888.49**
- **Archetype:** `file_cluster_8` (Distance: 13.384 IQR)
- **Magnitude:** 324.13 | **LOC:** 1739 | **CtrlFlow:** 67.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `_scan` (Impact: 390.5), `diffWorker` (Impact: 211.6), `fileDiff` (Impact: 207.6)

### 4. `src/harness/fakesHosts.ts` (TYPESCRIPT) -> Cumulative Risk: **871.48**
- **Archetype:** `file_cluster_13` (Distance: 13.982 IQR)
- **Magnitude:** 95.41 | **LOC:** 425 | **CtrlFlow:** 50.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `getSourceFile` (Impact: 130.7), `getAccessibleFileSystemEntries` (Impact: 64.0), `readDirectory` (Impact: 36.9)

### 5. `src/server/scriptVersionCache.ts` (TYPESCRIPT) -> Cumulative Risk: **869.57**
- **Archetype:** `file_cluster_13` (Distance: 13.835 IQR)
- **Magnitude:** 175.76 | **LOC:** 862 | **CtrlFlow:** 61.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `leaf` (Impact: 780.5), `insertAt` (Impact: 93.6), `getTextChangesBetweenVersions` (Impact: 43.4)

### 6. `src/harness/harnessLanguageService.ts` (TYPESCRIPT) -> Cumulative Risk: **867.88**
- **Archetype:** `file_cluster_13` (Distance: 12.596 IQR)
- **Magnitude:** 93.33 | **LOC:** 831 | **CtrlFlow:** 24.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.9952%)
- **Heaviest Functions:** `createLibCachingDocumentRegistry` (Impact: 600.9), `makeDefaultProxy` (Impact: 8.6), `getTextChangeRangeBetweenVersions` (Impact: 7.5)

### 7. `src/harness/evaluatorImpl.ts` (TYPESCRIPT) -> Cumulative Risk: **865.22**
- **Archetype:** `file_cluster_13` (Distance: 12.881 IQR)
- **Magnitude:** 195.85 | **LOC:** 760 | **CtrlFlow:** 38.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.9994%)
- **Heaviest Functions:** `register` (Impact: 727.0), `linkModule` (Impact: 381.6), `evaluateModule` (Impact: 178.5)

### 8. `src/server/typingInstallerAdapter.ts` (TYPESCRIPT) -> Cumulative Risk: **862.27**
- **Archetype:** `file_cluster_4` (Distance: 13.327 IQR)
- **Magnitude:** 77.03 | **LOC:** 256 | **CtrlFlow:** 76.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `handleMessage` (Impact: 481.3), `enqueueInstallTypingsRequest` (Impact: 30.9), `scheduleRequest` (Impact: 21.6)

### 9. `src/harness/util.ts` (TYPESCRIPT) -> Cumulative Risk: **858.01**
- **Archetype:** `file_cluster_4` (Distance: 12.594 IQR)
- **Magnitude:** 23.86 | **LOC:** 131 | **CtrlFlow:** 51.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Concurrency (99.9997%)
- **Heaviest Functions:** `guessIndentation` (Impact: 54.7), `getByteOrderMarkLength` (Impact: 39.5), `dedent` (Impact: 36.5)

### 10. `src/testRunner/unittests/evaluation/awaitUsingDeclarations.ts` (TYPESCRIPT) -> Cumulative Risk: **849.3**
- **Archetype:** `file_cluster_4` (Distance: 12.522 IQR)
- **Magnitude:** 296.04 | **LOC:** 2014 | **CtrlFlow:** 25.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `describe` (Impact: 934.5), `it` (Impact: 28.2), `FakeSuppressedError` (Impact: 1.9)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `tests/baselines/reference/manyConstExports(target=es2015).js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.323 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.381 IQR)
- **Top Global Matches:** file_cluster_8: 6.323, file_cluster_7: 7.366, file_cluster_1: 7.721
- **Magnitude:** 15217.04 | **LOC:** 10109 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 5000`
* *Risk/State:* `safety_bypasses: 100`
* *Architecture:* `api: 15000`
* *Defense:* `immutability_locks: 5000`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/baselines/reference/manyConstExports(target=es5).js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.323 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.381 IQR)
- **Top Global Matches:** file_cluster_8: 6.323, file_cluster_7: 7.366, file_cluster_1: 7.721
- **Magnitude:** 15217.04 | **LOC:** 10109 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 5000`
* *Risk/State:* `safety_bypasses: 100`
* *Architecture:* `api: 15000`
* *Defense:* `immutability_locks: 5000`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/baselines/reference/parserRealSource11.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.488 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.584 IQR)
- **Top Global Matches:** file_cluster_8: 13.488, file_cluster_17: 13.717, file_cluster_13: 13.741
- **Magnitude:** 4817.88 | **LOC:** 4518 | **CtrlFlow:** 39.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 41
- **Risk Profile:** Cognitive Load (45.0693%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `typeCheck` (Impact: 233.4 | O(2^N) | DB: 41)
  * `emit` (Impact: 177.7 | O(N^6) | DB: 1)
  * `isFiltered` (Impact: 106.4 | O(N^6) | DB: 17)
  * `emitRequired` (Impact: 95.6 | O(N^6) | DB: 7)
    * *Intent:* // 'actualText' is the text that the user has entered for the identifier. the text might // include ...
  * `addToControlFlow` (Impact: 91.3 | O(2^N) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 522`, `structural_boundaries: 789`, `args: 249`, `func_start: 328`, `class_start: 84`
* *Risk/State:* `safety_bypasses: 106`, `high_risk_execution: 2`, `state_mutation: 2318`, `dead_code: 8`, `planned_debt: 14`, `duplicate_logic: 208`
* *Architecture:* `api: 43`
* *Defense:* `safety: 22`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/baselines/reference/emitter.forAwait(target=es5).js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_4` (Drift: 15.357 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 5.984 IQR)
- **Top Global Matches:** file_cluster_4: 15.357, file_cluster_11: 15.616, file_cluster_15: 15.844
- **Magnitude:** 4141.26 | **LOC:** 682 | **CtrlFlow:** 66.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (49.9979%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `step` (Impact: 541.9 | O(2^N) | DB: 8)
  * `step` (Impact: 541.9 | O(2^N) | DB: 8)
  * `step` (Impact: 541.9 | O(2^N) | DB: 8)
  * `step` (Impact: 240.1 | O(N^5) | DB: 5)
  * `step` (Impact: 240.1 | O(N^5) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 619`, `structural_boundaries: 311`, `args: 188`, `func_start: 89`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 450`, `duplicate_logic: 79`
* *Architecture:* `concurrency: 151`
* *Defense:* `safety: 130`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/baselines/reference/enumLiteralsSubtypeReduction.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.175 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 1.892 IQR)
- **Top Global Matches:** file_cluster_8: 9.175, file_cluster_7: 9.96, file_cluster_1: 10.136
- **Magnitude:** 4024.5 | **LOC:** 4117 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.9986%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `run` (Impact: 2107.4 | O(N^3))
  * `run` (Impact: 1831.9 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1027`, `structural_boundaries: 1025`, `args: 3`, `func_start: 2`
* *Risk/State:* `state_mutation: 3`, `duplicate_logic: 2`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/baselines/reference/resolvingClassDeclarationWhenInBaseTypeResolution.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.773 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.498 IQR)
- **Top Global Matches:** file_cluster_8: 14.773, file_cluster_15: 14.801, file_cluster_2: 14.848
- **Magnitude:** 3957.62 | **LOC:** 3191 | **CtrlFlow:** 1.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (26.0525%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `salomonseni` (Impact: 1.8 | O(N^1) | DB: 2)
  * `uchidai` (Impact: 1.8 | O(N^1) | DB: 2)
  * `raffrayana` (Impact: 1.8 | O(N^1) | DB: 2)
  * `Uranium` (Impact: 1.8 | O(N^1) | DB: 2)
  * `nayaur` (Impact: 1.8 | O(N^1) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 6057`, `args: 2123`, `func_start: 2058`, `class_start: 300`
* *Risk/State:* `state_mutation: 3344`
* *Architecture:* `api: 100`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/baselines/reference/superInStaticMembers1(target=es5).js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_11` (Drift: 15.199 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 5.183 IQR)
- **Top Global Matches:** file_cluster_11: 15.199, file_cluster_12: 15.221, file_cluster_15: 15.395
- **Magnitude:** 3635.6 | **LOC:** 2064 | **CtrlFlow:** 40.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (36.824%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `extendStatics` (Impact: 41.9 | O(2^N) | DB: 1)
  * `extendStatics` (Impact: 41.9 | O(2^N) | DB: 1)
  * `extendStatics` (Impact: 41.9 | O(2^N) | DB: 1)
  * `extendStatics` (Impact: 41.9 | O(2^N) | DB: 1)
  * `extendStatics` (Impact: 41.9 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 570`, `structural_boundaries: 843`, `args: 482`, `func_start: 267`, `class_start: 52`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1034`, `duplicate_logic: 170`
* *Architecture:* `api: 55`, `import: 16`
* *Defense:* `safety: 282`, `doc: 59`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` external
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/baselines/reference/emitter.asyncGenerators.classMethods.es5(target=es5).js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_4` (Drift: 16.235 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 6.112 IQR)
- **Top Global Matches:** file_cluster_4: 16.235, file_cluster_11: 16.39, file_cluster_15: 16.53
- **Magnitude:** 3421.58 | **LOC:** 667 | **CtrlFlow:** 67.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (43.3999%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `step` (Impact: 240.1 | O(N^5) | DB: 5)
  * `step` (Impact: 240.1 | O(N^5) | DB: 5)
  * `step` (Impact: 240.1 | O(N^5) | DB: 5)
  * `step` (Impact: 240.1 | O(N^5) | DB: 5)
  * `step` (Impact: 240.1 | O(N^5) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 667`, `structural_boundaries: 329`, `args: 259`, `func_start: 125`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 546`, `duplicate_logic: 102`
* *Architecture:* `concurrency: 127`
* *Defense:* `safety: 171`, `doc: 10`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/baselines/reference/tsserver/projectReferences/project-is-indirectly-referenced-by-solution.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.973 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 1.358 IQR)
- **Top Global Matches:** file_cluster_8: 8.973, file_cluster_7: 9.83, file_cluster_1: 10.012
- **Magnitude:** 3092.08 | **LOC:** 4508 | **CtrlFlow:** 60.1% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.571%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 55`, `args: 8`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 10`
* *Architecture:* `io: 30`, `api: 20`, `import: 27`
* *Defense:* `doc: 15`, `immutability_locks: 29`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` main, functions
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/baselines/reference/tsserver/completionsIncomplete/works-with-PackageJsonAutoImportProvider.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.187 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 2.742 IQR)
- **Top Global Matches:** file_cluster_8: 9.187, file_cluster_7: 10.025, file_cluster_1: 10.24
- **Magnitude:** 2781.29 | **LOC:** 10676 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.4595%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 878`, `args: 1`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 2`, `state_mutation: 6`
* *Architecture:* `io: 1`, `api: 855`, `concurrency: 4`, `import: 52`
* *Defense:* `safety: 10`, `immutability_locks: 812`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` file_8, file_10, file_7, file_21, file_38, file_47, file_16, file_39...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/baselines/reference/emitter.asyncGenerators.objectLiteralMethods.es5(target=es5).js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_4` (Drift: 16.105 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 6.327 IQR)
- **Top Global Matches:** file_cluster_4: 16.105, file_cluster_11: 16.296, file_cluster_15: 16.505
- **Magnitude:** 2654.4 | **LOC:** 494 | **CtrlFlow:** 68.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (49.9985%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `step` (Impact: 240.1 | O(N^5) | DB: 5)
  * `step` (Impact: 240.1 | O(N^5) | DB: 5)
  * `step` (Impact: 240.1 | O(N^5) | DB: 5)
  * `step` (Impact: 240.1 | O(N^5) | DB: 5)
  * `step` (Impact: 240.1 | O(N^5) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 525`, `structural_boundaries: 245`, `args: 185`, `func_start: 85`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 426`, `duplicate_logic: 78`
* *Architecture:* `concurrency: 100`
* *Defense:* `safety: 131`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/baselines/reference/emitter.asyncGenerators.functionExpressions.es5(target=es5).js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_4` (Drift: 16.293 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 6.443 IQR)
- **Top Global Matches:** file_cluster_4: 16.293, file_cluster_11: 16.447, file_cluster_15: 16.648
- **Magnitude:** 2625.74 | **LOC:** 466 | **CtrlFlow:** 68.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (49.9984%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `step` (Impact: 240.1 | O(N^5) | DB: 5)
  * `step` (Impact: 240.1 | O(N^5) | DB: 5)
  * `step` (Impact: 240.1 | O(N^5) | DB: 5)
  * `step` (Impact: 240.1 | O(N^5) | DB: 5)
  * `step` (Impact: 240.1 | O(N^5) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 525`, `structural_boundaries: 245`, `args: 185`, `func_start: 85`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 426`, `duplicate_logic: 85`
* *Architecture:* `concurrency: 85`
* *Defense:* `safety: 131`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/baselines/reference/emitter.asyncGenerators.functionDeclarations.es5(target=es5).js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_4` (Drift: 16.222 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 6.301 IQR)
- **Top Global Matches:** file_cluster_4: 16.222, file_cluster_11: 16.389, file_cluster_15: 16.605
- **Magnitude:** 2604.74 | **LOC:** 466 | **CtrlFlow:** 68.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (49.9984%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `step` (Impact: 240.1 | O(N^5) | DB: 5)
  * `step` (Impact: 240.1 | O(N^5) | DB: 5)
  * `step` (Impact: 240.1 | O(N^5) | DB: 5)
  * `step` (Impact: 240.1 | O(N^5) | DB: 5)
  * `step` (Impact: 240.1 | O(N^5) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 525`, `structural_boundaries: 238`, `args: 185`, `func_start: 92`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 405`, `duplicate_logic: 85`
* *Architecture:* `concurrency: 85`
* *Defense:* `safety: 131`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/baselines/reference/tsserver/completionsIncomplete/works.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.839 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 2.845 IQR)
- **Top Global Matches:** file_cluster_8: 8.839, file_cluster_7: 9.715, file_cluster_1: 9.928
- **Magnitude:** 2475.4 | **LOC:** 22661 | **CtrlFlow:** 7.8% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.4228%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 172`, `structural_boundaries: 2034`
* *Risk/State:* `safety_bypasses: 11`, `high_risk_execution: 3`, `state_mutation: 9`
* *Architecture:* `io: 1`, `api: 2003`, `concurrency: 6`
* *Defense:* `safety: 15`, `immutability_locks: 2014`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/baselines/reference/callChain.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.382 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.243 IQR)
- **Top Global Matches:** file_cluster_8: 14.382, file_cluster_12: 14.635, file_cluster_11: 14.65
- **Magnitude:** 2440.44 | **LOC:** 78 | **CtrlFlow:** 91.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (48.1337%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 8`, `args: 7`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 57`, `state_mutation: 3`
* *Architecture:* None
* *Defense:* `safety: 84`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/baselines/reference/bluebirdStaticThis.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.451 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.286 IQR)
- **Top Global Matches:** file_cluster_4: 14.451, file_cluster_17: 15.13, file_cluster_2: 15.278
- **Magnitude:** 2288.6 | **LOC:** 154 | **CtrlFlow:** 31.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (50.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 61`, `args: 45`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 12`
* *Architecture:* `api: 4`, `concurrency: 248`
* *Defense:* `safety: 82`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/baselines/reference/usingDeclarations.1(target=es5).js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.305 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.694 IQR)
- **Top Global Matches:** file_cluster_4: 14.305, file_cluster_11: 14.518, file_cluster_8: 14.576
- **Magnitude:** 2205.26 | **LOC:** 875 | **CtrlFlow:** 60.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (46.8962%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `step` (Impact: 541.9 | O(2^N) | DB: 8)
  * `next` (Impact: 146.3 | O(2^N) | DB: 3)
  * `__disposeResources` (Impact: 140.9 | O(2^N) | DB: 6)
  * `ag` (Impact: 62.3 | O(N^6) | DB: 3)
  * `ag` (Impact: 53.6 | O(N^5) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 300`, `structural_boundaries: 199`, `args: 115`, `func_start: 89`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 43`, `state_mutation: 378`, `duplicate_logic: 35`
* *Architecture:* `api: 2`, `concurrency: 96`
* *Defense:* `safety: 134`, `doc: 3`, `immutability_locks: 3`, `cleanup: 82`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/baselines/reference/parserRealSource7.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.85 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.412 IQR)
- **Top Global Matches:** file_cluster_8: 11.85, file_cluster_17: 12.081, file_cluster_2: 12.17
- **Magnitude:** 2027.44 | **LOC:** 1522 | **CtrlFlow:** 63.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 28
- **Risk Profile:** Cognitive Load (37.2732%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `preCollectModuleTypes` (Impact: 331.8 | O(N^6) | DB: 28)
  * `preCollectModuleTypes` (Impact: 283.6 | O(N^5) | DB: 28)
  * `findSymbolFromAlias` (Impact: 208.7 | O(2^N) | DB: 8)
  * `findSymbolFromAlias` (Impact: 208.2 | O(2^N) | DB: 8)
  * `preCollectInterfaceTypes` (Impact: 136.8 | O(N^6) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 299`, `structural_boundaries: 170`, `args: 29`, `func_start: 44`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 84`, `state_mutation: 304`, `dead_code: 4`, `duplicate_logic: 26`
* *Architecture:* `api: 10`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/baselines/reference/assignmentCompatWithCallSignaturesWithRestParameters.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.459 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.035 IQR)
- **Top Global Matches:** file_cluster_8: 11.459, file_cluster_7: 12.18, file_cluster_15: 12.213
- **Magnitude:** 1989.86 | **LOC:** 85 | **CtrlFlow:** 24.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (30.3727%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 72`, `args: 64`, `func_start: 60`
* *Risk/State:* `state_mutation: 18`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/baselines/reference/tsserver/completionsIncomplete/ambient-module-specifier-resolutions-do-not-count-against-the-resolution-limit.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.521 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 3.216 IQR)
- **Top Global Matches:** file_cluster_8: 8.521, file_cluster_7: 9.426, file_cluster_1: 9.644
- **Magnitude:** 1951.68 | **LOC:** 16959 | **CtrlFlow:** 6.9% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.3853%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 119`, `structural_boundaries: 1612`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 1`, `state_mutation: 3`
* *Architecture:* `io: 1`, `api: 1601`, `concurrency: 2`
* *Defense:* `safety: 5`, `immutability_locks: 2406`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/baselines/reference/parserRealSource12.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.024 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 3.206 IQR)
- **Top Global Matches:** file_cluster_8: 12.024, file_cluster_2: 12.445, file_cluster_13: 12.511
- **Magnitude:** 1865.56 | **LOC:** 1032 | **CtrlFlow:** 74.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 109
- **Risk Profile:** Cognitive Load (36.3539%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `walkBinaryExpressionChildren` (Impact: 54.9 | O(N^5))
  * `walkBinaryExpressionChildren` (Impact: 54.9 | O(N^5))
  * `walkFuncDeclChildren` (Impact: 50.7 | O(N^4))
  * `walkFuncDeclChildren` (Impact: 50.7 | O(N^4))
  * `walkListChildren` (Impact: 49.9 | O(N^6) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 219`, `structural_boundaries: 75`, `args: 81`, `func_start: 88`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 37`, `state_mutation: 357`, `planned_debt: 2`, `duplicate_logic: 76`
* *Architecture:* `api: 39`
* *Defense:* `safety: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/baselines/reference/parserharness.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.561 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.497 IQR)
- **Top Global Matches:** file_cluster_8: 13.561, file_cluster_17: 13.667, file_cluster_11: 13.752
- **Magnitude:** 1797.2 | **LOC:** 3820 | **CtrlFlow:** 36.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 110
- **Risk Profile:** Cognitive Load (32.9497%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `on` (Impact: 548.3 | O(N^6) | DB: 110)
  * `runJSString` (Impact: 37.3 | O(N^5) | DB: 4)
  * `run` (Impact: 14.3 | O(2^N))
  * `extractCompilerSettings` (Impact: 10.6 | O(N^4) | DB: 3)
  * `describe` (Impact: 7.4 | O(N^3) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 309`, `structural_boundaries: 538`, `args: 226`, `func_start: 244`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 48`, `state_mutation: 1039`, `planned_debt: 4`, `fragile_debt: 15`
* *Architecture:* `io: 42`, `api: 54`, `concurrency: 12`, `import: 2`
* *Defense:* `safety: 74`, `doc: 62`, `test: 40`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` vm
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/baselines/reference/awaitUsingDeclarations.1(target=es5).js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.618 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.159 IQR)
- **Top Global Matches:** file_cluster_4: 13.618, file_cluster_8: 14.153, file_cluster_11: 14.16
- **Magnitude:** 1765.24 | **LOC:** 783 | **CtrlFlow:** 50.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (49.4332%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `step` (Impact: 541.9 | O(2^N) | DB: 8)
  * `next` (Impact: 146.3 | O(2^N) | DB: 3)
  * `ag` (Impact: 80.9 | O(N^6) | DB: 3)
  * `ag` (Impact: 80.9 | O(N^6) | DB: 3)
  * `af` (Impact: 68.6 | O(N^6) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 287`, `structural_boundaries: 284`, `args: 127`, `func_start: 32`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 83`, `state_mutation: 311`, `duplicate_logic: 13`
* *Architecture:* `api: 2`, `concurrency: 261`
* *Defense:* `safety: 96`, `doc: 1`, `immutability_locks: 3`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/baselines/reference/tsserver/projectReferences/project-is-directly-referenced-by-solution.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.851 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 1.323 IQR)
- **Top Global Matches:** file_cluster_8: 8.851, file_cluster_7: 9.702, file_cluster_1: 9.891
- **Magnitude:** 1747.86 | **LOC:** 3485 | **CtrlFlow:** 68.9% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.6189%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 73`, `structural_boundaries: 33`, `args: 2`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 10`
* *Architecture:* `io: 11`, `api: 14`, `import: 13`
* *Defense:* `doc: 15`, `immutability_locks: 21`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` main, functions
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/baselines/reference/controlFlowOptionalChain.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.054 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.828 IQR)
- **Top Global Matches:** file_cluster_8: 13.054, file_cluster_17: 13.576, file_cluster_0: 13.578
- **Magnitude:** 1725.22 | **LOC:** 1122 | **CtrlFlow:** 94.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (16.9622%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `f40` (Impact: 54.7 | O(N^3))
  * `f41` (Impact: 54.7 | O(N^3))
  * `f10` (Impact: 50.4 | O(N^2))
  * `f11` (Impact: 50.4 | O(N^2))
  * `f12` (Impact: 50.4 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 633`, `structural_boundaries: 35`, `args: 50`, `func_start: 66`
* *Risk/State:* `safety_bypasses: 295`, `state_mutation: 43`, `duplicate_logic: 51`
* *Architecture:* None
* *Defense:* `safety: 483`, `test: 7`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### 🚨 Severe Anti-Patterns (Language Convention Violations)
- `tests/baselines/reference/extractConstant/extractConstant_PropertyName_PrivateIdentifierKeyword.ts` (TYPESCRIPT) | **Drift Ratio: 1.9x**
  * **Global Archetype:** `file_cluster_8` (Drift: 3.45 IQR)
  * **Local Reality:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 6.556 IQR)
- `tests/cases/conformance/salsa/privateIdentifierExpando.ts` (TYPESCRIPT) | **Drift Ratio: 1.76x**
  * **Global Archetype:** `file_cluster_8` (Drift: 3.721 IQR)
  * **Local Reality:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 6.562 IQR)
- `tests/cases/conformance/es2021/intlDateTimeFormatRangeES2021.ts` (TYPESCRIPT) | **Drift Ratio: 1.73x**
  * **Global Archetype:** `file_cluster_8` (Drift: 5.067 IQR)
  * **Local Reality:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 8.772 IQR)
- `tests/cases/compiler/initializedDestructuringAssignmentTypes.ts` (TYPESCRIPT) | **Drift Ratio: 1.68x**
  * **Global Archetype:** `file_cluster_8` (Drift: 3.917 IQR)
  * **Local Reality:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 6.597 IQR)
- `tests/cases/conformance/es2025/regExpEscape.ts` (TYPESCRIPT) | **Drift Ratio: 1.67x**
  * **Global Archetype:** `file_cluster_8` (Drift: 4.581 IQR)
  * **Local Reality:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 7.651 IQR)

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `tests/baselines/reference/decoratedBlockScopedClass2(target=es2015).js` (JAVASCRIPT) | Magnitude: 28.32 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 22, branch: 18, state_mutation: 18, structural_boundaries: 15
- `tests/baselines/reference/decoratedDefaultExportsGetExportedAmd.js` (JAVASCRIPT) | Magnitude: 61.4 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 42, branch: 32, indent_spaces: 26, structural_boundaries: 20
- `tests/baselines/reference/usingDeclarationsWithESClassDecorators.7(module=commonjs,target=es2015).js` (JAVASCRIPT) | Magnitude: 24.94 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 15, state_mutation: 12, branch: 6
- `tests/baselines/reference/usingDeclarationsWithLegacyClassDecorators.10(module=esnext,target=esnext).js` (JAVASCRIPT) | Magnitude: 24.26 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 7, state_mutation: 6, api: 3, branch: 2
- `tests/baselines/reference/usingDeclarationsWithLegacyClassDecorators.3(module=esnext,target=esnext).js` (JAVASCRIPT) | Magnitude: 24.26 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 7, state_mutation: 6, api: 3, branch: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `tests/baselines/reference/noEmitOnError.js` (JAVASCRIPT) | Magnitude: 16.12 | Delta: **0.036 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: events: 4, structural_boundaries: 3, state_mutation: 3
- `tests/baselines/reference/isolatedModulesNoEmitOnError.js` (JAVASCRIPT) | Magnitude: 13.56 | Delta: **0.071 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 2, api: 2, events: 2, immutability_locks: 2
- `tests/cases/conformance/salsa/typeFromPrototypeAssignment4.ts` (TYPESCRIPT) | Magnitude: 0.58 | Delta: **0.099 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: reflection_metaprogramming: 4, indent_spaces: 4, doc: 3, closures: 3
- `tests/baselines/reference/typeFromPrototypeAssignment4.js` (JAVASCRIPT) | Magnitude: 9.9 | Delta: **0.122 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 9, args: 6, func_start: 6, doc: 6
- `eslint.config.mjs` (JAVASCRIPT) | Magnitude: 27.7 | Delta: **0.148 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 219, doc: 43, events: 40, decorators: 28

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `tests/baselines/reference/emitBundleWithShebangAndPrologueDirectives1(target=es5).js` (JAVASCRIPT) | Magnitude: 73.06 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 21, state_mutation: 19, structural_boundaries: 14, branch: 12
- `tests/cases/compiler/contextualTypingWithFixedTypeParameters1.ts` (TYPESCRIPT) | Magnitude: 3.0 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 10, args: 6, closures: 3, state_mutation: 2
- `tests/baselines/reference/decoratorOnClassMethod19(target=es2015).js` (JAVASCRIPT) | Magnitude: 47.08 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 36, indent_spaces: 34, branch: 30, structural_boundaries: 23
- `tests/baselines/reference/templateLiteralsAndDecoratorMetadata.js` (JAVASCRIPT) | Magnitude: 26.76 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 22, branch: 18, indent_spaces: 12, structural_boundaries: 11
- `src/compiler/transformers/utilities.ts` (TYPESCRIPT) | Magnitude: 138.85 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 554, branch: 189, structural_boundaries: 128, state_mutation: 101

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `tests/baselines/reference/propertyOverridesAccessors4(target=es5).js` (JAVASCRIPT) | Magnitude: 76.54 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 28, state_mutation: 19, structural_boundaries: 13, branch: 12
- `tests/baselines/reference/protectedClassPropertyAccessibleWithinSubclass3(target=es5).js` (JAVASCRIPT) | Magnitude: 87.44 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 36, state_mutation: 23, structural_boundaries: 15, args: 14
- `tests/baselines/reference/superPropertyAccess_ES5(target=es5).js` (JAVASCRIPT) | Magnitude: 127.14 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 64, state_mutation: 40, structural_boundaries: 39, args: 23
- `tests/baselines/reference/computedPropertyNames43_ES5(target=es5).js` (JAVASCRIPT) | Magnitude: 84.74 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 40, state_mutation: 23, structural_boundaries: 22, args: 16
- `tests/baselines/reference/computedPropertyNames44_ES5(target=es5).js` (JAVASCRIPT) | Magnitude: 84.74 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 40, state_mutation: 23, structural_boundaries: 22, args: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `tests/baselines/reference/declarationEmitExpressionInExtends6.js` (JAVASCRIPT) | Magnitude: 69.96 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 36, structural_boundaries: 31, branch: 28, indent_spaces: 25
- `tests/baselines/reference/moduleResolutionWithSuffixes_one_jsonModule.js` (JAVASCRIPT) | Magnitude: 21.36 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 6, state_mutation: 6, structural_boundaries: 3, import: 2
- `tests/baselines/reference/privacyGloImportParseErrors.js` (JAVASCRIPT) | Magnitude: 251.48 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 285, structural_boundaries: 247, state_mutation: 134, api: 75
- `tests/baselines/reference/globalThisDeclarationEmit.js` (JAVASCRIPT) | Magnitude: 22.26 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: api: 7, structural_boundaries: 4, immutability_locks: 4, safety_bypasses: 2
- `tests/cases/compiler/jsxCallElaborationCheckNoCrash1.tsx` (TYPESCRIPT) | Magnitude: 0.32 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 7, indent_spaces: 3, args: 2, func_start: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `tests/baselines/reference/emitBundleWithShebang2(target=es5).js` (JAVASCRIPT) | Magnitude: 89.04 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 29, state_mutation: 25, structural_boundaries: 22, branch: 14
- `tests/cases/compiler/exportDefaultInterfaceAndValue.ts` (TYPESCRIPT) | Magnitude: 1.66 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 6, state_mutation: 3, branch: 2, api: 2
- `tests/cases/compiler/contextualTyping24.ts` (TYPESCRIPT) | Magnitude: 0.21 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: structural_boundaries: 3, func_start: 1, safety: 1, state_mutation: 1
- `tests/baselines/reference/declFileTypeAnnotationParenType(target=es2015).js` (JAVASCRIPT) | Magnitude: 44.02 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 36, structural_boundaries: 29, args: 14, closures: 14
- `tests/cases/compiler/optionalArgsWithDefaultValues.ts` (TYPESCRIPT) | Magnitude: 3.21 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 8, structural_boundaries: 6, state_mutation: 6, args: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `tests/cases/compiler/contextualTypesNegatedTypeLikeConstraintInGenericMappedType3.ts` (TYPESCRIPT) | Magnitude: 0.9 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 15, generics: 10, branch: 5
- `tests/cases/compiler/inheritanceOfGenericConstructorMethod1.ts` (TYPESCRIPT) | Magnitude: 1.71 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: generics: 8, structural_boundaries: 7, state_mutation: 4, ui_framework: 4
- `tests/cases/conformance/decorators/class/decoratorOnClass2.ts` (TYPESCRIPT) | Magnitude: 0.53 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 3, args: 1, func_start: 1, class_start: 1
- `tests/cases/conformance/jsx/tsxNamespacedTagName2.tsx` (TYPESCRIPT) | Magnitude: 1.36 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: io: 4, immutability_locks: 4, structural_boundaries: 2, safety_bypasses: 1
- `tests/cases/compiler/genericFunctionsWithOptionalParameters1.ts` (TYPESCRIPT) | Magnitude: 6.37 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 3, structural_boundaries: 3, state_mutation: 3, generics: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `tests/baselines/reference/mappedTypeMultiInference.js` (JAVASCRIPT) | Magnitude: 19.4 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 11, state_mutation: 4, structural_boundaries: 3, dead_code: 2
- `tests/cases/fourslash/augmentedTypesModule3.ts` (TYPESCRIPT) | Magnitude: 1.52 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: structural_boundaries: 1, safety: 1, state_mutation: 1, dead_code: 1
- `tests/cases/compiler/excessiveStackDepthFlatArray.ts` (TYPESCRIPT) | Magnitude: 0.71 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 23, indent_spaces: 23, generics: 9, ui_framework: 5
- `tests/cases/fourslash/codeFixUndeclaredMethodFunctionArgs_importArgumentType.ts` (TYPESCRIPT) | Magnitude: 2.88 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 9, dead_code: 4, structural_boundaries: 3, args: 3
- `tests/cases/fourslash/refactorConvertParamsToDestructuredObject_methodOverrides.ts` (TYPESCRIPT) | Magnitude: 4.3 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 10, args: 4, func_start: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `tests/baselines/reference/jsxSpreadTag(target=esnext).js` (JAVASCRIPT) | Magnitude: 17.52 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: immutability_locks: 13, indent_spaces: 8, structural_boundaries: 6, ui_framework: 5
- `tests/baselines/reference/checkInfiniteExpansionTermination.js` (JAVASCRIPT) | Magnitude: 19.26 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 5, state_mutation: 4, ui_framework: 2, indent_spaces: 1
- `tests/baselines/reference/contextualTypingOfOptionalMembers.js` (JAVASCRIPT) | Magnitude: 31.84 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 45, structural_boundaries: 27, func_start: 19, ui_framework: 19
- `tests/cases/compiler/genericCallWithinOwnBodyCastTypeParameterIdentity.ts` (TYPESCRIPT) | Magnitude: 2.37 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 13, generics: 13, args: 7
- `tests/cases/compiler/awaitedTypeStrictNull.ts` (TYPESCRIPT) | Magnitude: 2.43 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 17, generics: 17, ui_framework: 10, concurrency: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `tests/baselines/reference/convertToAsyncFunction/convertToAsyncFunction_PromiseAllAndThen3.ts` (TYPESCRIPT) | Magnitude: 1.59 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: io: 12, sec_io: 10, structural_boundaries: 9, concurrency: 9
- `tests/baselines/reference/usingDeclarations.1(target=es2022).js` (JAVASCRIPT) | Magnitude: 773.28 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 586, branch: 185, safety: 125, concurrency: 92
- `tests/baselines/reference/nullishCoalescingOperatorInAsyncGenerator(target=es5).js` (JAVASCRIPT) | Magnitude: 65.56 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 23, branch: 13, structural_boundaries: 10, state_mutation: 9
- `tests/baselines/reference/plainJSBinderErrors.js` (JAVASCRIPT) | Magnitude: 77.8 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 56, structural_boundaries: 24, immutability_locks: 18, func_start: 16
- `tests/baselines/reference/asyncMultiFile_es5(target=es5).js` (JAVASCRIPT) | Magnitude: 601.62 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: branch: 60, indent_spaces: 35, state_mutation: 30, structural_boundaries: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `tests/cases/fourslash/getOutliningForBlockComments.ts` (TYPESCRIPT) | Magnitude: 1.05 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 49, dead_code: 20
- `tests/cases/fourslash/completionsCommentsCommentParsing.ts` (TYPESCRIPT) | Magnitude: 1.05 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 62, dead_code: 33
- `tests/cases/fourslash/quickInfoCommentsCommentParsing.ts` (TYPESCRIPT) | Magnitude: 1.05 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 62, dead_code: 33
- `tests/cases/fourslash/signatureHelpCommentsCommentParsing.ts` (TYPESCRIPT) | Magnitude: 1.05 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 62, dead_code: 33
- `tests/cases/fourslash/contextualTypingOfGenericCallSignatures2.ts` (TYPESCRIPT) | Magnitude: 1.1 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: structural_boundaries: 1, dead_code: 1, doc: 1, generics: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `tests/cases/conformance/es6/functionExpressions/FunctionExpression1_es6.ts` (TYPESCRIPT) | Magnitude: 0.21 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 1, func_start: 1, state_mutation: 1, lazy_evaluation: 1
- `tests/baselines/reference/jsdocVariableDeclarationWithTypeAnnotation.js` (JAVASCRIPT) | Magnitude: 14.6 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 12, structural_boundaries: 2, state_mutation: 2, indent_spaces: 1
- `tests/cases/conformance/jsdoc/callbackOnConstructor.ts` (TYPESCRIPT) | Magnitude: 0.36 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 6, structural_boundaries: 4, args: 2, func_start: 2
- `tests/cases/conformance/jsdoc/checkJsdocTypeTag3.ts` (TYPESCRIPT) | Magnitude: 1.15 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 2, structural_boundaries: 1, state_mutation: 1
- `tests/cases/conformance/salsa/malformedTags.ts` (TYPESCRIPT) | Magnitude: 1.15 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 2, structural_boundaries: 1, state_mutation: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `tests/baselines/reference/APISample_linter.js` (JAVASCRIPT) | Magnitude: 337.18 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 101, branch: 63, state_mutation: 59, structural_boundaries: 30
- `tests/baselines/reference/emptyVariableDeclarationBindingPatterns01_ES5iterable(target=es5).js` (JAVASCRIPT) | Magnitude: 173.14 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 154, state_mutation: 134, branch: 99, structural_boundaries: 65
- `tests/cases/compiler/constraintPropagationThroughReturnTypes.ts` (TYPESCRIPT) | Magnitude: 0.43 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 3, indent_spaces: 3, args: 2, func_start: 2
- `tests/cases/compiler/typeParameterAndArgumentOfSameName1.ts` (TYPESCRIPT) | Magnitude: 0.37 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 3, indent_spaces: 2, args: 1, func_start: 1
- `tests/cases/fourslash/completionsWithDeprecatedTag1.ts` (TYPESCRIPT) | Magnitude: 1.75 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 20, doc: 8, structural_boundaries: 3, api: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `tests/cases/fourslash/completionsCommentsClassMembers.ts` (TYPESCRIPT) | Magnitude: 1.05 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: doc: 25, dead_code: 17
- `tests/cases/fourslash/completionsCommentsFunctionExpression.ts` (TYPESCRIPT) | Magnitude: 1.05 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: doc: 17, dead_code: 4
- `tests/cases/fourslash/quickInfoCommentsClassMembers.ts` (TYPESCRIPT) | Magnitude: 1.05 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: doc: 25, dead_code: 17
- `tests/cases/fourslash/quickInfoCommentsFunctionExpression.ts` (TYPESCRIPT) | Magnitude: 1.05 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: doc: 17, dead_code: 4
- `tests/cases/fourslash/signatureHelpCommentsClassMembers.ts` (TYPESCRIPT) | Magnitude: 1.05 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: doc: 25, dead_code: 17

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/lib/webworker.generated.d.ts` -> Churn: **75.18%** | Cog Load: 15.2934% | Debt: 93.1198%
- `src/lib/esnext.temporal.d.ts` -> Churn: **73.66%** | Cog Load: 24.3205% | Debt: 72.1594%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `tests/baselines/reference/emitter.asyncGenerators.classMethods.es5(target=es5).js` -> **Ryan Cavanaugh** (100.0% isolated ownership) | Magnitude: 3421.58
- `tests/baselines/reference/emitter.asyncGenerators.objectLiteralMethods.es5(target=es5).js` -> **Ryan Cavanaugh** (100.0% isolated ownership) | Magnitude: 2654.4
- `tests/baselines/reference/emitter.asyncGenerators.functionExpressions.es5(target=es5).js` -> **Ryan Cavanaugh** (100.0% isolated ownership) | Magnitude: 2625.74
- `tests/baselines/reference/emitter.asyncGenerators.functionDeclarations.es5(target=es5).js` -> **Ryan Cavanaugh** (100.0% isolated ownership) | Magnitude: 2604.74
- `tests/baselines/reference/awaitUsingDeclarationsInForAwaitOf(target=es5).js` -> **Ryan Cavanaugh** (100.0% isolated ownership) | Magnitude: 1061.1

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/compiler/core.ts` -> **Severity: 52.6** (Blast Radius: 0.526 * Doc Risk: 100.0%)
- `src/typescript/typescript.ts` -> **Severity: 36.4** (Blast Radius: 0.364 * Doc Risk: 99.9999%)
- `src/compiler/transformers/module/module.ts` -> **Severity: 25.354** (Blast Radius: 1.418 * Doc Risk: 17.8804%)
- `src/tsserver/common.ts` -> **Severity: 22.454** (Blast Radius: 0.259 * Doc Risk: 86.6943%)
- `src/testRunner/unittests/tsbuildWatch/reexport.ts` -> **Severity: 20.149** (Blast Radius: 0.205 * Doc Risk: 98.2887%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
