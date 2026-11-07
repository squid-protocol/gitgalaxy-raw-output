# ARCHITECTURAL_BRIEF: libxev
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/mitchellh/libxev.git` |
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
- **Scope:** 72 analyzed artifact(s), 17092 LOC.
- **Load-bearing artifact:** `src/dynamic.zig` -- 15 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/main.zig` -- pulls in 17 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `src/backend/kqueue.zig` at magnitude 760.22 (structural weight, not risk).
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
| Total Artifacts | 87 |
| Analyzed Artifacts (Scanned) | 72 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 15 |
| Total LOC | 17092 |
| Volatility Index | 0.014 |
| % Scanned of codebase = | 82.8% |
| Dominant Lang | ZIG |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4529 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.4981 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 23.6% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.5546 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 4 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| ZIG | 42 | 16196 | 58.3% |
| MARKDOWN | 5 | 0 | 6.9% |
| C | 5 | 261 | 6.9% |
| JSON | 4 | 35 | 5.6% |
| NIX | 3 | 88 | 4.2% |
| TYPESCRIPT | 3 | 27 | 4.2% |
| XML | 3 | 2 | 4.2% |
| YAML | 2 | 119 | 2.8% |
| JAVASCRIPT | 2 | 34 | 2.8% |
| CSS | 2 | 330 | 2.8% |
| PLAINTEXT | 1 | 0 | 1.4% |

## 4.1 SOURCE ENCODINGS
All 72 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules (2) 32%, Data / Markup / Trivial 25%, Large Core Modules (3) 15%, Declarative / Non-Code 8%, Generic / Templated Code Files 4%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 64 | 88.9% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 6 | 8.3% |
| Static: Minified & Vendor Opaque Mass | 2 | 2.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 15*

