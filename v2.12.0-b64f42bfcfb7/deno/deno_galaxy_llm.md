# ARCHITECTURAL_BRIEF: deno
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/denoland/deno.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |
| **Archetype Brains** | trained against engine v2.9.1 (44ffeb1e, 2026-09-19); last measured at engine 49cba5db on language-crucible@v1.7.0 |
| **Function archetypes** | **VALIDATED**, 98.4% agreement with trained state |
| **File archetypes** | **VALIDATED**, 98.7% agreement with trained state |
| **Composition (file)** | **DEGRADED**, 97.4% agreement with trained state -- engine changes since training relabelled 2.6% of crucible files (agreement 97.4%); composition_file inputs disagree with the function model's labels: never read ['Annotated & Test Methods', 'Stateful Encapsulated Methods'], never emitted ['Annotated Framework Methods', 'Tests & Verification'] -- those units drop out and those input columns are always 0.0 (retrain tracked in #4111) |
| **Composition (repo)** | **INVALID**, labels withheld -- not measurable on one corpus; inherits composition_file's measured state; composition_repo reads the composition_file brain labels by name, but none of its 20 inputs (e.g. 'Static: Literature & Documentation') is a label the composition_file brain emits (e.g. 'Annotated Framework Methods Files') -- every input column is 0.0 (retrain tracked in #4111) |

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 10292 analyzed artifact(s), 742847 LOC.
- **Load-bearing artifact:** `libs/core/lib.rs` -- 289 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `libs/core/lib.rs` -- pulls in 200 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `tests/specs/compile/npmrc_auto_install/.npmrc` at magnitude 5000.0 (structural weight, not risk).
- **How to read this brief:** section 11 ranks artifacts by structural magnitude with a blast-radius line each; section 7 has the full dependency graph. The surface vectors in section 6 describe what is present in a file, not the probability of a defect -- Appendix A has the equations and the validation record behind that distinction.

## 1.5 SYSTEM ROLE & PHILOSOPHY
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
> *(Section 2, the structural-surface lexicon and its equations, is now **Appendix A** at the end of this brief -- the findings come first.)*

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 11685 |
| Analyzed Artifacts (Scanned) | 10292 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1393 |
| Total LOC | 742847 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 88.1% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6298 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1218 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 4.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.7845 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 192 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 2762 | 204984 | 26.8% |
| PLAINTEXT | 2738 | 51 | 26.6% |
| JSON | 2542 | 50661 | 24.7% |
| JAVASCRIPT | 1176 | 81224 | 11.4% |
| RUST | 895 | 405006 | 8.7% |
| MARKDOWN | 110 | 0 | 1.1% |
| HTML | 17 | 287 | 0.2% |
| YAML | 12 | 42 | 0.1% |
| CSS | 11 | 69 | 0.1% |
| SQLITE | 9 | 44 | 0.1% |
| XML | 8 | 0 | 0.1% |
| C | 3 | 103 | 0.0% |
| PYTHON | 2 | 16 | 0.0% |
| CPP | 2 | 40 | 0.0% |
| M4 | 2 | 77 | 0.0% |
| NIX | 1 | 133 | 0.0% |
| CSHARP | 1 | 100 | 0.0% |
| POWERSHELL | 1 | 10 | 0.0% |

## 4.1 SOURCE ENCODINGS
> 6 file(s) had no BOM, were not UTF-8 and matched no declared code page: decoded by a legacy guess (`--source-encoding` declares the real one).
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 10226 |
| unknown | unknown | 49 |
| utf-8 | bom | 9 |
| cp1252 | cp1252-fallback | 6 |
| utf-16-be | bom | 1 |
| utf-16-le | bom | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 78%, Declarative / Non-Code 5%, Large Core Modules (3) 4%, State Mutators Files 3%, Generic / Templated Code Files 2%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 7441 | 72.3% |
| Unknown | 49 | 0.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2798 | 27.2% |
| Static: Minified & Vendor Opaque Mass | 4 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1393*

