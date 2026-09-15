# ARCHITECTURAL_BRIEF: prettier
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/prettier/prettier.git` |
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
| Total Artifacts | 9196 |
| Analyzed Artifacts (Scanned) | 7044 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 2152 |
| Total LOC | 129378 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 76.6% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7084 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1033 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.5% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.73 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 127 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 4827 | 103043 | 68.5% |
| TYPESCRIPT | 623 | 8840 | 8.8% |
| HTML | 416 | 6249 | 5.9% |
| MARKDOWN | 412 | 0 | 5.8% |
| CSS | 294 | 8389 | 4.2% |
| YAML | 273 | 1823 | 3.9% |
| JSON | 95 | 975 | 1.3% |
| XML | 59 | 40 | 0.8% |
| PLAINTEXT | 44 | 0 | 0.6% |
| SHELL | 1 | 19 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Flat Modular Platform` (z +0.54; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 67%, Declarative / Non-Code 15%, Defensive Guards Files 5%, Interface Declarations Files 4%, State Mutators Files 3%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 6548 | 93.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 456 | 6.5% |
| Static: Minified & Vendor Opaque Mass | 40 | 0.6% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 2152*

**Composition by Extension & Reason:**
- `.snap`: 1431x Excluded (Unsupported Extension: '.snap'), 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Unsupported Format (.snap)
- `.js`: 155x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded: Neighborhood Micro-Mass Limit Exceeded, 1x Excluded (Lexical Monotony: High structural repetition detected in 5032 LOC)
- `.yml`: 94x Excluded: Neighborhood Micro-Mass Limit Exceeded, 21x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Saturation: Line 1 exceeds 500 chars)
- `.png`: 75x Excluded (Explicitly Denied Extension: '.png')
- `no_extension`: 58x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 13x Unsupported Format (.undeterminable), 1x Excluded (Unsupported Extension: '.uppercase-rocks')
- `.graphql`: 68x Excluded (Unsupported Extension: '.graphql')
- `.ts`: 51x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 2200 LOC), 1x Packed Payload Guard (Impossible Density: 3.43 hits/line)
- `.md`: 30x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 895 LOC)
- `.json`: 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.foo`: 9x Excluded (Unsupported Extension: '.foo'), 5x Unsupported Format (.foo)
- `.css`: 1x Excluded (Saturation: Line 2 exceeds 500 chars), 1x Excluded (Saturation: Line 85 exceeds 500 chars), 1x Zero-Density Threshold (LOC: 52, Signals: 0)
- `.mjs`: 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mjml`: 9x Excluded (Unsupported Extension: '.mjml')
- `.scss`: 1x Zero-Density Threshold (LOC: 168, Signals: 0), 1x Zero-Density Threshold (LOC: 117, Signals: 0), 1x Zero-Density Threshold (LOC: 97, Signals: 0)
- `.lock`: 3x Excluded (Unsupported Extension: '.lock'), 2x Unsupported Format (.lock), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 3.4 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.9 | 15.1 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 0.6 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 1.0 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 4.5 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 4.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 4.0 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 0.4 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 35.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 5.5 | 1.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 52.1 | 2.8 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 23.2 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 96.7 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 259 | 116 | 0 | `tests/format/flow/flow-repo/core_tests/boolean.js` |
| cleanup | 16 | 12 | 0 | `scripts/benchmark/compare.sh` |
| guards | 7350 | 916 | 1 | `src/language-js/parentheses/needs-parentheses.js` |
| danger | 2607 | 703 | 0 | `tests/format/flow/flow-repo/type-printer/types.js` |
| concurrency | 2306 | 427 | 0 | `tests/integration/__tests__/cache.js` |
| connectivity | 3799 | 1524 | 1 | `tests/format/flow/flow-repo/type-printer/types.js` |
| io | 1104 | 234 | 0 | `tests/format/angular/angular/real-world.component.html` |
| crypto | 4 | 3 | 0 | `tests/config/install-prettier.js` |
| ipc | 67 | 37 | 0 | `tests/format/js/module-blocks/quote-props/worker.js` |
| time | 54 | 25 | 0 | `tests/format/flow/flow-repo/date/date.js` |
| serialization | 93 | 53 | 0 | `tests/unit/whitespace-utilities.js` |
| regex | 290 | 135 | 0 | `tests/integration/__tests__/cache.js` |
| events | 697 | 158 | 0 | `tests/format/vue/event-binding/assignment.vue` |
| tests | 1332 | 210 | 0 | `tests/integration/__tests__/public-utilities.js` |
| docs | 1703 | 658 | 0 | `tests/format/flow/flow-repo/logical/logical.js` |
| debt | 1001 | 386 | 0 | `tests/format/js/function/dangling-comments.js` |
| mutation | 17853 | 2748 | 6 | `website/playground/Playground.jsx` |
| dead_code | 1898 | 809 | 1 | `tests/format/flow/flow-repo/logical/logical.js` |
| credential | 7 | 7 | 0 | `tests/format/json/json/pass1.json` |
| threat | 349 | 142 | 0 | `scripts/tools/eslint-plugin-prettier-internal-rules/test.js` |
| ml_ai | 179 | 20 | 0 | `tests/format/css/parens/parens.css` |
| ui | 2502 | 338 | 0 | `tests/format/flow/flow-repo/type-printer/types.js` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tests/format/angular/angular/real-world.component.html` (Hits: 130)
- `tests/integration/__tests__/cache.js` (Hits: 55)
- `tests/integration/__tests__/patterns-dirs.js` (Hits: 40)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **index.js** (`src/document/index.js`) — 120 inbound connections
2. **node-types.js** (`src/language-js/utilities/node-types.js`) — 55 inbound connections
3. **ast-path.js** (`src/common/ast-path.js`) — 47 inbound connections
4. **index.js** (`src/language-js/location/index.js`) — 36 inbound connections
5. **comments.js** (`src/language-js/utilities/comments.js`) — 32 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **users.yml** (`website/data/users.yml`) — 81 outbound dependencies
2. **estree.js** (`src/language-js/print/estree.js`) — 40 outbound dependencies
3. **flow.js** (`src/language-js/print/flow.js`) — 38 outbound dependencies
4. **typescript.js** (`src/language-js/print/typescript.js`) — 34 outbound dependencies
5. **production-plugins.js** (`src/main/plugins/builtin-plugins/production-plugins.js`) — 28 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `needsParentheses` **(Defensive Guards)** (@ `src/language-js/parentheses/needs-parentheses.js`) -> Impact: **768.1** | LOC: 848
  * *Intent:* /** * @import AstPath from "../../common/ast-path.js" */ /** * @param {AstPath} path * @returns {boolean} */
- `genericPrint` **(Many-Argument Workhorses)** (@ `src/language-css/printer-postcss.js`) -> Impact: **418.4** | LOC: 529
- `printCommaSeparatedValueGroup` **(Many-Argument Workhorses)** (@ `src/language-css/print/comma-separated-value-group.js`) -> Impact: **406.6** | LOC: 493
  * *Intent:* /** * @import AstPath from "../../common/ast-path.js" * @import {Doc} from "../../document/index.js" */ /** * @param {AstPath} path * @param {*} optio...
- `printFlow` **(Many-Argument Workhorses)** (@ `src/language-js/print/flow.js`) -> Impact: **322.1** | LOC: 315
- `printEstree` **(Many-Argument Workhorses)** (@ `src/language-js/print/estree.js`) -> Impact: **287.9** | LOC: 258
  * *Intent:* /** * @import AstPath from "../../common/ast-path.js" * @import {Doc} from "../../document/index.js" */ /** * @param {AstPath} path * @param {*} optio...
- `print` **(Many-Argument Workhorses)** (@ `src/language-handlebars/printer-glimmer.js`) -> Impact: **231.2** | LOC: 385
  * *Intent:* // Formatter based on @glimmerjs/syntax's built-in test formatter: // https://github.com/glimmerjs/glimmer-vm/blob/master/packages/%40glimmer/syntax/l...
- `printMdast` **(Many-Argument Workhorses)** (@ `src/language-markdown/print/mdast.js`) -> Impact: **224.8** | LOC: 336
- `printTernary` **(Many-Argument Workhorses)** (@ `src/language-js/print/ternary.js`) -> Impact: **212.8** | LOC: 276
  * *Intent:* /** * The following is the shared logic for * ternary operators, namely ConditionalExpression, * ConditionalTypeAnnotation and TSConditionalType * @pa...
- `tokenizeHtmlText` **(Many-Argument Workhorses)** (@ `src/language-markdown/parse/micromark/micromark-extension-html-text.js`) -> Impact: **204.1** | LOC: 762
  * *Intent:* /** * @this {TokenizeContext} * Context. * @type {Tokenizer} */
- `parseNestedCSS` **(Many-Argument Workhorses)** (@ `src/language-css/parser-postcss.js`) -> Impact: **196.3** | LOC: 428

*Function archetypes referenced above:*
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src/language-js/print` | 73 | 6944.86 | 20.5% | 1.5% |
| `tests/integration/__tests__` | 75 | 4716.1 | 11.23% | 0.0% |
| `tests/format/js/export-default/parentheses` | 1 | 1741.48 | 93.4% | 0.0% |
| `src/main` | 17 | 1560.88 | 44.55% | 4.45% |
| `src/language-markdown/print` | 12 | 1554.04 | 15.93% | 7.35% |
| `tests/format/yaml/spec` | 99 | 1265.98 | 0.05% | 0.0% |
| `src/language-css` | 10 | 1153.52 | 20.24% | 3.25% |
| `src/language-js/utilities` | 61 | 1137.52 | 8.71% | 5.83% |
| `website/playground` | 17 | 1111.62 | 16.44% | 6.74% |
| `src/language-js/parentheses` | 4 | 1079.78 | 26.2% | 5.98% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/document/public.d.ts` -> **99.9844%** Exposure
- `src/standalone.d.ts` -> **99.7527%** Exposure
- `src/index.d.ts` -> **99.5639%** Exposure
- `scripts/generate-flow-estree-type-definition.js` -> **98.4904%** Exposure
- `src/language-js/utilities/is-simple-call-argument.js` -> **98.1684%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `benchmarks/string-buffer-compress.js` -> **100.0%** Exposure
- `src/cli/index.js` -> **100.0%** Exposure
- `src/common/ast-path.js` -> **100.0%** Exposure
- `src/common/get-file-info.js` -> **100.0%** Exposure
- `src/config/editorconfig/editorconfig-to-prettier.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tests/format/flow/flow-repo/logical/logical.js` -> **65** Orphaned Functions | **0** Duplicates
- `src/index.d.ts` -> **44** Orphaned Functions | **2** Duplicates
- `tests/format/js/function/dangling-comments.js` -> **1** Orphaned Functions | **37** Duplicates
- `tests/format/flow/flow-repo/binding/rebinding.js` -> **33** Orphaned Functions | **4** Duplicates
- `tests/format/flow/flow-repo/dictionary/dictionary.js` -> **31** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `website/docusaurus.config.js` -> **96.6735%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `8` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1173` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/main/core.js` (JAVASCRIPT) -> Cumulative Risk: **720.73**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -1.15)
- **Magnitude:** 384.34 | **LOC:** 432 | **CtrlFlow:** 19.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.9992%)
- **Heaviest Functions:** `coreFormat` (Many-Argument Workhorses, Impact: 59.8), `formatWithCursor` (Compute Cores, Impact: 29.9), `formatRange` (Many-Argument Workhorses, Impact: 22.2)

### 2. `src/cli/index.js` (JAVASCRIPT) -> Cumulative Risk: **711.68**
- **Archetype:** `file_cluster_4` (Distance: N/A IQR)
- **Composition Archetype:** `Defensive Guards Files` (z -0.82)
- **Magnitude:** 129.38 | **LOC:** 123 | **CtrlFlow:** 29.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `main` (Defensive Guards, Impact: 42.2), `run` (Defensive Guards, Impact: 9.2)

### 3. `website/plugins/llms-txt-plugin.mjs` (JAVASCRIPT) -> Cumulative Risk: **701.34**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.23)
- **Magnitude:** 118.76 | **LOC:** 101 | **CtrlFlow:** 15.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.812%)
- **Heaviest Functions:** `getMdxFiles` (Many-Argument Workhorses, Impact: 29.1), `llmsTxtPlugin` (Compute Cores, Impact: 23.1), `loadContent` (I/O & Config Routines, Impact: 16.4)

### 4. `scripts/generate-flow-estree-type-definition.js` (JAVASCRIPT) -> Cumulative Risk: **699.15**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Compute Cores Files` (z +2.24)
- **Magnitude:** 69.86 | **LOC:** 100 | **CtrlFlow:** 15.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9999%), State Flux (99.9996%)
- **Heaviest Functions:** `toDts` (Compute Cores, Impact: 17.4), `getRelativePath` (I/O & Config Routines, Impact: 5.0)

