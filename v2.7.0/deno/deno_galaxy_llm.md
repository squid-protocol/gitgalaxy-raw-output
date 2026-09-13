# ARCHITECTURAL_BRIEF: deno
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/denoland/deno.git` |
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
| Total Artifacts | 11685 |
| Analyzed Artifacts (Scanned) | 10493 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1192 |
| Total LOC | 723906 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 89.8% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2548 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 104 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PLAINTEXT | 2827 | 81 | 26.9% |
| TYPESCRIPT | 2790 | 179766 | 26.6% |
| JSON | 2627 | 51171 | 25.0% |
| JAVASCRIPT | 1179 | 80993 | 11.2% |
| RUST | 898 | 410990 | 8.6% |
| MARKDOWN | 103 | 0 | 1.0% |
| HTML | 17 | 287 | 0.2% |
| CSS | 11 | 69 | 0.1% |
| YAML | 10 | 24 | 0.1% |
| SQLITE | 9 | 44 | 0.1% |
| XML | 8 | 0 | 0.1% |
| C | 3 | 103 | 0.0% |
| PYTHON | 2 | 16 | 0.0% |
| CPP | 2 | 40 | 0.0% |
| M4 | 2 | 77 | 0.0% |
| BINARY_THREAT | 2 | 2 | 0.0% |
| NIX | 1 | 133 | 0.0% |
| CSHARP | 1 | 100 | 0.0% |
| POWERSHELL | 1 | 10 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 7558 | 72.0% |
| Unknown | 81 | 0.8% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2850 | 27.2% |
| Static: Minified & Vendor Opaque Mass | 4 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1192*

**Composition by Extension & Reason:**
- `.tgz`: 242x Excluded (Explicitly Denied Extension: '.tgz')
- `.ts`: 156x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 16x Unsupported Format (.undeterminable), 7x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `.js`: 135x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 6x Excluded: Neighborhood Micro-Mass Limit Exceeded, 1x Excluded (Saturation: Line 5 exceeds 500 chars)
- `.toml`: 79x Unsupported Format (.toml), 58x Excluded (Unsupported Extension: '.toml'), 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 66x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 26x Unsupported Format (.undeterminable), 5x Excluded (Binary Format Detected)
- `.json`: 69x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Excluded: Neighborhood Micro-Mass Limit Exceeded, 3x Unsupported Format (.undeterminable)
- `.out`: 41x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 4 exceeds 500 chars), 1x Excluded (Binary Format Detected)
- `.lock`: 42x Excluded (Unsupported Extension: '.lock')
- `.jsonc`: 21x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.wasm`: 17x Excluded (Unsupported Extension: '.wasm'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.der`: 16x Excluded (Explicitly Denied Extension: '.der')
- `.yml`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rs`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 2399 LOC), 1x Excluded (Embedded Array/Matrix Payload: 2121 commas in 528 LOC)
- `.md`: 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cjs`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Packed Payload Guard (Impossible Density: 3.71 hits/line)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 5.3 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 15.3 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 7.3 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 4.9 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 6.3 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 12.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 6.5 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 64.6 | 0.3 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 34.9 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 7.4 | 0.7 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 4.9 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 26.5 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 19607 | 1072 | 1 | `ext/napi/js_native_api.rs` |
| cleanup | 2147 | 405 | 0 | `tests/integration/lsp_tests.rs` |
| guards | 22740 | 1388 | 2 | `cli/tsc/dts/lib.webworker.d.ts` |
| danger | 16500 | 1403 | 1 | `tests/integration/lsp_tests.rs` |
| concurrency | 24842 | 1445 | 2 | `tests/unit/serve_test.ts` |
| connectivity | 23670 | 2289 | 2 | `cli/tsc/dts/typescript.d.ts` |
| io | 6844 | 814 | 0 | `tests/unit_node/http_test.ts` |
| crypto | 37 | 16 | 0 | `ext/node/polyfills/01_require.js` |
| ipc | 1001 | 262 | 0 | `tests/unit_node/worker_threads_test.ts` |
| time | 1286 | 411 | 0 | `tests/unit/timers_test.ts` |
| serialization | 392 | 182 | 0 | `libs/npm/registry.rs` |
| regex | 279 | 108 | 0 | `ext/node/polyfills/deps/minimatch.js` |
| events | 4284 | 487 | 0 | `tests/unit_node/http_test.ts` |
| tests | 11388 | 613 | 0 | `tests/integration/lsp_tests.rs` |
| docs | 20921 | 873 | 0 | `cli/tsc/dts/lib.webworker.d.ts` |
| debt | 7451 | 2075 | 1 | `cli/tsc/dts/node/http2.d.cts` |
| mutation | 90751 | 2654 | 10 | `tests/integration/lsp_tests.rs` |
| dead_code | 11016 | 1429 | 1 | `cli/tsc/dts/lib.webworker.d.ts` |
| credential | 165 | 30 | 0 | `tests/integration/npm_tests.rs` |
| threat | 3416 | 445 | 0 | `libs/core/core.d.ts` |
| ml_ai | 742 | 140 | 0 | `libs/core/core.d.ts` |
| ui | 120 | 45 | 0 | `cli/tsc/dts/lib.es5.d.ts` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tests/unit_node/http_test.ts` (Hits: 298)
- `ext/node/polyfills/fs.ts` (Hits: 282)
- `tests/unit/fetch_test.ts` (Hits: 249)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **test_util.ts** (`tests/unit/test_util.ts`) — 127 inbound connections
2. **errors.ts** (`ext/node/polyfills/internal/errors.ts`) — 108 inbound connections
3. **validators.mjs** (`ext/node/polyfills/internal/validators.mjs`) — 79 inbound connections
4. **util.mjs** (`ext/node/polyfills/internal/util.mjs`) — 45 inbound connections
5. **00_webidl.js** (`ext/webidl/00_webidl.js`) — 37 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **lib.rs** (`libs/core/lib.rs`) — 169 outbound dependencies
2. **language_server.rs** (`cli/lsp/language_server.rs`) — 121 outbound dependencies
3. **tsc.rs** (`cli/lsp/tsc.rs`) — 116 outbound dependencies
4. **process.rs** (`runtime/subprocess_windows/src/process.rs`) — 112 outbound dependencies
5. **factory.rs** (`cli/factory.rs`) — 111 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `formatRaw` (@ `ext/web/01_console.js`) -> Impact: **474.2** | LOC: 420
- `check_special_file` (@ `runtime/permissions/lib.rs`) -> Impact: **301.0** | LOC: 787
  * *Intent:* /// Checks special file access, returning the failed permission type if /// not successful.
