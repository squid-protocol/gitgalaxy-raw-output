# ARCHITECTURAL_BRIEF: bun
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/bun` |
| **Timestamp** | `2026-08-03T19:25:24.009791+00:00` |
| **Scan Duration** | `27.38s` |
| **Git Branch** | `main` |
| **Git Commit** | `1cc837687b1d1f8d558a40110fbe3e61cc41fbcd` |
| **Git Remote** | `https://github.com/oven-sh/bun` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 3228 malicious artifacts.

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
| Total Artifacts | 12530 |
| Analyzed Artifacts (Scanned) | 3973 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 8557 |
| Total LOC | 834983 |
| Volatility Index | 0.003 |
| % Scanned of codebase = | 31.7% |
| Dominant Lang | ZIG |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6166 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1294 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.5% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.3612 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 106 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| CPP | 1293 | 158839 | 32.5% |
| ZIG | 1173 | 550678 | 29.5% |
| PLAINTEXT | 503 | 107 | 12.7% |
| TYPESCRIPT | 436 | 76027 | 11.0% |
| JAVASCRIPT | 258 | 19123 | 6.5% |
| HTML | 108 | 4122 | 2.7% |
| MARKDOWN | 66 | 0 | 1.7% |
| JSON | 36 | 788 | 0.9% |
| C | 29 | 17551 | 0.7% |
| SHELL | 13 | 1402 | 0.3% |
| XML | 13 | 5 | 0.3% |
| CSS | 13 | 1072 | 0.3% |
| RUST | 6 | 527 | 0.2% |
| PYTHON | 5 | 1961 | 0.1% |
| DOCKERFILE | 4 | 281 | 0.1% |
| YAML | 4 | 134 | 0.1% |
| NIX | 2 | 219 | 0.1% |
| PERL | 2 | 664 | 0.1% |
| M4 | 2 | 217 | 0.1% |
| POWERSHELL | 2 | 291 | 0.1% |
| BINARY_THREAT | 2 | 2 | 0.1% |
| PROTO | 1 | 11 | 0.0% |
| RUBY | 1 | 322 | 0.0% |
| MAKEFILE | 1 | 640 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.659`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 1941 | 48.9% |
| file_cluster_13 | 1141 | 28.7% |
| Unknown | 109 | 2.7% |
| file_cluster_4 | 103 | 2.6% |
| file_cluster_9 | 71 | 1.8% |
| file_cluster_16 | 45 | 1.1% |
| file_cluster_0 | 24 | 0.6% |
| file_cluster_11 | 20 | 0.5% |
| file_cluster_2 | 16 | 0.4% |
| file_cluster_17 | 13 | 0.3% |
| file_cluster_6 | 10 | 0.3% |
| file_cluster_12 | 7 | 0.2% |
| file_cluster_15 | 3 | 0.1% |
| file_cluster_7 | 2 | 0.1% |
| file_cluster_1 | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 462 | 11.6% |
| Static: Minified & Vendor Opaque Mass | 5 | 0.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 8557*

**Composition by Extension & Reason:**
- `.js`: 3844x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Monolithic Amalgamation: 46169 LOC exceeds safe regex boundaries), 1x Excluded (Saturation: Line 16 exceeds 500 chars)
- `.ts`: 1911x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Unsupported Format (.undeterminable), 1x Excluded (Machine-Generated Source Code Signature: 232 LOC)
- `.tgz`: 349x Excluded (Explicitly Denied Extension: '.tgz')
- `.mdx`: 332x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mjs`: 303x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 89 LOC), 1x Excluded (Saturation: Line 28 exceeds 500 chars)
- `.json`: 220x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 3974 LOC), 1x Excluded (Massive Static Asset Blob: 3780 LOC)
- `no_extension`: 139x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Binary Format Detected), 2x Unsupported Format (.undeterminable)
- `.map`: 100x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cjs`: 95x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.c`: 87x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Monolithic Amalgamation: 265971 LOC exceeds safe regex boundaries)
- `.txt`: 80x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 26758 LOC), 1x Excluded (Monolithic Amalgamation: 40117 LOC exceeds safe regex boundaries)
- `.md`: 67x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 41 LOC)
- `.lock`: 26x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 25x Excluded (Unsupported Extension: '.lock'), 7x Unsupported Format (.lock)
- `.snap`: 59x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.gyp`: 59x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 35.8 | 26.9 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 30.5 | 14.8 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 42.2 | 12.3 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 33.0 | 2.6 | 80.0 |
| API Exposure | 0.0 | 20.0 | 3.3 | 2.2 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 9.7 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 48.9 | 42.5 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 3.2 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 92.4 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 13.1 | 3.3 | 1.5 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 9.3 | 4.8 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 53.0 | 46.6 | 100.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 50.0 | 43.2 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 23.8 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 11.1 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 1.1 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 10.0 | 0.2 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `completions/bun.zsh` (Hits: 120)
- `src/sys.zig` (Hits: 103)
- `src/bun.zig` (Hits: 102)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **root.h** (`src/bun.js/bindings/root.h`) — 364 inbound connections
2. **config.h** (`src/bun.js/bindings/webcore/config.h`) — 257 inbound connections
3. **ZigGlobalObject.h** (`src/bun.js/bindings/ZigGlobalObject.h`) — 147 inbound connections
4. **ErrorCode.h** (`src/bun.js/bindings/ErrorCode.h`) — 96 inbound connections
5. **BunClientData.h** (`src/bun.js/bindings/BunClientData.h`) — 82 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **ZigGlobalObject.cpp** (`src/bun.js/bindings/ZigGlobalObject.cpp`) — 210 outbound dependencies
2. **bindings.cpp** (`src/bun.js/bindings/bindings.cpp`) — 128 outbound dependencies
3. **bun.zig** (`src/bun.zig`) — 116 outbound dependencies
4. **BunProcess.cpp** (`src/bun.js/bindings/BunProcess.cpp`) — 84 outbound dependencies
5. **jsc.zig** (`src/bun.js/jsc.zig`) — 78 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `writeWithFormatting` (@ `src/bun.js/test/pretty_format.zig`) -> Impact: **8411.2** | LOC: 1064
- `crashHandler` (@ `src/crash_handler.zig`) -> Impact: **6371.1** | LOC: 1225
  * *Intent:* /// This function is invoked when a crash happens. A crash is classified in `CrashReason`.
- `Parse` (@ `src/ast/parse.zig`) -> Impact: **5861.4** | LOC: 1086
- `parse` (@ `src/install/npm.zig`) -> Impact: **5802.9** | LOC: 904
  * *Intent:* /// This parses [Abbreviated metadata](https://github.com/npm/registry/blob/master/docs/responses/package-metadata.md#abbreviated-metadata-format)
- `Parser` (@ `src/interchange/yaml.zig`) -> Impact: **5692.7** | LOC: 1294
- `fromJS` (@ `src/bun.js/api/JSBundler.zig`) -> Impact: **5510.9** | LOC: 650
- `NewSocketHandler` (@ `src/deps/uws/socket.zig`) -> Impact: **5329.1** | LOC: 1021
- `fromJS` (@ `src/bun.js/api/server/ServerConfig.zig`) -> Impact: **4801.0** | LOC: 686
- `escapeXml` (@ `src/cli/test_command.zig`) -> Impact: **4759.0** | LOC: 1095
- `Calc` (@ `src/css/values/calc.zig`) -> Impact: **4745.8** | LOC: 1116
  * *Intent:* /// A mathematical expression used within the `calc()` function. /// /// This type supports generic value types. Values such as `Length`, `Percentage`...

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `describe` (@ `packages/bun-vscode/src/features/tests/__tests__/bun-test-controller.static-parser.test.ts`) -> **O(2^N) [Recursive]**
- `executeHandlers` (@ `packages/bun-uws/src/HttpRouter.h`) -> **O(2^N) [Recursive]**
  * *Intent:* /* Update currentUrl */
- `convertToExtern` (@ `src/bun.js/bindings/Bindgen/ExternVectorTraits.h`) -> **O(2^N) [Recursive]**
- `convert` (@ `src/bun.js/bindings/BunIDLConvert.h`) -> **O(2^N) [Recursive]**
- `functionName` (@ `src/bun.js/bindings/ErrorStackTrace.cpp`) -> **O(2^N) [Recursive]**
- `functionName` (@ `src/bun.js/bindings/ErrorStackTrace.cpp`) -> **O(2^N) [Recursive]**
- `JSC_DEFINE_HOST_FUNCTION` (@ `src/bun.js/bindings/JSCommonJSModule.cpp`) -> **O(2^N) [Recursive]**
  * *Intent:* * How cyclical dependencies are handled: * * Before executing the CommonJS module, we set the exports object in the * requireMap to an empty object. W...
- `toJS` (@ `src/bun.js/bindings/SQLClient.cpp`) -> **O(2^N) [Recursive]**
- `finishCreation` (@ `src/bun.js/bindings/ServerRouteList.cpp`) -> **O(2^N) [Recursive]**
- `Bun__deepMatch` (@ `src/bun.js/bindings/bindings.cpp`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `emitKeys` (@ `src/js/node/readline.ts`) -> DB Complexity: **308**
- `_bun_run_completion_[Truncated]` (@ `completions/bun.zsh`) -> DB Complexity: **277**
- `crashHandler` (@ `src/crash_handler.zig`) -> DB Complexity: **247**
  * *Intent:* /// This function is invoked when a crash happens. A crash is classified in `CrashReason`.
- `llhttp__internal__run` (@ `src/bun.js/bindings/node/http/llhttp/llhttp.c`) -> DB Complexity: **246**
- `parseTestBlocks` (@ `packages/bun-vscode/src/features/tests/bun-test-controller.ts`) -> DB Complexity: **231**
- `jsonString` (@ `src/bun.js/webview/ChromeBackend.cpp`) -> DB Complexity: **193**
- `describe` (@ `packages/bun-vscode/src/features/tests/__tests__/socket-integration.test.ts`) -> DB Complexity: **190**
- `generateHeapProfile` (@ `src/bun.js/bindings/BunHeapProfiler.cpp`) -> DB Complexity: **189**
- `JSC_DEFINE_HOST_FUNCTION` (@ `src/bun.js/modules/NodeModuleModule.cpp`) -> DB Complexity: **173**
- `_read_scripts_in_package_json_[Truncated` (@ `completions/bun.bash`) -> DB Complexity: **166**
  * *Intent:* # loads the scripts block in package.json

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src` | 127 | 164278.97 | 25.38% | 27.98% |
| `test/js/node/crypto/fixtures` | 26 | 130000.0 | 0.0% | 0.0% |
| `src/bun.js/bindings` | 457 | 106516.85 | 41.86% | 62.65% |
| `test/js/node/tls/fixtures` | 21 | 105000.0 | 0.0% | 0.0% |
| `src/ast` | 46 | 87908.72 | 26.79% | 24.15% |
| `test/js/third_party/jsonwebtoken` | 17 | 85000.0 | 0.0% | 0.0% |
| `src/cli` | 44 | 66980.14 | 35.8% | 16.88% |
| `src/bun.js/bindings/webcore` | 412 | 62940.66 | 53.4% | 74.79% |
| `src/bun.js/api` | 55 | 54550.74 | 21.26% | 30.89% |
| `src/install` | 30 | 53914.78 | 30.2% | 19.32% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `bench/async/bun.js` -> **100.0%** Exposure
- `bench/async/deno.js` -> **100.0%** Exposure
- `bench/async/node.mjs` -> **100.0%** Exposure
- `bench/cat/cat.mjs` -> **100.0%** Exposure
- `bench/crypto/diffie-hellman.mjs` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `bench/async/AsyncLocalStorage.mjs` -> **100.0%** Exposure
- `bench/cat/cat.mjs` -> **100.0%** Exposure
- `bench/snippets/array-shift.mjs` -> **100.0%** Exposure
- `bench/snippets/async-overhead.mjs` -> **100.0%** Exposure
- `bench/snippets/buffer-fill.mjs` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/bun.js/bindings/bindings.cpp` -> **236** Orphaned Functions | **0** Duplicates
- `src/bun.js/bindings/ncrypto.cpp` -> **172** Orphaned Functions | **50** Duplicates
- `src/css/values/color_generated.zig` -> **0** Orphaned Functions | **182** Duplicates
- `src/bun.js/node/node_fs.zig` -> **0** Orphaned Functions | **147** Duplicates
- `src/api/schema.zig` -> **0** Orphaned Functions | **132** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`src/js/internal/assert/utils.ts`** -> AI Confidence: **99.48%**
2. **`src/js/internal/sql/sqlite.ts`** -> AI Confidence: **99.48%**
3. **`src/js/internal/streams/pipeline.ts`** -> AI Confidence: **99.48%**
4. **`src/js/internal/streams/readable.ts`** -> AI Confidence: **99.48%**
5. **`src/js/internal/streams/writable.ts`** -> AI Confidence: **99.48%**
6. **`src/js/node/_http_agent.ts`** -> AI Confidence: **99.48%**
7. **`src/js/node/_http_server.ts`** -> AI Confidence: **99.48%**
8. **`src/js/node/http2.ts`** -> AI Confidence: **99.48%**
9. **`packages/bun-usockets/src/crypto/root_certs_linux.cpp`** -> AI Confidence: **99.48%**
10. **`src/bun.js/bindings/CallSite.cpp`** -> AI Confidence: **99.48%**
11. **`src/bun.js/bindings/ProcessBindingUV.cpp`** -> AI Confidence: **99.48%**
12. **`src/bun.js/bindings/webcore/JSEventModifierInit.cpp`** -> AI Confidence: **99.48%**
13. **`src/c-headers-for-zig.h`** -> AI Confidence: **99.48%**
14. **`src/bun.js.zig`** -> AI Confidence: **99.48%**
15. **`src/bundler/bundle_v2.zig`** -> AI Confidence: **99.48%**
16. **`src/bunfig.zig`** -> AI Confidence: **99.48%**
17. **`src/cli/audit_command.zig`** -> AI Confidence: **99.48%**
18. **`src/cli/build_command.zig`** -> AI Confidence: **99.48%**
19. **`src/cli/package_manager_command.zig`** -> AI Confidence: **99.48%**
20. **`src/cli/run_command.zig`** -> AI Confidence: **99.48%**
21. **`src/cli/test_command.zig`** -> AI Confidence: **99.48%**
22. **`src/deps/uucode/src/root.zig`** -> AI Confidence: **99.48%**
23. **`src/install/migration.zig`** -> AI Confidence: **99.48%**
24. **`src/install/yarn.zig`** -> AI Confidence: **99.48%**
25. **`src/js_printer.zig`** -> AI Confidence: **99.48%**
26. **`src/s3/client.zig`** -> AI Confidence: **99.48%**
27. **`src/s3/multipart.zig`** -> AI Confidence: **99.48%**
28. **`src/s3/simple_request.zig`** -> AI Confidence: **99.48%**
29. **`src/sql/mysql/protocol/PreparedStatement.zig`** -> AI Confidence: **99.48%**
30. **`src/sql/mysql/protocol/ResultSet.zig`** -> AI Confidence: **99.48%**
31. **`src/sql/postgres/PostgresProtocol.zig`** -> AI Confidence: **99.48%**
32. **`src/sql/postgres/PostgresRequest.zig`** -> AI Confidence: **99.48%**
33. **`src/sql/postgres/protocol/CopyData.zig`** -> AI Confidence: **99.48%**
34. **`src/sql/postgres/protocol/CopyFail.zig`** -> AI Confidence: **99.48%**
35. **`src/bun.js/bindings/node/http/llhttp/llhttp.c`** -> AI Confidence: **99.48%**
36. **`src/bun.js/bindings/root.h`** -> AI Confidence: **99.42%**
37. **`src/bake/hmr-runtime-client.ts`** -> AI Confidence: **99.39%**
38. **`src/js/node/_http_client.ts`** -> AI Confidence: **99.39%**
39. **`src/js/node/net.ts`** -> AI Confidence: **99.39%**
40. **`src/js/node/tls.ts`** -> AI Confidence: **99.39%**
41. **`src/bun.js/bindings/BunProcessReportObjectWindows.cpp`** -> AI Confidence: **99.39%**
42. **`src/bun.js/bindings/bun-spawn.cpp`** -> AI Confidence: **99.39%**
43. **`src/bun.js/bindings/webcore/JSMIMEParams.cpp`** -> AI Confidence: **99.39%**
44. **`src/bun.js/bindings/webcrypto/JSJsonWebKey.cpp`** -> AI Confidence: **99.39%**
45. **`src/bun.js/bindings/wrapAnsi.cpp`** -> AI Confidence: **99.39%**
46. **`src/ast/P.zig`** -> AI Confidence: **99.39%**
47. **`src/ast/parse.zig`** -> AI Confidence: **99.39%**
48. **`src/bun.js/VirtualMachine.zig`** -> AI Confidence: **99.39%**
49. **`src/bun.js/api/JSBundler.zig`** -> AI Confidence: **99.39%**
50. **`src/bun.js/api/Timer.zig`** -> AI Confidence: **99.39%**
51. **`src/bun.js/api/bun/socket.zig`** -> AI Confidence: **99.39%**
52. **`src/bun.js/api/bun/subprocess.zig`** -> AI Confidence: **99.39%**
53. **`src/bun.js/api/server.zig`** -> AI Confidence: **99.39%**
54. **`src/bun.js/event_loop.zig`** -> AI Confidence: **99.39%**
55. **`src/bun.js/jsc.zig`** -> AI Confidence: **99.39%**
56. **`src/bun.js/node.zig`** -> AI Confidence: **99.39%**
57. **`src/bun.js/node/node_fs.zig`** -> AI Confidence: **99.39%**
58. **`src/bun.js/webcore/Request.zig`** -> AI Confidence: **99.39%**
59. **`src/bundler/LinkerContext.zig`** -> AI Confidence: **99.39%**
60. **`src/bundler/ParseTask.zig`** -> AI Confidence: **99.39%**
61. **`src/cli/create_command.zig`** -> AI Confidence: **99.39%**
62. **`src/cli/upgrade_command.zig`** -> AI Confidence: **99.39%**
63. **`src/css/css_parser.zig`** -> AI Confidence: **99.39%**
64. **`src/css/properties/properties.zig`** -> AI Confidence: **99.39%**
65. **`src/css/rules/rules.zig`** -> AI Confidence: **99.39%**
66. **`src/deps/uws.zig`** -> AI Confidence: **99.39%**
67. **`src/http.zig`** -> AI Confidence: **99.39%**
68. **`src/http/websocket_client/WebSocketUpgradeClient.zig`** -> AI Confidence: **99.39%**
69. **`src/install/PackageManager.zig`** -> AI Confidence: **99.39%**
70. **`src/install/extract_tarball.zig`** -> AI Confidence: **99.39%**
71. **`src/install/lockfile.zig`** -> AI Confidence: **99.39%**
72. **`src/install/npm.zig`** -> AI Confidence: **99.39%**
73. **`src/install/pnpm.zig`** -> AI Confidence: **99.39%**
74. **`src/install/repository.zig`** -> AI Confidence: **99.39%**
75. **`src/io/io.zig`** -> AI Confidence: **99.39%**
76. **`src/linker.zig`** -> AI Confidence: **99.39%**
77. **`src/options.zig`** -> AI Confidence: **99.39%**
78. **`src/resolver/package_json.zig`** -> AI Confidence: **99.39%**
79. **`src/resolver/resolver.zig`** -> AI Confidence: **99.39%**
80. **`src/router.zig`** -> AI Confidence: **99.39%**
81. **`src/shell/Builtin.zig`** -> AI Confidence: **99.39%**
82. **`src/shell/shell.zig`** -> AI Confidence: **99.39%**
83. **`src/sourcemap/sourcemap.zig`** -> AI Confidence: **99.39%**
84. **`src/sql/postgres/DataCell.zig`** -> AI Confidence: **99.39%**
85. **`src/sys.zig`** -> AI Confidence: **99.39%**
86. **`src/transpiler.zig`** -> AI Confidence: **99.39%**
87. **`src/valkey/js_valkey.zig`** -> AI Confidence: **99.39%**
88. **`src/bun.js/bindings/BunHeapProfiler.cpp`** -> AI Confidence: **99.35%**
89. **`src/bun.js/ModuleLoader.zig`** -> AI Confidence: **99.35%**
90. **`packages/bun-vscode/src/features/tests/bun-test-controller.ts`** -> AI Confidence: **99.34%**
91. **`src/js/internal/streams/compose.ts`** -> AI Confidence: **99.34%**
92. **`src/js/node/child_process.ts`** -> AI Confidence: **99.34%**
93. **`src/bun.js/bindings/CPUFeatures.cpp`** -> AI Confidence: **99.34%**
94. **`src/bun.js/bindings/sliceAnsi.cpp`** -> AI Confidence: **99.34%**
95. **`src/bun.js/bindings/webcrypto/CryptoAlgorithmRSA_OAEP.cpp`** -> AI Confidence: **99.34%**
96. **`src/bake.zig`** -> AI Confidence: **99.34%**
97. **`src/bundler/Chunk.zig`** -> AI Confidence: **99.34%**
98. **`src/cli/filter_run.zig`** -> AI Confidence: **99.34%**
99. **`src/cli/install_completions_command.zig`** -> AI Confidence: **99.34%**
100. **`src/cli/pm_view_command.zig`** -> AI Confidence: **99.34%**
101. **`src/crash_handler.zig`** -> AI Confidence: **99.34%**
102. **`src/css/properties/border.zig`** -> AI Confidence: **99.34%**
103. **`src/install/PackageManager/install_with_manager.zig`** -> AI Confidence: **99.34%**
104. **`src/install/lockfile/Package.zig`** -> AI Confidence: **99.34%**
105. **`src/js_lexer.zig`** -> AI Confidence: **99.34%**
106. **`src/md/blocks.zig`** -> AI Confidence: **99.34%**
107. **`src/md/html_renderer.zig`** -> AI Confidence: **99.34%**
108. **`src/md/inlines.zig`** -> AI Confidence: **99.34%**
109. **`src/md/links.zig`** -> AI Confidence: **99.34%**
110. **`src/md/render_blocks.zig`** -> AI Confidence: **99.34%**
111. **`src/paths.zig`** -> AI Confidence: **99.34%**
112. **`src/s3/credentials.zig`** -> AI Confidence: **99.34%**
113. **`src/sql/mysql/protocol/ColumnDefinition41.zig`** -> AI Confidence: **99.34%**
114. **`src/sql/mysql/protocol/HandshakeResponse41.zig`** -> AI Confidence: **99.34%**
115. **`src/sql/mysql/protocol/Query.zig`** -> AI Confidence: **99.34%**
116. **`src/sql/postgres/protocol/Parse.zig`** -> AI Confidence: **99.34%**
117. **`src/sql/postgres/protocol/PasswordMessage.zig`** -> AI Confidence: **99.34%**
118. **`src/sql/postgres/protocol/SASLInitialResponse.zig`** -> AI Confidence: **99.34%**
119. **`src/sql/postgres/protocol/SASLResponse.zig`** -> AI Confidence: **99.34%**
120. **`src/sql/postgres/protocol/StartupMessage.zig`** -> AI Confidence: **99.34%**
121. **`src/windows.zig`** -> AI Confidence: **99.34%**
122. **`src/js/node/assert.ts`** -> AI Confidence: **99.33%**
123. **`src/js/internal/streams/transform.ts`** -> AI Confidence: **99.32%**
124. **`src/js/node/_http_common.ts`** -> AI Confidence: **99.32%**
125. **`src/js/node/cluster.ts`** -> AI Confidence: **99.32%**
126. **`dockerhub/debian/Dockerfile`** -> AI Confidence: **99.32%**
127. **`dockerhub/distroless/Dockerfile`** -> AI Confidence: **99.32%**
128. **`src/bun.js/bindings/webcore/HTTPHeaderNames.cpp`** -> AI Confidence: **99.32%**
129. **`src/bun.js/api/server/HTMLBundle.zig`** -> AI Confidence: **99.32%**
130. **`src/bun.js/bindings/ZigStackFrame.zig`** -> AI Confidence: **99.32%**
131. **`src/bun.js/test/diff/printDiff.zig`** -> AI Confidence: **99.32%**
132. **`src/bundler/linker_context/postProcessJSChunk.zig`** -> AI Confidence: **99.32%**
133. **`src/cli/publish_command.zig`** -> AI Confidence: **99.32%**
134. **`src/css/properties/animation.zig`** -> AI Confidence: **99.32%**
135. **`src/css/properties/box_shadow.zig`** -> AI Confidence: **99.32%**
136. **`src/css/properties/flex.zig`** -> AI Confidence: **99.32%**
137. **`src/css/properties/prefix_handler.zig`** -> AI Confidence: **99.32%**
138. **`src/css/rules/custom_media.zig`** -> AI Confidence: **99.32%**
139. **`src/css/rules/import.zig`** -> AI Confidence: **99.32%**
140. **`src/css/rules/namespace.zig`** -> AI Confidence: **99.32%**
141. **`src/css/rules/unknown.zig`** -> AI Confidence: **99.32%**
142. **`src/defines-table.zig`** -> AI Confidence: **99.32%**
143. **`src/http/Decompressor.zig`** -> AI Confidence: **99.32%**
144. **`src/http/HeaderBuilder.zig`** -> AI Confidence: **99.32%**
145. **`src/install/NetworkTask.zig`** -> AI Confidence: **99.32%**
146. **`src/install/PackageManager/PackageManagerOptions.zig`** -> AI Confidence: **99.32%**
147. **`src/md/containers.zig`** -> AI Confidence: **99.32%**
148. **`src/safety/CriticalSection.zig`** -> AI Confidence: **99.32%**
149. **`src/sql/mysql/MySQLRequest.zig`** -> AI Confidence: **99.32%**
150. **`src/sql/mysql/MySQLRequestQueue.zig`** -> AI Confidence: **99.32%**
151. **`src/sql/mysql/protocol/OKPacket.zig`** -> AI Confidence: **99.32%**
152. **`src/sql/postgres/SocketMonitor.zig`** -> AI Confidence: **99.32%**
153. **`src/sql/postgres/protocol/Close.zig`** -> AI Confidence: **99.32%**
154. **`src/sql/postgres/protocol/DataRow.zig`** -> AI Confidence: **99.32%**
155. **`src/sql/postgres/protocol/Describe.zig`** -> AI Confidence: **99.32%**
156. **`packages/bun-usockets/generate-root-certs.mjs`** -> AI Confidence: **99.31%**
157. **`src/css/build-prefixes.js`** -> AI Confidence: **99.31%**
158. **`packages/bun-debug-adapter-protocol/src/debugger/adapter.ts`** -> AI Confidence: **99.31%**
159. **`packages/bun-vscode/src/features/debug.ts`** -> AI Confidence: **99.31%**
160. **`src/bake/bun-framework-react/ssr.tsx`** -> AI Confidence: **99.31%**
161. **`src/codegen/bundle-functions.ts`** -> AI Confidence: **99.31%**
162. **`src/js/bun/sql.ts`** -> AI Confidence: **99.31%**
163. **`src/js/eval/feedback.ts`** -> AI Confidence: **99.31%**
164. **`src/js/internal/fs/streams.ts`** -> AI Confidence: **99.31%**
165. **`src/js/internal/streams/duplex.ts`** -> AI Confidence: **99.31%**
166. **`src/js/internal/streams/duplexify.ts`** -> AI Confidence: **99.31%**
167. **`src/js/internal/webstreams_adapters.ts`** -> AI Confidence: **99.31%**
168. **`src/js/node/dgram.ts`** -> AI Confidence: **99.31%**
169. **`src/js/node/fs.promises.ts`** -> AI Confidence: **99.31%**
170. **`src/js/node/fs.ts`** -> AI Confidence: **99.31%**
171. **`packages/bun-usockets/src/crypto/root_certs.cpp`** -> AI Confidence: **99.31%**
172. **`packages/bun-uws/src/App.h`** -> AI Confidence: **99.31%**
173. **`src/bun.js/bindings/AsymmetricKeyValue.cpp`** -> AI Confidence: **99.31%**
174. **`src/bun.js/bindings/BunAnalyzeTranspiledModule.cpp`** -> AI Confidence: **99.31%**
175. **`src/bun.js/bindings/BunCPUProfiler.cpp`** -> AI Confidence: **99.31%**
176. **`src/bun.js/bindings/BunDebugger.cpp`** -> AI Confidence: **99.31%**
177. **`src/bun.js/bindings/BunProcess.cpp`** -> AI Confidence: **99.31%**
178. **`src/bun.js/bindings/ConsoleObject.cpp`** -> AI Confidence: **99.31%**
179. **`src/bun.js/bindings/Cookie.cpp`** -> AI Confidence: **99.31%**
180. **`src/bun.js/bindings/ErrorStackTrace.cpp`** -> AI Confidence: **99.31%**
181. **`src/bun.js/bindings/FuzzilliREPRL.cpp`** -> AI Confidence: **99.31%**
182. **`src/bun.js/bindings/ImportMetaObject.cpp`** -> AI Confidence: **99.31%**
183. **`src/bun.js/bindings/InspectorTestReporterAgent.cpp`** -> AI Confidence: **99.31%**
184. **`src/bun.js/bindings/JSSecrets.cpp`** -> AI Confidence: **99.31%**
185. **`src/bun.js/bindings/NodeVM.cpp`** -> AI Confidence: **99.31%**
186. **`src/bun.js/bindings/NodeVMScript.cpp`** -> AI Confidence: **99.31%**
187. **`src/bun.js/bindings/NodeVMSourceTextModule.cpp`** -> AI Confidence: **99.31%**
188. **`src/bun.js/bindings/SQLClient.cpp`** -> AI Confidence: **99.31%**
189. **`src/bun.js/bindings/ScriptExecutionContext.cpp`** -> AI Confidence: **99.31%**
190. **`src/bun.js/bindings/SecretsDarwin.cpp`** -> AI Confidence: **99.31%**
191. **`src/bun.js/bindings/TextCodecCJK.cpp`** -> AI Confidence: **99.31%**
192. **`src/bun.js/bindings/ZigException.cpp`** -> AI Confidence: **99.31%**
193. **`src/bun.js/bindings/c-bindings.cpp`** -> AI Confidence: **99.31%**
194. **`src/bun.js/bindings/libuv/uv/unix.h`** -> AI Confidence: **99.31%**
195. **`src/bun.js/bindings/node/crypto/CryptoGenKeyPair.cpp`** -> AI Confidence: **99.31%**
196. **`src/bun.js/bindings/node/crypto/JSCipher.cpp`** -> AI Confidence: **99.31%**
197. **`src/bun.js/bindings/node/crypto/JSCipherConstructor.cpp`** -> AI Confidence: **99.31%**
198. **`src/bun.js/bindings/node/crypto/JSCipherPrototype.cpp`** -> AI Confidence: **99.31%**
199. **`src/bun.js/bindings/node/crypto/JSDiffieHellmanConstructor.cpp`** -> AI Confidence: **99.31%**
200. **`src/bun.js/bindings/sqlite/JSSQLStatement.cpp`** -> AI Confidence: **99.31%**
201. **`src/bun.js/bindings/webcore/EventTarget.cpp`** -> AI Confidence: **99.31%**
202. **`src/bun.js/bindings/webcore/HTTPParsers.cpp`** -> AI Confidence: **99.31%**
203. **`src/bun.js/bindings/webcore/JSMIMEType.cpp`** -> AI Confidence: **99.31%**
204. **`src/bun.js/bindings/webcore/JSPerformanceMeasureOptions.cpp`** -> AI Confidence: **99.31%**
205. **`src/bun.js/bindings/webcore/MessageEvent.cpp`** -> AI Confidence: **99.31%**
206. **`src/bun.js/bindings/webcore/Performance.cpp`** -> AI Confidence: **99.31%**
207. **`src/bun.js/bindings/webcore/PerformanceMark.cpp`** -> AI Confidence: **99.31%**
208. **`src/bun.js/bindings/webcore/SerializedScriptValue.cpp`** -> AI Confidence: **99.31%**
209. **`src/bun.js/bindings/webcore/StructuredClone.cpp`** -> AI Confidence: **99.31%**
210. **`src/bun.js/bindings/webcore/URLPattern.cpp`** -> AI Confidence: **99.31%**
211. **`src/bun.js/bindings/webcore/URLPatternConstructorStringParser.cpp`** -> AI Confidence: **99.31%**
212. **`src/bun.js/bindings/webcore/URLPatternParser.cpp`** -> AI Confidence: **99.31%**
213. **`src/bun.js/bindings/webcore/WebSocket.cpp`** -> AI Confidence: **99.31%**
214. **`src/bun.js/bindings/webcore/Worker.cpp`** -> AI Confidence: **99.31%**
215. **`src/bun.js/bindings/webcrypto/CryptoAlgorithmAES_CTR.cpp`** -> AI Confidence: **99.31%**
216. **`src/bun.js/bindings/webcrypto/CryptoAlgorithmECDSA.cpp`** -> AI Confidence: **99.31%**
217. **`src/bun.js/bindings/webcrypto/CryptoAlgorithmRSASSA_PKCS1_v1_5.cpp`** -> AI Confidence: **99.31%**
218. **`src/bun.js/bindings/webcrypto/CryptoAlgorithmRSA_PSS.cpp`** -> AI Confidence: **99.31%**
219. **`src/bun.js/bindings/webcrypto/CryptoAlgorithmX25519.cpp`** -> AI Confidence: **99.31%**
220. **`src/bun.js/bindings/webcrypto/CryptoKey.cpp`** -> AI Confidence: **99.31%**
221. **`src/bun.js/bindings/webcrypto/CryptoKeyAES.cpp`** -> AI Confidence: **99.31%**
222. **`src/bun.js/bindings/webcrypto/CryptoKeyHMAC.cpp`** -> AI Confidence: **99.31%**
223. **`src/bun.js/bindings/webcrypto/CryptoKeyOKPOpenSSL.cpp`** -> AI Confidence: **99.31%**
224. **`src/bun.js/bindings/webcrypto/CryptoKeyRSAOpenSSL.cpp`** -> AI Confidence: **99.31%**
225. **`src/bun.js/bindings/webcrypto/JSAesCbcCfbParams.cpp`** -> AI Confidence: **99.31%**
226. **`src/bun.js/bindings/webcrypto/JSAesCtrParams.cpp`** -> AI Confidence: **99.31%**
227. **`src/bun.js/bindings/webcrypto/JSAesGcmParams.cpp`** -> AI Confidence: **99.31%**
228. **`src/bun.js/bindings/webcrypto/JSCryptoHmacKeyAlgorithm.cpp`** -> AI Confidence: **99.31%**
229. **`src/bun.js/bindings/webcrypto/JSCryptoRsaHashedKeyAlgorithm.cpp`** -> AI Confidence: **99.31%**
230. **`src/bun.js/bindings/webcrypto/JSCryptoRsaKeyAlgorithm.cpp`** -> AI Confidence: **99.31%**
231. **`src/bun.js/bindings/webcrypto/JSEcdsaParams.cpp`** -> AI Confidence: **99.31%**
232. **`src/bun.js/bindings/webcrypto/JSHkdfParams.cpp`** -> AI Confidence: **99.31%**
233. **`src/bun.js/bindings/webcrypto/JSHmacKeyParams.cpp`** -> AI Confidence: **99.31%**
234. **`src/bun.js/bindings/webcrypto/JSPbkdf2Params.cpp`** -> AI Confidence: **99.31%**
235. **`src/bun.js/bindings/webcrypto/JSRsaHashedImportParams.cpp`** -> AI Confidence: **99.31%**
236. **`src/bun.js/bindings/webcrypto/JSRsaHashedKeyGenParams.cpp`** -> AI Confidence: **99.31%**
237. **`src/bun.js/bindings/webcrypto/JSRsaOaepParams.cpp`** -> AI Confidence: **99.31%**
238. **`src/bun.js/bindings/webcrypto/SubtleCrypto.cpp`** -> AI Confidence: **99.31%**
239. **`src/bun.js/bindings/windows/rescle.cpp`** -> AI Confidence: **99.31%**
240. **`src/bun.js/bindings/workaround-missing-symbols.cpp`** -> AI Confidence: **99.31%**
241. **`src/bun.js/bindings/wtf-bindings.cpp`** -> AI Confidence: **99.31%**
242. **`src/bun.js/modules/NodeConstantsModule.h`** -> AI Confidence: **99.31%**
243. **`src/bun.js/webview/ChromeBackend.cpp`** -> AI Confidence: **99.31%**
244. **`src/bun.js/webview/host_main.cpp`** -> AI Confidence: **99.31%**
245. **`misctools/http_bench.zig`** -> AI Confidence: **99.31%**
246. **`misctools/machbench.zig`** -> AI Confidence: **99.31%**
247. **`src/allocators.zig`** -> AI Confidence: **99.31%**
248. **`src/ast.zig`** -> AI Confidence: **99.31%**
249. **`src/bun.js/AsyncModule.zig`** -> AI Confidence: **99.31%**
250. **`src/bun.js/RuntimeTranspilerStore.zig`** -> AI Confidence: **99.31%**
251. **`src/bun.js/api/BunObject.zig`** -> AI Confidence: **99.31%**
252. **`src/bun.js/api/JSTranspiler.zig`** -> AI Confidence: **99.31%**
253. **`src/bun.js/api/filesystem_router.zig`** -> AI Confidence: **99.31%**
254. **`src/bun.js/rare_data.zig`** -> AI Confidence: **99.31%**
255. **`src/bun.js/test/bun_test.zig`** -> AI Confidence: **99.31%**
256. **`src/bun.js/test/expect.zig`** -> AI Confidence: **99.31%**
257. **`src/bun.js/webcore.zig`** -> AI Confidence: **99.31%**
258. **`src/bun.js/webcore/Blob.zig`** -> AI Confidence: **99.31%**
259. **`src/cli.zig`** -> AI Confidence: **99.31%**
260. **`src/http/AsyncHTTP.zig`** -> AI Confidence: **99.31%**
261. **`src/install/install.zig`** -> AI Confidence: **99.31%**
262. **`src/install/resolvers/folder_resolver.zig`** -> AI Confidence: **99.31%**
263. **`src/js_parser.zig`** -> AI Confidence: **99.31%**
264. **`src/md/parser.zig`** -> AI Confidence: **99.31%**
265. **`src/shell/interpreter.zig`** -> AI Confidence: **99.31%**
266. **`src/sql/mysql/MySQLConnection.zig`** -> AI Confidence: **99.31%**
267. **`src/sql/mysql/MySQLQuery.zig`** -> AI Confidence: **99.31%**
268. **`src/sql/mysql/MySQLStatement.zig`** -> AI Confidence: **99.31%**
269. **`src/sql/mysql/js/JSMySQLConnection.zig`** -> AI Confidence: **99.31%**
270. **`src/sql/mysql/js/JSMySQLQuery.zig`** -> AI Confidence: **99.31%**
271. **`src/sql/postgres/PostgresSQLConnection.zig`** -> AI Confidence: **99.31%**
272. **`src/sql/postgres/PostgresSQLQuery.zig`** -> AI Confidence: **99.31%**
273. **`src/sql/postgres/PostgresSQLStatement.zig`** -> AI Confidence: **99.31%**
274. **`src/sql/postgres/types/Tag.zig`** -> AI Confidence: **99.31%**
275. **`src/string/immutable.zig`** -> AI Confidence: **99.31%**
276. **`packages/bun-usockets/src/bsd.c`** -> AI Confidence: **99.31%**
277. **`src/bun.js/bindings/uv-posix-polyfills.c`** -> AI Confidence: **99.31%**
278. **`.claude/hooks/post-edit-zig-format.js`** -> AI Confidence: **99.29%**
279. **`bench/snippets/runner-entrypoint.js`** -> AI Confidence: **99.29%**
280. **`bench/snippets/semver.mjs`** -> AI Confidence: **99.29%**
281. **`misctools/publish-examples.js`** -> AI Confidence: **99.29%**
282. **`src/node-fallbacks/net.js`** -> AI Confidence: **99.29%**
283. **`misctools/bun-feature-data.ts`** -> AI Confidence: **99.29%**
284. **`packages/bun-error/stack-trace-parser.ts`** -> AI Confidence: **99.29%**
285. **`packages/bun-vscode/example/print.ts`** -> AI Confidence: **99.29%**
286. **`src/bake/client/css-reloader.ts`** -> AI Confidence: **99.29%**
287. **`src/bake/debug.ts`** -> AI Confidence: **99.29%**
288. **`src/codegen/builtin-parser.ts`** -> AI Confidence: **99.29%**
289. **`src/js/eval/fuzzilli-reprl.ts`** -> AI Confidence: **99.29%**
290. **`src/js/internal/assert/assertion_error.ts`** -> AI Confidence: **99.29%**
291. **`src/js/internal/assert/myers_diff.ts`** -> AI Confidence: **99.29%**
292. **`src/js/internal/html.ts`** -> AI Confidence: **99.29%**
293. **`src/js/internal/net/isIP.ts`** -> AI Confidence: **99.29%**
294. **`src/js/internal/sql/shared.ts`** -> AI Confidence: **99.29%**
295. **`src/js/internal/streams/destroy.ts`** -> AI Confidence: **99.29%**
296. **`src/js/internal/url.ts`** -> AI Confidence: **99.29%**
297. **`src/js/internal/validators.ts`** -> AI Confidence: **99.29%**
298. **`src/js/node/querystring.ts`** -> AI Confidence: **99.29%**
299. **`src/js/node/url.ts`** -> AI Confidence: **99.29%**
300. **`dockerhub/alpine/Dockerfile`** -> AI Confidence: **99.29%**
301. **`dockerhub/debian-slim/Dockerfile`** -> AI Confidence: **99.29%**
302. **`packages/bun-usockets/src/crypto/root_certs_header.h`** -> AI Confidence: **99.29%**
303. **`src/bun.js/api/ffi-stdalign.h`** -> AI Confidence: **99.29%**
304. **`src/bun.js/api/ffi-tgmath.h`** -> AI Confidence: **99.29%**
305. **`src/bun.js/bindings/decodeURIComponentSIMD.cpp`** -> AI Confidence: **99.29%**
306. **`src/bun.js/bindings/dh-primes.h`** -> AI Confidence: **99.29%**
307. **`src/bun.js/bindings/libuv/uv/sunos.h`** -> AI Confidence: **99.29%**
308. **`src/bun.js/bindings/webcore/RFC7230.cpp`** -> AI Confidence: **99.29%**
309. **`src/bun.js/bindings/webcrypto/CryptoKeyRSAComponents.cpp`** -> AI Confidence: **99.29%**
310. **`src/Global.zig`** -> AI Confidence: **99.29%**
311. **`src/api/schema.zig`** -> AI Confidence: **99.29%**
312. **`src/ast/B.zig`** -> AI Confidence: **99.29%**
313. **`src/ast/BundledAst.zig`** -> AI Confidence: **99.29%**
314. **`src/ast/ConvertESMExportsForHmr.zig`** -> AI Confidence: **99.29%**
315. **`src/ast/G.zig`** -> AI Confidence: **99.29%**
316. **`src/ast/foldStringAddition.zig`** -> AI Confidence: **99.29%**
317. **`src/ast/parseFn.zig`** -> AI Confidence: **99.29%**
318. **`src/ast/parseImportExport.zig`** -> AI Confidence: **99.29%**
319. **`src/ast/parseJSXElement.zig`** -> AI Confidence: **99.29%**
320. **`src/ast/parseProperty.zig`** -> AI Confidence: **99.29%**
321. **`src/ast/skipTypescript.zig`** -> AI Confidence: **99.29%**
322. **`src/bake/DevServer/IncrementalGraph.zig`** -> AI Confidence: **99.29%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `src/js/internal/assert/utils.ts` -> **23.7547%** Exposure
- `src/js/internal/html.ts` -> **0.0006%** Exposure
- `src/js/node/assert.ts` -> **0.0004%** Exposure
- `packages/bun-types/bun.d.ts` -> **0.0002%** Exposure
### Exploit Generation Surface
- `.claude/hooks/pre-bash-zig-build.js` -> **100.0%** Exposure
- `packages/bun-usockets/generate-root-certs.mjs` -> **100.0%** Exposure
- `src/api/schema.js` -> **100.0%** Exposure
- `src/js/internal/util/inspect.js` -> **100.0%** Exposure
- `src/js/thirdparty/ws.js` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `.claude/hooks/post-edit-zig-format.js` -> **100.0%** Exposure
- `.claude/hooks/pre-bash-zig-build.js` -> **100.0%** Exposure
- `bench/snippets/http-hello.js` -> **100.0%** Exposure
- `bench/snippets/new-incomingmessage.mjs` -> **100.0%** Exposure
- `packages/bun-usockets/generate-root-certs.mjs` -> **100.0%** Exposure
### Raw Memory Manipulation
- `packages/bun-uws/src/WebSocketContext.h` -> **10.0%** Exposure
- `src/bun.js/bindings/ProcessBindingConstants.cpp` -> **10.0%** Exposure
- `src/bun.js/bindings/node/crypto/JSCipherPrototype.cpp` -> **10.0%** Exposure
- `src/bun.js/bindings/sqlite/sqlite3_local.h` -> **10.0%** Exposure
- `src/bun.js/bindings/webcrypto/JSSubtleCrypto.cpp` -> **10.0%** Exposure
### Hardcoded Payload Artifacts
- `packages/bun-usockets/src/crypto/root_certs.h` -> **100.0%** Exposure
- `packages/bun-usockets/generate-root-certs.pl` -> **95.8312%** Exposure
- `packages/bun-types/globals.d.ts` -> **34.3653%** Exposure
### Algorithmic DoS Exposure
- `bench/react-hello-world/react-hello-world.workerd.jsx` -> **100.0%** Exposure
- `src/js/internal/util/inspect.js` -> **100.0%** Exposure
- `src/js/thirdparty/ws.js` -> **100.0%** Exposure
- `src/node-fallbacks/path.js` -> **100.0%** Exposure
- `src/node-fallbacks/url.js` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `39` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `12294` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/js/internal/sql/mysql.ts` (TYPESCRIPT) -> Cumulative Risk: **1000.02**
- **Archetype:** `file_cluster_4` (Distance: 13.496 IQR)
- **Magnitude:** 236.76 | **LOC:** 1167 | **CtrlFlow:** 69.3% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `normalizeQuery` (Impact: 801.6), `connect` (Impact: 152.6), `detectCommand` (Impact: 127.5)

### 2. `src/js/node/_http_outgoing.ts` (TYPESCRIPT) -> Cumulative Risk: **924.08**
- **Archetype:** `file_cluster_8` (Distance: 12.784 IQR)
- **Magnitude:** 72.89 | **LOC:** 589 | **CtrlFlow:** 72.1% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Tech Debt (99.9998%)
- **Heaviest Functions:** `write_` (Impact: 185.5), `addTrailers` (Impact: 38.9), `ObjectDefineProperty` (Impact: 28.8)

### 3. `src/js/builtins/ReadableStream.ts` (TYPESCRIPT) -> Cumulative Risk: **911.63**
- **Archetype:** `file_cluster_4` (Distance: 11.679 IQR)
- **Magnitude:** 57.67 | **LOC:** 516 | **CtrlFlow:** 52.2% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), State Flux (95.2504%)
- **Heaviest Functions:** `readableStreamToArrayBuffer` (Impact: 95.9), `readableStreamToBytes` (Impact: 91.8), `initializeReadableStream` (Impact: 67.8)

