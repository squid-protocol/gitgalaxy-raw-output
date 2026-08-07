# ARCHITECTURAL_BRIEF: swc
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_typescript/swc` |
| **Timestamp** | `2026-08-07T04:19:38.982389+00:00` |
| **Scan Duration** | `100.97s` |
| **Git Branch** | `main` |
| **Git Commit** | `52303ecaacdec85cac9b3200e1ab1dd3863d3f5c` |
| **Git Remote** | `https://github.com/swc-project/swc.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 35157 malicious artifacts.

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
| Total Artifacts | 82587 |
| Analyzed Artifacts (Scanned) | 54285 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 28302 |
| Total LOC | 2996819 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 65.7% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3546 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 65 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 27284 | 655991 | 50.3% |
| JSON | 17567 | 1801564 | 32.4% |
| TYPESCRIPT | 6475 | 169263 | 11.9% |
| RUST | 1305 | 319801 | 2.4% |
| CSS | 1144 | 49119 | 2.1% |
| PLAINTEXT | 195 | 1 | 0.4% |
| MARKDOWN | 128 | 0 | 0.2% |
| SHELL | 90 | 917 | 0.2% |
| XML | 90 | 0 | 0.2% |
| YAML | 4 | 75 | 0.0% |
| PYTHON | 3 | 88 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `7.749`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 47933 | 88.3% |
| file_cluster_13 | 2912 | 5.4% |
| file_cluster_0 | 872 | 1.6% |
| file_cluster_4 | 687 | 1.3% |
| file_cluster_16 | 564 | 1.0% |
| file_cluster_17 | 348 | 0.6% |
| file_cluster_2 | 260 | 0.5% |
| file_cluster_11 | 123 | 0.2% |
| file_cluster_15 | 99 | 0.2% |
| file_cluster_7 | 61 | 0.1% |
| file_cluster_12 | 59 | 0.1% |
| file_cluster_9 | 36 | 0.1% |
| file_cluster_1 | 5 | 0.0% |
| file_cluster_6 | 2 | 0.0% |
| Unknown | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 322 | 0.6% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 28302*

**Composition by Extension & Reason:**
- `.js`: 5037x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1632x Excluded: Neighborhood Micro-Mass Limit Exceeded, 20x Excluded (Saturation: Line 3 exceeds 500 chars)
- `.json`: 2998x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 144x Excluded: Neighborhood Micro-Mass Limit Exceeded, 7x Excluded (Static Asset Blob without Intent: 1155 LOC)
- `.rust-debug`: 3510x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 456x Excluded (Unsupported Extension: '.rust-debug')
- `.ts`: 2950x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 533x Excluded: Neighborhood Micro-Mass Limit Exceeded, 3x Excluded (Saturation: Line 5 exceeds 500 chars)
- `.swc-stderr`: 2856x Excluded (Unsupported Extension: '.swc-stderr'), 361x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.html`: 2676x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.stderr`: 1754x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 166x Excluded (Unsupported Extension: '.stderr')
- `.css`: 742x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 33x Excluded: Neighborhood Micro-Mass Limit Exceeded, 1x Excluded (Saturation: Line 98 exceeds 500 chars)
- `.debug`: 230x Excluded (Unsupported Extension: '.debug'), 5x Unsupported Format (.debug)
- `.toml`: 149x Unsupported Format (.toml), 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 5x Excluded (Unsupported Extension: '.toml')
- `.mjs`: 106x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 39 exceeds 500 chars)
- `no_extension`: 101x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Unsupported Format (.undeterminable)
- `.stdout`: 103x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.map`: 72x Excluded (Unsupported Extension: '.map'), 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.snap`: 59x Excluded (Unsupported Extension: '.snap'), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 9.0 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 25.4 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 1.2 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 0.3 | 0.0 | 0.0 |
| API Exposure | 0.0 | 20.8 | 1.0 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 2.9 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 2.3 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 62.0 | 66.7 | 100.0 |
| Instability Exposure | 0.0 | 0.7 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 1.9 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 0.9 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 68.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `crates/swc_bundler/tests/fixture/deno-9591/output/entry.inlined.ts` (Hits: 278)
- `crates/swc_bundler/tests/fixture/deno-9591/output/entry.ts` (Hits: 278)
- `crates/swc_bundler/tests/fixture/deno-9620/case1/output/entry.inlined.ts` (Hits: 207)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **react.js** (`crates/swc_ecma_minifier/benches/full/react.js`) — 397 inbound connections
2. **ts.ts** (`crates/swc/tests/projects/issue-655/ts.ts`) — 149 inbound connections
3. **0.js** (`crates/swc_sourcemap/tests/fixtures/ram_bundle/file_bundle_1/js-modules/0.js`) — 127 inbound connections
4. **Token.ts** (`crates/swc_bundler/tests/deno-exec/deno-8224/haystack-core/input/filter/Token.ts`) — 36 inbound connections
5. **HVal.ts** (`crates/swc_bundler/tests/deno-exec/deno-8224/haystack-core/input/core/HVal.ts`) — 30 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **lib.rs** (`crates/swc_ecma_ast/src/lib.rs`) — 441 outbound dependencies
2. **typescript.rs** (`crates/swc_estree_compat/src/babelify/typescript.rs`) — 158 outbound dependencies
3. **output.js** (`crates/swc_ecma_preset_env/tests/fixtures/corejs2/entry-shippedProposals/output.js`) — 149 outbound dependencies
4. **lib.rs** (`crates/swc_es_ast/src/lib.rs`) — 145 outbound dependencies
5. **expr.rs** (`crates/swc_estree_compat/src/swcify/expr.rs`) — 123 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `r1` (@ `crates/swc_ecma_minifier/tests/fixture/next/react-pdf-renderer/output.js`) -> Impact: **1628.5** | LOC: 873
- `Yd` (@ `crates/swc_ecma_minifier/tests/fixture/next/asmjs/1/output.js`) -> Impact: **1229.9** | LOC: 850
- `getTagNamespace` (@ `crates/swc_ecma_minifier/benches/full/vue.js`) -> Impact: **1181.3** | LOC: 1786
  * *Intent:* /* */
- `initExtend` (@ `crates/swc_ecma_minifier/benches/full/vue.js`) -> Impact: **1117.8** | LOC: 1796
- `queueActivatedComponent` (@ `crates/swc_ecma_minifier/benches/full/vue.js`) -> Impact: **1068.3** | LOC: 1886
- `Yd` (@ `crates/swc_ecma_minifier/tests/fixture/next/asmjs/1/input.js`) -> Impact: **1027.0** | LOC: 1038
- `e` (@ `crates/swc_ecma_minifier/tests/fixture/next/react-pdf-renderer/output.js`) -> Impact: **1000.5** | LOC: 889
- `tighten_body` (@ `crates/swc_ecma_minifier/tests/benches-full/terser.js`) -> Impact: **965.4** | LOC: 568
- `initProps` (@ `crates/swc_ecma_minifier/benches/full/vue.js`) -> Impact: **949.7** | LOC: 1813
- `addChangeToHistory` (@ `crates/swc_ecma_minifier/tests/fixture/next/feedback-2/codemirror/input.js`) -> Impact: **941.2** | LOC: 1651

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `crates/swc/tests/tsc-references` | 8596 | 164808.36 | 10.67% | 0.0% |
| `crates/swc_ecma_parser/tests/tsc` | 7322 | 78444.52 | 4.96% | 0.0% |
| `crates/swc_es_parser/tests/snapshots/ecma_reuse/tsc` | 4277 | 70222.26 | 5.8% | 0.0% |
| `crates/swc_ecma_minifier/tests/benches-full` | 4 | 47518.38 | 42.42% | 0.0% |
| `crates/swc_ecma_minifier/benches/full` | 5 | 35840.12 | 77.48% | 81.66% |
| `crates/swc_es_parser/tests/snapshots/ecma_reuse/test262-parser/pass` | 1824 | 28306.46 | 11.34% | 0.0% |
| `crates/swc_ecma_minifier/tests/projects/files` | 7 | 17352.24 | 63.2% | 0.0% |
| `crates/swc_ecma_parser/benches/files` | 6 | 16596.18 | 60.63% | 82.61% |
| `crates/swc_es_parser/benches/files` | 6 | 16596.18 | 60.63% | 82.61% |
| `crates/swc_ecma_minifier/tests/projects/output` | 4 | 13177.06 | 75.4% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `packages/core/src/index.ts` -> **100.0%** Exposure
- `packages/core/src/util.ts` -> **100.0%** Exposure
- `packages/minifier/src/binding.d.ts` -> **100.0%** Exposure
- `bindings/swc_cli/src/main.rs` -> **100.0%** Exposure
- `crates/hstr/src/global_store.rs` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `crates/swc_ecma_transforms_module/tests/fixture/common/amd-triple-slash-directive/1/input.ts` -> **100.0%** Exposure
- `crates/swc_ecma_transforms_module/tests/fixture/common/amd-triple-slash-directive/1/output.cts` -> **100.0%** Exposure
- `crates/swc_ecma_transforms_module/tests/fixture/common/amd-triple-slash-directive/2/input.ts` -> **100.0%** Exposure
- `crates/swc_ecma_transforms_module/tests/fixture/common/amd-triple-slash-directive/2/output.cts` -> **100.0%** Exposure
- `crates/swc_ecma_transforms_module/tests/fixture/common/amd-triple-slash-directive/3/input.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `crates/swc_ecma_minifier/benches/full/d3.js` -> **150** Orphaned Functions | **855** Duplicates
- `crates/swc_ecma_minifier/tests/benches-full/d3.js` -> **215** Orphaned Functions | **703** Duplicates
- `crates/swc_ecma_minifier/tests/fixture/next/wrap-contracts/output.js` -> **0** Orphaned Functions | **803** Duplicates
- `crates/swc_ecma_minifier/tests/fixture/next/react-pdf-renderer/output.js` -> **0** Orphaned Functions | **562** Duplicates
- `crates/swc_ecma_minifier/tests/benches-full/three.js` -> **0** Orphaned Functions | **416** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`crates/swc_ecma_transforms_optimization/src/simplify/expr/tests.rs`** -> AI Confidence: **99.48%**
2. **`crates/swc_ecma_preset_env/tests/fixtures/corejs2/entry-require/output.js`** -> AI Confidence: **99.48%**
3. **`crates/swc_ecma_preset_env/tests/fixtures/corejs3/entry-require/output.js`** -> AI Confidence: **99.48%**
4. **`crates/swc_bundler/tests/deno-exec/deno-8224/haystack-core/input/core/ZincReader.ts`** -> AI Confidence: **99.39%**
5. **`crates/swc_ecma_transforms_optimization/src/simplify/branch/tests.rs`** -> AI Confidence: **99.39%**
6. **`crates/swc/tests/tsc-references/exportAsNamespace4(module=umd).1.normal.js`** -> AI Confidence: **99.34%**
7. **`crates/swc_css_minifier/src/compressor/easing_function.rs`** -> AI Confidence: **99.32%**
8. **`crates/swc/tests/tsc-references/defaultExportInAwaitExpression01.1.normal.js`** -> AI Confidence: **99.32%**
9. **`crates/swc/tests/tsc-references/exportAsNamespace1(module=umd).1.normal.js`** -> AI Confidence: **99.32%**
10. **`crates/swc/tests/tsc-references/exportAsNamespace2(module=umd).1.normal.js`** -> AI Confidence: **99.32%**
11. **`crates/swc/tests/tsc-references/exportAsNamespace3(module=umd).1.normal.js`** -> AI Confidence: **99.32%**
12. **`crates/swc/tests/tsc-references/ifDoWhileStatements.1.normal.js`** -> AI Confidence: **99.32%**
13. **`crates/swc/tests/tsc-references/importCallExpressionNestedUMD2.2.minified.js`** -> AI Confidence: **99.32%**
14. **`crates/swc_ecma_transforms_module/tests/fixture/common/disable-strict-mode-strict-mode-false/output.umd.js`** -> AI Confidence: **99.32%**
15. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop-node/imports/output.umd.js`** -> AI Confidence: **99.32%**
16. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop/imports/output.umd.js`** -> AI Confidence: **99.32%**
17. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-5054/1/output.umd.js`** -> AI Confidence: **99.32%**
18. **`crates/swc_ecma_transforms_module/tests/fixture/common/lazy/import-only-allowed-from-object-config/output.umd.js`** -> AI Confidence: **99.32%**
19. **`crates/swc/tests/fixture/issues-4xxx/4108/1/output/index.ts`** -> AI Confidence: **99.31%**
20. **`crates/swc/tests/fixture/next.js/server/render/1/input/index.tsx`** -> AI Confidence: **99.31%**
21. **`crates/swc_bundler/tests/deno-exec/deno-8224/haystack-core/input/core/HDict.ts`** -> AI Confidence: **99.31%**
22. **`crates/swc_bundler/tests/deno-exec/deno-8224/haystack-core/input/core/HGrid.ts`** -> AI Confidence: **99.31%**
23. **`crates/swc_bundler/tests/deno-exec/deno-8224/haystack-core/input/core/HList.ts`** -> AI Confidence: **99.31%**
24. **`crates/swc_bundler/tests/deno-exec/deno-8224/haystack-core/input/core/HNamespace.ts`** -> AI Confidence: **99.31%**
25. **`crates/swc_bundler/tests/deno-exec/deno-8224/haystack-core/input/core/HNormalizer.ts`** -> AI Confidence: **99.31%**
26. **`crates/swc_bundler/tests/deno-exec/deno-8224/haystack-core/input/core/HNum.ts`** -> AI Confidence: **99.31%**
27. **`crates/swc_bundler/tests/deno-exec/deno-8224/haystack-core/input/core/HSpan.ts`** -> AI Confidence: **99.31%**
28. **`crates/swc_bundler/tests/deno-exec/deno-8224/haystack-core/input/core/util.ts`** -> AI Confidence: **99.31%**
29. **`crates/swc_bundler/tests/deno-exec/deno-8224/haystack-core/input/filter/FilterParser.ts`** -> AI Confidence: **99.31%**
30. **`crates/swc_bundler/tests/deno-exec/deno-9307/.case1/input/src/openApiToGraphQL/index.ts`** -> AI Confidence: **99.31%**
31. **`crates/swc_ecma_parser/tests/typescript/next/stack-overflow/1/input.ts`** -> AI Confidence: **99.31%**
32. **`crates/swc_ecma_transforms_typescript/tests/fixture/next/server/render/1/input.tsx`** -> AI Confidence: **99.31%**
33. **`packages/core/src/index.ts`** -> AI Confidence: **99.31%**
34. **`bindings/binding_es_ast_viewer/src/lib.rs`** -> AI Confidence: **99.31%**
35. **`crates/dbg-swc/src/es/minifier/ensure_size.rs`** -> AI Confidence: **99.31%**
36. **`crates/dbg-swc/src/es/minifier/next/check_size.rs`** -> AI Confidence: **99.31%**
37. **`crates/hstr/src/wtf8/not_quite_std.rs`** -> AI Confidence: **99.31%**
38. **`crates/swc/src/lib.rs`** -> AI Confidence: **99.31%**
39. **`crates/swc_bundler/src/modules/sort/stmt.rs`** -> AI Confidence: **99.31%**
40. **`crates/swc_bundler/src/modules/sort/tests.rs`** -> AI Confidence: **99.31%**
41. **`crates/swc_cli_impl/tests/issues.rs`** -> AI Confidence: **99.31%**
42. **`crates/swc_common/src/errors/emitter.rs`** -> AI Confidence: **99.31%**
43. **`crates/swc_css_codegen/src/lib.rs`** -> AI Confidence: **99.31%**
44. **`crates/swc_css_compat/src/compiler/color_hwb.rs`** -> AI Confidence: **99.31%**
45. **`crates/swc_css_compat/src/compiler/custom_media.rs`** -> AI Confidence: **99.31%**
46. **`crates/swc_css_minifier/src/compressor/color.rs`** -> AI Confidence: **99.31%**
47. **`crates/swc_css_minifier/src/compressor/media.rs`** -> AI Confidence: **99.31%**
48. **`crates/swc_css_parser/src/lexer/mod.rs`** -> AI Confidence: **99.31%**
49. **`crates/swc_css_parser/src/parser/at_rules/mod.rs`** -> AI Confidence: **99.31%**
50. **`crates/swc_css_parser/src/parser/values_and_units/mod.rs`** -> AI Confidence: **99.31%**
51. **`crates/swc_css_prefixer/src/prefixer.rs`** -> AI Confidence: **99.31%**
52. **`crates/swc_ecma_ast/src/source_map.rs`** -> AI Confidence: **99.31%**
53. **`crates/swc_ecma_codegen/src/class.rs`** -> AI Confidence: **99.31%**
54. **`crates/swc_ecma_codegen/src/decl.rs`** -> AI Confidence: **99.31%**
55. **`crates/swc_ecma_codegen/src/lib.rs`** -> AI Confidence: **99.31%**
56. **`crates/swc_ecma_codegen/src/lit.rs`** -> AI Confidence: **99.31%**
57. **`crates/swc_ecma_codegen/src/object.rs`** -> AI Confidence: **99.31%**
58. **`crates/swc_ecma_codegen/src/scope_helpers.rs`** -> AI Confidence: **99.31%**
59. **`crates/swc_ecma_codegen/src/stmt.rs`** -> AI Confidence: **99.31%**
60. **`crates/swc_ecma_compat_es2022/src/class_properties/member_init.rs`** -> AI Confidence: **99.31%**
61. **`crates/swc_ecma_lexer/src/common/parser/class_and_fn.rs`** -> AI Confidence: **99.31%**
62. **`crates/swc_ecma_lexer/src/common/parser/expr.rs`** -> AI Confidence: **99.31%**
63. **`crates/swc_ecma_lexer/src/common/parser/ident.rs`** -> AI Confidence: **99.31%**
64. **`crates/swc_ecma_lexer/src/common/parser/jsx.rs`** -> AI Confidence: **99.31%**
65. **`crates/swc_ecma_lexer/src/common/parser/module_item.rs`** -> AI Confidence: **99.31%**
66. **`crates/swc_ecma_lexer/src/common/parser/object.rs`** -> AI Confidence: **99.31%**
67. **`crates/swc_ecma_lexer/src/common/parser/pat.rs`** -> AI Confidence: **99.31%**
68. **`crates/swc_ecma_lexer/src/common/parser/stmt.rs`** -> AI Confidence: **99.31%**
69. **`crates/swc_ecma_lexer/src/common/parser/typescript.rs`** -> AI Confidence: **99.31%**
70. **`crates/swc_ecma_lexer/src/lexer/mod.rs`** -> AI Confidence: **99.31%**
71. **`crates/swc_ecma_lexer/src/lexer/state.rs`** -> AI Confidence: **99.31%**
72. **`crates/swc_ecma_lexer/src/lexer/table.rs`** -> AI Confidence: **99.31%**
73. **`crates/swc_ecma_lints/src/rules/default_param_last.rs`** -> AI Confidence: **99.31%**
74. **`crates/swc_ecma_lints/src/rules/no_throw_literal.rs`** -> AI Confidence: **99.31%**
75. **`crates/swc_ecma_lints/src/rules/use_is_nan.rs`** -> AI Confidence: **99.31%**
76. **`crates/swc_ecma_loader/src/resolvers/tsc.rs`** -> AI Confidence: **99.31%**
77. **`crates/swc_ecma_minifier/src/compress/hoist_decls.rs`** -> AI Confidence: **99.31%**
78. **`crates/swc_ecma_minifier/src/compress/optimize/conditionals.rs`** -> AI Confidence: **99.31%**
79. **`crates/swc_ecma_minifier/src/compress/optimize/evaluate.rs`** -> AI Confidence: **99.31%**
80. **`crates/swc_ecma_minifier/src/compress/optimize/inline.rs`** -> AI Confidence: **99.31%**
81. **`crates/swc_ecma_minifier/src/compress/optimize/loops.rs`** -> AI Confidence: **99.31%**
82. **`crates/swc_ecma_minifier/src/compress/optimize/ops.rs`** -> AI Confidence: **99.31%**
83. **`crates/swc_ecma_minifier/src/compress/optimize/sequences.rs`** -> AI Confidence: **99.31%**
84. **`crates/swc_ecma_minifier/src/compress/optimize/unused.rs`** -> AI Confidence: **99.31%**
85. **`crates/swc_ecma_minifier/src/compress/pure/bools.rs`** -> AI Confidence: **99.31%**
86. **`crates/swc_ecma_minifier/src/compress/pure/dead_code.rs`** -> AI Confidence: **99.31%**
87. **`crates/swc_ecma_minifier/src/compress/pure/loops.rs`** -> AI Confidence: **99.31%**
88. **`crates/swc_ecma_minifier/src/compress/pure/member_expr.rs`** -> AI Confidence: **99.31%**
89. **`crates/swc_ecma_minifier/src/compress/pure/misc.rs`** -> AI Confidence: **99.31%**
90. **`crates/swc_ecma_minifier/src/compress/util/mod.rs`** -> AI Confidence: **99.31%**
91. **`crates/swc_ecma_minifier/src/compress/util/tests.rs`** -> AI Confidence: **99.31%**
92. **`crates/swc_ecma_minifier/src/pass/mangle_names/preserver.rs`** -> AI Confidence: **99.31%**
93. **`crates/swc_ecma_minifier/src/pass/postcompress.rs`** -> AI Confidence: **99.31%**
94. **`crates/swc_ecma_minifier/src/program_data.rs`** -> AI Confidence: **99.31%**
95. **`crates/swc_ecma_parser/examples/parse.rs`** -> AI Confidence: **99.31%**
96. **`crates/swc_ecma_parser/src/legacy.rs`** -> AI Confidence: **99.31%**
97. **`crates/swc_ecma_parser/src/lexer/mod.rs`** -> AI Confidence: **99.31%**
98. **`crates/swc_ecma_parser/src/lexer/table.rs`** -> AI Confidence: **99.31%**
99. **`crates/swc_ecma_parser/src/parser/class_and_fn.rs`** -> AI Confidence: **99.31%**
100. **`crates/swc_ecma_parser/src/parser/expr.rs`** -> AI Confidence: **99.31%**
101. **`crates/swc_ecma_parser/src/parser/ident.rs`** -> AI Confidence: **99.31%**
102. **`crates/swc_ecma_parser/src/parser/jsx.rs`** -> AI Confidence: **99.31%**
103. **`crates/swc_ecma_parser/src/parser/module_item.rs`** -> AI Confidence: **99.31%**
104. **`crates/swc_ecma_parser/src/parser/object.rs`** -> AI Confidence: **99.31%**
105. **`crates/swc_ecma_parser/src/parser/pat.rs`** -> AI Confidence: **99.31%**
106. **`crates/swc_ecma_parser/src/parser/typescript.rs`** -> AI Confidence: **99.31%**
107. **`crates/swc_ecma_parser/tests/typescript.rs`** -> AI Confidence: **99.31%**
108. **`crates/swc_ecma_regexp/src/parser/pattern_parser/pattern_parser_impl.rs`** -> AI Confidence: **99.31%**
109. **`crates/swc_ecma_regexp_ast/src/display.rs`** -> AI Confidence: **99.31%**
110. **`crates/swc_ecma_transformer/src/options/mod.rs`** -> AI Confidence: **99.31%**
111. **`crates/swc_ecma_transforms_compat/tests/es2015_for_of.rs`** -> AI Confidence: **99.31%**
112. **`crates/swc_ecma_transforms_compat/tests/es2020_optional_chaining.rs`** -> AI Confidence: **99.31%**
113. **`crates/swc_ecma_transforms_optimization/src/simplify/branch/mod.rs`** -> AI Confidence: **99.31%**
114. **`crates/swc_ecma_transforms_optimization/src/simplify/expr/mod.rs`** -> AI Confidence: **99.31%**
115. **`crates/swc_ecma_transforms_optimization/src/simplify/inlining/scope.rs`** -> AI Confidence: **99.31%**
116. **`crates/swc_ecma_transforms_optimization/tests/simplify.rs`** -> AI Confidence: **99.31%**
117. **`crates/swc_ecma_transforms_optimization/tests/simplify_inlining.rs`** -> AI Confidence: **99.31%**
118. **`crates/swc_ecma_transforms_react/src/pure_annotations/mod.rs`** -> AI Confidence: **99.31%**
119. **`crates/swc_es_parser/src/lexer.rs`** -> AI Confidence: **99.31%**
120. **`crates/swc_es_parser/src/parser.rs`** -> AI Confidence: **99.31%**
121. **`crates/swc_es_parser/tests/typescript.rs`** -> AI Confidence: **99.31%**
122. **`crates/swc_es_semantics/src/analyzer.rs`** -> AI Confidence: **99.31%**
123. **`crates/swc_es_transforms/tests/tsc_corpus.rs`** -> AI Confidence: **99.31%**
124. **`crates/swc_estree_compat/src/babelify/operators.rs`** -> AI Confidence: **99.31%**
125. **`crates/swc_estree_compat/src/babelify/pat.rs`** -> AI Confidence: **99.31%**
126. **`crates/swc_html_codegen/src/lib.rs`** -> AI Confidence: **99.31%**
127. **`crates/swc_html_minifier/src/lib.rs`** -> AI Confidence: **99.31%**
128. **`crates/swc_sourcemap/src/detector.rs`** -> AI Confidence: **99.31%**
129. **`crates/swc_typescript/src/fast_dts/class.rs`** -> AI Confidence: **99.31%**
130. **`crates/swc_typescript/src/fast_dts/decl.rs`** -> AI Confidence: **99.31%**
131. **`crates/swc_typescript/src/fast_dts/enum.rs`** -> AI Confidence: **99.31%**
132. **`crates/swc_typescript/src/fast_dts/inferrer.rs`** -> AI Confidence: **99.31%**
133. **`crates/swc_typescript/src/fast_dts/mod.rs`** -> AI Confidence: **99.31%**
134. **`crates/swc_typescript/src/fast_dts/types.rs`** -> AI Confidence: **99.31%**
135. **`crates/swc_typescript/src/fast_dts/util/ast_ext.rs`** -> AI Confidence: **99.31%**
136. **`tools/swc-releaser/src/main.rs`** -> AI Confidence: **99.31%**
137. **`xtask/src/npm/util.rs`** -> AI Confidence: **99.31%**
138. **`crates/swc/tests/fixture/issues-1xxx/1333/case2/output/index.js`** -> AI Confidence: **99.31%**
139. **`crates/swc/tests/fixture/issues-1xxx/1333/case3/output/index.js`** -> AI Confidence: **99.31%**
140. **`crates/swc/tests/tsc-references/usingDeclarations.1(target=es5).1.normal.js`** -> AI Confidence: **99.31%**
141. **`crates/swc/tests/vercel/loader-only/next-39460/input/snippetSession.js`** -> AI Confidence: **99.31%**
142. **`crates/swc/tests/vercel/loader-only/next-39460/output/snippetSession.js`** -> AI Confidence: **99.31%**
143. **`crates/swc_ecma_minifier/scripts/x/terser/compress.js`** -> AI Confidence: **99.31%**
144. **`crates/swc_ecma_minifier/tests/fixture/issues/vercel/006/input.js`** -> AI Confidence: **99.31%**
145. **`crates/swc_ecma_minifier/tests/fixture/next/react-ace/chunks/8a28b14e.d8fbda268ed281a1/input.js`** -> AI Confidence: **99.31%**
146. **`crates/swc_ecma_minifier/tests/fixture/next/wrap-contracts/output.js`** -> AI Confidence: **99.31%**
147. **`crates/swc_ecma_preset_env/tests/fixtures/corejs2/entry-shippedProposals/output.js`** -> AI Confidence: **99.31%**
148. **`crates/swc_ecma_transforms_base/tests/resolver/vercel/next/server/render/1/input.js`** -> AI Confidence: **99.31%**
149. **`crates/swc_ecma_transforms_base/tests/resolver/vercel/next/server/render/1/output.js`** -> AI Confidence: **99.31%**
150. **`packages/minifier/src/binding.js`** -> AI Confidence: **99.31%**
151. **`packages/react-compiler/src/binding.js`** -> AI Confidence: **99.31%**
152. **`crates/swc/tests/errors/lints/use-is-nan/ts/default/input.ts`** -> AI Confidence: **99.29%**
153. **`crates/swc/tests/errors/lints/use-is-nan/ts/disable-any-cast/input.ts`** -> AI Confidence: **99.29%**
154. **`crates/swc/tests/fixture/issues-1xxx/1446/case3/input/index.tsx`** -> AI Confidence: **99.29%**
155. **`crates/swc/tests/fixture/issues-1xxx/1446/case3/output/index.tsx`** -> AI Confidence: **99.29%**
156. **`crates/swc/tests/fixture/issues-2xxx/2050/output/index.ts`** -> AI Confidence: **99.29%**
157. **`crates/swc/tests/fixture/issues-4xxx/4233/1/input/index.ts`** -> AI Confidence: **99.29%**
158. **`crates/swc/tests/fixture/issues-4xxx/4233/1/output/index.ts`** -> AI Confidence: **99.29%**
159. **`crates/swc/tests/fixture/issues-5xxx/5752/input/index.ts`** -> AI Confidence: **99.29%**
160. **`crates/swc/tests/fixture/issues-6xxx/6459/1/input/index.ts`** -> AI Confidence: **99.29%**
161. **`crates/swc/tests/fixture/issues-6xxx/6459/1/output/index.ts`** -> AI Confidence: **99.29%**
162. **`crates/swc/tests/fixture/issues-6xxx/6459/2/input/index.ts`** -> AI Confidence: **99.29%**
163. **`crates/swc/tests/fixture/issues-6xxx/6459/2/output/index.ts`** -> AI Confidence: **99.29%**
164. **`crates/swc/tests/fixture/issues-6xxx/6459/3/input/index.ts`** -> AI Confidence: **99.29%**
165. **`crates/swc/tests/fixture/issues-6xxx/6459/3/output/index.ts`** -> AI Confidence: **99.29%**
166. **`crates/swc/tests/fixture/issues-7xxx/7659/1/input/1.ts`** -> AI Confidence: **99.29%**
167. **`crates/swc/tests/fixture/issues-7xxx/7659/2/input/1.ts`** -> AI Confidence: **99.29%**
168. **`crates/swc/tests/fixture/issues-7xxx/7791/input/index.ts`** -> AI Confidence: **99.29%**
169. **`crates/swc/tests/fixture/issues-7xxx/7791/output/index.ts`** -> AI Confidence: **99.29%**
170. **`crates/swc_bundler/tests/deno-exec/deno-9350/full-2/input/helpers/logger.ts`** -> AI Confidence: **99.29%**
171. **`crates/swc_bundler/tests/deno-exec/deno-9350/full/input/helpers/logger.ts`** -> AI Confidence: **99.29%**
172. **`crates/swc_bundler/tests/deno-exec/deno-9350/step2/input/helpers/logger.ts`** -> AI Confidence: **99.29%**
173. **`crates/swc_bundler/tests/deno/deno-8627/input.ts`** -> AI Confidence: **99.29%**
174. **`crates/swc_bundler/tests/fixture/deno-8627/input/entry.ts`** -> AI Confidence: **99.29%**
175. **`crates/swc_bundler/tests/fixture/deno-8627/output/entry.inlined.ts`** -> AI Confidence: **99.29%**
176. **`crates/swc_bundler/tests/fixture/deno-8627/output/entry.ts`** -> AI Confidence: **99.29%**
177. **`crates/swc_bundler/tests/fixture/deno-9219/case1/output/entry.inlined.ts`** -> AI Confidence: **99.29%**
178. **`crates/swc_bundler/tests/fixture/deno-9219/case1/output/entry.ts`** -> AI Confidence: **99.29%**
179. **`crates/swc_bundler/tests/fixture/deno-9220/case1/output/entry.inlined.ts`** -> AI Confidence: **99.29%**
180. **`crates/swc_bundler/tests/fixture/deno-9220/case1/output/entry.ts`** -> AI Confidence: **99.29%**
181. **`crates/swc_ecma_parser/tests/span/ts/stmt/try-catch-unknown.ts`** -> AI Confidence: **99.29%**
182. **`crates/swc_ecma_parser/tests/tsc/ES5For-of12.ts`** -> AI Confidence: **99.29%**
183. **`crates/swc_ecma_parser/tests/tsc/ES5For-of18.ts`** -> AI Confidence: **99.29%**
184. **`crates/swc_ecma_parser/tests/tsc/ES5For-of19.ts`** -> AI Confidence: **99.29%**
185. **`crates/swc_ecma_parser/tests/tsc/ES5For-of21.ts`** -> AI Confidence: **99.29%**
186. **`crates/swc_ecma_parser/tests/tsc/ES5For-of28.ts`** -> AI Confidence: **99.29%**
187. **`crates/swc_ecma_parser/tests/tsc/ES5For-of29.ts`** -> AI Confidence: **99.29%**
188. **`crates/swc_ecma_parser/tests/tsc/ES5For-of35.ts`** -> AI Confidence: **99.29%**
189. **`crates/swc_ecma_parser/tests/tsc/ES5For-of36.ts`** -> AI Confidence: **99.29%**
190. **`crates/swc_ecma_parser/tests/tsc/ES5For-of37.ts`** -> AI Confidence: **99.29%**
191. **`crates/swc_ecma_parser/tests/tsc/ES5For-ofTypeCheck12.ts`** -> AI Confidence: **99.29%**
192. **`crates/swc_ecma_parser/tests/tsc/ES5For-ofTypeCheck13.ts`** -> AI Confidence: **99.29%**
193. **`crates/swc_ecma_parser/tests/tsc/callChain.3.ts`** -> AI Confidence: **99.29%**
194. **`crates/swc_ecma_parser/tests/tsc/callSignaturesWithOptionalParameters2.ts`** -> AI Confidence: **99.29%**
195. **`crates/swc_ecma_parser/tests/tsc/circularMultipleAssignmentDeclaration.ts`** -> AI Confidence: **99.29%**
196. **`crates/swc_ecma_parser/tests/tsc/controlFlowAliasing.ts`** -> AI Confidence: **99.29%**
197. **`crates/swc_ecma_parser/tests/tsc/controlFlowAliasingCatchVariables.ts`** -> AI Confidence: **99.29%**
198. **`crates/swc_ecma_parser/tests/tsc/controlFlowBinaryAndExpression.ts`** -> AI Confidence: **99.29%**
199. **`crates/swc_ecma_parser/tests/tsc/controlFlowCommaOperator.ts`** -> AI Confidence: **99.29%**
200. **`crates/swc_ecma_parser/tests/tsc/controlFlowComputedPropertyNames.ts`** -> AI Confidence: **99.29%**
201. **`crates/swc_ecma_parser/tests/tsc/controlFlowConditionalExpression.ts`** -> AI Confidence: **99.29%**
202. **`crates/swc_ecma_parser/tests/tsc/controlFlowDeleteOperator.ts`** -> AI Confidence: **99.29%**
203. **`crates/swc_ecma_parser/tests/tsc/controlFlowDestructuringDeclaration.ts`** -> AI Confidence: **99.29%**
204. **`crates/swc_ecma_parser/tests/tsc/controlFlowDoWhileStatement.ts`** -> AI Confidence: **99.29%**
205. **`crates/swc_ecma_parser/tests/tsc/controlFlowElementAccess.ts`** -> AI Confidence: **99.29%**
206. **`crates/swc_ecma_parser/tests/tsc/controlFlowForInStatement.ts`** -> AI Confidence: **99.29%**
207. **`crates/swc_ecma_parser/tests/tsc/controlFlowForOfStatement.ts`** -> AI Confidence: **99.29%**
208. **`crates/swc_ecma_parser/tests/tsc/controlFlowForStatement.ts`** -> AI Confidence: **99.29%**
209. **`crates/swc_ecma_parser/tests/tsc/controlFlowInstanceOfGuardPrimitives.ts`** -> AI Confidence: **99.29%**
210. **`crates/swc_ecma_parser/tests/tsc/controlFlowIteration.ts`** -> AI Confidence: **99.29%**
211. **`crates/swc_ecma_parser/tests/tsc/controlFlowNoIntermediateErrors.ts`** -> AI Confidence: **99.29%**
212. **`crates/swc_ecma_parser/tests/tsc/controlFlowNullishCoalesce.ts`** -> AI Confidence: **99.29%**
213. **`crates/swc_ecma_parser/tests/tsc/controlFlowOptionalChain.ts`** -> AI Confidence: **99.29%**
214. **`crates/swc_ecma_parser/tests/tsc/controlFlowOptionalChain3.tsx`** -> AI Confidence: **99.29%**
215. **`crates/swc_ecma_parser/tests/tsc/controlFlowTruthiness.ts`** -> AI Confidence: **99.29%**
216. **`crates/swc_ecma_parser/tests/tsc/controlFlowWhileStatement.ts`** -> AI Confidence: **99.29%**
217. **`crates/swc_ecma_parser/tests/tsc/deleteChain.ts`** -> AI Confidence: **99.29%**
218. **`crates/swc_ecma_parser/tests/tsc/destructuringCatch.ts`** -> AI Confidence: **99.29%**
219. **`crates/swc_ecma_parser/tests/tsc/destructuringControlFlow.ts`** -> AI Confidence: **99.29%**
220. **`crates/swc_ecma_parser/tests/tsc/destructuringObjectBindingPatternAndAssignment9SiblingInitializer.ts`** -> AI Confidence: **99.29%**
221. **`crates/swc_ecma_parser/tests/tsc/destructuringParameterDeclaration8.ts`** -> AI Confidence: **99.29%**
222. **`crates/swc_ecma_parser/tests/tsc/doWhileBreakStatements.ts`** -> AI Confidence: **99.29%**
223. **`crates/swc_ecma_parser/tests/tsc/doWhileContinueStatements.ts`** -> AI Confidence: **99.29%**
224. **`crates/swc_ecma_parser/tests/tsc/elementAccessChain.3.ts`** -> AI Confidence: **99.29%**
225. **`crates/swc_ecma_parser/tests/tsc/elementAccessChain.ts`** -> AI Confidence: **99.29%**
226. **`crates/swc_ecma_parser/tests/tsc/emitter.noCatchBinding.es2019.ts`** -> AI Confidence: **99.29%**
227. **`crates/swc_ecma_parser/tests/tsc/equalityWithEnumTypes.ts`** -> AI Confidence: **99.29%**
228. **`crates/swc_ecma_parser/tests/tsc/equalityWithtNullishCoalescingAssignment.ts`** -> AI Confidence: **99.29%**
229. **`crates/swc_ecma_parser/tests/tsc/es2016IntlAPIs.ts`** -> AI Confidence: **99.29%**
230. **`crates/swc_ecma_parser/tests/tsc/for-inStatementsArray.ts`** -> AI Confidence: **99.29%**
231. **`crates/swc_ecma_parser/tests/tsc/for-of55.ts`** -> AI Confidence: **99.29%**
232. **`crates/swc_ecma_parser/tests/tsc/forBreakStatements.ts`** -> AI Confidence: **99.29%**
233. **`crates/swc_ecma_parser/tests/tsc/forContinueStatements.ts`** -> AI Confidence: **99.29%**
234. **`crates/swc_ecma_parser/tests/tsc/intersectionNarrowing.ts`** -> AI Confidence: **99.29%**
235. **`crates/swc_ecma_parser/tests/tsc/invalidSwitchBreakStatement.ts`** -> AI Confidence: **99.29%**
236. **`crates/swc_ecma_parser/tests/tsc/jsDeclarationsOptionalTypeLiteralProps2.ts`** -> AI Confidence: **99.29%**
237. **`crates/swc_ecma_parser/tests/tsc/jsdocBindingInUnreachableCode.ts`** -> AI Confidence: **99.29%**
238. **`crates/swc_ecma_parser/tests/tsc/jsdocCatchClauseWithTypeAnnotation.ts`** -> AI Confidence: **99.29%**
239. **`crates/swc_ecma_parser/tests/tsc/literalTypes1.ts`** -> AI Confidence: **99.29%**
240. **`crates/swc_ecma_parser/tests/tsc/literalTypes3.ts`** -> AI Confidence: **99.29%**
241. **`crates/swc_ecma_parser/tests/tsc/logicalAssignment11.ts`** -> AI Confidence: **99.29%**
242. **`crates/swc_ecma_parser/tests/tsc/logicalAssignment4.ts`** -> AI Confidence: **99.29%**
243. **`crates/swc_ecma_parser/tests/tsc/logicalAssignment6.ts`** -> AI Confidence: **99.29%**
244. **`crates/swc_ecma_parser/tests/tsc/logicalAssignment7.ts`** -> AI Confidence: **99.29%**
245. **`crates/swc_ecma_parser/tests/tsc/logicalAssignment8.ts`** -> AI Confidence: **99.29%**
246. **`crates/swc_ecma_parser/tests/tsc/logicalAssignment9.ts`** -> AI Confidence: **99.29%**
247. **`crates/swc_ecma_parser/tests/tsc/memberFunctionsWithPublicOverloads.ts`** -> AI Confidence: **99.29%**
248. **`crates/swc_ecma_parser/tests/tsc/newTargetNarrowing.ts`** -> AI Confidence: **99.29%**
249. **`crates/swc_ecma_parser/tests/tsc/nullishCoalescingOperator12.ts`** -> AI Confidence: **99.29%**
250. **`crates/swc_ecma_parser/tests/tsc/nullishCoalescingOperator5.ts`** -> AI Confidence: **99.29%**
251. **`crates/swc_ecma_parser/tests/tsc/nullishCoalescingOperator6.ts`** -> AI Confidence: **99.29%**
252. **`crates/swc_ecma_parser/tests/tsc/nullishCoalescingOperator7.ts`** -> AI Confidence: **99.29%**
253. **`crates/swc_ecma_parser/tests/tsc/nullishCoalescingOperator8.ts`** -> AI Confidence: **99.29%**
254. **`crates/swc_ecma_parser/tests/tsc/nullishCoalescingOperatorInAsyncGenerator.ts`** -> AI Confidence: **99.29%**
255. **`crates/swc_ecma_parser/tests/tsc/nullishCoalescingOperator_es2020.ts`** -> AI Confidence: **99.29%**
256. **`crates/swc_ecma_parser/tests/tsc/objectSpreadRepeatedComplexity.ts`** -> AI Confidence: **99.29%**
257. **`crates/swc_ecma_parser/tests/tsc/objectSpreadRepeatedNullCheckPerf.ts`** -> AI Confidence: **99.29%**
258. **`crates/swc_ecma_parser/tests/tsc/optionalBindingParameters1.ts`** -> AI Confidence: **99.29%**
259. **`crates/swc_ecma_parser/tests/tsc/optionalBindingParameters2.ts`** -> AI Confidence: **99.29%**
260. **`crates/swc_ecma_parser/tests/tsc/optionalBindingParametersInOverloads1.ts`** -> AI Confidence: **99.29%**
261. **`crates/swc_ecma_parser/tests/tsc/optionalBindingParametersInOverloads2.ts`** -> AI Confidence: **99.29%**
262. **`crates/swc_ecma_parser/tests/tsc/optionalChainingInLoop.ts`** -> AI Confidence: **99.29%**
263. **`crates/swc_ecma_parser/tests/tsc/optionalChainingInTypeAssertions.ts`** -> AI Confidence: **99.29%**
264. **`crates/swc_ecma_parser/tests/tsc/parserArrowFunctionExpression7.ts`** -> AI Confidence: **99.29%**
265. **`crates/swc_ecma_parser/tests/tsc/parserConditionalExpression1.ts`** -> AI Confidence: **99.29%**
266. **`crates/swc_ecma_parser/tests/tsc/parserForInStatement8.ts`** -> AI Confidence: **99.29%**
267. **`crates/swc_ecma_parser/tests/tsc/parserForOfStatement25.ts`** -> AI Confidence: **99.29%**
268. **`crates/swc_ecma_parser/tests/tsc/parserForStatement9.ts`** -> AI Confidence: **99.29%**
269. **`crates/swc_ecma_parser/tests/tsc/parserOptionalTypeMembers1.ts`** -> AI Confidence: **99.29%**
270. **`crates/swc_ecma_parser/tests/tsc/parserParenthesizedVariableAndFunctionInTernary.ts`** -> AI Confidence: **99.29%**
271. **`crates/swc_ecma_parser/tests/tsc/parserParenthesizedVariableAndParenthesizedFunctionInTernary.ts`** -> AI Confidence: **99.29%**
272. **`crates/swc_ecma_parser/tests/tsc/parserRealSource13.ts`** -> AI Confidence: **99.29%**
273. **`crates/swc_ecma_parser/tests/tsc/parserRegularExpression4.ts`** -> AI Confidence: **99.29%**
274. **`crates/swc_ecma_parser/tests/tsc/parserSbp_7.9_A9_T3.ts`** -> AI Confidence: **99.29%**
275. **`crates/swc_ecma_parser/tests/tsc/parser_breakTarget3.ts`** -> AI Confidence: **99.29%**
276. **`crates/swc_ecma_parser/tests/tsc/parser_breakTarget4.ts`** -> AI Confidence: **99.29%**
277. **`crates/swc_ecma_parser/tests/tsc/parser_continueTarget3.ts`** -> AI Confidence: **99.29%**
278. **`crates/swc_ecma_parser/tests/tsc/parser_continueTarget4.ts`** -> AI Confidence: **99.29%**
279. **`crates/swc_ecma_parser/tests/tsc/parser_duplicateLabel3.ts`** -> AI Confidence: **99.29%**
280. **`crates/swc_ecma_parser/tests/tsc/parser_duplicateLabel4.ts`** -> AI Confidence: **99.29%**
281. **`crates/swc_ecma_parser/tests/tsc/plainJSTypeErrors.ts`** -> AI Confidence: **99.29%**
282. **`crates/swc_ecma_parser/tests/tsc/privateNameFieldUnaryMutation.ts`** -> AI Confidence: **99.29%**
283. **`crates/swc_ecma_parser/tests/tsc/propertyAccessChain.3.ts`** -> AI Confidence: **99.29%**
284. **`crates/swc_ecma_parser/tests/tsc/propertyAccessWidening.ts`** -> AI Confidence: **99.29%**
285. **`crates/swc_ecma_parser/tests/tsc/stringLiteralTypesInUnionTypes04.ts`** -> AI Confidence: **99.29%**
286. **`crates/swc_ecma_parser/tests/tsc/stringLiteralTypesWithVariousOperators01.ts`** -> AI Confidence: **99.29%**
287. **`crates/swc_ecma_parser/tests/tsc/stringLiteralTypesWithVariousOperators02.ts`** -> AI Confidence: **99.29%**
288. **`crates/swc_ecma_parser/tests/tsc/stringLiteralsWithSwitchStatements01.ts`** -> AI Confidence: **99.29%**
289. **`crates/swc_ecma_parser/tests/tsc/stringLiteralsWithSwitchStatements03.ts`** -> AI Confidence: **99.29%**
290. **`crates/swc_ecma_parser/tests/tsc/stringLiteralsWithSwitchStatements04.ts`** -> AI Confidence: **99.29%**
291. **`crates/swc_ecma_parser/tests/tsc/switchBreakStatements.ts`** -> AI Confidence: **99.29%**
292. **`crates/swc_ecma_parser/tests/tsc/switchWithConstrainedTypeVariable.ts`** -> AI Confidence: **99.29%**
293. **`crates/swc_ecma_parser/tests/tsc/symbolType1.ts`** -> AI Confidence: **99.29%**
294. **`crates/swc_ecma_parser/tests/tsc/symbolType11.ts`** -> AI Confidence: **99.29%**
295. **`crates/swc_ecma_parser/tests/tsc/templateStringInSwitchAndCase.ts`** -> AI Confidence: **99.29%**
296. **`crates/swc_ecma_parser/tests/tsc/templateStringInSwitchAndCaseES6.ts`** -> AI Confidence: **99.29%**
297. **`crates/swc_ecma_parser/tests/tsc/templateStringInWhileES6.ts`** -> AI Confidence: **99.29%**
298. **`crates/swc_ecma_parser/tests/tsc/thisPrototypeMethodCompoundAssignment.ts`** -> AI Confidence: **99.29%**
299. **`crates/swc_ecma_parser/tests/tsc/thisPrototypeMethodCompoundAssignmentJs.ts`** -> AI Confidence: **99.29%**
300. **`crates/swc_ecma_parser/tests/tsc/tryStatements.ts`** -> AI Confidence: **99.29%**
301. **`crates/swc_ecma_parser/tests/tsc/typeFromJSConstructor.ts`** -> AI Confidence: **99.29%**
302. **`crates/swc_ecma_parser/tests/tsc/typeFromPropertyAssignment36.ts`** -> AI Confidence: **99.29%**
303. **`crates/swc_ecma_parser/tests/tsc/typeGuardNesting.ts`** -> AI Confidence: **99.29%**
304. **`crates/swc_ecma_parser/tests/tsc/typeGuardOfFormTypeOfPrimitiveSubtype.ts`** -> AI Confidence: **99.29%**
305. **`crates/swc_ecma_parser/tests/tsc/typeGuardTautologicalConsistiency.ts`** -> AI Confidence: **99.29%**
306. **`crates/swc_ecma_parser/tests/tsc/typeGuardTypeOfUndefined.ts`** -> AI Confidence: **99.29%**
307. **`crates/swc_ecma_parser/tests/tsc/typeGuardsInDoStatement.ts`** -> AI Confidence: **99.29%**
308. **`crates/swc_ecma_parser/tests/tsc/typeGuardsInForStatement.ts`** -> AI Confidence: **99.29%**
309. **`crates/swc_ecma_parser/tests/tsc/typeGuardsInWhileStatement.ts`** -> AI Confidence: **99.29%**
310. **`crates/swc_ecma_parser/tests/tsc/typeGuardsTypeParameters.ts`** -> AI Confidence: **99.29%**
311. **`crates/swc_ecma_parser/tests/tsc/typeGuardsWithAny.ts`** -> AI Confidence: **99.29%**
312. **`crates/swc_ecma_parser/tests/tsc/unionTypeCallSignatures3.ts`** -> AI Confidence: **99.29%**
313. **`crates/swc_ecma_parser/tests/tsc/usePromiseFinally.ts`** -> AI Confidence: **99.29%**
314. **`crates/swc_ecma_parser/tests/tsc/useRegexpGroups.ts`** -> AI Confidence: **99.29%**
315. **`crates/swc_ecma_parser/tests/tsc/whileBreakStatements.ts`** -> AI Confidence: **99.29%**
316. **`crates/swc_ecma_parser/tests/tsc/whileContinueStatements.ts`** -> AI Confidence: **99.29%**
317. **`crates/swc_ecma_parser/tests/typescript-errors/deno-10112/case1/input.ts`** -> AI Confidence: **99.29%**
318. **`crates/swc_ecma_parser/tests/typescript-errors/deno-10112/case2/input.ts`** -> AI Confidence: **99.29%**
319. **`crates/swc_ecma_parser/tests/typescript-errors/instantiation-expr/case2/input.ts`** -> AI Confidence: **99.29%**
320. **`crates/swc_ecma_parser/tests/typescript-errors/nullish-coalescing-operator/no-paren-and-nullish/input.ts`** -> AI Confidence: **99.29%**
321. **`crates/swc_ecma_parser/tests/typescript-errors/nullish-coalescing-operator/no-paren-nullish-and/input.ts`** -> AI Confidence: **99.29%**
322. **`crates/swc_ecma_parser/tests/typescript-errors/nullish-coalescing-operator/no-paren-nullish-or/input.ts`** -> AI Confidence: **99.29%**
323. **`crates/swc_ecma_parser/tests/typescript-errors/nullish-coalescing-operator/no-paren-or-nullish/input.ts`** -> AI Confidence: **99.29%**
324. **`crates/swc_ecma_parser/tests/typescript-errors/optional-chaining/indirect-assign/input.ts`** -> AI Confidence: **99.29%**
325. **`crates/swc_ecma_parser/tests/typescript-errors/reserved-words/keywords/input.ts`** -> AI Confidence: **99.29%**
326. **`crates/swc_ecma_parser/tests/typescript-errors/types/tuple-optional-invalid/input.ts`** -> AI Confidence: **99.29%**
327. **`crates/swc_ecma_parser/tests/typescript/custom/issue-716/input.ts`** -> AI Confidence: **99.29%**
328. **`crates/swc_ecma_parser/tests/typescript/custom/ternary-paren/input.ts`** -> AI Confidence: **99.29%**
329. **`crates/swc_ecma_parser/tests/typescript/custom/ternary/input.ts`** -> AI Confidence: **99.29%**
330. **`crates/swc_ecma_parser/tests/typescript/custom/tsx-unary-paren/input.tsx`** -> AI Confidence: **99.29%**
331. **`crates/swc_ecma_parser/tests/typescript/function/annotated/input.ts`** -> AI Confidence: **99.29%**
332. **`crates/swc_ecma_parser/tests/typescript/function/anonymous/input.ts`** -> AI Confidence: **99.29%**
333. **`crates/swc_ecma_parser/tests/typescript/instantiation-expr/bin-op/input.ts`** -> AI Confidence: **99.29%**
334. **`crates/swc_ecma_parser/tests/typescript/instantiation-expr/more-exprs/input.ts`** -> AI Confidence: **99.29%**
335. **`crates/swc_ecma_parser/tests/typescript/instantiation-expr/optional-chaining/input.ts`** -> AI Confidence: **99.29%**
336. **`crates/swc_ecma_parser/tests/typescript/issue-1446/case2/input.tsx`** -> AI Confidence: **99.29%**
337. **`crates/swc_ecma_parser/tests/typescript/issue-947/input.ts`** -> AI Confidence: **99.29%**
338. **`crates/swc_ecma_parser/tests/typescript/nullish-coalescing-operator/and-nullish/input.ts`** -> AI Confidence: **99.29%**
339. **`crates/swc_ecma_parser/tests/typescript/nullish-coalescing-operator/associativity/input.ts`** -> AI Confidence: **99.29%**
340. **`crates/swc_ecma_parser/tests/typescript/nullish-coalescing-operator/expression/input.ts`** -> AI Confidence: **99.29%**
341. **`crates/swc_ecma_parser/tests/typescript/nullish-coalescing-operator/multiline/input.ts`** -> AI Confidence: **99.29%**
342. **`crates/swc_ecma_parser/tests/typescript/nullish-coalescing-operator/nullish-and/input.ts`** -> AI Confidence: **99.29%**
343. **`crates/swc_ecma_parser/tests/typescript/nullish-coalescing-operator/nullish-or/input.ts`** -> AI Confidence: **99.29%**
344. **`crates/swc_ecma_parser/tests/typescript/nullish-coalescing-operator/or-nullish/input.ts`** -> AI Confidence: **99.29%**
345. **`crates/swc_ecma_parser/tests/typescript/optional-chaining/conditional-decimal/input.ts`** -> AI Confidence: **99.29%**
346. **`crates/swc_ecma_parser/tests/typescript/optional-chaining/constructor-call/input.ts`** -> AI Confidence: **99.29%**
347. **`crates/swc_ecma_parser/tests/typescript/optional-chaining/function-call/input.ts`** -> AI Confidence: **99.29%**
348. **`crates/swc_ecma_parser/tests/typescript/optional-chaining/member-access-bracket/input.ts`** -> AI Confidence: **99.29%**
349. **`crates/swc_ecma_parser/tests/typescript/optional-chaining/member-access/input.ts`** -> AI Confidence: **99.29%**
350. **`crates/swc_ecma_parser/tests/typescript/optional-chaining/optioanl-chain-expression/input.ts`** -> AI Confidence: **99.29%**
351. **`crates/swc_ecma_parser/tests/typescript/optional-chaining/optional-tagged-template-literals/input.ts`** -> AI Confidence: **99.29%**
352. **`crates/swc_ecma_parser/tests/typescript/optional-chaining/parenthised-chain/input.ts`** -> AI Confidence: **99.29%**
353. **`crates/swc_ecma_parser/tests/typescript/optional-chaining/separated-chaining/input.ts`** -> AI Confidence: **99.29%**
354. **`crates/swc_ecma_parser/tests/typescript/optional-chaining/type-arguments-with-call/input.ts`** -> AI Confidence: **99.29%**
355. **`crates/swc_ecma_parser/tests/typescript/optional-chaining/type-arguments/input.ts`** -> AI Confidence: **99.29%**
356. **`crates/swc_ecma_parser/tests/typescript/stack-size/input.ts`** -> AI Confidence: **99.29%**
357. **`crates/swc_ecma_parser/tests/typescript/types/mapped/input.ts`** -> AI Confidence: **99.29%**
358. **`crates/swc_ecma_parser/tests/typescript/types/tuple-optional/input.ts`** -> AI Confidence: **99.29%**
359. **`crates/swc_ecma_parser/tests/typescript/types/tuple-rest-after-optional/input.ts`** -> AI Confidence: **99.29%**
360. **`crates/swc_ecma_parser/tests/typescript/v4/issue-866/input.ts`** -> AI Confidence: **99.29%**
361. **`crates/swc_ecma_parser/tests/typescript/v4/issue-941/input.ts`** -> AI Confidence: **99.29%**
362. **`crates/swc_ecma_transforms_base/tests/ts-resolver/ts_for_of_statements_for_of_23_01/input.ts`** -> AI Confidence: **99.29%**
363. **`crates/swc_ecma_transforms_base/tests/ts-resolver/ts_for_of_statements_for_of_23_01/output.ts`** -> AI Confidence: **99.29%**
364. **`crates/swc_ecma_transforms_base/tests/ts-resolver/ts_resolver_deno_undef_001/input.ts`** -> AI Confidence: **99.29%**
365. **`crates/swc_ecma_transforms_base/tests/ts-resolver/ts_resolver_deno_undef_001/output.ts`** -> AI Confidence: **99.29%**
366. **`crates/swc_ecma_transforms_module/tests/fixture/common/cts-import-export/export-import/output.umd.ts`** -> AI Confidence: **99.29%**
367. **`crates/swc_ecma_transforms_module/tests/fixture/common/cts-import-export/mixed/output.amd.ts`** -> AI Confidence: **99.29%**
368. **`crates/swc_ecma_transforms_module/tests/fixture/common/cts-import-export/mixed/output.cts`** -> AI Confidence: **99.29%**
369. **`crates/swc_ecma_transforms_module/tests/fixture/common/cts-import-export/mixed/output.umd.ts`** -> AI Confidence: **99.29%**
370. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-1686/output.umd.ts`** -> AI Confidence: **99.29%**
371. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-4898/1/output.umd.ts`** -> AI Confidence: **99.29%**
372. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-4898/2/output.amd.ts`** -> AI Confidence: **99.29%**
373. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-4898/2/output.cts`** -> AI Confidence: **99.29%**
374. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-4898/2/output.umd.ts`** -> AI Confidence: **99.29%**
375. **`packages/types/assumptions.ts`** -> AI Confidence: **99.29%**
376. **`crates/swc_css_codegen/src/macros.rs`** -> AI Confidence: **99.29%**
377. **`crates/swc_css_lints/src/dataset.rs`** -> AI Confidence: **99.29%**
378. **`crates/swc_css_minifier/src/compressor/transform_function.rs`** -> AI Confidence: **99.29%**
379. **`crates/swc_ecma_lexer/src/common/lexer/jsx.rs`** -> AI Confidence: **99.29%**
380. **`crates/swc_ecma_lexer/src/common/lexer/number.rs`** -> AI Confidence: **99.29%**
381. **`crates/swc_ecma_lexer/src/parser/macros.rs`** -> AI Confidence: **99.29%**
382. **`crates/swc_ecma_parser/src/lexer/jsx.rs`** -> AI Confidence: **99.29%**
383. **`crates/swc_ecma_parser/src/lexer/number.rs`** -> AI Confidence: **99.29%**
384. **`crates/swc_html_codegen/src/macros.rs`** -> AI Confidence: **99.29%**
385. **`crates/swc_html_parser/src/parser/macros.rs`** -> AI Confidence: **99.29%**
386. **`crates/swc_xml_codegen/src/macros.rs`** -> AI Confidence: **99.29%**
387. **`crates/jsdoc/tests/fixtures/also2.js`** -> AI Confidence: **99.29%**
388. **`crates/swc/tests/errors/lints/const-assign/1/input.js`** -> AI Confidence: **99.29%**
389. **`crates/swc/tests/errors/lints/default-case-last/default/input.js`** -> AI Confidence: **99.29%**
390. **`crates/swc/tests/errors/lints/dot-notation/restrict-keywords/input.js`** -> AI Confidence: **99.29%**
391. **`crates/swc/tests/errors/lints/dot-notation/simple/input.js`** -> AI Confidence: **99.29%**
392. **`crates/swc/tests/errors/lints/eqeqeq/always/input.js`** -> AI Confidence: **99.29%**
393. **`crates/swc/tests/errors/lints/eqeqeq/never/input.js`** -> AI Confidence: **99.29%**
394. **`crates/swc/tests/errors/lints/lint-config-error-level/1/input.js`** -> AI Confidence: **99.29%**
395. **`crates/swc/tests/errors/lints/no-param-reassign/allow-props-modification/input.js`** -> AI Confidence: **99.29%**
396. **`crates/swc/tests/errors/lints/no-param-reassign/default/input.js`** -> AI Confidence: **99.29%**
397. **`crates/swc/tests/errors/lints/no-prototype-builtins/default/input.js`** -> AI Confidence: **99.29%**
398. **`crates/swc/tests/errors/lints/no-restricted-syntax/labeled-stmt/input.js`** -> AI Confidence: **99.29%**
399. **`crates/swc/tests/errors/lints/radix/default/input.js`** -> AI Confidence: **99.29%**
400. **`crates/swc/tests/errors/lints/use-is-nan/js/default/input.js`** -> AI Confidence: **99.29%**
401. **`crates/swc/tests/errors/lints/use-is-nan/js/disable-index-of-check/input.js`** -> AI Confidence: **99.29%**
402. **`crates/swc/tests/errors/lints/use-is-nan/js/disable-switch-check/input.js`** -> AI Confidence: **99.29%**
403. **`crates/swc/tests/errors/lints/yoda/always/input.js`** -> AI Confidence: **99.29%**
404. **`crates/swc/tests/errors/lints/yoda/default/input.js`** -> AI Confidence: **99.29%**
405. **`crates/swc/tests/errors/lints/yoda/except-range/input.js`** -> AI Confidence: **99.29%**
406. **`crates/swc/tests/errors/lints/yoda/only-equality/input.js`** -> AI Confidence: **99.29%**
407. **`crates/swc/tests/exec/issues-11xxx/11754/exec.js`** -> AI Confidence: **99.29%**
408. **`crates/swc/tests/exec/issues-6xxx/6028/1/exec.js`** -> AI Confidence: **99.29%**
409. **`crates/swc/tests/exec/issues-6xxx/6303/exec.js`** -> AI Confidence: **99.29%**
410. **`crates/swc/tests/exec/issues-6xxx/6311/exec.js`** -> AI Confidence: **99.29%**
411. **`crates/swc/tests/exec/issues-6xxx/6762/1/exec.js`** -> AI Confidence: **99.29%**
412. **`crates/swc/tests/exec/issues-6xxx/6878/1/exec.js`** -> AI Confidence: **99.29%**
413. **`crates/swc/tests/exec/next/39412/exec.js`** -> AI Confidence: **99.29%**
414. **`crates/swc/tests/fixture/globals/member-expr/1/input/index.js`** -> AI Confidence: **99.29%**
415. **`crates/swc/tests/fixture/globals/member-expr/1/output/index.js`** -> AI Confidence: **99.29%**
416. **`crates/swc/tests/fixture/globals/member-expr/precendence/input/index.js`** -> AI Confidence: **99.29%**
417. **`crates/swc/tests/fixture/globals/member-expr/precendence/output/index.js`** -> AI Confidence: **99.29%**
418. **`crates/swc/tests/fixture/issues-11xxx/11379/input/index.js`** -> AI Confidence: **99.29%**
419. **`crates/swc/tests/fixture/issues-11xxx/11608/input/input.js`** -> AI Confidence: **99.29%**
420. **`crates/swc/tests/fixture/issues-11xxx/11612/input/index.js`** -> AI Confidence: **99.29%**
421. **`crates/swc/tests/fixture/issues-11xxx/11612/output/index.js`** -> AI Confidence: **99.29%**
422. **`crates/swc/tests/fixture/issues-11xxx/11754/input/input.js`** -> AI Confidence: **99.29%**
423. **`crates/swc/tests/fixture/issues-1xxx/1575/case1/input/index.js`** -> AI Confidence: **99.29%**
424. **`crates/swc/tests/fixture/issues-2xxx/2063/input/index.js`** -> AI Confidence: **99.29%**
425. **`crates/swc/tests/fixture/issues-2xxx/2164/es2015/input/index.js`** -> AI Confidence: **99.29%**
426. **`crates/swc/tests/fixture/issues-2xxx/2164/es2016/input/index.js`** -> AI Confidence: **99.29%**
427. **`crates/swc/tests/fixture/issues-2xxx/2164/es2018/input/index.js`** -> AI Confidence: **99.29%**
428. **`crates/swc/tests/fixture/issues-2xxx/2164/es2018/output/index.js`** -> AI Confidence: **99.29%**
429. **`crates/swc/tests/fixture/issues-2xxx/2164/es5/input/index.js`** -> AI Confidence: **99.29%**
430. **`crates/swc/tests/fixture/issues-2xxx/2170/case1/output/index.js`** -> AI Confidence: **99.29%**
431. **`crates/swc/tests/fixture/issues-2xxx/2531/1/input/index.js`** -> AI Confidence: **99.29%**
432. **`crates/swc/tests/fixture/issues-2xxx/2531/2/input/index.js`** -> AI Confidence: **99.29%**
433. **`crates/swc/tests/fixture/issues-2xxx/2793/input/index.js`** -> AI Confidence: **99.29%**
434. **`crates/swc/tests/fixture/issues-2xxx/2834/input/index.js`** -> AI Confidence: **99.29%**
435. **`crates/swc/tests/fixture/issues-2xxx/2834/output/index.js`** -> AI Confidence: **99.29%**
436. **`crates/swc/tests/fixture/issues-2xxx/2856/1/output/index.js`** -> AI Confidence: **99.29%**
437. **`crates/swc/tests/fixture/issues-4xxx/4249/1/input/index.js`** -> AI Confidence: **99.29%**
438. **`crates/swc/tests/fixture/issues-4xxx/4249/1/output/index.js`** -> AI Confidence: **99.29%**
439. **`crates/swc/tests/fixture/issues-4xxx/4855/input/1/input.js`** -> AI Confidence: **99.29%**
440. **`crates/swc/tests/fixture/issues-5xxx/5332/input/index.js`** -> AI Confidence: **99.29%**
441. **`crates/swc/tests/fixture/issues-5xxx/5332/output/index.js`** -> AI Confidence: **99.29%**
442. **`crates/swc/tests/fixture/issues-6xxx/6028/input/index.js`** -> AI Confidence: **99.29%**
443. **`crates/swc/tests/fixture/issues-6xxx/6420/input/input.js`** -> AI Confidence: **99.29%**
444. **`crates/swc/tests/fixture/issues-6xxx/6438/input/index.js`** -> AI Confidence: **99.29%**
445. **`crates/swc/tests/fixture/issues-6xxx/6438/output/index.js`** -> AI Confidence: **99.29%**
446. **`crates/swc/tests/fixture/issues-7xxx/7064/case1/input/index.js`** -> AI Confidence: **99.29%**
447. **`crates/swc/tests/fixture/issues-7xxx/7612/input/1.js`** -> AI Confidence: **99.29%**
448. **`crates/swc/tests/fixture/issues-7xxx/7612/output/1.js`** -> AI Confidence: **99.29%**
449. **`crates/swc/tests/fixture/issues-7xxx/7739/input/1.js`** -> AI Confidence: **99.29%**
450. **`crates/swc/tests/fixture/issues-8xxx/8326/1/input/index.js`** -> AI Confidence: **99.29%**
451. **`crates/swc/tests/fixture/issues-8xxx/8326/1/output/index.js`** -> AI Confidence: **99.29%**
452. **`crates/swc/tests/fixture/issues-8xxx/8398/input/index.js`** -> AI Confidence: **99.29%**
453. **`crates/swc/tests/fixture/issues-8xxx/8398/output/index.js`** -> AI Confidence: **99.29%**
454. **`crates/swc/tests/fixture/issues-8xxx/8482/output/index.js`** -> AI Confidence: **99.29%**
455. **`crates/swc/tests/fixture/issues-9xxx/9930/input/index.js`** -> AI Confidence: **99.29%**
456. **`crates/swc/tests/fixture/issues-9xxx/9930/output/index.js`** -> AI Confidence: **99.29%**
457. **`crates/swc/tests/fixture/sourcemap/issue-9567/input/index.js`** -> AI Confidence: **99.29%**
458. **`crates/swc/tests/fixture/sourcemap/issue-9567/output/index.js`** -> AI Confidence: **99.29%**
459. **`crates/swc/tests/source_map_inline.js`** -> AI Confidence: **99.29%**
460. **`crates/swc/tests/stacktrace/deno-10014/input/index.js`** -> AI Confidence: **99.29%**
461. **`crates/swc/tests/stacktrace/issue-622/input/index.js`** -> AI Confidence: **99.29%**
462. **`crates/swc/tests/tsc-references/TwoInternalModulesThatMergeEachWithExportedAndNonExportedClassesOfTheSameName.2.minified.js`** -> AI Confidence: **99.29%**
463. **`crates/swc/tests/tsc-references/TwoInternalModulesThatMergeEachWithExportedClassesOfTheSameName.2.minified.js`** -> AI Confidence: **99.29%**
464. **`crates/swc/tests/tsc-references/TwoInternalModulesThatMergeEachWithExportedModulesOfTheSameName.2.minified.js`** -> AI Confidence: **99.29%**
465. **`crates/swc/tests/tsc-references/anonymousDefaultExportsUmd.1.normal.js`** -> AI Confidence: **99.29%**
466. **`crates/swc/tests/tsc-references/assignmentCompatWithDiscriminatedUnion.2.minified.js`** -> AI Confidence: **99.29%**
467. **`crates/swc/tests/tsc-references/callChain.1.normal.js`** -> AI Confidence: **99.29%**
468. **`crates/swc/tests/tsc-references/callChain.2.1.normal.js`** -> AI Confidence: **99.29%**
469. **`crates/swc/tests/tsc-references/callChain.2.minified.js`** -> AI Confidence: **99.29%**
470. **`crates/swc/tests/tsc-references/callChain.3.2.minified.js`** -> AI Confidence: **99.29%**
471. **`crates/swc/tests/tsc-references/callChainInference.1.normal.js`** -> AI Confidence: **99.29%**
472. **`crates/swc/tests/tsc-references/callChainInference.2.minified.js`** -> AI Confidence: **99.29%**
473. **`crates/swc/tests/tsc-references/circularMultipleAssignmentDeclaration.1.normal.js`** -> AI Confidence: **99.29%**
474. **`crates/swc/tests/tsc-references/circularMultipleAssignmentDeclaration.2.minified.js`** -> AI Confidence: **99.29%**
475. **`crates/swc/tests/tsc-references/classStaticBlock24(module=umd).1.normal.js`** -> AI Confidence: **99.29%**
476. **`crates/swc/tests/tsc-references/constEnum4.1.normal.js`** -> AI Confidence: **99.29%**
477. **`crates/swc/tests/tsc-references/controlFlowAliasingCatchVariables.1.normal.js`** -> AI Confidence: **99.29%**
478. **`crates/swc/tests/tsc-references/controlFlowComputedPropertyNames.1.normal.js`** -> AI Confidence: **99.29%**
479. **`crates/swc/tests/tsc-references/controlFlowElementAccess2.1.normal.js`** -> AI Confidence: **99.29%**
480. **`crates/swc/tests/tsc-references/controlFlowElementAccess2.2.minified.js`** -> AI Confidence: **99.29%**
481. **`crates/swc/tests/tsc-references/controlFlowForInStatement2.2.minified.js`** -> AI Confidence: **99.29%**
482. **`crates/swc/tests/tsc-references/controlFlowInOperator.2.minified.js`** -> AI Confidence: **99.29%**
483. **`crates/swc/tests/tsc-references/controlFlowInstanceOfGuardPrimitives.1.normal.js`** -> AI Confidence: **99.29%**
484. **`crates/swc/tests/tsc-references/controlFlowOptionalChain.1.normal.js`** -> AI Confidence: **99.29%**
485. **`crates/swc/tests/tsc-references/controlFlowOptionalChain2.1.normal.js`** -> AI Confidence: **99.29%**
486. **`crates/swc/tests/tsc-references/controlFlowOptionalChain3.1.normal.js`** -> AI Confidence: **99.29%**
487. **`crates/swc/tests/tsc-references/controlFlowStringIndex.1.normal.js`** -> AI Confidence: **99.29%**
488. **`crates/swc/tests/tsc-references/controlFlowStringIndex.2.minified.js`** -> AI Confidence: **99.29%**
489. **`crates/swc/tests/tsc-references/controlFlowWithTemplateLiterals.1.normal.js`** -> AI Confidence: **99.29%**
490. **`crates/swc/tests/tsc-references/controlFlowWithTemplateLiterals.2.minified.js`** -> AI Confidence: **99.29%**
491. **`crates/swc/tests/tsc-references/defaultExportsGetExportedUmd.1.normal.js`** -> AI Confidence: **99.29%**
492. **`crates/swc/tests/tsc-references/dependentDestructuredVariables.1.normal.js`** -> AI Confidence: **99.29%**
493. **`crates/swc/tests/tsc-references/destructuringObjectBindingPatternAndAssignment4.1.normal.js`** -> AI Confidence: **99.29%**
494. **`crates/swc/tests/tsc-references/discriminatedUnionTypes2.1.normal.js`** -> AI Confidence: **99.29%**
495. **`crates/swc/tests/tsc-references/discriminatedUnionTypes2.2.minified.js`** -> AI Confidence: **99.29%**
496. **`crates/swc/tests/tsc-references/doWhileBreakStatements.1.normal.js`** -> AI Confidence: **99.29%**
497. **`crates/swc/tests/tsc-references/doWhileBreakStatements.2.minified.js`** -> AI Confidence: **99.29%**
498. **`crates/swc/tests/tsc-references/doWhileContinueStatements.1.normal.js`** -> AI Confidence: **99.29%**
499. **`crates/swc/tests/tsc-references/doWhileContinueStatements.2.minified.js`** -> AI Confidence: **99.29%**
500. **`crates/swc/tests/tsc-references/elementAccessChain.1.normal.js`** -> AI Confidence: **99.29%**
501. **`crates/swc/tests/tsc-references/elementAccessChain.2.1.normal.js`** -> AI Confidence: **99.29%**
502. **`crates/swc/tests/tsc-references/elementAccessChain.2.2.minified.js`** -> AI Confidence: **99.29%**
503. **`crates/swc/tests/tsc-references/emitDefaultParametersFunctionExpression.2.minified.js`** -> AI Confidence: **99.29%**
504. **`crates/swc/tests/tsc-references/emitter.noCatchBinding.es2019.1.normal.js`** -> AI Confidence: **99.29%**
505. **`crates/swc/tests/tsc-references/enumConstantMemberWithString.2.minified.js`** -> AI Confidence: **99.29%**
506. **`crates/swc/tests/tsc-references/enumConstantMemberWithStringEmitDeclaration.2.minified.js`** -> AI Confidence: **99.29%**
507. **`crates/swc/tests/tsc-references/enumConstantMemberWithTemplateLiterals.2.minified.js`** -> AI Confidence: **99.29%**
508. **`crates/swc/tests/tsc-references/enumConstantMemberWithTemplateLiteralsEmitDeclaration.2.minified.js`** -> AI Confidence: **99.29%**
509. **`crates/swc/tests/tsc-references/enumMergingErrors.1.normal.js`** -> AI Confidence: **99.29%**
510. **`crates/swc/tests/tsc-references/equalityWithIntersectionTypes01.1.normal.js`** -> AI Confidence: **99.29%**
511. **`crates/swc/tests/tsc-references/equalityWithUnionTypes01.1.normal.js`** -> AI Confidence: **99.29%**
512. **`crates/swc/tests/tsc-references/equalityWithtNullishCoalescingAssignment.1.normal.js`** -> AI Confidence: **99.29%**
513. **`crates/swc/tests/tsc-references/es2016IntlAPIs.1.normal.js`** -> AI Confidence: **99.29%**
514. **`crates/swc/tests/tsc-references/es2016IntlAPIs.2.minified.js`** -> AI Confidence: **99.29%**
515. **`crates/swc/tests/tsc-references/exhaustiveSwitchStatements1.2.minified.js`** -> AI Confidence: **99.29%**
516. **`crates/swc/tests/tsc-references/exportAssignmentOfExportNamespaceWithDefault.1.normal.js`** -> AI Confidence: **99.29%**
517. **`crates/swc/tests/tsc-references/exportAssignmentOfExportNamespaceWithDefault.2.minified.js`** -> AI Confidence: **99.29%**
518. **`crates/swc/tests/tsc-references/exportClassNameWithObjectUMD.1.normal.js`** -> AI Confidence: **99.29%**
519. **`crates/swc/tests/tsc-references/for-of58.1.normal.js`** -> AI Confidence: **99.29%**
520. **`crates/swc/tests/tsc-references/forBreakStatements.1.normal.js`** -> AI Confidence: **99.29%**
521. **`crates/swc/tests/tsc-references/forBreakStatements.2.minified.js`** -> AI Confidence: **99.29%**
522. **`crates/swc/tests/tsc-references/forContinueStatements.1.normal.js`** -> AI Confidence: **99.29%**
523. **`crates/swc/tests/tsc-references/forContinueStatements.2.minified.js`** -> AI Confidence: **99.29%**
524. **`crates/swc/tests/tsc-references/forStatements.2.minified.js`** -> AI Confidence: **99.29%**
525. **`crates/swc/tests/tsc-references/forStatementsMultipleValidDecl.2.minified.js`** -> AI Confidence: **99.29%**
526. **`crates/swc/tests/tsc-references/genericCallToOverloadedMethodWithOverloadedArguments.2.minified.js`** -> AI Confidence: **99.29%**
527. **`crates/swc/tests/tsc-references/ifDoWhileStatements.2.minified.js`** -> AI Confidence: **99.29%**
528. **`crates/swc/tests/tsc-references/importCallExpressionInExportEqualsUMD.1.normal.js`** -> AI Confidence: **99.29%**
529. **`crates/swc/tests/tsc-references/importCallExpressionInUMD5.1.normal.js`** -> AI Confidence: **99.29%**
530. **`crates/swc/tests/tsc-references/importCallExpressionNestedUMD.2.minified.js`** -> AI Confidence: **99.29%**
531. **`crates/swc/tests/tsc-references/instanceofOperatorWithRHSHasSymbolHasInstance.1.normal.js`** -> AI Confidence: **99.29%**
532. **`crates/swc/tests/tsc-references/intersectionAsWeakTypeSource.2.minified.js`** -> AI Confidence: **99.29%**
533. **`crates/swc/tests/tsc-references/intersectionNarrowing.1.normal.js`** -> AI Confidence: **99.29%**
534. **`crates/swc/tests/tsc-references/intersectionOfUnionNarrowing.1.normal.js`** -> AI Confidence: **99.29%**
535. **`crates/swc/tests/tsc-references/intersectionOfUnionNarrowing.2.minified.js`** -> AI Confidence: **99.29%**
536. **`crates/swc/tests/tsc-references/invalidNestedModules.2.minified.js`** -> AI Confidence: **99.29%**
537. **`crates/swc/tests/tsc-references/invalidSwitchBreakStatement.1.normal.js`** -> AI Confidence: **99.29%**
538. **`crates/swc/tests/tsc-references/jsDeclarationsFunctionWithDefaultAssignedMember.1.normal.js`** -> AI Confidence: **99.29%**
539. **`crates/swc/tests/tsc-references/jsDeclarationsFunctionWithDefaultAssignedMember.2.minified.js`** -> AI Confidence: **99.29%**
540. **`crates/swc/tests/tsc-references/jsDeclarationsOptionalTypeLiteralProps2.1.normal.js`** -> AI Confidence: **99.29%**
541. **`crates/swc/tests/tsc-references/literalTypes1.1.normal.js`** -> AI Confidence: **99.29%**
542. **`crates/swc/tests/tsc-references/literalTypes3.1.normal.js`** -> AI Confidence: **99.29%**
543. **`crates/swc/tests/tsc-references/logicalAssignment1(target=es2015).1.normal.js`** -> AI Confidence: **99.29%**
544. **`crates/swc/tests/tsc-references/logicalAssignment1(target=es2015).2.minified.js`** -> AI Confidence: **99.29%**
545. **`crates/swc/tests/tsc-references/logicalAssignment1(target=es2020).1.normal.js`** -> AI Confidence: **99.29%**
546. **`crates/swc/tests/tsc-references/logicalAssignment1(target=es2020).2.minified.js`** -> AI Confidence: **99.29%**
547. **`crates/swc/tests/tsc-references/logicalAssignment1(target=es2021).1.normal.js`** -> AI Confidence: **99.29%**
548. **`crates/swc/tests/tsc-references/logicalAssignment1(target=es2021).2.minified.js`** -> AI Confidence: **99.29%**
549. **`crates/swc/tests/tsc-references/logicalAssignment1(target=esnext).1.normal.js`** -> AI Confidence: **99.29%**
550. **`crates/swc/tests/tsc-references/logicalAssignment1(target=esnext).2.minified.js`** -> AI Confidence: **99.29%**
551. **`crates/swc/tests/tsc-references/logicalAssignment10(target=es2020).2.minified.js`** -> AI Confidence: **99.29%**
552. **`crates/swc/tests/tsc-references/logicalAssignment10(target=es2021).2.minified.js`** -> AI Confidence: **99.29%**
553. **`crates/swc/tests/tsc-references/logicalAssignment10(target=esnext).2.minified.js`** -> AI Confidence: **99.29%**
554. **`crates/swc/tests/tsc-references/logicalAssignment11(target=es2015).2.minified.js`** -> AI Confidence: **99.29%**
555. **`crates/swc/tests/tsc-references/logicalAssignment11(target=es2020).2.minified.js`** -> AI Confidence: **99.29%**
556. **`crates/swc/tests/tsc-references/logicalAssignment11(target=esnext).2.minified.js`** -> AI Confidence: **99.29%**
557. **`crates/swc/tests/tsc-references/logicalAssignment2(target=es2015).1.normal.js`** -> AI Confidence: **99.29%**
558. **`crates/swc/tests/tsc-references/logicalAssignment2(target=es2020).1.normal.js`** -> AI Confidence: **99.29%**
559. **`crates/swc/tests/tsc-references/logicalAssignment2(target=es2021).1.normal.js`** -> AI Confidence: **99.29%**
560. **`crates/swc/tests/tsc-references/logicalAssignment2(target=es2021).2.minified.js`** -> AI Confidence: **99.29%**
561. **`crates/swc/tests/tsc-references/logicalAssignment2(target=esnext).1.normal.js`** -> AI Confidence: **99.29%**
562. **`crates/swc/tests/tsc-references/logicalAssignment2(target=esnext).2.minified.js`** -> AI Confidence: **99.29%**
563. **`crates/swc/tests/tsc-references/logicalAssignment3(target=es2015).1.normal.js`** -> AI Confidence: **99.29%**
564. **`crates/swc/tests/tsc-references/logicalAssignment3(target=es2020).1.normal.js`** -> AI Confidence: **99.29%**
565. **`crates/swc/tests/tsc-references/logicalAssignment3(target=es2020).2.minified.js`** -> AI Confidence: **99.29%**
566. **`crates/swc/tests/tsc-references/logicalAssignment3(target=es2021).1.normal.js`** -> AI Confidence: **99.29%**
567. **`crates/swc/tests/tsc-references/logicalAssignment3(target=es2021).2.minified.js`** -> AI Confidence: **99.29%**
568. **`crates/swc/tests/tsc-references/logicalAssignment3(target=esnext).1.normal.js`** -> AI Confidence: **99.29%**
569. **`crates/swc/tests/tsc-references/logicalAssignment3(target=esnext).2.minified.js`** -> AI Confidence: **99.29%**
570. **`crates/swc/tests/tsc-references/logicalAssignment4(target=es2015).1.normal.js`** -> AI Confidence: **99.29%**
571. **`crates/swc/tests/tsc-references/logicalAssignment4(target=es2020).1.normal.js`** -> AI Confidence: **99.29%**
572. **`crates/swc/tests/tsc-references/logicalAssignment4(target=es2021).1.normal.js`** -> AI Confidence: **99.29%**
573. **`crates/swc/tests/tsc-references/logicalAssignment4(target=esnext).1.normal.js`** -> AI Confidence: **99.29%**
574. **`crates/swc/tests/tsc-references/logicalAssignment6(target=es2015).1.normal.js`** -> AI Confidence: **99.29%**
575. **`crates/swc/tests/tsc-references/logicalAssignment6(target=es2020).1.normal.js`** -> AI Confidence: **99.29%**
576. **`crates/swc/tests/tsc-references/logicalAssignment6(target=es2021).1.normal.js`** -> AI Confidence: **99.29%**
577. **`crates/swc/tests/tsc-references/logicalAssignment6(target=esnext).1.normal.js`** -> AI Confidence: **99.29%**
578. **`crates/swc/tests/tsc-references/logicalAssignment7(target=es2015).1.normal.js`** -> AI Confidence: **99.29%**
579. **`crates/swc/tests/tsc-references/logicalAssignment7(target=es2020).1.normal.js`** -> AI Confidence: **99.29%**
580. **`crates/swc/tests/tsc-references/logicalAssignment7(target=es2021).1.normal.js`** -> AI Confidence: **99.29%**
581. **`crates/swc/tests/tsc-references/logicalAssignment7(target=esnext).1.normal.js`** -> AI Confidence: **99.29%**
582. **`crates/swc/tests/tsc-references/logicalAssignment8(target=es2015).1.normal.js`** -> AI Confidence: **99.29%**
583. **`crates/swc/tests/tsc-references/logicalAssignment8(target=es2020).1.normal.js`** -> AI Confidence: **99.29%**
584. **`crates/swc/tests/tsc-references/logicalAssignment8(target=es2021).1.normal.js`** -> AI Confidence: **99.29%**
585. **`crates/swc/tests/tsc-references/logicalAssignment8(target=esnext).1.normal.js`** -> AI Confidence: **99.29%**
586. **`crates/swc/tests/tsc-references/mergeThreeInterfaces2.2.minified.js`** -> AI Confidence: **99.29%**
587. **`crates/swc/tests/tsc-references/mergeTwoInterfaces2.2.minified.js`** -> AI Confidence: **99.29%**
588. **`crates/swc/tests/tsc-references/moduleExportAssignment4.1.normal.js`** -> AI Confidence: **99.29%**
589. **`crates/swc/tests/tsc-references/moduleExportAssignment4.2.minified.js`** -> AI Confidence: **99.29%**
590. **`crates/swc/tests/tsc-references/multipleDefaultExports01.2.minified.js`** -> AI Confidence: **99.29%**
591. **`crates/swc/tests/tsc-references/multipleDefaultExports02.2.minified.js`** -> AI Confidence: **99.29%**
592. **`crates/swc/tests/tsc-references/nameCollision.2.minified.js`** -> AI Confidence: **99.29%**
593. **`crates/swc/tests/tsc-references/narrowExceptionVariableInCatchClause.1.normal.js`** -> AI Confidence: **99.29%**
594. **`crates/swc/tests/tsc-references/narrowFromAnyWithInstanceof.1.normal.js`** -> AI Confidence: **99.29%**
595. **`crates/swc/tests/tsc-references/narrowFromAnyWithInstanceof.2.minified.js`** -> AI Confidence: **99.29%**
596. **`crates/swc/tests/tsc-references/narrowFromAnyWithTypePredicate.1.normal.js`** -> AI Confidence: **99.29%**
597. **`crates/swc/tests/tsc-references/narrowFromAnyWithTypePredicate.2.minified.js`** -> AI Confidence: **99.29%**
598. **`crates/swc/tests/tsc-references/nestedModules.2.minified.js`** -> AI Confidence: **99.29%**
599. **`crates/swc/tests/tsc-references/newTargetNarrowing.1.normal.js`** -> AI Confidence: **99.29%**
600. **`crates/swc/tests/tsc-references/noPropertyAccessFromIndexSignature1.1.normal.js`** -> AI Confidence: **99.29%**
601. **`crates/swc/tests/tsc-references/noPropertyAccessFromIndexSignature1.2.minified.js`** -> AI Confidence: **99.29%**
602. **`crates/swc/tests/tsc-references/nullishCoalescingOperator1.2.minified.js`** -> AI Confidence: **99.29%**
603. **`crates/swc/tests/tsc-references/nullishCoalescingOperator11.2.minified.js`** -> AI Confidence: **99.29%**
604. **`crates/swc/tests/tsc-references/nullishCoalescingOperator12.1.normal.js`** -> AI Confidence: **99.29%**
605. **`crates/swc/tests/tsc-references/nullishCoalescingOperator2.2.minified.js`** -> AI Confidence: **99.29%**
606. **`crates/swc/tests/tsc-references/nullishCoalescingOperator3.1.normal.js`** -> AI Confidence: **99.29%**
607. **`crates/swc/tests/tsc-references/nullishCoalescingOperator3.2.minified.js`** -> AI Confidence: **99.29%**
608. **`crates/swc/tests/tsc-references/nullishCoalescingOperator4.2.minified.js`** -> AI Confidence: **99.29%**
609. **`crates/swc/tests/tsc-references/nullishCoalescingOperator6.1.normal.js`** -> AI Confidence: **99.29%**
610. **`crates/swc/tests/tsc-references/nullishCoalescingOperator7.1.normal.js`** -> AI Confidence: **99.29%**
611. **`crates/swc/tests/tsc-references/nullishCoalescingOperator7.2.minified.js`** -> AI Confidence: **99.29%**
612. **`crates/swc/tests/tsc-references/nullishCoalescingOperator9.2.minified.js`** -> AI Confidence: **99.29%**
613. **`crates/swc/tests/tsc-references/nullishCoalescingOperatorInParameterInitializer.2(target=es5).2.minified.js`** -> AI Confidence: **99.29%**
614. **`crates/swc/tests/tsc-references/nullishCoalescingOperator_es2020.1.normal.js`** -> AI Confidence: **99.29%**
615. **`crates/swc/tests/tsc-references/nullishCoalescingOperator_es2020.2.minified.js`** -> AI Confidence: **99.29%**
616. **`crates/swc/tests/tsc-references/nullishCoalescingOperator_not_strict.2.minified.js`** -> AI Confidence: **99.29%**
617. **`crates/swc/tests/tsc-references/objectSpreadRepeatedComplexity.1.normal.js`** -> AI Confidence: **99.29%**
618. **`crates/swc/tests/tsc-references/objectSpreadRepeatedNullCheckPerf.1.normal.js`** -> AI Confidence: **99.29%**
619. **`crates/swc/tests/tsc-references/objectSpreadRepeatedNullCheckPerf.2.minified.js`** -> AI Confidence: **99.29%**
620. **`crates/swc/tests/tsc-references/optionalChainingInParameterBindingPattern.2(target=es5).2.minified.js`** -> AI Confidence: **99.29%**
621. **`crates/swc/tests/tsc-references/optionalChainingInTypeAssertions(target=es2015).1.normal.js`** -> AI Confidence: **99.29%**
622. **`crates/swc/tests/tsc-references/optionalChainingInTypeAssertions(target=esnext).1.normal.js`** -> AI Confidence: **99.29%**
623. **`crates/swc/tests/tsc-references/optionalChainingInTypeAssertions(target=esnext).2.minified.js`** -> AI Confidence: **99.29%**
624. **`crates/swc/tests/tsc-references/optionalChainingInference.2.minified.js`** -> AI Confidence: **99.29%**
625. **`crates/swc/tests/tsc-references/parentheses.1.normal.js`** -> AI Confidence: **99.29%**
626. **`crates/swc/tests/tsc-references/parentheses.2.minified.js`** -> AI Confidence: **99.29%**
627. **`crates/swc/tests/tsc-references/parser509693.1.normal.js`** -> AI Confidence: **99.29%**
628. **`crates/swc/tests/tsc-references/parser509693.2.minified.js`** -> AI Confidence: **99.29%**
629. **`crates/swc/tests/tsc-references/parserArrowFunctionExpression14.2.minified.js`** -> AI Confidence: **99.29%**
630. **`crates/swc/tests/tsc-references/parserArrowFunctionExpression17.2.minified.js`** -> AI Confidence: **99.29%**
631. **`crates/swc/tests/tsc-references/parserArrowFunctionExpression7.1.normal.js`** -> AI Confidence: **99.29%**
632. **`crates/swc/tests/tsc-references/parserArrowFunctionExpression9.2.minified.js`** -> AI Confidence: **99.29%**
633. **`crates/swc/tests/tsc-references/parserConditionalExpression1.1.normal.js`** -> AI Confidence: **99.29%**
634. **`crates/swc/tests/tsc-references/parserConditionalExpression1.2.minified.js`** -> AI Confidence: **99.29%**
635. **`crates/swc/tests/tsc-references/parserConstructorAmbiguity4.1.normal.js`** -> AI Confidence: **99.29%**
636. **`crates/swc/tests/tsc-references/parserConstructorAmbiguity4.2.minified.js`** -> AI Confidence: **99.29%**
637. **`crates/swc/tests/tsc-references/parserDoStatement2.1.normal.js`** -> AI Confidence: **99.29%**
638. **`crates/swc/tests/tsc-references/parserForOfStatement10.1.normal.js`** -> AI Confidence: **99.29%**
639. **`crates/swc/tests/tsc-references/parserForOfStatement11.1.normal.js`** -> AI Confidence: **99.29%**
640. **`crates/swc/tests/tsc-references/parserForOfStatement12.1.normal.js`** -> AI Confidence: **99.29%**
641. **`crates/swc/tests/tsc-references/parserForStatement3.1.normal.js`** -> AI Confidence: **99.29%**
642. **`crates/swc/tests/tsc-references/parserForStatement3.2.minified.js`** -> AI Confidence: **99.29%**
643. **`crates/swc/tests/tsc-references/parserRealSource12.1.normal.js`** -> AI Confidence: **99.29%**
644. **`crates/swc/tests/tsc-references/parserRegularExpression3.1.normal.js`** -> AI Confidence: **99.29%**
645. **`crates/swc/tests/tsc-references/parserRegularExpression4.1.normal.js`** -> AI Confidence: **99.29%**
646. **`crates/swc/tests/tsc-references/parserRegularExpression4.2.minified.js`** -> AI Confidence: **99.29%**
647. **`crates/swc/tests/tsc-references/parserRegularExpression5.1.normal.js`** -> AI Confidence: **99.29%**
648. **`crates/swc/tests/tsc-references/parserRegularExpression5.2.minified.js`** -> AI Confidence: **99.29%**
649. **`crates/swc/tests/tsc-references/parserSbp_7.9_A9_T3.1.normal.js`** -> AI Confidence: **99.29%**
650. **`crates/swc/tests/tsc-references/parserTernaryAndCommaOperators1.1.normal.js`** -> AI Confidence: **99.29%**
651. **`crates/swc/tests/tsc-references/parserTernaryAndCommaOperators1.2.minified.js`** -> AI Confidence: **99.29%**
652. **`crates/swc/tests/tsc-references/parser_breakInIterationOrSwitchStatement1.1.normal.js`** -> AI Confidence: **99.29%**
653. **`crates/swc/tests/tsc-references/parser_breakInIterationOrSwitchStatement2.1.normal.js`** -> AI Confidence: **99.29%**
654. **`crates/swc/tests/tsc-references/parser_breakInIterationOrSwitchStatement3.1.normal.js`** -> AI Confidence: **99.29%**
655. **`crates/swc/tests/tsc-references/parser_breakTarget1.1.normal.js`** -> AI Confidence: **99.29%**
656. **`crates/swc/tests/tsc-references/parser_breakTarget2.1.normal.js`** -> AI Confidence: **99.29%**
657. **`crates/swc/tests/tsc-references/parser_breakTarget3.1.normal.js`** -> AI Confidence: **99.29%**
658. **`crates/swc/tests/tsc-references/parser_breakTarget4.1.normal.js`** -> AI Confidence: **99.29%**
659. **`crates/swc/tests/tsc-references/parser_continueInIterationStatement1.1.normal.js`** -> AI Confidence: **99.29%**
660. **`crates/swc/tests/tsc-references/parser_continueInIterationStatement1.2.minified.js`** -> AI Confidence: **99.29%**
661. **`crates/swc/tests/tsc-references/parser_continueInIterationStatement2.1.normal.js`** -> AI Confidence: **99.29%**
662. **`crates/swc/tests/tsc-references/parser_continueInIterationStatement2.2.minified.js`** -> AI Confidence: **99.29%**
663. **`crates/swc/tests/tsc-references/parser_continueInIterationStatement3.1.normal.js`** -> AI Confidence: **99.29%**
664. **`crates/swc/tests/tsc-references/parser_continueInIterationStatement3.2.minified.js`** -> AI Confidence: **99.29%**
665. **`crates/swc/tests/tsc-references/parser_continueTarget2.1.normal.js`** -> AI Confidence: **99.29%**
666. **`crates/swc/tests/tsc-references/parser_continueTarget3.1.normal.js`** -> AI Confidence: **99.29%**
667. **`crates/swc/tests/tsc-references/parser_continueTarget4.1.normal.js`** -> AI Confidence: **99.29%**
668. **`crates/swc/tests/tsc-references/parser_duplicateLabel4.1.normal.js`** -> AI Confidence: **99.29%**
669. **`crates/swc/tests/tsc-references/parser_duplicateLabel4.2.minified.js`** -> AI Confidence: **99.29%**
670. **`crates/swc/tests/tsc-references/plainJSTypeErrors.1.normal.js`** -> AI Confidence: **99.29%**
671. **`crates/swc/tests/tsc-references/propertyAccessChain.1.normal.js`** -> AI Confidence: **99.29%**
672. **`crates/swc/tests/tsc-references/propertyAccessChain.2.1.normal.js`** -> AI Confidence: **99.29%**
673. **`crates/swc/tests/tsc-references/propertyAccessChain.2.minified.js`** -> AI Confidence: **99.29%**
674. **`crates/swc/tests/tsc-references/spreadDuplicate.2.minified.js`** -> AI Confidence: **99.29%**
675. **`crates/swc/tests/tsc-references/spreadDuplicateExact.2.minified.js`** -> AI Confidence: **99.29%**
676. **`crates/swc/tests/tsc-references/stringLiteralMatchedInSwitch01.1.normal.js`** -> AI Confidence: **99.29%**
677. **`crates/swc/tests/tsc-references/stringLiteralMatchedInSwitch01.2.minified.js`** -> AI Confidence: **99.29%**
678. **`crates/swc/tests/tsc-references/stringLiteralsWithSwitchStatements03.1.normal.js`** -> AI Confidence: **99.29%**
679. **`crates/swc/tests/tsc-references/stringLiteralsWithSwitchStatements04.1.normal.js`** -> AI Confidence: **99.29%**
680. **`crates/swc/tests/tsc-references/superSymbolIndexedAccess1.2.minified.js`** -> AI Confidence: **99.29%**
681. **`crates/swc/tests/tsc-references/superSymbolIndexedAccess4.2.minified.js`** -> AI Confidence: **99.29%**
682. **`crates/swc/tests/tsc-references/switchBreakStatements.1.normal.js`** -> AI Confidence: **99.29%**
683. **`crates/swc/tests/tsc-references/switchWithConstrainedTypeVariable.1.normal.js`** -> AI Confidence: **99.29%**
684. **`crates/swc/tests/tsc-references/symbolType1.1.normal.js`** -> AI Confidence: **99.29%**
685. **`crates/swc/tests/tsc-references/symbolType11.1.normal.js`** -> AI Confidence: **99.29%**
686. **`crates/swc/tests/tsc-references/templateStringInSwitchAndCase.1.normal.js`** -> AI Confidence: **99.29%**
687. **`crates/swc/tests/tsc-references/templateStringInSwitchAndCaseES6.1.normal.js`** -> AI Confidence: **99.29%**
688. **`crates/swc/tests/tsc-references/templateStringInWhile.1.normal.js`** -> AI Confidence: **99.29%**
689. **`crates/swc/tests/tsc-references/templateStringInWhile.2.minified.js`** -> AI Confidence: **99.29%**
690. **`crates/swc/tests/tsc-references/templateStringInWhileES6.1.normal.js`** -> AI Confidence: **99.29%**
691. **`crates/swc/tests/tsc-references/tryStatements.1.normal.js`** -> AI Confidence: **99.29%**
692. **`crates/swc/tests/tsc-references/typeFromJSConstructor.1.normal.js`** -> AI Confidence: **99.29%**
693. **`crates/swc/tests/tsc-references/typeFromJSConstructor.2.minified.js`** -> AI Confidence: **99.29%**
694. **`crates/swc/tests/tsc-references/typeFromPropertyAssignment36.1.normal.js`** -> AI Confidence: **99.29%**
695. **`crates/swc/tests/tsc-references/typeFromPropertyAssignment8_1.2.minified.js`** -> AI Confidence: **99.29%**
696. **`crates/swc/tests/tsc-references/typeGuardIntersectionTypes.1.normal.js`** -> AI Confidence: **99.29%**
697. **`crates/swc/tests/tsc-references/typeGuardNarrowsPrimitiveIntersection.1.normal.js`** -> AI Confidence: **99.29%**
698. **`crates/swc/tests/tsc-references/typeGuardRedundancy.2.minified.js`** -> AI Confidence: **99.29%**
699. **`crates/swc/tests/tsc-references/typeGuardTautologicalConsistiency.1.normal.js`** -> AI Confidence: **99.29%**
700. **`crates/swc/tests/tsc-references/typeGuardTypeOfUndefined.1.normal.js`** -> AI Confidence: **99.29%**
701. **`crates/swc/tests/tsc-references/typeGuardsInDoStatement.1.normal.js`** -> AI Confidence: **99.29%**
702. **`crates/swc/tests/tsc-references/typeGuardsInForStatement.1.normal.js`** -> AI Confidence: **99.29%**
703. **`crates/swc/tests/tsc-references/typeGuardsInFunctionAndModuleBlock.2.minified.js`** -> AI Confidence: **99.29%**
704. **`crates/swc/tests/tsc-references/typeGuardsInWhileStatement.1.normal.js`** -> AI Confidence: **99.29%**
705. **`crates/swc/tests/tsc-references/typeGuardsWithAny.1.normal.js`** -> AI Confidence: **99.29%**
706. **`crates/swc/tests/tsc-references/typeofOperatorWithEnumType.2.minified.js`** -> AI Confidence: **99.29%**
707. **`crates/swc/tests/tsc-references/usePromiseFinally.2.minified.js`** -> AI Confidence: **99.29%**
708. **`crates/swc/tests/tsc-references/usingDeclarations.1(target=es2017).1.normal.js`** -> AI Confidence: **99.29%**
709. **`crates/swc/tests/tsc-references/usingDeclarations.1(target=es2022).1.normal.js`** -> AI Confidence: **99.29%**
710. **`crates/swc/tests/tsc-references/usingDeclarations.1(target=esnext).1.normal.js`** -> AI Confidence: **99.29%**
711. **`crates/swc/tests/tsc-references/validMultipleVariableDeclarations.2.minified.js`** -> AI Confidence: **99.29%**
712. **`crates/swc/tests/tsc-references/whileBreakStatements.1.normal.js`** -> AI Confidence: **99.29%**
713. **`crates/swc/tests/tsc-references/whileBreakStatements.2.minified.js`** -> AI Confidence: **99.29%**
714. **`crates/swc/tests/tsc-references/whileContinueStatements.1.normal.js`** -> AI Confidence: **99.29%**
715. **`crates/swc/tests/tsc-references/whileContinueStatements.2.minified.js`** -> AI Confidence: **99.29%**
716. **`crates/swc_ecma_compat_es2019/tests/__swc_snapshots__/src/optional_catch_binding.rs/catch_binding_name_collision_1.js`** -> AI Confidence: **99.29%**
717. **`crates/swc_ecma_compat_es2019/tests/__swc_snapshots__/src/optional_catch_binding.rs/issue_411.js`** -> AI Confidence: **99.29%**
718. **`crates/swc_ecma_minifier/tests/fixture/issues/10054/if/output.js`** -> AI Confidence: **99.29%**
719. **`crates/swc_ecma_minifier/tests/fixture/issues/10849/input.js`** -> AI Confidence: **99.29%**
720. **`crates/swc_ecma_minifier/tests/fixture/issues/10986/output.js`** -> AI Confidence: **99.29%**
721. **`crates/swc_ecma_minifier/tests/fixture/issues/3629/1/input.js`** -> AI Confidence: **99.29%**
722. **`crates/swc_ecma_minifier/tests/fixture/issues/4249/input.js`** -> AI Confidence: **99.29%**
723. **`crates/swc_ecma_minifier/tests/fixture/issues/4249/output.js`** -> AI Confidence: **99.29%**
724. **`crates/swc_ecma_minifier/tests/fixture/issues/4412/input.js`** -> AI Confidence: **99.29%**
725. **`crates/swc_ecma_minifier/tests/fixture/issues/4845/input.js`** -> AI Confidence: **99.29%**
726. **`crates/swc_ecma_minifier/tests/fixture/issues/4845/output.js`** -> AI Confidence: **99.29%**
727. **`crates/swc_ecma_minifier/tests/fixture/issues/5343/input.js`** -> AI Confidence: **99.29%**
728. **`crates/swc_ecma_minifier/tests/fixture/issues/5343/output.js`** -> AI Confidence: **99.29%**
729. **`crates/swc_ecma_minifier/tests/fixture/issues/5680/input.js`** -> AI Confidence: **99.29%**
730. **`crates/swc_ecma_minifier/tests/fixture/issues/5680/output.js`** -> AI Confidence: **99.29%**
731. **`crates/swc_ecma_minifier/tests/fixture/issues/5682/output.js`** -> AI Confidence: **99.29%**
732. **`crates/swc_ecma_minifier/tests/fixture/issues/5846/input.js`** -> AI Confidence: **99.29%**
733. **`crates/swc_ecma_minifier/tests/fixture/issues/6492/1/input.js`** -> AI Confidence: **99.29%**
734. **`crates/swc_ecma_minifier/tests/fixture/issues/6492/2/input.js`** -> AI Confidence: **99.29%**
735. **`crates/swc_ecma_minifier/tests/fixture/issues/6492/3/input.js`** -> AI Confidence: **99.29%**
736. **`crates/swc_ecma_minifier/tests/fixture/issues/6492/4/input.js`** -> AI Confidence: **99.29%**
737. **`crates/swc_ecma_minifier/tests/fixture/issues/7111/input.js`** -> AI Confidence: **99.29%**
738. **`crates/swc_ecma_minifier/tests/fixture/issues/7111/output.js`** -> AI Confidence: **99.29%**
739. **`crates/swc_ecma_minifier/tests/fixture/issues/7739/1/input.js`** -> AI Confidence: **99.29%**
740. **`crates/swc_ecma_minifier/tests/fixture/issues/7739/1/output.js`** -> AI Confidence: **99.29%**
741. **`crates/swc_ecma_minifier/tests/fixture/issues/8161/input.js`** -> AI Confidence: **99.29%**
742. **`crates/swc_ecma_minifier/tests/fixture/issues/8161/output.js`** -> AI Confidence: **99.29%**
743. **`crates/swc_ecma_minifier/tests/fixture/issues/8284/output.js`** -> AI Confidence: **99.29%**
744. **`crates/swc_ecma_minifier/tests/fixture/issues/8398/input.js`** -> AI Confidence: **99.29%**
745. **`crates/swc_ecma_minifier/tests/fixture/issues/8398/output.js`** -> AI Confidence: **99.29%**
746. **`crates/swc_ecma_minifier/tests/fixture/issues/9176/input.js`** -> AI Confidence: **99.29%**
747. **`crates/swc_ecma_minifier/tests/fixture/issues/9186/2/input.js`** -> AI Confidence: **99.29%**
748. **`crates/swc_ecma_minifier/tests/fixture/issues/9504/input.js`** -> AI Confidence: **99.29%**
749. **`crates/swc_ecma_minifier/tests/fixture/issues/9504/output.js`** -> AI Confidence: **99.29%**
750. **`crates/swc_ecma_minifier/tests/fixture/issues/9757/input.js`** -> AI Confidence: **99.29%**
751. **`crates/swc_ecma_minifier/tests/fixture/issues/9922/1/input.js`** -> AI Confidence: **99.29%**
752. **`crates/swc_ecma_minifier/tests/fixture/issues/9922/2/input.js`** -> AI Confidence: **99.29%**
753. **`crates/swc_ecma_minifier/tests/fixture/issues/vercel/001/input.js`** -> AI Confidence: **99.29%**
754. **`crates/swc_ecma_minifier/tests/fixture/issues/vercel/001/output.js`** -> AI Confidence: **99.29%**
755. **`crates/swc_ecma_minifier/tests/fixture/member_expr/callee/input.js`** -> AI Confidence: **99.29%**
756. **`crates/swc_ecma_minifier/tests/fixture/member_expr/callee/output.js`** -> AI Confidence: **99.29%**
757. **`crates/swc_ecma_minifier/tests/fixture/next/react-chartjs/input.js`** -> AI Confidence: **99.29%**
758. **`crates/swc_ecma_minifier/tests/fixture/next/react-chartjs/output.js`** -> AI Confidence: **99.29%**
759. **`crates/swc_ecma_minifier/tests/fixture/pr/6272/input.js`** -> AI Confidence: **99.29%**
760. **`crates/swc_ecma_minifier/tests/fixture/pr/6272/output.js`** -> AI Confidence: **99.29%**
761. **`crates/swc_ecma_minifier/tests/fixture/projects/angular/5/input.js`** -> AI Confidence: **99.29%**
762. **`crates/swc_ecma_minifier/tests/fixture/projects/angular/5/output.js`** -> AI Confidence: **99.29%**
763. **`crates/swc_ecma_minifier/tests/fixture/projects/backbone/2/output.js`** -> AI Confidence: **99.29%**
764. **`crates/swc_ecma_minifier/tests/fixture/projects/backbone/20/output.js`** -> AI Confidence: **99.29%**
765. **`crates/swc_ecma_minifier/tests/fixture/projects/backbone/3/input.js`** -> AI Confidence: **99.29%**
766. **`crates/swc_ecma_minifier/tests/fixture/projects/backbone/3/output.js`** -> AI Confidence: **99.29%**
767. **`crates/swc_ecma_minifier/tests/fixture/projects/jquery/16/input.js`** -> AI Confidence: **99.29%**
768. **`crates/swc_ecma_minifier/tests/fixture/projects/jquery/2/input.js`** -> AI Confidence: **99.29%**
769. **`crates/swc_ecma_minifier/tests/fixture/projects/jquery/2/output.js`** -> AI Confidence: **99.29%**
770. **`crates/swc_ecma_minifier/tests/fixture/projects/jquery/23/input.js`** -> AI Confidence: **99.29%**
771. **`crates/swc_ecma_minifier/tests/fixture/projects/jquery/23/output.js`** -> AI Confidence: **99.29%**
772. **`crates/swc_ecma_minifier/tests/fixture/projects/jquery/24/input.js`** -> AI Confidence: **99.29%**
773. **`crates/swc_ecma_minifier/tests/fixture/projects/jquery/24/output.js`** -> AI Confidence: **99.29%**
774. **`crates/swc_ecma_minifier/tests/fixture/projects/jquery/25/input.js`** -> AI Confidence: **99.29%**
775. **`crates/swc_ecma_minifier/tests/fixture/projects/jquery/25/output.js`** -> AI Confidence: **99.29%**
776. **`crates/swc_ecma_minifier/tests/fixture/projects/jquery/27/input.js`** -> AI Confidence: **99.29%**
777. **`crates/swc_ecma_minifier/tests/fixture/projects/jquery/27/output.js`** -> AI Confidence: **99.29%**
778. **`crates/swc_ecma_minifier/tests/fixture/projects/jquery/5/input.js`** -> AI Confidence: **99.29%**
779. **`crates/swc_ecma_minifier/tests/fixture/projects/jquery/5/output.js`** -> AI Confidence: **99.29%**
780. **`crates/swc_ecma_minifier/tests/fixture/projects/jquery/8/input.js`** -> AI Confidence: **99.29%**
781. **`crates/swc_ecma_minifier/tests/fixture/projects/jquery/8/output.js`** -> AI Confidence: **99.29%**
782. **`crates/swc_ecma_minifier/tests/fixture/projects/mootools/8/input.js`** -> AI Confidence: **99.29%**
783. **`crates/swc_ecma_minifier/tests/fixture/projects/mootools/8/output.js`** -> AI Confidence: **99.29%**
784. **`crates/swc_ecma_minifier/tests/fixture/projects/react/1/input.js`** -> AI Confidence: **99.29%**
785. **`crates/swc_ecma_minifier/tests/fixture/projects/underscore/16/input.js`** -> AI Confidence: **99.29%**
786. **`crates/swc_ecma_minifier/tests/fixture/projects/underscore/16/output.js`** -> AI Confidence: **99.29%**
787. **`crates/swc_ecma_minifier/tests/fixture/projects/underscore/17/input.js`** -> AI Confidence: **99.29%**
788. **`crates/swc_ecma_minifier/tests/fixture/projects/underscore/17/output.js`** -> AI Confidence: **99.29%**
789. **`crates/swc_ecma_minifier/tests/fixture/projects/yui/3/input.js`** -> AI Confidence: **99.29%**
790. **`crates/swc_ecma_minifier/tests/fixture/projects/yui/3/output.js`** -> AI Confidence: **99.29%**
791. **`crates/swc_ecma_minifier/tests/fixture/projects/yui/7/input.js`** -> AI Confidence: **99.29%**
792. **`crates/swc_ecma_minifier/tests/fixture/projects/yui/7/output.js`** -> AI Confidence: **99.29%**
793. **`crates/swc_ecma_minifier/tests/fixture/reduced/2/input.js`** -> AI Confidence: **99.29%**
794. **`crates/swc_ecma_minifier/tests/fixture/simple/inline/3/input.js`** -> AI Confidence: **99.29%**
795. **`crates/swc_ecma_minifier/tests/fixture/simple/inline/3/output.js`** -> AI Confidence: **99.29%**
796. **`crates/swc_ecma_minifier/tests/fixture/simple/switch/const/call/input.js`** -> AI Confidence: **99.29%**
797. **`crates/swc_ecma_minifier/tests/fixture/simple/switch/const/call/output.js`** -> AI Confidence: **99.29%**
798. **`crates/swc_ecma_minifier/tests/fixture/simple/switch/const/default/input.js`** -> AI Confidence: **99.29%**
799. **`crates/swc_ecma_minifier/tests/fixture/simple/switch/const/order/input.js`** -> AI Confidence: **99.29%**
800. **`crates/swc_ecma_minifier/tests/fixture/simple/switch/const/order/output.js`** -> AI Confidence: **99.29%**
801. **`crates/swc_ecma_minifier/tests/fixture/simple/switch/merge/non-const/input.js`** -> AI Confidence: **99.29%**
802. **`crates/swc_ecma_minifier/tests/fixture/simple/switch/merge/non-const/output.js`** -> AI Confidence: **99.29%**
803. **`crates/swc_ecma_minifier/tests/fixture/simple/switch/merge/simple/input.js`** -> AI Confidence: **99.29%**
804. **`crates/swc_ecma_minifier/tests/fixture/simple/switch/merge/simple/output.js`** -> AI Confidence: **99.29%**
805. **`crates/swc_ecma_minifier/tests/fixture/terser/issue-2435-1/1/input.js`** -> AI Confidence: **99.29%**
806. **`crates/swc_ecma_minifier/tests/fixture/terser/issue-2435-1/1/output.js`** -> AI Confidence: **99.29%**
807. **`crates/swc_ecma_minifier/tests/fixture/terser/issue-2435-1/2/input.js`** -> AI Confidence: **99.29%**
808. **`crates/swc_ecma_minifier/tests/fixture/terser/issue-2435-1/2/output.js`** -> AI Confidence: **99.29%**
809. **`crates/swc_ecma_minifier/tests/fixture/terser/issue-2435-1/3/input.js`** -> AI Confidence: **99.29%**
810. **`crates/swc_ecma_minifier/tests/fixture/terser/issue-2435-1/3/output.js`** -> AI Confidence: **99.29%**
811. **`crates/swc_ecma_minifier/tests/fixture/terser/issue-2435-1/4/input.js`** -> AI Confidence: **99.29%**
812. **`crates/swc_ecma_minifier/tests/fixture/terser/issue-2435-1/4/output.js`** -> AI Confidence: **99.29%**
813. **`crates/swc_ecma_minifier/tests/fixture/terser/issue-2535-2/1/input.js`** -> AI Confidence: **99.29%**
814. **`crates/swc_ecma_minifier/tests/fixture/terser/issue-2535-2/1/output.js`** -> AI Confidence: **99.29%**
815. **`crates/swc_ecma_minifier/tests/fixture/terser/issue-2535-2/2-1/input.js`** -> AI Confidence: **99.29%**
816. **`crates/swc_ecma_minifier/tests/fixture/terser/issue-2535-2/2-1/output.js`** -> AI Confidence: **99.29%**
817. **`crates/swc_ecma_minifier/tests/fixture/terser/issue-2535-2/2/input.js`** -> AI Confidence: **99.29%**
818. **`crates/swc_ecma_minifier/tests/fixture/terser/issue-2535-2/2/output.js`** -> AI Confidence: **99.29%**
819. **`crates/swc_ecma_minifier/tests/fixture/terser/issue-2535-2/3-1/input.js`** -> AI Confidence: **99.29%**
820. **`crates/swc_ecma_minifier/tests/fixture/terser/issue-2535-2/3-1/output.js`** -> AI Confidence: **99.29%**
821. **`crates/swc_ecma_minifier/tests/fixture/terser/issue-2535-2/3/input.js`** -> AI Confidence: **99.29%**
822. **`crates/swc_ecma_minifier/tests/fixture/terser/issue-2535-2/3/output.js`** -> AI Confidence: **99.29%**
823. **`crates/swc_ecma_minifier/tests/fixture/terser/issue-2535-2/4/input.js`** -> AI Confidence: **99.29%**
824. **`crates/swc_ecma_minifier/tests/fixture/terser/issue-2535-2/4/output.js`** -> AI Confidence: **99.29%**
825. **`crates/swc_ecma_minifier/tests/full/size/36260571a27136b062437bddc1782e84b71055f6/input.js`** -> AI Confidence: **99.29%**
826. **`crates/swc_ecma_minifier/tests/full/size/36260571a27136b062437bddc1782e84b71055f6/output.js`** -> AI Confidence: **99.29%**
827. **`crates/swc_ecma_minifier/tests/full/size/6d52ebcc72a64f1f1ef2594baecb5dcab49b1a32/input.js`** -> AI Confidence: **99.29%**
828. **`crates/swc_ecma_minifier/tests/full/size/6d52ebcc72a64f1f1ef2594baecb5dcab49b1a32/output.js`** -> AI Confidence: **99.29%**
829. **`crates/swc_ecma_minifier/tests/full/size/80eb9c2dd2f825dd3583cd0f1ffbd56b8c6191bb/input.js`** -> AI Confidence: **99.29%**
830. **`crates/swc_ecma_minifier/tests/full/size/b44e25a2b8c64cd1d2a448bc214c8f9a589b1245/output.js`** -> AI Confidence: **99.29%**
831. **`crates/swc_ecma_minifier/tests/full/size/bfb48fed563e5fb468b88b6a6670972c3ca7ee38/input.js`** -> AI Confidence: **99.29%**
832. **`crates/swc_ecma_minifier/tests/full/size/bfb48fed563e5fb468b88b6a6670972c3ca7ee38/output.js`** -> AI Confidence: **99.29%**
833. **`crates/swc_ecma_minifier/tests/full/size/cb540d49b738ee81973607e264bc9872f88acda8/input.js`** -> AI Confidence: **99.29%**
834. **`crates/swc_ecma_minifier/tests/full/size/de4c599f0856587c5478f4f8d3cce9d91f9c8937/output.js`** -> AI Confidence: **99.29%**
835. **`crates/swc_ecma_minifier/tests/pass-1/3/output.js`** -> AI Confidence: **99.29%**
836. **`crates/swc_ecma_minifier/tests/pass-1/issue-6788/1/input.js`** -> AI Confidence: **99.29%**
837. **`crates/swc_ecma_minifier/tests/pass-1/seq/1/input.js`** -> AI Confidence: **99.29%**
838. **`crates/swc_ecma_minifier/tests/pass-1/seq/1/output.js`** -> AI Confidence: **99.29%**
839. **`crates/swc_ecma_minifier/tests/projects/files/yui-3.12.0.js`** -> AI Confidence: **99.29%**
840. **`crates/swc_ecma_minifier/tests/projects/output/yui-3.12.0.js`** -> AI Confidence: **99.29%**
841. **`crates/swc_ecma_minifier/tests/terser/compress/block_scope/issue_334/input.js`** -> AI Confidence: **99.29%**
842. **`crates/swc_ecma_minifier/tests/terser/compress/block_scope/issue_334/output.mangleOnly.js`** -> AI Confidence: **99.29%**
843. **`crates/swc_ecma_minifier/tests/terser/compress/block_scope/issue_334/output.terser.js`** -> AI Confidence: **99.29%**
844. **`crates/swc_ecma_minifier/tests/terser/compress/blocks/issue_1672_for/input.js`** -> AI Confidence: **99.29%**
845. **`crates/swc_ecma_minifier/tests/terser/compress/blocks/issue_1672_for/output.js`** -> AI Confidence: **99.29%**
846. **`crates/swc_ecma_minifier/tests/terser/compress/blocks/issue_1672_for/output.mangleOnly.js`** -> AI Confidence: **99.29%**
847. **`crates/swc_ecma_minifier/tests/terser/compress/blocks/issue_1672_for/output.terser.js`** -> AI Confidence: **99.29%**
848. **`crates/swc_ecma_minifier/tests/terser/compress/blocks/issue_1672_for_strict/input.js`** -> AI Confidence: **99.29%**
849. **`crates/swc_ecma_minifier/tests/terser/compress/blocks/issue_1672_for_strict/output.js`** -> AI Confidence: **99.29%**
850. **`crates/swc_ecma_minifier/tests/terser/compress/blocks/issue_1672_for_strict/output.mangleOnly.js`** -> AI Confidence: **99.29%**
851. **`crates/swc_ecma_minifier/tests/terser/compress/blocks/issue_1672_for_strict/output.terser.js`** -> AI Confidence: **99.29%**
852. **`crates/swc_ecma_minifier/tests/terser/compress/blocks/issue_1672_if/input.js`** -> AI Confidence: **99.29%**
853. **`crates/swc_ecma_minifier/tests/terser/compress/blocks/issue_1672_if/output.js`** -> AI Confidence: **99.29%**
854. **`crates/swc_ecma_minifier/tests/terser/compress/blocks/issue_1672_if/output.mangleOnly.js`** -> AI Confidence: **99.29%**
855. **`crates/swc_ecma_minifier/tests/terser/compress/blocks/issue_1672_if/output.terser.js`** -> AI Confidence: **99.29%**
856. **`crates/swc_ecma_minifier/tests/terser/compress/blocks/issue_1672_if_strict/input.js`** -> AI Confidence: **99.29%**
857. **`crates/swc_ecma_minifier/tests/terser/compress/blocks/issue_1672_if_strict/output.js`** -> AI Confidence: **99.29%**
858. **`crates/swc_ecma_minifier/tests/terser/compress/blocks/issue_1672_if_strict/output.mangleOnly.js`** -> AI Confidence: **99.29%**
859. **`crates/swc_ecma_minifier/tests/terser/compress/blocks/issue_1672_if_strict/output.terser.js`** -> AI Confidence: **99.29%**
860. **`crates/swc_ecma_minifier/tests/terser/compress/blocks/keep_some_blocks/input.js`** -> AI Confidence: **99.29%**
861. **`crates/swc_ecma_minifier/tests/terser/compress/blocks/keep_some_blocks/output.js`** -> AI Confidence: **99.29%**
862. **`crates/swc_ecma_minifier/tests/terser/compress/blocks/keep_some_blocks/output.mangleOnly.js`** -> AI Confidence: **99.29%**
863. **`crates/swc_ecma_minifier/tests/terser/compress/blocks/keep_some_blocks/output.terser.js`** -> AI Confidence: **99.29%**
864. **`crates/swc_ecma_minifier/tests/terser/compress/collapse_vars/cascade_conditional/input.js`** -> AI Confidence: **99.29%**
865. **`crates/swc_ecma_minifier/tests/terser/compress/collapse_vars/cascade_conditional/output.js`** -> AI Confidence: **99.29%**
866. **`crates/swc_ecma_minifier/tests/terser/compress/collapse_vars/cascade_conditional/output.mangleOnly.js`** -> AI Confidence: **99.29%**
867. **`crates/swc_ecma_minifier/tests/terser/compress/collapse_vars/cascade_conditional/output.terser.js`** -> AI Confidence: **99.29%**
868. **`crates/swc_ecma_minifier/tests/terser/compress/collapse_vars/cascade_switch/input.js`** -> AI Confidence: **99.29%**
869. **`crates/swc_ecma_minifier/tests/terser/compress/collapse_vars/cascade_switch/output.js`** -> AI Confidence: **99.29%**
870. **`crates/swc_ecma_minifier/tests/terser/compress/collapse_vars/cascade_switch/output.mangleOnly.js`** -> AI Confidence: **99.29%**
871. **`crates/swc_ecma_minifier/tests/terser/compress/collapse_vars/cascade_switch/output.terser.js`** -> AI Confidence: **99.29%**
872. **`crates/swc_ecma_minifier/tests/terser/compress/collapse_vars/cond_branch_1/output.js`** -> AI Confidence: **99.29%**
873. **`crates/swc_ecma_minifier/tests/terser/compress/collapse_vars/cond_branch_1/output.terser.js`** -> AI Confidence: **99.29%**
874. **`crates/swc_ecma_minifier/tests/terser/compress/collapse_vars/double_def_2/output.js`** -> AI Confidence: **99.29%**
875. **`crates/swc_ecma_minifier/tests/terser/compress/collapse_vars/double_def_2/output.terser.js`** -> AI Confidence: **99.29%**
876. **`crates/swc_ecma_minifier/tests/terser/compress/collapse_vars/issue_1562/output.js`** -> AI Confidence: **99.29%**
877. **`crates/swc_ecma_minifier/tests/terser/compress/collapse_vars/issue_1562/output.terser.js`** -> AI Confidence: **99.29%**
878. **`crates/swc_ecma_minifier/tests/terser/compress/collapse_vars/issue_2250_1/output.js`** -> AI Confidence: **99.29%**
879. **`crates/swc_ecma_minifier/tests/terser/compress/collapse_vars/issue_2250_1/output.terser.js`** -> AI Confidence: **99.29%**
880. **`crates/swc_ecma_minifier/tests/terser/compress/collapse_vars/issue_2873_1/input.js`** -> AI Confidence: **99.29%**
881. **`crates/swc_ecma_minifier/tests/terser/compress/collapse_vars/issue_2873_1/output.js`** -> AI Confidence: **99.29%**
882. **`crates/swc_ecma_minifier/tests/terser/compress/collapse_vars/issue_2873_1/output.mangleOnly.js`** -> AI Confidence: **99.29%**
883. **`crates/swc_ecma_minifier/tests/terser/compress/collapse_vars/issue_2873_1/output.terser.js`** -> AI Confidence: **99.29%**
884. **`crates/swc_ecma_minifier/tests/terser/compress/collapse_vars/issue_2873_2/input.js`** -> AI Confidence: **99.29%**
885. **`crates/swc_ecma_minifier/tests/terser/compress/collapse_vars/issue_2873_2/output.js`** -> AI Confidence: **99.29%**
886. **`crates/swc_ecma_minifier/tests/terser/compress/collapse_vars/issue_2873_2/output.mangleOnly.js`** -> AI Confidence: **99.29%**
887. **`crates/swc_ecma_minifier/tests/terser/compress/collapse_vars/issue_2873_2/output.terser.js`** -> AI Confidence: **99.29%**
888. **`crates/swc_ecma_minifier/tests/terser/compress/collapse_vars/issue_2954_1/input.js`** -> AI Confidence: **99.29%**
889. **`crates/swc_ecma_minifier/tests/terser/compress/collapse_vars/issue_2954_1/output.js`** -> AI Confidence: **99.29%**
890. **`crates/swc_ecma_minifier/tests/terser/compress/collapse_vars/issue_2954_1/output.mangleOnly.js`** -> AI Confidence: **99.29%**
891. **`crates/swc_ecma_minifier/tests/terser/compress/collapse_vars/issue_2954_1/output.terser.js`** -> AI Confidence: **99.29%**
892. **`crates/swc_ecma_minifier/tests/terser/compress/collapse_vars/issue_2954_2/input.js`** -> AI Confidence: **99.29%**
893. **`crates/swc_ecma_minifier/tests/terser/compress/collapse_vars/issue_2954_2/output.js`** -> AI Confidence: **99.29%**
894. **`crates/swc_ecma_minifier/tests/terser/compress/collapse_vars/issue_2954_2/output.mangleOnly.js`** -> AI Confidence: **99.29%**
895. **`crates/swc_ecma_minifier/tests/terser/compress/collapse_vars/issue_2954_2/output.terser.js`** -> AI Confidence: **99.29%**
896. **`crates/swc_ecma_minifier/tests/terser/compress/collapse_vars/issue_2954_3/input.js`** -> AI Confidence: **99.29%**
897. **`crates/swc_ecma_minifier/tests/terser/compress/collapse_vars/issue_2954_3/output.js`** -> AI Confidence: **99.29%**
898. **`crates/swc_ecma_minifier/tests/terser/compress/collapse_vars/issue_2954_3/output.mangleOnly.js`** -> AI Confidence: **99.29%**
899. **`crates/swc_ecma_minifier/tests/terser/compress/collapse_vars/issue_2954_3/output.terser.js`** -> AI Confidence: **99.29%**
900. **`crates/swc_ecma_minifier/tests/terser/compress/collapse_vars/pure_getters_chain/output.js`** -> AI Confidence: **99.29%**
901. **`crates/swc_ecma_minifier/tests/terser/compress/collapse_vars/pure_getters_chain/output.terser.js`** -> AI Confidence: **99.29%**
902. **`crates/swc_ecma_minifier/tests/terser/compress/collapse_vars/switch_case_1/output.js`** -> AI Confidence: **99.29%**
903. **`crates/swc_ecma_minifier/tests/terser/compress/collapse_vars/switch_case_1/output.terser.js`** -> AI Confidence: **99.29%**
904. **`crates/swc_ecma_minifier/tests/terser/compress/collapse_vars/switch_case_3/output.js`** -> AI Confidence: **99.29%**
905. **`crates/swc_ecma_minifier/tests/terser/compress/comparing/issue_2857_1/input.js`** -> AI Confidence: **99.29%**
906. **`crates/swc_ecma_minifier/tests/terser/compress/comparing/issue_2857_1/output.js`** -> AI Confidence: **99.29%**
907. **`crates/swc_ecma_minifier/tests/terser/compress/comparing/issue_2857_1/output.mangleOnly.js`** -> AI Confidence: **99.29%**
908. **`crates/swc_ecma_minifier/tests/terser/compress/comparing/issue_2857_1/output.terser.js`** -> AI Confidence: **99.29%**
909. **`crates/swc_ecma_minifier/tests/terser/compress/comparing/issue_2857_2/input.js`** -> AI Confidence: **99.29%**
910. **`crates/swc_ecma_minifier/tests/terser/compress/comparing/issue_2857_2/output.js`** -> AI Confidence: **99.29%**
911. **`crates/swc_ecma_minifier/tests/terser/compress/comparing/issue_2857_2/output.mangleOnly.js`** -> AI Confidence: **99.29%**
912. **`crates/swc_ecma_minifier/tests/terser/compress/comparing/issue_2857_2/output.terser.js`** -> AI Confidence: **99.29%**
913. **`crates/swc_ecma_minifier/tests/terser/compress/comparing/issue_2857_3/input.js`** -> AI Confidence: **99.29%**
914. **`crates/swc_ecma_minifier/tests/terser/compress/comparing/issue_2857_3/output.js`** -> AI Confidence: **99.29%**
915. **`crates/swc_ecma_minifier/tests/terser/compress/comparing/issue_2857_3/output.mangleOnly.js`** -> AI Confidence: **99.29%**
916. **`crates/swc_ecma_minifier/tests/terser/compress/comparing/issue_2857_3/output.terser.js`** -> AI Confidence: **99.29%**
917. **`crates/swc_ecma_minifier/tests/terser/compress/comparing/issue_2857_4/input.js`** -> AI Confidence: **99.29%**
918. **`crates/swc_ecma_minifier/tests/terser/compress/comparing/issue_2857_4/output.js`** -> AI Confidence: **99.29%**
919. **`crates/swc_ecma_minifier/tests/terser/compress/comparing/issue_2857_4/output.mangleOnly.js`** -> AI Confidence: **99.29%**
920. **`crates/swc_ecma_minifier/tests/terser/compress/comparing/issue_2857_4/output.terser.js`** -> AI Confidence: **99.29%**
921. **`crates/swc_ecma_minifier/tests/terser/compress/comparing/issue_2857_5/input.js`** -> AI Confidence: **99.29%**
922. **`crates/swc_ecma_minifier/tests/terser/compress/comparing/issue_2857_5/output.js`** -> AI Confidence: **99.29%**
923. **`crates/swc_ecma_minifier/tests/terser/compress/comparing/issue_2857_5/output.mangleOnly.js`** -> AI Confidence: **99.29%**
924. **`crates/swc_ecma_minifier/tests/terser/compress/comparing/issue_2857_5/output.terser.js`** -> AI Confidence: **99.29%**
925. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/cond_1/input.js`** -> AI Confidence: **99.29%**
926. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/cond_1/output.js`** -> AI Confidence: **99.29%**
927. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/cond_1/output.mangleOnly.js`** -> AI Confidence: **99.29%**
928. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/cond_1/output.terser.js`** -> AI Confidence: **99.29%**
929. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/cond_2/input.js`** -> AI Confidence: **99.29%**
930. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/cond_2/output.js`** -> AI Confidence: **99.29%**
931. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/cond_2/output.mangleOnly.js`** -> AI Confidence: **99.29%**
932. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/cond_2/output.terser.js`** -> AI Confidence: **99.29%**
933. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/cond_4/input.js`** -> AI Confidence: **99.29%**
934. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/cond_4/output.mangleOnly.js`** -> AI Confidence: **99.29%**
935. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/cond_5/input.js`** -> AI Confidence: **99.29%**
936. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/cond_5/output.js`** -> AI Confidence: **99.29%**
937. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/cond_5/output.mangleOnly.js`** -> AI Confidence: **99.29%**
938. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/cond_5/output.terser.js`** -> AI Confidence: **99.29%**
939. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/cond_7/input.js`** -> AI Confidence: **99.29%**
940. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/cond_7/output.mangleOnly.js`** -> AI Confidence: **99.29%**
941. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/cond_8/input.js`** -> AI Confidence: **99.29%**
942. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/cond_8/output.mangleOnly.js`** -> AI Confidence: **99.29%**
943. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/cond_8b/input.js`** -> AI Confidence: **99.29%**
944. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/cond_8b/output.mangleOnly.js`** -> AI Confidence: **99.29%**
945. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/cond_8c/input.js`** -> AI Confidence: **99.29%**
946. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/cond_8c/output.mangleOnly.js`** -> AI Confidence: **99.29%**
947. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/cond_8c/output.terser.js`** -> AI Confidence: **99.29%**
948. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/cond_9/input.js`** -> AI Confidence: **99.29%**
949. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/cond_9/output.js`** -> AI Confidence: **99.29%**
950. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/cond_9/output.mangleOnly.js`** -> AI Confidence: **99.29%**
951. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/cond_9/output.terser.js`** -> AI Confidence: **99.29%**
952. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/equality_conditionals_false/input.js`** -> AI Confidence: **99.29%**
953. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/equality_conditionals_false/output.js`** -> AI Confidence: **99.29%**
954. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/equality_conditionals_false/output.mangleOnly.js`** -> AI Confidence: **99.29%**
955. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/equality_conditionals_false/output.terser.js`** -> AI Confidence: **99.29%**
956. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/equality_conditionals_true/input.js`** -> AI Confidence: **99.29%**
957. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/equality_conditionals_true/output.js`** -> AI Confidence: **99.29%**
958. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/equality_conditionals_true/output.mangleOnly.js`** -> AI Confidence: **99.29%**
959. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/equality_conditionals_true/output.terser.js`** -> AI Confidence: **99.29%**
960. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/ifs_1/input.js`** -> AI Confidence: **99.29%**
961. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/ifs_1/output.js`** -> AI Confidence: **99.29%**
962. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/ifs_1/output.mangleOnly.js`** -> AI Confidence: **99.29%**
963. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/ifs_1/output.terser.js`** -> AI Confidence: **99.29%**
964. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/ifs_2/input.js`** -> AI Confidence: **99.29%**
965. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/ifs_2/output.js`** -> AI Confidence: **99.29%**
966. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/ifs_2/output.mangleOnly.js`** -> AI Confidence: **99.29%**
967. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/ifs_2/output.terser.js`** -> AI Confidence: **99.29%**
968. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/ifs_4/input.js`** -> AI Confidence: **99.29%**
969. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/ifs_4/output.js`** -> AI Confidence: **99.29%**
970. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/ifs_4/output.mangleOnly.js`** -> AI Confidence: **99.29%**
971. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/ifs_4/output.terser.js`** -> AI Confidence: **99.29%**
972. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/ifs_5/output.js`** -> AI Confidence: **99.29%**
973. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/ifs_5/output.terser.js`** -> AI Confidence: **99.29%**
974. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/ifs_6/input.js`** -> AI Confidence: **99.29%**
975. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/ifs_6/output.js`** -> AI Confidence: **99.29%**
976. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/ifs_6/output.mangleOnly.js`** -> AI Confidence: **99.29%**
977. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/ifs_6/output.terser.js`** -> AI Confidence: **99.29%**
978. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/ifs_same_consequent/input.js`** -> AI Confidence: **99.29%**
979. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/ifs_same_consequent/output.js`** -> AI Confidence: **99.29%**
980. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/ifs_same_consequent/output.mangleOnly.js`** -> AI Confidence: **99.29%**
981. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/ifs_same_consequent/output.terser.js`** -> AI Confidence: **99.29%**
982. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/issue_2535_1/input.js`** -> AI Confidence: **99.29%**
983. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/issue_2535_1/output.js`** -> AI Confidence: **99.29%**
984. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/issue_2535_1/output.mangleOnly.js`** -> AI Confidence: **99.29%**
985. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/issue_2535_1/output.terser.js`** -> AI Confidence: **99.29%**
986. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/issue_2535_2/input.js`** -> AI Confidence: **99.29%**
987. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/issue_2535_2/output.js`** -> AI Confidence: **99.29%**
988. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/issue_2535_2/output.mangleOnly.js`** -> AI Confidence: **99.29%**
989. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/issue_2535_2/output.terser.js`** -> AI Confidence: **99.29%**
990. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/no_evaluate/input.js`** -> AI Confidence: **99.29%**
991. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/no_evaluate/output.mangleOnly.js`** -> AI Confidence: **99.29%**
992. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/trivial_boolean_ternary_expressions/input.js`** -> AI Confidence: **99.29%**
993. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/trivial_boolean_ternary_expressions/output.mangleOnly.js`** -> AI Confidence: **99.29%**
994. **`crates/swc_ecma_minifier/tests/terser/compress/const/issue_1191/input.js`** -> AI Confidence: **99.29%**
995. **`crates/swc_ecma_minifier/tests/terser/compress/const/issue_1191/output.js`** -> AI Confidence: **99.29%**
996. **`crates/swc_ecma_minifier/tests/terser/compress/const/issue_1191/output.mangleOnly.js`** -> AI Confidence: **99.29%**
997. **`crates/swc_ecma_minifier/tests/terser/compress/const/issue_1191/output.terser.js`** -> AI Confidence: **99.29%**
998. **`crates/swc_ecma_minifier/tests/terser/compress/dead_code/global_fns/input.js`** -> AI Confidence: **99.29%**
999. **`crates/swc_ecma_minifier/tests/terser/compress/dead_code/global_fns/output.js`** -> AI Confidence: **99.29%**
1000. **`crates/swc_ecma_minifier/tests/terser/compress/dead_code/global_fns/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1001. **`crates/swc_ecma_minifier/tests/terser/compress/dead_code/global_fns/output.terser.js`** -> AI Confidence: **99.29%**
1002. **`crates/swc_ecma_minifier/tests/terser/compress/debugger/drop_debugger/input.js`** -> AI Confidence: **99.29%**
1003. **`crates/swc_ecma_minifier/tests/terser/compress/debugger/drop_debugger/output.js`** -> AI Confidence: **99.29%**
1004. **`crates/swc_ecma_minifier/tests/terser/compress/debugger/drop_debugger/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1005. **`crates/swc_ecma_minifier/tests/terser/compress/debugger/drop_debugger/output.terser.js`** -> AI Confidence: **99.29%**
1006. **`crates/swc_ecma_minifier/tests/terser/compress/defaults/defaults_false/input.js`** -> AI Confidence: **99.29%**
1007. **`crates/swc_ecma_minifier/tests/terser/compress/defaults/defaults_false/output.js`** -> AI Confidence: **99.29%**
1008. **`crates/swc_ecma_minifier/tests/terser/compress/defaults/defaults_false/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1009. **`crates/swc_ecma_minifier/tests/terser/compress/defaults/defaults_false/output.terser.js`** -> AI Confidence: **99.29%**
1010. **`crates/swc_ecma_minifier/tests/terser/compress/defaults/defaults_false_evaluate_true/input.js`** -> AI Confidence: **99.29%**
1011. **`crates/swc_ecma_minifier/tests/terser/compress/defaults/defaults_false_evaluate_true/output.js`** -> AI Confidence: **99.29%**
1012. **`crates/swc_ecma_minifier/tests/terser/compress/defaults/defaults_false_evaluate_true/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1013. **`crates/swc_ecma_minifier/tests/terser/compress/defaults/defaults_false_evaluate_true/output.terser.js`** -> AI Confidence: **99.29%**
1014. **`crates/swc_ecma_minifier/tests/terser/compress/defaults/defaults_true/input.js`** -> AI Confidence: **99.29%**
1015. **`crates/swc_ecma_minifier/tests/terser/compress/defaults/defaults_true/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1016. **`crates/swc_ecma_minifier/tests/terser/compress/defaults/defaults_true_conditionals_false/input.js`** -> AI Confidence: **99.29%**
1017. **`crates/swc_ecma_minifier/tests/terser/compress/defaults/defaults_true_conditionals_false/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1018. **`crates/swc_ecma_minifier/tests/terser/compress/defaults/defaults_true_conditionals_false/output.terser.js`** -> AI Confidence: **99.29%**
1019. **`crates/swc_ecma_minifier/tests/terser/compress/defaults/defaults_true_evaluate_false/input.js`** -> AI Confidence: **99.29%**
1020. **`crates/swc_ecma_minifier/tests/terser/compress/defaults/defaults_true_evaluate_false/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1021. **`crates/swc_ecma_minifier/tests/terser/compress/defaults/defaults_true_evaluate_false/output.terser.js`** -> AI Confidence: **99.29%**
1022. **`crates/swc_ecma_minifier/tests/terser/compress/defaults/defaults_undefined/input.js`** -> AI Confidence: **99.29%**
1023. **`crates/swc_ecma_minifier/tests/terser/compress/defaults/defaults_undefined/output.js`** -> AI Confidence: **99.29%**
1024. **`crates/swc_ecma_minifier/tests/terser/compress/defaults/defaults_undefined/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1025. **`crates/swc_ecma_minifier/tests/terser/compress/defaults/defaults_undefined/output.terser.js`** -> AI Confidence: **99.29%**
1026. **`crates/swc_ecma_minifier/tests/terser/compress/destructuring/destructuring_constdef_in_loops/input.js`** -> AI Confidence: **99.29%**
1027. **`crates/swc_ecma_minifier/tests/terser/compress/destructuring/destructuring_constdef_in_loops/output.js`** -> AI Confidence: **99.29%**
1028. **`crates/swc_ecma_minifier/tests/terser/compress/destructuring/destructuring_constdef_in_loops/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1029. **`crates/swc_ecma_minifier/tests/terser/compress/destructuring/destructuring_constdef_in_loops/output.terser.js`** -> AI Confidence: **99.29%**
1030. **`crates/swc_ecma_minifier/tests/terser/compress/drop_unused/issue_1656/output.js`** -> AI Confidence: **99.29%**
1031. **`crates/swc_ecma_minifier/tests/terser/compress/drop_unused/issue_1656/output.terser.js`** -> AI Confidence: **99.29%**
1032. **`crates/swc_ecma_minifier/tests/terser/compress/drop_unused/issue_1830_1/output.js`** -> AI Confidence: **99.29%**
1033. **`crates/swc_ecma_minifier/tests/terser/compress/drop_unused/issue_1830_1/output.terser.js`** -> AI Confidence: **99.29%**
1034. **`crates/swc_ecma_minifier/tests/terser/compress/drop_unused/issue_1838/output.js`** -> AI Confidence: **99.29%**
1035. **`crates/swc_ecma_minifier/tests/terser/compress/drop_unused/issue_1838/output.terser.js`** -> AI Confidence: **99.29%**
1036. **`crates/swc_ecma_minifier/tests/terser/compress/drop_unused/issue_3146_1/input.js`** -> AI Confidence: **99.29%**
1037. **`crates/swc_ecma_minifier/tests/terser/compress/drop_unused/issue_3146_1/output.js`** -> AI Confidence: **99.29%**
1038. **`crates/swc_ecma_minifier/tests/terser/compress/drop_unused/issue_3146_1/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1039. **`crates/swc_ecma_minifier/tests/terser/compress/drop_unused/issue_3146_1/output.terser.js`** -> AI Confidence: **99.29%**
1040. **`crates/swc_ecma_minifier/tests/terser/compress/drop_unused/issue_3146_2/input.js`** -> AI Confidence: **99.29%**
1041. **`crates/swc_ecma_minifier/tests/terser/compress/drop_unused/issue_3146_2/output.js`** -> AI Confidence: **99.29%**
1042. **`crates/swc_ecma_minifier/tests/terser/compress/drop_unused/issue_3146_2/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1043. **`crates/swc_ecma_minifier/tests/terser/compress/drop_unused/issue_3146_2/output.terser.js`** -> AI Confidence: **99.29%**
1044. **`crates/swc_ecma_minifier/tests/terser/compress/drop_unused/unused_block_decls_in_catch/output.js`** -> AI Confidence: **99.29%**
1045. **`crates/swc_ecma_minifier/tests/terser/compress/drop_unused/unused_block_decls_in_catch/output.terser.js`** -> AI Confidence: **99.29%**
1046. **`crates/swc_ecma_minifier/tests/terser/compress/drop_unused/unused_null_conditional_chain/input.js`** -> AI Confidence: **99.29%**
1047. **`crates/swc_ecma_minifier/tests/terser/compress/drop_unused/unused_null_conditional_chain/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1048. **`crates/swc_ecma_minifier/tests/terser/compress/drop_unused/unused_var_in_catch/output.js`** -> AI Confidence: **99.29%**
1049. **`crates/swc_ecma_minifier/tests/terser/compress/drop_unused/unused_var_in_catch/output.terser.js`** -> AI Confidence: **99.29%**
1050. **`crates/swc_ecma_minifier/tests/terser/compress/drop_unused/used_block_decls_in_catch/output.js`** -> AI Confidence: **99.29%**
1051. **`crates/swc_ecma_minifier/tests/terser/compress/drop_unused/used_block_decls_in_catch/output.terser.js`** -> AI Confidence: **99.29%**
1052. **`crates/swc_ecma_minifier/tests/terser/compress/evaluate/and/input.js`** -> AI Confidence: **99.29%**
1053. **`crates/swc_ecma_minifier/tests/terser/compress/evaluate/and/output.js`** -> AI Confidence: **99.29%**
1054. **`crates/swc_ecma_minifier/tests/terser/compress/evaluate/and/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1055. **`crates/swc_ecma_minifier/tests/terser/compress/evaluate/and/output.terser.js`** -> AI Confidence: **99.29%**
1056. **`crates/swc_ecma_minifier/tests/terser/compress/evaluate/issue_1760_1/input.js`** -> AI Confidence: **99.29%**
1057. **`crates/swc_ecma_minifier/tests/terser/compress/evaluate/issue_1760_1/output.js`** -> AI Confidence: **99.29%**
1058. **`crates/swc_ecma_minifier/tests/terser/compress/evaluate/issue_1760_1/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1059. **`crates/swc_ecma_minifier/tests/terser/compress/evaluate/issue_1760_1/output.terser.js`** -> AI Confidence: **99.29%**
1060. **`crates/swc_ecma_minifier/tests/terser/compress/evaluate/issue_1760_2/input.js`** -> AI Confidence: **99.29%**
1061. **`crates/swc_ecma_minifier/tests/terser/compress/evaluate/issue_1760_2/output.js`** -> AI Confidence: **99.29%**
1062. **`crates/swc_ecma_minifier/tests/terser/compress/evaluate/issue_1760_2/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1063. **`crates/swc_ecma_minifier/tests/terser/compress/evaluate/issue_1760_2/output.terser.js`** -> AI Confidence: **99.29%**
1064. **`crates/swc_ecma_minifier/tests/terser/compress/evaluate/issue_2535_1/input.js`** -> AI Confidence: **99.29%**
1065. **`crates/swc_ecma_minifier/tests/terser/compress/evaluate/issue_2535_1/output.js`** -> AI Confidence: **99.29%**
1066. **`crates/swc_ecma_minifier/tests/terser/compress/evaluate/issue_2535_1/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1067. **`crates/swc_ecma_minifier/tests/terser/compress/evaluate/issue_2535_1/output.terser.js`** -> AI Confidence: **99.29%**
1068. **`crates/swc_ecma_minifier/tests/terser/compress/evaluate/issue_2535_2/input.js`** -> AI Confidence: **99.29%**
1069. **`crates/swc_ecma_minifier/tests/terser/compress/evaluate/issue_2535_2/output.js`** -> AI Confidence: **99.29%**
1070. **`crates/swc_ecma_minifier/tests/terser/compress/evaluate/issue_2535_2/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1071. **`crates/swc_ecma_minifier/tests/terser/compress/evaluate/issue_2535_2/output.terser.js`** -> AI Confidence: **99.29%**
1072. **`crates/swc_ecma_minifier/tests/terser/compress/evaluate/issue_2535_3/input.js`** -> AI Confidence: **99.29%**
1073. **`crates/swc_ecma_minifier/tests/terser/compress/evaluate/issue_2535_3/output.js`** -> AI Confidence: **99.29%**
1074. **`crates/swc_ecma_minifier/tests/terser/compress/evaluate/issue_2535_3/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1075. **`crates/swc_ecma_minifier/tests/terser/compress/evaluate/issue_2535_3/output.terser.js`** -> AI Confidence: **99.29%**
1076. **`crates/swc_ecma_minifier/tests/terser/compress/evaluate/null_conditional_chain_eval/input.js`** -> AI Confidence: **99.29%**
1077. **`crates/swc_ecma_minifier/tests/terser/compress/evaluate/null_conditional_chain_eval/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1078. **`crates/swc_ecma_minifier/tests/terser/compress/evaluate/or/input.js`** -> AI Confidence: **99.29%**
1079. **`crates/swc_ecma_minifier/tests/terser/compress/evaluate/or/output.js`** -> AI Confidence: **99.29%**
1080. **`crates/swc_ecma_minifier/tests/terser/compress/evaluate/or/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1081. **`crates/swc_ecma_minifier/tests/terser/compress/evaluate/or/output.terser.js`** -> AI Confidence: **99.29%**
1082. **`crates/swc_ecma_minifier/tests/terser/compress/evaluate/unary_prefix/input.js`** -> AI Confidence: **99.29%**
1083. **`crates/swc_ecma_minifier/tests/terser/compress/evaluate/unary_prefix/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1084. **`crates/swc_ecma_minifier/tests/terser/compress/expansions/avoid_spread_in_ternary/input.js`** -> AI Confidence: **99.29%**
1085. **`crates/swc_ecma_minifier/tests/terser/compress/expansions/avoid_spread_in_ternary/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1086. **`crates/swc_ecma_minifier/tests/terser/compress/functions/hoist_funs/input.js`** -> AI Confidence: **99.29%**
1087. **`crates/swc_ecma_minifier/tests/terser/compress/functions/hoist_funs/output.js`** -> AI Confidence: **99.29%**
1088. **`crates/swc_ecma_minifier/tests/terser/compress/functions/hoist_funs/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1089. **`crates/swc_ecma_minifier/tests/terser/compress/functions/hoist_funs/output.terser.js`** -> AI Confidence: **99.29%**
1090. **`crates/swc_ecma_minifier/tests/terser/compress/functions/hoist_funs_strict/input.js`** -> AI Confidence: **99.29%**
1091. **`crates/swc_ecma_minifier/tests/terser/compress/functions/hoist_funs_strict/output.js`** -> AI Confidence: **99.29%**
1092. **`crates/swc_ecma_minifier/tests/terser/compress/functions/hoist_funs_strict/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1093. **`crates/swc_ecma_minifier/tests/terser/compress/functions/hoist_funs_strict/output.terser.js`** -> AI Confidence: **99.29%**
1094. **`crates/swc_ecma_minifier/tests/terser/compress/functions/inline_loop_1/output.js`** -> AI Confidence: **99.29%**
1095. **`crates/swc_ecma_minifier/tests/terser/compress/functions/inline_loop_1/output.terser.js`** -> AI Confidence: **99.29%**
1096. **`crates/swc_ecma_minifier/tests/terser/compress/functions/inline_loop_2/output.js`** -> AI Confidence: **99.29%**
1097. **`crates/swc_ecma_minifier/tests/terser/compress/functions/inline_loop_2/output.terser.js`** -> AI Confidence: **99.29%**
1098. **`crates/swc_ecma_minifier/tests/terser/compress/functions/inline_loop_3/output.js`** -> AI Confidence: **99.29%**
1099. **`crates/swc_ecma_minifier/tests/terser/compress/functions/inline_loop_3/output.terser.js`** -> AI Confidence: **99.29%**
1100. **`crates/swc_ecma_minifier/tests/terser/compress/functions/issue_2097/input.js`** -> AI Confidence: **99.29%**
1101. **`crates/swc_ecma_minifier/tests/terser/compress/functions/issue_2097/output.js`** -> AI Confidence: **99.29%**
1102. **`crates/swc_ecma_minifier/tests/terser/compress/functions/issue_2097/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1103. **`crates/swc_ecma_minifier/tests/terser/compress/functions/issue_2097/output.terser.js`** -> AI Confidence: **99.29%**
1104. **`crates/swc_ecma_minifier/tests/terser/compress/functions/issue_2604_1/input.js`** -> AI Confidence: **99.29%**
1105. **`crates/swc_ecma_minifier/tests/terser/compress/functions/issue_2604_1/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1106. **`crates/swc_ecma_minifier/tests/terser/compress/functions/issue_2604_1/output.terser.js`** -> AI Confidence: **99.29%**
1107. **`crates/swc_ecma_minifier/tests/terser/compress/functions/issue_2604_2/input.js`** -> AI Confidence: **99.29%**
1108. **`crates/swc_ecma_minifier/tests/terser/compress/functions/issue_2604_2/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1109. **`crates/swc_ecma_minifier/tests/terser/compress/functions/issue_2620_3/input.js`** -> AI Confidence: **99.29%**
1110. **`crates/swc_ecma_minifier/tests/terser/compress/functions/issue_2620_3/output.js`** -> AI Confidence: **99.29%**
1111. **`crates/swc_ecma_minifier/tests/terser/compress/functions/issue_2620_3/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1112. **`crates/swc_ecma_minifier/tests/terser/compress/functions/issue_2620_3/output.terser.js`** -> AI Confidence: **99.29%**
1113. **`crates/swc_ecma_minifier/tests/terser/compress/functions/issue_2620_4/input.js`** -> AI Confidence: **99.29%**
1114. **`crates/swc_ecma_minifier/tests/terser/compress/functions/issue_2620_4/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1115. **`crates/swc_ecma_minifier/tests/terser/compress/functions/issue_2737_1/input.js`** -> AI Confidence: **99.29%**
1116. **`crates/swc_ecma_minifier/tests/terser/compress/functions/issue_2737_1/output.js`** -> AI Confidence: **99.29%**
1117. **`crates/swc_ecma_minifier/tests/terser/compress/functions/issue_2737_1/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1118. **`crates/swc_ecma_minifier/tests/terser/compress/functions/issue_2737_1/output.terser.js`** -> AI Confidence: **99.29%**
1119. **`crates/swc_ecma_minifier/tests/terser/compress/functions/issue_2783/output.js`** -> AI Confidence: **99.29%**
1120. **`crates/swc_ecma_minifier/tests/terser/compress/functions/recursive_inline_1/input.js`** -> AI Confidence: **99.29%**
1121. **`crates/swc_ecma_minifier/tests/terser/compress/functions/recursive_inline_1/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1122. **`crates/swc_ecma_minifier/tests/terser/compress/global_defs/conditional_chains/input.js`** -> AI Confidence: **99.29%**
1123. **`crates/swc_ecma_minifier/tests/terser/compress/global_defs/conditional_chains/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1124. **`crates/swc_ecma_minifier/tests/terser/compress/global_defs/issue_2167/input.js`** -> AI Confidence: **99.29%**
1125. **`crates/swc_ecma_minifier/tests/terser/compress/global_defs/issue_2167/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1126. **`crates/swc_ecma_minifier/tests/terser/compress/harmony/issue_2794_3/output.js`** -> AI Confidence: **99.29%**
1127. **`crates/swc_ecma_minifier/tests/terser/compress/harmony/issue_2794_3/output.terser.js`** -> AI Confidence: **99.29%**
1128. **`crates/swc_ecma_minifier/tests/terser/compress/harmony/module_enables_strict_mode/input.js`** -> AI Confidence: **99.29%**
1129. **`crates/swc_ecma_minifier/tests/terser/compress/harmony/module_enables_strict_mode/output.js`** -> AI Confidence: **99.29%**
1130. **`crates/swc_ecma_minifier/tests/terser/compress/harmony/module_enables_strict_mode/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1131. **`crates/swc_ecma_minifier/tests/terser/compress/harmony/module_enables_strict_mode/output.terser.js`** -> AI Confidence: **99.29%**
1132. **`crates/swc_ecma_minifier/tests/terser/compress/harmony/regression_for_of_const/input.js`** -> AI Confidence: **99.29%**
1133. **`crates/swc_ecma_minifier/tests/terser/compress/harmony/regression_for_of_const/output.js`** -> AI Confidence: **99.29%**
1134. **`crates/swc_ecma_minifier/tests/terser/compress/harmony/regression_for_of_const/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1135. **`crates/swc_ecma_minifier/tests/terser/compress/harmony/regression_for_of_const/output.terser.js`** -> AI Confidence: **99.29%**
1136. **`crates/swc_ecma_minifier/tests/terser/compress/hoist_props/issue_851_hoist_to_conflicting_name/input.js`** -> AI Confidence: **99.29%**
1137. **`crates/swc_ecma_minifier/tests/terser/compress/hoist_props/issue_851_hoist_to_conflicting_name/output.js`** -> AI Confidence: **99.29%**
1138. **`crates/swc_ecma_minifier/tests/terser/compress/hoist_props/issue_851_hoist_to_conflicting_name/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1139. **`crates/swc_ecma_minifier/tests/terser/compress/hoist_props/issue_851_hoist_to_conflicting_name/output.terser.js`** -> AI Confidence: **99.29%**
1140. **`crates/swc_ecma_minifier/tests/terser/compress/ie8/issue_1586_1/input.js`** -> AI Confidence: **99.29%**
1141. **`crates/swc_ecma_minifier/tests/terser/compress/ie8/issue_1586_1/output.js`** -> AI Confidence: **99.29%**
1142. **`crates/swc_ecma_minifier/tests/terser/compress/ie8/issue_1586_1/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1143. **`crates/swc_ecma_minifier/tests/terser/compress/ie8/issue_1586_1/output.terser.js`** -> AI Confidence: **99.29%**
1144. **`crates/swc_ecma_minifier/tests/terser/compress/ie8/issue_1586_2/input.js`** -> AI Confidence: **99.29%**
1145. **`crates/swc_ecma_minifier/tests/terser/compress/ie8/issue_1586_2/output.js`** -> AI Confidence: **99.29%**
1146. **`crates/swc_ecma_minifier/tests/terser/compress/ie8/issue_1586_2/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1147. **`crates/swc_ecma_minifier/tests/terser/compress/ie8/issue_1586_2/output.terser.js`** -> AI Confidence: **99.29%**
1148. **`crates/swc_ecma_minifier/tests/terser/compress/ie8/issue_2120_1/input.js`** -> AI Confidence: **99.29%**
1149. **`crates/swc_ecma_minifier/tests/terser/compress/ie8/issue_2120_1/output.js`** -> AI Confidence: **99.29%**
1150. **`crates/swc_ecma_minifier/tests/terser/compress/ie8/issue_2120_1/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1151. **`crates/swc_ecma_minifier/tests/terser/compress/ie8/issue_2120_1/output.terser.js`** -> AI Confidence: **99.29%**
1152. **`crates/swc_ecma_minifier/tests/terser/compress/ie8/issue_2120_2/input.js`** -> AI Confidence: **99.29%**
1153. **`crates/swc_ecma_minifier/tests/terser/compress/ie8/issue_2120_2/output.js`** -> AI Confidence: **99.29%**
1154. **`crates/swc_ecma_minifier/tests/terser/compress/ie8/issue_2120_2/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1155. **`crates/swc_ecma_minifier/tests/terser/compress/ie8/issue_2120_2/output.terser.js`** -> AI Confidence: **99.29%**
1156. **`crates/swc_ecma_minifier/tests/terser/compress/ie8/issue_2254_1/input.js`** -> AI Confidence: **99.29%**
1157. **`crates/swc_ecma_minifier/tests/terser/compress/ie8/issue_2254_1/output.js`** -> AI Confidence: **99.29%**
1158. **`crates/swc_ecma_minifier/tests/terser/compress/ie8/issue_2254_1/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1159. **`crates/swc_ecma_minifier/tests/terser/compress/ie8/issue_2254_1/output.terser.js`** -> AI Confidence: **99.29%**
1160. **`crates/swc_ecma_minifier/tests/terser/compress/ie8/issue_2254_2/input.js`** -> AI Confidence: **99.29%**
1161. **`crates/swc_ecma_minifier/tests/terser/compress/ie8/issue_2254_2/output.js`** -> AI Confidence: **99.29%**
1162. **`crates/swc_ecma_minifier/tests/terser/compress/ie8/issue_2254_2/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1163. **`crates/swc_ecma_minifier/tests/terser/compress/ie8/issue_2254_2/output.terser.js`** -> AI Confidence: **99.29%**
1164. **`crates/swc_ecma_minifier/tests/terser/compress/if_return/issue_512/output.js`** -> AI Confidence: **99.29%**
1165. **`crates/swc_ecma_minifier/tests/terser/compress/if_return/issue_512/output.terser.js`** -> AI Confidence: **99.29%**
1166. **`crates/swc_ecma_minifier/tests/terser/compress/inline/inline_into_scope_conflict_enclosed/input.js`** -> AI Confidence: **99.29%**
1167. **`crates/swc_ecma_minifier/tests/terser/compress/inline/inline_into_scope_conflict_enclosed/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1168. **`crates/swc_ecma_minifier/tests/terser/compress/inline/issue_308/output.terser.js`** -> AI Confidence: **99.29%**
1169. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1041/const_declaration/input.js`** -> AI Confidence: **99.29%**
1170. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1041/const_declaration/output.js`** -> AI Confidence: **99.29%**
1171. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1041/const_declaration/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1172. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1041/const_declaration/output.terser.js`** -> AI Confidence: **99.29%**
1173. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1052/deeply_nested/output.js`** -> AI Confidence: **99.29%**
1174. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1052/deeply_nested/output.terser.js`** -> AI Confidence: **99.29%**
1175. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1052/defun_else_if_return/output.js`** -> AI Confidence: **99.29%**
1176. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1052/defun_else_if_return/output.terser.js`** -> AI Confidence: **99.29%**
1177. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1052/defun_hoist_funs/output.js`** -> AI Confidence: **99.29%**
1178. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1052/defun_hoist_funs/output.terser.js`** -> AI Confidence: **99.29%**
1179. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1052/defun_if_return/output.js`** -> AI Confidence: **99.29%**
1180. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1052/defun_if_return/output.terser.js`** -> AI Confidence: **99.29%**
1181. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1052/multiple_functions/output.js`** -> AI Confidence: **99.29%**
1182. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1052/multiple_functions/output.terser.js`** -> AI Confidence: **99.29%**
1183. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1052/not_hoisted_when_already_nested/output.js`** -> AI Confidence: **99.29%**
1184. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1052/not_hoisted_when_already_nested/output.terser.js`** -> AI Confidence: **99.29%**
1185. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1052/single_function/output.js`** -> AI Confidence: **99.29%**
1186. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1052/single_function/output.terser.js`** -> AI Confidence: **99.29%**
1187. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1275/string_plus_optimization/input.js`** -> AI Confidence: **99.29%**
1188. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1275/string_plus_optimization/output.js`** -> AI Confidence: **99.29%**
1189. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1275/string_plus_optimization/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1190. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1275/string_plus_optimization/output.terser.js`** -> AI Confidence: **99.29%**
1191. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1447/else_with_empty_block/input.js`** -> AI Confidence: **99.29%**
1192. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1447/else_with_empty_block/output.js`** -> AI Confidence: **99.29%**
1193. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1447/else_with_empty_block/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1194. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1447/else_with_empty_block/output.terser.js`** -> AI Confidence: **99.29%**
1195. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1447/else_with_empty_statement/input.js`** -> AI Confidence: **99.29%**
1196. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1447/else_with_empty_statement/output.js`** -> AI Confidence: **99.29%**
1197. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1447/else_with_empty_statement/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1198. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1447/else_with_empty_statement/output.terser.js`** -> AI Confidence: **99.29%**
1199. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1588/screw_ie8/input.js`** -> AI Confidence: **99.29%**
1200. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1588/screw_ie8/output.js`** -> AI Confidence: **99.29%**
1201. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1588/screw_ie8/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1202. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1588/screw_ie8/output.terser.js`** -> AI Confidence: **99.29%**
1203. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1588/support_ie8/input.js`** -> AI Confidence: **99.29%**
1204. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1588/support_ie8/output.js`** -> AI Confidence: **99.29%**
1205. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1588/support_ie8/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1206. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1588/support_ie8/output.terser.js`** -> AI Confidence: **99.29%**
1207. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1673/side_effects_catch/input.js`** -> AI Confidence: **99.29%**
1208. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1673/side_effects_catch/output.js`** -> AI Confidence: **99.29%**
1209. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1673/side_effects_catch/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1210. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1673/side_effects_catch/output.terser.js`** -> AI Confidence: **99.29%**
1211. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1673/side_effects_else/input.js`** -> AI Confidence: **99.29%**
1212. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1673/side_effects_else/output.js`** -> AI Confidence: **99.29%**
1213. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1673/side_effects_else/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1214. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1673/side_effects_else/output.terser.js`** -> AI Confidence: **99.29%**
1215. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1673/side_effects_finally/input.js`** -> AI Confidence: **99.29%**
1216. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1673/side_effects_finally/output.js`** -> AI Confidence: **99.29%**
1217. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1673/side_effects_finally/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1218. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1673/side_effects_finally/output.terser.js`** -> AI Confidence: **99.29%**
1219. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1673/side_effects_label/input.js`** -> AI Confidence: **99.29%**
1220. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1673/side_effects_label/output.js`** -> AI Confidence: **99.29%**
1221. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1673/side_effects_label/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1222. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1673/side_effects_label/output.terser.js`** -> AI Confidence: **99.29%**
1223. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1673/side_effects_switch/input.js`** -> AI Confidence: **99.29%**
1224. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1673/side_effects_switch/output.js`** -> AI Confidence: **99.29%**
1225. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1673/side_effects_switch/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1226. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1673/side_effects_switch/output.terser.js`** -> AI Confidence: **99.29%**
1227. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1750/case_1/input.js`** -> AI Confidence: **99.29%**
1228. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1750/case_1/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1229. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1750/case_2/input.js`** -> AI Confidence: **99.29%**
1230. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1750/case_2/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1231. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1833/iife_do/input.js`** -> AI Confidence: **99.29%**
1232. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1833/iife_do/output.js`** -> AI Confidence: **99.29%**
1233. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1833/iife_do/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1234. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1833/iife_do/output.terser.js`** -> AI Confidence: **99.29%**
1235. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1833/iife_for/input.js`** -> AI Confidence: **99.29%**
1236. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1833/iife_for/output.js`** -> AI Confidence: **99.29%**
1237. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1833/iife_for/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1238. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1833/iife_for/output.terser.js`** -> AI Confidence: **99.29%**
1239. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1833/iife_while/input.js`** -> AI Confidence: **99.29%**
1240. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1833/iife_while/output.js`** -> AI Confidence: **99.29%**
1241. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1833/iife_while/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1242. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1833/iife_while/output.terser.js`** -> AI Confidence: **99.29%**
1243. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1833/label_do/input.js`** -> AI Confidence: **99.29%**
1244. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1833/label_do/output.js`** -> AI Confidence: **99.29%**
1245. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1833/label_do/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1246. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1833/label_do/output.terser.js`** -> AI Confidence: **99.29%**
1247. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1833/label_while/input.js`** -> AI Confidence: **99.29%**
1248. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1833/label_while/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1249. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1943/keyword/input.js`** -> AI Confidence: **99.29%**
1250. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1943/keyword/output.js`** -> AI Confidence: **99.29%**
1251. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1943/keyword/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1252. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1943/keyword/output.terser.js`** -> AI Confidence: **99.29%**
1253. **`crates/swc_ecma_minifier/tests/terser/compress/issue_281/issue_1288_side_effects/input.js`** -> AI Confidence: **99.29%**
1254. **`crates/swc_ecma_minifier/tests/terser/compress/issue_281/issue_1288_side_effects/output.js`** -> AI Confidence: **99.29%**
1255. **`crates/swc_ecma_minifier/tests/terser/compress/issue_281/issue_1288_side_effects/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1256. **`crates/swc_ecma_minifier/tests/terser/compress/issue_281/issue_1288_side_effects/output.terser.js`** -> AI Confidence: **99.29%**
1257. **`crates/swc_ecma_minifier/tests/terser/compress/issue_281/negate_iife_3/output.js`** -> AI Confidence: **99.29%**
1258. **`crates/swc_ecma_minifier/tests/terser/compress/issue_281/negate_iife_3/output.terser.js`** -> AI Confidence: **99.29%**
1259. **`crates/swc_ecma_minifier/tests/terser/compress/issue_281/negate_iife_3_off/output.js`** -> AI Confidence: **99.29%**
1260. **`crates/swc_ecma_minifier/tests/terser/compress/issue_281/negate_iife_3_off/output.terser.js`** -> AI Confidence: **99.29%**
1261. **`crates/swc_ecma_minifier/tests/terser/compress/issue_281/negate_iife_4/output.js`** -> AI Confidence: **99.29%**
1262. **`crates/swc_ecma_minifier/tests/terser/compress/issue_281/negate_iife_4/output.terser.js`** -> AI Confidence: **99.29%**
1263. **`crates/swc_ecma_minifier/tests/terser/compress/issue_281/negate_iife_5/output.js`** -> AI Confidence: **99.29%**
1264. **`crates/swc_ecma_minifier/tests/terser/compress/issue_281/negate_iife_5/output.terser.js`** -> AI Confidence: **99.29%**
1265. **`crates/swc_ecma_minifier/tests/terser/compress/issue_281/negate_iife_5_off/output.js`** -> AI Confidence: **99.29%**
1266. **`crates/swc_ecma_minifier/tests/terser/compress/issue_281/negate_iife_5_off/output.terser.js`** -> AI Confidence: **99.29%**
1267. **`crates/swc_ecma_minifier/tests/terser/compress/issue_59/keep_continue/input.js`** -> AI Confidence: **99.29%**
1268. **`crates/swc_ecma_minifier/tests/terser/compress/issue_59/keep_continue/output.js`** -> AI Confidence: **99.29%**
1269. **`crates/swc_ecma_minifier/tests/terser/compress/issue_59/keep_continue/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1270. **`crates/swc_ecma_minifier/tests/terser/compress/issue_59/keep_continue/output.terser.js`** -> AI Confidence: **99.29%**
1271. **`crates/swc_ecma_minifier/tests/terser/compress/issue_597/issue_1725/input.js`** -> AI Confidence: **99.29%**
1272. **`crates/swc_ecma_minifier/tests/terser/compress/issue_597/issue_1725/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1273. **`crates/swc_ecma_minifier/tests/terser/compress/issue_597/issue_1725/output.terser.js`** -> AI Confidence: **99.29%**
1274. **`crates/swc_ecma_minifier/tests/terser/compress/issue_637/wrongly_optimized/input.js`** -> AI Confidence: **99.29%**
1275. **`crates/swc_ecma_minifier/tests/terser/compress/issue_637/wrongly_optimized/output.js`** -> AI Confidence: **99.29%**
1276. **`crates/swc_ecma_minifier/tests/terser/compress/issue_637/wrongly_optimized/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1277. **`crates/swc_ecma_minifier/tests/terser/compress/issue_637/wrongly_optimized/output.terser.js`** -> AI Confidence: **99.29%**
1278. **`crates/swc_ecma_minifier/tests/terser/compress/issue_640/cond_5/input.js`** -> AI Confidence: **99.29%**
1279. **`crates/swc_ecma_minifier/tests/terser/compress/issue_640/cond_5/output.js`** -> AI Confidence: **99.29%**
1280. **`crates/swc_ecma_minifier/tests/terser/compress/issue_640/cond_5/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1281. **`crates/swc_ecma_minifier/tests/terser/compress/issue_640/cond_5/output.terser.js`** -> AI Confidence: **99.29%**
1282. **`crates/swc_ecma_minifier/tests/terser/compress/issue_640/conditional/input.js`** -> AI Confidence: **99.29%**
1283. **`crates/swc_ecma_minifier/tests/terser/compress/issue_640/conditional/output.js`** -> AI Confidence: **99.29%**
1284. **`crates/swc_ecma_minifier/tests/terser/compress/issue_640/conditional/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1285. **`crates/swc_ecma_minifier/tests/terser/compress/issue_640/conditional/output.terser.js`** -> AI Confidence: **99.29%**
1286. **`crates/swc_ecma_minifier/tests/terser/compress/issue_640/wrongly_optimized/input.js`** -> AI Confidence: **99.29%**
1287. **`crates/swc_ecma_minifier/tests/terser/compress/issue_640/wrongly_optimized/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1288. **`crates/swc_ecma_minifier/tests/terser/compress/issue_640/wrongly_optimized/output.terser.js`** -> AI Confidence: **99.29%**
1289. **`crates/swc_ecma_minifier/tests/terser/compress/issue_751/negate_booleans_1/input.js`** -> AI Confidence: **99.29%**
1290. **`crates/swc_ecma_minifier/tests/terser/compress/issue_751/negate_booleans_1/output.js`** -> AI Confidence: **99.29%**
1291. **`crates/swc_ecma_minifier/tests/terser/compress/issue_751/negate_booleans_1/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1292. **`crates/swc_ecma_minifier/tests/terser/compress/issue_751/negate_booleans_1/output.terser.js`** -> AI Confidence: **99.29%**
1293. **`crates/swc_ecma_minifier/tests/terser/compress/issue_751/negate_booleans_2/input.js`** -> AI Confidence: **99.29%**
1294. **`crates/swc_ecma_minifier/tests/terser/compress/issue_751/negate_booleans_2/output.js`** -> AI Confidence: **99.29%**
1295. **`crates/swc_ecma_minifier/tests/terser/compress/issue_751/negate_booleans_2/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1296. **`crates/swc_ecma_minifier/tests/terser/compress/issue_751/negate_booleans_2/output.terser.js`** -> AI Confidence: **99.29%**
1297. **`crates/swc_ecma_minifier/tests/terser/compress/issue_973/this_binding_conditionals/input.js`** -> AI Confidence: **99.29%**
1298. **`crates/swc_ecma_minifier/tests/terser/compress/issue_973/this_binding_conditionals/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1299. **`crates/swc_ecma_minifier/tests/terser/compress/issue_979/issue979_reported/input.js`** -> AI Confidence: **99.29%**
1300. **`crates/swc_ecma_minifier/tests/terser/compress/issue_979/issue979_reported/output.js`** -> AI Confidence: **99.29%**
1301. **`crates/swc_ecma_minifier/tests/terser/compress/issue_979/issue979_reported/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1302. **`crates/swc_ecma_minifier/tests/terser/compress/issue_979/issue979_reported/output.terser.js`** -> AI Confidence: **99.29%**
1303. **`crates/swc_ecma_minifier/tests/terser/compress/issue_979/issue979_test_negated_is_best/input.js`** -> AI Confidence: **99.29%**
1304. **`crates/swc_ecma_minifier/tests/terser/compress/issue_979/issue979_test_negated_is_best/output.js`** -> AI Confidence: **99.29%**
1305. **`crates/swc_ecma_minifier/tests/terser/compress/issue_979/issue979_test_negated_is_best/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1306. **`crates/swc_ecma_minifier/tests/terser/compress/issue_979/issue979_test_negated_is_best/output.terser.js`** -> AI Confidence: **99.29%**
1307. **`crates/swc_ecma_minifier/tests/terser/compress/labels/labels_1/input.js`** -> AI Confidence: **99.29%**
1308. **`crates/swc_ecma_minifier/tests/terser/compress/labels/labels_1/output.js`** -> AI Confidence: **99.29%**
1309. **`crates/swc_ecma_minifier/tests/terser/compress/labels/labels_1/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1310. **`crates/swc_ecma_minifier/tests/terser/compress/labels/labels_1/output.terser.js`** -> AI Confidence: **99.29%**
1311. **`crates/swc_ecma_minifier/tests/terser/compress/labels/labels_10/input.js`** -> AI Confidence: **99.29%**
1312. **`crates/swc_ecma_minifier/tests/terser/compress/labels/labels_10/output.js`** -> AI Confidence: **99.29%**
1313. **`crates/swc_ecma_minifier/tests/terser/compress/labels/labels_10/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1314. **`crates/swc_ecma_minifier/tests/terser/compress/labels/labels_10/output.terser.js`** -> AI Confidence: **99.29%**
1315. **`crates/swc_ecma_minifier/tests/terser/compress/labels/labels_2/input.js`** -> AI Confidence: **99.29%**
1316. **`crates/swc_ecma_minifier/tests/terser/compress/labels/labels_2/output.js`** -> AI Confidence: **99.29%**
1317. **`crates/swc_ecma_minifier/tests/terser/compress/labels/labels_2/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1318. **`crates/swc_ecma_minifier/tests/terser/compress/labels/labels_2/output.terser.js`** -> AI Confidence: **99.29%**
1319. **`crates/swc_ecma_minifier/tests/terser/compress/labels/labels_5/input.js`** -> AI Confidence: **99.29%**
1320. **`crates/swc_ecma_minifier/tests/terser/compress/labels/labels_5/output.js`** -> AI Confidence: **99.29%**
1321. **`crates/swc_ecma_minifier/tests/terser/compress/labels/labels_5/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1322. **`crates/swc_ecma_minifier/tests/terser/compress/labels/labels_5/output.terser.js`** -> AI Confidence: **99.29%**
1323. **`crates/swc_ecma_minifier/tests/terser/compress/labels/labels_6/input.js`** -> AI Confidence: **99.29%**
1324. **`crates/swc_ecma_minifier/tests/terser/compress/labels/labels_6/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1325. **`crates/swc_ecma_minifier/tests/terser/compress/labels/labels_7/input.js`** -> AI Confidence: **99.29%**
1326. **`crates/swc_ecma_minifier/tests/terser/compress/labels/labels_7/output.js`** -> AI Confidence: **99.29%**
1327. **`crates/swc_ecma_minifier/tests/terser/compress/labels/labels_7/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1328. **`crates/swc_ecma_minifier/tests/terser/compress/labels/labels_7/output.terser.js`** -> AI Confidence: **99.29%**
1329. **`crates/swc_ecma_minifier/tests/terser/compress/labels/labels_8/input.js`** -> AI Confidence: **99.29%**
1330. **`crates/swc_ecma_minifier/tests/terser/compress/labels/labels_8/output.js`** -> AI Confidence: **99.29%**
1331. **`crates/swc_ecma_minifier/tests/terser/compress/labels/labels_8/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1332. **`crates/swc_ecma_minifier/tests/terser/compress/labels/labels_8/output.terser.js`** -> AI Confidence: **99.29%**
1333. **`crates/swc_ecma_minifier/tests/terser/compress/labels/labels_9/input.js`** -> AI Confidence: **99.29%**
1334. **`crates/swc_ecma_minifier/tests/terser/compress/labels/labels_9/output.js`** -> AI Confidence: **99.29%**
1335. **`crates/swc_ecma_minifier/tests/terser/compress/labels/labels_9/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1336. **`crates/swc_ecma_minifier/tests/terser/compress/labels/labels_9/output.terser.js`** -> AI Confidence: **99.29%**
1337. **`crates/swc_ecma_minifier/tests/terser/compress/loops/do_switch/input.js`** -> AI Confidence: **99.29%**
1338. **`crates/swc_ecma_minifier/tests/terser/compress/loops/do_switch/output.js`** -> AI Confidence: **99.29%**
1339. **`crates/swc_ecma_minifier/tests/terser/compress/loops/do_switch/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1340. **`crates/swc_ecma_minifier/tests/terser/compress/loops/do_switch/output.terser.js`** -> AI Confidence: **99.29%**
1341. **`crates/swc_ecma_minifier/tests/terser/compress/loops/drop_if_break_1/input.js`** -> AI Confidence: **99.29%**
1342. **`crates/swc_ecma_minifier/tests/terser/compress/loops/drop_if_break_1/output.js`** -> AI Confidence: **99.29%**
1343. **`crates/swc_ecma_minifier/tests/terser/compress/loops/drop_if_break_1/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1344. **`crates/swc_ecma_minifier/tests/terser/compress/loops/drop_if_break_1/output.terser.js`** -> AI Confidence: **99.29%**
1345. **`crates/swc_ecma_minifier/tests/terser/compress/loops/drop_if_break_2/input.js`** -> AI Confidence: **99.29%**
1346. **`crates/swc_ecma_minifier/tests/terser/compress/loops/drop_if_break_2/output.js`** -> AI Confidence: **99.29%**
1347. **`crates/swc_ecma_minifier/tests/terser/compress/loops/drop_if_break_2/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1348. **`crates/swc_ecma_minifier/tests/terser/compress/loops/drop_if_break_2/output.terser.js`** -> AI Confidence: **99.29%**
1349. **`crates/swc_ecma_minifier/tests/terser/compress/loops/drop_if_break_3/input.js`** -> AI Confidence: **99.29%**
1350. **`crates/swc_ecma_minifier/tests/terser/compress/loops/drop_if_break_3/output.js`** -> AI Confidence: **99.29%**
1351. **`crates/swc_ecma_minifier/tests/terser/compress/loops/drop_if_break_3/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1352. **`crates/swc_ecma_minifier/tests/terser/compress/loops/drop_if_break_3/output.terser.js`** -> AI Confidence: **99.29%**
1353. **`crates/swc_ecma_minifier/tests/terser/compress/loops/drop_if_break_4/input.js`** -> AI Confidence: **99.29%**
1354. **`crates/swc_ecma_minifier/tests/terser/compress/loops/drop_if_break_4/output.js`** -> AI Confidence: **99.29%**
1355. **`crates/swc_ecma_minifier/tests/terser/compress/loops/drop_if_break_4/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1356. **`crates/swc_ecma_minifier/tests/terser/compress/loops/drop_if_break_4/output.terser.js`** -> AI Confidence: **99.29%**
1357. **`crates/swc_ecma_minifier/tests/terser/compress/loops/drop_if_else_break_1/input.js`** -> AI Confidence: **99.29%**
1358. **`crates/swc_ecma_minifier/tests/terser/compress/loops/drop_if_else_break_1/output.js`** -> AI Confidence: **99.29%**
1359. **`crates/swc_ecma_minifier/tests/terser/compress/loops/drop_if_else_break_1/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1360. **`crates/swc_ecma_minifier/tests/terser/compress/loops/drop_if_else_break_1/output.terser.js`** -> AI Confidence: **99.29%**
1361. **`crates/swc_ecma_minifier/tests/terser/compress/loops/drop_if_else_break_2/input.js`** -> AI Confidence: **99.29%**
1362. **`crates/swc_ecma_minifier/tests/terser/compress/loops/drop_if_else_break_2/output.js`** -> AI Confidence: **99.29%**
1363. **`crates/swc_ecma_minifier/tests/terser/compress/loops/drop_if_else_break_2/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1364. **`crates/swc_ecma_minifier/tests/terser/compress/loops/drop_if_else_break_2/output.terser.js`** -> AI Confidence: **99.29%**
1365. **`crates/swc_ecma_minifier/tests/terser/compress/loops/drop_if_else_break_3/input.js`** -> AI Confidence: **99.29%**
1366. **`crates/swc_ecma_minifier/tests/terser/compress/loops/drop_if_else_break_3/output.js`** -> AI Confidence: **99.29%**
1367. **`crates/swc_ecma_minifier/tests/terser/compress/loops/drop_if_else_break_3/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1368. **`crates/swc_ecma_minifier/tests/terser/compress/loops/drop_if_else_break_3/output.terser.js`** -> AI Confidence: **99.29%**
1369. **`crates/swc_ecma_minifier/tests/terser/compress/loops/drop_if_else_break_4/input.js`** -> AI Confidence: **99.29%**
1370. **`crates/swc_ecma_minifier/tests/terser/compress/loops/drop_if_else_break_4/output.js`** -> AI Confidence: **99.29%**
1371. **`crates/swc_ecma_minifier/tests/terser/compress/loops/drop_if_else_break_4/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1372. **`crates/swc_ecma_minifier/tests/terser/compress/loops/drop_if_else_break_4/output.terser.js`** -> AI Confidence: **99.29%**
1373. **`crates/swc_ecma_minifier/tests/terser/compress/loops/evaluate/input.js`** -> AI Confidence: **99.29%**
1374. **`crates/swc_ecma_minifier/tests/terser/compress/loops/evaluate/output.js`** -> AI Confidence: **99.29%**
1375. **`crates/swc_ecma_minifier/tests/terser/compress/loops/evaluate/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1376. **`crates/swc_ecma_minifier/tests/terser/compress/loops/evaluate/output.terser.js`** -> AI Confidence: **99.29%**
1377. **`crates/swc_ecma_minifier/tests/terser/compress/loops/in_parenthesis_1/input.js`** -> AI Confidence: **99.29%**
1378. **`crates/swc_ecma_minifier/tests/terser/compress/loops/in_parenthesis_1/output.js`** -> AI Confidence: **99.29%**
1379. **`crates/swc_ecma_minifier/tests/terser/compress/loops/in_parenthesis_1/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1380. **`crates/swc_ecma_minifier/tests/terser/compress/loops/in_parenthesis_1/output.terser.js`** -> AI Confidence: **99.29%**
1381. **`crates/swc_ecma_minifier/tests/terser/compress/loops/in_parenthesis_2/input.js`** -> AI Confidence: **99.29%**
1382. **`crates/swc_ecma_minifier/tests/terser/compress/loops/in_parenthesis_2/output.js`** -> AI Confidence: **99.29%**
1383. **`crates/swc_ecma_minifier/tests/terser/compress/loops/in_parenthesis_2/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1384. **`crates/swc_ecma_minifier/tests/terser/compress/loops/in_parenthesis_2/output.terser.js`** -> AI Confidence: **99.29%**
1385. **`crates/swc_ecma_minifier/tests/terser/compress/loops/init_side_effects/input.js`** -> AI Confidence: **99.29%**
1386. **`crates/swc_ecma_minifier/tests/terser/compress/loops/init_side_effects/output.js`** -> AI Confidence: **99.29%**
1387. **`crates/swc_ecma_minifier/tests/terser/compress/loops/init_side_effects/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1388. **`crates/swc_ecma_minifier/tests/terser/compress/loops/init_side_effects/output.terser.js`** -> AI Confidence: **99.29%**
1389. **`crates/swc_ecma_minifier/tests/terser/compress/loops/issue_1532/input.js`** -> AI Confidence: **99.29%**
1390. **`crates/swc_ecma_minifier/tests/terser/compress/loops/issue_1532/output.js`** -> AI Confidence: **99.29%**
1391. **`crates/swc_ecma_minifier/tests/terser/compress/loops/issue_1532/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1392. **`crates/swc_ecma_minifier/tests/terser/compress/loops/issue_1532/output.terser.js`** -> AI Confidence: **99.29%**
1393. **`crates/swc_ecma_minifier/tests/terser/compress/loops/issue_1648/output.js`** -> AI Confidence: **99.29%**
1394. **`crates/swc_ecma_minifier/tests/terser/compress/loops/issue_1648/output.terser.js`** -> AI Confidence: **99.29%**
1395. **`crates/swc_ecma_minifier/tests/terser/compress/loops/issue_186/input.js`** -> AI Confidence: **99.29%**
1396. **`crates/swc_ecma_minifier/tests/terser/compress/loops/issue_186/output.js`** -> AI Confidence: **99.29%**
1397. **`crates/swc_ecma_minifier/tests/terser/compress/loops/issue_186/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1398. **`crates/swc_ecma_minifier/tests/terser/compress/loops/issue_186/output.terser.js`** -> AI Confidence: **99.29%**
1399. **`crates/swc_ecma_minifier/tests/terser/compress/loops/issue_186_beautify/input.js`** -> AI Confidence: **99.29%**
1400. **`crates/swc_ecma_minifier/tests/terser/compress/loops/issue_186_beautify/output.js`** -> AI Confidence: **99.29%**
1401. **`crates/swc_ecma_minifier/tests/terser/compress/loops/issue_186_beautify/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1402. **`crates/swc_ecma_minifier/tests/terser/compress/loops/issue_186_beautify/output.terser.js`** -> AI Confidence: **99.29%**
1403. **`crates/swc_ecma_minifier/tests/terser/compress/loops/issue_186_beautify_braces/input.js`** -> AI Confidence: **99.29%**
1404. **`crates/swc_ecma_minifier/tests/terser/compress/loops/issue_186_beautify_braces/output.js`** -> AI Confidence: **99.29%**
1405. **`crates/swc_ecma_minifier/tests/terser/compress/loops/issue_186_beautify_braces/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1406. **`crates/swc_ecma_minifier/tests/terser/compress/loops/issue_186_beautify_braces/output.terser.js`** -> AI Confidence: **99.29%**
1407. **`crates/swc_ecma_minifier/tests/terser/compress/loops/issue_186_beautify_braces_ie8/input.js`** -> AI Confidence: **99.29%**
1408. **`crates/swc_ecma_minifier/tests/terser/compress/loops/issue_186_beautify_braces_ie8/output.js`** -> AI Confidence: **99.29%**
1409. **`crates/swc_ecma_minifier/tests/terser/compress/loops/issue_186_beautify_braces_ie8/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1410. **`crates/swc_ecma_minifier/tests/terser/compress/loops/issue_186_beautify_braces_ie8/output.terser.js`** -> AI Confidence: **99.29%**
1411. **`crates/swc_ecma_minifier/tests/terser/compress/loops/issue_186_beautify_ie8/input.js`** -> AI Confidence: **99.29%**
1412. **`crates/swc_ecma_minifier/tests/terser/compress/loops/issue_186_beautify_ie8/output.js`** -> AI Confidence: **99.29%**
1413. **`crates/swc_ecma_minifier/tests/terser/compress/loops/issue_186_beautify_ie8/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1414. **`crates/swc_ecma_minifier/tests/terser/compress/loops/issue_186_beautify_ie8/output.terser.js`** -> AI Confidence: **99.29%**
1415. **`crates/swc_ecma_minifier/tests/terser/compress/loops/issue_186_braces/input.js`** -> AI Confidence: **99.29%**
1416. **`crates/swc_ecma_minifier/tests/terser/compress/loops/issue_186_braces/output.js`** -> AI Confidence: **99.29%**
1417. **`crates/swc_ecma_minifier/tests/terser/compress/loops/issue_186_braces/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1418. **`crates/swc_ecma_minifier/tests/terser/compress/loops/issue_186_braces/output.terser.js`** -> AI Confidence: **99.29%**
1419. **`crates/swc_ecma_minifier/tests/terser/compress/loops/issue_186_braces_ie8/input.js`** -> AI Confidence: **99.29%**
1420. **`crates/swc_ecma_minifier/tests/terser/compress/loops/issue_186_braces_ie8/output.js`** -> AI Confidence: **99.29%**
1421. **`crates/swc_ecma_minifier/tests/terser/compress/loops/issue_186_braces_ie8/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1422. **`crates/swc_ecma_minifier/tests/terser/compress/loops/issue_186_braces_ie8/output.terser.js`** -> AI Confidence: **99.29%**
1423. **`crates/swc_ecma_minifier/tests/terser/compress/loops/issue_186_ie8/input.js`** -> AI Confidence: **99.29%**
1424. **`crates/swc_ecma_minifier/tests/terser/compress/loops/issue_186_ie8/output.js`** -> AI Confidence: **99.29%**
1425. **`crates/swc_ecma_minifier/tests/terser/compress/loops/issue_186_ie8/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1426. **`crates/swc_ecma_minifier/tests/terser/compress/loops/issue_186_ie8/output.terser.js`** -> AI Confidence: **99.29%**
1427. **`crates/swc_ecma_minifier/tests/terser/compress/loops/issue_2740_1/input.js`** -> AI Confidence: **99.29%**
1428. **`crates/swc_ecma_minifier/tests/terser/compress/loops/issue_2740_1/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1429. **`crates/swc_ecma_minifier/tests/terser/compress/loops/issue_2740_2/input.js`** -> AI Confidence: **99.29%**
1430. **`crates/swc_ecma_minifier/tests/terser/compress/loops/issue_2740_2/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1431. **`crates/swc_ecma_minifier/tests/terser/compress/loops/issue_2740_6/input.js`** -> AI Confidence: **99.29%**
1432. **`crates/swc_ecma_minifier/tests/terser/compress/loops/issue_2740_6/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1433. **`crates/swc_ecma_minifier/tests/terser/compress/loops/parse_do_while_with_semicolon/input.js`** -> AI Confidence: **99.29%**
1434. **`crates/swc_ecma_minifier/tests/terser/compress/loops/parse_do_while_with_semicolon/output.js`** -> AI Confidence: **99.29%**
1435. **`crates/swc_ecma_minifier/tests/terser/compress/loops/parse_do_while_with_semicolon/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1436. **`crates/swc_ecma_minifier/tests/terser/compress/loops/parse_do_while_with_semicolon/output.terser.js`** -> AI Confidence: **99.29%**
1437. **`crates/swc_ecma_minifier/tests/terser/compress/loops/parse_do_while_without_semicolon/input.js`** -> AI Confidence: **99.29%**
1438. **`crates/swc_ecma_minifier/tests/terser/compress/loops/parse_do_while_without_semicolon/output.js`** -> AI Confidence: **99.29%**
1439. **`crates/swc_ecma_minifier/tests/terser/compress/loops/parse_do_while_without_semicolon/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1440. **`crates/swc_ecma_minifier/tests/terser/compress/loops/parse_do_while_without_semicolon/output.terser.js`** -> AI Confidence: **99.29%**
1441. **`crates/swc_ecma_minifier/tests/terser/compress/loops/while_becomes_for/input.js`** -> AI Confidence: **99.29%**
1442. **`crates/swc_ecma_minifier/tests/terser/compress/loops/while_becomes_for/output.js`** -> AI Confidence: **99.29%**
1443. **`crates/swc_ecma_minifier/tests/terser/compress/loops/while_becomes_for/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1444. **`crates/swc_ecma_minifier/tests/terser/compress/loops/while_becomes_for/output.terser.js`** -> AI Confidence: **99.29%**
1445. **`crates/swc_ecma_minifier/tests/terser/compress/negate_iife/issue_1288/input.js`** -> AI Confidence: **99.29%**
1446. **`crates/swc_ecma_minifier/tests/terser/compress/negate_iife/issue_1288/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1447. **`crates/swc_ecma_minifier/tests/terser/compress/negate_iife/issue_1288_side_effects/input.js`** -> AI Confidence: **99.29%**
1448. **`crates/swc_ecma_minifier/tests/terser/compress/negate_iife/issue_1288_side_effects/output.js`** -> AI Confidence: **99.29%**
1449. **`crates/swc_ecma_minifier/tests/terser/compress/negate_iife/issue_1288_side_effects/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1450. **`crates/swc_ecma_minifier/tests/terser/compress/negate_iife/issue_1288_side_effects/output.terser.js`** -> AI Confidence: **99.29%**
1451. **`crates/swc_ecma_minifier/tests/terser/compress/nullish/conditional_to_nullish_coalescing/input.js`** -> AI Confidence: **99.29%**
1452. **`crates/swc_ecma_minifier/tests/terser/compress/nullish/conditional_to_nullish_coalescing/output.js`** -> AI Confidence: **99.29%**
1453. **`crates/swc_ecma_minifier/tests/terser/compress/nullish/conditional_to_nullish_coalescing/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1454. **`crates/swc_ecma_minifier/tests/terser/compress/nullish/conditional_to_nullish_coalescing/output.terser.js`** -> AI Confidence: **99.29%**
1455. **`crates/swc_ecma_minifier/tests/terser/compress/nullish/conditional_to_nullish_coalescing_2/input.js`** -> AI Confidence: **99.29%**
1456. **`crates/swc_ecma_minifier/tests/terser/compress/nullish/conditional_to_nullish_coalescing_2/output.js`** -> AI Confidence: **99.29%**
1457. **`crates/swc_ecma_minifier/tests/terser/compress/nullish/conditional_to_nullish_coalescing_2/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1458. **`crates/swc_ecma_minifier/tests/terser/compress/nullish/conditional_to_nullish_coalescing_2/output.terser.js`** -> AI Confidence: **99.29%**
1459. **`crates/swc_ecma_minifier/tests/terser/compress/nullish/nullish_coalescing_boolean_context/input.js`** -> AI Confidence: **99.29%**
1460. **`crates/swc_ecma_minifier/tests/terser/compress/nullish/nullish_coalescing_boolean_context/output.js`** -> AI Confidence: **99.29%**
1461. **`crates/swc_ecma_minifier/tests/terser/compress/nullish/nullish_coalescing_boolean_context/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1462. **`crates/swc_ecma_minifier/tests/terser/compress/nullish/nullish_coalescing_boolean_context/output.terser.js`** -> AI Confidence: **99.29%**
1463. **`crates/swc_ecma_minifier/tests/terser/compress/nullish/nullish_coalescing_mandatory_parens/input.js`** -> AI Confidence: **99.29%**
1464. **`crates/swc_ecma_minifier/tests/terser/compress/nullish/nullish_coalescing_mandatory_parens/output.js`** -> AI Confidence: **99.29%**
1465. **`crates/swc_ecma_minifier/tests/terser/compress/nullish/nullish_coalescing_mandatory_parens/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1466. **`crates/swc_ecma_minifier/tests/terser/compress/nullish/nullish_coalescing_mandatory_parens/output.terser.js`** -> AI Confidence: **99.29%**
1467. **`crates/swc_ecma_minifier/tests/terser/compress/nullish/nullish_coalescing_parens/input.js`** -> AI Confidence: **99.29%**
1468. **`crates/swc_ecma_minifier/tests/terser/compress/nullish/nullish_coalescing_parens/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1469. **`crates/swc_ecma_minifier/tests/terser/compress/nullish/simplify_nullish_coalescing/input.js`** -> AI Confidence: **99.29%**
1470. **`crates/swc_ecma_minifier/tests/terser/compress/nullish/simplify_nullish_coalescing/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1471. **`crates/swc_ecma_minifier/tests/terser/compress/object/concise_methods_and_keyword_names/input.js`** -> AI Confidence: **99.29%**
1472. **`crates/swc_ecma_minifier/tests/terser/compress/object/concise_methods_and_keyword_names/output.js`** -> AI Confidence: **99.29%**
1473. **`crates/swc_ecma_minifier/tests/terser/compress/object/concise_methods_and_keyword_names/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1474. **`crates/swc_ecma_minifier/tests/terser/compress/object/concise_methods_and_keyword_names/output.terser.js`** -> AI Confidence: **99.29%**
1475. **`crates/swc_ecma_minifier/tests/terser/compress/properties/dot_properties/input.js`** -> AI Confidence: **99.29%**
1476. **`crates/swc_ecma_minifier/tests/terser/compress/properties/dot_properties/output.js`** -> AI Confidence: **99.29%**
1477. **`crates/swc_ecma_minifier/tests/terser/compress/properties/dot_properties/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1478. **`crates/swc_ecma_minifier/tests/terser/compress/properties/dot_properties/output.terser.js`** -> AI Confidence: **99.29%**
1479. **`crates/swc_ecma_minifier/tests/terser/compress/properties/dot_properties_es5/input.js`** -> AI Confidence: **99.29%**
1480. **`crates/swc_ecma_minifier/tests/terser/compress/properties/dot_properties_es5/output.js`** -> AI Confidence: **99.29%**
1481. **`crates/swc_ecma_minifier/tests/terser/compress/properties/dot_properties_es5/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1482. **`crates/swc_ecma_minifier/tests/terser/compress/properties/dot_properties_es5/output.terser.js`** -> AI Confidence: **99.29%**
1483. **`crates/swc_ecma_minifier/tests/terser/compress/properties/literal_duplicate_key_side_effects/input.js`** -> AI Confidence: **99.29%**
1484. **`crates/swc_ecma_minifier/tests/terser/compress/properties/literal_duplicate_key_side_effects/output.js`** -> AI Confidence: **99.29%**
1485. **`crates/swc_ecma_minifier/tests/terser/compress/properties/literal_duplicate_key_side_effects/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1486. **`crates/swc_ecma_minifier/tests/terser/compress/properties/literal_duplicate_key_side_effects/output.terser.js`** -> AI Confidence: **99.29%**
1487. **`crates/swc_ecma_minifier/tests/terser/compress/properties/sub_properties/output.js`** -> AI Confidence: **99.29%**
1488. **`crates/swc_ecma_minifier/tests/terser/compress/properties/sub_properties/output.terser.js`** -> AI Confidence: **99.29%**
1489. **`crates/swc_ecma_minifier/tests/terser/compress/pure_funcs/boolean_and/input.js`** -> AI Confidence: **99.29%**
1490. **`crates/swc_ecma_minifier/tests/terser/compress/pure_funcs/boolean_and/output.js`** -> AI Confidence: **99.29%**
1491. **`crates/swc_ecma_minifier/tests/terser/compress/pure_funcs/boolean_and/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1492. **`crates/swc_ecma_minifier/tests/terser/compress/pure_funcs/boolean_and/output.terser.js`** -> AI Confidence: **99.29%**
1493. **`crates/swc_ecma_minifier/tests/terser/compress/pure_funcs/boolean_or/input.js`** -> AI Confidence: **99.29%**
1494. **`crates/swc_ecma_minifier/tests/terser/compress/pure_funcs/boolean_or/output.js`** -> AI Confidence: **99.29%**
1495. **`crates/swc_ecma_minifier/tests/terser/compress/pure_funcs/boolean_or/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1496. **`crates/swc_ecma_minifier/tests/terser/compress/pure_funcs/boolean_or/output.terser.js`** -> AI Confidence: **99.29%**
1497. **`crates/swc_ecma_minifier/tests/terser/compress/pure_funcs/conditional/input.js`** -> AI Confidence: **99.29%**
1498. **`crates/swc_ecma_minifier/tests/terser/compress/pure_funcs/conditional/output.js`** -> AI Confidence: **99.29%**
1499. **`crates/swc_ecma_minifier/tests/terser/compress/pure_funcs/conditional/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1500. **`crates/swc_ecma_minifier/tests/terser/compress/pure_funcs/conditional/output.terser.js`** -> AI Confidence: **99.29%**
1501. **`crates/swc_ecma_minifier/tests/terser/compress/pure_funcs/issue_2638/input.js`** -> AI Confidence: **99.29%**
1502. **`crates/swc_ecma_minifier/tests/terser/compress/pure_funcs/issue_2638/output.js`** -> AI Confidence: **99.29%**
1503. **`crates/swc_ecma_minifier/tests/terser/compress/pure_funcs/issue_2638/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1504. **`crates/swc_ecma_minifier/tests/terser/compress/pure_funcs/issue_2638/output.terser.js`** -> AI Confidence: **99.29%**
1505. **`crates/swc_ecma_minifier/tests/terser/compress/pure_funcs/issue_2705_6/input.js`** -> AI Confidence: **99.29%**
1506. **`crates/swc_ecma_minifier/tests/terser/compress/pure_funcs/issue_2705_6/output.js`** -> AI Confidence: **99.29%**
1507. **`crates/swc_ecma_minifier/tests/terser/compress/pure_funcs/issue_2705_6/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1508. **`crates/swc_ecma_minifier/tests/terser/compress/pure_funcs/issue_2705_6/output.terser.js`** -> AI Confidence: **99.29%**
1509. **`crates/swc_ecma_minifier/tests/terser/compress/pure_funcs/issue_526_1/input.js`** -> AI Confidence: **99.29%**
1510. **`crates/swc_ecma_minifier/tests/terser/compress/pure_funcs/issue_526_1/output.js`** -> AI Confidence: **99.29%**
1511. **`crates/swc_ecma_minifier/tests/terser/compress/pure_funcs/issue_526_1/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1512. **`crates/swc_ecma_minifier/tests/terser/compress/pure_funcs/issue_526_1/output.terser.js`** -> AI Confidence: **99.29%**
1513. **`crates/swc_ecma_minifier/tests/terser/compress/pure_getters/collapse_rhs_setter/input.js`** -> AI Confidence: **99.29%**
1514. **`crates/swc_ecma_minifier/tests/terser/compress/pure_getters/collapse_rhs_setter/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1515. **`crates/swc_ecma_minifier/tests/terser/compress/pure_getters/collapse_vars_1_true/output.js`** -> AI Confidence: **99.29%**
1516. **`crates/swc_ecma_minifier/tests/terser/compress/pure_getters/collapse_vars_1_true/output.terser.js`** -> AI Confidence: **99.29%**
1517. **`crates/swc_ecma_minifier/tests/terser/compress/pure_getters/set_immutable_1/output.js`** -> AI Confidence: **99.29%**
1518. **`crates/swc_ecma_minifier/tests/terser/compress/pure_getters/set_immutable_1/output.terser.js`** -> AI Confidence: **99.29%**
1519. **`crates/swc_ecma_minifier/tests/terser/compress/pure_getters/set_immutable_2/output.js`** -> AI Confidence: **99.29%**
1520. **`crates/swc_ecma_minifier/tests/terser/compress/pure_getters/set_immutable_3/output.js`** -> AI Confidence: **99.29%**
1521. **`crates/swc_ecma_minifier/tests/terser/compress/pure_getters/set_immutable_3/output.terser.js`** -> AI Confidence: **99.29%**
1522. **`crates/swc_ecma_minifier/tests/terser/compress/pure_getters/set_immutable_4/output.js`** -> AI Confidence: **99.29%**
1523. **`crates/swc_ecma_minifier/tests/terser/compress/pure_getters/set_immutable_5/output.js`** -> AI Confidence: **99.29%**
1524. **`crates/swc_ecma_minifier/tests/terser/compress/pure_getters/set_immutable_5/output.terser.js`** -> AI Confidence: **99.29%**
1525. **`crates/swc_ecma_minifier/tests/terser/compress/pure_getters/set_immutable_6/output.js`** -> AI Confidence: **99.29%**
1526. **`crates/swc_ecma_minifier/tests/terser/compress/pure_getters/set_immutable_6/output.terser.js`** -> AI Confidence: **99.29%**
1527. **`crates/swc_ecma_minifier/tests/terser/compress/pure_getters/set_mutable_1/input.js`** -> AI Confidence: **99.29%**
1528. **`crates/swc_ecma_minifier/tests/terser/compress/pure_getters/set_mutable_1/output.js`** -> AI Confidence: **99.29%**
1529. **`crates/swc_ecma_minifier/tests/terser/compress/pure_getters/set_mutable_1/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1530. **`crates/swc_ecma_minifier/tests/terser/compress/pure_getters/set_mutable_1/output.terser.js`** -> AI Confidence: **99.29%**
1531. **`crates/swc_ecma_minifier/tests/terser/compress/pure_getters/set_mutable_2/input.js`** -> AI Confidence: **99.29%**
1532. **`crates/swc_ecma_minifier/tests/terser/compress/pure_getters/set_mutable_2/output.js`** -> AI Confidence: **99.29%**
1533. **`crates/swc_ecma_minifier/tests/terser/compress/pure_getters/set_mutable_2/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1534. **`crates/swc_ecma_minifier/tests/terser/compress/pure_getters/set_mutable_2/output.terser.js`** -> AI Confidence: **99.29%**
1535. **`crates/swc_ecma_minifier/tests/terser/compress/pure_globals/globals_whose_access_is_pure/input.js`** -> AI Confidence: **99.29%**
1536. **`crates/swc_ecma_minifier/tests/terser/compress/pure_globals/globals_whose_access_is_pure/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1537. **`crates/swc_ecma_minifier/tests/terser/compress/pure_globals/window_access_is_impure/input.js`** -> AI Confidence: **99.29%**
1538. **`crates/swc_ecma_minifier/tests/terser/compress/pure_globals/window_access_is_impure/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1539. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/conditional_nested_1/input.js`** -> AI Confidence: **99.29%**
1540. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/conditional_nested_1/output.js`** -> AI Confidence: **99.29%**
1541. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/conditional_nested_1/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1542. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/conditional_nested_1/output.terser.js`** -> AI Confidence: **99.29%**
1543. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/defun_catch_1/input.js`** -> AI Confidence: **99.29%**
1544. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/defun_catch_1/output.js`** -> AI Confidence: **99.29%**
1545. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/defun_catch_1/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1546. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/defun_catch_1/output.terser.js`** -> AI Confidence: **99.29%**
1547. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/defun_catch_2/input.js`** -> AI Confidence: **99.29%**
1548. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/defun_catch_2/output.js`** -> AI Confidence: **99.29%**
1549. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/defun_catch_2/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1550. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/defun_catch_2/output.terser.js`** -> AI Confidence: **99.29%**
1551. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/defun_catch_3/input.js`** -> AI Confidence: **99.29%**
1552. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/defun_catch_3/output.js`** -> AI Confidence: **99.29%**
1553. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/defun_catch_3/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1554. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/defun_catch_3/output.terser.js`** -> AI Confidence: **99.29%**
1555. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/defun_catch_4/input.js`** -> AI Confidence: **99.29%**
1556. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/defun_catch_4/output.js`** -> AI Confidence: **99.29%**
1557. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/defun_catch_4/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1558. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/defun_catch_4/output.terser.js`** -> AI Confidence: **99.29%**
1559. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/defun_catch_5/input.js`** -> AI Confidence: **99.29%**
1560. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/defun_catch_5/output.js`** -> AI Confidence: **99.29%**
1561. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/defun_catch_5/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1562. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/defun_catch_5/output.terser.js`** -> AI Confidence: **99.29%**
1563. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/defun_catch_6/input.js`** -> AI Confidence: **99.29%**
1564. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/defun_catch_6/output.js`** -> AI Confidence: **99.29%**
1565. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/defun_catch_6/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1566. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/defun_catch_6/output.terser.js`** -> AI Confidence: **99.29%**
1567. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/issue_1595_4/input.js`** -> AI Confidence: **99.29%**
1568. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/issue_1595_4/output.js`** -> AI Confidence: **99.29%**
1569. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/issue_1595_4/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1570. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/issue_1595_4/output.terser.js`** -> AI Confidence: **99.29%**
1571. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/issue_1670_1/input.js`** -> AI Confidence: **99.29%**
1572. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/issue_1670_1/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1573. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/issue_1670_2/input.js`** -> AI Confidence: **99.29%**
1574. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/issue_1670_2/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1575. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/issue_1670_3/input.js`** -> AI Confidence: **99.29%**
1576. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/issue_1670_3/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1577. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/issue_1670_4/input.js`** -> AI Confidence: **99.29%**
1578. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/issue_1670_4/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1579. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/issue_1670_5/input.js`** -> AI Confidence: **99.29%**
1580. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/issue_1670_5/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1581. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/issue_1670_6/input.js`** -> AI Confidence: **99.29%**
1582. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/issue_1670_6/output.js`** -> AI Confidence: **99.29%**
1583. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/issue_1670_6/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1584. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/issue_1670_6/output.terser.js`** -> AI Confidence: **99.29%**
1585. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/issue_2420_2/output.js`** -> AI Confidence: **99.29%**
1586. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/issue_2420_2/output.terser.js`** -> AI Confidence: **99.29%**
1587. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/issue_2455/output.js`** -> AI Confidence: **99.29%**
1588. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/issue_2455/output.terser.js`** -> AI Confidence: **99.29%**
1589. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/issue_2992/input.js`** -> AI Confidence: **99.29%**
1590. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/issue_2992/output.js`** -> AI Confidence: **99.29%**
1591. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/issue_2992/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1592. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/issue_2992/output.terser.js`** -> AI Confidence: **99.29%**
1593. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/issue_3068_1/input.js`** -> AI Confidence: **99.29%**
1594. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/issue_3068_1/output.js`** -> AI Confidence: **99.29%**
1595. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/issue_3068_1/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1596. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/issue_3068_1/output.terser.js`** -> AI Confidence: **99.29%**
1597. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/issue_3068_2/input.js`** -> AI Confidence: **99.29%**
1598. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/issue_3068_2/output.js`** -> AI Confidence: **99.29%**
1599. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/issue_3068_2/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1600. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/issue_3068_2/output.terser.js`** -> AI Confidence: **99.29%**
1601. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/issue_308/output.js`** -> AI Confidence: **99.29%**
1602. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/issue_308/output.terser.js`** -> AI Confidence: **99.29%**
1603. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/recursive_inlining_3/input.js`** -> AI Confidence: **99.29%**
1604. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/recursive_inlining_3/output.js`** -> AI Confidence: **99.29%**
1605. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/recursive_inlining_3/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1606. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/recursive_inlining_3/output.terser.js`** -> AI Confidence: **99.29%**
1607. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/recursive_inlining_4/input.js`** -> AI Confidence: **99.29%**
1608. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/recursive_inlining_4/output.js`** -> AI Confidence: **99.29%**
1609. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/recursive_inlining_4/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1610. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/recursive_inlining_4/output.terser.js`** -> AI Confidence: **99.29%**
1611. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/recursive_inlining_5/input.js`** -> AI Confidence: **99.29%**
1612. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/recursive_inlining_5/output.js`** -> AI Confidence: **99.29%**
1613. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/recursive_inlining_5/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1614. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/recursive_inlining_5/output.terser.js`** -> AI Confidence: **99.29%**
1615. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/toplevel_on_loops_2/output.js`** -> AI Confidence: **99.29%**
1616. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/toplevel_on_loops_2/output.terser.js`** -> AI Confidence: **99.29%**
1617. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/toplevel_on_loops_3/output.js`** -> AI Confidence: **99.29%**
1618. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/toplevel_on_loops_3/output.terser.js`** -> AI Confidence: **99.29%**
1619. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/var_assign_2/output.terser.js`** -> AI Confidence: **99.29%**
1620. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/var_assign_3/output.js`** -> AI Confidence: **99.29%**
1621. **`crates/swc_ecma_minifier/tests/terser/compress/regexp/regexp_1/input.js`** -> AI Confidence: **99.29%**
1622. **`crates/swc_ecma_minifier/tests/terser/compress/regexp/regexp_1/output.js`** -> AI Confidence: **99.29%**
1623. **`crates/swc_ecma_minifier/tests/terser/compress/regexp/regexp_1/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1624. **`crates/swc_ecma_minifier/tests/terser/compress/regexp/regexp_1/output.terser.js`** -> AI Confidence: **99.29%**
1625. **`crates/swc_ecma_minifier/tests/terser/compress/regexp/regexp_2/input.js`** -> AI Confidence: **99.29%**
1626. **`crates/swc_ecma_minifier/tests/terser/compress/regexp/regexp_2/output.js`** -> AI Confidence: **99.29%**
1627. **`crates/swc_ecma_minifier/tests/terser/compress/regexp/regexp_2/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1628. **`crates/swc_ecma_minifier/tests/terser/compress/regexp/regexp_2/output.terser.js`** -> AI Confidence: **99.29%**
1629. **`crates/swc_ecma_minifier/tests/terser/compress/rename/issue_2120_1/input.js`** -> AI Confidence: **99.29%**
1630. **`crates/swc_ecma_minifier/tests/terser/compress/rename/issue_2120_1/output.js`** -> AI Confidence: **99.29%**
1631. **`crates/swc_ecma_minifier/tests/terser/compress/rename/issue_2120_1/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1632. **`crates/swc_ecma_minifier/tests/terser/compress/rename/issue_2120_1/output.terser.js`** -> AI Confidence: **99.29%**
1633. **`crates/swc_ecma_minifier/tests/terser/compress/rename/issue_2120_2/input.js`** -> AI Confidence: **99.29%**
1634. **`crates/swc_ecma_minifier/tests/terser/compress/rename/issue_2120_2/output.js`** -> AI Confidence: **99.29%**
1635. **`crates/swc_ecma_minifier/tests/terser/compress/rename/issue_2120_2/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1636. **`crates/swc_ecma_minifier/tests/terser/compress/rename/issue_2120_2/output.terser.js`** -> AI Confidence: **99.29%**
1637. **`crates/swc_ecma_minifier/tests/terser/compress/sequences/for_sequences/input.js`** -> AI Confidence: **99.29%**
1638. **`crates/swc_ecma_minifier/tests/terser/compress/sequences/for_sequences/output.js`** -> AI Confidence: **99.29%**
1639. **`crates/swc_ecma_minifier/tests/terser/compress/sequences/for_sequences/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1640. **`crates/swc_ecma_minifier/tests/terser/compress/sequences/for_sequences/output.terser.js`** -> AI Confidence: **99.29%**
1641. **`crates/swc_ecma_minifier/tests/terser/compress/sequences/make_sequences_2/input.js`** -> AI Confidence: **99.29%**
1642. **`crates/swc_ecma_minifier/tests/terser/compress/sequences/make_sequences_2/output.js`** -> AI Confidence: **99.29%**
1643. **`crates/swc_ecma_minifier/tests/terser/compress/sequences/make_sequences_2/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1644. **`crates/swc_ecma_minifier/tests/terser/compress/sequences/make_sequences_2/output.terser.js`** -> AI Confidence: **99.29%**
1645. **`crates/swc_ecma_minifier/tests/terser/compress/sequences/make_sequences_4/input.js`** -> AI Confidence: **99.29%**
1646. **`crates/swc_ecma_minifier/tests/terser/compress/sequences/make_sequences_4/output.js`** -> AI Confidence: **99.29%**
1647. **`crates/swc_ecma_minifier/tests/terser/compress/sequences/make_sequences_4/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1648. **`crates/swc_ecma_minifier/tests/terser/compress/sequences/make_sequences_4/output.terser.js`** -> AI Confidence: **99.29%**
1649. **`crates/swc_ecma_minifier/tests/terser/compress/sequences/negate_iife_for/input.js`** -> AI Confidence: **99.29%**
1650. **`crates/swc_ecma_minifier/tests/terser/compress/sequences/negate_iife_for/output.js`** -> AI Confidence: **99.29%**
1651. **`crates/swc_ecma_minifier/tests/terser/compress/sequences/negate_iife_for/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1652. **`crates/swc_ecma_minifier/tests/terser/compress/sequences/negate_iife_for/output.terser.js`** -> AI Confidence: **99.29%**
1653. **`crates/swc_ecma_minifier/tests/terser/compress/sequences/side_effects_cascade_1/input.js`** -> AI Confidence: **99.29%**
1654. **`crates/swc_ecma_minifier/tests/terser/compress/sequences/side_effects_cascade_1/output.js`** -> AI Confidence: **99.29%**
1655. **`crates/swc_ecma_minifier/tests/terser/compress/sequences/side_effects_cascade_1/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1656. **`crates/swc_ecma_minifier/tests/terser/compress/sequences/side_effects_cascade_1/output.terser.js`** -> AI Confidence: **99.29%**
1657. **`crates/swc_ecma_minifier/tests/terser/compress/sequences/side_effects_cascade_2/input.js`** -> AI Confidence: **99.29%**
1658. **`crates/swc_ecma_minifier/tests/terser/compress/sequences/side_effects_cascade_2/output.js`** -> AI Confidence: **99.29%**
1659. **`crates/swc_ecma_minifier/tests/terser/compress/sequences/side_effects_cascade_2/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1660. **`crates/swc_ecma_minifier/tests/terser/compress/sequences/side_effects_cascade_2/output.terser.js`** -> AI Confidence: **99.29%**
1661. **`crates/swc_ecma_minifier/tests/terser/compress/sequences/side_effects_cascade_3/input.js`** -> AI Confidence: **99.29%**
1662. **`crates/swc_ecma_minifier/tests/terser/compress/sequences/side_effects_cascade_3/output.js`** -> AI Confidence: **99.29%**
1663. **`crates/swc_ecma_minifier/tests/terser/compress/sequences/side_effects_cascade_3/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1664. **`crates/swc_ecma_minifier/tests/terser/compress/sequences/side_effects_cascade_3/output.terser.js`** -> AI Confidence: **99.29%**
1665. **`crates/swc_ecma_minifier/tests/terser/compress/switch/beautify/input.js`** -> AI Confidence: **99.29%**
1666. **`crates/swc_ecma_minifier/tests/terser/compress/switch/beautify/output.js`** -> AI Confidence: **99.29%**
1667. **`crates/swc_ecma_minifier/tests/terser/compress/switch/beautify/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1668. **`crates/swc_ecma_minifier/tests/terser/compress/switch/beautify/output.terser.js`** -> AI Confidence: **99.29%**
1669. **`crates/swc_ecma_minifier/tests/terser/compress/switch/constant_switch_1/input.js`** -> AI Confidence: **99.29%**
1670. **`crates/swc_ecma_minifier/tests/terser/compress/switch/constant_switch_1/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1671. **`crates/swc_ecma_minifier/tests/terser/compress/switch/constant_switch_2/input.js`** -> AI Confidence: **99.29%**
1672. **`crates/swc_ecma_minifier/tests/terser/compress/switch/constant_switch_2/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1673. **`crates/swc_ecma_minifier/tests/terser/compress/switch/constant_switch_3/input.js`** -> AI Confidence: **99.29%**
1674. **`crates/swc_ecma_minifier/tests/terser/compress/switch/constant_switch_3/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1675. **`crates/swc_ecma_minifier/tests/terser/compress/switch/constant_switch_4/input.js`** -> AI Confidence: **99.29%**
1676. **`crates/swc_ecma_minifier/tests/terser/compress/switch/constant_switch_4/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1677. **`crates/swc_ecma_minifier/tests/terser/compress/switch/constant_switch_5/input.js`** -> AI Confidence: **99.29%**
1678. **`crates/swc_ecma_minifier/tests/terser/compress/switch/constant_switch_5/output.js`** -> AI Confidence: **99.29%**
1679. **`crates/swc_ecma_minifier/tests/terser/compress/switch/constant_switch_5/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1680. **`crates/swc_ecma_minifier/tests/terser/compress/switch/constant_switch_5/output.terser.js`** -> AI Confidence: **99.29%**
1681. **`crates/swc_ecma_minifier/tests/terser/compress/switch/constant_switch_6/input.js`** -> AI Confidence: **99.29%**
1682. **`crates/swc_ecma_minifier/tests/terser/compress/switch/constant_switch_6/output.js`** -> AI Confidence: **99.29%**
1683. **`crates/swc_ecma_minifier/tests/terser/compress/switch/constant_switch_6/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1684. **`crates/swc_ecma_minifier/tests/terser/compress/switch/constant_switch_6/output.terser.js`** -> AI Confidence: **99.29%**
1685. **`crates/swc_ecma_minifier/tests/terser/compress/switch/constant_switch_7/input.js`** -> AI Confidence: **99.29%**
1686. **`crates/swc_ecma_minifier/tests/terser/compress/switch/constant_switch_7/output.js`** -> AI Confidence: **99.29%**
1687. **`crates/swc_ecma_minifier/tests/terser/compress/switch/constant_switch_7/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1688. **`crates/swc_ecma_minifier/tests/terser/compress/switch/constant_switch_7/output.terser.js`** -> AI Confidence: **99.29%**
1689. **`crates/swc_ecma_minifier/tests/terser/compress/switch/constant_switch_8/input.js`** -> AI Confidence: **99.29%**
1690. **`crates/swc_ecma_minifier/tests/terser/compress/switch/constant_switch_8/output.js`** -> AI Confidence: **99.29%**
1691. **`crates/swc_ecma_minifier/tests/terser/compress/switch/constant_switch_8/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1692. **`crates/swc_ecma_minifier/tests/terser/compress/switch/constant_switch_8/output.terser.js`** -> AI Confidence: **99.29%**
1693. **`crates/swc_ecma_minifier/tests/terser/compress/switch/constant_switch_9/input.js`** -> AI Confidence: **99.29%**
1694. **`crates/swc_ecma_minifier/tests/terser/compress/switch/constant_switch_9/output.js`** -> AI Confidence: **99.29%**
1695. **`crates/swc_ecma_minifier/tests/terser/compress/switch/constant_switch_9/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1696. **`crates/swc_ecma_minifier/tests/terser/compress/switch/constant_switch_9/output.terser.js`** -> AI Confidence: **99.29%**
1697. **`crates/swc_ecma_minifier/tests/terser/compress/switch/drop_case/input.js`** -> AI Confidence: **99.29%**
1698. **`crates/swc_ecma_minifier/tests/terser/compress/switch/drop_case/output.js`** -> AI Confidence: **99.29%**
1699. **`crates/swc_ecma_minifier/tests/terser/compress/switch/drop_case/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1700. **`crates/swc_ecma_minifier/tests/terser/compress/switch/drop_case/output.terser.js`** -> AI Confidence: **99.29%**
1701. **`crates/swc_ecma_minifier/tests/terser/compress/switch/drop_case_2/input.js`** -> AI Confidence: **99.29%**
1702. **`crates/swc_ecma_minifier/tests/terser/compress/switch/drop_case_2/output.js`** -> AI Confidence: **99.29%**
1703. **`crates/swc_ecma_minifier/tests/terser/compress/switch/drop_case_2/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1704. **`crates/swc_ecma_minifier/tests/terser/compress/switch/drop_case_2/output.terser.js`** -> AI Confidence: **99.29%**
1705. **`crates/swc_ecma_minifier/tests/terser/compress/switch/drop_default_1/input.js`** -> AI Confidence: **99.29%**
1706. **`crates/swc_ecma_minifier/tests/terser/compress/switch/drop_default_1/output.js`** -> AI Confidence: **99.29%**
1707. **`crates/swc_ecma_minifier/tests/terser/compress/switch/drop_default_1/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1708. **`crates/swc_ecma_minifier/tests/terser/compress/switch/drop_default_1/output.terser.js`** -> AI Confidence: **99.29%**
1709. **`crates/swc_ecma_minifier/tests/terser/compress/switch/drop_default_2/input.js`** -> AI Confidence: **99.29%**
1710. **`crates/swc_ecma_minifier/tests/terser/compress/switch/drop_default_2/output.js`** -> AI Confidence: **99.29%**
1711. **`crates/swc_ecma_minifier/tests/terser/compress/switch/drop_default_2/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1712. **`crates/swc_ecma_minifier/tests/terser/compress/switch/drop_default_2/output.terser.js`** -> AI Confidence: **99.29%**
1713. **`crates/swc_ecma_minifier/tests/terser/compress/switch/gut_entire_switch/input.js`** -> AI Confidence: **99.29%**
1714. **`crates/swc_ecma_minifier/tests/terser/compress/switch/gut_entire_switch/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1715. **`crates/swc_ecma_minifier/tests/terser/compress/switch/gut_entire_switch_2/input.js`** -> AI Confidence: **99.29%**
1716. **`crates/swc_ecma_minifier/tests/terser/compress/switch/gut_entire_switch_2/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1717. **`crates/swc_ecma_minifier/tests/terser/compress/switch/if_else/input.js`** -> AI Confidence: **99.29%**
1718. **`crates/swc_ecma_minifier/tests/terser/compress/switch/if_else/output.js`** -> AI Confidence: **99.29%**
1719. **`crates/swc_ecma_minifier/tests/terser/compress/switch/if_else/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1720. **`crates/swc_ecma_minifier/tests/terser/compress/switch/if_else/output.terser.js`** -> AI Confidence: **99.29%**
1721. **`crates/swc_ecma_minifier/tests/terser/compress/switch/if_else2/input.js`** -> AI Confidence: **99.29%**
1722. **`crates/swc_ecma_minifier/tests/terser/compress/switch/if_else2/output.js`** -> AI Confidence: **99.29%**
1723. **`crates/swc_ecma_minifier/tests/terser/compress/switch/if_else2/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1724. **`crates/swc_ecma_minifier/tests/terser/compress/switch/if_else2/output.terser.js`** -> AI Confidence: **99.29%**
1725. **`crates/swc_ecma_minifier/tests/terser/compress/switch/if_else3/input.js`** -> AI Confidence: **99.29%**
1726. **`crates/swc_ecma_minifier/tests/terser/compress/switch/if_else3/output.js`** -> AI Confidence: **99.29%**
1727. **`crates/swc_ecma_minifier/tests/terser/compress/switch/if_else3/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1728. **`crates/swc_ecma_minifier/tests/terser/compress/switch/if_else3/output.terser.js`** -> AI Confidence: **99.29%**
1729. **`crates/swc_ecma_minifier/tests/terser/compress/switch/if_else4/input.js`** -> AI Confidence: **99.29%**
1730. **`crates/swc_ecma_minifier/tests/terser/compress/switch/if_else4/output.js`** -> AI Confidence: **99.29%**
1731. **`crates/swc_ecma_minifier/tests/terser/compress/switch/if_else4/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1732. **`crates/swc_ecma_minifier/tests/terser/compress/switch/if_else4/output.terser.js`** -> AI Confidence: **99.29%**
1733. **`crates/swc_ecma_minifier/tests/terser/compress/switch/if_else5/input.js`** -> AI Confidence: **99.29%**
1734. **`crates/swc_ecma_minifier/tests/terser/compress/switch/if_else5/output.js`** -> AI Confidence: **99.29%**
1735. **`crates/swc_ecma_minifier/tests/terser/compress/switch/if_else5/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1736. **`crates/swc_ecma_minifier/tests/terser/compress/switch/if_else5/output.terser.js`** -> AI Confidence: **99.29%**
1737. **`crates/swc_ecma_minifier/tests/terser/compress/switch/if_else6/input.js`** -> AI Confidence: **99.29%**
1738. **`crates/swc_ecma_minifier/tests/terser/compress/switch/if_else6/output.js`** -> AI Confidence: **99.29%**
1739. **`crates/swc_ecma_minifier/tests/terser/compress/switch/if_else6/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1740. **`crates/swc_ecma_minifier/tests/terser/compress/switch/if_else6/output.terser.js`** -> AI Confidence: **99.29%**
1741. **`crates/swc_ecma_minifier/tests/terser/compress/switch/if_else7/input.js`** -> AI Confidence: **99.29%**
1742. **`crates/swc_ecma_minifier/tests/terser/compress/switch/if_else7/output.js`** -> AI Confidence: **99.29%**
1743. **`crates/swc_ecma_minifier/tests/terser/compress/switch/if_else7/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1744. **`crates/swc_ecma_minifier/tests/terser/compress/switch/if_else7/output.terser.js`** -> AI Confidence: **99.29%**
1745. **`crates/swc_ecma_minifier/tests/terser/compress/switch/if_switch_typeof/input.js`** -> AI Confidence: **99.29%**
1746. **`crates/swc_ecma_minifier/tests/terser/compress/switch/if_switch_typeof/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1747. **`crates/swc_ecma_minifier/tests/terser/compress/switch/issue_1083_1/input.js`** -> AI Confidence: **99.29%**
1748. **`crates/swc_ecma_minifier/tests/terser/compress/switch/issue_1083_1/output.js`** -> AI Confidence: **99.29%**
1749. **`crates/swc_ecma_minifier/tests/terser/compress/switch/issue_1083_1/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1750. **`crates/swc_ecma_minifier/tests/terser/compress/switch/issue_1083_1/output.terser.js`** -> AI Confidence: **99.29%**
1751. **`crates/swc_ecma_minifier/tests/terser/compress/switch/issue_1083_2/input.js`** -> AI Confidence: **99.29%**
1752. **`crates/swc_ecma_minifier/tests/terser/compress/switch/issue_1083_2/output.js`** -> AI Confidence: **99.29%**
1753. **`crates/swc_ecma_minifier/tests/terser/compress/switch/issue_1083_2/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1754. **`crates/swc_ecma_minifier/tests/terser/compress/switch/issue_1083_2/output.terser.js`** -> AI Confidence: **99.29%**
1755. **`crates/swc_ecma_minifier/tests/terser/compress/switch/issue_1083_3/input.js`** -> AI Confidence: **99.29%**
1756. **`crates/swc_ecma_minifier/tests/terser/compress/switch/issue_1083_3/output.js`** -> AI Confidence: **99.29%**
1757. **`crates/swc_ecma_minifier/tests/terser/compress/switch/issue_1083_3/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1758. **`crates/swc_ecma_minifier/tests/terser/compress/switch/issue_1083_3/output.terser.js`** -> AI Confidence: **99.29%**
1759. **`crates/swc_ecma_minifier/tests/terser/compress/switch/issue_1083_4/input.js`** -> AI Confidence: **99.29%**
1760. **`crates/swc_ecma_minifier/tests/terser/compress/switch/issue_1083_4/output.js`** -> AI Confidence: **99.29%**
1761. **`crates/swc_ecma_minifier/tests/terser/compress/switch/issue_1083_4/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1762. **`crates/swc_ecma_minifier/tests/terser/compress/switch/issue_1083_4/output.terser.js`** -> AI Confidence: **99.29%**
1763. **`crates/swc_ecma_minifier/tests/terser/compress/switch/issue_1083_5/input.js`** -> AI Confidence: **99.29%**
1764. **`crates/swc_ecma_minifier/tests/terser/compress/switch/issue_1083_5/output.js`** -> AI Confidence: **99.29%**
1765. **`crates/swc_ecma_minifier/tests/terser/compress/switch/issue_1083_5/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1766. **`crates/swc_ecma_minifier/tests/terser/compress/switch/issue_1083_5/output.terser.js`** -> AI Confidence: **99.29%**
1767. **`crates/swc_ecma_minifier/tests/terser/compress/switch/issue_1083_6/input.js`** -> AI Confidence: **99.29%**
1768. **`crates/swc_ecma_minifier/tests/terser/compress/switch/issue_1083_6/output.js`** -> AI Confidence: **99.29%**
1769. **`crates/swc_ecma_minifier/tests/terser/compress/switch/issue_1083_6/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1770. **`crates/swc_ecma_minifier/tests/terser/compress/switch/issue_1083_6/output.terser.js`** -> AI Confidence: **99.29%**
1771. **`crates/swc_ecma_minifier/tests/terser/compress/switch/issue_1674/input.js`** -> AI Confidence: **99.29%**
1772. **`crates/swc_ecma_minifier/tests/terser/compress/switch/issue_1674/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1773. **`crates/swc_ecma_minifier/tests/terser/compress/switch/issue_1679/input.js`** -> AI Confidence: **99.29%**
1774. **`crates/swc_ecma_minifier/tests/terser/compress/switch/issue_1679/output.js`** -> AI Confidence: **99.29%**
1775. **`crates/swc_ecma_minifier/tests/terser/compress/switch/issue_1679/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1776. **`crates/swc_ecma_minifier/tests/terser/compress/switch/issue_1679/output.terser.js`** -> AI Confidence: **99.29%**
1777. **`crates/swc_ecma_minifier/tests/terser/compress/switch/issue_1680_1/input.js`** -> AI Confidence: **99.29%**
1778. **`crates/swc_ecma_minifier/tests/terser/compress/switch/issue_1680_1/output.js`** -> AI Confidence: **99.29%**
1779. **`crates/swc_ecma_minifier/tests/terser/compress/switch/issue_1680_1/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1780. **`crates/swc_ecma_minifier/tests/terser/compress/switch/issue_1680_1/output.terser.js`** -> AI Confidence: **99.29%**
1781. **`crates/swc_ecma_minifier/tests/terser/compress/switch/issue_1680_2/input.js`** -> AI Confidence: **99.29%**
1782. **`crates/swc_ecma_minifier/tests/terser/compress/switch/issue_1680_2/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1783. **`crates/swc_ecma_minifier/tests/terser/compress/switch/issue_1690_1/input.js`** -> AI Confidence: **99.29%**
1784. **`crates/swc_ecma_minifier/tests/terser/compress/switch/issue_1690_1/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1785. **`crates/swc_ecma_minifier/tests/terser/compress/switch/issue_1690_2/input.js`** -> AI Confidence: **99.29%**
1786. **`crates/swc_ecma_minifier/tests/terser/compress/switch/issue_1690_2/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1787. **`crates/swc_ecma_minifier/tests/terser/compress/switch/issue_1690_2/output.terser.js`** -> AI Confidence: **99.29%**
1788. **`crates/swc_ecma_minifier/tests/terser/compress/switch/issue_1705_1/input.js`** -> AI Confidence: **99.29%**
1789. **`crates/swc_ecma_minifier/tests/terser/compress/switch/issue_1705_1/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1790. **`crates/swc_ecma_minifier/tests/terser/compress/switch/issue_1705_2/input.js`** -> AI Confidence: **99.29%**
1791. **`crates/swc_ecma_minifier/tests/terser/compress/switch/issue_1705_2/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1792. **`crates/swc_ecma_minifier/tests/terser/compress/switch/issue_1705_3/input.js`** -> AI Confidence: **99.29%**
1793. **`crates/swc_ecma_minifier/tests/terser/compress/switch/issue_1705_3/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1794. **`crates/swc_ecma_minifier/tests/terser/compress/switch/issue_1750/input.js`** -> AI Confidence: **99.29%**
1795. **`crates/swc_ecma_minifier/tests/terser/compress/switch/issue_1750/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1796. **`crates/swc_ecma_minifier/tests/terser/compress/switch/issue_2535/input.js`** -> AI Confidence: **99.29%**
1797. **`crates/swc_ecma_minifier/tests/terser/compress/switch/issue_2535/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1798. **`crates/swc_ecma_minifier/tests/terser/compress/switch/issue_376/input.js`** -> AI Confidence: **99.29%**
1799. **`crates/swc_ecma_minifier/tests/terser/compress/switch/issue_376/output.js`** -> AI Confidence: **99.29%**
1800. **`crates/swc_ecma_minifier/tests/terser/compress/switch/issue_376/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1801. **`crates/swc_ecma_minifier/tests/terser/compress/switch/issue_376/output.terser.js`** -> AI Confidence: **99.29%**
1802. **`crates/swc_ecma_minifier/tests/terser/compress/switch/issue_441_1/input.js`** -> AI Confidence: **99.29%**
1803. **`crates/swc_ecma_minifier/tests/terser/compress/switch/issue_441_1/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1804. **`crates/swc_ecma_minifier/tests/terser/compress/switch/issue_441_1/output.terser.js`** -> AI Confidence: **99.29%**
1805. **`crates/swc_ecma_minifier/tests/terser/compress/switch/issue_441_2/input.js`** -> AI Confidence: **99.29%**
1806. **`crates/swc_ecma_minifier/tests/terser/compress/switch/issue_441_2/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1807. **`crates/swc_ecma_minifier/tests/terser/compress/switch/issue_441_2/output.terser.js`** -> AI Confidence: **99.29%**
1808. **`crates/swc_ecma_minifier/tests/terser/compress/switch/keep_case/input.js`** -> AI Confidence: **99.29%**
1809. **`crates/swc_ecma_minifier/tests/terser/compress/switch/keep_case/output.js`** -> AI Confidence: **99.29%**
1810. **`crates/swc_ecma_minifier/tests/terser/compress/switch/keep_case/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1811. **`crates/swc_ecma_minifier/tests/terser/compress/switch/keep_case/output.terser.js`** -> AI Confidence: **99.29%**
1812. **`crates/swc_ecma_minifier/tests/terser/compress/switch/keep_default/input.js`** -> AI Confidence: **99.29%**
1813. **`crates/swc_ecma_minifier/tests/terser/compress/switch/keep_default/output.js`** -> AI Confidence: **99.29%**
1814. **`crates/swc_ecma_minifier/tests/terser/compress/switch/keep_default/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1815. **`crates/swc_ecma_minifier/tests/terser/compress/switch/keep_default/output.terser.js`** -> AI Confidence: **99.29%**
1816. **`crates/swc_ecma_minifier/tests/terser/compress/switch/turn_into_if/input.js`** -> AI Confidence: **99.29%**
1817. **`crates/swc_ecma_minifier/tests/terser/compress/switch/turn_into_if/output.js`** -> AI Confidence: **99.29%**
1818. **`crates/swc_ecma_minifier/tests/terser/compress/switch/turn_into_if/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1819. **`crates/swc_ecma_minifier/tests/terser/compress/switch/turn_into_if/output.terser.js`** -> AI Confidence: **99.29%**
1820. **`crates/swc_ecma_minifier/tests/terser/compress/switch/turn_into_if_2/input.js`** -> AI Confidence: **99.29%**
1821. **`crates/swc_ecma_minifier/tests/terser/compress/switch/turn_into_if_2/output.js`** -> AI Confidence: **99.29%**
1822. **`crates/swc_ecma_minifier/tests/terser/compress/switch/turn_into_if_2/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1823. **`crates/swc_ecma_minifier/tests/terser/compress/switch/turn_into_if_2/output.terser.js`** -> AI Confidence: **99.29%**
1824. **`crates/swc_ecma_minifier/tests/terser/compress/template_string/regex_1/input.js`** -> AI Confidence: **99.29%**
1825. **`crates/swc_ecma_minifier/tests/terser/compress/template_string/regex_1/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1826. **`crates/swc_ecma_minifier/tests/terser/compress/template_string/regex_1/output.terser.js`** -> AI Confidence: **99.29%**
1827. **`crates/swc_ecma_minifier/tests/terser/compress/template_string/regex_2/input.js`** -> AI Confidence: **99.29%**
1828. **`crates/swc_ecma_minifier/tests/terser/compress/template_string/regex_2/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1829. **`crates/swc_ecma_minifier/tests/terser/compress/transform/condition_evaluate/input.js`** -> AI Confidence: **99.29%**
1830. **`crates/swc_ecma_minifier/tests/terser/compress/transform/condition_evaluate/output.js`** -> AI Confidence: **99.29%**
1831. **`crates/swc_ecma_minifier/tests/terser/compress/transform/condition_evaluate/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1832. **`crates/swc_ecma_minifier/tests/terser/compress/transform/condition_evaluate/output.terser.js`** -> AI Confidence: **99.29%**
1833. **`crates/swc_ecma_minifier/tests/terser/compress/transform/if_else_empty/input.js`** -> AI Confidence: **99.29%**
1834. **`crates/swc_ecma_minifier/tests/terser/compress/transform/if_else_empty/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1835. **`crates/swc_ecma_minifier/tests/terser/compress/transform/if_else_empty/output.terser.js`** -> AI Confidence: **99.29%**
1836. **`crates/swc_ecma_minifier/tests/terser/compress/transform/label_if_break/input.js`** -> AI Confidence: **99.29%**
1837. **`crates/swc_ecma_minifier/tests/terser/compress/transform/label_if_break/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1838. **`crates/swc_ecma_minifier/tests/terser/compress/transform/while_if_break/input.js`** -> AI Confidence: **99.29%**
1839. **`crates/swc_ecma_minifier/tests/terser/compress/transform/while_if_break/output.js`** -> AI Confidence: **99.29%**
1840. **`crates/swc_ecma_minifier/tests/terser/compress/transform/while_if_break/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1841. **`crates/swc_ecma_minifier/tests/terser/compress/transform/while_if_break/output.terser.js`** -> AI Confidence: **99.29%**
1842. **`crates/swc_ecma_minifier/tests/terser/compress/try_catch/catch_destructuring_with_sequence/input.js`** -> AI Confidence: **99.29%**
1843. **`crates/swc_ecma_minifier/tests/terser/compress/try_catch/catch_destructuring_with_sequence/output.js`** -> AI Confidence: **99.29%**
1844. **`crates/swc_ecma_minifier/tests/terser/compress/try_catch/catch_destructuring_with_sequence/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1845. **`crates/swc_ecma_minifier/tests/terser/compress/try_catch/catch_destructuring_with_sequence/output.terser.js`** -> AI Confidence: **99.29%**
1846. **`crates/swc_ecma_minifier/tests/terser/compress/try_catch/issue_452/input.js`** -> AI Confidence: **99.29%**
1847. **`crates/swc_ecma_minifier/tests/terser/compress/try_catch/issue_452/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1848. **`crates/swc_ecma_minifier/tests/terser/compress/try_catch/parameterless_catch/input.js`** -> AI Confidence: **99.29%**
1849. **`crates/swc_ecma_minifier/tests/terser/compress/try_catch/parameterless_catch/output.js`** -> AI Confidence: **99.29%**
1850. **`crates/swc_ecma_minifier/tests/terser/compress/try_catch/parameterless_catch/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1851. **`crates/swc_ecma_minifier/tests/terser/compress/try_catch/parameterless_catch/output.terser.js`** -> AI Confidence: **99.29%**
1852. **`crates/swc_ecma_minifier/tests/terser/compress/typeof/issue_1668/input.js`** -> AI Confidence: **99.29%**
1853. **`crates/swc_ecma_minifier/tests/terser/compress/typeof/issue_1668/output.js`** -> AI Confidence: **99.29%**
1854. **`crates/swc_ecma_minifier/tests/terser/compress/typeof/issue_1668/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1855. **`crates/swc_ecma_minifier/tests/terser/compress/typeof/issue_1668/output.terser.js`** -> AI Confidence: **99.29%**
1856. **`crates/swc_ecma_minifier/tests/terser/compress/typeof/typeof_defun_1/input.js`** -> AI Confidence: **99.29%**
1857. **`crates/swc_ecma_minifier/tests/terser/compress/typeof/typeof_defun_1/output.mangleOnly.js`** -> AI Confidence: **99.29%**
1858. **`crates/swc_ecma_parser/benches/files/yui-3.12.0.js`** -> AI Confidence: **99.29%**
1859. **`crates/swc_ecma_parser/tests/comments/stmts/block/input.js`** -> AI Confidence: **99.29%**
1860. **`crates/swc_ecma_parser/tests/comments/stmts/switch/input.js`** -> AI Confidence: **99.29%**
1861. **`crates/swc_ecma_parser/tests/errors/duplicate_label/input.js`** -> AI Confidence: **99.29%**
1862. **`crates/swc_ecma_parser/tests/errors/explicit-resource-management/invalid-for-using-binding-in/input.js`** -> AI Confidence: **99.29%**
1863. **`crates/swc_ecma_parser/tests/errors/explicit-resource-management/invalid-for-using-binding-of-in/input.js`** -> AI Confidence: **99.29%**
1864. **`crates/swc_ecma_parser/tests/errors/explicit-resource-management/invalid-in-single-statement-context/input.js`** -> AI Confidence: **99.29%**
1865. **`crates/swc_ecma_parser/tests/errors/explicit-resource-management/invalid-using-binding-pattern-for-lhs/input.js`** -> AI Confidence: **99.29%**
1866. **`crates/swc_ecma_parser/tests/errors/optional-chaining/tagged-template.js`** -> AI Confidence: **99.29%**
1867. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/async_await/migrated_0000.js`** -> AI Confidence: **99.29%**
1868. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/catch/optional_catch_binding.js`** -> AI Confidence: **99.29%**
1869. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/comment_interning/break.js`** -> AI Confidence: **99.29%**
1870. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/comment_interning/catch.js`** -> AI Confidence: **99.29%**
1871. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/comment_interning/conditional.js`** -> AI Confidence: **99.29%**
1872. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/comment_interning/continue.js`** -> AI Confidence: **99.29%**
1873. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/comment_interning/for.js`** -> AI Confidence: **99.29%**
1874. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/comment_interning/if.js`** -> AI Confidence: **99.29%**
1875. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/comment_interning/switch.js`** -> AI Confidence: **99.29%**
1876. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/comment_interning/try.js`** -> AI Confidence: **99.29%**
1877. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/comment_interning/while.js`** -> AI Confidence: **99.29%**
1878. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/components/component_param_string_no_rename.js`** -> AI Confidence: **99.29%**
1879. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/components/component_params.js`** -> AI Confidence: **99.29%**
1880. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/components/declare_component_params.js`** -> AI Confidence: **99.29%**
1881. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/components/declare_component_params_rest.js`** -> AI Confidence: **99.29%**
1882. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/expression/binary-logical/and_on_lhs_of_or.js`** -> AI Confidence: **99.29%**
1883. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/expression/binary-logical/migrated_0000.js`** -> AI Confidence: **99.29%**
1884. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/expression/binary-logical/migrated_0001.js`** -> AI Confidence: **99.29%**
1885. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/expression/binary-logical/migrated_0002.js`** -> AI Confidence: **99.29%**
1886. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/expression/binary-logical/migrated_0003.js`** -> AI Confidence: **99.29%**
1887. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/expression/binary-logical/migrated_0004.js`** -> AI Confidence: **99.29%**
1888. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/expression/binary-logical/migrated_0005.js`** -> AI Confidence: **99.29%**
1889. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/for_of_loops/for_async_of.js`** -> AI Confidence: **99.29%**
1890. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/for_of_loops/for_async_of_escaped.js`** -> AI Confidence: **99.29%**
1891. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/internal_slot/object_optional.js`** -> AI Confidence: **99.29%**
1892. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/invalid_syntax/migrated_0007.js`** -> AI Confidence: **99.29%**
1893. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/invalid_syntax/migrated_0008.js`** -> AI Confidence: **99.29%**
1894. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/invalid_syntax/migrated_0009.js`** -> AI Confidence: **99.29%**
1895. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/logical_assignment_operators/and_assignment.js`** -> AI Confidence: **99.29%**
1896. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/logical_assignment_operators/nullish_assignment.js`** -> AI Confidence: **99.29%**
1897. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/logical_assignment_operators/or_assignment.js`** -> AI Confidence: **99.29%**
1898. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/match/as-identifier.js`** -> AI Confidence: **99.29%**
1899. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/match/expression-guards.js`** -> AI Confidence: **99.29%**
1900. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/match/statement-guards.js`** -> AI Confidence: **99.29%**
1901. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/nullish_coalescing/multiple.js`** -> AI Confidence: **99.29%**
1902. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/nullish_coalescing/multiple_no_whitespace.js`** -> AI Confidence: **99.29%**
1903. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/nullish_coalescing/precedence_and.js`** -> AI Confidence: **99.29%**
1904. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/nullish_coalescing/precedence_and_lhs_no_parens.js`** -> AI Confidence: **99.29%**
1905. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/nullish_coalescing/precedence_and_nested_lhs.js`** -> AI Confidence: **99.29%**
1906. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/nullish_coalescing/precedence_and_nested_rhs.js`** -> AI Confidence: **99.29%**
1907. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/nullish_coalescing/precedence_and_rhs_no_parens.js`** -> AI Confidence: **99.29%**
1908. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/nullish_coalescing/precedence_multiple_on_or_rhs_no_parens.js`** -> AI Confidence: **99.29%**
1909. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/nullish_coalescing/precedence_or.js`** -> AI Confidence: **99.29%**
1910. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/nullish_coalescing/precedence_or_lhs_no_parens.js`** -> AI Confidence: **99.29%**
1911. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/nullish_coalescing/precedence_or_no_parens.js`** -> AI Confidence: **99.29%**
1912. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/nullish_coalescing/precedence_or_rhs_no_parens.js`** -> AI Confidence: **99.29%**
1913. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/nullish_coalescing/simple.js`** -> AI Confidence: **99.29%**
1914. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/optional_chaining/class-constructor-call.js`** -> AI Confidence: **99.29%**
1915. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/optional_chaining/conditional-decimal.js`** -> AI Confidence: **99.29%**
1916. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/optional_chaining/function-call.js`** -> AI Confidence: **99.29%**
1917. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/optional_chaining/member-access-bracket.js`** -> AI Confidence: **99.29%**
1918. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/optional_chaining/member-access.js`** -> AI Confidence: **99.29%**
1919. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/optional_chaining/optional-chain-expression.js`** -> AI Confidence: **99.29%**
1920. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/optional_chaining/parenthesized-chain.js`** -> AI Confidence: **99.29%**
1921. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/optional_chaining/separated-chaining.js`** -> AI Confidence: **99.29%**
1922. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/optional_chaining/template-literal-tagged.js`** -> AI Confidence: **99.29%**
1923. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/optional_chaining/template-literals.js`** -> AI Confidence: **99.29%**
1924. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/statement/for/for_async_of_parens.js`** -> AI Confidence: **99.29%**
1925. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/statement/if/declare_in_consequent.js`** -> AI Confidence: **99.29%**
1926. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/statement/labelled/undefined_label_break.js`** -> AI Confidence: **99.29%**
1927. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/statement/labelled/undefined_label_continue.js`** -> AI Confidence: **99.29%**
1928. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/ts_syntax/as.js`** -> AI Confidence: **99.29%**
1929. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/typeapp_call/function_call_optional.js`** -> AI Confidence: **99.29%**
1930. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/typeapp_call/method_call_optional.js`** -> AI Confidence: **99.29%**
1931. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/typeapp_call/method_call_optional2.js`** -> AI Confidence: **99.29%**
1932. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/types/and_or/and.js`** -> AI Confidence: **99.29%**
1933. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/types/and_or/or.js`** -> AI Confidence: **99.29%**
1934. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/types/annotations/migrated_0001.js`** -> AI Confidence: **99.29%**
1935. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/types/annotations/migrated_0005.js`** -> AI Confidence: **99.29%**
1936. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/types/declare_namespace/unsupported-children.js`** -> AI Confidence: **99.29%**
1937. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/types/indexed_access/indexed_access_optional.js`** -> AI Confidence: **99.29%**
1938. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/types/indexed_access/invalid_optional.js`** -> AI Confidence: **99.29%**
1939. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/types/indexed_access/parenthesized_optional.js`** -> AI Confidence: **99.29%**
1940. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/types/interfaces/prop_named_static.js`** -> AI Confidence: **99.29%**
1941. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/types/interfaces/reserved_value.js`** -> AI Confidence: **99.29%**
1942. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/types/object/indexers/reserved_word_indexer_name.js`** -> AI Confidence: **99.29%**
1943. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/types/opaque_aliases/valid/reserved_value.js`** -> AI Confidence: **99.29%**
1944. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/types/parameter_defaults/migrated_0001.js`** -> AI Confidence: **99.29%**
1945. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/types/parameter_defaults/migrated_0002.js`** -> AI Confidence: **99.29%**
1946. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/types/parameter_defaults/migrated_0003.js`** -> AI Confidence: **99.29%**
1947. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/types/render_types/renders_maybe.js`** -> AI Confidence: **99.29%**
1948. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/types/this_constraints/error_optional.js`** -> AI Confidence: **99.29%**
1949. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/types/tuples/invalid_labeled_optional_missing_colon.js`** -> AI Confidence: **99.29%**
1950. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/types/tuples/invalid_labeled_optional_without_type.js`** -> AI Confidence: **99.29%**
1951. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/types/tuples/optional.js`** -> AI Confidence: **99.29%**
1952. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/types/tuples/spread-with-optional.js`** -> AI Confidence: **99.29%**
1953. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/types/typeof/default.js`** -> AI Confidence: **99.29%**
1954. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/uninitialized_const_bindings/migrated_0000.js`** -> AI Confidence: **99.29%**
1955. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/uninitialized_const_bindings/migrated_0001.js`** -> AI Confidence: **99.29%**
1956. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/uninitialized_const_bindings_invalid/migrated_0000.js`** -> AI Confidence: **99.29%**
1957. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/uninitialized_destructured_bindings/migrated_0005.js`** -> AI Confidence: **99.29%**
1958. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/uninitialized_destructured_bindings/migrated_0008.js`** -> AI Confidence: **99.29%**
1959. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/uninitialized_destructured_bindings_invalid/migrated_0002.js`** -> AI Confidence: **99.29%**
1960. **`crates/swc_ecma_parser/tests/flow/issue-11729-mapped-type-trailing-comma/basic.js`** -> AI Confidence: **99.29%**
1961. **`crates/swc_ecma_parser/tests/js/explicit-resource-management/valid-using-as-identifier-computed-member-no-plugin/input.js`** -> AI Confidence: **99.29%**
1962. **`crates/swc_ecma_parser/tests/js/explicit-resource-management/valid-using-as-identifier-computed-member/input.js`** -> AI Confidence: **99.29%**
1963. **`crates/swc_ecma_parser/tests/js/explicit-resource-management/valid-using-as-identifier-for-in/input.js`** -> AI Confidence: **99.29%**
1964. **`crates/swc_ecma_parser/tests/js/explicit-resource-management/valid-using-as-identifier-for-init/input.js`** -> AI Confidence: **99.29%**
1965. **`crates/swc_ecma_parser/tests/js/explicit-resource-management/valid-using-as-identifier-for-of/input.js`** -> AI Confidence: **99.29%**
1966. **`crates/swc_ecma_parser/tests/js/explicit-resource-management/valid-using-binding-using/input.js`** -> AI Confidence: **99.29%**
1967. **`crates/swc_ecma_parser/tests/js/optional-chaining/1/input.js`** -> AI Confidence: **99.29%**
1968. **`crates/swc_ecma_parser/tests/js/optional-chaining/2/input.js`** -> AI Confidence: **99.29%**
1969. **`crates/swc_ecma_parser/tests/js/optional-chaining/3/input.js`** -> AI Confidence: **99.29%**
1970. **`crates/swc_ecma_parser/tests/js/optional-chaining/4/input.js`** -> AI Confidence: **99.29%**
1971. **`crates/swc_ecma_parser/tests/js/optional-chaining/5/input.js`** -> AI Confidence: **99.29%**
1972. **`crates/swc_ecma_parser/tests/js/stack-overflow/1.js`** -> AI Confidence: **99.29%**
1973. **`crates/swc_ecma_parser/tests/jsx/basic/8/input.js`** -> AI Confidence: **99.29%**
1974. **`crates/swc_ecma_parser/tests/jsx/basic/issue-10729/input.js`** -> AI Confidence: **99.29%**
1975. **`crates/swc_ecma_parser/tests/jsx/basic/issue-11134/input.jsx`** -> AI Confidence: **99.29%**
1976. **`crates/swc_ecma_parser/tests/jsx/errors/issue-11650/input.js`** -> AI Confidence: **99.29%**
1977. **`crates/swc_ecma_parser/tests/span/js/expr/cond.js`** -> AI Confidence: **99.29%**
1978. **`crates/swc_ecma_parser/tests/span/js/expr/optional-chaining.js`** -> AI Confidence: **99.29%**
1979. **`crates/swc_ecma_parser/tests/span/js/srcmap/1/input.js`** -> AI Confidence: **99.29%**
1980. **`crates/swc_ecma_parser/tests/span/js/stmt/do-while.js`** -> AI Confidence: **99.29%**
1981. **`crates/swc_ecma_parser/tests/span/js/stmt/for-in.js`** -> AI Confidence: **99.29%**
1982. **`crates/swc_ecma_parser/tests/span/js/stmt/if.js`** -> AI Confidence: **99.29%**
1983. **`crates/swc_ecma_parser/tests/span/js/stmt/label.js`** -> AI Confidence: **99.29%**
1984. **`crates/swc_ecma_parser/tests/span/js/stmt/switch.js`** -> AI Confidence: **99.29%**
1985. **`crates/swc_ecma_parser/tests/span/js/stmt/try-catch-finally.js`** -> AI Confidence: **99.29%**
1986. **`crates/swc_ecma_parser/tests/span/js/stmt/try-catch.js`** -> AI Confidence: **99.29%**
1987. **`crates/swc_ecma_parser/tests/span/js/stmt/try-finally.js`** -> AI Confidence: **99.29%**
1988. **`crates/swc_ecma_parser/tests/span/js/stmt/while.js`** -> AI Confidence: **99.29%**
1989. **`crates/swc_ecma_preset_env/scripts/copy-data.js`** -> AI Confidence: **99.29%**
1990. **`crates/swc_ecma_preset_env/tests/fixtures/corejs2/usage-destructuring-catch/input.mjs`** -> AI Confidence: **99.29%**
1991. **`crates/swc_ecma_preset_env/tests/fixtures/corejs2/usage-for-of-destructure-with/input.mjs`** -> AI Confidence: **99.29%**
1992. **`crates/swc_ecma_preset_env/tests/fixtures/corejs3/usage-destructuring-catch/input.mjs`** -> AI Confidence: **99.29%**
1993. **`crates/swc_ecma_preset_env/tests/fixtures/corejs3/usage-for-of-destructure-with/input.mjs`** -> AI Confidence: **99.29%**
1994. **`crates/swc_ecma_preset_env/tests/fixtures/corejs3/usage-regexp/input.mjs`** -> AI Confidence: **99.29%**
1995. **`crates/swc_ecma_transforms_base/src/helpers/_check_private_redeclaration.js`** -> AI Confidence: **99.29%**
1996. **`crates/swc_ecma_transforms_base/src/helpers/_class_apply_descriptor_set.js`** -> AI Confidence: **99.29%**
1997. **`crates/swc_ecma_transforms_base/src/helpers/_class_check_private_static_access.js`** -> AI Confidence: **99.29%**
1998. **`crates/swc_ecma_transforms_base/src/helpers/_class_check_private_static_field_descriptor.js`** -> AI Confidence: **99.29%**
1999. **`crates/swc_ecma_transforms_base/src/helpers/_inherits.js`** -> AI Confidence: **99.29%**
2000. **`crates/swc_ecma_transforms_base/src/helpers/_new_arrow_check.js`** -> AI Confidence: **99.29%**
2001. **`crates/swc_ecma_transforms_base/src/helpers/_ts_add_disposable_resource.js`** -> AI Confidence: **99.29%**
2002. **`crates/swc_ecma_transforms_base/src/helpers/_ts_decorate.js`** -> AI Confidence: **99.29%**
2003. **`crates/swc_ecma_transforms_base/src/helpers/_ts_generator.js`** -> AI Confidence: **99.29%**
2004. **`crates/swc_ecma_transforms_base/src/helpers/_ts_rewrite_relative_import_extension.js`** -> AI Confidence: **99.29%**
2005. **`crates/swc_ecma_transforms_base/src/helpers/_using.js`** -> AI Confidence: **99.29%**
2006. **`crates/swc_ecma_transforms_base/tests/resolver/issues/281/1/input.js`** -> AI Confidence: **99.29%**
2007. **`crates/swc_ecma_transforms_base/tests/resolver/issues/281/1/output.js`** -> AI Confidence: **99.29%**
2008. **`crates/swc_ecma_transforms_base/tests/resolver/issues/281/2/input.js`** -> AI Confidence: **99.29%**
2009. **`crates/swc_ecma_transforms_base/tests/resolver/issues/281/2/output.js`** -> AI Confidence: **99.29%**
2010. **`crates/swc_ecma_transforms_base/tests/resolver/issues/483/input.js`** -> AI Confidence: **99.29%**
2011. **`crates/swc_ecma_transforms_base/tests/resolver/issues/483/output.js`** -> AI Confidence: **99.29%**
2012. **`crates/swc_ecma_transforms_base/tests/resolver/issues/6310/input.js`** -> AI Confidence: **99.29%**
2013. **`crates/swc_ecma_transforms_base/tests/resolver/issues/6310/output.js`** -> AI Confidence: **99.29%**
2014. **`crates/swc_ecma_transforms_base/tests/resolver/issues/788/2/input.js`** -> AI Confidence: **99.29%**
2015. **`crates/swc_ecma_transforms_base/tests/resolver/issues/788/2/output.js`** -> AI Confidence: **99.29%**
2016. **`crates/swc_ecma_transforms_base/tests/resolver/minifier/1/input.js`** -> AI Confidence: **99.29%**
2017. **`crates/swc_ecma_transforms_base/tests/resolver/minifier/1/output.js`** -> AI Confidence: **99.29%**
2018. **`crates/swc_ecma_transforms_base/tests/resolver/pr_1171/1/input.js`** -> AI Confidence: **99.29%**
2019. **`crates/swc_ecma_transforms_base/tests/resolver/pr_1171/1/output.js`** -> AI Confidence: **99.29%**
2020. **`crates/swc_ecma_transforms_base/tests/resolver/pr_1171/2/input.js`** -> AI Confidence: **99.29%**
2021. **`crates/swc_ecma_transforms_base/tests/resolver/pr_1171/2/output.js`** -> AI Confidence: **99.29%**
2022. **`crates/swc_ecma_transforms_compat/tests/__swc_snapshots__/tests/es2015_block_scoping.rs/issue_686.js`** -> AI Confidence: **99.29%**
2023. **`crates/swc_ecma_transforms_compat/tests/__swc_snapshots__/tests/es2015_destructuring.rs/array_pat_assign_prop_binding_4.js`** -> AI Confidence: **99.29%**
2024. **`crates/swc_ecma_transforms_compat/tests/__swc_snapshots__/tests/es2015_destructuring.rs/array_pat_assign_prop_binding_5.js`** -> AI Confidence: **99.29%**
2025. **`crates/swc_ecma_transforms_compat/tests/__swc_snapshots__/tests/es2015_destructuring.rs/array_pat_assign_prop_binding_6.js`** -> AI Confidence: **99.29%**
2026. **`crates/swc_ecma_transforms_compat/tests/__swc_snapshots__/tests/es2015_destructuring.rs/array_pat_assign_prop_binding_7.js`** -> AI Confidence: **99.29%**
2027. **`crates/swc_ecma_transforms_compat/tests/__swc_snapshots__/tests/es2015_destructuring.rs/issue_1477_1.js`** -> AI Confidence: **99.29%**
2028. **`crates/swc_ecma_transforms_compat/tests/__swc_snapshots__/tests/es2015_destructuring.rs/issue_1477_2.js`** -> AI Confidence: **99.29%**
2029. **`crates/swc_ecma_transforms_compat/tests/__swc_snapshots__/tests/es2015_destructuring.rs/issue_1477_3.js`** -> AI Confidence: **99.29%**
2030. **`crates/swc_ecma_transforms_compat/tests/__swc_snapshots__/tests/es2015_destructuring.rs/object_pat_assign_prop_2.js`** -> AI Confidence: **99.29%**
2031. **`crates/swc_ecma_transforms_compat/tests/__swc_snapshots__/tests/es2015_destructuring.rs/object_pat_assign_prop_binding_2.js`** -> AI Confidence: **99.29%**
2032. **`crates/swc_ecma_transforms_compat/tests/__swc_snapshots__/tests/es2015_parameters.rs/default_rest_mix.js`** -> AI Confidence: **99.29%**
2033. **`crates/swc_ecma_transforms_compat/tests/__swc_snapshots__/tests/es2020_nullish_coalescing.rs/assign_01.js`** -> AI Confidence: **99.29%**
2034. **`crates/swc_ecma_transforms_compat/tests/__swc_snapshots__/tests/es2020_nullish_coalescing.rs/issue_6328.js`** -> AI Confidence: **99.29%**
2035. **`crates/swc_ecma_transforms_compat/tests/__swc_snapshots__/tests/es2020_nullish_coalescing.rs/transform_static_refs_in_default.js`** -> AI Confidence: **99.29%**
2036. **`crates/swc_ecma_transforms_compat/tests/__swc_snapshots__/tests/es2020_optional_chaining.rs/simple_2.js`** -> AI Confidence: **99.29%**
2037. **`crates/swc_ecma_transforms_compat/tests/__swc_snapshots__/tests/es2021_logcal_assignments.rs/logical_ident.js`** -> AI Confidence: **99.29%**
2038. **`crates/swc_ecma_transforms_compat/tests/__swc_snapshots__/tests/es2021_logcal_assignments.rs/nullish_ident.js`** -> AI Confidence: **99.29%**
2039. **`crates/swc_ecma_transforms_compat/tests/arrow/statement/output.js`** -> AI Confidence: **99.29%**
2040. **`crates/swc_ecma_transforms_compat/tests/async-to-generator/nested-try/in-block-no-handler/exec.js`** -> AI Confidence: **99.29%**
2041. **`crates/swc_ecma_transforms_compat/tests/async-to-generator/nested-try/in-blokc-with-handler/exec.js`** -> AI Confidence: **99.29%**
2042. **`crates/swc_ecma_transforms_compat/tests/async-to-generator/nested-try/in-finally-with-catch/exec.js`** -> AI Confidence: **99.29%**
2043. **`crates/swc_ecma_transforms_compat/tests/for-of/1/exec.js`** -> AI Confidence: **99.29%**
2044. **`crates/swc_ecma_transforms_compat/tests/new-target/general/object/output.js`** -> AI Confidence: **99.29%**
2045. **`crates/swc_ecma_transforms_compat/tests/optional-chaining-loose/general-function-call-loose/input.js`** -> AI Confidence: **99.29%**
2046. **`crates/swc_ecma_transforms_compat/tests/optional-chaining-loose/general-function-call-loose/output.js`** -> AI Confidence: **99.29%**
2047. **`crates/swc_ecma_transforms_compat/tests/optional-chaining-loose/general-function-param-loose/input.js`** -> AI Confidence: **99.29%**
2048. **`crates/swc_ecma_transforms_compat/tests/optional-chaining-loose/general-function-param-loose/output.js`** -> AI Confidence: **99.29%**
2049. **`crates/swc_ecma_transforms_compat/tests/optional-chaining-loose/general-member-expression-loose/input.js`** -> AI Confidence: **99.29%**
2050. **`crates/swc_ecma_transforms_compat/tests/optional-chaining-loose/general-member-expression-loose/output.js`** -> AI Confidence: **99.29%**
2051. **`crates/swc_ecma_transforms_compat/tests/optional-chaining-loose/general-memoize-loose/input.js`** -> AI Confidence: **99.29%**
2052. **`crates/swc_ecma_transforms_compat/tests/optional-chaining-loose/general-memoize-loose/output.js`** -> AI Confidence: **99.29%**
2053. **`crates/swc_ecma_transforms_compat/tests/optional-chaining/call-1/input.js`** -> AI Confidence: **99.29%**
2054. **`crates/swc_ecma_transforms_compat/tests/optional-chaining/call-1/output.js`** -> AI Confidence: **99.29%**
2055. **`crates/swc_ecma_transforms_compat/tests/optional-chaining/call-2/input.js`** -> AI Confidence: **99.29%**
2056. **`crates/swc_ecma_transforms_compat/tests/optional-chaining/call-2/output.js`** -> AI Confidence: **99.29%**
2057. **`crates/swc_ecma_transforms_compat/tests/optional-chaining/curried-function-call/input.js`** -> AI Confidence: **99.29%**
2058. **`crates/swc_ecma_transforms_compat/tests/optional-chaining/curried-function-call/output.js`** -> AI Confidence: **99.29%**
2059. **`crates/swc_ecma_transforms_compat/tests/optional-chaining/general-assignment/input.js`** -> AI Confidence: **99.29%**
2060. **`crates/swc_ecma_transforms_compat/tests/optional-chaining/general-assignment/output.js`** -> AI Confidence: **99.29%**
2061. **`crates/swc_ecma_transforms_compat/tests/optional-chaining/general-containers/input.js`** -> AI Confidence: **99.29%**
2062. **`crates/swc_ecma_transforms_compat/tests/optional-chaining/general-containers/output.js`** -> AI Confidence: **99.29%**
2063. **`crates/swc_ecma_transforms_compat/tests/optional-chaining/general-function-call/input.js`** -> AI Confidence: **99.29%**
2064. **`crates/swc_ecma_transforms_compat/tests/optional-chaining/general-function-call/output.js`** -> AI Confidence: **99.29%**
2065. **`crates/swc_ecma_transforms_compat/tests/optional-chaining/general-member-access/input.js`** -> AI Confidence: **99.29%**
2066. **`crates/swc_ecma_transforms_compat/tests/optional-chaining/general-member-access/output.js`** -> AI Confidence: **99.29%**
2067. **`crates/swc_ecma_transforms_compat/tests/optional-chaining/general-memoize/input.js`** -> AI Confidence: **99.29%**
2068. **`crates/swc_ecma_transforms_compat/tests/optional-chaining/general-memoize/output.js`** -> AI Confidence: **99.29%**
2069. **`crates/swc_ecma_transforms_compat/tests/optional-chaining/general-unary/input.js`** -> AI Confidence: **99.29%**
2070. **`crates/swc_ecma_transforms_compat/tests/optional-chaining/general-unary/output.js`** -> AI Confidence: **99.29%**
2071. **`crates/swc_ecma_transforms_compat/tests/optional-chaining/indirect-eval-call/input.js`** -> AI Confidence: **99.29%**
2072. **`crates/swc_ecma_transforms_compat/tests/optional-chaining/indirect-eval-call/output.js`** -> AI Confidence: **99.29%**
2073. **`crates/swc_ecma_transforms_compat/tests/optional-chaining/issue-1092/1/input.js`** -> AI Confidence: **99.29%**
2074. **`crates/swc_ecma_transforms_compat/tests/optional-chaining/issue-1092/2/input.js`** -> AI Confidence: **99.29%**
2075. **`crates/swc_ecma_transforms_compat/tests/optional-chaining/issue-1136-1/input.js`** -> AI Confidence: **99.29%**
2076. **`crates/swc_ecma_transforms_compat/tests/optional-chaining/issue-2063/1/exec.js`** -> AI Confidence: **99.29%**
2077. **`crates/swc_ecma_transforms_compat/tests/optional-chaining/issue-2063/2/exec.js`** -> AI Confidence: **99.29%**
2078. **`crates/swc_ecma_transforms_compat/tests/optional-chaining/issue-6762/1/exec.js`** -> AI Confidence: **99.29%**
2079. **`crates/swc_ecma_transforms_compat/tests/optional-chaining/issue-6762/1/input.js`** -> AI Confidence: **99.29%**
2080. **`crates/swc_ecma_transforms_compat/tests/optional-chaining/issue-6762/1/output.js`** -> AI Confidence: **99.29%**
2081. **`crates/swc_ecma_transforms_compat/tests/optional-chaining/issue-7156/1/input.js`** -> AI Confidence: **99.29%**
2082. **`crates/swc_ecma_transforms_compat/tests/optional-chaining/issue-7156/1/output.js`** -> AI Confidence: **99.29%**
2083. **`crates/swc_ecma_transforms_compat/tests/optional-chaining/issue-7156/2/input.js`** -> AI Confidence: **99.29%**
2084. **`crates/swc_ecma_transforms_compat/tests/optional-chaining/issue-7312/input.js`** -> AI Confidence: **99.29%**
2085. **`crates/swc_ecma_transforms_compat/tests/optional-chaining/issue-7312/output.js`** -> AI Confidence: **99.29%**
2086. **`crates/swc_ecma_transforms_compat/tests/optional-chaining/issue-732/1/input.js`** -> AI Confidence: **99.29%**
2087. **`crates/swc_ecma_transforms_compat/tests/optional-chaining/issue-732/2/input.js`** -> AI Confidence: **99.29%**
2088. **`crates/swc_ecma_transforms_compat/tests/optional-chaining/issue-732/3/input.js`** -> AI Confidence: **99.29%**
2089. **`crates/swc_ecma_transforms_compat/tests/optional-chaining/issue-7441/1/input.js`** -> AI Confidence: **99.29%**
2090. **`crates/swc_ecma_transforms_compat/tests/optional-chaining/issue-7441/2/input.js`** -> AI Confidence: **99.29%**
2091. **`crates/swc_ecma_transforms_compat/tests/optional-chaining/issue-7441/3/input.js`** -> AI Confidence: **99.29%**
2092. **`crates/swc_ecma_transforms_compat/tests/optional-chaining/issue-7441/3/output.js`** -> AI Confidence: **99.29%**
2093. **`crates/swc_ecma_transforms_compat/tests/optional-chaining/parenthesis/input.js`** -> AI Confidence: **99.29%**
2094. **`crates/swc_ecma_transforms_compat/tests/optional-chaining/parenthesis/output.js`** -> AI Confidence: **99.29%**
2095. **`crates/swc_ecma_transforms_compat/tests/optional-chaining/simple-3/input.js`** -> AI Confidence: **99.29%**
2096. **`crates/swc_ecma_transforms_compat/tests/optional-chaining/simple-3/output.js`** -> AI Confidence: **99.29%**
2097. **`crates/swc_ecma_transforms_compat/tests/optional-chaining/swc-node-95-2/input.js`** -> AI Confidence: **99.29%**
2098. **`crates/swc_ecma_transforms_compat/tests/optional-chaining/swc-node-95-2/output.js`** -> AI Confidence: **99.29%**
2099. **`crates/swc_ecma_transforms_compat/tests/optional-chaining/swc-node-95-3/input.js`** -> AI Confidence: **99.29%**
2100. **`crates/swc_ecma_transforms_compat/tests/optional-chaining/swc-node-95-3/output.js`** -> AI Confidence: **99.29%**
2101. **`crates/swc_ecma_transforms_compat/tests/optional-chaining/swc-node-issue-62/input.js`** -> AI Confidence: **99.29%**
2102. **`crates/swc_ecma_transforms_module/tests/fixture/common/allow-top-level-this/false/output.umd.js`** -> AI Confidence: **99.29%**
2103. **`crates/swc_ecma_transforms_module/tests/fixture/common/allow-top-level-this/true/output.umd.js`** -> AI Confidence: **99.29%**
2104. **`crates/swc_ecma_transforms_module/tests/fixture/common/class-properties/private-method/output.umd.js`** -> AI Confidence: **99.29%**
2105. **`crates/swc_ecma_transforms_module/tests/fixture/common/class-properties/private/output.umd.js`** -> AI Confidence: **99.29%**
2106. **`crates/swc_ecma_transforms_module/tests/fixture/common/class-properties/public/output.umd.js`** -> AI Confidence: **99.29%**
2107. **`crates/swc_ecma_transforms_module/tests/fixture/common/class-property/output.umd.js`** -> AI Confidence: **99.29%**
2108. **`crates/swc_ecma_transforms_module/tests/fixture/common/custom/02/output.umd.js`** -> AI Confidence: **99.29%**
2109. **`crates/swc_ecma_transforms_module/tests/fixture/common/custom/named-define/output.umd.js`** -> AI Confidence: **99.29%**
2110. **`crates/swc_ecma_transforms_module/tests/fixture/common/custom/non-strict-mode/output.umd.js`** -> AI Confidence: **99.29%**
2111. **`crates/swc_ecma_transforms_module/tests/fixture/common/custom/usage/output.amd.js`** -> AI Confidence: **99.29%**
2112. **`crates/swc_ecma_transforms_module/tests/fixture/common/custom/usage/output.cjs`** -> AI Confidence: **99.29%**
2113. **`crates/swc_ecma_transforms_module/tests/fixture/common/custom/usage/output.umd.js`** -> AI Confidence: **99.29%**
2114. **`crates/swc_ecma_transforms_module/tests/fixture/common/export-interop-annotation/output.umd.js`** -> AI Confidence: **99.29%**
2115. **`crates/swc_ecma_transforms_module/tests/fixture/common/import-meta/output.amd.js`** -> AI Confidence: **99.29%**
2116. **`crates/swc_ecma_transforms_module/tests/fixture/common/import-meta/output.cjs`** -> AI Confidence: **99.29%**
2117. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop-module-string-names/export-from-string-as-string/output.umd.js`** -> AI Confidence: **99.29%**
2118. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop-module-string-names/export-from-string/output.umd.js`** -> AI Confidence: **99.29%**
2119. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop-module-string-names/export-from/output.umd.js`** -> AI Confidence: **99.29%**
2120. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop-module-string-names/import-named-string-can-be-identifier/output.umd.js`** -> AI Confidence: **99.29%**
2121. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop-module-string-names/import-named/output.amd.js`** -> AI Confidence: **99.29%**
2122. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop-module-string-names/import-named/output.cjs`** -> AI Confidence: **99.29%**
2123. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop-module-string-names/import-named/output.umd.js`** -> AI Confidence: **99.29%**
2124. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop-node/export-all/output.umd.js`** -> AI Confidence: **99.29%**
2125. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop-node/export-default-10/output.umd.js`** -> AI Confidence: **99.29%**
2126. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop-node/export-default-11/output.umd.js`** -> AI Confidence: **99.29%**
2127. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop-node/export-default-2/output.umd.js`** -> AI Confidence: **99.29%**
2128. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop-node/export-default-3/output.umd.js`** -> AI Confidence: **99.29%**
2129. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop-node/export-default-4/output.umd.js`** -> AI Confidence: **99.29%**
2130. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop-node/export-default-5/output.umd.js`** -> AI Confidence: **99.29%**
2131. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop-node/export-default-6/output.umd.js`** -> AI Confidence: **99.29%**
2132. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop-node/export-default-7/output.umd.js`** -> AI Confidence: **99.29%**
2133. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop-node/export-default-8/output.umd.js`** -> AI Confidence: **99.29%**
2134. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop-node/export-default-9/output.umd.js`** -> AI Confidence: **99.29%**
2135. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop-node/export-default/output.umd.js`** -> AI Confidence: **99.29%**
2136. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop-node/export-from-1/output.cjs`** -> AI Confidence: **99.29%**
2137. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop-node/export-from-1/output.umd.js`** -> AI Confidence: **99.29%**
2138. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop-node/export-from-2/output.umd.js`** -> AI Confidence: **99.29%**
2139. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop-node/export-from-4/output.umd.js`** -> AI Confidence: **99.29%**
2140. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop-node/export-from-5/output.umd.js`** -> AI Confidence: **99.29%**
2141. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop-node/export-from-6/output.umd.js`** -> AI Confidence: **99.29%**
2142. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop-node/export-from-7/output.umd.js`** -> AI Confidence: **99.29%**
2143. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop-node/export-named-1/output.umd.js`** -> AI Confidence: **99.29%**
2144. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop-node/export-named-3/output.umd.js`** -> AI Confidence: **99.29%**
2145. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop-node/export-named-4/output.umd.js`** -> AI Confidence: **99.29%**
2146. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop-node/imports-default/output.umd.js`** -> AI Confidence: **99.29%**
2147. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop-node/imports-glob/output.umd.js`** -> AI Confidence: **99.29%**
2148. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop-node/imports-mixing/output.amd.js`** -> AI Confidence: **99.29%**
2149. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop-node/imports-mixing/output.cjs`** -> AI Confidence: **99.29%**
2150. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop-node/imports-mixing/output.umd.js`** -> AI Confidence: **99.29%**
2151. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop-node/imports-named/output.umd.js`** -> AI Confidence: **99.29%**
2152. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop-node/imports-ordering/output.umd.js`** -> AI Confidence: **99.29%**
2153. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop-none/export-from/output.umd.js`** -> AI Confidence: **99.29%**
2154. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop-none/import-default-only/output.amd.js`** -> AI Confidence: **99.29%**
2155. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop-none/import-default-only/output.cjs`** -> AI Confidence: **99.29%**
2156. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop-none/import-default-only/output.umd.js`** -> AI Confidence: **99.29%**
2157. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop-none/import-wildcard/output.umd.js`** -> AI Confidence: **99.29%**
2158. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop/export-all/output.umd.js`** -> AI Confidence: **99.29%**
2159. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop/export-default-10/output.umd.js`** -> AI Confidence: **99.29%**
2160. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop/export-default-11/output.umd.js`** -> AI Confidence: **99.29%**
2161. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop/export-default-2/output.umd.js`** -> AI Confidence: **99.29%**
2162. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop/export-default-3/output.umd.js`** -> AI Confidence: **99.29%**
2163. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop/export-default-4/output.umd.js`** -> AI Confidence: **99.29%**
2164. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop/export-default-5/output.umd.js`** -> AI Confidence: **99.29%**
2165. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop/export-default-6/output.umd.js`** -> AI Confidence: **99.29%**
2166. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop/export-default-7/output.umd.js`** -> AI Confidence: **99.29%**
2167. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop/export-default-8/output.umd.js`** -> AI Confidence: **99.29%**
2168. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop/export-default-9/output.umd.js`** -> AI Confidence: **99.29%**
2169. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop/export-default/output.umd.js`** -> AI Confidence: **99.29%**
2170. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop/export-from-1/output.umd.js`** -> AI Confidence: **99.29%**
2171. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop/export-from-2/output.umd.js`** -> AI Confidence: **99.29%**
2172. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop/export-from-4/output.umd.js`** -> AI Confidence: **99.29%**
2173. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop/export-from-5/output.umd.js`** -> AI Confidence: **99.29%**
2174. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop/export-from-6/output.umd.js`** -> AI Confidence: **99.29%**
2175. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop/export-from-7/output.umd.js`** -> AI Confidence: **99.29%**
2176. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop/export-named-1/output.umd.js`** -> AI Confidence: **99.29%**
2177. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop/export-named-3/output.umd.js`** -> AI Confidence: **99.29%**
2178. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop/export-named-4/output.umd.js`** -> AI Confidence: **99.29%**
2179. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop/imports-call/output.amd.js`** -> AI Confidence: **99.29%**
2180. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop/imports-call/output.cjs`** -> AI Confidence: **99.29%**
2181. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop/imports-call/output.umd.js`** -> AI Confidence: **99.29%**
2182. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop/imports-default/output.amd.js`** -> AI Confidence: **99.29%**
2183. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop/imports-default/output.cjs`** -> AI Confidence: **99.29%**
2184. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop/imports-default/output.umd.js`** -> AI Confidence: **99.29%**
2185. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop/imports-glob/output.umd.js`** -> AI Confidence: **99.29%**
2186. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop/imports-mixing/output.amd.js`** -> AI Confidence: **99.29%**
2187. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop/imports-mixing/output.cjs`** -> AI Confidence: **99.29%**
2188. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop/imports-mixing/output.umd.js`** -> AI Confidence: **99.29%**
2189. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop/imports-named/output.umd.js`** -> AI Confidence: **99.29%**
2190. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop/imports-ordering/output.umd.js`** -> AI Confidence: **99.29%**
2191. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-1018/1/output.umd.js`** -> AI Confidence: **99.29%**
2192. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-1043/1/output.umd.js`** -> AI Confidence: **99.29%**
2193. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-1043/2/output.umd.js`** -> AI Confidence: **99.29%**
2194. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-1201/1/output.umd.js`** -> AI Confidence: **99.29%**
2195. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-1213/output.umd.js`** -> AI Confidence: **99.29%**
2196. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-1423/1/output.umd.js`** -> AI Confidence: **99.29%**
2197. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-1480/1/output.umd.js`** -> AI Confidence: **99.29%**
2198. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-1480/2/output.umd.js`** -> AI Confidence: **99.29%**
2199. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-1568/1/output.umd.js`** -> AI Confidence: **99.29%**
2200. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-1568/2/output.umd.js`** -> AI Confidence: **99.29%**
2201. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-1588/1/output.umd.js`** -> AI Confidence: **99.29%**
2202. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-1757/1/output.umd.js`** -> AI Confidence: **99.29%**
2203. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-176/output.umd.js`** -> AI Confidence: **99.29%**
2204. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-1780/1/output.umd.js`** -> AI Confidence: **99.29%**
2205. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-1786/1/output.umd.js`** -> AI Confidence: **99.29%**
2206. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-1787/1/output.amd.js`** -> AI Confidence: **99.29%**
2207. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-1787/1/output.cjs`** -> AI Confidence: **99.29%**
2208. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-1787/1/output.umd.js`** -> AI Confidence: **99.29%**
2209. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-1799/1/output.umd.js`** -> AI Confidence: **99.29%**
2210. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-1799/2/output.umd.js`** -> AI Confidence: **99.29%**
2211. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-2101/1/output.umd.js`** -> AI Confidence: **99.29%**
2212. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-2101/2/output.umd.js`** -> AI Confidence: **99.29%**
2213. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-2344/3/output.umd.js`** -> AI Confidence: **99.29%**
2214. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-235/output.umd.js`** -> AI Confidence: **99.29%**
2215. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-2548/case1/output.umd.js`** -> AI Confidence: **99.29%**
2216. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-2548/case2/output.umd.js`** -> AI Confidence: **99.29%**
2217. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-3246/1/output.umd.js`** -> AI Confidence: **99.29%**
2218. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-3246/2/output.umd.js`** -> AI Confidence: **99.29%**
2219. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-326/output.amd.js`** -> AI Confidence: **99.29%**
2220. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-326/output.cjs`** -> AI Confidence: **99.29%**
2221. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-326/output.umd.js`** -> AI Confidence: **99.29%**
2222. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-332/output.umd.js`** -> AI Confidence: **99.29%**
2223. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-335/output.amd.js`** -> AI Confidence: **99.29%**
2224. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-335/output.cjs`** -> AI Confidence: **99.29%**
2225. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-335/output.umd.js`** -> AI Confidence: **99.29%**
2226. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-3438/output.umd.js`** -> AI Confidence: **99.29%**
2227. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-3439/1/output.umd.js`** -> AI Confidence: **99.29%**
2228. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-3439/4/output.umd.js`** -> AI Confidence: **99.29%**
2229. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-389/1/output.amd.js`** -> AI Confidence: **99.29%**
2230. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-389/1/output.cjs`** -> AI Confidence: **99.29%**
2231. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-389/1/output.umd.js`** -> AI Confidence: **99.29%**
2232. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-389/2/output.amd.js`** -> AI Confidence: **99.29%**
2233. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-389/2/output.cjs`** -> AI Confidence: **99.29%**
2234. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-389/2/output.umd.js`** -> AI Confidence: **99.29%**
2235. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-3898/1/output.umd.js`** -> AI Confidence: **99.29%**
2236. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-396/1/output.umd.js`** -> AI Confidence: **99.29%**
2237. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-396/2/output.umd.js`** -> AI Confidence: **99.29%**
2238. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-4064/output.umd.js`** -> AI Confidence: **99.29%**
2239. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-4313/1/output.umd.js`** -> AI Confidence: **99.29%**
2240. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-456/1/output.umd.js`** -> AI Confidence: **99.29%**
2241. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-4700/1/output.umd.js`** -> AI Confidence: **99.29%**
2242. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-4718/1/output.umd.js`** -> AI Confidence: **99.29%**
2243. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-4798/1/output.umd.js`** -> AI Confidence: **99.29%**
2244. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-4799/output.umd.js`** -> AI Confidence: **99.29%**
2245. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-4984/1/output.umd.js`** -> AI Confidence: **99.29%**
2246. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-5063/1/output.umd.js`** -> AI Confidence: **99.29%**
2247. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-5157/2/output.umd.js`** -> AI Confidence: **99.29%**
2248. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-578/2/output.umd.js`** -> AI Confidence: **99.29%**
2249. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-605/output.umd.js`** -> AI Confidence: **99.29%**
2250. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-7180/output.cjs`** -> AI Confidence: **99.29%**
2251. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-7180/output.umd.js`** -> AI Confidence: **99.29%**
2252. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-724/output.umd.js`** -> AI Confidence: **99.29%**
2253. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-7315/output.umd.js`** -> AI Confidence: **99.29%**
2254. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-763/output.umd.js`** -> AI Confidence: **99.29%**
2255. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-8047/output.umd.js`** -> AI Confidence: **99.29%**
2256. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-831/2/output.umd.js`** -> AI Confidence: **99.29%**
2257. **`crates/swc_ecma_transforms_module/tests/fixture/common/lazy/computed-prop-name/output.umd.js`** -> AI Confidence: **99.29%**
2258. **`crates/swc_ecma_transforms_module/tests/fixture/common/lazy/export-named/output.umd.js`** -> AI Confidence: **99.29%**
2259. **`crates/swc_ecma_transforms_module/tests/fixture/common/lazy/import-all-from-object-config/output.umd.js`** -> AI Confidence: **99.29%**
2260. **`crates/swc_ecma_transforms_module/tests/fixture/common/lazy/issue-3081/1/output.umd.js`** -> AI Confidence: **99.29%**
2261. **`crates/swc_ecma_transforms_module/tests/fixture/common/lazy/issue-3081/2/output.umd.js`** -> AI Confidence: **99.29%**
2262. **`crates/swc_ecma_transforms_module/tests/fixture/common/lazy/local-import-default/output.amd.js`** -> AI Confidence: **99.29%**
2263. **`crates/swc_ecma_transforms_module/tests/fixture/common/lazy/local-import-default/output.cjs`** -> AI Confidence: **99.29%**
2264. **`crates/swc_ecma_transforms_module/tests/fixture/common/lazy/local-import-default/output.umd.js`** -> AI Confidence: **99.29%**
2265. **`crates/swc_ecma_transforms_module/tests/fixture/common/lazy/local-import-named/output.umd.js`** -> AI Confidence: **99.29%**
2266. **`crates/swc_ecma_transforms_module/tests/fixture/common/lazy/local-import-namespace/output.umd.js`** -> AI Confidence: **99.29%**
2267. **`crates/swc_ecma_transforms_module/tests/fixture/common/lazy/local-reexport-all/output.umd.js`** -> AI Confidence: **99.29%**
2268. **`crates/swc_ecma_transforms_module/tests/fixture/common/lazy/local-reexport-default/output.umd.js`** -> AI Confidence: **99.29%**
2269. **`crates/swc_ecma_transforms_module/tests/fixture/common/lazy/local-reexport-named/output.umd.js`** -> AI Confidence: **99.29%**
2270. **`crates/swc_ecma_transforms_module/tests/fixture/common/lazy/local-reexport-namespace/output.umd.js`** -> AI Confidence: **99.29%**
2271. **`crates/swc_ecma_transforms_module/tests/fixture/common/lazy/local-sideeffect/output.umd.js`** -> AI Confidence: **99.29%**
2272. **`crates/swc_ecma_transforms_module/tests/fixture/common/lazy/whitelist/import-default/output.amd.js`** -> AI Confidence: **99.29%**
2273. **`crates/swc_ecma_transforms_module/tests/fixture/common/lazy/whitelist/import-default/output.umd.js`** -> AI Confidence: **99.29%**
2274. **`crates/swc_ecma_transforms_module/tests/fixture/common/lazy/whitelist/import-named/output.umd.js`** -> AI Confidence: **99.29%**
2275. **`crates/swc_ecma_transforms_module/tests/fixture/common/lazy/whitelist/import-namespace/output.umd.js`** -> AI Confidence: **99.29%**
2276. **`crates/swc_ecma_transforms_module/tests/fixture/common/lazy/whitelist/reexport-all/output.umd.js`** -> AI Confidence: **99.29%**
2277. **`crates/swc_ecma_transforms_module/tests/fixture/common/lazy/whitelist/reexport-default/output.umd.js`** -> AI Confidence: **99.29%**
2278. **`crates/swc_ecma_transforms_module/tests/fixture/common/lazy/whitelist/sideeffect/output.umd.js`** -> AI Confidence: **99.29%**
2279. **`crates/swc_ecma_transforms_module/tests/fixture/common/misc/class-static-block/output.umd.js`** -> AI Confidence: **99.29%**
2280. **`crates/swc_ecma_transforms_module/tests/fixture/common/misc/copy-getters-setters/output.umd.js`** -> AI Confidence: **99.29%**
2281. **`crates/swc_ecma_transforms_module/tests/fixture/common/misc/import-const-throw/output.umd.js`** -> AI Confidence: **99.29%**
2282. **`crates/swc_ecma_transforms_module/tests/fixture/common/misc/undefined-this-arrow-function/output.umd.js`** -> AI Confidence: **99.29%**
2283. **`crates/swc_ecma_transforms_module/tests/fixture/common/misc/undefined-this-computed-class-method-1/output.umd.js`** -> AI Confidence: **99.29%**
2284. **`crates/swc_ecma_transforms_module/tests/fixture/common/misc/undefined-this-computed-class-method-2/output.umd.js`** -> AI Confidence: **99.29%**
2285. **`crates/swc_ecma_transforms_module/tests/fixture/common/misc/undefined-this-computed-class-method-3/output.umd.js`** -> AI Confidence: **99.29%**
2286. **`crates/swc_ecma_transforms_module/tests/fixture/common/misc/undefined-this-computed-class-property-name/output.umd.js`** -> AI Confidence: **99.29%**
2287. **`crates/swc_ecma_transforms_module/tests/fixture/common/misc/undefined-this-root-call/output.umd.js`** -> AI Confidence: **99.29%**
2288. **`crates/swc_ecma_transforms_module/tests/fixture/common/misc/undefined-this-root-declaration/output.umd.js`** -> AI Confidence: **99.29%**
2289. **`crates/swc_ecma_transforms_module/tests/fixture/common/misc/undefined-this-root-reference/output.umd.js`** -> AI Confidence: **99.29%**
2290. **`crates/swc_ecma_transforms_module/tests/fixture/common/regression/4209/output.umd.js`** -> AI Confidence: **99.29%**
2291. **`crates/swc_ecma_transforms_module/tests/fixture/common/regression/6647/output.amd.js`** -> AI Confidence: **99.29%**
2292. **`crates/swc_ecma_transforms_module/tests/fixture/common/regression/6647/output.cjs`** -> AI Confidence: **99.29%**
2293. **`crates/swc_ecma_transforms_module/tests/fixture/common/regression/6647/output.umd.js`** -> AI Confidence: **99.29%**
2294. **`crates/swc_ecma_transforms_module/tests/fixture/common/regression/t-7178/output.amd.js`** -> AI Confidence: **99.29%**
2295. **`crates/swc_ecma_transforms_module/tests/fixture/common/regression/t-7178/output.cjs`** -> AI Confidence: **99.29%**
2296. **`crates/swc_ecma_transforms_module/tests/fixture/common/regression/t-7178/output.umd.js`** -> AI Confidence: **99.29%**
2297. **`crates/swc_ecma_transforms_module/tests/fixture/common/strict/export-1/output.umd.js`** -> AI Confidence: **99.29%**
2298. **`crates/swc_ecma_transforms_module/tests/fixture/common/strict/export-2/output.umd.js`** -> AI Confidence: **99.29%**
2299. **`crates/swc_ecma_transforms_module/tests/fixture/common/strict/export-3/output.umd.js`** -> AI Confidence: **99.29%**
2300. **`crates/swc_ecma_transforms_module/tests/fixture/common/strict/export-4/output.umd.js`** -> AI Confidence: **99.29%**
2301. **`crates/swc_ecma_transforms_module/tests/fixture/common/strict/import-wildcard/output.umd.js`** -> AI Confidence: **99.29%**
2302. **`crates/swc_ecma_transforms_module/tests/fixture/common/strict/import/output.amd.js`** -> AI Confidence: **99.29%**
2303. **`crates/swc_ecma_transforms_module/tests/fixture/common/strict/import/output.cjs`** -> AI Confidence: **99.29%**
2304. **`crates/swc_ecma_transforms_module/tests/fixture/common/strict/import/output.umd.js`** -> AI Confidence: **99.29%**
2305. **`crates/swc_ecma_transforms_optimization/tests/__swc_snapshots__/src/inline_globals.rs/globals_simple.js`** -> AI Confidence: **99.29%**
2306. **`crates/swc_ecma_transforms_optimization/tests/__swc_snapshots__/src/inline_globals.rs/issue_215.js`** -> AI Confidence: **99.29%**
2307. **`crates/swc_ecma_transforms_optimization/tests/__swc_snapshots__/src/inline_globals.rs/node_env.js`** -> AI Confidence: **99.29%**
2308. **`crates/swc_ecma_transforms_optimization/tests/__swc_snapshots__/src/inline_globals.rs/non_global.js`** -> AI Confidence: **99.29%**
2309. **`crates/swc_ecma_transforms_optimization/tests/__swc_snapshots__/tests/const_modules.rs/imports_hoisted.js`** -> AI Confidence: **99.29%**
2310. **`crates/swc_ecma_transforms_optimization/tests/__swc_snapshots__/tests/const_modules.rs/simple_flags.js`** -> AI Confidence: **99.29%**
2311. **`crates/swc_ecma_transforms_optimization/tests/__swc_snapshots__/tests/remove_imports_with_side_effects.rs/single_pass.js`** -> AI Confidence: **99.29%**
2312. **`crates/swc_ecma_transforms_optimization/tests/__swc_snapshots__/tests/simplify_dce.rs/deno_9121_3.js`** -> AI Confidence: **99.29%**
2313. **`crates/swc_ecma_transforms_optimization/tests/__swc_snapshots__/tests/simplify_dce.rs/noop_2.js`** -> AI Confidence: **99.29%**
2314. **`crates/swc_ecma_transforms_optimization/tests/__swc_snapshots__/tests/simplify_dce.rs/noop_3.js`** -> AI Confidence: **99.29%**
2315. **`crates/swc_ecma_transforms_optimization/tests/__swc_snapshots__/tests/simplify_dce.rs/single_pass.js`** -> AI Confidence: **99.29%**
2316. **`crates/swc_ecma_transforms_optimization/tests/__swc_snapshots__/tests/simplify_inlining.rs/closure_compiler_1234.js`** -> AI Confidence: **99.29%**
2317. **`crates/swc_ecma_transforms_optimization/tests/__swc_snapshots__/tests/simplify_inlining.rs/const_1.js`** -> AI Confidence: **99.29%**
2318. **`crates/swc_ecma_transforms_optimization/tests/expr-simplifier/issue-1688/case1/input.js`** -> AI Confidence: **99.29%**
2319. **`crates/swc_ecma_transforms_optimization/tests/expr-simplifier/issue-1688/case1/output.js`** -> AI Confidence: **99.29%**
2320. **`crates/swc_ecma_transforms_optimization/tests/expr-simplifier/issue-1688/case2/input.js`** -> AI Confidence: **99.29%**
2321. **`crates/swc_ecma_transforms_optimization/tests/expr-simplifier/issue-1688/case2/output.js`** -> AI Confidence: **99.29%**
2322. **`crates/swc_ecma_transforms_optimization/tests/expr-simplifier/issue-1688/case3/input.js`** -> AI Confidence: **99.29%**
2323. **`crates/swc_ecma_transforms_optimization/tests/expr-simplifier/issue-1688/case3/output.js`** -> AI Confidence: **99.29%**
2324. **`crates/swc_ecma_transforms_proposal/tests/explicit-resource-management/exec-sync/multiple-dispose-errors-chain.js`** -> AI Confidence: **99.29%**
2325. **`crates/swc_ecma_transforms_proposal/tests/explicit-resource-management/source-maps/block/output.js`** -> AI Confidence: **99.29%**
2326. **`crates/swc_ecma_transforms_proposal/tests/explicit-resource-management/source-maps/for-of/input.js`** -> AI Confidence: **99.29%**
2327. **`crates/swc_ecma_transforms_proposal/tests/explicit-resource-management/source-maps/for-of/output.js`** -> AI Confidence: **99.29%**
2328. **`crates/swc_ecma_transforms_proposal/tests/explicit-resource-management/source-maps/switch/input.js`** -> AI Confidence: **99.29%**
2329. **`crates/swc_ecma_transforms_proposal/tests/explicit-resource-management/source-maps/switch/output.js`** -> AI Confidence: **99.29%**
2330. **`crates/swc_ecma_transforms_proposal/tests/explicit-resource-management/source-maps/top-level/output.mjs`** -> AI Confidence: **99.29%**
2331. **`crates/swc_ecma_transforms_proposal/tests/explicit-resource-management/transform-await/mixed/output.js`** -> AI Confidence: **99.29%**
2332. **`crates/swc_ecma_transforms_proposal/tests/explicit-resource-management/transform-await/only-using-await/output.js`** -> AI Confidence: **99.29%**
2333. **`crates/swc_ecma_transforms_proposal/tests/explicit-resource-management/transform-await/switch/output.js`** -> AI Confidence: **99.29%**
2334. **`crates/swc_ecma_transforms_proposal/tests/explicit-resource-management/transform-await/switch/output.mjs`** -> AI Confidence: **99.29%**
2335. **`crates/swc_ecma_transforms_proposal/tests/explicit-resource-management/transform-sync/bare-block/output.js`** -> AI Confidence: **99.29%**
2336. **`crates/swc_ecma_transforms_proposal/tests/explicit-resource-management/transform-sync/for-await-head/output.js`** -> AI Confidence: **99.29%**
2337. **`crates/swc_ecma_transforms_proposal/tests/explicit-resource-management/transform-sync/for-head/input.js`** -> AI Confidence: **99.29%**
2338. **`crates/swc_ecma_transforms_proposal/tests/explicit-resource-management/transform-sync/for-head/output.js`** -> AI Confidence: **99.29%**
2339. **`crates/swc_ecma_transforms_proposal/tests/explicit-resource-management/transform-sync/if-body/input.js`** -> AI Confidence: **99.29%**
2340. **`crates/swc_ecma_transforms_proposal/tests/explicit-resource-management/transform-sync/if-body/output.js`** -> AI Confidence: **99.29%**
2341. **`crates/swc_ecma_transforms_proposal/tests/explicit-resource-management/transform-sync/multiple-nested/output.js`** -> AI Confidence: **99.29%**
2342. **`crates/swc_ecma_transforms_proposal/tests/explicit-resource-management/transform-sync/multiple-same-level/output.js`** -> AI Confidence: **99.29%**
2343. **`crates/swc_ecma_transforms_proposal/tests/explicit-resource-management/transform-sync/switch/input.js`** -> AI Confidence: **99.29%**
2344. **`crates/swc_ecma_transforms_proposal/tests/explicit-resource-management/transform-sync/switch/output.js`** -> AI Confidence: **99.29%**
2345. **`crates/swc_ecma_transforms_react/tests/jsx/fixture/issue-1446/input.js`** -> AI Confidence: **99.29%**
2346. **`crates/swc_ecma_transforms_react/tests/jsx/fixture/issue-1446/output.mjs`** -> AI Confidence: **99.29%**
2347. **`crates/swc_ecma_transforms_typescript/tests/__swc_snapshots__/tests/strip.rs/issue_468_1.js`** -> AI Confidence: **99.29%**
2348. **`crates/swc_ecma_transforms_typescript/tests/__swc_snapshots__/tests/strip.rs/issue_468_2.js`** -> AI Confidence: **99.29%**
2349. **`crates/swc_ecma_transforms_typescript/tests/__swc_snapshots__/tests/strip.rs/issue_468_3.js`** -> AI Confidence: **99.29%**
2350. **`crates/swc_ecma_transforms_typescript/tests/__swc_snapshots__/tests/strip.rs/issue_468_7.js`** -> AI Confidence: **99.29%**
2351. **`crates/swc_ecma_transforms_typescript/tests/fixture/issue-1653/output.js`** -> AI Confidence: **99.29%**
2352. **`crates/swc_es_minifier/tests/fixtures/simplify-branches/input.js`** -> AI Confidence: **99.29%**
2353. **`crates/swc_es_parser/benches/files/yui-3.12.0.js`** -> AI Confidence: **99.29%**
2354. **`crates/swc_es_semantics/tests/fixtures/cfg/for_in_of/input.js`** -> AI Confidence: **99.29%**
2355. **`crates/swc_es_semantics/tests/fixtures/cfg/switch_fallthrough/input.js`** -> AI Confidence: **99.29%**
2356. **`crates/swc_es_semantics/tests/fixtures/cfg/try_catch_finally/input.js`** -> AI Confidence: **99.29%**
2357. **`crates/swc_es_transforms/tests/fixtures/lower-logical/input.js`** -> AI Confidence: **99.29%**
2358. **`crates/swc_es_transforms/tests/fixtures/lower-logical/output.js`** -> AI Confidence: **99.29%**
2359. **`crates/swc_es_transforms/tests/fixtures/lower-nullish/input.js`** -> AI Confidence: **99.29%**
2360. **`crates/swc_es_transforms/tests/fixtures/lower-nullish/output.js`** -> AI Confidence: **99.29%**
2361. **`crates/swc_node_bundler/tests/pass/cjs/conditional/input/entry.js`** -> AI Confidence: **99.29%**
2362. **`crates/swc_node_bundler/tests/pass/cjs/issue-967-recursive-require/input/a-a-a.js`** -> AI Confidence: **99.29%**
2363. **`crates/swc_node_bundler/tests/pass/cjs/issue-967-recursive-require/input/a-b.js`** -> AI Confidence: **99.29%**
2364. **`crates/swc_ts_fast_strip/tests/fixture/single-ts-stmt.js`** -> AI Confidence: **99.29%**
2365. **`crates/swc_ts_fast_strip/tests/fixture/single-ts-stmt.transform.js`** -> AI Confidence: **99.29%**
2366. **`packages/core/scripts/copy-readme.js`** -> AI Confidence: **99.29%**
2367. **`packages/helpers/esm/_ts_generator.js`** -> AI Confidence: **99.29%**
2368. **`scripts/validate-binary.js`** -> AI Confidence: **99.29%**
2369. **`crates/swc_ecma_minifier/scripts/_/notify.sh`** -> AI Confidence: **99.29%**
2370. **`crates/swc_ecma_minifier/scripts/_/postpone/ask-file.sh`** -> AI Confidence: **99.29%**
2371. **`crates/swc_estree_compat/scripts/update.sh`** -> AI Confidence: **99.29%**
2372. **`scripts/bench/build-crate.sh`** -> AI Confidence: **99.29%**
2373. **`scripts/cli_upload_gh_release.sh`** -> AI Confidence: **99.29%**
2374. **`crates/swc_bundler/tests/deno-exec/deno-8224/haystack-core/input/core/TrioReader.ts`** -> AI Confidence: **99.24%**
2375. **`bindings/binding_core_node/src/transform.rs`** -> AI Confidence: **99.24%**
2376. **`bindings/binding_html_wasm/src/lib.rs`** -> AI Confidence: **99.24%**
2377. **`bindings/binding_typescript_wasm/src/error_reporter.rs`** -> AI Confidence: **99.24%**
2378. **`crates/ast_node/src/encoding/decode.rs`** -> AI Confidence: **99.24%**
2379. **`crates/dbg-swc/src/es/minifier/compare.rs`** -> AI Confidence: **99.24%**
2380. **`crates/dbg-swc/src/es/minifier/reduce.rs`** -> AI Confidence: **99.24%**
2381. **`crates/dbg-swc/src/main.rs`** -> AI Confidence: **99.24%**
2382. **`crates/dbg-swc/src/util/minifier.rs`** -> AI Confidence: **99.24%**
2383. **`crates/hstr/src/global_store.rs`** -> AI Confidence: **99.24%**
2384. **`crates/jsdoc/src/lib.rs`** -> AI Confidence: **99.24%**
2385. **`crates/swc_cli_impl/src/commands/compile.rs`** -> AI Confidence: **99.24%**
2386. **`crates/swc_cli_impl/src/commands/plugin.rs`** -> AI Confidence: **99.24%**
2387. **`crates/swc_common/src/comments.rs`** -> AI Confidence: **99.24%**
2388. **`crates/swc_css_codegen/src/writer/basic.rs`** -> AI Confidence: **99.24%**
2389. **`crates/swc_css_compat/src/compiler/color_space_separated_parameters.rs`** -> AI Confidence: **99.24%**
2390. **`crates/swc_css_compat/src/compiler/legacy_rgb_and_hsl.rs`** -> AI Confidence: **99.24%**
2391. **`crates/swc_css_compat/src/compiler/media_query_ranges.rs`** -> AI Confidence: **99.24%**
2392. **`crates/swc_css_lints/src/rules/font_family_no_duplicate_names.rs`** -> AI Confidence: **99.24%**
2393. **`crates/swc_css_lints/src/rules/no_invalid_position_at_import_rule.rs`** -> AI Confidence: **99.24%**
2394. **`crates/swc_css_minifier/src/compressor/calc_sum.rs`** -> AI Confidence: **99.24%**
2395. **`crates/swc_css_modules/src/imports.rs`** -> AI Confidence: **99.24%**
2396. **`crates/swc_css_parser/src/parser/selectors/mod.rs`** -> AI Confidence: **99.24%**
2397. **`crates/swc_css_parser/src/parser/util.rs`** -> AI Confidence: **99.24%**
2398. **`crates/swc_css_utils/src/lib.rs`** -> AI Confidence: **99.24%**
2399. **`crates/swc_ecma_ast/src/ident.rs`** -> AI Confidence: **99.24%**
2400. **`crates/swc_ecma_ast/src/lit.rs`** -> AI Confidence: **99.24%**
2401. **`crates/swc_ecma_compat_es2015/src/spread.rs`** -> AI Confidence: **99.24%**
2402. **`crates/swc_ecma_compat_es2015/src/template_literal.rs`** -> AI Confidence: **99.24%**
2403. **`crates/swc_ecma_ext_transforms/src/jest.rs`** -> AI Confidence: **99.24%**
2404. **`crates/swc_ecma_lexer/examples/lexer.rs`** -> AI Confidence: **99.24%**
2405. **`crates/swc_ecma_lexer/src/token.rs`** -> AI Confidence: **99.24%**
2406. **`crates/swc_ecma_lints/src/rules/no_alert.rs`** -> AI Confidence: **99.24%**
2407. **`crates/swc_ecma_lints/src/rules/no_console.rs`** -> AI Confidence: **99.24%**
2408. **`crates/swc_ecma_lints/src/rules/no_empty_function.rs`** -> AI Confidence: **99.24%**
2409. **`crates/swc_ecma_lints/src/rules/no_param_reassign.rs`** -> AI Confidence: **99.24%**
2410. **`crates/swc_ecma_lints/src/rules/prefer_const.rs`** -> AI Confidence: **99.24%**
2411. **`crates/swc_ecma_lints/src/rules/prefer_object_spread.rs`** -> AI Confidence: **99.24%**
2412. **`crates/swc_ecma_lints/src/rules/prefer_regex_literals.rs`** -> AI Confidence: **99.24%**
2413. **`crates/swc_ecma_lints/src/rules/radix.rs`** -> AI Confidence: **99.24%**
2414. **`crates/swc_ecma_lints/src/rules/utils.rs`** -> AI Confidence: **99.24%**
2415. **`crates/swc_ecma_lints/src/rules/valid_typeof.rs`** -> AI Confidence: **99.24%**
2416. **`crates/swc_ecma_lints/src/rules/yoda.rs`** -> AI Confidence: **99.24%**
2417. **`crates/swc_ecma_loader/src/resolvers/node.rs`** -> AI Confidence: **99.24%**
2418. **`crates/swc_ecma_minifier/src/compress/optimize/bools.rs`** -> AI Confidence: **99.24%**
2419. **`crates/swc_ecma_minifier/src/compress/optimize/if_return.rs`** -> AI Confidence: **99.24%**
2420. **`crates/swc_ecma_minifier/src/compress/optimize/iife.rs`** -> AI Confidence: **99.24%**
2421. **`crates/swc_ecma_minifier/src/compress/optimize/strings.rs`** -> AI Confidence: **99.24%**
2422. **`crates/swc_ecma_minifier/src/compress/pure/conds.rs`** -> AI Confidence: **99.24%**
2423. **`crates/swc_ecma_minifier/src/compress/pure/evaluate.rs`** -> AI Confidence: **99.24%**
2424. **`crates/swc_ecma_minifier/src/compress/pure/numbers.rs`** -> AI Confidence: **99.24%**
2425. **`crates/swc_ecma_minifier/src/compress/pure/switches.rs`** -> AI Confidence: **99.24%**
2426. **`crates/swc_ecma_minifier/src/eval.rs`** -> AI Confidence: **99.24%**
2427. **`crates/swc_ecma_minifier/src/metadata/mod.rs`** -> AI Confidence: **99.24%**
2428. **`crates/swc_ecma_minifier/src/option/terser.rs`** -> AI Confidence: **99.24%**
2429. **`crates/swc_ecma_parser/src/lexer/token.rs`** -> AI Confidence: **99.24%**
2430. **`crates/swc_ecma_parser/src/parser/stmt.rs`** -> AI Confidence: **99.24%**
2431. **`crates/swc_ecma_parser/tests/errors.rs`** -> AI Confidence: **99.24%**
2432. **`crates/swc_ecma_preset_env/src/corejs2/entry.rs`** -> AI Confidence: **99.24%**
2433. **`crates/swc_ecma_preset_env/src/corejs2/mod.rs`** -> AI Confidence: **99.24%**
2434. **`crates/swc_ecma_preset_env/src/corejs3/usage.rs`** -> AI Confidence: **99.24%**
2435. **`crates/swc_ecma_transformer/src/regexp.rs`** -> AI Confidence: **99.24%**
2436. **`crates/swc_ecma_transforms_base/src/fixer.rs`** -> AI Confidence: **99.24%**
2437. **`crates/swc_ecma_transforms_classes/src/super_field.rs`** -> AI Confidence: **99.24%**
2438. **`crates/swc_ecma_transforms_compat/tests/es2015_block_scoping.rs`** -> AI Confidence: **99.24%**
2439. **`crates/swc_ecma_transforms_module/src/import_analysis.rs`** -> AI Confidence: **99.24%**
2440. **`crates/swc_ecma_transforms_module/src/module_decl_strip.rs`** -> AI Confidence: **99.24%**
2441. **`crates/swc_ecma_transforms_module/src/path.rs`** -> AI Confidence: **99.24%**
2442. **`crates/swc_ecma_transforms_module/src/system_js.rs`** -> AI Confidence: **99.24%**
2443. **`crates/swc_ecma_transforms_optimization/src/simplify/dce/mod.rs`** -> AI Confidence: **99.24%**
2444. **`crates/swc_ecma_transforms_proposal/src/decorator_impl.rs`** -> AI Confidence: **99.24%**
2445. **`crates/swc_ecma_transforms_proposal/src/decorators/legacy/metadata.rs`** -> AI Confidence: **99.24%**
2446. **`crates/swc_ecma_transforms_react/src/jsx/mod.rs`** -> AI Confidence: **99.24%**
2447. **`crates/swc_ecma_transforms_react/src/refresh/util.rs`** -> AI Confidence: **99.24%**
2448. **`crates/swc_ecma_utils/src/lib.rs`** -> AI Confidence: **99.24%**
2449. **`crates/swc_es_minifier/src/analysis.rs`** -> AI Confidence: **99.24%**
2450. **`crates/swc_es_minifier/src/rewrite.rs`** -> AI Confidence: **99.24%**
2451. **`crates/swc_es_parser/src/lexer/whitespace.rs`** -> AI Confidence: **99.24%**
2452. **`crates/swc_es_parser/tests/common/ecma_reuse.rs`** -> AI Confidence: **99.24%**
2453. **`crates/swc_es_semantics/src/cfg.rs`** -> AI Confidence: **99.24%**
2454. **`crates/swc_es_transforms/src/analysis.rs`** -> AI Confidence: **99.24%**
2455. **`crates/swc_estree_ast/src/class.rs`** -> AI Confidence: **99.24%**
2456. **`crates/swc_estree_ast/src/object.rs`** -> AI Confidence: **99.24%**
2457. **`crates/swc_estree_compat/src/babelify/expr.rs`** -> AI Confidence: **99.24%**
2458. **`crates/swc_estree_compat/src/babelify/jsx.rs`** -> AI Confidence: **99.24%**
2459. **`crates/swc_estree_compat/src/babelify/module.rs`** -> AI Confidence: **99.24%**
2460. **`crates/swc_estree_compat/src/babelify/module_decl.rs`** -> AI Confidence: **99.24%**
2461. **`crates/swc_estree_compat/src/babelify/typescript.rs`** -> AI Confidence: **99.24%**
2462. **`crates/swc_estree_compat/src/swcify/class.rs`** -> AI Confidence: **99.24%**
2463. **`crates/swc_estree_compat/src/swcify/expr.rs`** -> AI Confidence: **99.24%**
2464. **`crates/swc_estree_compat/src/swcify/pat.rs`** -> AI Confidence: **99.24%**
2465. **`crates/swc_estree_compat/tests/convert.rs`** -> AI Confidence: **99.24%**
2466. **`crates/swc_html_parser/src/lexer/mod.rs`** -> AI Confidence: **99.24%**
2467. **`crates/swc_ts_fast_strip/src/lib.rs`** -> AI Confidence: **99.24%**
2468. **`crates/swc_ts_fast_strip_binding/src/error_reporter.rs`** -> AI Confidence: **99.24%**
2469. **`crates/swc_typescript/src/fast_dts/function.rs`** -> AI Confidence: **99.24%**
2470. **`crates/swc_typescript/src/fast_dts/util/expando_function_collector.rs`** -> AI Confidence: **99.24%**
2471. **`crates/swc_xml_codegen/src/lib.rs`** -> AI Confidence: **99.24%**
2472. **`crates/swc_xml_parser/src/lexer/mod.rs`** -> AI Confidence: **99.24%**
2473. **`crates/testing_macros/src/fixture.rs`** -> AI Confidence: **99.24%**
2474. **`xtask/src/npm/nightly.rs`** -> AI Confidence: **99.24%**
2475. **`crates/swc/tests/vercel/full/react-autowhatever/2/output/index.js`** -> AI Confidence: **99.24%**
2476. **`packages/core/src/postinstall.ts`** -> AI Confidence: **99.23%**
2477. **`crates/ast_node/src/encoding/encode.rs`** -> AI Confidence: **99.23%**
2478. **`crates/swc_bundler/src/modules/sort/graph.rs`** -> AI Confidence: **99.23%**
2479. **`crates/swc_css_lints/src/rules/color_hex_length.rs`** -> AI Confidence: **99.23%**
2480. **`crates/swc_ecma_compat_es2022/src/class_properties/class_name_tdz.rs`** -> AI Confidence: **99.23%**
2481. **`crates/swc_ecma_minifier/src/compress/pure/arrows.rs`** -> AI Confidence: **99.23%**
2482. **`crates/swc_ecma_minifier/src/compress/pure/if_return.rs`** -> AI Confidence: **99.23%**
2483. **`crates/swc_ecma_minifier/src/compress/pure/sequences.rs`** -> AI Confidence: **99.23%**
2484. **`crates/swc_ecma_minifier/src/pass/global_defs.rs`** -> AI Confidence: **99.23%**
2485. **`crates/swc_ecma_utils/src/str.rs`** -> AI Confidence: **99.23%**
2486. **`crates/swc_es_parser/tests/errors.rs`** -> AI Confidence: **99.23%**
2487. **`crates/swc_node_comments/src/lib.rs`** -> AI Confidence: **99.23%**
2488. **`tools/generate-code/src/main.rs`** -> AI Confidence: **99.23%**
2489. **`xtask/src/util/mod.rs`** -> AI Confidence: **99.23%**
2490. **`crates/swc/tests/tsc-references/awaitUsingDeclarations.1(target=es5).1.normal.js`** -> AI Confidence: **99.23%**
2491. **`crates/swc/tests/tsc-references/exportAsNamespace4(module=umd).2.minified.js`** -> AI Confidence: **99.23%**
2492. **`crates/swc/tests/tsc-references/usingDeclarations.1(target=es2015).1.normal.js`** -> AI Confidence: **99.23%**
2493. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/comment_interning/types.js`** -> AI Confidence: **99.23%**
2494. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/types/grouping/nullable.js`** -> AI Confidence: **99.23%**
2495. **`packages/core/postinstall.js`** -> AI Confidence: **99.23%**
2496. **`crates/swc/tests/tsc-references/defaultExportInAwaitExpression01.2.minified.js`** -> AI Confidence: **99.2%**
2497. **`crates/swc/tests/tsc-references/exportAsNamespace1(module=umd).2.minified.js`** -> AI Confidence: **99.2%**
2498. **`crates/swc/tests/tsc-references/exportAsNamespace2(module=umd).2.minified.js`** -> AI Confidence: **99.2%**
2499. **`crates/swc/tests/tsc-references/importCallExpressionNestedUMD.1.normal.js`** -> AI Confidence: **99.2%**
2500. **`crates/swc/tests/fixture/ecosystem-ci/1/output/1.ts`** -> AI Confidence: **99.18%**
2501. **`crates/swc/tests/fixture/sourcemap/013/output/PistController.ts`** -> AI Confidence: **99.18%**
2502. **`crates/swc/tests/fixture/sourcemap/014/output/UserController.ts`** -> AI Confidence: **99.18%**
2503. **`crates/swc_bundler/tests/deno-exec/deno-8224/haystack-core/input/core/HStr.ts`** -> AI Confidence: **99.18%**
2504. **`crates/swc_bundler/tests/deno-exec/deno-8224/haystack-core/input/core/HSymbol.ts`** -> AI Confidence: **99.18%**
2505. **`crates/swc_bundler/tests/deno-exec/deno-8224/haystack-core/input/core/HXStr.ts`** -> AI Confidence: **99.18%**
2506. **`crates/swc_bundler/tests/deno-exec/deno-8224/haystack-core/input/filter/FilterLexer.ts`** -> AI Confidence: **99.18%**
2507. **`crates/swc_bundler/tests/deno-exec/deno-8224/haystack-core/input/filter/HFilterBuilder.ts`** -> AI Confidence: **99.18%**
2508. **`packages/types/index.ts`** -> AI Confidence: **99.18%**
2509. **`bindings/binding_core_node/src/print.rs`** -> AI Confidence: **99.18%**
2510. **`bindings/binding_minifier_node/src/minify.rs`** -> AI Confidence: **99.18%**
2511. **`crates/dbg-swc/src/es/exec_test.rs`** -> AI Confidence: **99.18%**
2512. **`crates/dbg-swc/src/es/minifier/compare_opts.rs`** -> AI Confidence: **99.18%**
2513. **`crates/dbg-swc/src/util/mod.rs`** -> AI Confidence: **99.18%**
2514. **`crates/hstr/benches/libs.rs`** -> AI Confidence: **99.18%**
2515. **`crates/hstr/src/wtf8/mod.rs`** -> AI Confidence: **99.18%**
2516. **`crates/preset_env_base/src/query.rs`** -> AI Confidence: **99.18%**
2517. **`crates/swc/benches/typescript.rs`** -> AI Confidence: **99.18%**
2518. **`crates/swc/tests/flow_strip_correctness.rs`** -> AI Confidence: **99.18%**
2519. **`crates/swc/tests/projects.rs`** -> AI Confidence: **99.18%**
2520. **`crates/swc/tests/serde.rs`** -> AI Confidence: **99.18%**
2521. **`crates/swc/tests/source_map.rs`** -> AI Confidence: **99.18%**
2522. **`crates/swc_allocator/benches/bench.rs`** -> AI Confidence: **99.18%**
2523. **`crates/swc_atoms/src/lib.rs`** -> AI Confidence: **99.18%**
2524. **`crates/swc_bundler/examples/bundle.rs`** -> AI Confidence: **99.18%**
2525. **`crates/swc_bundler/src/bundler/export.rs`** -> AI Confidence: **99.18%**
2526. **`crates/swc_bundler/src/bundler/finalize.rs`** -> AI Confidence: **99.18%**
2527. **`crates/swc_bundler/src/bundler/optimize.rs`** -> AI Confidence: **99.18%**
2528. **`crates/swc_bundler/src/id.rs`** -> AI Confidence: **99.18%**
2529. **`crates/swc_bundler/src/inline.rs`** -> AI Confidence: **99.18%**
2530. **`crates/swc_bundler/tests/fixture.rs`** -> AI Confidence: **99.18%**
2531. **`crates/swc_common/src/cache.rs`** -> AI Confidence: **99.18%**
2532. **`crates/swc_common/src/errors/diagnostic_builder.rs`** -> AI Confidence: **99.18%**
2533. **`crates/swc_common/src/input.rs`** -> AI Confidence: **99.18%**
2534. **`crates/swc_common/src/unknown.rs`** -> AI Confidence: **99.18%**
2535. **`crates/swc_config/src/glob.rs`** -> AI Confidence: **99.18%**
2536. **`crates/swc_core/tests/fixture/stub_napi/src/lib.rs`** -> AI Confidence: **99.18%**
2537. **`crates/swc_css_ast/src/lib.rs`** -> AI Confidence: **99.18%**
2538. **`crates/swc_css_lints/src/rule.rs`** -> AI Confidence: **99.18%**
2539. **`crates/swc_css_modules/src/lib.rs`** -> AI Confidence: **99.18%**
2540. **`crates/swc_ecma_compat_es2015/src/arrow.rs`** -> AI Confidence: **99.18%**
2541. **`crates/swc_ecma_compat_es2015/src/block_scoping/mod.rs`** -> AI Confidence: **99.18%**
2542. **`crates/swc_ecma_compat_es2015/src/for_of.rs`** -> AI Confidence: **99.18%**
2543. **`crates/swc_ecma_compat_es2015/src/object_super.rs`** -> AI Confidence: **99.18%**
2544. **`crates/swc_ecma_lexer/src/common/parser/buffer.rs`** -> AI Confidence: **99.18%**
2545. **`crates/swc_ecma_lints/src/rules/no_debugger.rs`** -> AI Confidence: **99.18%**
2546. **`crates/swc_ecma_lints/src/rules/no_restricted_syntax.rs`** -> AI Confidence: **99.18%**
2547. **`crates/swc_ecma_lints/src/rules/no_use_before_define.rs`** -> AI Confidence: **99.18%**
2548. **`crates/swc_ecma_lints/src/rules/no_var.rs`** -> AI Confidence: **99.18%**
2549. **`crates/swc_ecma_lints/tests/fixture.rs`** -> AI Confidence: **99.18%**
2550. **`crates/swc_ecma_minifier/benches/full.rs`** -> AI Confidence: **99.18%**
2551. **`crates/swc_ecma_minifier/src/lib.rs`** -> AI Confidence: **99.18%**
2552. **`crates/swc_ecma_minifier/src/pass/merge_exports.rs`** -> AI Confidence: **99.18%**
2553. **`crates/swc_ecma_minifier/src/usage_analyzer/alias/mod.rs`** -> AI Confidence: **99.18%**
2554. **`crates/swc_ecma_minifier/tests/compress.rs`** -> AI Confidence: **99.18%**
2555. **`crates/swc_ecma_minifier/tests/exec.rs`** -> AI Confidence: **99.18%**
2556. **`crates/swc_ecma_minifier/tests/terser_exec.rs`** -> AI Confidence: **99.18%**
2557. **`crates/swc_ecma_parser/examples/parse-all.rs`** -> AI Confidence: **99.18%**
2558. **`crates/swc_ecma_parser/examples/perf.rs`** -> AI Confidence: **99.18%**
2559. **`crates/swc_ecma_parser/src/parser/input.rs`** -> AI Confidence: **99.18%**
2560. **`crates/swc_ecma_parser/src/parser/tests.rs`** -> AI Confidence: **99.18%**
2561. **`crates/swc_ecma_parser/tests/comments.rs`** -> AI Confidence: **99.18%**
2562. **`crates/swc_ecma_parser/tests/jsx.rs`** -> AI Confidence: **99.18%**
2563. **`crates/swc_ecma_preset_env/src/corejs3/entry.rs`** -> AI Confidence: **99.18%**
2564. **`crates/swc_ecma_quote_macros/src/ctxt.rs`** -> AI Confidence: **99.18%**
2565. **`crates/swc_ecma_quote_macros/src/ret_type.rs`** -> AI Confidence: **99.18%**
2566. **`crates/swc_ecma_react_compiler/src/fast_check.rs`** -> AI Confidence: **99.18%**
2567. **`crates/swc_ecma_regexp/src/parser/reader/string_literal_parser/parser_impl.rs`** -> AI Confidence: **99.18%**
2568. **`crates/swc_ecma_transformer/src/common/statement_injector.rs`** -> AI Confidence: **99.18%**
2569. **`crates/swc_ecma_transformer/src/es2017/async_to_generator.rs`** -> AI Confidence: **99.18%**
2570. **`crates/swc_ecma_transformer/src/es2020/nullish_coalescing.rs`** -> AI Confidence: **99.18%**
2571. **`crates/swc_ecma_transformer/src/es2022/private_property_in_object.rs`** -> AI Confidence: **99.18%**
2572. **`crates/swc_ecma_transforms_base/benches/base.rs`** -> AI Confidence: **99.18%**
2573. **`crates/swc_ecma_transforms_base/src/perf.rs`** -> AI Confidence: **99.18%**
2574. **`crates/swc_ecma_transforms_base/src/rename/analyer_and_collector.rs`** -> AI Confidence: **99.18%**
2575. **`crates/swc_ecma_transforms_base/src/rename/mod.rs`** -> AI Confidence: **99.18%**
2576. **`crates/swc_ecma_transforms_base/src/tests.rs`** -> AI Confidence: **99.18%**
2577. **`crates/swc_ecma_transforms_base/tests/fixer_test262.rs`** -> AI Confidence: **99.18%**
2578. **`crates/swc_ecma_transforms_compat/src/class_fields_use_set.rs`** -> AI Confidence: **99.18%**
2579. **`crates/swc_ecma_transforms_compat/src/reserved_words.rs`** -> AI Confidence: **99.18%**
2580. **`crates/swc_ecma_transforms_macros/src/parallel.rs`** -> AI Confidence: **99.18%**
2581. **`crates/swc_ecma_transforms_module/src/module_ref_rewriter.rs`** -> AI Confidence: **99.18%**
2582. **`crates/swc_ecma_transforms_module/src/rewriter/import_rewriter_swc.rs`** -> AI Confidence: **99.18%**
2583. **`crates/swc_ecma_transforms_module/tests/umd.rs`** -> AI Confidence: **99.18%**
2584. **`crates/swc_ecma_transforms_proposal/src/decorators/legacy/mod.rs`** -> AI Confidence: **99.18%**
2585. **`crates/swc_ecma_transforms_proposal/src/explicit_resource_management.rs`** -> AI Confidence: **99.18%**
2586. **`crates/swc_ecma_transforms_react/src/display_name/mod.rs`** -> AI Confidence: **99.18%**
2587. **`crates/swc_ecma_transforms_testing/src/babel_like.rs`** -> AI Confidence: **99.18%**
2588. **`crates/swc_ecma_transforms_testing/src/lib.rs`** -> AI Confidence: **99.18%**
2589. **`crates/swc_ecma_transforms_typescript/src/typescript.rs`** -> AI Confidence: **99.18%**
2590. **`crates/swc_ecma_utils/src/factory.rs`** -> AI Confidence: **99.18%**
2591. **`crates/swc_es_parser/tests/bench_parser_inputs.rs`** -> AI Confidence: **99.18%**
2592. **`crates/swc_es_parser/tests/lexer_fixture.rs`** -> AI Confidence: **99.18%**
2593. **`crates/swc_es_parser/tests/span.rs`** -> AI Confidence: **99.18%**
2594. **`crates/swc_estree_ast/src/lit.rs`** -> AI Confidence: **99.18%**
2595. **`crates/swc_estree_compat/src/babelify/ident.rs`** -> AI Confidence: **99.18%**
2596. **`crates/swc_estree_compat/src/babelify/mod.rs`** -> AI Confidence: **99.18%**
2597. **`crates/swc_estree_compat/src/swcify/ctx.rs`** -> AI Confidence: **99.18%**
2598. **`crates/swc_estree_compat/tests/flavor.rs`** -> AI Confidence: **99.18%**
2599. **`crates/swc_graph_analyzer/src/lib.rs`** -> AI Confidence: **99.18%**
2600. **`crates/swc_html_parser/tests/common/mod.rs`** -> AI Confidence: **99.18%**
2601. **`crates/swc_plugin_backend_tests/tests/ecma_integration.rs`** -> AI Confidence: **99.18%**
2602. **`crates/swc_plugin_backend_tests/tests/ecma_loss.rs`** -> AI Confidence: **99.18%**
2603. **`crates/swc_plugin_backend_wasmer/src/lib.rs`** -> AI Confidence: **99.18%**
2604. **`crates/swc_plugin_proxy/src/source_map/plugin_source_map_proxy.rs`** -> AI Confidence: **99.18%**
2605. **`crates/swc_plugin_runner/src/imported_fn/comments.rs`** -> AI Confidence: **99.18%**
2606. **`crates/swc_plugin_runner/src/transform_executor.rs`** -> AI Confidence: **99.18%**
2607. **`crates/swc_sourcemap/src/lazy/mod.rs`** -> AI Confidence: **99.18%**
2608. **`crates/swc_ts_fast_strip_binding/src/lib.rs`** -> AI Confidence: **99.18%**
2609. **`crates/swc_xml_parser/src/parser/input.rs`** -> AI Confidence: **99.18%**
2610. **`crates/testing/src/errors/stderr.rs`** -> AI Confidence: **99.18%**
2611. **`crates/swc/tests/fixture/issues-2xxx/2056/1/input/index.js`** -> AI Confidence: **99.18%**
2612. **`crates/swc/tests/fixture/issues-2xxx/2056/1/output/index.js`** -> AI Confidence: **99.18%**
2613. **`crates/swc/tests/fixture/next.js/40399/3/output/index.js`** -> AI Confidence: **99.18%**
2614. **`crates/swc/tests/tsc-references/thisAndSuperInStaticMembers3.1.normal.js`** -> AI Confidence: **99.18%**
2615. **`crates/swc_ecma_minifier/tests/fixture/issues/react-instancesearch/003/input.js`** -> AI Confidence: **99.18%**
2616. **`crates/swc_ecma_minifier/tests/fixture/issues/react-instancesearch/003/output.js`** -> AI Confidence: **99.18%**
2617. **`crates/swc_ecma_minifier/tests/fixture/issues/react-instancesearch/004/input.js`** -> AI Confidence: **99.18%**
2618. **`crates/swc/tests/fixture/issues-9xxx/9821/case-default/output/index.ts`** -> AI Confidence: **99.17%**
2619. **`crates/swc/tests/fixture/issues-9xxx/9821/case-verbatimModuleSyntax/output/index.ts`** -> AI Confidence: **99.17%**
2620. **`crates/swc/tests/vercel/full/ms/1/input/index.ts`** -> AI Confidence: **99.17%**
2621. **`crates/swc_bundler/tests/deno-exec/deno-8224/haystack-core/input/core/UnitDimensions.ts`** -> AI Confidence: **99.17%**
2622. **`crates/swc_bundler/tests/fixture/deno-9620/case1/output/entry.inlined.ts`** -> AI Confidence: **99.17%**
2623. **`crates/swc_bundler/tests/fixture/deno-9620/case1/output/entry.ts`** -> AI Confidence: **99.17%**
2624. **`crates/swc_ecma_parser/tests/errors/conflict_marker_diff_3_trivia_1/input.ts`** -> AI Confidence: **99.17%**
2625. **`crates/swc_ecma_parser/tests/errors/conflict_marker_diff_3_trivia_2/input.ts`** -> AI Confidence: **99.17%**
2626. **`crates/swc_ecma_parser/tests/tsc/assertionsAndNonReturningFunctions.ts`** -> AI Confidence: **99.17%**
2627. **`crates/swc_ecma_parser/tests/tsc/controlFlowInOperator.ts`** -> AI Confidence: **99.17%**
2628. **`crates/swc_ecma_parser/tests/tsc/controlFlowOptionalChain2.ts`** -> AI Confidence: **99.17%**
2629. **`crates/swc_ecma_parser/tests/tsc/controlFlowTypeofObject.ts`** -> AI Confidence: **99.17%**
2630. **`crates/swc_ecma_parser/tests/tsc/ifDoWhileStatements.ts`** -> AI Confidence: **99.17%**
2631. **`crates/swc_ecma_parser/tests/tsc/keyofAndForIn.ts`** -> AI Confidence: **99.17%**
2632. **`crates/swc_ecma_parser/tests/tsc/literalTypesAndDestructuring.ts`** -> AI Confidence: **99.17%**
2633. **`crates/swc_ecma_parser/tests/tsc/logicalAssignment2.ts`** -> AI Confidence: **99.17%**
2634. **`crates/swc_ecma_parser/tests/tsc/methodSignaturesWithOverloads2.ts`** -> AI Confidence: **99.17%**
2635. **`crates/swc_ecma_parser/tests/tsc/narrowExceptionVariableInCatchClause.ts`** -> AI Confidence: **99.17%**
2636. **`crates/swc_ecma_parser/tests/tsc/nullishCoalescingOperator1.ts`** -> AI Confidence: **99.17%**
2637. **`crates/swc_ecma_parser/tests/tsc/nullishCoalescingOperator4.ts`** -> AI Confidence: **99.17%**
2638. **`crates/swc_ecma_parser/tests/tsc/objectRestForOf.ts`** -> AI Confidence: **99.17%**
2639. **`crates/swc_ecma_parser/tests/tsc/switchStatements.ts`** -> AI Confidence: **99.17%**
2640. **`crates/swc_ecma_parser/tests/tsc/symbolType8.ts`** -> AI Confidence: **99.17%**
2641. **`crates/swc_ecma_parser/tests/tsc/templateStringInEqualityChecks.ts`** -> AI Confidence: **99.17%**
2642. **`crates/swc_ecma_parser/tests/tsc/templateStringInEqualityChecksES6.ts`** -> AI Confidence: **99.17%**
2643. **`crates/swc_ecma_parser/tests/tsc/typeFromPrivatePropertyAssignment.ts`** -> AI Confidence: **99.17%**
2644. **`crates/swc_ecma_parser/tests/tsc/typeGuardOfFormNotExpr.ts`** -> AI Confidence: **99.17%**
2645. **`crates/swc_ecma_parser/tests/tsc/unknownType2.ts`** -> AI Confidence: **99.17%**
2646. **`crates/swc_ecma_parser/tests/typescript-errors/class/parameter-properties/input.ts`** -> AI Confidence: **99.17%**
2647. **`crates/swc_ecma_parser/tests/typescript/optional-chaining/chaining-off-optionally-chained-keys-named-class-or-function/input.ts`** -> AI Confidence: **99.17%**
2648. **`crates/swc_ecma_transforms_base/tests/ts-resolver/ts_resolver_catch_param/input.ts`** -> AI Confidence: **99.17%**
2649. **`crates/swc_ecma_transforms_base/tests/ts-resolver/ts_resolver_catch_param/output.ts`** -> AI Confidence: **99.17%**
2650. **`crates/swc_ecma_transforms_module/tests/fixture/common/cts-import-export/export-assign/output.umd.ts`** -> AI Confidence: **99.17%**
2651. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-5042/1/output.umd.ts`** -> AI Confidence: **99.17%**
2652. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-5042/2/output.umd.ts`** -> AI Confidence: **99.17%**
2653. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-895/output.umd.ts`** -> AI Confidence: **99.17%**
2654. **`crates/swc_ecma_transforms_typescript/tests/fixture/issue-366/1/input.ts`** -> AI Confidence: **99.17%**
2655. **`packages/html/index.ts`** -> AI Confidence: **99.17%**
2656. **`crates/swc_css_minifier/src/compressor/math/mod.rs`** -> AI Confidence: **99.17%**
2657. **`crates/swc_ecma_codegen/src/expr.rs`** -> AI Confidence: **99.17%**
2658. **`crates/swc_ecma_codegen/src/macros.rs`** -> AI Confidence: **99.17%**
2659. **`crates/swc_ecma_minifier/src/compress/optimize/props.rs`** -> AI Confidence: **99.17%**
2660. **`crates/swc_ecma_transformer/src/es2015/function_name.rs`** -> AI Confidence: **99.17%**
2661. **`crates/swc_es_codegen/src/lib.rs`** -> AI Confidence: **99.17%**
2662. **`crates/swc_es_transforms/src/rewrite.rs`** -> AI Confidence: **99.17%**
2663. **`crates/swc_sourcemap/src/js_identifiers.rs`** -> AI Confidence: **99.17%**
2664. **`crates/swc_xml_parser/src/parser/macros.rs`** -> AI Confidence: **99.17%**
2665. **`crates/jsdoc/tests/fixtures/also.js`** -> AI Confidence: **99.17%**
2666. **`crates/swc/tests/errors/lints/no-cond-assign/default/input.js`** -> AI Confidence: **99.17%**
2667. **`crates/swc/tests/errors/lints/no-throw-literal/default/input.js`** -> AI Confidence: **99.17%**
2668. **`crates/swc/tests/fixture/issues-11xxx/11379/output/index.js`** -> AI Confidence: **99.17%**
2669. **`crates/swc/tests/fixture/issues-2xxx/2022/full/output/index.js`** -> AI Confidence: **99.17%**
2670. **`crates/swc/tests/fixture/issues-2xxx/2022/no-opt/output/index.js`** -> AI Confidence: **99.17%**
2671. **`crates/swc/tests/fixture/issues-7xxx/7710/input/export-default-expr-3.js`** -> AI Confidence: **99.17%**
2672. **`crates/swc/tests/fixture/issues-8xxx/8774/output/index.js`** -> AI Confidence: **99.17%**
2673. **`crates/swc/tests/fixture/issues-8xxx/8880/input/1.js`** -> AI Confidence: **99.17%**
2674. **`crates/swc/tests/fixture/issues-9xxx/9673/output/1.js`** -> AI Confidence: **99.17%**
2675. **`crates/swc/tests/tsc-references/anonymousDefaultExportsUmd.2.minified.js`** -> AI Confidence: **99.17%**
2676. **`crates/swc/tests/tsc-references/assertionsAndNonReturningFunctions.1.normal.js`** -> AI Confidence: **99.17%**
2677. **`crates/swc/tests/tsc-references/awaitUsingDeclarations.1(target=es2017).1.normal.js`** -> AI Confidence: **99.17%**
2678. **`crates/swc/tests/tsc-references/awaitUsingDeclarations.1(target=es2022).1.normal.js`** -> AI Confidence: **99.17%**
2679. **`crates/swc/tests/tsc-references/awaitUsingDeclarations.1(target=esnext).1.normal.js`** -> AI Confidence: **99.17%**
2680. **`crates/swc/tests/tsc-references/callChain.2.2.minified.js`** -> AI Confidence: **99.17%**
2681. **`crates/swc/tests/tsc-references/callChain.3.1.normal.js`** -> AI Confidence: **99.17%**
2682. **`crates/swc/tests/tsc-references/controlFlowDoWhileStatement.1.normal.js`** -> AI Confidence: **99.17%**
2683. **`crates/swc/tests/tsc-references/controlFlowIteration.1.normal.js`** -> AI Confidence: **99.17%**
2684. **`crates/swc/tests/tsc-references/controlFlowNullishCoalesce.1.normal.js`** -> AI Confidence: **99.17%**
2685. **`crates/swc/tests/tsc-references/controlFlowParameter.1.normal.js`** -> AI Confidence: **99.17%**
2686. **`crates/swc/tests/tsc-references/controlFlowTypeofObject.1.normal.js`** -> AI Confidence: **99.17%**
2687. **`crates/swc/tests/tsc-references/defaultExportsGetExportedUmd.2.minified.js`** -> AI Confidence: **99.17%**
2688. **`crates/swc/tests/tsc-references/deleteChain.1.normal.js`** -> AI Confidence: **99.17%**
2689. **`crates/swc/tests/tsc-references/destructuringWithLiteralInitializers2.1.normal.js`** -> AI Confidence: **99.17%**
2690. **`crates/swc/tests/tsc-references/discriminatedUnionTypes1.1.normal.js`** -> AI Confidence: **99.17%**
2691. **`crates/swc/tests/tsc-references/equalityWithEnumTypes.1.normal.js`** -> AI Confidence: **99.17%**
2692. **`crates/swc/tests/tsc-references/exportImportAlias.2.minified.js`** -> AI Confidence: **99.17%**
2693. **`crates/swc/tests/tsc-references/importCallExpressionInUMD2.1.normal.js`** -> AI Confidence: **99.17%**
2694. **`crates/swc/tests/tsc-references/importCallExpressionInUMD5.2.minified.js`** -> AI Confidence: **99.17%**
2695. **`crates/swc/tests/tsc-references/importCallExpressionNestedUMD2.1.normal.js`** -> AI Confidence: **99.17%**
2696. **`crates/swc/tests/tsc-references/logicalAssignment11(target=es2015).1.normal.js`** -> AI Confidence: **99.17%**
2697. **`crates/swc/tests/tsc-references/logicalAssignment11(target=es2020).1.normal.js`** -> AI Confidence: **99.17%**
2698. **`crates/swc/tests/tsc-references/logicalAssignment11(target=esnext).1.normal.js`** -> AI Confidence: **99.17%**
2699. **`crates/swc/tests/tsc-references/logicalAssignment3(target=es2015).2.minified.js`** -> AI Confidence: **99.17%**
2700. **`crates/swc/tests/tsc-references/logicalAssignment9.1.normal.js`** -> AI Confidence: **99.17%**
2701. **`crates/swc/tests/tsc-references/noUncheckedIndexedAccess.2.minified.js`** -> AI Confidence: **99.17%**
2702. **`crates/swc/tests/tsc-references/nullishCoalescingOperator1.1.normal.js`** -> AI Confidence: **99.17%**
2703. **`crates/swc/tests/tsc-references/nullishCoalescingOperator8.1.normal.js`** -> AI Confidence: **99.17%**
2704. **`crates/swc/tests/tsc-references/objectTypeWithStringNamedPropertyOfIllegalCharacters.2.minified.js`** -> AI Confidence: **99.17%**
2705. **`crates/swc/tests/tsc-references/optionalChainingInParameterInitializer.2(target=es5).2.minified.js`** -> AI Confidence: **99.17%**
2706. **`crates/swc/tests/tsc-references/optionalChainingInTypeAssertions(target=es2015).2.minified.js`** -> AI Confidence: **99.17%**
2707. **`crates/swc/tests/tsc-references/parserModule1.1.normal.js`** -> AI Confidence: **99.17%**
2708. **`crates/swc/tests/tsc-references/parserRealSource2.1.normal.js`** -> AI Confidence: **99.17%**
2709. **`crates/swc/tests/tsc-references/propertyAccessChain.2.2.minified.js`** -> AI Confidence: **99.17%**
2710. **`crates/swc/tests/tsc-references/stringLiteralsWithSwitchStatements01.1.normal.js`** -> AI Confidence: **99.17%**
2711. **`crates/swc/tests/tsc-references/switchStatements.1.normal.js`** -> AI Confidence: **99.17%**
2712. **`crates/swc/tests/tsc-references/switchStatements.2.minified.js`** -> AI Confidence: **99.17%**
2713. **`crates/swc/tests/tsc-references/symbolType8.1.normal.js`** -> AI Confidence: **99.17%**
2714. **`crates/swc/tests/tsc-references/templateStringInEqualityChecks.1.normal.js`** -> AI Confidence: **99.17%**
2715. **`crates/swc/tests/tsc-references/templateStringInEqualityChecksES6.1.normal.js`** -> AI Confidence: **99.17%**
2716. **`crates/swc/tests/tsc-references/thisPrototypeMethodCompoundAssignmentJs.1.normal.js`** -> AI Confidence: **99.17%**
2717. **`crates/swc/tests/tsc-references/tsxEmit3.2.minified.js`** -> AI Confidence: **99.17%**
2718. **`crates/swc/tests/tsc-references/typeFromJSInitializer4.1.normal.js`** -> AI Confidence: **99.17%**
2719. **`crates/swc/tests/tsc-references/typeGuardOfFormExpr1AndExpr2.2.minified.js`** -> AI Confidence: **99.17%**
2720. **`crates/swc/tests/tsc-references/typeGuardOfFormExpr1OrExpr2.2.minified.js`** -> AI Confidence: **99.17%**
2721. **`crates/swc/tests/tsc-references/typeGuardOfFormInstanceOfOnInterface.2.minified.js`** -> AI Confidence: **99.17%**
2722. **`crates/swc/tests/tsc-references/typeGuardOfFormNotExpr.1.normal.js`** -> AI Confidence: **99.17%**
2723. **`crates/swc/tests/tsc-references/typeGuardOfFormTypeOfFunction.1.normal.js`** -> AI Confidence: **99.17%**
2724. **`crates/swc/tests/tsc-references/typeGuardOfFormTypeOfOther.2.minified.js`** -> AI Confidence: **99.17%**
2725. **`crates/swc/tests/tsc-references/typeGuardsInModule.1.normal.js`** -> AI Confidence: **99.17%**
2726. **`crates/swc/tests/tsc-references/unknownControlFlow.1.normal.js`** -> AI Confidence: **99.17%**
2727. **`crates/swc/tests/tsc-references/usingDeclarations.1(target=es2015).2.minified.js`** -> AI Confidence: **99.17%**
2728. **`crates/swc/tests/tsc-references/usingDeclarations.1(target=es2017).2.minified.js`** -> AI Confidence: **99.17%**
2729. **`crates/swc/tests/tsc-references/usingDeclarations.1(target=es2022).2.minified.js`** -> AI Confidence: **99.17%**
2730. **`crates/swc/tests/tsc-references/usingDeclarations.1(target=esnext).2.minified.js`** -> AI Confidence: **99.17%**
2731. **`crates/swc_ecma_compat_es2015/tests/__swc_snapshots__/src/block_scoped_fn.rs/hoisting_directives.js`** -> AI Confidence: **99.17%**
2732. **`crates/swc_ecma_minifier/tests/fixture/issues/2044/full/output.js`** -> AI Confidence: **99.17%**
2733. **`crates/swc_ecma_minifier/tests/fixture/issues/2044/pass-1/input.js`** -> AI Confidence: **99.17%**
2734. **`crates/swc_ecma_minifier/tests/fixture/issues/2044/pass-1/output.js`** -> AI Confidence: **99.17%**
2735. **`crates/swc_ecma_minifier/tests/fixture/issues/2044/pass-10/input.js`** -> AI Confidence: **99.17%**
2736. **`crates/swc_ecma_minifier/tests/fixture/issues/2044/pass-10/output.js`** -> AI Confidence: **99.17%**
2737. **`crates/swc_ecma_minifier/tests/fixture/issues/5682/input.js`** -> AI Confidence: **99.17%**
2738. **`crates/swc_ecma_minifier/tests/fixture/issues/8284/input.js`** -> AI Confidence: **99.17%**
2739. **`crates/swc_ecma_minifier/tests/fixture/issues/8813/output.js`** -> AI Confidence: **99.17%**
2740. **`crates/swc_ecma_minifier/tests/fixture/issues/8844/input.js`** -> AI Confidence: **99.17%**
2741. **`crates/swc_ecma_minifier/tests/fixture/issues/9785/output.js`** -> AI Confidence: **99.17%**
2742. **`crates/swc_ecma_minifier/tests/fixture/issues/framer-motion/1/input.js`** -> AI Confidence: **99.17%**
2743. **`crates/swc_ecma_minifier/tests/fixture/issues/stylis/1/input.js`** -> AI Confidence: **99.17%**
2744. **`crates/swc_ecma_minifier/tests/fixture/issues/stylis/1/output.js`** -> AI Confidence: **99.17%**
2745. **`crates/swc_ecma_minifier/tests/fixture/issues/stylis/2/input.js`** -> AI Confidence: **99.17%**
2746. **`crates/swc_ecma_minifier/tests/fixture/issues/stylis/2/output.js`** -> AI Confidence: **99.17%**
2747. **`crates/swc_ecma_minifier/tests/fixture/issues/vercel/005/input.js`** -> AI Confidence: **99.17%**
2748. **`crates/swc_ecma_minifier/tests/fixture/next/41527/1/input.js`** -> AI Confidence: **99.17%**
2749. **`crates/swc_ecma_minifier/tests/fixture/next/regression-1/framework-798bab57daac3897/input.js`** -> AI Confidence: **99.17%**
2750. **`crates/swc_ecma_minifier/tests/fixture/projects/backbone/19/output.js`** -> AI Confidence: **99.17%**
2751. **`crates/swc_ecma_minifier/tests/fixture/projects/backbone/2/input.js`** -> AI Confidence: **99.17%**
2752. **`crates/swc_ecma_minifier/tests/fixture/projects/backbone/20/input.js`** -> AI Confidence: **99.17%**
2753. **`crates/swc_ecma_minifier/tests/fixture/projects/jquery/1/input.js`** -> AI Confidence: **99.17%**
2754. **`crates/swc_ecma_minifier/tests/fixture/projects/jquery/1/output.js`** -> AI Confidence: **99.17%**
2755. **`crates/swc_ecma_minifier/tests/fixture/projects/jquery/10/input.js`** -> AI Confidence: **99.17%**
2756. **`crates/swc_ecma_minifier/tests/fixture/projects/jquery/10/output.js`** -> AI Confidence: **99.17%**
2757. **`crates/swc_ecma_minifier/tests/fixture/projects/jquery/13/input.js`** -> AI Confidence: **99.17%**
2758. **`crates/swc_ecma_minifier/tests/fixture/projects/jquery/13/output.js`** -> AI Confidence: **99.17%**
2759. **`crates/swc_ecma_minifier/tests/fixture/projects/jquery/16/output.js`** -> AI Confidence: **99.17%**
2760. **`crates/swc_ecma_minifier/tests/fixture/projects/jquery/21/input.js`** -> AI Confidence: **99.17%**
2761. **`crates/swc_ecma_minifier/tests/fixture/projects/jquery/3/output.js`** -> AI Confidence: **99.17%**
2762. **`crates/swc_ecma_minifier/tests/fixture/projects/jquery/9/input.js`** -> AI Confidence: **99.17%**
2763. **`crates/swc_ecma_minifier/tests/fixture/projects/jquery/9/output.js`** -> AI Confidence: **99.17%**
2764. **`crates/swc_ecma_minifier/tests/fixture/projects/next/extra/if_return/1/output.js`** -> AI Confidence: **99.17%**
2765. **`crates/swc_ecma_minifier/tests/fixture/projects/react/11/output.js`** -> AI Confidence: **99.17%**
2766. **`crates/swc_ecma_minifier/tests/fixture/projects/react/13/output.js`** -> AI Confidence: **99.17%**
2767. **`crates/swc_ecma_minifier/tests/fixture/projects/react/14/input.js`** -> AI Confidence: **99.17%**
2768. **`crates/swc_ecma_minifier/tests/fixture/projects/react/15/output.js`** -> AI Confidence: **99.17%**
2769. **`crates/swc_ecma_minifier/tests/fixture/projects/react/16/input.js`** -> AI Confidence: **99.17%**
2770. **`crates/swc_ecma_minifier/tests/fixture/projects/react/8/output.js`** -> AI Confidence: **99.17%**
2771. **`crates/swc_ecma_minifier/tests/fixture/projects/underscore/10/input.js`** -> AI Confidence: **99.17%**
2772. **`crates/swc_ecma_minifier/tests/fixture/projects/underscore/10/output.js`** -> AI Confidence: **99.17%**
2773. **`crates/swc_ecma_minifier/tests/fixture/projects/underscore/15/input.js`** -> AI Confidence: **99.17%**
2774. **`crates/swc_ecma_minifier/tests/fixture/projects/underscore/15/output.js`** -> AI Confidence: **99.17%**
2775. **`crates/swc_ecma_minifier/tests/fixture/projects/underscore/19/input.js`** -> AI Confidence: **99.17%**
2776. **`crates/swc_ecma_minifier/tests/fixture/projects/underscore/20/input.js`** -> AI Confidence: **99.17%**
2777. **`crates/swc_ecma_minifier/tests/fixture/projects/underscore/20/output.js`** -> AI Confidence: **99.17%**
2778. **`crates/swc_ecma_minifier/tests/fixture/projects/underscore/5/output.js`** -> AI Confidence: **99.17%**
2779. **`crates/swc_ecma_minifier/tests/fixture/projects/yui/12/input.js`** -> AI Confidence: **99.17%**
2780. **`crates/swc_ecma_minifier/tests/fixture/projects/yui/12/output.js`** -> AI Confidence: **99.17%**
2781. **`crates/swc_ecma_minifier/tests/fixture/projects/yui/13/input.js`** -> AI Confidence: **99.17%**
2782. **`crates/swc_ecma_minifier/tests/fixture/projects/yui/9/input.js`** -> AI Confidence: **99.17%**
2783. **`crates/swc_ecma_minifier/tests/fixture/projects/yui/9/output.js`** -> AI Confidence: **99.17%**
2784. **`crates/swc_ecma_minifier/tests/full/vercel/ms/1/input.js`** -> AI Confidence: **99.17%**
2785. **`crates/swc_ecma_minifier/tests/terser/compress/collapse_vars/issue_2974/input.js`** -> AI Confidence: **99.17%**
2786. **`crates/swc_ecma_minifier/tests/terser/compress/collapse_vars/issue_2974/output.mangleOnly.js`** -> AI Confidence: **99.17%**
2787. **`crates/swc_ecma_minifier/tests/terser/compress/collapse_vars/replace_all_var_scope/input.js`** -> AI Confidence: **99.17%**
2788. **`crates/swc_ecma_minifier/tests/terser/compress/collapse_vars/replace_all_var_scope/output.js`** -> AI Confidence: **99.17%**
2789. **`crates/swc_ecma_minifier/tests/terser/compress/collapse_vars/replace_all_var_scope/output.mangleOnly.js`** -> AI Confidence: **99.17%**
2790. **`crates/swc_ecma_minifier/tests/terser/compress/collapse_vars/replace_all_var_scope/output.terser.js`** -> AI Confidence: **99.17%**
2791. **`crates/swc_ecma_minifier/tests/terser/compress/collapse_vars/switch_case_3/input.js`** -> AI Confidence: **99.17%**
2792. **`crates/swc_ecma_minifier/tests/terser/compress/collapse_vars/switch_case_3/output.mangleOnly.js`** -> AI Confidence: **99.17%**
2793. **`crates/swc_ecma_minifier/tests/terser/compress/collapse_vars/switch_case_3/output.terser.js`** -> AI Confidence: **99.17%**
2794. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/cond_7/output.js`** -> AI Confidence: **99.17%**
2795. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/cond_7/output.terser.js`** -> AI Confidence: **99.17%**
2796. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/cond_8/output.terser.js`** -> AI Confidence: **99.17%**
2797. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/cond_8b/output.terser.js`** -> AI Confidence: **99.17%**
2798. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/ifs_3_should_warn/input.js`** -> AI Confidence: **99.17%**
2799. **`crates/swc_ecma_minifier/tests/terser/compress/conditionals/ifs_3_should_warn/output.mangleOnly.js`** -> AI Confidence: **99.17%**
2800. **`crates/swc_ecma_minifier/tests/terser/compress/dead_code/issue_2597/input.js`** -> AI Confidence: **99.17%**
2801. **`crates/swc_ecma_minifier/tests/terser/compress/dead_code/issue_2597/output.js`** -> AI Confidence: **99.17%**
2802. **`crates/swc_ecma_minifier/tests/terser/compress/dead_code/issue_2597/output.mangleOnly.js`** -> AI Confidence: **99.17%**
2803. **`crates/swc_ecma_minifier/tests/terser/compress/dead_code/issue_2597/output.terser.js`** -> AI Confidence: **99.17%**
2804. **`crates/swc_ecma_minifier/tests/terser/compress/dead_code/throw_assignment/input.js`** -> AI Confidence: **99.17%**
2805. **`crates/swc_ecma_minifier/tests/terser/compress/dead_code/throw_assignment/output.js`** -> AI Confidence: **99.17%**
2806. **`crates/swc_ecma_minifier/tests/terser/compress/dead_code/throw_assignment/output.mangleOnly.js`** -> AI Confidence: **99.17%**
2807. **`crates/swc_ecma_minifier/tests/terser/compress/dead_code/throw_assignment/output.terser.js`** -> AI Confidence: **99.17%**
2808. **`crates/swc_ecma_minifier/tests/terser/compress/dead_code/try_catch_finally/input.js`** -> AI Confidence: **99.17%**
2809. **`crates/swc_ecma_minifier/tests/terser/compress/dead_code/try_catch_finally/output.mangleOnly.js`** -> AI Confidence: **99.17%**
2810. **`crates/swc_ecma_minifier/tests/terser/compress/drop_unused/issue_2665/input.js`** -> AI Confidence: **99.17%**
2811. **`crates/swc_ecma_minifier/tests/terser/compress/drop_unused/issue_2665/output.mangleOnly.js`** -> AI Confidence: **99.17%**
2812. **`crates/swc_ecma_minifier/tests/terser/compress/expansions/avoid_spread_in_ternary/output.js`** -> AI Confidence: **99.17%**
2813. **`crates/swc_ecma_minifier/tests/terser/compress/expansions/avoid_spread_in_ternary/output.terser.js`** -> AI Confidence: **99.17%**
2814. **`crates/swc_ecma_minifier/tests/terser/compress/functions/issue_2604_1/output.js`** -> AI Confidence: **99.17%**
2815. **`crates/swc_ecma_minifier/tests/terser/compress/functions/issue_2604_2/output.js`** -> AI Confidence: **99.17%**
2816. **`crates/swc_ecma_minifier/tests/terser/compress/functions/issue_2604_2/output.terser.js`** -> AI Confidence: **99.17%**
2817. **`crates/swc_ecma_minifier/tests/terser/compress/functions/issue_3018/input.js`** -> AI Confidence: **99.17%**
2818. **`crates/swc_ecma_minifier/tests/terser/compress/functions/issue_3018/output.mangleOnly.js`** -> AI Confidence: **99.17%**
2819. **`crates/swc_ecma_minifier/tests/terser/compress/if_return/if_return_8/output.js`** -> AI Confidence: **99.17%**
2820. **`crates/swc_ecma_minifier/tests/terser/compress/if_return/if_return_8/output.terser.js`** -> AI Confidence: **99.17%**
2821. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1447/conditional_false_stray_else_in_loop/input.js`** -> AI Confidence: **99.17%**
2822. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1447/conditional_false_stray_else_in_loop/output.mangleOnly.js`** -> AI Confidence: **99.17%**
2823. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1639/issue_1639_2/input.js`** -> AI Confidence: **99.17%**
2824. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1639/issue_1639_2/output.mangleOnly.js`** -> AI Confidence: **99.17%**
2825. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1639/issue_1639_3/input.js`** -> AI Confidence: **99.17%**
2826. **`crates/swc_ecma_minifier/tests/terser/compress/issue_1639/issue_1639_3/output.mangleOnly.js`** -> AI Confidence: **99.17%**
2827. **`crates/swc_ecma_minifier/tests/terser/compress/labels/labels_3/input.js`** -> AI Confidence: **99.17%**
2828. **`crates/swc_ecma_minifier/tests/terser/compress/labels/labels_3/output.mangleOnly.js`** -> AI Confidence: **99.17%**
2829. **`crates/swc_ecma_minifier/tests/terser/compress/labels/labels_4/input.js`** -> AI Confidence: **99.17%**
2830. **`crates/swc_ecma_minifier/tests/terser/compress/labels/labels_4/output.mangleOnly.js`** -> AI Confidence: **99.17%**
2831. **`crates/swc_ecma_minifier/tests/terser/compress/negate_iife/issue_1288/output.js`** -> AI Confidence: **99.17%**
2832. **`crates/swc_ecma_minifier/tests/terser/compress/negate_iife/issue_1288/output.terser.js`** -> AI Confidence: **99.17%**
2833. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/conditional_nested_3/input.js`** -> AI Confidence: **99.17%**
2834. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/conditional_nested_3/output.js`** -> AI Confidence: **99.17%**
2835. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/conditional_nested_3/output.mangleOnly.js`** -> AI Confidence: **99.17%**
2836. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/conditional_nested_3/output.terser.js`** -> AI Confidence: **99.17%**
2837. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/do_while/input.js`** -> AI Confidence: **99.17%**
2838. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/do_while/output.js`** -> AI Confidence: **99.17%**
2839. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/do_while/output.mangleOnly.js`** -> AI Confidence: **99.17%**
2840. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/do_while/output.terser.js`** -> AI Confidence: **99.17%**
2841. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/var_if/input.js`** -> AI Confidence: **99.17%**
2842. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/var_if/output.js`** -> AI Confidence: **99.17%**
2843. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/var_if/output.mangleOnly.js`** -> AI Confidence: **99.17%**
2844. **`crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/var_if/output.terser.js`** -> AI Confidence: **99.17%**
2845. **`crates/swc_ecma_minifier/tests/terser/compress/switch/issue_1680_2/output.js`** -> AI Confidence: **99.17%**
2846. **`crates/swc_ecma_minifier/tests/terser/compress/switch/issue_1680_2/output.terser.js`** -> AI Confidence: **99.17%**
2847. **`crates/swc_ecma_minifier/tests/terser/compress/transform/if_return/output.js`** -> AI Confidence: **99.17%**
2848. **`crates/swc_ecma_minifier/tests/terser/compress/transform/if_return/output.terser.js`** -> AI Confidence: **99.17%**
2849. **`crates/swc_ecma_minifier/tests/terser/compress/typeof/typeof_defun_2/input.js`** -> AI Confidence: **99.17%**
2850. **`crates/swc_ecma_minifier/tests/terser/compress/typeof/typeof_defun_2/output.mangleOnly.js`** -> AI Confidence: **99.17%**
2851. **`crates/swc_ecma_parser/tests/flow-hermes/corpus/comment_interning/do_while.js`** -> AI Confidence: **99.17%**
2852. **`crates/swc_ecma_transforms_base/src/helpers/_interop_require_default.js`** -> AI Confidence: **99.17%**
2853. **`crates/swc_ecma_transforms_base/src/helpers/_iterable_to_array.js`** -> AI Confidence: **99.17%**
2854. **`crates/swc_ecma_transforms_base/src/helpers/_jsx.js`** -> AI Confidence: **99.17%**
2855. **`crates/swc_ecma_transforms_base/src/helpers/_object_without_properties.js`** -> AI Confidence: **99.17%**
2856. **`crates/swc_ecma_transforms_base/src/helpers/_sliced_to_array.js`** -> AI Confidence: **99.17%**
2857. **`crates/swc_ecma_transforms_base/src/helpers/_sliced_to_array_loose.js`** -> AI Confidence: **99.17%**
2858. **`crates/swc_ecma_transforms_base/src/helpers/_super_prop_base.js`** -> AI Confidence: **99.17%**
2859. **`crates/swc_ecma_transforms_base/src/helpers/_to_array.js`** -> AI Confidence: **99.17%**
2860. **`crates/swc_ecma_transforms_base/src/helpers/_to_consumable_array.js`** -> AI Confidence: **99.17%**
2861. **`crates/swc_ecma_transforms_base/src/helpers/_type_of.js`** -> AI Confidence: **99.17%**
2862. **`crates/swc_ecma_transforms_base/src/helpers/_unsupported_iterable_to_array.js`** -> AI Confidence: **99.17%**
2863. **`crates/swc_ecma_transforms_compat/tests/__swc_snapshots__/tests/es2015_classes.rs/issue_5102.js`** -> AI Confidence: **99.17%**
2864. **`crates/swc_ecma_transforms_compat/tests/__swc_snapshots__/tests/es2015_parameters.rs/default_before_last.js`** -> AI Confidence: **99.17%**
2865. **`crates/swc_ecma_transforms_compat/tests/__swc_snapshots__/tests/es2015_parameters.rs/destructuring_rest.js`** -> AI Confidence: **99.17%**
2866. **`crates/swc_ecma_transforms_compat/tests/__swc_snapshots__/tests/es2015_parameters.rs/issue_760.js`** -> AI Confidence: **99.17%**
2867. **`crates/swc_ecma_transforms_compat/tests/__swc_snapshots__/tests/es2018_object_rest_spread.rs/rest_catch_clause.js`** -> AI Confidence: **99.17%**
2868. **`crates/swc_ecma_transforms_compat/tests/__swc_snapshots__/tests/es2022_class_properties.rs/issue_1333_2.js`** -> AI Confidence: **99.17%**
2869. **`crates/swc_ecma_transforms_compat/tests/async-to-generator/issue-5913/2/exec.js`** -> AI Confidence: **99.17%**
2870. **`crates/swc_ecma_transforms_compat/tests/new-target/general/function/output.js`** -> AI Confidence: **99.17%**
2871. **`crates/swc_ecma_transforms_compat/tests/optional-chaining/issue-6886/exec.js`** -> AI Confidence: **99.17%**
2872. **`crates/swc_ecma_transforms_compat/tests/optional-chaining/issue-7156/1/exec.js`** -> AI Confidence: **99.17%**
2873. **`crates/swc_ecma_transforms_module/tests/fixture/common/custom/01/output.umd.js`** -> AI Confidence: **99.17%**
2874. **`crates/swc_ecma_transforms_module/tests/fixture/common/export-proto/output.umd.js`** -> AI Confidence: **99.17%**
2875. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop-module-string-names/export-named-string-can-be-identifier/output.umd.js`** -> AI Confidence: **99.17%**
2876. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop-module-string-names/export-named/output.umd.js`** -> AI Confidence: **99.17%**
2877. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop-node/export-from-3/output.umd.js`** -> AI Confidence: **99.17%**
2878. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop-node/export-named-2/output.umd.js`** -> AI Confidence: **99.17%**
2879. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop-node/export-named-5/output.umd.js`** -> AI Confidence: **99.17%**
2880. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop/export-from-3/output.umd.js`** -> AI Confidence: **99.17%**
2881. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop/export-named-2/output.umd.js`** -> AI Confidence: **99.17%**
2882. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop/export-named-5/output.umd.js`** -> AI Confidence: **99.17%**
2883. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-1614/1/output.umd.js`** -> AI Confidence: **99.17%**
2884. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-2211/1/output.umd.js`** -> AI Confidence: **99.17%**
2885. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-2297/output.umd.js`** -> AI Confidence: **99.17%**
2886. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-2548/case3/output.umd.js`** -> AI Confidence: **99.17%**
2887. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-3439/5/output.umd.js`** -> AI Confidence: **99.17%**
2888. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-369/output.umd.js`** -> AI Confidence: **99.17%**
2889. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-4534/1/output.umd.js`** -> AI Confidence: **99.17%**
2890. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-456/2/output.umd.js`** -> AI Confidence: **99.17%**
2891. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-4567/1/output.umd.js`** -> AI Confidence: **99.17%**
2892. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-4866/1/output.umd.js`** -> AI Confidence: **99.17%**
2893. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-962/output.umd.js`** -> AI Confidence: **99.17%**
2894. **`crates/swc_ecma_transforms_module/tests/fixture/common/lazy/export-default/output.umd.js`** -> AI Confidence: **99.17%**
2895. **`crates/swc_ecma_transforms_module/tests/fixture/common/lazy/whitelist/reexport-named/output.umd.js`** -> AI Confidence: **99.17%**
2896. **`crates/swc_ecma_transforms_module/tests/fixture/common/lazy/whitelist/reexport-namespace/output.umd.js`** -> AI Confidence: **99.17%**
2897. **`crates/swc_ecma_transforms_module/tests/fixture/common/regression/6733/output.umd.js`** -> AI Confidence: **99.17%**
2898. **`crates/swc_ecma_transforms_module/tests/fixture/common/strict/export-const/destructuring-array-default-params/output.umd.js`** -> AI Confidence: **99.17%**
2899. **`crates/swc_ecma_transforms_module/tests/fixture/common/strict/export-const/destructuring-array-rest/output.umd.js`** -> AI Confidence: **99.17%**
2900. **`crates/swc_ecma_transforms_module/tests/fixture/common/strict/export-const/destructuring-array/output.umd.js`** -> AI Confidence: **99.17%**
2901. **`crates/swc_ecma_transforms_module/tests/fixture/common/strict/export-const/destructuring-deep/output.umd.js`** -> AI Confidence: **99.17%**
2902. **`crates/swc_ecma_transforms_module/tests/fixture/common/strict/export-const/destructuring-object-default-params/output.umd.js`** -> AI Confidence: **99.17%**
2903. **`crates/swc_ecma_transforms_module/tests/fixture/common/strict/export-const/destructuring-object-rest/output.umd.js`** -> AI Confidence: **99.17%**
2904. **`crates/swc_ecma_transforms_module/tests/fixture/common/strict/export-const/destructuring-object/output.umd.js`** -> AI Confidence: **99.17%**
2905. **`crates/swc_ecma_transforms_module/tests/fixture/common/update-expression/negative-suffix/output.umd.js`** -> AI Confidence: **99.17%**
2906. **`crates/swc_ecma_transforms_module/tests/fixture/common/update-expression/positive-suffix/output.umd.js`** -> AI Confidence: **99.17%**
2907. **`crates/swc_ecma_transforms_optimization/tests/__swc_snapshots__/tests/simplify_dce.rs/deno_9212_2.js`** -> AI Confidence: **99.17%**
2908. **`crates/swc_ecma_transforms_optimization/tests/expr-simplifier/issue-3816/input.js`** -> AI Confidence: **99.17%**
2909. **`crates/swc_ecma_transforms_optimization/tests/expr-simplifier/issue-3816/output.js`** -> AI Confidence: **99.17%**
2910. **`crates/swc_ecma_transforms_proposal/tests/explicit-resource-management/exec-async/invalid-not-a-function.js`** -> AI Confidence: **99.17%**
2911. **`crates/swc_ecma_transforms_proposal/tests/explicit-resource-management/transform-await/switch/input.js`** -> AI Confidence: **99.17%**
2912. **`crates/swc_ecma_transforms_proposal/tests/explicit-resource-management/transform-sync/function-body/output.js`** -> AI Confidence: **99.17%**
2913. **`crates/swc_ecma_transforms_proposal/tests/explicit-resource-management/transform-sync/static-block/output.js`** -> AI Confidence: **99.17%**
2914. **`crates/swc_ecma_transforms_typescript/tests/__swc_snapshots__/tests/strip.rs/namespace_004.js`** -> AI Confidence: **99.17%**
2915. **`crates/swc_ecma_transforms_typescript/tests/fixture/issue-10097/output.js`** -> AI Confidence: **99.17%**
2916. **`crates/swc_es_semantics/tests/fixtures/cfg/labeled_break_continue/input.js`** -> AI Confidence: **99.17%**
2917. **`crates/swc_es_semantics/tests/fixtures/cfg/loop_shapes/input.js`** -> AI Confidence: **99.17%**
2918. **`crates/swc_es_semantics/tests/fixtures/cfg/switch_dispatch/input.js`** -> AI Confidence: **99.17%**
2919. **`crates/swc_es_semantics/tests/fixtures/cfg/try_finally_abrupt/input.js`** -> AI Confidence: **99.17%**
2920. **`crates/swc_es_semantics/tests/fixtures/scoping/switch_discriminant_order/input.js`** -> AI Confidence: **99.17%**
2921. **`crates/swc_node_bundler/tests/pass/helpers/simple/output/entry.js`** -> AI Confidence: **99.17%**
2922. **`crates/swc_node_bundler/tests/pass/issue-1328/case1/output/entry.js`** -> AI Confidence: **99.17%**
2923. **`crates/swc_sourcemap/tests/fixtures/ram_bundle/file_bundle_1/js-modules/3.js`** -> AI Confidence: **99.17%**
2924. **`packages/helpers/esm/_class_apply_descriptor_set.js`** -> AI Confidence: **99.17%**
2925. **`packages/helpers/esm/_jsx.js`** -> AI Confidence: **99.17%**
2926. **`packages/helpers/esm/_using.js`** -> AI Confidence: **99.17%**
2927. **`crates/swc_ecma_codegen/scripts/compare-file.sh`** -> AI Confidence: **99.17%**
2928. **`packages/core/scripts/cli_artifacts.sh`** -> AI Confidence: **99.17%**
2929. **`packages/html/scripts/cli_artifacts.sh`** -> AI Confidence: **99.17%**
2930. **`packages/minifier/scripts/cli_artifacts.sh`** -> AI Confidence: **99.17%**
2931. **`packages/react-compiler/scripts/cli_artifacts.sh`** -> AI Confidence: **99.17%**
2932. **`scripts/github/test-concurrent.sh`** -> AI Confidence: **99.17%**
2933. **`crates/swc_ecma_transforms/scripts/fixtures.py`** -> AI Confidence: **99.17%**
2934. **`crates/swc/tests/fixture/next.js/server/render/1/output/index.tsx`** -> AI Confidence: **99.16%**
2935. **`crates/swc_bundler/tests/deno-exec/deno-8224/haystack-core/input/filter/Node.ts`** -> AI Confidence: **99.16%**
2936. **`bindings/binding_core_node/src/bundle.rs`** -> AI Confidence: **99.16%**
2937. **`bindings/binding_core_node/src/parse.rs`** -> AI Confidence: **99.16%**
2938. **`bindings/binding_core_node/src/util.rs`** -> AI Confidence: **99.16%**
2939. **`bindings/binding_html_node/src/lib.rs`** -> AI Confidence: **99.16%**
2940. **`bindings/binding_minifier_node/src/util.rs`** -> AI Confidence: **99.16%**
2941. **`bindings/binding_typescript_wasm/src/lib.rs`** -> AI Confidence: **99.16%**
2942. **`crates/binding_macros/src/wasm.rs`** -> AI Confidence: **99.16%**
2943. **`crates/dbg-swc/src/bundle.rs`** -> AI Confidence: **99.16%**
2944. **`crates/dbg-swc/src/es/flow/strip.rs`** -> AI Confidence: **99.16%**
2945. **`crates/hstr/src/wtf8_atom.rs`** -> AI Confidence: **99.16%**
2946. **`crates/jsdoc/src/input.rs`** -> AI Confidence: **99.16%**
2947. **`crates/jsdoc/tests/fixture.rs`** -> AI Confidence: **99.16%**
2948. **`crates/preset_env_base/src/version.rs`** -> AI Confidence: **99.16%**
2949. **`crates/swc/benches/oxc.rs`** -> AI Confidence: **99.16%**
2950. **`crates/swc/src/builder.rs`** -> AI Confidence: **99.16%**
2951. **`crates/swc/src/config/mod.rs`** -> AI Confidence: **99.16%**
2952. **`crates/swc/src/plugin.rs`** -> AI Confidence: **99.16%**
2953. **`crates/swc/src/wasm_analysis.rs`** -> AI Confidence: **99.16%**
2954. **`crates/swc/tests/exec.rs`** -> AI Confidence: **99.16%**
2955. **`crates/swc/tests/flow_strip_hermes.rs`** -> AI Confidence: **99.16%**
2956. **`crates/swc/tests/tsc.rs`** -> AI Confidence: **99.16%**
2957. **`crates/swc_bundler/src/bundler/chunk/cjs.rs`** -> AI Confidence: **99.16%**
2958. **`crates/swc_bundler/src/bundler/chunk/computed_key.rs`** -> AI Confidence: **99.16%**
2959. **`crates/swc_bundler/src/bundler/chunk/merge.rs`** -> AI Confidence: **99.16%**
2960. **`crates/swc_bundler/src/bundler/chunk/mod.rs`** -> AI Confidence: **99.16%**
2961. **`crates/swc_bundler/src/bundler/import/mod.rs`** -> AI Confidence: **99.16%**
2962. **`crates/swc_bundler/src/bundler/load.rs`** -> AI Confidence: **99.16%**
2963. **`crates/swc_bundler/src/modules/sort/chunk.rs`** -> AI Confidence: **99.16%**
2964. **`crates/swc_bundler/src/util.rs`** -> AI Confidence: **99.16%**
2965. **`crates/swc_bundler/tests/common/mod.rs`** -> AI Confidence: **99.16%**
2966. **`crates/swc_common/src/errors/mod.rs`** -> AI Confidence: **99.16%**
2967. **`crates/swc_common/src/pos.rs`** -> AI Confidence: **99.16%**
2968. **`crates/swc_common/src/source_map.rs`** -> AI Confidence: **99.16%**
2969. **`crates/swc_common/src/syntax_pos.rs`** -> AI Confidence: **99.16%**
2970. **`crates/swc_compiler_base/src/lib.rs`** -> AI Confidence: **99.16%**
2971. **`crates/swc_compiler_base/src/source_map_scopes.rs`** -> AI Confidence: **99.16%**
2972. **`crates/swc_css_ast/src/base.rs`** -> AI Confidence: **99.16%**
2973. **`crates/swc_css_compat/src/compiler/color_hex_alpha.rs`** -> AI Confidence: **99.16%**
2974. **`crates/swc_css_compat/src/compiler/mod.rs`** -> AI Confidence: **99.16%**
2975. **`crates/swc_css_lints/src/config.rs`** -> AI Confidence: **99.16%**
2976. **`crates/swc_css_minifier/src/compressor/rules.rs`** -> AI Confidence: **99.16%**
2977. **`crates/swc_css_parser/src/parser/input.rs`** -> AI Confidence: **99.16%**
2978. **`crates/swc_ecma_ast/src/expr.rs`** -> AI Confidence: **99.16%**
2979. **`crates/swc_ecma_codegen/src/jsx.rs`** -> AI Confidence: **99.16%**
2980. **`crates/swc_ecma_codegen/src/text_writer/basic_impl.rs`** -> AI Confidence: **99.16%**
2981. **`crates/swc_ecma_compat_es2015/src/block_scoped_fn.rs`** -> AI Confidence: **99.16%**
2982. **`crates/swc_ecma_compat_es2015/src/block_scoping/vars.rs`** -> AI Confidence: **99.16%**
2983. **`crates/swc_ecma_compat_es2015/src/computed_props.rs`** -> AI Confidence: **99.16%**
2984. **`crates/swc_ecma_compat_es2015/src/destructuring.rs`** -> AI Confidence: **99.16%**
2985. **`crates/swc_ecma_compat_es2015/src/generator.rs`** -> AI Confidence: **99.16%**
2986. **`crates/swc_ecma_compat_es2022/src/class_properties/mod.rs`** -> AI Confidence: **99.16%**
2987. **`crates/swc_ecma_compat_es2022/src/class_properties/private_field.rs`** -> AI Confidence: **99.16%**
2988. **`crates/swc_ecma_compat_es2022/src/optional_chaining_impl.rs`** -> AI Confidence: **99.16%**
2989. **`crates/swc_ecma_lexer/src/common/lexer/mod.rs`** -> AI Confidence: **99.16%**
2990. **`crates/swc_ecma_lexer/src/common/parser/mod.rs`** -> AI Confidence: **99.16%**
2991. **`crates/swc_ecma_lexer/src/common/parser/output_type.rs`** -> AI Confidence: **99.16%**
2992. **`crates/swc_ecma_lexer/src/common/parser/util.rs`** -> AI Confidence: **99.16%**
2993. **`crates/swc_ecma_lexer/src/lexer/tests.rs`** -> AI Confidence: **99.16%**
2994. **`crates/swc_ecma_lexer/src/lib.rs`** -> AI Confidence: **99.16%**
2995. **`crates/swc_ecma_lints/src/config.rs`** -> AI Confidence: **99.16%**
2996. **`crates/swc_ecma_lints/src/rule.rs`** -> AI Confidence: **99.16%**
2997. **`crates/swc_ecma_lints/src/rules/critical_rules.rs`** -> AI Confidence: **99.16%**
2998. **`crates/swc_ecma_lints/src/rules/dot_notation.rs`** -> AI Confidence: **99.16%**
2999. **`crates/swc_ecma_lints/src/rules/eqeqeq.rs`** -> AI Confidence: **99.16%**
3000. **`crates/swc_ecma_lints/src/rules/no_bitwise.rs`** -> AI Confidence: **99.16%**
3001. **`crates/swc_ecma_lints/src/rules/no_loop_func.rs`** -> AI Confidence: **99.16%**
3002. **`crates/swc_ecma_lints/src/rules/no_new_object.rs`** -> AI Confidence: **99.16%**
3003. **`crates/swc_ecma_lints/src/rules/no_new_symbol.rs`** -> AI Confidence: **99.16%**
3004. **`crates/swc_ecma_lints/src/rules/no_prototype_builtins.rs`** -> AI Confidence: **99.16%**
3005. **`crates/swc_ecma_lints/src/rules/quotes.rs`** -> AI Confidence: **99.16%**
3006. **`crates/swc_ecma_lints/src/rules/symbol_description.rs`** -> AI Confidence: **99.16%**
3007. **`crates/swc_ecma_minifier/src/compress/optimize/arguments.rs`** -> AI Confidence: **99.16%**
3008. **`crates/swc_ecma_minifier/src/compress/optimize/mod.rs`** -> AI Confidence: **99.16%**
3009. **`crates/swc_ecma_minifier/src/compress/optimize/util.rs`** -> AI Confidence: **99.16%**
3010. **`crates/swc_ecma_minifier/src/compress/pure/mod.rs`** -> AI Confidence: **99.16%**
3011. **`crates/swc_ecma_minifier/src/compress/pure/strings.rs`** -> AI Confidence: **99.16%**
3012. **`crates/swc_ecma_minifier/src/compress/pure/vars.rs`** -> AI Confidence: **99.16%**
3013. **`crates/swc_ecma_minifier/src/pass/mangle_props.rs`** -> AI Confidence: **99.16%**
3014. **`crates/swc_ecma_minifier/src/usage_analyzer/analyzer/mod.rs`** -> AI Confidence: **99.16%**
3015. **`crates/swc_ecma_minifier/src/util/base54.rs`** -> AI Confidence: **99.16%**
3016. **`crates/swc_ecma_minifier/src/util/mod.rs`** -> AI Confidence: **99.16%**
3017. **`crates/swc_ecma_parser/src/lexer/state.rs`** -> AI Confidence: **99.16%**
3018. **`crates/swc_ecma_parser/src/parser/mod.rs`** -> AI Confidence: **99.16%**
3019. **`crates/swc_ecma_parser/tests/flow_hermes.rs`** -> AI Confidence: **99.16%**
3020. **`crates/swc_ecma_parser/tests/test262.rs`** -> AI Confidence: **99.16%**
3021. **`crates/swc_ecma_preset_env/src/lib.rs`** -> AI Confidence: **99.16%**
3022. **`crates/swc_ecma_quote_macros/src/ast/lit.rs`** -> AI Confidence: **99.16%**
3023. **`crates/swc_ecma_testing/src/lib.rs`** -> AI Confidence: **99.16%**
3024. **`crates/swc_ecma_transformer/src/es2018/object_rest_spread.rs`** -> AI Confidence: **99.16%**
3025. **`crates/swc_ecma_transforms_base/src/helpers/mod.rs`** -> AI Confidence: **99.16%**
3026. **`crates/swc_ecma_transforms_base/src/hygiene/tests.rs`** -> AI Confidence: **99.16%**
3027. **`crates/swc_ecma_transforms_base/src/rename/analyzer/scope.rs`** -> AI Confidence: **99.16%**
3028. **`crates/swc_ecma_transforms_base/src/resolver/mod.rs`** -> AI Confidence: **99.16%**
3029. **`crates/swc_ecma_transforms_base/tests/ts_resolver.rs`** -> AI Confidence: **99.16%**
3030. **`crates/swc_ecma_transforms_compat/tests/es2018_object_rest_spread.rs`** -> AI Confidence: **99.16%**
3031. **`crates/swc_ecma_transforms_macros/src/fast.rs`** -> AI Confidence: **99.16%**
3032. **`crates/swc_ecma_transforms_module/src/amd.rs`** -> AI Confidence: **99.16%**
3033. **`crates/swc_ecma_transforms_module/src/common_js.rs`** -> AI Confidence: **99.16%**
3034. **`crates/swc_ecma_transforms_module/src/umd.rs`** -> AI Confidence: **99.16%**
3035. **`crates/swc_ecma_transforms_module/src/util.rs`** -> AI Confidence: **99.16%**
3036. **`crates/swc_ecma_transforms_module/tests/amd.rs`** -> AI Confidence: **99.16%**
3037. **`crates/swc_ecma_transforms_module/tests/common_js.rs`** -> AI Confidence: **99.16%**
3038. **`crates/swc_ecma_transforms_optimization/src/const_modules.rs`** -> AI Confidence: **99.16%**
3039. **`crates/swc_ecma_transforms_optimization/src/inline_globals.rs`** -> AI Confidence: **99.16%**
3040. **`crates/swc_ecma_transforms_optimization/src/json_parse.rs`** -> AI Confidence: **99.16%**
3041. **`crates/swc_ecma_transforms_optimization/src/simplify/inlining/mod.rs`** -> AI Confidence: **99.16%**
3042. **`crates/swc_ecma_transforms_optimization/tests/simplify_dce.rs`** -> AI Confidence: **99.16%**
3043. **`crates/swc_ecma_transforms_proposal/src/decorators/mod.rs`** -> AI Confidence: **99.16%**
3044. **`crates/swc_ecma_transforms_proposal/tests/decorators.rs`** -> AI Confidence: **99.16%**
3045. **`crates/swc_ecma_transforms_react/src/refresh/hook.rs`** -> AI Confidence: **99.16%**
3046. **`crates/swc_ecma_transforms_react/src/refresh/mod.rs`** -> AI Confidence: **99.16%**
3047. **`crates/swc_ecma_transforms_typescript/src/semantic.rs`** -> AI Confidence: **99.16%**
3048. **`crates/swc_ecma_transforms_typescript/src/transform.rs`** -> AI Confidence: **99.16%**
3049. **`crates/swc_ecma_transforms_typescript/src/ts_enum.rs`** -> AI Confidence: **99.16%**
3050. **`crates/swc_ecma_transforms_typescript/tests/decorators_from_proposal.rs`** -> AI Confidence: **99.16%**
3051. **`crates/swc_ecma_transforms_typescript/tests/strip_correctness.rs`** -> AI Confidence: **99.16%**
3052. **`crates/swc_ecma_utils/src/function/fn_env_hoister.rs`** -> AI Confidence: **99.16%**
3053. **`crates/swc_eq_ignore_macros/src/lib.rs`** -> AI Confidence: **99.16%**
3054. **`crates/swc_error_reporters/src/diagnostic.rs`** -> AI Confidence: **99.16%**
3055. **`crates/swc_error_reporters/src/handler.rs`** -> AI Confidence: **99.16%**
3056. **`crates/swc_es_parser/benches/lexer.rs`** -> AI Confidence: **99.16%**
3057. **`crates/swc_es_parser/tests/comments.rs`** -> AI Confidence: **99.16%**
3058. **`crates/swc_es_parser/tests/js.rs`** -> AI Confidence: **99.16%**
3059. **`crates/swc_es_visit/src/lib.rs`** -> AI Confidence: **99.16%**
3060. **`crates/swc_estree_compat/src/babelify/class.rs`** -> AI Confidence: **99.16%**
3061. **`crates/swc_estree_compat/src/babelify/decl.rs`** -> AI Confidence: **99.16%**
3062. **`crates/swc_estree_compat/src/babelify/function.rs`** -> AI Confidence: **99.16%**
3063. **`crates/swc_estree_compat/src/babelify/lit.rs`** -> AI Confidence: **99.16%**
3064. **`crates/swc_estree_compat/src/babelify/prop.rs`** -> AI Confidence: **99.16%**
3065. **`crates/swc_estree_compat/src/babelify/stmt.rs`** -> AI Confidence: **99.16%**
3066. **`crates/swc_estree_compat/src/swcify/stmt.rs`** -> AI Confidence: **99.16%**
3067. **`crates/swc_estree_compat/src/swcify/typescript.rs`** -> AI Confidence: **99.16%**
3068. **`crates/swc_html_parser/src/parser/mod.rs`** -> AI Confidence: **99.16%**
3069. **`crates/swc_html_parser/tests/html5lib_tests.rs`** -> AI Confidence: **99.16%**
3070. **`crates/swc_node_bundler/src/loaders/swc.rs`** -> AI Confidence: **99.16%**
3071. **`crates/swc_node_bundler/tests/fixture.rs`** -> AI Confidence: **99.16%**
3072. **`crates/swc_plugin_backend_tests/tests/fixture/swc_internal_plugin/src/lib.rs`** -> AI Confidence: **99.16%**
3073. **`crates/swc_plugin_runner/src/cache.rs`** -> AI Confidence: **99.16%**
3074. **`crates/swc_sourcemap/src/builder.rs`** -> AI Confidence: **99.16%**
3075. **`crates/swc_sourcemap/src/decoder.rs`** -> AI Confidence: **99.16%**
3076. **`crates/swc_sourcemap/src/encoder.rs`** -> AI Confidence: **99.16%**
3077. **`crates/swc_sourcemap/src/hermes.rs`** -> AI Confidence: **99.16%**
3078. **`crates/swc_sourcemap/src/ram_bundle.rs`** -> AI Confidence: **99.16%**
3079. **`crates/swc_sourcemap/src/sourceview.rs`** -> AI Confidence: **99.16%**
3080. **`crates/swc_typescript/src/fast_dts/visitors/type_usage.rs`** -> AI Confidence: **99.16%**
3081. **`crates/swc_xml_parser/src/parser/mod.rs`** -> AI Confidence: **99.16%**
3082. **`crates/testing/src/lib.rs`** -> AI Confidence: **99.16%**
3083. **`crates/testing/src/output.rs`** -> AI Confidence: **99.16%**
3084. **`tools/generate-code/src/types.rs`** -> AI Confidence: **99.16%**
3085. **`crates/swc/tests/vercel/full/react-instantsearch/2/output/index.js`** -> AI Confidence: **99.16%**
3086. **`crates/swc/tests/vercel/loader-only/react-instantsearch/1/output/index.js`** -> AI Confidence: **99.16%**
3087. **`crates/swc_ecma_preset_env/tests/fixtures/corejs3/entry-require-all/output.js`** -> AI Confidence: **99.16%**
3088. **`crates/swc_ecma_preset_env/tests/fixtures/corejs3/entry-require-es-proposals/output.js`** -> AI Confidence: **99.16%**
3089. **`crates/swc_ecma_transforms_typescript/tests/fixture/next/server/render/1/output.js`** -> AI Confidence: **99.16%**
3090. **`packages/helpers/scripts/build.js`** -> AI Confidence: **99.16%**
3091. **`crates/swc/tests/fixture/sourcemap/012/input/CommentService.ts`** -> AI Confidence: **99.15%**
3092. **`crates/swc/tests/fixture/sourcemap/012/output/CommentService.ts`** -> AI Confidence: **99.15%**
3093. **`crates/swc_bundler/tests/deno-exec/deno-8224/haystack-core/input/core/HBool.ts`** -> AI Confidence: **99.15%**
3094. **`crates/swc_bundler/tests/deno-exec/deno-8224/haystack-core/input/core/HCoord.ts`** -> AI Confidence: **99.15%**
3095. **`crates/swc_bundler/tests/deno-exec/deno-8224/haystack-core/input/core/HDate.ts`** -> AI Confidence: **99.15%**
3096. **`crates/swc_bundler/tests/deno-exec/deno-8224/haystack-core/input/core/HRef.ts`** -> AI Confidence: **99.15%**
3097. **`crates/swc_bundler/tests/deno-exec/deno-8224/haystack-core/input/core/HTime.ts`** -> AI Confidence: **99.15%**
3098. **`crates/swc_bundler/tests/deno-exec/deno-8224/haystack-core/input/core/HUri.ts`** -> AI Confidence: **99.15%**
3099. **`crates/swc_bundler/tests/deno-exec/deno-8224/haystack-core/input/core/HVal.ts`** -> AI Confidence: **99.15%**
3100. **`bindings/binding_html_node/src/util.rs`** -> AI Confidence: **99.15%**
3101. **`bindings/binding_html_wasm/src/util.rs`** -> AI Confidence: **99.15%**
3102. **`crates/swc_arena/benches/bench.rs`** -> AI Confidence: **99.15%**
3103. **`crates/swc_arena/src/lib.rs`** -> AI Confidence: **99.15%**
3104. **`crates/swc_atoms/src/wtf8_atom.rs`** -> AI Confidence: **99.15%**
3105. **`crates/swc_bundler/src/bundler/keywords.rs`** -> AI Confidence: **99.15%**
3106. **`crates/swc_bundler/src/bundler/scope.rs`** -> AI Confidence: **99.15%**
3107. **`crates/swc_config/src/is_module.rs`** -> AI Confidence: **99.15%**
3108. **`crates/swc_config/src/source_map.rs`** -> AI Confidence: **99.15%**
3109. **`crates/swc_core/tests/integration.rs`** -> AI Confidence: **99.15%**
3110. **`crates/swc_css_lints/src/rules/at_rule_no_unknown.rs`** -> AI Confidence: **99.15%**
3111. **`crates/swc_css_lints/src/rules/color_hex_alpha.rs`** -> AI Confidence: **99.15%**
3112. **`crates/swc_css_lints/src/rules/declaration_no_important.rs`** -> AI Confidence: **99.15%**
3113. **`crates/swc_css_lints/src/rules/no_duplicate_at_import_rules.rs`** -> AI Confidence: **99.15%**
3114. **`crates/swc_css_lints/src/rules/unit_no_unknown.rs`** -> AI Confidence: **99.15%**
3115. **`crates/swc_ecma_ast/src/module.rs`** -> AI Confidence: **99.15%**
3116. **`crates/swc_ecma_lexer/src/common/parser/expr_ext.rs`** -> AI Confidence: **99.15%**
3117. **`crates/swc_ecma_lints/src/rules/constructor_super.rs`** -> AI Confidence: **99.15%**
3118. **`crates/swc_ecma_lints/src/rules/default_case_last.rs`** -> AI Confidence: **99.15%**
3119. **`crates/swc_ecma_lints/src/rules/no_compare_neg_zero.rs`** -> AI Confidence: **99.15%**
3120. **`crates/swc_ecma_lints/src/rules/no_empty_pattern.rs`** -> AI Confidence: **99.15%**
3121. **`crates/swc_ecma_lints/src/rules/no_new.rs`** -> AI Confidence: **99.15%**
3122. **`crates/swc_ecma_lints/src/rules/no_obj_calls.rs`** -> AI Confidence: **99.15%**
3123. **`crates/swc_ecma_lints/src/rules/no_sparse_arrays.rs`** -> AI Confidence: **99.15%**
3124. **`crates/swc_ecma_parser/src/error.rs`** -> AI Confidence: **99.15%**
3125. **`crates/swc_ecma_preset_env/src/node_colon_prefix_strip.rs`** -> AI Confidence: **99.15%**
3126. **`crates/swc_ecma_preset_env/src/transform_data.rs`** -> AI Confidence: **99.15%**
3127. **`crates/swc_ecma_regexp/src/parser/parser_impl.rs`** -> AI Confidence: **99.15%**
3128. **`crates/swc_ecma_transformer/src/es2015/duplicate_keys.rs`** -> AI Confidence: **99.15%**
3129. **`crates/swc_ecma_transformer/src/es2015/instanceof.rs`** -> AI Confidence: **99.15%**
3130. **`crates/swc_ecma_transformer/src/es2015/typeof_symbol.rs`** -> AI Confidence: **99.15%**
3131. **`crates/swc_ecma_transformer/src/es2016/exponentiation_operator.rs`** -> AI Confidence: **99.15%**
3132. **`crates/swc_ecma_transforms_module/src/rewriter/import_rewriter_typescript.rs`** -> AI Confidence: **99.15%**
3133. **`crates/swc_ecma_transforms_optimization/src/simplify/const_propagation.rs`** -> AI Confidence: **99.15%**
3134. **`crates/swc_ecma_transforms_optimization/tests/const_modules.rs`** -> AI Confidence: **99.15%**
3135. **`crates/swc_ecma_utils/src/ident.rs`** -> AI Confidence: **99.15%**
3136. **`crates/swc_es_parser/tests/jsx.rs`** -> AI Confidence: **99.15%**
3137. **`crates/swc_html_codegen/src/writer/basic.rs`** -> AI Confidence: **99.15%**
3138. **`crates/swc_xml_codegen/src/writer/basic.rs`** -> AI Confidence: **99.15%**
3139. **`crates/swc_ecma_minifier/tests/fixture/issues/react-instancesearch/002/input.js`** -> AI Confidence: **99.15%**
3140. **`crates/swc_ecma_minifier/tests/fixture/issues/react-instancesearch/002/output.js`** -> AI Confidence: **99.15%**
3141. **`crates/swc_ecma_minifier/tests/fixture/issues/react-instancesearch/004/output.js`** -> AI Confidence: **99.15%**
3142. **`packages/helpers/scripts/ast_grep.js`** -> AI Confidence: **99.15%**
3143. **`crates/swc/tests/fixture/issues-3xxx/3067/umd/output/src/index.ts`** -> AI Confidence: **99.13%**
3144. **`crates/swc_bundler/tests/deno-exec/deno-8224/haystack-core/input/core/TrioWriter.ts`** -> AI Confidence: **99.13%**
3145. **`crates/swc_bundler/tests/deno-exec/deno-8224/haystack-core/input/filter/GenerateHaystackFilterV3Visitor.ts`** -> AI Confidence: **99.13%**
3146. **`crates/swc_node_bundler/tests/pass/deno-001/full/input/http/_io.ts`** -> AI Confidence: **99.13%**
3147. **`crates/swc_node_bundler/tests/pass/deno-001/full/input/http/server.ts`** -> AI Confidence: **99.13%**
3148. **`crates/swc_css_compat/src/compiler/selector_not.rs`** -> AI Confidence: **99.13%**
3149. **`crates/swc_css_minifier/src/compressor/declaration.rs`** -> AI Confidence: **99.13%**
3150. **`crates/swc_css_minifier/src/compressor/selector.rs`** -> AI Confidence: **99.13%**
3151. **`crates/swc_css_minifier/src/compressor/supports.rs`** -> AI Confidence: **99.13%**
3152. **`crates/swc_ecma_codegen/src/typescript.rs`** -> AI Confidence: **99.13%**
3153. **`crates/swc_ecma_minifier/src/compress/optimize/static_alias.rs`** -> AI Confidence: **99.13%**
3154. **`crates/swc_ecma_minifier/src/util/size.rs`** -> AI Confidence: **99.13%**
3155. **`crates/swc_ecma_parser/src/lexer/whitespace.rs`** -> AI Confidence: **99.13%**
3156. **`crates/swc_ecma_regexp/src/parser/pattern_parser/state.rs`** -> AI Confidence: **99.13%**
3157. **`crates/swc_html_parser/src/parser/open_elements_stack.rs`** -> AI Confidence: **99.13%**
3158. **`crates/swc/tests/fixture/issues-1xxx/1333/case2/input/index.js`** -> AI Confidence: **99.13%**
3159. **`crates/swc/tests/tsc-references/awaitUsingDeclarations.1(target=es2015).1.normal.js`** -> AI Confidence: **99.13%**
3160. **`crates/swc/tests/tsc-references/decoratorMetadata.2.minified.js`** -> AI Confidence: **99.13%**
3161. **`crates/swc/tests/tsc-references/emitter.forAwait(target=es5).1.normal.js`** -> AI Confidence: **99.13%**
3162. **`crates/swc/tests/tsc-references/usingDeclarationsInForAwaitOf(target=es5).1.normal.js`** -> AI Confidence: **99.13%**
3163. **`crates/swc/tests/vercel/full/react-autosuggest/1/output/index.js`** -> AI Confidence: **99.13%**
3164. **`crates/swc/tests/vercel/full/utf8-1/output/index.js`** -> AI Confidence: **99.13%**
3165. **`crates/swc_ecma_minifier/tests/fixture/next/41527/1/output.js`** -> AI Confidence: **99.13%**
3166. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop-node/overview/output.umd.js`** -> AI Confidence: **99.13%**
3167. **`crates/swc_ecma_transforms_module/tests/fixture/common/interop/overview/output.umd.js`** -> AI Confidence: **99.13%**
3168. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-5260/output.umd.js`** -> AI Confidence: **99.13%**
3169. **`crates/swc/tests/fixture/issues-3xxx/3067/umd/output/src/inner/a/index.ts`** -> AI Confidence: **99.11%**
3170. **`crates/swc/tests/fixture/issues-3xxx/3067/umd/output/src/inner/b/index.ts`** -> AI Confidence: **99.11%**
3171. **`crates/swc_bundler/tests/fixture/deno-9212/case1/output/entry.inlined.ts`** -> AI Confidence: **99.11%**
3172. **`crates/swc_bundler/tests/fixture/deno-9212/case1/output/entry.ts`** -> AI Confidence: **99.11%**
3173. **`crates/swc_bundler/tests/fixture/deno-9591/output/entry.inlined.ts`** -> AI Confidence: **99.11%**
3174. **`crates/swc_bundler/tests/fixture/deno-9591/output/entry.ts`** -> AI Confidence: **99.11%**
3175. **`crates/swc_ecma_parser/tests/tsc/propertyAccessChain.ts`** -> AI Confidence: **99.11%**
3176. **`crates/swc_ecma_transforms_module/tests/fixture/common/amd-triple-slash-directive/1/output.umd.ts`** -> AI Confidence: **99.11%**
3177. **`crates/swc_ecma_transforms_module/tests/fixture/common/amd-triple-slash-directive/2/output.umd.ts`** -> AI Confidence: **99.11%**
3178. **`crates/swc_ecma_transforms_module/tests/fixture/common/amd-triple-slash-directive/3/output.umd.ts`** -> AI Confidence: **99.11%**
3179. **`crates/swc_ecma_transforms_module/tests/fixture/common/amd-triple-slash-directive/4/output.umd.ts`** -> AI Confidence: **99.11%**
3180. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-5042/3/output.umd.ts`** -> AI Confidence: **99.11%**
3181. **`crates/swc_ecma_compat_es2015/src/parameters.rs`** -> AI Confidence: **99.11%**
3182. **`crates/swc/tests/tsc-references/ES3For-ofTypeCheck1.2.minified.js`** -> AI Confidence: **99.11%**
3183. **`crates/swc/tests/tsc-references/ES3For-ofTypeCheck4.2.minified.js`** -> AI Confidence: **99.11%**
3184. **`crates/swc/tests/tsc-references/ES3For-ofTypeCheck6.2.minified.js`** -> AI Confidence: **99.11%**
3185. **`crates/swc/tests/tsc-references/ES5For-of24.2.minified.js`** -> AI Confidence: **99.11%**
3186. **`crates/swc/tests/tsc-references/ES5For-of25.2.minified.js`** -> AI Confidence: **99.11%**
3187. **`crates/swc/tests/tsc-references/ES5For-ofTypeCheck1.2.minified.js`** -> AI Confidence: **99.11%**
3188. **`crates/swc/tests/tsc-references/ES5For-ofTypeCheck11.2.minified.js`** -> AI Confidence: **99.11%**
3189. **`crates/swc/tests/tsc-references/ES5For-ofTypeCheck12.2.minified.js`** -> AI Confidence: **99.11%**
3190. **`crates/swc/tests/tsc-references/ES5For-ofTypeCheck14.2.minified.js`** -> AI Confidence: **99.11%**
3191. **`crates/swc/tests/tsc-references/ES5For-ofTypeCheck3.2.minified.js`** -> AI Confidence: **99.11%**
3192. **`crates/swc/tests/tsc-references/ES5For-ofTypeCheck4.2.minified.js`** -> AI Confidence: **99.11%**
3193. **`crates/swc/tests/tsc-references/ES5For-ofTypeCheck5.2.minified.js`** -> AI Confidence: **99.11%**
3194. **`crates/swc/tests/tsc-references/ES5For-ofTypeCheck6.2.minified.js`** -> AI Confidence: **99.11%**
3195. **`crates/swc/tests/tsc-references/ES5For-ofTypeCheck7.2.minified.js`** -> AI Confidence: **99.11%**
3196. **`crates/swc/tests/tsc-references/ES5For-ofTypeCheck8.2.minified.js`** -> AI Confidence: **99.11%**
3197. **`crates/swc/tests/tsc-references/ES5For-ofTypeCheck9.2.minified.js`** -> AI Confidence: **99.11%**
3198. **`crates/swc/tests/tsc-references/assignmentTypeNarrowing.2.minified.js`** -> AI Confidence: **99.11%**
3199. **`crates/swc/tests/tsc-references/classStaticBlock24(module=umd).2.minified.js`** -> AI Confidence: **99.11%**
3200. **`crates/swc/tests/tsc-references/controlFlowTruthiness.1.normal.js`** -> AI Confidence: **99.11%**
3201. **`crates/swc/tests/tsc-references/exportClassNameWithObjectUMD.2.minified.js`** -> AI Confidence: **99.11%**
3202. **`crates/swc/tests/tsc-references/exportsAndImports4-es6.1.normal.js`** -> AI Confidence: **99.11%**
3203. **`crates/swc/tests/tsc-references/importCallExpressionInExportEqualsUMD.2.minified.js`** -> AI Confidence: **99.11%**
3204. **`crates/swc/tests/tsc-references/importCallExpressionInUMD3.1.normal.js`** -> AI Confidence: **99.11%**
3205. **`crates/swc/tests/tsc-references/parameterInitializersBackwardReferencing(target=es5).1.normal.js`** -> AI Confidence: **99.11%**
3206. **`crates/swc/tests/tsc-references/parserES5ForOfStatement10.2.minified.js`** -> AI Confidence: **99.11%**
3207. **`crates/swc/tests/tsc-references/parserES5ForOfStatement8.2.minified.js`** -> AI Confidence: **99.11%**
3208. **`crates/swc/tests/tsc-references/parserES5ForOfStatement9.2.minified.js`** -> AI Confidence: **99.11%**
3209. **`crates/swc/tests/tsc-references/stringLiteralTypesOverloads01.2.minified.js`** -> AI Confidence: **99.11%**
3210. **`crates/swc/tests/tsc-references/stringLiteralTypesOverloads02.2.minified.js`** -> AI Confidence: **99.11%**
3211. **`crates/swc/tests/tsc-references/useObjectValuesAndEntries2.2.minified.js`** -> AI Confidence: **99.11%**
3212. **`crates/swc_ecma_minifier/tests/fixture/issues/5846/output.js`** -> AI Confidence: **99.11%**
3213. **`crates/swc_ecma_minifier/tests/fixture/projects/jquery/28/input.js`** -> AI Confidence: **99.11%**
3214. **`crates/swc_ecma_minifier/tests/fixture/projects/jquery/4/input.js`** -> AI Confidence: **99.11%**
3215. **`crates/swc_ecma_minifier/tests/fixture/projects/yui/13/output.js`** -> AI Confidence: **99.11%**
3216. **`crates/swc_ecma_minifier/tests/terser/compress/collapse_vars/cascade_statement/input.js`** -> AI Confidence: **99.11%**
3217. **`crates/swc_ecma_minifier/tests/terser/compress/collapse_vars/cascade_statement/output.js`** -> AI Confidence: **99.11%**
3218. **`crates/swc_ecma_minifier/tests/terser/compress/collapse_vars/cascade_statement/output.mangleOnly.js`** -> AI Confidence: **99.11%**
3219. **`crates/swc_ecma_minifier/tests/terser/compress/collapse_vars/cascade_statement/output.terser.js`** -> AI Confidence: **99.11%**
3220. **`crates/swc_ecma_minifier/tests/terser/compress/collapse_vars/issue_2497/output.js`** -> AI Confidence: **99.11%**
3221. **`crates/swc_ecma_minifier/tests/terser/compress/collapse_vars/issue_2497/output.terser.js`** -> AI Confidence: **99.11%**
3222. **`crates/swc_ecma_minifier/tests/terser/compress/dead_code/dead_code_constant_boolean_should_warn_more/input.js`** -> AI Confidence: **99.11%**
3223. **`crates/swc_ecma_minifier/tests/terser/compress/dead_code/dead_code_constant_boolean_should_warn_more/output.mangleOnly.js`** -> AI Confidence: **99.11%**
3224. **`crates/swc_ecma_transforms_base/src/helpers/_ts_values.js`** -> AI Confidence: **99.11%**
3225. **`crates/swc_ecma_transforms_compat/tests/__swc_snapshots__/tests/es2015_for_of.rs/spec_member_expr.js`** -> AI Confidence: **99.11%**
3226. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-2211/2/output.umd.js`** -> AI Confidence: **99.11%**
3227. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-2344/1/output.umd.js`** -> AI Confidence: **99.11%**
3228. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-4253/output.umd.js`** -> AI Confidence: **99.11%**
3229. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-5157/1/output.umd.js`** -> AI Confidence: **99.11%**
3230. **`packages/helpers/esm/_object_without_properties.js`** -> AI Confidence: **99.11%**
3231. **`scripts/patch-project.sh`** -> AI Confidence: **99.11%**
3232. **`crates/swc/tests/deno-unit/unit_tests.ts`** -> AI Confidence: **99.09%**
3233. **`crates/swc/tests/fixture/issues-5xxx/5644/input/index.ts`** -> AI Confidence: **99.09%**
3234. **`crates/swc/tests/fixture/issues-5xxx/5644/output/index.ts`** -> AI Confidence: **99.09%**
3235. **`crates/swc/tests/fixture/sourcemap/013/input/PistController.ts`** -> AI Confidence: **99.09%**
3236. **`crates/swc/tests/typescript/rewrite-relative-import-specifier/ts-emit/input/no.ts`** -> AI Confidence: **99.09%**
3237. **`crates/swc/tests/typescript/rewrite-relative-import-specifier/ts-emit/output/no.ts`** -> AI Confidence: **99.09%**
3238. **`crates/swc_bundler/tests/deno-exec/deno-8224/all/entry.ts`** -> AI Confidence: **99.09%**
3239. **`crates/swc_bundler/tests/deno-exec/deno-8224/haystack-core/input/core/UnitDatabase.ts`** -> AI Confidence: **99.09%**
3240. **`crates/swc_bundler/tests/deno-exec/deno-8224/haystack-core/input/index.ts`** -> AI Confidence: **99.09%**
3241. **`crates/swc_bundler/tests/deno-exec/deno-8224/haystack-core/input/shorthand.ts`** -> AI Confidence: **99.09%**
3242. **`crates/swc_ecma_parser/tests/tsc/allowImportingTsExtensions.ts`** -> AI Confidence: **99.09%**
3243. **`crates/swc_ecma_parser/tests/tsc/jsDeclarationsExportForms.ts`** -> AI Confidence: **99.09%**
3244. **`crates/swc_node_bundler/tests/pass/deno-001/full/input/textproto/mod.ts`** -> AI Confidence: **99.09%**
3245. **`crates/swc_node_bundler/tests/pass/deno-001/simple-1/input/http/server.ts`** -> AI Confidence: **99.09%**
3246. **`crates/swc_allocator/src/allocators/arena.rs`** -> AI Confidence: **99.09%**
3247. **`crates/swc_bundler/src/hash.rs`** -> AI Confidence: **99.09%**
3248. **`crates/swc_bundler/src/lib.rs`** -> AI Confidence: **99.09%**
3249. **`crates/swc_common/src/lib.rs`** -> AI Confidence: **99.09%**
3250. **`crates/swc_compiler_base/tests/source_map_scopes.rs`** -> AI Confidence: **99.09%**
3251. **`crates/swc_core/src/lib.rs`** -> AI Confidence: **99.09%**
3252. **`crates/swc_css_ast/src/selector.rs`** -> AI Confidence: **99.09%**
3253. **`crates/swc_css_compat/tests/fixture.rs`** -> AI Confidence: **99.09%**
3254. **`crates/swc_css_minifier/src/compressor/length.rs`** -> AI Confidence: **99.09%**
3255. **`crates/swc_css_minifier/tests/fixture.rs`** -> AI Confidence: **99.09%**
3256. **`crates/swc_css_parser/src/lib.rs`** -> AI Confidence: **99.09%**
3257. **`crates/swc_css_parser/src/parser/syntax/mod.rs`** -> AI Confidence: **99.09%**
3258. **`crates/swc_css_prefixer/tests/prefixer.rs`** -> AI Confidence: **99.09%**
3259. **`crates/swc_ecma_ast/src/class.rs`** -> AI Confidence: **99.09%**
3260. **`crates/swc_ecma_ast/src/typescript.rs`** -> AI Confidence: **99.09%**
3261. **`crates/swc_ecma_codegen/src/comments.rs`** -> AI Confidence: **99.09%**
3262. **`crates/swc_ecma_codegen/src/tests.rs`** -> AI Confidence: **99.09%**
3263. **`crates/swc_ecma_lexer/src/input.rs`** -> AI Confidence: **99.09%**
3264. **`crates/swc_ecma_lexer/src/utils.rs`** -> AI Confidence: **99.09%**
3265. **`crates/swc_ecma_minifier/examples/compress.rs`** -> AI Confidence: **99.09%**
3266. **`crates/swc_ecma_minifier/examples/minifier.rs`** -> AI Confidence: **99.09%**
3267. **`crates/swc_ecma_minifier/fuzz/fuzz_targets/bug.rs`** -> AI Confidence: **99.09%**
3268. **`crates/swc_ecma_minifier/src/metadata/tests.rs`** -> AI Confidence: **99.09%**
3269. **`crates/swc_ecma_minifier/tests/format.rs`** -> AI Confidence: **99.09%**
3270. **`crates/swc_ecma_parser/benches/parser.rs`** -> AI Confidence: **99.09%**
3271. **`crates/swc_ecma_parser/src/lib.rs`** -> AI Confidence: **99.09%**
3272. **`crates/swc_ecma_parser/tests/span.rs`** -> AI Confidence: **99.09%**
3273. **`crates/swc_ecma_transforms/src/lib.rs`** -> AI Confidence: **99.09%**
3274. **`crates/swc_ecma_transforms/tests/decorators.rs`** -> AI Confidence: **99.09%**
3275. **`crates/swc_ecma_transforms/tests/deno.rs`** -> AI Confidence: **99.09%**
3276. **`crates/swc_ecma_transforms_compat/src/lib.rs`** -> AI Confidence: **99.09%**
3277. **`crates/swc_ecma_transforms_compat/tests/es2015_classes.rs`** -> AI Confidence: **99.09%**
3278. **`crates/swc_ecma_transforms_module/tests/path_node.rs`** -> AI Confidence: **99.09%**
3279. **`crates/swc_ecma_transforms_module/tests/system_js.rs`** -> AI Confidence: **99.09%**
3280. **`crates/swc_ecma_transforms_optimization/tests/fixture.rs`** -> AI Confidence: **99.09%**
3281. **`crates/swc_ecma_transforms_proposal/tests/explicit_resource_management.rs`** -> AI Confidence: **99.09%**
3282. **`crates/swc_ecma_transforms_react/src/lib.rs`** -> AI Confidence: **99.09%**
3283. **`crates/swc_ecma_transforms_typescript/benches/compat.rs`** -> AI Confidence: **99.09%**
3284. **`crates/swc_ecma_transforms_typescript/examples/ts_to_js.rs`** -> AI Confidence: **99.09%**
3285. **`crates/swc_error_reporters/examples/swc_try.rs`** -> AI Confidence: **99.09%**
3286. **`crates/swc_error_reporters/tests/fixture.rs`** -> AI Confidence: **99.09%**
3287. **`crates/swc_es_ast/src/decl.rs`** -> AI Confidence: **99.09%**
3288. **`crates/swc_es_ast/src/expr.rs`** -> AI Confidence: **99.09%**
3289. **`crates/swc_es_ast/src/lib.rs`** -> AI Confidence: **99.09%**
3290. **`crates/swc_es_ast/src/store.rs`** -> AI Confidence: **99.09%**
3291. **`crates/swc_es_ast/tests/serde.rs`** -> AI Confidence: **99.09%**
3292. **`crates/swc_es_ast/tests/store.rs`** -> AI Confidence: **99.09%**
3293. **`crates/swc_es_minifier/benches/with_parse.rs`** -> AI Confidence: **99.09%**
3294. **`crates/swc_es_minifier/tests/common.rs`** -> AI Confidence: **99.09%**
3295. **`crates/swc_es_minifier/tests/no_ecma_dependency.rs`** -> AI Confidence: **99.09%**
3296. **`crates/swc_es_minifier/tests/regression.rs`** -> AI Confidence: **99.09%**
3297. **`crates/swc_es_parser/src/lib.rs`** -> AI Confidence: **99.09%**
3298. **`crates/swc_es_parser/tests/no_ecma_dependency.rs`** -> AI Confidence: **99.09%**
3299. **`crates/swc_es_transforms/benches/with_parse.rs`** -> AI Confidence: **99.09%**
3300. **`crates/swc_es_transforms/tests/no_ecma_dependency.rs`** -> AI Confidence: **99.09%**
3301. **`crates/swc_es_visit/tests/visit.rs`** -> AI Confidence: **99.09%**
3302. **`crates/swc_estree_ast/src/common.rs`** -> AI Confidence: **99.09%**
3303. **`crates/swc_estree_ast/src/decl.rs`** -> AI Confidence: **99.09%**
3304. **`crates/swc_estree_ast/src/expr.rs`** -> AI Confidence: **99.09%**
3305. **`crates/swc_estree_ast/src/flow.rs`** -> AI Confidence: **99.09%**
3306. **`crates/swc_estree_ast/src/lib.rs`** -> AI Confidence: **99.09%**
3307. **`crates/swc_estree_ast/src/module.rs`** -> AI Confidence: **99.09%**
3308. **`crates/swc_estree_ast/src/pat.rs`** -> AI Confidence: **99.09%**
3309. **`crates/swc_estree_ast/src/stmt.rs`** -> AI Confidence: **99.09%**
3310. **`crates/swc_estree_ast/src/typescript.rs`** -> AI Confidence: **99.09%**
3311. **`crates/swc_html_minifier/src/option.rs`** -> AI Confidence: **99.09%**
3312. **`crates/swc_html_parser/benches/parser.rs`** -> AI Confidence: **99.09%**
3313. **`crates/swc_html_parser/src/lib.rs`** -> AI Confidence: **99.09%**
3314. **`crates/swc_macros_common/src/prelude.rs`** -> AI Confidence: **99.09%**
3315. **`crates/swc_plugin_backend_tests/benches/ecma_invoke.rs`** -> AI Confidence: **99.09%**
3316. **`crates/swc_plugin_runner/src/imported_fn/mod.rs`** -> AI Confidence: **99.09%**
3317. **`crates/swc_sourcemap/src/lib.rs`** -> AI Confidence: **99.09%**
3318. **`crates/swc/tests/errors/lints/const-assign/2/input.js`** -> AI Confidence: **99.09%**
3319. **`crates/swc/tests/fixture/interop/node/output/index.js`** -> AI Confidence: **99.09%**
3320. **`crates/swc/tests/fixture/issues-11xxx/11046/es5/output/index.js`** -> AI Confidence: **99.09%**
3321. **`crates/swc/tests/tsc-references/awaitUsingDeclarations.1(target=es2015).2.minified.js`** -> AI Confidence: **99.09%**
3322. **`crates/swc/tests/tsc-references/exportAsNamespace3(module=umd).2.minified.js`** -> AI Confidence: **99.09%**
3323. **`crates/swc/tests/tsc-references/forStatementsMultipleInvalidDecl.2.minified.js`** -> AI Confidence: **99.09%**
3324. **`crates/swc/tests/tsc-references/generatedContextualTyping.2.minified.js`** -> AI Confidence: **99.09%**
3325. **`crates/swc/tests/tsc-references/importCallExpressionES5UMD.2.minified.js`** -> AI Confidence: **99.09%**
3326. **`crates/swc/tests/tsc-references/importCallExpressionInUMD4.1.normal.js`** -> AI Confidence: **99.09%**
3327. **`crates/swc/tests/tsc-references/importCallExpressionInUMD4.2.minified.js`** -> AI Confidence: **99.09%**
3328. **`crates/swc/tests/tsc-references/parameterInitializersForwardReferencing.2(target=es5).1.normal.js`** -> AI Confidence: **99.09%**
3329. **`crates/swc/tests/tsc-references/usingDeclarations.1(target=es5).2.minified.js`** -> AI Confidence: **99.09%**
3330. **`crates/swc/tests/tsc-references/usingDeclarationsWithLegacyClassDecorators.1(module=commonjs,target=es2015).1.normal.js`** -> AI Confidence: **99.09%**
3331. **`crates/swc/tests/tsc-references/usingDeclarationsWithLegacyClassDecorators.1(module=commonjs,target=es2015).2.minified.js`** -> AI Confidence: **99.09%**
3332. **`crates/swc/tests/tsc-references/usingDeclarationsWithLegacyClassDecorators.1(module=commonjs,target=esnext).1.normal.js`** -> AI Confidence: **99.09%**
3333. **`crates/swc/tests/tsc-references/usingDeclarationsWithLegacyClassDecorators.1(module=commonjs,target=esnext).2.minified.js`** -> AI Confidence: **99.09%**
3334. **`crates/swc/tests/tsc-references/usingDeclarationsWithLegacyClassDecorators.10(module=commonjs,target=es2015).1.normal.js`** -> AI Confidence: **99.09%**
3335. **`crates/swc/tests/tsc-references/usingDeclarationsWithLegacyClassDecorators.10(module=commonjs,target=es2015).2.minified.js`** -> AI Confidence: **99.09%**
3336. **`crates/swc/tests/tsc-references/usingDeclarationsWithLegacyClassDecorators.10(module=commonjs,target=esnext).1.normal.js`** -> AI Confidence: **99.09%**
3337. **`crates/swc/tests/tsc-references/usingDeclarationsWithLegacyClassDecorators.10(module=commonjs,target=esnext).2.minified.js`** -> AI Confidence: **99.09%**
3338. **`crates/swc/tests/tsc-references/usingDeclarationsWithLegacyClassDecorators.3(module=commonjs,target=es2015).1.normal.js`** -> AI Confidence: **99.09%**
3339. **`crates/swc/tests/tsc-references/usingDeclarationsWithLegacyClassDecorators.3(module=commonjs,target=es2015).2.minified.js`** -> AI Confidence: **99.09%**
3340. **`crates/swc/tests/tsc-references/usingDeclarationsWithLegacyClassDecorators.3(module=commonjs,target=esnext).1.normal.js`** -> AI Confidence: **99.09%**
3341. **`crates/swc/tests/tsc-references/usingDeclarationsWithLegacyClassDecorators.3(module=commonjs,target=esnext).2.minified.js`** -> AI Confidence: **99.09%**
3342. **`crates/swc/tests/tsc-references/usingDeclarationsWithLegacyClassDecorators.4(module=commonjs,target=es2015).1.normal.js`** -> AI Confidence: **99.09%**
3343. **`crates/swc/tests/tsc-references/usingDeclarationsWithLegacyClassDecorators.4(module=commonjs,target=es2015).2.minified.js`** -> AI Confidence: **99.09%**
3344. **`crates/swc/tests/tsc-references/usingDeclarationsWithLegacyClassDecorators.4(module=commonjs,target=esnext).1.normal.js`** -> AI Confidence: **99.09%**
3345. **`crates/swc/tests/tsc-references/usingDeclarationsWithLegacyClassDecorators.4(module=commonjs,target=esnext).2.minified.js`** -> AI Confidence: **99.09%**
3346. **`crates/swc/tests/tsc-references/usingDeclarationsWithLegacyClassDecorators.7(module=commonjs,target=es2015).1.normal.js`** -> AI Confidence: **99.09%**
3347. **`crates/swc/tests/tsc-references/usingDeclarationsWithLegacyClassDecorators.7(module=commonjs,target=es2015).2.minified.js`** -> AI Confidence: **99.09%**
3348. **`crates/swc/tests/tsc-references/usingDeclarationsWithLegacyClassDecorators.7(module=commonjs,target=esnext).1.normal.js`** -> AI Confidence: **99.09%**
3349. **`crates/swc/tests/tsc-references/usingDeclarationsWithLegacyClassDecorators.7(module=commonjs,target=esnext).2.minified.js`** -> AI Confidence: **99.09%**
3350. **`crates/swc/tests/tsc-references/usingDeclarationsWithLegacyClassDecorators.9(module=commonjs,target=es2015).1.normal.js`** -> AI Confidence: **99.09%**
3351. **`crates/swc/tests/tsc-references/usingDeclarationsWithLegacyClassDecorators.9(module=commonjs,target=es2015).2.minified.js`** -> AI Confidence: **99.09%**
3352. **`crates/swc/tests/tsc-references/usingDeclarationsWithLegacyClassDecorators.9(module=commonjs,target=esnext).1.normal.js`** -> AI Confidence: **99.09%**
3353. **`crates/swc/tests/tsc-references/usingDeclarationsWithLegacyClassDecorators.9(module=commonjs,target=esnext).2.minified.js`** -> AI Confidence: **99.09%**
3354. **`crates/swc/tests/tsc-references/verbatimModuleSyntaxRestrictionsESM.1.normal.js`** -> AI Confidence: **99.09%**
3355. **`crates/swc/tests/vercel/full/utf8-1/input/index.js`** -> AI Confidence: **99.09%**
3356. **`crates/swc_ecma_minifier/tests/fixture/issues/typescript/1/input.js`** -> AI Confidence: **99.09%**
3357. **`crates/swc_ecma_transforms_module/tests/fixture/common/ignore-dynamic/1/output.umd.js`** -> AI Confidence: **99.09%**
3358. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-11662/output.umd.js`** -> AI Confidence: **99.09%**
3359. **`crates/swc_ecma_transforms_module/tests/fixture/common/issue-5054/1/output.cjs`** -> AI Confidence: **99.09%**
3360. **`scripts/github/get-test-matrix.mjs`** -> AI Confidence: **99.09%**
3361. **`crates/swc_ecma_transforms/scripts/del.py`** -> AI Confidence: **99.09%**
3362. **`crates/swc/tests/fixture/ecosystem-ci/1/input/1.ts`** -> AI Confidence: **99.08%**
3363. **`crates/swc/tests/fixture/sourcemap/011/input/CommentControlller.ts`** -> AI Confidence: **99.08%**
3364. **`crates/swc/tests/fixture/sourcemap/011/output/CommentControlller.ts`** -> AI Confidence: **99.08%**
3365. **`crates/swc/tests/fixture/sourcemap/014/input/UserController.ts`** -> AI Confidence: **99.08%**
3366. **`crates/swc/tests/fixture/sourcemap/issue-3854/1-true/output/index.ts`** -> AI Confidence: **99.08%**
3367. **`crates/swc/tests/fixture/sourcemap/issue-3854/2-inline/output/index.ts`** -> AI Confidence: **99.08%**
3368. **`crates/swc_bundler/tests/deno-exec/deno-8224/haystack-core/input/core/HDateTime.ts`** -> AI Confidence: **99.08%**
3369. **`crates/swc_ecma_parser/tests/tsc/exportAssignTypes.ts`** -> AI Confidence: **99.08%**
3370. **`crates/swc_ts_fast_strip/tests/fixture/type-import-export.ts`** -> AI Confidence: **99.08%**
3371. **`bindings/binding_core_wasm/src/lib.rs`** -> AI Confidence: **99.08%**
3372. **`crates/dbg-swc/src/es/minifier/mod.rs`** -> AI Confidence: **99.08%**
3373. **`crates/hstr/src/dynamic.rs`** -> AI Confidence: **99.08%**
3374. **`crates/hstr/src/lib.rs`** -> AI Confidence: **99.08%**
3375. **`crates/swc/benches/bugs.rs`** -> AI Confidence: **99.08%**
3376. **`crates/swc/benches/isolated_declarations.rs`** -> AI Confidence: **99.08%**
3377. **`crates/swc/benches/minify.rs`** -> AI Confidence: **99.08%**
3378. **`crates/swc/examples/hygiene_visualizer.rs`** -> AI Confidence: **99.08%**
3379. **`crates/swc/src/dropped_comments_preserver.rs`** -> AI Confidence: **99.08%**
3380. **`crates/swc/tests/error_msg.rs`** -> AI Confidence: **99.08%**
3381. **`crates/swc/tests/rust_api.rs`** -> AI Confidence: **99.08%**
3382. **`crates/swc_bundler/examples/path.rs`** -> AI Confidence: **99.08%**
3383. **`crates/swc_bundler/src/bundler/chunk/plan/mod.rs`** -> AI Confidence: **99.08%**
3384. **`crates/swc_bundler/src/bundler/import/tests.rs`** -> AI Confidence: **99.08%**
3385. **`crates/swc_bundler/src/bundler/tests.rs`** -> AI Confidence: **99.08%**
3386. **`crates/swc_bundler/src/modules/mod.rs`** -> AI Confidence: **99.08%**
3387. **`crates/swc_bundler/src/modules/sort/mod.rs`** -> AI Confidence: **99.08%**
3388. **`crates/swc_bundler/tests/deno.rs`** -> AI Confidence: **99.08%**
3389. **`crates/swc_cli_impl/src/commands/mod.rs`** -> AI Confidence: **99.08%**
3390. **`crates/swc_common/src/errors/diagnostic.rs`** -> AI Confidence: **99.08%**
3391. **`crates/swc_common/src/private/mod.rs`** -> AI Confidence: **99.08%**
3392. **`crates/swc_common/tests/concurrent.rs`** -> AI Confidence: **99.08%**
3393. **`crates/swc_config/src/regex_js.rs`** -> AI Confidence: **99.08%**
3394. **`crates/swc_config_macro/src/merge.rs`** -> AI Confidence: **99.08%**
3395. **`crates/swc_core/tests/fixture/stub_wasm/src/lib.rs`** -> AI Confidence: **99.08%**
3396. **`crates/swc_css_ast/src/at_rule.rs`** -> AI Confidence: **99.08%**
3397. **`crates/swc_css_lints/src/rules/mod.rs`** -> AI Confidence: **99.08%**
3398. **`crates/swc_css_modules/tests/fixture.rs`** -> AI Confidence: **99.08%**
3399. **`crates/swc_css_modules/tests/with_compat.rs`** -> AI Confidence: **99.08%**
3400. **`crates/swc_css_parser/benches/compare.rs`** -> AI Confidence: **99.08%**
3401. **`crates/swc_css_parser/benches/parser.rs`** -> AI Confidence: **99.08%**
3402. **`crates/swc_css_parser/src/parser/mod.rs`** -> AI Confidence: **99.08%**
3403. **`crates/swc_css_parser/tests/fixture.rs`** -> AI Confidence: **99.08%**
3404. **`crates/swc_ecma_ast/src/decl.rs`** -> AI Confidence: **99.08%**
3405. **`crates/swc_ecma_ast/src/function.rs`** -> AI Confidence: **99.08%**
3406. **`crates/swc_ecma_ast/src/jsx.rs`** -> AI Confidence: **99.08%**
3407. **`crates/swc_ecma_ast/src/lib.rs`** -> AI Confidence: **99.08%**
3408. **`crates/swc_ecma_ast/src/module_decl.rs`** -> AI Confidence: **99.08%**
3409. **`crates/swc_ecma_ast/src/pat.rs`** -> AI Confidence: **99.08%**
3410. **`crates/swc_ecma_ast/src/prop.rs`** -> AI Confidence: **99.08%**
3411. **`crates/swc_ecma_ast/src/stmt.rs`** -> AI Confidence: **99.08%**
3412. **`crates/swc_ecma_compat_bugfixes/src/async_arrows_in_class.rs`** -> AI Confidence: **99.08%**
3413. **`crates/swc_ecma_compat_bugfixes/src/template_literal_caching.rs`** -> AI Confidence: **99.08%**
3414. **`crates/swc_ecma_compat_es2015/src/lib.rs`** -> AI Confidence: **99.08%**
3415. **`crates/swc_ecma_compat_es2015/src/new_target.rs`** -> AI Confidence: **99.08%**
3416. **`crates/swc_ecma_compat_es2020/src/lib.rs`** -> AI Confidence: **99.08%**
3417. **`crates/swc_ecma_compat_regexp/src/unicode_property.rs`** -> AI Confidence: **99.08%**
3418. **`crates/swc_ecma_hooks/tests/compose.rs`** -> AI Confidence: **99.08%**
3419. **`crates/swc_ecma_lexer/src/common/lexer/token.rs`** -> AI Confidence: **99.08%**
3420. **`crates/swc_ecma_lints/benches/all.rs`** -> AI Confidence: **99.08%**
3421. **`crates/swc_ecma_lints/src/rules/mod.rs`** -> AI Confidence: **99.08%**
3422. **`crates/swc_ecma_loader/tests/tsc_resolver.rs`** -> AI Confidence: **99.08%**
3423. **`crates/swc_ecma_minifier/examples/minify-all.rs`** -> AI Confidence: **99.08%**
3424. **`crates/swc_ecma_minifier/src/cli/bin.rs`** -> AI Confidence: **99.08%**
3425. **`crates/swc_ecma_minifier/src/debug.rs`** -> AI Confidence: **99.08%**
3426. **`crates/swc_ecma_minifier/src/option/mod.rs`** -> AI Confidence: **99.08%**
3427. **`crates/swc_ecma_minifier/src/pass/mangle_names/mod.rs`** -> AI Confidence: **99.08%**
3428. **`crates/swc_ecma_minifier/src/usage_analyzer/analyzer/storage.rs`** -> AI Confidence: **99.08%**
3429. **`crates/swc_ecma_minifier/tests/eval.rs`** -> AI Confidence: **99.08%**
3430. **`crates/swc_ecma_minifier/tests/mangle.rs`** -> AI Confidence: **99.08%**
3431. **`crates/swc_ecma_minifier/tests/size.rs`** -> AI Confidence: **99.08%**
3432. **`crates/swc_ecma_parser/benches/compare.rs`** -> AI Confidence: **99.08%**
3433. **`crates/swc_ecma_parser/tests/flow.rs`** -> AI Confidence: **99.08%**
3434. **`crates/swc_ecma_parser/tests/js.rs`** -> AI Confidence: **99.08%**
3435. **`crates/swc_ecma_preset_env/benches/polyfills.rs`** -> AI Confidence: **99.08%**
3436. **`crates/swc_ecma_quote_macros/src/builder.rs`** -> AI Confidence: **99.08%**
3437. **`crates/swc_ecma_regexp_ast/src/lib.rs`** -> AI Confidence: **99.08%**
3438. **`crates/swc_ecma_transformer/src/lib.rs`** -> AI Confidence: **99.08%**
3439. **`crates/swc_ecma_transforms/tests/es2015_function_name.rs`** -> AI Confidence: **99.08%**
3440. **`crates/swc_ecma_transforms_base/src/hygiene/mod.rs`** -> AI Confidence: **99.08%**
3441. **`crates/swc_ecma_transforms_base/src/rename/ops.rs`** -> AI Confidence: **99.08%**
3442. **`crates/swc_ecma_transforms_base/tests/fixture.rs`** -> AI Confidence: **99.08%**
3443. **`crates/swc_ecma_transforms_compat/tests/es2015_arrow.rs`** -> AI Confidence: **99.08%**
3444. **`crates/swc_ecma_transforms_compat/tests/es2015_destructuring.rs`** -> AI Confidence: **99.08%**
3445. **`crates/swc_ecma_transforms_compat/tests/es2015_generator.rs`** -> AI Confidence: **99.08%**
3446. **`crates/swc_ecma_transforms_compat/tests/es2015_generator_sparse_array.rs`** -> AI Confidence: **99.08%**
3447. **`crates/swc_ecma_transforms_compat/tests/es2015_object_super.rs`** -> AI Confidence: **99.08%**
3448. **`crates/swc_ecma_transforms_compat/tests/es2015_spread.rs`** -> AI Confidence: **99.08%**
3449. **`crates/swc_ecma_transforms_compat/tests/es2017_async_to_generator.rs`** -> AI Confidence: **99.08%**
3450. **`crates/swc_ecma_transforms_compat/tests/es2020_nullish_coalescing.rs`** -> AI Confidence: **99.08%**
3451. **`crates/swc_ecma_transforms_compat/tests/es2022_class_properties.rs`** -> AI Confidence: **99.08%**
3452. **`crates/swc_ecma_transforms_module/src/lib.rs`** -> AI Confidence: **99.08%**
3453. **`crates/swc_ecma_transforms_module/src/umd/config.rs`** -> AI Confidence: **99.08%**
3454. **`crates/swc_ecma_transforms_optimization/src/lib.rs`** -> AI Confidence: **99.08%**
3455. **`crates/swc_ecma_transforms_optimization/src/simplify/mod.rs`** -> AI Confidence: **99.08%**
3456. **`crates/swc_ecma_transforms_proposal/src/import_attributes.rs`** -> AI Confidence: **99.08%**
3457. **`crates/swc_ecma_transforms_react/src/jsx/tests.rs`** -> AI Confidence: **99.08%**
3458. **`crates/swc_ecma_transforms_react/src/pure_annotations/tests.rs`** -> AI Confidence: **99.08%**
3459. **`crates/swc_ecma_transforms_typescript/tests/strip.rs`** -> AI Confidence: **99.08%**
3460. **`crates/swc_ecmascript/src/lib.rs`** -> AI Confidence: **99.08%**
3461. **`crates/swc_error_reporters/src/lib.rs`** -> AI Confidence: **99.08%**
3462. **`crates/swc_es_ast/src/class.rs`** -> AI Confidence: **99.08%**
3463. **`crates/swc_es_ast/src/stmt.rs`** -> AI Confidence: **99.08%**
3464. **`crates/swc_es_minifier/src/engine.rs`** -> AI Confidence: **99.08%**
3465. **`crates/swc_es_parser/benches/parser.rs`** -> AI Confidence: **99.08%**
3466. **`crates/swc_es_parser/tests/smoke.rs`** -> AI Confidence: **99.08%**
3467. **`crates/swc_es_semantics/src/lib.rs`** -> AI Confidence: **99.08%**
3468. **`crates/swc_es_semantics/tests/common.rs`** -> AI Confidence: **99.08%**
3469. **`crates/swc_es_transforms/src/engine.rs`** -> AI Confidence: **99.08%**
3470. **`crates/swc_estree_ast/src/jsx.rs`** -> AI Confidence: **99.08%**
3471. **`crates/swc_estree_compat/benches/babelify.rs`** -> AI Confidence: **99.08%**
3472. **`crates/swc_estree_compat/src/swcify/lit.rs`** -> AI Confidence: **99.08%**
3473. **`crates/swc_html_minifier/benches/full.rs`** -> AI Confidence: **99.08%**
3474. **`crates/swc_html_minifier/tests/fixture.rs`** -> AI Confidence: **99.08%**
3475. **`crates/swc_html_parser/benches/compare.rs`** -> AI Confidence: **99.08%**
3476. **`crates/swc_node_bundler/src/v1/mod.rs`** -> AI Confidence: **99.08%**
3477. **`crates/swc_plugin_backend_tests/tests/ecma_rkyv.rs`** -> AI Confidence: **99.08%**
3478. **`crates/swc_plugin_runner/src/imported_fn/handler.rs`** -> AI Confidence: **99.08%**
3479. **`crates/swc_plugin_runner/src/imported_fn/source_map.rs`** -> AI Confidence: **99.08%**
3480. **`crates/swc_typescript/examples/isolated_declarations.rs`** -> AI Confidence: **99.08%**
3481. **`crates/swc_typescript/src/fast_dts/util/types.rs`** -> AI Confidence: **99.08%**
3482. **`crates/swc_typescript/tests/typescript.rs`** -> AI Confidence: **99.08%**
3483. **`crates/swc_xml_parser/src/lib.rs`** -> AI Confidence: **99.08%**
3484. **`crates/swc_xml_parser/tests/fixture.rs`** -> AI Confidence: **99.08%**
3485. **`crates/testing/src/string_errors.rs`** -> AI Confidence: **99.08%**
3486. **`xtask/src/main.rs`** -> AI Confidence: **99.08%**
3487. **`crates/swc/tests/fixture/issues-1xxx/1490/full/output/index.js`** -> AI Confidence: **99.08%**
3488. **`crates/swc/tests/fixture/issues-2xxx/2232/case1/output/index.js`** -> AI Confidence: **99.08%**
3489. **`crates/swc/tests/fixture/issues-6xxx/6984/1/output/index.js`** -> AI Confidence: **99.08%**
3490. **`crates/swc/tests/tsc-references/asyncMethodWithSuper_es5.1.normal.js`** -> AI Confidence: **99.08%**
3491. **`crates/swc/tests/tsc-references/emitter.asyncGenerators.classMethods.es5.1.normal.js`** -> AI Confidence: **99.08%**
3492. **`crates/swc/tests/tsc-references/errorSuperPropertyAccess.1.normal.js`** -> AI Confidence: **99.08%**
3493. **`crates/swc/tests/tsc-references/exportAssignTypes.1.normal.js`** -> AI Confidence: **99.08%**
3494. **`crates/swc/tests/tsc-references/exportAssignTypes.2.minified.js`** -> AI Confidence: **99.08%**
3495. **`crates/swc/tests/tsc-references/jsxJsxsCjsTransformKeyPropCustomImportPragma.1.normal.js`** -> AI Confidence: **99.08%**
3496. **`crates/swc/tests/tsc-references/jsxJsxsCjsTransformKeyPropCustomImportPragma.2.minified.js`** -> AI Confidence: **99.08%**
3497. **`crates/swc/tests/tsc-references/parserAstSpans1.1.normal.js`** -> AI Confidence: **99.08%**
3498. **`crates/swc/tests/tsc-references/parserAstSpans1.2.minified.js`** -> AI Confidence: **99.08%**
3499. **`crates/swc/tests/tsc-references/superPropertyAccessNoError.1.normal.js`** -> AI Confidence: **99.08%**
3500. **`crates/swc/tests/tsc-references/superPropertyAccessNoError.2.minified.js`** -> AI Confidence: **99.08%**
3501. **`crates/swc/tests/tsc-references/typeOfThisInStaticMembers10(target=es5).1.normal.js`** -> AI Confidence: **99.08%**
3502. **`crates/swc/tests/tsc-references/typeOfThisInStaticMembers10(target=es5).2.minified.js`** -> AI Confidence: **99.08%**
3503. **`crates/swc/tests/tsc-references/typeOfThisInStaticMembers11(target=es5).1.normal.js`** -> AI Confidence: **99.08%**
3504. **`crates/swc/tests/tsc-references/typeOfThisInStaticMembers11(target=es5).2.minified.js`** -> AI Confidence: **99.08%**
3505. **`crates/swc_ecma_minifier/tests/fixture/issues/11133/input.js`** -> AI Confidence: **99.08%**
3506. **`crates/swc_ecma_minifier/tests/fixture/issues/11133/output.js`** -> AI Confidence: **99.08%**
3507. **`crates/swc/tests/fixture/issues-1xxx/1687/output/input.tsx`** -> AI Confidence: **99.07%**
3508. **`crates/swc_bundler/tests/deno-exec/deno-8224/haystack-core/input/core/HMarker.ts`** -> AI Confidence: **99.07%**
3509. **`crates/swc_bundler/tests/deno-exec/deno-8224/haystack-core/input/core/HNa.ts`** -> AI Confidence: **99.07%**
3510. **`crates/swc_bundler/tests/deno-exec/deno-8224/haystack-core/input/core/HRemove.ts`** -> AI Confidence: **99.07%**
3511. **`bindings/binding_core_node/src/analyze.rs`** -> AI Confidence: **99.07%**
3512. **`bindings/binding_core_node/src/lib.rs`** -> AI Confidence: **99.07%**
3513. **`bindings/binding_core_node/src/minify.rs`** -> AI Confidence: **99.07%**
3514. **`crates/dbg-swc/src/es/mod.rs`** -> AI Confidence: **99.07%**
3515. **`crates/swc/examples/minify.rs`** -> AI Confidence: **99.07%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Hardcoded Payload Artifacts
- `crates/swc/tests/fixture/ecosystem-ci/1/input/1.ts` -> **67.9689%** Exposure
- `crates/swc/tests/fixture/ecosystem-ci/1/output/1.ts` -> **67.9689%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `6` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `24433` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `crates/swc_bundler/src/modules/mod.rs` (RUST) -> Cumulative Risk: **711.22**
- **Archetype:** `file_cluster_17` (Distance: 11.533 IQR)
- **Magnitude:** 185.78 | **LOC:** 312 | **CtrlFlow:** 10.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.8321%), Concurrency (99.8175%), Tech Debt (96.9702%)
- **Heaviest Functions:** `push_all` (Impact: 11.2), `print` (Impact: 9.2), `retain_mut` (Impact: 4.3)

### 2. `packages/helpers/esm/_async_generator.js` (JAVASCRIPT) -> Cumulative Risk: **673.33**
- **Archetype:** `file_cluster_4` (Distance: 13.06 IQR)
- **Magnitude:** 138.28 | **LOC:** 75 | **CtrlFlow:** 51.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9999%)
- **Heaviest Functions:** `_async_generator` (Impact: 40.9), `resume` (Impact: 18.3), `settle` (Impact: 18.1)

### 3. `crates/swc_ecma_transforms_base/src/helpers/_ts_dispose_resources.js` (JAVASCRIPT) -> Cumulative Risk: **670.59**
- **Archetype:** `file_cluster_4` (Distance: 13.902 IQR)
- **Magnitude:** 131.62 | **LOC:** 33 | **CtrlFlow:** 54.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Tech Debt (100.0%), Concurrency (100.0%), State Flux (100.0%)
- **Heaviest Functions:** `_ts_dispose_resources` (Impact: 25.9), `_ts_dispose_resources` (Impact: 23.8), `next` (Impact: 21.6)

### 4. `crates/swc_ecma_transforms_base/src/perf.rs` (RUST) -> Cumulative Risk: **667.57**
- **Archetype:** `file_cluster_4` (Distance: 12.003 IQR)
- **Magnitude:** 274.6 | **LOC:** 230 | **CtrlFlow:** 23.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Tech Debt (99.9881%), State Flux (99.9743%)
- **Heaviest Functions:** `fold_par` (Impact: 19.4), `fold_par` (Impact: 16.9), `visit_mut_par` (Impact: 13.9)

### 5. `scripts/update-all-swc-crates.sh` (SHELL) -> Cumulative Risk: **663.67**
- **Archetype:** `file_cluster_4` (Distance: 14.116 IQR)
- **Magnitude:** 4.77 | **LOC:** 28 | **CtrlFlow:** 36.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Tech Debt (100.0%), Concurrency (100.0%), State Flux (100.0%)
- **Heaviest Functions:** `__global_context__` (Impact: 5.1), `Anonymous_Block` (Impact: 3.1), `Anonymous_Block` (Impact: 3.1)

### 6. `crates/swc_ecma_transforms_base/src/helpers/_async_generator.js` (JAVASCRIPT) -> Cumulative Risk: **662.54**
- **Archetype:** `file_cluster_4` (Distance: 13.19 IQR)
- **Magnitude:** 137.04 | **LOC:** 64 | **CtrlFlow:** 53.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `_async_generator` (Impact: 40.7), `resume` (Impact: 18.3), `settle` (Impact: 18.1)

### 7. `crates/swc_ecma_parser/src/parser/mod.rs` (RUST) -> Cumulative Risk: **643.31**
- **Archetype:** `file_cluster_0` (Distance: 12.392 IQR)
- **Magnitude:** 493.9 | **LOC:** 922 | **CtrlFlow:** 38.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.6364%), Safety Score (95.0986%)
- **Heaviest Functions:** `Ok` (Impact: 26.9), `Ok` (Impact: 7.1), `new_from` (Impact: 5.7)

### 8. `crates/swc_ecma_minifier/src/compress/pure/mod.rs` (RUST) -> Cumulative Risk: **641.69**
- **Archetype:** `file_cluster_8` (Distance: 12.995 IQR)
- **Magnitude:** 782.9 | **LOC:** 1253 | **CtrlFlow:** 30.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9981%), Cognitive Load (93.0096%), Documentation (91.711%)
- **Heaviest Functions:** `visit_mut_expr` (Impact: 102.2), `visit_mut_stmt` (Impact: 32.5), `visit_mut_seq_expr` (Impact: 24.1)

### 9. `packages/helpers/esm/_apply_decs_2311.js` (JAVASCRIPT) -> Cumulative Risk: **638.98**
- **Archetype:** `file_cluster_8` (Distance: 13.174 IQR)
- **Magnitude:** 736.82 | **LOC:** 345 | **CtrlFlow:** 59.0% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.8818%), Cognitive Load (99.6137%)
- **Heaviest Functions:** `_apply_decs_2311` (Impact: 236.4), `applyDec` (Impact: 206.2), `applyMemberDecs` (Impact: 25.2)

### 10. `crates/swc_ecma_transforms_base/src/helpers/_jsx.js` (JAVASCRIPT) -> Cumulative Risk: **638.49**
- **Archetype:** `file_cluster_17` (Distance: 13.553 IQR)
- **Magnitude:** 69.2 | **LOC:** 31 | **CtrlFlow:** 75.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Cognitive Load (99.6943%), Tech Debt (92.4142%)
- **Heaviest Functions:** `_jsx` (Impact: 50.6)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `crates/swc_ecma_minifier/benches/full/d3.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.734 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.384 IQR)
- **Top Global Matches:** file_cluster_11: 14.734, file_cluster_8: 14.79, file_cluster_17: 14.961
- **Magnitude:** 22308.0 | **LOC:** 19567 | **CtrlFlow:** 52.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (96.7264%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `brush$1` (Impact: 298.8)
  * `started` (Impact: 228.8)
  * `clipRectangle` (Impact: 133.1)
  * `arc` (Impact: 123.6)
  * `formatLocale` (Impact: 122.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3820`, `structural_boundaries: 3399`, `args: 2136`, `func_start: 2116`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 211`, `high_risk_execution: 3`, `state_mutation: 7155`, `dead_code: 4`, `planned_debt: 18`, `duplicate_logic: 855`, `orphaned_logic: 150`
* *Architecture:* `io: 47`, `api: 549`, `concurrency: 42`
* *Defense:* `safety: 829`, `test: 6`, `immutability_locks: 284`, `cleanup: 53`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/swc_ecma_minifier/tests/benches-full/three.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_11` (Drift: 15.989 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.293 IQR)
- **Top Global Matches:** file_cluster_11: 15.989, file_cluster_15: 16.261, file_cluster_0: 16.325
- **Magnitude:** 19623.28 | **LOC:** 16409 | **CtrlFlow:** 60.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (47.6214%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `WebGLMorphtargets` (Impact: 725.8)
  * `setProgram` (Impact: 684.6)
  * `WebGLTextures` (Impact: 663.4)
  * `WebXRManager` (Impact: 530.7)
  * `render` (Impact: 475.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2722`, `structural_boundaries: 1757`, `args: 1003`, `func_start: 984`
* *Risk/State:* `safety_bypasses: 450`, `state_mutation: 6973`, `dead_code: 21`, `planned_debt: 10`, `duplicate_logic: 416`
* *Architecture:* `io: 42`, `api: 137`, `concurrency: 23`
* *Defense:* `safety: 1096`, `doc: 38`, `sync_locks: 6`, `immutability_locks: 17`, `cleanup: 52`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/swc_ecma_minifier/tests/benches-full/d3.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_11` (Drift: 15.127 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 4.64 IQR)
- **Top Global Matches:** file_cluster_11: 15.127, file_cluster_8: 15.297, file_cluster_17: 15.308
- **Magnitude:** 15600.98 | **LOC:** 11247 | **CtrlFlow:** 52.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.3175%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `brush$1` (Impact: 262.1)
  * `clipRectangle` (Impact: 206.6)
  * `started` (Impact: 203.1)
  * `linePoint` (Impact: 89.5)
  * `contours` (Impact: 76.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2724`, `structural_boundaries: 2466`, `args: 1765`, `func_start: 1607`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 367`, `high_risk_execution: 1`, `state_mutation: 5490`, `dead_code: 3`, `planned_debt: 12`, `duplicate_logic: 703`, `orphaned_logic: 215`
* *Architecture:* `io: 39`, `concurrency: 34`
* *Defense:* `safety: 510`, `test: 5`, `immutability_locks: 2`, `cleanup: 44`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/swc_ecma_minifier/tests/benches-full/terser.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_11` (Drift: 16.241 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.235 IQR)
- **Top Global Matches:** file_cluster_11: 16.241, file_cluster_17: 16.312, file_cluster_4: 16.346
- **Magnitude:** 10755.86 | **LOC:** 20385 | **CtrlFlow:** 67.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (47.4566%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `tighten_body` (Impact: 965.4)
  * `regexp_source_fix` (Impact: 804.3)
  * `DEFPRINT` (Impact: 682.8)
  * `statement1` (Impact: 296.5)
  * `unexpected` (Impact: 147.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2918`, `structural_boundaries: 1436`, `args: 721`, `func_start: 409`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 287`, `high_risk_execution: 1`, `state_mutation: 3503`, `dead_code: 13`, `planned_debt: 5`, `fragile_debt: 2`, `duplicate_logic: 164`
* *Architecture:* `api: 18`, `concurrency: 202`, `import: 1`
* *Defense:* `safety: 1063`, `doc: 25`, `test: 38`, `immutability_locks: 8`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` acorn, assert_clause:, source-map, is_default:
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/swc_ecma_minifier/benches/full/vue.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.21 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.765 IQR)
- **Top Global Matches:** file_cluster_11: 14.21, file_cluster_8: 14.223, file_cluster_17: 14.261
- **Magnitude:** 10072.36 | **LOC:** 11966 | **CtrlFlow:** 61.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (85.4314%), Tech Debt (99.9998%)
**Top Internal Functions/Classes:**
  * `getTagNamespace` (Impact: 1181.3)
    * *Intent:* /* */
  * `initExtend` (Impact: 1117.8)
  * `queueActivatedComponent` (Impact: 1068.3)
  * `initProps` (Impact: 949.7)
  * `createPatchFunction` (Impact: 477.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1177`, `structural_boundaries: 743`, `args: 265`, `func_start: 478`
* *Risk/State:* `safety_bypasses: 19`, `high_risk_execution: 3`, `state_mutation: 1579`, `dead_code: 13`, `planned_debt: 1`, `fragile_debt: 2`, `duplicate_logic: 151`
* *Architecture:* `io: 6`, `api: 50`, `concurrency: 41`
* *Defense:* `safety: 269`, `doc: 53`, `test: 4`, `immutability_locks: 3`, `cleanup: 22`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/swc_ecma_minifier/tests/projects/files/yui-3.12.0.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.389 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 3.61 IQR)
- **Top Global Matches:** file_cluster_8: 12.389, file_cluster_7: 12.601, file_cluster_15: 12.754
- **Magnitude:** 7057.34 | **LOC:** 11137 | **CtrlFlow:** 78.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (28.2769%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_use` (Impact: 880.0)
  * `_purge` (Impact: 762.3)
  * `_getEventData` (Impact: 700.2)
  * `Loader` (Impact: 541.1)
  * `process` (Impact: 435.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 824`, `structural_boundaries: 232`, `args: 154`, `func_start: 175`
* *Risk/State:* `safety_bypasses: 22`, `high_risk_execution: 1`, `state_mutation: 624`, `dead_code: 5`, `planned_debt: 10`, `fragile_debt: 7`, `duplicate_logic: 97`, `orphaned_logic: 20`
* *Architecture:* `io: 36`, `api: 1`, `concurrency: 26`, `import: 2`
* *Defense:* `safety: 106`, `doc: 398`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` yui-log
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/swc_ecma_parser/benches/files/yui-3.12.0.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.189 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 3.287 IQR)
- **Top Global Matches:** file_cluster_8: 12.189, file_cluster_7: 12.423, file_cluster_15: 12.63
- **Magnitude:** 6452.1 | **LOC:** 11543 | **CtrlFlow:** 78.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (21.4889%), Tech Debt (95.6949%)
**Top Internal Functions/Classes:**
  * `_use` (Impact: 900.7)
  * `_purge` (Impact: 760.0)
  * `_getEventData` (Impact: 699.9)
    * *Intent:* **/
  * `process` (Impact: 433.2)
  * `Loader` (Impact: 408.0)
    * *Intent:* /** * Get the last in the queue. LIFO support. * * @method last * @return {MIXED} the last item in t...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 824`, `structural_boundaries: 232`, `args: 154`, `func_start: 141`
* *Risk/State:* `safety_bypasses: 22`, `high_risk_execution: 1`, `state_mutation: 630`, `dead_code: 5`, `planned_debt: 10`, `fragile_debt: 7`, `duplicate_logic: 63`, `orphaned_logic: 19`
* *Architecture:* `io: 36`, `api: 1`, `concurrency: 26`, `import: 2`
* *Defense:* `safety: 106`, `doc: 398`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` yui-log
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/swc_es_parser/benches/files/yui-3.12.0.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.189 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 3.287 IQR)
- **Top Global Matches:** file_cluster_8: 12.189, file_cluster_7: 12.423, file_cluster_15: 12.63
- **Magnitude:** 6452.1 | **LOC:** 11543 | **CtrlFlow:** 78.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (21.4889%), Tech Debt (95.6949%)
**Top Internal Functions/Classes:**
  * `_use` (Impact: 900.7)
  * `_purge` (Impact: 760.0)
  * `_getEventData` (Impact: 699.9)
    * *Intent:* **/
  * `process` (Impact: 433.2)
  * `Loader` (Impact: 408.0)
    * *Intent:* /** * Get the last in the queue. LIFO support. * * @method last * @return {MIXED} the last item in t...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 824`, `structural_boundaries: 232`, `args: 154`, `func_start: 141`
* *Risk/State:* `safety_bypasses: 22`, `high_risk_execution: 1`, `state_mutation: 630`, `dead_code: 5`, `planned_debt: 10`, `fragile_debt: 7`, `duplicate_logic: 63`, `orphaned_logic: 19`
* *Architecture:* `io: 36`, `api: 1`, `concurrency: 26`, `import: 2`
* *Defense:* `safety: 106`, `doc: 398`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` yui-log
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `.github/swc-ecosystem-ci/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/swc_ecma_parser/benches/files/mootools-1.4.5.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.15 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.397 IQR)
- **Top Global Matches:** file_cluster_11: 14.15, file_cluster_15: 14.432, file_cluster_8: 14.454
- **Magnitude:** 4798.48 | **LOC:** 6448 | **CtrlFlow:** 51.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (98.4372%), Tech Debt (99.9964%)
**Top Internal Functions/Classes:**
  * `getProperty` (Impact: 683.8)
  * `parser` (Impact: 203.5)
  * `replace` (Impact: 26.6)
  * `force` (Impact: 21.4)
  * `mergeOne` (Impact: 18.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1089`, `structural_boundaries: 1033`, `args: 572`, `func_start: 450`
* *Risk/State:* `safety_bypasses: 242`, `high_risk_execution: 12`, `state_mutation: 2792`, `planned_debt: 59`, `fragile_debt: 1`, `duplicate_logic: 106`, `orphaned_logic: 21`
* *Architecture:* `io: 17`, `concurrency: 38`
* *Defense:* `safety: 55`, `cleanup: 38`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/swc_es_parser/benches/files/mootools-1.4.5.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.15 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.397 IQR)
- **Top Global Matches:** file_cluster_11: 14.15, file_cluster_15: 14.432, file_cluster_8: 14.454
- **Magnitude:** 4798.48 | **LOC:** 6448 | **CtrlFlow:** 51.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (98.4372%), Tech Debt (99.9964%)
**Top Internal Functions/Classes:**
  * `getProperty` (Impact: 683.8)
  * `parser` (Impact: 203.5)
  * `replace` (Impact: 26.6)
  * `force` (Impact: 21.4)
  * `mergeOne` (Impact: 18.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1089`, `structural_boundaries: 1033`, `args: 572`, `func_start: 450`
* *Risk/State:* `safety_bypasses: 242`, `high_risk_execution: 12`, `state_mutation: 2792`, `planned_debt: 59`, `fragile_debt: 1`, `duplicate_logic: 106`, `orphaned_logic: 21`
* *Architecture:* `io: 17`, `concurrency: 38`
* *Defense:* `safety: 55`, `cleanup: 38`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/swc_es_parser/src/parser.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.443 IQR)
- **Top Global Matches:** file_cluster_8: 13.443, file_cluster_0: 13.709, file_cluster_11: 13.904
- **Magnitude:** 4652.76 | **LOC:** 7092 | **CtrlFlow:** 50.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (25.8231%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `parse_jsx_element_expr` (Impact: 155.2)
  * `parse_class_expr` (Impact: 150.2)
  * `parse_export_decl` (Impact: 139.8)
  * `parse_postfix_expr` (Impact: 129.4)
  * `parse_ts_primary_type` (Impact: 126.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1462`, `structural_boundaries: 1442`, `args: 275`, `func_start: 215`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 122`, `state_mutation: 823`
* *Architecture:* `api: 51`, `concurrency: 28`, `import: 9`
* *Defense:* `safety: 622`, `doc: 11`, `test: 111`, `immutability_locks: 44`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Program, DUMMY_SP, ReturnStmt, crate::
    context::Context, Token, TsModuleDecl, FnDecl, TsIntersectionType...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/swc_ecma_minifier/tests/projects/files/mootools-1.4.5.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_11` (Drift: 13.746 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.244 IQR)
- **Top Global Matches:** file_cluster_11: 13.746, file_cluster_8: 13.943, file_cluster_15: 14.02
- **Magnitude:** 4421.58 | **LOC:** 7246 | **CtrlFlow:** 50.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getProperty` (Impact: 718.8)
  * `parser` (Impact: 210.2)
  * `force` (Impact: 21.4)
  * `typeOf` (Impact: 19.8)
    * *Intent:* */
  * `mergeOne` (Impact: 18.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 938`, `structural_boundaries: 912`, `args: 483`, `func_start: 399`
* *Risk/State:* `safety_bypasses: 221`, `high_risk_execution: 13`, `state_mutation: 2196`, `planned_debt: 53`, `fragile_debt: 1`, `duplicate_logic: 124`, `orphaned_logic: 22`
* *Architecture:* `io: 14`, `concurrency: 20`
* *Defense:* `safety: 49`, `cleanup: 35`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/swc_ecma_minifier/tests/projects/output/angular-1.2.5.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.42 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.783 IQR)
- **Top Global Matches:** file_cluster_0: 14.42, file_cluster_11: 14.443, file_cluster_15: 14.499
- **Magnitude:** 4390.78 | **LOC:** 12187 | **CtrlFlow:** 63.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (53.7996%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `collectDirectives` (Impact: 520.2)
  * `addDirective` (Impact: 476.8)
  * `$ControllerProvider` (Impact: 330.8)
    * *Intent:* /**
  * `assertNotHasOwnProperty` (Impact: 328.9)
    * *Intent:* /** * @ngdoc function * @name angular.isUndefined * @function
  * `compile` (Impact: 313.5)
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 951`, `structural_boundaries: 544`, `args: 429`, `func_start: 303`
* *Risk/State:* `safety_bypasses: 136`, `high_risk_execution: 7`, `state_mutation: 1210`, `dead_code: 11`, `planned_debt: 5`, `fragile_debt: 6`, `duplicate_logic: 5`, `orphaned_logic: 16`
* *Architecture:* `io: 147`, `concurrency: 58`
* *Defense:* `safety: 158`, `doc: 416`, `test: 48`, `cleanup: 24`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/swc_ecma_minifier/tests/projects/output/mootools-1.4.5.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.077 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.828 IQR)
- **Top Global Matches:** file_cluster_11: 14.077, file_cluster_15: 14.392, file_cluster_8: 14.465
- **Magnitude:** 3935.86 | **LOC:** 4346 | **CtrlFlow:** 53.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getProperty` (Impact: 555.3)
  * `parser` (Impact: 201.4)
  * `force` (Impact: 20.8)
  * `id` (Impact: 18.3)
  * `mergeOne` (Impact: 16.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 922`, `structural_boundaries: 817`, `args: 497`, `func_start: 379`
* *Risk/State:* `safety_bypasses: 224`, `high_risk_execution: 14`, `state_mutation: 2033`, `planned_debt: 53`, `fragile_debt: 1`, `duplicate_logic: 117`, `orphaned_logic: 21`
* *Architecture:* `io: 17`, `concurrency: 20`
* *Defense:* `safety: 49`, `cleanup: 36`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/swc_ecma_minifier/tests/projects/output/yui-3.12.0.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.196 IQR)
- **Local Micro-Species:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 3.554 IQR)
- **Top Global Matches:** file_cluster_8: 13.196, file_cluster_7: 13.368, file_cluster_15: 13.412
- **Magnitude:** 3871.32 | **LOC:** 7800 | **CtrlFlow:** 78.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (47.7903%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getLocation` (Impact: 655.8)
  * `parseUA` (Impact: 546.1)
  * `getRequires` (Impact: 107.8)
    * *Intent:* * Determines whether or not the provided item is a boolean. * @method isBoolean
  * `resolve` (Impact: 106.2)
  * `_use` (Impact: 91.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 783`, `structural_boundaries: 215`, `args: 154`, `func_start: 130`
* *Risk/State:* `safety_bypasses: 27`, `high_risk_execution: 1`, `state_mutation: 1186`, `dead_code: 5`, `planned_debt: 9`, `fragile_debt: 7`, `duplicate_logic: 37`, `orphaned_logic: 21`
* *Architecture:* `io: 28`, `api: 1`, `concurrency: 35`, `import: 3`
* *Defense:* `safety: 79`, `doc: 410`, `cleanup: 20`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` yui-log
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/swc_ecma_minifier/tests/projects/files/angular-1.2.5.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.054 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.114 IQR)
- **Top Global Matches:** file_cluster_8: 13.054, file_cluster_15: 13.16, file_cluster_11: 13.192
- **Magnitude:** 3402.0 | **LOC:** 21880 | **CtrlFlow:** 62.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (40.8121%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `next` (Impact: 435.1)
  * `Browser` (Impact: 406.1)
  * `notifyWhenNoOutstandingRequests` (Impact: 313.1)
  * `$ControllerProvider` (Impact: 212.0)
  * `minErr` (Impact: 209.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 373`, `structural_boundaries: 226`, `args: 175`, `func_start: 171`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 30`, `high_risk_execution: 2`, `state_mutation: 356`, `dead_code: 5`, `planned_debt: 4`, `duplicate_logic: 48`, `orphaned_logic: 47`
* *Architecture:* `io: 6`, `concurrency: 12`
* *Defense:* `safety: 74`, `doc: 165`, `test: 1`, `immutability_locks: 1`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/swc_ecma_parser/benches/files/angular-1.2.5.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_11` (Drift: 13.636 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.344 IQR)
- **Top Global Matches:** file_cluster_11: 13.636, file_cluster_15: 13.639, file_cluster_8: 13.674
- **Magnitude:** 3137.84 | **LOC:** 20369 | **CtrlFlow:** 62.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (44.7363%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `Browser` (Impact: 391.6)
  * `next` (Impact: 352.1)
    * *Intent:* /** * Checks if `obj` is a window object. *
  * `notifyWhenNoOutstandingRequests` (Impact: 251.4)
  * `minErr` (Impact: 208.1)
    * *Intent:* /** * @license AngularJS v1.2.5 * (c) 2010-2014 Google, Inc. http://angularjs.org * License: MIT */
  * `$ControllerProvider` (Impact: 200.4)
    * *Intent:* * @name ng.directive:ngApp * * @element ANY * @param {angular.Module} ngApp an optional application ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 371`, `structural_boundaries: 221`, `args: 172`, `func_start: 169`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 30`, `high_risk_execution: 2`, `state_mutation: 352`, `dead_code: 5`, `planned_debt: 4`, `duplicate_logic: 47`, `orphaned_logic: 47`
* *Architecture:* `io: 5`, `concurrency: 12`
* *Defense:* `safety: 74`, `doc: 161`, `test: 1`, `immutability_locks: 1`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/swc_es_parser/benches/files/angular-1.2.5.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_11` (Drift: 13.636 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 4.344 IQR)
- **Top Global Matches:** file_cluster_11: 13.636, file_cluster_15: 13.639, file_cluster_8: 13.674
- **Magnitude:** 3137.84 | **LOC:** 20369 | **CtrlFlow:** 62.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (44.7363%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `Browser` (Impact: 391.6)
  * `next` (Impact: 352.1)
    * *Intent:* /** * Checks if `obj` is a window object. *
  * `notifyWhenNoOutstandingRequests` (Impact: 251.4)
  * `minErr` (Impact: 208.1)
    * *Intent:* /** * @license AngularJS v1.2.5 * (c) 2010-2014 Google, Inc. http://angularjs.org * License: MIT */
  * `$ControllerProvider` (Impact: 200.4)
    * *Intent:* * @name ng.directive:ngApp * * @element ANY * @param {angular.Module} ngApp an optional application ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 371`, `structural_boundaries: 221`, `args: 172`, `func_start: 169`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 30`, `high_risk_execution: 2`, `state_mutation: 352`, `dead_code: 5`, `planned_debt: 4`, `duplicate_logic: 47`, `orphaned_logic: 47`
* *Architecture:* `io: 5`, `concurrency: 12`
* *Defense:* `safety: 74`, `doc: 161`, `test: 1`, `immutability_locks: 1`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/swc_ecma_lexer/src/common/parser/expr.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.7 IQR)
- **Top Global Matches:** file_cluster_8: 12.7, file_cluster_0: 12.773, file_cluster_11: 12.831
- **Magnitude:** 2594.42 | **LOC:** 2600 | **CtrlFlow:** 58.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (30.8069%), Tech Debt (10.9073%)
**Top Internal Functions/Classes:**
  * `parse_assignment_expr` (Impact: 596.4)
    * *Intent:* ///`parseMaybeAssign` (overridden)
  * `parse_member_expr_or_new_expr_inner` (Impact: 568.9)
  * `parse_subscript` (Impact: 333.2)
  * `parse_unary_expr` (Impact: 314.3)
  * `parse_paren_expr_or_arrow_fn` (Impact: 158.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 455`, `structural_boundaries: 318`, `args: 102`, `func_start: 25`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 112`, `dead_code: 6`, `planned_debt: 7`, `fragile_debt: 2`
* *Architecture:* `api: 21`, `concurrency: 5`, `import: 7`
* *Defense:* `safety: 217`, `doc: 25`, `test: 8`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` lexer::token::TokenFactory, parse_maybe_private_name, super::
    assign_target_or_spread::AssignTargetOrSpread, token_and_span::TokenAndSpan, swc_atoms::atom, Span, reparse_expr_as_pat, parse_jsx_text...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/swc_ecma_parser/src/parser/typescript.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.335 IQR)
- **Top Global Matches:** file_cluster_8: 13.335, file_cluster_0: 13.567, file_cluster_16: 13.569
- **Magnitude:** 2219.48 | **LOC:** 5212 | **CtrlFlow:** 54.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (22.1366%), Tech Debt (10.961%)
**Top Internal Functions/Classes:**
  * `parse_ts_list` (Impact: 696.2)
    * *Intent:* /// `tsParseList`
  * `parse_ts_type_param` (Impact: 122.4)
  * `parse_flow_component_param` (Impact: 105.2)
  * `parse_ts_type_or_type_predicate_ann` (Impact: 90.0)
  * `validate_flow_enum_members` (Impact: 50.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 453`, `structural_boundaries: 384`, `args: 131`, `func_start: 71`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 253`, `planned_debt: 1`, `fragile_debt: 5`
* *Architecture:* `api: 40`, `import: 6`
* *Defense:* `safety: 253`, `doc: 93`, `test: 29`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Atom, swc_atoms::atom, swc_ecma_visit::assert_eq_ignore_span, Span, swc_common::DUMMY_SP, PResult, crate::
    error::SyntaxError, Context...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/swc/tests/tsc-references/parserRealSource14.1.normal.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_11` (Drift: 18.144 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 3.239 IQR)
- **Top Global Matches:** file_cluster_11: 18.144, file_cluster_17: 18.192, file_cluster_0: 18.33
- **Magnitude:** 1944.82 | **LOC:** 371 | **CtrlFlow:** 61.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (44.8275%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `AstPath` (Impact: 210.4)
  * `getAstPathToPosition` (Impact: 29.7)
  * `pre` (Impact: 16.9)
    * *Intent:* //We need this options dealing with an AST coming from an incomplete AST. For example: // class foo ...
  * `isArgumentOfClassConstructor` (Impact: 15.8)
  * `lookInComments` (Impact: 12.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 165`, `structural_boundaries: 103`, `args: 75`, `func_start: 140`
* *Risk/State:* `safety_bypasses: 31`, `state_mutation: 1271`, `planned_debt: 2`, `duplicate_logic: 5`
* *Architecture:* `io: 9`, `import: 1`
* *Defense:* `safety: 114`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` _class_call_check
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/swc/tests/tsc-references/generatedContextualTyping.1.normal.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.92%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.293 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 3.685 IQR)
- **Top Global Matches:** file_cluster_8: 12.293, file_cluster_11: 12.867, file_cluster_7: 12.916
- **Magnitude:** 1843.58 | **LOC:** 2831 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (38.9425%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `x96` (Impact: 5.8)
  * `x108` (Impact: 5.8)
  * `x120` (Impact: 5.8)
  * `x85` (Impact: 5.7)
  * `x86` (Impact: 5.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 188`, `structural_boundaries: 693`, `args: 478`, `func_start: 751`
* *Risk/State:* `safety_bypasses: 48`, `state_mutation: 831`, `duplicate_logic: 199`, `orphaned_logic: 40`
* *Architecture:* `import: 3`
* *Defense:* `safety: 48`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` _class_call_check, _inherits, _call_super
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/swc_node_bundler/tests/pass/deno-001/full/output/entry.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.313 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.399 IQR)
- **Top Global Matches:** file_cluster_4: 14.313, file_cluster_17: 14.86, file_cluster_8: 14.979
- **Magnitude:** 1794.42 | **LOC:** 827 | **CtrlFlow:** 55.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `super` (Impact: 109.7)
  * `read` (Impact: 40.3)
  * `fixLength` (Impact: 36.3)
  * `readMIMEHeader` (Impact: 35.9)
  * `chunkedBodyReader` (Impact: 35.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 248`, `structural_boundaries: 200`, `args: 82`, `func_start: 86`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 638`, `duplicate_logic: 34`
* *Architecture:* `io: 3`, `api: 3`, `concurrency: 341`
* *Defense:* `safety: 106`, `test: 12`, `immutability_locks: 109`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/swc_ecma_minifier/benches/full/lodash.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.98%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.323 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Functions` (Drift: 3.463 IQR)
- **Top Global Matches:** file_cluster_0: 14.323, file_cluster_8: 14.398, file_cluster_11: 14.475
- **Magnitude:** 1784.34 | **LOC:** 17210 | **CtrlFlow:** 52.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (47.4309%), Tech Debt (16.2499%)
**Top Internal Functions/Classes:**
  * `baseForOwn` (Impact: 45.5)
    * *Intent:* /** * Creates a function like `_.invertBy`. * * @private * @param {Function} setter The function to ...
  * `slice` (Impact: 16.5)
  * `arrayEach` (Impact: 14.7)
    * *Intent:* /** * Creates a function like `_.over`.
  * `arrayEach` (Impact: 13.3)
  * `times` (Impact: 7.8)
    * *Intent:* /** * The base implementation of methods like `_.dropWhile` and `_.takeWhile` * without support for ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1116`, `structural_boundaries: 1004`, `args: 426`, `func_start: 372`
* *Risk/State:* `safety_bypasses: 188`, `state_mutation: 1443`, `dead_code: 2`, `fragile_debt: 1`, `duplicate_logic: 9`
* *Architecture:* `io: 82`, `api: 1`, `concurrency: 58`, `import: 1`
* *Defense:* `safety: 179`, `doc: 1503`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.018
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### 🚨 Severe Anti-Patterns (Language Convention Violations)
- `crates/swc_ecma_parser/tests/tsc/privateIdentifierExpando.ts` (TYPESCRIPT) | **Drift Ratio: 1.76x**
  * **Global Archetype:** `file_cluster_8` (Drift: 3.721 IQR)
  * **Local Reality:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 6.562 IQR)
- `crates/swc_ecma_parser/tests/tsc/intlDateTimeFormatRangeES2021.ts` (TYPESCRIPT) | **Drift Ratio: 1.73x**
  * **Global Archetype:** `file_cluster_8` (Drift: 5.067 IQR)
  * **Local Reality:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 8.772 IQR)
- `crates/swc/tests/fixture/issues-11xxx/11608/input/input.js` (JAVASCRIPT) | **Drift Ratio: 1.72x**
  * **Global Archetype:** `file_cluster_8` (Drift: 3.892 IQR)
  * **Local Reality:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 6.676 IQR)
- `crates/swc_ecma_parser/tests/span/ts/expr/as.ts` (TYPESCRIPT) | **Drift Ratio: 1.62x**
  * **Global Archetype:** `file_cluster_8` (Drift: 4.676 IQR)
  * **Local Reality:** `Cluster 2: Type Definitions & Bypasses` (Drift: 7.574 IQR)
- `crates/swc/tests/fixture/issues-11xxx/11539/input/index.js` (JAVASCRIPT) | **Drift Ratio: 1.59x**
  * **Global Archetype:** `file_cluster_8` (Drift: 4.603 IQR)
  * **Local Reality:** `Cluster 8: Declarative Glue & Inert Types` (Drift: 7.298 IQR)

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `crates/swc/tests/tsc-references/destructuringEvaluationOrder(target=es5).2.minified.js` (JAVASCRIPT) | Magnitude: 15.44 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 11, state_mutation: 11, decorators: 6, import: 6
- `crates/swc/tests/tsc-references/usingDeclarationsWithLegacyClassDecorators.1(module=commonjs,target=es2015).2.minified.js` (JAVASCRIPT) | Magnitude: 19.4 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 12, state_mutation: 4, branch: 3, structural_boundaries: 3
- `crates/swc/tests/tsc-references/usingDeclarationsWithLegacyClassDecorators.1(module=commonjs,target=esnext).2.minified.js` (JAVASCRIPT) | Magnitude: 19.4 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 12, state_mutation: 4, branch: 3, structural_boundaries: 3
- `crates/swc_ecma_transforms_proposal/tests/decorators/2022-03-runtime-errors--to-es2015/invalid-field-decorator-return/exec.js` (JAVASCRIPT) | Magnitude: 9.16 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 15, args: 9, closures: 9, func_start: 8
- `crates/swc_ecma_transforms_proposal/tests/decorators/2022-03-runtime-errors--to-es2015/invalid-getter-decorator-return/exec.js` (JAVASCRIPT) | Magnitude: 9.16 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 15, args: 9, closures: 9, func_start: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `crates/jsdoc/tests/fixtures/mixintag.js` (JAVASCRIPT) | Magnitude: 0.01 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: doc: 6, args: 3, func_start: 3, closures: 3
- `crates/swc/tests/tsc-references/typeFromPrototypeAssignment4.1.normal.js` (JAVASCRIPT) | Magnitude: 7.12 | Delta: **0.073 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: args: 5, reflection_metaprogramming: 4, indent_spaces: 4, func_start: 3
- `crates/swc_ecma_parser/tests/tsc/typeFromPrototypeAssignment4.ts` (TYPESCRIPT) | Magnitude: 0.58 | Delta: **0.099 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: reflection_metaprogramming: 4, indent_spaces: 4, doc: 3, closures: 3
- `crates/jsdoc/tests/fixtures/eventfirestag.js` (JAVASCRIPT) | Magnitude: 0.01 | Delta: **0.101 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: doc: 5, args: 3, func_start: 3, state_mutation: 3
- `crates/swc_ecma_parser/tests/typescript/custom/issue-259/input.ts` (TYPESCRIPT) | Magnitude: 1.05 | Delta: **0.206 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 1, args: 1, closures: 1, events: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `crates/swc/tests/tsc-references/optionalChainingInParameterInitializer(target=es2015).1.normal.js` (JAVASCRIPT) | Magnitude: 7.5 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 5, state_mutation: 3, closures: 3, branch: 2
- `crates/swc_ecma_parser/tests/tsc/thisPrototypeMethodCompoundAssignment.ts` (TYPESCRIPT) | Magnitude: 1.46 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 3, state_mutation: 3, safety: 2, args: 1
- `crates/swc/tests/tsc-references/witness.1.normal.js` (JAVASCRIPT) | Magnitude: 183.76 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 143, structural_boundaries: 69, indent_spaces: 47, func_start: 29
- `crates/swc_ecma_parser/benches/files/angular-1.2.5.js` (JAVASCRIPT) | Magnitude: 3137.84 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 1147, branch: 371, state_mutation: 352, structural_boundaries: 221
- `crates/swc_es_parser/benches/files/angular-1.2.5.js` (JAVASCRIPT) | Magnitude: 3137.84 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 1147, branch: 371, state_mutation: 352, structural_boundaries: 221

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `crates/swc/tests/tsc-references/constructorFunctionMethodTypeParameters.1.normal.js` (JAVASCRIPT) | Magnitude: 9.94 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 13, structural_boundaries: 5, state_mutation: 4, args: 3
- `crates/swc_ecma_minifier/tests/fixture/projects/jquery/7/output.js` (JAVASCRIPT) | Magnitude: 0.02 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 8, branch: 4, structural_boundaries: 4, state_mutation: 3
- `crates/swc/tests/tsc-references/prototypePropertyAssignmentMergeWithInterfaceMethod.1.normal.js` (JAVASCRIPT) | Magnitude: 3.04 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: doc: 3, args: 2, func_start: 2, closures: 2
- `crates/swc/tests/tsc-references/lateBoundAssignmentDeclarationSupport6.2.minified.js` (JAVASCRIPT) | Magnitude: 7.02 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: reflection_metaprogramming: 5, structural_boundaries: 3, state_mutation: 3, api: 2
- `crates/swc_ecma_parser/tests/tsc/methodsReturningThis.ts` (TYPESCRIPT) | Magnitude: 2.21 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: func_start: 11, structural_boundaries: 10, closures: 10, reflection_metaprogramming: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `crates/swc_ecma_compat_es2020/src/optional_chaining.rs` (RUST) | Magnitude: 7.64 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 7, api: 5, import: 5
- `crates/swc_nodejs_common/src/lib.rs` (RUST) | Magnitude: 21.36 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 15, generics: 13, safety: 6
- `crates/swc/tests/fixture/issues-1xxx/1799/case7-no-async/output/index.js` (JAVASCRIPT) | Magnitude: 0.01 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 4, state_mutation: 4, args: 3
- `crates/swc/tests/tsc-references/asOperatorASI.2.minified.js` (JAVASCRIPT) | Magnitude: 6.86 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 7, structural_boundaries: 5, func_start: 5, args: 3
- `crates/swc/tests/tsc-references/mixinAccessModifiers.2.minified.js` (JAVASCRIPT) | Magnitude: 67.72 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 36, func_start: 28, state_mutation: 22, args: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `crates/swc_ecma_parser/tests/typescript/issue-10800/input.d.ts` (TYPESCRIPT) | Magnitude: 1.15 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 4, args: 2, closures: 2, safety: 1
- `crates/swc_ecma_parser/tests/typescript/types/function-in-generic/input.ts` (TYPESCRIPT) | Magnitude: 1.15 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 1, args: 1, safety: 1, state_mutation: 1
- `crates/swc/tests/tsc-references/computedPropertyNames11_ES5.2.minified.js` (JAVASCRIPT) | Magnitude: 20.4 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 11, args: 11, func_start: 11, closures: 11
- `crates/swc_ecma_parser/tests/flow-hermes/corpus/types/array_postfix/migrated_004.js` (JAVASCRIPT) | Magnitude: 11.52 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 2, args: 1, state_mutation: 1, closures: 1
- `crates/swc_ecma_parser/tests/flow-hermes/corpus/types/array_postfix/migrated_005.js` (JAVASCRIPT) | Magnitude: 11.52 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 2, args: 1, state_mutation: 1, closures: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `crates/swc_config/src/merge.rs` (RUST) | Magnitude: 55.76 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 42, state_mutation: 22, structural_boundaries: 20, branch: 13
- `crates/swc_ecma_regexp/src/parser/parser_impl.rs` (RUST) | Magnitude: 43.54 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 87, structural_boundaries: 24, branch: 15, generics: 14
- `crates/swc_bundler/tests/deno-exec/deno-9307/.case1/input/src/types.d.ts` (TYPESCRIPT) | Magnitude: 3.03 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 43, structural_boundaries: 37, generics: 15, api: 14
- `crates/swc_ecma_parser/tests/tsc/assignmentCompatWithStringIndexer.ts` (TYPESCRIPT) | Magnitude: 1.25 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 23, generics: 10, state_mutation: 9
- `crates/swc_ecma_parser/tests/tsc/assignmentCompatWithStringIndexer2.ts` (TYPESCRIPT) | Magnitude: 1.25 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 23, generics: 10, state_mutation: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `crates/swc_ecma_minifier/tests/terser/compress/reduce_vars/issue_2450_5/output.terser.js` (JAVASCRIPT) | Magnitude: 2.96 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 4, args: 3, closures: 2, structural_boundaries: 1
- `crates/swc_sourcemap/src/decoder.rs` (RUST) | Magnitude: 304.16 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 379, structural_boundaries: 115, safety: 98, state_mutation: 93
- `crates/swc/tests/fixture/issues-6xxx/6726/input/index.jsx` (JAVASCRIPT) | Magnitude: 0.01 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 4, indent_spaces: 4, state_mutation: 3, args: 2
- `crates/swc_ecma_transforms_base/src/helpers/_wrap_reg_exp.js` (JAVASCRIPT) | Magnitude: 126.16 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 76, state_mutation: 49, structural_boundaries: 29, branch: 17
- `scripts/cargo/patch-section.sh` (SHELL) | Magnitude: 1.03 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: structural_boundaries: 6, io: 6, state_mutation: 5, safety: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `crates/swc_ecma_parser/tests/tsc/tsxSpreadAttributesResolution7.tsx` (TYPESCRIPT) | Magnitude: 0.57 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 7, indent_spaces: 7, generics: 4, args: 3
- `crates/swc_ecma_parser/tests/tsc/tsxSpreadAttributesResolution8.tsx` (TYPESCRIPT) | Magnitude: 0.4 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 9, structural_boundaries: 5, generics: 4, ui_framework: 3
- `crates/swc/tests/tsc-references/tsxStatelessFunctionComponentsWithTypeArguments5.1.normal.js` (JAVASCRIPT) | Magnitude: 14.34 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 29, structural_boundaries: 6, state_mutation: 6, ui_framework: 5
- `crates/swc_ecma_parser/tests/tsc/checkJsxChildrenProperty13.tsx` (TYPESCRIPT) | Magnitude: 0.47 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 9, indent_spaces: 8, generics: 5, class_start: 4
- `crates/swc_ecma_parser/tests/tsc/interfaceDoesNotDependOnBaseTypes.ts` (TYPESCRIPT) | Magnitude: 2.26 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: state_mutation: 9, structural_boundaries: 4, generics: 2, indent_spaces: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `crates/swc/tests/tsc-references/importCallExpressionInUMD1.1.normal.js` (JAVASCRIPT) | Magnitude: 19.68 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 43, branch: 18, safety: 16, structural_boundaries: 11
- `crates/swc_node_bundler/tests/pass/deno-001/simple-2/input/http/_io.ts` (TYPESCRIPT) | Magnitude: 4.57 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: api: 18, indent_spaces: 11, structural_boundaries: 10, concurrency: 10
- `crates/swc_ecma_parser/tests/tsc/arrowFunctionWithParameterNameAsync_es2017.ts` (TYPESCRIPT) | Magnitude: 1.67 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: concurrency: 2, structural_boundaries: 1, args: 1, func_start: 1
- `crates/swc_ecma_parser/tests/tsc/arrowFunctionWithParameterNameAsync_es5.ts` (TYPESCRIPT) | Magnitude: 1.67 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: concurrency: 2, structural_boundaries: 1, args: 1, func_start: 1
- `crates/swc_ecma_parser/tests/tsc/arrowFunctionWithParameterNameAsync_es6.ts` (TYPESCRIPT) | Magnitude: 1.67 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: concurrency: 2, structural_boundaries: 1, args: 1, func_start: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `crates/swc_bundler/src/load.rs` (RUST) | Magnitude: 15.16 | Delta: **0.054 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: doc: 29, indent_spaces: 10, structural_boundaries: 8, generics: 7
- `crates/swc_ecma_codegen/scripts/bench.sh` (SHELL) | Magnitude: 0.15 | Delta: **0.398 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: structural_boundaries: 1, safety: 1, dead_code: 1, test: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `crates/swc/tests/tsc-references/paramTagOnCallExpression.1.normal.js` (JAVASCRIPT) | Magnitude: 11.52 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 2, api: 1
- `crates/swc/tests/tsc-references/typeTagModuleExports.1.normal.js` (JAVASCRIPT) | Magnitude: 11.52 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 2, api: 1
- `crates/swc_ecma_parser/tests/tsc/callbackOnConstructor.ts` (TYPESCRIPT) | Magnitude: 0.36 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 6, structural_boundaries: 4, args: 2, func_start: 2
- `crates/swc/tests/tsc-references/importTag2.1.normal.js` (JAVASCRIPT) | Magnitude: 3.84 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 3, structural_boundaries: 2, api: 2, args: 1
- `crates/swc/tests/tsc-references/importTag3.1.normal.js` (JAVASCRIPT) | Magnitude: 3.84 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 3, structural_boundaries: 2, api: 2, args: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `crates/swc_ecma_parser/tests/tsc/narrowingGenericTypeFromInstanceof01.ts` (TYPESCRIPT) | Magnitude: 2.88 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 13, generics: 9, args: 8, func_start: 8
- `crates/swc_ecma_transforms_typescript/src/utils.rs` (RUST) | Magnitude: 15.06 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 27, structural_boundaries: 9, api: 7, safety: 5
- `crates/swc/tests/tsc-references/importAliasModuleExports.1.normal.js` (JAVASCRIPT) | Magnitude: 11.9 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 6, func_start: 6, reflection_metaprogramming: 5
- `crates/swc_ecma_transforms_react/tests/jsx/fixture/issue-5099/1/output.mjs` (JAVASCRIPT) | Magnitude: 0.01 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 8, immutability_locks: 4, api: 3
- `crates/swc/benches/oxc.rs` (RUST) | Magnitude: 30.26 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 63, structural_boundaries: 17, safety: 12, import: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `crates/swc_bundler/tests/deno-exec/deno-10153/case1/entry.ts` (TYPESCRIPT) | Magnitude: 1.63 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 7, dead_code: 3, structural_boundaries: 2, immutability_locks: 2
- `crates/swc/tests/tsc-references/innerTypeParameterShadowingOuterOne.1.normal.js` (JAVASCRIPT) | Magnitude: 12.32 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 4, args: 4, func_start: 4
- `crates/swc/tests/tsc-references/thisPropertyAssignment.1.normal.js` (JAVASCRIPT) | Magnitude: 7.26 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 5, indent_spaces: 4, structural_boundaries: 1, args: 1
- `crates/swc/tests/tsc-references/typeParameterAsTypeParameterConstraintTransitively2.1.normal.js` (JAVASCRIPT) | Magnitude: 11.58 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 11, func_start: 9, structural_boundaries: 5, args: 5
- `crates/swc_ecma_minifier/tests/fixture/issues/10539/input.js` (JAVASCRIPT) | Magnitude: 0.02 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 5, state_mutation: 2, dead_code: 2, memory_alloc: 2

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `crates/swc_ecma_parser/src/parser/class_and_fn.rs` -> Churn: **73.04%** | Cog Load: 10.3666% | Debt: 99.9995%
- `crates/swc_ecma_minifier/src/compress/optimize/mod.rs` -> Churn: **50.61%** | Cog Load: 51.6234% | Debt: 12.6346%
- `crates/swc_ecma_minifier/src/program_data.rs` -> Churn: **50.61%** | Cog Load: 23.3311% | Debt: 99.9054%
- `crates/swc_ecma_preset_env/tests/fixtures/transform/named-capturing-groups-regex/output.mjs` -> Churn: **50.61%** | Cog Load: 100.0% | Debt: 0.0%
- `crates/swc_ecma_transforms_base/src/helpers/_wrap_reg_exp.js` -> Churn: **50.61%** | Cog Load: 100.0% | Debt: 99.708%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `crates/swc_es_parser/src/parser.rs` -> **Donny/강동윤** (100.0% isolated ownership) | Magnitude: 4652.76
- `crates/swc_ecma_parser/src/parser/typescript.rs` -> **Donny/강동윤** (100.0% isolated ownership) | Magnitude: 2219.48
- `crates/swc_ecma_transforms_proposal/src/decorator_impl.rs` -> **Donny/강동윤** (100.0% isolated ownership) | Magnitude: 1295.82
- `crates/swc_ecma_minifier/src/compress/optimize/sequences.rs` -> **Donny/강동윤** (100.0% isolated ownership) | Magnitude: 1182.6
- `crates/swc_ecma_parser/src/lexer/mod.rs` -> **Donny/강동윤** (100.0% isolated ownership) | Magnitude: 1061.88

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `crates/swc_ecma_minifier/benches/full/react.js` -> **Severity: 72.297** (Blast Radius: 6.065 * Doc Risk: 11.9203%)
- `crates/swc_ecma_utils/src/str.rs` -> **Severity: 14.169** (Blast Radius: 0.143 * Doc Risk: 99.0856%)
- `crates/preset_env_base/src/version.rs` -> **Severity: 5.848** (Blast Radius: 0.091 * Doc Risk: 64.2592%)
- `crates/swc_plugin_runner/src/runtime.rs` -> **Severity: 5.564** (Blast Radius: 0.24 * Doc Risk: 23.1828%)
- `.github/bot/src/util/octokit.ts` -> **Severity: 4.577** (Blast Radius: 0.049 * Doc Risk: 93.4083%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
