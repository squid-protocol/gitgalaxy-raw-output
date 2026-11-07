# ARCHITECTURAL_BRIEF: effect
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/Effect-TS/effect.git` |
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
- **Scope:** 2126 analyzed artifact(s), 340552 LOC.
- **Load-bearing artifact:** `packages/effect/src/Function.ts` -- 340 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `packages/effect/src/index.ts` -- pulls in 175 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `packages/ai/openai/src/Generated.ts` at magnitude 2229.7 (structural weight, not risk).
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
| Analyzed Artifacts (Scanned) | 2126 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 82 |
| Total LOC | 340552 |
| Volatility Index | 0.004 |
| % Scanned of codebase = | 96.3% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6103 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1689 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 20.7% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.6579 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 119 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 1768 | 336784 | 83.2% |
| JSON | 208 | 2944 | 9.8% |
| MARKDOWN | 75 | 0 | 3.5% |
| PLAINTEXT | 41 | 0 | 1.9% |
| YAML | 12 | 293 | 0.6% |
| SHELL | 11 | 132 | 0.5% |
| JAVASCRIPT | 9 | 304 | 0.4% |
| NIX | 1 | 29 | 0.0% |
| HTML | 1 | 66 | 0.0% |

## 4.1 SOURCE ENCODINGS
All 2126 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 35%, Data / Markup / Trivial 23%, Generic / Templated Code Files 13%, Large Core Modules (3) 8%, Callbacks & Closures Files 7%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 2010 | 94.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 116 | 5.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 82*

**Composition by Extension & Reason:**
- `no_extension`: 41x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 16x Unsupported Format (.undeterminable)
- `.json`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Static Asset Blob without Intent: 1003 LOC)
- `.patch`: 4x Unsupported Format (.patch), 2x Excluded (Unsupported Extension: '.patch')
- `.toml`: 2x Excluded (Unsupported Extension: '.toml')
- `.png`: 2x Excluded (Explicitly Denied Extension: '.png')
- `.ts`: 2x Excluded (Saturation: Line 4 exceeds 500 chars)
- `.yml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.lock`: 1x Excluded (Unsupported Extension: '.lock')
- `.ini`: 1x Excluded (Unsupported Extension: '.ini')
- `.gz`: 1x Excluded (Explicitly Denied Extension: '.gz')
- `.yaml`: 1x Excluded (Massive Static Asset Blob: 14139 LOC)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 77.6 | 4.7 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 95.0 | 21.6 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 5.2 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 3.8 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 24.9 | 3.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 16.6 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 9.9 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 9.7 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 19.7 | 1.5 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 96.2 | 1.5 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 25.9 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 10060 | 1441 | 12 | `packages/effect/src/index.ts` |
| cleanup | 196 | 82 | 0 | `packages/effect/src/internal/channel/subexecutor.ts` |
| guards | 20048 | 1033 | 22 | `packages/ai/openai/src/Generated.ts` |
| danger | 6940 | 572 | 6 | `packages/effect/src/Effect.ts` |
| concurrency | 19844 | 948 | 22 | `packages/effect/test/Schema/JSONSchema.new.test.ts` |
| connectivity | 19627 | 1029 | 22 | `packages/ai/openai/src/Generated.ts` |
| io | 3322 | 304 | 2 | `packages/cluster/src/SqlMessageStorage.ts` |
| crypto | 3 | 3 | 0 | `packages/platform-node-shared/src/internal/fileSystem.ts` |
| ipc | 309 | 69 | 0 | `packages/platform/src/internal/worker.ts` |
| time | 412 | 72 | 0 | `packages/effect/test/Cron.test.ts` |
| serialization | 170 | 73 | 0 | `packages/effect/src/Schema.ts` |
| regex | 621 | 187 | 0 | `packages/effect/src/internal/stream.ts` |
| events | 12777 | 1493 | 15 | `packages/effect/src/Effect.ts` |
| tests | 11832 | 728 | 7 | `packages/effect/dtslint/Schema/Schema.tst.ts` |
| docs | 24379 | 954 | 24 | `packages/ai/openai/src/Generated.ts` |
| debt | 1293 | 247 | 1 | `packages/ai/openai/src/Generated.ts` |
| mutation | 43333 | 1587 | 51 | `packages/effect/test/Graph.test.ts` |
| dead_code | 641 | 215 | 1 | `packages/effect/src/internal/core.ts` |
| credential | 1 | 1 | 0 | `packages/ai/google/scripts/generate.sh` |
| threat | 3 | 3 | 0 | `packages/ai/ai/src/IdGenerator.ts` |
| ml_ai | 334 | 93 | 0 | `packages/effect/src/internal/defaultServices.ts` |
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

1. **Function.ts** (`packages/effect/src/Function.ts`) — 340 inbound connections
2. **Schema.ts** (`packages/effect/src/Schema.ts`) — 297 inbound connections
3. **Effect.ts** (`packages/effect/src/Effect.ts`) — 274 inbound connections
4. **TestUtils.ts** (`packages/effect/test/Schema/TestUtils.ts`) — 249 inbound connections
5. **index.ts** (`packages/effect/src/index.ts`) — 223 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.ts** (`packages/effect/src/index.ts`) — 175 outbound dependencies
2. **fiberRuntime.ts** (`packages/effect/src/internal/fiberRuntime.ts`) — 72 outbound dependencies
3. **Effect.ts** (`packages/effect/src/Effect.ts`) — 63 outbound dependencies
4. **index.ts** (`packages/platform/src/index.ts`) — 60 outbound dependencies
5. **stream.ts** (`packages/effect/src/internal/stream.ts`) — 58 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `decodeError` **(Many-Argument Workhorses)** (@ `packages/ai/openai/src/Generated.ts`) -> Impact: **540.7** | LOC: 1981
- `decodeError` **(Defensive Guards)** (@ `packages/ai/anthropic/src/Generated.ts`) -> Impact: **490.9** | LOC: 639
- `go` **(Many-Argument Workhorses)** (@ `packages/effect/src/JSONSchema.ts`) -> Impact: **340.5** | LOC: 362
- `go` **(Many-Argument Workhorses)** (@ `packages/effect/src/ParseResult.ts`) -> Impact: **162.5** | LOC: 306
- `go` **(Compute Cores)** (@ `packages/effect/src/Schema.ts`) -> Impact: **130.2** | LOC: 179
- `valuesOf` **(Callbacks & Closures)** (@ `packages/effect/test/TArray.test.ts`) -> Impact: **124.6** | LOC: 1022
- `intersectUnionMembers` **(Many-Argument Workhorses)** (@ `packages/effect/src/Schema.ts`) -> Impact: **117.0** | LOC: 140
- `compile` **(Many-Argument Workhorses)** (@ `packages/sql/src/internal/statement.ts`) -> Impact: **116.8** | LOC: 217
- `decodeError` **(Many-Argument Workhorses)** (@ `packages/ai/google/src/Generated.ts`) -> Impact: **110.1** | LOC: 678
- `escapeMermaidLabel` **(Many-Argument Workhorses)** (@ `packages/effect/src/Graph.ts`) -> Impact: **103.5** | LOC: 2014

*Function archetypes referenced above:*
  * **Callbacks & Closures**: built around closures/callbacks (handlers, async continuations)
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `packages/effect/src` | 177 | 19635.42 | 6.64% | 5.71% |
| `packages/effect/src/internal` | 82 | 16682.32 | 12.43% | 21.67% |
| `packages/effect/test` | 103 | 4866.18 | 2.42% | 0.0% |
| `packages/platform/src` | 61 | 4297.82 | 6.47% | 3.89% |
| `packages/platform/src/internal` | 29 | 3091.44 | 10.95% | 11.64% |
| `packages/ai/openai/src` | 9 | 2863.92 | 6.51% | 11.1% |
| `packages/cli/src/internal` | 16 | 2723.86 | 11.51% | 2.0% |
| `packages/cluster/src` | 39 | 2349.34 | 6.12% | 1.36% |
| `packages/effect/src/internal/stm` | 21 | 2014.32 | 7.83% | 20.37% |
| `packages/experimental/src` | 18 | 1694.6 | 10.32% | 7.36% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `packages/effect/src/internal/effectable.ts` -> **100.0%** Exposure
- `packages/experimental/test/PersistedCache.test.ts` -> **100.0%** Exposure
- `packages/effect/src/internal/supervisor.ts` -> **99.9999%** Exposure
- `packages/effect/dtslint/Match.tst.ts` -> **99.9981%** Exposure
- `packages/cli/src/internal/helpDoc/span.ts` -> **99.9978%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `packages/cli/src/internal/autoCorrect.ts` -> **100.0%** Exposure
- `packages/effect/src/HashRing.ts` -> **100.0%** Exposure
- `packages/effect/src/internal/hashMap/array.ts` -> **100.0%** Exposure
- `packages/effect/src/internal/redBlackTree.ts` -> **100.0%** Exposure
- `packages/effect/src/internal/schedule/intervals.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `packages/ai/openai/src/Generated.ts` -> **0** Orphaned Functions | **108** Duplicates
- `packages/effect/src/internal/core.ts` -> **63** Orphaned Functions | **38** Duplicates
- `packages/effect/src/Schema.ts` -> **43** Orphaned Functions | **32** Duplicates
- `packages/effect/src/internal/stream.ts` -> **0** Orphaned Functions | **71** Duplicates
- `packages/effect/src/internal/pubsub.ts` -> **0** Orphaned Functions | **41** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `7306` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `packages/ai/openai/src/Generated.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 9.687)
- **Top Global Matches:** file_cluster_5: 9.687, file_cluster_12: 10.976, file_cluster_0: 11.367
- **Magnitude:** 2229.7 | **LOC:** 22476 | **CtrlFlow:** 5.1% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **8**; blast radius 0.539; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Debt Markers (formerly Tech Debt) (53.5%), Guard Balance (formerly Safety Score) (48.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (33.7%)
- **Documentation Coverage:** 37.9032% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `decodeError` **(Many-Argument Workhorses)** (Impact: 540.7)
  * `make` **(Generic / Templated Code)** (Impact: 3.8)
  * `unexpectedStatus` **(Callbacks & Closures)** (Impact: 3.5)
  * `ClientError` **(Generic / Templated Code)** (Impact: 2.5)
  * `default` **(Callbacks & Closures)** (Impact: 2.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 526`, `structural_boundaries: 4831`, `args: 816`, `func_start: 34`, `class_start: 1239`
