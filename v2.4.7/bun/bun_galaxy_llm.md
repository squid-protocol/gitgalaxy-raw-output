# ARCHITECTURAL_BRIEF: bun
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/bun` |
| **Timestamp** | `2026-08-07T03:47:53.718149+00:00` |
| **Scan Duration** | `26.63s` |
| **Git Branch** | `main` |
| **Git Commit** | `1cc837687b1d1f8d558a40110fbe3e61cc41fbcd` |
| **Git Remote** | `https://github.com/oven-sh/bun` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 3228 malicious artifacts.

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
| Total Artifacts | 12530 |
| Analyzed Artifacts (Scanned) | 3973 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 8557 |
| Total LOC | 834983 |
| Volatility Index | 0.003 |
| % Scanned of codebase = | 31.7% |
| Dominant Lang | PLAINTEXT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6057 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
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
> **Architectural Drift Z-Score:** `4.652`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 1934 | 48.7% |
| file_cluster_13 | 1146 | 28.8% |
| Unknown | 109 | 2.7% |
| file_cluster_4 | 104 | 2.6% |
| file_cluster_9 | 71 | 1.8% |
| file_cluster_16 | 46 | 1.2% |
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
| Cognitive Load Exposure | 0.0 | 100.0 | 35.8 | 26.7 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 56.8 | 65.3 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 45.9 | 21.3 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 28.3 | 2.5 | 80.0 |
| API Exposure | 0.0 | 20.0 | 3.3 | 2.3 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 8.6 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 49.0 | 42.5 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 3.2 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 92.4 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 12.9 | 3.3 | 1.5 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 9.2 | 4.8 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 40.4 | 23.0 | 100.0 |
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

- `writeWithFormatting` (@ `src/bun.js/test/pretty_format.zig`) -> Impact: **1247.2** | LOC: 1064
- `forEach` (@ `src/bun.js/ConsoleObject.zig`) -> Impact: **1160.6** | LOC: 1094
- `fetchImpl` (@ `src/bun.js/webcore/fetch.zig`) -> Impact: **1118.5** | LOC: 1262
  * *Intent:* /// Shared implementation of fetch
- `SkipTypescript` (@ `src/ast/skipTypescript.zig`) -> Impact: **1099.0** | LOC: 1185
- `saveFromBinary_inner` (@ `src/install/lockfile/bun.lock.zig`) -> Impact: **1088.6** | LOC: 1295
- `parseIntoBinaryLockfile` (@ `src/install/lockfile/bun.lock.zig`) -> Impact: **1053.7** | LOC: 936
  * *Intent:* // const PkgMap = struct {};
