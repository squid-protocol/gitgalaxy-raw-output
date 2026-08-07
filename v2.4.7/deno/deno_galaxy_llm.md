# ARCHITECTURAL_BRIEF: deno
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_rust/deno` |
| **Timestamp** | `2026-08-07T04:05:05.085638+00:00` |
| **Scan Duration** | `15.8s` |
| **Git Branch** | `main` |
| **Git Commit** | `d198cda44b7fddb56d892a8ef2349d1630adfa37` |
| **Git Remote** | `https://github.com/denoland/deno.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 3786 malicious artifacts.

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
| Total Artifacts | 11685 |
| Analyzed Artifacts (Scanned) | 6701 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 4984 |
| Total LOC | 482895 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 57.3% |
| Dominant Lang | PLAINTEXT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.4296 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 21 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JSON | 2339 | 47293 | 34.9% |
| TYPESCRIPT | 2107 | 77711 | 31.4% |
| JAVASCRIPT | 875 | 61426 | 13.1% |
| RUST | 782 | 295183 | 11.7% |
| PLAINTEXT | 439 | 81 | 6.6% |
| MARKDOWN | 93 | 0 | 1.4% |
| HTML | 16 | 278 | 0.2% |
| CSS | 10 | 65 | 0.1% |
| YAML | 10 | 24 | 0.1% |
| SQLITE | 9 | 44 | 0.1% |
| XML | 8 | 0 | 0.1% |
| C | 3 | 103 | 0.0% |
| M4 | 3 | 182 | 0.0% |
| MAKEFILE | 2 | 330 | 0.0% |
| CPP | 2 | 40 | 0.0% |
| BINARY_THREAT | 2 | 2 | 0.0% |
| NIX | 1 | 133 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `6.343`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 4934 | 73.6% |
| file_cluster_13 | 772 | 11.5% |
| file_cluster_0 | 204 | 3.0% |
| file_cluster_4 | 160 | 2.4% |
| Unknown | 81 | 1.2% |
| file_cluster_16 | 56 | 0.8% |
| file_cluster_2 | 11 | 0.2% |
| file_cluster_17 | 10 | 0.1% |
| file_cluster_1 | 8 | 0.1% |
| file_cluster_11 | 6 | 0.1% |
| file_cluster_6 | 1 | 0.0% |
| file_cluster_15 | 1 | 0.0% |
| file_cluster_12 | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 452 | 6.7% |
| Static: Minified & Vendor Opaque Mass | 4 | 0.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 4984*

**Composition by Extension & Reason:**
- `.out`: 2238x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ts`: 829x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 16x Unsupported Format (.undeterminable), 7x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `.js`: 388x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 6x Excluded: Neighborhood Micro-Mass Limit Exceeded, 1x Excluded (Saturation: Line 5 exceeds 500 chars)
- `.json`: 374x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Unsupported Format (.undeterminable), 2x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `.tgz`: 242x Excluded (Explicitly Denied Extension: '.tgz')
- `.jsonc`: 188x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 79x Unsupported Format (.toml), 56x Excluded (Unsupported Extension: '.toml'), 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rs`: 125x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 2399 LOC), 1x Excluded (Embedded Array/Matrix Payload: 2121 commas in 528 LOC)
- `no_extension`: 69x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 24x Unsupported Format (.undeterminable), 5x Excluded (Binary Format Detected)
- `.lock`: 39x Excluded (Unsupported Extension: '.lock'), 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mjs`: 40x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cjs`: 25x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 20x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.wasm`: 14x Excluded (Unsupported Extension: '.wasm'), 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.der`: 16x Excluded (Explicitly Denied Extension: '.der')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 8.3 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 10.6 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 10.4 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 2.8 | 0.0 | 0.0 |
| API Exposure | 0.0 | 19.3 | 1.5 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 12.7 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 6.8 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 64.6 | 0.3 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 53.8 | 40.0 | 100.0 |
| Instability Exposure | 0.0 | 8.8 | 0.9 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 5.2 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 6.3 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 52.8 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `ext/node/polyfills/fs.ts` (Hits: 279)
- `cli/rt/file_system.rs` (Hits: 99)
- `ext/node/polyfills/path/_posix.ts` (Hits: 73)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **ts.rs** (`libs/config/deno_json/ts.rs`) — 524 inbound connections
2. **test_util.ts** (`tests/unit/test_util.ts`) — 23 inbound connections
3. **web.js** (`ext/node/polyfills/stream/web.js`) — 11 inbound connections
4. **tsx.tsx** (`tests/specs/run/package_json_type/commonjs/jsx/tsx.tsx`) — 7 inbound connections
5. **consumers.js** (`ext/node/polyfills/stream/consumers.js`) — 5 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **language_server.rs** (`cli/lsp/language_server.rs`) — 121 outbound dependencies
2. **tsc.rs** (`cli/lsp/tsc.rs`) — 116 outbound dependencies
3. **process.rs** (`runtime/subprocess_windows/src/process.rs`) — 112 outbound dependencies
4. **factory.rs** (`cli/factory.rs`) — 111 outbound dependencies
5. **module_loader.rs** (`cli/module_loader.rs`) — 110 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `importKeyEC` (@ `ext/crypto/00_crypto.js`) -> Impact: **1061.9** | LOC: 1976
- `weak_callback` (@ `ext/napi/js_native_api.rs`) -> Impact: **653.4** | LOC: 2246
- `resolve` (@ `libs/node_resolver/resolution.rs`) -> Impact: **652.1** | LOC: 1560
  * *Intent:* /// This function is an implementation of `defaultResolve` in /// `lib/internal/modules/esm/resolve.js` from Node.
