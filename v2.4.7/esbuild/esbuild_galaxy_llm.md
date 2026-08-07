# ARCHITECTURAL_BRIEF: esbuild
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_typescript/esbuild` |
| **Timestamp** | `2026-08-07T04:15:06.192706+00:00` |
| **Scan Duration** | `2.94s` |
| **Git Branch** | `main` |
| **Git Commit** | `6a794dff68e6a43539f6da671e3080efdf11ca70` |
| **Git Remote** | `https://github.com/evanw/esbuild.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 136 malicious artifacts.

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
| Total Artifacts | 348 |
| Analyzed Artifacts (Scanned) | 194 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 154 |
| Total LOC | 59835 |
| Volatility Index | 0.005 |
| % Scanned of codebase = | 55.7% |
| Dominant Lang | GO |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3997 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3105 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 2.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.6417 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 10 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| GO | 102 | 30844 | 52.6% |
| PLAINTEXT | 25 | 0 | 12.9% |
| JAVASCRIPT | 24 | 22452 | 12.4% |
| MARKDOWN | 13 | 0 | 6.7% |
| JSON | 9 | 3138 | 4.6% |
| TYPESCRIPT | 8 | 1032 | 4.1% |
| XML | 5 | 0 | 2.6% |
| HTML | 5 | 1475 | 2.6% |
| MAKEFILE | 1 | 804 | 0.5% |
| SHELL | 1 | 18 | 0.5% |
| CSS | 1 | 72 | 0.5% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.213`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 120 | 61.9% |
| file_cluster_13 | 18 | 9.3% |
| file_cluster_4 | 13 | 6.7% |
| file_cluster_17 | 3 | 1.5% |
| file_cluster_15 | 1 | 0.5% |
| file_cluster_11 | 1 | 0.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 38 | 19.6% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 154*

**Composition by Extension & Reason:**
- `.go`: 42x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 423 LOC), 1x Excluded (Machine-Generated Source Code Signature: 938 LOC)
- `.json`: 34x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 5304 LOC), 1x Excluded (Static Asset Blob without Intent: 2344 LOC)
- `.md`: 35x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ts`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 5x Excluded (Explicitly Denied Extension: '.png')
- `.yml`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mod`: 1x Unsupported Format (.mod)
- `.sum`: 1x Excluded (Unsupported Extension: '.sum')
- `.version`: 1x Excluded (Unsupported Extension: '.version')
- `.js`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.lock`: 1x Excluded (Unsupported Extension: '.lock')
- `.conf`: 1x Excluded (Unsupported Extension: '.conf')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 36.9 | 37.9 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 68.6 | 83.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 45.5 | 29.8 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 32.1 | 2.4 | 80.0 |
| API Exposure | 0.0 | 17.8 | 3.0 | 1.4 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 10.7 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 69.4 | 100.0 | 100.0 |
| Commented Logic Exposure | 0.0 | 22.8 | 1.4 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 90.7 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 10.3 | 0.9 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 65.4 | 4.8 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 29.4 | 17.9 | 11.9 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `scripts/js-api-tests.js` (Hits: 592)
- `scripts/plugin-tests.js` (Hits: 344)
- `scripts/end-to-end-tests.js` (Hits: 203)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **strings.go** (`internal/helpers/strings.go`) — 58 inbound connections
2. **logger.go** (`internal/logger/logger.go`) — 43 inbound connections
3. **fs.go** (`internal/fs/fs.go`) — 28 inbound connections
4. **css_ast.go** (`internal/css_ast/css_ast.go`) — 24 inbound connections
5. **ast.go** (`internal/ast/ast.go`) — 23 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **css_decl_table.go** (`internal/css_ast/css_decl_table.go`) — 331 outbound dependencies
2. **tables.go** (`internal/js_lexer/tables.go`) — 253 outbound dependencies
3. **css_decls_color.go** (`internal/css_parser/css_decls_color.go`) — 179 outbound dependencies
4. **css_parser.go** (`internal/css_parser/css_parser.go`) — 132 outbound dependencies
5. **end-to-end-tests.js** (`scripts/end-to-end-tests.js`) — 126 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `printBinding` (@ `internal/js_printer/js_printer.go`) -> Impact: **1224.1** | LOC: 1653
- `parseListOfDeclarations` (@ `internal/css_parser/css_parser.go`) -> Impact: **865.5** | LOC: 1241
- `CloneTokensWithImportRecords` (@ `internal/css_ast/css_ast.go`) -> Impact: **639.4** | LOC: 1080
- `Next` (@ `internal/js_lexer/js_lexer.go`) -> Impact: **554.8** | LOC: 632
- `lateConstantFoldUnaryOrBinaryOrIfExpr` (@ `internal/js_printer/js_printer.go`) -> Impact: **538.6** | LOC: 631
- `simplifyUnusedStringAdditionChain` (@ `internal/js_ast/js_ast_helpers.go`) -> Impact: **462.3** | LOC: 686
- `printExprCommentsAfterCloseTokenAtLoc` (@ `internal/js_printer/js_printer.go`) -> Impact: **459.0** | LOC: 509
- `mangleLocalCSS` (@ `internal/linker/linker.go`) -> Impact: **435.6** | LOC: 677
- `mergeCompoundSelectors` (@ `internal/css_parser/css_parser_selector.go`) -> Impact: **419.1** | LOC: 830
- `validatePathTemplate` (@ `pkg/api/api_impl.go`) -> Impact: **373.7** | LOC: 794

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `scripts` | 28 | 19875.29 | 51.72% | 67.98% |
| `internal/css_parser` | 20 | 9906.66 | 49.65% | 35.42% |
| `internal/linker` | 2 | 5234.34 | 54.93% | 11.02% |
| `internal/js_parser` | 6 | 4532.64 | 44.02% | 27.71% |
| `__monolith__` | 13 | 3909.16 | 10.23% | 0.94% |
| `internal/js_printer` | 1 | 3882.96 | 47.97% | 13.24% |
| `internal/js_lexer` | 2 | 3143.4 | 28.61% | 8.19% |
| `pkg/api` | 6 | 2959.62 | 23.71% | 46.86% |
| `internal/resolver` | 6 | 2938.7 | 31.81% | 24.07% |
| `internal/js_ast` | 3 | 2906.1 | 29.42% | 59.24% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `internal/css_ast/css_ast.go` -> **100.0%** Exposure
- `internal/fs/error_other.go` -> **100.0%** Exposure
- `internal/fs/iswin_other.go` -> **100.0%** Exposure
- `internal/fs/iswin_wasm.go` -> **100.0%** Exposure
- `internal/fs/iswin_windows.go` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `dl.sh` -> **100.0%** Exposure
- `internal/bundler/bundler.go` -> **100.0%** Exposure
- `internal/config/config.go` -> **100.0%** Exposure
- `internal/css_ast/css_ast.go` -> **100.0%** Exposure
- `internal/css_lexer/css_lexer.go` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `scripts/decorator-tests.js` -> **0** Orphaned Functions | **918** Duplicates
- `scripts/end-to-end-tests.js` -> **0** Orphaned Functions | **521** Duplicates
- `scripts/plugin-tests.js` -> **88** Orphaned Functions | **106** Duplicates
- `scripts/js-api-tests.js` -> **84** Orphaned Functions | **33** Duplicates
- `internal/css_ast/css_ast.go` -> **16** Orphaned Functions | **75** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`internal/bundler/bundler.go`** -> AI Confidence: **99.48%**
2. **`internal/css_lexer/css_lexer.go`** -> AI Confidence: **99.48%**
3. **`internal/css_parser/css_decls_animation.go`** -> AI Confidence: **99.48%**
4. **`internal/css_parser/css_decls_color.go`** -> AI Confidence: **99.48%**
5. **`internal/css_parser/css_decls_gradient.go`** -> AI Confidence: **99.48%**
6. **`internal/css_parser/css_decls_list_style.go`** -> AI Confidence: **99.48%**
7. **`internal/css_parser/css_decls_transform.go`** -> AI Confidence: **99.48%**
8. **`internal/css_parser/css_parser.go`** -> AI Confidence: **99.48%**
9. **`internal/css_parser/css_parser_selector.go`** -> AI Confidence: **99.48%**
10. **`internal/css_printer/css_printer.go`** -> AI Confidence: **99.48%**
11. **`internal/js_lexer/js_lexer.go`** -> AI Confidence: **99.48%**
12. **`internal/js_parser/js_parser_lower.go`** -> AI Confidence: **99.48%**
13. **`internal/js_parser/js_parser_lower_class.go`** -> AI Confidence: **99.48%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `2177` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `internal/css_ast/css_ast.go` (GO) -> Cumulative Risk: **678.31**
- **Archetype:** `file_cluster_8` (Distance: 13.662 IQR)
- **Magnitude:** 2298.24 | **LOC:** 1581 | **CtrlFlow:** 52.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `CloneTokensWithImportRecords` (Impact: 639.4), `String` (Impact: 30.4), `ContainsNestingCombinator` (Impact: 23.2)