- `migrateNPMLockfile` (@ `src/install/migration.zig`) -> Impact: **1053.1** | LOC: 924
- `ParseStmt` (@ `src/ast/parseStmt.zig`) -> Impact: **1031.3** | LOC: 1082
- `NewLexer_` (@ `src/js_lexer.zig`) -> Impact: **1025.4** | LOC: 1155
- `serializeComponent` (@ `src/css/selectors/selector.zig`) -> Impact: **983.1** | LOC: 924

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `test/js/node/crypto/fixtures` | 26 | 130000.0 | 0.0% | 0.0% |
| `test/js/node/tls/fixtures` | 21 | 105000.0 | 0.0% | 0.0% |
| `test/js/third_party/jsonwebtoken` | 17 | 85000.0 | 0.0% | 0.0% |
| `src/bun.js/bindings` | 457 | 76065.35 | 41.8% | 63.46% |
| `src` | 127 | 64244.97 | 25.2% | 34.22% |
| `src/bun.js/bindings/webcore` | 412 | 50992.46 | 53.28% | 74.79% |
| `test/js/node/http/fixtures` | 8 | 40000.0 | 0.0% | 0.0% |
| `src/ast` | 46 | 37738.72 | 28.13% | 27.32% |
| `src/bun.js/bindings/webcrypto` | 181 | 21151.2 | 52.04% | 51.61% |
| `src/deps` | 15 | 20393.78 | 13.92% | 77.62% |

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
- `src/bun.js/bindings/ncrypto.cpp` -> **328** Orphaned Functions | **91** Duplicates
- `src/bun.js/bindings/bindings.cpp` -> **241** Orphaned Functions | **0** Duplicates
- `src/css/values/color_generated.zig` -> **0** Orphaned Functions | **182** Duplicates
- `src/bun.js/node/node_fs.zig` -> **0** Orphaned Functions | **169** Duplicates
- `src/css/selectors/parser.zig` -> **0** Orphaned Functions | **145** Duplicates

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
279. **`bench/snippets/semver.mjs`** -> AI Confidence: **99.29%**
280. **`misctools/publish-examples.js`** -> AI Confidence: **99.29%**
281. **`src/node-fallbacks/net.js`** -> AI Confidence: **99.29%**
282. **`misctools/bun-feature-data.ts`** -> AI Confidence: **99.29%**
283. **`packages/bun-error/stack-trace-parser.ts`** -> AI Confidence: **99.29%**
284. **`packages/bun-vscode/example/print.ts`** -> AI Confidence: **99.29%**
285. **`src/bake/client/css-reloader.ts`** -> AI Confidence: **99.29%**
286. **`src/bake/debug.ts`** -> AI Confidence: **99.29%**
287. **`src/codegen/builtin-parser.ts`** -> AI Confidence: **99.29%**
288. **`src/js/eval/fuzzilli-reprl.ts`** -> AI Confidence: **99.29%**
289. **`src/js/internal/assert/assertion_error.ts`** -> AI Confidence: **99.29%**
290. **`src/js/internal/assert/myers_diff.ts`** -> AI Confidence: **99.29%**
291. **`src/js/internal/html.ts`** -> AI Confidence: **99.29%**
292. **`src/js/internal/net/isIP.ts`** -> AI Confidence: **99.29%**
293. **`src/js/internal/sql/shared.ts`** -> AI Confidence: **99.29%**
294. **`src/js/internal/streams/destroy.ts`** -> AI Confidence: **99.29%**
295. **`src/js/internal/url.ts`** -> AI Confidence: **99.29%**
296. **`src/js/internal/validators.ts`** -> AI Confidence: **99.29%**
297. **`src/js/node/querystring.ts`** -> AI Confidence: **99.29%**
298. **`src/js/node/url.ts`** -> AI Confidence: **99.29%**
299. **`src/cli/install.sh`** -> AI Confidence: **99.29%**
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