- `usageIntersection` (@ `ext/crypto/00_crypto.js`) -> Impact: **599.1** | LOC: 1997
- `isBindOptions` (@ `ext/node/polyfills/dgram.ts`) -> Impact: **587.7** | LOC: 1171
- `matches_pkg` (@ `libs/config/workspace/mod.rs`) -> Impact: **586.8** | LOC: 1644
- `resolve_package_subpath_from_deno_module` (@ `libs/node_resolver/resolution.rs`) -> Impact: **538.2** | LOC: 1261
- `parse_compiler_options` (@ `libs/resolver/deno_json.rs`) -> Impact: **528.6** | LOC: 1452
- `npm_system_info` (@ `cli/args/flags.rs`) -> Impact: **451.3** | LOC: 1682
- `config_folders_sorted_by_dependencies` (@ `libs/config/workspace/mod.rs`) -> Impact: **437.6** | LOC: 1650
  * *Intent:* /// Gets the folders sorted by whether they have a dependency on each other.

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `tests/unit_node/crypto/testdata/asymmetric` | 12 | 60000.0 | 0.0% | 0.0% |
| `tests/testdata/tls` | 13 | 55000.0 | 0.0% | 0.0% |
| `tests/unit_node/testdata` | 26 | 25000.2 | 4.44% | 0.0% |
| `tests/specs/npm/npmrc_certfile` | 7 | 20028.34 | 1.43% | 0.0% |
| `tests/wpt/runner/certs` | 5 | 20001.0 | 0.0% | 0.0% |
| `tests/testdata/webcrypto` | 4 | 20000.0 | 0.0% | 0.0% |
| `tests/specs/run/tls_starttls` | 6 | 15054.66 | 9.38% | 0.0% |
| `tests/specs/run/tls_connecttls` | 6 | 15042.8 | 5.58% | 0.0% |
| `cli/lsp` | 31 | 10726.36 | 16.73% | 59.97% |
| `ext/web` | 35 | 10073.93 | 20.43% | 67.01% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `cli/cache/fast_check.rs` -> **100.0%** Exposure
- `cli/integration_tests_runner.rs` -> **100.0%** Exposure
- `cli/lsp/client.rs` -> **100.0%** Exposure
- `cli/lsp/parent_process_checker.rs` -> **100.0%** Exposure
- `cli/rt/integration_tests_runner.rs` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `cli/tools/bundle/html.rs` -> **100.0%** Exposure
- `cli/util/draw_thread.rs` -> **100.0%** Exposure
- `cli/util/retry.rs` -> **100.0%** Exposure
- `cli/util/sync/mod.rs` -> **100.0%** Exposure
- `cli/util/unix.rs` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `ext/node/polyfills/internal/errors.ts` -> **0** Orphaned Functions | **560** Duplicates
- `ext/web/06_streams.js` -> **0** Orphaned Functions | **426** Duplicates
- `cli/args/flags.rs` -> **148** Orphaned Functions | **22** Duplicates
- `cli/tools/lint/ast_buffer/ts_estree.rs` -> **150** Orphaned Functions | **4** Duplicates
- `tests/integration/lsp_tests.rs` -> **145** Orphaned Functions | **9** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`ext/node/polyfills/url.ts`** -> AI Confidence: **99.43%**
2. **`ext/node/polyfills/internal/readline/interface.mjs`** -> AI Confidence: **99.39%**
3. **`ext/node/polyfills/internal/streams/compose.js`** -> AI Confidence: **99.39%**
4. **`ext/node/polyfills/internal/streams/readable.js`** -> AI Confidence: **99.39%**
5. **`ext/node/polyfills/internal/streams/writable.js`** -> AI Confidence: **99.39%**
6. **`ext/node/polyfills/http.ts`** -> AI Confidence: **99.39%**
7. **`ext/node/polyfills/assert.ts`** -> AI Confidence: **99.34%**
8. **`ext/node/polyfills/http2.ts`** -> AI Confidence: **99.34%**
9. **`ext/node/polyfills/internal/crypto/diffiehellman.ts`** -> AI Confidence: **99.34%**
10. **`ext/node/polyfills/path/_posix.ts`** -> AI Confidence: **99.34%**
11. **`tests/bench/stdio/stdio.c`** -> AI Confidence: **99.34%**
12. **`ext/fetch/22_http_client.js`** -> AI Confidence: **99.32%**
13. **`ext/node/polyfills/02_init.js`** -> AI Confidence: **99.32%**
14. **`tests/specs/node/child_process_shell_escape/main.ts`** -> AI Confidence: **99.32%**
15. **`cli/args/flags_net.rs`** -> AI Confidence: **99.31%**
16. **`cli/factory.rs`** -> AI Confidence: **99.31%**
17. **`cli/lsp/path_to_regex.rs`** -> AI Confidence: **99.31%**
18. **`cli/lsp/ts_server.rs`** -> AI Confidence: **99.31%**
19. **`cli/tools/init/mod.rs`** -> AI Confidence: **99.31%**
20. **`cli/util/archive.rs`** -> AI Confidence: **99.31%**
21. **`cli/util/path.rs`** -> AI Confidence: **99.31%**
22. **`ext/node/ops/assert.rs`** -> AI Confidence: **99.31%**
23. **`ext/webgpu/webidl.rs`** -> AI Confidence: **99.31%**
24. **`libs/core/extensions.rs`** -> AI Confidence: **99.31%**
25. **`libs/core/module_specifier.rs`** -> AI Confidence: **99.31%**
26. **`libs/node_resolver/resolution.rs`** -> AI Confidence: **99.31%**
27. **`libs/npm_installer/bin_entries/windows_shim.rs`** -> AI Confidence: **99.31%**
28. **`libs/ops/op2/config.rs`** -> AI Confidence: **99.31%**
29. **`libs/ops/op2/signature.rs`** -> AI Confidence: **99.31%**
30. **`libs/ops/op2/signature_retval.rs`** -> AI Confidence: **99.31%**
31. **`libs/resolver/cjs/mod.rs`** -> AI Confidence: **99.31%**
32. **`libs/resolver/deno_json.rs`** -> AI Confidence: **99.31%**
33. **`libs/resolver/factory.rs`** -> AI Confidence: **99.31%**
34. **`libs/serde_v8/magic/any_value.rs`** -> AI Confidence: **99.31%**
35. **`runtime/fmt_errors.rs`** -> AI Confidence: **99.31%**
36. **`ext/fetch/22_body.js`** -> AI Confidence: **99.31%**
37. **`ext/fetch/23_request.js`** -> AI Confidence: **99.31%**
38. **`ext/fetch/26_fetch.js`** -> AI Confidence: **99.31%**
39. **`ext/fetch/27_eventsource.js`** -> AI Confidence: **99.31%**
40. **`ext/http/01_http.js`** -> AI Confidence: **99.31%**
41. **`ext/image/01_image.js`** -> AI Confidence: **99.31%**
42. **`ext/node/polyfills/_events.mjs`** -> AI Confidence: **99.31%**
43. **`ext/node/polyfills/_http_agent.mjs`** -> AI Confidence: **99.31%**
44. **`ext/node/polyfills/_process/streams.mjs`** -> AI Confidence: **99.31%**
45. **`ext/node/polyfills/_tls_wrap.js`** -> AI Confidence: **99.31%**
46. **`ext/node/polyfills/inspector.js`** -> AI Confidence: **99.31%**
47. **`ext/node/polyfills/internal/assert/assertion_error.js`** -> AI Confidence: **99.31%**
48. **`ext/node/polyfills/internal/buffer.mjs`** -> AI Confidence: **99.31%**
49. **`ext/node/polyfills/internal/console/constructor.mjs`** -> AI Confidence: **99.31%**
50. **`ext/node/polyfills/internal/event_target.mjs`** -> AI Confidence: **99.31%**
51. **`ext/node/polyfills/internal/http2/compat.js`** -> AI Confidence: **99.31%**
52. **`ext/node/polyfills/internal/streams/duplex.js`** -> AI Confidence: **99.31%**
53. **`ext/node/polyfills/internal/streams/duplexify.js`** -> AI Confidence: **99.31%**
54. **`ext/node/polyfills/internal/streams/end-of-stream.js`** -> AI Confidence: **99.31%**
55. **`ext/node/polyfills/internal/streams/operators.js`** -> AI Confidence: **99.31%**
56. **`ext/node/polyfills/internal/streams/pipeline.js`** -> AI Confidence: **99.31%**
57. **`ext/node/polyfills/internal/tty.js`** -> AI Confidence: **99.31%**
58. **`ext/node/polyfills/internal/webstreams/adapters.js`** -> AI Confidence: **99.31%**
59. **`ext/process/40_process.js`** -> AI Confidence: **99.31%**
60. **`ext/web/06_streams.js`** -> AI Confidence: **99.31%**
61. **`ext/web/10_filereader.js`** -> AI Confidence: **99.31%**
62. **`ext/web/13_message_port.js`** -> AI Confidence: **99.31%**
63. **`ext/web/15_performance.js`** -> AI Confidence: **99.31%**
64. **`ext/websocket/01_websocket.js`** -> AI Confidence: **99.31%**
65. **`ext/websocket/02_websocketstream.js`** -> AI Confidence: **99.31%**
66. **`runtime/js/11_workers.js`** -> AI Confidence: **99.31%**
67. **`runtime/js/99_main.js`** -> AI Confidence: **99.31%**
68. **`cli/tsc/dts/node/child_process.d.cts`** -> AI Confidence: **99.31%**
69. **`cli/tsc/dts/node/fs/promises.d.cts`** -> AI Confidence: **99.31%**
70. **`cli/tsc/dts/node/http.d.cts`** -> AI Confidence: **99.31%**
71. **`ext/http/00_serve.ts`** -> AI Confidence: **99.31%**
72. **`ext/node/polyfills/_fs/_fs_glob.ts`** -> AI Confidence: **99.31%**
73. **`ext/node/polyfills/_fs/_fs_read.ts`** -> AI Confidence: **99.31%**
74. **`ext/node/polyfills/_fs/_fs_readdir.ts`** -> AI Confidence: **99.31%**
75. **`ext/node/polyfills/_fs/cp/cp.ts`** -> AI Confidence: **99.31%**
76. **`ext/node/polyfills/_http_outgoing.ts`** -> AI Confidence: **99.31%**
77. **`ext/node/polyfills/child_process.ts`** -> AI Confidence: **99.31%**
78. **`ext/node/polyfills/dgram.ts`** -> AI Confidence: **99.31%**
79. **`ext/node/polyfills/internal/crypto/cipher.ts`** -> AI Confidence: **99.31%**
80. **`ext/node/polyfills/internal/crypto/hash.ts`** -> AI Confidence: **99.31%**
81. **`ext/node/polyfills/internal/crypto/keys.ts`** -> AI Confidence: **99.31%**
82. **`ext/node/polyfills/internal/crypto/random.ts`** -> AI Confidence: **99.31%**
83. **`ext/node/polyfills/internal/crypto/sig.ts`** -> AI Confidence: **99.31%**
84. **`ext/node/polyfills/internal/crypto/x509.ts`** -> AI Confidence: **99.31%**
85. **`ext/node/polyfills/internal/stream_base_commons.ts`** -> AI Confidence: **99.31%**
86. **`ext/node/polyfills/internal/util/comparisons.ts`** -> AI Confidence: **99.31%**
87. **`ext/node/polyfills/internal_binding/pipe_wrap.ts`** -> AI Confidence: **99.31%**
88. **`ext/node/polyfills/internal_binding/stream_wrap.ts`** -> AI Confidence: **99.31%**
89. **`ext/node/polyfills/internal_binding/tcp_wrap.ts`** -> AI Confidence: **99.31%**
90. **`ext/node/polyfills/internal_binding/udp_wrap.ts`** -> AI Confidence: **99.31%**
91. **`ext/node/polyfills/path/_win32.ts`** -> AI Confidence: **99.31%**
92. **`ext/node/polyfills/timers.ts`** -> AI Confidence: **99.31%**
93. **`libs/core/ops_builtin_types.rs`** -> AI Confidence: **99.29%**
94. **`ext/node/polyfills/internal/readline/utils.mjs`** -> AI Confidence: **99.29%**
95. **`ext/node/polyfills/internal/streams/destroy.js`** -> AI Confidence: **99.29%**
96. **`libs/core/examples/wasm.js`** -> AI Confidence: **99.29%**
97. **`tests/registry/npm/@denotest/bin/0.6.0/cli-cjs.js`** -> AI Confidence: **99.29%**
98. **`tests/registry/npm/@denotest/bin/1.0.0/cli-cjs.js`** -> AI Confidence: **99.29%**
99. **`tests/specs/cpu_prof/basic/verify.js`** -> AI Confidence: **99.29%**
100. **`tests/specs/cpu_prof/custom_name/verify.js`** -> AI Confidence: **99.29%**
101. **`tests/specs/cpu_prof/deno_exit/verify.js`** -> AI Confidence: **99.29%**
102. **`tests/specs/cpu_prof/eval/verify.js`** -> AI Confidence: **99.29%**
103. **`tests/specs/cpu_prof/flamegraph/verify.js`** -> AI Confidence: **99.29%**
104. **`tests/specs/future/unstable_flags/main.js`** -> AI Confidence: **99.29%**
105. **`tests/specs/install/global/npm_multiple_bins/assert_uninstalled.js`** -> AI Confidence: **99.29%**
106. **`tests/specs/lint/all/file1.js`** -> AI Confidence: **99.29%**
107. **`tests/specs/lint/compact/file1.js`** -> AI Confidence: **99.29%**
108. **`tests/specs/lint/glob/without_config/file1.js`** -> AI Confidence: **99.29%**
109. **`tests/specs/lint/ignore/without_config/file1.js`** -> AI Confidence: **99.29%**
110. **`tests/specs/lint/json/file1.js`** -> AI Confidence: **99.29%**
111. **`tests/specs/lint/quiet/file1.js`** -> AI Confidence: **99.29%**
112. **`tests/specs/node/errors_have_code/main.cjs`** -> AI Confidence: **99.29%**
113. **`tests/specs/node/worker_threads_resource_limits/oom_worker.mjs`** -> AI Confidence: **99.29%**
114. **`tests/specs/permission/special/main.js`** -> AI Confidence: **99.29%**
115. **`tests/specs/run/cjs/check_source_line_is_correct/index.cjs`** -> AI Confidence: **99.29%**
116. **`tests/specs/run/exit_code/main.js`** -> AI Confidence: **99.29%**
117. **`tests/testdata/benches/text_decoder_perf.js`** -> AI Confidence: **99.29%**
118. **`tests/testdata/subdir/shebang_file.js`** -> AI Confidence: **99.29%**
119. **`tests/testdata/workers/event_worker.js`** -> AI Confidence: **99.29%**
120. **`tests/testdata/workers/non_deno_worker.js`** -> AI Confidence: **99.29%**
121. **`tests/testdata/workers/test_worker.js`** -> AI Confidence: **99.29%**
122. **`tools/verify_pr_title.js`** -> AI Confidence: **99.29%**
123. **`ext/node/polyfills/internal/http2/util.ts`** -> AI Confidence: **99.29%**
124. **`ext/node/polyfills/internal/process/warning.ts`** -> AI Confidence: **99.29%**
125. **`ext/node/polyfills/internal_binding/constants.ts`** -> AI Confidence: **99.29%**
126. **`ext/node/polyfills/internal_binding/node_options.ts`** -> AI Confidence: **99.29%**
127. **`ext/webidl/internal.d.ts`** -> AI Confidence: **99.29%**
128. **`libs/core_testing/integration/error_rejection_order/error_rejection_order.ts`** -> AI Confidence: **99.29%**
129. **`libs/core_testing/integration/error_with_stack/error_with_stack.ts`** -> AI Confidence: **99.29%**
130. **`libs/core_testing/integration/wasm_stack_trace/wasm_stack_trace.ts`** -> AI Confidence: **99.29%**
131. **`tests/registry/jsr/@std/path/0.220.1/_common/normalize_string.ts`** -> AI Confidence: **99.29%**
132. **`tests/specs/bench/allow_none/allow_none.ts`** -> AI Confidence: **99.29%**
133. **`tests/specs/bench/ignore/ignore.ts`** -> AI Confidence: **99.29%**
134. **`tests/specs/bundle/require_browser/has-createrequire.ts`** -> AI Confidence: **99.29%**
135. **`tests/specs/check/compiler_options_types/set_node_modules_dir.ts`** -> AI Confidence: **99.29%**
136. **`tests/specs/check/definitely_typed/set_node_modules_dir.ts`** -> AI Confidence: **99.29%**
137. **`tests/specs/check/import_meta_no_errors/set_node_modules_dir.ts`** -> AI Confidence: **99.29%**
138. **`tests/specs/check/type_reference_import_meta/set_node_modules_dir.ts`** -> AI Confidence: **99.29%**
139. **`tests/specs/check/use_unknown_in_catch_variables/main.ts`** -> AI Confidence: **99.29%**
140. **`tests/specs/compile/code_cache/cleanup.ts`** -> AI Confidence: **99.29%**
141. **`tests/specs/compile/determinism/assert_equal.ts`** -> AI Confidence: **99.29%**
142. **`tests/specs/compile/relative_permissions/main.ts`** -> AI Confidence: **99.29%**
143. **`tests/specs/doc/html/check_file.ts`** -> AI Confidence: **99.29%**
144. **`tests/specs/install/byonm_run_tag_after_install/replace-version-req.ts`** -> AI Confidence: **99.29%**
145. **`tests/specs/install/cache_out_of_date_with_lockfile/update.ts`** -> AI Confidence: **99.29%**
146. **`tests/specs/install/deno_install_arch/verify_output.ts`** -> AI Confidence: **99.29%**
147. **`tests/specs/install/directories_bin/verify_setup.ts`** -> AI Confidence: **99.29%**
148. **`tests/specs/lockfile/out_of_date_npm_info/rm-version.ts`** -> AI Confidence: **99.29%**
149. **`tests/specs/node/process_title/main.ts`** -> AI Confidence: **99.29%**
150. **`tests/specs/npm/link_npm_package_deep/backup_linked.ts`** -> AI Confidence: **99.29%**
151. **`tests/specs/npm/link_npm_package_deep/verify_linked.ts`** -> AI Confidence: **99.29%**
152. **`tests/specs/npm/link_npm_package_top_level/backup_cowsay.ts`** -> AI Confidence: **99.29%**
153. **`tests/specs/npm/link_npm_package_top_level/verify_cowsay.ts`** -> AI Confidence: **99.29%**
154. **`tests/specs/permission/deny_run_binary_absolute_path/main.ts`** -> AI Confidence: **99.29%**
155. **`tests/specs/permission/ignore_env/config/main.ts`** -> AI Confidence: **99.29%**
156. **`tests/specs/permission/ignore_env/flags/main.ts`** -> AI Confidence: **99.29%**
157. **`tests/specs/permission/ignore_read/config/main.ts`** -> AI Confidence: **99.29%**
158. **`tests/specs/permission/ignore_read/flags/main.ts`** -> AI Confidence: **99.29%**
159. **`tests/specs/permission/path_case_insensitive/main.ts`** -> AI Confidence: **99.29%**
160. **`tests/specs/permission/path_not_permitted/main.ts`** -> AI Confidence: **99.29%**
161. **`tests/specs/permission/path_not_permitted/sub.ts`** -> AI Confidence: **99.29%**
162. **`tests/specs/permission/write_allow_binary/main.ts`** -> AI Confidence: **99.29%**
163. **`tests/specs/permission/write_allow_binary/sub.ts`** -> AI Confidence: **99.29%**
164. **`tests/specs/run/_070_location/070_location.ts`** -> AI Confidence: **99.29%**
165. **`tests/specs/run/_071_location_unset/071_location_unset.ts`** -> AI Confidence: **99.29%**
166. **`tests/specs/run/error_019_stack_function/error_019_stack_function.ts`** -> AI Confidence: **99.29%**
167. **`tests/specs/run/error_additional_property_keys_panic/main.ts`** -> AI Confidence: **99.29%**
168. **`tests/specs/run/ld_preload/env_arg.ts`** -> AI Confidence: **99.29%**
169. **`tests/specs/run/ld_preload/set_with_allow_env.ts`** -> AI Confidence: **99.29%**
170. **`tests/specs/run/no_deno_json/code/noconfig.ts`** -> AI Confidence: **99.29%**
171. **`tests/specs/run/node_env_var_allowlist/node_env_var_allowlist.ts`** -> AI Confidence: **99.29%**
172. **`tests/specs/run/run_coverage/foo.ts`** -> AI Confidence: **99.29%**
173. **`tests/specs/run/sqlite_numbered_params/main.ts`** -> AI Confidence: **99.29%**
174. **`tests/specs/run/tz_env/main.ts`** -> AI Confidence: **99.29%**
175. **`tests/testdata/run/066_prompt.ts`** -> AI Confidence: **99.29%**
176. **`tests/testdata/run/090_run_permissions_request_sync.ts`** -> AI Confidence: **99.29%**
177. **`tests/testdata/run/tty_raw_mode_arrow_keys.ts`** -> AI Confidence: **99.29%**
178. **`tests/testdata/workers/bench_worker.ts`** -> AI Confidence: **99.29%**
179. **`tests/testdata/workers/test_worker.ts`** -> AI Confidence: **99.29%**
180. **`ext/node/polyfills/fs.ts`** -> AI Confidence: **99.25%**
181. **`ext/node/polyfills/internal/child_process.ts`** -> AI Confidence: **99.25%**
182. **`ext/node/polyfills/net.ts`** -> AI Confidence: **99.25%**
183. **`ext/node/polyfills/worker_threads.ts`** -> AI Confidence: **99.25%**
184. **`cli/args/mod.rs`** -> AI Confidence: **99.24%**
185. **`cli/lsp/analysis.rs`** -> AI Confidence: **99.24%**
186. **`cli/lsp/testing/collectors.rs`** -> AI Confidence: **99.24%**
187. **`cli/rt/binary.rs`** -> AI Confidence: **99.24%**
188. **`cli/rt/file_system.rs`** -> AI Confidence: **99.24%**
189. **`cli/tools/clean.rs`** -> AI Confidence: **99.24%**
190. **`cli/tools/info.rs`** -> AI Confidence: **99.24%**
191. **`cli/tools/installer/local.rs`** -> AI Confidence: **99.24%**
192. **`cli/tools/installer/mod.rs`** -> AI Confidence: **99.24%**
193. **`cli/tools/pm/approve_scripts.rs`** -> AI Confidence: **99.24%**
194. **`cli/tools/pm/interactive_picker.rs`** -> AI Confidence: **99.24%**
195. **`cli/tools/pm/mod.rs`** -> AI Confidence: **99.24%**
196. **`cli/tools/publish/diagnostics.rs`** -> AI Confidence: **99.24%**
197. **`cli/tools/publish/mod.rs`** -> AI Confidence: **99.24%**
198. **`cli/tools/run/mod.rs`** -> AI Confidence: **99.24%**
199. **`cli/tools/task.rs`** -> AI Confidence: **99.24%**
200. **`cli/tools/test/fmt.rs`** -> AI Confidence: **99.24%**
201. **`cli/tools/x.rs`** -> AI Confidence: **99.24%**
202. **`cli/tsc/diagnostics.rs`** -> AI Confidence: **99.24%**
203. **`ext/crypto/export_key.rs`** -> AI Confidence: **99.24%**
204. **`ext/crypto/import_key.rs`** -> AI Confidence: **99.24%**
205. **`ext/fs/interface.rs`** -> AI Confidence: **99.24%**
206. **`ext/fs/std_fs.rs`** -> AI Confidence: **99.24%**
207. **`ext/net/raw.rs`** -> AI Confidence: **99.24%**
208. **`ext/node/ops/fs.rs`** -> AI Confidence: **99.24%**
209. **`ext/node/ops/os/priority.rs`** -> AI Confidence: **99.24%**
210. **`ext/node/ops/util.rs`** -> AI Confidence: **99.24%**
211. **`ext/node_crypto/sign.rs`** -> AI Confidence: **99.24%**
212. **`ext/web/compression.rs`** -> AI Confidence: **99.24%**
213. **`libs/config/glob/mod.rs`** -> AI Confidence: **99.24%**
214. **`libs/core/runtime/ops.rs`** -> AI Confidence: **99.24%**
215. **`libs/core/runtime/stats.rs`** -> AI Confidence: **99.24%**
216. **`libs/core/uv_compat.rs`** -> AI Confidence: **99.24%**
217. **`libs/lockfile/transforms.rs`** -> AI Confidence: **99.24%**
218. **`libs/node_resolver/errors.rs`** -> AI Confidence: **99.24%**
219. **`libs/npm_cache/fs_util.rs`** -> AI Confidence: **99.24%**
220. **`libs/npm_installer/factory.rs`** -> AI Confidence: **99.24%**
221. **`libs/ops/conversion/from_v8/struct.rs`** -> AI Confidence: **99.24%**
222. **`libs/ops/cppgc.rs`** -> AI Confidence: **99.24%**
223. **`libs/ops/webidl/dictionary.rs`** -> AI Confidence: **99.24%**
224. **`libs/resolver/graph.rs`** -> AI Confidence: **99.24%**
225. **`libs/resolver/npm/byonm.rs`** -> AI Confidence: **99.24%**
226. **`libs/resolver/npm/managed/common.rs`** -> AI Confidence: **99.24%**
227. **`libs/resolver/workspace.rs`** -> AI Confidence: **99.24%**
228. **`libs/typescript_go_client/src/lib.rs`** -> AI Confidence: **99.24%**
229. **`tests/bench/main.rs`** -> AI Confidence: **99.24%**
230. **`tests/node_compat/mod.rs`** -> AI Confidence: **99.24%**
231. **`tests/specs/mod.rs`** -> AI Confidence: **99.24%**
232. **`tests/util/server/npm.rs`** -> AI Confidence: **99.24%**
233. **`tests/util/server/servers/mod.rs`** -> AI Confidence: **99.24%**
234. **`ext/node/polyfills/_readline.mjs`** -> AI Confidence: **99.24%**
235. **`ext/node/polyfills/internal/fs/streams.mjs`** -> AI Confidence: **99.24%**
236. **`ext/node/polyfills/internal/fs/utils.mjs`** -> AI Confidence: **99.24%**
237. **`tests/bench/testdata/express-router.js`** -> AI Confidence: **99.24%**
238. **`ext/node/polyfills/crypto.ts`** -> AI Confidence: **99.24%**
239. **`ext/node/polyfills/internal/fs/handle.ts`** -> AI Confidence: **99.24%**
240. **`cli/tools/jupyter/install.rs`** -> AI Confidence: **99.23%**
241. **`libs/cache_dir/deno_dir.rs`** -> AI Confidence: **99.23%**
242. **`libs/config/deno_json/permissions.rs`** -> AI Confidence: **99.23%**
243. **`libs/ops/conversion/mod.rs`** -> AI Confidence: **99.23%**
244. **`ext/cache/01_cache.js`** -> AI Confidence: **99.23%**
245. **`ext/node/polyfills/internal/util/parse_args/parse_args.js`** -> AI Confidence: **99.23%**
246. **`ext/web/01_console.js`** -> AI Confidence: **99.23%**
247. **`cli/tsc/dts/node/buffer.d.cts`** -> AI Confidence: **99.23%**
248. **`ext/node/polyfills/sqlite.ts`** -> AI Confidence: **99.23%**
249. **`ext/crypto/00_crypto.js`** -> AI Confidence: **99.22%**
250. **`tools/memfd_create_shim.c`** -> AI Confidence: **99.2%**
251. **`cli/cache/module_info.rs`** -> AI Confidence: **99.18%**
252. **`cli/cache/node.rs`** -> AI Confidence: **99.18%**
253. **`cli/file_fetcher.rs`** -> AI Confidence: **99.18%**
254. **`cli/graph_container.rs`** -> AI Confidence: **99.18%**
255. **`cli/http_util.rs`** -> AI Confidence: **99.18%**
256. **`cli/jsr.rs`** -> AI Confidence: **99.18%**
257. **`cli/lsp/logging.rs`** -> AI Confidence: **99.18%**
258. **`cli/lsp/parent_process_checker.rs`** -> AI Confidence: **99.18%**
259. **`cli/lsp/trace.rs`** -> AI Confidence: **99.18%**
260. **`cli/module_loader.rs`** -> AI Confidence: **99.18%**
261. **`cli/npm.rs`** -> AI Confidence: **99.18%**
262. **`cli/rt/code_cache.rs`** -> AI Confidence: **99.18%**
263. **`cli/rt/run.rs`** -> AI Confidence: **99.18%**
264. **`cli/standalone/virtual_fs.rs`** -> AI Confidence: **99.18%**
265. **`cli/tools/bundle/provider.rs`** -> AI Confidence: **99.18%**
266. **`cli/tools/jupyter/mod.rs`** -> AI Confidence: **99.18%**
267. **`cli/tools/lint/linter.rs`** -> AI Confidence: **99.18%**
268. **`cli/tools/lint/rules/mod.rs`** -> AI Confidence: **99.18%**
269. **`cli/tools/publish/module_content.rs`** -> AI Confidence: **99.18%**
270. **`cli/tools/publish/provenance.rs`** -> AI Confidence: **99.18%**
271. **`cli/tools/publish/tar.rs`** -> AI Confidence: **99.18%**
272. **`cli/tools/test/sanitizers.rs`** -> AI Confidence: **99.18%**
273. **`cli/util/console.rs`** -> AI Confidence: **99.18%**
274. **`cli/util/file_watcher.rs`** -> AI Confidence: **99.18%**
275. **`cli/util/fs.rs`** -> AI Confidence: **99.18%**
276. **`ext/cache/lsc_shard.rs`** -> AI Confidence: **99.18%**
277. **`ext/cron/local.rs`** -> AI Confidence: **99.18%**
278. **`ext/cron/socket.rs`** -> AI Confidence: **99.18%**
279. **`ext/crypto/ed25519.rs`** -> AI Confidence: **99.18%**
280. **`ext/crypto/encrypt.rs`** -> AI Confidence: **99.18%**
281. **`ext/fetch/proxy.rs`** -> AI Confidence: **99.18%**
282. **`ext/ffi/call.rs`** -> AI Confidence: **99.18%**
283. **`ext/ffi/callback.rs`** -> AI Confidence: **99.18%**
284. **`ext/ffi/dlfcn.rs`** -> AI Confidence: **99.18%**
285. **`ext/http/http_next.rs`** -> AI Confidence: **99.18%**
286. **`ext/http/request_body.rs`** -> AI Confidence: **99.18%**
287. **`ext/http/service.rs`** -> AI Confidence: **99.18%**
288. **`ext/image/bitmap.rs`** -> AI Confidence: **99.18%**
289. **`ext/image/image_ops.rs`** -> AI Confidence: **99.18%**
290. **`ext/io/bi_pipe.rs`** -> AI Confidence: **99.18%**
291. **`ext/io/fs.rs`** -> AI Confidence: **99.18%**
292. **`ext/kv/remote.rs`** -> AI Confidence: **99.18%**
293. **`ext/kv/sqlite.rs`** -> AI Confidence: **99.18%**
294. **`ext/net/ops_tls.rs`** -> AI Confidence: **99.18%**
295. **`ext/net/ops_unix.rs`** -> AI Confidence: **99.18%**
296. **`ext/net/quic.rs`** -> AI Confidence: **99.18%**
297. **`ext/node/ops/handle_wrap.rs`** -> AI Confidence: **99.18%**
298. **`ext/node/ops/http.rs`** -> AI Confidence: **99.18%**
299. **`ext/node/ops/http2/stream.rs`** -> AI Confidence: **99.18%**
300. **`ext/node/ops/os/cpus.rs`** -> AI Confidence: **99.18%**
301. **`ext/node/ops/tls.rs`** -> AI Confidence: **99.18%**
302. **`ext/node/ops/vm.rs`** -> AI Confidence: **99.18%**
303. **`ext/node_crypto/md5_sha1.rs`** -> AI Confidence: **99.18%**
304. **`ext/node_sqlite/session.rs`** -> AI Confidence: **99.18%**
305. **`ext/node_sqlite/sql_tag_store.rs`** -> AI Confidence: **99.18%**
306. **`ext/process/ipc.rs`** -> AI Confidence: **99.18%**
307. **`ext/web/message_port.rs`** -> AI Confidence: **99.18%**
308. **`ext/web/stream_resource.rs`** -> AI Confidence: **99.18%**
309. **`ext/webgpu/buffer.rs`** -> AI Confidence: **99.18%**
310. **`ext/webgpu/command_encoder.rs`** -> AI Confidence: **99.18%**
311. **`ext/webgpu/device.rs`** -> AI Confidence: **99.18%**
312. **`ext/webgpu/error.rs`** -> AI Confidence: **99.18%**
313. **`ext/webgpu/query_set.rs`** -> AI Confidence: **99.18%**
314. **`ext/webgpu/render_pipeline.rs`** -> AI Confidence: **99.18%**
315. **`ext/webgpu/texture.rs`** -> AI Confidence: **99.18%**
316. **`libs/cache_dir/cache.rs`** -> AI Confidence: **99.18%**
317. **`libs/cache_dir/file_fetcher/auth_tokens.rs`** -> AI Confidence: **99.18%**
318. **`libs/cache_dir/global/cache_file.rs`** -> AI Confidence: **99.18%**
319. **`libs/cache_dir/global/mod.rs`** -> AI Confidence: **99.18%**
320. **`libs/config/glob/collector.rs`** -> AI Confidence: **99.18%**
321. **`libs/config/glob/gitignore.rs`** -> AI Confidence: **99.18%**
322. **`libs/core/arena/raw_arena.rs`** -> AI Confidence: **99.18%**
323. **`libs/core/examples/snapshot/src/main.rs`** -> AI Confidence: **99.18%**
324. **`libs/core/examples/ts_module_loader.rs`** -> AI Confidence: **99.18%**
325. **`libs/core/extension_set.rs`** -> AI Confidence: **99.18%**
326. **`libs/core/io/buffers.rs`** -> AI Confidence: **99.18%**
327. **`libs/core/io/resource.rs`** -> AI Confidence: **99.18%**
328. **`libs/core/modules/module_map_data.rs`** -> AI Confidence: **99.18%**
329. **`libs/core/ops.rs`** -> AI Confidence: **99.18%**
330. **`libs/core/runtime/bindings.rs`** -> AI Confidence: **99.18%**
331. **`libs/core/runtime/jsruntime.rs`** -> AI Confidence: **99.18%**
332. **`libs/core/runtime/op_driver/mod.rs`** -> AI Confidence: **99.18%**
333. **`libs/core/runtime/setup.rs`** -> AI Confidence: **99.18%**
334. **`libs/core/source_map.rs`** -> AI Confidence: **99.18%**
335. **`libs/core/tasks.rs`** -> AI Confidence: **99.18%**
336. **`libs/core/uv_compat/stream.rs`** -> AI Confidence: **99.18%**
337. **`libs/core_testing/checkin/runner/testing.rs`** -> AI Confidence: **99.18%**
338. **`libs/dcore/src/metrics.rs`** -> AI Confidence: **99.18%**
339. **`libs/eszip/examples/builder.rs`** -> AI Confidence: **99.18%**
340. **`libs/node_resolver/analyze.rs`** -> AI Confidence: **99.18%**
341. **`libs/node_resolver/package_json.rs`** -> AI Confidence: **99.18%**
342. **`libs/npm/registry.rs`** -> AI Confidence: **99.18%**
343. **`libs/npm/resolution/graph.rs`** -> AI Confidence: **99.18%**
344. **`libs/npm/resolution/snapshot.rs`** -> AI Confidence: **99.18%**
345. **`libs/npm_cache/registry_info.rs`** -> AI Confidence: **99.18%**
346. **`libs/npm_installer/extra_info.rs`** -> AI Confidence: **99.18%**
347. **`libs/npm_installer/global.rs`** -> AI Confidence: **99.18%**
348. **`libs/npm_installer/graph.rs`** -> AI Confidence: **99.18%**
349. **`libs/npm_installer/initializer.rs`** -> AI Confidence: **99.18%**
350. **`libs/npm_installer/process_state.rs`** -> AI Confidence: **99.18%**
351. **`libs/ops/conversion/from_v8/mod.rs`** -> AI Confidence: **99.18%**
352. **`libs/ops/conversion/to_v8/mod.rs`** -> AI Confidence: **99.18%**
353. **`libs/ops/op2/dispatch_fast.rs`** -> AI Confidence: **99.18%**
354. **`libs/resolver/cache/disk_cache.rs`** -> AI Confidence: **99.18%**
355. **`libs/resolver/cache/parsed_source.rs`** -> AI Confidence: **99.18%**
356. **`libs/resolver/file_fetcher.rs`** -> AI Confidence: **99.18%**
357. **`libs/resolver/npm/managed/global.rs`** -> AI Confidence: **99.18%**
358. **`libs/resolver/npm/mod.rs`** -> AI Confidence: **99.18%**
359. **`libs/serde_v8/de.rs`** -> AI Confidence: **99.18%**
360. **`libs/serde_v8/magic/buffer.rs`** -> AI Confidence: **99.18%**
361. **`libs/serde_v8/magic/bytestring.rs`** -> AI Confidence: **99.18%**
362. **`libs/serde_v8/magic/detached_buffer.rs`** -> AI Confidence: **99.18%**
363. **`runtime/coverage.rs`** -> AI Confidence: **99.18%**
364. **`runtime/cpu_profiler/mod.rs`** -> AI Confidence: **99.18%**
365. **`runtime/ops/fs_events.rs`** -> AI Confidence: **99.18%**
366. **`runtime/ops/http.rs`** -> AI Confidence: **99.18%**
367. **`runtime/ops/runtime.rs`** -> AI Confidence: **99.18%**
368. **`runtime/ops/tty.rs`** -> AI Confidence: **99.18%**
369. **`runtime/permissions/which.rs`** -> AI Confidence: **99.18%**
370. **`runtime/subprocess_windows/src/anon_pipe.rs`** -> AI Confidence: **99.18%**
371. **`runtime/subprocess_windows/src/process_stdio.rs`** -> AI Confidence: **99.18%**
372. **`runtime/web_worker.rs`** -> AI Confidence: **99.18%**
373. **`tests/bench/lsp.rs`** -> AI Confidence: **99.18%**
374. **`tests/bench_util/js_runtime.rs`** -> AI Confidence: **99.18%**
375. **`tests/integration/jupyter_tests.rs`** -> AI Confidence: **99.18%**
376. **`tests/unit_node/mod.rs`** -> AI Confidence: **99.18%**
377. **`libs/core_testing/checkin/runtime/__init.js`** -> AI Confidence: **99.18%**
378. **`runtime/js/98_global_scope_window.js`** -> AI Confidence: **99.18%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Hardcoded Payload Artifacts
- `ext/node_crypto/x509.rs` -> **52.7577%** Exposure
- `ext/node/ops/tls.rs` -> **37.9014%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `9` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `16695` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `ext/node/polyfills/internal/dns/promises.ts` (TYPESCRIPT) -> Cumulative Risk: **747.82**
- **Archetype:** `file_cluster_8` (Distance: 12.237 IQR)
- **Magnitude:** 41.7 | **LOC:** 593 | **CtrlFlow:** 39.4% | **Authorship Centralization:** 40.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Concurrency (98.1734%), State Flux (94.7857%)
- **Heaviest Functions:** `lookup` (Impact: 49.2), `createLookupPromise` (Impact: 23.4), `_resolve` (Impact: 14.7)

