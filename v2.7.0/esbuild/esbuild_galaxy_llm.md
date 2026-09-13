# ARCHITECTURAL_BRIEF: esbuild
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/evanw/esbuild.git` |
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
| Total Artifacts | 348 |
| Analyzed Artifacts (Scanned) | 314 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 34 |
| Total LOC | 146852 |
| Volatility Index | 0.003 |
| % Scanned of codebase = | 90.2% |
| Dominant Lang | GO |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4418 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2001 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 1.3% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.0031 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 19 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| GO | 144 | 102991 | 45.9% |
| PLAINTEXT | 55 | 0 | 17.5% |
| MARKDOWN | 45 | 0 | 14.3% |
| JAVASCRIPT | 24 | 29197 | 7.6% |
| TYPESCRIPT | 20 | 9072 | 6.4% |
| JSON | 13 | 3242 | 4.1% |
| XML | 5 | 0 | 1.6% |
| HTML | 5 | 1456 | 1.6% |
| MAKEFILE | 1 | 804 | 0.3% |
| SHELL | 1 | 18 | 0.3% |
| CSS | 1 | 72 | 0.3% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 214 | 68.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 100 | 31.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 34*

**Composition by Extension & Reason:**
- `.go`: 1x Excluded (Machine-Generated Source Code Signature: 423 LOC), 1x Excluded (Machine-Generated Source Code Signature: 938 LOC), 1x Excluded (Machine-Generated Source Code Signature: 432 LOC)
- `no_extension`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 5x Excluded (Explicitly Denied Extension: '.png')
- `.yml`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 1x Excluded (Massive Static Asset Blob: 5304 LOC), 1x Excluded (Static Asset Blob without Intent: 2344 LOC)
- `.mod`: 1x Unsupported Format (.mod)
- `.sum`: 1x Excluded (Unsupported Extension: '.sum')
- `.version`: 1x Excluded (Unsupported Extension: '.version')
- `.ts`: 1x Unsupported Format (.undeterminable)
- `.js`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.lock`: 1x Excluded (Unsupported Extension: '.lock')
- `.conf`: 1x Excluded (Unsupported Extension: '.conf')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 30.4 | 25.9 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.9 | 57.7 | 68.9 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 35.2 | 22.5 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 27.8 | 2.3 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 11.2 | 3.6 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 13.9 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 62.9 | 99.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 30.7 | 1.6 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 87.4 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 8.7 | 0.9 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 65.0 | 6.1 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 76.1 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 4070 | 119 | 27 | `internal/js_ast/js_ast_helpers.go` |
| cleanup | 214 | 23 | 0 | `Makefile` |
| guards | 5284 | 161 | 31 | `scripts/end-to-end-tests.js` |
| danger | 2643 | 79 | 8 | `scripts/end-to-end-tests.js` |
| concurrency | 3957 | 64 | 12 | `scripts/js-api-tests.js` |
| connectivity | 6068 | 144 | 33 | `internal/js_ast/js_ast.go` |
| io | 1890 | 46 | 4 | `scripts/js-api-tests.js` |
| crypto | 2 | 2 | 0 | `scripts/esbuild.js` |
| ipc | 202 | 32 | 1 | `lib/npm/node.ts` |
| time | 109 | 29 | 0 | `scripts/js-api-tests.js` |
| serialization | 237 | 26 | 0 | `scripts/js-api-tests.js` |
| regex | 176 | 34 | 1 | `scripts/js-api-tests.js` |
| events | 200 | 23 | 0 | `scripts/js-api-tests.js` |
| tests | 3559 | 52 | 3 | `scripts/js-api-tests.js` |
| docs | 4865 | 125 | 44 | `internal/linker/linker.go` |
| debt | 1862 | 70 | 4 | `scripts/decorator-tests.js` |
| mutation | 27415 | 174 | 185 | `scripts/end-to-end-tests.js` |
| dead_code | 2449 | 147 | 14 | `scripts/js-api-tests.js` |
| credential | 11 | 5 | 0 | `dl.sh` |
| threat | 315 | 25 | 0 | `scripts/decorator-tests.js` |
| ml_ai | 86 | 14 | 0 | `internal/js_ast/js_ast_helpers.go` |
| ui | 40 | 10 | 0 | `scripts/try.html` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.2**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `scripts/js-api-tests.js` (Hits: 783)
- `scripts/plugin-tests.js` (Hits: 180)
- `scripts/end-to-end-tests.js` (Hits: 171)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **strings.go** (`internal/helpers/strings.go`) — 71 inbound connections
2. **logger.go** (`internal/logger/logger.go`) — 61 inbound connections
3. **config.go** (`internal/config/config.go`) — 37 inbound connections
4. **fs.go** (`internal/fs/fs.go`) — 36 inbound connections
5. **compat.go** (`internal/compat/compat.go`) — 33 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **bundler_default_test.go** (`internal/bundler_tests/bundler_default_test.go`) — 486 outbound dependencies
2. **bundler_css_test.go** (`internal/bundler_tests/bundler_css_test.go`) — 340 outbound dependencies
3. **css_decl_table.go** (`internal/css_ast/css_decl_table.go`) — 331 outbound dependencies
4. **tables.go** (`internal/js_lexer/tables.go`) — 253 outbound dependencies
5. **bundler_dce_test.go** (`internal/bundler_tests/bundler_dce_test.go`) — 202 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `printExpr` (@ `internal/js_printer/js_printer.go`) -> Impact: **923.4** | LOC: 1348
- `parseOptionsImpl` (@ `pkg/cli/cli_impl.go`) -> Impact: **795.4** | LOC: 926
- `TestMangleIf` (@ `internal/js_parser/js_parser_test.go`) -> Impact: **662.0** | LOC: 257
- `printStmt` (@ `internal/js_printer/js_printer.go`) -> Impact: **359.1** | LOC: 809
- `finalizeImportsExportsResult` (@ `internal/resolver/resolver.go`) -> Impact: **274.2** | LOC: 287
- `ParseTSConfigJSON` (@ `internal/resolver/tsconfig_json.go`) -> Impact: **246.8** | LOC: 298
- `TestFor` (@ `internal/js_parser/js_parser_test.go`) -> Impact: **245.4** | LOC: 127
- `Next` (@ `internal/js_lexer/js_lexer.go`) -> Impact: **241.6** | LOC: 632
- `parseAtRule` (@ `internal/css_parser/css_parser.go`) -> Impact: **240.3** | LOC: 591
- `printRule` (@ `internal/css_printer/css_printer.go`) -> Impact: **235.4** | LOC: 308

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `scripts` | 28 | 27735.4 | 62.99% | 27.76% |
| `internal/js_parser` | 10 | 11875.84 | 36.81% | 40.95% |
| `internal/css_parser` | 21 | 8000.54 | 37.87% | 25.32% |
| `internal/bundler_tests` | 15 | 7862.4 | 7.74% | 75.42% |
| `internal/linker` | 2 | 4627.12 | 44.01% | 4.39% |
| `internal/resolver` | 7 | 4355.26 | 27.99% | 20.7% |
| `internal/js_printer` | 2 | 4222.6 | 30.87% | 52.51% |
| `internal/js_ast` | 4 | 3315.34 | 12.45% | 39.21% |
| `lib/shared` | 5 | 3181.84 | 70.8% | 6.38% |
| `pkg/api` | 8 | 3143.3 | 14.84% | 37.92% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `scripts/decorator-tests.ts` -> **100.0%** Exposure
- `scripts/decorator-tests.js` -> **100.0%** Exposure
- `internal/fs/iswin_wasm.go` -> **99.9965%** Exposure
- `npm/esbuild-wasm/bin/esbuild` -> **99.9963%** Exposure
- `internal/helpers/bitset.go` -> **99.9665%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `cmd/esbuild/stdio_protocol.go` -> **100.0%** Exposure
- `internal/bundler_tests/bundler_test.go` -> **100.0%** Exposure
- `internal/config/config.go` -> **100.0%** Exposure
- `internal/css_parser/css_decls.go` -> **100.0%** Exposure
- `internal/css_parser/css_decls_box_shadow.go` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `scripts/decorator-tests.js` -> **0** Orphaned Functions | **475** Duplicates
- `scripts/js-api-tests.js` -> **322** Orphaned Functions | **9** Duplicates
- `internal/bundler_tests/bundler_default_test.go` -> **301** Orphaned Functions | **0** Duplicates
- `scripts/decorator-tests.ts` -> **0** Orphaned Functions | **210** Duplicates
- `internal/js_parser/js_parser_test.go` -> **130** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `4225` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `lib/npm/browser.ts` (TYPESCRIPT) -> Cumulative Risk: **787.32**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 193.54 | **LOC:** 230 | **CtrlFlow:** 13.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (97.8187%)
- **Heaviest Functions:** `initialize` (Impact: 9.3), `startRunningService` (Impact: 7.0), `onmessage` (Impact: 6.1)