### 2. `scripts/end-to-end-tests.js` (JAVASCRIPT) -> Cumulative Risk: **661.19**
- **Archetype:** `file_cluster_4` (Distance: 15.337 IQR)
- **Magnitude:** 7898.96 | **LOC:** 9848 | **CtrlFlow:** 36.1% | **Authorship Centralization:** 83.3%
- **Primary Risk Drivers:** Tech Debt (100.0%), Concurrency (100.0%), Spec Match (100.0%), State Flux (99.9377%)
- **Heaviest Functions:** `test` (Impact: 157.8), `test` (Impact: 37.9), `async` (Impact: 29.9)

### 3. `internal/ast/ast.go` (GO) -> Cumulative Risk: **627.54**
- **Archetype:** `file_cluster_15` (Distance: 14.116 IQR)
- **Magnitude:** 396.58 | **LOC:** 828 | **CtrlFlow:** 41.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9993%), Tech Debt (97.7458%)
- **Heaviest Functions:** `StringForMetafile` (Impact: 25.7), `Scan` (Impact: 18.1), `ShuffleByCharFreq` (Impact: 15.8)

### 4. `scripts/destructuring-fuzzer.js` (JAVASCRIPT) -> Cumulative Risk: **616.82**
- **Archetype:** `file_cluster_4` (Distance: 13.257 IQR)
- **Magnitude:** 626.52 | **LOC:** 403 | **CtrlFlow:** 29.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.975%), Tech Debt (99.2385%)
- **Heaviest Functions:** `generateTestCase` (Impact: 66.4), `object` (Impact: 29.8), `verify` (Impact: 28.9)

### 5. `internal/css_parser/css_reduce_calc.go` (GO) -> Cumulative Risk: **596.75**
- **Archetype:** `file_cluster_8` (Distance: 13.694 IQR)
- **Magnitude:** 928.32 | **LOC:** 606 | **CtrlFlow:** 71.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.6595%), Tech Debt (98.1014%)
- **Heaviest Functions:** `tryToParseCalcTerm` (Impact: 150.8), `partiallySimplify` (Impact: 59.9), `convertToToken` (Impact: 48.2)

### 6. `internal/bundler/bundler.go` (GO) -> Cumulative Risk: **595.98**
- **Archetype:** `file_cluster_8` (Distance: 14.441 IQR)
- **Magnitude:** 1022.0 | **LOC:** 3532 | **CtrlFlow:** 81.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.5944%), Concurrency (97.9718%)
- **Heaviest Functions:** `preprocessInjectedFiles` (Impact: 99.9), `ScanBundle` (Impact: 85.3), `sanitizeFilePathForVirtualModulePath` (Impact: 28.1)

### 7. `internal/helpers/joiner.go` (GO) -> Cumulative Risk: **593.39**
- **Archetype:** `file_cluster_8` (Distance: 12.491 IQR)
- **Magnitude:** 99.7 | **LOC:** 87 | **CtrlFlow:** 53.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.0462%), Safety Score (92.8242%)
- **Heaviest Functions:** `Done` (Impact: 18.6), `Contains` (Impact: 10.5), `EnsureNewlineAtEnd` (Impact: 7.0)

