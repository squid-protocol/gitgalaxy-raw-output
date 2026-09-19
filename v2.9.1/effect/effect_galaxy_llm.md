# ARCHITECTURAL_BRIEF: effect
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/Effect-TS/effect.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 2115 analyzed artifact(s), 338934 LOC.
- **Load-bearing artifact:** `packages/effect/src/internal/opCodes/effect.ts` -- 446 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `packages/effect/src/index.ts` -- pulls in 178 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `packages/ai/openai/src/Generated.ts` at magnitude 3420.5 (structural weight, not risk).
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
| Total Artifacts | 2208 |
| Analyzed Artifacts (Scanned) | 2115 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 93 |
| Total LOC | 338934 |
| Volatility Index | 0.004 |
| % Scanned of codebase = | 95.8% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4936 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3924 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.6978 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 62 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 1767 | 335412 | 83.5% |
| JSON | 208 | 2944 | 9.8% |
| MARKDOWN | 73 | 0 | 3.5% |
| PLAINTEXT | 40 | 0 | 1.9% |
| SHELL | 11 | 132 | 0.5% |
| JAVASCRIPT | 9 | 304 | 0.4% |
| YAML | 5 | 47 | 0.2% |
| NIX | 1 | 29 | 0.0% |
| HTML | 1 | 66 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Hub-Coupled Monorepo`
> **Architectural Drift Z-Score:** `5.842`
> **Composition Archetype:** `Hub-Coupled Monorepo` (z +5.84; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 35%, Data / Markup / Trivial 23%, Generic / Templated Code Files 13%, Callbacks & Closures Files 10%, Large Core Modules (3) 8%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 2002 | 94.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 113 | 5.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 93*

**Composition by Extension & Reason:**
- `no_extension`: 42x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 16x Unsupported Format (.undeterminable)
- `.yml`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Static Asset Blob without Intent: 1003 LOC)
- `.patch`: 4x Unsupported Format (.patch), 2x Excluded (Unsupported Extension: '.patch')
- `.md`: 1x Excluded (Machine-Generated Source Code Signature: 78 LOC), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 34 LOC)
- `.ts`: 2x Excluded (Saturation: Line 4 exceeds 500 chars), 1x Excluded (Machine-Generated Source Code Signature: 1757 LOC)
- `.toml`: 2x Excluded (Unsupported Extension: '.toml')
- `.png`: 2x Excluded (Explicitly Denied Extension: '.png')
- `.lock`: 1x Excluded (Unsupported Extension: '.lock')
- `.ini`: 1x Excluded (Unsupported Extension: '.ini')
- `.gz`: 1x Excluded (Explicitly Denied Extension: '.gz')
- `.yaml`: 1x Excluded (Massive Static Asset Blob: 14139 LOC)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 89.2 | 5.3 | 2.5 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 23.7 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 4.7 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 4.8 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 25.0 | 3.3 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 16.7 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 9.9 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 14.7 | 0.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 31.1 | 2.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 89.4 | 1.7 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 25.3 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 10040 | 1440 | 12 | `packages/effect/src/index.ts` |
| cleanup | 196 | 82 | 0 | `packages/effect/src/internal/channel/subexecutor.ts` |
| guards | 19933 | 1032 | 22 | `packages/ai/openai/src/Generated.ts` |
| danger | 6928 | 571 | 6 | `packages/effect/src/Effect.ts` |
| concurrency | 19810 | 944 | 22 | `packages/effect/test/Schema/JSONSchema.new.test.ts` |
| connectivity | 19639 | 1021 | 22 | `packages/ai/openai/src/Generated.ts` |
| io | 3321 | 303 | 2 | `packages/cluster/src/SqlMessageStorage.ts` |
| crypto | 0 | 0 | 0 | - |
| ipc | 309 | 69 | 0 | `packages/platform/src/internal/worker.ts` |
| time | 412 | 72 | 0 | `packages/effect/test/Cron.test.ts` |
| serialization | 168 | 72 | 0 | `packages/effect/src/Schema.ts` |
| regex | 621 | 187 | 0 | `packages/effect/src/internal/stream.ts` |
| events | 12749 | 1491 | 15 | `packages/effect/src/Effect.ts` |
| tests | 11832 | 728 | 7 | `packages/effect/dtslint/Schema/Schema.tst.ts` |
| docs | 24319 | 946 | 24 | `packages/ai/openai/src/Generated.ts` |
| debt | 794 | 207 | 0 | `packages/effect/src/internal/pubsub.ts` |
| mutation | 43104 | 1584 | 51 | `packages/effect/test/Graph.test.ts` |
| dead_code | 760 | 269 | 1 | `packages/effect/src/internal/core.ts` |
| credential | 1 | 1 | 0 | `packages/ai/google/scripts/generate.sh` |
| threat | 585 | 160 | 0 | `packages/effect/src/Effect.ts` |
| ml_ai | 338 | 95 | 0 | `packages/effect/src/internal/defaultServices.ts` |
| ui | 2782 | 272 | 1 | `packages/effect/src/internal/channel.ts` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `packages/cluster/src/SqlMessageStorage.ts` (Hits: 120)
- `packages/sql-pg/test/Client.test.ts` (Hits: 95)
- `packages/effect/src/internal/configProvider.ts` (Hits: 84)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **effect.ts** (`packages/effect/src/internal/opCodes/effect.ts`) — 446 inbound connections
2. **Schema.ts** (`packages/effect/src/Schema.ts`) — 420 inbound connections
3. **Function.ts** (`packages/effect/src/Function.ts`) — 345 inbound connections
4. **Layer.ts** (`packages/effect/src/Layer.ts`) — 230 inbound connections
5. **Context.ts** (`packages/effect/src/Context.ts`) — 177 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.ts** (`packages/effect/src/index.ts`) — 178 outbound dependencies
2. **fiberRuntime.ts** (`packages/effect/src/internal/fiberRuntime.ts`) — 72 outbound dependencies
3. **Effect.ts** (`packages/effect/src/Effect.ts`) — 68 outbound dependencies
4. **Schema.ts** (`packages/effect/src/Schema.ts`) — 63 outbound dependencies
5. **index.ts** (`packages/platform/src/index.ts`) — 60 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `decodeError` **(Many-Argument Workhorses)** (@ `packages/ai/anthropic/src/Generated.ts`) -> Impact: **845.4** | LOC: 1216
- `decodeError` **(Many-Argument Workhorses)** (@ `packages/ai/openai/src/Generated.ts`) -> Impact: **712.3** | LOC: 3611
- `_R` **(Many-Argument Workhorses)** (@ `packages/effect/src/Effect.ts`) -> Impact: **562.5** | LOC: 6724
- `escapeMermaidLabel` **(Many-Argument Workhorses)** (@ `packages/effect/src/Graph.ts`) -> Impact: **503.8** | LOC: 2014
- `go` **(Many-Argument Workhorses)** (@ `packages/effect/src/JSONSchema.ts`) -> Impact: **349.0** | LOC: 362
- `expectError` **(Many-Argument Workhorses)** (@ `packages/effect/test/Schema/JSONSchema.test.ts`) -> Impact: **314.3** | LOC: 4900
- `logWithLevel` **(Many-Argument Workhorses)** (@ `packages/effect/src/Effect.ts`) -> Impact: **263.2** | LOC: 2458
  * *Intent:* * const program = Effect.logWithLevel( * LogLevel.Error, * "Critical error encountered", * Cause.die("System failure!") * ) * * Effect.runFork(program...
- `default` **(I/O & Config Routines)** (@ `packages/ai/openrouter/src/Generated.ts`) -> Impact: **204.6** | LOC: 4011
- `default` **(I/O & Config Routines)** (@ `packages/ai/anthropic/src/Generated.ts`) -> Impact: **197.0** | LOC: 3279
  * *Intent:* /** * Deleted object type. * * For file deletion, this is always `"file_deleted"`. */
- `valuesOf` **(Many-Argument Workhorses)** (@ `packages/effect/test/TArray.test.ts`) -> Impact: **182.6** | LOC: 1022

*Function archetypes referenced above:*
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `packages/effect/src` | 177 | 24965.14 | 7.02% | 5.05% |
| `packages/effect/src/internal` | 82 | 21049.39 | 12.72% | 19.7% |
| `packages/effect/test` | 103 | 6073.48 | 2.78% | 0.0% |
| `packages/platform/src` | 61 | 4784.17 | 6.69% | 4.0% |
| `packages/ai/openai/src` | 9 | 4458.12 | 8.48% | 4.92% |
| `packages/platform/src/internal` | 29 | 3633.84 | 11.34% | 3.04% |
| `packages/cli/src/internal` | 16 | 3151.26 | 11.65% | 2.05% |
| `packages/cluster/src` | 39 | 2656.34 | 5.86% | 0.22% |
| `packages/effect/src/internal/stm` | 21 | 2392.02 | 7.86% | 14.29% |
| `packages/ai/ai/src` | 15 | 2010.91 | 6.59% | 6.84% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `packages/experimental/test/utils/extend.ts` -> **100.0%** Exposure
- `packages/effect/src/internal/supervisor.ts` -> **99.9999%** Exposure
- `packages/cli/src/internal/helpDoc/span.ts` -> **99.9982%** Exposure
- `packages/vitest/src/utils.ts` -> **99.9939%** Exposure
- `packages/effect/src/internal/metric/keyType.ts` -> **99.9869%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `packages/cli/src/internal/autoCorrect.ts` -> **100.0%** Exposure
- `packages/effect/src/HashRing.ts` -> **100.0%** Exposure
- `packages/effect/src/internal/hashMap/array.ts` -> **100.0%** Exposure
- `packages/effect/src/internal/redBlackTree.ts` -> **100.0%** Exposure
- `packages/effect/src/internal/schedule/intervals.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `packages/effect/src/internal/core.ts` -> **64** Orphaned Functions | **29** Duplicates
- `packages/effect/src/Schema.ts` -> **46** Orphaned Functions | **8** Duplicates
- `packages/effect/src/internal/pubsub.ts` -> **0** Orphaned Functions | **41** Duplicates
- `packages/effect/src/SchemaAST.ts` -> **0** Orphaned Functions | **33** Duplicates
- `packages/effect/src/internal/stream.ts` -> **0** Orphaned Functions | **26** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `7517` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `packages/ai/openai/src/Generated.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 3420.5 | **LOC:** 22476 | **CtrlFlow:** 5.2% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.256; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (45.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (28.1%)
- **Documentation Coverage:** 37.9032% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `decodeError` **(Many-Argument Workhorses)** (Impact: 712.3)
  * `default` **(I/O & Config Routines)** (Impact: 135.9)
  * `default` **(I/O & Config Routines)** (Impact: 65.1)
  * `default` **(I/O & Config Routines)** (Impact: 48.0)
  * `default` **(I/O & Config Routines)** (Impact: 43.7)
**Contextual Mitigations & Amplifications:**
* *Api Near Db Sink:* 2 instances
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 535`, `structural_boundaries: 4831`, `args: 816`, `func_start: 34`, `class_start: 1239`
* *Risk/State:* `safety_bypasses: 266`, `high_risk_execution: 6`, `duplicate_logic: 15`
* *Architecture:* `io: 8`, `api: 1241`, `import: 8`
* *Defense:* `safety: 254`, `doc: 3300`, `immutability_locks: 578`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.256
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` HttpClient, HttpClientError, HttpClientRequest, HttpClientResponse, Data, Effect, ParseResult, Schema
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/effect/src/internal/stream.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 2804.44 | **LOC:** 8803 | **CtrlFlow:** 8.4% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **58**; blast radius 0.256; role: Isolated/Orphan
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Guard Balance (formerly Safety Score) (54.6%), Debt Markers (formerly Tech Debt) (21.7%), Concurrency Surface (formerly Concurrency) (15.5%)
- **Documentation Coverage:** 59.5376% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `running` **(Many-Argument Workhorses)** (Impact: 117.9)
  * `toPull` **(Generic / Templated Code)** (Impact: 77.8)
  * `onDone` **(Generic / Templated Code)** (Impact: 55.4)
  * `hasNext` **(Many-Argument Workhorses)** (Impact: 38.7)
  * `zipChunks` **(Generic / Templated Code)** (Impact: 36.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 77 instances
* *Concurrency (weighted view):* 31
* *State Mutation (weighted view):* 266
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 682`, `structural_boundaries: 3599`, `args: 1759`, `func_start: 432`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 53`, `state_mutation: 112`, `planned_debt: 1`, `duplicate_logic: 26`
* *Architecture:* `api: 320`, `concurrency: 11`, `import: 61`
* *Defense:* `safety: 56`, `doc: 315`, `immutability_locks: 534`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.256
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Cause.js, Channel.js, Chunk.js, Clock.js, Context.js, Deferred.js, Duration.js, Effect.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/effect/src/internal/fiberRuntime.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 2043.12 | **LOC:** 3861 | **CtrlFlow:** 18.7% | **Authorship Centralization:** 40.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **72**; blast radius 0.256; role: Isolated/Orphan
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (90.7%), Guard Balance (formerly Safety Score) (84.8%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (78.5%)
- **Documentation Coverage:** 72.043% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `allSuccesses` **(Generic / Templated Code)** (Impact: 117.7)
  * `forkWithScopeOverride` **(Generic / Templated Code)** (Impact: 92.4)
  * `withEarlyRelease` **(Generic / Templated Code)** (Impact: 85.2)
  * `allEither` **(Defensive Guards)** (Impact: 69.5)
  * `existsLoop` **(Generic / Templated Code)** (Impact: 58.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 123 instances
* *Concurrency (weighted view):* 27
* *State Mutation (weighted view):* 402
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 609`, `structural_boundaries: 1257`, `args: 621`, `func_start: 198`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 219`, `state_mutation: 156`, `dead_code: 2`, `planned_debt: 2`, `fragile_debt: 2`, `duplicate_logic: 3`
* *Architecture:* `io: 3`, `api: 140`, `concurrency: 12`, `import: 77`
* *Defense:* `safety: 53`, `doc: 96`, `immutability_locks: 203`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.256
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Array.js, Boolean.js, Cause.js, Chunk.js, Clock.js, ConfigProvider.js, Context.js, DefaultServices.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/effect/src/Graph.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 1600.28 | **LOC:** 3736 | **CtrlFlow:** 16.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.256; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (86.2%), Connectivity (formerly Api Exposure) (62.1%), Complexity Load (formerly Cognitive Load) (42.3%)
- **Documentation Coverage:** 13.253% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `escapeMermaidLabel` **(Many-Argument Workhorses)** (Impact: 503.8)
  * `removeEdgeInternal` **(Many-Argument Workhorses)** (Impact: 23.3)
  * `neighborsDirected` **(Many-Argument Workhorses)** (Impact: 21.9)
    * *Intent:* * * const nodeA = 0 * const nodeB = 1 * * // Get outgoing neighbors (nodes that nodeA points to) * c...
  * `addEdge` **(Many-Argument Workhorses)** (Impact: 21.6)
    * *Intent:* * ```ts * import { Graph } from "effect" * * const result = Graph.mutate(Graph.directed<string, numb...
  * `nodeLabel` **(Compute Cores)** (Impact: 20.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 193 instances
* *State Mutation (weighted view):* 619
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 395`, `structural_boundaries: 542`, `args: 145`, `func_start: 87`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 75`, `state_mutation: 233`
* *Architecture:* `io: 40`, `api: 88`, `import: 37`
* *Defense:* `safety: 33`, `doc: 94`, `immutability_locks: 41`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.256
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Data.js, Equal.js, Function.js, Hash.js, Inspectable.js, Option.js, Pipeable.js, Types.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/effect/src/Effect.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 1563.14 | **LOC:** 14816 | **CtrlFlow:** 15.8% | **Authorship Centralization:** 75.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **68**; blast radius 0.256; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Guard Balance (formerly Safety Score) (85.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (18.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (15.8%)
- **Documentation Coverage:** 66.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_R` **(Many-Argument Workhorses)** (Impact: 562.5)
  * `logWithLevel` **(Many-Argument Workhorses)** (Impact: 263.2)
    * *Intent:* * const program = Effect.logWithLevel( * LogLevel.Error, * "Critical error encountered", * Cause.die...
  * `transposeOption` **(Generic / Templated Code)** (Impact: 31.8)
    * *Intent:* * // ▼ * const maybe = Option.some(Effect.succeed(42)) * * // ┌─── Effect<Option<number>, never, nev...
  * `fnApply` **(Defensive Guards)** (Impact: 20.1)
  * `_R` **(Generic / Templated Code)** (Impact: 18.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 72
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 596`, `structural_boundaries: 2681`, `args: 816`, `func_start: 39`, `class_start: 28`
* *Risk/State:* `safety_bypasses: 405`, `state_mutation: 32`, `planned_debt: 3`, `duplicate_logic: 2`
* *Architecture:* `api: 389`, `concurrency: 6`, `import: 64`
* *Defense:* `safety: 49`, `doc: 409`, `sync_locks: 3`, `immutability_locks: 368`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.256
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Array.js, Cause.js, Chunk.js, Clock.js, ConfigProvider.js, Console.js, Context.js, Deferred.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/ai/anthropic/src/Generated.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1522.1 | **LOC:** 7226 | **CtrlFlow:** 14.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.256; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Guard Balance (formerly Safety Score) (28.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (22.1%), Complexity Load (formerly Cognitive Load) (5.2%)
- **Documentation Coverage:** 42.8571% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `decodeError` **(Many-Argument Workhorses)** (Impact: 845.4)
  * `default` **(I/O & Config Routines)** (Impact: 197.0)
    * *Intent:* /** * Deleted object type. * * For file deletion, this is always `"file_deleted"`. */
  * `default` **(I/O & Config Routines)** (Impact: 32.0)
    * *Intent:* /** * Deleted object type. * * For file deletion, this is always `"file_deleted"`. */
  * `default` **(I/O & Config Routines)** (Impact: 6.2)
    * *Intent:* /** * Whether there are more results available. */
  * `default` **(I/O & Config Routines)** (Impact: 6.2)
    * *Intent:* /** * Whether there are more results available. */
**Contextual Mitigations & Amplifications:**
* *Api Near Db Sink:* 1 instances
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 508`, `structural_boundaries: 1549`, `args: 294`, `func_start: 9`, `class_start: 342`
* *Risk/State:* `safety_bypasses: 40`
* *Architecture:* `api: 344`, `import: 8`
* *Defense:* `safety: 264`, `doc: 689`, `immutability_locks: 224`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.256
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` HttpClient, HttpClientError, HttpClientRequest, HttpClientResponse, Data, Effect, ParseResult, Schema
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/effect/src/Micro.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 1468.98 | **LOC:** 4406 | **CtrlFlow:** 15.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **25**; blast radius 0.256; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (85.8%), Connectivity (formerly Api Exposure) (77.8%), Mutation Surface (formerly State Flux) (75.8%), Concurrency Surface (formerly Concurrency) (27.7%)
- **Documentation Coverage:** 34.7826% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `defaultValue` **(Generic / Templated Code)** (Impact: 67.3)
  * `uninterruptibleMask` **(Generic / Templated Code)** (Impact: 56.5)
    * *Intent:* * ```ts * import * as Micro from "effect/Micro" * * Micro.uninterruptibleMask((restore) => * Micro.s...
  * `makePrimitiveProto` **(Generic / Templated Code)** (Impact: 27.2)
  * `while` **(Generic / Templated Code)** (Impact: 26.4)
  * `flip` **(Generic / Templated Code)** (Impact: 26.1)
    * *Intent:* /** * Swap the error and success types of the `Micro` effect. * */
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 87 instances
* *High Risk Execution (weighted view):* 12
* *Concurrency (weighted view):* 33
* *State Mutation (weighted view):* 296
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 376`, `structural_boundaries: 1456`, `args: 542`, `func_start: 157`, `class_start: 34`
* *Risk/State:* `safety_bypasses: 173`, `high_risk_execution: 16`, `state_mutation: 122`, `duplicate_logic: 6`
* *Architecture:* `api: 220`, `concurrency: 18`, `import: 29`
* *Defense:* `safety: 56`, `doc: 219`, `immutability_locks: 148`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.256
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Array.js, Channel.js, Context.js, Effect.js, Effectable.js, Either.js, Equal.js, Function.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/effect/src/SchemaAST.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1316.92 | **LOC:** 3048 | **CtrlFlow:** 23.2% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **68** in-repo importer(s); it depends on **15**; blast radius 5.631; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (92.7%), Debt Markers (formerly Tech Debt) (88.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (60.7%)
- **Documentation Coverage:** 15.9574% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `unify` **(Compute Cores)** (Impact: 58.2)
  * `equals` **(Compute Cores)** (Impact: 57.8)
  * `encodedAST_` **(Compute Cores)** (Impact: 46.8)
  * `pick` **(Compute Cores)** (Impact: 38.2)
    * *Intent:* /** * Equivalent at runtime to the built-in TypeScript utility type `Pick`. * */
  * `typeAST` **(Compute Cores)** (Impact: 31.0)
    * *Intent:* /** */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 59 instances
* *State Mutation (weighted view):* 181
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 420`, `structural_boundaries: 847`, `args: 269`, `func_start: 148`, `class_start: 34`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 63`, `duplicate_logic: 33`
* *Architecture:* `io: 4`, `api: 179`, `import: 30`
* *Defense:* `safety: 33`, `doc: 267`, `immutability_locks: 108`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 5.631
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.042545
  * `Imports (Out-Degree: 0):` Array.js, Effect.js, Equivalence.js, Function.js, GlobalValue.js, Inspectable.js, Number.js, Option.js...
  * `Imported By (In-Degree: 68):` (Excluded from Brief to save tokens)

### `packages/effect/src/ParseResult.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1222.72 | **LOC:** 2031 | **CtrlFlow:** 26.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **102** in-repo importer(s); it depends on **16**; blast radius 7.832; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.5%), Guard Balance (formerly Safety Score) (77.0%), Connectivity (formerly Api Exposure) (77.0%), Complexity Load (formerly Cognitive Load) (39.2%)
- **Documentation Coverage:** 55.3191% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `go` **(Many-Argument Workhorses)** (Impact: 167.7)
  * `computeResult` **(Compute Cores)** (Impact: 93.3)
    * *Intent:* // --------------------------------------------- // compute result // ------------------------------...
  * `computeResult` **(Compute Cores)** (Impact: 64.0)
    * *Intent:* // --------------------------------------------- // compute result // ------------------------------...
  * `getLiterals` **(Many-Argument Workhorses)** (Impact: 52.7)
  * `encodeUnknownPromise` **(Generic / Templated Code)** (Impact: 41.3)
    * *Intent:* /** */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 102 instances
* *State Mutation (weighted view):* 313
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 395`, `structural_boundaries: 623`, `args: 233`, `func_start: 65`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 109`, `dead_code: 1`, `planned_debt: 2`, `duplicate_logic: 2`
* *Architecture:* `io: 20`, `api: 67`, `concurrency: 6`, `import: 20`
* *Defense:* `safety: 40`, `doc: 86`, `immutability_locks: 57`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.832
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.061848
  * `Imports (Out-Degree: 0):` Array.js, Cause.js, Data.js, Effect.js, Either.js, Exit.js, Function.js, GlobalValue.js...
  * `Imported By (In-Degree: 102):` (Excluded from Brief to save tokens)

### `packages/effect/src/internal/redBlackTree.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1222.68 | **LOC:** 1246 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 0.256; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.6%), Connectivity (formerly Api Exposure) (73.3%), Complexity Load (formerly Cognitive Load) (60.6%)
- **Documentation Coverage:** 56.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fixDoubleBlack` **(Compute Cores)** (Impact: 83.9)
    * *Intent:* /** * Fix up a double black node in a Red-Black Tree. */
  * `getOrder` **(Compute Cores)** (Impact: 66.1)
  * `[Symbol.iterator]` **(Generic / Templated Code)** (Impact: 54.9)
  * `visitBetween` **(Many-Argument Workhorses)** (Impact: 28.8)
  * `visitGreaterThanEqual` **(Many-Argument Workhorses)** (Impact: 24.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 231 instances
* *State Mutation (weighted view):* 711
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 233`, `structural_boundaries: 324`, `args: 137`, `func_start: 43`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 42`, `state_mutation: 249`
* *Architecture:* `api: 42`, `import: 15`
* *Defense:* `safety: 9`, `doc: 38`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.256
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Chunk.js, Equal.js, Function.js, Hash.js, Inspectable.js, Option.js, Order.js, Ordering.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/effect/src/internal/core.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 1215.54 | **LOC:** 3167 | **CtrlFlow:** 9.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **51**; blast radius 0.256; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (94.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.4%), Mutation Surface (formerly State Flux) (24.9%)
- **Documentation Coverage:** 61.8893% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `exitInterrupt` **(Generic / Templated Code)** (Impact: 32.4)
  * `sync` **(Generic / Templated Code)** (Impact: 26.6)
  * `fiberRefUnsafeMakeRuntimeFlags` **(Generic / Templated Code)** (Impact: 23.6)
  * `fiberIdWith` **(Generic / Templated Code)** (Impact: 21.7)
  * `onSuccess` **(Generic / Templated Code)** (Impact: 19.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 35 instances
* *State Mutation (weighted view):* 137
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 244`, `structural_boundaries: 1570`, `args: 686`, `func_start: 214`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 64`, `state_mutation: 67`, `duplicate_logic: 29`, `unreferenced_by_name: 64`
* *Architecture:* `api: 276`, `concurrency: 3`, `import: 52`
* *Defense:* `safety: 24`, `doc: 145`, `immutability_locks: 109`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.256
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Array.js, Cause.js, Chunk.js, Context.js, Deferred.js, Differ.js, Duration.js, Effect.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/effect/src/internal/pubsub.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 1074.26 | **LOC:** 1763 | **CtrlFlow:** 13.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 0.256; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Debt Markers (formerly Tech Debt) (98.8%), Guard Balance (formerly Safety Score) (86.4%), Concurrency Surface (formerly Concurrency) (55.7%)
- **Documentation Coverage:** 70.3911% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `unsafeCompleteSubscribers` **(Generic / Templated Code)** (Impact: 30.5)
    * *Intent:* /** * Describes how publishers should signal to subscribers waiting for * additional values from the...
  * `unsafeStrategyCompletePollers` **(Many-Argument Workhorses)** (Impact: 23.6)
  * `unsafeOnPubSubEmptySpace` **(Compute Cores)** (Impact: 16.7)
  * `unsafeSlidingPublish` **(Compute Cores)** (Impact: 16.4)
  * `makeBoundedPubSub` **(Generic / Templated Code)** (Impact: 13.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 111 instances
* *Concurrency (weighted view):* 42
* *State Mutation (weighted view):* 377
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 193`, `structural_boundaries: 407`, `args: 233`, `func_start: 162`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 32`, `state_mutation: 155`, `duplicate_logic: 41`
* *Architecture:* `api: 23`, `concurrency: 22`, `import: 18`
* *Defense:* `safety: 1`, `doc: 53`, `immutability_locks: 42`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.256
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Chunk.js, Deferred.js, Effect.js, Effectable.js, Function.js, MutableQueue.js, MutableRef.js, Number.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/cli/src/internal/options.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 905.4 | **LOC:** 2220 | **CtrlFlow:** 15.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **40**; blast radius 0.256; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (84.9%), Guard Balance (formerly Safety Score) (58.4%), Mutation Surface (formerly State Flux) (32.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (11.5%)
- **Documentation Coverage:** 40.1408% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `onNonEmpty` **(Many-Argument Workhorses)** (Impact: 41.9)
  * `loop` **(Compute Cores)** (Impact: 37.6)
  * `makeChoice` **(Many-Argument Workhorses)** (Impact: 33.7)
  * `getZshCompletions` **(Type Conversions)** (Impact: 28.8)
  * `getHelpInternal` **(Type Conversions)** (Impact: 24.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 98
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 295`, `structural_boundaries: 674`, `args: 274`, `func_start: 97`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 56`, `planned_debt: 1`
* *Architecture:* `io: 10`, `api: 78`, `import: 40`
* *Defense:* `safety: 25`, `doc: 78`, `immutability_locks: 32`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.256
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` CliConfig.js, HelpDoc.js, Options.js, Primitive.js, Prompt.js, Usage.js, ValidationError.js, autoCorrect.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/effect/src/internal/core-effect.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 824.96 | **LOC:** 2305 | **CtrlFlow:** 9.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **40**; blast radius 0.256; role: Isolated/Orphan
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (97.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.1%), Mutation Surface (formerly State Flux) (36.6%)
- **Documentation Coverage:** 89.1892% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `unsafeMakeSpan` **(Many-Argument Workhorses)** (Impact: 49.5)
  * `endSpan` **(Generic / Templated Code)** (Impact: 37.7)
  * `serviceOptional` **(Generic / Templated Code)** (Impact: 33.8)
  * `logWithLevel` **(Generic / Templated Code)** (Impact: 32.0)
  * `predicate` **(Generic / Templated Code)** (Impact: 30.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 41 instances
* *State Mutation (weighted view):* 129
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 199`, `structural_boundaries: 1081`, `args: 491`, `func_start: 72`
* *Risk/State:* `safety_bypasses: 95`, `state_mutation: 47`
* *Architecture:* `api: 137`, `concurrency: 4`, `import: 41`
* *Defense:* `safety: 53`, `doc: 26`, `immutability_locks: 72`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.256
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Array.js, Cause.js, Chunk.js, Clock.js, Context.js, Duration.js, Effect.js, Exit.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/effect/test/TPubSub.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 791.42 | **LOC:** 903 | **CtrlFlow:** 0.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.256; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (98.5%), Guard Balance (formerly Safety Score) (47.5%), Complexity Load (formerly Cognitive Load) (5.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 349`, `args: 171`, `func_start: 17`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `concurrency: 70`, `import: 3`
* *Defense:* `test: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.256
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` vitest, utils, effect
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/ai/openrouter/src/Generated.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 762.58 | **LOC:** 6082 | **CtrlFlow:** 0.9% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.256; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (47.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (20.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `default` **(I/O & Config Routines)** (Impact: 204.6)
  * `decodeError` **(Many-Argument Workhorses)** (Impact: 91.4)
  * `default` **(I/O & Config Routines)** (Impact: 10.0)
  * `unexpectedStatus` **(Generic / Templated Code)** (Impact: 5.5)
  * `default` **(Generic / Templated Code)** (Impact: 4.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 1353`, `args: 99`, `func_start: 9`, `class_start: 351`
* *Risk/State:* `safety_bypasses: 20`
* *Architecture:* `api: 353`, `import: 8`
* *Defense:* `safety: 16`, `doc: 550`, `immutability_locks: 50`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.256
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` HttpClient, HttpClientError, HttpClientRequest, HttpClientResponse, Data, Effect, ParseResult, Schema
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/effect/src/internal/sink.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 754.62 | **LOC:** 2121 | **CtrlFlow:** 5.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **26**; blast radius 0.256; role: Isolated/Orphan
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (94.7%), Debt Markers (formerly Tech Debt) (89.8%), Guard Balance (formerly Safety Score) (50.7%), Mutation Surface (formerly State Flux) (8.7%)
- **Documentation Coverage:** 27.49% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `withDuration` **(Generic / Templated Code)** (Impact: 43.9)
  * `foldWeightedDecomposeEffectFold` **(Many-Argument Workhorses)** (Impact: 25.6)
  * `foldWeightedDecomposeFold` **(Many-Argument Workhorses)** (Impact: 23.1)
  * `indexWhere` **(Generic / Templated Code)** (Impact: 12.8)
  * `leftover` **(Generic / Templated Code)** (Impact: 12.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 45
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 108`, `structural_boundaries: 1040`, `args: 437`, `func_start: 174`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 21`, `fragile_debt: 1`, `duplicate_logic: 22`
* *Architecture:* `io: 1`, `api: 120`, `import: 27`
* *Defense:* `safety: 7`, `doc: 135`, `immutability_locks: 85`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.256
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Array.js, Cause.js, Channel.js, Chunk.js, Clock.js, Context.js, Duration.js, Effect.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/sql/src/internal/statement.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 715.7 | **LOC:** 994 | **CtrlFlow:** 17.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 0.256; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Guard Balance (formerly Safety Score) (89.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (66.1%)
- **Documentation Coverage:** 68.8073% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `compile` **(Many-Argument Workhorses)** (Impact: 120.8)
  * `placeholderNoIncrement` **(Compute Cores)** (Impact: 79.2)
  * `statement` **(Many-Argument Workhorses)** (Impact: 25.5)
  * `primitiveKind` **(Compute Cores)** (Impact: 21.2)
  * `join` **(Many-Argument Workhorses)** (Impact: 15.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 68 instances
* *State Mutation (weighted view):* 206
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 153`, `structural_boundaries: 306`, `args: 97`, `func_start: 67`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 42`, `state_mutation: 70`, `duplicate_logic: 2`
* *Architecture:* `io: 82`, `api: 34`, `import: 13`
* *Defense:* `safety: 9`, `doc: 23`, `immutability_locks: 67`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.256
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` SqlConnection.js, SqlError.js, Statement.js, Effect, Effectable, FiberRef, Function, GlobalValue...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/effect/src/internal/dateTime.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 710.22 | **LOC:** 1278 | **CtrlFlow:** 23.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **19**; blast radius 0.256; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (45.7%), Debt Markers (formerly Tech Debt) (36.7%), Mutation Surface (formerly State Flux) (12.4%), Complexity Load (formerly Cognitive Load) (12.3%)
- **Documentation Coverage:** 28.5714% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `endOfDate` **(Many-Argument Workhorses)** (Impact: 62.4)
  * `unsafeMakeZoned` **(Defensive Guards)** (Impact: 54.5)
  * `startOfDate` **(Many-Argument Workhorses)** (Impact: 42.7)
  * `calculateNamedOffset` **(Generic / Templated Code)** (Impact: 41.5)
  * `intlTimeZone` **(Defensive Guards)** (Impact: 40.8)
    * *Intent:* // ============================================================================= // formatting // ==...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 43
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 242`, `structural_boundaries: 412`, `args: 161`, `func_start: 67`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 17`, `unreferenced_by_name: 20`
* *Architecture:* `api: 81`, `import: 20`
* *Defense:* `safety: 34`, `doc: 81`, `immutability_locks: 63`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.256
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Cause.js, Clock.js, DateTime.js, Duration.js, Effect.js, Either.js, Equal.js, Equivalence.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/effect/src/internal/cause.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 703.0 | **LOC:** 1050 | **CtrlFlow:** 16.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 0.256; role: Isolated/Orphan
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.2%), Complexity Load (formerly Cognitive Load) (40.9%)
- **Documentation Coverage:** 24.7788% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parallelCase` **(Many-Argument Workhorses)** (Impact: 56.0)
  * `prettyErrorStack` **(Many-Argument Workhorses)** (Impact: 40.9)
  * `evaluateCause` **(Compute Cores)** (Impact: 29.7)
    * *Intent:* // ----------------------------------------------------------------------------- // Evaluation // --...
  * `makePrettyError` **(Compute Cores)** (Impact: 19.5)
  * `prettyErrorMessage` **(Defensive Guards)** (Impact: 14.3)
    * *Intent:* /** * A utility function for generating human-readable error messages from a generic error of type `...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 80 instances
* *State Mutation (weighted view):* 254
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 137`, `structural_boundaries: 413`, `args: 163`, `func_start: 75`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 94`, `fragile_debt: 1`
* *Architecture:* `io: 1`, `api: 55`, `import: 19`
* *Defense:* `safety: 10`, `doc: 63`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.256
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Array.js, Cause.js, Chunk.js, Either.js, Equal.js, FiberId.js, Function.js, GlobalValue.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/effect/src/internal/channel.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 689.28 | **LOC:** 2604 | **CtrlFlow:** 3.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **37**; blast radius 0.256; role: Isolated/Orphan
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (92.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (54.3%), Mutation Surface (formerly State Flux) (17.7%)
- **Documentation Coverage:** 40.8284% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `splitLinesChunk` **(Compute Cores)** (Impact: 32.7)
  * `onOtherDone` **(Generic / Templated Code)** (Impact: 31.6)
  * `onRight` **(Generic / Templated Code)** (Impact: 24.7)
  * `writeChunkWriter` **(Generic / Templated Code)** (Impact: 23.3)
  * `merge` **(Generic / Templated Code)** (Impact: 21.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 23 instances
* *State Mutation (weighted view):* 76
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 86`, `structural_boundaries: 883`, `args: 411`, `func_start: 122`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 30`, `duplicate_logic: 4`
* *Architecture:* `api: 90`, `concurrency: 11`, `import: 39`
* *Defense:* `safety: 5`, `doc: 93`, `immutability_locks: 48`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.256
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Cause.js, Channel.js, Chunk.js, Context.js, Deferred.js, Effect.js, Either.js, Equal.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/effect/src/Unify.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 663.39 | **LOC:** 114 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **1**; blast radius 0.708; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (98.1%), Connectivity (formerly Api Exposure) (77.2%), Complexity Load (formerly Cognitive Load) (4.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 90`, `args: 16`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 20`
* *Architecture:* `api: 8`, `import: 1`
* *Defense:* `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.708
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.009345
  * `Imports (Out-Degree: 0):` Function.js
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `packages/platform/src/internal/path.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 660.76 | **LOC:** 608 | **CtrlFlow:** 39.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.256; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.5%), Complexity Load (formerly Cognitive Load) (77.6%), Connectivity (formerly Api Exposure) (55.4%)
- **Documentation Coverage:** 95.8333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `normalizeStringPosix` **(Compute Cores)** (Impact: 60.7)
    * *Intent:* /** * The following functions are adapted from the Node.js source code: * https://github.com/nodejs/...
  * `relative` **(Compute Cores)** (Impact: 56.5)
  * `parse` **(Compute Cores)** (Impact: 47.7)
  * `basename` **(Compute Cores)** (Impact: 46.7)
  * `extname` **(Compute Cores)** (Impact: 26.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 101 instances
* *State Mutation (weighted view):* 303
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 192`, `structural_boundaries: 70`, `args: 15`, `func_start: 17`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 101`
* *Architecture:* `io: 62`, `api: 9`, `import: 6`
* *Defense:* `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.256
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Error.js, Path.js, Context, Effect, Function, Layer
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/ai/openai/src/OpenAiLanguageModel.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 639.48 | **LOC:** 1452 | **CtrlFlow:** 22.4% | **Authorship Centralization:** 37.5%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **24**; blast radius 0.256; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (60.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (56.2%)
- **Documentation Coverage:** 57.8947% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `catch` **(Defensive Guards)** (Impact: 135.4)
  * `getSystemMessageMode` **(Compute Cores)** (Impact: 101.7)
    * *Intent:* // ============================================================================= // Prompt Conversio...
  * `annotateStreamResponse` **(Many-Argument Workhorses)** (Impact: 51.3)
  * `catch` **(Compute Cores)** (Impact: 38.3)
  * `prepareResponseFormat` **(Defensive Guards)** (Impact: 11.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 62 instances
* *State Mutation (weighted view):* 201
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 252`, `structural_boundaries: 295`, `args: 38`, `func_start: 15`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 77`, `planned_debt: 3`, `fragile_debt: 1`
* *Architecture:* `api: 27`, `import: 25`
* *Defense:* `safety: 64`, `doc: 27`, `immutability_locks: 53`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.256
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` Generated.js, OpenAiClient.js, OpenAiTelemetry.js, OpenAiTokenizer.js, OpenAiTool.js, utilities.js, AiError, IdGenerator...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/effect/src/internal/schedule.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 598.12 | **LOC:** 2200 | **CtrlFlow:** 6.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **28**; blast radius 0.256; role: Isolated/Orphan
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Guard Balance (formerly Safety Score) (55.0%), Debt Markers (formerly Tech Debt) (23.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (14.8%)
- **Documentation Coverage:** 18.239% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `unfold` **(Generic / Templated Code)** (Impact: 23.1)
  * `collectWhileEffect` **(Generic / Templated Code)** (Impact: 20.0)
  * `intersectWithLoop` **(Many-Argument Workhorses)** (Impact: 12.3)
  * `fixed` **(Compute Cores)** (Impact: 11.7)
  * `minuteOfHour` **(Generic / Templated Code)** (Impact: 11.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 118`, `structural_boundaries: 920`, `args: 479`, `func_start: 97`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 10`, `fragile_debt: 1`, `duplicate_logic: 6`
* *Architecture:* `io: 1`, `api: 131`, `import: 29`
* *Defense:* `safety: 4`, `doc: 138`, `test: 2`, `immutability_locks: 65`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.256
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Cause.js, Chunk.js, Clock.js, Context.js, Cron.js, DateTime.js, Duration.js, Effect.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `packages/ai/anthropic/src/Generated.ts` -> **Maxwell Brown** (100.0% isolated ownership) | Magnitude: 1522.1
- `packages/effect/src/ParseResult.ts` -> **Giulio Canti** (100.0% isolated ownership) | Magnitude: 1222.72
- `packages/cli/src/internal/options.ts` -> **Cristian Velasquez Ramos** (100.0% isolated ownership) | Magnitude: 905.4
- `packages/effect/src/internal/core-effect.ts` -> **Michael Arnaldi** (100.0% isolated ownership) | Magnitude: 824.96
- `packages/sql/src/internal/statement.ts` -> **Tim** (100.0% isolated ownership) | Magnitude: 715.7

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `packages/platform/src/HttpLayerRouter.ts` -> **Severity: 0.005** (Bridge: 0.0001 * Flux: 71.7751%)
- `packages/rpc/src/RpcServer.ts` -> **Severity: 0.005** (Bridge: 0.0001 * Flux: 46.6017%)
- `packages/experimental/src/Reactivity.ts` -> **Severity: 0.004** (Bridge: 0.0 * Flux: 99.8921%)
- `packages/platform/src/Headers.ts` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 86.1381%)
- `packages/cluster/src/Sharding.ts` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 97.5933%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `packages/effect/src/Function.ts` -> **Severity: 15.111** (Embedded: 0.2406 * Error Risk: 62.8181%)
- `packages/effect/src/Schema.ts` -> **Severity: 11.812** (Embedded: 0.2028 * Error Risk: 58.2543%)
- `packages/effect/src/Context.ts` -> **Severity: 10.066** (Embedded: 0.1066 * Error Risk: 94.4538%)
- `packages/effect/src/Layer.ts` -> **Severity: 7.923** (Embedded: 0.1097 * Error Risk: 72.2158%)
- `packages/effect/src/ParseResult.ts` -> **Severity: 4.765** (Embedded: 0.0618 * Error Risk: 77.0375%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `packages/effect/src/Function.ts` -> **Severity: 3117.697** (Blast Radius: 46.518 * Doc Risk: 67.0213%)
- `packages/effect/src/Schema.ts` -> **Severity: 2360.319** (Blast Radius: 54.205 * Doc Risk: 43.5443%)
- `packages/effect/src/ParseResult.ts` -> **Severity: 433.259** (Blast Radius: 7.832 * Doc Risk: 55.3191%)
- `packages/effect/src/Stream.ts` -> **Severity: 391.0** (Blast Radius: 7.82 * Doc Risk: 50.0%)
- `packages/effect/src/Cause.ts` -> **Severity: 295.933** (Blast Radius: 4.439 * Doc Risk: 66.6667%)

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
