# ARCHITECTURAL_BRIEF: prettier
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_typescript/prettier` |
| **Timestamp** | `2026-08-07T04:17:16.339079+00:00` |
| **Scan Duration** | `8.23s` |
| **Git Branch** | `main` |
| **Git Commit** | `574b18d7d692370ace1b67c763b486926b4fb139` |
| **Git Remote** | `https://github.com/prettier/prettier.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 3807 malicious artifacts.

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
| Total Artifacts | 9196 |
| Analyzed Artifacts (Scanned) | 5238 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 3958 |
| Total LOC | 115828 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 57.0% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.4008 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 23 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 3195 | 88947 | 61.0% |
| TYPESCRIPT | 611 | 8671 | 11.7% |
| HTML | 397 | 5919 | 7.6% |
| MARKDOWN | 375 | 0 | 7.2% |
| CSS | 300 | 9897 | 5.7% |
| YAML | 169 | 1383 | 3.2% |
| JSON | 88 | 952 | 1.7% |
| XML | 58 | 40 | 1.1% |
| PLAINTEXT | 44 | 0 | 0.8% |
| SHELL | 1 | 19 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `6.35`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 3892 | 74.3% |
| file_cluster_13 | 484 | 9.2% |
| file_cluster_2 | 136 | 2.6% |
| file_cluster_4 | 80 | 1.5% |
| file_cluster_16 | 70 | 1.3% |
| file_cluster_17 | 60 | 1.1% |
| file_cluster_0 | 20 | 0.4% |
| file_cluster_9 | 11 | 0.2% |
| file_cluster_6 | 6 | 0.1% |
| file_cluster_7 | 6 | 0.1% |
| file_cluster_11 | 5 | 0.1% |
| file_cluster_15 | 4 | 0.1% |
| file_cluster_1 | 3 | 0.1% |
| file_cluster_12 | 2 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 419 | 8.0% |
| Static: Minified & Vendor Opaque Mass | 40 | 0.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 3958*