**Composition by Extension & Reason:**
- `.scd`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 10540 LOC)
- `.lock`: 1x Excluded (Unsupported Extension: '.lock')
- `.ico`: 1x Excluded (Explicitly Denied Extension: '.ico')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 92.1 | 9.8 | 5.1 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 78.4 | 29.4 | 42.7 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 99.8 | 23.8 | 10.7 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 6.8 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 28.7 | 6.6 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 7.9 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 21.9 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 23.1 | 1.8 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 2.1 | 0.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 3.8 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 55.0 | 59.5 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 638 | 26 | 24 | `src/backend/iocp.zig` |
| cleanup | 160 | 25 | 8 | `src/backend/kqueue.zig` |
| guards | 1722 | 43 | 69 | `src/backend/kqueue.zig` |
| danger | 980 | 29 | 40 | `src/backend/kqueue.zig` |
| concurrency | 39 | 10 | 1 | `src/queue_mpsc.zig` |
| connectivity | 826 | 52 | 36 | `src/windows.zig` |
| io | 146 | 20 | 6 | `src/watcher/udp.zig` |
| crypto | 0 | 0 | 0 | - |
| ipc | 47 | 18 | 1 | `src/watcher/stream.zig` |
| time | 4 | 3 | 0 | `src/backend/kqueue.zig` |
| serialization | 0 | 0 | 0 | - |
| regex | 0 | 0 | 0 | - |
| events | 303 | 20 | 19 | `src/watcher/stream.zig` |
| tests | 111 | 19 | 6 | `src/backend/io_uring.zig` |
| docs | 1567 | 32 | 76 | `src/backend/kqueue.zig` |
| debt | 165 | 23 | 8 | `src/backend/iocp.zig` |
| mutation | 3472 | 52 | 138 | `src/backend/kqueue.zig` |
| dead_code | 33 | 27 | 1 | `src/watcher/tcp.zig` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 63 | 12 | 3 | `src/backend/kqueue.zig` |
| ui | 33 | 3 | 0 | `website/styles/Home.module.css` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/watcher/udp.zig` (Hits: 32)
- `src/watcher/file.zig` (Hits: 18)
- `src/watcher/stream.zig` (Hits: 17)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **dynamic.zig** (`src/dynamic.zig`) — 15 inbound connections
2. **xev.h** (`include/xev.h`) — 11 inbound connections
3. **main.zig** (`src/main.zig`) — 8 inbound connections
4. **queue.zig** (`src/queue.zig`) — 7 inbound connections
5. **stream.zig** (`src/watcher/stream.zig`) — 7 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **main.zig** (`src/main.zig`) — 17 outbound dependencies
2. **api.zig** (`src/api.zig`) — 11 outbound dependencies
3. **dynamic.zig** (`src/dynamic.zig`) — 11 outbound dependencies
4. **epoll.zig** (`src/backend/epoll.zig`) — 9 outbound dependencies
5. **kqueue.zig** (`src/backend/kqueue.zig`) — 9 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `invoke` **(Many-Argument Workhorses)** (@ `src/backend/io_uring.zig`) -> Impact: **109.5** | LOC: 151
  * *Intent:* /// Invokes the callback for this completion after properly constructing /// the Result based on the res code.
- `start` **(Many-Argument Workhorses)** (@ `src/backend/epoll.zig`) -> Impact: **99.6** | LOC: 295
- `start_completion` **(Many-Argument Workhorses)** (@ `src/backend/iocp.zig`) -> Impact: **98.9** | LOC: 315
  * *Intent:* // Start the completion.
- `perform` **(Defensive Guards)** (@ `src/backend/kqueue.zig`) -> Impact: **85.7** | LOC: 155
  * *Intent:* /// Perform the operation associated with this completion. This will /// perform the full blocking operation for the completion.
- `syscall_result` **(Many-Argument Workhorses)** (@ `src/backend/kqueue.zig`) -> Impact: **80.0** | LOC: 146
  * *Intent:* /// Returns the error result for the given result code. This is called /// in the situation that kqueue fails to enqueue the completion or /// a raw s...
- `Writeable` **(Many-Argument Workhorses)** (@ `src/watcher/stream.zig`) -> Impact: **70.9** | LOC: 418
- `tick` **(Many-Argument Workhorses)** (@ `src/backend/kqueue.zig`) -> Impact: **70.0** | LOC: 257
  * *Intent:* /// Tick through the event loop once, waiting for at least "wait" completions /// to be processed by the loop itself.
- `tick` **(Many-Argument Workhorses)** (@ `src/backend/epoll.zig`) -> Impact: **66.9** | LOC: 194
  * *Intent:* /// Tick through the event loop once, waiting for at least "wait" completions /// to be processed by the loop itself.
- `tick` **(Many-Argument Workhorses)** (@ `src/backend/wasi_poll.zig`) -> Impact: **62.7** | LOC: 180
  * *Intent:* /// Tick through the event loop once, waiting for at least "wait" completions /// to be processed by the loop itself.
- `tick` **(Many-Argument Workhorses)** (@ `src/backend/iocp.zig`) -> Impact: **57.7** | LOC: 184
  * *Intent:* /// Tick through the event loop once, waiting for at least "wait" completions to be processed by /// the loop itself.

*Function archetypes referenced above:*
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src/watcher` | 8 | 2847.2 | 4.77% | 46.84% |
| `src/backend` | 5 | 2806.5 | 8.92% | 58.27% |
| `src` | 13 | 1559.02 | 15.62% | 24.31% |
| `src/bench` | 12 | 372.48 | 16.7% | 25.25% |
| `__monolith__` | 5 | 131.32 | 1.15% | 2.13% |
| `examples` | 5 | 121.52 | 24.39% | 0.0% |
| `include` | 1 | 61.4 | 0.0% | 25.51% |
| `website` | 4 | 36.56 | 1.38% | 9.44% |
| `.github/workflows` | 1 | 33.16 | 0.0% | 99.83% |
| `src/linux` | 1 | 27.74 | 3.42% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `.github/workflows/test.yml` -> **99.8256%** Exposure
- `src/heap.zig` -> **95.8477%** Exposure
- `src/queue_mpsc.zig` -> **95.5022%** Exposure
- `src/watcher/timer.zig` -> **79.4712%** Exposure
- `src/backend/iocp.zig` -> **70.1334%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `src/heap.zig` -> **99.998%** Exposure
- `src/queue.zig` -> **99.9955%** Exposure
- `src/ThreadPool.zig` -> **99.9714%** Exposure
- `src/queue_mpsc.zig` -> **99.95%** Exposure
- `src/bench/async1.zig` -> **99.7916%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/backend/iocp.zig` -> **0** Orphaned Functions | **15** Duplicates
- `src/backend/kqueue.zig` -> **0** Orphaned Functions | **12** Duplicates
- `src/backend/epoll.zig` -> **0** Orphaned Functions | **11** Duplicates
- `src/watcher/file.zig` -> **0** Orphaned Functions | **10** Duplicates
- `src/watcher/tcp.zig` -> **0** Orphaned Functions | **10** Duplicates

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
- **Unknown Dependencies:** `146` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/backend/kqueue.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 9.028)
- **Top Global Matches:** file_cluster_12: 9.028, file_cluster_7: 9.522, file_cluster_5: 10.858
- **Magnitude:** 760.22 | **LOC:** 2900 | **CtrlFlow:** 10.5% | **Authorship Centralization:** 40.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **9**; blast radius 10.445; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Mutation Surface (formerly State Flux) (72.6%), Guard Balance (formerly Safety Score) (64.1%), Connectivity (formerly Api Exposure) (50.4%)
- **Documentation Coverage:** 47.4359% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `perform` **(Defensive Guards)** (Impact: 85.7)
    * *Intent:* /// Perform the operation associated with this completion. This will /// perform the full blocking o...
  * `syscall_result` **(Many-Argument Workhorses)** (Impact: 80.0)
    * *Intent:* /// Returns the error result for the given result code. This is called /// in the situation that kqu...
  * `tick` **(Many-Argument Workhorses)** (Impact: 70.0)
    * *Intent:* /// Tick through the event loop once, waiting for at least "wait" completions /// to be processed by...
  * `start` **(Many-Argument Workhorses)** (Impact: 34.1)
    * *Intent:* /// Start the completion. This returns true if the Kevent was set /// and should be queued.
  * `submit` **(Compute Cores)** (Impact: 24.4)
    * *Intent:* /// Submit any enqueue completions. This does not fire any callbacks /// for completed events (succe...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 35 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 171
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 212`, `structural_boundaries: 275`, `args: 64`, `func_start: 64`, `class_start: 27`
* *Risk/State:* `safety_bypasses: 137`, `high_risk_execution: 2`, `state_mutation: 101`, `dead_code: 1`, `planned_debt: 5`, `duplicate_logic: 12`
* *Architecture:* `io: 8`, `api: 33`, `concurrency: 2`, `import: 9`
* *Defense:* `safety: 234`, `doc: 179`, `test: 13`, `cleanup: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 10.445
  * `Choke Point (Betweenness):` 0.00171 | `Ripple Effect (Closeness):` 0.141013
  * `Imports (Out-Degree: 7):` ThreadPool.zig, darwin.zig, heap.zig, loop.zig, main.zig, queue.zig, queue_mpsc.zig, builtin...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/watcher/stream.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.918)
- **Top Global Matches:** file_cluster_4: 7.918, file_cluster_12: 10.891, file_cluster_6: 11.808
- **Magnitude:** 734.12 | **LOC:** 1444 | **CtrlFlow:** 9.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **4**; blast radius 34.905; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (76.1%), Guard Balance (formerly Safety Score) (48.9%), Debt Markers (formerly Tech Debt) (31.8%)
- **Documentation Coverage:** 65.3846% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Writeable` **(Many-Argument Workhorses)** (Impact: 70.9)
  * `Stream` **(Defensive Guards)** (Impact: 47.1)
    * *Intent:* /// Creates a stream type that is meant to be embedded within other types. /// A stream is something...
  * `read` **(Many-Argument Workhorses)** (Impact: 44.5)
    * *Intent:* /// Read from the socket. This performs a single read. The callback must /// requeue the read if add...
  * `Readable` **(Many-Argument Workhorses)** (Impact: 42.8)
  * `Pollable` **(Many-Argument Workhorses)** (Impact: 41.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 41
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 108`, `structural_boundaries: 101`, `args: 48`, `func_start: 48`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 31`, `state_mutation: 21`, `duplicate_logic: 8`
* *Architecture:* `io: 17`, `api: 49`, `import: 4`
* *Defense:* `safety: 69`, `doc: 85`, `test: 4`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 34.905
  * `Choke Point (Betweenness):` 0.004719 | `Ripple Effect (Closeness):` 0.207804
  * `Imports (Out-Degree: 2):` queue.zig, builtin, common.zig, std
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `src/backend/iocp.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 9.788)
- **Top Global Matches:** file_cluster_12: 9.788, file_cluster_7: 10.122, file_cluster_5: 11.255
- **Magnitude:** 591.94 | **LOC:** 2377 | **CtrlFlow:** 8.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 10.445; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (70.1%), Guard Balance (formerly Safety Score) (66.3%), Mutation Surface (formerly State Flux) (63.4%)
- **Documentation Coverage:** 45.8333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `start_completion` **(Many-Argument Workhorses)** (Impact: 98.9)
    * *Intent:* // Start the completion.
  * `tick` **(Many-Argument Workhorses)** (Impact: 57.7)
    * *Intent:* /// Tick through the event loop once, waiting for at least "wait" completions to be processed by ///...
  * `perform` **(Compute Cores)** (Impact: 51.5)
    * *Intent:* /// Perform the operation associated with this completion. This will perform the full blocking /// o...
  * `stop_completion` **(Many-Argument Workhorses)** (Impact: 26.6)
    * *Intent:* /// Stop the completion. Fill `cancel_result` if it is non-null.
  * `callback` **(Type Conversions)** (Impact: 11.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 26 instances
* *State Mutation (weighted view):* 127
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 139`, `structural_boundaries: 258`, `args: 52`, `func_start: 52`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 124`, `high_risk_execution: 1`, `state_mutation: 75`, `dead_code: 1`, `planned_debt: 2`, `duplicate_logic: 15`
* *Architecture:* `io: 6`, `api: 40`, `concurrency: 1`, `import: 6`
* *Defense:* `safety: 179`, `doc: 147`, `test: 14`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 10.445
  * `Choke Point (Betweenness):` 0.00171 | `Ripple Effect (Closeness):` 0.142712
  * `Imports (Out-Degree: 4):` heap.zig, loop.zig, queue.zig, windows.zig, builtin, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/backend/epoll.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 9.758)
- **Top Global Matches:** file_cluster_12: 9.758, file_cluster_4: 10.272, file_cluster_7: 10.71
- **Magnitude:** 547.66 | **LOC:** 2062 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **9**; blast radius 10.445; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (64.9%), Mutation Surface (formerly State Flux) (64.5%), Connectivity (formerly Api Exposure) (51.7%), Guard Balance (formerly Safety Score) (45.7%)
- **Documentation Coverage:** 40.678% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `start` **(Many-Argument Workhorses)** (Impact: 99.6)
  * `tick` **(Many-Argument Workhorses)** (Impact: 66.9)
    * *Intent:* /// Tick through the event loop once, waiting for at least "wait" completions /// to be processed by...
  * `perform` **(Defensive Guards)** (Impact: 51.1)
    * *Intent:* /// Perform the operation associated with this completion. This will /// perform the full blocking o...
  * `stop_completion` **(Many-Argument Workhorses)** (Impact: 23.5)
  * `callback` **(Type Conversions)** (Impact: 11.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 24 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 110
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 163`, `structural_boundaries: 216`, `args: 45`, `func_start: 45`, `class_start: 23`
* *Risk/State:* `safety_bypasses: 79`, `high_risk_execution: 2`, `state_mutation: 62`, `planned_debt: 3`, `fragile_debt: 1`, `duplicate_logic: 11`
* *Architecture:* `io: 8`, `api: 31`, `import: 9`
* *Defense:* `safety: 218`, `doc: 142`, `test: 12`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 10.445
  * `Choke Point (Betweenness):` 0.000101 | `Ripple Effect (Closeness):` 0.141013
  * `Imports (Out-Degree: 7):` ThreadPool.zig, heap.zig, timerfd.zig, loop.zig, main.zig, queue.zig, queue_mpsc.zig, builtin...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/backend/io_uring.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 10.736)
