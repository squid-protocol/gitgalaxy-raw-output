# ARCHITECTURAL_BRIEF: bun
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/oven-sh/bun` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 10153 analyzed artifact(s), 1433154 LOC.
- **Load-bearing artifact:** `test/napi/node-napi-tests/test/js-native-api/common.h` -- 2462 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `test/bundler/esbuild/default.test.ts` -- pulls in 233 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `test/bundler/esbuild/lower.test.ts` at magnitude 47663.85 (structural weight, not risk).
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
| Total Artifacts | 12530 |
| Analyzed Artifacts (Scanned) | 10153 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 2377 |
| Total LOC | 1433154 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 81.0% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6485 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2478 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 2.6% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.3284 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 343 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 4199 | 232412 | 41.4% |
| TYPESCRIPT | 2207 | 425555 | 21.7% |
| CPP | 1333 | 193832 | 13.1% |
| ZIG | 1175 | 501078 | 11.6% |
| PLAINTEXT | 571 | 110 | 5.6% |
| HTML | 129 | 5845 | 1.3% |
| JSON | 126 | 3141 | 1.2% |
| C | 121 | 29863 | 1.2% |
| MARKDOWN | 116 | 0 | 1.1% |
| PYTHON | 69 | 3351 | 0.7% |
| CSS | 27 | 31721 | 0.3% |
| SHELL | 23 | 1695 | 0.2% |
| XML | 16 | 6 | 0.2% |
| YAML | 10 | 493 | 0.1% |
| DOCKERFILE | 9 | 435 | 0.1% |
| RUST | 7 | 560 | 0.1% |
| NIX | 2 | 219 | 0.0% |
| PERL | 2 | 664 | 0.0% |
| POWERSHELL | 2 | 350 | 0.0% |
| MAKEFILE | 2 | 1327 | 0.0% |
| SQLITE | 2 | 162 | 0.0% |
| BINARY_THREAT | 2 | 2 | 0.0% |
| PROTO | 1 | 11 | 0.0% |
| RUBY | 1 | 322 | 0.0% |
| CSV | 1 | 0 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Hub-Coupled Monorepo`
> **Architectural Drift Z-Score:** `5.608`
> **Composition Archetype:** `Hub-Coupled Monorepo` (z +5.61; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 31%, Data / Markup / Trivial 23%, Large Core Modules (2) 9%, Large Core Modules (3) 8%, State Mutators Files 7%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 9458 | 93.2% |
| Unknown | 109 | 1.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 577 | 5.7% |
| Static: Minified & Vendor Opaque Mass | 9 | 0.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 2377*

**Composition by Extension & Reason:**
- `.tgz`: 349x Excluded (Explicitly Denied Extension: '.tgz')
- `.mdx`: 328x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 195x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 20x Excluded: Neighborhood Micro-Mass Limit Exceeded, 3x Excluded (Saturation: Line 1 exceeds 500 chars)
- `.ts`: 193x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded: Neighborhood Micro-Mass Limit Exceeded, 1x Excluded (Machine-Generated Source Code Signature: 232 LOC)
- `.json`: 127x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded: Neighborhood Micro-Mass Limit Exceeded, 1x Excluded (Massive Static Asset Blob: 3974 LOC)
- `no_extension`: 113x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 14x Unsupported Format (.undeterminable), 4x Excluded (Binary Format Detected)
- `.map`: 99x Unresolved Ambiguity (No Retainable Structure), 1x Excluded (Saturation: Line 5 exceeds 500 chars)
- `.mjs`: 39x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 21x Excluded: Neighborhood Micro-Mass Limit Exceeded, 1x Excluded (Machine-Generated Source Code Signature: 89 LOC)
- `.lock`: 38x Excluded (Unsupported Extension: '.lock'), 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 7x Unsupported Format (.lock)
- `.snap`: 58x Excluded (Unsupported Extension: '.snap'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cmake`: 36x Excluded (Unsupported Extension: '.cmake'), 11x Unsupported Format (.cmake), 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 52x Excluded (Explicitly Denied Extension: '.png')
- `.idl`: 49x Unsupported Format (.idl)
- `.snapshot`: 46x Excluded (Unsupported Extension: '.snapshot')
- `.toml`: 28x Excluded (Unsupported Extension: '.toml'), 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 5x Unsupported Format (.toml)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 14.7 | 5.6 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 32.8 | 33.3 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 10.9 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 6.4 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 11.4 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 21.3 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 13.7 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 1.6 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 10.5 | 1.5 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 3.9 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 46.3 | 25.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 105581 | 3068 | 16 | `src/deps/boringssl.translated.zig` |
| cleanup | 9371 | 1950 | 2 | `test/js/sql/sqlite-sql.test.ts` |
| guards | 82988 | 4505 | 15 | `test/js/bun/css/files/materialize.css` |
| danger | 31088 | 3156 | 6 | `src/deps/boringssl.translated.zig` |
| concurrency | 51906 | 2828 | 7 | `test/js/sql/sql.test.ts` |
| connectivity | 63118 | 3404 | 7 | `src/deps/boringssl.translated.zig` |
| io | 24885 | 2922 | 4 | `test/js/sql/sql.test.ts` |
| crypto | 338 | 264 | 0 | `test/js/node/test/parallel/test-eslint-crypto-check.js` |
| ipc | 2811 | 758 | 0 | `src/crash_handler.zig` |
| time | 3390 | 778 | 0 | `test/js/bun/test/fake-timers/sinonjs/fake-timers.test.ts` |
| serialization | 3278 | 553 | 0 | `test/cli/install/bun-install.test.ts` |
| regex | 4156 | 609 | 0 | `test/js/bun/glob/match.test.ts` |
| events | 16813 | 2184 | 4 | `test/js/node/events/event-emitter.test.ts` |
| tests | 76607 | 3911 | 10 | `test/js/sql/sql.test.ts` |
| docs | 23360 | 1093 | 1 | `src/windows.zig` |
| debt | 20756 | 3104 | 4 | `test/bundler/esbuild/default.test.ts` |
| mutation | 295109 | 7863 | 61 | `src/deps/boringssl.translated.zig` |
| dead_code | 12869 | 2193 | 2 | `src/bun.js/bindings/ncrypto.cpp` |
| credential | 2950 | 61 | 0 | `packages/bun-usockets/src/crypto/root_certs.h` |
| threat | 11488 | 1482 | 1 | `src/bun.js/bindings/node/http/llhttp/llhttp.c` |
| ml_ai | 2780 | 495 | 0 | `src/css/values/color.zig` |
| ui | 1825 | 204 | 0 | `test/js/bun/css/files/materialize.css` |

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

1. **common.h** (`test/napi/node-napi-tests/test/js-native-api/common.h`) — 2462 inbound connections
2. **h.cjs** (`test/js/node/module/children-fixture/h.cjs`) — 872 inbound connections
3. **root.h** (`src/bun.js/bindings/root.h`) — 364 inbound connections
4. **config.h** (`src/bun.js/bindings/webcore/config.h`) — 258 inbound connections
5. **runner.mjs** (`bench/runner.mjs`) — 156 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **default.test.ts** (`test/bundler/esbuild/default.test.ts`) — 233 outbound dependencies
2. **ZigGlobalObject.cpp** (`src/bun.js/bindings/ZigGlobalObject.cpp`) — 210 outbound dependencies
3. **bindings.cpp** (`src/bun.js/bindings/bindings.cpp`) — 128 outbound dependencies
4. **bun.zig** (`src/bun.zig`) — 116 outbound dependencies
5. **bundler_barrel.test.ts** (`test/bundler/bundler_barrel.test.ts`) — 95 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `expectBundled` **(Many-Argument Workhorses)** (@ `test/bundler/expectBundled.ts`) -> Impact: **1189.6** | LOC: 1387
- `llhttp__internal__run` **(Many-Argument Workhorses)** (@ `src/bun.js/bindings/node/http/llhttp/llhttp.c`) -> Impact: **786.1** | LOC: 1443
- `parse` **(Many-Argument Workhorses)** (@ `src/cli/Arguments.zig`) -> Impact: **749.5** | LOC: 1230
- `printAs` **(Many-Argument Workhorses)** (@ `src/bun.js/ConsoleObject.zig`) -> Impact: **710.1** | LOC: 1078
- `parse` **(Many-Argument Workhorses)** (@ `src/css/properties/properties_generated.zig`) -> Impact: **665.5** | LOC: 1070
  * *Intent:* /// Parses a CSS property by name.
- `NewPrinter` **(Many-Argument Workhorses)** (@ `src/js_printer.zig`) -> Impact: **660.5** | LOC: 1410
- `call_uv_func` **(Many-Argument Workhorses)** (@ `test/napi/uv-stub-stuff/plugin.c`) -> Impact: **639.6** | LOC: 2468
  * *Intent:* // GENERATED CODE ... NO TOUCHY!! #include <node_api.h> #include <signal.h> #include <stdio.h> #include <string.h> #include <unistd.h> #include <uv.h>
- `setsockopt_6_or_4` **(Many-Argument Workhorses)** (@ `packages/bun-usockets/src/bsd.c`) -> Impact: **639.1** | LOC: 1221
- `parse` **(Many-Argument Workhorses)** (@ `src/install/npm.zig`) -> Impact: **633.9** | LOC: 915
  * *Intent:* /// This parses [Abbreviated metadata](https://github.com/npm/registry/blob/master/docs/responses/package-metadata.md#abbreviated-metadata-format)
- `migrateYarnLockfile` **(Many-Argument Workhorses)** (@ `src/install/yarn.zig`) -> Impact: **631.1** | LOC: 1140

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `test/js/node/crypto/fixtures` | 27 | 130000.02 | 0.0% | 0.0% |
| `test/js/node/tls/fixtures` | 22 | 105000.01 | 0.0% | 0.0% |
| `test/js/third_party/jsonwebtoken` | 17 | 85000.0 | 0.0% | 0.0% |
| `src/bun.js/bindings` | 457 | 55063.82 | 14.33% | 54.68% |
| `test/bundler/esbuild` | 14 | 52694.65 | 7.48% | 0.0% |
| `test/js/node/test/parallel` | 2200 | 45833.14 | 13.18% | 0.0% |
| `src` | 125 | 44678.26 | 18.21% | 10.17% |
| `test/js/sql` | 16 | 42597.72 | 28.44% | 0.0% |
| `test/js/node/http/fixtures` | 9 | 40000.01 | 1.41% | 0.0% |
| `test/regression/issue` | 334 | 35105.17 | 11.98% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `packages/bun-types/bun.d.ts` -> **100.0%** Exposure
- `packages/bun-types/html-rewriter.d.ts` -> **100.0%** Exposure
- `packages/bun-types/jsc.d.ts` -> **100.0%** Exposure
- `packages/bun-types/redis.d.ts` -> **100.0%** Exposure
- `packages/bun-types/shell.d.ts` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `bench/module-loader/create.js` -> **100.0%** Exposure
- `bench/snippets/array-shift.mjs` -> **100.0%** Exposure
- `misctools/headers-cleaner.js` -> **100.0%** Exposure
- `misctools/mime.js` -> **100.0%** Exposure
- `misctools/publish-examples.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/bun.js/bindings/ncrypto.cpp` -> **359** Orphaned Functions | **0** Duplicates
- `src/bun.js/bindings/bindings.cpp` -> **315** Orphaned Functions | **0** Duplicates
- `src/bun.js/bindings/uv-posix-stubs.c` -> **305** Orphaned Functions | **0** Duplicates
- `test/bundler/transpiler/esbuild-decorator-tests.ts` -> **0** Orphaned Functions | **210** Duplicates
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
- **Binary Anomalies (X-Ray):** `53` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `23767` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `test/bundler/esbuild/lower.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 47663.85 | **LOC:** 1809 | **CtrlFlow:** 17.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **36**; blast radius 0.03; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (53.3%), Complexity Load (formerly Cognitive Load) (46.4%), Connectivity (formerly Api Exposure) (10.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 66 instances
* *Amplified Cascading Flux:* 38 instances
* *Concurrency (weighted view):* 542
* *State Mutation (weighted view):* 192
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 296`, `structural_boundaries: 681`, `args: 238`, `func_start: 165`, `class_start: 55`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 6`, `state_mutation: 116`, `planned_debt: 5`
* *Architecture:* `io: 1`, `api: 150`, `concurrency: 212`, `import: 67`
* *Defense:* `safety: 103`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` expectBundled, arrow-1, arrow-2, bar1, bar2, bar3, bar4, baz1...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/js/sql/sqlite-sql.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 35662.23 | **LOC:** 5382 | **CtrlFlow:** 3.5% | **Authorship Centralization:** 75.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.03; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (49.0%), Guard Balance (formerly Safety Score) (22.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (19.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 7 instances
* *Amplified Race Conditions:* 207 instances
* *Amplified Cascading Flux:* 61 instances
* *Concurrency (weighted view):* 2257
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 209
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 148`, `structural_boundaries: 1367`, `args: 431`, `func_start: 219`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 87`
* *Architecture:* `io: 1169`, `concurrency: 1222`, `import: 7`
* *Defense:* `safety: 101`, `test: 967`, `sync_locks: 2`, `immutability_locks: 17`, `cleanup: 121`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` bun, bun:test, harness, node:fs, promises, node:path, path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/bundler/bundler_decorator_metadata.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 16357.97 | **LOC:** 1265 | **CtrlFlow:** 14.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.03; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (90.2%), Complexity Load (formerly Cognitive Load) (37.3%), Concurrency Surface (formerly Concurrency) (13.3%), Connectivity (formerly Api Exposure) (1.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 76 instances
* *State Mutation (weighted view):* 268
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 181`, `structural_boundaries: 441`, `args: 71`, `func_start: 103`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 68`, `state_mutation: 116`
* *Architecture:* `api: 1`, `concurrency: 2`, `import: 3`
* *Defense:* `safety: 4`, `test: 1`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` expectBundled, foo.js, bun:test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/deps/boringssl.translated.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 14576.0 | **LOC:** 19292 | **CtrlFlow:** 0.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 0.039; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Guard Balance (formerly Safety Score) (84.7%), Test Surface (formerly Verification) (80.0%), Dead Code Surface (formerly Dead Code) (17.4%)
- **Documentation Coverage:** 99.7271% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `init` **(Many-Argument Workhorses)** (Impact: 21.3)
  * `write` **(Type Conversions)** (Impact: 8.5)
  * `getCertErrorFromNo` **(I/O & Config Routines)** (Impact: 6.7)
  * `read` **(Type Conversions)** (Impact: 6.4)
  * `getError` **(Type Conversions)** (Impact: 6.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 1486`, `args: 3047`, `func_start: 2889`, `class_start: 169`
* *Risk/State:* `safety_bypasses: 1814`, `dead_code: 226`
* *Architecture:* `api: 9038`, `import: 191`
* *Defense:* `safety: 11`, `doc: 34`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.039
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000146
  * `Imports (Out-Degree: 0):` bun, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/bun.js/bindings/node/http/llhttp/llhttp.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 5897.3 | **LOC:** 10155 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.03; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 92.619% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `llhttp__internal__run` **(Many-Argument Workhorses)** (Impact: 786.1)
  * `llparse__match_sequence_to_lower` **(Many-Argument Workhorses)** (Impact: 18.7)
  * `llhttp__internal__c_mul_add_content_length` **(Many-Argument Workhorses)** (Impact: 14.7)
  * `llhttp__internal__c_mul_add_content_length_1` **(Many-Argument Workhorses)** (Impact: 14.7)
  * `llhttp__internal__c_mul_add_status_code` **(Many-Argument Workhorses)** (Impact: 14.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1367 instances
* *State Mutation (weighted view):* 4583
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1943`, `structural_boundaries: 792`, `args: 91`, `func_start: 63`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 1849`, `unreferenced_by_name: 2`
* *Architecture:* `api: 94`, `import: 8`
* *Defense:* `safety: 2`, `immutability_locks: 533`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` arm_neon.h, llhttp.h, nmmintrin.h, stdint.h, stdlib.h, string.h, wasm_simd128.h, x86intrin.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bench/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
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
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
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
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
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

### `bench/grpc-server/cert.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
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
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
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
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
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
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
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
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
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
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
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
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
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

### `packages/bun-uws/misc/cert.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
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
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
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
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
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

### `test/js/bun/http/fixtures/cert.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
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
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
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
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
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
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
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
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
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
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
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

### `test/js/node/crypto/fixtures/ec_p256_public.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
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
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `packages/bun-types/bun.d.ts` -> Churn: **100.0%** | Cog Load: 9.4586% | Debt: 100.0%
- `src/bun.js/bindings/bindings.cpp` -> Churn: **95.88%** | Cog Load: 40.5566% | Debt: 99.9996%
- `src/bun.js/bindings/ZigGlobalObject.cpp` -> Churn: **92.27%** | Cog Load: 16.6182% | Debt: 98.8678%
- `src/cli/Arguments.zig` -> Churn: **89.74%** | Cog Load: 95.1546% | Debt: 9.0324%
- `src/bun.zig` -> Churn: **81.98%** | Cog Load: 25.0287% | Debt: 63.6173%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/deps/boringssl.translated.zig` -> **pfg** (100.0% isolated ownership) | Magnitude: 14576.0
- `test/bundler/metafile.test.ts` -> **robobun** (100.0% isolated ownership) | Magnitude: 4942.13
- `test/cli/install/bun-run.test.ts` -> **robobun** (100.0% isolated ownership) | Magnitude: 4411.41
- `src/css/properties/properties_generated.zig` -> **pfg** (100.0% isolated ownership) | Magnitude: 4236.22
- `packages/bun-vscode/src/features/tests/__tests__/bun-test-controller.static-parser.test.ts` -> **Michael H** (100.0% isolated ownership) | Magnitude: 3560.22

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/install/PackageManager.zig` -> **Severity: 0.016** (Bridge: 0.0002 * Flux: 97.422%)
- `src/install/PackageManager/CommandLineArguments.zig` -> **Severity: 0.015** (Bridge: 0.0001 * Flux: 99.7277%)
- `src/install/install.zig` -> **Severity: 0.015** (Bridge: 0.0002 * Flux: 76.0524%)
- `src/cli.zig` -> **Severity: 0.013** (Bridge: 0.0002 * Flux: 71.3397%)
- `src/bundler/bundle_v2.zig` -> **Severity: 0.012** (Bridge: 0.0001 * Flux: 99.3384%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `test/napi/node-napi-tests/test/js-native-api/common.h` -> **Severity: 17.461** (Embedded: 0.2399 * Error Risk: 72.7823%)
- `src/napi/js_native_api.h` -> **Severity: 10.193** (Embedded: 0.1351 * Error Risk: 75.4559%)
- `src/napi/js_native_api_types.h` -> **Severity: 8.183** (Embedded: 0.1213 * Error Risk: 67.4492%)
- `src/js/internal/shared.ts` -> **Severity: 2.307** (Embedded: 0.0257 * Error Risk: 89.7686%)
- `src/bun.js/bindings/libuv/uv.h` -> **Severity: 2.247** (Embedded: 0.0241 * Error Risk: 93.2995%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `test/napi/node-napi-tests/test/js-native-api/common-inl.h` -> **Severity: 1318.2** (Blast Radius: 13.182 * Doc Risk: 100.0%)
- `src/js/internal/primordials.js` -> **Severity: 604.4** (Blast Radius: 6.044 * Doc Risk: 100.0%)
- `src/js/internal/shared.ts` -> **Severity: 594.8** (Blast Radius: 5.948 * Doc Risk: 100.0%)
- `src/css/css_parser.zig` -> **Severity: 569.421** (Blast Radius: 7.718 * Doc Risk: 73.7783%)
- `src/js/node/async_hooks.ts` -> **Severity: 250.1** (Blast Radius: 2.501 * Doc Risk: 100.0%)

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