* *Risk/State:* `safety_bypasses: 266`, `high_risk_execution: 6`, `duplicate_logic: 108`
* *Architecture:* `io: 8`, `api: 1241`, `import: 8`
* *Defense:* `safety: 254`, `doc: 3300`, `immutability_locks: 578`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.539
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002353
  * `Imports (Out-Degree: 0):` HttpClient, HttpClientError, HttpClientRequest, HttpClientResponse, Data, Effect, ParseResult, Schema
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `packages/effect/src/internal/stream.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.628)
- **Top Global Matches:** file_cluster_0: 8.628, file_cluster_5: 10.773, file_cluster_12: 11.938
- **Magnitude:** 1947.14 | **LOC:** 8803 | **CtrlFlow:** 8.2% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **58**; blast radius 0.282; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Debt Markers (formerly Tech Debt) (68.9%), Guard Balance (formerly Safety Score) (51.5%), Concurrency Surface (formerly Concurrency) (15.5%)
- **Documentation Coverage:** 59.8077% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `consumer` **(Compute Cores)** (Impact: 29.0)
  * `queueFromBufferOptionsPush` **(Defensive Guards)** (Impact: 24.8)
  * `queueFromBufferOptions` **(Defensive Guards)** (Impact: 23.6)
  * `groupAdjacentByChunk` **(Many-Argument Workhorses)** (Impact: 21.9)
  * `onSuccess` **(Compute Cores)** (Impact: 20.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 77 instances
* *Concurrency (weighted view):* 31
* *State Mutation (weighted view):* 266
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 663`, `structural_boundaries: 3599`, `args: 1759`, `func_start: 422`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 53`, `state_mutation: 112`, `planned_debt: 1`, `duplicate_logic: 71`
* *Architecture:* `api: 317`, `concurrency: 11`, `import: 61`
* *Defense:* `safety: 56`, `doc: 315`, `immutability_locks: 534`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.282
  * `Choke Point (Betweenness):` 0.003406 | `Ripple Effect (Closeness):` 0.126
  * `Imports (Out-Degree: 58):` Cause.js, Channel.js, Chunk.js, Clock.js, Context.js, Deferred.js, Duration.js, Effect.js...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `packages/effect/src/internal/fiberRuntime.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.598)
