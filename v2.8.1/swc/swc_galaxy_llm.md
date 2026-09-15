# ARCHITECTURAL_BRIEF: swc
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/swc-project/swc.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
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
## 2. THE 13-POINT STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (EQUATIONS & CONTEXT)
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

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 82586 |
| Analyzed Artifacts (Scanned) | 57785 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 24801 |
| Total LOC | 3536225 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 70.0% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.845 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2956 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.0947 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 101 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 28478 | 848968 | 49.3% |
| JSON | 19417 | 1969836 | 33.6% |
| TYPESCRIPT | 6664 | 191269 | 11.5% |
| CSS | 1337 | 151530 | 2.3% |
| RUST | 1332 | 373540 | 2.3% |
| PLAINTEXT | 216 | 2 | 0.4% |
| MARKDOWN | 134 | 0 | 0.2% |
| XML | 111 | 52 | 0.2% |
| SHELL | 90 | 917 | 0.2% |
| YAML | 3 | 23 | 0.0% |
| PYTHON | 3 | 88 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Flat Modular Platform` (z +1.61; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 70%, Declarative / Non-Code 8%, State Mutators Files 6%, Interface Declarations Files 6%, Callbacks & Closures Files 5%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 57423 | 99.4% |
| Unknown | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 348 | 0.6% |
| Static: Minified & Vendor Opaque Mass | 13 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 24801*

**Composition by Extension & Reason:**
- `.js`: 5008x Excluded: Neighborhood Micro-Mass Limit Exceeded, 488x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 20x Excluded (Saturation: Line 3 exceeds 500 chars)
- `.rust-debug`: 3966x Excluded (Unsupported Extension: '.rust-debug')
- `.ts`: 2758x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 533x Excluded: Neighborhood Micro-Mass Limit Exceeded, 3x Excluded (Saturation: Line 5 exceeds 500 chars)
- `.swc-stderr`: 2859x Excluded (Unsupported Extension: '.swc-stderr'), 358x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.html`: 2676x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 1149x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 145x Excluded: Neighborhood Micro-Mass Limit Exceeded, 7x Excluded (Static Asset Blob without Intent: 1155 LOC)
- `.stderr`: 1920x Excluded (Unsupported Extension: '.stderr')
- `.css`: 538x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 41x Excluded: Neighborhood Micro-Mass Limit Exceeded, 1x Excluded (Saturation: Line 98 exceeds 500 chars)
- `.debug`: 230x Excluded (Unsupported Extension: '.debug'), 5x Unsupported Format (.debug)
- `.toml`: 149x Unsupported Format (.toml), 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 5x Excluded (Unsupported Extension: '.toml')
- `.stdout`: 102x Excluded (Unsupported Extension: '.stdout'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 94x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Unsupported Format (.undeterminable)
- `.map`: 76x Excluded (Unsupported Extension: '.map')
- `.mjs`: 75x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 39 exceeds 500 chars)
- `.snap`: 61x Excluded (Unsupported Extension: '.snap')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 2.9 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 15.3 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 0.8 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 0.6 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 2.7 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 2.2 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 1.5 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 36.7 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.7 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 1.8 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 30.9 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 68.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 15148 | 1719 | 0 | `crates/swc_ecma_parser/src/parser/typescript.rs` |
| cleanup | 795 | 158 | 0 | `crates/swc_ecma_minifier/tests/benches-full/three.js` |
| guards | 73167 | 6368 | 1 | `crates/swc_ecma_minifier/tests/fixture/next/react-pdf-renderer/output.js` |
| danger | 41485 | 5618 | 0 | `crates/swc_ecma_minifier/tests/fixture/next/react-pdf-renderer/output.js` |
| concurrency | 16253 | 2454 | 0 | `crates/swc_ecma_minifier/tests/fixture/next/wrap-contracts/output.js` |
| connectivity | 37122 | 9064 | 1 | `crates/swc_ecma_minifier/tests/fixture/next/wrap-contracts/output.js` |
| io | 3385 | 559 | 0 | `crates/swc_bundler/tests/fixture/deno-9591/output/entry.inlined.ts` |
| crypto | 3 | 3 | 0 | `crates/swc/tests/fixture/issues-1xxx/1545/case1/input/index.js` |
| ipc | 136 | 42 | 0 | `crates/swc_ecma_minifier/tests/fixture/issues/quagga2/1.4.2/1/input.js` |
| time | 1687 | 344 | 0 | `crates/swc_ecma_minifier/tests/fixture/next/react-ace/chunks/8a28b14e.d8fbda268ed281a1/input.js` |
| serialization | 673 | 262 | 0 | `crates/swc_ecma_minifier/tests/fixture/next/wrap-contracts/output.js` |
| regex | 3015 | 311 | 0 | `crates/swc_ecma_minifier/tests/fixture/next/react-ace/chunks/8a28b14e.d8fbda268ed281a1/input.js` |
| events | 5125 | 411 | 0 | `crates/swc_ecma_minifier/tests/fixture/next/wrap-contracts/output.js` |
| tests | 12038 | 1719 | 0 | `crates/swc_ecma_minifier/tests/exec.rs` |
| docs | 26672 | 2093 | 0 | `crates/swc_ecma_minifier/tests/fixture/next/wrap-contracts/output.js` |
| debt | 22384 | 8997 | 1 | `crates/swc_ecma_minifier/tests/fixture/next/wrap-contracts/output.js` |
| mutation | 345811 | 21642 | 5 | `crates/swc_ecma_minifier/tests/fixture/next/asmjs/1/input.js` |
| dead_code | 25364 | 9085 | 1 | `crates/swc_ecma_minifier/tests/benches-full/d3.js` |
| credential | 35 | 21 | 0 | `crates/swc_ecma_minifier/tests/fixture/next/react-ace/chunks/8a28b14e.d8fbda268ed281a1/input.js` |
| threat | 21786 | 3627 | 0 | `crates/swc_ecma_minifier/tests/fixture/next/react-pdf-renderer/output.js` |
| ml_ai | 891 | 182 | 0 | `crates/swc_ecma_minifier/tests/benches-full/three.js` |
| ui | 7861 | 794 | 0 | `crates/swc_ecma_minifier/tests/benches-full/terser.js` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `crates/swc_bundler/tests/fixture/deno-9591/output/entry.inlined.ts` (Hits: 278)
- `crates/swc_bundler/tests/fixture/deno-9591/output/entry.ts` (Hits: 278)
- `crates/swc_bundler/tests/fixture/deno-9620/case1/output/entry.inlined.ts` (Hits: 207)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **react.js** (`crates/swc_ecma_minifier/benches/full/react.js`) — 402 inbound connections
2. **0.js** (`crates/swc_sourcemap/tests/fixtures/ram_bundle/file_bundle_1/js-modules/0.js`) — 127 inbound connections
3. **test_util.ts** (`crates/swc/tests/deno-unit/test_util.ts`) — 70 inbound connections
4. **Token.ts** (`crates/swc_bundler/tests/deno-exec/deno-8224/haystack-core/input/filter/Token.ts`) — 36 inbound connections
5. **ts.ts** (`crates/swc/tests/projects/issue-655/ts.ts`) — 32 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **lib.rs** (`crates/swc_ecma_ast/src/lib.rs`) — 441 outbound dependencies
2. **typescript.rs** (`crates/swc_estree_compat/src/babelify/typescript.rs`) — 158 outbound dependencies
3. **output.js** (`crates/swc_ecma_preset_env/tests/fixtures/corejs2/entry-shippedProposals/output.js`) — 149 outbound dependencies
4. **lib.rs** (`crates/swc_es_ast/src/lib.rs`) — 145 outbound dependencies
5. **expr.rs** (`crates/swc_estree_compat/src/swcify/expr.rs`) — 123 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `r1` **(Defensive Guards)** (@ `crates/swc_ecma_minifier/tests/fixture/next/react-pdf-renderer/output.js`) -> Impact: **1400.7** | LOC: 873
- `Yd` **(Many-Argument Workhorses)** (@ `crates/swc_ecma_minifier/tests/fixture/next/asmjs/1/output.js`) -> Impact: **1027.5** | LOC: 850
- `patchOuterDeco` **(Many-Argument Workhorses)** (@ `crates/swc_ecma_minifier/tests/fixture/next/31077/static/chunks/1606726a.10299989c08cb523/output.js`) -> Impact: **1025.2** | LOC: 692
- `dispatchKey` **(Many-Argument Workhorses)** (@ `crates/swc_ecma_minifier/tests/fixture/next/feedback-2/codemirror/input.js`) -> Impact: **885.3** | LOC: 1651
- `t` **(Defensive Guards)** (@ `crates/swc_ecma_minifier/tests/fixture/next/feedback-3/579-dcac359116b2707c/output.js`) -> Impact: **875.1** | LOC: 806
- `Yd` **(Many-Argument Workhorses)** (@ `crates/swc_ecma_minifier/tests/fixture/next/asmjs/1/input.js`) -> Impact: **857.8** | LOC: 1038
- `baseCreateRenderer` **(Many-Argument Workhorses)** (@ `crates/swc/benches/assets/renderer.ts`) -> Impact: **841.1** | LOC: 2065
  * *Intent:* // implementation