### Hardcoded Payload Artifacts
- `packages/bun-usockets/src/crypto/root_certs.h` -> **100.0%** Exposure
- `packages/bun-usockets/generate-root-certs.pl` -> **95.8312%** Exposure
- `packages/bun-types/globals.d.ts` -> **34.3653%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `39` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `12294` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/js/internal/sql/mysql.ts` (TYPESCRIPT) -> Cumulative Risk: **775.77**
- **Archetype:** `file_cluster_4` (Distance: 13.512 IQR)
- **Magnitude:** 145.06 | **LOC:** 1167 | **CtrlFlow:** 69.3% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.496%), Concurrency (95.8124%)
- **Heaviest Functions:** `normalizeQuery` (Impact: 141.6), `onClose` (Impact: 85.2), `detectCommand` (Impact: 65.5)

### 2. `src/runtime.js` (JAVASCRIPT) -> Cumulative Risk: **751.31**
- **Archetype:** `file_cluster_11` (Distance: 14.536 IQR)
- **Magnitude:** 639.98 | **LOC:** 324 | **CtrlFlow:** 45.6% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9781%)
- **Heaviest Functions:** `__decorateElement` (Impact: 133.1), `__privateSet` (Impact: 59.0), `__toESM` (Impact: 35.2)

### 3. `packages/bun-usockets/src/loop.c` (C) -> Cumulative Risk: **739.62**
- **Archetype:** `file_cluster_8` (Distance: 13.961 IQR)
- **Magnitude:** 461.58 | **LOC:** 643 | **CtrlFlow:** 60.2% | **Authorship Centralization:** 36.4%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Cognitive Load (97.0058%)
- **Heaviest Functions:** `us_internal_dispatch_ready_poll` (Impact: 123.2), `us_internal_handle_low_priority_sockets` (Impact: 13.3), `us_internal_free_closed_sockets` (Impact: 9.2)

### 4. `packages/bun-usockets/src/eventing/epoll_kqueue.c` (C) -> Cumulative Risk: **721.27**
- **Archetype:** `file_cluster_13` (Distance: 14.294 IQR)
- **Magnitude:** 497.78 | **LOC:** 847 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 40.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.0342%)
- **Heaviest Functions:** `us_poll_resize` (Impact: 69.3), `us_internal_dispatch_ready_polls` (Impact: 37.9), `kqueue_change` (Impact: 28.4)

### 5. `src/js/builtins/ReadableStreamInternals.ts` (TYPESCRIPT) -> Cumulative Risk: **718.62**
- **Archetype:** `file_cluster_8` (Distance: 12.51 IQR)
- **Magnitude:** 197.49 | **LOC:** 2431 | **CtrlFlow:** 52.0% | **Authorship Centralization:** 42.9%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.8605%), State Flux (98.4095%), Concurrency (97.971%)
- **Heaviest Functions:** `readableStreamFromAsyncIterator` (Impact: 244.9), `cancel` (Impact: 163.1), `readStreamIntoSink` (Impact: 81.3)

### 6. `src/bun.js/bindings/webcore/SerializedScriptValue.cpp` (CPP) -> Cumulative Risk: **712.84**
- **Archetype:** `file_cluster_11` (Distance: 20.181 IQR)
- **Magnitude:** 2802.96 | **LOC:** 6840 | **CtrlFlow:** 62.4% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Cognitive Load (93.7466%)
- **Heaviest Functions:** `CloneDeserializer::deserialize` (Impact: 136.4), `readTerminal` (Impact: 123.0), `read` (Impact: 83.4)

### 7. `src/js/builtins/ReadableStream.ts` (TYPESCRIPT) -> Cumulative Risk: **709.29**
- **Archetype:** `file_cluster_4` (Distance: 11.658 IQR)
- **Magnitude:** 50.58 | **LOC:** 516 | **CtrlFlow:** 52.2% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9988%), Tech Debt (98.8352%), State Flux (95.2504%)
- **Heaviest Functions:** `readableStreamToArrayBuffer` (Impact: 49.9), `readableStreamToBytes` (Impact: 47.9), `initializeReadableStream` (Impact: 46.5)

### 8. `src/bun.js/bindings/ZigSourceProvider.cpp` (CPP) -> Cumulative Risk: **703.75**
- **Archetype:** `file_cluster_11` (Distance: 20.049 IQR)
- **Magnitude:** 319.56 | **LOC:** 395 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 60.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (97.4951%)
- **Heaviest Functions:** `SourceProvider::create` (Impact: 40.2), `generateCachedModuleByteCodeFromSourceCo` (Impact: 12.3), `generateCachedCommonJSProgramByteCodeFro` (Impact: 12.3)

### 9. `src/js/builtins/CommonJS.ts` (TYPESCRIPT) -> Cumulative Risk: **703.39**
- **Archetype:** `file_cluster_4` (Distance: 13.711 IQR)
- **Magnitude:** 30.12 | **LOC:** 440 | **CtrlFlow:** 53.7% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.8816%), Tech Debt (99.6631%), Cognitive Load (98.278%)
- **Heaviest Functions:** `loadEsmIntoCjs` (Impact: 120.8), `createRequireCache` (Impact: 27.5), `get` (Impact: 7.6)

### 10. `src/js/node/worker_threads.ts` (TYPESCRIPT) -> Cumulative Risk: **703.19**
- **Archetype:** `file_cluster_11` (Distance: 13.019 IQR)
- **Magnitude:** 26.71 | **LOC:** 427 | **CtrlFlow:** 41.5% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Concurrency (99.6825%), Cognitive Load (98.1929%)
- **Heaviest Functions:** `injectFakeEmitter` (Impact: 20.9), `functionForEventType` (Impact: 9.3), `onError` (Impact: 9.3)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/deps/boringssl.translated.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.856 IQR)
- **Top Global Matches:** file_cluster_8: 13.856, file_cluster_13: 14.11, file_cluster_7: 14.113
- **Magnitude:** 12802.2 | **LOC:** 19292 | **CtrlFlow:** 70.8% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (7.1654%), Tech Debt (8.9122%)
**Top Internal Functions/Classes:**
  * `handshake` (Impact: 41.1)
  * `ERR_get_next_error_library` (Impact: 25.8)
  * `init` (Impact: 25.6)
  * `write` (Impact: 11.9)
  * `SSL_CTX_set_custom_verify` (Impact: 11.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1472`, `structural_boundaries: 606`, `args: 3266`, `func_start: 2889`, `class_start: 169`