**Composition by Extension & Reason:**
- `.tgz`: 242x Excluded (Explicitly Denied Extension: '.tgz')
- `.ts`: 207x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 7x Excluded: Neighborhood Micro-Mass Limit Exceeded, 1x Excluded (Machine-Generated Source Code Signature: 74 LOC)
- `.js`: 137x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 6x Excluded: Neighborhood Micro-Mass Limit Exceeded, 1x Excluded (Saturation: Line 5 exceeds 500 chars)
- `.toml`: 79x Unsupported Format (.toml), 58x Excluded (Unsupported Extension: '.toml'), 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 123x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Excluded: Neighborhood Micro-Mass Limit Exceeded, 1x Excluded (Static Asset Blob without Intent: 1109 LOC)
- `no_extension`: 63x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 32x Unsupported Format (.undeterminable), 3x Excluded (Binary Format Detected)
- `.out`: 89x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 4 exceeds 500 chars), 1x Excluded (Binary Format Detected)
- `.jsonc`: 66x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.lock`: 42x Excluded (Unsupported Extension: '.lock')
- `.pem`: 23x Excluded (Unsupported Extension: '.pem')
- `.wasm`: 17x Excluded (Unsupported Extension: '.wasm'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.der`: 16x Excluded (Explicitly Denied Extension: '.der')
- `.rs`: 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Unrecognized Syntax (Dense Structure / Global Regex Timeout), 1x Excluded (Machine-Generated Source Code Signature: 120 LOC)
- `.yml`: 1x Excluded (Machine-Generated Source Code Signature: 50 LOC), 1x Excluded (Machine-Generated Source Code Signature: 5833 LOC), 1x Excluded (Machine-Generated Source Code Signature: 39 LOC)
- `.png`: 9x Excluded (Explicitly Denied Extension: '.png')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 5.4 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 96.3 | 13.6 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 4.7 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 5.0 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 8.9 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 12.4 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 6.7 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 88.8 | 0.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 5.2 | 0.6 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 4.6 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 26.3 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 4413 | 725 | 0 | `ext/node/ops/http2/session.rs` |
| cleanup | 2397 | 408 | 0 | `cli/tsc/dts/lib.dom.d.ts` |
| guards | 26551 | 1405 | 2 | `cli/tsc/dts/lib.dom.d.ts` |
| danger | 17647 | 1421 | 1 | `cli/tsc/dts/lib.dom.d.ts` |
| concurrency | 25640 | 1470 | 2 | `tests/unit/serve_test.ts` |
| connectivity | 26289 | 2270 | 2 | `cli/tsc/dts/typescript.d.ts` |
| io | 7083 | 821 | 0 | `tests/unit_node/http_test.ts` |
| crypto | 49 | 40 | 0 | `cli/tsc/dts/node/process.d.cts` |
| ipc | 1025 | 264 | 0 | `tests/unit_node/worker_threads_test.ts` |
| time | 1310 | 416 | 0 | `tests/unit/timers_test.ts` |
| serialization | 413 | 188 | 0 | `libs/npm/registry.rs` |
| regex | 292 | 114 | 0 | `ext/node/polyfills/deps/minimatch.js` |
| events | 4910 | 504 | 0 | `cli/tsc/dts/lib.dom.d.ts` |
| tests | 11090 | 620 | 0 | `tests/integration/lsp_tests.rs` |
| docs | 26924 | 887 | 0 | `cli/tsc/dts/lib.dom.d.ts` |
| debt | 8621 | 2085 | 1 | `cli/tsc/dts/lib.dom.d.ts` |
| mutation | 92403 | 2673 | 11 | `tests/integration/lsp_tests.rs` |
| dead_code | 6904 | 887 | 0 | `cli/tsc/dts/lib.dom.d.ts` |
| credential | 579 | 253 | 0 | `tools/deno.lock.json` |
| threat | 110 | 53 | 0 | `ext/node/polyfills/internal/buffer.d.ts` |
| ml_ai | 783 | 140 | 0 | `libs/core/core.d.ts` |
| ui | 122 | 46 | 0 | `cli/tsc/dts/lib.es5.d.ts` |

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