**Composition by Extension & Reason:**
- `.js`: 1788x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded: Neighborhood Micro-Mass Limit Exceeded, 1x Excluded (Lexical Monotony: High structural repetition detected in 5032 LOC)
- `.snap`: 1443x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Unsupported Format (.snap)
- `.yml`: 221x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Saturation: Line 1 exceeds 500 chars), 1x Excluded (Saturation: Line 2 exceeds 500 chars)
- `no_extension`: 58x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 13x Unsupported Format (.undeterminable), 3x Excluded (Unsupported Extension: '.js"')
- `.png`: 75x Excluded (Explicitly Denied Extension: '.png')
- `.md`: 67x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 895 LOC)
- `.graphql`: 64x Excluded (Unsupported Extension: '.graphql'), 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ts`: 61x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 2200 LOC)
- `.json`: 16x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.foo`: 9x Excluded (Unsupported Extension: '.foo'), 5x Unsupported Format (.foo)
- `.css`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 2 exceeds 500 chars), 1x Excluded (Saturation: Line 85 exceeds 500 chars)
- `.mjs`: 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.html`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 16 LOC)
- `.mjml`: 9x Excluded (Unsupported Extension: '.mjml')
- `.json5`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 9.6 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 21.5 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 2.7 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 1.5 | 0.0 | 0.0 |
| API Exposure | 0.0 | 19.2 | 1.6 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 6.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 2.6 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 0.5 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 54.1 | 46.7 | 100.0 |
| Instability Exposure | 0.0 | 5.5 | 1.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 52.1 | 2.9 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 4.8 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 99.2 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tests/format/angular/angular/real-world.component.html` (Hits: 130)
- `scripts/tools/eslint-plugin-prettier-internal-rules/test.js` (Hits: 96)
- `src/language-handlebars/printer-glimmer.js` (Hits: 66)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **js.html** (`tests/format/html/js/js.html`) — 558 inbound connections
2. **test.js** (`scripts/tools/eslint-plugin-prettier-internal-rules/test.js`) — 11 inbound connections
3. **css.js** (`src/language-js/embed/css.js`) — 10 inbound connections
4. **fs.js** (`tests/format/flow/flow-repo/node_tests/fs/fs.js`) — 7 inbound connections
5. **d.js** (`tests/format/flow/flow-repo/incremental_mixed_naming_cycle/d.js`) — 4 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **estree.js** (`src/language-js/print/estree.js`) — 40 outbound dependencies
2. **flow.js** (`src/language-js/print/flow.js`) — 38 outbound dependencies
3. **typescript.js** (`src/language-js/print/typescript.js`) — 34 outbound dependencies
4. **production-plugins.js** (`src/main/plugins/builtin-plugins/production-plugins.js`) — 28 outbound dependencies
5. **es6modules.js** (`tests/format/flow/flow-repo/es6modules/es6modules.js`) — 24 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `genericPrint` (@ `src/language-css/printer-postcss.js`) -> Impact: **412.3** | LOC: 526
- `printAssignment` (@ `src/language-js/print/assignment.js`) -> Impact: **322.4** | LOC: 338
  * *Intent:* /** * @import AstPath from "../../common/ast-path.js"
- `printFlow` (@ `src/language-js/print/flow.js`) -> Impact: **322.1** | LOC: 315
- `printEstree` (@ `src/language-js/print/estree.js`) -> Impact: **292.4** | LOC: 258
  * *Intent:* /** * @import AstPath from "../../common/ast-path.js" * @import {Doc} from "../../document/index.js"
- `printCommaSeparatedValueGroup` (@ `src/language-css/print/comma-separated-value-group.js`) -> Impact: **227.1** | LOC: 261
  * *Intent:* /** * @import AstPath from "../../common/ast-path.js" * @import {Doc} from "../../document/index.js"
- `printMdast` (@ `src/language-markdown/print/mdast.js`) -> Impact: **226.4** | LOC: 329
- `parseNestedCSS` (@ `src/language-css/parser-postcss.js`) -> Impact: **203.2** | LOC: 427
- `genericPrint` (@ `src/language-graphql/printer-graphql.js`) -> Impact: **194.7** | LOC: 413
- `tokenizeHtmlText` (@ `src/language-markdown/parse/micromark/micromark-extension-html-text.js`) -> Impact: **189.9** | LOC: 478
- `isInlineValueCommentNode` (@ `src/language-css/print/comma-separated-value-group.js`) -> Impact: **182.5** | LOC: 221

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src/language-js/print` | 73 | 6364.44 | 22.88% | 20.39% |
| `tests/integration/__tests__` | 75 | 2598.24 | 9.01% | 0.0% |
| `src/language-markdown/print` | 12 | 1510.28 | 18.99% | 48.99% |
| `src/language-css` | 10 | 1254.28 | 11.41% | 32.28% |
| `src/language-js/utilities` | 61 | 1190.22 | 12.27% | 9.77% |
| `tests/format/js/comments` | 50 | 1100.48 | 6.93% | 0.0% |
| `website/playground` | 16 | 955.54 | 13.86% | 21.99% |
| `tests/format/flow/flow-repo/refinements` | 28 | 942.58 | 29.69% | 0.0% |
| `tests/format/js/comments/between-head-and-body` | 3 | 914.22 | 31.67% | 0.0% |
| `src/main` | 17 | 894.78 | 33.04% | 25.43% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `scripts/lint-changelog.js` -> **100.0%** Exposure
- `src/config/editorconfig/index.js` -> **100.0%** Exposure
- `src/document/builders/align.js` -> **100.0%** Exposure
- `src/document/builders/if-break.js` -> **100.0%** Exposure
- `src/document/printer/indent.js` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `benchmarks/string-buffer-compress.js` -> **100.0%** Exposure
- `bin/prettier.cjs` -> **100.0%** Exposure
- `src/common/ast-path.js` -> **100.0%** Exposure
- `src/common/get-file-info.js` -> **100.0%** Exposure
- `src/config/find-project-root.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tests/format/css/atrule/supports.css` -> **0** Orphaned Functions | **102** Duplicates
- `tests/integration/__tests__/infer-parser.js` -> **0** Orphaned Functions | **69** Duplicates
- `tests/format/flow/flow-repo/logical/logical.js` -> **65** Orphaned Functions | **0** Duplicates
- `tests/integration/__tests__/file-info.js` -> **0** Orphaned Functions | **54** Duplicates
- `tests/integration/__tests__/config-resolution.js` -> **0** Orphaned Functions | **45** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`scripts/lint-changelog.js`** -> AI Confidence: **99.39%**
2. **`src/document/printer/printer.js`** -> AI Confidence: **99.39%**
3. **`src/language-css/printer-postcss.js`** -> AI Confidence: **99.39%**
4. **`src/language-js/comments/can-attach-comment.js`** -> AI Confidence: **99.39%**
5. **`src/language-js/parentheses/needs-parentheses.js`** -> AI Confidence: **99.39%**
6. **`src/language-js/print/ternary.js`** -> AI Confidence: **99.39%**
7. **`src/language-js/massage-ast/index.js`** -> AI Confidence: **99.34%**
8. **`tests/format/js/require/require.js`** -> AI Confidence: **99.32%**
9. **`scripts/draft-blog-post.js`** -> AI Confidence: **99.31%**
10. **`src/cli/format.js`** -> AI Confidence: **99.31%**
11. **`src/cli/index.js`** -> AI Confidence: **99.31%**
12. **`src/language-css/parse/parse-value.js`** -> AI Confidence: **99.31%**
13. **`src/language-css/parser-postcss.js`** -> AI Confidence: **99.31%**
14. **`src/language-graphql/printer-graphql.js`** -> AI Confidence: **99.31%**
15. **`src/language-handlebars/printer-glimmer.js`** -> AI Confidence: **99.31%**
16. **`src/language-html/embed.js`** -> AI Confidence: **99.31%**
17. **`src/language-html/parse/parse.js`** -> AI Confidence: **99.31%**
18. **`src/language-html/parse/postprocess.js`** -> AI Confidence: **99.31%**
19. **`src/language-html/utilities/index.js`** -> AI Confidence: **99.31%**
20. **`src/language-js/comments/handle-comments.js`** -> AI Confidence: **99.31%**
21. **`src/language-js/parentheses/parent-needs-parentheses.js`** -> AI Confidence: **99.31%**
22. **`src/language-js/parse/oxc.js`** -> AI Confidence: **99.31%**
23. **`src/language-js/parse/postprocess/index.js`** -> AI Confidence: **99.31%**
24. **`src/language-js/print/array.js`** -> AI Confidence: **99.31%**
25. **`src/language-js/print/arrow-function.js`** -> AI Confidence: **99.31%**
26. **`src/language-js/print/assignment.js`** -> AI Confidence: **99.31%**
27. **`src/language-js/print/binaryish.js`** -> AI Confidence: **99.31%**
28. **`src/language-js/print/call-arguments.js`** -> AI Confidence: **99.31%**
29. **`src/language-js/print/call-expression.js`** -> AI Confidence: **99.31%**
30. **`src/language-js/print/class-body.js`** -> AI Confidence: **99.31%**
31. **`src/language-js/print/class.js`** -> AI Confidence: **99.31%**
32. **`src/language-js/print/estree.js`** -> AI Confidence: **99.31%**
33. **`src/language-js/print/flow.js`** -> AI Confidence: **99.31%**
34. **`src/language-js/print/function-parameters.js`** -> AI Confidence: **99.31%**
35. **`src/language-js/print/function-type.js`** -> AI Confidence: **99.31%**
36. **`src/language-js/print/function.js`** -> AI Confidence: **99.31%**
37. **`src/language-js/print/if-statement.js`** -> AI Confidence: **99.31%**
38. **`src/language-js/print/jsx.js`** -> AI Confidence: **99.31%**
39. **`src/language-js/print/mapped-type.js`** -> AI Confidence: **99.31%**
40. **`src/language-js/print/match.js`** -> AI Confidence: **99.31%**
41. **`src/language-js/print/member-chain.js`** -> AI Confidence: **99.31%**
42. **`src/language-js/print/module.js`** -> AI Confidence: **99.31%**
43. **`src/language-js/print/object.js`** -> AI Confidence: **99.31%**
44. **`src/language-js/print/template-literal.js`** -> AI Confidence: **99.31%**
45. **`src/language-js/print/union-type.js`** -> AI Confidence: **99.31%**
46. **`src/language-markdown/print/mdast.js`** -> AI Confidence: **99.31%**
47. **`src/language-yaml/printer-yaml.js`** -> AI Confidence: **99.31%**
48. **`src/main/ast-to-doc.js`** -> AI Confidence: **99.31%**
49. **`src/main/comments/print.js`** -> AI Confidence: **99.31%**
50. **`tests/config/install-prettier.js`** -> AI Confidence: **99.31%**
51. **`website/playground/Playground.jsx`** -> AI Confidence: **99.31%**
52. **`website/playground/panels.jsx`** -> AI Confidence: **99.31%**
53. **`puppeteer.config.cjs`** -> AI Confidence: **99.29%**
54. **`src/cli/options/create-minimist-options.js`** -> AI Confidence: **99.29%**
55. **`src/common/common-options.evaluate.js`** -> AI Confidence: **99.29%**
56. **`src/config/editorconfig/editorconfig-to-prettier.js`** -> AI Confidence: **99.29%**
57. **`src/document/utilities/traverse-doc.js`** -> AI Confidence: **99.29%**
58. **`src/language-css/print/comma-separated-value-group.js`** -> AI Confidence: **99.29%**
59. **`src/language-html/massage-ast/index.js`** -> AI Confidence: **99.29%**
60. **`src/language-html/print/angular-control-flow-block-settings.evaluate.js`** -> AI Confidence: **99.29%**
61. **`src/language-js/massage-ast/key.js`** -> AI Confidence: **99.29%**
62. **`src/main/comments/utilities.js`** -> AI Confidence: **99.29%**
63. **`src/main/core-options.evaluate.js`** -> AI Confidence: **99.29%**
64. **`src/utilities/print-number.js`** -> AI Confidence: **99.29%**
65. **`tests/format/flow/_errors_/spread-with-optional.js`** -> AI Confidence: **99.29%**
66. **`tests/format/flow/as-satisfies-expression/ternary.js`** -> AI Confidence: **99.29%**
67. **`tests/format/flow/component/component-type-annotation.js`** -> AI Confidence: **99.29%**
68. **`tests/format/flow/component/declare-component.js`** -> AI Confidence: **99.29%**
69. **`tests/format/flow/flow-repo/abnormal/break-continue.js`** -> AI Confidence: **99.29%**
70. **`tests/format/flow/flow-repo/error_messages/errors.js`** -> AI Confidence: **99.29%**
71. **`tests/format/flow/flow-repo/iterable/variance.js`** -> AI Confidence: **99.29%**
72. **`tests/format/flow/flow-repo/keys/keys.js`** -> AI Confidence: **99.29%**
73. **`tests/format/flow/flow-repo/nullable/maybe.js`** -> AI Confidence: **99.29%**
74. **`tests/format/flow/flow-repo/nullable/simple_nullable.js`** -> AI Confidence: **99.29%**
75. **`tests/format/flow/flow-repo/optional/loop.js`** -> AI Confidence: **99.29%**
76. **`tests/format/flow/flow-repo/optional/nullable.js`** -> AI Confidence: **99.29%**
77. **`tests/format/flow/flow-repo/optional_props/test3_exact_annot.js`** -> AI Confidence: **99.29%**
78. **`tests/format/flow/flow-repo/predicates-declared/sanity-parameter-mismatch.js`** -> AI Confidence: **99.29%**
79. **`tests/format/flow/flow-repo/refinements/computed_string_literal.js`** -> AI Confidence: **99.29%**
80. **`tests/format/flow/flow-repo/refinements/eq.js`** -> AI Confidence: **99.29%**
81. **`tests/format/flow/flow-repo/refinements/missing-property-cond.js`** -> AI Confidence: **99.29%**
82. **`tests/format/flow/flow-repo/refinements/mixed.js`** -> AI Confidence: **99.29%**
83. **`tests/format/flow/flow-repo/refinements/tagged_union.js`** -> AI Confidence: **99.29%**
84. **`tests/format/flow/flow-repo/refinements/tagged_union_import.js`** -> AI Confidence: **99.29%**
85. **`tests/format/flow/flow-repo/refinements/union.js`** -> AI Confidence: **99.29%**
86. **`tests/format/flow/flow-repo/switch/switch.js`** -> AI Confidence: **99.29%**
87. **`tests/format/flow/flow-repo/tagged-unions/type-decls-neg.js`** -> AI Confidence: **99.29%**
88. **`tests/format/flow/flow-repo/tagged-unions/type-decls-pos.js`** -> AI Confidence: **99.29%**
89. **`tests/format/flow/flow-repo/try/abnormals.js`** -> AI Confidence: **99.29%**
90. **`tests/format/flow/flow-repo/tuples/optional.js`** -> AI Confidence: **99.29%**
91. **`tests/format/flow/flow-repo/type-at-pos/trycatch.js`** -> AI Confidence: **99.29%**
92. **`tests/format/flow/flow-repo/type-printer/types.js`** -> AI Confidence: **99.29%**
93. **`tests/format/flow/flow-repo/union_new/issue-1462-ii.js`** -> AI Confidence: **99.29%**
94. **`tests/format/flow/flow-repo/union_new/issue-1664.js`** -> AI Confidence: **99.29%**
95. **`tests/format/flow/flow-repo/union_new/issue-2232.js`** -> AI Confidence: **99.29%**
96. **`tests/format/flow/flow-repo/union_new/test13.js`** -> AI Confidence: **99.29%**
97. **`tests/format/flow/flow-repo/union_new/test7.js`** -> AI Confidence: **99.29%**
98. **`tests/format/flow/generic/nullable.js`** -> AI Confidence: **99.29%**
99. **`tests/format/flow/hook/declare-hook.js`** -> AI Confidence: **99.29%**
100. **`tests/format/flow/intersection/intersection.js`** -> AI Confidence: **99.29%**
101. **`tests/format/flow/mapped-types/mapped-types.js`** -> AI Confidence: **99.29%**
102. **`tests/format/flow/mapped-types/ts-compatibility.js`** -> AI Confidence: **99.29%**
103. **`tests/format/flow/match/from-hermes-repo/regression.js`** -> AI Confidence: **99.29%**
104. **`tests/format/flow/maybe/maybe_return.js`** -> AI Confidence: **99.29%**
105. **`tests/format/flow/maybe/prettier-ignore.js`** -> AI Confidence: **99.29%**
106. **`tests/format/flow/optional-indexed-access/optional-indexed-access.js`** -> AI Confidence: **99.29%**
107. **`tests/format/flow/tuples/optional.js`** -> AI Confidence: **99.29%**
108. **`tests/format/js/_errors_/discard-binding/invalid-assignment-for.js`** -> AI Confidence: **99.29%**
109. **`tests/format/js/_errors_/discard-binding/invalid-catch-parameter.js`** -> AI Confidence: **99.29%**
110. **`tests/format/js/_errors_/discard-binding/invalid-rest-element-array-pattern-for-lhs.js`** -> AI Confidence: **99.29%**
111. **`tests/format/js/_errors_/discard-binding/invalid-rest-element-object-pattern-for-lhs.js`** -> AI Confidence: **99.29%**
112. **`tests/format/js/_errors_/explicit-resource-management/invalid-for-using-binding-in.js`** -> AI Confidence: **99.29%**
113. **`tests/format/js/_errors_/explicit-resource-management/invalid-for-using-binding-of-in.js`** -> AI Confidence: **99.29%**
114. **`tests/format/js/_errors_/explicit-resource-management/invalid-for-using-binding-of-of.js`** -> AI Confidence: **99.29%**
115. **`tests/format/js/_errors_/explicit-resource-management/invalid-using-binding-pattern.js`** -> AI Confidence: **99.29%**
116. **`tests/format/js/_errors_/partial-template-strings.js`** -> AI Confidence: **99.29%**
117. **`tests/format/js/arrays/empty.js`** -> AI Confidence: **99.29%**
118. **`tests/format/js/arrays/issue-10159.js`** -> AI Confidence: **99.29%**
119. **`tests/format/js/assignment-comments/call.js`** -> AI Confidence: **99.29%**
120. **`tests/format/js/assignment/binaryish.js`** -> AI Confidence: **99.29%**
121. **`tests/format/js/assignment/call-with-template.js`** -> AI Confidence: **99.29%**
122. **`tests/format/js/assignment/issue-1419.js`** -> AI Confidence: **99.29%**
123. **`tests/format/js/assignment/issue-2482-1.js`** -> AI Confidence: **99.29%**
124. **`tests/format/js/assignment/issue-4094.js`** -> AI Confidence: **99.29%**
125. **`tests/format/js/assignment/sequence.js`** -> AI Confidence: **99.29%**
126. **`tests/format/js/babel-plugins/bigint.js`** -> AI Confidence: **99.29%**
127. **`tests/format/js/babel-plugins/flow.js`** -> AI Confidence: **99.29%**
128. **`tests/format/js/babel-plugins/logical-assignment-operators.js`** -> AI Confidence: **99.29%**
129. **`tests/format/js/babel-plugins/optional-catch-binding.js`** -> AI Confidence: **99.29%**
130. **`tests/format/js/babel-plugins/optional-chaining-assignment.js`** -> AI Confidence: **99.29%**
131. **`tests/format/js/babel-plugins/optional-chaining.js`** -> AI Confidence: **99.29%**
132. **`tests/format/js/babel-plugins/partial-application.js`** -> AI Confidence: **99.29%**
133. **`tests/format/js/babel-plugins/regexp-modifiers.js`** -> AI Confidence: **99.29%**
134. **`tests/format/js/babel-plugins/throw-expressions.js`** -> AI Confidence: **99.29%**
135. **`tests/format/js/binary-expressions/array-and-object.js`** -> AI Confidence: **99.29%**
136. **`tests/format/js/binary-expressions/call.js`** -> AI Confidence: **99.29%**
137. **`tests/format/js/binary-expressions/chain-expression.js`** -> AI Confidence: **99.29%**
138. **`tests/format/js/binary-expressions/comment.js`** -> AI Confidence: **99.29%**
139. **`tests/format/js/binary-expressions/if.js`** -> AI Confidence: **99.29%**
140. **`tests/format/js/binary-expressions/inline-jsx.js`** -> AI Confidence: **99.29%**
141. **`tests/format/js/binary-expressions/inline-object-array.js`** -> AI Confidence: **99.29%**
142. **`tests/format/js/binary-expressions/jsx_parent.js`** -> AI Confidence: **99.29%**
143. **`tests/format/js/binary-expressions/like-regexp.js`** -> AI Confidence: **99.29%**
144. **`tests/format/js/binary-expressions/unary.js`** -> AI Confidence: **99.29%**
145. **`tests/format/js/bind-expressions/bind_parens.js`** -> AI Confidence: **99.29%**
146. **`tests/format/js/call/boolean/boolean.js`** -> AI Confidence: **99.29%**
147. **`tests/format/js/call/first-argument-expansion/issue-2456.js`** -> AI Confidence: **99.29%**
148. **`tests/format/js/call/no-argument/no-arguments.js`** -> AI Confidence: **99.29%**
149. **`tests/format/js/chain-expression/call-expression.js`** -> AI Confidence: **99.29%**
150. **`tests/format/js/chain-expression/issue-15785-3.js`** -> AI Confidence: **99.29%**
151. **`tests/format/js/chain-expression/issue-15912.js`** -> AI Confidence: **99.29%**
152. **`tests/format/js/chain-expression/member-chain.js`** -> AI Confidence: **99.29%**
153. **`tests/format/js/chain-expression/member-expression.js`** -> AI Confidence: **99.29%**
154. **`tests/format/js/chain-expression/new-expression.js`** -> AI Confidence: **99.29%**
155. **`tests/format/js/chain-expression/number.js`** -> AI Confidence: **99.29%**
156. **`tests/format/js/chain-expression/tagged-template-literals.js`** -> AI Confidence: **99.29%**
157. **`tests/format/js/comments-closure-typecast/issue-9358.js`** -> AI Confidence: **99.29%**
158. **`tests/format/js/comments/15661.js`** -> AI Confidence: **99.29%**
159. **`tests/format/js/comments/16398.js`** -> AI Confidence: **99.29%**
160. **`tests/format/js/comments/between-head-and-body/between-head-and-body.js`** -> AI Confidence: **99.29%**
161. **`tests/format/js/comments/between-head-and-body/empty-statement.js`** -> AI Confidence: **99.29%**
162. **`tests/format/js/comments/between-head-and-body/non-block.js`** -> AI Confidence: **99.29%**
163. **`tests/format/js/comments/binary-expressions-block-comments.js`** -> AI Confidence: **99.29%**
164. **`tests/format/js/comments/binary-expressions-single-comments.js`** -> AI Confidence: **99.29%**
165. **`tests/format/js/comments/break-continue-statements-2.js`** -> AI Confidence: **99.29%**
166. **`tests/format/js/comments/break-continue-statements-3.js`** -> AI Confidence: **99.29%**
167. **`tests/format/js/comments/break-continue-statements.js`** -> AI Confidence: **99.29%**
168. **`tests/format/js/comments/call_comment.js`** -> AI Confidence: **99.29%**
169. **`tests/format/js/comments/dangling_for.js`** -> AI Confidence: **99.29%**
170. **`tests/format/js/comments/if.js`** -> AI Confidence: **99.29%**
171. **`tests/format/js/comments/multi-comments-2.js`** -> AI Confidence: **99.29%**
172. **`tests/format/js/comments/single-star-jsdoc.js`** -> AI Confidence: **99.29%**
173. **`tests/format/js/comments/switch.js`** -> AI Confidence: **99.29%**
174. **`tests/format/js/comments/try.js`** -> AI Confidence: **99.29%**
175. **`tests/format/js/comments/while-like/if.js`** -> AI Confidence: **99.29%**
176. **`tests/format/js/comments/while-like/while.js`** -> AI Confidence: **99.29%**
177. **`tests/format/js/comments/while-like/with.js`** -> AI Confidence: **99.29%**
178. **`tests/format/js/conditional/new-expression.js`** -> AI Confidence: **99.29%**
179. **`tests/format/js/conditional/new-ternary-examples.js`** -> AI Confidence: **99.29%**
180. **`tests/format/js/conditional/postfix-ternary-regressions.js`** -> AI Confidence: **99.29%**
181. **`tests/format/js/discard-binding/discard-binding-for-bindings.js`** -> AI Confidence: **99.29%**
182. **`tests/format/js/discard-binding/discard-binding-for-lhs.js`** -> AI Confidence: **99.29%**
183. **`tests/format/js/discard-binding/discard-binding-for-using-binding.js`** -> AI Confidence: **99.29%**
184. **`tests/format/js/empty-statement/body.js`** -> AI Confidence: **99.29%**
185. **`tests/format/js/empty-statement/no-newline.js`** -> AI Confidence: **99.29%**
186. **`tests/format/js/explicit-resource-management/using-declarations.js`** -> AI Confidence: **99.29%**
187. **`tests/format/js/explicit-resource-management/valid-await-using-comments.js`** -> AI Confidence: **99.29%**
188. **`tests/format/js/explicit-resource-management/valid-using-as-identifier-computed-member.js`** -> AI Confidence: **99.29%**
189. **`tests/format/js/explicit-resource-management/valid-using-as-identifier-for-in.js`** -> AI Confidence: **99.29%**
190. **`tests/format/js/explicit-resource-management/valid-using-as-identifier-for-init.js`** -> AI Confidence: **99.29%**
191. **`tests/format/js/explicit-resource-management/valid-using-as-identifier-for-of.js`** -> AI Confidence: **99.29%**
192. **`tests/format/js/explicit-resource-management/valid-using-binding-using.js`** -> AI Confidence: **99.29%**
193. **`tests/format/js/for-of/comments.js`** -> AI Confidence: **99.29%**
194. **`tests/format/js/for/9812-2.js`** -> AI Confidence: **99.29%**
195. **`tests/format/js/for/9812.js`** -> AI Confidence: **99.29%**
196. **`tests/format/js/for/continue-and-break-comment-1.js`** -> AI Confidence: **99.29%**
197. **`tests/format/js/for/continue-and-break-comment-2.js`** -> AI Confidence: **99.29%**
198. **`tests/format/js/if/blank-lines.js`** -> AI Confidence: **99.29%**
199. **`tests/format/js/if/comment-between-condition-and-body.js`** -> AI Confidence: **99.29%**
200. **`tests/format/js/if/comment_before_else.js`** -> AI Confidence: **99.29%**
201. **`tests/format/js/if/condition-break/boolean-expression.js`** -> AI Confidence: **99.29%**
202. **`tests/format/js/if/condition-break/real-world-cases.js`** -> AI Confidence: **99.29%**
203. **`tests/format/js/if/condition-break/unary-expression.js`** -> AI Confidence: **99.29%**
204. **`tests/format/js/if/expr_and_same_line_comments.js`** -> AI Confidence: **99.29%**
205. **`tests/format/js/if/if_comments.js`** -> AI Confidence: **99.29%**
206. **`tests/format/js/if/issue-15168.js`** -> AI Confidence: **99.29%**
207. **`tests/format/js/if/non-block.js`** -> AI Confidence: **99.29%**
208. **`tests/format/js/if/trailing_comment.js`** -> AI Confidence: **99.29%**
209. **`tests/format/js/label/comment.js`** -> AI Confidence: **99.29%**
210. **`tests/format/js/last-argument-expansion/function-body-in-mode-break.js`** -> AI Confidence: **99.29%**
211. **`tests/format/js/logical-assignment/inside-call/18171.js`** -> AI Confidence: **99.29%**
212. **`tests/format/js/logical-assignment/logical-assignment.js`** -> AI Confidence: **99.29%**
213. **`tests/format/js/logical-expressions/in-unary-expression.js`** -> AI Confidence: **99.29%**
214. **`tests/format/js/logical-expressions/issue-7024.js`** -> AI Confidence: **99.29%**
215. **`tests/format/js/logical-expressions/logical-expression-operators.js`** -> AI Confidence: **99.29%**
216. **`tests/format/js/logical-expressions/multiple-comments/17192.js`** -> AI Confidence: **99.29%**
217. **`tests/format/js/member/conditional.js`** -> AI Confidence: **99.29%**
218. **`tests/format/js/member/logical.js`** -> AI Confidence: **99.29%**
219. **`tests/format/js/method-chain/18171.js`** -> AI Confidence: **99.29%**
220. **`tests/format/js/method-chain/assignment-lhs.js`** -> AI Confidence: **99.29%**
221. **`tests/format/js/method-chain/conditional.js`** -> AI Confidence: **99.29%**
222. **`tests/format/js/method-chain/issue-17457.js`** -> AI Confidence: **99.29%**
223. **`tests/format/js/method-chain/multiple-members.js`** -> AI Confidence: **99.29%**
224. **`tests/format/js/multiparser-comments/comment-inside.js`** -> AI Confidence: **99.29%**
225. **`tests/format/js/multiparser-css/issue-11797.js`** -> AI Confidence: **99.29%**
226. **`tests/format/js/multiparser-css/url.js`** -> AI Confidence: **99.29%**
227. **`tests/format/js/multiparser-markdown/0-indent.js`** -> AI Confidence: **99.29%**
228. **`tests/format/js/multiparser-markdown/issue-5021.js`** -> AI Confidence: **99.29%**
229. **`tests/format/js/new-expression/new_expression.js`** -> AI Confidence: **99.29%**
230. **`tests/format/js/no-semi/do-while-statement.js`** -> AI Confidence: **99.29%**
231. **`tests/format/js/no-semi/for-in-statement.js`** -> AI Confidence: **99.29%**
232. **`tests/format/js/no-semi/for-of-statement.js`** -> AI Confidence: **99.29%**
233. **`tests/format/js/no-semi/for-statement.js`** -> AI Confidence: **99.29%**
234. **`tests/format/js/no-semi/if-statement.js`** -> AI Confidence: **99.29%**
235. **`tests/format/js/no-semi/labeled-statement.js`** -> AI Confidence: **99.29%**
236. **`tests/format/js/no-semi/while-statement.js`** -> AI Confidence: **99.29%**
237. **`tests/format/js/nullish-coalescing/nullish_coalesing_operator.js`** -> AI Confidence: **99.29%**
238. **`tests/format/js/object-colon-bug/bug.js`** -> AI Confidence: **99.29%**
239. **`tests/format/js/objects/escape-sequence-key.js`** -> AI Confidence: **99.29%**
240. **`tests/format/js/objects/range.js`** -> AI Confidence: **99.29%**
241. **`tests/format/js/optional-catch-binding/optional_catch_binding.js`** -> AI Confidence: **99.29%**
242. **`tests/format/js/optional-chaining-assignment/invalid-destructuring-arr.js`** -> AI Confidence: **99.29%**
243. **`tests/format/js/optional-chaining-assignment/invalid-destructuring-obj.js`** -> AI Confidence: **99.29%**
244. **`tests/format/js/optional-chaining-assignment/invalid-fn-param-assign.js`** -> AI Confidence: **99.29%**
245. **`tests/format/js/optional-chaining-assignment/invalid-fn-param.js`** -> AI Confidence: **99.29%**
246. **`tests/format/js/optional-chaining-assignment/invalid-for-await-of.js`** -> AI Confidence: **99.29%**
247. **`tests/format/js/optional-chaining-assignment/invalid-for-in.js`** -> AI Confidence: **99.29%**
248. **`tests/format/js/optional-chaining-assignment/invalid-for-of.js`** -> AI Confidence: **99.29%**
249. **`tests/format/js/optional-chaining-assignment/invalid-inc-postfix.js`** -> AI Confidence: **99.29%**
250. **`tests/format/js/optional-chaining-assignment/invalid-inc-prefix.js`** -> AI Confidence: **99.29%**
251. **`tests/format/js/optional-chaining-assignment/valid-lhs-eq.js`** -> AI Confidence: **99.29%**
252. **`tests/format/js/optional-chaining-assignment/valid-lhs-plus-eq.js`** -> AI Confidence: **99.29%**
253. **`tests/format/js/optional-chaining-assignment/valid-parenthesized.js`** -> AI Confidence: **99.29%**
254. **`tests/format/js/optional-chaining/as-key.js`** -> AI Confidence: **99.29%**
255. **`tests/format/js/optional-chaining/chaining.js`** -> AI Confidence: **99.29%**
256. **`tests/format/js/optional-chaining/eval.js`** -> AI Confidence: **99.29%**
257. **`tests/format/js/private-in/private-in.js`** -> AI Confidence: **99.29%**
258. **`tests/format/js/range/nested-print-width.js`** -> AI Confidence: **99.29%**
259. **`tests/format/js/range/nested.js`** -> AI Confidence: **99.29%**
260. **`tests/format/js/range/nested2.js`** -> AI Confidence: **99.29%**
261. **`tests/format/js/range/nested3.js`** -> AI Confidence: **99.29%**
262. **`tests/format/js/range/try-catch.js`** -> AI Confidence: **99.29%**
263. **`tests/format/js/regex/regexp-modifiers.js`** -> AI Confidence: **99.29%**
264. **`tests/format/js/sloppy-mode/function-declaration-in-if.js`** -> AI Confidence: **99.29%**
265. **`tests/format/js/sloppy-mode/function-declaration-in-while.js`** -> AI Confidence: **99.29%**
266. **`tests/format/js/switch/comments.js`** -> AI Confidence: **99.29%**
267. **`tests/format/js/switch/comments2.js`** -> AI Confidence: **99.29%**
268. **`tests/format/js/switch/empty_lines.js`** -> AI Confidence: **99.29%**
269. **`tests/format/js/switch/empty_statement.js`** -> AI Confidence: **99.29%**
270. **`tests/format/js/switch/empty_switch.js`** -> AI Confidence: **99.29%**
271. **`tests/format/js/switch/switch.js`** -> AI Confidence: **99.29%**
272. **`tests/format/js/template-literals/conditional-expressions.js`** -> AI Confidence: **99.29%**
273. **`tests/format/js/template-literals/expression-break.js`** -> AI Confidence: **99.29%**
274. **`tests/format/js/template-literals/expressions.js`** -> AI Confidence: **99.29%**
275. **`tests/format/js/template-literals/logical-expressions.js`** -> AI Confidence: **99.29%**
276. **`tests/format/js/template/comment.js`** -> AI Confidence: **99.29%**
277. **`tests/format/js/ternaries/binary.js`** -> AI Confidence: **99.29%**
278. **`tests/format/js/ternaries/func-call.js`** -> AI Confidence: **99.29%**
279. **`tests/format/js/ternaries/indent-after-paren.js`** -> AI Confidence: **99.29%**
280. **`tests/format/js/ternaries/nested-in-condition.js`** -> AI Confidence: **99.29%**
281. **`tests/format/js/ternaries/nested.js`** -> AI Confidence: **99.29%**
282. **`tests/format/js/throw_statement/binaryish.js`** -> AI Confidence: **99.29%**
283. **`tests/format/js/try/catch.js`** -> AI Confidence: **99.29%**
284. **`tests/format/js/try/empty.js`** -> AI Confidence: **99.29%**
285. **`tests/format/js/try/try.js`** -> AI Confidence: **99.29%**
286. **`tests/format/js/v8_intrinsic/intrinsic_call.js`** -> AI Confidence: **99.29%**
287. **`tests/format/js/while/indent.js`** -> AI Confidence: **99.29%**
288. **`tests/format/jsx/do/do.js`** -> AI Confidence: **99.29%**
289. **`tests/format/jsx/jsx/conditional-expression.js`** -> AI Confidence: **99.29%**
290. **`tests/format/jsx/jsx/logical-expression.js`** -> AI Confidence: **99.29%**
291. **`tests/format/jsx/jsx/parens.js`** -> AI Confidence: **99.29%**
292. **`tests/format/jsx/jsx/quotes.js`** -> AI Confidence: **99.29%**
293. **`tests/format/jsx/jsx/ternary.js`** -> AI Confidence: **99.29%**
294. **`tests/format/jsx/spread/attribute.js`** -> AI Confidence: **99.29%**
295. **`tests/integration/cli/config/js/file.js`** -> AI Confidence: **99.29%**
296. **`website/playground/install-service-worker.js`** -> AI Confidence: **99.29%**
297. **`tests/format/typescript/_errors_/catch-clause-with-initializer/catch-clause-with-initializer.ts`** -> AI Confidence: **99.29%**
298. **`tests/format/typescript/as/ternary.ts`** -> AI Confidence: **99.29%**
299. **`tests/format/typescript/binary-expressions/chain-expression.ts`** -> AI Confidence: **99.29%**
300. **`tests/format/typescript/cast/18406.ts`** -> AI Confidence: **99.29%**
301. **`tests/format/typescript/cast/as-const.ts`** -> AI Confidence: **99.29%**
302. **`tests/format/typescript/cast/parenthesis.ts`** -> AI Confidence: **99.29%**
303. **`tests/format/typescript/catch-clause/type-annotation.ts`** -> AI Confidence: **99.29%**
304. **`tests/format/typescript/chain-expression/call-expression.ts`** -> AI Confidence: **99.29%**
305. **`tests/format/typescript/chain-expression/member-chain.ts`** -> AI Confidence: **99.29%**
306. **`tests/format/typescript/chain-expression/member-expression.ts`** -> AI Confidence: **99.29%**
307. **`tests/format/typescript/chain-expression/new-expression.ts`** -> AI Confidence: **99.29%**
308. **`tests/format/typescript/chain-expression/tagged-template-literals.ts`** -> AI Confidence: **99.29%**
309. **`tests/format/typescript/chain-expression/test2.ts`** -> AI Confidence: **99.29%**
310. **`tests/format/typescript/conformance/types/functions/functionOverloadErrorsSyntax.ts`** -> AI Confidence: **99.29%**
311. **`tests/format/typescript/conformance/types/union/unionTypeCallSignatures3.ts`** -> AI Confidence: **99.29%**
312. **`tests/format/typescript/destructuring/destructuring.ts`** -> AI Confidence: **99.29%**
313. **`tests/format/typescript/error-recovery/jsdoc_only_types.ts`** -> AI Confidence: **99.29%**
314. **`tests/format/typescript/instantiation-expression/property-access.ts`** -> AI Confidence: **99.29%**
315. **`tests/format/typescript/non-null/optional-chain.ts`** -> AI Confidence: **99.29%**
316. **`tests/format/typescript/nosemi/type.ts`** -> AI Confidence: **99.29%**
317. **`tests/format/typescript/optional-call/type-parameters.ts`** -> AI Confidence: **99.29%**
318. **`tests/format/typescript/optional-chaining/as-key.ts`** -> AI Confidence: **99.29%**
319. **`tests/format/typescript/template-literals/expressions.ts`** -> AI Confidence: **99.29%**
320. **`tests/format/typescript/template-literals/member-expression.ts`** -> AI Confidence: **99.29%**
321. **`tests/format/typescript/ternaries/indent.ts`** -> AI Confidence: **99.29%**
322. **`tests/format/typescript/tsx/keyword.tsx`** -> AI Confidence: **99.29%**
323. **`src/language-html/printer-html.js`** -> AI Confidence: **99.24%**
324. **`src/language-js/print/index.js`** -> AI Confidence: **99.24%**
325. **`src/language-js/print/type-parameters.js`** -> AI Confidence: **99.24%**
326. **`src/language-js/print/typescript.js`** -> AI Confidence: **99.24%**
327. **`src/utilities/public.js`** -> AI Confidence: **99.24%**
328. **`src/language-html/embed/vue-attributes.js`** -> AI Confidence: **99.23%**
329. **`src/language-js/parse/babel.js`** -> AI Confidence: **99.23%**
330. **`src/language-js/print/key.js`** -> AI Confidence: **99.23%**
331. **`src/language-js/print/miscellaneous.js`** -> AI Confidence: **99.23%**
332. **`src/language-js/utilities/comments.js`** -> AI Confidence: **99.23%**
333. **`src/language-js/print/block.js`** -> AI Confidence: **99.22%**
334. **`src/language-css/loc.js`** -> AI Confidence: **99.2%**
335. **`src/language-html/print-preprocess.js`** -> AI Confidence: **99.2%**
336. **`src/language-js/embed/graphql.js`** -> AI Confidence: **99.2%**
337. **`src/language-js/print/ternary-old.js`** -> AI Confidence: **99.2%**
338. **`src/language-js/utilities/left-side.js`** -> AI Confidence: **99.2%**
339. **`src/language-markdown/massage-ast/index.js`** -> AI Confidence: **99.2%**
340. **`src/language-markdown/print/children.js`** -> AI Confidence: **99.2%**
341. **`src/language-markdown/utilities.js`** -> AI Confidence: **99.2%**
342. **`src/language-yaml/print/block.js`** -> AI Confidence: **99.2%**
343. **`src/language-yaml/print/mapping-item.js`** -> AI Confidence: **99.2%**
344. **`scripts/generate-unused-typescript-specifiers.js`** -> AI Confidence: **99.18%**
345. **`src/document/builders/index.js`** -> AI Confidence: **99.18%**
346. **`tests/unit/syntax-transform.js`** -> AI Confidence: **99.18%**
347. **`website/docusaurus.config.js`** -> AI Confidence: **99.18%**
348. **`website/src/pages/users/index.jsx`** -> AI Confidence: **99.18%**
349. **`src/cli/cli-options.evaluate.js`** -> AI Confidence: **99.17%**
350. **`src/language-css/massage-ast/index.js`** -> AI Confidence: **99.17%**
351. **`src/language-graphql/massage-ast/index.js`** -> AI Confidence: **99.17%**
352. **`src/language-js/comments/is-gap.js`** -> AI Confidence: **99.17%**
353. **`src/language-js/location/start.js`** -> AI Confidence: **99.17%**
354. **`src/language-js/massage-ast/regexp-literal.js`** -> AI Confidence: **99.17%**
355. **`src/language-js/utilities/call-arguments.js`** -> AI Confidence: **99.17%**
356. **`src/language-js/utilities/is-flow-object-type-property-a-function.js`** -> AI Confidence: **99.17%**
357. **`src/language-json/massage-ast/index.js`** -> AI Confidence: **99.17%**
358. **`src/language-json/parse/json.js`** -> AI Confidence: **99.17%**
359. **`src/language-yaml/massage-ast/index.js`** -> AI Confidence: **99.17%**
360. **`src/main/normalize-options.js`** -> AI Confidence: **99.17%**
361. **`src/universal/assert.browser.js`** -> AI Confidence: **99.17%**
362. **`tests/format/flow/flow-repo/binary/in.js`** -> AI Confidence: **99.17%**
363. **`tests/format/flow/flow-repo/destructuring/defaults.js`** -> AI Confidence: **99.17%**
364. **`tests/format/flow/flow-repo/get-def/class.js`** -> AI Confidence: **99.17%**
365. **`tests/format/flow/flow-repo/intersection/pred.js`** -> AI Confidence: **99.17%**
366. **`tests/format/flow/flow-repo/promises/covariance.js`** -> AI Confidence: **99.17%**
367. **`tests/format/flow/flow-repo/refi/switch.js`** -> AI Confidence: **99.17%**
368. **`tests/format/flow/flow-repo/refinements/hasOwnProperty.js`** -> AI Confidence: **99.17%**
369. **`tests/format/flow/flow-repo/refinements/void.js`** -> AI Confidence: **99.17%**
370. **`tests/format/flow/flow-repo/switch/more_switch.js`** -> AI Confidence: **99.17%**
371. **`tests/format/flow/flow-repo/switch/trailing_cases.js`** -> AI Confidence: **99.17%**
372. **`tests/format/flow/flow-repo/symbol/symbol.js`** -> AI Confidence: **99.17%**
373. **`tests/format/flow/flow-repo/type-at-pos/predicates.js`** -> AI Confidence: **99.17%**
374. **`tests/format/flow/flow-repo/type-destructors/non_maybe_type.js`** -> AI Confidence: **99.17%**
375. **`tests/format/flow/method/consistent-breaking.js`** -> AI Confidence: **99.17%**
376. **`tests/format/js/assignment/destructuring.js`** -> AI Confidence: **99.17%**
377. **`tests/format/js/babel-plugins/nullish-coalescing-operator.js`** -> AI Confidence: **99.17%**
378. **`tests/format/js/conditional/comments.js`** -> AI Confidence: **99.17%**
379. **`tests/format/js/function/function_expression.js`** -> AI Confidence: **99.17%**
380. **`tests/format/js/last-argument-expansion/break-parent.js`** -> AI Confidence: **99.17%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Hardcoded Payload Artifacts
- `website/docusaurus.config.js` -> **99.1691%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `10` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `928` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `scripts/benchmark/compare.sh` (SHELL) -> Cumulative Risk: **660.82**
- **Archetype:** `file_cluster_4` (Distance: 13.603 IQR)
- **Magnitude:** 2.36 | **LOC:** 26 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9912%), Concurrency (99.9909%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 3.4), `__global_context__` (Impact: 1.6), `cleanup` (Impact: 1.2)

### 2. `src/language-js/parentheses/identifier.js` (JAVASCRIPT) -> Cumulative Risk: **612.09**
- **Archetype:** `file_cluster_4` (Distance: 12.472 IQR)
- **Magnitude:** 111.64 | **LOC:** 113 | **CtrlFlow:** 63.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9972%), Tech Debt (97.0063%), Cognitive Load (89.7882%)
- **Heaviest Functions:** `shouldAddParenthesesToIdentifier` (Impact: 74.6), `startsWithNoLookaheadToken` (Impact: 2.1), `startsWithNoLookaheadToken` (Impact: 2.1)

### 3. `src/language-js/print/class-body.js` (JAVASCRIPT) -> Cumulative Risk: **607.43**
- **Archetype:** `file_cluster_13` (Distance: 11.359 IQR)
- **Magnitude:** 188.06 | **LOC:** 333 | **CtrlFlow:** 67.4% | **Authorship Centralization:** 92.3%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.2862%), Tech Debt (96.0691%), Cognitive Load (87.7891%)
- **Heaviest Functions:** `printClassBody` (Impact: 130.3), `isClassProperty` (Impact: 4.5), `hasNewline` (Impact: 4.4)

### 4. `src/language-js/embed/graphql.js` (JAVASCRIPT) -> Cumulative Risk: **606.74**
- **Archetype:** `file_cluster_4` (Distance: 13.116 IQR)
- **Magnitude:** 109.34 | **LOC:** 124 | **CtrlFlow:** 73.6% | **Authorship Centralization:** 80.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9604%), Concurrency (95.9301%), Cognitive Load (93.1451%)
- **Heaviest Functions:** `printEmbedGraphQL` (Impact: 52.2), `printGraphqlComments` (Impact: 15.2), `isEmbedGraphQL` (Impact: 1.1)

### 5. `src/cli/index.js` (JAVASCRIPT) -> Cumulative Risk: **597.48**
- **Archetype:** `file_cluster_13` (Distance: 10.223 IQR)
- **Magnitude:** 104.18 | **LOC:** 123 | **CtrlFlow:** 53.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.8568%), Tech Debt (99.6245%), Documentation (92.9063%)
- **Heaviest Functions:** `main` (Impact: 58.0), `run` (Impact: 15.9), `printToScreen` (Impact: 4.6)

### 6. `src/language-js/print/member-chain.js` (JAVASCRIPT) -> Cumulative Risk: **574.77**
- **Archetype:** `file_cluster_13` (Distance: 12.03 IQR)
- **Magnitude:** 281.96 | **LOC:** 420 | **CtrlFlow:** 66.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.7792%), State Flux (98.7366%), Verification (80.0%)
- **Heaviest Functions:** `printMemberChain` (Impact: 144.8), `rec` (Impact: 32.4), `printCallArguments` (Impact: 7.0)

### 7. `website/plugins/llms-txt-plugin.mjs` (JAVASCRIPT) -> Cumulative Risk: **564.67**
- **Archetype:** `file_cluster_4` (Distance: 9.832 IQR)
- **Magnitude:** 126.86 | **LOC:** 101 | **CtrlFlow:** 39.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Cognitive Load (92.7046%), Verification (80.0%)
- **Heaviest Functions:** `getMdxFiles` (Impact: 28.9), `llmsTxtPlugin` (Impact: 27.3), `loadContent` (Impact: 25.9)

### 8. `src/language-html/embed.js` (JAVASCRIPT) -> Cumulative Risk: **556.03**
- **Archetype:** `file_cluster_8` (Distance: 10.541 IQR)
- **Magnitude:** 150.72 | **LOC:** 162 | **CtrlFlow:** 57.3% | **Authorship Centralization:** 71.4%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.6479%), Verification (80.0%), Tech Debt (78.025%)
- **Heaviest Functions:** `embed` (Impact: 70.3), `printClosingTagSuffix` (Impact: 24.6), `printClosingTagSuffix` (Impact: 18.9)

### 9. `bin/prettier.cjs` (JAVASCRIPT) -> Cumulative Risk: **548.2**
- **Archetype:** `file_cluster_4` (Distance: 13.295 IQR)
- **Magnitude:** 38.14 | **LOC:** 37 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9868%), Cognitive Load (98.4452%)
- **Heaviest Functions:** `pleaseUpgradeNode` (Impact: 7.7), `runCli` (Impact: 1.9)

### 10. `src/language-js/print/class.js` (JAVASCRIPT) -> Cumulative Risk: **537.09**
- **Archetype:** `file_cluster_13` (Distance: 12.414 IQR)
- **Magnitude:** 263.12 | **LOC:** 372 | **CtrlFlow:** 56.8% | **Authorship Centralization:** 92.3%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9128%), Verification (80.0%), Tech Debt (77.4981%)
- **Heaviest Functions:** `shouldPrintClassInGroupModeWithoutCache` (Impact: 40.2), `printClassWithoutDecorators` (Impact: 38.0), `printClassProperty` (Impact: 24.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `tests/config/install-prettier.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.157 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.026 IQR)
- **Top Global Matches:** file_cluster_8: 9.157, file_cluster_13: 9.234, file_cluster_0: 9.747
- **Magnitude:** 831.22 | **LOC:** 139 | **CtrlFlow:** 48.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (8.8467%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 23`, `args: 10`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 4`
* *Architecture:* `io: 20`, `api: 2`, `import: 9`
* *Defense:* `safety: 5`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.172
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` outdent, node:os, node:perf_hooks, node:child_process, node:path, prettier, picocolors, node:crypto...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/language-css/printer-postcss.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.377 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.94 IQR)
- **Top Global Matches:** file_cluster_8: 10.377, file_cluster_13: 10.812, file_cluster_17: 10.978
- **Magnitude:** 715.18 | **LOC:** 603 | **CtrlFlow:** 71.7% | **Authorship Centralization:** 60.0%
- **Risk Profile:** Cognitive Load (19.9501%), Tech Debt (71.1493%)
**Top Internal Functions/Classes:**
  * `genericPrint` (Impact: 412.3)
  * `isAtWordPlaceholderNode` (Impact: 77.9)
  * `isDetachedRulesetDeclarationNode` (Impact: 73.3)
  * `indent` (Impact: 26.4)
  * `lastLineHasInlineComment` (Impact: 19.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 193`, `structural_boundaries: 76`, `args: 6`, `func_start: 33`
* *Risk/State:* `state_mutation: 9`, `duplicate_logic: 7`
* *Architecture:* `io: 35`, `api: 1`, `import: 14`
* *Defense:* `safety: 48`, `immutability_locks: 30`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.172
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` is-non-empty-array.js, embed.js, loc.js, index.js, misc.js, parenthesized-value-group.js, unexpected-node-error.js, sequence.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/format/flow/conditional-types/conditional-types.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.024 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.607 IQR)
- **Top Global Matches:** file_cluster_8: 8.024, file_cluster_2: 8.716, file_cluster_15: 9.018
- **Magnitude:** 638.02 | **LOC:** 28 | **CtrlFlow:** 45.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (17.4999%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 33`, `args: 4`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 4`
* *Architecture:* `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.172
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/language-js/print/assignment.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.109 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.0 IQR)
- **Top Global Matches:** file_cluster_8: 11.109, file_cluster_13: 11.164, file_cluster_17: 11.36
- **Magnitude:** 568.02 | **LOC:** 469 | **CtrlFlow:** 61.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (37.0799%), Tech Debt (64.2319%)
**Top Internal Functions/Classes:**
  * `printAssignment` (Impact: 322.4)
    * *Intent:* /** * @import AstPath from "../../common/ast-path.js"
  * `shouldBreakAfterOperator` (Impact: 66.0)
  * `isPoorlyBreakableMemberOrCallChain` (Impact: 31.5)
  * `isCallExpressionWithComplexTypeArguments` (Impact: 18.5)
  * `isComplexDestructuring` (Impact: 14.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 107`, `structural_boundaries: 66`, `args: 21`, `func_start: 29`
* *Risk/State:* `state_mutation: 12`, `dead_code: 1`, `planned_debt: 2`, `duplicate_logic: 2`
* *Architecture:* `io: 15`, `api: 3`, `import: 11`
* *Defense:* `safety: 34`, `doc: 4`, `immutability_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.172
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` call-expression.js, get-string-width.js, binaryish.js, ast-path.js, has-leading-own-line-comment.js, call-arguments.js, is-lone-short-argument.js, union-type.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/language-html/utilities/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.089 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.427 IQR)
- **Top Global Matches:** file_cluster_8: 11.089, file_cluster_13: 11.704, file_cluster_7: 11.752
- **Magnitude:** 527.08 | **LOC:** 655 | **CtrlFlow:** 64.1% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (18.7907%), Tech Debt (98.3716%)
**Top Internal Functions/Classes:**
  * `isLeadingSpaceSensitiveNode` (Impact: 46.1)
  * `_isLeadingSpaceSensitiveNode` (Impact: 36.7)
  * `isTrailingSpaceSensitiveNode` (Impact: 36.7)
  * `getNodeCssStyleDisplay` (Impact: 34.9)
  * `inferParserByTypeAttribute` (Impact: 29.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 196`, `structural_boundaries: 110`, `args: 56`, `func_start: 76`
* *Risk/State:* `state_mutation: 9`, `planned_debt: 1`, `duplicate_logic: 9`
* *Architecture:* `api: 3`, `import: 6`
* *Defense:* `safety: 89`, `doc: 4`, `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.172
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` index.js, is-unknown-namespace.js, infer-parser.js, ast-path.js, constants.evaluate.js, index.js, html-whitespace.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/format/flow/flow-repo/promises/promise.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.931 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 6.841 IQR)
- **Top Global Matches:** file_cluster_4: 13.931, file_cluster_11: 14.657, file_cluster_6: 14.939
- **Magnitude:** 514.42 | **LOC:** 227 | **CtrlFlow:** 26.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `reject` (Impact: 6.3)
  * `resolve` (Impact: 4.7)
  * `reject` (Impact: 3.2)
    * *Intent:* ///////////////////////////////////////////////// // == Promise constructor reject() function == // ...
  * `reject` (Impact: 3.2)
    * *Intent:* // TODO: Promise constructor reject(Promise<T>) ~> catch(Promise<T>)
  * `resolve` (Impact: 2.2)
    * *Intent:* // Promise constructor resolve(T); resolve(U); -> then(T|U)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 51`, `args: 41`, `func_start: 13`
* *Risk/State:* `state_mutation: 102`, `planned_debt: 14`, `duplicate_logic: 13`
* *Architecture:* `concurrency: 376`
* *Defense:* `safety: 13`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.172
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/language-css/print/comma-separated-value-group.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.749 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.063 IQR)
- **Top Global Matches:** file_cluster_8: 12.749, file_cluster_17: 12.865, file_cluster_13: 12.91
- **Magnitude:** 507.34 | **LOC:** 568 | **CtrlFlow:** 86.6% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (45.1246%), Tech Debt (78.5409%)
**Top Internal Functions/Classes:**
  * `printCommaSeparatedValueGroup` (Impact: 227.1)
    * *Intent:* /** * @import AstPath from "../../common/ast-path.js" * @import {Doc} from "../../document/index.js"
  * `isInlineValueCommentNode` (Impact: 182.5)
  * `isPossibleFontSize` (Impact: 18.3)
  * `insideAtRuleNode` (Impact: 9.6)
    * *Intent:* // TODO: Improve this part // This `lineSuffix` should be done in `value-comment` print // But since...
  * `insideAtRuleNode` (Impact: 6.4)
    * *Intent:* // Ignore SCSS @forward wildcard suffix
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 116`, `structural_boundaries: 18`, `args: 5`, `func_start: 12`
* *Risk/State:* `state_mutation: 46`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 11`, `api: 2`, `import: 3`
* *Defense:* `safety: 50`, `doc: 8`, `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.172
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` index.js, index.js, loc.js, ast-path.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/format/js/comments/between-head-and-body/empty-statement.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.299 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 1.606 IQR)
- **Top Global Matches:** file_cluster_8: 6.299, file_cluster_7: 7.603, file_cluster_1: 7.797
- **Magnitude:** 451.6 | **LOC:** 100 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (31.7956%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 5`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.172
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/format/js/comments/between-head-and-body/non-block.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.22 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 1.859 IQR)
- **Top Global Matches:** file_cluster_8: 7.22, file_cluster_7: 8.381, file_cluster_1: 8.559
- **Magnitude:** 451.6 | **LOC:** 100 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (31.7956%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `func_start: 45`
* *Risk/State:* `safety_bypasses: 5`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.172
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/language-markdown/parse/micromark/micromark-extension-html-text.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.248 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 3.494 IQR)
- **Top Global Matches:** file_cluster_8: 11.248, file_cluster_7: 11.59, file_cluster_1: 11.824
- **Magnitude:** 425.28 | **LOC:** 813 | **CtrlFlow:** 47.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (7.6763%), Tech Debt (71.7091%)
**Top Internal Functions/Classes:**
  * `tokenizeHtmlText` (Impact: 189.9)
  * `tagOpenAttributeValueBefore` (Impact: 18.8)
  * `tagOpenAttributeValueUnquoted` (Impact: 18.5)
    * *Intent:* /** * After `</x`, in a tag name. * * ```markdown * > | a </b> c * ^ * ```
  * `tagOpenBetween` (Impact: 13.3)
    * *Intent:* /**
  * `tagOpen` (Impact: 11.2)
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 90`, `args: 32`, `func_start: 40`
* *Risk/State:* `state_mutation: 3`, `duplicate_logic: 5`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `safety: 58`, `doc: 69`, `test: 5`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.172
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` micromark-util-types, micromark-util-character, micromark-util-symbol, micromark-factory-space
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/language-markdown/print/preprocess.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.915 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.033 IQR)
- **Top Global Matches:** file_cluster_8: 11.915, file_cluster_17: 12.202, file_cluster_13: 12.262
- **Magnitude:** 416.46 | **LOC:** 603 | **CtrlFlow:** 56.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (22.935%), Tech Debt (79.35%)
**Top Internal Functions/Classes:**
  * `splitTextIntoSentencesLegacy` (Impact: 134.8)
  * `markAlignedList` (Impact: 25.9)
  * `markAncestors` (Impact: 25.2)
  * `getBracketContent` (Impact: 21.6)
  * `preprocess` (Impact: 18.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 93`, `structural_boundaries: 73`, `args: 32`, `func_start: 22`
* *Risk/State:* `state_mutation: 39`, `dead_code: 1`, `duplicate_logic: 5`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `safety: 50`, `doc: 7`, `immutability_locks: 30`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.172
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` html-whitespace.js, utilities.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/language-js/print/flow.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.91 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.717 IQR)
- **Top Global Matches:** file_cluster_13: 9.91, file_cluster_8: 9.94, file_cluster_7: 10.629
- **Magnitude:** 404.58 | **LOC:** 378 | **CtrlFlow:** 55.7% | **Authorship Centralization:** 87.5%
- **Risk Profile:** Cognitive Load (22.0495%), Tech Debt (59.2934%)
**Top Internal Functions/Classes:**
  * `printFlow` (Impact: 322.1)
  * `printTypeParameters` (Impact: 26.6)
  * `print` (Impact: 17.3)
  * `printClassMemberSemicolon` (Impact: 9.2)
  * `print` (Impact: 7.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 136`, `structural_boundaries: 108`, `args: 1`, `func_start: 36`
* *Risk/State:* `state_mutation: 6`, `planned_debt: 2`, `duplicate_logic: 2`
* *Architecture:* `io: 57`, `api: 2`, `import: 38`
* *Defense:* `safety: 11`, `doc: 1`, `test: 3`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.172
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` print-number.js, tuple.js, component.js, key.js, print-string.js, module.js, binary-cast-expression.js, index.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/language-js/print/estree.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.465 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.711 IQR)
- **Top Global Matches:** file_cluster_13: 9.465, file_cluster_8: 9.678, file_cluster_7: 10.168
- **Magnitude:** 385.52 | **LOC:** 345 | **CtrlFlow:** 52.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (23.8485%), Tech Debt (13.7579%)
**Top Internal Functions/Classes:**
  * `printEstree` (Impact: 292.4)
    * *Intent:* /** * @import AstPath from "../../common/ast-path.js" * @import {Doc} from "../../document/index.js"
  * `printTypeAnnotationProperty` (Impact: 39.0)
  * `print` (Impact: 30.7)
  * `isArrayExpression` (Impact: 2.2)
  * `group` (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 132`, `structural_boundaries: 118`, `args: 1`, `func_start: 11`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 9`, `fragile_debt: 1`
* *Architecture:* `io: 52`, `api: 1`, `concurrency: 3`, `import: 39`
* *Defense:* `safety: 4`, `doc: 7`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.172
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` sequence-expression.js, is-meaningful-empty-statement.js, expression-statement.js, member.js, print.js, do-while-statement.js, ast-path.js, try-statement.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/document/utilities/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.068 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.801 IQR)
- **Top Global Matches:** file_cluster_8: 11.068, file_cluster_13: 11.386, file_cluster_17: 11.508
- **Magnitude:** 382.28 | **LOC:** 426 | **CtrlFlow:** 66.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (24.4921%), Tech Debt (64.5049%)
**Top Internal Functions/Classes:**
  * `cleanDocFn` (Impact: 85.4)
  * `mapDoc` (Impact: 41.7)
    * *Intent:* /**
  * `process` (Impact: 36.9)
  * `stripTrailingHardlineFromDoc` (Impact: 35.0)
  * `isEmptyDoc` (Impact: 16.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 123`, `structural_boundaries: 61`, `args: 27`, `func_start: 28`
* *Risk/State:* `state_mutation: 30`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 2`, `import: 6`
* *Defense:* `safety: 30`, `doc: 8`, `test: 1`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.172
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` invalid-doc-error.js, traverse-doc.js, get-doc-type.js, assert-doc.js, index.js, trim-newlines
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/format/js/comments/15661.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.108 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 1.644 IQR)
- **Top Global Matches:** file_cluster_8: 6.108, file_cluster_7: 7.449, file_cluster_1: 7.645
- **Magnitude:** 370.16 | **LOC:** 72 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (14.8454%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 4`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.172
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/language-js/print/jsx.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.863 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.217 IQR)
- **Top Global Matches:** file_cluster_8: 11.863, file_cluster_13: 11.971, file_cluster_17: 12.125
- **Magnitude:** 368.3 | **LOC:** 856 | **CtrlFlow:** 65.0% | **Authorship Centralization:** 94.4%
- **Risk Profile:** Cognitive Load (20.6363%), Tech Debt (99.3307%)
**Top Internal Functions/Classes:**
  * `printJsx` (Impact: 40.1)
  * `printJsxExpressionContainer` (Impact: 35.6)
  * `printJsxOpeningElement` (Impact: 28.8)
    * *Intent:* // Keep (up to one) blank line between tags/expressions/text.
  * `separatorNoWhitespace` (Impact: 20.5)
    * *Intent:* // Note that children always satisfy the rule of fill() content. // - printJsxChildren always return...
  * `separatorWithWhitespace` (Impact: 20.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 141`, `structural_boundaries: 76`, `args: 32`, `func_start: 61`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 55`, `dead_code: 1`, `fragile_debt: 1`, `duplicate_logic: 10`
* *Architecture:* `io: 47`, `api: 3`, `import: 12`
* *Defense:* `safety: 54`, `doc: 10`, `immutability_locks: 46`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.172
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` strip-chain-element-wrappers.js, needs-parentheses.js, get-raw.js, print.js, jsx-whitespace.js, create-type-check-function.js, ast-path.js, node-types.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/language-markdown/print/mdast.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.446 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.031 IQR)
- **Top Global Matches:** file_cluster_8: 11.446, file_cluster_13: 11.503, file_cluster_0: 11.947
- **Magnitude:** 367.84 | **LOC:** 560 | **CtrlFlow:** 60.7% | **Authorship Centralization:** 57.1%
- **Risk Profile:** Cognitive Load (34.8704%), Tech Debt (26.0935%)
**Top Internal Functions/Classes:**
  * `printMdast` (Impact: 226.4)
  * `indent` (Impact: 31.2)
  * `prevOrNextWord` (Impact: 17.9)
    * *Intent:* /** * @import AstPath from "../../common/ast-path.js";
  * `printTitle` (Impact: 10.8)
  * `printChildren` (Impact: 10.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 122`, `structural_boundaries: 79`, `args: 12`, `func_start: 21`
* *Risk/State:* `state_mutation: 24`, `duplicate_logic: 2`
* *Architecture:* `io: 37`, `api: 3`, `import: 17`
* *Defense:* `safety: 46`, `doc: 3`, `immutability_locks: 33`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.172
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` children.js, collapse-white-space, table.js, sentence.js, heading.js, word.js, get-max-continuous-count.js, list.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/format/flow/flow-repo/logical/logical.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.596 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.197 IQR)
- **Top Global Matches:** file_cluster_8: 12.596, file_cluster_7: 12.816, file_cluster_1: 13.011
- **Magnitude:** 354.8 | **LOC:** 515 | **CtrlFlow:** 54.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (38.4156%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `logical3c` (Impact: 7.1)
    * *Intent:* /**
  * `logical7a` (Impact: 7.1)
  * `logical11b` (Impact: 6.3)
  * `logical12b` (Impact: 6.3)
  * `logical7c` (Impact: 6.2)
    * *Intent:* /** * A literal on the left side of ||
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 106`, `structural_boundaries: 88`, `args: 65`, `func_start: 65`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 66`, `orphaned_logic: 65`
* *Architecture:* None
* *Defense:* `doc: 64`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.172
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/format/flow/flow-repo/init/hoisted2.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.981 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.667 IQR)
- **Top Global Matches:** file_cluster_8: 12.981, file_cluster_7: 13.491, file_cluster_13: 13.544
- **Magnitude:** 342.56 | **LOC:** 269 | **CtrlFlow:** 41.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (76.742%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `switch_post_init` (Impact: 12.8)
  * `switch_partial_post_init` (Impact: 11.0)
  * `switch_scoped_init_4` (Impact: 7.3)
  * `if_post_init` (Impact: 5.6)
  * `if_post_init` (Impact: 5.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 67`, `args: 30`, `func_start: 30`
* *Risk/State:* `state_mutation: 193`, `duplicate_logic: 8`, `orphaned_logic: 22`
* *Architecture:* None
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.172
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `website/playground/Playground.jsx` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.05 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.241 IQR)
- **Top Global Matches:** file_cluster_8: 10.05, file_cluster_2: 10.372, file_cluster_13: 10.489
- **Magnitude:** 321.38 | **LOC:** 581 | **CtrlFlow:** 54.2% | **Authorship Centralization:** 84.6%
- **Risk Profile:** Cognitive Load (14.9802%), Tech Debt (65.6752%)
**Top Internal Functions/Classes:**
  * `setup` (Impact: 149.1)
  * `render` (Impact: 73.8)
  * `formatInput` (Impact: 13.4)
  * `setSelectionAsRange` (Impact: 13.0)
  * `insertDummyId` (Impact: 11.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 66`, `args: 28`, `func_start: 19`
* *Risk/State:* `planned_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `io: 1`, `api: 1`, `concurrency: 1`, `import: 16`
* *Defense:* `safety: 35`, `immutability_locks: 53`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.172
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` codeSamples.mjs, dummyId.js, inputs.jsx, language.js, SidebarOptions.jsx, PrettierFormat.js, options.jsx, utilities.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/integration/__tests__/cache.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.267 IQR)
- **Local Micro-Species:** `Cluster 1: Async Testing & I/O Mocks` (Drift: 5.4 IQR)
- **Top Global Matches:** file_cluster_8: 8.267, file_cluster_4: 9.188, file_cluster_7: 9.224
- **Magnitude:** 317.3 | **LOC:** 708 | **CtrlFlow:** 3.9% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (26.3344%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 45.1)
  * `describe` (Impact: 16.3)
  * `describe` (Impact: 16.0)
  * `describe` (Impact: 9.0)
  * `it` (Impact: 6.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 123`, `args: 40`, `func_start: 77`
* *Risk/State:* `safety_bypasses: 2`, `duplicate_logic: 40`, `orphaned_logic: 2`
* *Architecture:* `io: 58`, `concurrency: 112`, `import: 3`
* *Defense:* `test: 157`, `immutability_locks: 58`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.172
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:url, node:path, promises
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/format/js/if/condition-break/boolean-expression.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.156 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.004 IQR)
- **Top Global Matches:** file_cluster_8: 12.156, file_cluster_7: 12.991, file_cluster_0: 13.114
- **Magnitude:** 308.2 | **LOC:** 44 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (34.7787%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* None
* *Defense:* `safety: 27`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.172
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/language-css/utilities/index.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.469 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.241 IQR)
- **Top Global Matches:** file_cluster_8: 11.469, file_cluster_17: 12.041, file_cluster_0: 12.097
- **Magnitude:** 305.36 | **LOC:** 449 | **CtrlFlow:** 60.0% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (15.7903%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `isSCSSMapItemNode` (Impact: 30.6)
  * `isConfigurationNode` (Impact: 18.3)
  * `maybeToLowerCase` (Impact: 16.1)
  * `isSCSSControlDirectiveNode` (Impact: 12.5)
  * `hasParensAroundNode` (Impact: 10.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 114`, `structural_boundaries: 76`, `args: 55`, `func_start: 52`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 3`
* *Architecture:* `io: 18`, `api: 2`
* *Defense:* `safety: 105`, `immutability_locks: 17`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.172
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/language-html/print-preprocess.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.2%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.887 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.006 IQR)
- **Top Global Matches:** file_cluster_8: 10.887, file_cluster_13: 11.445, file_cluster_7: 11.492
- **Magnitude:** 302.2 | **LOC:** 411 | **CtrlFlow:** 72.2% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (18.5091%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `mergeSimpleElementIntoText` (Impact: 40.2)
  * `extractWhitespaces` (Impact: 38.3)
  * `isSimpleElement` (Impact: 35.0)
  * `extractInterpolation` (Impact: 23.9)
  * `mergeNodeIntoText` (Impact: 21.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 91`, `structural_boundaries: 35`, `args: 26`, `func_start: 16`
* *Risk/State:* `state_mutation: 24`
* *Architecture:* `api: 2`, `import: 3`
* *Defense:* `safety: 39`, `doc: 3`, `immutability_locks: 29`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.172
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` index.js, html-whitespace.js, angular-html-parser
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/language-graphql/printer-graphql.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.189 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.31 IQR)
- **Top Global Matches:** file_cluster_8: 10.189, file_cluster_13: 10.574, file_cluster_17: 10.609
- **Magnitude:** 301.2 | **LOC:** 513 | **CtrlFlow:** 62.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (29.1949%), Tech Debt (21.5648%)
**Top Internal Functions/Classes:**
  * `genericPrint` (Impact: 194.7)
  * `printDirectives` (Impact: 18.5)
  * `print` (Impact: 11.4)
  * `printDirectives` (Impact: 8.8)
  * `printSequence` (Impact: 7.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 96`, `structural_boundaries: 58`, `args: 10`, `func_start: 90`
* *Risk/State:* `state_mutation: 27`, `duplicate_logic: 2`
* *Architecture:* `io: 56`, `api: 1`, `import: 10`
* *Defense:* `safety: 14`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.172
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` is-non-empty-array.js, loc.js, unexpected-node-error.js, description.js, index.js, print.js, is-next-line-empty.js, get-visitor-keys.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `tests/format/typescript/decorators-ts/angular.ts` (TYPESCRIPT) | Magnitude: 1.52 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 4, decorators: 3, structural_boundaries: 2, class_start: 1
- `tests/format/vue/html-vue/elastic-header.html` (HTML) | Magnitude: 77.3 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 93, state_mutation: 50, structural_boundaries: 18, args: 9
- `tests/format/js/decorators/class-expression/super-class.js` (JAVASCRIPT) | Magnitude: 11.04 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 6, class_start: 2, decorators: 2
- `tests/format/html/attributes/class-bem2.html` (HTML) | Magnitude: 0.02 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 19, args: 5, decorators: 5, structural_boundaries: 3
- `tests/format/vue/vue/filter.vue` (HTML) | Magnitude: 13.12 | Delta: **0.051 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: decorators: 6, structural_boundaries: 4, args: 4, indent_spaces: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `tests/format/vue/event-binding/non-ascii-expression.vue` (HTML) | Magnitude: 12.08 | Delta: **0.094 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 2, events: 2, listeners: 2, indent_spaces: 2
- `tests/format/vue/event-binding/non-ascii-expression-ts.vue` (HTML) | Magnitude: 2.22 | Delta: **0.152 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 17, events: 14, listeners: 14, indent_spaces: 14
- `tests/format/vue/event-binding/assignment.vue` (HTML) | Magnitude: 15.68 | Delta: **0.303 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 32, events: 30, listeners: 30, structural_boundaries: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `tests/format/flow/flow-repo/call_properties/F.js` (JAVASCRIPT) | Magnitude: 45.3 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 18, args: 9, state_mutation: 9, closures: 3
- `tests/format/js/call/first-argument-expansion/issue-5172.js` (JAVASCRIPT) | Magnitude: 57.98 | Delta: **0.038 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 54, branch: 35, structural_boundaries: 20, safety: 17
- `tests/format/flow/flow-repo/refi/heap.js` (JAVASCRIPT) | Magnitude: 138.78 | Delta: **0.062 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 196, state_mutation: 129, branch: 63, structural_boundaries: 44
- `tests/format/flow/flow-repo/call_properties/B.js` (JAVASCRIPT) | Magnitude: 12.18 | Delta: **0.072 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 16, args: 9, state_mutation: 9, safety_bypasses: 2
- `tests/format/js/for/for-in-with-initializer.js` (JAVASCRIPT) | Magnitude: 36.5 | Delta: **0.141 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 30, structural_boundaries: 15, branch: 13, args: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `tests/format/flow/flow-repo/sealed/function.js` (JAVASCRIPT) | Magnitude: 11.22 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: args: 3, func_start: 3, api: 3, state_mutation: 3
- `tests/format/flow/flow-repo/object_api/object_assign.js` (JAVASCRIPT) | Magnitude: 5.64 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 4, state_mutation: 3, reflection_metaprogramming: 3, args: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/language-css/print/parenthesized-value-group.js` (JAVASCRIPT) | Magnitude: 181.24 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 146, branch: 59, structural_boundaries: 34, safety: 32
- `src/utilities/skip-trailing-comment.js` (JAVASCRIPT) | Magnitude: 8.72 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 7, structural_boundaries: 5, branch: 4, doc: 4
- `scripts/tools/eslint-plugin-prettier-internal-rules/index.js` (JAVASCRIPT) | Magnitude: 0.02 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 23, branch: 15, structural_boundaries: 9, io: 7
- `tests/format/flow/flow-repo/jsx_intrinsics.custom/main.js` (JAVASCRIPT) | Magnitude: 20.24 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 7, state_mutation: 5, indent_spaces: 3, ui_framework: 2
- `src/utilities/ast.js` (JAVASCRIPT) | Magnitude: 45.88 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 29, doc: 14, branch: 11, structural_boundaries: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `tests/format/flow/flow-repo/closure/const.js` (JAVASCRIPT) | Magnitude: 74.72 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 25, structural_boundaries: 21, state_mutation: 17, branch: 13
- `tests/format/js/for/parentheses.js` (JAVASCRIPT) | Magnitude: 81.06 | Delta: **0.062 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 66, branch: 42, structural_boundaries: 40, args: 15
- `tests/format/flow/flow-repo/declare_export/ES6_Default_AnonFunction1.js` (JAVASCRIPT) | Magnitude: 11.52 | Delta: **0.386 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 2, branch: 1, args: 1, api: 1
- `tests/format/flow/flow-repo/declare_export/ES6_Default_AnonFunction2.js` (JAVASCRIPT) | Magnitude: 11.52 | Delta: **0.386 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 2, branch: 1, args: 1, api: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `tests/format/vue/vue/self_closing_style.vue` (HTML) | Magnitude: 13.08 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: encapsulation: 2, structural_boundaries: 1, class_start: 1, api: 1
- `tests/format/typescript/tuple/trailing-comma-for-empty-tuples.ts` (TYPESCRIPT) | Magnitude: 1.1 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 3, branch: 1, generics: 1
- `tests/format/typescript/interface2/comments-ts-and-flow/18216-type-parameters.ts` (TYPESCRIPT) | Magnitude: 1.54 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 12, generics: 12, class_start: 6, ui_framework: 6
- `tests/format/typescript/optional-type/complex.ts` (TYPESCRIPT) | Magnitude: 1.1 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 3, structural_boundaries: 3, generics: 1
- `tests/format/typescript/comments/10260.ts` (TYPESCRIPT) | Magnitude: 1.55 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 16, doc: 12, args: 8, safety: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/language-js/utilities/class-members.js` (JAVASCRIPT) | Magnitude: 31.88 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 50, structural_boundaries: 13, branch: 9, safety: 9
- `tests/format/flow/flow-repo/generators/class_failure.js` (JAVASCRIPT) | Magnitude: 11.88 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 10, structural_boundaries: 7, branch: 5, indent_spaces: 5
- `tests/format/flow/flow-repo/init/let.js` (JAVASCRIPT) | Magnitude: 174.0 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 90, state_mutation: 83, structural_boundaries: 35, branch: 31
- `src/language-js/print/ternary-old.js` (JAVASCRIPT) | Magnitude: 147.88 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 159, branch: 56, safety: 30, immutability_locks: 30
- `tests/format/flow/flow-repo/this_type/self.js` (JAVASCRIPT) | Magnitude: 4.8 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: structural_boundaries: 4, func_start: 3, indent_spaces: 3, args: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `src/standalone.d.ts` (TYPESCRIPT) | Magnitude: 7.92 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 5, args: 4, func_start: 4, api: 4
- `tests/format/flow/flow-repo/react/proptypes_sealed.js` (JAVASCRIPT) | Magnitude: 5.44 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 9, args: 2, func_start: 2, state_mutation: 2
- `tests/format/flow/flow-repo/taint/use-types.js` (JAVASCRIPT) | Magnitude: 21.72 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 7, args: 7, func_start: 7, indent_spaces: 7
- `tests/format/js/assignment/chain-two-segments.js` (JAVASCRIPT) | Magnitude: 6.8 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 3, indent_spaces: 3, branch: 1, structural_boundaries: 1
- `tests/format/flow/flow-repo/union/issue-256.js` (JAVASCRIPT) | Magnitude: 3.12 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 2, args: 2, closures: 2, func_start: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/config/resolve-config.js` (JAVASCRIPT) | Magnitude: 84.32 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 83, structural_boundaries: 23, branch: 21, concurrency: 18
- `tests/format/js/method-chain/comment.js` (JAVASCRIPT) | Magnitude: 29.52 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 19, state_mutation: 11, concurrency: 8, structural_boundaries: 6
- `tests/format/js/yield/arrow.js` (JAVASCRIPT) | Magnitude: 14.6 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 6, args: 4, lazy_evaluation: 4, indent_spaces: 3
- `src/config/prettier-config/loaders.js` (JAVASCRIPT) | Magnitude: 77.7 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 65, structural_boundaries: 31, concurrency: 20, branch: 16
- `tests/format/js/async/conditional-expression.js` (JAVASCRIPT) | Magnitude: 19.64 | Delta: **0.04 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: concurrency: 9, indent_spaces: 6, branch: 4, structural_boundaries: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `src/utilities/try-combinations.js` (JAVASCRIPT) | Magnitude: 11.84 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 9, doc: 4, branch: 3, state_mutation: 3
- `tests/format/flow/flow-repo/typecast/typecast.js` (JAVASCRIPT) | Magnitude: 20.24 | Delta: **0.105 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 8, state_mutation: 5, args: 3
- `tests/format/css/comments/types.css` (CSS) | Magnitude: 0.53 | Delta: **0.349 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: planned_debt: 3, doc: 2
- `tests/format/flow/flow-repo/type-at-pos/function_expressions.js` (JAVASCRIPT) | Magnitude: 4.24 | Delta: **0.378 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: immutability_locks: 4, indent_spaces: 4, func_start: 3, structural_boundaries: 2
- `tests/format/js/explicit-resource-management/valid-for-await-using-binding-escaped-of-of.js` (JAVASCRIPT) | Magnitude: 10.52 | Delta: **0.526 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: dead_code: 1, planned_debt: 1, sec_reflection_metaprogramming: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `tests/format/flow/flow-repo/declare_export/ES6_ExportAllFrom_Source1.js` (JAVASCRIPT) | Magnitude: 12.52 | Delta: **0.062 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 2, api: 1, state_mutation: 1, doc: 1
- `tests/format/flow/flow-repo/declare_export/ES6_ExportAllFrom_Source2.js` (JAVASCRIPT) | Magnitude: 12.52 | Delta: **0.062 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 2, api: 1, state_mutation: 1, doc: 1
- `tests/format/flow/flow-repo/es6modules/ES6_ExportAllFrom_Source1.js` (JAVASCRIPT) | Magnitude: 12.52 | Delta: **0.062 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 2, api: 1, state_mutation: 1, doc: 1
- `tests/format/flow/flow-repo/es6modules/ES6_ExportAllFrom_Source2.js` (JAVASCRIPT) | Magnitude: 12.52 | Delta: **0.062 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 2, api: 1, state_mutation: 1, doc: 1
- `tests/format/flow/flow-repo/es6modules/ES6_ExportFrom_Source1.js` (JAVASCRIPT) | Magnitude: 12.52 | Delta: **0.062 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 2, api: 1, state_mutation: 1, doc: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `tests/format/jsx/optional-chaining/optional-chaining.jsx` (JAVASCRIPT) | Magnitude: 33.32 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 36, branch: 12, safety: 12, structural_boundaries: 9
- `src/language-js/comments/can-attach-comment.js` (JAVASCRIPT) | Magnitude: 16.98 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 58, branch: 47, safety: 34, doc: 21
- `tests/format/flow/flow-repo/node_tests/buffer/buffer.js` (JAVASCRIPT) | Magnitude: 27.72 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 13, state_mutation: 12, args: 9, comprehensions: 6
- `tests/format/flow/flow-repo/refi/void_tests.js` (JAVASCRIPT) | Magnitude: 72.8 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 63, indent_spaces: 55, branch: 31, structural_boundaries: 20
- `tests/format/flow/flow-repo/this_type/import.js` (JAVASCRIPT) | Magnitude: 5.5 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 12, memory_alloc: 8, api: 3, import: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `tests/format/flow/flow-repo/binding/tdz.js` (JAVASCRIPT) | Magnitude: 8.56 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: func_start: 6, structural_boundaries: 4, indent_spaces: 4, args: 3
- `tests/format/typescript/compiler/privacyGloImport.ts` (TYPESCRIPT) | Magnitude: 7.94 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 105, indent_spaces: 77, state_mutation: 37, api: 33
- `tests/format/flow/flow-repo/strict/obj.js` (JAVASCRIPT) | Magnitude: 14.56 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: structural_boundaries: 2, state_mutation: 2, api: 1, dead_code: 1
- `tests/format/flow/flow-repo/strict/fun.js` (JAVASCRIPT) | Magnitude: 3.86 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: structural_boundaries: 2, dead_code: 2, args: 1, func_start: 1
- `tests/format/js/discard-binding/object-pattern.js` (JAVASCRIPT) | Magnitude: 5.84 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: safety_bypasses: 16, indent_spaces: 9, branch: 4, args: 3

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/language-js/comments/handle-comments.js` -> Churn: **52.13%** | Cog Load: 16.3072% | Debt: 99.7825%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `tests/config/install-prettier.js` -> **fisker Cheung** (100.0% isolated ownership) | Magnitude: 831.22
- `src/language-js/print/assignment.js` -> **fisker Cheung** (100.0% isolated ownership) | Magnitude: 568.02
- `tests/format/flow/flow-repo/promises/promise.js` -> **fisker Cheung** (100.0% isolated ownership) | Magnitude: 514.42
- `tests/format/js/comments/between-head-and-body/empty-statement.js` -> **fisker Cheung** (100.0% isolated ownership) | Magnitude: 451.6
- `tests/format/js/comments/between-head-and-body/non-block.js` -> **fisker Cheung** (100.0% isolated ownership) | Magnitude: 451.6

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `scripts/tools/eslint-plugin-prettier-internal-rules/test.js` -> **Severity: 31.934** (Blast Radius: 1.786 * Doc Risk: 17.8804%)
- `src/language-js/embed/css.js` -> **Severity: 24.282** (Blast Radius: 1.358 * Doc Risk: 17.8804%)
- `src/document/builders/index.js` -> **Severity: 17.2** (Blast Radius: 0.172 * Doc Risk: 100.0%)
- `src/document/builders/types.js` -> **Severity: 17.2** (Blast Radius: 0.172 * Doc Risk: 100.0%)
- `src/language-js/parse/utilities/source-types.js` -> **Severity: 17.2** (Blast Radius: 0.172 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
