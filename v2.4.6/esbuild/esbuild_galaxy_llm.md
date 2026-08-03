# ARCHITECTURAL_BRIEF: esbuild
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_typescript/esbuild` |
| **Timestamp** | `2026-08-03T19:54:18.379004+00:00` |
| **Scan Duration** | `3.11s` |
| **Git Branch** | `main` |
| **Git Commit** | `6a794dff68e6a43539f6da671e3080efdf11ca70` |
| **Git Remote** | `https://github.com/evanw/esbuild.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 136 malicious artifacts.

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
| Cognitive Load Exposure | 0.0 | 100.0 | 36.8 | 37.9 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 62.9 | 82.4 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 41.1 | 23.3 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 34.6 | 2.5 | 80.0 |
| API Exposure | 0.0 | 17.8 | 3.0 | 1.4 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 11.6 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 69.4 | 100.0 | 100.0 |
| Commented Logic Exposure | 0.0 | 22.8 | 1.4 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 90.7 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 10.3 | 0.9 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 65.4 | 4.8 | 0.0 | 0.0 |
| Documentation Exposure | 3.2 | 100.0 | 36.0 | 17.9 | 11.9 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 18.3 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 13.5 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 4.1 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
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

- `printBinding` (@ `internal/js_printer/js_printer.go`) -> Impact: **3507.0** | LOC: 1653
- `parseListOfDeclarations` (@ `internal/css_parser/css_parser.go`) -> Impact: **2472.3** | LOC: 1241
- `simplifyUnusedStringAdditionChain` (@ `internal/js_ast/js_ast_helpers.go`) -> Impact: **1318.3** | LOC: 686
- `CloneTokensWithImportRecords` (@ `internal/css_ast/css_ast.go`) -> Impact: **1224.9** | LOC: 1080
- `mergeCompoundSelectors` (@ `internal/css_parser/css_parser_selector.go`) -> Impact: **1174.3** | LOC: 830
- `convertStmtsForChunk` (@ `internal/linker/linker.go`) -> Impact: **1104.7** | LOC: 854
  * *Intent:* // Encode import-specific constraints in the dependency graph
- `validatePathTemplate` (@ `pkg/api/api_impl.go`) -> Impact: **1041.7** | LOC: 794
- `Next` (@ `internal/js_lexer/js_lexer.go`) -> Impact: **816.5** | LOC: 632
- `mangleLocalCSS` (@ `internal/linker/linker.go`) -> Impact: **636.4** | LOC: 677
- `parseNumericLiteralOrDot` (@ `internal/js_lexer/js_lexer.go`) -> Impact: **536.0** | LOC: 457

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `runIfIdle` (@ `scripts/try.html`) -> **O(2^N) [Recursive]**
- `assertEq` (@ `scripts/decorator-tests.js`) -> **O(2^N) [Recursive]**
- `assertEq` (@ `scripts/decorator-tests.js`) -> **O(2^N) [Recursive]**
- `test` (@ `scripts/deno-tests.js`) -> **O(2^N) [Recursive]**
- `parseListOfDeclarations` (@ `internal/css_parser/css_parser.go`) -> **O(2^N) [Recursive]**
- `mergeCompoundSelectors` (@ `internal/css_parser/css_parser_selector.go`) -> **O(2^N) [Recursive]**
- `simplifyUnusedStringAdditionChain` (@ `internal/js_ast/js_ast_helpers.go`) -> **O(2^N) [Recursive]**
- `printBinding` (@ `internal/js_printer/js_printer.go`) -> **O(2^N) [Recursive]**
- `convertStmtsForChunk` (@ `internal/linker/linker.go`) -> **O(2^N) [Recursive]**
  * *Intent:* // Encode import-specific constraints in the dependency graph