1. **lib.rs** (`libs/core/lib.rs`) — 289 inbound connections
2. **mod.rs** (`libs/ops/op2/mod.rs`) — 151 inbound connections
3. **error.rs** (`libs/core/error.rs`) — 133 inbound connections
4. **ops.rs** (`libs/core/ops.rs`) — 112 inbound connections
5. **test_util.ts** (`tests/unit/test_util.ts`) — 105 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **lib.rs** (`libs/core/lib.rs`) — 200 outbound dependencies
2. **language_server.rs** (`cli/lsp/language_server.rs`) — 121 outbound dependencies
3. **lib.rs** (`ext/telemetry/lib.rs`) — 120 outbound dependencies
4. **tsc.rs** (`cli/lsp/tsc.rs`) — 116 outbound dependencies
5. **process.rs** (`runtime/subprocess_windows/src/process.rs`) — 112 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `formatRaw` **(Many-Argument Workhorses)** (@ `ext/web/01_console.js`) -> Impact: **454.6** | LOC: 420
- `urlParse` **(Many-Argument Workhorses)** (@ `ext/node/polyfills/url.ts`) -> Impact: **264.2** | LOC: 324
- `objectComparisonStart` **(Many-Argument Workhorses)** (@ `ext/node/polyfills/internal/util/comparisons.ts`) -> Impact: **255.3** | LOC: 187
- `sync_resolution_with_fs` **(Many-Argument Workhorses)** (@ `libs/npm_installer/local.rs`) -> Impact: **254.7** | LOC: 764
- `iterateSubpatterns` **(Many-Argument Workhorses)** (@ `ext/node/polyfills/_fs/_fs_glob.ts`) -> Impact: **217.5** | LOC: 262
- `emitKeys` **(Many-Argument Workhorses)** (@ `ext/node/polyfills/internal/readline/utils.mjs`) -> Impact: **208.1** | LOC: 456
  * *Intent:* */
- `write_standalone_binary` **(Many-Argument Workhorses)** (@ `cli/standalone/binary.rs`) -> Impact: **200.1** | LOC: 521
  * *Intent:* /// This functions creates a standalone deno binary by appending a bundle /// and magic trailer to the currently executing binary.
- `importKeyRSA` **(Many-Argument Workhorses)** (@ `ext/crypto/00_crypto.js`) -> Impact: **197.4** | LOC: 420
- `resolve_peers_of_node` **(Many-Argument Workhorses)** (@ `libs/npm/resolution/graph.rs`) -> Impact: **194.1** | LOC: 452
  * *Intent:* /// Recursively resolve peer deps for a node and its subtree. /// /// Returns which peers bubble up (resolved from outside this subtree) /// and the f...
