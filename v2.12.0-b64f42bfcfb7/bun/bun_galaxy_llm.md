# ARCHITECTURAL_BRIEF: bun
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/oven-sh/bun` |
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
- **Scope:** 9858 analyzed artifact(s), 1518205 LOC.
- **Load-bearing artifact:** `test/napi/node-napi-tests/test/js-native-api/common.h` -- 2440 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/bun.js/bindings/ZigGlobalObject.cpp` -- pulls in 210 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `bench/react-hello-world/react-hello-world.node.js` at magnitude 42886.92 (structural weight, not risk).
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
| Total Artifacts | 12655 |
| Analyzed Artifacts (Scanned) | 9858 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 2797 |
| Total LOC | 1518205 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 77.9% |
| Dominant Lang | ZIG |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6692 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2342 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 13.8% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 6.1468 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 314 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 4044 | 276365 | 41.0% |
| TYPESCRIPT | 2181 | 419329 | 22.1% |
| CPP | 1287 | 256049 | 13.1% |
| ZIG | 1128 | 468641 | 11.4% |
| PLAINTEXT | 543 | 63 | 5.5% |
| HTML | 129 | 5845 | 1.3% |
| JSON | 123 | 3102 | 1.2% |
| MARKDOWN | 109 | 0 | 1.1% |
| C | 106 | 23343 | 1.1% |
| PYTHON | 69 | 3351 | 0.7% |
| YAML | 44 | 2544 | 0.4% |
| CSS | 28 | 53915 | 0.3% |
| SHELL | 23 | 1749 | 0.2% |
| XML | 15 | 5 | 0.2% |
| DOCKERFILE | 10 | 565 | 0.1% |
| RUST | 7 | 560 | 0.1% |
| NIX | 2 | 219 | 0.0% |
| POWERSHELL | 2 | 350 | 0.0% |
| MAKEFILE | 2 | 1327 | 0.0% |
| SQLITE | 2 | 162 | 0.0% |
| PROTO | 1 | 11 | 0.0% |
| PERL | 1 | 388 | 0.0% |
| RUBY | 1 | 322 | 0.0% |
| CSV | 1 | 0 | 0.0% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 9797 |
| unknown | unknown | 60 |
| utf-8 | bom | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 32%, Data / Markup / Trivial 22%, Large Core Modules (2) 9%, Large Core Modules (3) 8%, Callbacks & Closures Files 7%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 9197 | 93.3% |
| Unknown | 60 | 0.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 589 | 6.0% |
| Static: Minified & Vendor Opaque Mass | 12 | 0.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 2797*