- `clone` **(Compute Cores)** (@ `crates/swc_ecma_minifier/tests/fixture/next/wrap-contracts/output.js`) -> Impact: **840.8** | LOC: 1147
  * *Intent:* /* * Create and return a BigNumber constructor.
- `parse` **(Compute Cores)** (@ `crates/swc_ecma_minifier/tests/benches-full/terser.js`) -> Impact: **806.7** | LOC: 823
- `OutputStream` **(Defensive Guards)** (@ `crates/swc_ecma_minifier/tests/benches-full/terser.js`) -> Impact: **802.3** | LOC: 772

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `crates/swc_ecma_minifier/benches/full` | 5 | 519800.25 | 73.21% | 22.71% |
| `crates/swc_ecma_parser/tests/tsc` | 7340 | 131014.03 | 1.09% | 0.0% |
| `crates/swc/tests/tsc-references` | 8618 | 121538.6 | 2.82% | 0.0% |
| `crates/swc_es_parser/tests/snapshots/ecma_reuse/tsc` | 4290 | 70426.22 | 0.0% | 0.0% |
| `crates/swc_ecma_minifier/tests/benches-full` | 4 | 51974.12 | 41.61% | 0.0% |
| `crates/swc_ecma_minifier/tests/projects/files` | 7 | 29585.98 | 70.4% | 0.0% |
| `crates/swc_html_parser/tests/html5lib-tests-fixture` | 1754 | 29585.0 | 0.0% | 0.0% |
| `crates/swc_es_parser/tests/snapshots/ecma_reuse/test262-parser/pass` | 1824 | 28306.46 | 0.0% | 0.0% |
| `crates/swc_ecma_parser/benches/files` | 6 | 27561.78 | 67.88% | 54.39% |
| `crates/swc_es_parser/benches/files` | 6 | 27561.78 | 67.88% | 54.39% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `packages/minifier/src/binding.d.ts` -> **100.0%** Exposure
- `crates/swc_allocator/src/allocators/scoped.rs` -> **100.0%** Exposure
- `crates/swc_common/src/pos.rs` -> **100.0%** Exposure
- `crates/swc_ecma_ast/src/source_map.rs` -> **100.0%** Exposure
- `crates/swc_ecma_codegen/src/text_writer.rs` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `crates/swc_ecma_transforms_module/tests/fixture/common/issue-5042/2/output.umd.ts` -> **100.0%** Exposure
- `crates/swc_arena/benches/bench.rs` -> **100.0%** Exposure
- `crates/swc_common/src/errors/styled_buffer.rs` -> **100.0%** Exposure
- `crates/swc_css_compat/src/compiler/color_alpha_parameter.rs` -> **100.0%** Exposure
- `crates/swc_css_minifier/src/compressor/unicode_range.rs` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `crates/swc_ecma_minifier/tests/fixture/next/wrap-contracts/output.js` -> **143** Orphaned Functions | **619** Duplicates
- `crates/swc_ecma_minifier/tests/benches-full/d3.js` -> **196** Orphaned Functions | **114** Duplicates
- `crates/swc/tests/tsc-references/generatedContextualTyping.1.normal.js` -> **40** Orphaned Functions | **138** Duplicates
- `crates/swc_ecma_transforms_optimization/tests/simplify_inlining.rs` -> **165** Orphaned Functions | **0** Duplicates
- `crates/swc_css_codegen/src/lib.rs` -> **163** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `crates/swc/tests/fixture/ecosystem-ci/1/input/1.ts` -> **67.9689%** Exposure
- `crates/swc/tests/fixture/ecosystem-ci/1/output/1.ts` -> **67.9689%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `4` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `24933` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `crates/swc_ecma_parser/benches/files/underscore-1.5.2.js` (JAVASCRIPT) -> Cumulative Risk: **727.24**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z +0.17)
- **Magnitude:** 1345.92 | **LOC:** 1277 | **CtrlFlow:** 30.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.8249%)
- **Heaviest Functions:** `eq` (Many-Argument Workhorses, Impact: 96.1), `template` (Many-Argument Workhorses, Impact: 30.8), `foldr` (Defensive Guards, Impact: 25.8)

### 2. `crates/swc_es_parser/benches/files/underscore-1.5.2.js` (JAVASCRIPT) -> Cumulative Risk: **727.24**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z +0.17)
- **Magnitude:** 1345.92 | **LOC:** 1277 | **CtrlFlow:** 30.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.8249%)
- **Heaviest Functions:** `eq` (Many-Argument Workhorses, Impact: 96.1), `template` (Many-Argument Workhorses, Impact: 30.8), `foldr` (Defensive Guards, Impact: 25.8)

### 3. `crates/swc_ecma_parser/benches/files/backbone-1.1.0.js` (JAVASCRIPT) -> Cumulative Risk: **697.0**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z +0.58)
- **Magnitude:** 1425.04 | **LOC:** 1582 | **CtrlFlow:** 37.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Cognitive Load (98.6857%)
- **Heaviest Functions:** `set` (Compute Cores, Impact: 87.6), `sync` (Defensive Guards, Impact: 47.0), `save` (Many-Argument Workhorses, Impact: 46.7)

### 4. `crates/swc_es_parser/benches/files/backbone-1.1.0.js` (JAVASCRIPT) -> Cumulative Risk: **697.0**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z +0.58)
- **Magnitude:** 1425.04 | **LOC:** 1582 | **CtrlFlow:** 37.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Cognitive Load (98.6857%)
- **Heaviest Functions:** `set` (Compute Cores, Impact: 87.6), `sync` (Defensive Guards, Impact: 47.0), `save` (Many-Argument Workhorses, Impact: 46.7)

### 5. `crates/swc_ecma_minifier/src/program_data.rs` (RUST) -> Cumulative Risk: **676.96**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.18)
- **Magnitude:** 547.18 | **LOC:** 746 | **CtrlFlow:** 15.8% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.999%), Tech Debt (99.0913%), Documentation (91.5254%)
- **Heaviest Functions:** `merge` (Many-Argument Workhorses, Impact: 63.4), `report_assign` (Many-Argument Workhorses, Impact: 42.1), `declare_decl` (Many-Argument Workhorses, Impact: 40.3)

### 6. `crates/swc_ecma_transforms_base/src/helpers/_async_generator_delegate.js` (JAVASCRIPT) -> Cumulative Risk: **674.16**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z +0.16)
- **Magnitude:** 57.88 | **LOC:** 40 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.3307%)
- **Heaviest Functions:** `_async_generator_delegate` (Defensive Guards, Impact: 13.3), `next` (Callbacks & Closures, Impact: 3.2), `throw` (Callbacks & Closures, Impact: 3.2)

### 7. `packages/helpers/esm/_async_generator_delegate.js` (JAVASCRIPT) -> Cumulative Risk: **673.58**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z +0.05)
- **Magnitude:** 59.42 | **LOC:** 52 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (98.7872%)
- **Heaviest Functions:** `_async_generator_delegate` (Defensive Guards, Impact: 13.7), `next` (Callbacks & Closures, Impact: 3.3), `throw` (Callbacks & Closures, Impact: 3.2)

### 8. `crates/swc_ecma_minifier/benches/full/d3.js` (JAVASCRIPT) -> Cumulative Risk: **672.25**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.09)
- **Magnitude:** 23355.8 | **LOC:** 19567 | **CtrlFlow:** 23.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Cognitive Load (96.8638%)
- **Heaviest Functions:** `brush$1` (Defensive Guards, Impact: 235.6), `started` (Compute Cores, Impact: 176.3), `clipRectangle` (Many-Argument Workhorses, Impact: 133.1)

### 9. `crates/swc_ecma_parser/benches/files/mootools-1.4.5.js` (JAVASCRIPT) -> Cumulative Risk: **671.25**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z +0.49)
- **Magnitude:** 5410.4 | **LOC:** 6448 | **CtrlFlow:** 31.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (98.5292%)
- **Heaviest Functions:** `matchNode` (Many-Argument Workhorses, Impact: 498.1), `search` (Many-Argument Workhorses, Impact: 278.7), `parser` (Many-Argument Workhorses, Impact: 174.6)

### 10. `crates/swc_es_parser/benches/files/mootools-1.4.5.js` (JAVASCRIPT) -> Cumulative Risk: **671.25**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z +0.49)
- **Magnitude:** 5410.4 | **LOC:** 6448 | **CtrlFlow:** 31.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (98.5292%)
- **Heaviest Functions:** `matchNode` (Many-Argument Workhorses, Impact: 498.1), `search` (Many-Argument Workhorses, Impact: 278.7), `parser` (Many-Argument Workhorses, Impact: 174.6)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `crates/swc_ecma_minifier/benches/full/lodash.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 480917.15 | **LOC:** 17210 | **CtrlFlow:** 30.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (43.6139%), Tech Debt (8.0981%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 11 instances
* *Amplified Cascading Flux:* 943 instances
* *Concurrency (weighted view):* 73
* *State Mutation (weighted view):* 3273
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1800`, `structural_boundaries: 1577`, `args: 693`, `func_start: 512`
* *Risk/State:* `safety_bypasses: 338`, `state_mutation: 1387`, `dead_code: 5`, `planned_debt: 1`, `fragile_debt: 2`
* *Architecture:* `api: 1`, `concurrency: 18`, `import: 1`
* *Defense:* `safety: 300`, `doc: 680`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.017
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/swc_ecma_minifier/benches/full/d3.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 23355.8 | **LOC:** 19567 | **CtrlFlow:** 23.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (96.8638%), Tech Debt (64.3966%)
**Top Internal Functions/Classes:**
  * `brush$1` **(Defensive Guards)** (Impact: 235.6)
  * `started` **(Compute Cores)** (Impact: 176.3)
  * `clipRectangle` **(Many-Argument Workhorses)** (Impact: 133.1)
    * *Intent:* // TODO Use d3-polygon’s polygonContains here for the ring check? // TODO Eliminate duplicate buffer...
  * `zoom` **(Defensive Guards)** (Impact: 119.8)
  * `clipLine` **(Many-Argument Workhorses)** (Impact: 106.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 15 instances
* *Amplified Cascading Flux:* 2767 instances
* *Concurrency (weighted view):* 95
* *State Mutation (weighted view):* 9757
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3866`, `structural_boundaries: 3682`, `args: 2246`, `func_start: 2031`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 216`, `high_risk_execution: 4`, `state_mutation: 4223`, `dead_code: 5`, `planned_debt: 18`, `duplicate_logic: 113`, `unreferenced_by_name: 50`
* *Architecture:* `io: 4`, `api: 549`, `concurrency: 20`
* *Defense:* `safety: 901`, `test: 6`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.017
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/swc_ecma_minifier/tests/benches-full/three.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 21635.54 | **LOC:** 16409 | **CtrlFlow:** 31.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.0878%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `WebGLTextures` **(Defensive Guards)** (Impact: 657.8)
  * `WebGLRenderer` **(Defensive Guards)** (Impact: 407.2)
  * `WebGLProgram` **(Many-Argument Workhorses)** (Impact: 398.2)
  * `earcutLinked` **(Defensive Guards)** (Impact: 290.7)
  * `ObjectLoader` **(Defensive Guards)** (Impact: 230.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 1571 instances
* *Concurrency (weighted view):* 33
* *State Mutation (weighted view):* 5209
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4752`, `structural_boundaries: 3972`, `args: 2378`, `func_start: 2190`
* *Risk/State:* `safety_bypasses: 919`, `state_mutation: 2067`, `dead_code: 29`, `planned_debt: 12`, `duplicate_logic: 134`
* *Architecture:* `io: 4`, `api: 309`, `concurrency: 13`
* *Defense:* `safety: 1969`, `doc: 46`, `sync_locks: 6`, `immutability_locks: 3`, `cleanup: 42`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.017
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/swc_ecma_minifier/tests/benches-full/d3.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 14862.3 | **LOC:** 11247 | **CtrlFlow:** 32.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.3632%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `clipRectangle` **(Many-Argument Workhorses)** (Impact: 208.9)
    * *Intent:* // TODO Use d3-polygon’s polygonContains here for the ring check? // TODO Eliminate duplicate buffer...
  * `brush$1` **(Defensive Guards)** (Impact: 204.7)
  * `started` **(Defensive Guards)** (Impact: 155.6)
  * `zoom` **(Defensive Guards)** (Impact: 104.8)
  * `formatLocale` **(Defensive Guards)** (Impact: 101.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 958 instances
* *High Risk Execution (weighted view):* 1
* *Concurrency (weighted view):* 50
* *State Mutation (weighted view):* 3144
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3643`, `structural_boundaries: 3304`, `args: 2227`, `func_start: 1907`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 497`, `high_risk_execution: 3`, `state_mutation: 1228`, `dead_code: 5`, `planned_debt: 15`, `duplicate_logic: 114`, `unreferenced_by_name: 196`
* *Architecture:* `io: 4`, `concurrency: 20`
* *Defense:* `safety: 692`, `test: 6`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.017
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/swc_ecma_minifier/tests/projects/files/angular-1.2.5.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 13424.62 | **LOC:** 21880 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (64.3641%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getterFn` **(Many-Argument Workhorses)** (Impact: 628.3)
  * `$CompileProvider` **(Many-Argument Workhorses)** (Impact: 539.6)
  * `applyDirectivesToNode` **(Many-Argument Workhorses)** (Impact: 352.5)
    * *Intent:* * @param {function(angular.Scope[, cloneAttachFn]} transcludeFn A linking function, where the * scop...
  * `link` **(Many-Argument Workhorses)** (Impact: 242.1)
  * `minErr` **(Compute Cores)** (Impact: 181.3)
    * *Intent:* * * If fewer arguments are specified than necessary for interpolation, the extra * interpolation mar...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 7 instances
* *Amplified Race Conditions:* 28 instances
* *Amplified Cascading Flux:* 1339 instances
* *High Risk Execution (weighted view):* 14
* *Concurrency (weighted view):* 180
* *State Mutation (weighted view):* 4378
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2268`, `structural_boundaries: 1529`, `args: 1055`, `func_start: 689`
* *Risk/State:* `safety_bypasses: 188`, `high_risk_execution: 21`, `state_mutation: 1700`, `dead_code: 36`, `planned_debt: 17`, `fragile_debt: 12`, `duplicate_logic: 10`, `unreferenced_by_name: 47`
* *Architecture:* `io: 4`, `api: 1`, `concurrency: 40`
* *Defense:* `safety: 413`, `doc: 438`, `test: 203`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.017
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/swc_ecma_parser/benches/files/angular-1.2.5.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 13409.94 | **LOC:** 20369 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (53.5999%), Tech Debt (24.4496%)
**Top Internal Functions/Classes:**
  * `getterFn` **(Many-Argument Workhorses)** (Impact: 619.6)
  * `$CompileProvider` **(Many-Argument Workhorses)** (Impact: 548.6)
  * `applyDirectivesToNode` **(Many-Argument Workhorses)** (Impact: 343.8)
    * *Intent:* * @param {function(angular.Scope[, cloneAttachFn]} transcludeFn A linking function, where the * scop...
  * `link` **(Many-Argument Workhorses)** (Impact: 238.3)
  * `minErr` **(Compute Cores)** (Impact: 180.1)
    * *Intent:* * * If fewer arguments are specified than necessary for interpolation, the extra * interpolation mar...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 7 instances
* *Amplified Race Conditions:* 30 instances
* *Amplified Cascading Flux:* 1361 instances
* *High Risk Execution (weighted view):* 14
* *Concurrency (weighted view):* 190
* *State Mutation (weighted view):* 4391
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2268`, `structural_boundaries: 1529`, `args: 1055`, `func_start: 684`
* *Risk/State:* `safety_bypasses: 188`, `high_risk_execution: 21`, `state_mutation: 1669`, `dead_code: 36`, `planned_debt: 17`, `fragile_debt: 12`, `duplicate_logic: 6`, `unreferenced_by_name: 50`
* *Architecture:* `io: 6`, `api: 1`, `concurrency: 40`
* *Defense:* `safety: 413`, `doc: 438`, `test: 203`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.017
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/swc_es_parser/benches/files/angular-1.2.5.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 13409.94 | **LOC:** 20369 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (53.5999%), Tech Debt (24.4496%)
**Top Internal Functions/Classes:**
  * `getterFn` **(Many-Argument Workhorses)** (Impact: 619.6)
  * `$CompileProvider` **(Many-Argument Workhorses)** (Impact: 548.6)
  * `applyDirectivesToNode` **(Many-Argument Workhorses)** (Impact: 343.8)
    * *Intent:* * @param {function(angular.Scope[, cloneAttachFn]} transcludeFn A linking function, where the * scop...
  * `link` **(Many-Argument Workhorses)** (Impact: 238.3)
  * `minErr` **(Compute Cores)** (Impact: 180.1)
    * *Intent:* * * If fewer arguments are specified than necessary for interpolation, the extra * interpolation mar...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 7 instances
* *Amplified Race Conditions:* 30 instances
* *Amplified Cascading Flux:* 1361 instances
* *High Risk Execution (weighted view):* 14
* *Concurrency (weighted view):* 190
* *State Mutation (weighted view):* 4391
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2268`, `structural_boundaries: 1529`, `args: 1055`, `func_start: 684`
* *Risk/State:* `safety_bypasses: 188`, `high_risk_execution: 21`, `state_mutation: 1669`, `dead_code: 36`, `planned_debt: 17`, `fragile_debt: 12`, `duplicate_logic: 6`, `unreferenced_by_name: 50`
* *Architecture:* `io: 6`, `api: 1`, `concurrency: 40`
* *Defense:* `safety: 413`, `doc: 438`, `test: 203`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.017
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/swc_ecma_minifier/benches/full/vue.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 10078.0 | **LOC:** 11966 | **CtrlFlow:** 30.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.9287%), Tech Debt (9.2757%)
**Top Internal Functions/Classes:**
  * `createPatchFunction` **(Compute Cores)** (Impact: 351.2)
  * `parseHTML` **(Compute Cores)** (Impact: 149.4)
  * `patchVnode` **(Many-Argument Workhorses)** (Impact: 98.9)
  * `enter` **(Compute Cores)** (Impact: 97.6)
    * *Intent:* /* */
  * `addHandler` **(Many-Argument Workhorses)** (Impact: 97.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 9 instances
* *Amplified Race Conditions:* 24 instances
* *Amplified Cascading Flux:* 1091 instances
* *High Risk Execution (weighted view):* 2
* *Concurrency (weighted view):* 152
* *State Mutation (weighted view):* 3443
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2873`, `structural_boundaries: 2000`, `args: 675`, `func_start: 645`
* *Risk/State:* `safety_bypasses: 63`, `high_risk_execution: 11`, `state_mutation: 1261`, `dead_code: 31`, `planned_debt: 1`, `fragile_debt: 13`
* *Architecture:* `api: 17`, `concurrency: 32`
* *Defense:* `safety: 649`, `doc: 118`, `immutability_locks: 2`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.017
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/swc_ecma_minifier/tests/projects/output/angular-1.2.5.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 8589.12 | **LOC:** 12187 | **CtrlFlow:** 31.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (50.2153%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getterFn` **(Many-Argument Workhorses)** (Impact: 549.3)
  * `$CompileProvider` **(Many-Argument Workhorses)** (Impact: 480.0)
    * *Intent:* * var templateHTML = angular.element('<p>{{total}}</p>'), * scope = ....; * * var clonedElement = $c...
  * `compileNodes` **(Many-Argument Workhorses)** (Impact: 359.3)
    * *Intent:* /** * Compile function matches each node in nodeList against the directives. Once all directives * f...
  * `$HttpProvider` **(Compute Cores)** (Impact: 250.6)
  * `link` **(Many-Argument Workhorses)** (Impact: 206.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 6 instances
* *Amplified Race Conditions:* 18 instances
* *Amplified Cascading Flux:* 549 instances
* *High Risk Execution (weighted view):* 12
* *Concurrency (weighted view):* 128
* *State Mutation (weighted view):* 1839
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2081`, `structural_boundaries: 1179`, `args: 1024`, `func_start: 527`
* *Risk/State:* `safety_bypasses: 300`, `high_risk_execution: 18`, `state_mutation: 741`, `dead_code: 28`, `planned_debt: 14`, `fragile_debt: 11`, `duplicate_logic: 5`, `unreferenced_by_name: 12`
* *Architecture:* `io: 19`, `api: 1`, `concurrency: 38`
* *Defense:* `safety: 360`, `doc: 375`, `test: 160`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.017
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/swc_ecma_minifier/tests/benches-full/terser.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 7991.4 | **LOC:** 20385 | **CtrlFlow:** 30.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (32.8753%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `parse` **(Compute Cores)** (Impact: 806.7)
  * `OutputStream` **(Defensive Guards)** (Impact: 802.3)
  * `statement1` **(Many-Argument Workhorses)** (Impact: 282.5)
  * `run_cli` **(Defensive Guards)** (Impact: 187.0)
  * `helpInformation` **(Defensive Guards)** (Impact: 121.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 9 instances
* *Amplified Race Conditions:* 10 instances
* *Amplified Cascading Flux:* 813 instances
* *High Risk Execution (weighted view):* 3
* *Concurrency (weighted view):* 176
* *State Mutation (weighted view):* 2543
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5798`, `structural_boundaries: 3318`, `args: 1750`, `func_start: 719`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 625`, `high_risk_execution: 12`, `state_mutation: 917`, `dead_code: 25`, `planned_debt: 10`, `fragile_debt: 7`, `duplicate_logic: 22`
* *Architecture:* `io: 22`, `api: 23`, `concurrency: 126`, `import: 5`
* *Defense:* `safety: 2086`, `doc: 43`, `test: 36`, `sync_locks: 2`, `immutability_locks: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.017
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` source-map, acorn, assert_clause:, is_default:
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/swc_ecma_minifier/tests/benches-full/vue.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 7484.88 | **LOC:** 4452 | **CtrlFlow:** 69.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (37.1156%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ast` **(Defensive Guards)** (Impact: 380.4)
    * *Intent:* /* */ var ref$1 = (baseCompile = function(template, options) {
  * `patch` **(Compute Cores)** (Impact: 296.5)
  * `createComponent` **(Many-Argument Workhorses)** (Impact: 199.1)
  * `patchVnode` **(Defensive Guards)** (Impact: 144.8)
  * `genData$2` **(Defensive Guards)** (Impact: 133.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Race Conditions:* 19 instances
* *Amplified Cascading Flux:* 435 instances
* *High Risk Execution (weighted view):* 2
* *Concurrency (weighted view):* 127
* *State Mutation (weighted view):* 1359
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2645`, `structural_boundaries: 1203`, `args: 617`, `func_start: 407`
* *Risk/State:* `safety_bypasses: 178`, `high_risk_execution: 6`, `state_mutation: 489`, `dead_code: 22`, `planned_debt: 1`, `fragile_debt: 7`, `duplicate_logic: 2`
* *Architecture:* `api: 18`, `concurrency: 32`
* *Defense:* `safety: 561`, `doc: 97`, `immutability_locks: 2`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.017
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/swc_ecma_parser/tests/typescript/next/stack-overflow/1/input.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 7250.0 | **LOC:** 6923 | **CtrlFlow:** 25.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `q` **(Compute Cores)** (Impact: 384.1)
  * `formatAttributes` **(Compute Cores)** (Impact: 195.3)
  * `parse` **(Compute Cores)** (Impact: 142.1)
  * `h` **(Callbacks & Closures)** (Impact: 106.7)
  * `transform` **(Compute Cores)** (Impact: 55.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Rce:* 1 instances
* *Amplified Race Conditions:* 43 instances
* *Amplified Cascading Flux:* 835 instances
* *Concurrency (weighted view):* 324
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 2807
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1707`, `structural_boundaries: 1326`, `args: 701`, `func_start: 497`, `class_start: 34`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 1137`, `duplicate_logic: 13`
* *Architecture:* `io: 48`, `api: 20`, `concurrency: 109`, `import: 10`
* *Defense:* `safety: 57`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.017
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` crypto, fs, cssnano-simple, lru-cache, node-fetch, postcss-safe-parser, terser, path...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/swc_ecma_minifier/tests/projects/files/yui-3.12.0.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 6218.82 | **LOC:** 11137 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (53.2363%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `addModule` **(Many-Argument Workhorses)** (Impact: 160.3)
    * *Intent:* * @param {Array} [config.lang] Array of BCP 47 language tags of languages for which this module has ...
  * `parseUA` **(Compute Cores)** (Impact: 130.3)
    * *Intent:* * these fields can have. * @class UA * @static */ /** * Static method on `YUI.Env` for parsing a UA ...
  * `getRequires` **(Compute Cores)** (Impact: 117.6)
    * *Intent:* /** * Returns an object containing properties for all modules required * in order to load the reques...
  * `resolve` **(Many-Argument Workhorses)** (Impact: 114.3)
    * *Intent:* * @return {Object} Object hash (js and css) of two arrays of file lists * @example This method can b...
  * `_use` **(Many-Argument Workhorses)** (Impact: 113.1)
    * *Intent:* **/
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 18 instances
* *Amplified Cascading Flux:* 1025 instances
* *Concurrency (weighted view):* 115
* *State Mutation (weighted view):* 3173
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1427`, `structural_boundaries: 401`, `args: 251`, `func_start: 203`
* *Risk/State:* `safety_bypasses: 20`, `high_risk_execution: 2`, `state_mutation: 1123`, `dead_code: 13`, `planned_debt: 18`, `fragile_debt: 12`, `duplicate_logic: 42`, `unreferenced_by_name: 21`
* *Architecture:* `api: 1`, `concurrency: 25`, `import: 5`
* *Defense:* `safety: 164`, `doc: 258`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.017
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` yui-log
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/swc_ecma_parser/benches/files/yui-3.12.0.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 5959.88 | **LOC:** 11543 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (59.2178%), Tech Debt (32.7636%)
**Top Internal Functions/Classes:**
  * `addModule` **(Many-Argument Workhorses)** (Impact: 159.5)
    * *Intent:* * @param {Array} [config.lang] Array of BCP 47 language tags of languages for which this module has ...
  * `parseUA` **(Compute Cores)** (Impact: 130.6)
    * *Intent:* * these fields can have. * @class UA * @static */ /** * Static method on `YUI.Env` for parsing a UA ...
  * `getRequires` **(Compute Cores)** (Impact: 116.9)
    * *Intent:* /** * Returns an object containing properties for all modules required * in order to load the reques...
  * `_use` **(Many-Argument Workhorses)** (Impact: 113.2)
    * *Intent:* **/
  * `resolve` **(Many-Argument Workhorses)** (Impact: 112.8)
    * *Intent:* * @return {Object} Object hash (js and css) of two arrays of file lists * @example This method can b...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 17 instances
* *Amplified Cascading Flux:* 1026 instances
* *Concurrency (weighted view):* 110
* *State Mutation (weighted view):* 3175
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1427`, `structural_boundaries: 401`, `args: 251`, `func_start: 170`
* *Risk/State:* `safety_bypasses: 20`, `high_risk_execution: 2`, `state_mutation: 1123`, `dead_code: 13`, `planned_debt: 18`, `fragile_debt: 12`, `duplicate_logic: 14`, `unreferenced_by_name: 20`
* *Architecture:* `api: 1`, `concurrency: 25`, `import: 5`
* *Defense:* `safety: 164`, `doc: 258`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.017
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` yui-log
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/swc_es_parser/benches/files/yui-3.12.0.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 5959.88 | **LOC:** 11543 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (59.2178%), Tech Debt (32.7636%)
**Top Internal Functions/Classes:**
  * `addModule` **(Many-Argument Workhorses)** (Impact: 159.5)
    * *Intent:* * @param {Array} [config.lang] Array of BCP 47 language tags of languages for which this module has ...
  * `parseUA` **(Compute Cores)** (Impact: 130.6)
    * *Intent:* * these fields can have. * @class UA * @static */ /** * Static method on `YUI.Env` for parsing a UA ...
  * `getRequires` **(Compute Cores)** (Impact: 116.9)
    * *Intent:* /** * Returns an object containing properties for all modules required * in order to load the reques...
  * `_use` **(Many-Argument Workhorses)** (Impact: 113.2)
    * *Intent:* **/
  * `resolve` **(Many-Argument Workhorses)** (Impact: 112.8)
    * *Intent:* * @return {Object} Object hash (js and css) of two arrays of file lists * @example This method can b...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 17 instances
* *Amplified Cascading Flux:* 1026 instances
* *Concurrency (weighted view):* 110
* *State Mutation (weighted view):* 3175
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1427`, `structural_boundaries: 401`, `args: 251`, `func_start: 170`
* *Risk/State:* `safety_bypasses: 20`, `high_risk_execution: 2`, `state_mutation: 1123`, `dead_code: 13`, `planned_debt: 18`, `fragile_debt: 12`, `duplicate_logic: 14`, `unreferenced_by_name: 20`
* *Architecture:* `api: 1`, `concurrency: 25`, `import: 5`
* *Defense:* `safety: 164`, `doc: 258`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.017
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` yui-log
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/swc_ecma_minifier/tests/projects/files/mootools-1.4.5.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 5628.9 | **LOC:** 7246 | **CtrlFlow:** 25.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `matchNode` **(Many-Argument Workhorses)** (Impact: 506.4)
  * `search` **(Many-Argument Workhorses)** (Impact: 281.4)
  * `parser` **(Many-Argument Workhorses)** (Impact: 175.6)
  * `setDocument` **(Defensive Guards)** (Impact: 98.5)
  * `send` **(Compute Cores)** (Impact: 54.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 11 instances
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 808 instances
* *High Risk Execution (weighted view):* 9
* *Concurrency (weighted view):* 23
* *State Mutation (weighted view):* 2598
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1445`, `structural_boundaries: 1354`, `args: 672`, `func_start: 495`
* *Risk/State:* `safety_bypasses: 304`, `high_risk_execution: 20`, `state_mutation: 982`, `dead_code: 4`, `planned_debt: 64`, `fragile_debt: 2`, `duplicate_logic: 10`, `unreferenced_by_name: 44`
* *Architecture:* `io: 4`, `concurrency: 8`
* *Defense:* `safety: 107`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.017
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/swc_ecma_parser/benches/files/mootools-1.4.5.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 5410.4 | **LOC:** 6448 | **CtrlFlow:** 31.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (98.3021%), Tech Debt (72.6077%)
**Top Internal Functions/Classes:**
  * `matchNode` **(Many-Argument Workhorses)** (Impact: 498.1)
  * `search` **(Many-Argument Workhorses)** (Impact: 278.7)
  * `parser` **(Many-Argument Workhorses)** (Impact: 174.6)
  * `setDocument` **(Defensive Guards)** (Impact: 96.0)
  * `send` **(Compute Cores)** (Impact: 53.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 11 instances
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 766 instances
* *High Risk Execution (weighted view):* 9
* *Concurrency (weighted view):* 23
* *State Mutation (weighted view):* 2437
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1445`, `structural_boundaries: 1354`, `args: 672`, `func_start: 468`
* *Risk/State:* `safety_bypasses: 304`, `high_risk_execution: 20`, `state_mutation: 905`, `dead_code: 4`, `planned_debt: 64`, `fragile_debt: 2`, `duplicate_logic: 10`, `unreferenced_by_name: 45`
* *Architecture:* `io: 4`, `concurrency: 8`
* *Defense:* `safety: 107`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.017
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/swc_es_parser/benches/files/mootools-1.4.5.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 5410.4 | **LOC:** 6448 | **CtrlFlow:** 31.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (98.3021%), Tech Debt (72.6077%)
**Top Internal Functions/Classes:**
  * `matchNode` **(Many-Argument Workhorses)** (Impact: 498.1)
  * `search` **(Many-Argument Workhorses)** (Impact: 278.7)
  * `parser` **(Many-Argument Workhorses)** (Impact: 174.6)
  * `setDocument` **(Defensive Guards)** (Impact: 96.0)
  * `send` **(Compute Cores)** (Impact: 53.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 11 instances
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 766 instances
* *High Risk Execution (weighted view):* 9
* *Concurrency (weighted view):* 23
* *State Mutation (weighted view):* 2437
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1445`, `structural_boundaries: 1354`, `args: 672`, `func_start: 468`
* *Risk/State:* `safety_bypasses: 304`, `high_risk_execution: 20`, `state_mutation: 905`, `dead_code: 4`, `planned_debt: 64`, `fragile_debt: 2`, `duplicate_logic: 10`, `unreferenced_by_name: 45`
* *Architecture:* `io: 4`, `concurrency: 8`
* *Defense:* `safety: 107`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.017
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `.github/swc-ecosystem-ci/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.017
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/swc_ecma_minifier/benches/full/moment.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 4022.48 | **LOC:** 5671 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.8878%), Tech Debt (9.7163%)
**Top Internal Functions/Classes:**
  * `createDuration` **(Many-Argument Workhorses)** (Impact: 43.4)
  * `getSetOffset` **(Defensive Guards)** (Impact: 42.1)
    * *Intent:* // MOMENTS // keepLocalTime = true means only change the timezone, without // affecting the local ho...
  * `checkOverflow` **(Defensive Guards)** (Impact: 38.9)
  * `configFromArray` **(Defensive Guards)** (Impact: 38.3)
    * *Intent:* // convert an array to a date. // the array should mirror the parameters below // note: all values p...
  * `isValid` **(Defensive Guards)** (Impact: 31.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 643 instances
* *State Mutation (weighted view):* 2237
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1203`, `structural_boundaries: 696`, `args: 347`, `func_start: 285`
* *Risk/State:* `safety_bypasses: 80`, `state_mutation: 951`, `dead_code: 6`, `planned_debt: 11`, `unreferenced_by_name: 2`
* *Architecture:* `api: 2`
* *Defense:* `safety: 223`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.017
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/swc_es_parser/src/parser.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 3840.2 | **LOC:** 7092 | **CtrlFlow:** 22.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (24.6069%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `parse_export_decl` **(Compute Cores)** (Impact: 139.8)
  * `parse_jsx_element_expr` **(Compute Cores)** (Impact: 112.4)
  * `parse_class_expr` **(Compute Cores)** (Impact: 109.2)
  * `parse_postfix_expr` **(Compute Cores)** (Impact: 94.9)
  * `parse_ts_primary_type` **(Compute Cores)** (Impact: 92.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 232 instances
* *Concurrency (weighted view):* 53
* *State Mutation (weighted view):* 731
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1462`, `structural_boundaries: 1441`, `args: 275`, `func_start: 215`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 122`, `high_risk_execution: 15`, `state_mutation: 267`
* *Architecture:* `api: 47`, `concurrency: 23`, `import: 9`
* *Defense:* `safety: 31`, `doc: 11`, `test: 111`, `immutability_locks: 27`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.017
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ArrayPat, AssignExpr, AssignOp, AstStore, BigIntLit, BinaryExpr, BinaryOp, BlockStmt...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/swc_ecma_minifier/tests/projects/output/mootools-1.4.5.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 3798.1 | **LOC:** 4346 | **CtrlFlow:** 36.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `matchNode` **(Compute Cores)** (Impact: 462.5)
  * `search` **(Compute Cores)** (Impact: 264.0)
  * `parser` **(Many-Argument Workhorses)** (Impact: 172.5)
    * *Intent:* */ "^(?:\\s*(,)\\s*|\\s*(<combinator>+)\\s*|(\\s+)|(<unicode>+|\\*)|\\#(<unicode>+)|\\.(<unicode>+)|...
  * `setDocument` **(Defensive Guards)** (Impact: 88.2)
  * `send` **(Compute Cores)** (Impact: 50.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 11 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 359 instances
* *High Risk Execution (weighted view):* 9
* *Concurrency (weighted view):* 13
* *State Mutation (weighted view):* 1145
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1399`, `structural_boundaries: 1187`, `args: 672`, `func_start: 442`
* *Risk/State:* `safety_bypasses: 301`, `high_risk_execution: 20`, `state_mutation: 427`, `dead_code: 4`, `planned_debt: 64`, `fragile_debt: 2`, `duplicate_logic: 8`, `unreferenced_by_name: 45`
* *Architecture:* `io: 4`, `concurrency: 8`
* *Defense:* `safety: 107`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.017
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/swc_ecma_minifier/tests/projects/output/yui-3.12.0.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 3541.36 | **LOC:** 7800 | **CtrlFlow:** 27.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (32.3543%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `addModule` **(Compute Cores)** (Impact: 144.5)
    * *Intent:* * @param {String} [config.group] The group the module belongs to -- this is set automatically when i...
  * `parseUA` **(Compute Cores)** (Impact: 111.6)
    * *Intent:* * looking for a particular range of versions. Because of this, * some of the granularity of the vers...
  * `getRequires` **(Compute Cores)** (Impact: 107.8)
    * *Intent:* /** * Returns an object containing properties for all modules required * in order to load the reques...
  * `resolve` **(Compute Cores)** (Impact: 102.7)
    * *Intent:* * @param {Array} [s=loader.sorted] An override for the loader.sorted array * @return {Object} Object...
  * `mix` **(Many-Argument Workhorses)** (Impact: 95.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 10 instances
* *Amplified Cascading Flux:* 339 instances
* *Concurrency (weighted view):* 75
* *State Mutation (weighted view):* 1047
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1342`, `structural_boundaries: 371`, `args: 250`, `func_start: 183`
* *Risk/State:* `safety_bypasses: 36`, `high_risk_execution: 2`, `state_mutation: 369`, `dead_code: 6`, `planned_debt: 14`, `fragile_debt: 8`, `duplicate_logic: 44`, `unreferenced_by_name: 19`
* *Architecture:* `api: 1`, `concurrency: 25`, `import: 5`
* *Defense:* `safety: 146`, `doc: 254`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.017
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` yui-log
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/swc_ecma_parser/src/parser/typescript.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 2650.84 | **LOC:** 5212 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (12.3796%), Tech Debt (8.9588%)
**Top Internal Functions/Classes:**
  * `parse_ts_non_array_type` **(Compute Cores)** (Impact: 152.5)
    * *Intent:* /// `tsParseNonArrayType`
  * `parse_ts_decl` **(Many-Argument Workhorses)** (Impact: 140.5)
    * *Intent:* /// Common to tsTryParseDeclare, tsTryParseExportDeclaration, and /// tsParseExpressionStatement. //...
  * `try_parse_ts_declare` **(Many-Argument Workhorses)** (Impact: 114.7)
    * *Intent:* /// `tsTryParseDeclare`
  * `parse_ts_type_param` **(Many-Argument Workhorses)** (Impact: 110.3)
    * *Intent:* /// `tsParseTypeParameter`
  * `parse_flow_component_param` **(Many-Argument Workhorses)** (Impact: 96.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 55 instances
* *High Risk Execution (weighted view):* 10
* *State Mutation (weighted view):* 173
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1105`, `structural_boundaries: 836`, `args: 275`, `func_start: 128`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 93`, `high_risk_execution: 11`, `state_mutation: 63`, `planned_debt: 1`, `fragile_debt: 5`
* *Architecture:* `api: 31`, `concurrency: 1`, `import: 11`
* *Defense:* `safety: 24`, `doc: 93`, `test: 71`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.017
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Atom, Context, PResult, Parser, Span, Spanned, Syntax, Wtf8Atom...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `crates/swc_html_parser/src/parser/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 2398.9 | **LOC:** 8723 | **CtrlFlow:** 19.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (62.7494%), Tech Debt (8.0103%)
**Top Internal Functions/Classes:**
  * `process_token` **(Many-Argument Workhorses)** (Impact: 396.6)
  * `process_token_in_foreign_content` **(Many-Argument Workhorses)** (Impact: 89.6)
  * `run_the_adoption_agency_algorithm` **(Many-Argument Workhorses)** (Impact: 85.6)
    * *Intent:* // // 17. Append that new element to furthest block. // // 18. Remove formatting element from the li...
  * `get_appropriate_place_for_inserting_node` **(Compute Cores)** (Impact: 75.5)
    * *Intent:* // These steps are involved in part because it's possible for elements, the // table element in this...
  * `reset_insertion_mode` **(Compute Cores)** (Impact: 68.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 17 instances
* *Amplified Cascading Flux:* 319 instances
* *High Risk Execution (weighted view):* 19
* *State Mutation (weighted view):* 1121
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1009`, `structural_boundaries: 474`, `args: 250`, `func_start: 49`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 23`, `high_risk_execution: 36`, `state_mutation: 483`, `dead_code: 11`, `unreferenced_by_name: 3`
* *Architecture:* `api: 12`, `import: 10`
* *Defense:* `safety: 64`, `doc: 3`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.017
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Atom, DUMMY_SP, ErrorKind, ParserInput, active_formatting_element_stack::*, crate::
    error::Error, doctypes::*, lexer::State...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `crates/swc_ecma_minifier/src/compress/optimize/mod.rs` -> Churn: **50.61%** | Cog Load: 29.6723% | Debt: 73.1873%
- `crates/swc_ecma_minifier/src/compress/optimize/unused.rs` -> Churn: **50.61%** | Cog Load: 24.1385% | Debt: 54.029%
- `crates/swc_ecma_minifier/src/program_data.rs` -> Churn: **50.61%** | Cog Load: 54.6604% | Debt: 99.0913%
- `crates/swc_ecma_transforms_base/src/helpers/_wrap_reg_exp.js` -> Churn: **50.61%** | Cog Load: 100.0% | Debt: 90.9512%
- `packages/helpers/esm/_wrap_reg_exp.js` -> Churn: **50.61%** | Cog Load: 100.0% | Debt: 70.9934%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `crates/swc_es_parser/src/parser.rs` -> **Donny/강동윤** (100.0% isolated ownership) | Magnitude: 3840.2
- `crates/swc_ecma_parser/src/parser/typescript.rs` -> **Donny/강동윤** (100.0% isolated ownership) | Magnitude: 2650.84
- `crates/swc_ecma_transforms_proposal/src/decorator_impl.rs` -> **Donny/강동윤** (100.0% isolated ownership) | Magnitude: 1666.64
- `crates/swc_ecma_parser/src/parser/stmt.rs` -> **Donny/강동윤** (100.0% isolated ownership) | Magnitude: 1570.42
- `crates/swc_ecma_minifier/src/compress/pure/misc.rs` -> **Donny/강동윤** (100.0% isolated ownership) | Magnitude: 1513.66

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `crates/swc_ecma_minifier/benches/full/react.js` -> **Severity: 0.4** (Embedded: 0.007 * Error Risk: 57.5285%)
- `crates/swc/tests/deno-unit/test_util.ts` -> **Severity: 0.083** (Embedded: 0.0012 * Error Risk: 68.5742%)
- `crates/swc_node_bundler/tests/pass/deno-001/full/input/io/bufio.ts` -> **Severity: 0.058** (Embedded: 0.0007 * Error Risk: 86.5113%)
- `crates/swc_node_bundler/tests/pass/deno-001/full/input/bytes/mod.ts` -> **Severity: 0.041** (Embedded: 0.0005 * Error Risk: 89.9505%)
- `crates/swc_bundler/tests/deno-exec/deno-8224/haystack-core/input/core/HGrid.ts` -> **Severity: 0.04** (Embedded: 0.0005 * Error Risk: 82.799%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `crates/swc_ecma_minifier/benches/full/react.js` -> **Severity: 445.781** (Blast Radius: 5.758 * Doc Risk: 77.4194%)
- `crates/swc/tests/deno-unit/test_util.ts` -> **Severity: 49.034** (Blast Radius: 1.017 * Doc Risk: 48.2143%)
- `crates/swc/tests/projects/issue-655/ts.ts` -> **Severity: 43.2** (Blast Radius: 0.432 * Doc Risk: 100.0%)
- `crates/swc_sourcemap/tests/fixtures/react-native-hermes/module.js` -> **Severity: 28.22** (Blast Radius: 0.37 * Doc Risk: 76.27%)
- `crates/swc_node_bundler/tests/pass/deno-001/full/input/_util/assert.ts` -> **Severity: 18.0** (Blast Radius: 0.36 * Doc Risk: 50.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