- `validatePathTemplate` (@ `pkg/api/api_impl.go`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `parseListOfDeclarations` (@ `internal/css_parser/css_parser.go`) -> DB Complexity: **230**
- `printBinding` (@ `internal/js_printer/js_printer.go`) -> DB Complexity: **222**
- `CloneTokensWithImportRecords` (@ `internal/css_ast/css_ast.go`) -> DB Complexity: **206**
- `convertStmtsForChunk` (@ `internal/linker/linker.go`) -> DB Complexity: **206**
  * *Intent:* // Encode import-specific constraints in the dependency graph
- `mergeCompoundSelectors` (@ `internal/css_parser/css_parser_selector.go`) -> DB Complexity: **205**
- `mangleLocalCSS` (@ `internal/linker/linker.go`) -> DB Complexity: **192**
- `validatePathTemplate` (@ `pkg/api/api_impl.go`) -> DB Complexity: **179**
- `validateComposesFromProperties` (@ `internal/linker/linker.go`) -> DB Complexity: **175**
- `Next` (@ `internal/js_lexer/js_lexer.go`) -> DB Complexity: **140**
- `parseNumericLiteralOrDot` (@ `internal/js_lexer/js_lexer.go`) -> DB Complexity: **132**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `scripts` | 28 | 17632.44 | 51.01% | 57.86% |
| `internal/css_parser` | 20 | 11922.36 | 49.64% | 34.01% |
| `internal/js_parser` | 6 | 5371.84 | 45.5% | 22.09% |
| `internal/linker` | 2 | 5334.04 | 51.0% | 6.7% |
| `internal/js_printer` | 1 | 4818.26 | 47.71% | 9.0% |
| `__monolith__` | 13 | 3981.16 | 10.43% | 0.94% |
| `internal/js_lexer` | 2 | 3378.6 | 28.64% | 7.37% |
| `internal/resolver` | 6 | 3324.3 | 31.81% | 23.11% |
| `internal/js_ast` | 3 | 3303.5 | 29.55% | 57.71% |
| `pkg/api` | 6 | 3101.12 | 22.27% | 45.4% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `internal/fs/error_other.go` -> **100.0%** Exposure
- `internal/fs/iswin_other.go` -> **100.0%** Exposure
- `internal/fs/iswin_wasm.go` -> **100.0%** Exposure
- `internal/fs/iswin_windows.go` -> **100.0%** Exposure
- `internal/helpers/bitset.go` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `dl.sh` -> **100.0%** Exposure
- `internal/bundler/bundler.go` -> **100.0%** Exposure
- `internal/config/config.go` -> **100.0%** Exposure
- `internal/css_ast/css_ast.go` -> **100.0%** Exposure
- `internal/css_lexer/css_lexer.go` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `scripts/end-to-end-tests.js` -> **0** Orphaned Functions | **244** Duplicates
- `scripts/decorator-tests.js` -> **0** Orphaned Functions | **241** Duplicates
- `scripts/plugin-tests.js` -> **88** Orphaned Functions | **96** Duplicates
- `scripts/js-api-tests.js` -> **84** Orphaned Functions | **25** Duplicates
- `internal/js_ast/js_ast.go` -> **11** Orphaned Functions | **46** Duplicates

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

### Obfuscation & Evasion Surface
- `scripts/test262.js` -> **0.0001%** Exposure
### Exploit Generation Surface
- `internal/bundler/bundler.go` -> **100.0%** Exposure
- `internal/js_lexer/js_lexer.go` -> **100.0%** Exposure
- `internal/linker/linker.go` -> **100.0%** Exposure
- `internal/logger/logger.go` -> **100.0%** Exposure
- `internal/resolver/resolver.go` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `scripts/end-to-end-tests.js` -> **100.0%** Exposure
- `scripts/js-api-tests.js` -> **100.0%** Exposure
- `scripts/node-unref-tests.js` -> **100.0%** Exposure
- `scripts/plugin-tests.js` -> **100.0%** Exposure
- `scripts/register-test.js` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `internal/css_parser/css_decls_color.go` -> **100.0%** Exposure
- `internal/css_parser/css_decls_composes.go` -> **100.0%** Exposure
- `internal/css_parser/css_decls_transform.go` -> **100.0%** Exposure
- `internal/css_parser/css_parser.go` -> **100.0%** Exposure
- `internal/css_parser/css_parser_media.go` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `2177` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `scripts/end-to-end-tests.js` (JAVASCRIPT) -> Cumulative Risk: **889.39**
- **Archetype:** `file_cluster_4` (Distance: 15.318 IQR)
- **Magnitude:** 6473.76 | **LOC:** 9848 | **CtrlFlow:** 36.1% | **Authorship Centralization:** 83.3%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `async` (Impact: 88.8), `test` (Impact: 36.6), `test` (Impact: 29.5)

### 2. `scripts/plugin-tests.js` (JAVASCRIPT) -> Cumulative Risk: **833.16**
- **Archetype:** `file_cluster_4` (Distance: 11.756 IQR)
- **Magnitude:** 1772.62 | **LOC:** 3513 | **CtrlFlow:** 26.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `setup` (Impact: 23.5), `setup` (Impact: 22.0), `main` (Impact: 20.3)

### 3. `scripts/register-test.js` (JAVASCRIPT) -> Cumulative Risk: **816.01**
- **Archetype:** `file_cluster_4` (Distance: 11.962 IQR)
- **Magnitude:** 143.38 | **LOC:** 116 | **CtrlFlow:** 37.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `removeRecursiveSync` (Impact: 24.0), `main` (Impact: 19.9), `main` (Impact: 4.5)

### 4. `scripts/js-api-tests.js` (JAVASCRIPT) -> Cumulative Risk: **770.69**
- **Archetype:** `file_cluster_4` (Distance: 12.34 IQR)
- **Magnitude:** 2999.98 | **LOC:** 8070 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `reject` (Impact: 42.5), `check` (Impact: 25.2), `main` (Impact: 23.4)

### 5. `internal/linker/linker.go` (GO) -> Cumulative Risk: **769.96**
- **Archetype:** `file_cluster_8` (Distance: 15.076 IQR)
- **Magnitude:** 5147.04 | **LOC:** 7294 | **CtrlFlow:** 83.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `convertStmtsForChunk` (Impact: 1104.7), `mangleLocalCSS` (Impact: 636.4), `validateComposesFromProperties` (Impact: 446.5)

### 6. `scripts/terser-tests.js` (JAVASCRIPT) -> Cumulative Risk: **740.56**
- **Archetype:** `file_cluster_17` (Distance: 12.789 IQR)
- **Magnitude:** 318.08 | **LOC:** 373 | **CtrlFlow:** 53.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), State Flux (99.9827%), Algorithmic Dos (99.851%)
- **Heaviest Functions:** `parse_test` (Impact: 149.7), `main` (Impact: 60.8), `as_toplevel` (Impact: 12.8)

### 7. `internal/js_lexer/js_lexer.go` (GO) -> Cumulative Risk: **701.06**
- **Archetype:** `file_cluster_8` (Distance: 14.137 IQR)
- **Magnitude:** 3217.3 | **LOC:** 2666 | **CtrlFlow:** 92.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `Next` (Impact: 816.5), `parseNumericLiteralOrDot` (Impact: 536.0), `NextInsideJSXElement` (Impact: 138.6)

### 8. `internal/resolver/yarnpnp.go` (GO) -> Cumulative Risk: **697.69**
- **Archetype:** `file_cluster_8` (Distance: 12.749 IQR)
- **Magnitude:** 513.76 | **LOC:** 685 | **CtrlFlow:** 69.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `resolveViaFallback` (Impact: 183.7), `resolveToUnqualified` (Impact: 26.7), `getDependencyTarget` (Impact: 17.2)

### 9. `internal/bundler/bundler.go` (GO) -> Cumulative Risk: **695.98**
- **Archetype:** `file_cluster_8` (Distance: 14.449 IQR)
- **Magnitude:** 1023.8 | **LOC:** 3532 | **CtrlFlow:** 81.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), Safety Score (99.5944%)
- **Heaviest Functions:** `preprocessInjectedFiles` (Impact: 99.9), `ScanBundle` (Impact: 85.3), `sanitizeFilePathForVirtualModulePath` (Impact: 28.1)