### 2. `ext/node/polyfills/http.ts` (TYPESCRIPT) -> Cumulative Risk: **747.31**
- **Archetype:** `file_cluster_13` (Distance: 14.459 IQR)
- **Magnitude:** 245.72 | **LOC:** 2621 | **CtrlFlow:** 70.4% | **Authorship Centralization:** 22.2%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (97.6266%)
- **Heaviest Functions:** `constructor` (Impact: 185.2), `_writeHeader` (Impact: 107.0), `writeHead` (Impact: 54.9)

### 3. `ext/node/polyfills/_fs/_fs_readdir.ts` (TYPESCRIPT) -> Cumulative Risk: **715.56**
- **Archetype:** `file_cluster_4` (Distance: 12.646 IQR)
- **Magnitude:** 17.92 | **LOC:** 187 | **CtrlFlow:** 64.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.8283%)
- **Heaviest Functions:** `readdir` (Impact: 54.7), `readdirSync` (Impact: 42.5), `decode` (Impact: 7.3)

### 4. `ext/node/polyfills/_http_outgoing.ts` (TYPESCRIPT) -> Cumulative Risk: **683.47**
- **Archetype:** `file_cluster_13` (Distance: 12.992 IQR)
- **Magnitude:** 33.02 | **LOC:** 965 | **CtrlFlow:** 56.2% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (98.6348%)
- **Heaviest Functions:** `_storeHeader` (Impact: 10.5), `setTimeout` (Impact: 9.4), `debug` (Impact: 8.5)