- `urlParse` (@ `ext/node/polyfills/url.ts`) -> Impact: **264.2** | LOC: 324
- `sync_resolution_with_fs` (@ `libs/npm_installer/local.rs`) -> Impact: **256.4** | LOC: 764
- `objectComparisonStart` (@ `ext/node/polyfills/internal/util/comparisons.ts`) -> Impact: **255.3** | LOC: 187
- `iterateSubpatterns` (@ `ext/node/polyfills/_fs/_fs_glob.ts`) -> Impact: **217.5** | LOC: 262
- `importKeyRSA` (@ `ext/crypto/00_crypto.js`) -> Impact: **214.5** | LOC: 420
- `emitKeys` (@ `ext/node/polyfills/internal/readline/utils.mjs`) -> Impact: **208.1** | LOC: 456
  * *Intent:* */
- `write_standalone_binary` (@ `cli/standalone/binary.rs`) -> Impact: **202.1** | LOC: 521
  * *Intent:* /// This functions creates a standalone deno binary by appending a bundle /// and magic trailer to the currently executing binary.
- `formatter` (@ `ext/web/01_console.js`) -> Impact: **197.6** | LOC: 391

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `tests/unit_node/crypto/testdata/asymmetric` | 12 | 60000.0 | 0.0% | 0.0% |
| `tests/testdata/tls` | 13 | 55000.0 | 0.0% | 0.0% |
| `tests/unit_node/testdata` | 26 | 25000.21 | 2.21% | 0.0% |
| `ext/node/polyfills` | 63 | 23897.15 | 36.49% | 24.54% |
| `tests/unit` | 103 | 21574.0 | 19.48% | 0.0% |
| `tests/specs/npm/npmrc_certfile` | 9 | 20030.34 | 0.0% | 0.0% |
| `tests/wpt/runner/certs` | 5 | 20001.0 | 0.0% | 0.0% |
| `tests/testdata/webcrypto` | 4 | 20000.0 | 0.0% | 0.0% |
| `tests/specs/run/tls_starttls` | 7 | 15152.04 | 6.93% | 0.0% |
| `tests/specs/run/tls_connecttls` | 7 | 15136.08 | 3.1% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `ext/net/io.rs` -> **100.0%** Exposure
- `ext/webgpu/adapter.rs` -> **100.0%** Exposure
- `libs/core/ops_builtin_types.rs` -> **100.0%** Exposure
- `libs/napi_sys/src/functions.rs` -> **100.0%** Exposure
- `libs/ops/op2/test_cases/compiler_pass/async.rs` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `cli/util/draw_thread.rs` -> **100.0%** Exposure
- `cli/util/progress_bar/renderer.rs` -> **100.0%** Exposure
- `cli/util/text_encoding.rs` -> **100.0%** Exposure
- `cli/util/unix.rs` -> **100.0%** Exposure
- `libs/lockfile/tests/helpers/mod.rs` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `cli/tsc/dts/lib.webworker.d.ts` -> **394** Orphaned Functions | **199** Duplicates
- `cli/tsc/dts/lib.es5.d.ts` -> **123** Orphaned Functions | **225** Duplicates
- `cli/tsc/dts/node/http2.d.cts` -> **28** Orphaned Functions | **262** Duplicates
- `tests/integration/lsp_tests.rs` -> **243** Orphaned Functions | **0** Duplicates
- `cli/tsc/dts/node/stream.d.cts` -> **42** Orphaned Functions | **197** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `tests/unit_node/crypto/crypto_key_test.ts` -> **99.9946%** Exposure
- `cli/tsc/dts/lib.deno_net.d.ts` -> **98.2321%** Exposure
- `ext/tls/lib.rs` -> **97.7512%** Exposure
- `tests/unit_node/tls_test.ts` -> **73.1059%** Exposure
- `ext/node_crypto/x509.rs` -> **58.5958%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `8` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `19534` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `ext/node/polyfills/internal/dns/promises.ts` (TYPESCRIPT) -> Cumulative Risk: **765.3**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 392.56 | **LOC:** 593 | **CtrlFlow:** 11.2% | **Authorship Centralization:** 40.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.3109%)
- **Heaviest Functions:** `lookup` (Impact: 39.6), `createLookupPromise` (Impact: 21.8), `_resolve` (Impact: 13.2)