- `resolveObject` **(Compute Cores)** (@ `ext/node/polyfills/url.ts`) -> Impact: **194.0** | LOC: 288

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `tests/testdata/tls` | 7 | 25000.0 | 0.0% | 0.0% |
| `tests/unit_node/crypto/testdata/asymmetric` | 5 | 25000.0 | 0.0% | 0.0% |
| `ext/node/polyfills` | 63 | 23402.14 | 36.66% | 22.86% |
| `tests/unit` | 104 | 22121.0 | 18.84% | 0.0% |
| `tests/testdata/webcrypto` | 4 | 20000.0 | 0.0% | 0.0% |
| `cli/lsp` | 31 | 12737.86 | 18.39% | 4.39% |
| `ext/web` | 36 | 12125.63 | 31.31% | 27.01% |
| `tests/specs/npm/npmrc_certfile` | 7 | 10030.34 | 0.0% | 0.0% |
| `tests/wpt/runner/certs` | 3 | 10001.0 | 0.0% | 0.0% |
| `tests/unit_node/testdata` | 23 | 10000.21 | 2.46% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `ext/io/12_io.js` -> **100.0%** Exposure
- `ext/node/polyfills/_brotli.js` -> **100.0%** Exposure
- `ext/node/polyfills/_process/streams.mjs` -> **100.0%** Exposure
- `ext/node/polyfills/internal/blocklist.mjs` -> **100.0%** Exposure
- `ext/node/polyfills/internal/crypto/_randomFill.mjs` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `cli/js/40_bench.js` -> **100.0%** Exposure
- `cli/tsc/97_ts_host.js` -> **100.0%** Exposure
- `cli/tsc/98_lsp.js` -> **100.0%** Exposure
- `cli/tsc/99_main_compiler.js` -> **100.0%** Exposure
- `ext/crypto/00_crypto.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `cli/tsc/dts/lib.dom.d.ts` -> **831** Orphaned Functions | **838** Duplicates
- `cli/tsc/dts/lib.webworker.d.ts` -> **394** Orphaned Functions | **199** Duplicates
- `cli/tsc/dts/lib.es5.d.ts` -> **123** Orphaned Functions | **225** Duplicates
- `cli/tsc/dts/node/http2.d.cts` -> **28** Orphaned Functions | **262** Duplicates
- `cli/tsc/dts/node/stream.d.cts` -> **42** Orphaned Functions | **197** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `tests/unit/webcrypto_test.ts` -> **99.9999%** Exposure
- `tests/specs/audit/package_json_only/__test__.jsonc` -> **99.9954%** Exposure
- `tests/unit_node/crypto/crypto_key_test.ts` -> **99.9946%** Exposure
- `cli/tsc/dts/lib.deno_net.d.ts` -> **98.2321%** Exposure
- `ext/tls/lib.rs` -> **97.7512%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `10` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `19438` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `tests/specs/compile/npmrc_auto_install/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.075
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/specs/compile/npmrc_byonm/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.075
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/specs/npm/npmrc/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.075
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/specs/npm/npmrc_alongside_jsr_scope/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.075
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/specs/npm/npmrc_bad_registry_config/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.075
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/specs/npm/npmrc_bad_token/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.075
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/specs/npm/npmrc_basic_auth/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.075
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/specs/npm/npmrc_certfile/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.075
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/specs/npm/npmrc_certfile/client.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.075
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/specs/npm/npmrc_deno_json/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.075
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/specs/npm/npmrc_email_auth/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.075
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/specs/npm/npmrc_email_no_password/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.075
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/specs/npm/npmrc_homedir/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.075
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/specs/npm/npmrc_homedir_package_both/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.075
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/specs/npm/npmrc_homedir_package_both/subdir/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.075
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/specs/npm/npmrc_install_arg/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.075
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/specs/npm/npmrc_jsr_scope/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.075
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/specs/npm/npmrc_missing_certfile/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.075
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/specs/npm/npmrc_no_auth/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.075
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/specs/npm/npmrc_no_auth_install/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.075
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/specs/npm/npmrc_not_next_to_package_json/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.075
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/specs/npm/npmrc_password_no_username/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.075
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/specs/npm/npmrc_tarball_other_server/fail/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.075
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/specs/npm/npmrc_tarball_other_server/success/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.075
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/specs/npm/npmrc_username_no_password/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.075
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `cli/lsp/refactor.rs` (RUST) | Magnitude: 53.18 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 140, args: 27, structural_boundaries: 22, api: 20
- `cli/util/console.rs` (RUST) | Magnitude: 224.76 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 361, structural_boundaries: 118, core_var_decl: 78, design_snake_case: 70
- `libs/core/benches/ops/sync.rs` (RUST) | Magnitude: 179.32 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 367, args: 76, func_start: 70, structural_boundaries: 59
- `libs/dcore/src/inspector_server.rs` (RUST) | Magnitude: 172.7 | Delta: **0.042** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 369, structural_boundaries: 132, core_var_decl: 58, design_snake_case: 46
- `ext/net/lib.rs` (RUST) | Magnitude: 37.7 | Delta: **0.057** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 158, structural_boundaries: 26, api: 20, decorators: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `ext/web/01_broadcast_channel.js` (JAVASCRIPT) | Magnitude: 101.08 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 130, branch: 30, structural_boundaries: 26, core_var_decl: 22
- `tests/specs/bundle/html/multiple-html-bundle.asserts.ts` (TYPESCRIPT) | Magnitude: 18.56 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 5, branch: 4, args: 3
- `tests/registry/npm/@denotest/esm-import-cjs-default/1.0.0/index.mjs` (JAVASCRIPT) | Magnitude: 18.3 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: safety: 18, structural_boundaries: 8, debug_prints: 8, import: 4
- `tests/unit/tls_test.ts` (TYPESCRIPT) | Magnitude: 1031.78 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 1145, concurrency: 332, structural_boundaries: 278, core_var_decl: 177
- `tests/unit/files_test.ts` (TYPESCRIPT) | Magnitude: 452.3 | Delta: **0.051** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 783, concurrency: 214, structural_boundaries: 212, core_var_decl: 191

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `tests/specs/run/_018_async_catch/018_async_catch.ts` (TYPESCRIPT) | Magnitude: 7.88 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 9, safety: 7, structural_boundaries: 5, concurrency: 5
- `libs/core_testing/unit/resource_test.ts` (TYPESCRIPT) | Magnitude: 74.34 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 133, core_var_decl: 23, concurrency: 20, design_snake_case: 20
- `tests/unit/text_encoding_test.ts` (TYPESCRIPT) | Magnitude: 80.74 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 275, core_var_decl: 95, design_snake_case: 83, args: 33
- `ext/web/10_filereader.js` (JAVASCRIPT) | Magnitude: 224.58 | Delta: **0.045** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 359, structural_boundaries: 56, core_var_decl: 45, branch: 44
- `tests/unit/image_bitmap_test.ts` (TYPESCRIPT) | Magnitude: 147.74 | Delta: **0.106** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 272, structural_boundaries: 100, concurrency: 100, core_var_decl: 74

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `ext/node/polyfills/internal/buffer.mjs` (JAVASCRIPT) | Magnitude: 2477.44 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 2215, state_mutation: 491, branch: 489, structural_boundaries: 417
- `tests/unit/serve_test.ts` (TYPESCRIPT) | Magnitude: 2783.32 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 3590, structural_boundaries: 1213, concurrency: 980, core_var_decl: 698
- `cli/lsp/resolver.rs` (RUST) | Magnitude: 586.78 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 1293, structural_boundaries: 280, branch: 144, args: 137
- `cli/tsc/dts/node/dgram.d.cts` (TYPESCRIPT) | Magnitude: 185.44 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 138, structural_boundaries: 129, args: 73, func_start: 72
- `libs/resolver/npm/managed/local.rs` (RUST) | Magnitude: 89.72 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 171, structural_boundaries: 54, branch: 28, import: 22

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `tests/specs/test/doc_ts_declare_global/lib.d.ts` (TYPESCRIPT) | Magnitude: 0.19 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 3, api: 2, args: 1, func_start: 1
- `tests/unit/navigator_test.ts` (TYPESCRIPT) | Magnitude: 2.46 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 3, args: 2, func_start: 2, test: 2
- `tests/testdata/run/import_meta/main.ts` (TYPESCRIPT) | Magnitude: 0.02 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: structural_boundaries: 28, indent_spaces: 23, dependency_injection: 12, debug_prints: 11
- `cli/tools/lint/ast_buffer/mod.rs` (RUST) | Magnitude: 0.0 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 6, import: 3, indent_spaces: 3, args: 1
- `tests/specs/doc/deno_doc/deno_doc.ts` (TYPESCRIPT) | Magnitude: 2.14 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 1, args: 1, func_start: 1, api: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `cli/tsc/dts/node/worker_threads.d.cts` (TYPESCRIPT) | Magnitude: 212.34 | Delta: **0.138** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 198, structural_boundaries: 191, args: 109, func_start: 107

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `cli/tsc/dts/lib.esnext.error.d.ts` (TYPESCRIPT) | Magnitude: 0.08 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 2, args: 1, func_start: 1, class_start: 1
- `libs/resolver/cjs/analyzer/deno_ast.rs` (RUST) | Magnitude: 26.78 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 51, structural_boundaries: 16, args: 7, import: 7
- `ext/io/12_io.js` (JAVASCRIPT) | Magnitude: 94.06 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 192, structural_boundaries: 44, args: 30, func_start: 29
- `tests/specs/cli/otel_basic/propagators_api.ts` (TYPESCRIPT) | Magnitude: 7.02 | Delta: **0.039** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 4, args: 3, func_start: 3
- `libs/core/uv_compat.rs` (RUST) | Magnitude: 584.22 | Delta: **0.057** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 867, structural_boundaries: 300, pointers: 132, branch: 126

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `tests/testdata/assets/DenoWinRunner.cs` (CSHARP) | Magnitude: 0.05 | Delta: **0.134** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 87, core_var_decl: 21, structural_boundaries: 14, branch: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `tests/specs/check/ambient_modules/modules.d.ts` (TYPESCRIPT) | Magnitude: 0.83 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 9, indent_spaces: 4, branch: 2, api: 2
- `cli/lib/lib.rs` (RUST) | Magnitude: 23.68 | Delta: **0.082** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 9, api: 9
- `cli/tsc/dts/node/undici/index.d.ts` (TYPESCRIPT) | Magnitude: 1.42 | Delta: **0.095** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 70, import: 65, indent_spaces: 35, branch: 17
- `ext/node/ops/mod.rs` (RUST) | Magnitude: 45.6 | Delta: **0.108** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 30, api: 30, encapsulation: 1
- `cli/tools/mod.rs` (RUST) | Magnitude: 0.04 | Delta: **0.172** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 23, api: 23

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `tests/napi/instance_data_test.js` (JAVASCRIPT) | Magnitude: 20.54 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 5, state_mutation: 3, branch: 2
- `ext/node/polyfills/internal/process/report.ts` (TYPESCRIPT) | Magnitude: 7.32 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 64, structural_boundaries: 6, import: 3, core_var_decl: 3
- `libs/ops/op2/generator_state.rs` (RUST) | Magnitude: 50.1 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 44, doc: 37, api: 34, structural_boundaries: 7
- `runtime/js/06_util.js` (JAVASCRIPT) | Magnitude: 11.12 | Delta: **0.051** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 5, core_var_decl: 4, branch: 3
- `tests/napi/cleanup_hook_test.js` (JAVASCRIPT) | Magnitude: 20.56 | Delta: **0.051** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 5, state_mutation: 3, core_var_decl: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `tests/util/server/servers/ws.rs` (RUST) | Magnitude: 171.22 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 200, structural_boundaries: 155, concurrency: 63, branch: 40
- `ext/web/01_mimesniff.js` (JAVASCRIPT) | Magnitude: 176.98 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 284, core_var_decl: 50, structural_boundaries: 43, branch: 40
- `ext/node/polyfills/internal/streams/operators.js` (JAVASCRIPT) | Magnitude: 455.3 | Delta: **0.067** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 350, branch: 93, structural_boundaries: 74, core_var_decl: 48
- `tests/util/server/npm.rs` (RUST) | Magnitude: 332.64 | Delta: **0.071** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 446, structural_boundaries: 136, branch: 96, core_var_decl: 66
- `libs/resolver/lockfile.rs` (RUST) | Magnitude: 251.52 | Delta: **0.074** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 471, structural_boundaries: 107, args: 53, branch: 49

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `libs/cache_dir/file_fetcher/mod.rs` (RUST) | Magnitude: 532.26 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 972, structural_boundaries: 198, decorators: 130, branch: 105
- `libs/eszip/examples/viewer.rs` (RUST) | Magnitude: 36.8 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 75, structural_boundaries: 35, core_var_decl: 20, design_snake_case: 19
- `ext/process/ipc.rs` (RUST) | Magnitude: 474.06 | Delta: **0.031** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 550, structural_boundaries: 255, branch: 71, generics: 63
- `libs/npm/resolution/tracing/mod.rs` (RUST) | Magnitude: 26.48 | Delta: **0.034** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 54, api: 21, core_var_decl: 18, design_snake_case: 17
- `libs/core/runtime/jsruntime.rs` (RUST) | Magnitude: 1101.42 | Delta: **0.052** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 2150, structural_boundaries: 715, doc: 369, core_var_decl: 292

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `libs/npm/resolution/overrides.rs` (RUST) | Magnitude: 432.36 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 1386, structural_boundaries: 267, core_var_decl: 253, test: 241
- `libs/eszip/examples/builder.rs` (RUST) | Magnitude: 60.24 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 176, structural_boundaries: 55, core_var_decl: 28, design_snake_case: 26
- `tests/specs/npm/compare_globals/main.ts` (TYPESCRIPT) | Magnitude: 23.8 | Delta: **0.05** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: debug_prints: 16, structural_boundaries: 11, concurrency: 8, thread_sleeps: 8
- `cli/tsc/dts/node/tty.d.cts` (TYPESCRIPT) | Magnitude: 62.64 | Delta: **0.063** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: structural_boundaries: 41, indent_spaces: 38, args: 26, func_start: 26
- `ext/node/polyfills/internal/fs/streams.d.ts` (TYPESCRIPT) | Magnitude: 9.76 | Delta: **0.066** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: structural_boundaries: 212, indent_spaces: 146, args: 99, func_start: 99

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `ext/node/polyfills/url.ts` (TYPESCRIPT) | Magnitude: 1424.88 | Delta: **0.101** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 1024, branch: 402, state_mutation: 233, core_var_decl: 176

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `ext/node/polyfills/process.ts` -> Churn: **75.27%** | Cog Load: 53.8234% | Debt: 33.3155%
- `ext/node/polyfills/internal/child_process.ts` -> Churn: **71.83%** | Cog Load: 66.9561% | Debt: 19.3209%
- `ext/node/polyfills/worker_threads.ts` -> Churn: **68.46%** | Cog Load: 90.4852% | Debt: 26.3285%
- `tools/lint.js` -> Churn: **55.63%** | Cog Load: 77.4384% | Debt: 0.0%
- `ext/node/polyfills/01_require.js` -> Churn: **54.22%** | Cog Load: 66.2013% | Debt: 39.6354%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `tests/unit/kv_test.ts` -> **Kenta Moriuchi** (100.0% isolated ownership) | Magnitude: 2489.0
- `tests/unit/http_test.ts` -> **Kenta Moriuchi** (100.0% isolated ownership) | Magnitude: 2287.44
- `ext/node/polyfills/internal/streams/readable.js` -> **Kenta Moriuchi** (100.0% isolated ownership) | Magnitude: 1561.14
- `libs/eszip/v2.rs` -> **David Sherret** (100.0% isolated ownership) | Magnitude: 1308.64
- `cli/tsc/dts/node/fs.d.cts` -> **David Sherret** (100.0% isolated ownership) | Magnitude: 1264.8

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `tests/util/lib/test_runner.rs` -> **Severity: 0.056** (Bridge: 0.0006 * Flux: 95.2665%)
- `cli/tools/bench/reporters.rs` -> **Severity: 0.047** (Bridge: 0.0006 * Flux: 79.7076%)
- `tests/util/lib/lib.rs` -> **Severity: 0.046** (Bridge: 0.0006 * Flux: 79.0177%)
- `cli/lib.rs` -> **Severity: 0.015** (Bridge: 0.0004 * Flux: 41.7222%)
- `cli/tools/bench/mod.rs` -> **Severity: 0.01** (Bridge: 0.0002 * Flux: 41.9957%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `libs/core/lib.rs` -> **Severity: 1.233** (Embedded: 0.0245 * Error Risk: 50.303%)
- `libs/ops/op2/mod.rs` -> **Severity: 1.226** (Embedded: 0.0203 * Error Risk: 60.4262%)
- `libs/core/convert.rs` -> **Severity: 1.194** (Embedded: 0.0187 * Error Risk: 63.8542%)
- `libs/core/error.rs` -> **Severity: 1.174** (Embedded: 0.0213 * Error Risk: 55.2059%)
- `libs/core/async_cancel.rs` -> **Severity: 1.075** (Embedded: 0.0177 * Error Risk: 60.7734%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `libs/core/lib.rs` -> **Severity: 899.279** (Blast Radius: 11.855 * Doc Risk: 75.8565%)
- `libs/core/modules/mod.rs` -> **Severity: 532.803** (Blast Radius: 7.033 * Doc Risk: 75.7576%)
- `tests/util/lib/lib.rs` -> **Severity: 451.918** (Blast Radius: 5.026 * Doc Risk: 89.916%)
- `libs/core/error.rs` -> **Severity: 313.583** (Blast Radius: 5.42 * Doc Risk: 57.8567%)
- `libs/core/convert.rs` -> **Severity: 294.368** (Blast Radius: 4.182 * Doc Risk: 70.3894%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 3619 literal sites + 84 sites through wrappers = 3703
- **`panics_and_aborts`:** 3267 literal sites + 147 sites through wrappers = 3414

- `createOnErrorCb` (function, debug_prints, primitive): 59 call sites in 1 files -- `tests/unit/serve_test.ts`
- `createOnErrorCb` (function, panics_and_aborts, primitive): 59 call sites in 1 files -- `tests/unit/serve_test.ts`
- `notImplemented` (function, panics_and_aborts, primitive): 59 call sites in 20 files -- `ext/node/polyfills/_utils.ts`
- `unreachable` (function, panics_and_aborts, primitive): 4 call sites in 1 files -- `tests/unit/tls_test.ts`
- `d` (function, debug_prints, primitive): 3 call sites in 2 files -- `tests/specs/run/eszip2/src/d.js`
- `packAndPostMessageHandlingError` (function, panics_and_aborts, primitive): 3 call sites in 1 files -- `ext/web/06_streams.js`
- `unpack_object` (function, panics_and_aborts, primitive): 3 call sites in 1 files -- `libs/config/deno_json/mod.rs`
- `cb` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `ext/node/polyfills/_readline.mjs`
- `op_test_print_debug` (function, debug_prints, primitive): 2 call sites in 1 files -- `libs/core/runtime/ops.rs`
- `realPrintName` (function, debug_prints, primitive): 2 call sites in 1 files -- `tests/specs/clean/entrypoint/print-dir.ts`
- `ring_bell` (function, debug_prints, primitive): 2 call sites in 1 files -- `cli/tools/publish/mod.rs`
- `transformStreamDefaultControllerPerformTransform` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `ext/web/06_streams.js`
*(+31 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 135343 call pairs -- scoped 15.0%, unique 0.0%, ambiguous 31.2%, external 53.8%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| rust | 102524 | 14.6% | 0.0% | 25.4% | 60.0% |
| typescript | 21988 | 11.1% | 0.0% | 58.0% | 30.9% |
| javascript | 10804 | 26.3% | 0.0% | 32.5% | 41.1% |
| csharp | 13 | 7.7% | 0.0% | 0.0% | 92.3% |
| c | 6 | 0.0% | 0.0% | 0.0% | 100.0% |
| cpp | 6 | 0.0% | 0.0% | 0.0% | 100.0% |
| html | 2 | 0.0% | 0.0% | 0.0% | 100.0% |

## APPENDIX A. STRUCTURAL SURFACE LEXICON (EQUATIONS & CONTEXT)
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

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with high Structural Magnitude combined with a wide Blast Radius, severe Z-Scores (Architectural Drift), or extreme spikes in individual surface vectors (like Mutation Surface or Complexity Load). Do NOT sum the surface vectors together or treat any total of them as a score -- they are independently scaled meters in different units (#3112). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
