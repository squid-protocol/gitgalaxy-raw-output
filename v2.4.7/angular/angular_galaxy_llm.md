# ARCHITECTURAL_BRIEF: angular
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_web/angular` |
| **Timestamp** | `2026-08-07T04:21:17.784382+00:00` |
| **Scan Duration** | `15.23s` |
| **Git Branch** | `main` |
| **Git Commit** | `9d76ac82290e047f1481fb38bd95233e951a77de` |
| **Git Remote** | `https://github.com/angular/angular.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 3660 malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are a Senior Technical Storyteller and Codebase Architect. GitGalaxy has translated the non-visual architecture of this repository into measurable Structural Signatures (regex-derived counts, not an AST or compiler pass). Your job is to weave those signatures into a coherent, factual narrative about how this system is built -- its architecture, design patterns, and complexity -- not to render a verdict.
> 
> **CORE DIRECTIVES:**
> 1. **Narrate the Architecture, Don't Judge the Author:** Frame every observation as a blameless description of the system's physical reality. High Risk Exposure (e.g., Cognitive Load Exposure) describes where the architecture may be drifting into fragile territory, not developer incompetence -- it is a prompt to investigate, never a verdict.
> 2. **The Physical Reality Rule:** Base your narrative strictly on the provided Structural Signatures and the numbers derived from them. Do not hallucinate meaning, and do not restate a heuristic's raw label (e.g. a 'Logic Bomb' or 'O(2^N)' flag) as a confirmed finding of malice or a guaranteed defect -- explain what the signature actually measures, weave it into the story of the file, and let the reader draw their own conclusion.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`. Tell that balance as part of the narrative, not as an isolated alarm.
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
> **Architectural Drift Z-Score:** `4.434`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 2640 | 44.4% |
| file_cluster_13 | 1816 | 30.6% |
| file_cluster_4 | 147 | 2.5% |
| file_cluster_16 | 104 | 1.8% |
| file_cluster_0 | 101 | 1.7% |
| file_cluster_17 | 37 | 0.6% |
| file_cluster_2 | 33 | 0.6% |
| file_cluster_11 | 8 | 0.1% |
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
| Cognitive Load Exposure | 0.0 | 100.0 | 14.2 | 5.2 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 27.6 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 14.2 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 7.8 | 1.1 | 0.0 |
| API Exposure | 0.0 | 18.5 | 4.2 | 4.4 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 9.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 20.2 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 0.4 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 81.9 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 46.4 | 2.2 | 0.4 | 0.0 |
| Volatility Exposure | 0.0 | 67.9 | 5.4 | 3.1 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 18.1 | 11.9 | 0.0 |
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