- **Top Global Matches:** file_cluster_5: 7.598, file_cluster_12: 10.636, file_cluster_7: 11.499
- **Magnitude:** 1457.32 | **LOC:** 3861 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 40.0%
- **Blast Radius:** changing it is visible to **34** in-repo importer(s); it depends on **72**; blast radius 1.852; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (90.4%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (78.1%), Guard Balance (formerly Safety Score) (63.9%)
- **Documentation Coverage:** 72.5632% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `allValidate` **(Defensive Guards)** (Impact: 42.5)
  * `allEither` **(Defensive Guards)** (Impact: 35.9)
  * `runLoop` **(Compute Cores)** (Impact: 30.5)
    * *Intent:* /** * The main run-loop for evaluating effects. * * **NOTE**: This method must be invoked by the fib...
  * `[OpCodes.OP_FAILURE]` **(Compute Cores)** (Impact: 27.3)
  * `evaluateEffect` **(Defensive Guards)** (Impact: 23.6)
    * *Intent:* /** * Evaluates an effect until completion, potentially asynchronously. * * **NOTE**: This method mu...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 122 instances
* *Concurrency (weighted view):* 27
* *State Mutation (weighted view):* 400
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 605`, `structural_boundaries: 1257`, `args: 621`, `func_start: 198`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 219`, `state_mutation: 156`, `planned_debt: 2`, `fragile_debt: 2`, `duplicate_logic: 3`
* *Architecture:* `io: 3`, `api: 138`, `concurrency: 12`, `import: 77`
* *Defense:* `safety: 53`, `doc: 96`, `immutability_locks: 203`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.852
  * `Choke Point (Betweenness):` 0.005761 | `Ripple Effect (Closeness):` 0.168629
  * `Imports (Out-Degree: 72):` Array.js, Boolean.js, Cause.js, Chunk.js, Clock.js, ConfigProvider.js, Context.js, DefaultServices.js...
  * `Imported By (In-Degree: 34):` (Excluded from Brief to save tokens)

### `packages/effect/src/SchemaAST.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.105)
- **Top Global Matches:** file_cluster_4: 9.105, file_cluster_12: 9.654, file_cluster_5: 10.209
- **Magnitude:** 1258.92 | **LOC:** 3048 | **CtrlFlow:** 22.7% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **52** in-repo importer(s); it depends on **15**; blast radius 6.742; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (92.6%), Debt Markers (formerly Tech Debt) (88.7%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (60.0%)
- **Documentation Coverage:** 15.847% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `unify` **(Compute Cores)** (Impact: 57.9)
  * `equals` **(Compute Cores)** (Impact: 53.6)
  * `encodedAST_` **(Compute Cores)** (Impact: 46.5)
  * `pick` **(Compute Cores)** (Impact: 37.8)
    * *Intent:* /** * Equivalent at runtime to the built-in TypeScript utility type `Pick`. * */
  * `typeAST` **(Compute Cores)** (Impact: 31.0)
    * *Intent:* /** */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 59 instances
* *State Mutation (weighted view):* 181
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 411`, `structural_boundaries: 847`, `args: 269`, `func_start: 148`, `class_start: 34`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 63`, `duplicate_logic: 33`
* *Architecture:* `io: 4`, `api: 178`, `import: 30`
* *Defense:* `safety: 33`, `doc: 267`, `immutability_locks: 108`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.742
  * `Choke Point (Betweenness):` 0.001591 | `Ripple Effect (Closeness):` 0.149308
  * `Imports (Out-Degree: 15):` Array.js, Effect.js, Equivalence.js, Function.js, GlobalValue.js, Inspectable.js, Number.js, Option.js...
  * `Imported By (In-Degree: 52):` (Excluded from Brief to save tokens)

### `packages/effect/src/Micro.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.516)
- **Top Global Matches:** file_cluster_5: 8.516, file_cluster_12: 12.237, file_cluster_7: 13.074
- **Magnitude:** 1250.08 | **LOC:** 4406 | **CtrlFlow:** 14.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **23**; blast radius 0.7; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (77.8%), Mutation Surface (formerly State Flux) (75.8%), Guard Balance (formerly Safety Score) (66.9%), Concurrency Surface (formerly Concurrency) (27.7%)
- **Documentation Coverage:** 35.3712% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `uninterruptibleMask` **(Generic / Templated Code)** (Impact: 40.6)
    * *Intent:* * ```ts * import * as Micro from "effect/Micro" * * Micro.uninterruptibleMask((restore) => * Micro.s...
  * `flip` **(Generic / Templated Code)** (Impact: 26.1)
    * *Intent:* /** * Swap the error and success types of the `Micro` effect. * */
  * `either` **(Generic / Templated Code)** (Impact: 24.4)
    * *Intent:* /** * Replace the success value of the given `Micro` effect with an `Either`, * wrapping the success...
  * `runFork` **(Defensive Guards)** (Impact: 18.1)
    * *Intent:* * const handle = Micro.succeed(42).pipe( * Micro.delay(1000), * Micro.runFork * ) * * handle.addObse...
  * `eval` **(Defensive Guards)** (Impact: 17.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 87 instances
* *High Risk Execution (weighted view):* 12
* *Concurrency (weighted view):* 33
* *State Mutation (weighted view):* 296
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 366`, `structural_boundaries: 1456`, `args: 542`, `func_start: 157`, `class_start: 34`
* *Risk/State:* `safety_bypasses: 173`, `high_risk_execution: 16`, `state_mutation: 122`, `duplicate_logic: 8`
* *Architecture:* `api: 220`, `concurrency: 18`, `import: 29`
* *Defense:* `safety: 56`, `doc: 219`, `immutability_locks: 148`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.7
  * `Choke Point (Betweenness):` 0.000257 | `Ripple Effect (Closeness):` 0.148447
  * `Imports (Out-Degree: 23):` Array.js, Channel.js, Context.js, Effect.js, Effectable.js, Either.js, Equal.js, Function.js...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `packages/effect/src/internal/redBlackTree.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.691)
- **Top Global Matches:** file_cluster_5: 7.691, file_cluster_12: 10.052, file_cluster_0: 11.077
- **Magnitude:** 1070.48 | **LOC:** 1246 | **CtrlFlow:** 20.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **14**; blast radius 0.225; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.3%), Connectivity (formerly Api Exposure) (73.3%), Complexity Load (formerly Cognitive Load) (60.6%)
- **Documentation Coverage:** 56.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fixDoubleBlack` **(Compute Cores)** (Impact: 83.9)
    * *Intent:* /** * Fix up a double black node in a Red-Black Tree. */
  * `visitBetween` **(Many-Argument Workhorses)** (Impact: 28.6)
  * `visitGreaterThanEqual` **(Generic / Templated Code)** (Impact: 24.0)
  * `visitLessThan` **(Generic / Templated Code)** (Impact: 19.2)
  * `[Equal.symbol]` **(Defensive Guards)** (Impact: 14.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 231 instances
* *State Mutation (weighted view):* 711
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 230`, `structural_boundaries: 324`, `args: 137`, `func_start: 43`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 42`, `state_mutation: 249`
* *Architecture:* `api: 42`, `import: 15`
* *Defense:* `safety: 9`, `doc: 38`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.225
  * `Choke Point (Betweenness):` 0.00023 | `Ripple Effect (Closeness):` 0.105008
  * `Imports (Out-Degree: 14):` Chunk.js, Equal.js, Function.js, Hash.js, Inspectable.js, Option.js, Order.js, Ordering.js...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/effect/src/internal/pubsub.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.275)
- **Top Global Matches:** file_cluster_5: 7.275, file_cluster_0: 8.896, file_cluster_12: 8.917
- **Magnitude:** 1070.46 | **LOC:** 1763 | **CtrlFlow:** 13.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **17**; blast radius 0.232; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Debt Markers (formerly Tech Debt) (98.8%), Guard Balance (formerly Safety Score) (64.9%), Concurrency Surface (formerly Concurrency) (55.7%)
- **Documentation Coverage:** 70.3911% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `unsafeCompleteSubscribers` **(Generic / Templated Code)** (Impact: 30.5)
    * *Intent:* /** * Describes how publishers should signal to subscribers waiting for * additional values from the...
  * `unsafeStrategyCompletePollers` **(Many-Argument Workhorses)** (Impact: 23.4)
  * `unsafeOnPubSubEmptySpace` **(Compute Cores)** (Impact: 16.7)
  * `unsafeSlidingPublish` **(Compute Cores)** (Impact: 16.4)
  * `makeBoundedPubSub` **(Generic / Templated Code)** (Impact: 13.6)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.232
  * `Choke Point (Betweenness):` 1.3e-05 | `Ripple Effect (Closeness):` 0.109761
  * `Imports (Out-Degree: 17):` Chunk.js, Deferred.js, Effect.js, Effectable.js, Function.js, MutableQueue.js, MutableRef.js, Number.js...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/effect/src/internal/core.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.606)
- **Top Global Matches:** file_cluster_5: 8.606, file_cluster_0: 10.161, file_cluster_12: 11.282
- **Magnitude:** 972.84 | **LOC:** 3167 | **CtrlFlow:** 9.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **66** in-repo importer(s); it depends on **51**; blast radius 3.985; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (97.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (54.8%), Mutation Surface (formerly State Flux) (23.7%)
- **Documentation Coverage:** 67.4267% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fiberRefUnsafeMake` **(Defensive Guards)** (Impact: 12.9)
  * `asVoid` **(Generic / Templated Code)** (Impact: 10.9)
  * `exitCollectAll` **(Generic / Templated Code)** (Impact: 9.2)
  * `yieldNow` **(Defensive Guards)** (Impact: 7.5)
  * `fiberRefUnsafeMakeRuntimeFlags` **(Generic / Templated Code)** (Impact: 7.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 33 instances
* *State Mutation (weighted view):* 133
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 240`, `structural_boundaries: 1570`, `args: 686`, `func_start: 211`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 64`, `state_mutation: 67`, `duplicate_logic: 38`, `unreferenced_by_name: 63`
* *Architecture:* `api: 276`, `concurrency: 3`, `import: 52`
* *Defense:* `safety: 24`, `doc: 145`, `immutability_locks: 109`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.985
  * `Choke Point (Betweenness):` 0.00368 | `Ripple Effect (Closeness):` 0.172612
  * `Imports (Out-Degree: 51):` Array.js, Cause.js, Chunk.js, Context.js, Deferred.js, Differ.js, Duration.js, Effect.js...
  * `Imported By (In-Degree: 66):` (Excluded from Brief to save tokens)

### `packages/effect/src/ParseResult.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 9.861)
- **Top Global Matches:** file_cluster_5: 9.861, file_cluster_4: 10.397, file_cluster_12: 10.426
- **Magnitude:** 942.32 | **LOC:** 2031 | **CtrlFlow:** 26.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **62** in-repo importer(s); it depends on **16**; blast radius 4.004; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.5%), Connectivity (formerly Api Exposure) (77.0%), Guard Balance (formerly Safety Score) (59.9%), Complexity Load (formerly Cognitive Load) (38.7%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `go` **(Many-Argument Workhorses)** (Impact: 162.5)
  * `getArrayFormatterIssues` **(Compute Cores)** (Impact: 36.1)
  * `getLiterals` **(Compute Cores)** (Impact: 33.3)
  * `formatTree` **(Callbacks & Closures)** (Impact: 22.0)
  * `handleForbidden` **(Many-Argument Workhorses)** (Impact: 17.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 102 instances
* *State Mutation (weighted view):* 313
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 384`, `structural_boundaries: 623`, `args: 233`, `func_start: 65`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 109`, `planned_debt: 2`, `duplicate_logic: 2`
* *Architecture:* `io: 20`, `api: 67`, `concurrency: 6`, `import: 20`
* *Defense:* `safety: 40`, `doc: 86`, `immutability_locks: 57`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.004
  * `Choke Point (Betweenness):` 0.000924 | `Ripple Effect (Closeness):` 0.148774
  * `Imports (Out-Degree: 16):` Array.js, Cause.js, Data.js, Effect.js, Either.js, Exit.js, Function.js, GlobalValue.js...
  * `Imported By (In-Degree: 62):` (Excluded from Brief to save tokens)

### `packages/ai/anthropic/src/Generated.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 10.985)
- **Top Global Matches:** file_cluster_4: 10.985, file_cluster_0: 12.86, file_cluster_5: 13.284
- **Magnitude:** 928.2 | **LOC:** 7226 | **CtrlFlow:** 10.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **8**; blast radius 0.462; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Guard Balance (formerly Safety Score) (42.3%), Debt Markers (formerly Tech Debt) (11.2%), Complexity Load (formerly Cognitive Load) (4.2%)
- **Documentation Coverage:** 42.8571% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `decodeError` **(Defensive Guards)** (Impact: 490.9)
  * `make` **(Generic / Templated Code)** (Impact: 3.8)
  * `unexpectedStatus` **(Callbacks & Closures)** (Impact: 3.5)
  * `ClientError` **(Generic / Templated Code)** (Impact: 2.5)
  * `default` **(Callbacks & Closures)** (Impact: 2.0)
    * *Intent:* /** * Whether the file can be downloaded. */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 367`, `structural_boundaries: 1549`, `args: 294`, `func_start: 9`, `class_start: 342`
* *Risk/State:* `safety_bypasses: 40`, `duplicate_logic: 6`
* *Architecture:* `api: 344`, `import: 8`
* *Defense:* `safety: 264`, `doc: 689`, `immutability_locks: 224`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.462
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001882
  * `Imports (Out-Degree: 0):` HttpClient, HttpClientError, HttpClientRequest, HttpClientResponse, Data, Effect, ParseResult, Schema
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `packages/effect/src/Graph.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.154)
- **Top Global Matches:** file_cluster_5: 6.154, file_cluster_12: 8.133, file_cluster_0: 9.188
- **Magnitude:** 871.28 | **LOC:** 3736 | **CtrlFlow:** 4.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **9**; blast radius 0.26; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (95.0%), Connectivity (formerly Api Exposure) (62.1%), Guard Balance (formerly Safety Score) (59.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (11.1%)
- **Documentation Coverage:** 15.8537% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `escapeMermaidLabel` **(Many-Argument Workhorses)** (Impact: 103.5)
  * `removeEdgeInternal` **(Compute Cores)** (Impact: 21.7)
  * `[Equal.symbol]` **(Compute Cores)** (Impact: 20.7)
  * `addEdge` **(Many-Argument Workhorses)** (Impact: 20.5)
    * *Intent:* * ```ts * import { Graph } from "effect" * * const result = Graph.mutate(Graph.directed<string, numb...
  * `removeNode` **(Compute Cores)** (Impact: 14.2)
    * *Intent:* * * const result = Graph.mutate(Graph.directed<string, number>(), (mutable) => { * const nodeA = Gra...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 59 instances
* *State Mutation (weighted view):* 351
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 111`, `structural_boundaries: 542`, `args: 145`, `func_start: 84`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 75`, `state_mutation: 233`
* *Architecture:* `io: 40`, `api: 88`, `import: 37`
* *Defense:* `safety: 33`, `doc: 94`, `immutability_locks: 41`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.26
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.080127
  * `Imports (Out-Degree: 14):` Data.js, Equal.js, Function.js, Hash.js, Inspectable.js, Option.js, Pipeable.js, Types.js...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/effect/test/TPubSub.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.608)
- **Top Global Matches:** file_cluster_10: 4.608, file_cluster_2: 6.301, file_cluster_13: 6.989
- **Magnitude:** 791.42 | **LOC:** 903 | **CtrlFlow:** 0.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.152; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (98.5%), Guard Balance (formerly Safety Score) (49.1%), Complexity Load (formerly Cognitive Load) (5.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 349`, `args: 171`, `func_start: 17`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `concurrency: 70`, `import: 3`
* *Defense:* `test: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.152
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` vitest, utils, effect
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/cli/src/internal/options.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.439)
- **Top Global Matches:** file_cluster_0: 8.439, file_cluster_5: 8.617, file_cluster_12: 9.096
- **Magnitude:** 730.9 | **LOC:** 2220 | **CtrlFlow:** 14.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **40**; blast radius 0.301; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (84.9%), Guard Balance (formerly Safety Score) (52.8%), Mutation Surface (formerly State Flux) (33.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (11.5%)
- **Documentation Coverage:** 41.1348% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getZshCompletions` **(Type Conversions)** (Impact: 28.8)
  * `getHelpInternal` **(Type Conversions)** (Impact: 24.9)
  * `modifySingle` **(Type Conversions)** (Impact: 21.1)
  * `getFishCompletions` **(Type Conversions)** (Impact: 20.5)
  * `getUsageInternal` **(Type Conversions)** (Impact: 19.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 100
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 276`, `structural_boundaries: 674`, `args: 274`, `func_start: 97`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 56`, `planned_debt: 1`
* *Architecture:* `io: 10`, `api: 78`, `import: 40`
* *Defense:* `safety: 25`, `doc: 78`, `immutability_locks: 32`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.301
  * `Choke Point (Betweenness):` 2.3e-05 | `Ripple Effect (Closeness):` 0.005882
  * `Imports (Out-Degree: 19):` CliConfig.js, HelpDoc.js, Options.js, Primitive.js, Prompt.js, Usage.js, ValidationError.js, autoCorrect.js...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `packages/sql/src/internal/statement.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.545)