### 5. `ext/node/polyfills/internal/streams/from.js` (JAVASCRIPT) -> Cumulative Risk: **678.94**
- **Archetype:** `file_cluster_4` (Distance: 12.514 IQR)
- **Magnitude:** 293.9 | **LOC:** 219 | **CtrlFlow:** 64.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Concurrency (100.0%), Spec Match (100.0%), State Flux (99.091%)
- **Heaviest Functions:** `from` (Impact: 113.7), `nextSyncWithAsyncValues` (Impact: 23.6), `nextSyncWithSyncValues` (Impact: 20.7)

### 6. `libs/core_testing/checkin/runtime/async.ts` (TYPESCRIPT) -> Cumulative Risk: **671.22**
- **Archetype:** `file_cluster_8` (Distance: 10.13 IQR)
- **Magnitude:** 10.04 | **LOC:** 150 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (96.4916%)
- **Heaviest Functions:** `countWithTraces` (Impact: 11.2), `count` (Impact: 7.5), `op_stats_delete` (Impact: 4.1)

### 7. `ext/node/polyfills/internal/crypto/cipher.ts` (TYPESCRIPT) -> Cumulative Risk: **665.08**
- **Archetype:** `file_cluster_13` (Distance: 12.78 IQR)
- **Magnitude:** 73.13 | **LOC:** 724 | **CtrlFlow:** 47.9% | **Authorship Centralization:** 58.3%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.9999%), Safety Score (90.4094%)
- **Heaviest Functions:** `final` (Impact: 34.0), `final` (Impact: 31.5), `Cipheriv` (Impact: 24.3)