### 4. `src/js/node/events.ts` (TYPESCRIPT) -> Cumulative Risk: **909.45**
- **Archetype:** `file_cluster_8` (Distance: 13.264 IQR)
- **Magnitude:** 119.89 | **LOC:** 866 | **CtrlFlow:** 56.4% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.9995%)
- **Heaviest Functions:** `on` (Impact: 159.2), `emit` (Impact: 111.1), `emit` (Impact: 100.6)

### 5. `src/js/bun/sql.ts` (TYPESCRIPT) -> Cumulative Risk: **894.93**
- **Archetype:** `file_cluster_4` (Distance: 12.092 IQR)
- **Magnitude:** 148.42 | **LOC:** 1078 | **CtrlFlow:** 49.5% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `onTransactionConnected` (Impact: 483.9), `onReserveConnected` (Impact: 216.5), `sql` (Impact: 63.8)

### 6. `src/bake/client/websocket.ts` (TYPESCRIPT) -> Cumulative Risk: **887.77**
- **Archetype:** `file_cluster_4` (Distance: 12.158 IQR)
- **Magnitude:** 19.12 | **LOC:** 199 | **CtrlFlow:** 60.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), Algorithmic Dos (99.1752%)
- **Heaviest Functions:** `onClose` (Impact: 20.0), `sendBuffered` (Impact: 17.4), `onMessage` (Impact: 15.2)