- **Top Global Matches:** file_cluster_5: 7.545, file_cluster_12: 9.191, file_cluster_7: 10.892
- **Magnitude:** 727.5 | **LOC:** 994 | **CtrlFlow:** 16.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **13**; blast radius 0.291; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (66.6%), Connectivity (formerly Api Exposure) (65.5%)
- **Documentation Coverage:** 69.0909% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `compile` **(Many-Argument Workhorses)** (Impact: 116.8)
  * `placeholderNoIncrement` **(Compute Cores)** (Impact: 77.8)
  * `statement` **(Many-Argument Workhorses)** (Impact: 25.3)
  * `primitiveKind` **(Compute Cores)** (Impact: 21.1)
  * `extractPrimitive` **(Many-Argument Workhorses)** (Impact: 19.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 68 instances
* *State Mutation (weighted view):* 206
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 147`, `structural_boundaries: 306`, `args: 97`, `func_start: 66`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 42`, `state_mutation: 70`, `duplicate_logic: 2`
* *Architecture:* `io: 82`, `api: 33`, `import: 13`
* *Defense:* `safety: 9`, `doc: 23`, `immutability_locks: 67`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.291
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002406
  * `Imports (Out-Degree: 3):` SqlConnection.js, SqlError.js, Statement.js, Effect, Effectable, FiberRef, Function, GlobalValue...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/effect/src/Effect.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 9.111)