- **Top Global Matches:** file_cluster_12: 10.736, file_cluster_4: 10.983, file_cluster_7: 11.257
- **Magnitude:** 480.06 | **LOC:** 1792 | **CtrlFlow:** 9.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 10.445; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (53.6%), Guard Balance (formerly Safety Score) (48.0%), Mutation Surface (formerly State Flux) (47.7%), Debt Markers (formerly Tech Debt) (43.1%)
- **Documentation Coverage:** 48.2143% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `invoke` **(Many-Argument Workhorses)** (Impact: 109.5)
    * *Intent:* /// Invokes the callback for this completion after properly constructing /// the Result based on the...
  * `add_` **(Many-Argument Workhorses)** (Impact: 44.2)
    * *Intent:* /// Internal add function. The only difference is try_submit. If try_submit /// is true, then this f...
  * `tick_` **(Defensive Guards)** (Impact: 36.4)
    * *Intent:* /// Tick the loop. The mode is comptime so we can do some tricks to /// avoid function calls and run...
  * `readResult` **(Defensive Guards)** (Impact: 19.1)
  * `cancel` **(Many-Argument Workhorses)** (Impact: 15.1)
    * *Intent:* /// Submits a completion cancelation request. /// Results in error.NotFound if the completion couldn...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 17 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 72
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 115`, `structural_boundaries: 152`, `args: 40`, `func_start: 40`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 78`, `high_risk_execution: 1`, `state_mutation: 38`, `planned_debt: 4`, `fragile_debt: 1`, `duplicate_logic: 6`
* *Architecture:* `io: 6`, `api: 33`, `import: 5`
* *Defense:* `safety: 156`, `doc: 157`, `test: 14`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 10.445
  * `Choke Point (Betweenness):` 0.000101 | `Ripple Effect (Closeness):` 0.142712
  * `Imports (Out-Degree: 3):` timerfd.zig, loop.zig, queue.zig, builtin, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/backend/wasi_poll.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 9.102)