### 2. `ext/node/polyfills/internal/fs/streams.mjs` (JAVASCRIPT) -> Cumulative Risk: **751.99**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 461.42 | **LOC:** 580 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (94.2857%)
- **Heaviest Functions:** `WriteStream` (Impact: 33.1), `ReadStream` (Impact: 32.7), `_read` (Impact: 22.1)

### 3. `ext/node/polyfills/internal/crypto/sig.ts` (TYPESCRIPT) -> Cumulative Risk: **749.89**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 3.28 | **LOC:** 425 | **CtrlFlow:** 25.1% | **Authorship Centralization:** 75.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.3356%)
- **Heaviest Functions:** `verifyOneShot` (Impact: 87.3), `signOneShot` (Impact: 57.2), `verify` (Impact: 22.3)

### 4. `ext/node/polyfills/internal/child_process.ts` (TYPESCRIPT) -> Cumulative Risk: **741.27**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 1470.76 | **LOC:** 2032 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 62.5%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9866%), Documentation (90.1408%), Concurrency (84.3115%)
- **Heaviest Functions:** `spawnInternal` (Impact: 131.9), `escapeShellArg` (Impact: 117.8), `normalizeSpawnArguments` (Impact: 108.8)

### 5. `ext/fs/interface.rs` (RUST) -> Cumulative Risk: **738.03**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 297.76 | **LOC:** 434 | **CtrlFlow:** 7.8% | **Authorship Centralization:** 40.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9974%), Concurrency (99.233%)
- **Heaviest Functions:** `from` (Impact: 22.2), `write_file_sync` (Impact: 11.8), `write_file_async` (Impact: 11.8)

### 6. `ext/node/polyfills/http.ts` (TYPESCRIPT) -> Cumulative Risk: **732.76**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 2306.0 | **LOC:** 2621 | **CtrlFlow:** 28.8% | **Authorship Centralization:** 26.7%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9995%), Cognitive Load (95.0592%), Safety Score (91.1915%)
- **Heaviest Functions:** `constructor` (Impact: 181.3), `matchKnownFields` (Impact: 177.4), `_writeHeader` (Impact: 91.5)