### 7. `src/js/builtins/ReadableStreamInternals.ts` (TYPESCRIPT) -> Cumulative Risk: **883.77**
- **Archetype:** `file_cluster_8` (Distance: 12.52 IQR)
- **Magnitude:** 222.46 | **LOC:** 2431 | **CtrlFlow:** 52.0% | **Authorship Centralization:** 42.9%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `readableStreamFromAsyncIterator` (Impact: 894.4), `readStreamIntoSink` (Impact: 119.3), `readableStreamPipeToWritableStream` (Impact: 61.2)

### 8. `packages/bun-release/src/fetch.ts` (TYPESCRIPT) -> Cumulative Risk: **883.66**
- **Archetype:** `file_cluster_4` (Distance: 10.317 IQR)
- **Magnitude:** 13.66 | **LOC:** 71 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `get` (Impact: 73.1), `debug` (Impact: 21.1), `isRedirect` (Impact: 14.6)

### 9. `src/bun.js/bindings/webcore/JSDOMPromiseDeferred.h` (CPP) -> Cumulative Risk: **862.18**
- **Archetype:** `file_cluster_8` (Distance: 12.99 IQR)
- **Magnitude:** 450.36 | **LOC:** 403 | **CtrlFlow:** 15.3% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `settle` (Impact: 10.8), `settle` (Impact: 10.8), `DOMPromiseDeferredBase` (Impact: 10.6)