### 5. `src/index.cjs` (JAVASCRIPT) -> Cumulative Risk: **664.29**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +1.71)
- **Magnitude:** 55.52 | **LOC:** 78 | **CtrlFlow:** 7.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.9323%)
- **Heaviest Functions:** `debugApis[name]` (Defensive Guards, Impact: 6.4), `prettier[name]` (Callbacks & Closures, Impact: 3.6), `get` (Interface Declarations, Impact: 1.6)

### 6. `src/main/ast-to-doc.js` (JAVASCRIPT) -> Cumulative Risk: **655.27**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Defensive Guards Files` (z -1.62)
- **Magnitude:** 145.86 | **LOC:** 164 | **CtrlFlow:** 30.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.997%), Concurrency (99.9665%), Cognitive Load (84.2268%)
- **Heaviest Functions:** `callPluginPrintFunction` (Many-Argument Workhorses, Impact: 36.3), `printAstToDoc` (Defensive Guards, Impact: 29.5), `mainPrintInternal` (Defensive Guards, Impact: 11.0)

### 7. `src/main/parse.js` (JAVASCRIPT) -> Cumulative Risk: **650.16**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Defensive Guards Files` (z +1.20)
- **Magnitude:** 41.32 | **LOC:** 42 | **CtrlFlow:** 9.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.9254%)
- **Heaviest Functions:** `parse` (Defensive Guards, Impact: 4.6), `handleParseError` (State Mutators, Impact: 4.1)