### 7. `ext/node/polyfills/worker_threads.ts` (TYPESCRIPT) -> Cumulative Risk: **725.81**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 921.3 | **LOC:** 1268 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 64.3%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9788%), Cognitive Load (90.5814%), Safety Score (85.5256%)
- **Heaviest Functions:** `constructor` (Impact: 152.2), `__initWorkerThreads` (Impact: 60.6), `webMessagePortToNodeMessagePort` (Impact: 32.2)

### 8. `ext/node/ops/tls.rs` (RUST) -> Cumulative Risk: **722.99**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 376.14 | **LOC:** 639 | **CtrlFlow:** 11.4% | **Authorship Centralization:** 16.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9974%), State Flux (89.7043%)
- **Heaviest Functions:** `op_node_tls_start` (Impact: 22.1), `try_read` (Impact: 19.7), `read` (Impact: 18.7)

### 9. `ext/node/polyfills/internal/stream_base_commons.ts` (TYPESCRIPT) -> Cumulative Risk: **722.25**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 267.12 | **LOC:** 378 | **CtrlFlow:** 22.6% | **Authorship Centralization:** 25.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9972%), Concurrency (95.4129%)
- **Heaviest Functions:** `onStreamRead` (Impact: 45.2), `handleWriteReq` (Impact: 31.9), `setStreamTimeout` (Impact: 18.1)

### 10. `ext/node/ops/http.rs` (RUST) -> Cumulative Risk: **719.42**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 450.46 | **LOC:** 823 | **CtrlFlow:** 11.0% | **Authorship Centralization:** 28.6%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9994%), Documentation (94.4444%), Cognitive Load (81.8407%)
- **Heaviest Functions:** `op_node_http_request_with_conn` (Impact: 110.7), `read` (Impact: 23.4), `op_node_http_response_reclaim_conn` (Impact: 11.9)

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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.086
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.086
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.086
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.086
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.086
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.086
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.086
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.086
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.086
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.086
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.086
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.086
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.086
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.086
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.086
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.086
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.086
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.086
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.086
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.086
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.086
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.086
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.086
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.086
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.086
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `ext/node/polyfills/process.ts` -> Churn: **77.74%** | Cog Load: 53.6142% | Debt: 34.1463%
- `ext/node/polyfills/internal/child_process.ts` -> Churn: **71.83%** | Cog Load: 72.1221% | Debt: 19.7047%
- `ext/node/polyfills/worker_threads.ts` -> Churn: **69.18%** | Cog Load: 90.5814% | Debt: 27.0606%
- `cli/lsp/config.rs` -> Churn: **63.5%** | Cog Load: 7.0205% | Debt: 69.9616%
- `ext/node/polyfills/internal/fs/handle.ts` -> Churn: **61.55%** | Cog Load: 68.0792% | Debt: 100.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `tests/unit/kv_test.ts` -> **Kenta Moriuchi** (100.0% isolated ownership) | Magnitude: 2503.5
- `ext/node/polyfills/internal/streams/readable.js` -> **Kenta Moriuchi** (100.0% isolated ownership) | Magnitude: 1584.04
- `libs/eszip/v2.rs` -> **David Sherret** (100.0% isolated ownership) | Magnitude: 1288.04
- `cli/tsc/dts/node/fs.d.cts` -> **David Sherret** (100.0% isolated ownership) | Magnitude: 1264.8
- `ext/node_crypto/keys.rs` -> **Bartek Iwańczuk** (85.7% isolated ownership) | Magnitude: 1108.0

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `ext/io/12_io.js` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 100.0%)
- `ext/node/polyfills/internal/util/inspect.mjs` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 100.0%)
- `ext/web/06_streams.js` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 97.5955%)
- `ext/node/polyfills/internal/errors.ts` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 89.4001%)
- `ext/node/polyfills/internal/util/colors.ts` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 100.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `ext/node/polyfills/internal/util/colors.ts` -> **Severity: 438.3** (Blast Radius: 4.383 * Doc Risk: 100.0%)
- `ext/node/polyfills/internal/errors.ts` -> **Severity: 433.257** (Blast Radius: 4.399 * Doc Risk: 98.4899%)
- `ext/webidl/00_webidl.js` -> **Severity: 401.12** (Blast Radius: 4.579 * Doc Risk: 87.6%)
- `ext/io/12_io.js` -> **Severity: 353.334** (Blast Radius: 4.078 * Doc Risk: 86.644%)
- `tests/napi/common.js` -> **Severity: 279.6** (Blast Radius: 2.796 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