### 10. `src/js/node/net.ts` (TYPESCRIPT) -> Cumulative Risk: **857.39**
- **Archetype:** `file_cluster_8` (Distance: 12.474 IQR)
- **Magnitude:** 130.67 | **LOC:** 2658 | **CtrlFlow:** 77.1% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Tech Debt (99.9775%)
- **Heaviest Functions:** `listen` (Impact: 293.3), `handshake` (Impact: 91.9), `open` (Impact: 66.9)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/bun.js/node/node_fs.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.781 IQR)
- **Top Global Matches:** file_cluster_8: 13.781, file_cluster_0: 13.983, file_cluster_7: 14.046
- **Magnitude:** 18963.46 | **LOC:** 7058 | **CtrlFlow:** 70.3% | **Authorship Centralization:** 25.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 31
- **Risk Profile:** Cognitive Load (37.4805%), Tech Debt (99.8857%)
**Top Internal Functions/Classes:**
  * `_copySingleFileSync` (Impact: 1339.5 | O(N^6) | DB: 31)
    * *Intent:* /// This is `copyFile`, but it copies symlinks as-is
  * `cpSyncInner` (Impact: 1017.8 | O(2^N) | DB: 8)
  * `readFileWithOptions` (Impact: 900.9 | O(N^6) | DB: 7)
  * `NewAsyncCpTask` (Impact: 695.9 | O(N^6) | DB: 26)
  * `fromJS` (Impact: 623.8 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1889`, `structural_boundaries: 797`, `args: 280`, `func_start: 279`, `class_start: 63`
* *Risk/State:* `safety_bypasses: 152`, `state_mutation: 506`, `dead_code: 12`, `planned_debt: 13`, `fragile_debt: 3`, `duplicate_logic: 147`
* *Architecture:* `io: 41`, `api: 425`, `concurrency: 6`, `import: 8`
* *Defense:* `safety: 681`, `doc: 107`, `sync_locks: 3`, `immutability_locks: 636`, `cleanup: 156`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node_fs_watcher.zig, bun, node_fs_binding.zig, node_fs_stat_watcher.zig, fs.zig, std, dir_iterator.zig, node_fs_constant.zig
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ast/P.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.368 IQR)
- **Top Global Matches:** file_cluster_8: 14.368, file_cluster_0: 14.395, file_cluster_11: 14.451
- **Magnitude:** 17404.88 | **LOC:** 6967 | **CtrlFlow:** 71.5% | **Authorship Centralization:** 27.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 31
- **Risk Profile:** Cognitive Load (25.6539%), Tech Debt (12.779%)
**Top Internal Functions/Classes:**
  * `substituteSingleUseSymbolInExpr` (Impact: 2113.5 | O(2^N) | DB: 8)
  * `NewParser_` (Impact: 1582.5 | O(N^6) | DB: 21)
  * `exprCanBeRemovedIfUnusedWithoutDCECheck` (Impact: 824.0 | O(2^N))
  * `lowerClass` (Impact: 814.4 | O(N^6) | DB: 31)
  * `processImportStatement` (Impact: 680.8 | O(N^6) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1781`, `structural_boundaries: 711`, `args: 151`, `func_start: 144`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 192`, `high_risk_execution: 2`, `state_mutation: 615`, `dead_code: 53`, `planned_debt: 20`, `fragile_debt: 5`, `duplicate_logic: 2`
* *Architecture:* `api: 292`, `concurrency: 31`, `import: 12`
* *Defense:* `safety: 683`, `doc: 105`, `immutability_locks: 556`, `cleanup: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std, lowerDecorators.zig, symbols.zig, defines.zig, bun, parse.zig, repl_transforms.zig, maybe.zig...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/js_printer.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.998 IQR)
- **Top Global Matches:** file_cluster_8: 12.998, file_cluster_0: 13.292, file_cluster_7: 13.368
- **Magnitude:** 16055.16 | **LOC:** 6399 | **CtrlFlow:** 80.1% | **Authorship Centralization:** 24.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 29
- **Risk Profile:** Cognitive Load (30.9515%), Tech Debt (13.8168%)
**Top Internal Functions/Classes:**
  * `printExpr` (Impact: 4032.8 | O(2^N) | DB: 14)
  * `NewPrinter` (Impact: 3036.4 | O(N^6) | DB: 28)
  * `printStmt` (Impact: 2752.8 | O(2^N) | DB: 11)
  * `printAst` (Impact: 1039.4 | O(N^5) | DB: 29)
  * `printBinding` (Impact: 765.0 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1406`, `structural_boundaries: 349`, `args: 171`, `func_start: 169`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 82`, `high_risk_execution: 2`, `state_mutation: 348`, `dead_code: 30`, `planned_debt: 14`, `fragile_debt: 3`, `duplicate_logic: 5`
* *Architecture:* `io: 3`, `api: 203`, `concurrency: 6`, `import: 9`
* *Defense:* `safety: 380`, `doc: 12`, `test: 2`, `immutability_locks: 405`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` sourcemap.zig, import_record.zig, runtime.zig, bun, options.zig, fs.zig, renamer.zig, std...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/bun.js/api/bun/h2_frame_parser.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.14%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.276 IQR)
- **Top Global Matches:** file_cluster_8: 13.276, file_cluster_0: 13.524, file_cluster_11: 13.543
- **Magnitude:** 15356.18 | **LOC:** 4840 | **CtrlFlow:** 69.4% | **Authorship Centralization:** 25.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 49
- **Risk Profile:** Cognitive Load (56.6711%), Tech Debt (38.8015%)
**Top Internal Functions/Classes:**
  * `toValidHeaderName` (Impact: 4647.9 | O(2^N) | DB: 49)
    * *Intent:* /// validate header name and convert to lowecase if needed
  * `constructor` (Impact: 861.9 | O(2^N) | DB: 5)
  * `decodeHeaderBlock` (Impact: 724.8 | O(2^N) | DB: 4)
  * `loadSettingsFromJSValue` (Impact: 559.5 | O(N^6) | DB: 2)
  * `sendData` (Impact: 536.3 | O(2^N) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1516`, `structural_boundaries: 670`, `args: 146`, `func_start: 146`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 109`, `state_mutation: 478`, `dead_code: 10`, `planned_debt: 9`, `duplicate_logic: 21`
* *Architecture:* `io: 14`, `api: 158`, `concurrency: 7`, `import: 3`
* *Defense:* `safety: 368`, `doc: 36`, `immutability_locks: 490`, `cleanup: 42`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std, bun, lshpack.zig
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/interchange/yaml.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.412 IQR)
- **Top Global Matches:** file_cluster_0: 14.412, file_cluster_9: 14.443, file_cluster_8: 14.458
- **Magnitude:** 13145.44 | **LOC:** 5741 | **CtrlFlow:** 78.1% | **Authorship Centralization:** 45.5%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 19
- **Risk Profile:** Cognitive Load (29.5564%), Tech Debt (51.1139%)
**Top Internal Functions/Classes:**
  * `Parser` (Impact: 5692.7 | O(2^N) | DB: 19)
  * `scanBlockHeader` (Impact: 4359.9 | O(2^N) | DB: 19)
    * *Intent:* // positions parser at the first line break, or eof
  * `scanPlainScalar` (Impact: 1613.3 | O(N^6) | DB: 11)
  * `chars` (Impact: 513.2 | O(N^6))
  * `parse` (Impact: 121.4 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1496`, `structural_boundaries: 420`, `args: 225`, `func_start: 204`, `class_start: 46`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 191`, `dead_code: 108`, `planned_debt: 17`, `fragile_debt: 1`, `duplicate_logic: 29`
* *Architecture:* `api: 190`, `import: 2`
* *Defense:* `safety: 470`, `doc: 56`, `immutability_locks: 343`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.469
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std, bun
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/resolver/resolver.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.885 IQR)
- **Top Global Matches:** file_cluster_8: 13.885, file_cluster_0: 13.975, file_cluster_13: 13.99
- **Magnitude:** 11577.38 | **LOC:** 4406 | **CtrlFlow:** 71.5% | **Authorship Centralization:** 35.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 40
- **Risk Profile:** Cognitive Load (29.795%), Tech Debt (17.1756%)
**Top Internal Functions/Classes:**
  * `resolveAndAutoInstall` (Impact: 2649.8 | O(2^N) | DB: 9)
  * `dirInfoUncached` (Impact: 1311.1 | O(N^6) | DB: 16)
  * `dirInfoCachedMaybeLog` (Impact: 831.4 | O(N^6) | DB: 40)
  * `resolveWithoutSymlinks` (Impact: 641.5 | O(N^6) | DB: 10)
  * `enqueueDependencyToResolve` (Impact: 488.2 | O(2^N) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1264`, `structural_boundaries: 505`, `args: 78`, `func_start: 77`, `class_start: 27`
* *Risk/State:* `safety_bypasses: 96`, `high_risk_execution: 1`, `state_mutation: 428`, `dead_code: 22`, `planned_debt: 9`, `fragile_debt: 2`, `duplicate_logic: 6`
* *Architecture:* `io: 51`, `api: 135`, `import: 23`
* *Defense:* `safety: 420`, `doc: 51`, `sync_locks: 16`, `immutability_locks: 335`, `cleanup: 20`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` resolution.zig, options.zig, system_timer.zig, dir_info.zig, cache.zig, dependency.zig, tsconfig_json.zig, bun...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/crash_handler.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.582 IQR)
- **Top Global Matches:** file_cluster_8: 13.582, file_cluster_0: 13.698, file_cluster_7: 13.746
- **Magnitude:** 11479.38 | **LOC:** 2308 | **CtrlFlow:** 78.9% | **Authorship Centralization:** 29.4%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 247
- **Risk Profile:** Cognitive Load (39.6927%), Tech Debt (18.9347%)
**Top Internal Functions/Classes:**
  * `crashHandler` (Impact: 6371.1 | O(2^N) | DB: 247)
    * *Intent:* /// This function is invoked when a crash happens. A crash is classified in `CrashReason`.
  * `coldHandleErrorReturnTrace` (Impact: 4403.9 | O(2^N) | DB: 76)
  * `report` (Impact: 186.5 | O(N^6) | DB: 19)
    * *Intent:* /// Bun automatically reports crashes on Windows and macOS /// /// These URLs contain no source code...
  * `format` (Impact: 86.6 | O(N^6))
  * `format` (Impact: 42.3 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 733`, `structural_boundaries: 196`, `args: 67`, `func_start: 66`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 54`, `high_risk_execution: 7`, `state_mutation: 215`, `dead_code: 5`, `planned_debt: 4`, `fragile_debt: 4`, `duplicate_logic: 2`
* *Architecture:* `io: 102`, `api: 56`, `concurrency: 18`, `import: 5`
* *Defense:* `safety: 315`, `doc: 114`, `test: 3`, `sync_locks: 10`, `immutability_locks: 188`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` sourcemap.zig, CPUFeatures.zig, bun, std, builtin
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/deps/boringssl.translated.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.8 IQR)
- **Top Global Matches:** file_cluster_8: 13.8, file_cluster_13: 14.101, file_cluster_7: 14.105
- **Magnitude:** 10821.3 | **LOC:** 19292 | **CtrlFlow:** 70.8% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (7.1654%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ref` (Impact: 5.4 | O(N^2))
  * `dup` (Impact: 5.3 | O(N^2))
  * `sk_void_call_cmp_func` (Impact: 4.4 | O(N^1) | DB: 2)
  * `sk_OPENSSL_STRING_call_cmp_func` (Impact: 4.4 | O(N^1) | DB: 2)
  * `sk_BIO_call_cmp_func` (Impact: 4.4 | O(N^1) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1472`, `structural_boundaries: 606`, `args: 3266`, `func_start: 2889`, `class_start: 169`
* *Risk/State:* `safety_bypasses: 1814`, `state_mutation: 120`, `dead_code: 226`
* *Architecture:* `api: 9480`, `import: 191`
* *Defense:* `safety: 25`, `doc: 34`, `immutability_locks: 9873`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std, bun
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/bun.js/test/pretty_format.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.343 IQR)
- **Top Global Matches:** file_cluster_8: 12.343, file_cluster_0: 12.766, file_cluster_7: 12.781
- **Magnitude:** 10815.94 | **LOC:** 2147 | **CtrlFlow:** 73.9% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 38
- **Risk Profile:** Cognitive Load (24.2608%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `writeWithFormatting` (Impact: 8411.2 | O(2^N) | DB: 38)
  * `format` (Impact: 1036.7 | O(2^N) | DB: 4)
  * `printAsymmetricMatcher` (Impact: 519.0 | O(N^5) | DB: 1)
  * `get` (Impact: 481.0 | O(2^N) | DB: 2)
  * `printAsymmetricMatcherPromisePrefix` (Impact: 24.8 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 661`, `structural_boundaries: 234`, `args: 30`, `func_start: 30`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 56`, `state_mutation: 135`, `dead_code: 1`, `planned_debt: 6`, `duplicate_logic: 3`
* *Architecture:* `api: 42`, `import: 4`
* *Defense:* `safety: 251`, `doc: 3`, `immutability_locks: 136`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std, pool.zig, expect.zig, bun
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/bun.js/webcore/Blob.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.942 IQR)
- **Top Global Matches:** file_cluster_8: 13.942, file_cluster_0: 14.093, file_cluster_11: 14.122
- **Magnitude:** 10708.86 | **LOC:** 4972 | **CtrlFlow:** 68.5% | **Authorship Centralization:** 22.6%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 19
- **Risk Profile:** Cognitive Load (30.0871%), Tech Debt (88.4399%)
**Top Internal Functions/Classes:**
  * `writeFileInternal` (Impact: 781.9 | O(N^6) | DB: 8)
    * *Intent:* /// ## Errors /// - If `path_or_blob` is a detached blob /// ## Panics /// - If `path_or_blob` is a ...
  * `fromJSWithoutDeferGC` (Impact: 655.8 | O(N^6) | DB: 19)
  * `getWriter` (Impact: 635.7 | O(N^6) | DB: 11)
  * `writeFileWithSourceDestination` (Impact: 535.3 | O(N^6) | DB: 6)
  * `pipeReadableStreamToBlob` (Impact: 511.3 | O(N^6) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1419`, `structural_boundaries: 653`, `args: 212`, `func_start: 208`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 96`, `state_mutation: 497`, `dead_code: 15`, `planned_debt: 17`, `fragile_debt: 3`, `duplicate_logic: 47`
* *Architecture:* `io: 4`, `api: 253`, `concurrency: 7`, `import: 9`
* *Defense:* `safety: 411`, `doc: 69`, `immutability_locks: 438`, `cleanup: 82`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` env.zig, S3File.zig, read_file.zig, bun, write_file.zig, Store.zig, Archive.zig, std...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/bun.js/ConsoleObject.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.966 IQR)
- **Top Global Matches:** file_cluster_8: 12.966, file_cluster_0: 13.266, file_cluster_11: 13.275
- **Magnitude:** 10599.16 | **LOC:** 3824 | **CtrlFlow:** 76.9% | **Authorship Centralization:** 35.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 31
- **Risk Profile:** Cognitive Load (50.6116%), Tech Debt (25.2618%)
**Top Internal Functions/Classes:**
  * `PropertyIterator` (Impact: 4734.8 | O(2^N) | DB: 31)
  * `writeWithFormatting` (Impact: 682.6 | O(N^6) | DB: 8)
  * `messageWithTypeAndLevel_` (Impact: 605.7 | O(N^5) | DB: 6)
  * `printTable` (Impact: 582.1 | O(N^6) | DB: 7)
  * `format2` (Impact: 474.5 | O(N^5) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1154`, `structural_boundaries: 346`, `args: 66`, `func_start: 66`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 100`, `state_mutation: 276`, `dead_code: 8`, `planned_debt: 17`, `duplicate_logic: 9`
* *Architecture:* `api: 85`, `import: 5`
* *Defense:* `safety: 427`, `doc: 10`, `sync_locks: 7`, `immutability_locks: 238`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pretty_format.zig, pool.zig, bun, cli.zig, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/bun.js/node/path.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.11%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.139 IQR)
- **Top Global Matches:** file_cluster_8: 13.139, file_cluster_0: 13.297, file_cluster_11: 13.297
- **Magnitude:** 10098.8 | **LOC:** 2978 | **CtrlFlow:** 70.3% | **Authorship Centralization:** 22.2%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 20
- **Risk Profile:** Cognitive Load (41.3484%), Tech Debt (8.0638%)
**Top Internal Functions/Classes:**
  * `resolveWindowsT` (Impact: 1252.1 | O(2^N) | DB: 20)
    * *Intent:* /// Based on Node v21.6.1 path.win32.resolve: /// https://github.com/nodejs/node/blob/6ae20aa63de782...
  * `relativeWindowsT` (Impact: 882.1 | O(2^N) | DB: 11)
    * *Intent:* /// Based on Node v21.6.1 path.win32.relative: /// https://github.com/nodejs/node/blob/6ae20aa63de78...
  * `relativePosixT` (Impact: 720.9 | O(2^N) | DB: 8)
    * *Intent:* /// Based on Node v21.6.1 path.posix.relative: /// https://github.com/nodejs/node/blob/6ae20aa63de78...
  * `parseWindowsT` (Impact: 651.8 | O(2^N) | DB: 15)
    * *Intent:* // Based on Node v21.6.1 path.win32.parse // https://github.com/nodejs/node/blob/6ae20aa63de78294b18...
  * `basenameWindowsT` (Impact: 579.1 | O(2^N) | DB: 7)
    * *Intent:* /// Based on Node v21.6.1 path.win32.basename: /// https://github.com/nodejs/node/blob/6ae20aa63de78...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 917`, `structural_boundaries: 388`, `args: 85`, `func_start: 85`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 496`, `dead_code: 14`, `planned_debt: 1`
* *Architecture:* `io: 4`, `api: 112`, `import: 3`
* *Defense:* `safety: 122`, `doc: 57`, `test: 1`, `immutability_locks: 345`, `cleanup: 30`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std, validators.zig, bun
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/bundler/bundle_v2.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.823 IQR)
- **Top Global Matches:** file_cluster_8: 13.823, file_cluster_7: 14.019, file_cluster_13: 14.03
- **Magnitude:** 10074.56 | **LOC:** 5034 | **CtrlFlow:** 78.8% | **Authorship Centralization:** 32.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 45
- **Risk Profile:** Cognitive Load (26.1988%), Tech Debt (14.4688%)
**Top Internal Functions/Classes:**
  * `processServerComponentManifestFiles` (Impact: 3219.8 | O(2^N) | DB: 45)
    * *Intent:* /// This generates the two asts for 'bun:bake/client' and 'bun:bake/server'. Both are generated /// ...
  * `findReachableFiles` (Impact: 899.6 | O(2^N) | DB: 13)
  * `resolveImportRecords` (Impact: 890.8 | O(N^6) | DB: 17)
    * *Intent:* /// Resolve all unresolved import records for a module. Skips records that /// are already resolved ...
  * `onParseTaskComplete` (Impact: 678.8 | O(2^N) | DB: 4)
  * `onResolve` (Impact: 554.4 | O(2^N) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1112`, `structural_boundaries: 300`, `args: 104`, `func_start: 102`, `class_start: 36`
* *Risk/State:* `safety_bypasses: 72`, `state_mutation: 369`, `dead_code: 4`, `planned_debt: 17`, `fragile_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `io: 10`, `api: 253`, `concurrency: 2`, `import: 32`
* *Defense:* `safety: 421`, `doc: 174`, `sync_locks: 4`, `immutability_locks: 500`, `cleanup: 54`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` LinkerContext.zig, PathToSourceIndexMap.zig, LinkerGraph.zig, resolver.zig, ThreadPool.zig, HTMLScanner.zig, AstBuilder.zig, js_lexer.zig...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/sys.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.991 IQR)
- **Top Global Matches:** file_cluster_8: 12.991, file_cluster_0: 13.091, file_cluster_11: 13.16
- **Magnitude:** 9889.26 | **LOC:** 4382 | **CtrlFlow:** 70.3% | **Authorship Centralization:** 31.8%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 24
- **Risk Profile:** Cognitive Load (22.1775%), Tech Debt (10.3887%)
**Top Internal Functions/Classes:**
  * `socketpairImpl` (Impact: 356.1 | O(N^6) | DB: 16)
  * `write` (Impact: 258.4 | O(2^N) | DB: 5)
  * `openFileAtWindowsNtPath` (Impact: 249.4 | O(N^6) | DB: 8)
    * *Intent:* /// you need a reference file descriptor the "invalid_fd" file descriptor is used /// to signify tha...
  * `read` (Impact: 245.4 | O(2^N) | DB: 1)
  * `openDirAtWindowsNtPath` (Impact: 232.3 | O(N^6) | DB: 10)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1328`, `structural_boundaries: 561`, `args: 170`, `func_start: 167`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 139`, `state_mutation: 205`, `dead_code: 24`, `planned_debt: 21`, `fragile_debt: 1`
* *Architecture:* `io: 103`, `api: 332`, `concurrency: 12`, `import: 14`
* *Defense:* `safety: 240`, `doc: 83`, `immutability_locks: 531`, `cleanup: 19`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` libuv_error_map.zig, dir.zig, workaround_missing_symbols.zig, File.zig, bun, Error.zig, PosixStat.zig, std...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/bun.js/api/JSBundler.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.861 IQR)
- **Top Global Matches:** file_cluster_8: 13.861, file_cluster_13: 14.085, file_cluster_0: 14.088
- **Magnitude:** 9377.88 | **LOC:** 2033 | **CtrlFlow:** 73.4% | **Authorship Centralization:** 45.2%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 58
- **Risk Profile:** Cognitive Load (44.6207%), Tech Debt (19.0612%)
**Top Internal Functions/Classes:**
  * `fromJS` (Impact: 5510.9 | O(2^N) | DB: 58)
  * `build` (Impact: 1625.0 | O(2^N) | DB: 7)
  * `fromJS` (Impact: 1306.0 | O(2^N) | DB: 12)
  * `resolve` (Impact: 221.3 | O(N^6))
    * *Intent:* /// Returns a resolver Result for a file in the map, or null if not found. /// This creates a minima...
  * `get` (Impact: 96.1 | O(2^N))
    * *Intent:* /// Resolve a specifier against the file map. /// Returns the contents if the specifier exactly matc...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 631`, `structural_boundaries: 229`, `args: 75`, `func_start: 74`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 161`, `dead_code: 2`, `duplicate_logic: 7`
* *Architecture:* `io: 8`, `api: 83`, `import: 7`
* *Defense:* `safety: 349`, `doc: 31`, `immutability_locks: 164`, `cleanup: 117`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` compile_target.zig, bun, resolver.zig, fs.zig, std, options.zig, resolve_path.zig
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/install/npm.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.356 IQR)
- **Top Global Matches:** file_cluster_8: 13.356, file_cluster_13: 13.528, file_cluster_0: 13.587
- **Magnitude:** 9316.42 | **LOC:** 2791 | **CtrlFlow:** 72.2% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 66
- **Risk Profile:** Cognitive Load (54.9448%), Tech Debt (32.8155%)
**Top Internal Functions/Classes:**
  * `parse` (Impact: 5802.9 | O(2^N) | DB: 66)
    * *Intent:* /// This parses [Abbreviated metadata](https://github.com/npm/registry/blob/master/docs/responses/pa...
  * `Negatable` (Impact: 720.9 | O(2^N) | DB: 4)
  * `findByDistTagWithFilter` (Impact: 399.2 | O(N^6) | DB: 3)
  * `whoami` (Impact: 327.4 | O(2^N) | DB: 6)
  * `findBestVersionWithFilter` (Impact: 300.1 | O(N^6) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 741`, `structural_boundaries: 285`, `args: 56`, `func_start: 56`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 38`, `high_risk_execution: 1`, `state_mutation: 322`, `dead_code: 3`, `planned_debt: 3`, `fragile_debt: 2`, `duplicate_logic: 9`
* *Architecture:* `io: 13`, `api: 114`, `concurrency: 6`, `import: 15`
* *Defense:* `safety: 278`, `doc: 33`, `immutability_locks: 387`, `cleanup: 18`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` url.zig, integrity.zig, pool.zig, bun, install.zig, env_loader.zig, identity_context.zig, bin.zig...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/css/css_parser.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.472 IQR)
- **Top Global Matches:** file_cluster_11: 14.472, file_cluster_0: 14.525, file_cluster_8: 14.535
- **Magnitude:** 9250.9 | **LOC:** 7330 | **CtrlFlow:** 71.4% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 27
- **Risk Profile:** Cognitive Load (26.0509%), Tech Debt (60.449%)
**Top Internal Functions/Classes:**
  * `NestedRuleParser` (Impact: 1596.8 | O(N^6) | DB: 19)
  * `DeriveParse` (Impact: 802.9 | O(N^6) | DB: 4)
  * `StyleSheet` (Impact: 622.2 | O(N^6) | DB: 27)
  * `TopLevelRuleParser` (Impact: 532.5 | O(N^6) | DB: 7)
  * `StyleSheetParser` (Impact: 283.3 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1966`, `structural_boundaries: 787`, `args: 337`, `func_start: 321`, `class_start: 73`
* *Risk/State:* `safety_bypasses: 88`, `high_risk_execution: 1`, `state_mutation: 356`, `dead_code: 71`, `planned_debt: 44`, `fragile_debt: 4`, `duplicate_logic: 40`
* *Architecture:* `api: 530`, `import: 25`
* *Defense:* `safety: 637`, `doc: 356`, `immutability_locks: 863`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` dependencies.zig, targets.zig, prefixes.zig, small_list.zig, media_query.zig, properties.zig, logical.zig, rules.zig...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/bun.js/bindings/node/http/llhttp/llhttp.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.313 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.728 IQR)
- **Top Global Matches:** file_cluster_8: 14.313, file_cluster_12: 14.34, file_cluster_11: 14.574
- **Magnitude:** 9225.1 | **LOC:** 10155 | **CtrlFlow:** 79.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 246
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (10.3784%)
**Top Internal Functions/Classes:**
  * `llhttp__internal__run` (Impact: 1469.7 | O(N^4) | DB: 246)
  * `llparse__match_sequence_to_lower` (Impact: 24.1 | O(N^4) | DB: 11)
  * `llparse__match_sequence_to_lower_unsafe` (Impact: 19.1 | O(N^4) | DB: 11)
  * `llparse__match_sequence_id` (Impact: 19.1 | O(N^4) | DB: 11)
  * `llhttp__internal_execute` (Impact: 13.7 | O(N^3) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3023`, `structural_boundaries: 792`, `func_start: 63`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 4802`, `duplicate_logic: 11`, `orphaned_logic: 6`
* *Architecture:* `io: 1`, `api: 2563`, `import: 8`
* *Defense:* `safety: 2`, `immutability_locks: 533`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` llhttp.h, wasm_simd128.h, string.h, stdlib.h, x86intrin.h, arm_neon.h, stdint.h, nmmintrin.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/cli/pack_command.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.2%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.989 IQR)
- **Top Global Matches:** file_cluster_8: 12.989, file_cluster_0: 13.284, file_cluster_13: 13.346
- **Magnitude:** 8208.6 | **LOC:** 2842 | **CtrlFlow:** 75.3% | **Authorship Centralization:** 25.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 43
- **Risk Profile:** Cognitive Load (28.8558%), Tech Debt (9.065%)
**Top Internal Functions/Classes:**
  * `pack` (Impact: 3356.5 | O(2^N) | DB: 43)
  * `iterateIncludedProjectTree` (Impact: 595.4 | O(N^6) | DB: 11)
  * `addBundledDep` (Impact: 584.1 | O(N^6) | DB: 8)
  * `addEntireTree` (Impact: 457.2 | O(N^6) | DB: 5)
    * *Intent:* /// Adds all files in a directory tree to `pack_list` (default ignores still apply)
  * `iterateProjectTree` (Impact: 385.1 | O(N^6) | DB: 4)
    * *Intent:* /// Returns a list of files to pack and another list of files from bundled dependencies
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 768`, `structural_boundaries: 252`, `args: 36`, `func_start: 36`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 52`, `state_mutation: 265`, `dead_code: 6`, `planned_debt: 7`
* *Architecture:* `io: 14`, `api: 25`, `import: 3`
* *Defense:* `safety: 328`, `doc: 12`, `sync_locks: 4`, `immutability_locks: 261`, `cleanup: 45`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std, libarchive.zig, bun
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/bun.js/api/server.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.386 IQR)
- **Top Global Matches:** file_cluster_8: 13.386, file_cluster_13: 13.629, file_cluster_0: 13.657
- **Magnitude:** 8190.62 | **LOC:** 3478 | **CtrlFlow:** 71.2% | **Authorship Centralization:** 24.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (24.7306%), Tech Debt (85.9526%)
**Top Internal Functions/Classes:**
  * `onUpgrade` (Impact: 812.6 | O(N^6) | DB: 16)
  * `setRoutes` (Impact: 787.9 | O(2^N) | DB: 13)
  * `listen` (Impact: 589.5 | O(2^N) | DB: 4)
    * *Intent:* // TODO: make this return JSError!void, and do not deinitialize on synchronous failure, to allow err...
  * `fromJS` (Impact: 384.9 | O(2^N) | DB: 2)
  * `onListenFailed` (Impact: 320.5 | O(2^N) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 920`, `structural_boundaries: 372`, `args: 131`, `func_start: 131`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 39`, `state_mutation: 279`, `dead_code: 5`, `planned_debt: 8`, `duplicate_logic: 32`
* *Architecture:* `api: 184`, `import: 16`
* *Defense:* `safety: 310`, `doc: 42`, `immutability_locks: 273`, `cleanup: 82`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` options.zig, std, StaticRoute.zig, FileRoute.zig, HTMLBundle.zig, ServerWebSocket.zig, NodeHTTPResponse.zig, runtime.zig...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/css/values/color.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.124 IQR)
- **Top Global Matches:** file_cluster_8: 13.124, file_cluster_7: 13.28, file_cluster_0: 13.352
- **Magnitude:** 8075.08 | **LOC:** 4717 | **CtrlFlow:** 68.5% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (14.8146%), Tech Debt (70.3642%)
**Top Internal Functions/Classes:**
  * `supportsCondition` (Impact: 1678.2 | O(N^6) | DB: 13)
  * `toCss` (Impact: 706.5 | O(2^N) | DB: 3)
  * `interpolate` (Impact: 616.0 | O(2^N) | DB: 6)
    * *Intent:* /// Mixes this color with another color, including the specified amount of each. /// Implemented acc...
  * `parsePredefinedRelative` (Impact: 543.6 | O(N^5))
  * `parse` (Impact: 305.0 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 966`, `structural_boundaries: 445`, `args: 244`, `func_start: 239`, `class_start: 66`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 110`, `dead_code: 29`, `planned_debt: 6`, `fragile_debt: 2`, `duplicate_logic: 35`
* *Architecture:* `api: 551`, `import: 5`
* *Defense:* `safety: 285`, `doc: 210`, `immutability_locks: 990`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` css_parser.zig, color_generated.zig, bun, color_js.zig, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/shell/shell.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.897 IQR)
- **Top Global Matches:** file_cluster_8: 13.897, file_cluster_0: 14.034, file_cluster_13: 14.062
- **Magnitude:** 7878.3 | **LOC:** 4699 | **CtrlFlow:** 71.9% | **Authorship Centralization:** 31.2%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 21
- **Risk Profile:** Cognitive Load (41.8943%), Tech Debt (94.9253%)
**Top Internal Functions/Classes:**
  * `asHumanReadable` (Impact: 2866.3 | O(N^6) | DB: 21)
  * `parse_atom` (Impact: 474.9 | O(N^6) | DB: 8)
  * `parse_cond_expr` (Impact: 308.2 | O(N^6))
  * `parse_if_clause` (Impact: 295.1 | O(N^6) | DB: 1)
  * `parse_assign` (Impact: 179.4 | O(N^6))
    * *Intent:* /// Try to parse an assignment. If no assignment could be parsed then return /// null and backtrack ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1599`, `structural_boundaries: 624`, `args: 252`, `func_start: 252`, `class_start: 59`