- **Top Global Matches:** file_cluster_5: 9.111, file_cluster_7: 13.416, file_cluster_12: 13.559
- **Magnitude:** 671.74 | **LOC:** 14816 | **CtrlFlow:** 15.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **274** in-repo importer(s); it depends on **63**; blast radius 11.815; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Guard Balance (formerly Safety Score) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (18.1%), Debt Markers (formerly Tech Debt) (13.7%)
- **Documentation Coverage:** 68.9655% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fnApply` **(Defensive Guards)** (Impact: 20.1)
  * `get` **(Many-Argument Workhorses)** (Impact: 9.5)
  * `TagClass` **(I/O & Config Routines)** (Impact: 8.9)
  * `fn` **(Compute Cores)** (Impact: 8.0)
    * *Intent:* * (effect, n) => Effect.delay(effect, `${n / 100} seconds`) * ) * * Effect.runFork(myfunc(100).pipe(...
  * `next` **(Generic / Templated Code)** (Impact: 6.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 72
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 584`, `structural_boundaries: 2681`, `args: 816`, `func_start: 39`, `class_start: 28`
* *Risk/State:* `safety_bypasses: 405`, `state_mutation: 32`, `planned_debt: 3`, `duplicate_logic: 6`
* *Architecture:* `api: 389`, `concurrency: 6`, `import: 64`
* *Defense:* `safety: 49`, `doc: 409`, `sync_locks: 3`, `immutability_locks: 368`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 11.815
  * `Choke Point (Betweenness):` 0.020336 | `Ripple Effect (Closeness):` 0.232699
  * `Imports (Out-Degree: 63):` Array.js, Cause.js, Chunk.js, Clock.js, ConfigProvider.js, Console.js, Context.js, Deferred.js...
  * `Imported By (In-Degree: 274):` (Excluded from Brief to save tokens)