### 2. `lib/shared/common.ts` (TYPESCRIPT) -> Cumulative Risk: **785.83**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 2364.72 | **LOC:** 1879 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `buildOrContextImpl` (Impact: 196.2), `flagsForBuildOptions` (Impact: 160.2), `buildOrContextContinue` (Impact: 100.5)

### 3. `lib/deno/wasm.ts` (TYPESCRIPT) -> Cumulative Risk: **781.28**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 185.66 | **LOC:** 204 | **CtrlFlow:** 13.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (97.7914%)
- **Heaviest Functions:** `startRunningService` (Impact: 8.8), `initialize` (Impact: 6.4), `onmessage` (Impact: 6.1)

### 4. `lib/npm/node.ts` (TYPESCRIPT) -> Cumulative Risk: **762.64**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 337.88 | **LOC:** 636 | **CtrlFlow:** 18.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (98.3947%), State Flux (97.1417%)
- **Heaviest Functions:** `extractProperties` (Impact: 22.3), `esbuildCommandAndArgs` (Impact: 11.6), `transformSync` (Impact: 11.1)

### 5. `lib/deno/mod.ts` (TYPESCRIPT) -> Cumulative Risk: **735.87**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 328.08 | **LOC:** 425 | **CtrlFlow:** 17.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.4281%)
- **Heaviest Functions:** `getCachePath` (Impact: 21.5), `extractFileFromTarGzip` (Impact: 11.4), `spawnNew` (Impact: 11.1)

### 6. `scripts/esbuild.js` (JAVASCRIPT) -> Cumulative Risk: **717.62**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 245.18 | **LOC:** 409 | **CtrlFlow:** 9.5% | **Authorship Centralization:** 85.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9999%), Concurrency (99.6924%)
- **Heaviest Functions:** `buildWasmLib` (Impact: 17.7), `generateWorkerCode` (Impact: 13.3), `updateVersionGo` (Impact: 13.2)

