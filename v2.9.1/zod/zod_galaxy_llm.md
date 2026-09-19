# ARCHITECTURAL_BRIEF: zod
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/colinhacks/zod.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 411 analyzed artifact(s), 55423 LOC.
- **Load-bearing artifact:** `packages/zod/src/v4/core/core.ts` -- 7 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `packages/zod/src/v4/core/index.ts` -- pulls in 16 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `.npmrc` at magnitude 5000.0 (structural weight, not risk).
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
| Total Artifacts | 567 |
| Analyzed Artifacts (Scanned) | 411 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 156 |
| Total LOC | 55423 |
| Volatility Index | 0.01 |
| % Scanned of codebase = | 72.5% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7243 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3781 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 4 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 353 | 54486 | 85.9% |
| MARKDOWN | 18 | 0 | 4.4% |
| JSON | 18 | 291 | 4.4% |
| PLAINTEXT | 9 | 1 | 2.2% |
| XML | 6 | 48 | 1.5% |
| YAML | 3 | 11 | 0.7% |
| HTML | 2 | 537 | 0.5% |
| JAVASCRIPT | 2 | 49 | 0.5% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Mid Flat Project`
> **Architectural Drift Z-Score:** `2.709`
> **Composition Archetype:** `Mid Flat Project` (z +2.71; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 37%, Data / Markup / Trivial 24%, Large Core Modules (2) 15%, Callbacks & Closures Files 6%, Generic / Templated Code Files 5%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 382 | 92.9% |
| Unknown | 1 | 0.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 26 | 6.3% |
| Static: Minified & Vendor Opaque Mass | 2 | 0.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 156*

**Composition by Extension & Reason:**
- `.tsx`: 28x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 27x Excluded (Explicitly Denied Extension: '.png')
- `no_extension`: 17x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.mdx`: 17x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ts`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 13 exceeds 500 chars), 1x Excluded (Saturation: Line 63 exceeds 500 chars)
- `.json`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ai`: 8x Excluded (Explicitly Denied Extension: '.ai')
- `.jpg`: 8x Excluded (Explicitly Denied Extension: '.jpg')
- `.pdf`: 8x Excluded (Explicitly Denied Extension: '.pdf')
- `.yml`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.svg`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ico`: 2x Excluded (Explicitly Denied Extension: '.ico')
- `.css`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mjs`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 12474 LOC)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 11.3 | 6.2 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.3 | 17.2 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 4.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 3.9 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 8.6 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 19.4 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 10.5 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 3.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 6.8 | 1.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 6.9 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 41.7 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 134 | 34 | 0 | `packages/zod/src/v3/types.ts` |
| cleanup | 0 | 0 | 0 | - |
| guards | 5072 | 266 | 28 | `packages/zod/src/v4/mini/tests/index.test.ts` |
| danger | 1702 | 143 | 9 | `packages/zod/src/v3/types.ts` |
| concurrency | 1128 | 115 | 6 | `packages/zod/src/v3/tests/async-parsing.test.ts` |
| connectivity | 2238 | 142 | 4 | `packages/zod/src/v4/core/schemas.ts` |
| io | 991 | 90 | 6 | `packages/zod/src/v4/classic/tests/to-json-schema.test.ts` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 129 | 35 | 0 | `packages/zod/src/v4/classic/tests/codec.test.ts` |
| serialization | 57 | 25 | 0 | `packages/zod/src/v4/core/to-json-schema.ts` |
| regex | 69 | 19 | 0 | `packages/zod/src/v4/core/util.ts` |
| events | 167 | 38 | 0 | `packages/docs-v3/blog/index.html` |
| tests | 6841 | 168 | 47 | `packages/zod/src/v4/classic/tests/string.test.ts` |
| docs | 303 | 33 | 0 | `packages/zod/src/v4/classic/schemas.ts` |
| debt | 364 | 71 | 2 | `packages/zod/src/v4/classic/schemas.ts` |
| mutation | 7757 | 309 | 46 | `packages/zod/src/v3/types.ts` |
| dead_code | 486 | 80 | 2 | `packages/zod/src/v4/core/api.ts` |
| credential | 7 | 2 | 0 | `packages/zod/src/v4/classic/tests/string.test.ts` |
| threat | 131 | 33 | 0 | `packages/zod/src/v3/types.ts` |
| ml_ai | 113 | 27 | 0 | `packages/tsc/generate.ts` |
| ui | 23 | 4 | 0 | `packages/zod/src/v3/types.ts` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `packages/zod/src/v4/classic/tests/to-json-schema.test.ts` (Hits: 159)
- `packages/zod/src/v4/classic/tests/string.test.ts` (Hits: 111)
- `packages/zod/src/v3/types.ts` (Hits: 82)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **core.ts** (`packages/zod/src/v4/core/core.ts`) — 7 inbound connections
2. **ERROR_HANDLING.md** (`packages/docs-v3/ERROR_HANDLING.md`) — 5 inbound connections
3. **config.ts** (`packages/zod/src/v4/core/config.ts`) — 4 inbound connections
4. **CHANGELOG.md** (`packages/docs-v3/CHANGELOG.md`) — 3 inbound connections
5. **README_ZH.md** (`packages/docs-v3/README_ZH.md`) — 2 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.ts** (`packages/zod/src/v4/core/index.ts`) — 16 outbound dependencies
2. **external.ts** (`packages/zod/src/v4/classic/external.ts`) — 12 outbound dependencies
3. **schemas.ts** (`packages/zod/src/v4/core/schemas.ts`) — 12 outbound dependencies
4. **index.html** (`packages/docs-v3/blog/index.html`) — 11 outbound dependencies
5. **index.html** (`packages/docs-v3/index.html`) — 11 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `convertBaseSchema` **(Many-Argument Workhorses)** (@ `packages/zod/src/v4/classic/from-json-schema.ts`) -> Impact: **284.7** | LOC: 394
- `validateOpenAPI30Schema` **(Many-Argument Workhorses)** (@ `packages/zod/src/v4/classic/tests/to-json-schema.test.ts`) -> Impact: **234.0** | LOC: 1202
- `getSizing` **(Defensive Guards)** (@ `packages/zod/src/v4/locales/he.ts`) -> Impact: **163.7** | LOC: 192
- `_parse` **(Compute Cores)** (@ `packages/zod/src/v3/types.ts`) -> Impact: **137.1** | LOC: 309
- `errorMap` **(Compute Cores)** (@ `packages/zod/src/v3/locales/en.ts`) -> Impact: **132.5** | LOC: 121
- `finalize` **(Many-Argument Workhorses)** (@ `packages/zod/src/v4/core/to-json-schema.ts`) -> Impact: **117.0** | LOC: 158
- `flattenRef` **(Defensive Guards)** (@ `packages/zod/src/v4/core/to-json-schema.ts`) -> Impact: **95.2** | LOC: 150
  * *Intent:* // flatten refs - inherit properties from parent schemas
- `errorMap` **(Defensive Guards)** (@ `packages/zod/src/v3/tests/error.test.ts`) -> Impact: **82.0** | LOC: 197
- `errorMap` **(Defensive Guards)** (@ `packages/zod/src/v4/classic/tests/error.test.ts`) -> Impact: **76.0** | LOC: 304
- `check` **(Compute Cores)** (@ `packages/zod/src/v4/core/schemas.ts`) -> Impact: **74.8** | LOC: 308

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `packages/zod/src/v4/classic/tests` | 74 | 9368.63 | 8.43% | 0.0% |
| `packages/zod/src/v3/tests` | 61 | 9059.36 | 8.98% | 0.0% |
| `packages/zod/src/v4/core` | 19 | 6808.5 | 37.67% | 16.46% |
| `__monolith__` | 16 | 5127.16 | 0.83% | 0.0% |
| `packages/zod/src/v4/classic` | 10 | 2118.56 | 17.05% | 21.36% |
| `packages/zod/src/v4/mini/tests` | 15 | 1215.76 | 4.43% | 0.0% |
| `packages/zod/src/v4/mini` | 7 | 936.62 | 3.43% | 1.51% |
| `packages/bench` | 33 | 638.32 | 17.79% | 18.56% |
| `packages/tsc` | 7 | 384.34 | 19.91% | 0.0% |
| `packages/zod/src/v3/helpers` | 6 | 328.46 | 18.24% | 39.2% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `packages/bench/safe.ts` -> **100.0%** Exposure
- `packages/zod/src/v4/classic/schemas.ts` -> **99.9542%** Exposure
- `packages/bench/key-iteration.ts` -> **99.7527%** Exposure
- `packages/zod/src/v4/classic/compat.ts` -> **99.6827%** Exposure
- `packages/zod/src/v4/core/api.ts` -> **99.1964%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `packages/bench/instanceof.ts` -> **100.0%** Exposure
- `packages/tsc/generate.ts` -> **100.0%** Exposure
- `packages/zod/src/v3/benchmarks/index.ts` -> **100.0%** Exposure
- `packages/zod/src/v3/helpers/parseUtil.ts` -> **100.0%** Exposure
- `packages/zod/src/v3/locales/en.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `packages/zod/src/v4/core/api.ts` -> **104** Orphaned Functions | **0** Duplicates
- `packages/zod/src/v4/classic/schemas.ts` -> **0** Orphaned Functions | **77** Duplicates
- `packages/zod/src/v3/types.ts` -> **39** Orphaned Functions | **19** Duplicates
- `packages/zod/src/v4/core/util.ts` -> **47** Orphaned Functions | **2** Duplicates
- `packages/zod/src/v4/classic/tests/codec.test.ts` -> **2** Orphaned Functions | **13** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `8` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `492` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.32
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v4/core/schemas.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2613.06 | **LOC:** 4557 | **CtrlFlow:** 17.6% | **Authorship Centralization:** 53.8%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 2.32; role: Isolated/Orphan
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Mutation Surface (formerly State Flux) (99.8%), Concurrency Surface (formerly Concurrency) (99.2%)
- **Documentation Coverage:** 96.3303% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `check` **(Compute Cores)** (Impact: 74.8)
  * `parse` **(Many-Argument Workhorses)** (Impact: 71.8)
  * `runChecks` **(Many-Argument Workhorses)** (Impact: 44.2)
  * `handleIntersectionResults` **(Many-Argument Workhorses)** (Impact: 42.2)
  * `parse` **(Many-Argument Workhorses)** (Impact: 38.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 41 instances
* *Amplified Cascading Flux:* 229 instances
* *Concurrency (weighted view):* 285
* *State Mutation (weighted view):* 738
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 582`, `structural_boundaries: 1750`, `args: 298`, `func_start: 96`, `class_start: 225`
* *Risk/State:* `safety_bypasses: 78`, `state_mutation: 280`, `dead_code: 25`, `planned_debt: 5`
* *Architecture:* `io: 15`, `api: 338`, `concurrency: 80`, `import: 13`
* *Defense:* `safety: 94`, `doc: 50`, `immutability_locks: 38`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.32
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` api.js, checks.js, core.js, doc.js, errors.js, json-schema.js, parse.js, regexes.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v4/classic/schemas.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 1890.84 | **LOC:** 2410 | **CtrlFlow:** 15.1% | **Authorship Centralization:** 78.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 2.32; role: Isolated/Orphan
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Debt Markers (formerly Tech Debt) (100.0%), Mutation Surface (formerly State Flux) (98.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (96.4%)
- **Documentation Coverage:** 87.3043% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `finite` **(Defensive Guards)** (Impact: 20.6)
    * *Intent:* // inst.finite = (params) => inst.check(core.finite(params));
  * `_function` **(Defensive Guards)** (Impact: 18.9)
  * `addIssue` **(Defensive Guards)** (Impact: 17.1)
  * `processJSONSchema` **(Defensive Guards)** (Impact: 14.4)
  * `hash` **(Defensive Guards)** (Impact: 12.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 34 instances
* *Concurrency (weighted view):* 53
* *State Mutation (weighted view):* 312
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 285`, `structural_boundaries: 1079`, `args: 551`, `func_start: 475`, `class_start: 81`
* *Risk/State:* `safety_bypasses: 116`, `state_mutation: 244`, `dead_code: 5`, `duplicate_logic: 77`
* *Architecture:* `io: 3`, `api: 262`, `concurrency: 18`, `import: 8`
* *Defense:* `safety: 37`, `doc: 65`, `test: 1`, `immutability_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.32
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index.js, json-schema-processors.js, standard-schema.js, to-json-schema.js, checks.js, iso.js, parse.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v4/classic/tests/partial.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 1811.29 | **LOC:** 428 | **CtrlFlow:** 8.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 2.32; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (73.0%), Complexity Load (formerly Cognitive Load) (12.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (9.3%), Guard Balance (formerly Safety Score) (2.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 14
* *State Mutation (weighted view):* 5
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 33`, `args: 26`, `func_start: 2`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `io: 4`, `concurrency: 4`, `import: 2`
* *Defense:* `safety: 83`, `test: 60`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.32
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` vitest, v4
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v3/tests/refine.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 1464.85 | **LOC:** 314 | **CtrlFlow:** 7.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 2.32; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (82.1%), Guard Balance (formerly Safety Score) (16.0%), Complexity Load (formerly Cognitive Load) (11.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 68`, `args: 38`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 2`
* *Architecture:* `io: 10`, `concurrency: 13`, `import: 4`
* *Defense:* `safety: 25`, `test: 38`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.32
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ZodError.js, util.js, vitest, v3
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v3/tests/object.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1448.43 | **LOC:** 435 | **CtrlFlow:** 5.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 2.32; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (90.5%), Complexity Load (formerly Cognitive Load) (11.9%), Guard Balance (formerly Safety Score) (3.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 99`, `args: 42`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 6`, `planned_debt: 1`
* *Architecture:* `concurrency: 20`, `import: 3`
* *Defense:* `safety: 75`, `test: 69`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.32
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` util.js, vitest, v3
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v4/classic/tests/transform.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 1417.82 | **LOC:** 362 | **CtrlFlow:** 5.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 2.32; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (77.0%), Guard Balance (formerly Safety Score) (27.0%), Complexity Load (formerly Cognitive Load) (11.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 61`, `args: 41`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 4`
* *Architecture:* `io: 11`, `concurrency: 14`, `import: 2`
* *Defense:* `safety: 15`, `test: 45`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.32
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` vitest, v4
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v3/tests/transformer.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 1300.18 | **LOC:** 234 | **CtrlFlow:** 9.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 2.32; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (95.4%), Complexity Load (formerly Cognitive Load) (16.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 49`, `args: 34`, `func_start: 4`
* *Risk/State:* None
* *Architecture:* `io: 2`, `concurrency: 14`, `import: 3`
* *Defense:* `safety: 13`, `test: 38`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.32
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` util.js, vitest, v3
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v4/classic/tests/discriminated-unions.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 1106.88 | **LOC:** 662 | **CtrlFlow:** 2.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 2.32; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (38.9%), Complexity Load (formerly Cognitive Load) (7.2%), Guard Balance (formerly Safety Score) (5.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 152`, `args: 35`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`
* *Architecture:* `io: 9`, `concurrency: 11`, `import: 2`
* *Defense:* `safety: 95`, `test: 82`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.32
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` vitest, v4
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v3/tests/partials.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 1003.56 | **LOC:** 244 | **CtrlFlow:** 10.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 2.32; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (94.8%), Complexity Load (formerly Cognitive Load) (18.5%), Guard Balance (formerly Safety Score) (3.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 14
* *State Mutation (weighted view):* 4
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 29`, `args: 15`, `func_start: 2`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `concurrency: 4`, `import: 4`
* *Defense:* `safety: 41`, `test: 45`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.32
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` util.js, vitest, v3
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v4/core/api.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 900.3 | **LOC:** 1799 | **CtrlFlow:** 11.3% | **Authorship Centralization:** 60.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 2.32; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (65.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (32.6%)
- **Documentation Coverage:** 97.5309% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_stringbool` **(Defensive Guards)** (Impact: 53.3)
  * `addIssue` **(Defensive Guards)** (Impact: 18.1)
  * `_superRefine` **(Defensive Guards)** (Impact: 18.0)
  * `_tuple` **(Many-Argument Workhorses)** (Impact: 12.0)
    * *Intent:* // export function _tuple( // Class: util.SchemaClass<schemas.$ZodTuple>, // items: [], // params?: ...
  * `_stringFormat` **(Generic / Templated Code)** (Impact: 7.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 58
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 161`, `structural_boundaries: 769`, `args: 139`, `func_start: 124`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 42`, `state_mutation: 20`, `dead_code: 8`, `unreferenced_by_name: 104`
* *Architecture:* `io: 1`, `api: 250`, `concurrency: 1`, `import: 6`
* *Defense:* `safety: 13`, `doc: 7`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.32
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` checks.js, core.js, errors.js, registries.js, schemas.js, util.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v4/mini/schemas.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 818.08 | **LOC:** 1917 | **CtrlFlow:** 9.3% | **Authorship Centralization:** 72.2%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 2.32; role: Isolated/Orphan
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (89.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.6%)
- **Documentation Coverage:** 97.6471% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_function` **(Defensive Guards)** (Impact: 18.9)
  * `hash` **(Defensive Guards)** (Impact: 12.8)
  * `tuple` **(Compute Cores)** (Impact: 10.8)
  * `object` **(Generic / Templated Code)** (Impact: 9.2)
  * `custom` **(Defensive Guards)** (Impact: 9.0)
    * *Intent:* // ZodCustom // custom schema
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 7 instances
* *Concurrency (weighted view):* 15
* *State Mutation (weighted view):* 33
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 134`, `structural_boundaries: 843`, `args: 221`, `func_start: 147`, `class_start: 74`
* *Risk/State:* `safety_bypasses: 104`, `state_mutation: 19`, `dead_code: 4`, `duplicate_logic: 2`
* *Architecture:* `io: 2`, `api: 263`, `concurrency: 5`, `import: 3`
* *Defense:* `safety: 14`, `doc: 5`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.32
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index.js, util.js, parse.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v4/core/json-schema-processors.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 757.28 | **LOC:** 668 | **CtrlFlow:** 26.2% | **Authorship Centralization:** 83.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 2.32; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.4%), Complexity Load (formerly Cognitive Load) (83.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `numberProcessor` **(Many-Argument Workhorses)** (Impact: 53.5)
  * `literalProcessor` **(Many-Argument Workhorses)** (Impact: 51.2)
  * `tupleProcessor` **(Many-Argument Workhorses)** (Impact: 43.0)
  * `stringProcessor` **(Many-Argument Workhorses)** (Impact: 39.8)
    * *Intent:* // ==================== SIMPLE TYPE PROCESSORS ====================
  * `recordProcessor` **(Many-Argument Workhorses)** (Impact: 29.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 80 instances
* *State Mutation (weighted view):* 252
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 148`, `structural_boundaries: 149`, `args: 55`, `func_start: 42`
* *Risk/State:* `safety_bypasses: 54`, `state_mutation: 92`
* *Architecture:* `io: 22`, `api: 44`, `import: 6`
* *Defense:* `safety: 9`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.32
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` checks.js, json-schema.js, registries.js, schemas.js, to-json-schema.js, util.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v4/core/util.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 751.1 | **LOC:** 979 | **CtrlFlow:** 27.2% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 2.32; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (97.8%), Mutation Surface (formerly State Flux) (88.2%), Guard Balance (formerly Safety Score) (84.8%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `finalizeIssue` **(Defensive Guards)** (Impact: 43.4)
  * `getParsedType` **(Compute Cores)** (Impact: 39.7)
  * `partial` **(Many-Argument Workhorses)** (Impact: 24.6)
  * `createTransparentProxy` **(Defensive Guards)** (Impact: 23.0)
  * `floatSafeRemainder` **(Defensive Guards)** (Impact: 18.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 31 instances
* *Concurrency (weighted view):* 9
* *State Mutation (weighted view):* 93
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 226`, `structural_boundaries: 462`, `args: 102`, `func_start: 79`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 76`, `state_mutation: 31`, `dead_code: 4`, `duplicate_logic: 2`, `unreferenced_by_name: 47`
* *Architecture:* `io: 9`, `api: 131`, `concurrency: 4`, `import: 5`
* *Defense:* `safety: 40`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.32
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` checks.js, core.js, errors.js, schemas.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v4/mini/tests/string.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 740.41 | **LOC:** 348 | **CtrlFlow:** 2.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 2.32; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (44.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (7.5%), Complexity Load (formerly Cognitive Load) (7.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (4.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 106`, `args: 101`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 5`
* *Architecture:* `io: 53`, `concurrency: 6`, `import: 2`
* *Defense:* `safety: 85`, `test: 148`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.32
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` vitest, mini
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v4/core/checks.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 626.86 | **LOC:** 1294 | **CtrlFlow:** 13.1% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 2.32; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (93.8%), Guard Balance (formerly Safety Score) (85.8%), Complexity Load (formerly Cognitive Load) (54.1%)
- **Documentation Coverage:** 95.2381% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `check` **(Compute Cores)** (Impact: 27.4)
  * `check` **(Compute Cores)** (Impact: 20.5)
  * `check` **(Compute Cores)** (Impact: 17.7)
  * `check` **(Generic / Templated Code)** (Impact: 16.7)
  * `check` **(Compute Cores)** (Impact: 16.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 87 instances
* *State Mutation (weighted view):* 279
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 117`, `structural_boundaries: 388`, `args: 70`, `func_start: 21`, `class_start: 66`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 105`, `dead_code: 15`
* *Architecture:* `api: 93`, `concurrency: 1`, `import: 5`
* *Defense:* `safety: 26`, `doc: 3`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.32
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` core.js, errors.js, regexes.js, schemas.js, util.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v3/tests/discriminated-unions.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 587.22 | **LOC:** 316 | **CtrlFlow:** 2.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 2.32; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (65.1%), Complexity Load (formerly Cognitive Load) (8.7%), Guard Balance (formerly Safety Score) (4.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 103`, `args: 22`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`
* *Architecture:* `io: 4`, `concurrency: 10`, `import: 2`
* *Defense:* `safety: 69`, `test: 36`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.32
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` vitest, v3
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v4/classic/tests/tuple.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 488.56 | **LOC:** 184 | **CtrlFlow:** 5.9% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 2.32; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (88.5%), Guard Balance (formerly Safety Score) (24.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (16.5%), Complexity Load (formerly Cognitive Load) (12.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 22`, `args: 15`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 6`
* *Architecture:* `io: 6`, `concurrency: 9`, `import: 2`
* *Defense:* `safety: 9`, `test: 34`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.32
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` vitest, v4
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v3/tests/standard-schema.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 463.58 | **LOC:** 84 | **CtrlFlow:** 16.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 2.32; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (52.8%), Dead Code Surface (formerly Dead Code) (17.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 20`, `args: 9`, `func_start: 2`
* *Risk/State:* `dead_code: 1`
* *Architecture:* `io: 2`, `concurrency: 14`, `import: 4`
* *Defense:* `safety: 9`, `test: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.32
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` util.js, standard-schema.js, spec, vitest, v3
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v3/tests/set.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 446.05 | **LOC:** 143 | **CtrlFlow:** 7.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 2.32; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (55.5%), Complexity Load (formerly Cognitive Load) (14.4%), Guard Balance (formerly Safety Score) (8.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 21`, `args: 13`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 6`
* *Architecture:* `io: 3`, `concurrency: 4`, `import: 4`
* *Defense:* `safety: 10`, `test: 50`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.32
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` util.js, vitest, v3
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v4/classic/tests/to-json-schema.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 349.12 | **LOC:** 2991 | **CtrlFlow:** 5.2% | **Authorship Centralization:** 55.6%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 2.32; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (53.7%), Guard Balance (formerly Safety Score) (26.1%), Concurrency Surface (formerly Concurrency) (12.9%), Complexity Load (formerly Cognitive Load) (7.5%)
- **Documentation Coverage:** 94.7368% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `validateOpenAPI30Schema` **(Many-Argument Workhorses)** (Impact: 234.0)
  * `override` **(I/O & Config Routines)** (Impact: 13.2)
  * `override` **(Compute Cores)** (Impact: 4.5)
  * `override` **(Defensive Guards)** (Impact: 4.2)
  * `override` **(Parameter Forwarders)** (Impact: 3.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 14
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 140`, `structural_boundaries: 441`, `args: 119`, `func_start: 19`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 10`, `dead_code: 1`, `fragile_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 159`, `concurrency: 3`, `import: 3`
* *Defense:* `safety: 129`, `doc: 1`, `test: 267`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.32
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` openapi-schema-validator, vitest, zod, core
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v4/classic/tests/record.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 348.1 | **LOC:** 633 | **CtrlFlow:** 0.4% | **Authorship Centralization:** 83.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 2.32; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (46.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (43.9%), Guard Balance (formerly Safety Score) (16.4%), Complexity Load (formerly Cognitive Load) (7.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 58`, `args: 29`, `func_start: 3`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`
* *Architecture:* `io: 21`, `concurrency: 13`, `import: 2`
* *Defense:* `safety: 38`, `test: 84`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.32
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` vitest, v4
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v4/classic/tests/preprocess.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 345.08 | **LOC:** 283 | **CtrlFlow:** 1.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 2.32; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (56.9%), Guard Balance (formerly Safety Score) (32.3%), Complexity Load (formerly Cognitive Load) (7.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 38`, `args: 25`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 10`
* *Architecture:* `io: 11`, `concurrency: 8`, `import: 2`
* *Defense:* `safety: 17`, `test: 32`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.32
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` vitest, v4
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v4/classic/tests/pipe.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 344.66 | **LOC:** 102 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 2.32; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (71.8%), Complexity Load (formerly Cognitive Load) (11.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 22`, `args: 17`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `io: 2`, `concurrency: 4`, `import: 2`
* *Defense:* `safety: 6`, `test: 18`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.32
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` vitest, v4
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v3/tests/preprocess.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 343.83 | **LOC:** 187 | **CtrlFlow:** 2.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 2.32; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (92.7%), Guard Balance (formerly Safety Score) (14.9%), Complexity Load (formerly Cognitive Load) (11.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 38`, `args: 23`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 3`
* *Architecture:* `io: 5`, `concurrency: 11`, `import: 3`
* *Defense:* `safety: 21`, `test: 24`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.32
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` util.js, vitest, v3
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `packages/zod/src/v4/core/schemas.ts` -> Churn: **100.0%** | Cog Load: 59.7598% | Debt: 8.1905%
- `packages/zod/src/v4/classic/schemas.ts` -> Churn: **96.43%** | Cog Load: 23.9633% | Debt: 99.9542%
- `packages/zod/src/v4/core/util.ts` -> Churn: **72.76%** | Cog Load: 43.4457% | Debt: 97.8015%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `packages/zod/src/v4/classic/tests/partial.test.ts` -> **kevinmitch14** (100.0% isolated ownership) | Magnitude: 1811.29
- `packages/zod/src/v4/core/json-schema-processors.ts` -> **Colin McDonnell** (83.3% isolated ownership) | Magnitude: 757.28
- `packages/zod/src/v4/mini/tests/string.test.ts` -> **Nathaniel Gerlek** (100.0% isolated ownership) | Magnitude: 740.41
- `packages/zod/src/v4/classic/tests/record.test.ts` -> **Colin McDonnell** (83.3% isolated ownership) | Magnitude: 348.1
- `packages/zod/src/v4/classic/tests/union.test.ts` -> **Colin McDonnell** (100.0% isolated ownership) | Magnitude: 330.05

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `packages/zod/src/v4/core/core.ts` -> **Severity: 1.262** (Embedded: 0.017 * Error Risk: 74.1176%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `packages/zod/src/v4/core/core.ts` -> **Severity: 1007.688** (Blast Radius: 16.123 * Doc Risk: 62.5%)
- `packages/zod/src/v4/core/config.ts` -> **Severity: 1006.0** (Blast Radius: 10.06 * Doc Risk: 100.0%)
- `packages/bench/array.ts` -> **Severity: 232.0** (Blast Radius: 2.32 * Doc Risk: 100.0%)
- `packages/bench/benchUtil.ts` -> **Severity: 232.0** (Blast Radius: 2.32 * Doc Risk: 100.0%)
- `packages/bench/boolean.ts` -> **Severity: 232.0** (Blast Radius: 2.32 * Doc Risk: 100.0%)

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