- `index` (@ `packages/compiler-cli/src/ngtsc/annotations/component/src/handler.ts`) -> Impact: **498.2** | LOC: 1020
- `resolve` (@ `packages/compiler-cli/src/ngtsc/annotations/component/src/handler.ts`) -> Impact: **465.2** | LOC: 942
- `describe` (@ `packages/compiler-cli/src/ngtsc/typecheck/test/type_check_block_spec.ts`) -> Impact: **404.5** | LOC: 365
- `getSemanticReference` (@ `packages/compiler-cli/src/ngtsc/annotations/component/src/handler.ts`) -> Impact: **401.6** | LOC: 733
- `ingestDeferTriggers` (@ `packages/compiler/src/template/pipeline/src/ingest.ts`) -> Impact: **387.5** | LOC: 679
- `migrateClass` (@ `packages/core/schematics/ng-generate/inject-migration/migration.ts`) -> Impact: **376.3** | LOC: 417
- `locateHostElement` (@ `packages/core/src/render3/instructions/shared.ts`) -> Impact: **325.7** | LOC: 537
- `escapeForTemplateLiteral` (@ `packages/compiler/src/output/output_ast.ts`) -> Impact: **274.4** | LOC: 748
- `detectTraits` (@ `packages/compiler-cli/src/ngtsc/transform/src/compilation.ts`) -> Impact: **256.4** | LOC: 407
- `assertValidDateFormat` (@ `packages/common/src/i18n/format_date.ts`) -> Impact: **245.2** | LOC: 384

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `__monolith__` | 19 | 5165.79 | 3.79% | 6.03% |
| `packages/core/src/render3` | 50 | 513.15 | 12.65% | 36.1% |
| `packages/compiler-cli/src/ngtsc/typecheck/test` | 14 | 488.14 | 8.57% | 0.0% |
| `packages/common/http/src` | 19 | 485.63 | 29.37% | 43.4% |
| `adev/src/app/features/update` | 5 | 473.39 | 25.56% | 21.86% |
| `packages/compiler/src/template/pipeline/src/phases` | 68 | 445.79 | 20.25% | 24.76% |
| `packages/service-worker/worker/src` | 16 | 393.08 | 40.76% | 16.71% |
| `packages/compiler/src/ml_parser` | 11 | 388.59 | 24.18% | 31.1% |
| `packages/language-service/src` | 19 | 384.03 | 30.66% | 18.86% |
| `packages/core/src/render3/instructions` | 39 | 379.6 | 8.6% | 42.08% |

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
- `packages/compiler-cli/src/ngtsc/typecheck/test/type_check_block_spec.ts` -> **0** Orphaned Functions | **207** Duplicates
- `packages/compiler/src/template/pipeline/ir/src/expression.ts` -> **0** Orphaned Functions | **178** Duplicates
- `packages/compiler-cli/src/ngtsc/indexer/test/template_spec.ts` -> **0** Orphaned Functions | **114** Duplicates
- `packages/compiler-cli/src/ngtsc/typecheck/test/type_checker__get_symbol_of_template_node_spec.ts` -> **0** Orphaned Functions | **97** Duplicates
- `packages/compiler-cli/src/ngtsc/translator/test/typescript_ast_factory_spec.ts` -> **0** Orphaned Functions | **96** Duplicates

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
156. **`.agent/skills/pr_review/scripts/determine_review_type.sh`** -> AI Confidence: **99.29%**
157. **`.agent/skills/pr_review/scripts/post_inline_comment.sh`** -> AI Confidence: **99.29%**
158. **`packages/zone.js/scripts/sauce/sauce_connect_block.sh`** -> AI Confidence: **99.29%**
159. **`devtools/projects/ng-devtools-backend/src/lib/version.ts`** -> AI Confidence: **99.29%**
160. **`devtools/projects/shell-browser/src/app/ng-validate.ts`** -> AI Confidence: **99.29%**
161. **`modules/benchmarks/src/tree/baseline/tree.ts`** -> AI Confidence: **99.29%**
162. **`packages/common/src/directives/ng_class.ts`** -> AI Confidence: **99.29%**
163. **`packages/common/src/directives/ng_component_outlet.ts`** -> AI Confidence: **99.29%**
164. **`packages/common/src/pipes/date_pipe.ts`** -> AI Confidence: **99.29%**
165. **`packages/compiler/src/template/pipeline/src/phases/assign_i18n_slot_dependencies.ts`** -> AI Confidence: **99.29%**
166. **`packages/compiler/src/template/pipeline/src/phases/attribute_extraction.ts`** -> AI Confidence: **99.29%**
167. **`packages/compiler/src/template/pipeline/src/phases/convert_i18n_bindings.ts`** -> AI Confidence: **99.29%**
168. **`packages/compiler/src/template/pipeline/src/phases/defer_resolve_targets.ts`** -> AI Confidence: **99.29%**
169. **`packages/compiler/src/template/pipeline/src/phases/i18n_text_extraction.ts`** -> AI Confidence: **99.29%**
170. **`packages/compiler/src/template/pipeline/src/phases/resolve_i18n_expression_placeholders.ts`** -> AI Confidence: **99.29%**
171. **`packages/compiler/src/template/pipeline/src/phases/wrap_icus.ts`** -> AI Confidence: **99.29%**
172. **`packages/router/src/route_injector_cleanup.ts`** -> AI Confidence: **99.29%**
173. **`packages/service-worker/config/src/glob.ts`** -> AI Confidence: **99.29%**
174. **`vscode-ng-language-service/syntaxes/src/expression.ts`** -> AI Confidence: **99.29%**
175. **`vscode-ng-language-service/syntaxes/src/template-blocks.ts`** -> AI Confidence: **99.29%**
176. **`vscode-ng-language-service/syntaxes/src/template-tag.ts`** -> AI Confidence: **99.29%**
177. **`goldens/public-api/manage.js`** -> AI Confidence: **99.29%**
178. **`karma-js.conf.js`** -> AI Confidence: **99.29%**
179. **`adev/src/app/features/references/api-reference-details-page/api-reference-details-page.component.ts`** -> AI Confidence: **99.24%**
180. **`adev/src/app/features/references/api-reference-list/api-reference-list.component.ts`** -> AI Confidence: **99.24%**
181. **`devtools/projects/ng-devtools-backend/src/lib/client-event-subscribers.ts`** -> AI Confidence: **99.24%**
182. **`devtools/projects/ng-devtools/src/lib/devtools-tabs/directive-explorer/property-pane/property-view/property-view-body/prop-actions-menu/prop-actions-menu.component.ts`** -> AI Confidence: **99.24%**
183. **`packages/animations/browser/src/dsl/animation.ts`** -> AI Confidence: **99.24%**
184. **`packages/common/src/directives/ng_optimized_image/ng_optimized_image.ts`** -> AI Confidence: **99.24%**
185. **`packages/compiler-cli/linker/src/file_linker/linker_environment.ts`** -> AI Confidence: **99.24%**
186. **`packages/compiler-cli/linker/src/file_linker/partial_linkers/partial_component_linker_1.ts`** -> AI Confidence: **99.24%**
187. **`packages/compiler-cli/src/ngtsc/annotations/common/src/evaluation.ts`** -> AI Confidence: **99.24%**
188. **`packages/compiler-cli/src/ngtsc/annotations/directive/src/handler.ts`** -> AI Confidence: **99.24%**
189. **`packages/compiler-cli/src/ngtsc/core/src/compiler.ts`** -> AI Confidence: **99.24%**
190. **`packages/compiler-cli/src/ngtsc/program.ts`** -> AI Confidence: **99.24%**
191. **`packages/compiler-cli/src/ngtsc/typecheck/extended/test/checks/nullish_coalescing_not_nullable/nullish_coalescing_not_nullable_spec.ts`** -> AI Confidence: **99.24%**
192. **`packages/compiler-cli/src/ngtsc/typecheck/src/ops/directive_constructor.ts`** -> AI Confidence: **99.24%**
193. **`packages/compiler-cli/src/ngtsc/typecheck/src/ops/inputs.ts`** -> AI Confidence: **99.24%**
194. **`packages/compiler-cli/src/ngtsc/typecheck/src/tcb_adapter.ts`** -> AI Confidence: **99.24%**
195. **`packages/compiler-cli/src/ngtsc/typecheck/test/type_check_block_spec.ts`** -> AI Confidence: **99.24%**
196. **`packages/compiler/src/i18n/i18n_html_parser.ts`** -> AI Confidence: **99.24%**
197. **`packages/compiler/src/render3/view/t2_binder.ts`** -> AI Confidence: **99.24%**
198. **`packages/compiler/src/render3/view/util.ts`** -> AI Confidence: **99.24%**
199. **`packages/core/schematics/migrations/signal-migration/src/migration.ts`** -> AI Confidence: **99.24%**
200. **`packages/core/schematics/migrations/signal-migration/src/phase_analysis.ts`** -> AI Confidence: **99.24%**
201. **`packages/core/schematics/ng-generate/inject-migration/index.ts`** -> AI Confidence: **99.24%**
202. **`packages/core/schematics/ng-generate/standalone-migration/index.ts`** -> AI Confidence: **99.24%**
203. **`packages/core/src/application/application_ref.ts`** -> AI Confidence: **99.24%**
204. **`packages/core/src/change_detection/scheduling/ng_zone_scheduling.ts`** -> AI Confidence: **99.24%**
205. **`packages/core/src/change_detection/scheduling/zoneless_scheduling_impl.ts`** -> AI Confidence: **99.24%**
206. **`packages/core/src/di/injector.ts`** -> AI Confidence: **99.24%**
207. **`packages/core/src/di/provider_collection.ts`** -> AI Confidence: **99.24%**
208. **`packages/core/src/di/r3_injector.ts`** -> AI Confidence: **99.24%**
209. **`packages/core/src/metadata/directives.ts`** -> AI Confidence: **99.24%**
210. **`packages/core/src/render3/i18n/i18n_util.ts`** -> AI Confidence: **99.24%**
211. **`packages/core/src/render3/instructions/animation.ts`** -> AI Confidence: **99.24%**
212. **`packages/core/src/render3/instructions/element_container.ts`** -> AI Confidence: **99.24%**
213. **`packages/core/src/render3/instructions/projection.ts`** -> AI Confidence: **99.24%**
214. **`packages/core/src/render3/jit/directive.ts`** -> AI Confidence: **99.24%**
215. **`packages/core/src/render3/pipe.ts`** -> AI Confidence: **99.24%**
216. **`packages/core/src/render3/queries/query.ts`** -> AI Confidence: **99.24%**
217. **`packages/core/src/render3/reactivity/after_render_effect.ts`** -> AI Confidence: **99.24%**
218. **`packages/core/src/render3/util/signal_debug.ts`** -> AI Confidence: **99.24%**
219. **`packages/core/src/render3/view/elements.ts`** -> AI Confidence: **99.24%**
220. **`packages/core/src/render3/view_ref.ts`** -> AI Confidence: **99.24%**
221. **`packages/core/src/resource/resource.ts`** -> AI Confidence: **99.24%**
222. **`packages/core/src/sanitization/sanitization.ts`** -> AI Confidence: **99.24%**
223. **`packages/forms/signals/src/api/structure.ts`** -> AI Confidence: **99.24%**
224. **`packages/forms/src/directives/reactive_directives/form_control_directive.ts`** -> AI Confidence: **99.24%**
225. **`packages/language-service/src/codefixes/fix_missing_import.ts`** -> AI Confidence: **99.24%**
226. **`packages/language-service/src/refactorings/convert_to_signal_queries/apply_query_refactoring.ts`** -> AI Confidence: **99.24%**
227. **`packages/localize/tools/src/extract/index.ts`** -> AI Confidence: **99.24%**
228. **`packages/localize/tools/test/translate/source_files/es2015_translate_plugin_spec.ts`** -> AI Confidence: **99.24%**
229. **`packages/service-worker/worker/src/driver.ts`** -> AI Confidence: **99.24%**
230. **`vscode-ng-language-service/client/src/client.ts`** -> AI Confidence: **99.24%**
231. **`vscode-ng-language-service/server/src/handlers/hover.ts`** -> AI Confidence: **99.24%**
232. **`vscode-ng-language-service/syntaxes/src/build.ts`** -> AI Confidence: **99.24%**
233. **`packages/common/http/src/xhr.ts`** -> AI Confidence: **99.23%**
234. **`packages/common/src/pipes/number_pipe.ts`** -> AI Confidence: **99.23%**
235. **`packages/compiler-cli/src/ngtsc/metadata/src/dts.ts`** -> AI Confidence: **99.23%**
236. **`packages/compiler-cli/src/ngtsc/metadata/src/util.ts`** -> AI Confidence: **99.23%**
237. **`packages/compiler-cli/src/ngtsc/typecheck/extended/test/checks/unparenthesized_nullish_coalescing/unparenthesized_nullish_coalescing_spec.ts`** -> AI Confidence: **99.23%**
238. **`packages/compiler-cli/src/ngtsc/typecheck/src/type_constructor.ts`** -> AI Confidence: **99.23%**
239. **`packages/compiler-cli/src/perform_compile.ts`** -> AI Confidence: **99.23%**
240. **`packages/compiler/src/i18n/extractor_merger.ts`** -> AI Confidence: **99.23%**
241. **`packages/compiler/src/i18n/i18n_parser.ts`** -> AI Confidence: **99.23%**
242. **`packages/compiler/src/template/pipeline/src/phases/binding_specialization.ts`** -> AI Confidence: **99.23%**
243. **`packages/compiler/src/template/pipeline/src/phases/resolve_sanitizers.ts`** -> AI Confidence: **99.23%**
244. **`packages/core/schematics/migrations/signal-migration/src/passes/6_migrate_input_declarations.ts`** -> AI Confidence: **99.23%**
245. **`packages/core/schematics/ng-generate/standalone-migration/util.ts`** -> AI Confidence: **99.23%**
246. **`packages/core/schematics/utils/tsurge/helpers/create_program.ts`** -> AI Confidence: **99.23%**
247. **`packages/core/schematics/utils/tsurge/test/output_migration.ts`** -> AI Confidence: **99.23%**
248. **`packages/core/src/application/stability_debug_impl.ts`** -> AI Confidence: **99.23%**
249. **`packages/core/src/di/contextual.ts`** -> AI Confidence: **99.23%**
250. **`packages/core/src/render3/errors.ts`** -> AI Confidence: **99.23%**
251. **`packages/core/src/render3/i18n/i18n_icu_container_visitor.ts`** -> AI Confidence: **99.23%**
252. **`packages/core/src/render3/instructions/text_interpolation.ts`** -> AI Confidence: **99.23%**
253. **`packages/core/src/render3/node_manipulation_i18n.ts`** -> AI Confidence: **99.23%**
254. **`packages/forms/signals/src/field/structure.ts`** -> AI Confidence: **99.23%**
255. **`packages/language-service/src/refactorings/convert_to_signal_input/apply_input_refactoring.ts`** -> AI Confidence: **99.23%**
256. **`packages/localize/tools/src/translate/source_files/source_file_translation_handler.ts`** -> AI Confidence: **99.23%**
257. **`packages/router/src/directives/router_link_active.ts`** -> AI Confidence: **99.23%**
258. **`packages/router/src/operators/activate_routes.ts`** -> AI Confidence: **99.23%**
259. **`packages/router/src/router_preloader.ts`** -> AI Confidence: **99.23%**
260. **`packages/router/src/router_state.ts`** -> AI Confidence: **99.23%**
261. **`packages/service-worker/worker/testing/scope.ts`** -> AI Confidence: **99.23%**
262. **`packages/compiler-cli/src/ngtsc/scope/src/standalone.ts`** -> AI Confidence: **99.22%**
263. **`packages/common/src/i18n/format_date.ts`** -> AI Confidence: **99.2%**
264. **`packages/common/src/i18n/format_number.ts`** -> AI Confidence: **99.2%**
265. **`packages/compiler-cli/src/ngtsc/metadata/src/ng_module_index.ts`** -> AI Confidence: **99.2%**
266. **`packages/compiler/src/template/pipeline/src/phases/conditionals.ts`** -> AI Confidence: **99.2%**
267. **`packages/compiler/src/template/pipeline/src/phases/next_context_merging.ts`** -> AI Confidence: **99.2%**
268. **`packages/compiler/src/template/pipeline/src/phases/propagate_i18n_blocks.ts`** -> AI Confidence: **99.2%**
269. **`packages/compiler/src/template/pipeline/src/phases/strip_nonrequired_parentheses.ts`** -> AI Confidence: **99.2%**
270. **`packages/core/schematics/migrations/signal-migration/src/batch/merge_unit_data.ts`** -> AI Confidence: **99.2%**
271. **`packages/core/schematics/migrations/signal-migration/src/utils/is_identifier_free_in_scope.ts`** -> AI Confidence: **99.2%**
272. **`packages/misc/angular-in-memory-web-api/src/interfaces.ts`** -> AI Confidence: **99.2%**
273. **`adev/src/app/editor/code-editor/code-editor.component.ts`** -> AI Confidence: **99.18%**
274. **`adev/src/app/editor/code-editor/extensions/autocomplete.ts`** -> AI Confidence: **99.18%**
275. **`adev/src/app/editor/preview/preview.component.spec.ts`** -> AI Confidence: **99.18%**
276. **`adev/src/app/features/playground/playground.component.ts`** -> AI Confidence: **99.18%**
277. **`devtools/projects/ng-devtools/src/lib/devtools-tabs/directive-explorer/directive-forest/directive-forest.component.ts`** -> AI Confidence: **99.18%**
278. **`devtools/projects/ng-devtools/src/lib/devtools-tabs/directive-explorer/property-pane/for-loop-view/for-loop-view.component.ts`** -> AI Confidence: **99.18%**
279. **`devtools/projects/ng-devtools/src/lib/devtools-tabs/directive-explorer/property-pane/property-pane.component.ts`** -> AI Confidence: **99.18%**
280. **`devtools/projects/ng-devtools/src/lib/devtools-tabs/directive-explorer/property-pane/property-view/property-view.component.ts`** -> AI Confidence: **99.18%**
281. **`devtools/projects/ng-devtools/src/lib/devtools-tabs/directive-explorer/signal-graph-pane/signal-graph-pane.component.ts`** -> AI Confidence: **99.18%**
282. **`devtools/projects/ng-devtools/src/lib/devtools-tabs/profiler/profiler.component.ts`** -> AI Confidence: **99.18%**
283. **`devtools/projects/ng-devtools/src/lib/devtools.component.ts`** -> AI Confidence: **99.18%**
284. **`packages/animations/browser/src/render/animation_engine_next.ts`** -> AI Confidence: **99.18%**
285. **`packages/benchpress/src/runner.ts`** -> AI Confidence: **99.18%**
286. **`packages/benchpress/src/sampler.ts`** -> AI Confidence: **99.18%**
287. **`packages/common/http/src/jsonp.ts`** -> AI Confidence: **99.18%**
288. **`packages/compiler-cli/src/ngtsc/annotations/common/test/diagnostics_spec.ts`** -> AI Confidence: **99.18%**
289. **`packages/compiler-cli/src/ngtsc/imports/src/emitter.ts`** -> AI Confidence: **99.18%**
290. **`packages/compiler-cli/src/ngtsc/imports/test/emitter_spec.ts`** -> AI Confidence: **99.18%**
291. **`packages/compiler-cli/src/ngtsc/indexer/test/util.ts`** -> AI Confidence: **99.18%**
292. **`packages/compiler-cli/src/ngtsc/reflection/test/ts_host_spec.ts`** -> AI Confidence: **99.18%**
293. **`packages/compiler-cli/src/ngtsc/sourcemaps/test/source_file_spec.ts`** -> AI Confidence: **99.18%**
294. **`packages/compiler-cli/src/ngtsc/typecheck/extended/test/checks/uninvoked_function_in_event_binding/uninvoked_function_in_event_binding_spec.ts`** -> AI Confidence: **99.18%**
295. **`packages/compiler-cli/src/ngtsc/typecheck/extended/test/checks/uninvoked_track_function/uninvoked_track_function.spec.ts`** -> AI Confidence: **99.18%**
296. **`packages/compiler-cli/src/ngtsc/typecheck/testing/index.ts`** -> AI Confidence: **99.18%**
297. **`packages/compiler/src/render3/view/template.ts`** -> AI Confidence: **99.18%**
298. **`packages/core/schematics/migrations/signal-migration/src/input_detection/known_inputs.ts`** -> AI Confidence: **99.18%**
299. **`packages/core/schematics/utils/tsurge/testing/run_single.ts`** -> AI Confidence: **99.18%**
300. **`packages/core/src/application/application_ngmodule_factory_compiler.ts`** -> AI Confidence: **99.18%**
301. **`packages/core/src/authoring/model/model_signal.ts`** -> AI Confidence: **99.18%**
302. **`packages/core/src/defer/dom_triggers.ts`** -> AI Confidence: **99.18%**
303. **`packages/core/src/hydration/api.ts`** -> AI Confidence: **99.18%**
304. **`packages/core/src/linker/template_ref.ts`** -> AI Confidence: **99.18%**
305. **`packages/core/src/platform/bootstrap.ts`** -> AI Confidence: **99.18%**
306. **`packages/core/src/platform/platform.ts`** -> AI Confidence: **99.18%**
307. **`packages/core/src/render3/di.ts`** -> AI Confidence: **99.18%**
308. **`packages/core/src/render3/features/ng_onchanges_feature.ts`** -> AI Confidence: **99.18%**
309. **`packages/core/src/render3/instructions/i18n.ts`** -> AI Confidence: **99.18%**
310. **`packages/core/src/render3/instructions/queries.ts`** -> AI Confidence: **99.18%**
311. **`packages/core/src/render3/instructions/text.ts`** -> AI Confidence: **99.18%**
312. **`packages/core/src/render3/instructions/two_way.ts`** -> AI Confidence: **99.18%**
313. **`packages/core/src/render3/interfaces/node.ts`** -> AI Confidence: **99.18%**
314. **`packages/core/src/render3/scope.ts`** -> AI Confidence: **99.18%**
315. **`packages/core/src/render3/util/discovery_utils.ts`** -> AI Confidence: **99.18%**
316. **`packages/core/src/render3/util/global_utils.ts`** -> AI Confidence: **99.18%**
317. **`packages/core/src/render3/view/construction.ts`** -> AI Confidence: **99.18%**
318. **`packages/core/src/render3/view/listeners.ts`** -> AI Confidence: **99.18%**
319. **`packages/forms/signals/src/api/rules/validation/standard_schema.ts`** -> AI Confidence: **99.18%**
320. **`packages/forms/signals/src/directive/control_native.ts`** -> AI Confidence: **99.18%**
321. **`packages/forms/signals/src/field/node.ts`** -> AI Confidence: **99.18%**
322. **`packages/forms/signals/src/schema/logic.ts`** -> AI Confidence: **99.18%**
323. **`packages/forms/src/directives/reactive_directives/abstract_form.directive.ts`** -> AI Confidence: **99.18%**
324. **`packages/forms/src/directives/reactive_directives/form_group_name.ts`** -> AI Confidence: **99.18%**
325. **`packages/forms/src/directives/shared.ts`** -> AI Confidence: **99.18%**
326. **`packages/language-service/src/quick_info.ts`** -> AI Confidence: **99.18%**
327. **`packages/language-service/src/refactorings/convert_to_signal_input/full_class_input_refactoring.ts`** -> AI Confidence: **99.18%**
328. **`packages/language-service/src/refactorings/convert_to_signal_queries/full_class_query_refactoring.ts`** -> AI Confidence: **99.18%**
329. **`packages/language-service/src/refactorings/convert_to_signal_queries/individual_query_refactoring.ts`** -> AI Confidence: **99.18%**
330. **`packages/localize/tools/test/extract/translation_files/xliff1_translation_serializer_spec.ts`** -> AI Confidence: **99.18%**
331. **`packages/localize/tools/test/translate/translation_files/translation_loader_spec.ts`** -> AI Confidence: **99.18%**
332. **`packages/misc/angular-in-memory-web-api/src/http-client-backend-service.ts`** -> AI Confidence: **99.18%**
333. **`packages/router/src/operators/check_guards.ts`** -> AI Confidence: **99.18%**
334. **`packages/router/src/operators/resolve_data.ts`** -> AI Confidence: **99.18%**
335. **`packages/service-worker/worker/src/app-version.ts`** -> AI Confidence: **99.18%**
336. **`vscode-ng-language-service/server/src/handlers/folding.ts`** -> AI Confidence: **99.18%**
337. **`vscode-ng-language-service/server/src/session.ts`** -> AI Confidence: **99.18%**
338. **`tools/legacy-saucelabs/build-saucelabs-test-bundle.mjs`** -> AI Confidence: **99.18%**
339. **`.agent/skills/pr_review/scripts/reply_pr_comment.sh`** -> AI Confidence: **99.17%**
340. **`.agent/skills/pr_review/scripts/submit_pr_review.sh`** -> AI Confidence: **99.17%**
341. **`scripts/test/run-saucelabs-tests.sh`** -> AI Confidence: **99.17%**
342. **`tools/saucelabs/sauce-service.sh`** -> AI Confidence: **99.17%**
343. **`adev/shared-docs/utils/analytics.utils.ts`** -> AI Confidence: **99.17%**
344. **`modules/benchmarks/src/largetable/baseline/table.ts`** -> AI Confidence: **99.17%**
345. **`packages/benchpress/src/metric/perflog_metric.ts`** -> AI Confidence: **99.17%**
346. **`packages/common/http/testing/src/request.ts`** -> AI Confidence: **99.17%**
347. **`packages/common/src/directives/ng_if.ts`** -> AI Confidence: **99.17%**
348. **`packages/compiler-cli/src/ngtsc/core/api/src/public_options.ts`** -> AI Confidence: **99.17%**
349. **`packages/compiler/src/directive_matching.ts`** -> AI Confidence: **99.17%**
350. **`packages/compiler/src/ml_parser/lexer.ts`** -> AI Confidence: **99.17%**
351. **`packages/compiler/src/template/pipeline/src/phases/generate_advance.ts`** -> AI Confidence: **99.17%**
352. **`packages/compiler/src/template/pipeline/src/phases/nonbindable.ts`** -> AI Confidence: **99.17%**
353. **`packages/compiler/src/template/pipeline/src/phases/remove_empty_bindings.ts`** -> AI Confidence: **99.17%**
354. **`packages/compiler/src/template/pipeline/src/phases/remove_unused_i18n_attrs.ts`** -> AI Confidence: **99.17%**
355. **`packages/compiler/src/template/pipeline/src/phases/resolve_contexts.ts`** -> AI Confidence: **99.17%**
356. **`packages/compiler/src/template/pipeline/src/phases/resolve_defer_deps_fns.ts`** -> AI Confidence: **99.17%**
357. **`packages/compiler/src/template/pipeline/src/phases/slot_allocation.ts`** -> AI Confidence: **99.17%**
358. **`packages/compiler/src/template/pipeline/src/phases/style_binding_specialization.ts`** -> AI Confidence: **99.17%**
359. **`packages/compiler/src/template/pipeline/src/phases/variable_optimization.ts`** -> AI Confidence: **99.17%**
360. **`packages/core/schematics/utils/tsurge/helpers/string_manipulation/cut_string_line_length.ts`** -> AI Confidence: **99.17%**
361. **`packages/core/src/render3/list_reconciliation.ts`** -> AI Confidence: **99.17%**
362. **`packages/core/src/util/comparison.ts`** -> AI Confidence: **99.17%**
363. **`packages/language-service/src/quick_info_built_ins.ts`** -> AI Confidence: **99.17%**
364. **`packages/language-service/src/utils/format.ts`** -> AI Confidence: **99.17%**
365. **`packages/localize/tools/src/extract/translation_files/icu_parsing.ts`** -> AI Confidence: **99.17%**
366. **`packages/service-worker/config/src/duration.ts`** -> AI Confidence: **99.17%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Hardcoded Payload Artifacts
- `adev/src/app/environment.ts` -> **99.9997%** Exposure
- `packages/core/src/application/application_init.ts` -> **99.9462%** Exposure
- `packages/core/src/application/application_ref.ts` -> **99.4854%** Exposure
- `packages/core/src/di/r3_injector.ts` -> **56.1377%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `36` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `4795` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `packages/core/src/application/application_ref.ts` (TYPESCRIPT) -> Cumulative Risk: **703.79**
- **Archetype:** `file_cluster_13` (Distance: 14.128 IQR)
- **Magnitude:** 27.43 | **LOC:** 857 | **CtrlFlow:** 44.0% | **Authorship Centralization:** 30.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.6676%), Secrets Risk (99.4854%)
- **Heaviest Functions:** `synchronizeOnce` (Impact: 28.4), `synchronize` (Impact: 23.8), `tickImpl` (Impact: 23.4)