* *Risk/State:* `safety_bypasses: 48`, `high_risk_execution: 5`, `state_mutation: 352`, `dead_code: 19`, `planned_debt: 21`, `fragile_debt: 3`, `duplicate_logic: 53`
* *Architecture:* `api: 253`, `import: 9`
* *Defense:* `safety: 423`, `doc: 179`, `sync_locks: 1`, `immutability_locks: 487`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AllocScope.zig, interpreter.zig, sys.zig, Yield.zig, bun, std, builtin, subproc.zig
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/bun.js/bindings/bindings.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.229 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.19 IQR)
- **Top Global Matches:** file_cluster_13: 15.229, file_cluster_8: 15.338, file_cluster_0: 15.37
- **Magnitude:** 7422.5 | **LOC:** 6349 | **CtrlFlow:** 44.2% | **Authorship Centralization:** 22.8%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 87
- **Risk Profile:** Cognitive Load (88.7229%), Tech Debt (99.9997%)
**Top Internal Functions/Classes:**
  * `Bun__deepMatch` (Impact: 1068.6 | O(2^N) | DB: 24)
  * `matchAsymmetricMatcherAndGetFlags` (Impact: 1002.6 | O(N^6) | DB: 79)
  * `JSC__JSValue__forEachPropertyImpl` (Impact: 739.6 | O(N^6) | DB: 87)
  * `JSC__JSValue__forEachPropertyOrdered` (Impact: 199.8 | O(N^4) | DB: 34)
  * `JSC__JSValue__getIfPropertyExistsFromPat` (Impact: 188.8 | O(N^6) | DB: 41)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 654`, `structural_boundaries: 826`, `args: 491`, `func_start: 182`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 22`, `high_risk_execution: 6`, `state_mutation: 2210`, `dead_code: 6`, `planned_debt: 4`, `fragile_debt: 81`, `orphaned_logic: 236`