**Composition by Extension & Reason:**
- `.js`: 382x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 16x Excluded: Neighborhood Micro-Mass Limit Exceeded, 3x Excluded (Saturation: Line 1 exceeds 500 chars)
- `.tgz`: 349x Excluded (Explicitly Denied Extension: '.tgz')
- `.mdx`: 328x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ts`: 225x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded: Neighborhood Micro-Mass Limit Exceeded, 1x Excluded (Machine-Generated Source Code Signature: 2724 LOC)
- `.pem`: 150x Excluded (Unsupported Extension: '.pem'), 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 148x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded: Neighborhood Micro-Mass Limit Exceeded, 1x Excluded (Massive Static Asset Blob: 3974 LOC)
- `no_extension`: 114x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 13x Unsupported Format (.undeterminable), 4x Excluded (Binary Format Detected)
- `.map`: 100x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mjs`: 39x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 21x Excluded: Neighborhood Micro-Mass Limit Exceeded, 1x Excluded (Saturation: Line 28 exceeds 500 chars)
- `.lock`: 36x Excluded (Unsupported Extension: '.lock'), 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 7x Unsupported Format (.lock)
- `.snap`: 58x Excluded (Unsupported Extension: '.snap'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.zig`: 52x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 5398 LOC), 1x Excluded (Machine-Generated Source Code Signature: 2204 LOC)
- `.png`: 52x Excluded (Explicitly Denied Extension: '.png')
- `.h`: 49x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 68 exceeds 500 chars)
- `.idl`: 49x Unsupported Format (.idl)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 13.7 | 5.4 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 28.6 | 42.7 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 10.2 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 6.1 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 11.2 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 21.8 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 13.4 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 1.8 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 7.8 | 0.8 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 3.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 45.9 | 14.8 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 19574 | 2385 | 4 | `src/bun.js/bindings/FFI.zig` |
| cleanup | 9267 | 1910 | 2 | `test/js/sql/sqlite-sql.test.ts` |
| guards | 92937 | 4393 | 15 | `bench/react-hello-world/react-hello-world.node.js` |
| danger | 30966 | 3045 | 6 | `bench/react-hello-world/react-hello-world.node.js` |
| concurrency | 51847 | 2810 | 8 | `test/js/sql/sql.test.ts` |
| connectivity | 56748 | 3294 | 7 | `test/js/bun/css/files/bulma.css` |
| io | 24602 | 2899 | 4 | `test/js/sql/sql.test.ts` |
| crypto | 348 | 309 | 0 | `packages/bun-types/bun.d.ts` |
| ipc | 2732 | 747 | 0 | `src/crash_handler.zig` |
| time | 3395 | 776 | 0 | `test/js/bun/test/fake-timers/sinonjs/fake-timers.test.ts` |
| serialization | 3287 | 550 | 0 | `test/cli/install/bun-install.test.ts` |
| regex | 4200 | 603 | 0 | `test/js/bun/glob/match.test.ts` |
| events | 16572 | 2172 | 4 | `bench/react-hello-world/react-hello-world.node.js` |
| tests | 75189 | 3900 | 11 | `test/js/sql/sql.test.ts` |
| docs | 23339 | 1081 | 1 | `src/windows.zig` |
| debt | 21380 | 3090 | 4 | `test/bundler/esbuild/default.test.ts` |
| mutation | 286464 | 7708 | 60 | `bench/react-hello-world/react-hello-world.node.js` |
| dead_code | 12707 | 1851 | 2 | `src/bun.js/bindings/webcore/SerializedScriptValue.cpp` |
| credential | 294 | 64 | 0 | `test/js/node/test/parallel/test-crypto-dh-stateless.js` |
| threat | 549 | 115 | 0 | `test/js/bun/test/expect.test.js` |
| ml_ai | 2730 | 478 | 0 | `src/css/values/color.zig` |
| ui | 2825 | 207 | 0 | `test/js/bun/css/files/bulma.css` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `test/js/sql/sql.test.ts` (Hits: 2008)
- `test/js/sql/sqlite-sql.test.ts` (Hits: 1169)
- `test/js/node/fs/fs.test.ts` (Hits: 611)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **common.h** (`test/napi/node-napi-tests/test/js-native-api/common.h`) — 2440 inbound connections
2. **h.cjs** (`test/js/node/module/children-fixture/h.cjs`) — 848 inbound connections
3. **root.h** (`src/bun.js/bindings/root.h`) — 365 inbound connections
4. **config.h** (`src/bun.js/bindings/webcore/config.h`) — 260 inbound connections
5. **tmpdir.js** (`test/js/node/test/common/tmpdir.js`) — 225 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **ZigGlobalObject.cpp** (`src/bun.js/bindings/ZigGlobalObject.cpp`) — 210 outbound dependencies
2. **default.test.ts** (`test/bundler/esbuild/default.test.ts`) — 207 outbound dependencies
3. **bindings.cpp** (`src/bun.js/bindings/bindings.cpp`) — 128 outbound dependencies
4. **bun.zig** (`src/bun.zig`) — 117 outbound dependencies
5. **bundler_barrel.test.ts** (`test/bundler/bundler_barrel.test.ts`) — 93 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `llhttp__internal__run` **(Many-Argument Workhorses)** (@ `src/bun.js/bindings/node/http/llhttp/llhttp.c`) -> Impact: **4250.4** | LOC: 8848
- `NewPrinter` **(Many-Argument Workhorses)** (@ `src/js_printer.zig`) -> Impact: **2572.1** | LOC: 4982
- `NewParser_` **(Many-Argument Workhorses)** (@ `src/ast/P.zig`) -> Impact: **1977.7** | LOC: 6833
- `NewLexer_` **(Many-Argument Workhorses)** (@ `src/js_lexer.zig`) -> Impact: **1509.3** | LOC: 2946
- `parse` **(Many-Argument Workhorses)** (@ `src/css/properties/properties_generated.zig`) -> Impact: **1081.5** | LOC: 1750
  * *Intent:* /// Parses a CSS property by name.
- `expectBundled` **(Many-Argument Workhorses)** (@ `test/bundler/expectBundled.ts`) -> Impact: **1068.9** | LOC: 1387
- `Parser` **(Many-Argument Workhorses)** (@ `src/interchange/yaml.zig`) -> Impact: **939.3** | LOC: 4983
- `printAs` **(Many-Argument Workhorses)** (@ `src/bun.js/ConsoleObject.zig`) -> Impact: **889.9** | LOC: 1449
- `NewRequestContext` **(Many-Argument Workhorses)** (@ `src/bun.js/api/server/RequestContext.zig`) -> Impact: **836.1** | LOC: 2563
- `NewServer` **(Many-Argument Workhorses)** (@ `src/bun.js/api/server.zig`) -> Impact: **767.3** | LOC: 2391

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `test/js/node/crypto/fixtures` | 15 | 70000.02 | 0.0% | 0.0% |
| `src/bun.js/bindings` | 458 | 55711.86 | 13.6% | 52.19% |
| `test/js/node/tls/fixtures` | 11 | 50000.01 | 0.0% | 0.0% |
| `src` | 128 | 47883.08 | 18.42% | 9.63% |
| `test/js/third_party/jsonwebtoken` | 9 | 45000.0 | 0.0% | 0.0% |
| `test/js/node/test/parallel` | 2202 | 44401.59 | 12.83% | 0.0% |
| `bench/react-hello-world` | 7 | 42941.62 | 26.0% | 35.04% |
| `test/js/sql` | 16 | 30124.01 | 27.07% | 0.0% |
| `src/js/node` | 62 | 27864.08 | 54.35% | 19.27% |
| `test/cli/install` | 63 | 27716.74 | 26.86% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `.github/ISSUE_TEMPLATE/2-bug-report.yml` -> **100.0%** Exposure
- `.github/ISSUE_TEMPLATE/3-typescript-bug-report.yml` -> **100.0%** Exposure
- `packages/bun-types/bun.d.ts` -> **100.0%** Exposure
- `packages/bun-types/html-rewriter.d.ts` -> **100.0%** Exposure
- `packages/bun-types/jsc.d.ts` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `src/cli/install.sh` -> **100.0%** Exposure
- `bench/snippets/array-shift.mjs` -> **100.0%** Exposure
- `bench/snippets/dns.node.mjs` -> **100.0%** Exposure
- `bench/snippets/microtask-throughput.mjs` -> **100.0%** Exposure
- `misctools/headers-cleaner.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/bun.js/bindings/ncrypto.cpp` -> **360** Orphaned Functions | **0** Duplicates
- `test/bundler/transpiler/esbuild-decorator-tests.ts` -> **0** Orphaned Functions | **322** Duplicates
- `src/bun.js/bindings/bindings.cpp` -> **315** Orphaned Functions | **0** Duplicates
- `src/bun.js/bindings/uv-posix-stubs.c` -> **305** Orphaned Functions | **0** Duplicates
- `packages/bun-types/bun.d.ts` -> **126** Orphaned Functions | **50** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `test/js/node/test/parallel/test-crypto-dh-stateless.js` -> **100.0%** Exposure
- `test/js/node/test/parallel/test-crypto-x509.js` -> **100.0%** Exposure
- `test/js/node/test/parallel/test-tls-cert-ext-encoding.js` -> **100.0%** Exposure
- `test/js/node/test/parallel/test-tls-use-after-free-regression.js` -> **100.0%** Exposure
- `test/js/node/tls/test-node-extra-ca-certs.test.ts` -> **100.0%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `39` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `23282` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `bench/react-hello-world/react-hello-world.node.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 11.773)
- **Top Global Matches:** file_cluster_4: 11.773, file_cluster_12: 13.338, file_cluster_7: 14.899
- **Magnitude:** 42886.92 | **LOC:** 46169 | **CtrlFlow:** 28.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.03; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Complexity Load (formerly Cognitive Load) (84.8%), Guard Balance (formerly Safety Score) (54.5%), Concurrency Surface (formerly Concurrency) (27.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `s9` **(Many-Argument Workhorses)** (Impact: 502.8)
  * `H1` **(Many-Argument Workhorses)** (Impact: 469.6)
  * `kY` **(Defensive Guards)** (Impact: 366.4)
  * `oI` **(Defensive Guards)** (Impact: 297.5)
  * `zL` **(Defensive Guards)** (Impact: 285.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 118 instances
* *Amplified Race Conditions:* 86 instances
* *Amplified Cascading Flux:* 3216 instances
* *High Risk Execution (weighted view):* 34
* *Concurrency (weighted view):* 602
* *State Mutation (weighted view):* 11238
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12914`, `structural_boundaries: 9216`, `args: 3294`, `func_start: 3028`
* *Risk/State:* `safety_bypasses: 2141`, `high_risk_execution: 152`, `state_mutation: 4806`, `planned_debt: 5`, `fragile_debt: 162`, `duplicate_logic: 80`, `unreferenced_by_name: 3`
* *Architecture:* `io: 16`, `api: 5`, `concurrency: 172`, `import: 17`
* *Defense:* `safety: 6866`, `doc: 2`, `test: 5`, `immutability_locks: 15`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` MyComponent, async_hooks, http, client, stream, util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/js/sql/sqlite-sql.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.162)
- **Top Global Matches:** file_cluster_10: 6.162, file_cluster_2: 8.205, file_cluster_13: 8.515
- **Magnitude:** 23599.15 | **LOC:** 5382 | **CtrlFlow:** 2.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.03; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (48.9%), Guard Balance (formerly Safety Score) (39.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (6.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 7 instances
* *Amplified Race Conditions:* 207 instances
* *Amplified Cascading Flux:* 57 instances
* *Concurrency (weighted view):* 2257
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 201
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 1367`, `args: 431`, `func_start: 219`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 87`
* *Architecture:* `io: 1169`, `concurrency: 1222`, `import: 7`
* *Defense:* `safety: 101`, `test: 967`, `sync_locks: 2`, `immutability_locks: 17`, `cleanup: 121`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` bun, bun:test, harness, node:fs, promises, node:path, path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/bun.js/bindings/node/http/llhttp/llhttp.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 8.245)
- **Top Global Matches:** file_cluster_15: 8.245, file_cluster_16: 9.273, file_cluster_4: 9.965
- **Magnitude:** 9337.6 | **LOC:** 10155 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **8**; blast radius 0.035; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.7%)
- **Documentation Coverage:** 92.619% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `llhttp__internal__run` **(Many-Argument Workhorses)** (Impact: 4250.4)
  * `llparse__match_sequence_to_lower` **(Many-Argument Workhorses)** (Impact: 18.7)
  * `llhttp__internal__c_mul_add_content_length` **(Many-Argument Workhorses)** (Impact: 14.7)
  * `llhttp__internal__c_mul_add_content_length_1` **(Many-Argument Workhorses)** (Impact: 14.7)
  * `llhttp__internal__c_mul_add_status_code` **(Many-Argument Workhorses)** (Impact: 14.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1355 instances
* *State Mutation (weighted view):* 4559
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1937`, `structural_boundaries: 792`, `args: 91`, `func_start: 63`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 1849`, `unreferenced_by_name: 2`
* *Architecture:* `api: 94`, `import: 8`
* *Defense:* `safety: 2`, `immutability_locks: 533`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.035
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000135
  * `Imports (Out-Degree: 4):` arm_neon.h, llhttp.h, nmmintrin.h, stdint.h, stdlib.h, string.h, wasm_simd128.h, x86intrin.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/js_printer.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.148)
- **Top Global Matches:** file_cluster_4: 8.148, file_cluster_12: 12.216, file_cluster_6: 12.482
- **Magnitude:** 6132.46 | **LOC:** 6399 | **CtrlFlow:** 19.4% | **Authorship Centralization:** 38.5%
- **Blast Radius:** changing it is visible to **17** in-repo importer(s); it depends on **9**; blast radius 0.222; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (78.7%), Mutation Surface (formerly State Flux) (69.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (52.8%)
- **Documentation Coverage:** 49.1354% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `NewPrinter` **(Many-Argument Workhorses)** (Impact: 2572.1)
  * `printExpr` **(Many-Argument Workhorses)** (Impact: 575.9)
  * `printStmt` **(Many-Argument Workhorses)** (Impact: 382.8)
  * `printRequireOrImportExpr` **(Many-Argument Workhorses)** (Impact: 148.4)
  * `printProperty` **(Many-Argument Workhorses)** (Impact: 132.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 131 instances
* *Concurrency (weighted view):* 9
* *State Mutation (weighted view):* 430
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1033`, `structural_boundaries: 357`, `args: 171`, `func_start: 169`, `class_start: 23`
* *Risk/State:* `safety_bypasses: 82`, `state_mutation: 168`, `dead_code: 26`, `planned_debt: 14`, `fragile_debt: 2`
* *Architecture:* `io: 3`, `api: 183`, `concurrency: 4`, `import: 9`
* *Defense:* `safety: 375`, `doc: 12`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.222
  * `Choke Point (Betweenness):` 6.2e-05 | `Ripple Effect (Closeness):` 0.024564
  * `Imports (Out-Degree: 12):` analyze_transpiled_module.zig, fs.zig, import_record.zig, options.zig, renamer.zig, runtime.zig, sourcemap.zig, bun...
  * `Imported By (In-Degree: 17):` (Excluded from Brief to save tokens)

### `src/ast/P.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.52)
- **Top Global Matches:** file_cluster_4: 9.52, file_cluster_12: 12.446, file_cluster_6: 13.08
- **Magnitude:** 5340.32 | **LOC:** 6967 | **CtrlFlow:** 16.0% | **Authorship Centralization:** 38.5%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **11**; blast radius 0.052; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.1%), Connectivity (formerly Api Exposure) (69.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (64.5%), Guard Balance (formerly Safety Score) (50.4%)
- **Documentation Coverage:** 94.4828% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `NewParser_` **(Many-Argument Workhorses)** (Impact: 1977.7)
  * `substituteSingleUseSymbolInExpr` **(Many-Argument Workhorses)** (Impact: 160.3)
  * `toAST` **(Many-Argument Workhorses)** (Impact: 119.7)
  * `lowerClass` **(Defensive Guards)** (Impact: 115.1)
  * `processImportStatement` **(Many-Argument Workhorses)** (Impact: 100.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 210 instances
* *Memory Alloc (weighted view):* 56
* *State Mutation (weighted view):* 807
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 817`, `structural_boundaries: 709`, `args: 144`, `func_start: 144`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 177`, `high_risk_execution: 1`, `state_mutation: 387`, `dead_code: 45`, `planned_debt: 20`, `fragile_debt: 5`
* *Architecture:* `api: 214`, `concurrency: 3`, `import: 12`
* *Defense:* `safety: 642`, `doc: 105`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.052
  * `Choke Point (Betweenness):` 0.000151 | `Ripple Effect (Closeness):` 0.018545
  * `Imports (Out-Degree: 18):` defines.zig, lowerDecorators.zig, maybe.zig, parse.zig, repl_transforms.zig, skipTypescript.zig, symbols.zig, visit.zig...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `bench/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bench/async/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bench/ffi/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bench/grpc-server/key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bench/gzip/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bench/log/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bench/modules/node_os/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bench/sqlite/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/bun-release/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/bun-uws/misc/key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/js/bun/http/fixtures/cert.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/js/deno/fixtures/id_rsaEncryption.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/js/deno/fixtures/id_rsassaPss.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/js/deno/fixtures/id_rsassaPss_default.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/js/deno/fixtures/id_rsassaPss_saltLen_30.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/js/node/crypto/fixtures/ec_p256_private.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/js/node/crypto/fixtures/ec_p384_private.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/js/node/crypto/fixtures/ec_p521_private.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/js/node/crypto/fixtures/ec_secp256k1_private.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/js/node/crypto/fixtures/ed25519_private.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `test/regression/issue/21830.fixture.ts` (TYPESCRIPT) | Magnitude: 126.26 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 39, structural_boundaries: 30, concurrency: 27, args: 16
- `src/bake/DevServer/memory_cost.zig` (ZIG) | Magnitude: 116.14 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 166, state_mutation: 37, core_var_decl: 23, design_snake_case: 16
- `src/ast/Stmt.zig` (ZIG) | Magnitude: 134.26 | Delta: **0.037** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 317, pointers: 37, structural_boundaries: 33, core_var_decl: 32
- `src/bun.js/bindings/webcore/JSEventTargetCustom.cpp` (CPP) | Magnitude: 27.14 | Delta: **0.039** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 17, pointers: 9, branch: 8
- `src/bun.js/bindings/JSNodePerformanceHooksHistogramConstructor.h` (CPP) | Magnitude: 13.42 | Delta: **0.042** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 12, args: 7, func_start: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `src/bun.js/bindings/napi_handle_scope.h` (CPP) | Magnitude: 23.18 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 46, structural_boundaries: 28, args: 17, api: 5
- `test/js/node/test/parallel/test-zlib-write-after-close.js` (JAVASCRIPT) | Magnitude: 15.24 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 7, core_var_decl: 3, design_snake_case: 3, import: 2
- `test/js/node/test/parallel/test-crypto-dh.js` (JAVASCRIPT) | Magnitude: 22.76 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 74, core_var_decl: 22, design_snake_case: 19, test: 17
- `test/js/node/test/parallel/test-fs-promises-file-handle-read.js` (JAVASCRIPT) | Magnitude: 137.16 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 98, concurrency: 46, core_var_decl: 42, structural_boundaries: 41
- `test/js/bun/spawn/spawn-stdin-destroy.test.ts` (TYPESCRIPT) | Magnitude: 44.02 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 27, structural_boundaries: 16, concurrency: 13, args: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `test/js/node/test/parallel/test-fs-promises-file-handle-write.js` (JAVASCRIPT) | Magnitude: 26.88 | Delta: **0.047** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 40, core_var_decl: 21, concurrency: 18, structural_boundaries: 15
- `src/bun.js/bindings/Cookie.h` (CPP) | Magnitude: 61.6 | Delta: **0.051** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 94, immutability_locks: 40, structural_boundaries: 34, core_var_decl: 27
- `src/bun.js/bindings/node/crypto/JSKeyObject.h` (CPP) | Magnitude: 0.32 | Delta: **0.071** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 37, structural_boundaries: 22, args: 15, import: 9
- `src/bun.js/bindings/ncrypto.h` (CPP) | Magnitude: 255.98 | Delta: **0.083** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 979, immutability_locks: 565, structural_boundaries: 428, args: 378
- `src/bun.js/bindings/node/crypto/JSDiffieHellman.h` (CPP) | Magnitude: 0.32 | Delta: **0.09** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 37, structural_boundaries: 22, args: 14, func_start: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `test/js/node/test/fixtures/eval/stdin_messages.js` (JAVASCRIPT) | Magnitude: 0.02 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 18, core_var_decl: 6, design_snake_case: 6, state_mutation: 4
- `test/js/web/broadcastchannel/broadcast-channel-worker-gc.test.ts` (TYPESCRIPT) | Magnitude: 227.81 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 101, concurrency: 28, structural_boundaries: 24, core_var_decl: 23
- `test/js/node/http/client-timeout-error.test.ts` (TYPESCRIPT) | Magnitude: 114.37 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 55, structural_boundaries: 17, concurrency: 12, core_var_decl: 12
- `src/bun.js/webcore/blob/copy_file.zig` (ZIG) | Magnitude: 587.44 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 992, branch: 155, core_var_decl: 128, structural_boundaries: 116
- `test/bundler/transpiler/bun-pragma.test.ts` (TYPESCRIPT) | Magnitude: 15.16 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 17, core_var_decl: 13, io: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `test/integration/vite-build/the-test-app/src/lib/components/ui/popover/popover-content.svelte` (HTML) | Magnitude: 28.54 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 15, structural_boundaries: 10, api: 4, decorators: 2
- `src/bun.js/bindings/webcore/JSPerformanceMarkOptions.cpp` (CPP) | Magnitude: 36.88 | Delta: **0.045** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 33, branch: 10, structural_boundaries: 9, core_var_decl: 8
- `test/js/node/test/fixtures/es-module-loaders/hooks-initialize.mjs` (JAVASCRIPT) | Magnitude: 0.01 | Delta: **0.05** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 3, args: 1, func_start: 1, io: 1
- `test/regression/issue/15276.test.ts` (TYPESCRIPT) | Magnitude: 15.26 | Delta: **0.061** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 9, test: 4, decorators: 4, structural_boundaries: 3
- `test/integration/vite-build/the-test-app/src/lib/components/ui/command/command.svelte` (HTML) | Magnitude: 29.68 | Delta: **0.062** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 13, structural_boundaries: 7, api: 3, decorators: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `src/sql/postgres/protocol/DataRow.zig` (ZIG) | Magnitude: 22.3 | Delta: **0.077** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 19, core_var_decl: 11, safety: 8, design_snake_case: 8
- `test/js/bun/test/todo-test-fixture.js` (JAVASCRIPT) | Magnitude: 27.4 | Delta: **0.082** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: planned_debt: 14, structural_boundaries: 13, concurrency: 12, indent_spaces: 12
- `test/js/bun/resolve/resolve-bad-parent.test.mjs` (JAVASCRIPT) | Magnitude: 15.2 | Delta: **0.131** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 7, indent_spaces: 6, args: 4, closures: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `src/ast/TS.zig` (ZIG) | Magnitude: 11.12 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: doc: 97, indent_spaces: 18, core_var_decl: 13, globals: 11
- `src/bun.js/bindings/node/crypto/JSHmac.h` (CPP) | Magnitude: 0.25 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 68, structural_boundaries: 27, args: 23, import: 11
- `src/codegen/bindgenv2/internal/base.ts` (TYPESCRIPT) | Magnitude: 78.56 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 80, structural_boundaries: 46, args: 25, func_start: 22
- `src/bun.js/api/server/SSLConfig.zig` (ZIG) | Magnitude: 358.12 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 385, structural_boundaries: 85, core_var_decl: 80, branch: 79
- `src/bun.js/bindings/webcore/BroadcastChannel.h` (CPP) | Magnitude: 19.82 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 37, structural_boundaries: 25, immutability_locks: 16, args: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `test/napi/node-napi-tests/test/js-native-api/test_number/test_number.c` (C) | Magnitude: 16.26 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 62, pointers: 21, structural_boundaries: 5, args: 5
- `test/js/bun/ffi/ffi.test.fixture.receiver.c` (C) | Magnitude: 137.92 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 126, structural_boundaries: 112, args: 64, encapsulation: 47
- `test/napi/node-napi-tests/test/js-native-api/test_promise/test_promise.c` (C) | Magnitude: 19.86 | Delta: **0.051** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 33, pointers: 11, structural_boundaries: 7, args: 4
- `test/js/bun/ffi/ffi.test.fixture.callback.c` (C) | Magnitude: 136.62 | Delta: **0.11** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 122, structural_boundaries: 115, args: 64, encapsulation: 47

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/bun.js/bindings/node/NodeTimers.h` (CPP) | Magnitude: 15.2 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 1, import: 1, macros: 1
- `src/bun.js/bindings/Bindgen.h` (CPP) | Magnitude: 15.22 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: import: 10, fragile_debt: 1, macros: 1
- `test/js/node/test/fixtures/keys/selfsigned-no-keycertsign/https_renew_cert.sh` (SHELL) | Magnitude: 0.0 | Delta: **0.074** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 6, indent_spaces: 2, branch: 1, safety: 1
- `src/bun.js/modules/NodeConstantsModule.h` (CPP) | Magnitude: 22.2 | Delta: **0.081** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: args: 576, indent_spaces: 399, macros: 278, import: 14
- `src/bun.js/bindings/node/crypto/CryptoDhJob.h` (CPP) | Magnitude: 0.1 | Delta: **0.118** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 23, args: 13, structural_boundaries: 8, branch: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `src/sql/postgres/AnyPostgresError.zig` (ZIG) | Magnitude: 24.6 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 122, core_var_decl: 28, design_snake_case: 24, design_short_vars: 16
- `test/js/node/test/fixtures/workload/fibonacci-sigint.js` (JAVASCRIPT) | Magnitude: 0.0 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: branch: 3, structural_boundaries: 2, safety: 2, indent_spaces: 2
- `test/integration/vite-build/the-test-app/svelte.config.js` (JAVASCRIPT) | Magnitude: 16.36 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 3, decorators: 2, import: 2
- `test/js/node/test/fixtures/es-module-loaders/hooks-input.mjs` (JAVASCRIPT) | Magnitude: 0.06 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 61, test: 17, structural_boundaries: 13, core_var_decl: 9
- `test/bundler/bundler_minify_symbol_for.test.ts` (TYPESCRIPT) | Magnitude: 34.9 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 241, test: 39, core_var_decl: 29, design_snake_case: 25

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/js/internal/fs/cp-sync.ts` (TYPESCRIPT) | Magnitude: 195.22 | Delta: **0.036** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 146, branch: 56, structural_boundaries: 38, args: 25
- `src/bun.js/api/server/FileRoute.zig` (ZIG) | Magnitude: 258.94 | Delta: **0.045** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 402, branch: 65, core_var_decl: 56, structural_boundaries: 52
- `src/copy_file.zig` (ZIG) | Magnitude: 143.52 | Delta: **0.054** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 190, branch: 45, structural_boundaries: 41, core_var_decl: 39
- `src/http/websocket_client.zig` (ZIG) | Magnitude: 1350.98 | Delta: **0.072** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 1302, core_var_decl: 287, design_snake_case: 240, branch: 197
- `src/bun.js/bindings/URLDecomposition.cpp` (CPP) | Magnitude: 132.82 | Delta: **0.081** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 129, branch: 57, structural_boundaries: 57, core_var_decl: 27

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `packages/bun-plugin-svelte/src/options.spec.ts` (TYPESCRIPT) | Magnitude: 16.94 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 39, structural_boundaries: 16, test: 10, args: 9
- `src/bun.zig` (ZIG) | Magnitude: 2262.04 | Delta: **0.039** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 2244, core_var_decl: 601, api: 523, structural_boundaries: 517
- `src/sql/postgres/PostgresProtocol.zig` (ZIG) | Magnitude: 46.5 | Delta: **0.063** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: core_var_decl: 49, globals: 47, api: 43, design_pascal_case: 43
- `src/memory.zig` (ZIG) | Magnitude: 65.26 | Delta: **0.083** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 101, doc: 72, branch: 26, core_var_decl: 22
- `src/sql/mysql/protocol/PreparedStatement.zig` (ZIG) | Magnitude: 59.0 | Delta: **0.087** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 69, core_var_decl: 24, safety: 19, globals: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `src/s3/download_stream.zig` (ZIG) | Magnitude: 149.0 | Delta: **0.09** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 195, core_var_decl: 49, design_snake_case: 41, branch: 36

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `packages/bun-types/devserver.d.ts` (TYPESCRIPT) | Magnitude: 0.7 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: structural_boundaries: 26, indent_spaces: 21, doc: 12, args: 8
- `src/api/schema.js` (JAVASCRIPT) | Magnitude: 2329.36 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 2838, structural_boundaries: 648, branch: 629, core_var_decl: 599
- `test/js/bun/resolve/toml/toml.test.js` (JAVASCRIPT) | Magnitude: 22.22 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 51, test: 33, core_var_decl: 22, structural_boundaries: 21
- `test/js/node/net/socketaddress.spec.ts` (TYPESCRIPT) | Magnitude: 30.5 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 249, test: 80, structural_boundaries: 51, args: 48
- `test/js/node/test/parallel/test-fs-write-file-invalid-path.js` (JAVASCRIPT) | Magnitude: 16.62 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 11, core_var_decl: 10, design_snake_case: 7, structural_boundaries: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `src/css/rules/scope.zig` (ZIG) | Magnitude: 33.96 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 44, safety: 16, doc: 9, core_var_decl: 8
- `misctools/ntquery.cpp` (CPP) | Magnitude: 80.46 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 136, branch: 26, structural_boundaries: 20, pointers: 20
- `test/integration/vite-build/the-test-app/src/routes/+layout.svelte` (HTML) | Magnitude: 116.22 | Delta: **0.067** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 387, core_var_decl: 118, design_snake_case: 75, structural_boundaries: 65
- `src/bun.js/bindings/webcore/EventDispatcher.cpp` (CPP) | Magnitude: 70.76 | Delta: **0.121** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 72, dead_code: 35, branch: 24, structural_boundaries: 16
- `src/handle_oom.zig` (ZIG) | Magnitude: 27.52 | Delta: **0.133** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 39, branch: 23, doc: 18, core_var_decl: 14

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `packages/bun-types/bun.d.ts` -> Churn: **100.0%** | Cog Load: 9.4444% | Debt: 100.0%
- `src/bun.js/bindings/bindings.cpp` -> Churn: **84.07%** | Cog Load: 39.8807% | Debt: 99.9996%
- `src/bun.js/bindings/ZigGlobalObject.cpp` -> Churn: **81.9%** | Cog Load: 15.7564% | Debt: 98.8387%
- `src/cli/Arguments.zig` -> Churn: **78.85%** | Cog Load: 94.3075% | Debt: 8.8912%
- `src/bun.js/bindings/BunObject.cpp` -> Churn: **77.75%** | Cog Load: 42.5176% | Debt: 99.0241%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `test/js/sql/sqlite-sql.test.ts` -> **Alistair Smith** (100.0% isolated ownership) | Magnitude: 23599.15
- `src/css/properties/properties_generated.zig` -> **pfg** (100.0% isolated ownership) | Magnitude: 4778.92
- `test/cli/install/bun-run.test.ts` -> **robobun** (100.0% isolated ownership) | Magnitude: 4091.26
- `test/bundler/metafile.test.ts` -> **robobun** (100.0% isolated ownership) | Magnitude: 3994.69
- `test/bundler/transpiler/esbuild-decorator-tests.ts` -> **Jarred Sumner** (100.0% isolated ownership) | Magnitude: 2475.88

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/bun.js/bindings/napi.cpp` -> **Severity: 1.931** (Bridge: 0.0195 * Flux: 99.0384%)
- `src/bun.zig` -> **Severity: 0.604** (Bridge: 0.007 * Flux: 85.9246%)
- `src/bun.js/bindings/ZigGlobalObject.cpp` -> **Severity: 0.514** (Bridge: 0.0189 * Flux: 27.1785%)
- `src/bun.js/bindings/webcrypto/SubtleCrypto.cpp` -> **Severity: 0.202** (Bridge: 0.0021 * Flux: 95.3023%)
- `src/bun.js.zig` -> **Severity: 0.195** (Bridge: 0.002 * Flux: 99.9982%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `test/napi/node-napi-tests/test/js-native-api/common.h` -> **Severity: 9.078** (Embedded: 0.1606 * Error Risk: 56.52%)
- `src/napi/js_native_api.h` -> **Severity: 8.794** (Embedded: 0.144 * Error Risk: 61.0811%)
- `src/napi/node_api.h` -> **Severity: 7.145** (Embedded: 0.0905 * Error Risk: 78.913%)
- `src/napi/js_native_api_types.h` -> **Severity: 7.014** (Embedded: 0.1284 * Error Risk: 54.6296%)
- `src/bun.js/bindings/headers.h` -> **Severity: 6.775** (Embedded: 0.0847 * Error Risk: 80.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `test/napi/node-napi-tests/test/js-native-api/common-inl.h` -> **Severity: 1280.8** (Blast Radius: 12.808 * Doc Risk: 100.0%)
- `src/css/css_parser.zig` -> **Severity: 375.163** (Blast Radius: 5.085 * Doc Risk: 73.7783%)
- `src/bun.js/bindings/napi.cpp` -> **Severity: 341.9** (Blast Radius: 3.419 * Doc Risk: 100.0%)
- `test/js/node/test/common/tmpdir.js` -> **Severity: 321.7** (Blast Radius: 3.217 * Doc Risk: 100.0%)
- `src/bun.js/bindings/bun-simdutf.zig` -> **Severity: 225.425** (Blast Radius: 2.296 * Doc Risk: 98.1818%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 8403 literal sites + 25 sites through wrappers = 8428
- **`memory_alloc`:** 4987 literal sites + 40 sites through wrappers = 5027
- **`panics_and_aborts`:** 9343 literal sites + 123 sites through wrappers = 9466

- `databases` (function, memory_alloc, primitive): 21 call sites in 1 files -- `src/bun.js/bindings/sqlite/JSSQLStatement.cpp`
- `newSym` (function, panics_and_aborts, primitive): 20 call sites in 1 files -- `src/ast/lowerDecorators.zig`
- `decodeError` (function, panics_and_aborts, primitive): 13 call sites in 1 files -- `packages/bun-error/sourcemap.ts`
- `throwError` (function, panics_and_aborts, primitive): 12 call sites in 1 files -- `src/codegen/cppbind.ts`
- `exit` (function, debug_prints, primitive): 9 call sites in 1 files -- `packages/bun-lambda/runtime.ts`
- `exit` (function, panics_and_aborts, primitive): 9 call sites in 1 files -- `packages/bun-lambda/runtime.ts`
- `throwSettingRangeError` (function, panics_and_aborts, primitive): 9 call sites in 1 files -- `src/js/node/http2.ts`
- `error` (function, panics_and_aborts, primitive): 8 call sites in 1 files -- `src/js/node/punycode.ts`
- `__typeError` (function, panics_and_aborts, primitive): 6 call sites in 1 files -- `src/runtime.js`
- `EINVAL` (function, panics_and_aborts, primitive): 5 call sites in 1 files -- `src/js/node/dgram.ts`
- `newWeakMapExpr` (function, panics_and_aborts, primitive): 5 call sites in 1 files -- `src/ast/lowerDecorators.zig`
- `extractCssUrl` (function, panics_and_aborts, primitive): 4 call sites in 1 files -- `test/bake/dev/css.test.ts`
*(+48 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 200623 call pairs -- scoped 21.5%, unique 1.5%, ambiguous 38.3%, external 38.8%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| zig | 94679 | 23.9% | 0.0% | 46.8% | 29.3% |
| cpp | 54058 | 16.6% | 2.8% | 28.0% | 52.6% |
| typescript | 25855 | 17.1% | 0.0% | 40.8% | 42.1% |
| javascript | 21452 | 30.1% | 0.0% | 31.6% | 38.3% |
| c | 3074 | 6.4% | 48.8% | 0.2% | 44.6% |
| python | 938 | 26.5% | 0.0% | 1.3% | 72.2% |
| shell | 236 | 21.6% | 0.0% | 0.0% | 78.4% |
| html | 117 | 19.7% | 0.0% | 0.0% | 80.3% |
| ruby | 84 | 17.9% | 0.0% | 2.4% | 79.8% |
| rust | 82 | 15.9% | 0.0% | 1.2% | 82.9% |

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