### 10. `scripts/decorator-tests.js` (JAVASCRIPT) -> Cumulative Risk: **685.92**
- **Archetype:** `file_cluster_8` (Distance: 13.027 IQR)
- **Magnitude:** 3193.18 | **LOC:** 5384 | **CtrlFlow:** 7.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), Tech Debt (99.9837%)
- **Heaviest Functions:** `__decorateElement` (Impact: 130.8), `assertEq` (Impact: 15.9), `assertEq` (Impact: 11.9)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `scripts/end-to-end-tests.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_4` (Drift: 15.318 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 6.073 IQR)
- **Top Global Matches:** file_cluster_4: 15.318, file_cluster_13: 15.628, file_cluster_11: 15.744
- **Magnitude:** 6473.76 | **LOC:** 9848 | **CtrlFlow:** 36.1% | **Authorship Centralization:** 83.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 19
- **Risk Profile:** Cognitive Load (98.4174%), Tech Debt (99.9958%)
**Top Internal Functions/Classes:**
  * `async` (Impact: 88.8 | O(2^N) | DB: 2)
  * `test` (Impact: 36.6 | O(N^3))
  * `test` (Impact: 29.5 | O(N^2) | DB: 2)
  * `test` (Impact: 22.0 | O(N^2) | DB: 14)
  * `test` (Impact: 21.4 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1606`, `structural_boundaries: 2844`, `args: 860`, `func_start: 1378`, `class_start: 130`
* *Risk/State:* `safety_bypasses: 102`, `high_risk_execution: 1`, `state_mutation: 1938`, `dead_code: 11`, `fragile_debt: 7`, `duplicate_logic: 244`
* *Architecture:* `io: 203`, `api: 482`, `concurrency: 2517`, `import: 413`
* *Defense:* `safety: 1051`, `test: 690`, `immutability_locks: 270`, `cleanup: 37`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.698
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` d, zen-observable,  Note: re-exporting prototype properties using, fs, shared, foo.js, index.mts, foo...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/linker/linker.go` (GO | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.076 IQR)
- **Top Global Matches:** file_cluster_8: 15.076, file_cluster_7: 15.099, file_cluster_13: 15.218
- **Magnitude:** 5147.04 | **LOC:** 7294 | **CtrlFlow:** 83.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 206
- **Risk Profile:** Cognitive Load (39.4763%), Tech Debt (13.3923%)
**Top Internal Functions/Classes:**
  * `convertStmtsForChunk` (Impact: 1104.7 | O(2^N) | DB: 206)
    * *Intent:* // Encode import-specific constraints in the dependency graph
  * `mangleLocalCSS` (Impact: 636.4 | O(N^2) | DB: 192)
  * `validateComposesFromProperties` (Impact: 446.5 | O(N^2) | DB: 175)
  * `maybeAppendLegalComments` (Impact: 213.7 | O(N^1) | DB: 81)
  * `Link` (Impact: 42.2 | O(2^N) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 732`, `structural_boundaries: 148`, `args: 37`, `func_start: 37`, `class_start: 18`
* *Risk/State:* `state_mutation: 2375`, `dead_code: 11`, `planned_debt: 2`, `fragile_debt: 1`, `duplicate_logic: 2`, `orphaned_logic: 3`
* *Architecture:* `api: 160`, `concurrency: 30`, `import: 1`
* *Defense:* `safety: 9`, `doc: 316`, `sync_locks: 5`, `immutability_locks: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.861
  * `Choke Point (Betweenness):` 0.000236 | `Ripple Effect (Closeness):` 0.005181
  * `Imports (Out-Degree: 21):` js_lexer, base64, helpers, runtime, path, js_printer, resolver, strings...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `internal/js_printer/js_printer.go` (GO | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.661 IQR)
- **Top Global Matches:** file_cluster_8: 13.661, file_cluster_7: 13.851, file_cluster_15: 14.063
- **Magnitude:** 4818.26 | **LOC:** 5026 | **CtrlFlow:** 89.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 222
- **Risk Profile:** Cognitive Load (47.7098%), Tech Debt (8.9969%)
**Top Internal Functions/Classes:**
  * `printBinding` (Impact: 3507.0 | O(2^N) | DB: 222)
  * `printUnquotedUTF16` (Impact: 185.3 | O(N^2) | DB: 80)
  * `printNumber` (Impact: 53.4 | O(N^1) | DB: 3)
  * `QuoteIdentifier` (Impact: 27.6 | O(N^1) | DB: 14)
  * `willPrintExprCommentsForAnyOf` (Impact: 10.2 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 572`, `structural_boundaries: 64`, `args: 32`, `func_start: 32`, `class_start: 1`
* *Risk/State:* `state_mutation: 983`, `dead_code: 1`, `orphaned_logic: 3`
* *Architecture:* `api: 12`, `import: 1`
* *Defense:* `doc: 83`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.814
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.006908
  * `Imports (Out-Degree: 8):` strings, strconv, ast, sourcemap, big, js_ast, helpers, bytes...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Makefile` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.034 IQR)
- **Top Global Matches:** file_cluster_8: 13.034, file_cluster_0: 13.221, file_cluster_11: 13.252
- **Magnitude:** 3567.08 | **LOC:** 1174 | **CtrlFlow:** 95.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (37.7802%), Tech Debt (12.2239%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 301`, `structural_boundaries: 14`, `func_start: 162`
* *Risk/State:* `state_mutation: 127`, `dead_code: 13`, `fragile_debt: 2`
* *Architecture:* `io: 117`, `api: 2`
* *Defense:* `test: 4`, `cleanup: 85`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.698
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/css_parser/css_parser.go` (GO | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.932 IQR)
- **Top Global Matches:** file_cluster_8: 13.932, file_cluster_7: 14.072, file_cluster_13: 14.276
- **Magnitude:** 3305.28 | **LOC:** 2487 | **CtrlFlow:** 81.0% | **Authorship Centralization:** 83.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 230
- **Risk Profile:** Cognitive Load (47.1684%), Tech Debt (8.9377%)
**Top Internal Functions/Classes:**
  * `parseListOfDeclarations` (Impact: 2472.3 | O(2^N) | DB: 230)
  * `Equal` (Impact: 25.7 | O(N^1) | DB: 4)
  * `OptionsFromConfig` (Impact: 8.0 | O(N^1) | DB: 2)
  * `Parse` (Impact: 3.9 | O(N^1) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 353`, `structural_boundaries: 83`, `args: 17`, `func_start: 17`, `class_start: 7`
* *Risk/State:* `state_mutation: 727`, `dead_code: 1`, `orphaned_logic: 2`
* *Architecture:* `api: 46`, `import: 1`
* *Defense:* `doc: 65`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.568
  * `Choke Point (Betweenness):` 0.000342 | `Ripple Effect (Closeness):` 0.01658
  * `Imports (Out-Degree: 9):` right-middle, s, strong, -ms-viewport, h4, col, li, i...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `internal/js_lexer/js_lexer.go` (GO | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.137 IQR)
- **Top Global Matches:** file_cluster_8: 14.137, file_cluster_7: 14.257, file_cluster_15: 14.4
- **Magnitude:** 3217.3 | **LOC:** 2666 | **CtrlFlow:** 92.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 140
- **Risk Profile:** Cognitive Load (48.1275%), Tech Debt (14.7461%)
**Top Internal Functions/Classes:**
  * `Next` (Impact: 816.5 | O(N^2) | DB: 140)
  * `parseNumericLiteralOrDot` (Impact: 536.0 | O(N^2) | DB: 132)
  * `NextInsideJSXElement` (Impact: 138.6 | O(N^1) | DB: 36)
  * `NextJSXElementChild` (Impact: 88.9 | O(N^2) | DB: 26)
  * `scanIdentifierWithEscapes` (Impact: 41.4 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 569`, `structural_boundaries: 48`, `args: 34`, `func_start: 34`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 1172`, `dead_code: 1`, `orphaned_logic: 12`
* *Architecture:* `api: 146`, `import: 1`
* *Defense:* `doc: 97`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.07
  * `Choke Point (Betweenness):` 0.001439 | `Ripple Effect (Closeness):` 0.048226
  * `Imports (Out-Degree: 7):` import, static, catch, const, private, protected, while, helpers...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `scripts/decorator-tests.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.027 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.529 IQR)
- **Top Global Matches:** file_cluster_8: 13.027, file_cluster_15: 13.23, file_cluster_4: 13.231
- **Magnitude:** 3193.18 | **LOC:** 5384 | **CtrlFlow:** 7.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (90.717%), Tech Debt (99.9837%)
**Top Internal Functions/Classes:**
  * `__decorateElement` (Impact: 130.8 | O(N^1) | DB: 7)
  * `assertEq` (Impact: 15.9 | O(2^N) | DB: 3)
  * `assertEq` (Impact: 11.9 | O(2^N) | DB: 3)
  * `assertEq` (Impact: 11.8 | O(2^N) | DB: 3)
  * `assertEq` (Impact: 11.8 | O(2^N) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 204`, `structural_boundaries: 2531`, `args: 1870`, `func_start: 1897`, `class_start: 131`
* *Risk/State:* `safety_bypasses: 51`, `state_mutation: 1616`, `duplicate_logic: 241`
* *Architecture:* `concurrency: 338`
* *Defense:* `safety: 158`, `test: 1`, `immutability_locks: 380`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.698
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/js-api-tests.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.34 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.502 IQR)
- **Top Global Matches:** file_cluster_4: 12.34, file_cluster_8: 12.856, file_cluster_13: 12.919
- **Magnitude:** 2999.98 | **LOC:** 8070 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 22
- **Risk Profile:** Cognitive Load (99.9648%), Tech Debt (95.5348%)
**Top Internal Functions/Classes:**
  * `reject` (Impact: 42.5 | O(2^N) | DB: 7)
  * `check` (Impact: 25.2 | O(N^3) | DB: 3)
  * `main` (Impact: 23.4 | O(N^1) | DB: 11)
  * `onRequest` (Impact: 12.1 | O(2^N) | DB: 16)
  * `onRequest` (Impact: 12.0 | O(2^N) | DB: 16)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 305`, `structural_boundaries: 1176`, `args: 341`, `func_start: 372`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 28`, `high_risk_execution: 3`, `state_mutation: 383`, `dead_code: 1`, `fragile_debt: 1`, `duplicate_logic: 25`, `orphaned_logic: 84`
* *Architecture:* `io: 592`, `api: 72`, `concurrency: 2115`, `import: 119`
* *Defense:* `safety: 218`, `test: 492`, `immutability_locks: 508`, `cleanup: 35`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.698
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` shared2, other, file.png, foo.js, foo.js, cjs, $chunk, foo.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/js_ast/js_ast_helpers.go` (GO | Tier 2 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.95 IQR)
- **Top Global Matches:** file_cluster_8: 13.95, file_cluster_7: 14.048, file_cluster_13: 14.148
- **Magnitude:** 2357.88 | **LOC:** 3017 | **CtrlFlow:** 69.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 105
- **Risk Profile:** Cognitive Load (48.7986%), Tech Debt (12.9651%)
**Top Internal Functions/Classes:**
  * `simplifyUnusedStringAdditionChain` (Impact: 1318.3 | O(2^N) | DB: 105)
  * `MangleIfExpr` (Impact: 277.6 | O(2^N) | DB: 48)
  * `ForEachIdentifierBinding` (Impact: 45.0 | O(2^N) | DB: 3)
  * `JoinWithLeftAssociativeOp` (Impact: 10.8 | O(N^1) | DB: 6)
  * `IsOptionalChain` (Impact: 10.6 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 367`, `structural_boundaries: 160`, `args: 19`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `state_mutation: 587`, `dead_code: 3`, `orphaned_logic: 5`
* *Architecture:* `api: 69`, `import: 1`
* *Defense:* `doc: 71`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.698
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` -Infinity, Infinity, helpers, true, strings, ast, object, boolean...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/css_ast/css_ast.go` (GO | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.841 IQR)
- **Top Global Matches:** file_cluster_8: 13.841, file_cluster_15: 13.94, file_cluster_7: 14.034
- **Magnitude:** 2321.64 | **LOC:** 1581 | **CtrlFlow:** 52.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 206
- **Risk Profile:** Cognitive Load (67.3072%), Tech Debt (14.3442%)
**Top Internal Functions/Classes:**
  * `CloneTokensWithImportRecords` (Impact: 1224.9 | O(2^N) | DB: 206)
  * `EqualIgnoringWhitespace` (Impact: 22.7 | O(N^1))
  * `NumberOrFractionForPercentage` (Impact: 18.4 | O(N^1) | DB: 2)
  * `HashTokens` (Impact: 18.1 | O(2^N) | DB: 5)
    * *Intent:* // This is necessary when comparing tokens between two different files
  * `CloneTokensWithoutImportRecords` (Impact: 16.5 | O(2^N) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 300`, `structural_boundaries: 273`, `args: 108`, `func_start: 108`, `class_start: 37`
* *Risk/State:* `state_mutation: 627`, `orphaned_logic: 8`
* *Architecture:* `api: 282`, `import: 1`
* *Defense:* `doc: 32`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 17.05
  * `Choke Point (Betweenness):` 0.001237 | `Ripple Effect (Closeness):` 0.131347
  * `Imports (Out-Degree: 4):` is, where, strings, global, strconv, ast, before, not...
  * `Imported By (In-Degree: 24):` (Excluded from Brief to save tokens)

### `pkg/api/api_impl.go` (GO | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.886 IQR)
- **Top Global Matches:** file_cluster_8: 13.886, file_cluster_7: 13.996, file_cluster_13: 14.143
- **Magnitude:** 2209.58 | **LOC:** 2566 | **CtrlFlow:** 70.9% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 179
- **Risk Profile:** Cognitive Load (38.6177%), Tech Debt (8.3336%)
**Top Internal Functions/Classes:**
  * `validatePathTemplate` (Impact: 1041.7 | O(2^N) | DB: 179)
  * `loadPlugins` (Impact: 193.7 | O(N^2) | DB: 86)
  * `validatePathsArray` (Impact: 10.9 | O(N^1) | DB: 5)
    * *Intent:* ////////////////////////////////////////////////////////////////////////////////
  * `onLoad` (Impact: 10.7 | O(N^1) | DB: 15)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 227`, `structural_boundaries: 93`, `args: 31`, `func_start: 31`, `class_start: 6`
* *Risk/State:* `state_mutation: 779`, `orphaned_logic: 1`
* *Architecture:* `api: 130`, `concurrency: 24`, `import: 1`
* *Defense:* `safety: 6`, `doc: 59`, `sync_locks: 11`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.698
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` js, cache, base64, helpers, regexp, path, resolver, strings...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/css_parser/css_parser_selector.go` (GO | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.525 IQR)
- **Top Global Matches:** file_cluster_8: 13.525, file_cluster_7: 13.69, file_cluster_13: 13.894
- **Magnitude:** 1939.18 | **LOC:** 998 | **CtrlFlow:** 79.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 205
- **Risk Profile:** Cognitive Load (39.5547%), Tech Debt (9.137%)
**Top Internal Functions/Classes:**
  * `mergeCompoundSelectors` (Impact: 1174.3 | O(2^N) | DB: 205)
  * `parseSelectorList` (Impact: 78.1 | O(N^1) | DB: 17)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 246`, `structural_boundaries: 63`, `args: 12`, `func_start: 12`, `class_start: 2`
* *Risk/State:* `state_mutation: 652`, `fragile_debt: 1`
* *Architecture:* `api: 20`, `import: 1`
* *Defense:* `doc: 46`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.698
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` is, where, strings, global, not, before, nth-last-of-type, 0...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/plugin-tests.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.756 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.322 IQR)
- **Top Global Matches:** file_cluster_4: 11.756, file_cluster_8: 11.954, file_cluster_13: 12.165
- **Magnitude:** 1772.62 | **LOC:** 3513 | **CtrlFlow:** 26.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 36
- **Risk Profile:** Cognitive Load (91.0193%), Tech Debt (99.9999%)
**Top Internal Functions/Classes:**
  * `setup` (Impact: 23.5 | O(N^3) | DB: 21)
  * `setup` (Impact: 22.0 | O(N^4) | DB: 36)
  * `main` (Impact: 20.3 | O(N^1) | DB: 11)
  * `setup` (Impact: 17.7 | O(N^5) | DB: 17)
  * `setup` (Impact: 17.7 | O(N^3) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 280`, `structural_boundaries: 765`, `args: 368`, `func_start: 224`
* *Risk/State:* `safety_bypasses: 55`, `state_mutation: 158`, `planned_debt: 3`, `duplicate_logic: 96`, `orphaned_logic: 88`
* *Architecture:* `io: 344`, `api: 92`, `concurrency: 730`, `import: 69`
* *Defense:* `safety: 130`, `test: 237`, `immutability_locks: 224`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.698
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` extern, import, esbuild, fib($n - 2) $args.path, plugin:used-true, test.wasm, path, fs...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/js_parser/js_parser_lower_class.go` (GO | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.77 IQR)
- **Top Global Matches:** file_cluster_8: 14.77, file_cluster_7: 14.837, file_cluster_13: 14.855
- **Magnitude:** 1667.32 | **LOC:** 2601 | **CtrlFlow:** 82.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 62
- **Risk Profile:** Cognitive Load (37.1863%), Tech Debt (17.287%)
**Top Internal Functions/Classes:**
  * `computeClassLoweringInfo` (Impact: 361.3 | O(2^N) | DB: 62)
  * `lowerSuperPropertyOrPrivateInAssign` (Impact: 116.5 | O(2^N) | DB: 24)
  * `insertStmtsAfterSuperCall` (Impact: 66.1 | O(N^1) | DB: 54)
  * `rewriteAutoAccessorToGetSet` (Impact: 57.6 | O(N^1) | DB: 32)
  * `finishAndGenerateCode` (Impact: 40.8 | O(N^1) | DB: 12)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 228`, `structural_boundaries: 47`, `args: 25`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 736`, `dead_code: 10`, `orphaned_logic: 8`
* *Architecture:* `api: 70`, `import: 1`
* *Defense:* `doc: 74`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.698
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` ast, js_ast, helpers, compat, config, fmt, logger
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pkg/cli/cli_impl.go` (GO | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.753 IQR)
- **Top Global Matches:** file_cluster_8: 14.753, file_cluster_7: 15.001, file_cluster_13: 15.026
- **Magnitude:** 1639.26 | **LOC:** 1565 | **CtrlFlow:** 78.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 31
- **Risk Profile:** Cognitive Load (56.0022%), Tech Debt (8.7936%)
**Top Internal Functions/Classes:**
  * `parseServeOptionsImpl` (Impact: 51.4 | O(N^1) | DB: 31)
    * *Intent:* // This should already have been checked above
  * `serveImpl` (Impact: 29.0 | O(N^1) | DB: 14)
    * *Intent:* // Write the metafile to the file system
  * `parseTargets` (Impact: 23.4 | O(N^1) | DB: 14)
  * `filterAnalyzeFlags` (Impact: 21.1 | O(N^1) | DB: 8)
  * `parseOptionsForRun` (Impact: 17.5 | O(N^1) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 445`, `structural_boundaries: 125`, `args: 10`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 1415`, `dead_code: 1`, `orphaned_logic: 2`
* *Architecture:* `api: 22`, `concurrency: 6`, `import: 1`
* *Defense:* `safety: 42`, `doc: 39`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.698
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` resolve-extensions, reserve-props, debugger, conditions, es2018, preserve, logger, keep-names...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/resolver/resolver.go` (GO | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.204 IQR)
- **Top Global Matches:** file_cluster_8: 14.204, file_cluster_7: 14.295, file_cluster_13: 14.443
- **Magnitude:** 1468.86 | **LOC:** 2973 | **CtrlFlow:** 76.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 94
- **Risk Profile:** Cognitive Load (39.9306%), Tech Debt (22.8639%)
**Top Internal Functions/Classes:**
  * `Resolve` (Impact: 386.0 | O(N^2) | DB: 94)
  * `loadAsMainField` (Impact: 182.2 | O(N^1) | DB: 64)
  * `loadAsDirectory` (Impact: 21.2 | O(N^1) | DB: 6)
    * *Intent:* // Check the "browser" map
  * `loadAsIndexWithBrowserRemapping` (Impact: 13.3 | O(N^1) | DB: 6)
  * `loadAsFileOrDirectory` (Impact: 13.1 | O(N^1) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 342`, `structural_boundaries: 104`, `args: 15`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `state_mutation: 785`, `dead_code: 3`, `fragile_debt: 3`, `orphaned_logic: 4`
* *Architecture:* `api: 14`, `import: 1`
* *Defense:* `safety: 7`, `doc: 125`, `sync_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.305
  * `Choke Point (Betweenness):` 0.000396 | `Ripple Effect (Closeness):` 0.025907
  * `Imports (Out-Degree: 9):` _tls_wrap, async_hooks, _stream_passthrough, constants, querystring, cache, web, types...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `internal/js_parser/ts_parser.go` (GO | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.5 IQR)
- **Top Global Matches:** file_cluster_8: 13.5, file_cluster_7: 13.612, file_cluster_11: 13.714
- **Magnitude:** 1438.72 | **LOC:** 2087 | **CtrlFlow:** 84.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 27
- **Risk Profile:** Cognitive Load (38.3795%), Tech Debt (22.9096%)
**Top Internal Functions/Classes:**
  * `skipTypeScriptTypeWithFlags` (Impact: 401.5 | O(2^N) | DB: 4)
    * *Intent:* // "{1: y}"
  * `skipTypeScriptTypeParameters` (Impact: 89.1 | O(N^1) | DB: 19)
  * `skipTypeScriptObjectType` (Impact: 69.7 | O(N^1) | DB: 3)
  * `generateClosureForTypeScriptNamespaceOrE` (Impact: 69.5 | O(N^1) | DB: 21)
  * `tsIsStartOfExpression` (Impact: 65.2 | O(N^1) | DB: 20)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 296`, `structural_boundaries: 56`, `args: 19`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `state_mutation: 412`, `dead_code: 9`, `planned_debt: 2`, `fragile_debt: 1`, `orphaned_logic: 6`
* *Architecture:* `api: 68`
* *Defense:* `safety: 5`, `doc: 72`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.698
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` js_lexer, never, helpers, any, strings, ast, abstract, object...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/css_parser/css_reduce_calc.go` (GO | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.694 IQR)
- **Top Global Matches:** file_cluster_8: 13.694, file_cluster_7: 13.828, file_cluster_15: 13.93
- **Magnitude:** 1244.32 | **LOC:** 606 | **CtrlFlow:** 71.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 47
- **Risk Profile:** Cognitive Load (39.0572%), Tech Debt (98.1014%)
**Top Internal Functions/Classes:**
  * `tryToParseCalcTerm` (Impact: 294.8 | O(2^N) | DB: 47)
  * `partiallySimplify` (Impact: 115.8 | O(2^N) | DB: 29)
  * `convertToToken` (Impact: 92.3 | O(2^N) | DB: 28)
  * `partiallySimplify` (Impact: 55.9 | O(2^N) | DB: 19)
  * `convertToToken` (Impact: 41.4 | O(2^N) | DB: 12)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 153`, `structural_boundaries: 61`, `args: 15`, `func_start: 15`, `class_start: 8`
* *Risk/State:* `state_mutation: 483`, `duplicate_logic: 12`, `orphaned_logic: 1`
* *Architecture:* `api: 44`, `import: 1`
* *Defense:* `safety: 1`, `doc: 34`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.698
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` strings, strconv, css_lexer, css_ast, math, fmt, logger
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/css_parser/css_decls_color.go` (GO | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.598 IQR)
- **Top Global Matches:** file_cluster_8: 13.598, file_cluster_7: 13.942, file_cluster_13: 14.117
- **Magnitude:** 1215.04 | **LOC:** 939 | **CtrlFlow:** 78.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 83
- **Risk Profile:** Cognitive Load (82.6437%), Tech Debt (9.5296%)
**Top Internal Functions/Classes:**
  * `parseColor` (Impact: 314.2 | O(N^2) | DB: 83)
  * `lowerAndMinifyColor` (Impact: 114.5 | O(N^1) | DB: 34)
    * *Intent:* // Convert newer color syntax to older color syntax for older browsers
  * `tryToGenerateColor` (Impact: 45.1 | O(N^1) | DB: 27)
  * `looksLikeColor` (Impact: 23.8 | O(N^1) | DB: 2)
  * `degreesForAngle` (Impact: 23.1 | O(N^1) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 241`, `structural_boundaries: 65`, `args: 22`, `func_start: 22`, `class_start: 1`
* *Risk/State:* `state_mutation: 556`, `orphaned_logic: 2`
* *Architecture:* `import: 1`
* *Defense:* `doc: 10`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.698
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` lightseagreen, oklab, lemonchiffon, lavenderblush, turquoise, aquamarine, hsl, silver...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/js_parser/js_parser_lower.go` (GO | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_11` (Drift: 15.218 IQR)
- **Top Global Matches:** file_cluster_11: 15.218, file_cluster_13: 15.263, file_cluster_0: 15.287
- **Magnitude:** 1106.82 | **LOC:** 2133 | **CtrlFlow:** 79.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 130
- **Risk Profile:** Cognitive Load (46.9062%), Tech Debt (24.898%)
**Top Internal Functions/Classes:**
  * `lowerFunction` (Impact: 388.8 | O(N^1) | DB: 130)
  * `markSyntaxFeature` (Impact: 58.8 | O(N^1) | DB: 20)
  * `markStrictModeFeature` (Impact: 40.5 | O(N^1) | DB: 14)
  * `whyStrictMode` (Impact: 21.2 | O(N^1) | DB: 9)
  * `markAsyncFn` (Impact: 5.9 | O(N^1) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 171`, `structural_boundaries: 44`, `args: 15`, `func_start: 15`
* *Risk/State:* `state_mutation: 504`, `dead_code: 11`, `planned_debt: 1`, `orphaned_logic: 5`
* *Architecture:* `api: 61`, `import: 1`
* *Defense:* `doc: 47`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.698
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` ast, js_ast, helpers, compat, config, fmt, logger
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/resolver/package_json.go` (GO | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.129 IQR)
- **Top Global Matches:** file_cluster_8: 13.129, file_cluster_7: 13.281, file_cluster_13: 13.476
- **Magnitude:** 1081.26 | **LOC:** 1463 | **CtrlFlow:** 68.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 41
- **Risk Profile:** Cognitive Load (38.3312%), Tech Debt (40.2223%)
**Top Internal Functions/Classes:**
  * `parseImportsExportsMap` (Impact: 166.9 | O(N^2) | DB: 41)
  * `esmPackageTargetReverseResolve` (Impact: 140.7 | O(2^N) | DB: 10)
  * `checkBrowserMap` (Impact: 95.5 | O(N^1) | DB: 27)
  * `parsePackageJSON` (Impact: 48.0 | O(N^1) | DB: 21)
  * `globstarToEscapedRegexp` (Impact: 23.9 | O(N^1) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 212`, `structural_boundaries: 98`, `args: 14`, `func_start: 14`, `class_start: 6`
* *Risk/State:* `state_mutation: 476`, `dead_code: 1`, `fragile_debt: 2`, `orphaned_logic: 7`
* *Architecture:* `api: 18`, `import: 1`
* *Defense:* `safety: 1`, `doc: 64`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.698
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` import, commonjs, js_lexer, strings, require, js_parser, module, js_ast...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/css_printer/css_printer.go` (GO | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.273 IQR)
- **Top Global Matches:** file_cluster_8: 13.273, file_cluster_7: 13.503, file_cluster_13: 13.641
- **Magnitude:** 1037.68 | **LOC:** 1324 | **CtrlFlow:** 89.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 30
- **Risk Profile:** Cognitive Load (47.5517%), Tech Debt (10.3629%)
**Top Internal Functions/Classes:**
  * `printTokens` (Impact: 209.0 | O(2^N) | DB: 25)
  * `printIdent` (Impact: 87.6 | O(N^1) | DB: 19)
  * `printQuotedWithQuote` (Impact: 61.9 | O(N^1) | DB: 30)
  * `printWithEscape` (Impact: 55.6 | O(N^1) | DB: 18)
  * `printRule` (Impact: 47.0 | O(N^1) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 233`, `structural_boundaries: 28`, `args: 18`, `func_start: 18`, `class_start: 3`
* *Risk/State:* `state_mutation: 392`, `dead_code: 2`, `orphaned_logic: 2`
* *Architecture:* `api: 7`, `import: 1`
* *Defense:* `doc: 25`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.814
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.006908
  * `Imports (Out-Degree: 8):` strings, linear-gradient, sourcemap, ast, repeating-linear-gradient, matrix, matrix3d, helpers...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `internal/bundler/bundler.go` (GO | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.449 IQR)
- **Top Global Matches:** file_cluster_8: 14.449, file_cluster_7: 14.549, file_cluster_4: 14.572
- **Magnitude:** 1023.8 | **LOC:** 3532 | **CtrlFlow:** 81.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 55
- **Risk Profile:** Cognitive Load (43.8904%), Tech Debt (12.602%)
**Top Internal Functions/Classes:**
  * `preprocessInjectedFiles` (Impact: 99.9 | O(N^1) | DB: 55)
  * `ScanBundle` (Impact: 85.3 | O(N^1) | DB: 30)
  * `sanitizeFilePathForVirtualModulePath` (Impact: 28.1 | O(N^1) | DB: 5)
    * *Intent:* // Support data URLs
  * `allocateSourceIndex` (Impact: 6.1 | O(N^1) | DB: 5)
  * `allocateGlobSourceIndex` (Impact: 6.1 | O(N^1) | DB: 5)
    * *Intent:* // Failed imports inside a try/catch are silently turned into // external imports instead of causing...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 188`, `structural_boundaries: 42`, `args: 6`, `func_start: 6`, `class_start: 5`
* *Risk/State:* `state_mutation: 697`, `orphaned_logic: 4`
* *Architecture:* `io: 1`, `api: 31`, `concurrency: 54`, `import: 1`
* *Defense:* `safety: 6`, `doc: 77`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.977
  * `Choke Point (Betweenness):` 0.000128 | `Ripple Effect (Closeness):` 0.010363
  * `Imports (Out-Degree: 14):` .module.css, js_lexer, cache, base64, , helpers, runtime, .cjs...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `internal/runtime/runtime.go` (GO | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.292 IQR)
- **Top Global Matches:** file_cluster_8: 14.292, file_cluster_7: 14.49, file_cluster_13: 14.667
- **Magnitude:** 760.18 | **LOC:** 612 | **CtrlFlow:** 76.1% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(N) | **DB Complexity:** 0
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
- **Algorithmic:** O(N) | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (9.9481%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `EnsureValidIdentifier` (Impact: 29.1 | O(N^1) | DB: 9)
    * *Intent:* // This object represents all of these types of import statements: // // import 'path' // import {it...
  * `ConstValueToExpr` (Impact: 15.0 | O(N^1))
  * `HasSameFlagsAs` (Impact: 10.1 | O(N^1))
  * `HasSameFlagsAs` (Impact: 7.6 | O(N^1))
  * `BinaryAssignTarget` (Impact: 7.2 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 185`, `args: 59`, `func_start: 59`, `class_start: 66`
* *Risk/State:* `state_mutation: 75`, `dead_code: 4`, `duplicate_logic: 46`, `orphaned_logic: 11`
* *Architecture:* `api: 430`, `import: 1`
* *Defense:* `doc: 106`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 14.338
  * `Choke Point (Betweenness):` 0.000211 | `Ripple Effect (Closeness):` 0.116062
  * `Imports (Out-Degree: 2):` strconv, ast, logger, _
  * `Imported By (In-Degree: 21):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `internal/js_parser/js_parser_lower.go` (GO) | Magnitude: 1106.82 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 554, state_mutation: 504, encapsulation: 179, branch: 171

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `internal/logger/logger_other.go` (GO) | Magnitude: 6.98 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 3, args: 2, func_start: 2, api: 2
- `internal/helpers/glob.go` (GO) | Magnitude: 37.36 | Delta: **0.057 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 19, state_mutation: 16, api: 8, structural_boundaries: 6
- `internal/logger/logger_darwin.go` (GO) | Magnitude: 35.12 | Delta: **0.095 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 24, indent_tabs: 13, encapsulation: 7, explicit_casts: 4
- `internal/logger/logger_linux.go` (GO) | Magnitude: 35.12 | Delta: **0.095 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 24, indent_tabs: 13, encapsulation: 7, explicit_casts: 4
- `pkg/cli/cli.go` (GO) | Magnitude: 38.5 | Delta: **0.104 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 18, indent_tabs: 17, doc: 10, structural_boundaries: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `internal/ast/ast.go` (GO) | Magnitude: 414.78 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 231, api: 126, state_mutation: 117, structural_boundaries: 67

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `scripts/terser-tests.js` (JAVASCRIPT) | Magnitude: 318.08 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 212, state_mutation: 69, branch: 58, structural_boundaries: 51
- `compat-table/src/css_table.ts` (TYPESCRIPT) | Magnitude: 9.13 | Delta: **0.331 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 39, indent_spaces: 34, state_mutation: 28, args: 23
- `compat-table/src/js_table.ts` (TYPESCRIPT) | Magnitude: 8.33 | Delta: **0.545 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 41, indent_spaces: 39, state_mutation: 28, args: 24

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `pkg/api/watcher.go` (GO) | Magnitude: 147.72 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: state_mutation: 88, indent_tabs: 78, branch: 21, encapsulation: 21
- `internal/fs/fs.go` (GO) | Magnitude: 105.6 | Delta: **0.056 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 51, state_mutation: 34, structural_boundaries: 20, doc: 15
- `scripts/uglify-tests.js` (JAVASCRIPT) | Magnitude: 76.16 | Delta: **0.097 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 70, state_mutation: 20, structural_boundaries: 18, branch: 14
- `scripts/browser/index.html` (HTML) | Magnitude: 476.08 | Delta: **0.178 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 371, structural_boundaries: 84, concurrency: 76, func_start: 67
- `scripts/destructuring-fuzzer.js` (JAVASCRIPT) | Magnitude: 584.42 | Delta: **0.18 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 291, state_mutation: 269, structural_boundaries: 164, branch: 68

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `internal/fs/fs_real.go` (GO) | Magnitude: 636.3 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 306, state_mutation: 256, encapsulation: 110, branch: 77
- `internal/linker/linker.go` (GO) | Magnitude: 5147.04 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: state_mutation: 2375, indent_tabs: 2367, encapsulation: 910, branch: 732
- `internal/helpers/dataurl.go` (GO) | Magnitude: 53.38 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 29, indent_tabs: 27, encapsulation: 10, branch: 9
- `compat-table/src/index.ts` (TYPESCRIPT) | Magnitude: 12.29 | Delta: **0.04 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 224, structural_boundaries: 49, immutability_locks: 46, branch: 36
- `internal/cache/cache_fs.go` (GO) | Magnitude: 24.44 | Delta: **0.04 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 18, state_mutation: 9, structural_boundaries: 6, branch: 5

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `scripts/end-to-end-tests.js` -> **Evan Wallace** (83.3% isolated ownership) | Magnitude: 6473.76
- `internal/linker/linker.go` -> **Evan Wallace** (100.0% isolated ownership) | Magnitude: 5147.04
- `internal/js_printer/js_printer.go` -> **Evan Wallace** (100.0% isolated ownership) | Magnitude: 4818.26
- `Makefile` -> **Evan Wallace** (100.0% isolated ownership) | Magnitude: 3567.08
- `internal/css_parser/css_parser.go` -> **Evan Wallace** (83.3% isolated ownership) | Magnitude: 3305.28

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
- `internal/css_ast/css_ast.go` -> **Severity: 12.649** (Embedded: 0.1313 * Error Risk: 96.3052%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `internal/helpers/strings.go` -> **Severity: 16692.518** (Blast Radius: 172.466 * Doc Risk: 96.7873%)
- `internal/ast/ast.go` -> **Severity: 3634.6** (Blast Radius: 36.346 * Doc Risk: 100.0%)
- `internal/helpers/path.go` -> **Severity: 2269.466** (Blast Radius: 23.025 * Doc Risk: 98.5653%)
- `internal/css_ast/css_ast.go` -> **Severity: 1705.0** (Blast Radius: 17.05 * Doc Risk: 100.0%)
- `internal/logger/logger.go` -> **Severity: 1458.236** (Blast Radius: 81.555 * Doc Risk: 17.8804%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