- **Top Global Matches:** file_cluster_12: 9.102, file_cluster_7: 9.859, file_cluster_4: 10.855
- **Magnitude:** 426.62 | **LOC:** 1649 | **CtrlFlow:** 9.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 10.445; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (81.9%), Debt Markers (formerly Tech Debt) (65.5%), Guard Balance (formerly Safety Score) (58.8%), Connectivity (formerly Api Exposure) (55.5%)
- **Documentation Coverage:** 36.5385% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `tick` **(Many-Argument Workhorses)** (Impact: 62.7)
    * *Intent:* /// Tick through the event loop once, waiting for at least "wait" completions /// to be processed by...
  * `perform` **(Defensive Guards)** (Impact: 44.8)
    * *Intent:* /// Perform the operation associated with this completion. This will /// perform the full blocking o...
  * `start` **(Defensive Guards)** (Impact: 22.2)
  * `stop_completion` **(Many-Argument Workhorses)** (Impact: 18.1)
  * `timer_reset` **(Many-Argument Workhorses)** (Impact: 9.9)
    * *Intent:* /// See io_uring.timer_reset for docs.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 24 instances
* *State Mutation (weighted view):* 112
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 103`, `structural_boundaries: 159`, `args: 36`, `func_start: 36`, `class_start: 24`
* *Risk/State:* `safety_bypasses: 66`, `state_mutation: 64`, `planned_debt: 3`, `duplicate_logic: 9`
* *Architecture:* `io: 4`, `api: 36`, `concurrency: 1`, `import: 5`
* *Defense:* `safety: 137`, `doc: 129`, `test: 8`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 10.445
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.141013
  * `Imports (Out-Degree: 3):` heap.zig, main.zig, queue.zig, builtin, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/ThreadPool.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.393)
- **Top Global Matches:** file_cluster_12: 7.393, file_cluster_7: 8.709, file_cluster_5: 10.02
- **Magnitude:** 414.06 | **LOC:** 828 | **CtrlFlow:** 18.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **1**; blast radius 22.961; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Concurrency Surface (formerly Concurrency) (66.8%), Guard Balance (formerly Safety Score) (61.4%)
- **Documentation Coverage:** 43.75% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `wait` **(Type Conversions)** (Impact: 25.3)
  * `notifySlow` **(Type Conversions)** (Impact: 24.8)
  * `pop` **(Defensive Guards)** (Impact: 19.7)
    * *Intent:* /// Try to dequeue a Node/Task from the ThreadPool. /// Spurious reports of dequeue() returning empt...
  * `push` **(Many-Argument Workhorses)** (Impact: 16.8)
  * `steal` **(Many-Argument Workhorses)** (Impact: 15.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 43 instances
* *Concurrency (weighted view):* 19
* *State Mutation (weighted view):* 142
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 97`, `structural_boundaries: 91`, `args: 27`, `func_start: 26`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 56`, `planned_debt: 4`
* *Architecture:* `api: 9`, `concurrency: 9`, `import: 1`
* *Defense:* `safety: 38`, `doc: 74`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 22.961
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.162514
  * `Imports (Out-Degree: 0):` std
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `src/watcher/tcp.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.853)
- **Top Global Matches:** file_cluster_4: 8.853, file_cluster_12: 9.619, file_cluster_5: 10.714
- **Magnitude:** 412.62 | **LOC:** 936 | **CtrlFlow:** 7.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **5**; blast radius 16.516; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (67.8%), Connectivity (formerly Api Exposure) (61.2%), Guard Balance (formerly Safety Score) (44.6%), Mutation Surface (formerly State Flux) (12.1%)
- **Documentation Coverage:** 75.3846% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TCPTests` **(Defensive Guards)** (Impact: 56.2)
  * `TCPDynamic` **(Compute Cores)** (Impact: 42.5)
  * `TCPStream` **(Defensive Guards)** (Impact: 40.8)
  * `accept` **(Many-Argument Workhorses)** (Impact: 16.0)
  * `connect` **(Many-Argument Workhorses)** (Impact: 13.6)
    * *Intent:* /// Establish a connection as a client.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 8
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 93`, `args: 42`, `func_start: 42`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 4`, `dead_code: 3`, `duplicate_logic: 10`
* *Architecture:* `io: 17`, `api: 30`, `import: 5`
* *Defense:* `safety: 81`, `doc: 20`, `test: 3`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 16.516
  * `Choke Point (Betweenness):` 0.00184 | `Ripple Effect (Closeness):` 0.166832
  * `Imports (Out-Degree: 4):` ThreadPool.zig, builtin, common.zig, std, stream.zig
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/watcher/udp.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.289)
- **Top Global Matches:** file_cluster_12: 7.289, file_cluster_5: 8.378, file_cluster_7: 9.191
- **Magnitude:** 374.7 | **LOC:** 1004 | **CtrlFlow:** 4.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **5**; blast radius 16.516; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (62.7%), Debt Markers (formerly Tech Debt) (56.3%), Guard Balance (formerly Safety Score) (52.7%), Mutation Surface (formerly State Flux) (37.6%)
- **Documentation Coverage:** 45.5882% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `UDPDynamic` **(Compute Cores)** (Impact: 32.1)
  * `UDPSendMsg` **(I/O & Config Routines)** (Impact: 23.1)
    * *Intent:* /// UDP implementation that uses sendmsg/recvmsg
  * `write` **(Many-Argument Workhorses)** (Impact: 21.1)
    * *Intent:* /// Write to the socket. This performs a single write. Additional writes /// can be queued by callin...
  * `read` **(Many-Argument Workhorses)** (Impact: 19.9)
    * *Intent:* /// Read from the socket. This performs a single read. The callback must /// requeue the read if add...
  * `UDPTests` **(Defensive Guards)** (Impact: 15.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 40
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 51`, `args: 39`, `func_start: 39`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 33`, `state_mutation: 20`, `planned_debt: 1`, `duplicate_logic: 6`
* *Architecture:* `io: 32`, `api: 34`, `import: 5`
* *Defense:* `safety: 40`, `doc: 55`, `test: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 16.516
  * `Choke Point (Betweenness):` 0.00184 | `Ripple Effect (Closeness):` 0.166832
  * `Imports (Out-Degree: 4):` ThreadPool.zig, builtin, common.zig, std, stream.zig
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/watcher/async.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.845)
- **Top Global Matches:** file_cluster_12: 6.845, file_cluster_5: 8.796, file_cluster_15: 9.213
- **Magnitude:** 373.36 | **LOC:** 829 | **CtrlFlow:** 7.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **4**; blast radius 16.516; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (60.5%), Debt Markers (formerly Tech Debt) (54.2%), Guard Balance (formerly Safety Score) (44.0%), Mutation Surface (formerly State Flux) (22.5%)
- **Documentation Coverage:** 58.4615% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `AsyncMachPort` **(Compute Cores)** (Impact: 30.8)
    * *Intent:* /// Async implementation using mach ports (Darwin). /// /// This allocates a mach port per async req...
  * `AsyncEventFd` **(Defensive Guards)** (Impact: 26.2)
    * *Intent:* /// Async implementation using eventfd (Unix/Linux).
  * `AsyncDynamic` **(Defensive Guards)** (Impact: 17.7)
  * `AsyncLoopState` **(Many-Argument Workhorses)** (Impact: 16.2)
    * *Intent:* /// Async implementation that is deferred to the backend implementation /// loop state. This is kind...
  * `waitPoll` **(Many-Argument Workhorses)** (Impact: 16.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 62`, `args: 41`, `func_start: 41`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 10`, `planned_debt: 2`, `duplicate_logic: 4`
* *Architecture:* `io: 6`, `api: 27`, `concurrency: 1`, `import: 4`
* *Defense:* `safety: 56`, `doc: 62`, `test: 3`, `sync_locks: 5`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 16.516
  * `Choke Point (Betweenness):` 0.004623 | `Ripple Effect (Closeness):` 0.166832
  * `Imports (Out-Degree: 3):` darwin.zig, builtin, common.zig, std
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/watcher/file.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.764)
- **Top Global Matches:** file_cluster_12: 8.764, file_cluster_4: 9.229, file_cluster_5: 9.851
- **Magnitude:** 344.36 | **LOC:** 976 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **5**; blast radius 16.516; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (65.8%), Connectivity (formerly Api Exposure) (56.3%), Guard Balance (formerly Safety Score) (46.4%), Mutation Surface (formerly State Flux) (19.9%)
- **Documentation Coverage:** 78.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `FileStream` **(Many-Argument Workhorses)** (Impact: 47.5)
    * *Intent:* /// An implementation of File that uses the stream abstractions.
  * `FileTests` **(Defensive Guards)** (Impact: 46.8)
  * `pread` **(Many-Argument Workhorses)** (Impact: 24.7)
  * `FileDynamic` **(Compute Cores)** (Impact: 21.2)
  * `queuePWrite` **(Many-Argument Workhorses)** (Impact: 16.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 20
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 121`, `args: 34`, `func_start: 34`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 12`, `duplicate_logic: 10`
* *Architecture:* `io: 18`, `api: 23`, `import: 5`
* *Defense:* `safety: 77`, `doc: 25`, `test: 7`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 16.516
  * `Choke Point (Betweenness):` 0.00127 | `Ripple Effect (Closeness):` 0.166832
  * `Imports (Out-Degree: 4):` main.zig, builtin, common.zig, std, stream.zig
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/watcher/timer.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.208)
- **Top Global Matches:** file_cluster_12: 8.208, file_cluster_5: 9.191, file_cluster_4: 9.972
- **Magnitude:** 310.18 | **LOC:** 642 | **CtrlFlow:** 6.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **2**; blast radius 16.516; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (79.5%), Connectivity (formerly Api Exposure) (53.4%), Guard Balance (formerly Safety Score) (43.9%), Mutation Surface (formerly State Flux) (11.0%)
- **Documentation Coverage:** 65.7895% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TimerLoop` **(Type Conversions)** (Impact: 38.9)
    * *Intent:* /// An implementation that uses the loop timer methods.
  * `cancel` **(Many-Argument Workhorses)** (Impact: 32.0)
    * *Intent:* /// Cancel a previously started timer. The timer to cancel used the completion /// "c_cancel". A new...
  * `TimerDynamic` **(Compute Cores)** (Impact: 24.6)
  * `reset` **(Many-Argument Workhorses)** (Impact: 19.8)
    * *Intent:* /// Reset a timer to execute in next_ms milliseconds. If the timer /// is already started, this will...
  * `run` **(Many-Argument Workhorses)** (Impact: 18.7)
    * *Intent:* /// This will use the monotonic clock on your system if available so /// this is immune to system cl...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 4
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 61`, `args: 27`, `func_start: 27`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 2`, `duplicate_logic: 8`
* *Architecture:* `io: 1`, `api: 16`, `import: 2`
* *Defense:* `safety: 52`, `doc: 43`, `test: 5`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 16.516
  * `Choke Point (Betweenness):` 3.4e-05 | `Ripple Effect (Closeness):` 0.166832
  * `Imports (Out-Degree: 1):` builtin, std
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/watcher/process.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.032)
- **Top Global Matches:** file_cluster_12: 7.032, file_cluster_5: 8.258, file_cluster_15: 9.681
- **Magnitude:** 293.08 | **LOC:** 573 | **CtrlFlow:** 8.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **4**; blast radius 16.516; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (56.5%), Guard Balance (formerly Safety Score) (45.5%), Debt Markers (formerly Tech Debt) (19.4%), Mutation Surface (formerly State Flux) (12.2%)
- **Documentation Coverage:** 60.5263% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `wait` **(Many-Argument Workhorses)** (Impact: 38.5)
  * `callback` **(Many-Argument Workhorses)** (Impact: 31.9)
  * `ProcessIocp` **(Defensive Guards)** (Impact: 26.4)
  * `ProcessPidFd` **(Compute Cores)** (Impact: 17.1)
    * *Intent:* /// Process implementation using pidfd (Linux).
  * `wait` **(Many-Argument Workhorses)** (Impact: 16.6)
    * *Intent:* /// Wait for the process to exit. This will automatically call /// `waitpid` or equivalent and repor...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 5
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 67`, `args: 25`, `func_start: 25`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 3`, `duplicate_logic: 2`
* *Architecture:* `io: 3`, `api: 18`, `import: 4`
* *Defense:* `safety: 38`, `doc: 14`, `test: 3`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 16.516
  * `Choke Point (Betweenness):` 0.004623 | `Ripple Effect (Closeness):` 0.166832
  * `Imports (Out-Degree: 3):` windows.zig, builtin, common.zig, std
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/dynamic.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.182)
- **Top Global Matches:** file_cluster_12: 8.182, file_cluster_0: 8.488, file_cluster_15: 8.87
- **Magnitude:** 289.08 | **LOC:** 525 | **CtrlFlow:** 13.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **15** in-repo importer(s); it depends on **11**; blast radius 85.617; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (73.8%), Mutation Surface (formerly State Flux) (63.8%), Guard Balance (formerly Safety Score) (44.4%), Complexity Load (formerly Cognitive Load) (9.2%)
- **Documentation Coverage:** 49.2063% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Xev` **(Defensive Guards)** (Impact: 44.2)
    * *Intent:* /// The goal of this API is to match the static Xev() (in main.zig) /// API as closely as possible. ...
  * `Union` **(Many-Argument Workhorses)** (Impact: 14.4)
    * *Intent:* /// Creates a union type that can hold the implementation of a given /// backend by common field nam...
  * `DynamicCompletion` **(Compute Cores)** (Impact: 11.1)
  * `DynamicReadBuffer` **(Compute Cores)** (Impact: 9.1)
  * `DynamicPollEvent` **(Defensive Guards)** (Impact: 8.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 46`, `args: 31`, `func_start: 31`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 9`
* *Architecture:* `io: 1`, `api: 57`, `import: 12`
* *Defense:* `safety: 31`, `doc: 76`, `test: 5`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 85.617
  * `Choke Point (Betweenness):` 0.095343 | `Ripple Effect (Closeness):` 0.263224
  * `Imports (Out-Degree: 9):` builtin, loop.zig, main.zig, std, async.zig, file.zig, process.zig, stream.zig...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `src/heap.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.758)
- **Top Global Matches:** file_cluster_4: 6.758, file_cluster_15: 9.572, file_cluster_16: 10.741
- **Magnitude:** 209.92 | **LOC:** 380 | **CtrlFlow:** 8.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **1**; blast radius 18.161; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (95.8%), Guard Balance (formerly Safety Score) (49.8%), Connectivity (formerly Api Exposure) (44.5%)
- **Documentation Coverage:** 30.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Intrusive` **(Many-Argument Workhorses)** (Impact: 47.1)
    * *Intent:* /// (rather, shifting allocation up to the consumer which can choose how they /// want the memory to...
  * `meld` **(Many-Argument Workhorses)** (Impact: 12.1)
    * *Intent:* /// Meld (union) two heaps together. This isn't a generalized /// union. It assumes that a.heap.next...
  * `remove` **(Defensive Guards)** (Impact: 11.8)
    * *Intent:* /// Remove the value v from the heap.
  * `combine_siblings` **(Defensive Guards)** (Impact: 11.4)
    * *Intent:* /// Combine the siblings of the leftmost value "left" into a single /// new rooted with the minimum ...
  * `deleteMin` **(Defensive Guards)** (Impact: 6.3)
    * *Intent:* /// Delete the minimum value from the heap and return it.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 29 instances
* *State Mutation (weighted view):* 88
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 52`, `args: 14`, `func_start: 14`, `class_start: 6`
* *Risk/State:* `state_mutation: 30`, `duplicate_logic: 6`
* *Architecture:* `api: 6`, `import: 1`
* *Defense:* `safety: 38`, `doc: 37`, `test: 6`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 18.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.156495
  * `Imports (Out-Degree: 0):` std
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/c_api.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 8.072)
- **Top Global Matches:** file_cluster_7: 8.072, file_cluster_12: 9.458, file_cluster_5: 10.438
- **Magnitude:** 167.18 | **LOC:** 361 | **CtrlFlow:** 4.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 10.445; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (78.4%), Debt Markers (formerly Tech Debt) (64.9%), Connectivity (formerly Api Exposure) (64.4%), Mutation Surface (formerly State Flux) (48.8%)
- **Documentation Coverage:** 98.5294% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `xev_timer_reset` **(Many-Argument Workhorses)** (Impact: 10.4)
  * `xev_timer_run` **(Type Conversions)** (Impact: 9.8)
  * `xev_timer_cancel` **(Type Conversions)** (Impact: 9.8)
  * `xev_async_wait` **(Type Conversions)** (Impact: 9.2)
  * `callback` **(Type Conversions)** (Impact: 7.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 17
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 19`, `args: 34`, `func_start: 33`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 15`, `planned_debt: 2`, `duplicate_logic: 2`
* *Architecture:* `api: 27`, `import: 3`
* *Defense:* `safety: 28`, `doc: 5`, `test: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 10.445
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.141013
  * `Imports (Out-Degree: 3):` builtin, main.zig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/windows.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.07)