### 2. `packages/compiler/src/output/output_ast.ts` (TYPESCRIPT) -> Cumulative Risk: **697.34**
- **Archetype:** `file_cluster_8` (Distance: 12.893 IQR)
- **Magnitude:** 121.41 | **LOC:** 2091 | **CtrlFlow:** 32.7% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9994%), Tech Debt (99.9947%), Safety Score (99.1427%)
- **Heaviest Functions:** `escapeForTemplateLiteral` (Impact: 274.4), `visitIfStmt` (Impact: 34.8), `constructor` (Impact: 26.0)

### 3. `adev/src/content/tutorials/playground/3-minigame/src/main.ts` (TYPESCRIPT) -> Cumulative Risk: **695.48**
- **Archetype:** `file_cluster_4` (Distance: 13.262 IQR)
- **Magnitude:** 29.7 | **LOC:** 218 | **CtrlFlow:** 53.6% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9906%)
- **Heaviest Functions:** `mouseMove` (Impact: 20.1), `powerUpAccuracy` (Impact: 18.4), `getChangingQuote` (Impact: 8.5)

### 4. `packages/router/src/apply_redirects.ts` (TYPESCRIPT) -> Cumulative Risk: **688.27**
- **Archetype:** `file_cluster_13` (Distance: 10.898 IQR)
- **Magnitude:** 12.39 | **LOC:** 207 | **CtrlFlow:** 38.6% | **Authorship Centralization:** 80.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.361%), State Flux (98.6166%), Tech Debt (87.6996%)
- **Heaviest Functions:** `lineralizeSegments` (Impact: 9.5), `createQueryParams` (Impact: 7.6), `namedOutletsRedirect` (Impact: 6.3)