### 7. `pkg/api/serve_other.go` (GO) -> Cumulative Risk: **706.12**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 847.7 | **LOC:** 1059 | **CtrlFlow:** 26.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9992%), Concurrency (99.118%), Tech Debt (98.5551%)
- **Heaviest Functions:** `ServeHTTP` (Impact: 152.8), `Serve` (Impact: 94.8), `broadcastBuildResult` (Impact: 46.1)

### 8. `lib/shared/worker.ts` (TYPESCRIPT) -> Cumulative Risk: **689.61**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 112.84 | **LOC:** 103 | **CtrlFlow:** 23.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `read` (Impact: 19.0), `tryToInstantiateModule` (Impact: 11.3), `writeSync` (Impact: 11.2)

### 9. `scripts/decorator-tests.js` (JAVASCRIPT) -> Cumulative Risk: **681.92**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 3529.98 | **LOC:** 5384 | **CtrlFlow:** 3.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.9957%)
- **Heaviest Functions:** `__decorateElement` (Impact: 130.9), `__runInitializers` (Impact: 9.2), `prettyPrint` (Impact: 7.5)

### 10. `scripts/decorator-tests.ts` (TYPESCRIPT) -> Cumulative Risk: **669.94**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 2493.38 | **LOC:** 3913 | **CtrlFlow:** 3.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.996%)
- **Heaviest Functions:** `prettyPrint` (Impact: 7.5), `capture` (Impact: 7.4), `capture` (Impact: 6.9)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `scripts/end-to-end-tests.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 11309.86 | **LOC:** 9848 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 83.3%
- **Risk Profile:** Cognitive Load (99.6378%), Tech Debt (9.4259%)
**Top Internal Functions/Classes:**
  * `test` (Impact: 147.2)
  * `quote` (Impact: 84.5)
    * *Intent:* // Use the shell to set the working directory instead of using node's // "child_process" module. For...
  * `waitForCondition` (Impact: 16.9)
  * `patchString` (Impact: 11.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 37 instances
* *Amplified Rce:* 10 instances
* *Amplified Race Conditions:* 534 instances
* *Amplified Cascading Flux:* 2068 instances
* *High Risk Execution (weighted view):* 28
* *Concurrency (weighted view):* 3536
* *Sec Tainted Injection (weighted view):* 10
* *State Mutation (weighted view):* 6699
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1817`, `structural_boundaries: 3508`, `args: 1034`, `func_start: 675`, `class_start: 144`
* *Risk/State:* `safety_bypasses: 118`, `high_risk_execution: 65`, `state_mutation: 2563`, `dead_code: 13`, `planned_debt: 1`, `fragile_debt: 8`, `unreferenced_by_name: 1`
* *Architecture:* `io: 171`, `api: 635`, `concurrency: 866`, `import: 547`
* *Defense:* `safety: 1435`, `test: 819`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.702
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` #pkg, bar.js, , common, qux, , file.js, File1.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/js_parser/js_parser_test.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 4549.48 | **LOC:** 6956 | **CtrlFlow:** 38.0% | **Authorship Centralization:** 91.7%
- **Risk Profile:** Cognitive Load (43.2354%), Tech Debt (73.3341%)
**Top Internal Functions/Classes:**
  * `TestMangleIf` (Impact: 662.0)
  * `TestFor` (Impact: 245.4)
  * `TestSwitch` (Impact: 200.8)
  * `TestMangleSwitch` (Impact: 161.5)
  * `TestMangleBooleanWithSideEffects` (Impact: 135.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 90 instances
* *State Mutation (weighted view):* 612
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2237`, `structural_boundaries: 1510`, `args: 150`, `func_start: 150`, `class_start: 1`
* *Risk/State:* `state_mutation: 432`, `dead_code: 1`, `fragile_debt: 5`, `unreferenced_by_name: 130`
* *Architecture:* `api: 135`, `import: 1`
* *Defense:* `doc: 154`, `test: 137`, `immutability_locks: 88`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.702
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` fmt, ast, compat, config, helpers, js_ast, js_printer, logger...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/linker/linker.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 4538.12 | **LOC:** 7294 | **CtrlFlow:** 24.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (36.8087%), Tech Debt (8.775%)
**Top Internal Functions/Classes:**
  * `scanImportsAndExports` (Impact: 189.8)
  * `generateCodeForFileInChunkJS` (Impact: 187.7)
  * `generateChunkJS` (Impact: 155.1)
  * `convertStmtsForChunk` (Impact: 141.6)
  * `generateChunkCSS` (Impact: 140.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 616 instances
* *Concurrency (weighted view):* 24
* *State Mutation (weighted view):* 1945
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1202`, `structural_boundaries: 595`, `args: 75`, `func_start: 75`, `class_start: 27`
* *Risk/State:* `high_risk_execution: 11`, `state_mutation: 713`, `dead_code: 30`, `planned_debt: 5`, `fragile_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 15`, `concurrency: 9`, `import: 1`
* *Defense:* `safety: 1`, `doc: 631`, `sync_locks: 5`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.966
  * `Choke Point (Betweenness):` 0.000257 | `Ripple Effect (Closeness):` 0.00639
  * `Imports (Out-Degree: 21):` bytes, base64, binary, fmt, ast, bundler, compat, config...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `scripts/js-api-tests.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 4213.62 | **LOC:** 8070 | **CtrlFlow:** 4.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (93.3704%), Tech Debt (99.3371%)
**Top Internal Functions/Classes:**
  * `check` (Impact: 35.9)
  * `regExpFeatures` (Impact: 25.9)
  * `singleUseExpressionSubstitution` (Impact: 24.8)
  * `check` (Impact: 23.2)
  * `registerClassPrivateTests` (Impact: 21.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 31 instances
* *Amplified Rce:* 11 instances
* *Amplified Race Conditions:* 103 instances
* *Amplified Cascading Flux:* 57 instances
* *High Risk Execution (weighted view):* 26
* *Concurrency (weighted view):* 2059
* *Sec Tainted Injection (weighted view):* 14
* *State Mutation (weighted view):* 236
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 344`, `structural_boundaries: 2243`, `args: 732`, `func_start: 531`, `class_start: 23`
* *Risk/State:* `safety_bypasses: 77`, `high_risk_execution: 57`, `state_mutation: 122`, `dead_code: 2`, `fragile_debt: 3`, `duplicate_logic: 9`, `unreferenced_by_name: 322`
* *Architecture:* `io: 783`, `api: 176`, `concurrency: 1544`, `import: 231`
* *Defense:* `safety: 367`, `test: 964`, `immutability_locks: 3`, `cleanup: 47`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.702
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` $chunk, $path.basename(inputCommon), $chunk, , $chunk, $path.basename(imported), $path.basename(inputCommon), a.unknown...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/js_printer/js_printer.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3792.18 | **LOC:** 5026 | **CtrlFlow:** 32.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (48.469%), Tech Debt (8.4572%)
**Top Internal Functions/Classes:**
  * `printExpr` (Impact: 923.4)
  * `printStmt` (Impact: 359.1)
  * `printUnquotedUTF16` (Impact: 135.2)
  * `printRequireOrImportExpr` (Impact: 125.6)
  * `printProperty` (Impact: 121.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 335 instances
* *State Mutation (weighted view):* 1013
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1324`, `structural_boundaries: 245`, `args: 71`, `func_start: 71`, `class_start: 6`
* *Risk/State:* `high_risk_execution: 7`, `state_mutation: 343`, `dead_code: 3`, `planned_debt: 2`, `unreferenced_by_name: 2`
* *Architecture:* `api: 35`, `import: 1`
* *Defense:* `doc: 168`, `test: 5`, `immutability_locks: 14`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.252
  * `Choke Point (Betweenness):` 0.000164 | `Ripple Effect (Closeness):` 0.01141
  * `Imports (Out-Degree: 8):` bytes, fmt, ast, compat, config, helpers, js_ast, logger...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `scripts/decorator-tests.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3529.98 | **LOC:** 5384 | **CtrlFlow:** 3.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (89.3602%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `__decorateElement` (Impact: 130.9)
  * `__runInitializers` (Impact: 9.2)
  * `prettyPrint` (Impact: 7.5)
  * `__decoratorContext` (Impact: 7.4)
  * `__privateMethod` (Impact: 6.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 50 instances
* *Amplified Cascading Flux:* 222 instances
* *Concurrency (weighted view):* 308
* *State Mutation (weighted view):* 1674
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 194`, `structural_boundaries: 2531`, `args: 1870`, `func_start: 639`, `class_start: 131`
* *Risk/State:* `safety_bypasses: 51`, `state_mutation: 1230`, `duplicate_logic: 475`
* *Architecture:* `concurrency: 58`
* *Defense:* `safety: 158`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.702
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/bundler/bundler.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2680.56 | **LOC:** 3532 | **CtrlFlow:** 23.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (38.5262%), Tech Debt (11.4932%)
**Top Internal Functions/Classes:**
  * `parseFile` (Impact: 225.0)
  * `processScannedFiles` (Impact: 154.8)
  * `runOnLoadPlugins` (Impact: 112.6)
  * `addEntryPoints` (Impact: 108.6)
  * `RunOnResolvePlugins` (Impact: 99.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 9 instances
* *Amplified Cascading Flux:* 353 instances
* *Concurrency (weighted view):* 60
* *State Mutation (weighted view):* 1096
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 637`, `structural_boundaries: 303`, `args: 34`, `func_start: 34`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 2`, `state_mutation: 390`, `dead_code: 4`, `planned_debt: 3`, `fragile_debt: 3`, `unreferenced_by_name: 2`
* *Architecture:* `io: 1`, `api: 16`, `concurrency: 15`, `import: 1`
* *Defense:* `safety: 7`, `doc: 243`, `sync_locks: 5`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.576
  * `Choke Point (Betweenness):` 0.000558 | `Ripple Effect (Closeness):` 0.015974
  * `Imports (Out-Degree: 14):` , .cjs, .css, .cts, .js, .json, .jsx, .mjs...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `scripts/decorator-tests.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2493.38 | **LOC:** 3913 | **CtrlFlow:** 3.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.36%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `prettyPrint` (Impact: 7.5)
  * `capture` (Impact: 7.4)
  * `capture` (Impact: 6.9)
  * `capture` (Impact: 5.1)
  * `capture` (Impact: 4.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 56 instances
* *Amplified Cascading Flux:* 207 instances
* *Concurrency (weighted view):* 339
* *State Mutation (weighted view):* 1152
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 126`, `structural_boundaries: 2525`, `args: 1686`, `func_start: 386`, `class_start: 130`
* *Risk/State:* `safety_bypasses: 223`, `state_mutation: 738`, `planned_debt: 1`, `duplicate_logic: 210`
* *Architecture:* `api: 2`, `concurrency: 59`
* *Defense:* `safety: 10`, `test: 1`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.702
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/shared/common.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2364.72 | **LOC:** 1879 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (20.4247%)
**Top Internal Functions/Classes:**
  * `buildOrContextImpl` (Impact: 196.2)
  * `flagsForBuildOptions` (Impact: 160.2)
  * `buildOrContextContinue` (Impact: 100.5)
    * *Intent:* // "buildOrContext" cannot be written using async/await due to "buildSync" // and must be written in...
  * `createChannel` (Impact: 98.8)
    * *Intent:* // This can't use any promises in the main execution flow because it must work // for both sync and ...
  * `pushCommonFlags` (Impact: 96.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 11 instances
* *Amplified Cascading Flux:* 283 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 87
* *State Mutation (weighted view):* 862
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 406`, `structural_boundaries: 356`, `args: 160`, `func_start: 108`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 69`, `high_risk_execution: 1`, `state_mutation: 296`, `dead_code: 1`, `fragile_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `io: 28`, `api: 18`, `concurrency: 32`, `import: 3`
* *Defense:* `safety: 52`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.32
  * `Choke Point (Betweenness):` 0.000297 | `Ripple Effect (Closeness):` 0.02399
  * `Imports (Out-Degree: 2):` stdio_protocol, types, uint8array_json_parser
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `internal/js_lexer/js_lexer.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2252.62 | **LOC:** 2666 | **CtrlFlow:** 31.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (47.5332%), Tech Debt (16.5667%)
**Top Internal Functions/Classes:**
  * `Next` (Impact: 241.6)
  * `tryToDecodeEscapeSequences` (Impact: 152.1)
    * *Intent:* // If this fails, this returns "nil, false, end" where "end" is the value to // store to "lexer.end"...
  * `parseNumericLiteralOrDot` (Impact: 120.3)
  * `NextInsideJSXElement` (Impact: 56.0)
  * `scanCommentText` (Impact: 46.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 354 instances
* *Amplified Sql Injection:* 3 instances
* *State Mutation (weighted view):* 1070
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 657`, `structural_boundaries: 133`, `args: 45`, `func_start: 45`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 11`, `state_mutation: 362`, `dead_code: 1`, `unreferenced_by_name: 18`
* *Architecture:* `api: 181`, `import: 1`
* *Defense:* `doc: 137`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.646
  * `Choke Point (Betweenness):` 0.001498 | `Ripple Effect (Closeness):` 0.035512
  * `Imports (Out-Degree: 7):` break, case, catch, class, const, continue, debugger, default...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `internal/js_ast/js_ast_helpers.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2238.22 | **LOC:** 3017 | **CtrlFlow:** 44.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (26.6025%), Tech Debt (16.965%)
**Top Internal Functions/Classes:**
  * `SimplifyUnusedExpr` (Impact: 192.7)
    * *Intent:* // This will return a nil expression if the expression can be totally removed. // // This function i...
  * `MangleIfExpr` (Impact: 146.1)
    * *Intent:* // This function intentionally avoids mutating the input AST so it can be // called after the AST ha...
  * `CheckEqualityIfNoSideEffects` (Impact: 115.5)
    * *Intent:* // Returns "equal, ok". If "ok" is false, then nothing is known about the two // values. If "ok" is ...
  * `FoldBinaryOperator` (Impact: 111.1)
    * *Intent:* // This function intentionally avoids mutating the input AST so it can be // called after the AST ha...
  * `ExprCanBeRemovedIfUnused` (Impact: 109.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 119 instances
* *State Mutation (weighted view):* 361
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 929`, `structural_boundaries: 519`, `args: 56`, `func_start: 56`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 123`, `dead_code: 3`, `unreferenced_by_name: 19`
* *Architecture:* `api: 67`, `import: 1`
* *Defense:* `doc: 146`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.702
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` -Infinity, Infinity, NaN, bigint, boolean, false, function, ast...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/resolver/resolver.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2173.52 | **LOC:** 2973 | **CtrlFlow:** 30.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (31.4051%), Tech Debt (18.6886%)
**Top Internal Functions/Classes:**
  * `finalizeImportsExportsResult` (Impact: 274.2)
  * `parseTSConfigFromSource` (Impact: 166.0)
  * `loadNodeModules` (Impact: 117.0)
  * `Resolve` (Impact: 116.4)
  * `ResolveGlob` (Impact: 104.5)
    * *Intent:* // This returns nil on failure and non-nil on success. Note that this may // return an empty array t...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 194 instances
* *State Mutation (weighted view):* 598
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 633`, `structural_boundaries: 303`, `args: 38`, `func_start: 38`, `class_start: 9`
* *Risk/State:* `state_mutation: 210`, `dead_code: 6`, `fragile_debt: 4`, `unreferenced_by_name: 8`
* *Architecture:* `api: 30`, `import: 1`
* *Defense:* `safety: 7`, `doc: 238`, `sync_locks: 7`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.765
  * `Choke Point (Betweenness):` 0.000329 | `Ripple Effect (Closeness):` 0.018588
  * `Imports (Out-Degree: 11):` .cjs, .js, .jsx, .mjs, _http_agent, _http_client, _http_common, _http_incoming...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `internal/js_parser/js_parser_lower_class.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2098.78 | **LOC:** 2601 | **CtrlFlow:** 27.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (37.3967%), Tech Debt (12.1628%)
**Top Internal Functions/Classes:**
  * `processProperties` (Impact: 180.7)
  * `finishAndGenerateCode` (Impact: 131.1)
  * `lowerField` (Impact: 100.6)
    * *Intent:* // Handle lowering of instance and static fields. Move their initializers // from the class body to ...
  * `analyzeProperty` (Impact: 80.0)
  * `computeClassLoweringInfo` (Impact: 73.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 309 instances
* *State Mutation (weighted view):* 960
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 481`, `structural_boundaries: 118`, `args: 33`, `func_start: 33`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 342`, `dead_code: 17`, `unreferenced_by_name: 9`
* *Architecture:* `import: 1`
* *Defense:* `doc: 213`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.702
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` fmt, ast, compat, config, helpers, js_ast, logger
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/plugin-tests.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2015.1 | **LOC:** 3513 | **CtrlFlow:** 6.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (61.3729%), Tech Debt (72.971%)
**Top Internal Functions/Classes:**
  * `resolveWithSideEffectsFalse` (Impact: 17.8)
  * `noResolveDirInVirtualModule` (Impact: 16.1)
  * `onLoadWithInternalOnResolveAndQuerySuffix` (Impact: 13.7)
  * `caseInsensitiveRegExp` (Impact: 13.4)
  * `importAttributesOnResolve` (Impact: 13.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 12 instances
* *Amplified Rce:* 5 instances
* *Amplified Race Conditions:* 77 instances
* *Amplified Cascading Flux:* 15 instances
* *High Risk Execution (weighted view):* 2
* *Concurrency (weighted view):* 806
* *Sec Tainted Injection (weighted view):* 5
* *State Mutation (weighted view):* 115
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 196`, `structural_boundaries: 855`, `args: 401`, `func_start: 216`
* *Risk/State:* `safety_bypasses: 59`, `high_risk_execution: 14`, `state_mutation: 85`, `duplicate_logic: 6`, `unreferenced_by_name: 99`
* *Architecture:* `io: 180`, `api: 97`, `concurrency: 421`, `import: 75`
* *Defense:* `safety: 147`, `test: 268`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.702
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` base.js, esbuild, example.custom, example.js, name, index, loadme, name...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/bundler_tests/bundler_default_test.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1907.68 | **LOC:** 9410 | **CtrlFlow:** 3.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (6.7138%), Tech Debt (93.3927%)
**Top Internal Functions/Classes:**
  * `TestWarningsInsideNodeModules` (Impact: 43.3)
  * `TestErrorsForAssertTypeJSON` (Impact: 42.6)
  * `TestCommentPreservation` (Impact: 22.4)
  * `TestRequireResolve` (Impact: 16.8)
  * `TestKeepNamesAllForms` (Impact: 16.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 26 instances
* *State Mutation (weighted view):* 217
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 293`, `structural_boundaries: 1379`, `args: 301`, `func_start: 301`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 165`, `dead_code: 6`, `fragile_debt: 2`, `unreferenced_by_name: 301`
* *Architecture:* `api: 301`, `import: 117`
* *Defense:* `doc: 79`, `test: 326`, `immutability_locks: 86`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.702
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` bad-typeof.js, bad0.js, bad1.js, bad10.js, bad11.js, bad12.js, bad13.js, bad14.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/logger/logger.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1757.56 | **LOC:** 2074 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (36.362%), Tech Debt (58.1913%)
**Top Internal Functions/Classes:**
  * `detailStruct` (Impact: 74.3)
  * `msgString` (Impact: 64.9)
  * `GenerateStringInJSTable` (Impact: 64.6)
    * *Intent:* // For Yarn PnP we sometimes parse JSON embedded in a JS string. This generates // a table that rema...
  * `PrintSummary` (Impact: 63.2)
  * `NewStderrLog` (Impact: 51.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 226 instances
* *State Mutation (weighted view):* 685
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 393`, `structural_boundaries: 217`, `args: 60`, `func_start: 60`, `class_start: 19`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 233`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 28`
* *Architecture:* `api: 187`, `import: 1`
* *Defense:* `doc: 116`, `sync_locks: 21`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 79.069
  * `Choke Point (Betweenness):` 0.001615 | `Ripple Effect (Closeness):` 0.221708
  * `Imports (Out-Degree: 2):` DEBUG, ERROR, INFO, NOTE, VERBOSE, WARNING, X, binary...
  * `Imported By (In-Degree: 61):` (Excluded from Brief to save tokens)

### `pkg/api/api_impl.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1750.46 | **LOC:** 2566 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (30.6623%), Tech Debt (13.4968%)
**Top Internal Functions/Classes:**
  * `validateBuildOptions` (Impact: 110.5)
  * `analyzeMetafileImpl` (Impact: 80.8)
  * `rebuildImpl` (Impact: 76.6)
  * `validateDefines` (Impact: 75.6)
  * `validateFeatures` (Impact: 53.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 204 instances
* *High Risk Execution (weighted view):* 14
* *Concurrency (weighted view):* 15
* *State Mutation (weighted view):* 638
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 464`, `structural_boundaries: 303`, `args: 65`, `func_start: 65`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 15`, `state_mutation: 230`, `dead_code: 1`, `unreferenced_by_name: 13`
* *Architecture:* `api: 7`, `concurrency: 5`, `import: 1`
* *Defense:* `safety: 8`, `doc: 131`, `sync_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.702
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` .css, .js, bytes, css, base64, binary, errors, fmt...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/css_parser/css_parser.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1729.72 | **LOC:** 2487 | **CtrlFlow:** 28.8% | **Authorship Centralization:** 83.3%
- **Risk Profile:** Cognitive Load (46.7355%), Tech Debt (9.9881%)
**Top Internal Functions/Classes:**
  * `parseAtRule` (Impact: 240.3)
  * `convertTokensHelper` (Impact: 153.8)
  * `parseListOfRules` (Impact: 64.8)
  * `mangleRules` (Impact: 63.5)
  * `parseSelectorRule` (Impact: 48.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 234 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 714
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 537`, `structural_boundaries: 222`, `args: 40`, `func_start: 40`, `class_start: 12`
* *Risk/State:* `state_mutation: 246`, `dead_code: 1`, `fragile_debt: 1`, `unreferenced_by_name: 2`
* *Architecture:* `api: 7`, `concurrency: 1`, `import: 1`
* *Defense:* `doc: 139`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.589
  * `Choke Point (Betweenness):` 0.000242 | `Ripple Effect (Closeness):` 0.017039
  * `Imports (Out-Degree: 9):` -moz-document, -ms-viewport, a, abbr, active, address, annotation, area...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `pkg/cli/cli_impl.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1693.24 | **LOC:** 1565 | **CtrlFlow:** 34.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (63.2226%), Tech Debt (8.2625%)
**Top Internal Functions/Classes:**
  * `parseOptionsImpl` (Impact: 795.4)
  * `runImpl` (Impact: 99.7)
  * `parseServeOptionsImpl` (Impact: 36.0)
  * `serveImpl` (Impact: 21.4)
  * `parseOptionsForRun` (Impact: 18.0)
    * *Intent:* // This returns either BuildOptions, TransformOptions, or an error
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 205 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 620
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 458`, `structural_boundaries: 156`, `args: 15`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 2`, `state_mutation: 210`, `dead_code: 1`, `unreferenced_by_name: 1`
* *Architecture:* `concurrency: 2`, `import: 1`
* *Defense:* `safety: 43`, `doc: 46`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.702
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` --analyze, abs-paths, alias, allow-overwrite, ascii, asset-names, automatic, banner...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/js_parser/ts_parser_test.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1500.18 | **LOC:** 3318 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (45.9594%), Tech Debt (39.121%)
**Top Internal Functions/Classes:**
  * `TestTSNamespaceExports` (Impact: 73.3)
  * `TestTSClass` (Impact: 64.7)
  * `TestTSNamespace` (Impact: 60.7)
  * `TestTSTypes` (Impact: 59.1)
  * `TestTSEnum` (Impact: 37.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 214 instances
* *State Mutation (weighted view):* 784
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 267`, `structural_boundaries: 599`, `args: 53`, `func_start: 53`
* *Risk/State:* `state_mutation: 356`, `fragile_debt: 2`, `unreferenced_by_name: 37`
* *Architecture:* `api: 41`, `import: 1`
* *Defense:* `doc: 77`, `test: 37`, `immutability_locks: 302`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.702
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` compat, config, testing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/js_parser/js_parser_lower.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1445.48 | **LOC:** 2133 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (35.2175%), Tech Debt (33.7934%)
**Top Internal Functions/Classes:**
  * `lowerOptionalChain` (Impact: 133.3)
  * `lowerFunction` (Impact: 124.9)
  * `lowerObjectRestHelper` (Impact: 104.0)
  * `markSyntaxFeature` (Impact: 64.5)
  * `lowerTemplateLiteral` (Impact: 41.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 184 instances
* *State Mutation (weighted view):* 585
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 334`, `structural_boundaries: 156`, `args: 36`, `func_start: 36`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 217`, `dead_code: 13`, `planned_debt: 1`, `unreferenced_by_name: 18`
* *Architecture:* `import: 1`
* *Defense:* `doc: 111`, `test: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.702
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` fmt, ast, compat, config, helpers, js_ast, logger
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/bundler_tests/bundler_dce_test.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1265.96 | **LOC:** 5010 | **CtrlFlow:** 7.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (9.0391%), Tech Debt (81.2618%)
**Top Internal Functions/Classes:**
  * `TestDeadCodeInsideUnusedCases` (Impact: 89.2)
  * `TestNoSideEffectsComment` (Impact: 80.5)
    * *Intent:* // See: https://github.com/rollup/rollup/pull/5024
  * `TestNoSideEffectsCommentIgnoreAnnotations` (Impact: 75.9)
  * `TestNoSideEffectsCommentMinifyWhitespace` (Impact: 75.9)
  * `TestDCETypeOfEqualsStringGuardCondition` (Impact: 63.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 142
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 359`, `structural_boundaries: 447`, `args: 121`, `func_start: 121`
* *Risk/State:* `safety_bypasses: 32`, `state_mutation: 104`, `fragile_debt: 2`, `unreferenced_by_name: 121`
* *Architecture:* `api: 121`, `import: 18`
* *Defense:* `doc: 44`, `test: 121`, `immutability_locks: 205`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.702
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` nested.js, file.j, require-demo-pkg, .data, .js, entry.js, index.js, package.json...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `internal/css_ast/css_ast.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1227.66 | **LOC:** 1581 | **CtrlFlow:** 23.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (24.0617%), Tech Debt (26.5053%)
**Top Internal Functions/Classes:**
  * `Equal` (Impact: 35.6)
  * `Equal` (Impact: 24.0)
  * `NumberOrFractionForPercentage` (Impact: 18.4)
  * `Equal` (Impact: 18.3)
  * `Equal` (Impact: 16.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 72 instances
* *State Mutation (weighted view):* 262
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 289`, `structural_boundaries: 336`, `args: 115`, `func_start: 115`, `class_start: 43`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 118`, `unreferenced_by_name: 18`
* *Architecture:* `api: 310`, `import: 1`
* *Defense:* `doc: 51`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 12.784
  * `Choke Point (Betweenness):` 0.000684 | `Ripple Effect (Closeness):` 0.117894
  * `Imports (Out-Degree: 4):` before, cm, ast, css_lexer, helpers, logger, global, has...
  * `Imported By (In-Degree: 24):` (Excluded from Brief to save tokens)

### `internal/css_printer/css_printer.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1191.56 | **LOC:** 1324 | **CtrlFlow:** 36.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (44.844%), Tech Debt (8.4234%)
**Top Internal Functions/Classes:**
  * `printRule` (Impact: 235.4)
  * `printTokens` (Impact: 99.9)
  * `printCompoundSelector` (Impact: 84.1)
  * `printIdent` (Impact: 83.6)
    * *Intent:* // Note: This function is hot in profiles
  * `printMediaQuery` (Impact: 73.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 94 instances
* *State Mutation (weighted view):* 284
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 405`, `structural_boundaries: 70`, `args: 23`, `func_start: 23`, `class_start: 4`
* *Risk/State:* `high_risk_execution: 5`, `state_mutation: 96`, `dead_code: 2`, `unreferenced_by_name: 1`
* *Architecture:* `api: 20`, `import: 1`
* *Defense:* `doc: 32`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.023
  * `Choke Point (Betweenness):` 2.6e-05 | `Ripple Effect (Closeness):` 0.00852
  * `Imports (Out-Degree: 8):` fmt, ast, compat, config, css_ast, css_lexer, helpers, logger...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `internal/resolver/package_json.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1111.64 | **LOC:** 1463 | **CtrlFlow:** 31.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (29.0394%), Tech Debt (30.6335%)
**Top Internal Functions/Classes:**
  * `esmPackageTargetResolve` (Impact: 169.9)
  * `parseImportsExportsMap` (Impact: 106.9)
  * `parsePackageJSON` (Impact: 97.7)
  * `checkBrowserMap` (Impact: 93.8)
  * `esmPackageTargetReverseResolve` (Impact: 59.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 94 instances
* *State Mutation (weighted view):* 283
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 342`, `structural_boundaries: 173`, `args: 20`, `func_start: 20`, `class_start: 7`
* *Risk/State:* `state_mutation: 95`, `dead_code: 1`, `fragile_debt: 2`, `unreferenced_by_name: 9`
* *Architecture:* `api: 3`, `import: 1`
* *Defense:* `safety: 2`, `doc: 104`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.702
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` commonjs, default, fmt, config, helpers, js_ast, js_lexer, js_parser...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `Makefile` -> Churn: **63.17%** | Cog Load: 53.603% | Debt: 82.6043%
- `scripts/esbuild.js` -> Churn: **51.21%** | Cog Load: 85.5241% | Debt: 21.9866%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `scripts/end-to-end-tests.js` -> **Evan Wallace** (83.3% isolated ownership) | Magnitude: 11309.86
- `internal/js_parser/js_parser_test.go` -> **Evan Wallace** (91.7% isolated ownership) | Magnitude: 4549.48
- `internal/linker/linker.go` -> **Evan Wallace** (100.0% isolated ownership) | Magnitude: 4538.12
- `scripts/js-api-tests.js` -> **Evan Wallace** (100.0% isolated ownership) | Magnitude: 4213.62
- `internal/js_printer/js_printer.go` -> **Evan Wallace** (100.0% isolated ownership) | Magnitude: 3792.18

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `internal/config/config.go` -> **Severity: 0.17** (Bridge: 0.0017 * Flux: 100.0%)
- `internal/logger/logger.go` -> **Severity: 0.161** (Bridge: 0.0016 * Flux: 100.0%)
- `internal/js_lexer/js_lexer.go` -> **Severity: 0.15** (Bridge: 0.0015 * Flux: 100.0%)
- `internal/css_ast/css_ast.go` -> **Severity: 0.068** (Bridge: 0.0007 * Flux: 99.7533%)
- `internal/runtime/runtime.go` -> **Severity: 0.066** (Bridge: 0.0007 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `internal/logger/logger.go` -> **Severity: 20.554** (Embedded: 0.2217 * Error Risk: 92.7081%)
- `internal/runtime/runtime.go` -> **Severity: 13.629** (Embedded: 0.1381 * Error Risk: 98.694%)
- `internal/compat/compat.go` -> **Severity: 10.257** (Embedded: 0.1411 * Error Risk: 72.7027%)
- `internal/ast/ast.go` -> **Severity: 9.955** (Embedded: 0.1516 * Error Risk: 65.6723%)
- `internal/css_ast/css_ast.go` -> **Severity: 9.171** (Embedded: 0.1179 * Error Risk: 77.7928%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `internal/helpers/strings.go` -> **Severity: 14125.0** (Blast Radius: 141.25 * Doc Risk: 100.0%)
- `internal/logger/logger.go` -> **Severity: 6250.215** (Blast Radius: 79.069 * Doc Risk: 79.0476%)
- `internal/ast/ast.go` -> **Severity: 2278.201** (Blast Radius: 34.173 * Doc Risk: 66.6667%)
- `internal/compat/compat.go` -> **Severity: 2095.601** (Blast Radius: 31.434 * Doc Risk: 66.6667%)
- `internal/fs/fs.go` -> **Severity: 1785.6** (Blast Radius: 27.9 * Doc Risk: 64.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