- **Top Global Matches:** file_cluster_12: 7.07, file_cluster_15: 8.729, file_cluster_2: 9.491
- **Magnitude:** 140.58 | **LOC:** 252 | **CtrlFlow:** 10.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **1**; blast radius 14.344; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (93.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (52.0%), Complexity Load (formerly Cognitive Load) (6.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CreateFile` **(Many-Argument Workhorses)** (Impact: 12.3)
  * `SetInformationJobObject` **(Many-Argument Workhorses)** (Impact: 9.9)
  * `ReadFile` **(Type Conversions)** (Impact: 8.8)
  * `WriteFile` **(Type Conversions)** (Impact: 8.8)
  * `AssignProcessToJobObject` **(Compute Cores)** (Impact: 7.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 12`, `args: 12`, `func_start: 12`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 4`
* *Architecture:* `io: 2`, `api: 68`, `import: 1`
* *Defense:* `safety: 1`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 14.344
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.140845
  * `Imports (Out-Degree: 0):` std
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/bench/ping-pongs.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.917)
- **Top Global Matches:** file_cluster_12: 7.917, file_cluster_7: 8.31, file_cluster_5: 9.981
- **Magnitude:** 93.56 | **LOC:** 362 | **CtrlFlow:** 2.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 7.444; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (46.4%), Mutation Surface (formerly State Flux) (24.0%), Concurrency Surface (formerly Concurrency) (14.9%), Debt Markers (formerly Tech Debt) (10.4%)
- **Documentation Coverage:** 85.1852% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `readCallback` **(Many-Argument Workhorses)** (Impact: 12.3)
  * `readCallback` **(Many-Argument Workhorses)** (Impact: 9.6)
  * `main` **(Defensive Guards)** (Impact: 4.5)
  * `writeCallback` **(Many-Argument Workhorses)** (Impact: 3.7)
  * `writeCallback` **(Many-Argument Workhorses)** (Impact: 3.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 2 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 45`, `args: 19`, `func_start: 19`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 5`, `dead_code: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 3`, `api: 10`, `concurrency: 1`, `import: 2`
* *Defense:* `safety: 39`, `doc: 5`, `cleanup: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` std, xev
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/queue_mpsc.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.887)
- **Top Global Matches:** file_cluster_12: 8.887, file_cluster_9: 9.252, file_cluster_15: 10.405
- **Magnitude:** 89.44 | **LOC:** 117 | **CtrlFlow:** 6.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **1**; blast radius 12.982; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (95.5%), Complexity Load (formerly Cognitive Load) (49.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Intrusive` **(Defensive Guards)** (Impact: 11.4)
    * *Intent:* /// This is an implementatin of a Vyukov Queue[1]. /// TODO(mitchellh): I haven't audited yet if I g...
  * `pop` **(Defensive Guards)** (Impact: 9.9)
    * *Intent:* /// Pop the first in element from the queue. This must be called /// by only a single consumer at an...
  * `push` **(State Mutators)** (Impact: 2.0)
    * *Intent:* /// Push an item onto the queue. This can be called by any number /// of producers.
  * `init` **(State Mutators)** (Impact: 1.7)
    * *Intent:* /// Initialize the queue. This requires a stable pointer to itself. /// This must be called before t...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 5 instances
* *Concurrency (weighted view):* 41
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 10`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 8`, `planned_debt: 8`
* *Architecture:* `api: 4`, `concurrency: 11`, `import: 1`
* *Defense:* `safety: 15`, `doc: 24`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 12.982
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.150905
  * `Imports (Out-Degree: 0):` std
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `build.zig` (ZIG | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.996)
- **Top Global Matches:** file_cluster_8: 7.996, file_cluster_6: 10.002, file_cluster_4: 18.188
- **Magnitude:** 80.14 | **LOC:** 331 | **CtrlFlow:** 12.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 7.444; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (10.7%), Complexity Load (formerly Cognitive Load) (5.8%), Connectivity (formerly Api Exposure) (2.4%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 30.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `build` **(Defensive Guards)** (Impact: 40.5)
    * *Intent:* /// A note on my build.zig style: I try to create all the artifacts first, /// unattached to any ste...
  * `buildExamples` **(Many-Argument Workhorses)** (Impact: 19.6)
  * `buildBenchmarks` **(Defensive Guards)** (Impact: 9.3)
  * `manPages` **(Defensive Guards)** (Impact: 4.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 32`, `args: 4`, `func_start: 4`
* *Risk/State:* `unreferenced_by_name: 1`
* *Architecture:* `io: 3`, `api: 1`, `import: 1`
* *Defense:* `safety: 34`, `doc: 6`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/bench/ping-udp1.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 7.58)
- **Top Global Matches:** file_cluster_7: 7.58, file_cluster_12: 7.819, file_cluster_5: 9.584
- **Magnitude:** 75.8 | **LOC:** 180 | **CtrlFlow:** 5.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 7.444; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.1%), Guard Balance (formerly Safety Score) (60.0%), Complexity Load (formerly Cognitive Load) (23.4%), Debt Markers (formerly Tech Debt) (13.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `readCallback` **(Many-Argument Workhorses)** (Impact: 17.0)
  * `run` **(Defensive Guards)** (Impact: 7.5)
  * `writeCallback` **(Many-Argument Workhorses)** (Impact: 6.7)
  * `closeCallback` **(Defensive Guards)** (Impact: 2.9)
  * `start` **(State Mutators)** (Impact: 2.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 7 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 21
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 17`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 7`, `dead_code: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 4`, `api: 10`, `import: 3`
* *Defense:* `safety: 16`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` builtin, std, xev
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/bench/async1.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 7.268)
- **Top Global Matches:** file_cluster_7: 7.268, file_cluster_12: 9.106, file_cluster_5: 9.824
- **Magnitude:** 65.48 | **LOC:** 108 | **CtrlFlow:** 9.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **2**; blast radius 26.428; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.9%), Mutation Surface (formerly State Flux) (99.8%), Guard Balance (formerly Safety Score) (77.6%), Complexity Load (formerly Cognitive Load) (61.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `mainAsyncCallback` **(Defensive Guards)** (Impact: 7.5)
  * `asyncCallback` **(Defensive Guards)** (Impact: 7.4)
  * `run` **(Defensive Guards)** (Impact: 7.0)
  * `threadMain` **(Defensive Guards)** (Impact: 3.4)
  * `init` **(Defensive Guards)** (Impact: 1.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 6 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 12
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 13`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 1`, `state_mutation: 6`, `dead_code: 1`
* *Architecture:* `api: 6`, `concurrency: 2`, `import: 2`
* *Defense:* `safety: 19`, `doc: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 26.428
  * `Choke Point (Betweenness):` 0.016298 | `Ripple Effect (Closeness):` 0.042254
  * `Imports (Out-Degree: 2):` std, xev
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `include/xev.h` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Centroid distance: 4.854)
- **Top Global Matches:** file_cluster_17: 4.854, file_cluster_2: 6.925, file_cluster_15: 7.091
- **Magnitude:** 61.4 | **LOC:** 104 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **2**; blast radius 71.039; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Guard Balance (formerly Safety Score) (43.4%), Debt Markers (formerly Tech Debt) (25.5%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 51`, `args: 9`, `class_start: 10`
* *Risk/State:* `state_mutation: 2`, `planned_debt: 2`
* *Architecture:* `api: 43`, `import: 2`
* *Defense:* `safety: 7`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 71.039
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.176975
  * `Imports (Out-Degree: 0):` stddef.h, stdint.h
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `examples/million-timers.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.597)
- **Top Global Matches:** file_cluster_11: 6.597, file_cluster_15: 6.955, file_cluster_16: 7.045
- **Magnitude:** 60.28 | **LOC:** 92 | **CtrlFlow:** 6.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 7.444; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (70.5%), Complexity Load (formerly Cognitive Load) (56.7%), Connectivity (formerly Api Exposure) (3.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(I/O & Config Routines)** (Impact: 7.2)
    * *Intent:* #endif
  * `hrtime` **(Encapsulated Accessors)** (Impact: 3.0)
    * *Intent:* #ifdef _WIN32 #include <windows.h>
  * `timer_cb` **(Parameter Forwarders)** (Impact: 2.4)
  * `hrtime` **(Interface Declarations)** (Impact: 1.2)
    * *Intent:* #else
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Cascading Flux:* 13 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 41
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 11`, `args: 6`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 15`, `unreferenced_by_name: 1`
* *Architecture:* `api: 4`, `import: 6`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.444
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` stdint.h, stdio.h, stdlib.h, time.h, windows.h, xev.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 9.104)
- **Top Global Matches:** file_cluster_2: 9.104, file_cluster_17: 9.111, file_cluster_13: 9.764
- **Magnitude:** 59.72 | **LOC:** 131 | **CtrlFlow:** 8.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **17**; blast radius 52.952; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Complexity Load (formerly Cognitive Load) (7.4%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 1`
* *Risk/State:* None
* *Architecture:* `api: 43`, `import: 19`
* *Defense:* `safety: 1`, `doc: 24`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 52.952
  * `Choke Point (Betweenness):` 0.081048 | `Ripple Effect (Closeness):` 0.211519
  * `Imports (Out-Degree: 15):` ThreadPool.zig, api.zig, backend.zig, epoll.zig, io_uring.zig, iocp.zig, kqueue.zig, wasi_poll.zig...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/backend.zig` (ZIG) | Magnitude: 19.9 | Delta: **0.077** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 46, branch: 9, import: 7, core_var_decl: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `src/main.zig` (ZIG) | Magnitude: 59.72 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: core_var_decl: 62, globals: 47, api: 43, design_pascal_case: 36

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `src/darwin.zig` (ZIG) | Magnitude: 54.76 | Delta: **0.084** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: doc: 143, core_var_decl: 138, design_upper_case: 120, indent_spaces: 111

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `.github/workflows/test.yml` -> Churn: **51.81%** | Cog Load: 0.0% | Debt: 99.8256%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/backend/io_uring.zig` -> **Buck McCready** (100.0% isolated ownership) | Magnitude: 480.06

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/dynamic.zig` -> **Severity: 6.084** (Bridge: 0.0953 * Flux: 63.8078%)
- `src/bench/async1.zig` -> **Severity: 1.626** (Bridge: 0.0163 * Flux: 99.7916%)
- `src/bench/async_pummel_1.zig` -> **Severity: 1.625** (Bridge: 0.0163 * Flux: 99.714%)
- `src/watcher/stream.zig` -> **Severity: 0.129** (Bridge: 0.0047 * Flux: 27.3855%)
- `src/backend/kqueue.zig` -> **Severity: 0.124** (Bridge: 0.0017 * Flux: 72.6336%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/linux/timerfd.zig` -> **Severity: 11.972** (Embedded: 0.1527 * Error Risk: 78.3871%)
- `src/dynamic.zig` -> **Severity: 11.687** (Embedded: 0.2632 * Error Risk: 44.3986%)
- `src/c_api.zig` -> **Severity: 11.061** (Embedded: 0.141 * Error Risk: 78.4429%)
- `src/watcher/stream.zig` -> **Severity: 10.168** (Embedded: 0.2078 * Error Risk: 48.9327%)
- `src/ThreadPool.zig` -> **Severity: 9.974** (Embedded: 0.1625 * Error Risk: 61.3745%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/dynamic.zig` -> **Severity: 4212.896** (Blast Radius: 85.617 * Doc Risk: 49.2063%)
- `src/bench/async1.zig` -> **Severity: 2642.8** (Blast Radius: 26.428 * Doc Risk: 100.0%)
- `src/bench/async_pummel_1.zig` -> **Severity: 2642.8** (Blast Radius: 26.428 * Doc Risk: 100.0%)
- `src/watcher/stream.zig` -> **Severity: 2282.249** (Blast Radius: 34.905 * Doc Risk: 65.3846%)
- `src/windows.zig` -> **Severity: 1434.4** (Blast Radius: 14.344 * Doc Risk: 100.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 2065 call pairs -- scoped 17.9%, unique 0.0%, ambiguous 11.3%, external 70.8%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| zig | 2021 | 18.3% | 0.0% | 11.6% | 70.2% |
| c | 41 | 2.4% | 0.0% | 0.0% | 97.6% |
| typescript | 2 | 0.0% | 0.0% | 0.0% | 100.0% |
| javascript | 1 | 0.0% | 0.0% | 0.0% | 100.0% |

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
