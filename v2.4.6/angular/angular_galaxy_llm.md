# ARCHITECTURAL_BRIEF: angular
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_web/angular` |
| **Timestamp** | `2026-08-03T20:00:37.477801+00:00` |
| **Scan Duration** | `15.45s` |
| **Git Branch** | `main` |
| **Git Commit** | `9d76ac82290e047f1481fb38bd95233e951a77de` |
| **Git Remote** | `https://github.com/angular/angular.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 3660 malicious artifacts.

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
| Total Artifacts | 9855 |
| Analyzed Artifacts (Scanned) | 5940 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 3915 |
| Total LOC | 349915 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 60.3% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1819 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 1.5% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 373 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 3512 | 276712 | 59.1% |
| MARKDOWN | 562 | 0 | 9.5% |
| PLAINTEXT | 435 | 1 | 7.3% |
| CSS | 417 | 23541 | 7.0% |
| HTML | 414 | 20831 | 7.0% |
| JSON | 336 | 21731 | 5.7% |
| JAVASCRIPT | 104 | 3375 | 1.8% |
| XML | 81 | 166 | 1.4% |
| YAML | 35 | 1111 | 0.6% |
| PYTHON | 22 | 1536 | 0.4% |
| SHELL | 15 | 729 | 0.3% |
| NIX | 7 | 182 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.415`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 2648 | 44.6% |
| file_cluster_13 | 1784 | 30.0% |
| file_cluster_4 | 167 | 2.8% |
| file_cluster_16 | 107 | 1.8% |
| file_cluster_0 | 99 | 1.7% |
| file_cluster_17 | 38 | 0.6% |
| file_cluster_2 | 34 | 0.6% |
| file_cluster_11 | 9 | 0.2% |
| file_cluster_7 | 7 | 0.1% |
| file_cluster_1 | 6 | 0.1% |
| file_cluster_12 | 5 | 0.1% |
| file_cluster_6 | 4 | 0.1% |
| file_cluster_9 | 4 | 0.1% |
| file_cluster_15 | 2 | 0.0% |
| Unknown | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 996 | 16.8% |
| Static: Minified & Vendor Opaque Mass | 29 | 0.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 3915*

**Composition by Extension & Reason:**
- `.ts`: 1787x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 5x Unsupported Format (.undeterminable), 2x Excluded (Saturation: Line 13 exceeds 500 chars)
- `.js`: 793x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.bazel`: 334x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Unsupported Extension: '.bazel')
- `.png`: 180x Excluded (Explicitly Denied Extension: '.png')
- `.json`: 137x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Excluded (Massive Static Asset Blob: 7696 LOC), 1x Excluded (Massive Static Asset Blob: 7529 LOC)
- `.mts`: 142x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 64x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Excluded (Machine-Generated Source Code Signature: 28 LOC), 2x Excluded (Machine-Generated Source Code Signature: 50 LOC)
- `no_extension`: 56x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 20x Unsupported Format (.undeterminable)
- `.scss`: 40x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.html`: 37x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 54 exceeds 500 chars), 1x Excluded (Saturation: Line 7 exceeds 500 chars)
- `.gif`: 36x Excluded (Explicitly Denied Extension: '.gif')
- `.ico`: 33x Excluded (Explicitly Denied Extension: '.ico')
- `.tsx`: 30x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Massive Static Asset Blob: 8745 LOC), 2x Excluded (Massive Static Asset Blob: 8722 LOC)
- `.yml`: 19x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 14.3 | 5.2 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 26.9 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 8.5 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 9.6 | 1.1 | 0.0 |
| API Exposure | 0.0 | 18.5 | 4.1 | 4.4 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 9.9 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 20.3 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 0.4 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 81.9 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 46.4 | 2.2 | 0.4 | 0.0 |
| Volatility Exposure | 0.0 | 67.9 | 5.4 | 3.1 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 23.7 | 11.9 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 14.0 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 5.2 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.4 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `adev/src/app/routing/navigation-entries/index.ts` (Hits: 314)
- `devtools/projects/ng-devtools/src/lib/devtools-tabs/injector-tree/injector-tree-fns.spec.ts` (Hits: 95)
- `packages/localize/tools/test/translate/integration/main_spec.ts` (Hits: 87)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **platform-browser.ts** (`packages/platform-browser/src/platform-browser.ts`) — 232 inbound connections
2. **router.ts** (`packages/router/src/router.ts`) — 155 inbound connections
3. **output_ast.ts** (`packages/compiler/src/output/output_ast.ts`) — 83 inbound connections
4. **path.ts** (`packages/compiler-cli/src/ngtsc/util/src/path.ts`) — 76 inbound connections
5. **view_utils.ts** (`packages/core/src/render3/util/view_utils.ts`) — 57 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **emit.ts** (`packages/compiler/src/template/pipeline/src/emit.ts`) — 73 outbound dependencies
2. **core_private_export.ts** (`packages/core/src/core_private_export.ts`) — 60 outbound dependencies
3. **compiler.ts** (`packages/compiler/src/compiler.ts`) — 59 outbound dependencies
4. **core.ts** (`packages/core/src/core.ts`) — 56 outbound dependencies
5. **component_ref.ts** (`packages/core/src/render3/component_ref.ts`) — 47 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `index` (@ `packages/compiler-cli/src/ngtsc/annotations/component/src/handler.ts`) -> Impact: **945.4** | LOC: 1020
- `describe` (@ `packages/compiler-cli/src/ngtsc/typecheck/test/type_check_block_spec.ts`) -> Impact: **790.7** | LOC: 365
- `locateHostElement` (@ `packages/core/src/render3/instructions/shared.ts`) -> Impact: **773.9** | LOC: 537
- `escapeForTemplateLiteral` (@ `packages/compiler/src/output/output_ast.ts`) -> Impact: **748.5** | LOC: 748
- `ingestDeferTriggers` (@ `packages/compiler/src/template/pipeline/src/ingest.ts`) -> Impact: **741.1** | LOC: 679
- `migrateClass` (@ `packages/core/schematics/ng-generate/inject-migration/migration.ts`) -> Impact: **731.8** | LOC: 417
- `transformExpressionsInOp` (@ `packages/compiler/src/template/pipeline/ir/src/expression.ts`) -> Impact: **698.9** | LOC: 160
- `resolvePlaceholdersForView` (@ `packages/compiler/src/template/pipeline/src/phases/resolve_i18n_element_placeholders.ts`) -> Impact: **650.8** | LOC: 295
- `describe` (@ `packages/compiler-cli/src/ngtsc/typecheck/test/type_check_block_spec.ts`) -> Impact: **616.8** | LOC: 1425
- `assertValidDateFormat` (@ `packages/common/src/i18n/format_date.ts`) -> Impact: **584.2** | LOC: 384

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `describe` (@ `devtools/projects/ng-devtools/src/lib/devtools-tabs/router-tree/router-details-row/route-data-serializer.spec.ts`) -> **O(2^N) [Recursive]**
  * *Intent:* /** * @license * Copyright Google LLC All Rights Reserved. * * Use of this source code is governed by an MIT-style license that can be
- `describe` (@ `packages/localize/tools/test/translate/translation_files/translation_parsers/xliff2_translation_parser_spec.ts`) -> **O(2^N) [Recursive]**
- `bootstrap` (@ `packages/upgrade/static/src/upgrade_module.ts`) -> **O(2^N) [Recursive]**
  * *Intent:* /** * Bootstrap an AngularJS application from this NgModule
- `createTView` (@ `tools/symbol-extractor/symbol_extractor_spec/hello_world_min_debug.js`) -> **O(2^N) [Recursive]**
- `describe` (@ `packages/compiler-cli/src/ngtsc/transform/jit/test/downlevel_decorators_transform_spec.ts`) -> **O(2^N) [Recursive]**
- `createWithEachNg1VersionFn` (@ `packages/upgrade/src/common/test/helpers/common_test_helpers.ts`) -> **O(2^N) [Recursive]**
- `getScriptInfo` (@ `vscode-ng-language-service/server/src/text_render.ts`) -> **O(2^N) [Recursive]**
- `describe` (@ `devtools/cypress/integration/node-selection.e2e.js`) -> **O(2^N) [Recursive]**
  * *Intent:* /** * @license
- `sendRequestToTsVfs` (@ `adev/src/app/editor/code-editor/extensions/autocomplete.ts`) -> **O(2^N) [Recursive]**
- `describe` (@ `adev/src/app/editor/embedded-tutorial-manager.service.spec.ts`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `runInNativeFileSystem` (@ `packages/localize/tools/test/translate/integration/main_spec.ts`) -> DB Complexity: **286**
- `service-setup-command_[Truncated]` (@ `tools/saucelabs/sauce-service.sh`) -> DB Complexity: **191**
- `runInEachFileSystem` (@ `packages/compiler-cli/src/ngtsc/sourcemaps/test/source_file_loader_spec.ts`) -> DB Complexity: **164**
- `monkeyPatchTypeScript` (@ `packages/compiler-cli/src/ngtsc/file_system/testing/src/test_helper.ts`) -> DB Complexity: **131**
- `escapeForTemplateLiteral` (@ `packages/compiler/src/output/output_ast.ts`) -> DB Complexity: **126**
- `runInNativeFileSystem` (@ `packages/localize/tools/test/extract/integration/main_spec.ts`) -> DB Complexity: **123**
- `init` (@ `adev/src/app/editor/node-runtime-sandbox.service.ts`) -> DB Complexity: **111**
- `runInEachFileSystem` (@ `packages/localize/tools/test/translate/output_path_spec.ts`) -> DB Complexity: **109**
- `index` (@ `packages/compiler-cli/src/ngtsc/annotations/component/src/handler.ts`) -> DB Complexity: **107**
- `runInEachFileSystem` (@ `packages/compiler-cli/src/ngtsc/sourcemaps/test/source_file_spec.ts`) -> DB Complexity: **107**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `__monolith__` | 19 | 5174.39 | 3.79% | 6.03% |
| `packages/compiler/src/template/pipeline/src/phases` | 68 | 708.56 | 20.15% | 6.66% |
| `packages/common/http/src` | 19 | 632.53 | 28.87% | 30.9% |
| `packages/core/src/render3` | 50 | 549.25 | 13.31% | 13.34% |
| `adev/src/app/features/update` | 5 | 466.14 | 31.23% | 1.86% |
| `packages/language-service/src` | 19 | 452.19 | 30.34% | 8.72% |
| `packages/compiler/src/ml_parser` | 11 | 433.41 | 25.49% | 21.42% |
| `packages/service-worker/worker/src` | 16 | 420.71 | 40.76% | 16.71% |
| `packages/zone.js` | 20 | 374.52 | 6.17% | 23.94% |
| `packages/compiler-cli/src/ngtsc/typecheck/src` | 23 | 370.72 | 23.09% | 6.07% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `.agent/skills/pr_review/scripts/determine_review_type.sh` -> **100.0%** Exposure
- `.agent/skills/pr_review/scripts/get_pr_comments.sh` -> **100.0%** Exposure
- `packages/router/scripts/build.sh` -> **100.0%** Exposure
- `packages/router/scripts/karma.sh` -> **100.0%** Exposure
- `packages/zone.js/scripts/sauce/sauce_connect_block.sh` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `.agent/skills/pr_review/scripts/post_inline_comment.sh` -> **100.0%** Exposure
- `.agent/skills/pr_review/scripts/reply_pr_comment.sh` -> **100.0%** Exposure
- `.agent/skills/pr_review/scripts/submit_pr_review.sh` -> **100.0%** Exposure
- `packages/zone.js/scripts/sauce/sauce_connect_setup.sh` -> **100.0%** Exposure
- `scripts/ci/publish-snapshot-build-artifacts.sh` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `packages/compiler/src/template/pipeline/ir/src/expression.ts` -> **0** Orphaned Functions | **156** Duplicates
- `packages/common/http/src/client.ts` -> **0** Orphaned Functions | **81** Duplicates
- `packages/compiler/src/expression_parser/ast.ts` -> **0** Orphaned Functions | **70** Duplicates
- `packages/compiler/src/render3/r3_ast.ts` -> **0** Orphaned Functions | **63** Duplicates
- `packages/router/src/events.ts` -> **0** Orphaned Functions | **35** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`packages/common/http/src/client.ts`** -> AI Confidence: **99.48%**
2. **`packages/core/schematics/ng-generate/standalone-migration/prune-modules.ts`** -> AI Confidence: **99.48%**
3. **`packages/compiler-cli/src/ngtsc/annotations/component/src/handler.ts`** -> AI Confidence: **99.39%**
4. **`packages/compiler-cli/src/ngtsc/transform/src/compilation.ts`** -> AI Confidence: **99.39%**
5. **`packages/compiler/src/template/pipeline/src/phases/reify.ts`** -> AI Confidence: **99.39%**
6. **`packages/core/src/render3/instructions/change_detection.ts`** -> AI Confidence: **99.39%**
7. **`packages/core/src/render3/node_animations.ts`** -> AI Confidence: **99.39%**
8. **`packages/core/src/render3/view/directives.ts`** -> AI Confidence: **99.39%**
9. **`packages/language-service/src/document_symbols.ts`** -> AI Confidence: **99.39%**
10. **`packages/compiler/src/template/pipeline/src/ingest.ts`** -> AI Confidence: **99.35%**
11. **`packages/common/http/src/request.ts`** -> AI Confidence: **99.34%**
12. **`packages/compiler/src/render3/r3_control_flow.ts`** -> AI Confidence: **99.34%**
13. **`packages/compiler/src/render3/r3_deferred_blocks.ts`** -> AI Confidence: **99.34%**
14. **`packages/core/schematics/ng-generate/inject-migration/migration.ts`** -> AI Confidence: **99.34%**
15. **`packages/localize/schematics/ng-add/index.ts`** -> AI Confidence: **99.34%**
16. **`packages/compiler/src/template/pipeline/src/phases/create_i18n_contexts.ts`** -> AI Confidence: **99.32%**
17. **`packages/compiler/src/template/pipeline/src/phases/generate_variables.ts`** -> AI Confidence: **99.32%**
18. **`packages/compiler/src/template/pipeline/src/phases/resolve_i18n_element_placeholders.ts`** -> AI Confidence: **99.32%**
19. **`packages/compiler/src/template/pipeline/src/phases/resolve_names.ts`** -> AI Confidence: **99.32%**
20. **`tools/symbol-extractor/run_all_symbols_extractor_tests.js`** -> AI Confidence: **99.32%**
21. **`adev/src/app/core/layout/navigation/navigation.component.ts`** -> AI Confidence: **99.31%**
22. **`adev/src/app/editor/code-editor/workers/typescript-vfs.worker.ts`** -> AI Confidence: **99.31%**
23. **`adev/src/app/features/update/update.component.ts`** -> AI Confidence: **99.31%**
24. **`devtools/projects/ng-devtools-backend/src/lib/component-tree/component-tree.ts`** -> AI Confidence: **99.31%**
25. **`devtools/projects/ng-devtools/src/lib/devtools-tabs/injector-tree/injector-tree.component.ts`** -> AI Confidence: **99.31%**
26. **`devtools/projects/ng-devtools/src/lib/shared/split/split.component.ts`** -> AI Confidence: **99.31%**
27. **`packages/animations/browser/src/dsl/animation_transition_factory.ts`** -> AI Confidence: **99.31%**
28. **`packages/animations/browser/src/render/timeline_animation_engine.ts`** -> AI Confidence: **99.31%**
29. **`packages/animations/browser/src/render/transition_animation_engine.ts`** -> AI Confidence: **99.31%**
30. **`packages/common/http/src/fetch.ts`** -> AI Confidence: **99.31%**
31. **`packages/common/http/src/resource.ts`** -> AI Confidence: **99.31%**
32. **`packages/common/http/src/transfer_cache.ts`** -> AI Confidence: **99.31%**
33. **`packages/compiler-cli/linker/src/file_linker/partial_linkers/partial_directive_linker_1.ts`** -> AI Confidence: **99.31%**
34. **`packages/compiler-cli/src/ngtsc/annotations/common/src/diagnostics.ts`** -> AI Confidence: **99.31%**
35. **`packages/compiler-cli/src/ngtsc/annotations/component/src/util.ts`** -> AI Confidence: **99.31%**
36. **`packages/compiler-cli/src/ngtsc/annotations/directive/src/query_functions.ts`** -> AI Confidence: **99.31%**
37. **`packages/compiler-cli/src/ngtsc/annotations/directive/src/shared.ts`** -> AI Confidence: **99.31%**
38. **`packages/compiler-cli/src/ngtsc/annotations/ng_module/src/handler.ts`** -> AI Confidence: **99.31%**
39. **`packages/compiler-cli/src/ngtsc/annotations/src/injectable.ts`** -> AI Confidence: **99.31%**
40. **`packages/compiler-cli/src/ngtsc/incremental/src/incremental.ts`** -> AI Confidence: **99.31%**
41. **`packages/compiler-cli/src/ngtsc/partial_evaluator/src/diagnostics.ts`** -> AI Confidence: **99.31%**
42. **`packages/compiler-cli/src/ngtsc/partial_evaluator/src/interpreter.ts`** -> AI Confidence: **99.31%**
43. **`packages/compiler-cli/src/ngtsc/preprocessor.ts`** -> AI Confidence: **99.31%**
44. **`packages/compiler-cli/src/ngtsc/scope/src/local.ts`** -> AI Confidence: **99.31%**
45. **`packages/compiler-cli/src/ngtsc/transform/src/transform.ts`** -> AI Confidence: **99.31%**
46. **`packages/compiler-cli/src/ngtsc/typecheck/src/checker.ts`** -> AI Confidence: **99.31%**
47. **`packages/compiler-cli/src/ngtsc/typecheck/src/oob.ts`** -> AI Confidence: **99.31%**
48. **`packages/compiler-cli/src/ngtsc/typecheck/src/ops/events.ts`** -> AI Confidence: **99.31%**
49. **`packages/compiler-cli/src/ngtsc/typecheck/src/ops/scope.ts`** -> AI Confidence: **99.31%**
50. **`packages/compiler-cli/src/ngtsc/typecheck/src/ops/signal_forms.ts`** -> AI Confidence: **99.31%**
51. **`packages/compiler-cli/src/ngtsc/typecheck/src/template_symbol_builder.ts`** -> AI Confidence: **99.31%**
52. **`packages/compiler-cli/src/ngtsc/validation/src/source_file_validator.ts`** -> AI Confidence: **99.31%**
53. **`packages/compiler/src/render3/partial/directive.ts`** -> AI Confidence: **99.31%**
54. **`packages/compiler/src/render3/r3_deferred_triggers.ts`** -> AI Confidence: **99.31%**
55. **`packages/compiler/src/render3/view/i18n/meta.ts`** -> AI Confidence: **99.31%**
56. **`packages/compiler/src/render3/view/query_generation.ts`** -> AI Confidence: **99.31%**
57. **`packages/compiler/src/template/pipeline/ir/src/expression.ts`** -> AI Confidence: **99.31%**
58. **`packages/compiler/src/template/pipeline/src/phases/i18n_const_collection.ts`** -> AI Confidence: **99.31%**
59. **`packages/compiler/src/template_parser/binding_parser.ts`** -> AI Confidence: **99.31%**
60. **`packages/core/primitives/event-dispatch/src/action_resolver.ts`** -> AI Confidence: **99.31%**
61. **`packages/core/schematics/migrations/output-migration/output-migration.ts`** -> AI Confidence: **99.31%**
62. **`packages/core/schematics/migrations/signal-migration/src/convert-input/convert_to_signal.ts`** -> AI Confidence: **99.31%**
63. **`packages/core/schematics/migrations/signal-migration/src/passes/1_identify_inputs.ts`** -> AI Confidence: **99.31%**
64. **`packages/core/schematics/migrations/signal-migration/src/passes/problematic_patterns/common_incompatible_patterns.ts`** -> AI Confidence: **99.31%**
65. **`packages/core/schematics/migrations/signal-migration/src/passes/reference_migration/helpers/standard_reference.ts`** -> AI Confidence: **99.31%**
66. **`packages/core/schematics/migrations/signal-migration/src/passes/reference_migration/migrate_ts_references.ts`** -> AI Confidence: **99.31%**
67. **`packages/core/schematics/migrations/signal-migration/src/passes/reference_migration/migrate_ts_type_references.ts`** -> AI Confidence: **99.31%**
68. **`packages/core/schematics/migrations/signal-migration/src/passes/reference_resolution/identify_host_references.ts`** -> AI Confidence: **99.31%**
69. **`packages/core/schematics/migrations/signal-migration/src/passes/reference_resolution/identify_ts_references.ts`** -> AI Confidence: **99.31%**
70. **`packages/core/schematics/migrations/signal-queries-migration/convert_query_property.ts`** -> AI Confidence: **99.31%**
71. **`packages/core/schematics/migrations/signal-queries-migration/migration.ts`** -> AI Confidence: **99.31%**
72. **`packages/core/schematics/ng-generate/control-flow-migration/migration.ts`** -> AI Confidence: **99.31%**
73. **`packages/core/schematics/ng-generate/ngclass-to-class-migration/util.ts`** -> AI Confidence: **99.31%**
74. **`packages/core/schematics/ng-generate/ngstyle-to-style-migration/util.ts`** -> AI Confidence: **99.31%**
75. **`packages/core/schematics/ng-generate/route-lazy-loading/index.ts`** -> AI Confidence: **99.31%**
76. **`packages/core/schematics/ng-generate/route-lazy-loading/to-lazy-routes.ts`** -> AI Confidence: **99.31%**
77. **`packages/core/schematics/ng-generate/standalone-migration/standalone-bootstrap.ts`** -> AI Confidence: **99.31%**
78. **`packages/core/schematics/ng-generate/standalone-migration/to-standalone.ts`** -> AI Confidence: **99.31%**
79. **`packages/core/schematics/utils/tsurge/helpers/angular_devkit/run_in_devkit.ts`** -> AI Confidence: **99.31%**
80. **`packages/core/schematics/utils/typescript/imports.ts`** -> AI Confidence: **99.31%**
81. **`packages/core/src/animation/utils.ts`** -> AI Confidence: **99.31%**
82. **`packages/core/src/application/create_application.ts`** -> AI Confidence: **99.31%**
83. **`packages/core/src/defer/instructions.ts`** -> AI Confidence: **99.31%**
84. **`packages/core/src/defer/registry.ts`** -> AI Confidence: **99.31%**
85. **`packages/core/src/defer/utils.ts`** -> AI Confidence: **99.31%**
86. **`packages/core/src/event_emitter.ts`** -> AI Confidence: **99.31%**
87. **`packages/core/src/hydration/annotate.ts`** -> AI Confidence: **99.31%**
88. **`packages/core/src/hydration/cleanup.ts`** -> AI Confidence: **99.31%**
89. **`packages/core/src/hydration/error_handling.ts`** -> AI Confidence: **99.31%**
90. **`packages/core/src/hydration/i18n.ts`** -> AI Confidence: **99.31%**
91. **`packages/core/src/hydration/node_lookup_utils.ts`** -> AI Confidence: **99.31%**
92. **`packages/core/src/hydration/views.ts`** -> AI Confidence: **99.31%**
93. **`packages/core/src/image_performance_warning.ts`** -> AI Confidence: **99.31%**
94. **`packages/core/src/linker/view_container_ref.ts`** -> AI Confidence: **99.31%**
95. **`packages/core/src/render3/collect_native_nodes.ts`** -> AI Confidence: **99.31%**
96. **`packages/core/src/render3/component_ref.ts`** -> AI Confidence: **99.31%**
97. **`packages/core/src/render3/context_discovery.ts`** -> AI Confidence: **99.31%**
98. **`packages/core/src/render3/definition.ts`** -> AI Confidence: **99.31%**
99. **`packages/core/src/render3/di_setup.ts`** -> AI Confidence: **99.31%**
100. **`packages/core/src/render3/errors_di.ts`** -> AI Confidence: **99.31%**
101. **`packages/core/src/render3/features/host_directives_feature.ts`** -> AI Confidence: **99.31%**
102. **`packages/core/src/render3/features/inherit_definition_feature.ts`** -> AI Confidence: **99.31%**
103. **`packages/core/src/render3/hooks.ts`** -> AI Confidence: **99.31%**
104. **`packages/core/src/render3/i18n/i18n_apply.ts`** -> AI Confidence: **99.31%**
105. **`packages/core/src/render3/i18n/i18n_parse.ts`** -> AI Confidence: **99.31%**
106. **`packages/core/src/render3/instructions/control.ts`** -> AI Confidence: **99.31%**
107. **`packages/core/src/render3/instructions/control_flow.ts`** -> AI Confidence: **99.31%**
108. **`packages/core/src/render3/instructions/element.ts`** -> AI Confidence: **99.31%**
109. **`packages/core/src/render3/instructions/listener.ts`** -> AI Confidence: **99.31%**
110. **`packages/core/src/render3/instructions/shared.ts`** -> AI Confidence: **99.31%**
111. **`packages/core/src/render3/instructions/styling.ts`** -> AI Confidence: **99.31%**
112. **`packages/core/src/render3/instructions/template.ts`** -> AI Confidence: **99.31%**
113. **`packages/core/src/render3/instructions/write_to_directive_input.ts`** -> AI Confidence: **99.31%**
114. **`packages/core/src/render3/node_manipulation.ts`** -> AI Confidence: **99.31%**
115. **`packages/core/src/render3/node_selector_matcher.ts`** -> AI Confidence: **99.31%**
116. **`packages/core/src/render3/queries/query_execution.ts`** -> AI Confidence: **99.31%**
117. **`packages/core/src/render3/queries/query_reactive.ts`** -> AI Confidence: **99.31%**
118. **`packages/core/src/render3/reactivity/effect.ts`** -> AI Confidence: **99.31%**
119. **`packages/core/src/render3/styling/style_binding_list.ts`** -> AI Confidence: **99.31%**
120. **`packages/core/src/render3/util/control_flow.ts`** -> AI Confidence: **99.31%**
121. **`packages/core/src/render3/util/view_utils.ts`** -> AI Confidence: **99.31%**
122. **`packages/core/src/render3/view/container.ts`** -> AI Confidence: **99.31%**
123. **`packages/core/src/render3/view/directive_outputs.ts`** -> AI Confidence: **99.31%**
124. **`packages/core/src/render3/view_manipulation.ts`** -> AI Confidence: **99.31%**
125. **`packages/core/src/resource/debounce.ts`** -> AI Confidence: **99.31%**
126. **`packages/core/testing/src/test_bed_compiler.ts`** -> AI Confidence: **99.31%**
127. **`packages/forms/signals/compat/src/signal_form_control/signal_form_control.ts`** -> AI Confidence: **99.31%**
128. **`packages/forms/src/directives/ng_control.ts`** -> AI Confidence: **99.31%**
129. **`packages/forms/src/directives/ng_model.ts`** -> AI Confidence: **99.31%**
130. **`packages/forms/src/directives/reactive_directives/form_control_name.ts`** -> AI Confidence: **99.31%**
131. **`packages/forms/src/model/abstract_model.ts`** -> AI Confidence: **99.31%**
132. **`packages/language-service/src/completions.ts`** -> AI Confidence: **99.31%**
133. **`packages/language-service/src/definitions.ts`** -> AI Confidence: **99.31%**
134. **`packages/language-service/src/inlay_hints.ts`** -> AI Confidence: **99.31%**
135. **`packages/language-service/src/references_and_rename_utils.ts`** -> AI Confidence: **99.31%**
136. **`packages/language-service/src/signature_help.ts`** -> AI Confidence: **99.31%**
137. **`packages/language-service/src/utils/index.ts`** -> AI Confidence: **99.31%**
138. **`packages/language-service/src/utils/ts_utils.ts`** -> AI Confidence: **99.31%**
139. **`packages/language-service/testing/src/project.ts`** -> AI Confidence: **99.31%**
140. **`packages/localize/tools/src/extract/translation_files/xliff1_translation_serializer.ts`** -> AI Confidence: **99.31%**
141. **`packages/localize/tools/src/extract/translation_files/xliff2_translation_serializer.ts`** -> AI Confidence: **99.31%**
142. **`packages/localize/tools/test/translate/source_files/es5_translate_plugin_spec.ts`** -> AI Confidence: **99.31%**
143. **`packages/platform-browser/src/browser.ts`** -> AI Confidence: **99.31%**
144. **`packages/platform-server/src/utils.ts`** -> AI Confidence: **99.31%**
145. **`packages/router/src/directives/router_link.ts`** -> AI Confidence: **99.31%**
146. **`packages/router/src/directives/router_outlet.ts`** -> AI Confidence: **99.31%**
147. **`packages/router/src/navigation_transition.ts`** -> AI Confidence: **99.31%**
148. **`packages/router/src/router.ts`** -> AI Confidence: **99.31%**
149. **`packages/router/src/router_module.ts`** -> AI Confidence: **99.31%**
150. **`packages/router/src/statemanager/navigation_state_manager.ts`** -> AI Confidence: **99.31%**
151. **`packages/router/src/statemanager/state_manager.ts`** -> AI Confidence: **99.31%**
152. **`packages/router/src/utils/preactivation.ts`** -> AI Confidence: **99.31%**
153. **`scripts/diff-release-package.mts`** -> AI Confidence: **99.31%**
154. **`vscode-ng-language-service/server/src/handlers/completions.ts`** -> AI Confidence: **99.31%**
155. **`devtools/tools/angular-optimization/esbuild-plugin.mjs`** -> AI Confidence: **99.31%**
156. **`packages/zone.js/scripts/sauce/sauce_connect_block.sh`** -> AI Confidence: **99.29%**
157. **`devtools/projects/ng-devtools-backend/src/lib/version.ts`** -> AI Confidence: **99.29%**
158. **`devtools/projects/shell-browser/src/app/ng-validate.ts`** -> AI Confidence: **99.29%**
159. **`modules/benchmarks/src/tree/baseline/tree.ts`** -> AI Confidence: **99.29%**
160. **`packages/common/src/directives/ng_class.ts`** -> AI Confidence: **99.29%**
161. **`packages/common/src/directives/ng_component_outlet.ts`** -> AI Confidence: **99.29%**
162. **`packages/common/src/pipes/date_pipe.ts`** -> AI Confidence: **99.29%**
163. **`packages/compiler/src/template/pipeline/src/phases/assign_i18n_slot_dependencies.ts`** -> AI Confidence: **99.29%**
164. **`packages/compiler/src/template/pipeline/src/phases/attribute_extraction.ts`** -> AI Confidence: **99.29%**
165. **`packages/compiler/src/template/pipeline/src/phases/convert_i18n_bindings.ts`** -> AI Confidence: **99.29%**
166. **`packages/compiler/src/template/pipeline/src/phases/defer_resolve_targets.ts`** -> AI Confidence: **99.29%**
167. **`packages/compiler/src/template/pipeline/src/phases/i18n_text_extraction.ts`** -> AI Confidence: **99.29%**
168. **`packages/compiler/src/template/pipeline/src/phases/resolve_i18n_expression_placeholders.ts`** -> AI Confidence: **99.29%**
169. **`packages/compiler/src/template/pipeline/src/phases/wrap_icus.ts`** -> AI Confidence: **99.29%**
170. **`packages/router/src/route_injector_cleanup.ts`** -> AI Confidence: **99.29%**
171. **`packages/service-worker/config/src/glob.ts`** -> AI Confidence: **99.29%**
172. **`vscode-ng-language-service/syntaxes/src/expression.ts`** -> AI Confidence: **99.29%**
173. **`vscode-ng-language-service/syntaxes/src/template-blocks.ts`** -> AI Confidence: **99.29%**
174. **`vscode-ng-language-service/syntaxes/src/template-tag.ts`** -> AI Confidence: **99.29%**
175. **`goldens/public-api/manage.js`** -> AI Confidence: **99.29%**
176. **`karma-js.conf.js`** -> AI Confidence: **99.29%**
177. **`adev/src/app/features/references/api-reference-details-page/api-reference-details-page.component.ts`** -> AI Confidence: **99.24%**
178. **`adev/src/app/features/references/api-reference-list/api-reference-list.component.ts`** -> AI Confidence: **99.24%**
179. **`devtools/projects/ng-devtools-backend/src/lib/client-event-subscribers.ts`** -> AI Confidence: **99.24%**
180. **`devtools/projects/ng-devtools/src/lib/devtools-tabs/directive-explorer/property-pane/property-view/property-view-body/prop-actions-menu/prop-actions-menu.component.ts`** -> AI Confidence: **99.24%**
181. **`packages/animations/browser/src/dsl/animation.ts`** -> AI Confidence: **99.24%**
182. **`packages/common/src/directives/ng_optimized_image/ng_optimized_image.ts`** -> AI Confidence: **99.24%**
183. **`packages/compiler-cli/linker/src/file_linker/linker_environment.ts`** -> AI Confidence: **99.24%**
184. **`packages/compiler-cli/linker/src/file_linker/partial_linkers/partial_component_linker_1.ts`** -> AI Confidence: **99.24%**
185. **`packages/compiler-cli/src/ngtsc/annotations/common/src/evaluation.ts`** -> AI Confidence: **99.24%**
186. **`packages/compiler-cli/src/ngtsc/annotations/directive/src/handler.ts`** -> AI Confidence: **99.24%**
187. **`packages/compiler-cli/src/ngtsc/core/src/compiler.ts`** -> AI Confidence: **99.24%**
188. **`packages/compiler-cli/src/ngtsc/program.ts`** -> AI Confidence: **99.24%**
189. **`packages/compiler-cli/src/ngtsc/typecheck/extended/test/checks/nullish_coalescing_not_nullable/nullish_coalescing_not_nullable_spec.ts`** -> AI Confidence: **99.24%**
190. **`packages/compiler-cli/src/ngtsc/typecheck/src/ops/directive_constructor.ts`** -> AI Confidence: **99.24%**
191. **`packages/compiler-cli/src/ngtsc/typecheck/src/ops/inputs.ts`** -> AI Confidence: **99.24%**
192. **`packages/compiler-cli/src/ngtsc/typecheck/src/tcb_adapter.ts`** -> AI Confidence: **99.24%**
193. **`packages/compiler-cli/src/ngtsc/typecheck/test/type_check_block_spec.ts`** -> AI Confidence: **99.24%**
194. **`packages/compiler/src/i18n/i18n_html_parser.ts`** -> AI Confidence: **99.24%**
195. **`packages/compiler/src/render3/view/t2_binder.ts`** -> AI Confidence: **99.24%**
196. **`packages/compiler/src/render3/view/util.ts`** -> AI Confidence: **99.24%**
197. **`packages/core/schematics/migrations/signal-migration/src/migration.ts`** -> AI Confidence: **99.24%**
198. **`packages/core/schematics/migrations/signal-migration/src/phase_analysis.ts`** -> AI Confidence: **99.24%**
199. **`packages/core/schematics/ng-generate/inject-migration/index.ts`** -> AI Confidence: **99.24%**
200. **`packages/core/schematics/ng-generate/standalone-migration/index.ts`** -> AI Confidence: **99.24%**
201. **`packages/core/src/application/application_ref.ts`** -> AI Confidence: **99.24%**
202. **`packages/core/src/change_detection/scheduling/ng_zone_scheduling.ts`** -> AI Confidence: **99.24%**
203. **`packages/core/src/change_detection/scheduling/zoneless_scheduling_impl.ts`** -> AI Confidence: **99.24%**
204. **`packages/core/src/di/injector.ts`** -> AI Confidence: **99.24%**
205. **`packages/core/src/di/provider_collection.ts`** -> AI Confidence: **99.24%**
206. **`packages/core/src/di/r3_injector.ts`** -> AI Confidence: **99.24%**
207. **`packages/core/src/metadata/directives.ts`** -> AI Confidence: **99.24%**
208. **`packages/core/src/render3/i18n/i18n_util.ts`** -> AI Confidence: **99.24%**
209. **`packages/core/src/render3/instructions/animation.ts`** -> AI Confidence: **99.24%**
210. **`packages/core/src/render3/instructions/element_container.ts`** -> AI Confidence: **99.24%**
211. **`packages/core/src/render3/instructions/projection.ts`** -> AI Confidence: **99.24%**
212. **`packages/core/src/render3/jit/directive.ts`** -> AI Confidence: **99.24%**
213. **`packages/core/src/render3/pipe.ts`** -> AI Confidence: **99.24%**
214. **`packages/core/src/render3/queries/query.ts`** -> AI Confidence: **99.24%**
215. **`packages/core/src/render3/reactivity/after_render_effect.ts`** -> AI Confidence: **99.24%**
216. **`packages/core/src/render3/util/signal_debug.ts`** -> AI Confidence: **99.24%**
217. **`packages/core/src/render3/view/elements.ts`** -> AI Confidence: **99.24%**
218. **`packages/core/src/render3/view_ref.ts`** -> AI Confidence: **99.24%**
219. **`packages/core/src/resource/resource.ts`** -> AI Confidence: **99.24%**
220. **`packages/core/src/sanitization/sanitization.ts`** -> AI Confidence: **99.24%**
221. **`packages/forms/signals/src/api/structure.ts`** -> AI Confidence: **99.24%**
222. **`packages/forms/src/directives/reactive_directives/form_control_directive.ts`** -> AI Confidence: **99.24%**
223. **`packages/language-service/src/codefixes/fix_missing_import.ts`** -> AI Confidence: **99.24%**
224. **`packages/language-service/src/refactorings/convert_to_signal_queries/apply_query_refactoring.ts`** -> AI Confidence: **99.24%**
225. **`packages/localize/tools/src/extract/index.ts`** -> AI Confidence: **99.24%**
226. **`packages/localize/tools/test/translate/source_files/es2015_translate_plugin_spec.ts`** -> AI Confidence: **99.24%**
227. **`packages/service-worker/worker/src/driver.ts`** -> AI Confidence: **99.24%**
228. **`vscode-ng-language-service/client/src/client.ts`** -> AI Confidence: **99.24%**
229. **`vscode-ng-language-service/server/src/handlers/hover.ts`** -> AI Confidence: **99.24%**
230. **`vscode-ng-language-service/syntaxes/src/build.ts`** -> AI Confidence: **99.24%**
231. **`packages/common/http/src/xhr.ts`** -> AI Confidence: **99.23%**
232. **`packages/common/src/pipes/number_pipe.ts`** -> AI Confidence: **99.23%**
233. **`packages/compiler-cli/src/ngtsc/metadata/src/dts.ts`** -> AI Confidence: **99.23%**
234. **`packages/compiler-cli/src/ngtsc/metadata/src/util.ts`** -> AI Confidence: **99.23%**
235. **`packages/compiler-cli/src/ngtsc/typecheck/extended/test/checks/unparenthesized_nullish_coalescing/unparenthesized_nullish_coalescing_spec.ts`** -> AI Confidence: **99.23%**
236. **`packages/compiler-cli/src/ngtsc/typecheck/src/type_constructor.ts`** -> AI Confidence: **99.23%**
237. **`packages/compiler-cli/src/perform_compile.ts`** -> AI Confidence: **99.23%**
238. **`packages/compiler/src/i18n/extractor_merger.ts`** -> AI Confidence: **99.23%**
239. **`packages/compiler/src/i18n/i18n_parser.ts`** -> AI Confidence: **99.23%**
240. **`packages/compiler/src/template/pipeline/src/phases/binding_specialization.ts`** -> AI Confidence: **99.23%**
241. **`packages/compiler/src/template/pipeline/src/phases/resolve_sanitizers.ts`** -> AI Confidence: **99.23%**
242. **`packages/core/schematics/migrations/signal-migration/src/passes/6_migrate_input_declarations.ts`** -> AI Confidence: **99.23%**
243. **`packages/core/schematics/ng-generate/standalone-migration/util.ts`** -> AI Confidence: **99.23%**
244. **`packages/core/schematics/utils/tsurge/helpers/create_program.ts`** -> AI Confidence: **99.23%**
245. **`packages/core/schematics/utils/tsurge/test/output_migration.ts`** -> AI Confidence: **99.23%**
246. **`packages/core/src/application/stability_debug_impl.ts`** -> AI Confidence: **99.23%**
247. **`packages/core/src/di/contextual.ts`** -> AI Confidence: **99.23%**
248. **`packages/core/src/render3/errors.ts`** -> AI Confidence: **99.23%**
249. **`packages/core/src/render3/i18n/i18n_icu_container_visitor.ts`** -> AI Confidence: **99.23%**
250. **`packages/core/src/render3/instructions/text_interpolation.ts`** -> AI Confidence: **99.23%**
251. **`packages/core/src/render3/node_manipulation_i18n.ts`** -> AI Confidence: **99.23%**
252. **`packages/forms/signals/src/field/structure.ts`** -> AI Confidence: **99.23%**
253. **`packages/language-service/src/refactorings/convert_to_signal_input/apply_input_refactoring.ts`** -> AI Confidence: **99.23%**
254. **`packages/localize/tools/src/translate/source_files/source_file_translation_handler.ts`** -> AI Confidence: **99.23%**
255. **`packages/router/src/directives/router_link_active.ts`** -> AI Confidence: **99.23%**
256. **`packages/router/src/operators/activate_routes.ts`** -> AI Confidence: **99.23%**
257. **`packages/router/src/router_preloader.ts`** -> AI Confidence: **99.23%**
258. **`packages/router/src/router_state.ts`** -> AI Confidence: **99.23%**
259. **`packages/service-worker/worker/testing/scope.ts`** -> AI Confidence: **99.23%**
260. **`packages/compiler-cli/src/ngtsc/scope/src/standalone.ts`** -> AI Confidence: **99.22%**
261. **`packages/common/src/i18n/format_date.ts`** -> AI Confidence: **99.2%**
262. **`packages/common/src/i18n/format_number.ts`** -> AI Confidence: **99.2%**
263. **`packages/compiler-cli/src/ngtsc/metadata/src/ng_module_index.ts`** -> AI Confidence: **99.2%**
264. **`packages/compiler/src/template/pipeline/src/phases/conditionals.ts`** -> AI Confidence: **99.2%**
265. **`packages/compiler/src/template/pipeline/src/phases/next_context_merging.ts`** -> AI Confidence: **99.2%**
266. **`packages/compiler/src/template/pipeline/src/phases/propagate_i18n_blocks.ts`** -> AI Confidence: **99.2%**
267. **`packages/compiler/src/template/pipeline/src/phases/strip_nonrequired_parentheses.ts`** -> AI Confidence: **99.2%**
268. **`packages/core/schematics/migrations/signal-migration/src/batch/merge_unit_data.ts`** -> AI Confidence: **99.2%**
269. **`packages/core/schematics/migrations/signal-migration/src/utils/is_identifier_free_in_scope.ts`** -> AI Confidence: **99.2%**
270. **`packages/misc/angular-in-memory-web-api/src/interfaces.ts`** -> AI Confidence: **99.2%**
271. **`adev/src/app/editor/code-editor/code-editor.component.ts`** -> AI Confidence: **99.18%**
272. **`adev/src/app/editor/code-editor/extensions/autocomplete.ts`** -> AI Confidence: **99.18%**
273. **`adev/src/app/editor/preview/preview.component.spec.ts`** -> AI Confidence: **99.18%**
274. **`adev/src/app/features/playground/playground.component.ts`** -> AI Confidence: **99.18%**
275. **`devtools/projects/ng-devtools/src/lib/devtools-tabs/directive-explorer/directive-forest/directive-forest.component.ts`** -> AI Confidence: **99.18%**
276. **`devtools/projects/ng-devtools/src/lib/devtools-tabs/directive-explorer/property-pane/for-loop-view/for-loop-view.component.ts`** -> AI Confidence: **99.18%**
277. **`devtools/projects/ng-devtools/src/lib/devtools-tabs/directive-explorer/property-pane/property-pane.component.ts`** -> AI Confidence: **99.18%**
278. **`devtools/projects/ng-devtools/src/lib/devtools-tabs/directive-explorer/property-pane/property-view/property-view.component.ts`** -> AI Confidence: **99.18%**
279. **`devtools/projects/ng-devtools/src/lib/devtools-tabs/directive-explorer/signal-graph-pane/signal-graph-pane.component.ts`** -> AI Confidence: **99.18%**
280. **`devtools/projects/ng-devtools/src/lib/devtools-tabs/profiler/profiler.component.ts`** -> AI Confidence: **99.18%**
281. **`devtools/projects/ng-devtools/src/lib/devtools.component.ts`** -> AI Confidence: **99.18%**
282. **`packages/animations/browser/src/render/animation_engine_next.ts`** -> AI Confidence: **99.18%**
283. **`packages/benchpress/src/runner.ts`** -> AI Confidence: **99.18%**
284. **`packages/benchpress/src/sampler.ts`** -> AI Confidence: **99.18%**
285. **`packages/common/http/src/jsonp.ts`** -> AI Confidence: **99.18%**
286. **`packages/compiler-cli/src/ngtsc/annotations/common/test/diagnostics_spec.ts`** -> AI Confidence: **99.18%**
287. **`packages/compiler-cli/src/ngtsc/imports/src/emitter.ts`** -> AI Confidence: **99.18%**
288. **`packages/compiler-cli/src/ngtsc/imports/test/emitter_spec.ts`** -> AI Confidence: **99.18%**
289. **`packages/compiler-cli/src/ngtsc/indexer/test/util.ts`** -> AI Confidence: **99.18%**
290. **`packages/compiler-cli/src/ngtsc/reflection/test/ts_host_spec.ts`** -> AI Confidence: **99.18%**
291. **`packages/compiler-cli/src/ngtsc/sourcemaps/test/source_file_spec.ts`** -> AI Confidence: **99.18%**
292. **`packages/compiler-cli/src/ngtsc/typecheck/extended/test/checks/uninvoked_function_in_event_binding/uninvoked_function_in_event_binding_spec.ts`** -> AI Confidence: **99.18%**
293. **`packages/compiler-cli/src/ngtsc/typecheck/extended/test/checks/uninvoked_track_function/uninvoked_track_function.spec.ts`** -> AI Confidence: **99.18%**
294. **`packages/compiler-cli/src/ngtsc/typecheck/testing/index.ts`** -> AI Confidence: **99.18%**
295. **`packages/compiler/src/render3/view/template.ts`** -> AI Confidence: **99.18%**
296. **`packages/core/schematics/migrations/signal-migration/src/input_detection/known_inputs.ts`** -> AI Confidence: **99.18%**
297. **`packages/core/schematics/utils/tsurge/testing/run_single.ts`** -> AI Confidence: **99.18%**
298. **`packages/core/src/application/application_ngmodule_factory_compiler.ts`** -> AI Confidence: **99.18%**
299. **`packages/core/src/authoring/model/model_signal.ts`** -> AI Confidence: **99.18%**
300. **`packages/core/src/defer/dom_triggers.ts`** -> AI Confidence: **99.18%**
301. **`packages/core/src/hydration/api.ts`** -> AI Confidence: **99.18%**
302. **`packages/core/src/linker/template_ref.ts`** -> AI Confidence: **99.18%**
303. **`packages/core/src/platform/bootstrap.ts`** -> AI Confidence: **99.18%**
304. **`packages/core/src/platform/platform.ts`** -> AI Confidence: **99.18%**
305. **`packages/core/src/render3/di.ts`** -> AI Confidence: **99.18%**
306. **`packages/core/src/render3/features/ng_onchanges_feature.ts`** -> AI Confidence: **99.18%**
307. **`packages/core/src/render3/instructions/i18n.ts`** -> AI Confidence: **99.18%**
308. **`packages/core/src/render3/instructions/queries.ts`** -> AI Confidence: **99.18%**
309. **`packages/core/src/render3/instructions/text.ts`** -> AI Confidence: **99.18%**
310. **`packages/core/src/render3/instructions/two_way.ts`** -> AI Confidence: **99.18%**
311. **`packages/core/src/render3/interfaces/node.ts`** -> AI Confidence: **99.18%**
312. **`packages/core/src/render3/scope.ts`** -> AI Confidence: **99.18%**
313. **`packages/core/src/render3/util/discovery_utils.ts`** -> AI Confidence: **99.18%**
314. **`packages/core/src/render3/util/global_utils.ts`** -> AI Confidence: **99.18%**
315. **`packages/core/src/render3/view/construction.ts`** -> AI Confidence: **99.18%**
316. **`packages/core/src/render3/view/listeners.ts`** -> AI Confidence: **99.18%**
317. **`packages/forms/signals/src/api/rules/validation/standard_schema.ts`** -> AI Confidence: **99.18%**
318. **`packages/forms/signals/src/directive/control_native.ts`** -> AI Confidence: **99.18%**
319. **`packages/forms/signals/src/field/node.ts`** -> AI Confidence: **99.18%**
320. **`packages/forms/signals/src/schema/logic.ts`** -> AI Confidence: **99.18%**
321. **`packages/forms/src/directives/reactive_directives/abstract_form.directive.ts`** -> AI Confidence: **99.18%**
322. **`packages/forms/src/directives/reactive_directives/form_group_name.ts`** -> AI Confidence: **99.18%**
323. **`packages/forms/src/directives/shared.ts`** -> AI Confidence: **99.18%**
324. **`packages/language-service/src/quick_info.ts`** -> AI Confidence: **99.18%**
325. **`packages/language-service/src/refactorings/convert_to_signal_input/full_class_input_refactoring.ts`** -> AI Confidence: **99.18%**
326. **`packages/language-service/src/refactorings/convert_to_signal_queries/full_class_query_refactoring.ts`** -> AI Confidence: **99.18%**
327. **`packages/language-service/src/refactorings/convert_to_signal_queries/individual_query_refactoring.ts`** -> AI Confidence: **99.18%**
328. **`packages/localize/tools/test/extract/translation_files/xliff1_translation_serializer_spec.ts`** -> AI Confidence: **99.18%**
329. **`packages/localize/tools/test/translate/translation_files/translation_loader_spec.ts`** -> AI Confidence: **99.18%**
330. **`packages/misc/angular-in-memory-web-api/src/http-client-backend-service.ts`** -> AI Confidence: **99.18%**
331. **`packages/router/src/operators/check_guards.ts`** -> AI Confidence: **99.18%**
332. **`packages/router/src/operators/resolve_data.ts`** -> AI Confidence: **99.18%**
333. **`packages/service-worker/worker/src/app-version.ts`** -> AI Confidence: **99.18%**
334. **`vscode-ng-language-service/server/src/handlers/folding.ts`** -> AI Confidence: **99.18%**
335. **`vscode-ng-language-service/server/src/session.ts`** -> AI Confidence: **99.18%**
336. **`tools/legacy-saucelabs/build-saucelabs-test-bundle.mjs`** -> AI Confidence: **99.18%**
337. **`.agent/skills/pr_review/scripts/determine_review_type.sh`** -> AI Confidence: **99.17%**
338. **`.agent/skills/pr_review/scripts/post_inline_comment.sh`** -> AI Confidence: **99.17%**
339. **`scripts/test/run-saucelabs-tests.sh`** -> AI Confidence: **99.17%**
340. **`adev/shared-docs/utils/analytics.utils.ts`** -> AI Confidence: **99.17%**
341. **`modules/benchmarks/src/largetable/baseline/table.ts`** -> AI Confidence: **99.17%**
342. **`packages/benchpress/src/metric/perflog_metric.ts`** -> AI Confidence: **99.17%**
343. **`packages/common/http/testing/src/request.ts`** -> AI Confidence: **99.17%**
344. **`packages/common/src/directives/ng_if.ts`** -> AI Confidence: **99.17%**
345. **`packages/compiler-cli/src/ngtsc/core/api/src/public_options.ts`** -> AI Confidence: **99.17%**
346. **`packages/compiler/src/directive_matching.ts`** -> AI Confidence: **99.17%**
347. **`packages/compiler/src/ml_parser/lexer.ts`** -> AI Confidence: **99.17%**
348. **`packages/compiler/src/template/pipeline/src/phases/generate_advance.ts`** -> AI Confidence: **99.17%**
349. **`packages/compiler/src/template/pipeline/src/phases/nonbindable.ts`** -> AI Confidence: **99.17%**
350. **`packages/compiler/src/template/pipeline/src/phases/remove_empty_bindings.ts`** -> AI Confidence: **99.17%**
351. **`packages/compiler/src/template/pipeline/src/phases/remove_unused_i18n_attrs.ts`** -> AI Confidence: **99.17%**
352. **`packages/compiler/src/template/pipeline/src/phases/resolve_contexts.ts`** -> AI Confidence: **99.17%**
353. **`packages/compiler/src/template/pipeline/src/phases/resolve_defer_deps_fns.ts`** -> AI Confidence: **99.17%**
354. **`packages/compiler/src/template/pipeline/src/phases/slot_allocation.ts`** -> AI Confidence: **99.17%**
355. **`packages/compiler/src/template/pipeline/src/phases/style_binding_specialization.ts`** -> AI Confidence: **99.17%**
356. **`packages/compiler/src/template/pipeline/src/phases/variable_optimization.ts`** -> AI Confidence: **99.17%**
357. **`packages/core/schematics/utils/tsurge/helpers/string_manipulation/cut_string_line_length.ts`** -> AI Confidence: **99.17%**
358. **`packages/core/src/render3/list_reconciliation.ts`** -> AI Confidence: **99.17%**
359. **`packages/core/src/util/comparison.ts`** -> AI Confidence: **99.17%**
360. **`packages/language-service/src/quick_info_built_ins.ts`** -> AI Confidence: **99.17%**
361. **`packages/language-service/src/utils/format.ts`** -> AI Confidence: **99.17%**
362. **`packages/localize/tools/src/extract/translation_files/icu_parsing.ts`** -> AI Confidence: **99.17%**
363. **`packages/service-worker/config/src/duration.ts`** -> AI Confidence: **99.17%**
364. **`packages/upgrade/static/src/upgrade_component.ts`** -> AI Confidence: **99.17%**
365. **`tools/symbol-extractor/symbol_extractor.mts`** -> AI Confidence: **99.17%**
366. **`vscode-ng-language-service/syntaxes/src/host-object-literal.ts`** -> AI Confidence: **99.17%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `packages/compiler/src/ml_parser/entities.ts` -> **0.0368%** Exposure
### Exploit Generation Surface
- `adev/scripts/routes/generate-routes.mts` -> **100.0%** Exposure
- `adev/src/app/core/layout/progress-bar/progress-bar.component.ts` -> **100.0%** Exposure
- `adev/src/app/core/layout/secondary-navigation/secondary-navigation.component.ts` -> **100.0%** Exposure
- `adev/src/app/editor/code-editor/code-mirror-editor.service.ts` -> **100.0%** Exposure
- `adev/src/app/editor/embedded-tutorial-manager.service.spec.ts` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `scripts/ci/publish-snapshot-build-artifacts.sh` -> **100.0%** Exposure
- `tools/saucelabs/sauce-service.sh` -> **100.0%** Exposure
- `adev/src/app/core/services/analytics/analytics-format-error.ts` -> **100.0%** Exposure
- `adev/src/content/examples/animations/src/app/animations.ts` -> **100.0%** Exposure
- `packages/animations/browser/src/error_helpers.ts` -> **100.0%** Exposure
### Hardcoded Payload Artifacts
- `adev/src/app/environment.ts` -> **99.9997%** Exposure
- `packages/core/src/application/application_init.ts` -> **99.9462%** Exposure
- `packages/core/src/application/application_ref.ts` -> **99.4854%** Exposure
- `packages/core/src/di/r3_injector.ts` -> **56.1377%** Exposure
### Algorithmic DoS Exposure
- `tools/saucelabs/sauce-service.sh` -> **100.0%** Exposure
- `adev/src/app/app-scroller.ts` -> **100.0%** Exposure
- `adev/src/app/core/layout/navigation/navigation.component.ts` -> **100.0%** Exposure
- `adev/src/app/core/layout/progress-bar/progress-bar.component.ts` -> **100.0%** Exposure
- `adev/src/app/core/layout/secondary-navigation/secondary-navigation.component.ts` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `36` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `4795` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `vscode-ng-language-service/server/src/server_host.ts` (TYPESCRIPT) -> Cumulative Risk: **939.6**
- **Archetype:** `file_cluster_13` (Distance: 12.646 IQR)
- **Magnitude:** 32.71 | **LOC:** 290 | **CtrlFlow:** 39.7% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `watchDirectory` (Impact: 99.4), `watchFile` (Impact: 79.6), `notifyFileChange` (Impact: 39.3)

### 2. `packages/core/src/change_detection/scheduling/ng_zone_scheduling.ts` (TYPESCRIPT) -> Cumulative Risk: **930.95**
- **Archetype:** `file_cluster_13` (Distance: 12.971 IQR)
- **Magnitude:** 20.66 | **LOC:** 282 | **CtrlFlow:** 45.9% | **Authorship Centralization:** 62.5%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `initialize` (Impact: 30.2), `getNgZoneOptions` (Impact: 18.4), `initialize` (Impact: 15.3)

### 3. `packages/service-worker/worker/src/driver.ts` (TYPESCRIPT) -> Cumulative Risk: **895.35**
- **Archetype:** `file_cluster_4` (Distance: 13.838 IQR)
- **Magnitude:** 160.07 | **LOC:** 1398 | **CtrlFlow:** 42.6% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `assignVersion` (Impact: 330.4), `handleClick` (Impact: 80.5), `onFetch` (Impact: 48.5)

### 4. `packages/router/src/navigation_transition.ts` (TYPESCRIPT) -> Cumulative Risk: **889.51**
- **Archetype:** `file_cluster_13` (Distance: 12.708 IQR)
- **Magnitude:** 47.61 | **LOC:** 1022 | **CtrlFlow:** 46.6% | **Authorship Centralization:** 81.2%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.9894%)
- **Heaviest Functions:** `catchError` (Impact: 80.8), `switchMap` (Impact: 52.7), `switchTap` (Impact: 47.9)

### 5. `packages/router/src/router_preloader.ts` (TYPESCRIPT) -> Cumulative Risk: **885.84**
- **Archetype:** `file_cluster_4` (Distance: 13.272 IQR)
- **Magnitude:** 24.05 | **LOC:** 194 | **CtrlFlow:** 46.4% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), State Flux (99.9966%)
- **Heaviest Functions:** `processRoutes` (Impact: 111.0), `preloadConfig` (Impact: 39.8), `ngOnDestroy` (Impact: 3.0)

### 6. `packages/router/src/statemanager/state_manager.ts` (TYPESCRIPT) -> Cumulative Risk: **879.93**
- **Archetype:** `file_cluster_13` (Distance: 13.579 IQR)
- **Magnitude:** 27.13 | **LOC:** 309 | **CtrlFlow:** 59.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `handleRouterEvent` (Impact: 50.6), `restoreHistory` (Impact: 21.6), `listener` (Impact: 20.5)

### 7. `packages/animations/browser/src/render/transition_animation_engine.ts` (TYPESCRIPT) -> Cumulative Risk: **876.14**
- **Archetype:** `file_cluster_17` (Distance: 13.088 IQR)
- **Magnitude:** 116.84 | **LOC:** 1944 | **CtrlFlow:** 58.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `insertNode` (Impact: 55.5), `removeNode` (Impact: 54.8), `removeNode` (Impact: 48.9)

### 8. `devtools/projects/ng-devtools/src/lib/devtools-tabs/transfer-state/transfer-state.component.ts` (TYPESCRIPT) -> Cumulative Risk: **865.62**
- **Archetype:** `file_cluster_13` (Distance: 12.529 IQR)
- **Magnitude:** 14.03 | **LOC:** 177 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 40.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (99.9996%)
- **Heaviest Functions:** `copyToClipboard` (Impact: 19.4), `loadTransferState` (Impact: 14.8), `getValueType` (Impact: 6.2)

### 9. `packages/benchpress/src/webdriver/ios_driver_extension.ts` (TYPESCRIPT) -> Cumulative Risk: **861.07**
- **Archetype:** `file_cluster_4` (Distance: 11.225 IQR)
- **Magnitude:** 19.1 | **LOC:** 145 | **CtrlFlow:** 37.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), State Flux (99.9889%)
- **Heaviest Functions:** `_convertPerfRecordsToEvents` (Impact: 95.5), `readPerfLog` (Impact: 7.9), `timeEnd` (Impact: 7.3)

### 10. `packages/service-worker/worker/src/idle.ts` (TYPESCRIPT) -> Cumulative Risk: **850.07**
- **Archetype:** `file_cluster_4` (Distance: 14.213 IQR)
- **Magnitude:** 23.93 | **LOC:** 114 | **CtrlFlow:** 36.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `execute` (Impact: 16.7), `trigger` (Impact: 11.9), `schedule` (Impact: 8.4)

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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `adev/src/app/features/update/recommendations.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.29 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.6 IQR)
- **Top Global Matches:** file_cluster_8: 9.29, file_cluster_0: 9.736, file_cluster_1: 10.081
- **Magnitude:** 421.19 | **LOC:** 2916 | **CtrlFlow:** 52.1% | **Authorship Centralization:** 40.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (7.0837%), Tech Debt (9.3181%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 163`, `structural_boundaries: 150`, `args: 3`, `func_start: 1`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 40`, `state_mutation: 13`, `planned_debt: 1`, `fragile_debt: 4`
* *Architecture:* `io: 84`, `api: 10`, `concurrency: 16`, `import: 15`
* *Defense:* `safety: 81`, `doc: 1`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.155
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` platform-browser, core
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/compiler/src/ml_parser/lexer.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.37 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.401 IQR)
- **Top Global Matches:** file_cluster_8: 14.37, file_cluster_0: 14.451, file_cluster_13: 14.534
- **Magnitude:** 308.19 | **LOC:** 1834 | **CtrlFlow:** 69.6% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 53
- **Risk Profile:** Cognitive Load (70.9503%), Tech Debt (41.6578%)
**Top Internal Functions/Classes:**
  * `_consumeTagOpen` (Impact: 120.8 | O(N^3) | DB: 31)
  * `processEscapeSequence` (Impact: 101.0 | O(N^3) | DB: 53)
  * `tokenize` (Impact: 93.2 | O(N^3) | DB: 35)
  * `prematureEndPredicate` (Impact: 91.2 | O(2^N) | DB: 25)
  * `_consumeBlockParameters` (Impact: 81.9 | O(N^3) | DB: 15)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 410`, `structural_boundaries: 179`, `args: 153`, `func_start: 135`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 1597`, `duplicate_logic: 14`
* *Architecture:* `io: 2`, `api: 10`, `import: 5`
* *Defense:* `safety: 46`, `doc: 37`, `immutability_locks: 99`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` entities, tokens, chars, parse_util, tags
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/common/http/src/client.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.146 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.944 IQR)
- **Top Global Matches:** file_cluster_8: 11.146, file_cluster_16: 11.271, file_cluster_2: 11.39
- **Magnitude:** 289.42 | **LOC:** 5025 | **CtrlFlow:** 97.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (22.3692%), Tech Debt (99.8781%)
**Top Internal Functions/Classes:**
  * `options` (Impact: 58.1 | O(2^N))
    * *Intent:* // No validation needed for JSON responses, as they can be of any type.
  * `options` (Impact: 58.1 | O(2^N))
  * `options` (Impact: 55.1 | O(2^N))
    * *Intent:* /** * Constructs a `DELETE` request that interprets the body as a `Blob` and returns * the response ...
  * `options` (Impact: 52.1 | O(2^N))
  * `options` (Impact: 52.1 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1401`, `structural_boundaries: 30`, `args: 68`, `func_start: 85`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 82`, `state_mutation: 16`, `duplicate_logic: 81`
* *Architecture:* `io: 1`, `api: 3`, `concurrency: 118`, `import: 10`
* *Defense:* `safety: 1`, `doc: 377`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` core, backend, request, rxjs, context, response, errors, headers...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/compiler/src/template/pipeline/ir/src/expression.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.133 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.666 IQR)
- **Top Global Matches:** file_cluster_8: 13.133, file_cluster_13: 13.199, file_cluster_11: 13.328
- **Magnitude:** 212.07 | **LOC:** 1448 | **CtrlFlow:** 51.5% | **Authorship Centralization:** 58.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (69.7911%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `transformExpressionsInOp` (Impact: 698.9 | O(2^N) | DB: 2)
  * `transformExpressionsInExpression` (Impact: 387.0 | O(2^N) | DB: 5)
  * `transformExpressionsInStatement` (Impact: 54.9 | O(2^N))
  * `clone` (Impact: 24.7 | O(2^N) | DB: 4)
  * `isEquivalent` (Impact: 24.6 | O(2^N) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 229`, `structural_boundaries: 216`, `args: 220`, `func_start: 212`, `class_start: 29`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 331`, `planned_debt: 3`, `duplicate_logic: 156`
* *Architecture:* `api: 62`, `import: 11`
* *Defense:* `safety: 57`, `doc: 26`, `immutability_locks: 84`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` create, parse_util, traits, operations, util, update, handle, shared...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/compiler-cli/src/ngtsc/typecheck/test/type_check_block_spec.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.236 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 5.878 IQR)
- **Top Global Matches:** file_cluster_8: 12.236, file_cluster_0: 12.422, file_cluster_11: 12.646
- **Magnitude:** 202.41 | **LOC:** 3182 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 54.2%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 73
- **Risk Profile:** Cognitive Load (24.8198%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 790.7 | O(N^3) | DB: 7)
  * `describe` (Impact: 616.8 | O(2^N) | DB: 73)
  * `describe` (Impact: 88.3 | O(N^3) | DB: 20)
  * `it` (Impact: 52.1 | O(N^4))
  * `describe` (Impact: 45.3 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 355`, `structural_boundaries: 532`, `args: 630`, `func_start: 577`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 119`, `state_mutation: 215`, `fragile_debt: 1`, `duplicate_logic: 27`
* *Architecture:* `api: 5`, `import: 8`
* *Defense:* `safety: 55`, `doc: 1`, `test: 573`, `immutability_locks: 338`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` testing, core, typescript, imports, compiler, testing, api, file_system
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/compiler/src/output/output_ast.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.93 IQR)
- **Local Micro-Species:** `Cluster 2: Type Definitions & Bypasses` (Drift: 4.309 IQR)
- **Top Global Matches:** file_cluster_8: 12.93, file_cluster_13: 13.039, file_cluster_11: 13.089
- **Magnitude:** 163.59 | **LOC:** 2091 | **CtrlFlow:** 32.7% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 126
- **Risk Profile:** Cognitive Load (77.1283%), Tech Debt (99.9469%)
**Top Internal Functions/Classes:**
  * `escapeForTemplateLiteral` (Impact: 748.5 | O(2^N) | DB: 126)
  * `visitIfStmt` (Impact: 34.8 | O(N^1) | DB: 26)
  * `constructor` (Impact: 26.0 | O(N^1) | DB: 1)
    * *Intent:* // TODO: Should we deep clone statements?
  * `isEquivalent` (Impact: 20.4 | O(2^N) | DB: 3)
  * `constructor` (Impact: 18.6 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 182`, `structural_boundaries: 375`, `args: 271`, `func_start: 245`, `class_start: 45`
* *Risk/State:* `safety_bypasses: 174`, `state_mutation: 434`, `dead_code: 1`, `planned_debt: 3`, `duplicate_logic: 30`
* *Architecture:* `io: 1`, `api: 131`, `import: 4`
* *Defense:* `safety: 13`, `doc: 16`, `immutability_locks: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 5.808
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` meta, parse_util, digest, i18n_ast
  * `Imported By (In-Degree: 83):` (Excluded from Brief to save tokens)

### `packages/service-worker/worker/src/driver.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.838 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 5.708 IQR)
- **Top Global Matches:** file_cluster_4: 13.838, file_cluster_17: 14.284, file_cluster_13: 14.627
- **Magnitude:** 160.07 | **LOC:** 1398 | **CtrlFlow:** 42.6% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 79
- **Risk Profile:** Cognitive Load (77.0992%), Tech Debt (14.974%)
**Top Internal Functions/Classes:**
  * `assignVersion` (Impact: 330.4 | O(2^N) | DB: 79)
  * `handleClick` (Impact: 80.5 | O(N^2) | DB: 15)
    * *Intent:* /** * The handler for fetch events.
  * `onFetch` (Impact: 48.5 | O(N^2) | DB: 28)
    * *Intent:* /** * Determines if a given URL scope corresponds to localhost.
  * `handleFetch` (Impact: 34.8 | O(2^N) | DB: 8)
  * `ensureInitialized` (Impact: 12.4 | O(N^1) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 100`, `structural_boundaries: 135`, `args: 56`, `func_start: 35`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 15`, `high_risk_execution: 1`, `state_mutation: 345`, `dead_code: 2`, `planned_debt: 2`, `fragile_debt: 2`
* *Architecture:* `io: 9`, `api: 6`, `concurrency: 684`, `import: 10`
* *Defense:* `safety: 45`, `doc: 12`, `immutability_locks: 50`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.148
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` idle, error, db-cache, app-version, adapter, api, database, debug...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/compiler-cli/src/ngtsc/annotations/component/src/handler.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.874 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.932 IQR)
- **Top Global Matches:** file_cluster_13: 12.874, file_cluster_17: 13.023, file_cluster_8: 13.048
- **Magnitude:** 158.42 | **LOC:** 2643 | **CtrlFlow:** 72.1% | **Authorship Centralization:** 30.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 107
- **Risk Profile:** Cognitive Load (88.3061%), Tech Debt (12.3716%)
**Top Internal Functions/Classes:**
  * `index` (Impact: 945.4 | O(N^3) | DB: 107)
  * `makeDiagnostic` (Impact: 63.2 | O(2^N) | DB: 1)
  * `makeResourceNotFoundError` (Impact: 25.2 | O(N^3) | DB: 1)
  * `makeDiagnostic` (Impact: 10.8 | O(N^2) | DB: 2)
  * `isUsedPipe` (Impact: 8.4 | O(N^2) | DB: 11)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 269`, `structural_boundaries: 104`, `args: 46`, `func_start: 36`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 494`, `dead_code: 3`, `duplicate_logic: 3`
* *Architecture:* `io: 5`, `api: 2`, `import: 37`
* *Defense:* `safety: 28`, `doc: 14`, `immutability_locks: 149`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` ng_module, perf, util, cycles, file_system, typecheck, jit_declaration_registry, transform...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/compiler/src/template/pipeline/src/ingest.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.73 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.985 IQR)
- **Top Global Matches:** file_cluster_8: 12.73, file_cluster_13: 12.944, file_cluster_17: 12.982
- **Magnitude:** 143.14 | **LOC:** 1939 | **CtrlFlow:** 70.0% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 38
- **Risk Profile:** Cognitive Load (23.8797%), Tech Debt (12.6703%)
**Top Internal Functions/Classes:**
  * `ingestDeferTriggers` (Impact: 741.1 | O(N^3) | DB: 38)
  * `ingestDeferBlock` (Impact: 104.5 | O(N^2) | DB: 5)
  * `ingestNodes` (Impact: 46.6 | O(N^1))
  * `ingestHostBinding` (Impact: 45.8 | O(N^2) | DB: 1)
  * `ingestBoundText` (Impact: 42.5 | O(N^2) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 282`, `structural_boundaries: 121`, `args: 122`, `func_start: 104`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 200`, `planned_debt: 14`
* *Architecture:* `api: 11`, `import: 15`
* *Defense:* `safety: 75`, `doc: 38`, `immutability_locks: 91`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.122
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` i18n_ast, binding_parser, api, constant_pool, ast, conversion, parse_util, tags...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/compiler/src/expression_parser/parser.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.763 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.923 IQR)
- **Top Global Matches:** file_cluster_8: 13.763, file_cluster_13: 13.927, file_cluster_7: 13.976
- **Magnitude:** 135.46 | **LOC:** 1951 | **CtrlFlow:** 64.8% | **Authorship Centralization:** 58.8%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 29
- **Risk Profile:** Cognitive Load (41.1519%), Tech Debt (39.8705%)
**Top Internal Functions/Classes:**
  * `parseCallChain` (Impact: 70.7 | O(N^3) | DB: 22)
  * `parseTemplateBindings` (Impact: 57.0 | O(N^2) | DB: 27)
  * `parsePrefix` (Impact: 53.6 | O(2^N) | DB: 29)
    * *Intent:* /** * Generator used to iterate over the character indexes of a string that are outside of quotes. *...
  * `parseAccessMember` (Impact: 41.8 | O(N^2) | DB: 29)
    * *Intent:* /**
  * `parsePrimary` (Impact: 40.0 | O(N^3) | DB: 21)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 158`, `structural_boundaries: 86`, `args: 47`, `func_start: 43`, `class_start: 6`
* *Risk/State:* `state_mutation: 770`, `duplicate_logic: 6`
* *Architecture:* `api: 16`, `import: 5`
* *Defense:* `safety: 6`, `doc: 30`, `immutability_locks: 85`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` lexer, ast, chars, parse_util, tokens
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zone.js/tools.bzl` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.284 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.309 IQR)
- **Top Global Matches:** file_cluster_8: 7.284, file_cluster_7: 7.982, file_cluster_1: 8.28
- **Magnitude:** 131.16 | **LOC:** 197 | **CtrlFlow:** 63.2% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (5.6167%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ts_project` (Impact: 118.6 | O(N^5) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 7`, `args: 7`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 2`
* *Architecture:* `api: 7`
* *Defense:* `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/animations/browser/src/render/transition_animation_engine.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.088 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 5.277 IQR)
- **Top Global Matches:** file_cluster_17: 13.088, file_cluster_13: 13.19, file_cluster_11: 13.297
- **Magnitude:** 116.84 | **LOC:** 1944 | **CtrlFlow:** 58.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (72.963%), Tech Debt (97.2726%)
**Top Internal Functions/Classes:**
  * `insertNode` (Impact: 55.5 | O(2^N) | DB: 5)
  * `removeNode` (Impact: 54.8 | O(N^3) | DB: 8)
  * `removeNode` (Impact: 48.9 | O(2^N) | DB: 4)
  * `trigger` (Impact: 46.0 | O(2^N) | DB: 11)
  * `triggerLeaveAnimation` (Impact: 40.8 | O(N^3) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 148`, `structural_boundaries: 106`, `args: 102`, `func_start: 65`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 92`, `state_mutation: 456`, `dead_code: 4`, `duplicate_logic: 19`
* *Architecture:* `api: 31`, `import: 12`
* *Defense:* `safety: 7`, `doc: 2`, `immutability_locks: 96`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.145
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` animation_style_normalizer, animation_driver, shared, core, animation_transition_factory, animations, element_instruction_map, animation_trigger...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/compiler-cli/src/ngtsc/typecheck/src/checker.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.935 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.984 IQR)
- **Top Global Matches:** file_cluster_13: 12.935, file_cluster_8: 13.058, file_cluster_17: 13.111
- **Magnitude:** 112.65 | **LOC:** 1911 | **CtrlFlow:** 54.5% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (65.1668%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getDirectiveScopeData` (Impact: 182.8 | O(N^3) | DB: 17)
  * `getTemplateDirectiveInScope` (Impact: 46.1 | O(N^2) | DB: 8)
    * *Intent:* // Don't resolve pipes for selectorless components since they're already in the file.
  * `getPotentialPipes` (Impact: 40.3 | O(N^2) | DB: 8)
  * `getDiagnosticsForFile` (Impact: 33.4 | O(N^3) | DB: 9)
  * `maybeAdoptPriorResults` (Impact: 32.7 | O(N^2) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 177`, `structural_boundaries: 148`, `args: 79`, `func_start: 56`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 429`
* *Architecture:* `io: 4`, `api: 16`, `import: 24`
* *Defense:* `safety: 34`, `doc: 12`, `immutability_locks: 149`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` scope, file_system, shims, context, diagnostics, a, source, completion...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/language-service/src/completions.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.874 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.191 IQR)
- **Top Global Matches:** file_cluster_8: 12.874, file_cluster_13: 12.964, file_cluster_7: 13.201
- **Magnitude:** 104.91 | **LOC:** 1555 | **CtrlFlow:** 61.1% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(N^3) | **DB Complexity:** 27
- **Risk Profile:** Cognitive Load (50.9811%), Tech Debt (8.1027%)
**Top Internal Functions/Classes:**
  * `getElementTagCompletion` (Impact: 247.7 | O(N^3) | DB: 27)
  * `getPropertyExpressionCompletion` (Impact: 79.2 | O(N^3) | DB: 19)
  * `getCompletionsAtPosition` (Impact: 45.4 | O(N^2) | DB: 16)
    * *Intent:* /** * Cache the symbol info from the completion entry details. This will be replaced when invoking *...
  * `getPropertyExpressionCompletionDetails` (Impact: 33.8 | O(N^2) | DB: 10)
  * `getBlockCompletions` (Impact: 27.6 | O(N^2) | DB: 2)
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 160`, `structural_boundaries: 102`, `args: 31`, `func_start: 28`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 430`, `planned_debt: 1`
* *Architecture:* `api: 6`, `import: 9`
* *Defense:* `safety: 13`, `doc: 20`, `immutability_locks: 54`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` display_parts, api, typescript, compiler, core, template_target, attribute_completions, ts_utils...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/core/testing/src/test_bed_compiler.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.873 IQR)
- **Local Micro-Species:** `Cluster 2: Type Definitions & Bypasses` (Drift: 6.008 IQR)
- **Top Global Matches:** file_cluster_4: 13.873, file_cluster_17: 13.936, file_cluster_13: 14.098
- **Magnitude:** 101.73 | **LOC:** 1228 | **CtrlFlow:** 51.5% | **Authorship Centralization:** 60.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 23
- **Risk Profile:** Cognitive Load (43.9747%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `applyProviderOverridesInScope` (Impact: 118.2 | O(2^N) | DB: 23)
  * `queueTypesFromModulesArray` (Impact: 74.5 | O(N^3) | DB: 5)
  * `configureTestingModule` (Impact: 58.8 | O(2^N) | DB: 14)
  * `collectModulesAffectedByOverrides` (Impact: 37.6 | O(N^3) | DB: 19)
  * `verifyNoStandaloneFlagOverrides` (Impact: 24.8 | O(N^2))
    * *Intent:* // At this point, the module has a valid module def (ɵmod), but the override may have introduced
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 124`, `structural_boundaries: 117`, `args: 78`, `func_start: 74`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 65`, `state_mutation: 354`, `dead_code: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 5`, `api: 20`, `concurrency: 85`, `import: 7`
* *Defense:* `safety: 45`, `doc: 3`, `immutability_locks: 58`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.197
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` test_bed_common, compiler, metadata_override, resolvers, core, application_error_handler, render3
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `integration/trusted-types/src/app/app.component.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.487 IQR)
- **Top Global Matches:** file_cluster_8: 8.487, file_cluster_0: 9.191, file_cluster_2: 9.326
- **Magnitude:** 99.38 | **LOC:** 909 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0295%), Tech Debt (15.1532%)
**Top Internal Functions/Classes:**
  * `media` (Impact: 5.0 | O(N^1))
    * *Intent:* /* Responsive Styles */
  * `media` (Impact: 2.3 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 37`, `args: 59`, `func_start: 2`, `class_start: 56`
* *Risk/State:* `duplicate_logic: 2`
* *Architecture:* `io: 28`, `api: 76`
* *Defense:* `safety: 11`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zone.js/example/profiling.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.54 IQR)
- **Top Global Matches:** file_cluster_8: 10.54, file_cluster_4: 10.728, file_cluster_7: 11.13
- **Magnitude:** 97.38 | **LOC:** 118 | **CtrlFlow:** 36.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (90.3275%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `asyncBogosort` (Impact: 21.4 | O(2^N) | DB: 2)
    * *Intent:* /* * This is a really efficient algorithm. * * First, check if the array is sorted. * - If it is, ca...
  * `isSorted` (Impact: 10.8 | O(N^3) | DB: 1)
  * `time` (Impact: 7.1 | O(2^N))
  * `onInvokeTask` (Impact: 5.5 | O(N^3) | DB: 2)
  * `reset` (Impact: 3.6 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 14`, `args: 12`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 21`, `orphaned_logic: 1`
* *Architecture:* `io: 1`, `api: 1`, `concurrency: 19`, `import: 1`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` style.css, zone.js, long-stack-trace-zone.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/compiler/src/expression_parser/lexer.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.652 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.137 IQR)
- **Top Global Matches:** file_cluster_8: 13.652, file_cluster_13: 13.847, file_cluster_7: 13.918
- **Magnitude:** 95.42 | **LOC:** 792 | **CtrlFlow:** 44.7% | **Authorship Centralization:** 71.4%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 46
- **Risk Profile:** Cognitive Load (71.722%), Tech Debt (35.8509%)
**Top Internal Functions/Classes:**
  * `scanToken` (Impact: 223.5 | O(2^N) | DB: 46)
  * `toString` (Impact: 56.1 | O(2^N) | DB: 3)
  * `scanNumber` (Impact: 31.4 | O(N^2) | DB: 9)
  * `scanComplexOperator` (Impact: 18.0 | O(N^1) | DB: 7)
  * `scanEquals` (Impact: 10.8 | O(N^1) | DB: 10)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 96`, `structural_boundaries: 119`, `args: 52`, `func_start: 52`, `class_start: 6`
* *Risk/State:* `state_mutation: 448`, `duplicate_logic: 3`
* *Architecture:* `api: 38`, `import: 1`
* *Defense:* `safety: 5`, `doc: 9`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` chars
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration/cli-hello-world-lazy/src/app/app.component.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.552 IQR)
- **Top Global Matches:** file_cluster_8: 8.552, file_cluster_0: 9.258, file_cluster_2: 9.392
- **Magnitude:** 92.04 | **LOC:** 889 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0359%), Tech Debt (15.3703%)
**Top Internal Functions/Classes:**
  * `media` (Impact: 5.0 | O(N^1))
    * *Intent:* /* Responsive Styles */
  * `media` (Impact: 2.3 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 31`, `args: 58`, `func_start: 2`, `class_start: 56`
* *Risk/State:* `duplicate_logic: 2`
* *Architecture:* `io: 24`, `api: 69`
* *Defense:* `safety: 11`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration/cli-hello-world/src/app/app.component.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.553 IQR)
- **Top Global Matches:** file_cluster_8: 8.553, file_cluster_0: 9.259, file_cluster_2: 9.393
- **Magnitude:** 92.02 | **LOC:** 887 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0363%), Tech Debt (15.3835%)
**Top Internal Functions/Classes:**
  * `media` (Impact: 5.0 | O(N^1))
    * *Intent:* /* Responsive Styles */
  * `media` (Impact: 2.3 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 31`, `args: 59`, `func_start: 2`, `class_start: 55`
* *Risk/State:* `duplicate_logic: 2`
* *Architecture:* `io: 24`, `api: 69`
* *Defense:* `safety: 11`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/core/src/render3/instructions/shared.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.302 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 5.046 IQR)
- **Top Global Matches:** file_cluster_13: 12.302, file_cluster_0: 12.58, file_cluster_8: 12.6
- **Magnitude:** 91.67 | **LOC:** 826 | **CtrlFlow:** 58.7% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(N^4) | **DB Complexity:** 21
- **Risk Profile:** Cognitive Load (11.9029%), Tech Debt (8.1985%)
**Top Internal Functions/Classes:**
  * `locateHostElement` (Impact: 773.9 | O(N^4) | DB: 21)
  * `executeTemplate` (Impact: 22.7 | O(N^1))
  * `saveResolvedLocalsInData` (Impact: 18.9 | O(N^3) | DB: 2)
    * *Intent:* /** * Creates directive instances. */
  * `createDirectivesInstances` (Impact: 4.3 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 132`, `structural_boundaries: 93`, `args: 64`, `func_start: 65`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 61`, `planned_debt: 1`
* *Architecture:* `api: 24`, `import: 38`
* *Defense:* `safety: 46`, `doc: 43`, `immutability_locks: 62`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` error_handler, sanitization, renderer, di, construction, assert, node_assert, type_checks...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/compiler-cli/src/ngtsc/transform/src/compilation.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.857 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 5.612 IQR)
- **Top Global Matches:** file_cluster_13: 13.857, file_cluster_4: 13.927, file_cluster_17: 13.962
- **Magnitude:** 88.57 | **LOC:** 815 | **CtrlFlow:** 71.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 57
- **Risk Profile:** Cognitive Load (80.7646%), Tech Debt (19.0749%)
**Top Internal Functions/Classes:**
  * `detectTraits` (Impact: 492.4 | O(N^3) | DB: 57)
  * `adopt` (Impact: 28.8 | O(N^2) | DB: 11)
  * `visit` (Impact: 20.4 | O(2^N) | DB: 2)
  * `getAnalyzedRecords` (Impact: 9.2 | O(N^2) | DB: 6)
  * `constructor` (Impact: 9.1 | O(N^1) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 140`, `structural_boundaries: 56`, `args: 34`, `func_start: 28`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 253`, `dead_code: 2`, `duplicate_logic: 2`
* *Architecture:* `api: 7`, `concurrency: 31`, `import: 15`
* *Defense:* `safety: 53`, `doc: 12`, `immutability_locks: 49`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` api, typescript, compiler, indexer, xi18n, api, declaration, trait...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `devtools/cypress/integration/node-selection.e2e.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.043 IQR)
- **Local Micro-Species:** `Cluster 1: Async Testing & I/O Mocks` (Drift: 5.822 IQR)
- **Top Global Matches:** file_cluster_8: 9.043, file_cluster_17: 9.757, file_cluster_1: 9.805
- **Magnitude:** 86.24 | **LOC:** 156 | **CtrlFlow:** 14.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (17.6326%), Tech Debt (86.1846%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 69.7 | O(2^N))
    * *Intent:* /** * @license
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 29`, `args: 27`, `func_start: 22`
* *Risk/State:* `safety_bypasses: 1`, `planned_debt: 10`
* *Architecture:* `concurrency: 14`
* *Defense:* `doc: 1`, `test: 40`, `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zone.js/example/benchmarks/addEventListener.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.124 IQR)
- **Top Global Matches:** file_cluster_8: 12.124, file_cluster_13: 12.22, file_cluster_15: 12.325
- **Magnitude:** 84.44 | **LOC:** 64 | **CtrlFlow:** 34.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (67.5087%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `addRemoveCallback` (Impact: 39.3 | O(N^3) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 21`, `args: 7`, `func_start: 1`
* *Risk/State:* `state_mutation: 39`
* *Architecture:* `io: 1`, `api: 5`, `import: 1`
* *Defense:* `doc: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` zone.js, style.css
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `packages/service-worker/worker/testing/utils.ts` (TYPESCRIPT) | Magnitude: 1.56 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 10, doc: 8, io: 6
- `packages/common/src/directives/ng_template_outlet.ts` (TYPESCRIPT) | Magnitude: 3.0 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 30, state_mutation: 15, structural_boundaries: 8, doc: 5
- `packages/examples/forms/ts/simpleFormGroup/simple_form_group_example.ts` (TYPESCRIPT) | Magnitude: 1.28 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 6, decorators: 4, args: 3
- `adev/src/content/examples/attribute-directives/src/app/highlight.directive.1.ts` (TYPESCRIPT) | Magnitude: 0.38 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 5, structural_boundaries: 3, decorators: 2, args: 1
- `integration/cli-hello-world-ivy-i18n/src/app/app.component.ts` (TYPESCRIPT) | Magnitude: 0.47 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 6, structural_boundaries: 3, api: 3, decorators: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `devtools/projects/ng-devtools/src/lib/devtools-tabs/directive-explorer/directive-forest/breadcrumbs/breadcrumbs.component.html` (HTML) | Magnitude: 15.6 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 22, decorators: 6, events: 6, args: 4
- `devtools/projects/ng-devtools/src/lib/devtools-tabs/profiler/recording-timeline/recording-visualizer/bargraph-visualizer/bargraph-visualizer.component.html` (HTML) | Magnitude: 10.52 | Delta: **0.171 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: class_start: 1, events: 1
- `packages/common/src/directives/ng_optimized_image/error_helper.ts` (TYPESCRIPT) | Magnitude: 0.59 | Delta: **0.172 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 4, structural_boundaries: 2, api: 2, branch: 1
- `packages/core/src/render3/util/misc_utils.ts` (TYPESCRIPT) | Magnitude: 1.41 | Delta: **0.227 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 12, indent_spaces: 8, api: 6, doc: 6
- `devtools/cypress/plugins/index.js` (JAVASCRIPT) | Magnitude: 3.94 | Delta: **0.362 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: doc: 3, api: 2, structural_boundaries: 1, args: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `packages/elements/src/create-custom-element.ts` (TYPESCRIPT) | Magnitude: 13.14 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 91, state_mutation: 57, structural_boundaries: 26, doc: 21
- `devtools/src/iframe-message-bus.ts` (TYPESCRIPT) | Magnitude: 6.97 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 53, state_mutation: 20, structural_boundaries: 18, branch: 9
- `packages/animations/browser/src/render/renderer.ts` (TYPESCRIPT) | Magnitude: 29.23 | Delta: **0.054 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 163, state_mutation: 129, structural_boundaries: 45, args: 35
- `packages/core/src/util/decorators.ts` (TYPESCRIPT) | Magnitude: 12.88 | Delta: **0.084 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 114, safety_bypasses: 49, structural_boundaries: 43, branch: 31
- `devtools/src/app/demo-app/todo/home/todos.component.ts` (TYPESCRIPT) | Magnitude: 8.45 | Delta: **0.112 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 104, structural_boundaries: 29, state_mutation: 29, planned_debt: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `.agent/skills/pr_review/scripts/get_pr_comments.sh` (SHELL) | Magnitude: 1.59 | Delta: **0.104 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 8, state_mutation: 6, io: 5, branch: 4
- `.agent/skills/pr_review/scripts/submit_pr_review.sh` (SHELL) | Magnitude: 3.95 | Delta: **0.107 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 24, indent_spaces: 12, io: 8, branch: 7
- `.agent/skills/pr_review/scripts/post_inline_comment.sh` (SHELL) | Magnitude: 3.42 | Delta: **0.114 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 18, io: 12, branch: 8, reflection_metaprogramming: 7
- `packages/core/src/testability/testability.externs.js` (JAVASCRIPT) | Magnitude: 7.68 | Delta: **0.18 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 14, args: 4, func_start: 4, closures: 3
- `scripts/ci/publish-snapshot-build-artifacts.sh` (SHELL) | Magnitude: 16.39 | Delta: **0.242 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 107, state_mutation: 71, reflection_metaprogramming: 51, branch: 43

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `adev/src/content/examples/signal-forms/src/login-validation-complete/app/app.ts` (TYPESCRIPT) | Magnitude: 2.07 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 7, args: 6, func_start: 6
- `packages/router/src/create_url_tree.ts` (TYPESCRIPT) | Magnitude: 39.24 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 250, branch: 94, structural_boundaries: 51, state_mutation: 45
- `adev/src/content/examples/animations/src/app/toggle-animations-page.ts` (TYPESCRIPT) | Magnitude: 1.63 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 4, decorators: 2, import: 2
- `packages/compiler-cli/src/ngtsc/transform/jit/src/initializer_api_transforms/transform_api.ts` (TYPESCRIPT) | Magnitude: 1.4 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 25, structural_boundaries: 11, api: 5, doc: 4
- `modules/benchmarks/src/expanding_rows/expanding_row_host.ts` (TYPESCRIPT) | Magnitude: 25.61 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 172, state_mutation: 130, branch: 32, doc: 32

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `tools/symbol-extractor/symbol_extractor_spec/simple.js` (JAVASCRIPT) | Magnitude: 0.0 | Delta: **0.058 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: args: 3, closures: 3, func_start: 2, indent_spaces: 2
- `tools/symbol-extractor/symbol_extractor_spec/iife_arrow_function.js` (JAVASCRIPT) | Magnitude: 0.0 | Delta: **0.079 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: args: 3, closures: 3, structural_boundaries: 2, func_start: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `packages/core/src/di/injector_compatibility.ts` (TYPESCRIPT) | Magnitude: 10.59 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 69, structural_boundaries: 57, doc: 41, generics: 27
- `packages/compiler-cli/src/ngtsc/imports/src/patch_alias_reference_resolution.ts` (TYPESCRIPT) | Magnitude: 3.62 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 36, structural_boundaries: 17, branch: 10, args: 10
- `packages/core/rxjs-interop/src/rx_resource.ts` (TYPESCRIPT) | Magnitude: 12.91 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 57, structural_boundaries: 18, generics: 16, concurrency: 15
- `devtools/projects/ng-devtools-backend/src/lib/hooks/profiler/shared.ts` (TYPESCRIPT) | Magnitude: 13.38 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 180, structural_boundaries: 36, state_mutation: 34, safety: 27
- `devtools/src/app/demo-app/todo/home/todos.service.ts` (TYPESCRIPT) | Magnitude: 1.18 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 12, planned_debt: 9, generics: 5, args: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `packages/zone.js/check-file-size.js` (JAVASCRIPT) | Magnitude: 22.72 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 18, io: 6, branch: 4, structural_boundaries: 3
- `packages/core/schematics/ng-generate/cleanup-unused-imports/unused_imports_migration.ts` (TYPESCRIPT) | Magnitude: 28.66 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 158, state_mutation: 49, branch: 47, structural_boundaries: 29
- `devtools/projects/ng-devtools-backend/src/lib/hooks/profiler/polyfill.ts` (TYPESCRIPT) | Magnitude: 15.55 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 113, structural_boundaries: 26, state_mutation: 25, immutability_locks: 21
- `packages/core/schematics/ng-generate/control-flow-migration/types.ts` (TYPESCRIPT) | Magnitude: 69.58 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 367, state_mutation: 281, structural_boundaries: 90, branch: 74
- `packages/upgrade/src/common/src/upgrade_helper.ts` (TYPESCRIPT) | Magnitude: 36.33 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 230, state_mutation: 82, branch: 71, structural_boundaries: 52

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `devtools/projects/ng-devtools/src/lib/shared/icon/icon.component.ts` (TYPESCRIPT) | Magnitude: 1.73 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 6, api: 2, ui_framework: 2
- `packages/compiler-cli/linker/src/file_linker/partial_linkers/partial_directive_linker_1.ts` (TYPESCRIPT) | Magnitude: 14.61 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 205, structural_boundaries: 41, branch: 39, ui_framework: 21
- `adev/src/content/examples/animations/src/app/animations-package/open-close.html` (HTML) | Magnitude: 13.12 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 3, indent_spaces: 2, ui_framework: 1, decorators: 1
- `adev/src/content/examples/animations/src/app/open-close.1.html` (HTML) | Magnitude: 13.12 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 3, indent_spaces: 2, ui_framework: 1, decorators: 1
- `adev/src/content/examples/animations/src/app/open-close.2.html` (HTML) | Magnitude: 13.12 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 3, indent_spaces: 2, ui_framework: 1, decorators: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `scripts/benchmarks/index.mts` (TYPESCRIPT) | Magnitude: 5.7 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 87, structural_boundaries: 36, concurrency: 26, args: 15
- `adev/src/app/editor/node-runtime-sandbox.service.spec.ts` (TYPESCRIPT) | Magnitude: 6.86 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 193, structural_boundaries: 53, args: 47, func_start: 47
- `devtools/cypress/support/commands.js` (JAVASCRIPT) | Magnitude: 11.28 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 7, concurrency: 5, args: 4
- `adev/src/content/examples/aria/multiselect/src/basic/app/app.ts` (TYPESCRIPT) | Magnitude: 3.84 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 41, structural_boundaries: 15, state_mutation: 12, concurrency: 12
- `adev/src/content/examples/aria/multiselect/src/basic/material/app/app.ts` (TYPESCRIPT) | Magnitude: 3.84 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 41, structural_boundaries: 15, state_mutation: 12, concurrency: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `packages/core/src/render/api.ts` (TYPESCRIPT) | Magnitude: 3.79 | Delta: **0.069 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 75, indent_spaces: 42, safety_bypasses: 27, args: 24
- `packages/core/primitives/signals/src/weak_ref.ts` (TYPESCRIPT) | Magnitude: 0.41 | Delta: **0.337 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: api: 2, structural_boundaries: 1, args: 1, func_start: 1
- `adev/src/app/features/home/home.component.spec.ts` (TYPESCRIPT) | Magnitude: 1.62 | Delta: **0.361 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: dead_code: 3, indent_spaces: 3, args: 1, func_start: 1
- `packages/system.d.ts` (TYPESCRIPT) | Magnitude: 1.15 | Delta: **0.392 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: structural_boundaries: 2, doc: 2, safety_bypasses: 1, state_mutation: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `packages/localize/src/utils/src/constants.ts` (TYPESCRIPT) | Magnitude: 1.46 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 4, structural_boundaries: 3, api: 3, immutability_locks: 3
- `packages/core/src/core.externs.js` (JAVASCRIPT) | Magnitude: 11.52 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 2, structural_boundaries: 1, state_mutation: 1
- `packages/common/locales/generate-locales-tool/bin/base-locale.ts` (TYPESCRIPT) | Magnitude: 1.15 | Delta: **0.059 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 2, structural_boundaries: 1, api: 1, immutability_locks: 1
- `packages/common/src/directives/ng_optimized_image/image_loaders/constants.ts` (TYPESCRIPT) | Magnitude: 1.15 | Delta: **0.059 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 2, structural_boundaries: 1, api: 1, immutability_locks: 1
- `packages/core/primitives/event-dispatch/src/event_contract_defines.ts` (TYPESCRIPT) | Magnitude: 1.15 | Delta: **0.059 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 2, structural_boundaries: 1, api: 1, immutability_locks: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `packages/benchpress/src/validator.ts` (TYPESCRIPT) | Magnitude: 0.66 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 6, doc: 4, structural_boundaries: 3, api: 3
- `packages/examples/common/pipes/ts/titlecase_pipe.ts` (TYPESCRIPT) | Magnitude: 1.64 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 16, safety: 7, structural_boundaries: 4, decorators: 3
- `modules/playground/src/animate/app/animate-app.ts` (TYPESCRIPT) | Magnitude: 7.01 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 91, state_mutation: 42, func_start: 28, args: 22
- `packages/compiler-cli/src/ngtsc/transform/jit/src/initializer_api_transforms/transform.ts` (TYPESCRIPT) | Magnitude: 8.76 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 85, structural_boundaries: 30, branch: 13, import: 11
- `integration/platform-server-hydration/copy-event-dispatch-contract.mjs` (JAVASCRIPT) | Magnitude: 14.68 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_1`
  * Top Architectural Signatures: decorators: 2, indent_spaces: 2, structural_boundaries: 1, func_start: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `adev/src/content/examples/forms/src/assets/forms.css` (CSS) | Magnitude: 0.66 | Delta: **0.074 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: class_start: 3, dead_code: 2, indent_spaces: 2, branch: 1
- `integration/cli-hello-world-ivy-i18n/src/environments/environment.ts` (TYPESCRIPT) | Magnitude: 1.26 | Delta: **0.094 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: structural_boundaries: 1, api: 1, dead_code: 1, immutability_locks: 1
- `adev/src/content/examples/form-validation/src/app/template/actor-form-template.component.css` (CSS) | Magnitude: 0.58 | Delta: **0.105 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: class_start: 1, dead_code: 1, indent_spaces: 1
- `adev/src/content/examples/animations/src/app/animations.css` (CSS) | Magnitude: 0.16 | Delta: **0.112 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 23, dead_code: 8, class_start: 7, thread_sleeps: 2

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `packages/forms/signals/src/field/node.ts` -> Churn: **60.6%** | Cog Load: 51.332% | Debt: 9.9379%
- `packages/core/src/render3/instructions/control.ts` -> Churn: **54.69%** | Cog Load: 67.4528% | Debt: 8.849%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `packages/common/http/src/client.ts` -> **SkyZeroZx** (100.0% isolated ownership) | Magnitude: 289.42
- `packages/zone.js/example/profiling.html` -> **Matthieu Riegler** (100.0% isolated ownership) | Magnitude: 97.38
- `packages/compiler-cli/src/ngtsc/transform/src/compilation.ts` -> **Andrew Scott** (100.0% isolated ownership) | Magnitude: 88.57
- `devtools/cypress/integration/node-selection.e2e.js` -> **Matthieu Riegler** (100.0% isolated ownership) | Magnitude: 86.24
- `packages/zone.js/example/benchmarks/addEventListener.html` -> **Matthieu Riegler** (100.0% isolated ownership) | Magnitude: 84.44

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `packages/core/src/render3/component_ref.ts` -> **Severity: 0.02** (Bridge: 0.0002 * Flux: 99.8573%)
- `packages/core/src/render3/ng_module_ref.ts` -> **Severity: 0.017** (Bridge: 0.0002 * Flux: 71.7751%)
- `packages/router/src/router.ts` -> **Severity: 0.017** (Bridge: 0.0002 * Flux: 100.0%)
- `packages/router/src/navigation_transition.ts` -> **Severity: 0.01** (Bridge: 0.0001 * Flux: 99.9894%)
- `packages/core/src/di/provider_collection.ts` -> **Severity: 0.009** (Bridge: 0.0001 * Flux: 93.3705%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `packages/platform-browser/src/platform-browser.ts` -> **Severity: 1780.2** (Blast Radius: 17.802 * Doc Risk: 100.0%)
- `packages/platform-browser/src/dom/events/dom_events.ts` -> **Severity: 782.7** (Blast Radius: 7.827 * Doc Risk: 100.0%)
- `packages/compiler/src/chars.ts` -> **Severity: 641.0** (Blast Radius: 6.41 * Doc Risk: 100.0%)
- `packages/compiler-cli/src/ngtsc/util/src/path.ts` -> **Severity: 594.2** (Blast Radius: 6.183 * Doc Risk: 96.1022%)
- `packages/compiler/src/output/output_ast.ts` -> **Severity: 503.257** (Blast Radius: 5.808 * Doc Risk: 86.649%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
