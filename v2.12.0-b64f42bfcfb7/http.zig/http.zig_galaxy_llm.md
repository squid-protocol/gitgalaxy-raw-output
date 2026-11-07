# ARCHITECTURAL_BRIEF: http.zig
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/karlseguin/http.zig.git` |
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
- **Scope:** 33 analyzed artifact(s), 9015 LOC.
- **Load-bearing artifact:** `src/httpz.zig` -- 21 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/httpz.zig` -- pulls in 15 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `src/worker.zig` at magnitude 1022.84 (structural weight, not risk).
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
| Total Artifacts | 35 |
| Analyzed Artifacts (Scanned) | 33 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 2 |
| Total LOC | 9015 |
| Volatility Index | 0.061 |
| % Scanned of codebase = | 94.3% |
| Dominant Lang | ZIG |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2916 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.5636 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 45.5% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.1258 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 1 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| ZIG | 31 | 8997 | 93.9% |
| MAKEFILE | 1 | 18 | 3.0% |
| MARKDOWN | 1 | 0 | 3.0% |

## 4.1 SOURCE ENCODINGS
All 33 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules (2) 45%, State Mutators Files 18%, Large Core Modules (3) 15%, Data / Markup / Trivial 6%, Declarative / Non-Code 3%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 32 | 97.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1 | 3.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 2*