### 8. `ext/node/polyfills/internal_binding/stream_wrap.ts` (TYPESCRIPT) -> Cumulative Risk: **658.9**
- **Archetype:** `file_cluster_13` (Distance: 13.105 IQR)
- **Magnitude:** 41.44 | **LOC:** 512 | **CtrlFlow:** 46.9% | **Authorship Centralization:** 22.2%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Concurrency (99.9644%), State Flux (98.9552%)
- **Heaviest Functions:** `super` (Impact: 102.9), `read` (Impact: 43.9), `writev` (Impact: 29.1)

### 9. `ext/node/polyfills/_http_agent.mjs` (JAVASCRIPT) -> Cumulative Risk: **654.4**
- **Archetype:** `file_cluster_11` (Distance: 13.592 IQR)
- **Magnitude:** 539.26 | **LOC:** 531 | **CtrlFlow:** 64.5% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Cognitive Load (98.0973%)
- **Heaviest Functions:** `Agent` (Impact: 116.2), `addRequest` (Impact: 62.0), `debug` (Impact: 13.1)

### 10. `ext/node/polyfills/internal_binding/cares_wrap.ts` (TYPESCRIPT) -> Cumulative Risk: **651.93**
- **Archetype:** `file_cluster_8` (Distance: 11.42 IQR)
- **Magnitude:** 32.4 | **LOC:** 640 | **CtrlFlow:** 32.4% | **Authorship Centralization:** 40.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Concurrency (98.8084%), State Flux (85.6666%)
- **Heaviest Functions:** `getaddrinfo` (Impact: 53.4), `query` (Impact: 19.5), `queryA` (Impact: 11.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `tests/specs/cert/cafile_compile/RootCA.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/specs/cert/cafile_env_fetch/RootCA.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/specs/cert/cafile_install/RootCA.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/specs/cert/cafile_ts_fetch/RootCA.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/specs/cert/cafile_url_imports/RootCA.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/specs/compile/npmrc_auto_install/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/specs/compile/npmrc_byonm/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/specs/npm/npmrc/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/specs/npm/npmrc_alongside_jsr_scope/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/specs/npm/npmrc_bad_registry_config/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/specs/npm/npmrc_bad_token/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/specs/npm/npmrc_basic_auth/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/specs/npm/npmrc_certfile/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/specs/npm/npmrc_certfile/RootCA.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/specs/npm/npmrc_certfile/client.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/specs/npm/npmrc_certfile/client.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/specs/npm/npmrc_deno_json/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/specs/npm/npmrc_email_auth/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/specs/npm/npmrc_email_no_password/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/specs/npm/npmrc_homedir/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/specs/npm/npmrc_homedir_package_both/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/specs/npm/npmrc_homedir_package_both/subdir/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/specs/npm/npmrc_install_arg/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/specs/npm/npmrc_jsr_scope/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/specs/npm/npmrc_missing_certfile/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.138
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### 🚨 Severe Anti-Patterns (Language Convention Violations)
- `tests/specs/clean/entrypoint/rewrite.ts` (TYPESCRIPT) | **Drift Ratio: 1.64x**
  * **Global Archetype:** `file_cluster_8` (Drift: 4.638 IQR)
  * **Local Reality:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 7.627 IQR)
- `tests/specs/run/set_exit_code_2/set_exit_code_2.ts` (TYPESCRIPT) | **Drift Ratio: 1.6x**
  * **Global Archetype:** `file_cluster_8` (Drift: 3.628 IQR)
  * **Local Reality:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.822 IQR)

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `libs/cache_dir/file_fetcher/auth_tokens.rs` (RUST) | Magnitude: 121.24 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 277, structural_boundaries: 112, safety_bypasses: 39, test: 37
- `libs/core/async_cell.rs` (RUST) | Magnitude: 367.06 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 492, structural_boundaries: 168, generics: 150, args: 61
- `ext/napi/node_api.rs` (RUST) | Magnitude: 291.64 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 491, structural_boundaries: 183, pointers: 95, state_mutation: 88
- `libs/ops/op2/test_cases/async/async_opstate.rs` (RUST) | Magnitude: 4.22 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: safety: 6, structural_boundaries: 3, import: 3, decorators: 2
- `ext/web/stream_resource.rs` (RUST) | Magnitude: 410.88 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 514, structural_boundaries: 175, state_mutation: 87, args: 70

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `ext/node/polyfills/internal/fs/streams.d.ts` (TYPESCRIPT) | Magnitude: 3.6 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 146, structural_boundaries: 113, func_start: 109, args: 99
- `cli/tsc/dts/node/tty.d.cts` (TYPESCRIPT) | Magnitude: 2.43 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 36, doc: 29, structural_boundaries: 24, args: 24
- `cli/tsc/dts/node/cluster.d.cts` (TYPESCRIPT) | Magnitude: 7.23 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 132, func_start: 98, args: 95, structural_boundaries: 92
- `cli/tsc/dts/node/dgram.d.cts` (TYPESCRIPT) | Magnitude: 6.14 | Delta: **0.047 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 137, args: 72, func_start: 72, structural_boundaries: 64
- `cli/tsc/dts/node/net.d.cts` (TYPESCRIPT) | Magnitude: 8.08 | Delta: **0.065 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 330, func_start: 188, args: 175, structural_boundaries: 166

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `ext/node/polyfills/internal/util/debuglog.ts` (TYPESCRIPT) | Magnitude: 1.06 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 7, args: 5, func_start: 3
- `ext/node/polyfills/net.ts` (TYPESCRIPT) | Magnitude: 197.01 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 1302, state_mutation: 666, branch: 364, structural_boundaries: 201
- `ext/node/polyfills/internal/streams/transform.js` (JAVASCRIPT) | Magnitude: 140.96 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 85, state_mutation: 60, branch: 27, func_start: 14
- `tests/wpt/runner/testharnessreport.js` (JAVASCRIPT) | Magnitude: 21.4 | Delta: **0.057 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 16, state_mutation: 6, structural_boundaries: 4, branch: 3
- `ext/node/polyfills/_http_agent.mjs` (JAVASCRIPT) | Magnitude: 539.26 | Delta: **0.094 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 246, state_mutation: 216, branch: 69, func_start: 40

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `libs/core/core.d.ts` (TYPESCRIPT) | Magnitude: 71.42 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 1128, structural_boundaries: 652, api: 584, immutability_locks: 576

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `ext/http/http_next.rs` (RUST) | Magnitude: 691.46 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 938, structural_boundaries: 373, safety: 197, concurrency: 151
- `tests/specs/npm/npmrc_alongside_jsr_scope/main.ts` (TYPESCRIPT) | Magnitude: 1.67 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 2, decorators: 2, import: 2, debug_prints: 2
- `ext/web/benches/url_ops.rs` (RUST) | Magnitude: 6.54 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 6, import: 5, args: 2
- `libs/core/reactor.rs` (RUST) | Magnitude: 27.44 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 25, doc: 22, structural_boundaries: 17, generics: 13
- `tests/specs/node/worker_threads/eval_cjs_require.mjs` (JAVASCRIPT) | Magnitude: 19.24 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: ipc_rpc_bridges: 5, concurrency: 4, structural_boundaries: 3, import: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `cli/tsc/dts/node/readline.d.cts` (TYPESCRIPT) | Magnitude: 5.77 | Delta: **0.073 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 122, structural_boundaries: 87, args: 72, func_start: 71

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `libs/cache_dir/cache.rs` (RUST) | Magnitude: 99.96 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 228, structural_boundaries: 56, generics: 46, safety: 45
- `ext/node/ops/vm.rs` (RUST) | Magnitude: 900.3 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 948, structural_boundaries: 293, generics: 137, state_mutation: 136
- `cli/tsc/dts/node/module.d.cts` (TYPESCRIPT) | Magnitude: 9.12 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 167, doc: 75, structural_boundaries: 67, branch: 33
- `tests/specs/run/jsx_import_source/jsx_import_source_pragma.tsx` (TYPESCRIPT) | Magnitude: 0.49 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 3, args: 2, func_start: 2, indent_spaces: 2
- `tests/specs/run/jsx_import_source/jsx_import_source_pragma_import_map.tsx` (TYPESCRIPT) | Magnitude: 0.49 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 3, args: 2, func_start: 2, indent_spaces: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `tests/bench_util/profiling.rs` (RUST) | Magnitude: 35.84 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 50, structural_boundaries: 15, args: 9, state_mutation: 9
- `libs/core/examples/hello_world.rs` (RUST) | Magnitude: 8.32 | Delta: **0.041 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 5, doc: 4, args: 3
- `tests/specs/bundle/html/same-name-sub-folder-bundle.asserts.ts` (TYPESCRIPT) | Magnitude: 1.66 | Delta: **0.063 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 13, args: 11, func_start: 8, branch: 7
- `ext/node/polyfills/internal/primordials.mjs` (JAVASCRIPT) | Magnitude: 86.67 | Delta: **0.076 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 43, api: 25, immutability_locks: 25, args: 18
- `cli/tools/bundle/provider.rs` (RUST) | Magnitude: 0.1 | Delta: **0.091 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 154, structural_boundaries: 46, safety: 30, concurrency: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `cli/tsc/dts/node/undici/dispatcher.d.ts` (TYPESCRIPT) | Magnitude: 17.71 | Delta: **0.038 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 232, structural_boundaries: 110, safety: 85, args: 84
- `cli/tsc/dts/node/fs/promises.d.cts` (TYPESCRIPT) | Magnitude: 5.3 | Delta: **0.049 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 178, doc: 47, branch: 42, structural_boundaries: 25
- `tests/specs/npm/local_dir_no_duplicate_resolution/main.tsx` (TYPESCRIPT) | Magnitude: 0.2 | Delta: **0.057 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, ui_framework: 3, args: 2, func_start: 2
- `tests/registry/jsr/@std/http/1.0.0/mod.ts` (TYPESCRIPT) | Magnitude: 2.46 | Delta: **0.067 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 15, doc: 12, branch: 9
- `cli/tsc/dts/node/diagnostics_channel.d.cts` (TYPESCRIPT) | Magnitude: 4.71 | Delta: **0.113 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 91, doc: 65, structural_boundaries: 31, generics: 27

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `libs/core/runtime/op_driver/future_arena.rs` (RUST) | Magnitude: 147.0 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 186, structural_boundaries: 74, concurrency: 53, generics: 53
- `ext/net/tunnel.rs` (RUST) | Magnitude: 155.86 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 97, structural_boundaries: 52, concurrency: 51, import: 24
- `tests/specs/cli/otel_basic/http_propagators_call.ts` (TYPESCRIPT) | Magnitude: 1.15 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: io: 2, structural_boundaries: 1, concurrency: 1, sec_io: 1
- `tests/specs/run/fetch_async_error_stack/fetch_async_error_stack.ts` (TYPESCRIPT) | Magnitude: 1.15 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: io: 2, structural_boundaries: 1, concurrency: 1, sec_io: 1
- `libs/core_testing/integration/worker_terminate_op/worker_terminate_op.ts` (TYPESCRIPT) | Magnitude: 2.32 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: concurrency: 8, structural_boundaries: 7, debug_prints: 4, import: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `cli/tsc/dts/node/compatibility/iterators.d.cts` (TYPESCRIPT) | Magnitude: 1.47 | Delta: **0.201 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: generics: 11, structural_boundaries: 10, indent_spaces: 5, class_start: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `cli/tools/publish/module_content.rs` (RUST) | Magnitude: 0.15 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 445, structural_boundaries: 92, safety: 54, import: 34
- `tests/specs/run/_015_duplicate_parallel_import/015_duplicate_parallel_import.js` (JAVASCRIPT) | Magnitude: 17.3 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 5, args: 3, safety: 3
- `tests/specs/compile/bytes_and_text_imports/basic/main.ts` (TYPESCRIPT) | Magnitude: 1.54 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 19, import: 9, debug_prints: 9, io: 3
- `cli/util/archive.rs` (RUST) | Magnitude: 73.02 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 89, branch: 22, structural_boundaries: 17, safety: 11
- `libs/dcore/src/main.rs` (RUST) | Magnitude: 98.72 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 196, structural_boundaries: 54, branch: 29, safety: 21

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `ext/node/polyfills/process.ts` -> Churn: **77.74%** | Cog Load: 26.2851% | Debt: 100.0%
- `cli/args/mod.rs` -> Churn: **76.79%** | Cog Load: 11.1586% | Debt: 66.8497%
- `ext/node/polyfills/internal/child_process.ts` -> Churn: **73.04%** | Cog Load: 37.8553% | Debt: 95.6474%
- `cli/lsp/language_server.rs` -> Churn: **71.2%** | Cog Load: 45.3751% | Debt: 99.7257%
- `ext/node/polyfills/worker_threads.ts` -> Churn: **69.18%** | Cog Load: 49.8118% | Debt: 100.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `ext/node_crypto/keys.rs` -> **Bartek Iwańczuk** (85.7% isolated ownership) | Magnitude: 1363.5
- `libs/eszip/v2.rs` -> **David Sherret** (100.0% isolated ownership) | Magnitude: 1136.18
- `ext/node/polyfills/internal/streams/readable.js` -> **Kenta Moriuchi** (100.0% isolated ownership) | Magnitude: 780.98
- `libs/ops/op2/dispatch_slow.rs` -> **Bartek Iwańczuk** (100.0% isolated ownership) | Magnitude: 671.32
- `ext/node/polyfills/internal/streams/writable.js` -> **Kenta Moriuchi** (100.0% isolated ownership) | Magnitude: 665.22

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `libs/config/deno_json/ts.rs` -> **Severity: 6298.8** (Blast Radius: 62.988 * Doc Risk: 100.0%)
- `ext/net/io.rs` -> **Severity: 77.844** (Blast Radius: 1.343 * Doc Risk: 57.9626%)
- `ext/node/polyfills/stream/web.js` -> **Severity: 45.193** (Blast Radius: 0.917 * Doc Risk: 49.2835%)
- `ext/node/polyfills/internal/util/colors.ts` -> **Severity: 35.491** (Blast Radius: 1.343 * Doc Risk: 26.4266%)
- `cli/tools/bench/mitata.rs` -> **Severity: 25.6** (Blast Radius: 0.256 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