* *Risk/State:* `safety_bypasses: 1814`, `state_mutation: 120`, `dead_code: 226`, `duplicate_logic: 13`
* *Architecture:* `api: 9855`, `import: 191`
* *Defense:* `safety: 25`, `doc: 34`, `immutability_locks: 9873`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` bun, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/bun.js/bindings/node/http/llhttp/llhttp.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.313 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.728 IQR)
- **Top Global Matches:** file_cluster_8: 14.313, file_cluster_12: 14.34, file_cluster_11: 14.574
- **Magnitude:** 8328.0 | **LOC:** 10155 | **CtrlFlow:** 79.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (10.3784%)
**Top Internal Functions/Classes:**
  * `llhttp__internal__run` (Impact: 631.1)
  * `llparse__match_sequence_to_lower` (Impact: 10.6)
  * `llparse__match_sequence_to_lower_unsafe` (Impact: 8.6)
  * `llparse__match_sequence_id` (Impact: 8.6)
  * `llhttp__internal_execute` (Impact: 7.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3023`, `structural_boundaries: 792`, `func_start: 63`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 4802`, `duplicate_logic: 11`, `orphaned_logic: 6`
* *Architecture:* `io: 1`, `api: 2563`, `import: 8`
* *Defense:* `safety: 2`, `immutability_locks: 533`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` nmmintrin.h, wasm_simd128.h, llhttp.h, string.h, stdlib.h, stdint.h, x86intrin.h, arm_neon.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/bun.js/node/node_fs.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.779 IQR)
- **Top Global Matches:** file_cluster_8: 13.779, file_cluster_0: 13.98, file_cluster_7: 14.043
- **Magnitude:** 5683.76 | **LOC:** 7058 | **CtrlFlow:** 70.6% | **Authorship Centralization:** 25.0%
- **Risk Profile:** Cognitive Load (37.194%), Tech Debt (99.9701%)
**Top Internal Functions/Classes:**
  * `readFileWithOptions` (Impact: 269.2)
  * `NewAsyncCpTask` (Impact: 215.9)
  * `_copySingleFileSync` (Impact: 194.6)
    * *Intent:* /// This is `copyFile`, but it copies symlinks as-is
  * `mkdirRecursiveOSPathImpl` (Impact: 161.3)
  * `cpSyncInner` (Impact: 152.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1889`, `structural_boundaries: 788`, `args: 280`, `func_start: 279`, `class_start: 63`
* *Risk/State:* `safety_bypasses: 152`, `state_mutation: 504`, `dead_code: 12`, `planned_debt: 13`, `fragile_debt: 3`, `duplicate_logic: 169`
* *Architecture:* `io: 41`, `api: 427`, `concurrency: 6`, `import: 8`
* *Defense:* `safety: 681`, `doc: 107`, `sync_locks: 3`, `immutability_locks: 636`, `cleanup: 156`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std, bun, node_fs_binding.zig, node_fs_stat_watcher.zig, dir_iterator.zig, node_fs_watcher.zig, node_fs_constant.zig, fs.zig
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ast/P.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.352 IQR)
- **Top Global Matches:** file_cluster_8: 14.352, file_cluster_0: 14.381, file_cluster_11: 14.436
- **Magnitude:** 5436.48 | **LOC:** 6967 | **CtrlFlow:** 71.9% | **Authorship Centralization:** 28.6%
- **Risk Profile:** Cognitive Load (25.5349%), Tech Debt (12.779%)
**Top Internal Functions/Classes:**
  * `NewParser_` (Impact: 486.8)
  * `substituteSingleUseSymbolInExpr` (Impact: 319.7)
  * `lowerClass` (Impact: 244.3)
  * `processImportStatement` (Impact: 203.2)
  * `exprCanBeRemovedIfUnusedWithoutDCECheck` (Impact: 127.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1781`, `structural_boundaries: 695`, `args: 151`, `func_start: 144`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 192`, `high_risk_execution: 2`, `state_mutation: 615`, `dead_code: 53`, `planned_debt: 20`, `fragile_debt: 5`, `duplicate_logic: 2`
* *Architecture:* `api: 293`, `concurrency: 31`, `import: 12`
* *Defense:* `safety: 683`, `doc: 105`, `immutability_locks: 556`, `cleanup: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` symbols.zig, std, bun, visit.zig, defines.zig, maybe.zig, repl_transforms.zig, visitBinaryExpression.zig...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/css/css_parser.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.456 IQR)
- **Top Global Matches:** file_cluster_11: 14.456, file_cluster_0: 14.506, file_cluster_8: 14.522
- **Magnitude:** 5181.0 | **LOC:** 7330 | **CtrlFlow:** 71.4% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (25.9997%), Tech Debt (93.9529%)
**Top Internal Functions/Classes:**
  * `NestedRuleParser` (Impact: 486.8)
  * `DeriveParse` (Impact: 237.8)
  * `parseBlock` (Impact: 198.6)
  * `StyleSheet` (Impact: 192.2)
  * `generateCode` (Impact: 191.4)
    * *Intent:* /// } /// ``` /// /// During parsing, we can check if it is one of the void fields (in this case `th...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1966`, `structural_boundaries: 786`, `args: 337`, `func_start: 321`, `class_start: 73`
* *Risk/State:* `safety_bypasses: 88`, `high_risk_execution: 2`, `state_mutation: 356`, `dead_code: 71`, `planned_debt: 44`, `fragile_debt: 4`, `duplicate_logic: 81`
* *Architecture:* `api: 540`, `import: 25`
* *Defense:* `safety: 637`, `doc: 356`, `immutability_locks: 863`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` bun, targets.zig, rules.zig, declaration.zig, prefixes.zig, small_list.zig, properties.zig, std...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/js_printer.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.99 IQR)
- **Top Global Matches:** file_cluster_8: 12.99, file_cluster_0: 13.28, file_cluster_7: 13.359
- **Magnitude:** 5119.86 | **LOC:** 6399 | **CtrlFlow:** 80.4% | **Authorship Centralization:** 24.0%
- **Risk Profile:** Cognitive Load (30.3153%), Tech Debt (45.6697%)
**Top Internal Functions/Classes:**
  * `NewPrinter` (Impact: 915.1)
  * `printExpr` (Impact: 625.1)
  * `printStmt` (Impact: 414.8)
  * `printAst` (Impact: 362.7)
  * `printRequireError` (Impact: 200.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1393`, `structural_boundaries: 339`, `args: 171`, `func_start: 169`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 82`, `high_risk_execution: 2`, `state_mutation: 348`, `dead_code: 30`, `planned_debt: 14`, `fragile_debt: 3`, `duplicate_logic: 30`
* *Architecture:* `io: 3`, `api: 207`, `concurrency: 6`, `import: 9`
* *Defense:* `safety: 380`, `doc: 12`, `test: 2`, `immutability_locks: 405`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` renamer.zig, std, sourcemap.zig, import_record.zig, bun, runtime.zig, fs.zig, analyze_transpiled_module.zig...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bench/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bench/async/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bench/ffi/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bench/grpc-server/cert.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bench/grpc-server/key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bench/gzip/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bench/log/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bench/modules/node_os/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bench/sqlite/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/bun-release/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/bun-uws/misc/cert.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/bun-uws/misc/key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/js/bun/http/fixtures/cert.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/js/bun/http/fixtures/cert.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/js/deno/fixtures/id_rsaEncryption.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/js/deno/fixtures/id_rsassaPss.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/js/deno/fixtures/id_rsassaPss_default.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/js/deno/fixtures/id_rsassaPss_saltLen_30.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/js/node/crypto/fixtures/ec_p256_private.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/string/SmolStr.zig` (ZIG) | Magnitude: 226.4 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 215, branch: 67, state_mutation: 56, structural_boundaries: 47
- `test/integration/vite-build/the-test-app/src/lib/components/ui/checkbox/checkbox.svelte` (HTML) | Magnitude: 19.64 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 27, structural_boundaries: 10, safety: 4, decorators: 4
- `src/bun.js/bindings/JSRef.zig` (ZIG) | Magnitude: 104.64 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 118, doc: 90, branch: 38, pointers: 28
- `src/bun.js/bindings/webcore/JSDOMPromiseDeferred.cpp` (CPP) | Magnitude: 292.38 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 181, indent_spaces: 134, structural_boundaries: 56, branch: 36
- `src/cli/create_command.zig` (ZIG) | Magnitude: 1523.24 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 2015, branch: 551, state_mutation: 396, bitwise_ops: 284

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `packages/bun-types/devserver.d.ts` (TYPESCRIPT) | Magnitude: 4.18 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 20, doc: 16, safety: 13, structural_boundaries: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `src/js/node/_http_agent.ts` (TYPESCRIPT) | Magnitude: 82.15 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 321, indent_spaces: 314, branch: 106, args: 59
- `src/js/node/_http_server.ts` (TYPESCRIPT) | Magnitude: 254.57 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 718, state_mutation: 297, branch: 238, args: 91
- `src/bun.js/bindings/webcore/JSDOMConvertUnion.h` (CPP) | Magnitude: 342.48 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 221, indent_spaces: 218, structural_boundaries: 143, branch: 57
- `src/bun.js/bindings/webcore/SerializedScriptValue.cpp` (CPP) | Magnitude: 2802.96 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 2311, state_mutation: 1601, branch: 772, structural_boundaries: 465
- `packages/bun-uws/src/MoveOnlyFunction.h` (CPP) | Magnitude: 426.7 | Delta: **0.044 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 370, indent_spaces: 203, structural_boundaries: 144, branch: 42

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `src/js/internal/streams/duplex.ts` (TYPESCRIPT) | Magnitude: 7.45 | Delta: **0.043 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 37, state_mutation: 33, reflection_metaprogramming: 22, branch: 11
- `src/js/node/path.ts` (TYPESCRIPT) | Magnitude: 4.52 | Delta: **0.058 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 52, reflection_metaprogramming: 24, branch: 9, io: 7
- `src/deps/uucode/src/get.zig` (ZIG) | Magnitude: 155.34 | Delta: **0.058 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 92, branch: 53, reflection_metaprogramming: 43, encapsulation: 31
- `src/bun.js/api/ffi-stdalign.h` (CPP) | Magnitude: 21.22 | Delta: **0.068 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: macros: 10, reflection_metaprogramming: 7, state_mutation: 6, branch: 3
- `src/bun.js/bindings/sqlite/sqlite3_local.h` (CPP) | Magnitude: 32.74 | Delta: **0.087 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: macros: 365, reflection_metaprogramming: 343, pointers: 320, indent_spaces: 319

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/install/install_binding.zig` (ZIG) | Magnitude: 37.94 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 48, globals: 24, encapsulation: 23, immutability_locks: 21
- `src/install/resolvers/folder_resolver.zig` (ZIG) | Magnitude: 242.14 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 287, globals: 63, encapsulation: 61, branch: 57
- `src/bun.js/bindings/JSX509CertificatePrototype.h` (CPP) | Magnitude: 22.26 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 25, structural_boundaries: 13, state_mutation: 10, args: 7
- `src/bun.js/bindings/ScriptExecutionContext.h` (CPP) | Magnitude: 8.64 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 106, structural_boundaries: 32, safety_bypasses: 25, branch: 18
- `src/bun.js/bindings/webcrypto/CryptoKeyRSAComponents.h` (CPP) | Magnitude: 234.32 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: state_mutation: 182, indent_spaces: 56, immutability_locks: 36, branch: 23

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `src/cli/uninstall.ps1` (POWERSHELL) | Magnitude: 63.7 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 63, branch: 32, state_mutation: 32, closures: 28
- `bench/snippets/buffer-read.js` (JAVASCRIPT) | Magnitude: 8.7 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: structural_boundaries: 44, args: 39, func_start: 39, closures: 39
- `bench/snippets/buffer.js` (JAVASCRIPT) | Magnitude: 24.54 | Delta: **0.06 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: structural_boundaries: 46, args: 40, func_start: 40, closures: 40

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `src/sql/mysql/protocol/NewReader.zig` (ZIG) | Magnitude: 190.64 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 106, branch: 39, api: 29, structural_boundaries: 22
- `src/ast/parseImportExport.zig` (ZIG) | Magnitude: 715.6 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 353, branch: 147, safety: 67, globals: 48
- `packages/bun-types/ffi.d.ts` (TYPESCRIPT) | Magnitude: 2.12 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 183, doc: 47, structural_boundaries: 26, generics: 22
- `src/ptr/shared.zig` (ZIG) | Magnitude: 1519.84 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 438, branch: 156, doc: 121, structural_boundaries: 68
- `packages/bun-types/sqlite.d.ts` (TYPESCRIPT) | Magnitude: 1.92 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: doc: 133, indent_spaces: 129, immutability_locks: 75, structural_boundaries: 26

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/js/internal/fs/cp-sync.ts` (TYPESCRIPT) | Magnitude: 20.82 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 146, branch: 62, structural_boundaries: 37, args: 31
- `src/node-fallbacks/url.js` (JAVASCRIPT) | Magnitude: 905.72 | Delta: **0.052 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 388, state_mutation: 384, branch: 185, structural_boundaries: 76
- `bench/cat/cat.mjs` (JAVASCRIPT) | Magnitude: 15.08 | Delta: **0.07 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: branch: 3, structural_boundaries: 3, state_mutation: 3, immutability_locks: 2
- `src/node-fallbacks/util.js` (JAVASCRIPT) | Magnitude: 457.42 | Delta: **0.074 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 331, structural_boundaries: 106, branch: 101, state_mutation: 86
- `src/codegen/helpers.ts` (TYPESCRIPT) | Magnitude: 12.17 | Delta: **0.1 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 102, structural_boundaries: 44, branch: 27, api: 24

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `src/init/react-app/src/App.tsx` (TYPESCRIPT) | Magnitude: 0.49 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 7, ui_framework: 5, import: 3
- `packages/bun-types/shell.d.ts` (TYPESCRIPT) | Magnitude: 1.32 | Delta: **0.047 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 29, doc: 23, args: 14, func_start: 14
- `src/init/react-tailwind/src/App.tsx` (TYPESCRIPT) | Magnitude: 0.55 | Delta: **0.047 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 7, ui_framework: 7, import: 3
- `packages/bun-error/index.tsx` (TYPESCRIPT) | Magnitude: 49.93 | Delta: **0.067 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 682, state_mutation: 149, branch: 148, structural_boundaries: 121
- `bench/snippets/react-dom-render.bun.js` (JAVASCRIPT) | Magnitude: 33.46 | Delta: **0.136 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: structural_boundaries: 33, concurrency: 25, indent_spaces: 19, func_start: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `bench/snippets/peek-promise.mjs` (JAVASCRIPT) | Magnitude: 20.86 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 17, concurrency: 7, args: 6, func_start: 6
- `bench/snippets/shell-spawn.mjs` (JAVASCRIPT) | Magnitude: 33.38 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 19, concurrency: 13, args: 8
- `bench/postMessage/structureClone-string.mjs` (JAVASCRIPT) | Magnitude: 35.98 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: func_start: 16, indent_spaces: 15, structural_boundaries: 12, duplicate_logic: 12
- `src/darwin.zig` (ZIG) | Magnitude: 68.8 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 78, api: 38, immutability_locks: 30, args: 26
- `src/bun.js/bindings/libuv/generate_uv_posix_stubs.ts` (TYPESCRIPT) | Magnitude: 36.36 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 270, structural_boundaries: 80, state_mutation: 70, branch: 62

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `packages/bun-uws/src/ProxyParser.h` (CPP) | Magnitude: 75.54 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 69, state_mutation: 43, structural_boundaries: 24, branch: 12
- `src/bun.js/node/assert/myers_diff.zig` (ZIG) | Magnitude: 380.56 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 445, branch: 139, immutability_locks: 131, globals: 70
- `packages/bun-native-plugin-rs/src/lib.rs` (RUST) | Magnitude: 122.72 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: doc: 343, indent_spaces: 229, structural_boundaries: 52, state_mutation: 38
- `src/js/builtins/Ipc.ts` (TYPESCRIPT) | Magnitude: 2.82 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 21, dead_code: 17, doc: 14, branch: 7
- `packages/bun-usockets/src/crypto/default_ciphers.h` (CPP) | Magnitude: 0.15 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 16, macros: 2, dead_code: 1, reflection_metaprogramming: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `src/feature_flags.zig` (ZIG) | Magnitude: 48.7 | Delta: **0.05 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 61, api: 36, immutability_locks: 35, globals: 33
- `src/ast/TS.zig` (ZIG) | Magnitude: 31.76 | Delta: **0.093 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 97, indent_spaces: 84, api: 16, globals: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/bake/incremental_visualizer.html` (HTML) | Magnitude: 167.68 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 353, structural_boundaries: 55, state_mutation: 42, immutability_locks: 41
- `src/bun.js/bindings/Base64Helpers.h` (CPP) | Magnitude: 14.12 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 2, fragile_debt: 2, args: 1, state_mutation: 1
- `src/bundler/linker_context/generateCompileResultForHtmlChunk.zig` (ZIG) | Magnitude: 86.4 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 264, branch: 95, state_mutation: 68, immutability_locks: 60
- `src/js/internal/streams/legacy.ts` (TYPESCRIPT) | Magnitude: 11.19 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 67, state_mutation: 24, branch: 23, func_start: 16
- `src/bun.js/bindings/NodeAsyncHooks.cpp` (CPP) | Magnitude: 5.94 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 6, pointers: 6, import: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `src/bun.js/bindings/TextCodecReplacement.h` (CPP) | Magnitude: 17.3 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 6, args: 5, immutability_locks: 5, structural_boundaries: 4
- `src/bun.js/bindings/TextCodecUserDefined.h` (CPP) | Magnitude: 17.28 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: args: 5, immutability_locks: 5, indent_spaces: 5, structural_boundaries: 4
- `src/bun.js/bindings/TextCodecASCIIFastPath.h` (CPP) | Magnitude: 24.88 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 15, safety: 12, state_mutation: 12
- `src/bun.js/bindings/webcrypto/CryptoAlgorithmEd25519.h` (CPP) | Magnitude: 148.74 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 145, branch: 19, immutability_locks: 19, indent_spaces: 13
- `src/bun.js/bindings/ZigGeneratedCode.cpp` (CPP) | Magnitude: 96.68 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 160, pointers: 91, args: 59, structural_boundaries: 38

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `packages/bun-types/bun.d.ts` -> Churn: **100.0%** | Cog Load: 9.5561% | Debt: 99.9999%
- `src/bun.js/bindings/bindings.cpp` -> Churn: **96.92%** | Cog Load: 88.3688% | Debt: 99.9998%
- `src/bun.js/bindings/ZigGlobalObject.cpp` -> Churn: **92.89%** | Cog Load: 89.3418% | Debt: 99.9995%
- `src/bun.zig` -> Churn: **90.65%** | Cog Load: 21.2719% | Debt: 99.9647%
- `src/bun.js/webcore/Blob.zig` -> Churn: **82.72%** | Cog Load: 30.0318% | Debt: 92.7644%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/api/schema.js` -> **Dylan Conway** (100.0% isolated ownership) | Magnitude: 3243.56
- `src/css/properties/properties_generated.zig` -> **pfg** (100.0% isolated ownership) | Magnitude: 2186.18
- `src/ast/lowerDecorators.zig` -> **Jarred Sumner** (100.0% isolated ownership) | Magnitude: 2028.7
- `src/bun.js/webview/ChromeBackend.cpp` -> **Jarred Sumner** (100.0% isolated ownership) | Magnitude: 1610.26
- `src/deps/uucode/src/types.zig` -> **Jarred Sumner** (100.0% isolated ownership) | Magnitude: 1454.64

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

- `src/bun.js/bindings/root.h` -> **Severity: 1677.106** (Blast Radius: 64.838 * Doc Risk: 25.8661%)
- `src/bun.js/bindings/ZigGlobalObject.h` -> **Severity: 1273.4** (Blast Radius: 12.734 * Doc Risk: 100.0%)
- `src/bun.js/bindings/JSDOMWrapper.h` -> **Severity: 758.1** (Blast Radius: 7.581 * Doc Risk: 100.0%)
- `src/codegen/bindgenv2/internal/any.ts` -> **Severity: 482.7** (Blast Radius: 4.827 * Doc Risk: 100.0%)
- `src/bun.js/bindings/BunClientData.h` -> **Severity: 370.667** (Blast Radius: 6.129 * Doc Risk: 60.4776%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