### `packages/effect/src/Unify.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Centroid distance: 11.087)
- **Top Global Matches:** file_cluster_14: 11.087, file_cluster_5: 11.278, file_cluster_7: 13.027
- **Magnitude:** 663.39 | **LOC:** 114 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **31** in-repo importer(s); it depends on **1**; blast radius 3.674; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (80.0%), Connectivity (formerly Api Exposure) (77.2%), Complexity Load (formerly Cognitive Load) (4.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 90`, `args: 16`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 20`
* *Architecture:* `api: 8`, `import: 1`
* *Defense:* `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 3.674
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.18728
  * `Imports (Out-Degree: 1):` Function.js
  * `Imported By (In-Degree: 31):` (Excluded from Brief to save tokens)

### `packages/platform/src/internal/path.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 11.449)
- **Top Global Matches:** file_cluster_8: 11.449, file_cluster_3: 13.45, file_cluster_6: 23.831
- **Magnitude:** 660.76 | **LOC:** 608 | **CtrlFlow:** 39.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **6**; blast radius 0.613; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (77.6%), Guard Balance (formerly Safety Score) (77.1%), Connectivity (formerly Api Exposure) (55.4%)
- **Documentation Coverage:** 95.8333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `normalizeStringPosix` **(Compute Cores)** (Impact: 60.7)
    * *Intent:* /** * The following functions are adapted from the Node.js source code: * https://github.com/nodejs/...
  * `relative` **(Many-Argument Workhorses)** (Impact: 56.5)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.613
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00827
  * `Imports (Out-Degree: 2):` Error.js, Path.js, Context, Effect, Function, Layer
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/effect/src/internal/sink.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.57)
- **Top Global Matches:** file_cluster_0: 7.57, file_cluster_10: 11.406, file_cluster_15: 11.732
- **Magnitude:** 648.62 | **LOC:** 2121 | **CtrlFlow:** 5.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **26**; blast radius 0.25; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (97.3%), Connectivity (formerly Api Exposure) (94.7%), Guard Balance (formerly Safety Score) (50.2%), Mutation Surface (formerly State Flux) (8.7%)
- **Documentation Coverage:** 29.8805% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `foldWeightedDecomposeEffectFold` **(Many-Argument Workhorses)** (Impact: 24.8)
  * `foldWeightedDecomposeFold` **(Many-Argument Workhorses)** (Impact: 22.9)
  * `indexWhere` **(Generic / Templated Code)** (Impact: 12.7)
  * `fromQueue` **(Generic / Templated Code)** (Impact: 9.5)
  * `foldChunkSplitEffectInternal` **(Generic / Templated Code)** (Impact: 8.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 45
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 106`, `structural_boundaries: 1040`, `args: 437`, `func_start: 174`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 21`, `fragile_debt: 1`, `duplicate_logic: 29`
* *Architecture:* `io: 1`, `api: 120`, `import: 27`
* *Defense:* `safety: 7`, `doc: 135`, `immutability_locks: 85`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.25
  * `Choke Point (Betweenness):` 0.00016 | `Ripple Effect (Closeness):` 0.124952
  * `Imports (Out-Degree: 26):` Array.js, Cause.js, Channel.js, Chunk.js, Clock.js, Context.js, Duration.js, Effect.js...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `packages/effect/src/internal/cause.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.814)
- **Top Global Matches:** file_cluster_0: 8.814, file_cluster_5: 8.823, file_cluster_12: 10.284
- **Magnitude:** 634.1 | **LOC:** 1050 | **CtrlFlow:** 16.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **18**; blast radius 1.057; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (64.8%), Complexity Load (formerly Cognitive Load) (41.1%)
- **Documentation Coverage:** 29.2035% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `prettyErrorStack` **(Many-Argument Workhorses)** (Impact: 38.6)
  * `evaluateCause` **(Compute Cores)** (Impact: 29.2)
    * *Intent:* // ----------------------------------------------------------------------------- // Evaluation // --...
  * `makePrettyError` **(Compute Cores)** (Impact: 18.8)
  * `prettyErrorMessage` **(Defensive Guards)** (Impact: 14.0)
    * *Intent:* /** * A utility function for generating human-readable error messages from a generic error of type `...
  * `pretty` **(Defensive Guards)** (Impact: 12.8)
    * *Intent:* // ----------------------------------------------------------------------------- // Pretty Printing ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 81 instances
* *State Mutation (weighted view):* 256
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 137`, `structural_boundaries: 413`, `args: 163`, `func_start: 74`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 94`, `fragile_debt: 1`
* *Architecture:* `io: 1`, `api: 55`, `import: 19`
* *Defense:* `safety: 10`, `doc: 63`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.057
  * `Choke Point (Betweenness):` 0.000365 | `Ripple Effect (Closeness):` 0.180625
  * `Imports (Out-Degree: 18):` Array.js, Cause.js, Chunk.js, Either.js, Equal.js, FiberId.js, Function.js, GlobalValue.js...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `packages/effect/src/internal/core-effect.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.921)
- **Top Global Matches:** file_cluster_5: 7.921, file_cluster_12: 11.618, file_cluster_0: 11.888
- **Magnitude:** 595.06 | **LOC:** 2305 | **CtrlFlow:** 9.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **16** in-repo importer(s); it depends on **40**; blast radius 0.5; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (97.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (57.4%), Mutation Surface (formerly State Flux) (36.6%)
- **Documentation Coverage:** 88.9908% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `unsafeMakeSpan` **(Many-Argument Workhorses)** (Impact: 39.3)
  * `diffFiberRefsAndRuntimeFlags` **(Generic / Templated Code)** (Impact: 23.1)
  * `serviceOptional` **(Generic / Templated Code)** (Impact: 12.4)
  * `endSpan` **(Generic / Templated Code)** (Impact: 12.2)
  * `logWithLevel` **(Compute Cores)** (Impact: 11.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 41 instances
* *State Mutation (weighted view):* 129
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 190`, `structural_boundaries: 1081`, `args: 491`, `func_start: 72`
* *Risk/State:* `safety_bypasses: 95`, `state_mutation: 47`
* *Architecture:* `api: 137`, `concurrency: 4`, `import: 41`
* *Defense:* `safety: 53`, `doc: 26`, `immutability_locks: 72`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.5
  * `Choke Point (Betweenness):` 0.00028 | `Ripple Effect (Closeness):` 0.160377
  * `Imports (Out-Degree: 40):` Array.js, Cause.js, Chunk.js, Clock.js, Context.js, Duration.js, Effect.js, Exit.js...
  * `Imported By (In-Degree: 16):` (Excluded from Brief to save tokens)

### `packages/effect/src/internal/channel/channelExecutor.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.642)
- **Top Global Matches:** file_cluster_0: 8.642, file_cluster_15: 9.521, file_cluster_10: 9.616
- **Magnitude:** 545.68 | **LOC:** 1201 | **CtrlFlow:** 11.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **25**; blast radius 0.219; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (67.8%), Guard Balance (formerly Safety Score) (59.7%)
- **Documentation Coverage:** 94.8276% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run` **(Callbacks & Closures)** (Impact: 52.0)
  * `performPullFromUpstream` **(Compute Cores)** (Impact: 17.9)
  * `applyUpstreamPullStrategy` **(Generic / Templated Code)** (Impact: 16.8)
  * `finishWithDoneValue` **(Many-Argument Workhorses)** (Impact: 16.6)
  * `pullFromChild` **(Many-Argument Workhorses)** (Impact: 15.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 59 instances
* *State Mutation (weighted view):* 214
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 121`, `structural_boundaries: 453`, `args: 144`, `func_start: 54`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 96`, `planned_debt: 1`, `duplicate_logic: 9`
* *Architecture:* `api: 10`, `concurrency: 4`, `import: 25`
* *Defense:* `safety: 6`, `doc: 7`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.219
  * `Choke Point (Betweenness):` 0.000715 | `Ripple Effect (Closeness):` 0.101291
  * `Imports (Out-Degree: 25):` Cause.js, Channel.js, ChildExecutorDecision.js, Context.js, Deferred.js, Effect.js, ExecutionStrategy.js, Exit.js...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `packages/effect/src/internal/channel.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.613)
- **Top Global Matches:** file_cluster_0: 8.613, file_cluster_10: 11.783, file_cluster_5: 11.794
- **Magnitude:** 538.88 | **LOC:** 2604 | **CtrlFlow:** 3.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **37**; blast radius 0.211; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (92.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (51.4%), Debt Markers (formerly Tech Debt) (18.8%)
- **Documentation Coverage:** 42.0118% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `splitLinesChunk` **(Compute Cores)** (Impact: 32.6)
  * `merge` **(Generic / Templated Code)** (Impact: 21.1)
  * `go` **(Compute Cores)** (Impact: 11.3)
  * `handleSide` **(Generic / Templated Code)** (Impact: 8.8)
  * `onFailure` **(Callbacks & Closures)** (Impact: 6.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 23 instances
* *State Mutation (weighted view):* 76
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 86`, `structural_boundaries: 883`, `args: 411`, `func_start: 122`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 30`, `duplicate_logic: 10`
* *Architecture:* `api: 90`, `concurrency: 11`, `import: 39`
* *Defense:* `safety: 5`, `doc: 93`, `immutability_locks: 48`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.211
  * `Choke Point (Betweenness):` 0.001488 | `Ripple Effect (Closeness):` 0.123469
  * `Imports (Out-Degree: 37):` Cause.js, Channel.js, Chunk.js, Context.js, Deferred.js, Effect.js, Either.js, Equal.js...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `packages/effect/src/internal/dateTime.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.914)
- **Top Global Matches:** file_cluster_4: 8.914, file_cluster_0: 9.03, file_cluster_15: 9.578
- **Magnitude:** 517.62 | **LOC:** 1278 | **CtrlFlow:** 22.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **19**; blast radius 0.236; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (48.5%), Debt Markers (formerly Tech Debt) (27.8%), Mutation Surface (formerly State Flux) (12.4%), Connectivity (formerly Api Exposure) (12.3%)
- **Documentation Coverage:** 28.5714% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `unsafeMakeZoned` **(Defensive Guards)** (Impact: 44.9)
  * `makeZonedFromAdjusted` **(Many-Argument Workhorses)** (Impact: 36.2)
  * `toUtc` **(Defensive Guards)** (Impact: 35.0)
    * *Intent:* // ============================================================================= // time zones // ==...
  * `startOfDate` **(Many-Argument Workhorses)** (Impact: 28.0)
  * `endOfDate` **(Many-Argument Workhorses)** (Impact: 28.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 43
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 235`, `structural_boundaries: 412`, `args: 161`, `func_start: 67`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 17`, `unreferenced_by_name: 16`
* *Architecture:* `api: 81`, `import: 20`
* *Defense:* `safety: 34`, `doc: 81`, `immutability_locks: 63`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.236
  * `Choke Point (Betweenness):` 2.8e-05 | `Ripple Effect (Closeness):` 0.124923
  * `Imports (Out-Degree: 19):` Cause.js, Clock.js, DateTime.js, Duration.js, Effect.js, Either.js, Equal.js, Equivalence.js...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/ai/openrouter/src/Generated.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.528)
- **Top Global Matches:** file_cluster_4: 9.528, file_cluster_0: 11.893, file_cluster_6: 12.144
- **Magnitude:** 506.98 | **LOC:** 6082 | **CtrlFlow:** 0.9% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **8**; blast radius 0.511; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Guard Balance (formerly Safety Score) (49.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (24.1%), Debt Markers (formerly Tech Debt) (9.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `decodeError` **(Many-Argument Workhorses)** (Impact: 51.3)
  * `make` **(Generic / Templated Code)** (Impact: 3.8)
  * `unexpectedStatus` **(Callbacks & Closures)** (Impact: 3.5)
  * `ClientError` **(Generic / Templated Code)** (Impact: 2.5)
  * `default` **(Callbacks & Closures)** (Impact: 2.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 1353`, `args: 99`, `func_start: 9`, `class_start: 351`
* *Risk/State:* `safety_bypasses: 20`, `duplicate_logic: 4`
* *Architecture:* `api: 353`, `import: 8`
* *Defense:* `safety: 16`, `doc: 550`, `immutability_locks: 50`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.511
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001882
  * `Imports (Out-Degree: 0):` HttpClient, HttpClientError, HttpClientRequest, HttpClientResponse, Data, Effect, ParseResult, Schema
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `packages/effect/src/HashMap.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 9.159)
- **Top Global Matches:** file_cluster_5: 9.159, file_cluster_7: 13.185, file_cluster_0: 13.433
- **Magnitude:** 497.33 | **LOC:** 520 | **CtrlFlow:** 2.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **33** in-repo importer(s); it depends on **8**; blast radius 1.691; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Guard Balance (formerly Safety Score) (65.2%), Complexity Load (formerly Cognitive Load) (2.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 177`, `args: 56`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 10`
* *Architecture:* `api: 46`, `import: 10`
* *Defense:* `safety: 6`, `doc: 47`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.691
  * `Choke Point (Betweenness):` 0.001577 | `Ripple Effect (Closeness):` 0.196224
  * `Imports (Out-Degree: 8):` Equal.js, HashSet.js, Inspectable.js, Option.js, Pipeable.js, Types.js, hashMap.js, keySet.js
  * `Imported By (In-Degree: 33):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `packages/effect/test/Schema/Schema/Class/transformOrFail.test.ts` (TYPESCRIPT) | Magnitude: 0.77 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 70, structural_boundaries: 19, args: 7, import: 6
- `packages/effect/src/internal/cause.ts` (TYPESCRIPT) | Magnitude: 634.1 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 694, structural_boundaries: 413, generics: 237, args: 163
- `packages/effect/src/Order.ts` (TYPESCRIPT) | Magnitude: 95.76 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 125, structural_boundaries: 120, generics: 95, args: 49
- `packages/effect/test/util.ts` (TYPESCRIPT) | Magnitude: 109.62 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 72, structural_boundaries: 62, branch: 22, generics: 22
- `packages/effect/src/MetricBoundaries.ts` (TYPESCRIPT) | Magnitude: 22.5 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 20, indent_spaces: 12, doc: 8, immutability_locks: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `packages/effect/test/Schema/Schema/suspend.test.ts` (TYPESCRIPT) | Magnitude: 5.76 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 118, structural_boundaries: 42, immutability_locks: 23, args: 14
- `packages/effect/test/Schema/Schema/Array/headOrElse.test.ts` (TYPESCRIPT) | Magnitude: 3.83 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 58, structural_boundaries: 20, concurrency: 14, args: 7
- `packages/effect/test/Effect/lifting.test.ts` (TYPESCRIPT) | Magnitude: 8.62 | Delta: **0.045** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 40, structural_boundaries: 11, lazy_evaluation: 9, safety: 7
- `packages/platform-node/test/RpcServer.test.ts` (TYPESCRIPT) | Magnitude: 18.48 | Delta: **0.046** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 164, core_var_decl: 19, structural_boundaries: 17, lazy_evaluation: 10
- `packages/typeclass/src/data/BigInt.ts` (TYPESCRIPT) | Magnitude: 24.64 | Delta: **0.05** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 15, doc: 7, api: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `packages/cluster/src/RunnerAddress.ts` (TYPESCRIPT) | Magnitude: 17.8 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 18, indent_spaces: 18, doc: 11, api: 8
- `packages/effect/dtslint/Function.tst.ts` (TYPESCRIPT) | Magnitude: 10.84 | Delta: **0.046** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 43, structural_boundaries: 26, args: 14, test: 14
- `packages/effect/test/Channel/environment.test.ts` (TYPESCRIPT) | Magnitude: 17.16 | Delta: **0.05** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 78, structural_boundaries: 31, listeners: 13, args: 12
- `packages/effect/test/Stream/streamable.test.ts` (TYPESCRIPT) | Magnitude: 1.52 | Delta: **0.079** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 10, listeners: 6, import: 5
- `packages/effect/test/Schema/Serializable.test.ts` (TYPESCRIPT) | Magnitude: 0.23 | Delta: **0.082** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 97, structural_boundaries: 19, args: 11, test: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `packages/platform-bun/src/internal/httpServer.ts` (TYPESCRIPT) | Magnitude: 220.8 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 383, structural_boundaries: 153, args: 62, branch: 48
- `packages/ai/anthropic/src/AnthropicLanguageModel.ts` (TYPESCRIPT) | Magnitude: 455.54 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 1274, structural_boundaries: 360, branch: 226, core_var_decl: 122
- `packages/platform/src/internal/httpPlatform.ts` (TYPESCRIPT) | Magnitude: 55.46 | Delta: **0.037** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 89, structural_boundaries: 35, branch: 19, import: 12
- `packages/cluster/src/Sharding.ts` (TYPESCRIPT) | Magnitude: 396.5 | Delta: **0.044** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 1101, structural_boundaries: 334, branch: 197, core_var_decl: 165
- `packages/effect/test/Inspectable.test.ts` (TYPESCRIPT) | Magnitude: 306.68 | Delta: **0.046** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 220, structural_boundaries: 37, args: 34, closures: 34

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `packages/effect/test/Effect/provide-runtime.test.ts` (TYPESCRIPT) | Magnitude: 60.01 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 56, structural_boundaries: 29, core_var_decl: 15, listeners: 12
- `packages/sql-mysql2/examples/statement-transform.ts` (TYPESCRIPT) | Magnitude: 15.88 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 30, io: 8, structural_boundaries: 6, listeners: 5
- `packages/sql-drizzle/examples/sqlite.ts` (TYPESCRIPT) | Magnitude: 16.56 | Delta: **0.114** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 13, lazy_evaluation: 7, core_var_decl: 7, structural_boundaries: 5
- `packages/cli/test/utils/wc.ts` (TYPESCRIPT) | Magnitude: 18.38 | Delta: **0.14** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 7, structural_boundaries: 6, core_var_decl: 4, design_camel_case: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `packages/typeclass/src/SemiProduct.ts` (TYPESCRIPT) | Magnitude: 26.24 | Delta: **0.131** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 114, generics: 97, structural_boundaries: 96, safety_bypasses: 49
- `packages/effect/src/internal/fiberMessage.ts` (TYPESCRIPT) | Magnitude: 26.76 | Delta: **0.132** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 43, indent_spaces: 18, api: 17, doc: 17
- `packages/effect/src/Unify.ts` (TYPESCRIPT) | Magnitude: 663.39 | Delta: **0.191** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: structural_boundaries: 90, generics: 63, indent_spaces: 52, safety_bypasses: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `packages/effect/src/internal/string-utils.ts` (TYPESCRIPT) | Magnitude: 66.12 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 54, structural_boundaries: 24, core_var_decl: 22, branch: 16
- `packages/effect/src/Scheduler.ts` (TYPESCRIPT) | Magnitude: 237.56 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 181, structural_boundaries: 108, branch: 46, args: 42
- `packages/platform-node-shared/src/internal/fileSystem.ts` (TYPESCRIPT) | Magnitude: 201.94 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 476, structural_boundaries: 163, args: 102, core_var_decl: 80
- `packages/platform/src/HttpApiScalar.ts` (TYPESCRIPT) | Magnitude: 22.7 | Delta: **0.058** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 147, structural_boundaries: 34, immutability_locks: 26, branch: 24
- `packages/effect/test/Cron.test.ts` (TYPESCRIPT) | Magnitude: 41.68 | Delta: **0.097** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 296, core_var_decl: 84, time_date_logic: 83, design_snake_case: 80

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `packages/printer/src/index.ts` (TYPESCRIPT) | Magnitude: 20.64 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 7, api: 7, doc: 7, import: 7
- `packages/effect/src/index.ts` (TYPESCRIPT) | Magnitude: 194.66 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 182, structural_boundaries: 176, api: 176, import: 176
- `packages/platform/src/index.ts` (TYPESCRIPT) | Magnitude: 78.2 | Delta: **0.039** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 60, api: 60, doc: 60, import: 60
- `packages/printer-ansi/src/Ansi.ts` (TYPESCRIPT) | Magnitude: 84.52 | Delta: **0.047** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 92, doc: 69, api: 68, core_var_decl: 50
- `packages/cli/src/HelpDoc/Span.ts` (TYPESCRIPT) | Magnitude: 37.94 | Delta: **0.056** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 45, doc: 23, api: 22, indent_spaces: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `packages/effect/src/Symbol.ts` (TYPESCRIPT) | Magnitude: 14.08 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 6, doc: 3, api: 2, import: 2
- `packages/effect/src/RegExp.ts` (TYPESCRIPT) | Magnitude: 13.56 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 6, doc: 3, args: 2, safety: 2
- `scripts/circular.mjs` (JAVASCRIPT) | Magnitude: 16.48 | Delta: **0.058** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 3, import: 2, debug_prints: 2
- `packages/ai/amazon-bedrock/src/index.ts` (TYPESCRIPT) | Magnitude: 19.12 | Delta: **0.067** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 6, api: 6, doc: 6, import: 6
- `packages/ai/anthropic/src/index.ts` (TYPESCRIPT) | Magnitude: 19.12 | Delta: **0.067** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 6, api: 6, doc: 6, import: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `packages/effect/src/internal/dateTime.ts` (TYPESCRIPT) | Magnitude: 517.62 | Delta: **0.116** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 805, structural_boundaries: 412, branch: 235, args: 161

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `packages/platform-node-shared/src/internal/multipart.ts` (TYPESCRIPT) | Magnitude: 60.52 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 99, structural_boundaries: 51, args: 20, import: 13
- `packages/effect/src/Arbitrary.ts` (TYPESCRIPT) | Magnitude: 392.94 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 792, structural_boundaries: 264, branch: 182, args: 108
- `packages/rpc/src/RpcWorker.ts` (TYPESCRIPT) | Magnitude: 13.94 | Delta: **0.071** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 37, structural_boundaries: 35, generics: 13, listeners: 12
- `packages/platform-node-shared/src/internal/commandExecutor.ts` (TYPESCRIPT) | Magnitude: 47.18 | Delta: **0.089** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 194, structural_boundaries: 92, args: 43, core_var_decl: 25
- `packages/ai/ai/src/Chat.ts` (TYPESCRIPT) | Magnitude: 79.66 | Delta: **0.095** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 282, structural_boundaries: 118, core_var_decl: 55, generics: 48

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `packages/effect/test/Function.test.ts` (TYPESCRIPT) | Magnitude: 18.18 | Delta: **0.059** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 157, structural_boundaries: 76, args: 68, closures: 34

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `packages/effect/src/internal/encoding/base64Url.ts` (TYPESCRIPT) | Magnitude: 16.52 | Delta: **0.176** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 12, core_var_decl: 6, design_snake_case: 6
- `packages/opentelemetry/src/NodeSdk.ts` (TYPESCRIPT) | Magnitude: 30.96 | Delta: **0.212** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 75, structural_boundaries: 38, generics: 21, branch: 20
- `packages/effect/src/PubSub.ts` (TYPESCRIPT) | Magnitude: 31.94 | Delta: **0.235** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 44, generics: 39, doc: 19, args: 16

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `packages/effect/src/ParseResult.ts` -> **Giulio Canti** (100.0% isolated ownership) | Magnitude: 942.32
- `packages/effect/src/Graph.ts` -> **Dex Devlon** (100.0% isolated ownership) | Magnitude: 871.28
- `packages/cli/src/internal/options.ts` -> **Cristian Velasquez Ramos** (100.0% isolated ownership) | Magnitude: 730.9
- `packages/effect/src/Effect.ts` -> **Michael Arnaldi** (100.0% isolated ownership) | Magnitude: 671.74
- `packages/effect/src/internal/cause.ts` -> **Lucas Herzinger Souza** (100.0% isolated ownership) | Magnitude: 634.1

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `packages/effect/src/internal/fiberRuntime.ts` -> **Severity: 0.45** (Bridge: 0.0058 * Flux: 78.1207%)
- `packages/platform/src/Cookies.ts` -> **Severity: 0.19** (Bridge: 0.0019 * Flux: 99.9709%)
- `packages/effect/src/internal/stm/core.ts` -> **Severity: 0.189** (Bridge: 0.002 * Flux: 95.2327%)
- `packages/effect/src/Inspectable.ts` -> **Severity: 0.128** (Bridge: 0.0023 * Flux: 55.7637%)
- `packages/effect/src/internal/context.ts` -> **Severity: 0.116** (Bridge: 0.0014 * Flux: 81.4044%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `packages/effect/src/Effect.ts` -> **Severity: 18.616** (Embedded: 0.2327 * Error Risk: 80.0%)
- `packages/effect/src/Types.ts` -> **Severity: 17.232** (Embedded: 0.2284 * Error Risk: 75.4545%)
- `packages/effect/src/Request.ts` -> **Severity: 16.243** (Embedded: 0.1927 * Error Risk: 84.3121%)
- `packages/effect/src/Unify.ts` -> **Severity: 14.982** (Embedded: 0.1873 * Error Risk: 80.0%)
- `packages/effect/src/Context.ts` -> **Severity: 14.877** (Embedded: 0.186 * Error Risk: 80.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `packages/effect/src/Function.ts` -> **Severity: 2101.118** (Blast Radius: 31.35 * Doc Risk: 67.0213%)
- `packages/effect/test/Schema/TestUtils.ts` -> **Severity: 1331.0** (Blast Radius: 13.31 * Doc Risk: 100.0%)
- `packages/effect/src/Schema.ts` -> **Severity: 903.435** (Blast Radius: 18.943 * Doc Risk: 47.6923%)
- `packages/effect/src/Effect.ts` -> **Severity: 814.827** (Blast Radius: 11.815 * Doc Risk: 68.9655%)
- `packages/effect/src/Pipeable.ts` -> **Severity: 494.9** (Blast Radius: 9.898 * Doc Risk: 50.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`panics_and_aborts`:** 357 literal sites + 2 sites through wrappers = 359

- `absurd` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `packages/effect/src/Arbitrary.ts`
- `absurd` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `packages/effect/src/internal/fiberRuntime.ts`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 28717 call pairs -- scoped 32.5%, unique 0.0%, ambiguous 23.6%, external 43.9%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| typescript | 28646 | 32.6% | 0.0% | 23.7% | 43.8% |
| shell | 39 | 12.8% | 0.0% | 0.0% | 87.2% |
| javascript | 25 | 12.0% | 0.0% | 24.0% | 64.0% |
| html | 7 | 0.0% | 0.0% | 0.0% | 100.0% |

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