**Composition by Extension & Reason:**
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 58.3 | 18.5 | 14.7 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 80.0 | 35.4 | 44.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 37.8 | 4.5 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 8.8 | 2.4 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 83.9 | 33.4 | 29.3 | 8.2 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 76.9 | 6.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 39.1 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 32.8 | 2.3 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 12.7 | 2.0 | 0.5 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 21.5 | 21.1 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 85.3 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 190 | 25 | 15 | `src/httpz.zig` |
| cleanup | 209 | 24 | 18 | `src/httpz.zig` |
| guards | 1772 | 28 | 160 | `src/httpz.zig` |
| danger | 408 | 13 | 43 | `src/httpz.zig` |
| concurrency | 114 | 9 | 13 | `src/worker.zig` |
| connectivity | 403 | 31 | 29 | `src/httpz.zig` |
| io | 57 | 9 | 8 | `src/worker.zig` |
| crypto | 0 | 0 | 0 | - |
| ipc | 26 | 8 | 2 | `src/worker.zig` |
| time | 3 | 2 | 0 | `test_runner.zig` |
| serialization | 0 | 0 | 0 | - |
| regex | 4 | 3 | 0 | `test_runner.zig` |
| events | 5 | 4 | 1 | `src/httpz.zig` |
| tests | 136 | 14 | 10 | `src/httpz.zig` |
| docs | 6 | 5 | 1 | `src/testing.zig` |
| debt | 46 | 21 | 3 | `src/request.zig` |
| mutation | 2436 | 31 | 174 | `src/httpz.zig` |
| dead_code | 37 | 16 | 3 | `src/router.zig` |
| credential | 2 | 2 | 0 | `build.zig.zon` |
| threat | 0 | 0 | 0 | - |
| ml_ai | 10 | 4 | 1 | `test_runner.zig` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **4.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.5**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/worker.zig` (Hits: 14)
- `src/httpz.zig` (Hits: 10)
- `src/request.zig` (Hits: 8)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **httpz.zig** (`src/httpz.zig`) — 21 inbound connections
2. **t.zig** (`src/t.zig`) — 11 inbound connections
3. **metrics.zig** (`src/metrics.zig`) — 5 inbound connections
4. **worker.zig** (`src/worker.zig`) — 5 inbound connections
5. **buffer.zig** (`src/buffer.zig`) — 4 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **httpz.zig** (`src/httpz.zig`) — 15 outbound dependencies
2. **request.zig** (`src/request.zig`) — 10 outbound dependencies
3. **response.zig** (`src/response.zig`) — 8 outbound dependencies
4. **worker.zig** (`src/worker.zig`) — 8 outbound dependencies
5. **t.zig** (`src/t.zig`) — 5 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `NonBlocking` **(Many-Argument Workhorses)** (@ `src/worker.zig`) -> Impact: **112.2** | LOC: 615
  * *Intent:* // This is a NonBlocking worker. We have N workers, each accepting connections // and largely working in isolation from each other (the only thing the...
- `Server` **(Defensive Guards)** (@ `src/httpz.zig`) -> Impact: **105.4** | LOC: 411
- `Blocking` **(Defensive Guards)** (@ `src/worker.zig`) -> Impact: **79.7** | LOC: 312
  * *Intent:* // This is our Blocking worker. It's very different than NonBlocking and much // simpler. (WSH is our websocket handler, and can be void)
- `Router` **(Defensive Guards)** (@ `src/router.zig`) -> Impact: **58.1** | LOC: 262
- `getRoute` **(Many-Argument Workhorses)** (@ `src/router.zig`) -> Impact: **56.7** | LOC: 60
- `addRoute` **(Many-Argument Workhorses)** (@ `src/router.zig`) -> Impact: **53.1** | LOC: 83
- `handleRequest` **(Many-Argument Workhorses)** (@ `src/worker.zig`) -> Impact: **48.8** | LOC: 81
- `Worker` **(Compute Cores)** (@ `src/thread_pool.zig`) -> Impact: **43.2** | LOC: 156
- `parse` **(Defensive Guards)** (@ `src/request.zig`) -> Impact: **43.1** | LOC: 62
  * *Intent:* // returns true if the header has been fully parsed
- `main` **(Defensive Guards)** (@ `test_runner.zig`) -> Impact: **39.9** | LOC: 118

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src` | 14 | 4471.06 | 28.18% | 6.76% |
| `examples` | 11 | 251.06 | 11.85% | 0.0% |
| `__monolith__` | 5 | 199.72 | 8.93% | 9.77% |
| `src/middleware` | 2 | 68.36 | 9.25% | 0.0% |
| `examples/middleware` | 1 | 12.6 | 5.52% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `Makefile` -> **37.7541%** Exposure
- `src/key_value.zig` -> **30.691%** Exposure
- `test_runner.zig` -> **11.0899%** Exposure
- `src/request.zig` -> **10.89%** Exposure
- `src/response.zig` -> **9.8868%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `src/url.zig` -> **99.9753%** Exposure
- `src/thread_pool.zig` -> **99.9655%** Exposure
- `src/request.zig` -> **99.7207%** Exposure
- `src/response.zig` -> **98.7973%** Exposure
- `src/testing.zig` -> **97.6061%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `examples/02_handler.zig` -> **3** Orphaned Functions | **0** Duplicates
- `examples/08_websocket.zig` -> **3** Orphaned Functions | **0** Duplicates
- `examples/05_request_takeover.zig` -> **2** Orphaned Functions | **0** Duplicates
- `Makefile` -> **1** Orphaned Functions | **0** Duplicates
- `examples/01_basic.zig` -> **1** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `105` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/worker.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.471)
- **Top Global Matches:** file_cluster_12: 7.471, file_cluster_4: 9.189, file_cluster_5: 9.787
- **Magnitude:** 1022.84 | **LOC:** 1971 | **CtrlFlow:** 10.4% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **8**; blast radius 63.136; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Mutation Surface (formerly State Flux) (97.1%), Connectivity (formerly Api Exposure) (65.1%), Guard Balance (formerly Safety Score) (45.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `NonBlocking` **(Many-Argument Workhorses)** (Impact: 112.2)
    * *Intent:* // This is a NonBlocking worker. We have N workers, each accepting connections // and largely workin...
  * `Blocking` **(Defensive Guards)** (Impact: 79.7)
    * *Intent:* // This is our Blocking worker. It's very different than NonBlocking and much // simpler. (WSH is ou...
  * `handleRequest` **(Many-Argument Workhorses)** (Impact: 48.8)
  * `run` **(Many-Argument Workhorses)** (Impact: 33.6)
  * `init` **(Defensive Guards)** (Impact: 23.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 12 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 58 instances
* *Concurrency (weighted view):* 13
* *Memory Alloc (weighted view):* 4
* *State Mutation (weighted view):* 211
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 148`, `structural_boundaries: 218`, `args: 89`, `func_start: 89`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 33`, `state_mutation: 95`, `fragile_debt: 1`
* *Architecture:* `io: 14`, `api: 37`, `concurrency: 8`, `import: 8`
* *Defense:* `safety: 215`, `test: 2`, `sync_locks: 40`, `cleanup: 51`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 63.136
  * `Choke Point (Betweenness):` 0.031166 | `Ripple Effect (Closeness):` 0.440104
  * `Imports (Out-Degree: 5):` buffer.zig, builtin, httpz.zig, metrics.zig, std, t.zig, thread_pool.zig, websocket
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/httpz.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.425)
- **Top Global Matches:** file_cluster_12: 8.425, file_cluster_5: 9.694, file_cluster_7: 10.151
- **Magnitude:** 789.74 | **LOC:** 2432 | **CtrlFlow:** 7.4% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **21** in-repo importer(s); it depends on **15**; blast radius 190.156; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Connectivity (formerly Api Exposure) (83.9%), Mutation Surface (formerly State Flux) (74.6%), Guard Balance (formerly Safety Score) (36.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Server` **(Defensive Guards)** (Impact: 105.4)
  * `upgradeWebsocket` **(Defensive Guards)** (Impact: 31.6)
  * `init` **(Defensive Guards)** (Impact: 30.8)
  * `listen` **(Defensive Guards)** (Impact: 27.5)
  * `handleRequest` **(Many-Argument Workhorses)** (Impact: 27.4)
    * *Intent:* // This is always called from within a threadpool thread. For nonblocking, // notifyingHandler (abov...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Mitigated Memory Allocs:* 5 instances
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 40 instances
* *Api Near Db Sink:* 2 instances
* *High Risk Execution (weighted view):* 1
* *Concurrency (weighted view):* 35
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 171
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 146`, `structural_boundaries: 469`, `args: 82`, `func_start: 76`, `class_start: 23`
* *Risk/State:* `safety_bypasses: 87`, `high_risk_execution: 4`, `state_mutation: 91`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `io: 10`, `api: 56`, `concurrency: 10`, `import: 16`
* *Defense:* `safety: 470`, `test: 46`, `sync_locks: 10`, `cleanup: 72`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 190.156
  * `Choke Point (Betweenness):` 0.312668 | `Ripple Effect (Closeness):` 0.681452
  * `Imports (Out-Degree: 12):` build, builtin, config.zig, key_value.zig, metrics.zig, middleware.zig, request.zig, response.zig...
  * `Imported By (In-Degree: 21):` (Excluded from Brief to save tokens)

### `src/request.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.974)
- **Top Global Matches:** file_cluster_4: 6.974, file_cluster_12: 10.073, file_cluster_6: 11.624
- **Magnitude:** 738.84 | **LOC:** 1854 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **10**; blast radius 55.273; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.7%), Connectivity (formerly Api Exposure) (52.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (43.1%), Guard Balance (formerly Safety Score) (37.6%)
- **Documentation Coverage:** 93.1034% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse` **(Defensive Guards)** (Impact: 43.1)
    * *Intent:* // returns true if the header has been fully parsed
  * `parseHeaders` **(Many-Argument Workhorses)** (Impact: 34.4)
  * `prepareForBody` **(Many-Argument Workhorses)** (Impact: 29.4)
    * *Intent:* // we've finished reading the header
  * `getContentDispotionAttributes` **(Defensive Guards)** (Impact: 29.2)
    * *Intent:* // I'm sorry
  * `parseMultiFormData` **(Defensive Guards)** (Impact: 28.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 78 instances
* *State Mutation (weighted view):* 286
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 198`, `structural_boundaries: 262`, `args: 38`, `func_start: 38`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 130`, `planned_debt: 5`, `fragile_debt: 2`
* *Architecture:* `io: 8`, `api: 25`, `import: 12`
* *Defense:* `safety: 352`, `doc: 1`, `test: 21`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 55.273
  * `Choke Point (Betweenness):` 0.028058 | `Ripple Effect (Closeness):` 0.4225
  * `Imports (Out-Degree: 9):` buffer.zig, config.zig, httpz.zig, key_value.zig, metrics.zig, params.zig, std, t.zig...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/router.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.887)
- **Top Global Matches:** file_cluster_12: 7.887, file_cluster_4: 9.052, file_cluster_15: 9.609
- **Magnitude:** 535.14 | **LOC:** 886 | **CtrlFlow:** 9.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 21.033; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (94.1%), Connectivity (formerly Api Exposure) (67.2%), Guard Balance (formerly Safety Score) (36.6%), Complexity Load (formerly Cognitive Load) (34.0%)
- **Documentation Coverage:** 96.7742% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Router` **(Defensive Guards)** (Impact: 58.1)
  * `getRoute` **(Many-Argument Workhorses)** (Impact: 56.7)
  * `addRoute` **(Many-Argument Workhorses)** (Impact: 53.1)
  * `Group` **(Defensive Guards)** (Impact: 22.4)
  * `tryMergeConfig` **(Defensive Guards)** (Impact: 10.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 11 instances
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 27 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 90
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 91`, `args: 71`, `func_start: 71`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 13`, `high_risk_execution: 11`, `state_mutation: 36`, `dead_code: 10`, `planned_debt: 1`
* *Architecture:* `api: 54`, `import: 4`
* *Defense:* `safety: 160`, `doc: 1`, `test: 6`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 21.033
  * `Choke Point (Betweenness):` 0.008821 | `Ripple Effect (Closeness):` 0.377232
  * `Imports (Out-Degree: 3):` httpz.zig, params.zig, std, t.zig
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/testing.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.713)
- **Top Global Matches:** file_cluster_5: 7.713, file_cluster_12: 7.968, file_cluster_7: 8.318
- **Magnitude:** 318.64 | **LOC:** 668 | **CtrlFlow:** 11.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 21.033; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (68.3%), Connectivity (formerly Api Exposure) (58.3%), Guard Balance (formerly Safety Score) (43.1%)
- **Documentation Coverage:** 97.0588% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `compareValue` **(Defensive Guards)** (Impact: 35.0)
  * `parseWithAllocator` **(Defensive Guards)** (Impact: 17.7)
  * `escapeString` **(Defensive Guards)** (Impact: 13.3)
  * `decodeChunkedEncoding` **(Defensive Guards)** (Impact: 12.1)
  * `compare` **(Defensive Guards)** (Impact: 11.5)
    * *Intent:* // We compare by getting the string representation of a and b // and then parsing it into a std.json...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 19 instances
* *Memory Alloc (weighted view):* 4
* *State Mutation (weighted view):* 82
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 128`, `args: 36`, `func_start: 36`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 44`, `fragile_debt: 1`
* *Architecture:* `io: 3`, `api: 27`, `concurrency: 1`, `import: 4`
* *Defense:* `safety: 125`, `doc: 2`, `test: 14`, `cleanup: 19`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 21.033
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.377232
  * `Imports (Out-Degree: 4):` httpz.zig, std, t.zig, worker.zig
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/thread_pool.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.376)
- **Top Global Matches:** file_cluster_4: 7.376, file_cluster_12: 9.205, file_cluster_15: 9.838
- **Magnitude:** 280.52 | **LOC:** 443 | **CtrlFlow:** 12.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 18.297; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (58.1%), Guard Balance (formerly Safety Score) (50.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Worker` **(Compute Cores)** (Impact: 43.2)
  * `spawn` **(Compute Cores)** (Impact: 22.5)
  * `ThreadPool` **(Defensive Guards)** (Impact: 18.3)
  * `getNext` **(Compute Cores)** (Impact: 15.4)
  * `init` **(Defensive Guards)** (Impact: 8.6)
    * *Intent:* // we expect allocator to be an Arena
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 23 instances
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 91
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 48`, `args: 17`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 45`, `planned_debt: 1`
* *Architecture:* `api: 13`, `concurrency: 14`, `import: 2`
* *Defense:* `safety: 48`, `test: 3`, `sync_locks: 12`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 18.297
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.293403
  * `Imports (Out-Degree: 1):` std, t.zig
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/response.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.312)
- **Top Global Matches:** file_cluster_12: 6.312, file_cluster_15: 7.318, file_cluster_16: 9.038
- **Magnitude:** 239.14 | **LOC:** 676 | **CtrlFlow:** 7.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **8**; blast radius 55.273; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.8%), Connectivity (formerly Api Exposure) (60.2%), Guard Balance (formerly Safety Score) (44.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (43.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `prepareHeader` **(Compute Cores)** (Impact: 27.4)
  * `serializeCookie` **(Many-Argument Workhorses)** (Impact: 27.4)
    * *Intent:* // we expect arena to be an ArenaAllocator
  * `headerOpts` **(Defensive Guards)** (Impact: 11.4)
  * `write` **(Defensive Guards)** (Impact: 8.2)
  * `writeInt` **(Compute Cores)** (Impact: 7.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 19 instances
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 88
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 82`, `args: 20`, `func_start: 20`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 50`, `fragile_debt: 1`
* *Architecture:* `io: 3`, `api: 24`, `concurrency: 1`, `import: 8`
* *Defense:* `safety: 78`, `test: 10`, `cleanup: 18`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 55.273
  * `Choke Point (Betweenness):` 0.008653 | `Ripple Effect (Closeness):` 0.4225
  * `Imports (Out-Degree: 6):` buffer.zig, builtin, config.zig, httpz.zig, key_value.zig, std, t.zig, worker.zig
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/t.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 8.22)
- **Top Global Matches:** file_cluster_7: 8.22, file_cluster_5: 9.182, file_cluster_12: 9.255
- **Magnitude:** 158.18 | **LOC:** 353 | **CtrlFlow:** 11.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **5**; blast radius 144.605; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (80.1%), Guard Balance (formerly Safety Score) (80.0%), Connectivity (formerly Api Exposure) (80.0%), Concurrency Surface (formerly Concurrency) (40.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `allocInit` **(Defensive Guards)** (Impact: 23.0)
  * `expect` **(Defensive Guards)** (Impact: 14.1)
  * `read` **(Defensive Guards)** (Impact: 13.3)
  * `stream` **(Defensive Guards)** (Impact: 6.7)
  * `write` **(Defensive Guards)** (Impact: 5.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 6 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 6
* *Memory Alloc (weighted view):* 6
* *State Mutation (weighted view):* 26
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 60`, `args: 20`, `func_start: 20`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 29`, `high_risk_execution: 4`, `state_mutation: 14`
* *Architecture:* `io: 8`, `api: 22`, `concurrency: 1`, `import: 5`
* *Defense:* `safety: 47`, `test: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 144.605
  * `Choke Point (Betweenness):` 0.072749 | `Ripple Effect (Closeness):` 0.502976
  * `Imports (Out-Degree: 5):` buffer.zig, builtin, httpz.zig, std, worker.zig
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `test_runner.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.057)
- **Top Global Matches:** file_cluster_4: 8.057, file_cluster_12: 9.334, file_cluster_15: 9.469
- **Magnitude:** 129.98 | **LOC:** 299 | **CtrlFlow:** 19.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 7.564; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (89.3%), Guard Balance (formerly Safety Score) (46.0%), Complexity Load (formerly Cognitive Load) (34.6%), Debt Markers (formerly Tech Debt) (11.1%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(Defensive Guards)** (Impact: 39.9)
  * `endTiming` **(Defensive Guards)** (Impact: 8.3)
  * `status` **(Generic / Templated Code)** (Impact: 6.5)
  * `display` **(Defensive Guards)** (Impact: 6.1)
  * `readEnvBool` **(Defensive Guards)** (Impact: 4.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 9 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 42`, `args: 17`, `func_start: 17`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 4`, `state_mutation: 9`, `dead_code: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 4`, `import: 2`
* *Defense:* `safety: 26`, `test: 2`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.564
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` builtin, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/url.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.538)
- **Top Global Matches:** file_cluster_12: 7.538, file_cluster_7: 9.131, file_cluster_5: 9.853
- **Magnitude:** 119.86 | **LOC:** 270 | **CtrlFlow:** 14.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **4**; blast radius 30.723; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (58.3%), Connectivity (formerly Api Exposure) (45.3%)
- **Documentation Coverage:** 60.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `unescape` **(Many-Argument Workhorses)** (Impact: 30.6)
    * *Intent:* // std.Url.unescapeString has 2 problems // First, it doesn't convert '+' -> ' ' // Second, it _alwa...
  * `isValid` **(Defensive Guards)** (Impact: 11.0)
  * `parse` **(Defensive Guards)** (Impact: 3.6)
  * `asUint` **(Type Conversions)** (Impact: 3.4)
    * *Intent:* /// converts ascii to unsigned int of appropriate size
  * `decodeHex` **(Type Conversions)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 18 instances
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 57
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 27`, `args: 6`, `func_start: 6`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 21`
* *Architecture:* `api: 7`, `import: 4`
* *Defense:* `safety: 52`, `doc: 1`, `test: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 30.723
  * `Choke Point (Betweenness):` 0.000336 | `Ripple Effect (Closeness):` 0.398585
  * `Imports (Out-Degree: 2):` builtin, metrics.zig, std, t.zig
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/key_value.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.121)
- **Top Global Matches:** file_cluster_12: 7.121, file_cluster_5: 8.408, file_cluster_7: 9.262
- **Magnitude:** 95.06 | **LOC:** 223 | **CtrlFlow:** 6.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **2**; blast radius 34.083; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (80.5%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (60.5%), Guard Balance (formerly Safety Score) (43.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `KeyValue` **(Type Conversions)** (Impact: 24.0)
  * `init` **(Type Conversions)** (Impact: 9.3)
  * `get` **(Compute Cores)** (Impact: 5.6)
  * `deinit` **(Type Conversions)** (Impact: 5.4)
  * `strHash` **(Defensive Guards)** (Impact: 4.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 5 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 17
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 31`, `args: 10`, `func_start: 10`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 7`, `fragile_debt: 2`
* *Architecture:* `api: 12`, `import: 2`
* *Defense:* `safety: 28`, `test: 4`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 34.083
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.398585
  * `Imports (Out-Degree: 1):` std, t.zig
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/buffer.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.321)
- **Top Global Matches:** file_cluster_0: 7.321, file_cluster_15: 8.627, file_cluster_13: 9.984
- **Magnitude:** 74.94 | **LOC:** 239 | **CtrlFlow:** 7.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **4**; blast radius 55.93; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (57.8%), Mutation Surface (formerly State Flux) (52.5%), Guard Balance (formerly Safety Score) (33.2%), Complexity Load (formerly Cognitive Load) (10.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `init` **(Defensive Guards)** (Impact: 11.3)
  * `allocType` **(Many-Argument Workhorses)** (Impact: 8.0)
  * `grow` **(Defensive Guards)** (Impact: 5.4)
  * `release` **(Generic / Templated Code)** (Impact: 4.1)
  * `free` **(Generic / Templated Code)** (Impact: 3.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 10 instances
* *Amplified Cascading Flux:* 3 instances
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 27`, `args: 11`, `func_start: 11`, `class_start: 3`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* `api: 10`, `concurrency: 1`, `import: 4`
* *Defense:* `safety: 42`, `test: 2`, `sync_locks: 12`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 55.93
  * `Choke Point (Betweenness):` 0.001344 | `Ripple Effect (Closeness):` 0.335317
  * `Imports (Out-Degree: 3):` httpz.zig, metrics.zig, std, t.zig
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/middleware/Cors.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.421)
- **Top Global Matches:** file_cluster_15: 7.421, file_cluster_9: 7.694, file_cluster_16: 7.922
- **Magnitude:** 56.84 | **LOC:** 114 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 25.443; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (85.0%), Guard Balance (formerly Safety Score) (42.6%), Connectivity (formerly Api Exposure) (38.6%), Complexity Load (formerly Cognitive Load) (18.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `execute` **(Many-Argument Workhorses)** (Impact: 31.5)
  * `parseOrigin` **(Defensive Guards)** (Impact: 8.3)
  * `init` **(Defensive Guards)** (Impact: 2.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 12`, `args: 3`, `func_start: 3`, `class_start: 2`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 4`, `import: 2`
* *Defense:* `safety: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 25.443
  * `Choke Point (Betweenness):` 0.015121 | `Ripple Effect (Closeness):` 0.267405
  * `Imports (Out-Degree: 1):` httpz.zig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `examples/01_basic.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.665)
- **Top Global Matches:** file_cluster_15: 6.665, file_cluster_2: 8.047, file_cluster_11: 8.179
- **Magnitude:** 36.42 | **LOC:** 127 | **CtrlFlow:** 2.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 7.564; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (44.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (21.1%), Complexity Load (formerly Cognitive Load) (17.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (3.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `formPost` **(Defensive Guards)** (Impact: 4.0)
  * `hello` **(Defensive Guards)** (Impact: 3.8)
  * `main` **(I/O & Config Routines)** (Impact: 3.1)
    * *Intent:* // This example demonstrates basic httpz usage, with focus on using the // httpz.Request and httpz.R...
  * `index` **(State Mutators)** (Impact: 2.3)
  * `writer` **(State Mutators)** (Impact: 2.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 2 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 10
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 8`, `args: 9`, `func_start: 9`
* *Risk/State:* `state_mutation: 6`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `safety: 11`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.564
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` httpz, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/config.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.627)
- **Top Global Matches:** file_cluster_15: 5.627, file_cluster_2: 7.083, file_cluster_11: 7.379
- **Magnitude:** 35.78 | **LOC:** 116 | **CtrlFlow:** 6.1% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **4**; blast radius 34.083; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (74.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (48.5%), Complexity Load (formerly Cognitive Load) (4.2%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parseAddress` **(Defensive Guards)** (Impact: 4.9)
  * `workerCount` **(Defensive Guards)** (Impact: 4.5)
  * `isUnixAddress` **(Defensive Guards)** (Impact: 3.2)
  * `threadPoolCount` **(Defensive Guards)** (Impact: 3.0)
  * `localhost` **(Parameter Forwarders)** (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 9`, `args: 6`, `func_start: 6`, `class_start: 9`
* *Risk/State:* None
* *Architecture:* `io: 4`, `api: 15`, `import: 4`
* *Defense:* `safety: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 34.083
  * `Choke Point (Betweenness):` 0.000924 | `Ripple Effect (Closeness):` 0.391204
  * `Imports (Out-Degree: 3):` httpz.zig, request.zig, response.zig, std
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `examples/10_file_upload.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.415)
- **Top Global Matches:** file_cluster_0: 8.415, file_cluster_15: 9.147, file_cluster_9: 9.532
- **Magnitude:** 33.48 | **LOC:** 137 | **CtrlFlow:** 11.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 7.564; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Dead Code Surface (formerly Dead Code) (32.8%), Guard Balance (formerly Safety Score) (21.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (21.1%), Complexity Load (formerly Cognitive Load) (9.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `upload` **(Defensive Guards)** (Impact: 23.0)
  * `main` **(I/O & Config Routines)** (Impact: 2.4)
    * *Intent:* // This example demonstrates handling file uploads using multipart/form-data. // It shows how to: //...
  * `index` **(Generic / Templated Code)** (Impact: 2.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Memory Alloc (weighted view):* 0
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 6`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 3`, `dead_code: 5`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `safety: 34`, `test: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.564
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` httpz, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/params.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.043)
- **Top Global Matches:** file_cluster_15: 6.043, file_cluster_2: 8.132, file_cluster_11: 8.136
- **Magnitude:** 32.2 | **LOC:** 89 | **CtrlFlow:** 5.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **2**; blast radius 18.744; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (90.6%), Connectivity (formerly Api Exposure) (56.4%), Guard Balance (formerly Safety Score) (43.8%), Complexity Load (formerly Cognitive Load) (18.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get` **(Compute Cores)** (Impact: 5.7)
  * `addValue` **(Parameter Forwarders)** (Impact: 3.8)
  * `init` **(Defensive Guards)** (Impact: 2.1)
  * `deinit` **(State Mutators)** (Impact: 1.9)
  * `addNames` **(Defensive Guards)** (Impact: 1.9)
    * *Intent:* // It should be impossible for names.len != self.len at this point, but it's // a bit dangerous to a...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 2 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 7
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 6`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 7`, `import: 2`
* *Defense:* `safety: 8`, `test: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 18.744
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.293403
  * `Imports (Out-Degree: 1):` std, t.zig
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `examples/07_advanced_routing.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.736)
- **Top Global Matches:** file_cluster_15: 6.736, file_cluster_2: 8.139, file_cluster_11: 8.153
- **Magnitude:** 31.56 | **LOC:** 93 | **CtrlFlow:** 1.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 7.564; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (51.3%), Complexity Load (formerly Cognitive Load) (27.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (21.1%), Connectivity (formerly Api Exposure) (6.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dispatch` **(Defensive Guards)** (Impact: 4.8)
  * `main` **(I/O & Config Routines)** (Impact: 2.9)
    * *Intent:* // This example shows more advanced routing example, namely route groups // and route configuration....
  * `index` **(State Mutators)** (Impact: 2.5)
  * `infoDispatch` **(Parameter Forwarders)** (Impact: 2.4)
    * *Intent:* // special dispatch set in the info route
  * `page1` **(State Mutators)** (Impact: 2.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 2 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 10
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 8`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 6`, `unreferenced_by_name: 1`
* *Architecture:* `api: 3`, `import: 2`
* *Defense:* `safety: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.564
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` httpz, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/08_websocket.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.063)
- **Top Global Matches:** file_cluster_15: 6.063, file_cluster_11: 7.75, file_cluster_2: 7.889
- **Magnitude:** 30.36 | **LOC:** 103 | **CtrlFlow:** 1.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 7.564; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (21.1%), Complexity Load (formerly Cognitive Load) (18.7%), Connectivity (formerly Api Exposure) (8.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ws` **(State Mutators)** (Impact: 4.7)
  * `index` **(State Mutators)** (Impact: 2.7)
  * `main` **(Defensive Guards)** (Impact: 2.2)
    * *Intent:* // This example show how to upgrade a request to websocket.
  * `init` **(Parameter Forwarders)** (Impact: 2.0)
    * *Intent:* // context is any abitrary data that you want, you'll pass it to upgradeWebsocket
  * `clientMessage` **(Parameter Forwarders)** (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 2 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 8
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 8`, `args: 6`, `func_start: 6`, `class_start: 3`
* *Risk/State:* `state_mutation: 4`, `unreferenced_by_name: 3`
* *Architecture:* `api: 6`, `import: 2`
* *Defense:* `safety: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.564
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` httpz, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/metrics.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.236)
- **Top Global Matches:** file_cluster_2: 6.236, file_cluster_17: 7.073, file_cluster_15: 7.149
- **Magnitude:** 30.18 | **LOC:** 116 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **2**; blast radius 65.89; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (74.8%), Test Surface (formerly Verification) (2.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `write` **(Defensive Guards)** (Impact: 2.1)
  * `allocBufferEmpty` **(State Mutators)** (Impact: 1.6)
  * `allocBufferLarge` **(State Mutators)** (Impact: 1.6)
  * `allocUnescape` **(State Mutators)** (Impact: 1.6)
  * `timeoutRequest` **(State Mutators)** (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1`, `args: 12`, `func_start: 12`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 12`, `import: 2`
* *Defense:* `safety: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 65.89
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.429835
  * `Imports (Out-Degree: 0):` metrics, std
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `examples/04_action_context.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.524)
- **Top Global Matches:** file_cluster_12: 7.524, file_cluster_7: 8.627, file_cluster_5: 10.042
- **Magnitude:** 27.12 | **LOC:** 94 | **CtrlFlow:** 3.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 7.564; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.7%), Complexity Load (formerly Cognitive Load) (26.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (21.1%), Connectivity (formerly Api Exposure) (4.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dispatch` **(Many-Argument Workhorses)** (Impact: 8.0)
    * *Intent:* // In example_3, our action type was: httpz.Action(*Handler). // In this example, we've changed it t...
  * `index` **(State Mutators)** (Impact: 2.5)
  * `main` **(Defensive Guards)** (Impact: 2.4)
    * *Intent:* // This example is very similar to 03_dispatch.zig, but shows how the action // state can be a diffe...
  * `admin` **(Defensive Guards)** (Impact: 2.1)
    * *Intent:* // because of our dispatch method, this can only be called when env.user != null
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 2 instances
* *Api Near Db Sink:* 1 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 8`, `args: 4`, `func_start: 4`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 5`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `safety: 7`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.564
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` httpz, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/02_handler.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.307)
- **Top Global Matches:** file_cluster_15: 7.307, file_cluster_11: 8.421, file_cluster_2: 8.425
- **Magnitude:** 26.52 | **LOC:** 93 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 7.564; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.0%), Concurrency Surface (formerly Concurrency) (27.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (21.1%), Connectivity (formerly Api Exposure) (7.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `uncaughtError` **(State Mutators)** (Impact: 2.8)
    * *Intent:* // If the handler defines the special "uncaughtError" function, it'll be // called when an action re...
  * `index` **(State Mutators)** (Impact: 2.6)
  * `main` **(I/O & Config Routines)** (Impact: 2.4)
    * *Intent:* // This example demonstrates using a custom Handler. It shows how to have // global state (here we s...
  * `hits` **(Parameter Forwarders)** (Impact: 2.4)
  * `notFound` **(State Mutators)** (Impact: 2.2)
    * *Intent:* // If the handler defines a special "notFound" function, it'll be called // when a request is made a...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Memory Alloc (weighted view):* 0
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 8`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 6`, `unreferenced_by_name: 3`
* *Architecture:* `api: 4`, `concurrency: 1`, `import: 2`
* *Defense:* `safety: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.564
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` httpz, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `readme.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 26.3 | **LOC:** 1315 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.564
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/03_dispatch.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.778)
- **Top Global Matches:** file_cluster_15: 7.778, file_cluster_2: 8.342, file_cluster_13: 8.466
- **Magnitude:** 18.96 | **LOC:** 59 | **CtrlFlow:** 6.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 7.564; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (46.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (21.1%), Complexity Load (formerly Cognitive Load) (11.5%), Connectivity (formerly Api Exposure) (5.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `index` **(State Mutators)** (Impact: 6.5)
  * `dispatch` **(Defensive Guards)** (Impact: 2.8)
    * *Intent:* // In addition to the special "notFound" and "uncaughtError" shown in example 2 // the special "disp...
  * `main` **(Defensive Guards)** (Impact: 2.0)
    * *Intent:* // This example uses a custom dispatch method on our handler for greater control // in how actions a...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 1 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 5
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 7`, `args: 3`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 3`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `safety: 5`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.564
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` httpz, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `build.zig` (ZIG | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 6.632)
- **Top Global Matches:** file_cluster_9: 6.632, file_cluster_2: 12.137, file_cluster_16: 12.254
- **Magnitude:** 15.86 | **LOC:** 105 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 21.033; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (46.9%), Connectivity (formerly Api Exposure) (16.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (12.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (12.5%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `build` **(I/O & Config Routines)** (Impact: 12.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 21.033
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.39278
  * `Imports (Out-Degree: 0):` std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `examples/05_request_takeover.zig` (ZIG) | Magnitude: 8.02 | Delta: **0.109** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 18, core_var_decl: 9, design_snake_case: 6, structural_boundaries: 5

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/request.zig` -> **Karl Seguin** (100.0% isolated ownership) | Magnitude: 738.84
- `src/testing.zig` -> **Karl Seguin** (100.0% isolated ownership) | Magnitude: 318.64
- `src/response.zig` -> **Karl Seguin** (100.0% isolated ownership) | Magnitude: 239.14
- `src/key_value.zig` -> **Karl Seguin** (100.0% isolated ownership) | Magnitude: 95.06

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/httpz.zig` -> **Severity: 23.325** (Bridge: 0.3127 * Flux: 74.5997%)
- `src/t.zig` -> **Severity: 5.831** (Bridge: 0.0727 * Flux: 80.1488%)
- `src/worker.zig` -> **Severity: 3.027** (Bridge: 0.0312 * Flux: 97.1098%)
- `src/request.zig` -> **Severity: 2.798** (Bridge: 0.0281 * Flux: 99.7207%)
- `src/middleware/Cors.zig` -> **Severity: 1.286** (Bridge: 0.0151 * Flux: 85.0424%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/t.zig` -> **Severity: 40.238** (Embedded: 0.503 * Error Risk: 80.0%)
- `src/httpz.zig` -> **Severity: 24.939** (Embedded: 0.6815 * Error Risk: 36.5964%)
- `src/worker.zig` -> **Severity: 20.154** (Embedded: 0.4401 * Error Risk: 45.7943%)
- `src/response.zig` -> **Severity: 18.891** (Embedded: 0.4225 * Error Risk: 44.7126%)
- `build.zig` -> **Severity: 18.424** (Embedded: 0.3928 * Error Risk: 46.9066%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/httpz.zig` -> **Severity: 19015.6** (Blast Radius: 190.156 * Doc Risk: 100.0%)
- `src/t.zig` -> **Severity: 14460.5** (Blast Radius: 144.605 * Doc Risk: 100.0%)
- `src/metrics.zig` -> **Severity: 6589.0** (Blast Radius: 65.89 * Doc Risk: 100.0%)
- `src/worker.zig` -> **Severity: 6313.6** (Blast Radius: 63.136 * Doc Risk: 100.0%)
- `src/buffer.zig` -> **Severity: 5593.0** (Blast Radius: 55.93 * Doc Risk: 100.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 1488 call pairs -- scoped 30.0%, unique 0.0%, ambiguous 12.8%, external 57.3%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| zig | 1488 | 30.0% | 0.0% | 12.8% | 57.3% |

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
