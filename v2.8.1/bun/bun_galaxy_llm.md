# ARCHITECTURAL_BRIEF: bun
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/oven-sh/bun` |
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
| Total Artifacts | 12530 |
| Analyzed Artifacts (Scanned) | 10146 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 2384 |
| Total LOC | 1431691 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 81.0% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6422 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2478 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 2.6% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.3285 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 342 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 4200 | 232412 | 41.4% |
| TYPESCRIPT | 2199 | 424092 | 21.7% |
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
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Hub-Coupled Monorepo` (z -0.39; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 32%, Data / Markup / Trivial 23%, Large Core Modules 13%, State Mutators Files 7%, Interface Declarations Files 6%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 9451 | 93.2% |
| Unknown | 109 | 1.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 577 | 5.7% |
| Static: Minified & Vendor Opaque Mass | 9 | 0.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 2384*

**Composition by Extension & Reason:**
- `.tgz`: 349x Excluded (Explicitly Denied Extension: '.tgz')
- `.mdx`: 328x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 195x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 19x Excluded: Neighborhood Micro-Mass Limit Exceeded, 3x Excluded (Saturation: Line 1 exceeds 500 chars)
- `.ts`: 193x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 8x Unsupported Format (.undeterminable), 2x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `.json`: 127x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded: Neighborhood Micro-Mass Limit Exceeded, 1x Excluded (Massive Static Asset Blob: 3974 LOC)
- `no_extension`: 113x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 14x Unsupported Format (.undeterminable), 4x Excluded (Binary Format Detected)
- `.map`: 100x Excluded (Unsupported Extension: '.map')
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
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 14.6 | 5.6 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 33.0 | 33.9 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 10.9 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 6.4 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 11.4 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 21.3 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 13.7 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 1.6 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 60.5 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 10.7 | 1.5 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 3.9 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 46.3 | 25.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 105580 | 3067 | 16 | `src/deps/boringssl.translated.zig` |
| cleanup | 9371 | 1950 | 2 | `test/js/sql/sqlite-sql.test.ts` |
| guards | 82956 | 4500 | 15 | `test/js/bun/css/files/materialize.css` |
| danger | 31038 | 3150 | 6 | `src/deps/boringssl.translated.zig` |
| concurrency | 51855 | 2823 | 7 | `test/js/sql/sql.test.ts` |
| connectivity | 63111 | 3400 | 7 | `src/deps/boringssl.translated.zig` |
| io | 24865 | 2916 | 4 | `test/js/sql/sql.test.ts` |
| crypto | 338 | 264 | 0 | `test/js/node/test/parallel/test-eslint-crypto-check.js` |
| ipc | 2810 | 757 | 0 | `src/crash_handler.zig` |
| time | 3390 | 778 | 0 | `test/js/bun/test/fake-timers/sinonjs/fake-timers.test.ts` |
| serialization | 3266 | 549 | 0 | `test/cli/install/bun-install.test.ts` |
| regex | 4111 | 605 | 0 | `test/js/bun/glob/match.test.ts` |
| events | 16809 | 2183 | 4 | `test/js/node/events/event-emitter.test.ts` |
| tests | 76601 | 3910 | 10 | `test/js/sql/sql.test.ts` |
| docs | 23346 | 1088 | 1 | `src/windows.zig` |
| debt | 20707 | 3097 | 4 | `test/bundler/esbuild/default.test.ts` |
| mutation | 294734 | 7856 | 60 | `src/deps/boringssl.translated.zig` |
| dead_code | 12868 | 2192 | 2 | `src/bun.js/bindings/ncrypto.cpp` |
| credential | 2950 | 61 | 0 | `packages/bun-usockets/src/crypto/root_certs.h` |
| threat | 11491 | 1484 | 1 | `src/bun.js/bindings/node/http/llhttp/llhttp.c` |
| ml_ai | 2772 | 494 | 0 | `src/css/values/color.zig` |
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
- **Unknown Dependencies:** `23750` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/js/node/http2.ts` (TYPESCRIPT) -> Cumulative Risk: **778.66**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.87)
- **Magnitude:** 3230.54 | **LOC:** 4239 | **CtrlFlow:** 26.9% | **Authorship Centralization:** 60.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.7726%), Documentation (99.7067%), Tech Debt (97.0999%)
- **Heaviest Functions:** `doSendFileFD` (Many-Argument Workhorses, Impact: 90.8), `constructor` (Many-Argument Workhorses, Impact: 83.5), `validateSettings` (Compute Cores, Impact: 74.9)

### 2. `src/js/builtins/ReadableStreamInternals.ts` (TYPESCRIPT) -> Cumulative Risk: **771.54**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -1.09)
- **Magnitude:** 2027.3 | **LOC:** 2431 | **CtrlFlow:** 20.3% | **Authorship Centralization:** 60.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9594%), Concurrency (99.7527%)
- **Heaviest Functions:** `readStreamIntoSink` (Many-Argument Workhorses, Impact: 63.4), `readableStreamFromAsyncIterator` (Defensive Guards, Impact: 59.8), `assignStreamIntoResumableSink` (Defensive Guards, Impact: 56.0)

### 3. `src/js/builtins/CommonJS.ts` (TYPESCRIPT) -> Cumulative Risk: **768.79**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.53)
- **Magnitude:** 372.82 | **LOC:** 440 | **CtrlFlow:** 32.0% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9934%), Cognitive Load (97.8235%)
- **Heaviest Functions:** `overridableRequire` (Many-Argument Workhorses, Impact: 60.3), `loadEsmIntoCjs` (Compute Cores, Impact: 57.3), `requireResolve` (Defensive Guards, Impact: 24.6)

### 4. `src/bake/bun-framework-react/client.tsx` (TYPESCRIPT) -> Cumulative Risk: **760.2**
- **Archetype:** `file_cluster_8` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.80)
- **Magnitude:** 422.14 | **LOC:** 471 | **CtrlFlow:** 26.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.9999%)
- **Heaviest Functions:** `goto` (Defensive Guards, Impact: 47.9), `readCssMetadataFallback` (Compute Cores, Impact: 32.2), `readChunk` (Compute Cores, Impact: 26.8)

### 5. `src/bun.js/bindings/webcore/SerializedScriptValue.cpp` (CPP) -> Cumulative Risk: **756.51**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -1.48)
- **Magnitude:** 3358.5 | **LOC:** 6840 | **CtrlFlow:** 26.2% | **Authorship Centralization:** 58.3%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.8605%), State Flux (97.0196%)
- **Heaviest Functions:** `SerializedScriptValue::create` (Many-Argument Workhorses, Impact: 379.1), `dumpIfTerminal` (Many-Argument Workhorses, Impact: 178.4), `SerializedScriptValue::deserialize` (Many-Argument Workhorses, Impact: 158.8)

### 6. `src/js/node/fs.promises.ts` (TYPESCRIPT) -> Cumulative Risk: **752.27**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.42)
- **Magnitude:** 761.74 | **LOC:** 718 | **CtrlFlow:** 24.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.992%)
- **Heaviest Functions:** `writeFileAsyncIterator` (Defensive Guards, Impact: 96.2), `watch` (Compute Cores, Impact: 36.5), `read` (Many-Argument Workhorses, Impact: 35.6)

### 7. `src/js/internal/sql/mysql.ts` (TYPESCRIPT) -> Cumulative Risk: **750.68**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.53)
- **Magnitude:** 1035.14 | **LOC:** 1167 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9999%), Documentation (97.1429%), Concurrency (96.9366%)
- **Heaviest Functions:** `normalizeQuery` (Many-Argument Workhorses, Impact: 139.6), `connect` (Compute Cores, Impact: 60.8), `detectCommand` (Compute Cores, Impact: 44.6)

### 8. `src/js/internal/streams/from.ts` (TYPESCRIPT) -> Cumulative Risk: **744.4**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.24)
- **Magnitude:** 254.32 | **LOC:** 194 | **CtrlFlow:** 25.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `from` (Many-Argument Workhorses, Impact: 89.3), `close` (Compute Cores, Impact: 9.2), `nextSyncWithSyncValues` (I/O & Config Routines, Impact: 8.5)

### 9. `src/js/node/net.ts` (TYPESCRIPT) -> Cumulative Risk: **744.0**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -1.06)
- **Magnitude:** 2727.02 | **LOC:** 2658 | **CtrlFlow:** 26.9% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Cognitive Load (98.0965%)
- **Heaviest Functions:** `[kRealListen]` (Many-Argument Workhorses, Impact: 163.0), `listen` (Many-Argument Workhorses, Impact: 98.0), `connect` (Compute Cores, Impact: 91.6)

### 10. `src/bun.js/bindings/webcore/HTTPParsers.cpp` (CPP) -> Cumulative Risk: **740.31**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.79)
- **Magnitude:** 831.2 | **LOC:** 1021 | **CtrlFlow:** 38.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9991%), Tech Debt (99.9358%)
- **Heaviest Functions:** `parseHTTPHeader` (Many-Argument Workhorses, Impact: 99.6), `parseXSSProtectionHeader` (Many-Argument Workhorses, Impact: 44.6), `extractCharsetFromMediaType` (Compute Cores, Impact: 36.2)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `test/bundler/esbuild/lower.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 47663.85 | **LOC:** 1809 | **CtrlFlow:** 17.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (46.3672%), Tech Debt (0.0%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` expectBundled, arrow-1, arrow-2, bar1, bar2, bar3, bar4, baz1...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/js/sql/sqlite-sql.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 35662.23 | **LOC:** 5382 | **CtrlFlow:** 3.5% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (48.9604%), Tech Debt (0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` bun, bun:test, harness, node:fs, promises, node:path, path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/bundler/bundler_decorator_metadata.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 16357.97 | **LOC:** 1265 | **CtrlFlow:** 14.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (37.332%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 76 instances
* *State Mutation (weighted view):* 268
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 181`, `structural_boundaries: 441`, `args: 71`, `func_start: 103`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 68`, `state_mutation: 116`
* *Architecture:* `api: 1`, `concurrency: 2`, `import: 3`
* *Defense:* `safety: 4`, `test: 1`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` expectBundled, foo.js, bun:test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/deps/boringssl.translated.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 14576.0 | **LOC:** 19292 | **CtrlFlow:** 0.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (5.3652%), Tech Debt (0.0%)
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
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000148
  * `Imports (Out-Degree: 0):` bun, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/bun.js/bindings/node/http/llhttp/llhttp.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 5897.3 | **LOC:** 10155 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (7.7651%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` arm_neon.h, llhttp.h, nmmintrin.h, stdint.h, stdlib.h, string.h, wasm_simd128.h, x86intrin.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bench/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bench/async/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bench/ffi/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bench/grpc-server/cert.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bench/grpc-server/key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bench/gzip/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bench/log/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bench/modules/node_os/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bench/sqlite/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/bun-release/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/bun-uws/misc/cert.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/bun-uws/misc/key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/js/bun/http/fixtures/cert.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/js/bun/http/fixtures/cert.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/js/deno/fixtures/id_rsaEncryption.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/js/deno/fixtures/id_rsassaPss.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/js/deno/fixtures/id_rsassaPss_default.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/js/deno/fixtures/id_rsassaPss_saltLen_30.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/js/node/crypto/fixtures/ec_p256_private.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/js/node/crypto/fixtures/ec_p256_public.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.031
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

- `packages/bun-types/bun.d.ts` -> Churn: **100.0%** | Cog Load: 9.4586% | Debt: 100.0%
- `src/bun.js/bindings/bindings.cpp` -> Churn: **96.43%** | Cog Load: 40.5566% | Debt: 99.9996%
- `src/bun.js/bindings/ZigGlobalObject.cpp` -> Churn: **92.27%** | Cog Load: 16.6182% | Debt: 98.8678%
- `src/cli/Arguments.zig` -> Churn: **89.74%** | Cog Load: 95.1546% | Debt: 9.0324%
- `src/bun.zig` -> Churn: **84.45%** | Cog Load: 25.0287% | Debt: 63.6173%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/deps/boringssl.translated.zig` -> **pfg** (100.0% isolated ownership) | Magnitude: 14576.0
- `test/bundler/metafile.test.ts` -> **robobun** (100.0% isolated ownership) | Magnitude: 4942.13
- `test/cli/install/bun-run.test.ts` -> **robobun** (100.0% isolated ownership) | Magnitude: 4411.41
- `src/css/properties/properties_generated.zig` -> **pfg** (100.0% isolated ownership) | Magnitude: 4236.22
- `packages/bun-vscode/src/features/tests/__tests__/bun-test-controller.static-parser.test.ts` -> **Michael H** (100.0% isolated ownership) | Magnitude: 3560.22

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/install/PackageManager.zig` -> **Severity: 0.016** (Bridge: 0.0002 * Flux: 97.422%)
- `src/install/PackageManager/CommandLineArguments.zig` -> **Severity: 0.015** (Bridge: 0.0002 * Flux: 99.7277%)
- `src/install/install.zig` -> **Severity: 0.015** (Bridge: 0.0002 * Flux: 76.0524%)
- `src/cli.zig` -> **Severity: 0.014** (Bridge: 0.0002 * Flux: 71.3397%)
- `src/bundler/bundle_v2.zig` -> **Severity: 0.013** (Bridge: 0.0001 * Flux: 99.3384%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `test/napi/node-napi-tests/test/js-native-api/common.h` -> **Severity: 17.644** (Embedded: 0.2424 * Error Risk: 72.7823%)
- `src/napi/js_native_api.h` -> **Severity: 10.299** (Embedded: 0.1365 * Error Risk: 75.4559%)
- `src/napi/js_native_api_types.h` -> **Severity: 8.268** (Embedded: 0.1226 * Error Risk: 67.4492%)
- `src/js/internal/shared.ts` -> **Severity: 2.358** (Embedded: 0.026 * Error Risk: 90.8418%)
- `src/bun.js/bindings/libuv/uv.h` -> **Severity: 2.27** (Embedded: 0.0243 * Error Risk: 93.2995%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `test/napi/node-napi-tests/test/js-native-api/common-inl.h` -> **Severity: 1322.1** (Blast Radius: 13.221 * Doc Risk: 100.0%)
- `src/js/internal/primordials.js` -> **Severity: 606.1** (Blast Radius: 6.061 * Doc Risk: 100.0%)
- `src/js/internal/shared.ts` -> **Severity: 596.5** (Blast Radius: 5.965 * Doc Risk: 100.0%)
- `src/css/css_parser.zig` -> **Severity: 571.413** (Blast Radius: 7.745 * Doc Risk: 73.7783%)
- `src/js/node/async_hooks.ts` -> **Severity: 250.9** (Blast Radius: 2.509 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