### 8. `scripts/clean-cspell.js` (JAVASCRIPT) -> Cumulative Risk: **649.9**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Defensive Guards Files` (z +1.26)
- **Magnitude:** 40.9 | **LOC:** 62 | **CtrlFlow:** 8.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9999%), State Flux (99.9254%)
- **Heaviest Functions:** `runSpellcheck` (Defensive Guards, Impact: 11.3), `updateConfig` (Interface Declarations, Impact: 1.6)

### 9. `src/language-html/embed.js` (JAVASCRIPT) -> Cumulative Risk: **630.83**
- **Archetype:** `file_cluster_7` (Distance: N/A IQR)
- **Composition Archetype:** `Defensive Guards Files` (z -0.77)
- **Magnitude:** 105.72 | **LOC:** 162 | **CtrlFlow:** 28.1% | **Authorship Centralization:** 71.4%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.587%), State Flux (94.2971%)
- **Heaviest Functions:** `embed` (Defensive Guards, Impact: 66.8)

### 10. `src/language-markdown/embed.js` (JAVASCRIPT) -> Cumulative Risk: **630.19**
- **Archetype:** `file_cluster_4` (Distance: N/A IQR)
- **Composition Archetype:** `Defensive Guards Files` (z -0.86)
- **Magnitude:** 79.86 | **LOC:** 106 | **CtrlFlow:** 26.5% | **Authorship Centralization:** 80.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.8982%), State Flux (99.2068%)
- **Heaviest Functions:** `embed` (Defensive Guards, Impact: 36.9), `validateImportExport` (Defensive Guards, Impact: 7.8), `__onHtmlBindingRoot` (Interface Declarations, Impact: 3.5)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `tests/format/js/export-default/parentheses/format.test.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1741.48 | **LOC:** 86 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (93.397%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 56`, `args: 5`, `func_start: 2`
* *Risk/State:* `state_mutation: 6`, `planned_debt: 1`
* *Architecture:* `api: 45`, `concurrency: 3`
* *Defense:* `safety: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.123
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/language-js/parentheses/needs-parentheses.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 837.12 | **LOC:** 1000 | **CtrlFlow:** 53.0% | **Authorship Centralization:** 85.7%
- **Risk Profile:** Cognitive Load (46.6534%), Tech Debt (8.7172%)
**Top Internal Functions/Classes:**
  * `needsParentheses` **(Defensive Guards)** (Impact: 768.1)
    * *Intent:* /** * @import AstPath from "../../common/ast-path.js" */ /** * @param {AstPath} path * @returns {boo...
  * `isFollowedByRightBracket` **(Defensive Guards)** (Impact: 24.2)
    * *Intent:* /** * @param {AstPath} path * @returns {boolean} */
  * `isPathInForStatementInitializer` **(Defensive Guards)** (Impact: 7.7)
    * *Intent:* /** * @param {AstPath} path * @returns {boolean} */
  * `endsWithRightBracket` **(Interface Declarations)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 438`, `structural_boundaries: 166`, `args: 22`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 6`, `planned_debt: 1`
* *Architecture:* `api: 1`, `import: 13`
* *Defense:* `safety: 249`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.314
  * `Choke Point (Betweenness):` 1.6e-05 | `Ripple Effect (Closeness):` 0.00153
  * `Imports (Out-Degree: 12):` ast-path.js, comments.js, create-type-check-function.js, function-parameters.js, get-precedence.js, is-bitwise-operator.js, is-nullish-coalescing.js, is-object-property.js...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `tests/integration/__tests__/cache.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 729.3 | **LOC:** 708 | **CtrlFlow:** 0.8% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (49.9932%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `clean` **(Tests & Verification)** (Impact: 38.8)
  * `runCliWithoutGitignore` **(Many-Argument Workhorses)** (Impact: 5.2)
  * `resolveDir` **(Interface Declarations)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 86 instances
* *Amplified Cascading Flux:* 7 instances
* *Concurrency (weighted view):* 542
* *State Mutation (weighted view):* 129
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 123`, `args: 40`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 115`, `unreferenced_by_name: 1`
* *Architecture:* `io: 55`, `concurrency: 112`, `import: 3`
* *Defense:* `test: 83`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.123
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` promises, node:path, node:url
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/config/install-prettier.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 710.56 | **LOC:** 139 | **CtrlFlow:** 15.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (14.6026%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 25`, `args: 10`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 6`
* *Architecture:* `io: 16`, `api: 2`, `import: 9`
* *Defense:* `safety: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.176
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000141
  * `Imports (Out-Degree: 0):` node:child_process, node:crypto, node:fs, node:os, node:path, node:perf_hooks, outdent, picocolors...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tests/format/flow/flow-repo/type_param_variance2/libs/Promise.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 663.6 | **LOC:** 48 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 10`, `args: 8`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 7`
* *Architecture:* `concurrency: 18`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.123
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/language-js/print/jsx.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 647.86 | **LOC:** 856 | **CtrlFlow:** 31.0% | **Authorship Centralization:** 94.4%
- **Risk Profile:** Cognitive Load (35.6403%), Tech Debt (10.3581%)
**Top Internal Functions/Classes:**
  * `printJsxElementInternal` **(Many-Argument Workhorses)** (Impact: 161.7)
    * *Intent:* // This is both to break children before attributes, // and to ensure that when children break, thei...
  * `printJsxChildren` **(Many-Argument Workhorses)** (Impact: 65.1)
    * *Intent:* // JSX Children are strange, mostly for two reasons: // 1. JSX reads newlines into string values, in...
  * `printJsx` **(Compute Cores)** (Impact: 40.1)
  * `printJsxExpressionContainer` **(Defensive Guards)** (Impact: 35.6)
  * `printJsxOpeningElement` **(Many-Argument Workhorses)** (Impact: 35.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 36 instances
* *State Mutation (weighted view):* 111
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 204`, `structural_boundaries: 91`, `args: 36`, `func_start: 23`
* *Risk/State:* `state_mutation: 39`, `dead_code: 1`, `fragile_debt: 1`
* *Architecture:* `api: 2`, `import: 12`
* *Defense:* `safety: 97`, `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.123
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` ast-path.js, index.js, print.js, get-preferred-quote.js, unexpected-node-error.js, needs-parentheses.js, estree.js, comments.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/format/typescript/_errors_/modifiers/format.test.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 624.03 | **LOC:** 157 | **CtrlFlow:** 8.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (8.4928%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 38`, `args: 20`, `func_start: 1`, `class_start: 4`
* *Risk/State:* None
* *Architecture:* `api: 4`, `concurrency: 2`, `import: 1`
* *Defense:* `safety: 18`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.123
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` outdent
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/integration/__tests__/stdin-filepath.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 609.88 | **LOC:** 150 | **CtrlFlow:** 8.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.4471%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 29
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 13`, `args: 17`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 11`
* *Architecture:* `import: 2`
* *Defense:* `test: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.123
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ci-info, outdent
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/language-handlebars/printer-glimmer.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 540.76 | **LOC:** 858 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 80.0%
- **Risk Profile:** Cognitive Load (58.5339%), Tech Debt (9.0786%)
**Top Internal Functions/Classes:**
  * `print` **(Many-Argument Workhorses)** (Impact: 231.2)
    * *Intent:* // Formatter based on @glimmerjs/syntax's built-in test formatter: // https://github.com/glimmerjs/g...
  * `isElseIfBlock` **(Defensive Guards)** (Impact: 14.5)
  * `isPathExpressionPartNeedBrackets` **(Defensive Guards)** (Impact: 12.8)
  * `printParams` **(Defensive Guards)** (Impact: 9.6)
  * `printInverse` **(Many-Argument Workhorses)** (Impact: 8.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 38 instances
* *State Mutation (weighted view):* 115
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 174`, `structural_boundaries: 120`, `args: 51`, `func_start: 36`
* *Risk/State:* `state_mutation: 39`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `api: 1`, `import: 10`
* *Defense:* `safety: 79`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.24
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.00058
  * `Imports (Out-Degree: 5):` index.js, get-preferred-quote.js, html-whitespace.js, is-non-empty-array.js, unexpected-node-error.js, embed.js, get-visitor-keys.js, loc.js...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/language-css/print/comma-separated-value-group.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 523.92 | **LOC:** 568 | **CtrlFlow:** 48.7% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (63.0954%), Tech Debt (13.8131%)
**Top Internal Functions/Classes:**
  * `printCommaSeparatedValueGroup` **(Many-Argument Workhorses)** (Impact: 406.6)
    * *Intent:* /** * @import AstPath from "../../common/ast-path.js" * @import {Doc} from "../../document/index.js"...
  * `isPossibleFontSize` **(Defensive Guards)** (Impact: 15.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 31 instances
* *State Mutation (weighted view):* 93
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 200`, `structural_boundaries: 59`, `args: 5`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 31`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `safety: 84`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.152
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000524
  * `Imports (Out-Degree: 2):` ast-path.js, index.js, loc.js, index.js
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tests/integration/__tests__/infer-plugins-ext-dir.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 523.01 | **LOC:** 209 | **CtrlFlow:** 5.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.6999%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 34
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 15`, `args: 11`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 14`
* *Architecture:* `api: 5`, `import: 1`
* *Defense:* `test: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.123
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` outdent
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/language-js/comments/handle-comments.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 500.6 | **LOC:** 1088 | **CtrlFlow:** 29.1% | **Authorship Centralization:** 91.1%
- **Risk Profile:** Cognitive Load (15.9698%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `handleLastFunctionParameterComments` **(Defensive Guards)** (Impact: 67.5)
  * `handleClassComments` **(Defensive Guards)** (Impact: 32.4)
  * `handleMethodNameComments` **(Defensive Guards)** (Impact: 29.7)
  * `handleCommentInEmptyParens` **(Defensive Guards)** (Impact: 23.2)
  * `handleModuleSpecifiersComments` **(Defensive Guards)** (Impact: 21.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 30
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 255`, `structural_boundaries: 118`, `args: 39`, `func_start: 36`
* *Risk/State:* `state_mutation: 10`, `dead_code: 1`
* *Architecture:* `api: 1`, `import: 22`
* *Defense:* `safety: 149`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.181
  * `Choke Point (Betweenness):` 6e-06 | `Ripple Effect (Closeness):` 0.0006
  * `Imports (Out-Degree: 22):` utilities.js, get-next-non-space-non-comment-character-index.js, get-next-non-space-non-comment-character.js, has-newline-in-range.js, has-newline.js, is-non-empty-array.js, index.js, estree.js...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/language-html/utilities/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 468.78 | **LOC:** 655 | **CtrlFlow:** 36.7% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (19.0138%), Tech Debt (9.3985%)
**Top Internal Functions/Classes:**
  * `isLeadingSpaceSensitiveNode` **(Defensive Guards)** (Impact: 46.1)
  * `isTrailingSpaceSensitiveNode` **(Defensive Guards)** (Impact: 36.7)
  * `getNodeCssStyleDisplay` **(Defensive Guards)** (Impact: 34.9)
  * `shouldPreserveContent` **(Defensive Guards)** (Impact: 24.4)
  * `inferParserByTypeAttribute` **(Compute Cores)** (Impact: 24.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 196`, `structural_boundaries: 110`, `args: 56`, `func_start: 52`
* *Risk/State:* `state_mutation: 4`, `planned_debt: 1`
* *Architecture:* `api: 1`, `import: 6`
* *Defense:* `safety: 89`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.123
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` ast-path.js, index.js, index.js, html-whitespace.js, infer-parser.js, constants.evaluate.js, is-unknown-namespace.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/language-css/printer-postcss.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 442.02 | **LOC:** 603 | **CtrlFlow:** 36.9% | **Authorship Centralization:** 60.0%
- **Risk Profile:** Cognitive Load (20.7058%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `genericPrint` **(Many-Argument Workhorses)** (Impact: 418.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 196`, `structural_boundaries: 76`, `args: 6`, `func_start: 1`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `api: 1`, `import: 14`
* *Defense:* `safety: 51`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.24
  * `Choke Point (Betweenness):` 4e-06 | `Ripple Effect (Closeness):` 0.00058
  * `Imports (Out-Degree: 7):` index.js, is-non-empty-array.js, print-string.js, unexpected-node-error.js, embed.js, get-visitor-keys.js, loc.js, index.js...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/language-markdown/print/mdast.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 433.62 | **LOC:** 560 | **CtrlFlow:** 31.1% | **Authorship Centralization:** 57.1%
- **Risk Profile:** Cognitive Load (25.3143%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `printMdast` **(Many-Argument Workhorses)** (Impact: 224.8)
  * `processor` **(Compute Cores)** (Impact: 30.7)
  * `printRoot` **(Many-Argument Workhorses)** (Impact: 29.1)
  * `printTitle` **(Defensive Guards)** (Impact: 28.3)
  * `prevOrNextWord` **(Defensive Guards)** (Impact: 14.7)
    * *Intent:* /** * @import AstPath from "../../common/ast-path.js"; * @import {Doc} from "../../document/index.js...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 17 instances
* *State Mutation (weighted view):* 52
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 151`, `structural_boundaries: 103`, `args: 21`, `func_start: 14`
* *Risk/State:* `state_mutation: 18`
* *Architecture:* `api: 2`, `import: 17`
* *Defense:* `safety: 61`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.228
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.000141
  * `Imports (Out-Degree: 12):` ast-path.js, index.js, get-max-continuous-count.js, get-min-not-present-continuous-count.js, get-preferred-quote.js, unexpected-node-error.js, loc.js, utilities.js...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/language-markdown/parse/micromark/micromark-extension-html-text.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 432.08 | **LOC:** 813 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (10.6131%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `tokenizeHtmlText` **(Many-Argument Workhorses)** (Impact: 204.1)
    * *Intent:* /** * @this {TokenizeContext} * Context. * @type {Tokenizer} */
  * `tagOpenAttributeValueBefore` **(Defensive Guards)** (Impact: 15.6)
    * *Intent:* /** * Before unquoted, double quoted, or single quoted attribute value, allowing * whitespace. * * `...
  * `tagOpenAttributeValueUnquoted` **(Defensive Guards)** (Impact: 15.3)
    * *Intent:* /** * In unquoted attribute value. * * ```markdown * > | a <b c=d> e * ^ * ``` * * @type {State} */...
  * `tagOpenBetween` **(Defensive Guards)** (Impact: 11.1)
    * *Intent:* /** * In opening tag, after tag name. * * ```markdown * > | a <b> c * ^ * ``` * * @type {State} */...
  * `tagOpen` **(Defensive Guards)** (Impact: 9.3)
    * *Intent:* /** * After `<x`, in opening tag name. * * ```markdown * > | a <b> c * ^ * ``` * * @type {State} */...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 39
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 90`, `args: 32`, `func_start: 32`
* *Risk/State:* `state_mutation: 13`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `safety: 58`, `doc: 35`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000189
  * `Imports (Out-Degree: 0):` micromark-factory-space, micromark-util-character, micromark-util-symbol, micromark-util-types
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/document/printer/printer.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 427.0 | **LOC:** 578 | **CtrlFlow:** 25.9% | **Authorship Centralization:** 92.3%
- **Risk Profile:** Cognitive Load (41.3842%), Tech Debt (17.0037%)
**Top Internal Functions/Classes:**
  * `printDocToString` **(Many-Argument Workhorses)** (Impact: 141.1)
    * *Intent:* */
  * `fits` **(Many-Argument Workhorses)** (Impact: 106.4)
    * *Intent:* /** * @param {Command} next * @param {Command[]} restCommands * @param {number} remainingWidth * @pa...
  * `printGroup` **(I/O & Config Routines)** (Impact: 13.3)
    * *Intent:* /** @type {Command} */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 52 instances
* *State Mutation (weighted view):* 156
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 106`, `structural_boundaries: 65`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 52`, `dead_code: 3`, `fragile_debt: 2`
* *Architecture:* `api: 2`, `import: 8`
* *Defense:* `safety: 20`, `doc: 18`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.278
  * `Choke Point (Betweenness):` 2.2e-05 | `Ripple Effect (Closeness):` 0.010394
  * `Imports (Out-Degree: 5):` end-of-line.js, get-string-width.js, index.js, index.js, invalid-doc-error.js, indent.js, print-result.js, trim-indentation.js
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/cli/format.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 420.2 | **LOC:** 507 | **CtrlFlow:** 27.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (89.2453%), Tech Debt (10.0529%)
**Top Internal Functions/Classes:**
  * `formatFiles` **(Compute Cores)** (Impact: 100.7)
  * `format` **(Many-Argument Workhorses)** (Impact: 45.5)
  * `handleError` **(Many-Argument Workhorses)** (Impact: 44.0)
  * `stringify` **(Defensive Guards)** (Impact: 22.3)
  * `formatStdin` **(Compute Cores)** (Impact: 12.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Race Conditions:* 10 instances
* *Amplified Cascading Flux:* 25 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 83
* *State Mutation (weighted view):* 79
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 111`, `structural_boundaries: 76`, `args: 10`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 3`, `state_mutation: 29`, `planned_debt: 1`
* *Architecture:* `io: 5`, `api: 1`, `concurrency: 33`, `import: 12`
* *Defense:* `safety: 36`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.123
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` index.js, expand-patterns.js, find-cache-file.js, format-results-cache.js, mockable.js, get-options-for-file.js, prettier-internal.js, utilities.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/language-markdown/print/preprocess.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 415.12 | **LOC:** 603 | **CtrlFlow:** 26.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (39.8268%), Tech Debt (53.6879%)
**Top Internal Functions/Classes:**
  * `splitTextIntoSentences` **(Defensive Guards)** (Impact: 39.0)
  * `markAlignedList` **(Defensive Guards)** (Impact: 35.2)
  * `markAlignedListLegacy` **(Defensive Guards)** (Impact: 27.9)
  * `getBracketContent` **(Defensive Guards)** (Impact: 19.6)
  * `preprocess` **(Defensive Guards)** (Impact: 18.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 40 instances
* *State Mutation (weighted view):* 120
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 109`, `structural_boundaries: 90`, `args: 37`, `func_start: 21`
* *Risk/State:* `state_mutation: 40`, `dead_code: 2`, `duplicate_logic: 4`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `safety: 63`, `doc: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.228
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000141
  * `Imports (Out-Degree: 1):` html-whitespace.js, utilities.js
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/main/core.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 384.34 | **LOC:** 432 | **CtrlFlow:** 19.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (99.8588%), Tech Debt (10.6834%)
**Top Internal Functions/Classes:**
  * `coreFormat` **(Many-Argument Workhorses)** (Impact: 59.8)
  * `formatWithCursor` **(Compute Cores)** (Impact: 29.9)
  * `formatRange` **(Many-Argument Workhorses)** (Impact: 22.2)
  * `ensureIndexInText` **(Defensive Guards)** (Impact: 10.6)
  * `normalizeInputAndOptions` **(Many-Argument Workhorses)** (Impact: 9.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 13 instances
* *Amplified Cascading Flux:* 36 instances
* *Concurrency (weighted view):* 96
* *State Mutation (weighted view):* 117
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 66`, `args: 14`, `func_start: 14`
* *Risk/State:* `state_mutation: 45`, `planned_debt: 1`
* *Architecture:* `api: 2`, `concurrency: 31`, `import: 12`
* *Defense:* `safety: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.23
  * `Choke Point (Betweenness):` 5e-06 | `Ripple Effect (Closeness):` 0.00092
  * `Imports (Out-Degree: 7):` end-of-line.js, constants.js, index.js, get-alignment-size.js, ast-to-doc.js, get-cursor-node.js, massage-ast.js, normalize-format-options.js...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/language-css/parser-postcss.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 366.3 | **LOC:** 453 | **CtrlFlow:** 28.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (73.857%), Tech Debt (11.9203%)
**Top Internal Functions/Classes:**
  * `parseNestedCSS` **(Many-Argument Workhorses)** (Impact: 196.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 52 instances
* *State Mutation (weighted view):* 159
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 101`, `structural_boundaries: 62`, `args: 6`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 55`, `dead_code: 1`, `planned_debt: 2`
* *Architecture:* `api: 4`, `import: 15`
* *Defense:* `safety: 45`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.24
  * `Choke Point (Betweenness):` 6e-06 | `Ripple Effect (Closeness):` 0.00058
  * `Imports (Out-Degree: 10):` parser-create-error.js, index.js, is-object.js, replace-non-line-breaks-with-space.js, loc.js, parse-media-query.js, parse-selector.js, parse-value.js...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/language-js/print/assignment.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 343.14 | **LOC:** 469 | **CtrlFlow:** 31.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (22.8909%), Tech Debt (11.4275%)
**Top Internal Functions/Classes:**
  * `chooseLayout` **(Many-Argument Workhorses)** (Impact: 77.9)
  * `shouldBreakAfterOperator` **(Many-Argument Workhorses)** (Impact: 61.5)
  * `printAssignment` **(Many-Argument Workhorses)** (Impact: 31.8)
    * *Intent:* /** * @import AstPath from "../../common/ast-path.js" */
  * `isPoorlyBreakableMemberOrCallChain` **(Defensive Guards)** (Impact: 28.9)
    * *Intent:* /** * A chain with no calls at all or whose calls are all without arguments or with lone short argum...
  * `isCallExpressionWithComplexTypeArguments` **(Defensive Guards)** (Impact: 18.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 21
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 121`, `structural_boundaries: 91`, `args: 25`, `func_start: 19`
* *Risk/State:* `state_mutation: 7`, `dead_code: 1`, `planned_debt: 2`
* *Architecture:* `api: 2`, `import: 11`
* *Defense:* `safety: 42`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.123
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` ast-path.js, index.js, get-string-width.js, is-non-empty-array.js, call-arguments.js, has-leading-own-line-comment.js, is-lone-short-argument.js, is-object-property.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `website/static/worker.mjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 337.66 | **LOC:** 337 | **CtrlFlow:** 15.9% | **Authorship Centralization:** 60.0%
- **Risk Profile:** Cognitive Load (84.4553%), Tech Debt (16.4117%)
**Top Internal Functions/Classes:**
  * `handleFormatMessage` **(Compute Cores)** (Impact: 29.0)
    * *Intent:* /** */
  * `formatCode` **(Defensive Guards)** (Impact: 9.4)
    * *Intent:* /** */
  * `createPlugin` **(Callbacks & Closures)** (Impact: 8.2)
    * *Intent:* // Similar to `createParsersAndPrinters` in `src/plugins/builtin-plugins-proxy.js`
  * `stringifyError` **(Defensive Guards)** (Impact: 8.1)
  * `serializeAst` **(Defensive Guards)** (Impact: 6.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 25 instances
* *Amplified Cascading Flux:* 23 instances
* *Concurrency (weighted view):* 163
* *State Mutation (weighted view):* 73
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 66`, `args: 19`, `func_start: 15`
* *Risk/State:* `state_mutation: 27`, `fragile_debt: 1`
* *Architecture:* `api: 2`, `concurrency: 38`, `import: 4`
* *Defense:* `safety: 26`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.207
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000354
  * `Imports (Out-Degree: 2):` playground-settings.js, prettier-plugin-doc-explorer.mjs
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/language-js/print/flow.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 336.88 | **LOC:** 378 | **CtrlFlow:** 40.1% | **Authorship Centralization:** 87.5%
- **Risk Profile:** Cognitive Load (21.5512%), Tech Debt (12.0917%)
**Top Internal Functions/Classes:**
  * `printFlow` **(Many-Argument Workhorses)** (Impact: 322.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 136`, `structural_boundaries: 108`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 2`, `planned_debt: 2`
* *Architecture:* `api: 2`, `import: 38`
* *Defense:* `safety: 11`, `doc: 1`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.123
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 27):` assert, index.js, print-number.js, print-string.js, get-raw.js, is-flow-keyword-type.js, is-method.js, array-type.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/language-html/print-preprocess.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 332.6 | **LOC:** 411 | **CtrlFlow:** 24.0% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (55.363%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `extractWhitespaces` **(Many-Argument Workhorses)** (Impact: 36.6)
    * *Intent:* /** * - add `hasLeadingSpaces` field * - add `hasTrailingSpaces` field * - add `hasDanglingSpaces` f...
  * `mergeSimpleElementIntoText` **(Defensive Guards)** (Impact: 27.7)
  * `isSimpleElement` **(Defensive Guards)** (Impact: 27.6)
  * `extractInterpolation` **(Defensive Guards)** (Impact: 20.4)
  * `mergeNodeIntoText` **(Defensive Guards)** (Impact: 17.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 32 instances
* *State Mutation (weighted view):* 108
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 42`, `args: 26`, `func_start: 14`
* *Risk/State:* `state_mutation: 44`
* *Architecture:* `api: 3`, `import: 3`
* *Defense:* `safety: 39`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.123
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` html-whitespace.js, index.js, angular-html-parser
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `tests/format/js/export-default/parentheses/format.test.js` -> **fisker Cheung** (100.0% isolated ownership) | Magnitude: 1741.48
- `src/language-js/parentheses/needs-parentheses.js` -> **fisker Cheung** (85.7% isolated ownership) | Magnitude: 837.12
- `tests/config/install-prettier.js` -> **fisker Cheung** (100.0% isolated ownership) | Magnitude: 710.56
- `tests/format/flow/flow-repo/type_param_variance2/libs/Promise.js` -> **fisker Cheung** (100.0% isolated ownership) | Magnitude: 663.6
- `src/language-js/print/jsx.js` -> **fisker Cheung** (94.4% isolated ownership) | Magnitude: 647.86

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/document/printer/printer.js` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 99.9997%)
- `src/index.js` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 43.1409%)
- `scripts/utilities/generate-schema.js` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 95.3635%)
- `src/document/utilities/assert-doc.js` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 94.0548%)
- `src/document/utilities/invalid-doc-error.js` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 68.9974%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/document/printer/printer.js` -> **Severity: 0.872** (Embedded: 0.0104 * Error Risk: 83.9174%)
- `src/document/builders/align.js` -> **Severity: 0.649** (Embedded: 0.0083 * Error Risk: 78.0498%)
- `src/utilities/get-string-width.js` -> **Severity: 0.632** (Embedded: 0.0081 * Error Risk: 78.0498%)
- `src/document/builders/join.js` -> **Severity: 0.621** (Embedded: 0.0083 * Error Risk: 74.6494%)
- `src/common/ast-path.js` -> **Severity: 0.592** (Embedded: 0.0089 * Error Risk: 66.3468%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `tests/config/get-prettier.js` -> **Severity: 289.6** (Blast Radius: 2.896 * Doc Risk: 100.0%)
- `src/document/debug.js` -> **Severity: 141.45** (Blast Radius: 1.886 * Doc Risk: 75.0%)
- `src/language-js/location/is-index.js` -> **Severity: 141.3** (Blast Radius: 1.413 * Doc Risk: 100.0%)
- `tests/config/browser-prettier/server.js` -> **Severity: 134.8** (Blast Radius: 1.348 * Doc Risk: 100.0%)
- `tests/config/browser-prettier/browser-prettier.js` -> **Severity: 130.1** (Blast Radius: 2.602 * Doc Risk: 50.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