* *Architecture:* `import: 128`
* *Defense:* `safety: 8`, `doc: 17`, `test: 33`, `sync_locks: 3`, `immutability_locks: 99`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 37):` WTFString.h, HTTPHeaderNames.h, JSDOMConvertStrings.h, helpers.h, GregorianDateTime.h, root.h, BooleanObject.h, ExceptionScope.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/bundler/LinkerContext.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.588 IQR)
- **Top Global Matches:** file_cluster_8: 12.588, file_cluster_13: 12.757, file_cluster_0: 12.924
- **Magnitude:** 7282.34 | **LOC:** 2772 | **CtrlFlow:** 74.4% | **Authorship Centralization:** 26.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (17.787%), Tech Debt (23.6317%)
**Top Internal Functions/Classes:**
  * `matchImportWithExport` (Impact: 953.3 | O(2^N) | DB: 3)
  * `markFileLiveForTreeShaking` (Impact: 804.6 | O(2^N) | DB: 1)
  * `validateTLA` (Impact: 647.1 | O(2^N) | DB: 4)
  * `generateSourceMapForChunk` (Impact: 601.6 | O(2^N) | DB: 12)
  * `breakOutputIntoPieces` (Impact: 587.8 | O(2^N) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 512`, `structural_boundaries: 176`, `args: 55`, `func_start: 55`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 49`, `state_mutation: 171`, `dead_code: 8`, `planned_debt: 7`, `fragile_debt: 1`, `duplicate_logic: 6`
* *Architecture:* `io: 1`, `api: 133`, `concurrency: 19`, `import: 38`
* *Defense:* `safety: 138`, `doc: 18`, `immutability_locks: 330`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` doStep5.zig, computeCrossChunkDependencies.zig, writeOutputFilesToDisk.zig, generateChunksInParallel.zig, resolver.zig, generateCompileResultForHtmlChunk.zig, findImportedCSSFilesInJSOrder.zig, generateCompileResultForCssChunk.zig...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/css/values/gradient.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.2%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.377 IQR)
- **Top Global Matches:** file_cluster_8: 13.377, file_cluster_7: 13.588, file_cluster_13: 13.71
- **Magnitude:** 7236.28 | **LOC:** 1658 | **CtrlFlow:** 71.9% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (26.9324%), Tech Debt (99.2765%)
**Top Internal Functions/Classes:**
  * `WebKitGradientPointComponent` (Impact: 2755.6 | O(2^N) | DB: 7)
    * *Intent:* /// A keyword or number within a [WebKitGradientPoint](WebKitGradientPoint).
  * `parse` (Impact: 795.8 | O(2^N))
    * *Intent:* /// A legacy `-webkit-gradient()`.
  * `toCss` (Impact: 451.1 | O(2^N) | DB: 2)
  * `parse` (Impact: 419.1 | O(2^N))
  * `toCss` (Impact: 309.9 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 619`, `structural_boundaries: 242`, `args: 98`, `func_start: 98`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 63`, `dead_code: 1`, `duplicate_logic: 44`
* *Architecture:* `api: 110`, `import: 3`
* *Defense:* `safety: 269`, `doc: 95`, `immutability_locks: 186`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std, bun, css_parser.zig
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/string/SmolStr.zig` (ZIG) | Magnitude: 405.8 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 215, branch: 67, state_mutation: 56, structural_boundaries: 47
- `test/integration/vite-build/the-test-app/src/lib/components/ui/checkbox/checkbox.svelte` (HTML) | Magnitude: 19.64 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 27, structural_boundaries: 10, safety: 4, decorators: 4
- `src/bun.js/bindings/JSRef.zig` (ZIG) | Magnitude: 191.84 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 118, doc: 90, branch: 38, pointers: 28
- `src/bun.js/bindings/webcore/JSDOMPromiseDeferred.cpp` (CPP) | Magnitude: 350.28 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 181, indent_spaces: 134, structural_boundaries: 56, branch: 36
- `src/cli/create_command.zig` (ZIG) | Magnitude: 5127.14 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 2015, branch: 551, state_mutation: 396, bitwise_ops: 284

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `packages/bun-types/devserver.d.ts` (TYPESCRIPT) | Magnitude: 4.18 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 20, doc: 16, safety: 13, structural_boundaries: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `src/js/node/_http_agent.ts` (TYPESCRIPT) | Magnitude: 91.12 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 321, indent_spaces: 314, branch: 106, args: 59
- `src/js/node/_http_server.ts` (TYPESCRIPT) | Magnitude: 203.12 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 718, state_mutation: 311, branch: 238, args: 89
- `src/bun.js/bindings/webcore/JSDOMConvertUnion.h` (CPP) | Magnitude: 856.38 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 221, indent_spaces: 218, structural_boundaries: 143, branch: 57
- `src/bun.js/bindings/webcore/SerializedScriptValue.cpp` (CPP) | Magnitude: 4693.46 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 2311, state_mutation: 1601, branch: 772, structural_boundaries: 465
- `packages/bun-uws/src/MoveOnlyFunction.h` (CPP) | Magnitude: 513.4 | Delta: **0.044 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 370, indent_spaces: 203, structural_boundaries: 144, branch: 42

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `src/js/internal/streams/duplex.ts` (TYPESCRIPT) | Magnitude: 7.36 | Delta: **0.043 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 37, state_mutation: 33, reflection_metaprogramming: 22, branch: 11
- `src/deps/uucode/src/get.zig` (ZIG) | Magnitude: 234.04 | Delta: **0.058 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 92, branch: 53, reflection_metaprogramming: 43, encapsulation: 31
- `src/js/node/path.ts` (TYPESCRIPT) | Magnitude: 2.66 | Delta: **0.059 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 52, reflection_metaprogramming: 24, branch: 9, io: 7
- `src/bun.js/api/ffi-stdalign.h` (CPP) | Magnitude: 21.22 | Delta: **0.068 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: macros: 10, reflection_metaprogramming: 7, state_mutation: 6, branch: 3
- `src/bun.js/bindings/sqlite/sqlite3_local.h` (CPP) | Magnitude: 32.74 | Delta: **0.087 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: macros: 365, reflection_metaprogramming: 343, pointers: 320, indent_spaces: 319

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/install/install_binding.zig` (ZIG) | Magnitude: 63.04 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 48, globals: 24, encapsulation: 23, immutability_locks: 21
- `src/bun.js/bindings/JSX509CertificatePrototype.h` (CPP) | Magnitude: 25.96 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 25, structural_boundaries: 13, state_mutation: 10, args: 7
- `src/bun.js/bindings/ScriptExecutionContext.h` (CPP) | Magnitude: 11.64 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 106, structural_boundaries: 32, safety_bypasses: 25, branch: 18
- `src/bun.js/bindings/webcrypto/CryptoKeyRSAComponents.h` (CPP) | Magnitude: 253.52 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: state_mutation: 182, indent_spaces: 56, immutability_locks: 36, branch: 23
- `src/js/internal/stream.ts` (TYPESCRIPT) | Magnitude: 3.53 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 51, immutability_locks: 20, import: 17, func_start: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `src/cli/uninstall.ps1` (POWERSHELL) | Magnitude: 63.7 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 63, branch: 32, state_mutation: 32, closures: 28
- `bench/snippets/buffer-read.js` (JAVASCRIPT) | Magnitude: 8.7 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: structural_boundaries: 44, args: 39, func_start: 39, closures: 39
- `bench/snippets/buffer.js` (JAVASCRIPT) | Magnitude: 29.74 | Delta: **0.06 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: structural_boundaries: 46, args: 40, func_start: 40, closures: 40

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `src/ast/parseImportExport.zig` (ZIG) | Magnitude: 1255.4 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 353, branch: 147, safety: 67, globals: 48
- `src/collections/array_list.zig` (ZIG) | Magnitude: 650.06 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 317, doc: 78, pointers: 70, api: 64
- `packages/bun-types/ffi.d.ts` (TYPESCRIPT) | Magnitude: 2.77 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 183, doc: 47, structural_boundaries: 26, generics: 22
- `src/system_timer.zig` (ZIG) | Magnitude: 19.14 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 17, args: 5, func_start: 5, api: 5
- `src/ptr/shared.zig` (ZIG) | Magnitude: 1654.24 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 438, branch: 156, doc: 121, structural_boundaries: 68

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/js/internal/fs/cp-sync.ts` (TYPESCRIPT) | Magnitude: 21.73 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 146, branch: 62, structural_boundaries: 37, args: 32
- `src/node-fallbacks/url.js` (JAVASCRIPT) | Magnitude: 1794.82 | Delta: **0.051 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 388, state_mutation: 386, branch: 185, structural_boundaries: 76
- `src/node-fallbacks/util.js` (JAVASCRIPT) | Magnitude: 556.02 | Delta: **0.068 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 331, structural_boundaries: 106, branch: 101, state_mutation: 86
- `bench/cat/cat.mjs` (JAVASCRIPT) | Magnitude: 15.08 | Delta: **0.07 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: branch: 3, structural_boundaries: 3, state_mutation: 3, immutability_locks: 2
- `src/codegen/helpers.ts` (TYPESCRIPT) | Magnitude: 14.36 | Delta: **0.099 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 102, structural_boundaries: 44, branch: 27, api: 24

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `src/init/react-app/src/App.tsx` (TYPESCRIPT) | Magnitude: 0.84 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 7, ui_framework: 5, import: 3
- `packages/bun-types/shell.d.ts` (TYPESCRIPT) | Magnitude: 1.0 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 29, doc: 23, args: 14, func_start: 14
- `src/init/react-tailwind/src/App.tsx` (TYPESCRIPT) | Magnitude: 0.9 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 7, ui_framework: 7, import: 3
- `packages/bun-error/index.tsx` (TYPESCRIPT) | Magnitude: 77.22 | Delta: **0.066 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 682, state_mutation: 149, branch: 148, structural_boundaries: 121
- `bench/snippets/react-dom-render.bun.js` (JAVASCRIPT) | Magnitude: 33.46 | Delta: **0.136 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: structural_boundaries: 33, concurrency: 25, indent_spaces: 19, func_start: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `bench/postMessage/structureClone-string.mjs` (JAVASCRIPT) | Magnitude: 31.58 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: func_start: 16, indent_spaces: 15, structural_boundaries: 12, args: 8
- `bench/snippets/peek-promise.mjs` (JAVASCRIPT) | Magnitude: 20.86 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 17, concurrency: 7, args: 6, func_start: 6
- `src/darwin.zig` (ZIG) | Magnitude: 83.1 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 78, api: 36, immutability_locks: 30, args: 26
- `src/bun.js/bindings/libuv/generate_uv_posix_stubs.ts` (TYPESCRIPT) | Magnitude: 27.08 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 270, structural_boundaries: 80, state_mutation: 70, branch: 62
- `bench/websocket-server/chat-client.mjs` (JAVASCRIPT) | Magnitude: 103.72 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 124, state_mutation: 49, branch: 27, concurrency: 26

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `packages/bun-uws/src/ProxyParser.h` (CPP) | Magnitude: 98.54 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 69, state_mutation: 43, structural_boundaries: 24, branch: 12
- `src/bun.js/node/assert/myers_diff.zig` (ZIG) | Magnitude: 745.06 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 445, branch: 139, immutability_locks: 131, globals: 70
- `packages/bun-native-plugin-rs/src/lib.rs` (RUST) | Magnitude: 163.92 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: doc: 343, indent_spaces: 229, structural_boundaries: 52, state_mutation: 38
- `src/js/builtins/Ipc.ts` (TYPESCRIPT) | Magnitude: 2.99 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 21, dead_code: 17, doc: 14, branch: 7
- `packages/bun-usockets/src/crypto/default_ciphers.h` (CPP) | Magnitude: 0.15 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 16, macros: 2, dead_code: 1, reflection_metaprogramming: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `src/feature_flags.zig` (ZIG) | Magnitude: 50.7 | Delta: **0.05 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 61, api: 36, immutability_locks: 35, globals: 33
- `src/ast/TS.zig` (ZIG) | Magnitude: 42.16 | Delta: **0.093 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 97, indent_spaces: 84, api: 16, globals: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/bun.js/event_loop/ConcurrentPromiseTask.zig` (ZIG) | Magnitude: 41.16 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 46, globals: 15, pointers: 14, encapsulation: 14
- `src/bun.js/node/net/BlockList.zig` (ZIG) | Magnitude: 581.98 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 167, branch: 107, immutability_locks: 61, bitwise_ops: 57
- `src/bun.js/bindings/Base64Helpers.h` (CPP) | Magnitude: 14.12 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 2, fragile_debt: 2, args: 1, state_mutation: 1
- `src/bun.js/bindings/NodeAsyncHooks.cpp` (CPP) | Magnitude: 5.94 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 6, pointers: 6, import: 5
- `src/bun.js/bindings/webcrypto/CryptoKeyOKP.cpp` (CPP) | Magnitude: 526.18 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 148, indent_spaces: 131, branch: 74, structural_boundaries: 52

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `src/bun.js/bindings/TextCodecReplacement.h` (CPP) | Magnitude: 17.3 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 6, args: 5, immutability_locks: 5, structural_boundaries: 4
- `src/bun.js/bindings/TextCodecUserDefined.h` (CPP) | Magnitude: 17.28 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: args: 5, immutability_locks: 5, indent_spaces: 5, structural_boundaries: 4
- `src/bun.js/bindings/TextCodecASCIIFastPath.h` (CPP) | Magnitude: 28.28 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 15, safety: 12, state_mutation: 12
- `src/bun.js/bindings/webcrypto/CryptoAlgorithmEd25519.h` (CPP) | Magnitude: 148.74 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 145, branch: 19, immutability_locks: 19, indent_spaces: 13
- `src/bun.js/bindings/ZigGeneratedCode.cpp` (CPP) | Magnitude: 112.08 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 160, pointers: 91, args: 59, structural_boundaries: 38

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `packages/bun-types/bun.d.ts` -> Churn: **100.0%** | Cog Load: 9.5561% | Debt: 98.9589%
- `src/bun.js/bindings/bindings.cpp` -> Churn: **96.92%** | Cog Load: 88.7229% | Debt: 99.9997%
- `src/bun.js/bindings/ZigGlobalObject.cpp` -> Churn: **93.37%** | Cog Load: 89.8307% | Debt: 99.9995%
- `src/bun.zig` -> Churn: **91.58%** | Cog Load: 22.4077% | Debt: 99.7187%
- `src/bun.js/webcore/Blob.zig` -> Churn: **82.72%** | Cog Load: 30.0871% | Debt: 88.4399%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/css/properties/properties_generated.zig` -> **pfg** (100.0% isolated ownership) | Magnitude: 6395.98
- `src/bun.js/test/diff/diff_match_patch.zig` -> **pfg** (100.0% isolated ownership) | Magnitude: 4921.64
- `src/ast/skipTypescript.zig` -> **pfg** (100.0% isolated ownership) | Magnitude: 4117.78
- `src/api/schema.js` -> **Dylan Conway** (100.0% isolated ownership) | Magnitude: 3341.86
- `src/deps/uucode/src/types.zig` -> **Jarred Sumner** (100.0% isolated ownership) | Magnitude: 3339.04

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/bun.js/bindings/JSDOMWrapper.h` -> **Severity: 0.042** (Bridge: 0.0004 * Flux: 99.9993%)
- `src/bun.js/bindings/ZigGlobalObject.h` -> **Severity: 0.038** (Bridge: 0.0009 * Flux: 41.1265%)
- `src/bun.js/bindings/InternalModuleRegistry.h` -> **Severity: 0.028** (Bridge: 0.0003 * Flux: 100.0%)
- `src/bun.js/bindings/BunClientData.h` -> **Severity: 0.026** (Bridge: 0.0003 * Flux: 100.0%)
- `src/bun.js/bindings/DOMWrapperWorld.h` -> **Severity: 0.021** (Bridge: 0.0002 * Flux: 100.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/bun.js/bindings/root.h` -> **Severity: 2098.197** (Blast Radius: 64.838 * Doc Risk: 32.3606%)
- `src/bun.js/bindings/ZigGlobalObject.h` -> **Severity: 1273.4** (Blast Radius: 12.734 * Doc Risk: 100.0%)
- `src/bun.js/bindings/webcore/JSDOMConvertBase.h` -> **Severity: 813.8** (Blast Radius: 8.138 * Doc Risk: 100.0%)
- `src/bun.js/bindings/JSDOMWrapper.h` -> **Severity: 758.1** (Blast Radius: 7.581 * Doc Risk: 100.0%)
- `src/bun.js/bindings/JSDOMGlobalObject.h` -> **Severity: 652.884** (Blast Radius: 6.543 * Doc Risk: 99.7836%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