### 5. `devtools/projects/shell-browser/src/app/chrome-message-bus.ts` (TYPESCRIPT) -> Cumulative Risk: **686.51**
- **Archetype:** `file_cluster_16` (Distance: 13.724 IQR)
- **Magnitude:** 8.03 | **LOC:** 87 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9881%)
- **Heaviest Functions:** `emit` (Impact: 5.8), `on` (Impact: 4.1), `once` (Impact: 3.9)

### 6. `devtools/projects/ng-devtools/src/lib/devtools-tabs/profiler/profiler.component.ts` (TYPESCRIPT) -> Cumulative Risk: **685.91**
- **Archetype:** `file_cluster_13` (Distance: 13.094 IQR)
- **Magnitude:** 12.57 | **LOC:** 129 | **CtrlFlow:** 23.3% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.998%), Cognitive Load (98.2543%)
- **Heaviest Functions:** `constructor` (Impact: 14.1), `setTimeout` (Impact: 4.7), `setTimeout` (Impact: 3.2)

### 7. `packages/router/src/router_config_loader.ts` (TYPESCRIPT) -> Cumulative Risk: **683.54**
- **Archetype:** `file_cluster_4` (Distance: 13.372 IQR)
- **Magnitude:** 26.92 | **LOC:** 192 | **CtrlFlow:** 51.5% | **Authorship Centralization:** 40.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9881%)
- **Heaviest Functions:** `loadChildren` (Impact: 24.5), `loadComponent` (Impact: 22.3), `loader` (Impact: 16.9)

### 8. `devtools/projects/ng-devtools-backend/src/lib/hooks/profiler/native.ts` (TYPESCRIPT) -> Cumulative Risk: **671.44**
- **Archetype:** `file_cluster_11` (Distance: 13.6 IQR)
- **Magnitude:** 19.58 | **LOC:** 253 | **CtrlFlow:** 17.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9996%), Tech Debt (99.9876%)
- **Heaviest Functions:** `ProfilerEvent.TemplateUpdateStart` (Impact: 12.0), `ProfilerEvent.TemplateUpdateEnd` (Impact: 7.7), `onIndexForest` (Impact: 2.6)