### 8. `scripts/decorator-tests.js` (JAVASCRIPT) -> Cumulative Risk: **590.1**
- **Archetype:** `file_cluster_8` (Distance: 12.921 IQR)
- **Magnitude:** 4726.68 | **LOC:** 5384 | **CtrlFlow:** 7.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.9042%), Concurrency (95.3477%)
- **Heaviest Functions:** `assertEq` (Impact: 231.8), `__decorateElement` (Impact: 130.8), `assertEq` (Impact: 50.7)

### 9. `scripts/register-test.js` (JAVASCRIPT) -> Cumulative Risk: **572.59**
- **Archetype:** `file_cluster_4` (Distance: 11.963 IQR)
- **Magnitude:** 155.08 | **LOC:** 116 | **CtrlFlow:** 37.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Tech Debt (99.996%), Cognitive Load (99.97%)
- **Heaviest Functions:** `main` (Impact: 19.9), `removeRecursiveSync` (Impact: 17.1), `runTest` (Impact: 7.7)

### 10. `internal/js_ast/js_ast.go` (GO) -> Cumulative Risk: **569.01**
- **Archetype:** `file_cluster_8` (Distance: 11.773 IQR)
- **Magnitude:** 723.0 | **LOC:** 1860 | **CtrlFlow:** 19.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (83.2018%)
- **Heaviest Functions:** `EnsureValidIdentifier` (Impact: 29.1), `ConstValueToExpr` (Impact: 15.0), `HasSameFlagsAs` (Impact: 10.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `scripts/end-to-end-tests.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_4` (Drift: 15.337 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 6.384 IQR)
- **Top Global Matches:** file_cluster_4: 15.337, file_cluster_13: 15.645, file_cluster_11: 15.765
- **Magnitude:** 7898.96 | **LOC:** 9848 | **CtrlFlow:** 36.1% | **Authorship Centralization:** 83.3%
- **Risk Profile:** Cognitive Load (98.3635%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `test` (Impact: 157.8)
  * `test` (Impact: 37.9)
    * *Intent:* // Test minification of mangled properties (class and object) with a keyword before them
  * `async` (Impact: 29.9)
  * `waitForCondition` (Impact: 28.0)
  * `test` (Impact: 26.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1606`, `structural_boundaries: 2844`, `args: 860`, `func_start: 1378`, `class_start: 130`
* *Risk/State:* `safety_bypasses: 102`, `high_risk_execution: 1`, `state_mutation: 1924`, `dead_code: 11`, `fragile_debt: 7`, `duplicate_logic: 521`
* *Architecture:* `io: 203`, `api: 482`, `concurrency: 2507`, `import: 413`
* *Defense:* `safety: 1051`, `test: 690`, `immutability_locks: 270`, `cleanup: 37`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.698
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` node2.ts, out, export-private, node, d, child, foo.css, foo.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/linker/linker.go` (GO | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.052 IQR)
- **Top Global Matches:** file_cluster_8: 15.052, file_cluster_7: 15.075, file_cluster_13: 15.195
- **Magnitude:** 5047.34 | **LOC:** 7294 | **CtrlFlow:** 83.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (47.3474%), Tech Debt (22.036%)
**Top Internal Functions/Classes:**
  * `mangleLocalCSS` (Impact: 435.6)
  * `computeCrossChunkDependencies` (Impact: 353.7)
    * *Intent:* // Reserve all target properties in the cache
  * `convertStmtsForChunk` (Impact: 293.0)
    * *Intent:* // Encode import-specific constraints in the dependency graph
  * `validateComposesFromProperties` (Impact: 260.7)
  * `breakOutputIntoPieces` (Impact: 166.0)
    * *Intent:* // JavaScript modules are traversed in depth-first postorder. This is the // order that JavaScript m...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 732`, `structural_boundaries: 148`, `args: 37`, `func_start: 37`, `class_start: 18`
* *Risk/State:* `state_mutation: 2375`, `dead_code: 11`, `planned_debt: 2`, `fragile_debt: 1`, `duplicate_logic: 2`, `orphaned_logic: 13`
* *Architecture:* `api: 160`, `concurrency: 30`, `import: 1`
* *Defense:* `safety: 9`, `doc: 316`, `sync_locks: 5`, `immutability_locks: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.861
  * `Choke Point (Betweenness):` 0.000236 | `Ripple Effect (Closeness):` 0.005181
  * `Imports (Out-Degree: 21):` css_lexer, js_ast, sync, strings, graph, css_ast, strconv, sourcemap...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `scripts/decorator-tests.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.921 IQR)
- **Local Micro-Species:** `Cluster 6: Documented Native Core Logic` (Drift: 5.201 IQR)
- **Top Global Matches:** file_cluster_8: 12.921, file_cluster_4: 13.12, file_cluster_15: 13.121
- **Magnitude:** 4726.68 | **LOC:** 5384 | **CtrlFlow:** 7.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (85.8269%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `assertEq` (Impact: 231.8)
  * `__decorateElement` (Impact: 130.8)
  * `assertEq` (Impact: 50.7)
  * `assertEq` (Impact: 50.5)
  * `assertEq` (Impact: 49.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 204`, `structural_boundaries: 2531`, `args: 1870`, `func_start: 1897`, `class_start: 131`
* *Risk/State:* `safety_bypasses: 51`, `state_mutation: 1430`, `duplicate_logic: 918`
* *Architecture:* `concurrency: 328`
* *Defense:* `safety: 158`, `test: 1`, `immutability_locks: 380`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.698
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/js_printer/js_printer.go` (GO | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.655 IQR)
- **Top Global Matches:** file_cluster_8: 13.655, file_cluster_7: 13.845, file_cluster_15: 14.057
- **Magnitude:** 3882.96 | **LOC:** 5026 | **CtrlFlow:** 89.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (47.9721%), Tech Debt (13.2385%)
**Top Internal Functions/Classes:**
  * `printBinding` (Impact: 1224.1)
  * `lateConstantFoldUnaryOrBinaryOrIfExpr` (Impact: 538.6)
  * `printExprCommentsAfterCloseTokenAtLoc` (Impact: 459.0)
  * `printUnquotedUTF16` (Impact: 91.7)
  * `printIf` (Impact: 60.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 572`, `structural_boundaries: 64`, `args: 32`, `func_start: 32`, `class_start: 1`
* *Risk/State:* `state_mutation: 983`, `dead_code: 1`, `orphaned_logic: 10`
* *Architecture:* `api: 12`, `import: 1`
* *Defense:* `doc: 83`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.814
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.006908
  * `Imports (Out-Degree: 8):` compat, sourcemap, utf8, helpers, js_ast, fmt, math, bytes...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Makefile` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.931 IQR)
- **Top Global Matches:** file_cluster_8: 12.931, file_cluster_0: 13.131, file_cluster_11: 13.17
- **Magnitude:** 3495.08 | **LOC:** 1174 | **CtrlFlow:** 95.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (35.1741%), Tech Debt (12.2239%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 295`, `structural_boundaries: 14`, `func_start: 162`
* *Risk/State:* `state_mutation: 115`, `dead_code: 13`, `fragile_debt: 2`
* *Architecture:* `io: 117`, `api: 2`
* *Defense:* `test: 4`, `cleanup: 85`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.698
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/js_lexer/js_lexer.go` (GO | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.13 IQR)
- **Top Global Matches:** file_cluster_8: 14.13, file_cluster_7: 14.25, file_cluster_15: 14.393
- **Magnitude:** 2982.1 | **LOC:** 2666 | **CtrlFlow:** 92.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.0691%), Tech Debt (16.3771%)
**Top Internal Functions/Classes:**
  * `Next` (Impact: 554.8)
  * `parseNumericLiteralOrDot` (Impact: 365.0)
  * `ScanRegExp` (Impact: 183.2)
    * *Intent:* // "..."
  * `NextInsideJSXElement` (Impact: 138.6)
  * `NextJSXElementChild` (Impact: 61.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 569`, `structural_boundaries: 48`, `args: 34`, `func_start: 34`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 1168`, `dead_code: 1`, `orphaned_logic: 14`
* *Architecture:* `api: 146`, `import: 1`
* *Defense:* `doc: 97`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.07
  * `Choke Point (Betweenness):` 0.001439 | `Ripple Effect (Closeness):` 0.048226
  * `Imports (Out-Degree: 7):` super, function, break, return, utf8, js_ast, continue, while...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `scripts/js-api-tests.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.343 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.52 IQR)
- **Top Global Matches:** file_cluster_4: 12.343, file_cluster_8: 12.862, file_cluster_13: 12.923
- **Magnitude:** 2918.98 | **LOC:** 8070 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (99.961%), Tech Debt (97.8383%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 23.4)
  * `check` (Impact: 13.1)
  * `reject` (Impact: 12.3)
  * `runTest` (Impact: 9.3)
  * `invalid` (Impact: 7.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 305`, `structural_boundaries: 1176`, `args: 357`, `func_start: 372`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 28`, `high_risk_execution: 4`, `state_mutation: 383`, `dead_code: 1`, `fragile_debt: 1`, `duplicate_logic: 33`, `orphaned_logic: 84`
* *Architecture:* `io: 592`, `api: 72`, `concurrency: 2105`, `import: 119`
* *Defense:* `safety: 218`, `test: 492`, `immutability_locks: 508`, `cleanup: 35`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.698
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` disabled, jsx-runtime, assert, vm, chunk-3MCOY2GR.js, other, text.txt, file.png...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/css_parser/css_parser.go` (GO | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.924 IQR)
- **Top Global Matches:** file_cluster_8: 13.924, file_cluster_7: 14.064, file_cluster_13: 14.269
- **Magnitude:** 2323.98 | **LOC:** 2487 | **CtrlFlow:** 81.0% | **Authorship Centralization:** 83.3%
- **Risk Profile:** Cognitive Load (47.4043%), Tech Debt (10.5031%)
**Top Internal Functions/Classes:**
  * `parseListOfDeclarations` (Impact: 865.5)
  * `parseAtRule` (Impact: 334.7)
  * `parseDeclaration` (Impact: 61.0)
  * `parseSelectorRule` (Impact: 48.4)
  * `scanForEndOfRule` (Impact: 40.0)
    * *Intent:* // Remove leading and trailing whitespace
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 353`, `structural_boundaries: 83`, `args: 17`, `func_start: 17`, `class_start: 7`
* *Risk/State:* `state_mutation: 727`, `dead_code: 1`, `orphaned_logic: 4`
* *Architecture:* `api: 46`, `import: 1`
* *Defense:* `doc: 65`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.568
  * `Choke Point (Betweenness):` 0.000342 | `Ripple Effect (Closeness):` 0.01658
  * `Imports (Out-Degree: 9):` h1, right-middle, css_lexer, div, charset, s, pre, dt...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `internal/css_ast/css_ast.go` (GO | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.662 IQR)
- **Top Global Matches:** file_cluster_8: 13.662, file_cluster_15: 13.777, file_cluster_7: 13.857
- **Magnitude:** 2298.24 | **LOC:** 1581 | **CtrlFlow:** 52.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (66.5258%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `CloneTokensWithImportRecords` (Impact: 639.4)
  * `String` (Impact: 30.4)
  * `ContainsNestingCombinator` (Impact: 23.2)
  * `EqualIgnoringWhitespace` (Impact: 22.7)
  * `Equal` (Impact: 22.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 300`, `structural_boundaries: 273`, `args: 108`, `func_start: 108`, `class_start: 37`
* *Risk/State:* `state_mutation: 553`, `duplicate_logic: 75`, `orphaned_logic: 16`
* *Architecture:* `api: 282`, `import: 1`
* *Defense:* `doc: 32`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 17.05
  * `Choke Point (Betweenness):` 0.001237 | `Ripple Effect (Closeness):` 0.131347
  * `Imports (Out-Degree: 4):` css_lexer, nth-child, global, nth-of-type, strconv, before, local, nth-last-child...
  * `Imported By (In-Degree: 24):` (Excluded from Brief to save tokens)

### `pkg/api/api_impl.go` (GO | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.884 IQR)
- **Top Global Matches:** file_cluster_8: 13.884, file_cluster_7: 13.993, file_cluster_13: 14.139
- **Magnitude:** 2041.68 | **LOC:** 2566 | **CtrlFlow:** 70.9% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (47.3066%), Tech Debt (17.0697%)
**Top Internal Functions/Classes:**
  * `validatePathTemplate` (Impact: 373.7)
  * `activeBuildOrRecentBuildOrRebuild` (Impact: 176.4)
  * `loadPlugins` (Impact: 134.5)
  * `validateBuildOptions` (Impact: 116.9)
  * `analyzeMetafileImpl` (Impact: 86.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 227`, `structural_boundaries: 93`, `args: 31`, `func_start: 31`, `class_start: 6`
* *Risk/State:* `state_mutation: 775`, `orphaned_logic: 9`
* *Architecture:* `api: 130`, `concurrency: 24`, `import: 1`
* *Defense:* `safety: 6`, `doc: 59`, `sync_locks: 11`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.698
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` css, .js, utf8, js_ast, sync, logger, strings, graph...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/js_ast/js_ast_helpers.go` (GO | Tier 2 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.953 IQR)
- **Top Global Matches:** file_cluster_8: 13.953, file_cluster_7: 14.05, file_cluster_13: 14.15
- **Magnitude:** 1960.48 | **LOC:** 3017 | **CtrlFlow:** 69.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.4085%), Tech Debt (17.5595%)
**Top Internal Functions/Classes:**
  * `simplifyUnusedStringAdditionChain` (Impact: 462.3)
  * `isInt32OrUint32` (Impact: 285.9)
  * `MangleIfExpr` (Impact: 104.3)
  * `ExprCanBeRemovedIfUnused` (Impact: 80.3)
  * `StmtsCanBeRemovedIfUnused` (Impact: 69.5)
    * *Intent:* // of "foo?.bar" to save the value of "foo" to ensure that it's only // evaluated once. Specifically...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 367`, `structural_boundaries: 160`, `args: 19`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `state_mutation: 587`, `dead_code: 3`, `orphaned_logic: 8`
* *Architecture:* `api: 69`, `import: 1`
* *Defense:* `doc: 71`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.698
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` function, number, strings, boolean, true, strconv, object, ast...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/css_parser/css_parser_selector.go` (GO | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.527 IQR)
- **Top Global Matches:** file_cluster_8: 13.527, file_cluster_7: 13.692, file_cluster_13: 13.896
- **Magnitude:** 1645.88 | **LOC:** 998 | **CtrlFlow:** 79.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (39.5547%), Tech Debt (9.137%)
**Top Internal Functions/Classes:**
  * `mergeCompoundSelectors` (Impact: 419.1)
  * `parseCompoundSelector` (Impact: 106.9)
    * *Intent:* // Parent
  * `parseNthIndex` (Impact: 92.4)
  * `parseSelectorList` (Impact: 78.1)
  * `parseAttributeSelector` (Impact: 76.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 246`, `structural_boundaries: 63`, `args: 12`, `func_start: 12`, `class_start: 2`
* *Risk/State:* `state_mutation: 652`, `fragile_debt: 1`
* *Architecture:* `api: 20`, `import: 1`
* *Defense:* `doc: 46`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.698
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` 0, css_lexer, nth-child, global, nth-of-type, before, fmt, local...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pkg/cli/cli_impl.go` (GO | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.753 IQR)
- **Top Global Matches:** file_cluster_8: 14.753, file_cluster_7: 15.001, file_cluster_13: 15.026
- **Magnitude:** 1639.26 | **LOC:** 1565 | **CtrlFlow:** 78.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (56.0022%), Tech Debt (8.7936%)
**Top Internal Functions/Classes:**
  * `parseServeOptionsImpl` (Impact: 51.4)
    * *Intent:* // This should already have been checked above
  * `serveImpl` (Impact: 29.0)
    * *Intent:* // Write the metafile to the file system
  * `parseTargets` (Impact: 23.4)
  * `filterAnalyzeFlags` (Impact: 21.1)
  * `parseOptionsForRun` (Impact: 17.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 445`, `structural_boundaries: 125`, `args: 10`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 1415`, `dead_code: 1`, `orphaned_logic: 2`
* *Architecture:* `api: 22`, `concurrency: 6`, `import: 1`
* *Defense:* `safety: 42`, `doc: 39`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.698
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` target, --analyze, automatic, legal-comments, charset, keep-names, color, jsx-side-effects...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/plugin-tests.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.754 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.364 IQR)
- **Top Global Matches:** file_cluster_4: 11.754, file_cluster_8: 11.952, file_cluster_13: 12.16
- **Magnitude:** 1554.12 | **LOC:** 3513 | **CtrlFlow:** 26.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (90.1334%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 20.3)
  * `setup` (Impact: 12.2)
  * `makeRebuildUntilPlugin` (Impact: 11.4)
  * `fetchUntilSuccessOrTimeout` (Impact: 11.2)
  * `reject` (Impact: 10.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 280`, `structural_boundaries: 765`, `args: 368`, `func_start: 224`
* *Risk/State:* `safety_bypasses: 55`, `high_risk_execution: 1`, `state_mutation: 158`, `planned_debt: 3`, `duplicate_logic: 106`, `orphaned_logic: 88`
* *Architecture:* `io: 344`, `api: 92`, `concurrency: 720`, `import: 69`
* *Defense:* `safety: 130`, `test: 237`, `immutability_locks: 224`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.698
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` fib($n - 2), loadme, assert, entry, <virtual>, util, url, loadme...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/resolver/resolver.go` (GO | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.179 IQR)
- **Top Global Matches:** file_cluster_8: 14.179, file_cluster_7: 14.271, file_cluster_13: 14.419
- **Magnitude:** 1399.86 | **LOC:** 2973 | **CtrlFlow:** 76.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (39.9306%), Tech Debt (28.6203%)
**Top Internal Functions/Classes:**
  * `Resolve` (Impact: 194.1)
  * `loadAsMainField` (Impact: 134.2)
  * `ResolveGlob` (Impact: 92.8)
    * *Intent:* // This mutex serves two purposes. First of all, it guards access to "dirCache" // which is potentia...
  * `loadNodeModules` (Impact: 46.5)
  * `loadAsDirectory` (Impact: 21.2)
    * *Intent:* // Check the "browser" map
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 342`, `structural_boundaries: 104`, `args: 15`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `state_mutation: 785`, `dead_code: 3`, `fragile_debt: 3`, `orphaned_logic: 6`
* *Architecture:* `api: 14`, `import: 1`
* *Defense:* `safety: 7`, `doc: 125`, `sync_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.305
  * `Choke Point (Betweenness):` 0.000396 | `Ripple Effect (Closeness):` 0.025907
  * `Imports (Out-Degree: 9):` sync, posix, _stream_duplex, dns, diagnostics_channel, promises, errors, v8...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `internal/js_parser/js_parser_lower_class.go` (GO | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.733 IQR)
- **Top Global Matches:** file_cluster_8: 14.733, file_cluster_7: 14.801, file_cluster_13: 14.82
- **Magnitude:** 1393.82 | **LOC:** 2601 | **CtrlFlow:** 82.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (37.1863%), Tech Debt (19.0217%)
**Top Internal Functions/Classes:**
  * `computeClassLoweringInfo` (Impact: 189.9)
  * `lowerSuperPropertyOrPrivateInAssign` (Impact: 60.1)
  * `insertStmtsAfterSuperCall` (Impact: 48.5)
  * `finishAndGenerateCode` (Impact: 34.1)
  * `rewriteAutoAccessorToGetSet` (Impact: 30.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 228`, `structural_boundaries: 47`, `args: 25`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 736`, `dead_code: 10`, `orphaned_logic: 9`
* *Architecture:* `api: 70`, `import: 1`
* *Defense:* `doc: 74`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.698
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` compat, js_ast, fmt, config, logger, helpers, ast
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/js_parser/ts_parser.go` (GO | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.474 IQR)
- **Top Global Matches:** file_cluster_8: 13.474, file_cluster_7: 13.587, file_cluster_13: 13.689
- **Magnitude:** 1146.32 | **LOC:** 2087 | **CtrlFlow:** 84.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (38.3795%), Tech Debt (25.6916%)
**Top Internal Functions/Classes:**
  * `skipTypeScriptTypeWithFlags` (Impact: 173.9)
    * *Intent:* // "{1: y}"
  * `skipTypeScriptTypeParameters` (Impact: 89.1)
  * `skipTypeScriptObjectType` (Impact: 69.7)
  * `tsIsStartOfExpression` (Impact: 65.2)
  * `isTypeScriptArrowReturnTypeAfterQuestion` (Impact: 58.1)
    * *Intent:* // Valid: // "type Foo<out T> = T" // "type Foo<out out> = T"
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 296`, `structural_boundaries: 56`, `args: 19`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `state_mutation: 412`, `dead_code: 9`, `planned_debt: 2`, `fragile_debt: 1`, `orphaned_logic: 7`
* *Architecture:* `api: 68`
* *Defense:* `safety: 5`, `doc: 72`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.698
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` js_ast, number, strings, boolean, object, asserts, symbol, ast...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/css_parser/css_decls_color.go` (GO | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.594 IQR)
- **Top Global Matches:** file_cluster_8: 13.594, file_cluster_7: 13.939, file_cluster_13: 14.113
- **Magnitude:** 1083.04 | **LOC:** 939 | **CtrlFlow:** 78.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (82.6437%), Tech Debt (9.5296%)
**Top Internal Functions/Classes:**
  * `parseColor` (Impact: 214.2)
  * `lowerAndMinifyColor` (Impact: 94.8)
    * *Intent:* // Convert newer color syntax to older color syntax for older browsers
  * `tryToGenerateColor` (Impact: 32.8)
  * `looksLikeColor` (Impact: 23.8)
  * `degreesForAngle` (Impact: 23.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 241`, `structural_boundaries: 65`, `args: 22`, `func_start: 22`, `class_start: 1`
* *Risk/State:* `state_mutation: 556`, `orphaned_logic: 2`
* *Architecture:* `import: 1`
* *Defense:* `doc: 10`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.698
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` mediumaquamarine, css_lexer, darkorchid, violet, srgb, greenyellow, mediumorchid, xyz-d50...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/js_parser/js_parser_lower.go` (GO | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_11` (Drift: 15.198 IQR)
- **Top Global Matches:** file_cluster_11: 15.198, file_cluster_13: 15.244, file_cluster_0: 15.265
- **Magnitude:** 1035.72 | **LOC:** 2133 | **CtrlFlow:** 79.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (38.0426%), Tech Debt (54.115%)
**Top Internal Functions/Classes:**
  * `lowerFunction` (Impact: 191.3)
  * `markSyntaxFeature` (Impact: 49.0)
  * `lowerObjectRestInForLoopInit` (Impact: 47.1)
  * `captureKeyForObjectRest` (Impact: 44.2)
  * `markStrictModeFeature` (Impact: 29.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 171`, `structural_boundaries: 44`, `args: 15`, `func_start: 15`
* *Risk/State:* `state_mutation: 504`, `dead_code: 11`, `planned_debt: 1`, `orphaned_logic: 10`
* *Architecture:* `api: 61`, `import: 1`
* *Defense:* `doc: 47`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.698
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` compat, js_ast, fmt, config, logger, helpers, ast
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/bundler/bundler.go` (GO | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.441 IQR)
- **Top Global Matches:** file_cluster_8: 14.441, file_cluster_7: 14.541, file_cluster_4: 14.564
- **Magnitude:** 1022.0 | **LOC:** 3532 | **CtrlFlow:** 81.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (43.8904%), Tech Debt (12.602%)
**Top Internal Functions/Classes:**
  * `preprocessInjectedFiles` (Impact: 99.9)
  * `ScanBundle` (Impact: 85.3)
  * `sanitizeFilePathForVirtualModulePath` (Impact: 28.1)
    * *Intent:* // Support data URLs
  * `allocateSourceIndex` (Impact: 5.2)
  * `allocateGlobSourceIndex` (Impact: 5.2)
    * *Intent:* // Failed imports inside a try/catch are silently turned into // external imports instead of causing...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 188`, `structural_boundaries: 42`, `args: 6`, `func_start: 6`, `class_start: 5`
* *Risk/State:* `state_mutation: 697`, `orphaned_logic: 4`
* *Architecture:* `io: 1`, `api: 31`, `concurrency: 54`, `import: 1`
* *Defense:* `safety: 6`, `doc: 77`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.977
  * `Choke Point (Betweenness):` 0.000128 | `Ripple Effect (Closeness):` 0.010363
  * `Imports (Out-Degree: 14):` rand, .js, utf8, js_ast, sync, .txt, unicode, strings...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `internal/css_parser/css_reduce_calc.go` (GO | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.694 IQR)
- **Top Global Matches:** file_cluster_8: 13.694, file_cluster_7: 13.828, file_cluster_15: 13.93
- **Magnitude:** 928.32 | **LOC:** 606 | **CtrlFlow:** 71.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (39.0572%), Tech Debt (98.1014%)
**Top Internal Functions/Classes:**
  * `tryToParseCalcTerm` (Impact: 150.8)
  * `partiallySimplify` (Impact: 59.9)
  * `convertToToken` (Impact: 48.2)
  * `partiallySimplify` (Impact: 29.0)
  * `convertToToken` (Impact: 21.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 153`, `structural_boundaries: 61`, `args: 15`, `func_start: 15`, `class_start: 8`
* *Risk/State:* `state_mutation: 483`, `duplicate_logic: 12`, `orphaned_logic: 1`
* *Architecture:* `api: 44`, `import: 1`
* *Defense:* `safety: 1`, `doc: 34`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.698
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` css_lexer, fmt, math, strings, css_ast, logger, strconv
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/resolver/package_json.go` (GO | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.101 IQR)
- **Top Global Matches:** file_cluster_8: 13.101, file_cluster_7: 13.255, file_cluster_13: 13.451
- **Magnitude:** 886.66 | **LOC:** 1463 | **CtrlFlow:** 68.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (38.3312%), Tech Debt (40.2223%)
**Top Internal Functions/Classes:**
  * `parseImportsExportsMap` (Impact: 114.2)
  * `checkBrowserMap` (Impact: 69.7)
  * `parsePackageJSON` (Impact: 48.0)
  * `esmPackageTargetReverseResolve` (Impact: 39.9)
  * `globstarToEscapedRegexp` (Impact: 23.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 212`, `structural_boundaries: 98`, `args: 14`, `func_start: 14`, `class_start: 6`
* *Risk/State:* `state_mutation: 476`, `dead_code: 1`, `fragile_debt: 2`, `orphaned_logic: 7`
* *Architecture:* `api: 18`, `import: 1`
* *Defense:* `safety: 1`, `doc: 64`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.698
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` module, regexp, url, js_parser, js_ast, require, fmt, strings...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/css_printer/css_printer.go` (GO | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.25 IQR)
- **Top Global Matches:** file_cluster_8: 13.25, file_cluster_7: 13.481, file_cluster_13: 13.62
- **Magnitude:** 835.08 | **LOC:** 1324 | **CtrlFlow:** 89.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (47.5517%), Tech Debt (10.3629%)
**Top Internal Functions/Classes:**
  * `printTokens` (Impact: 90.1)
  * `printIdent` (Impact: 63.0)
  * `printQuotedWithQuote` (Impact: 44.9)
  * `printWithEscape` (Impact: 35.8)
  * `printRule` (Impact: 34.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 233`, `structural_boundaries: 28`, `args: 18`, `func_start: 18`, `class_start: 3`
* *Risk/State:* `state_mutation: 392`, `dead_code: 2`, `orphaned_logic: 2`
* *Architecture:* `api: 7`, `import: 1`
* *Defense:* `doc: 25`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.814
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.006908
  * `Imports (Out-Degree: 8):` compat, sourcemap, css_lexer, repeating-linear-gradient, utf8, linear-gradient, matrix3d, fmt...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `internal/runtime/runtime.go` (GO | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.292 IQR)
- **Top Global Matches:** file_cluster_8: 14.292, file_cluster_7: 14.49, file_cluster_13: 14.667
- **Magnitude:** 760.18 | **LOC:** 612 | **CtrlFlow:** 76.1% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (38.1565%), Tech Debt (9.7841%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 105`, `structural_boundaries: 33`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 731`, `planned_debt: 2`
* *Architecture:* `api: 7`
* *Defense:* `doc: 26`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 39.242
  * `Choke Point (Betweenness):` 0.001093 | `Ripple Effect (Closeness):` 0.141256
  * `Imports (Out-Degree: 2):` compat, logger
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `internal/js_ast/js_ast.go` (GO | Tier 2 | 🚨 AI THREAT: 98.82%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.773 IQR)
- **Top Global Matches:** file_cluster_8: 11.773, file_cluster_7: 11.877, file_cluster_15: 11.966
- **Magnitude:** 723.0 | **LOC:** 1860 | **CtrlFlow:** 19.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (9.9481%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `EnsureValidIdentifier` (Impact: 29.1)
    * *Intent:* // This object represents all of these types of import statements: // // import 'path' // import {it...
  * `ConstValueToExpr` (Impact: 15.0)
  * `HasSameFlagsAs` (Impact: 10.1)
  * `HasSameFlagsAs` (Impact: 7.6)
  * `BinaryAssignTarget` (Impact: 7.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 185`, `args: 59`, `func_start: 59`, `class_start: 66`
* *Risk/State:* `state_mutation: 75`, `dead_code: 4`, `duplicate_logic: 46`, `orphaned_logic: 11`
* *Architecture:* `api: 430`, `import: 1`
* *Defense:* `doc: 106`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 14.338
  * `Choke Point (Betweenness):` 0.000211 | `Ripple Effect (Closeness):` 0.116062
  * `Imports (Out-Degree: 2):` _, logger, strconv, ast
  * `Imported By (In-Degree: 21):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `internal/js_parser/js_parser_lower.go` (GO) | Magnitude: 1035.72 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 554, state_mutation: 504, encapsulation: 179, branch: 171

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `internal/logger/logger_other.go` (GO) | Magnitude: 6.98 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 3, args: 2, func_start: 2, api: 2
- `internal/helpers/glob.go` (GO) | Magnitude: 37.36 | Delta: **0.057 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 19, state_mutation: 16, api: 8, structural_boundaries: 6
- `scripts/ts-type-tests.js` (JAVASCRIPT) | Magnitude: 179.54 | Delta: **0.094 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 428, structural_boundaries: 117, state_mutation: 72, concurrency: 43
- `internal/logger/logger_darwin.go` (GO) | Magnitude: 35.12 | Delta: **0.095 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 24, indent_tabs: 13, encapsulation: 7, explicit_casts: 4
- `internal/logger/logger_linux.go` (GO) | Magnitude: 35.12 | Delta: **0.095 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 24, indent_tabs: 13, encapsulation: 7, explicit_casts: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `internal/ast/ast.go` (GO) | Magnitude: 396.58 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 231, api: 126, state_mutation: 117, structural_boundaries: 67

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `scripts/terser-tests.js` (JAVASCRIPT) | Magnitude: 313.48 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 212, state_mutation: 69, branch: 58, structural_boundaries: 51
- `compat-table/src/css_table.ts` (TYPESCRIPT) | Magnitude: 8.71 | Delta: **0.331 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 39, indent_spaces: 34, state_mutation: 28, args: 23
- `compat-table/src/js_table.ts` (TYPESCRIPT) | Magnitude: 7.3 | Delta: **0.545 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 41, indent_spaces: 39, state_mutation: 28, args: 24

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `pkg/api/watcher.go` (GO) | Magnitude: 147.72 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: state_mutation: 88, indent_tabs: 78, branch: 21, encapsulation: 21
- `internal/fs/fs.go` (GO) | Magnitude: 89.5 | Delta: **0.056 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 51, state_mutation: 34, structural_boundaries: 20, doc: 15
- `scripts/uglify-tests.js` (JAVASCRIPT) | Magnitude: 77.66 | Delta: **0.098 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 70, state_mutation: 20, structural_boundaries: 18, branch: 14
- `scripts/destructuring-fuzzer.js` (JAVASCRIPT) | Magnitude: 626.52 | Delta: **0.112 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 291, state_mutation: 267, structural_boundaries: 164, branch: 68
- `scripts/plugin-tests.js` (JAVASCRIPT) | Magnitude: 1554.12 | Delta: **0.198 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 2948, structural_boundaries: 765, concurrency: 720, args: 368

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `internal/fs/fs_real.go` (GO) | Magnitude: 510.9 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 306, state_mutation: 256, encapsulation: 110, branch: 77
- `internal/linker/linker.go` (GO) | Magnitude: 5047.34 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: state_mutation: 2375, indent_tabs: 2367, encapsulation: 910, branch: 732
- `internal/helpers/dataurl.go` (GO) | Magnitude: 53.38 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 29, indent_tabs: 27, encapsulation: 10, branch: 9
- `compat-table/src/index.ts` (TYPESCRIPT) | Magnitude: 10.65 | Delta: **0.036 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 224, structural_boundaries: 49, immutability_locks: 46, branch: 36
- `internal/cache/cache_fs.go` (GO) | Magnitude: 24.44 | Delta: **0.04 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 18, state_mutation: 9, structural_boundaries: 6, branch: 5

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `scripts/end-to-end-tests.js` -> **Evan Wallace** (83.3% isolated ownership) | Magnitude: 7898.96
- `internal/linker/linker.go` -> **Evan Wallace** (100.0% isolated ownership) | Magnitude: 5047.34
- `scripts/decorator-tests.js` -> **Evan Wallace** (100.0% isolated ownership) | Magnitude: 4726.68
- `internal/js_printer/js_printer.go` -> **Evan Wallace** (100.0% isolated ownership) | Magnitude: 3882.96
- `Makefile` -> **Evan Wallace** (100.0% isolated ownership) | Magnitude: 3495.08

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `internal/logger/logger.go` -> **Severity: 0.272** (Bridge: 0.0027 * Flux: 100.0%)
- `internal/js_lexer/js_lexer.go` -> **Severity: 0.144** (Bridge: 0.0014 * Flux: 100.0%)
- `internal/css_ast/css_ast.go` -> **Severity: 0.124** (Bridge: 0.0012 * Flux: 100.0%)
- `internal/config/config.go` -> **Severity: 0.111** (Bridge: 0.0011 * Flux: 100.0%)
- `internal/runtime/runtime.go` -> **Severity: 0.109** (Bridge: 0.0011 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `internal/helpers/strings.go` -> **Severity: 27.172** (Embedded: 0.3486 * Error Risk: 77.9569%)
- `internal/logger/logger.go` -> **Severity: 23.464** (Embedded: 0.24 * Error Risk: 97.7806%)
- `internal/ast/ast.go` -> **Severity: 14.588** (Embedded: 0.1688 * Error Risk: 86.4283%)
- `internal/runtime/runtime.go` -> **Severity: 14.125** (Embedded: 0.1413 * Error Risk: 99.9991%)
- `internal/css_ast/css_ast.go` -> **Severity: 12.431** (Embedded: 0.1313 * Error Risk: 94.6435%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `internal/helpers/strings.go` -> **Severity: 14122.879** (Blast Radius: 172.466 * Doc Risk: 81.8879%)
- `internal/ast/ast.go` -> **Severity: 3634.6** (Blast Radius: 36.346 * Doc Risk: 100.0%)
- `internal/helpers/path.go` -> **Severity: 2038.463** (Blast Radius: 23.025 * Doc Risk: 88.5326%)
- `internal/css_ast/css_ast.go` -> **Severity: 1705.0** (Blast Radius: 17.05 * Doc Risk: 100.0%)
- `internal/logger/logger.go` -> **Severity: 1458.236** (Blast Radius: 81.555 * Doc Risk: 17.8804%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