### 9. `packages/router/src/router_preloader.ts` (TYPESCRIPT) -> Cumulative Risk: **664.76**
- **Archetype:** `file_cluster_4` (Distance: 13.275 IQR)
- **Magnitude:** 15.91 | **LOC:** 194 | **CtrlFlow:** 46.4% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), State Flux (99.9966%), Tech Debt (99.9188%)
- **Heaviest Functions:** `processRoutes` (Impact: 38.3), `preloadConfig` (Impact: 20.7), `mergeMap` (Impact: 9.5)

### 10. `packages/core/src/change_detection/scheduling/ng_zone_scheduling.ts` (TYPESCRIPT) -> Cumulative Risk: **655.52**
- **Archetype:** `file_cluster_13` (Distance: 12.975 IQR)
- **Magnitude:** 19.52 | **LOC:** 282 | **CtrlFlow:** 45.9% | **Authorship Centralization:** 62.5%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.7583%), Safety Score (88.5431%)
- **Heaviest Functions:** `getNgZoneOptions` (Impact: 18.4), `initialize` (Impact: 16.1), `provideZoneChangeDetection` (Impact: 8.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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
- **Global Archetype:** `file_cluster_8` (Drift: 14.357 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.404 IQR)
- **Top Global Matches:** file_cluster_8: 14.357, file_cluster_0: 14.435, file_cluster_13: 14.518
- **Magnitude:** 270.82 | **LOC:** 1834 | **CtrlFlow:** 69.6% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (56.7795%), Tech Debt (76.9995%)
**Top Internal Functions/Classes:**
  * `_consumeTagOpen` (Impact: 62.9)
  * `processEscapeSequence` (Impact: 52.5)
  * `peek` (Impact: 52.4)
  * `tokenize` (Impact: 48.0)
  * `_consumeBlockParameters` (Impact: 42.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 410`, `structural_boundaries: 179`, `args: 147`, `func_start: 135`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 1591`, `duplicate_logic: 24`
* *Architecture:* `io: 2`, `api: 10`, `import: 5`
* *Defense:* `safety: 46`, `doc: 37`, `immutability_locks: 99`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` chars, entities, parse_util, tags, tokens
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/core/src/metadata/directives.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.68 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 3.83 IQR)
- **Top Global Matches:** file_cluster_0: 10.68, file_cluster_13: 11.017, file_cluster_8: 11.066
- **Magnitude:** 267.61 | **LOC:** 1094 | **CtrlFlow:** 40.5% | **Authorship Centralization:** 64.3%
- **Risk Profile:** Cognitive Load (6.0298%), Tech Debt (10.8687%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 88`, `args: 15`, `func_start: 4`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 18`, `dead_code: 1`, `planned_debt: 3`
* *Architecture:* `io: 1`, `api: 21`, `import: 10`
* *Defense:* `safety: 21`, `doc: 47`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` core, provider, type, decorators, constants, schema, pipe, view...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/compiler-cli/src/ngtsc/annotations/component/src/handler.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.863 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.905 IQR)
- **Top Global Matches:** file_cluster_13: 12.863, file_cluster_17: 13.024, file_cluster_8: 13.057
- **Magnitude:** 250.67 | **LOC:** 2643 | **CtrlFlow:** 72.1% | **Authorship Centralization:** 30.0%
- **Risk Profile:** Cognitive Load (88.42%), Tech Debt (25.8483%)
**Top Internal Functions/Classes:**
  * `index` (Impact: 498.2)
  * `resolve` (Impact: 465.2)
  * `getSemanticReference` (Impact: 401.6)
  * `handleDependencyCycles` (Impact: 155.6)
  * `compileHmrUpdateDeclaration` (Impact: 105.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 269`, `structural_boundaries: 104`, `args: 46`, `func_start: 36`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 492`, `dead_code: 3`, `duplicate_logic: 8`
* *Architecture:* `io: 5`, `api: 8`, `import: 37`
* *Defense:* `safety: 28`, `doc: 14`, `immutability_locks: 149`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` common, symbol, directive, api, util, animations, scope, selectorless...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/compiler-cli/src/ngtsc/typecheck/test/type_check_block_spec.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.16 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 5.836 IQR)
- **Top Global Matches:** file_cluster_8: 12.16, file_cluster_0: 12.338, file_cluster_11: 12.581
- **Magnitude:** 218.11 | **LOC:** 3182 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 54.2%
- **Risk Profile:** Cognitive Load (23.0718%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 404.5)
  * `describe` (Impact: 180.4)
  * `describe` (Impact: 76.0)
  * `describe` (Impact: 46.7)
  * `it` (Impact: 36.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 355`, `structural_boundaries: 532`, `args: 630`, `func_start: 577`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 119`, `state_mutation: 195`, `fragile_debt: 1`, `duplicate_logic: 207`
* *Architecture:* `api: 5`, `import: 8`
* *Defense:* `safety: 55`, `doc: 1`, `test: 573`, `immutability_locks: 338`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` core, testing, testing, file_system, compiler, typescript, api, imports
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/common/http/src/client.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.17 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.945 IQR)
- **Top Global Matches:** file_cluster_8: 11.17, file_cluster_16: 11.294, file_cluster_2: 11.413
- **Magnitude:** 175.93 | **LOC:** 5025 | **CtrlFlow:** 97.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (22.3692%), Tech Debt (99.8781%)
**Top Internal Functions/Classes:**
  * `request` (Impact: 23.3)
  * `request` (Impact: 23.3)
  * `request` (Impact: 23.3)
  * `request` (Impact: 23.3)
    * *Intent:* /** * Constructs a request which interprets the body as a text stream and returns the full * `HttpRe...
  * `post` (Impact: 22.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1401`, `structural_boundaries: 30`, `args: 85`, `func_start: 85`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 82`, `state_mutation: 16`, `duplicate_logic: 81`
* *Architecture:* `io: 1`, `api: 3`, `concurrency: 118`, `import: 10`
* *Defense:* `safety: 1`, `doc: 377`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` core, operators, rxjs, params, request, errors, context, response...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/compiler/src/template/pipeline/src/ingest.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.74 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.03 IQR)
- **Top Global Matches:** file_cluster_8: 12.74, file_cluster_13: 12.928, file_cluster_17: 12.957
- **Magnitude:** 174.75 | **LOC:** 1939 | **CtrlFlow:** 70.0% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (38.6294%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `ingestDeferTriggers` (Impact: 387.5)
  * `ingestTemplateBindings` (Impact: 136.4)
  * `createTemplateBinding` (Impact: 125.1)
  * `asMessage` (Impact: 74.8)
  * `ingestDeferBlock` (Impact: 71.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 282`, `structural_boundaries: 121`, `args: 123`, `func_start: 104`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 204`, `planned_debt: 14`, `duplicate_logic: 55`
* *Architecture:* `api: 14`, `import: 15`
* *Defense:* `safety: 75`, `doc: 38`, `immutability_locks: 91`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.122
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` api, ast, tags, conversion, output_ast, r3_ast, ir, compilation...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/service-worker/worker/src/driver.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.811 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 5.694 IQR)
- **Top Global Matches:** file_cluster_4: 13.811, file_cluster_17: 14.28, file_cluster_13: 14.603
- **Magnitude:** 141.68 | **LOC:** 1398 | **CtrlFlow:** 42.6% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (77.0992%), Tech Debt (14.974%)
**Top Internal Functions/Classes:**
  * `assignVersion` (Impact: 95.7)
  * `handleClick` (Impact: 54.6)
    * *Intent:* /** * The handler for fetch events.
  * `setupUpdate` (Impact: 34.2)
  * `onFetch` (Impact: 33.5)
    * *Intent:* /** * Determines if a given URL scope corresponds to localhost.
  * `handleFetch` (Impact: 12.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 100`, `structural_boundaries: 135`, `args: 56`, `func_start: 35`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 15`, `high_risk_execution: 1`, `state_mutation: 341`, `dead_code: 2`, `planned_debt: 2`, `fragile_debt: 2`
* *Architecture:* `io: 9`, `api: 15`, `concurrency: 684`, `import: 10`
* *Defense:* `safety: 45`, `doc: 12`, `immutability_locks: 50`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.148
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` api, database, adapter, idle, db-cache, msg, manifest, app-version...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/compiler/src/template/pipeline/ir/src/expression.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.133 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.688 IQR)
- **Top Global Matches:** file_cluster_8: 13.133, file_cluster_13: 13.198, file_cluster_11: 13.328
- **Magnitude:** 134.2 | **LOC:** 1448 | **CtrlFlow:** 51.5% | **Authorship Centralization:** 58.3%
- **Risk Profile:** Cognitive Load (69.5504%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `transformExpressionsInOp` (Impact: 238.3)
  * `transformExpressionsInExpression` (Impact: 132.1)
  * `transformExpressionsInStatement` (Impact: 28.1)
  * `transformExpressionsInStatement` (Impact: 20.6)
  * `transformExpressionsInOp` (Impact: 16.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 229`, `structural_boundaries: 216`, `args: 218`, `func_start: 212`, `class_start: 29`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 331`, `planned_debt: 3`, `duplicate_logic: 178`
* *Architecture:* `api: 62`, `import: 11`
* *Defense:* `safety: 57`, `doc: 26`, `immutability_locks: 84`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` shared, enums, util, create, traits, handle, parse_util, operations...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/compiler/src/output/output_ast.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.893 IQR)
- **Local Micro-Species:** `Cluster 2: Type Definitions & Bypasses` (Drift: 4.311 IQR)
- **Top Global Matches:** file_cluster_8: 12.893, file_cluster_13: 13.001, file_cluster_11: 13.053
- **Magnitude:** 121.41 | **LOC:** 2091 | **CtrlFlow:** 32.7% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (77.3561%), Tech Debt (99.9947%)
**Top Internal Functions/Classes:**
  * `escapeForTemplateLiteral` (Impact: 274.4)
  * `visitIfStmt` (Impact: 34.8)
  * `constructor` (Impact: 26.0)
    * *Intent:* // TODO: Should we deep clone statements?
  * `visitArrowFunctionExpr` (Impact: 25.3)
  * `constructor` (Impact: 18.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 182`, `structural_boundaries: 375`, `args: 258`, `func_start: 245`, `class_start: 45`
* *Risk/State:* `safety_bypasses: 174`, `state_mutation: 428`, `dead_code: 1`, `planned_debt: 3`, `duplicate_logic: 37`
* *Architecture:* `io: 1`, `api: 132`, `import: 4`
* *Defense:* `safety: 13`, `doc: 16`, `immutability_locks: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 5.808
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` parse_util, digest, meta, i18n_ast
  * `Imported By (In-Degree: 83):` (Excluded from Brief to save tokens)

### `packages/compiler-cli/src/ngtsc/typecheck/test/type_checker__get_symbol_of_template_node_spec.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.506 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 5.315 IQR)
- **Top Global Matches:** file_cluster_8: 10.506, file_cluster_0: 11.093, file_cluster_7: 11.114
- **Magnitude:** 121.31 | **LOC:** 2794 | **CtrlFlow:** 18.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (8.6512%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 154.8)
  * `runInEachFileSystem` (Impact: 137.6)
  * `describe` (Impact: 103.6)
  * `describe` (Impact: 49.1)
  * `describe` (Impact: 22.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 77`, `structural_boundaries: 330`, `args: 413`, `func_start: 398`, `class_start: 41`
* *Risk/State:* `safety_bypasses: 224`, `state_mutation: 64`, `duplicate_logic: 97`
* *Architecture:* `io: 2`, `api: 71`, `import: 12`
* *Defense:* `safety: 49`, `doc: 1`, `test: 258`, `immutability_locks: 433`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` core, testing, testing, file_system, compiler, tcb_util, typescript, reflection...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/compiler/src/expression_parser/parser.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.752 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.914 IQR)
- **Top Global Matches:** file_cluster_8: 13.752, file_cluster_13: 13.909, file_cluster_7: 13.96
- **Magnitude:** 119.19 | **LOC:** 1951 | **CtrlFlow:** 64.8% | **Authorship Centralization:** 58.8%
- **Risk Profile:** Cognitive Load (41.1519%), Tech Debt (39.8705%)
**Top Internal Functions/Classes:**
  * `parseTemplateBindings` (Impact: 39.6)
  * `parseCallChain` (Impact: 36.1)
  * `parseAccessMember` (Impact: 28.8)
    * *Intent:* /**
  * `parseRelational` (Impact: 23.8)
  * `parsePrimary` (Impact: 21.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 158`, `structural_boundaries: 86`, `args: 48`, `func_start: 44`, `class_start: 6`
* *Risk/State:* `state_mutation: 760`, `duplicate_logic: 6`
* *Architecture:* `api: 20`, `import: 5`
* *Defense:* `safety: 6`, `doc: 30`, `immutability_locks: 85`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ast, tokens, chars, lexer, parse_util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration/trusted-types/src/app/app.component.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.487 IQR)
- **Top Global Matches:** file_cluster_8: 8.487, file_cluster_0: 9.191, file_cluster_2: 9.326
- **Magnitude:** 99.38 | **LOC:** 909 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (5.0295%), Tech Debt (15.1532%)
**Top Internal Functions/Classes:**
  * `media` (Impact: 5.0)
    * *Intent:* /* Responsive Styles */
  * `media` (Impact: 2.3)
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

### `packages/compiler-cli/src/ngtsc/typecheck/src/checker.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.932 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.98 IQR)
- **Top Global Matches:** file_cluster_13: 12.932, file_cluster_8: 13.061, file_cluster_17: 13.112
- **Magnitude:** 98.86 | **LOC:** 1911 | **CtrlFlow:** 54.5% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (65.1668%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getDirectiveScopeData` (Impact: 97.9)
  * `getPotentialElementTags` (Impact: 43.2)
  * `getTemplateDirectiveInScope` (Impact: 31.4)
    * *Intent:* // Don't resolve pipes for selectorless components since they're already in the file.
  * `getPotentialPipes` (Impact: 27.3)
  * `maybeAdoptPriorResults` (Impact: 22.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 177`, `structural_boundaries: 148`, `args: 77`, `func_start: 56`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 429`
* *Architecture:* `io: 4`, `api: 19`, `import: 24`
* *Defense:* `safety: 34`, `doc: 12`, `immutability_locks: 149`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` shim, completion, api, perf, context, tcb_util, program_driver, template_symbol_builder...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/language-service/src/completions.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.883 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.172 IQR)
- **Top Global Matches:** file_cluster_8: 12.883, file_cluster_13: 12.956, file_cluster_7: 13.201
- **Magnitude:** 97.12 | **LOC:** 1555 | **CtrlFlow:** 61.1% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (50.9811%), Tech Debt (8.1027%)
**Top Internal Functions/Classes:**
  * `getElementTagCompletion` (Impact: 129.7)
  * `getPropertyExpressionCompletion` (Impact: 41.2)
  * `getClassPropertyNameFromDirective` (Impact: 40.3)
  * `getElementAttributeCompletionDetails` (Impact: 31.7)
  * `getCompletionsAtPosition` (Impact: 30.7)
    * *Intent:* /** * Cache the symbol info from the completion entry details. This will be replaced when invoking *...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 160`, `structural_boundaries: 102`, `args: 29`, `func_start: 28`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 430`, `planned_debt: 1`
* *Architecture:* `api: 11`, `import: 9`
* *Defense:* `safety: 13`, `doc: 20`, `immutability_locks: 54`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` core, attribute_completions, compiler, ts_utils, typescript, bar.component, template_target, utils...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/animations/browser/src/render/transition_animation_engine.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.08 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 5.271 IQR)
- **Top Global Matches:** file_cluster_17: 13.08, file_cluster_13: 13.184, file_cluster_11: 13.291
- **Magnitude:** 94.24 | **LOC:** 1944 | **CtrlFlow:** 58.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.963%), Tech Debt (99.5899%)
**Top Internal Functions/Classes:**
  * `removeNode` (Impact: 28.8)
  * `triggerLeaveAnimation` (Impact: 21.2)
  * `listen` (Impact: 20.1)
  * `insertNode` (Impact: 19.7)
  * `removeClass` (Impact: 18.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 148`, `structural_boundaries: 106`, `args: 101`, `func_start: 65`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 92`, `state_mutation: 456`, `dead_code: 4`, `duplicate_logic: 25`
* *Architecture:* `api: 31`, `import: 12`
* *Defense:* `safety: 7`, `doc: 2`, `immutability_locks: 96`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.145
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` error_helpers, core, animation_driver, animation_style_normalizer, util, animations, animation_trigger, animation_transition_factory...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/core/src/render3/instructions/shared.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.26 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 4.929 IQR)
- **Top Global Matches:** file_cluster_13: 12.26, file_cluster_0: 12.523, file_cluster_8: 12.593
- **Magnitude:** 94.24 | **LOC:** 826 | **CtrlFlow:** 58.7% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (11.9029%), Tech Debt (99.977%)
**Top Internal Functions/Classes:**
  * `locateHostElement` (Impact: 325.7)
  * `setDirectiveInput` (Impact: 59.4)
  * `findDirectiveDefMatches` (Impact: 27.9)
  * `setAllInputsForProperty` (Impact: 25.5)
  * `setNgReflectProperties` (Impact: 25.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 132`, `structural_boundaries: 93`, `args: 65`, `func_start: 65`
* *Risk/State:* `safety_bypasses: 24`, `high_risk_execution: 1`, `state_mutation: 61`, `planned_debt: 1`, `duplicate_logic: 17`
* *Architecture:* `api: 33`, `import: 38`
* *Defense:* `safety: 46`, `doc: 43`, `immutability_locks: 62`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` context_discovery, node, view, devtools, tokens, element_validation, dom_node_manipulation, utils...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/core/testing/src/test_bed_compiler.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.855 IQR)
- **Local Micro-Species:** `Cluster 2: Type Definitions & Bypasses` (Drift: 5.987 IQR)
- **Top Global Matches:** file_cluster_4: 13.855, file_cluster_17: 13.92, file_cluster_13: 14.087
- **Magnitude:** 92.54 | **LOC:** 1228 | **CtrlFlow:** 51.5% | **Authorship Centralization:** 60.0%
- **Risk Profile:** Cognitive Load (43.9747%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `queueTypesFromModulesArrayRecur` (Impact: 42.3)
  * `applyProviderOverridesInScope` (Impact: 42.2)
  * `queueTypesFromModulesArray` (Impact: 38.5)
  * `configureTestingModule` (Impact: 20.7)
  * `collectModulesAffectedByOverrides` (Impact: 19.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 124`, `structural_boundaries: 117`, `args: 79`, `func_start: 74`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 65`, `state_mutation: 352`, `dead_code: 1`, `duplicate_logic: 12`
* *Architecture:* `io: 5`, `api: 20`, `concurrency: 85`, `import: 7`
* *Defense:* `safety: 45`, `doc: 3`, `immutability_locks: 58`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.197
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` core, application_error_handler, compiler, render3, metadata_override, resolvers, test_bed_common
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `integration/cli-hello-world-lazy/src/app/app.component.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.552 IQR)
- **Top Global Matches:** file_cluster_8: 8.552, file_cluster_0: 9.258, file_cluster_2: 9.392
- **Magnitude:** 92.04 | **LOC:** 889 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (5.0359%), Tech Debt (15.3703%)
**Top Internal Functions/Classes:**
  * `media` (Impact: 5.0)
    * *Intent:* /* Responsive Styles */
  * `media` (Impact: 2.3)
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
- **Risk Profile:** Cognitive Load (5.0363%), Tech Debt (15.3835%)
**Top Internal Functions/Classes:**
  * `media` (Impact: 5.0)
    * *Intent:* /* Responsive Styles */
  * `media` (Impact: 2.3)
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

### `devtools/cypress/integration/node-selection.e2e.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.042 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 6.554 IQR)
- **Top Global Matches:** file_cluster_8: 9.042, file_cluster_17: 9.698, file_cluster_1: 9.8
- **Magnitude:** 86.24 | **LOC:** 156 | **CtrlFlow:** 14.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (17.6326%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 17.7)
    * *Intent:* /** * @license
  * `describe` (Impact: 10.8)
  * `describe` (Impact: 8.3)
    * *Intent:* /** * @license * Copyright Google LLC All Rights Reserved. * * Use of this source code is governed b...
  * `it` (Impact: 5.1)
  * `it` (Impact: 4.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 29`, `args: 27`, `func_start: 22`
* *Risk/State:* `safety_bypasses: 1`, `planned_debt: 10`, `duplicate_logic: 12`, `orphaned_logic: 1`
* *Architecture:* `concurrency: 14`
* *Defense:* `doc: 1`, `test: 40`, `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/compiler-cli/src/ngtsc/transform/src/compilation.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.817 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 5.559 IQR)
- **Top Global Matches:** file_cluster_13: 13.817, file_cluster_4: 13.881, file_cluster_17: 13.93
- **Magnitude:** 84.34 | **LOC:** 815 | **CtrlFlow:** 71.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (80.2307%), Tech Debt (66.0283%)
**Top Internal Functions/Classes:**
  * `detectTraits` (Impact: 256.4)
  * `compile` (Impact: 38.4)
  * `analyzeTrait` (Impact: 29.6)
  * `resolve` (Impact: 28.8)
  * `analyzeClass` (Impact: 22.4)
    * *Intent:* // This is at least the second handler to match this class. This is a slower path that some // class...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 140`, `structural_boundaries: 56`, `args: 34`, `func_start: 28`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 251`, `dead_code: 2`, `duplicate_logic: 6`
* *Architecture:* `api: 11`, `concurrency: 31`, `import: 15`
* *Defense:* `safety: 53`, `doc: 12`, `immutability_locks: 49`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` typescript, semantic_graph, api, api, declaration, indexer, xi18n, compiler...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zone.js/example/profiling.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.559 IQR)
- **Top Global Matches:** file_cluster_8: 10.559, file_cluster_4: 10.711, file_cluster_7: 11.146
- **Magnitude:** 83.58 | **LOC:** 118 | **CtrlFlow:** 36.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (76.9314%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `sortAndPrintArray` (Impact: 6.7)
  * `asyncBogosort` (Impact: 5.8)
    * *Intent:* /* * This is a really efficient algorithm. * * First, check if the array is sorted. * - If it is, ca...
  * `setTimeout` (Impact: 5.7)
  * `isSorted` (Impact: 5.6)
  * `cb` (Impact: 3.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 14`, `args: 12`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 21`, `duplicate_logic: 4`, `orphaned_logic: 2`
* *Architecture:* `io: 1`, `api: 1`, `concurrency: 19`, `import: 1`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.104
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` style.css, zone.js, long-stack-trace-zone.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/core/src/render3/node_manipulation.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.805 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.153 IQR)
- **Top Global Matches:** file_cluster_13: 11.805, file_cluster_8: 11.99, file_cluster_0: 12.105
- **Magnitude:** 80.31 | **LOC:** 1087 | **CtrlFlow:** 63.6% | **Authorship Centralization:** 76.2%
- **Risk Profile:** Cognitive Load (16.8694%), Tech Debt (94.5168%)
**Top Internal Functions/Classes:**
  * `detachViewFromDOM` (Impact: 223.2)
    * *Intent:* /**
  * `getClosestRElement` (Impact: 148.4)
  * `applyNodes` (Impact: 72.2)
  * `getFirstNativeNode` (Impact: 40.8)
  * `processCleanups` (Impact: 28.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 112`, `structural_boundaries: 64`, `args: 47`, `func_start: 47`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 49`, `dead_code: 1`, `fragile_debt: 1`, `duplicate_logic: 7`
* *Architecture:* `api: 18`, `import: 27`
* *Defense:* `safety: 15`, `doc: 56`, `immutability_locks: 49`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.497
  * `Choke Point (Betweenness):` 3.6e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` assert, view, node, type_checks, profiler, dom_node_manipulation, utils, devtools...
  * `Imported By (In-Degree: 18):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `modules/benchmarks/src/expanding_rows/expanding_row_host.ts` (TYPESCRIPT) | Magnitude: 25.34 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 172, state_mutation: 130, branch: 32, doc: 32
- `packages/service-worker/worker/testing/utils.ts` (TYPESCRIPT) | Magnitude: 1.56 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 10, doc: 8, io: 6
- `packages/common/src/directives/ng_template_outlet.ts` (TYPESCRIPT) | Magnitude: 3.34 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 30, state_mutation: 15, structural_boundaries: 8, doc: 5
- `packages/examples/forms/ts/simpleFormGroup/simple_form_group_example.ts` (TYPESCRIPT) | Magnitude: 0.97 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 6, decorators: 4, args: 3
- `adev/src/content/examples/attribute-directives/src/app/highlight.directive.1.ts` (TYPESCRIPT) | Magnitude: 0.38 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 5, structural_boundaries: 3, decorators: 2, args: 1

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
- `devtools/src/iframe-message-bus.ts` (TYPESCRIPT) | Magnitude: 8.04 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 53, state_mutation: 20, structural_boundaries: 18, args: 12
- `packages/animations/browser/src/render/renderer.ts` (TYPESCRIPT) | Magnitude: 28.71 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 163, state_mutation: 101, structural_boundaries: 45, args: 35
- `packages/core/src/util/decorators.ts` (TYPESCRIPT) | Magnitude: 14.99 | Delta: **0.084 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 114, safety_bypasses: 49, structural_boundaries: 43, branch: 31
- `devtools/src/app/demo-app/todo/home/todos.component.ts` (TYPESCRIPT) | Magnitude: 8.08 | Delta: **0.106 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 104, structural_boundaries: 29, state_mutation: 29, planned_debt: 18
- `packages/core/src/change_detection/differs/default_iterable_differ.ts` (TYPESCRIPT) | Magnitude: 52.32 | Delta: **0.158 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 286, state_mutation: 250, generics: 65, branch: 55

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `.agent/skills/pr_review/scripts/submit_pr_review.sh` (SHELL) | Magnitude: 4.38 | Delta: **0.097 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 24, indent_spaces: 12, branch: 10, io: 8
- `.agent/skills/pr_review/scripts/post_inline_comment.sh` (SHELL) | Magnitude: 3.84 | Delta: **0.101 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 18, io: 12, branch: 11, reflection_metaprogramming: 7
- `.agent/skills/pr_review/scripts/get_pr_comments.sh` (SHELL) | Magnitude: 1.73 | Delta: **0.113 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 8, state_mutation: 6, branch: 5, io: 5
- `packages/core/src/testability/testability.externs.js` (JAVASCRIPT) | Magnitude: 7.68 | Delta: **0.18 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 14, args: 4, func_start: 4, closures: 3
- `scripts/ci/publish-snapshot-build-artifacts.sh` (SHELL) | Magnitude: 15.76 | Delta: **0.247 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 107, state_mutation: 71, reflection_metaprogramming: 51, branch: 48

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `packages/router/src/create_url_tree.ts` (TYPESCRIPT) | Magnitude: 30.19 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 250, branch: 94, structural_boundaries: 51, state_mutation: 45
- `adev/src/content/examples/animations/src/app/toggle-animations-page.ts` (TYPESCRIPT) | Magnitude: 1.63 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 4, decorators: 2, import: 2
- `packages/compiler-cli/src/ngtsc/typecheck/extended/api/api.ts` (TYPESCRIPT) | Magnitude: 8.92 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 93, structural_boundaries: 29, state_mutation: 24, generics: 20
- `packages/compiler-cli/src/ngtsc/transform/jit/src/initializer_api_transforms/transform_api.ts` (TYPESCRIPT) | Magnitude: 1.4 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 25, structural_boundaries: 11, api: 5, doc: 4
- `packages/compiler/src/template/pipeline/src/phases/nonbindable.ts` (TYPESCRIPT) | Magnitude: 3.96 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 32, branch: 13, immutability_locks: 6, structural_boundaries: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `tools/symbol-extractor/symbol_extractor_spec/simple.js` (JAVASCRIPT) | Magnitude: 0.0 | Delta: **0.058 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: args: 3, closures: 3, func_start: 2, indent_spaces: 2
- `tools/symbol-extractor/symbol_extractor_spec/iife_arrow_function.js` (JAVASCRIPT) | Magnitude: 0.0 | Delta: **0.079 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: args: 3, closures: 3, structural_boundaries: 2, func_start: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `packages/core/src/di/injector_compatibility.ts` (TYPESCRIPT) | Magnitude: 9.64 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 69, structural_boundaries: 57, doc: 41, api: 27
- `devtools/projects/shell-browser/src/app/chrome-message-bus.ts` (TYPESCRIPT) | Magnitude: 8.03 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 59, state_mutation: 34, structural_boundaries: 25, generics: 19
- `devtools/projects/ng-devtools-backend/src/lib/hooks/profiler/shared.ts` (TYPESCRIPT) | Magnitude: 13.21 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 180, structural_boundaries: 36, state_mutation: 34, safety: 27
- `devtools/src/app/demo-app/todo/home/todos.service.ts` (TYPESCRIPT) | Magnitude: 1.18 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 12, planned_debt: 9, generics: 5, args: 4
- `packages/core/schematics/migrations/signal-migration/src/flow_analysis/flow_node_internals.ts` (TYPESCRIPT) | Magnitude: 1.37 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 50, structural_boundaries: 30, bitwise_ops: 13, doc: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `packages/zone.js/check-file-size.js` (JAVASCRIPT) | Magnitude: 14.12 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 18, io: 6, branch: 4, structural_boundaries: 3
- `packages/core/schematics/ng-generate/cleanup-unused-imports/unused_imports_migration.ts` (TYPESCRIPT) | Magnitude: 35.76 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 158, state_mutation: 49, branch: 47, structural_boundaries: 29
- `packages/core/schematics/ng-generate/control-flow-migration/types.ts` (TYPESCRIPT) | Magnitude: 53.46 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 367, state_mutation: 281, structural_boundaries: 90, branch: 74
- `packages/upgrade/src/common/src/upgrade_helper.ts` (TYPESCRIPT) | Magnitude: 26.52 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 230, state_mutation: 82, branch: 71, structural_boundaries: 52
- `packages/core/src/util/array_utils.ts` (TYPESCRIPT) | Magnitude: 14.29 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 66, state_mutation: 54, structural_boundaries: 29, doc: 25

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `devtools/projects/ng-devtools/src/lib/shared/icon/icon.component.ts` (TYPESCRIPT) | Magnitude: 1.73 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 6, api: 2, ui_framework: 2
- `packages/compiler-cli/linker/src/file_linker/partial_linkers/partial_directive_linker_1.ts` (TYPESCRIPT) | Magnitude: 13.15 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 205, structural_boundaries: 41, branch: 39, ui_framework: 21
- `adev/src/content/examples/animations/src/app/animations-package/open-close.html` (HTML) | Magnitude: 13.12 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 3, indent_spaces: 2, ui_framework: 1, decorators: 1
- `adev/src/content/examples/animations/src/app/open-close.1.html` (HTML) | Magnitude: 13.12 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 3, indent_spaces: 2, ui_framework: 1, decorators: 1
- `adev/src/content/examples/animations/src/app/open-close.2.html` (HTML) | Magnitude: 13.12 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 3, indent_spaces: 2, ui_framework: 1, decorators: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `adev/src/content/examples/signal-forms/src/login-validation-complete/app/app.ts` (TYPESCRIPT) | Magnitude: 2.23 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 7, args: 6, func_start: 6
- `scripts/benchmarks/index.mts` (TYPESCRIPT) | Magnitude: 6.27 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 87, structural_boundaries: 36, concurrency: 26, args: 15
- `devtools/cypress/support/commands.js` (JAVASCRIPT) | Magnitude: 11.28 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 7, concurrency: 5, args: 4
- `packages/core/rxjs-interop/src/pending_until_event.ts` (TYPESCRIPT) | Magnitude: 4.17 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 37, structural_boundaries: 13, args: 13, func_start: 10
- `packages/core/src/util/promise_with_resolvers.ts` (TYPESCRIPT) | Magnitude: 3.3 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 13, generics: 10, args: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `packages/core/src/render/api.ts` (TYPESCRIPT) | Magnitude: 4.09 | Delta: **0.07 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 75, indent_spaces: 42, safety_bypasses: 27, structural_boundaries: 23
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
- `packages/common/src/directives/ng_component_outlet.ts` (TYPESCRIPT) | Magnitude: 13.6 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 93, indent_spaces: 66, branch: 14, args: 6
- `packages/examples/common/pipes/ts/titlecase_pipe.ts` (TYPESCRIPT) | Magnitude: 1.64 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 16, safety: 7, structural_boundaries: 4, decorators: 3
- `packages/compiler-cli/src/ngtsc/annotations/component/test/component_spec.ts` (TYPESCRIPT) | Magnitude: 51.4 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 1059, structural_boundaries: 199, immutability_locks: 194, decorators: 112
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

- `packages/forms/signals/src/api/types.ts` -> Churn: **67.88%** | Cog Load: 4.1722% | Debt: 99.2355%
- `packages/forms/signals/src/field/node.ts` -> Churn: **60.6%** | Cog Load: 51.4165% | Debt: 9.9379%
- `packages/core/src/render3/instructions/control.ts` -> Churn: **54.69%** | Cog Load: 67.3569% | Debt: 56.6714%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `packages/common/http/src/client.ts` -> **SkyZeroZx** (100.0% isolated ownership) | Magnitude: 175.93
- `packages/compiler-cli/src/ngtsc/typecheck/test/type_checker__get_symbol_of_template_node_spec.ts` -> **Andrew Scott** (100.0% isolated ownership) | Magnitude: 121.31
- `devtools/cypress/integration/node-selection.e2e.js` -> **Matthieu Riegler** (100.0% isolated ownership) | Magnitude: 86.24
- `packages/compiler-cli/src/ngtsc/transform/src/compilation.ts` -> **Andrew Scott** (100.0% isolated ownership) | Magnitude: 84.34
- `packages/zone.js/example/profiling.html` -> **Matthieu Riegler** (100.0% isolated ownership) | Magnitude: 83.58

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `packages/core/src/render3/component_ref.ts` -> **Severity: 0.02** (Bridge: 0.0002 * Flux: 99.8573%)
- `packages/router/src/router.ts` -> **Severity: 0.017** (Bridge: 0.0002 * Flux: 100.0%)
- `packages/core/src/render3/ng_module_ref.ts` -> **Severity: 0.012** (Bridge: 0.0002 * Flux: 49.5238%)
- `packages/router/src/navigation_transition.ts` -> **Severity: 0.01** (Bridge: 0.0001 * Flux: 99.9876%)
- `packages/core/src/di/provider_collection.ts` -> **Severity: 0.009** (Bridge: 0.0001 * Flux: 90.7601%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `packages/platform-browser/src/platform-browser.ts` -> **Severity: 1780.2** (Blast Radius: 17.802 * Doc Risk: 100.0%)
- `packages/compiler/src/chars.ts` -> **Severity: 641.0** (Blast Radius: 6.41 * Doc Risk: 100.0%)
- `packages/compiler/src/output/output_ast.ts` -> **Severity: 498.329** (Blast Radius: 5.808 * Doc Risk: 85.8005%)
- `packages/platform-browser/src/dom/events/dom_events.ts` -> **Severity: 482.139** (Blast Radius: 7.827 * Doc Risk: 61.5995%)
- `packages/compiler/src/i18n/i18n_ast.ts` -> **Severity: 457.181** (Blast Radius: 4.598 * Doc Risk: 99.4305%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
