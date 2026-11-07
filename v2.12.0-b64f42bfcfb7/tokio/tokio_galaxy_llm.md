# ARCHITECTURAL_BRIEF: tokio
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/tokio-rs/tokio` |
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
- **Scope:** 801 analyzed artifact(s), 94915 LOC.
- **Load-bearing artifact:** `tokio-test/src/lib.rs` -- 100 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `tokio/src/io/mod.rs` -- pulls in 78 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `tokio/tests/async_send_sync.rs` at magnitude 1105.26 (structural weight, not risk).
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
| Total Artifacts | 843 |
| Analyzed Artifacts (Scanned) | 801 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 42 |
| Total LOC | 94915 |
| Volatility Index | 0.005 |
| % Scanned of codebase = | 95.0% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6136 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.283 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 34.8% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 5.9617 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 43 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUST | 768 | 93499 | 95.9% |
| MARKDOWN | 22 | 0 | 2.7% |
| YAML | 10 | 1368 | 1.2% |
| JSON | 1 | 48 | 0.1% |

## 4.1 SOURCE ENCODINGS
All 801 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Generic / Templated Code Files 24%, Declarative / Non-Code 17%, Encapsulated Accessors Files 14%, State Mutators Files 12%, Large Core Modules (3) 12%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 779 | 97.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 22 | 2.7% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 42*

**Composition by Extension & Reason:**
- `.toml`: 13x Unsupported Format (.toml), 5x Excluded (Unsupported Extension: '.toml')
- `no_extension`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.stderr`: 6x Excluded (Unsupported Extension: '.stderr')
- `.yml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.dic`: 1x Excluded (Unsupported Extension: '.dic')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 15.2 | 8.5 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 82.9 | 35.7 | 47.7 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 7.1 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 7.9 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 82.8 | 22.1 | 20.1 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 51.9 | 53.3 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 15.8 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 15.2 | 0.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 6.5 | 0.9 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 4.8 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 67.5 | 85.7 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 717 | 200 | 3 | `tokio/tests/rt_threaded.rs` |
| cleanup | 769 | 183 | 2 | `tokio/tests/sync_mpsc.rs` |
| guards | 3228 | 477 | 12 | `tokio/src/runtime/scheduler/multi_thread/worker.rs` |
| danger | 3632 | 368 | 12 | `tokio-util/tests/codecs.rs` |
| concurrency | 11191 | 605 | 34 | `tokio/tests/async_send_sync.rs` |
| connectivity | 5327 | 555 | 20 | `tokio/src/net/windows/named_pipe.rs` |
| io | 808 | 265 | 2 | `tokio/tests/async_send_sync.rs` |
| crypto | 0 | 0 | 0 | - |
| ipc | 169 | 42 | 0 | `tokio/tests/sync_mpsc.rs` |
| time | 113 | 73 | 0 | `tokio/src/time/instant.rs` |
| serialization | 1 | 1 | 0 | `examples/tinyhttp.rs` |
| regex | 0 | 0 | 0 | - |
| events | 533 | 83 | 1 | `tokio/tests/async_send_sync.rs` |
| tests | 5721 | 402 | 17 | `tokio/tests/sync_mpsc.rs` |
| docs | 49226 | 470 | 135 | `tokio/src/net/windows/named_pipe.rs` |
| debt | 589 | 164 | 2 | `tokio/src/net/windows/named_pipe.rs` |
| mutation | 14394 | 664 | 50 | `tokio/tests/macros_select.rs` |
| dead_code | 1588 | 255 | 6 | `tokio/tests/sync_mpsc.rs` |
| credential | 0 | 0 | 0 | - |
| threat | 42 | 3 | 0 | `tokio-util/tests/length_delimited.rs` |
| ml_ai | 40 | 18 | 0 | `tokio/src/runtime/scheduler/multi_thread/stats.rs` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.3333**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tokio/tests/async_send_sync.rs` (Hits: 90)
- `tokio/tests/fs_file.rs` (Hits: 35)
- `tokio/src/fs/file/tests.rs` (Hits: 28)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **lib.rs** (`tokio-test/src/lib.rs`) — 100 inbound connections
2. **async_read.rs** (`tokio/src/io/async_read.rs`) — 69 inbound connections
3. **async_write.rs** (`tokio/src/io/async_write.rs`) — 69 inbound connections
4. **mod.rs** (`tokio/src/loom/mod.rs`) — 68 inbound connections
5. **read_buf.rs** (`tokio/src/io/read_buf.rs`) — 59 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **mod.rs** (`tokio/src/io/mod.rs`) — 78 outbound dependencies
2. **mod.rs** (`tokio/src/io/util/mod.rs`) — 62 outbound dependencies
3. **mod.rs** (`tokio/src/fs/mod.rs`) — 57 outbound dependencies
4. **mod.rs** (`tokio/src/runtime/mod.rs`) — 57 outbound dependencies
5. **mod.rs** (`tokio/src/loom/std/mod.rs`) — 56 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `test_combination` **(Many-Argument Workhorses)** (@ `tokio/src/runtime/tests/task_combinations.rs`) -> Impact: **181.1** | LOC: 333
- `poll_acquire` **(Many-Argument Workhorses)** (@ `tokio/src/sync/batch_semaphore.rs`) -> Impact: **60.2** | LOC: 126
- `poll_notified` **(Many-Argument Workhorses)** (@ `tokio/src/sync/notify.rs`) -> Impact: **54.2** | LOC: 217
- `test_named_pipe_multi_client_ready` **(I/O & Config Routines)** (@ `tokio/tests/net_named_pipe.rs`) -> Impact: **52.9** | LOC: 178
- `fmt` **(Compute Cores)** (@ `tokio/src/io/interest.rs`) -> Impact: **46.2** | LOC: 58
- `windows_main` **(I/O & Config Routines)** (@ `examples/named-pipe-ready.rs`) -> Impact: **43.2** | LOC: 144
- `parse_knobs` **(Many-Argument Workhorses)** (@ `tokio-macros/src/entry.rs`) -> Impact: **41.8** | LOC: 155
- `build_config` **(Many-Argument Workhorses)** (@ `tokio-macros/src/entry.rs`) -> Impact: **40.5** | LOC: 95
- `poll_next_many` **(Many-Argument Workhorses)** (@ `tokio-stream/src/stream_map.rs`) -> Impact: **39.1** | LOC: 66
  * *Intent:* /// Polls to receive multiple items on this `StreamMap`, extending the provided `buffer`. /// /// This method returns: /// * `Poll::Pending` if no ite...
- `poll_copy` **(Many-Argument Workhorses)** (@ `tokio/src/io/util/copy.rs`) -> Impact: **38.3** | LOC: 140

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `tokio/tests` | 163 | 13503.8 | 18.87% | 0.0% |
| `tokio-util/tests` | 29 | 2700.38 | 17.15% | 0.0% |
| `tokio/src/sync` | 12 | 2329.22 | 16.23% | 34.23% |
| `tokio/src/io/util` | 37 | 1452.96 | 10.6% | 2.51% |
| `tokio/src/io` | 18 | 1244.62 | 12.65% | 23.12% |
| `benches` | 17 | 1240.98 | 48.83% | 5.81% |
| `tokio/src/runtime/tests` | 11 | 1237.34 | 22.13% | 0.0% |
| `tokio/src/runtime/scheduler/multi_thread` | 11 | 1118.62 | 15.26% | 7.29% |
| `tokio/src/runtime` | 13 | 1106.68 | 8.88% | 8.44% |
| `tokio/src/runtime/task` | 11 | 1092.26 | 10.99% | 15.37% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `tokio-util/src/task/abort_on_drop.rs` -> **100.0%** Exposure
- `tokio/src/io/async_write.rs` -> **100.0%** Exposure
- `tokio/src/net/unix/split.rs` -> **100.0%** Exposure
- `tokio/src/net/windows/named_pipe.rs` -> **100.0%** Exposure
- `tokio/src/signal/windows.rs` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `tokio/src/io/util/buf_writer.rs` -> **100.0%** Exposure
- `tokio/src/io/util/read_line.rs` -> **100.0%** Exposure
- `tokio/src/io/util/read_to_end.rs` -> **100.0%** Exposure
- `tokio/src/runtime/scheduler/util/time_alt.rs` -> **100.0%** Exposure
- `tokio/src/util/idle_notified_set.rs` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tokio/tests/sync_mpsc.rs` -> **89** Orphaned Functions | **0** Duplicates
- `tokio/tests/rt_common.rs` -> **46** Orphaned Functions | **0** Duplicates
- `tokio/src/net/windows/named_pipe.rs` -> **0** Orphaned Functions | **44** Duplicates
- `tokio/src/process/mod.rs` -> **32** Orphaned Functions | **5** Duplicates
- `tokio/tests/macros_select.rs` -> **37** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `6608` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `tokio/tests/async_send_sync.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.235)
- **Top Global Matches:** file_cluster_0: 8.235, file_cluster_13: 11.947, file_cluster_10: 12.571
- **Magnitude:** 1105.26 | **LOC:** 779 | **CtrlFlow:** 3.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 0.361; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (52.1%), Complexity Load (formerly Cognitive Load) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `as_raw_fd` **(State Mutators)** (Impact: 1.6)
  * `require_send` **(Generic / Templated Code)** (Impact: 1.5)
  * `require_sync` **(Generic / Templated Code)** (Impact: 1.5)
  * `require_unpin` **(Generic / Templated Code)** (Impact: 1.5)
  * `some_item` **(State Mutators)** (Impact: 1.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 145`, `args: 11`, `func_start: 7`, `class_start: 8`
* *Risk/State:* `high_risk_execution: 4`, `planned_debt: 2`, `duplicate_logic: 3`, `unreferenced_by_name: 1`
* *Architecture:* `io: 90`, `concurrency: 1080`, `import: 22`
* *Defense:* `sync_locks: 28`, `immutability_locks: 3`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.361
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` self::*, std::cell::Cell, std::future::Future, std::io::SeekFrom, std::net::SocketAddr, std::pin::Pin, std::rc::Rc, tokio::io::unix::*...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tokio/tests/rt_common.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.6)
- **Top Global Matches:** file_cluster_5: 7.6, file_cluster_7: 8.333, file_cluster_12: 8.943
- **Magnitude:** 694.5 | **LOC:** 1439 | **CtrlFlow:** 7.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **32**; blast radius 0.361; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (68.8%), Complexity Load (formerly Cognitive Load) (39.7%)
- **Documentation Coverage:** 95.3125% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `yield_defers_until_park_inner` **(Compute Cores)** (Impact: 18.7)
    * *Intent:* /// Implementation of `yield_defers_until_park` test. Returns `true` if the /// test passed.
  * `ping_pong_saturation` **(I/O & Config Routines)** (Impact: 10.1)
    * *Intent:* // Tests that the "next task" scheduler optimization is not able to starve // other tasks.
  * `wake_from_thread_local` **(Callbacks & Closures)** (Impact: 9.5)
  * `spawn_many_from_task` **(Annotated & Test Methods)** (Impact: 7.6)
  * `spawn_many_from_block_on` **(Annotated & Test Methods)** (Impact: 7.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Race Conditions:* 29 instances
* *Amplified Cascading Flux:* 15 instances
* *Concurrency (weighted view):* 411
* *Memory Alloc (weighted view):* 4
* *State Mutation (weighted view):* 47
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 73`, `structural_boundaries: 467`, `args: 95`, `func_start: 63`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 75`, `high_risk_execution: 6`, `state_mutation: 17`, `unreferenced_by_name: 46`
* *Architecture:* `io: 3`, `concurrency: 266`, `import: 34`
* *Defense:* `safety: 2`, `doc: 14`, `test: 82`, `sync_locks: 18`, `immutability_locks: 12`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.361
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` std::cell::RefCell, std::future::Future, std::future::poll_fn, std::pin::Pin, std::sync::Arc, std::sync::Barrier, std::sync::atomic::AtomicBool, std::sync::atomic::Ordering...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tokio/tests/sync_mpsc.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.054)
- **Top Global Matches:** file_cluster_5: 8.054, file_cluster_12: 9.397, file_cluster_7: 9.469
- **Magnitude:** 694.18 | **LOC:** 1513 | **CtrlFlow:** 6.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **20**; blast radius 0.361; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (49.0%), Guard Balance (formerly Safety Score) (48.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (8.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `try_reserve_many_full` **(Annotated & Test Methods)** (Impact: 9.1)
  * `drop_all_elements_during_panic` **(Annotated & Test Methods)** (Impact: 6.2)
  * `try_recv_unbounded` **(Annotated & Test Methods)** (Impact: 4.9)
  * `send_recv_many_unbounded` **(Annotated & Test Methods)** (Impact: 4.4)
  * `try_reserve_many_edge_cases` **(Annotated & Test Methods)** (Impact: 4.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Race Conditions:* 17 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 434
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 442`, `args: 100`, `func_start: 94`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 53`, `high_risk_execution: 11`, `state_mutation: 9`, `dead_code: 1`, `unreferenced_by_name: 89`
* *Architecture:* `api: 1`, `concurrency: 349`, `import: 20`
* *Defense:* `test: 292`, `sync_locks: 5`, `immutability_locks: 3`, `cleanup: 64`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.361
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` mpsc_stream, futures::future::FutureExt, std::fmt, std::future::Future, std::panic, std::sync::Arc, std::sync::atomic::AtomicUsize, std::sync::atomic::Ordering::Relaxed...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tokio/tests/macros_select.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.194)
- **Top Global Matches:** file_cluster_12: 7.194, file_cluster_7: 8.425, file_cluster_5: 9.359
- **Magnitude:** 604.32 | **LOC:** 761 | **CtrlFlow:** 4.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 0.361; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (62.4%), Complexity Load (formerly Cognitive Load) (50.0%), Connectivity (formerly Api Exposure) (2.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `biased_eventually_ready` **(Annotated & Test Methods)** (Impact: 8.8)
  * `join_with_select` **(Annotated & Test Methods)** (Impact: 6.7)
  * `select_streams` **(Annotated & Test Methods)** (Impact: 5.1)
  * `deterministic_select_multi_thread` **(Annotated & Test Methods)** (Impact: 5.1)
  * `select_is_budget_aware` **(Annotated & Test Methods)** (Impact: 4.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 43 instances
* *Amplified Cascading Flux:* 24 instances
* *Concurrency (weighted view):* 393
* *State Mutation (weighted view):* 98
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 162`, `args: 47`, `func_start: 42`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 18`, `high_risk_execution: 8`, `state_mutation: 50`, `unreferenced_by_name: 37`
* *Architecture:* `api: 1`, `concurrency: 178`, `import: 18`
* *Defense:* `test: 55`, `immutability_locks: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.361
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` futures::future, self::maybe_tokio_test, std::cell::Cell, std::future::poll_fn, std::mem, std::task::Poll::Ready, tokio::runtime::RngSeed, tokio::sync::mpsc...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tokio/tests/rt_threaded.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.391)
- **Top Global Matches:** file_cluster_5: 8.391, file_cluster_7: 8.921, file_cluster_12: 9.68
- **Magnitude:** 534.4 | **LOC:** 933 | **CtrlFlow:** 9.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **26**; blast radius 0.361; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (72.6%), Complexity Load (formerly Cognitive Load) (43.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (13.7%)
- **Documentation Coverage:** 92.8571% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_tuning` **(I/O & Config Routines)** (Impact: 22.7)
    * *Intent:* // Testing the tuning logic is tricky as it is inherently timing based, and more // of a heuristic t...
  * `many_multishot_futures` **(I/O & Config Routines)** (Impact: 13.2)
  * `drop_threadpool_drops_futures` **(Annotated & Test Methods)** (Impact: 8.8)
  * `blocking` **(Annotated & Test Methods)** (Impact: 8.3)
  * `wake_during_shutdown` **(Generic / Templated Code)** (Impact: 8.1)
    * *Intent:* /// Demonstrates tokio-rs/tokio#3869
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 6 instances
* *Amplified Race Conditions:* 32 instances
* *Amplified Cascading Flux:* 20 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 294
* *Memory Alloc (weighted view):* 13
* *State Mutation (weighted view):* 66
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 246`, `args: 58`, `func_start: 39`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 58`, `high_risk_execution: 1`, `state_mutation: 26`, `unreferenced_by_name: 28`
* *Architecture:* `io: 1`, `concurrency: 134`, `import: 17`
* *Defense:* `safety: 3`, `doc: 7`, `test: 42`, `sync_locks: 26`, `immutability_locks: 6`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.361
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` self::*, std::future::Future, std::future::poll_fn, std::pin::Pin, std::sync::Arc, std::sync::Mutex, std::sync::atomic::AtomicBool, std::sync::atomic::AtomicUsize...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tokio/src/runtime/scheduler/multi_thread/worker.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.624)
- **Top Global Matches:** file_cluster_0: 7.624, file_cluster_12: 8.001, file_cluster_5: 8.498
- **Magnitude:** 503.02 | **LOC:** 1508 | **CtrlFlow:** 12.0% | **Authorship Centralization:** 25.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **42**; blast radius 2.098; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (92.1%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (61.2%), Guard Balance (formerly Safety Score) (52.9%)
- **Documentation Coverage:** 80.8824% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `block_in_place` **(Compute Cores)** (Impact: 26.8)
  * `run` **(Many-Argument Workhorses)** (Impact: 24.2)
  * `run_task` **(Many-Argument Workhorses)** (Impact: 19.8)
  * `schedule_local` **(Many-Argument Workhorses)** (Impact: 17.3)
  * `park` **(Defensive Guards)** (Impact: 15.3)
    * *Intent:* /// Parks the worker thread while waiting for tasks to execute. /// /// This function checks if inde...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 31 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 113
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 111`, `structural_boundaries: 244`, `args: 69`, `func_start: 55`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 2`, `state_mutation: 51`
* *Architecture:* `api: 29`, `concurrency: 2`, `import: 18`
* *Defense:* `safety: 23`, `doc: 172`, `test: 10`, `sync_locks: 20`, `immutability_locks: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.098
  * `Choke Point (Betweenness):` 0.015718 | `Ripple Effect (Closeness):` 0.152728
  * `Imports (Out-Degree: 33):` metrics, taskdump, taskdump_mock, crate::loom::sync::Arc, crate::loom::sync::Mutex, crate::loom::sync::atomic::AtomicBool, crate::runtime, crate::runtime::Config...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `tokio/tests/task_local_set.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.659)
- **Top Global Matches:** file_cluster_5: 7.659, file_cluster_12: 8.496, file_cluster_7: 8.537
- **Magnitude:** 493.42 | **LOC:** 809 | **CtrlFlow:** 4.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **26**; blast radius 0.361; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (64.3%), Complexity Load (formerly Cognitive Load) (44.5%)
- **Documentation Coverage:** 94.7368% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `local_tasks_are_polled_after_tick_inner` **(I/O & Config Routines)** (Impact: 11.1)
  * `with_timeout` **(Generic / Templated Code)** (Impact: 6.9)
    * *Intent:* /// Runs a test function in a separate thread, and panics if the test does not /// complete within t...
  * `complete` **(Compute Cores)** (Impact: 6.1)
  * `run_until_does_not_get_own_budget` **(Annotated & Test Methods)** (Impact: 5.2)
    * *Intent:* // This test compares that, when the task driving `run_until` has already // consumed budget, the `r...
  * `drop_cancels_remote_tasks` **(Annotated & Test Methods)** (Impact: 4.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Race Conditions:* 34 instances
* *Amplified Cascading Flux:* 6 instances
* *Concurrency (weighted view):* 339
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 31
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 213`, `args: 82`, `func_start: 38`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 36`, `high_risk_execution: 8`, `state_mutation: 19`, `fragile_debt: 1`, `unreferenced_by_name: 29`
* *Architecture:* `concurrency: 169`, `import: 24`
* *Defense:* `safety: 1`, `doc: 7`, `test: 64`, `sync_locks: 4`, `immutability_locks: 26`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.361
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` futures::FutureExt, futures::future, futures::future::join_all, futures::future::pending, futures::future::ready, self::*, std::cell::Cell, std::future::Future...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tokio/tests/udp.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 12.607)
- **Top Global Matches:** file_cluster_7: 12.607, file_cluster_12: 13.692, file_cluster_5: 13.817
- **Magnitude:** 436.22 | **LOC:** 725 | **CtrlFlow:** 31.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.361; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (80.0%), Connectivity (formerly Api Exposure) (55.5%), Complexity Load (formerly Cognitive Load) (44.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `send_to_try_peek_from` **(Annotated & Test Methods)** (Impact: 16.9)
  * `try_send_recv` **(I/O & Config Routines)** (Impact: 14.2)
  * `try_recv_buf` **(I/O & Config Routines)** (Impact: 14.2)
  * `try_send_to_recv_from` **(Annotated & Test Methods)** (Impact: 14.1)
  * `try_recv_buf_from` **(Annotated & Test Methods)** (Impact: 14.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 178
* *State Mutation (weighted view):* 7
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 170`, `structural_boundaries: 360`, `args: 41`, `func_start: 21`
* *Risk/State:* `safety_bypasses: 61`, `high_risk_execution: 10`, `state_mutation: 3`
* *Architecture:* `io: 18`, `api: 19`, `concurrency: 153`, `import: 5`
* *Defense:* `safety: 2`, `doc: 1`, `test: 87`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.361
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` std::future::poll_fn, std::io, std::sync::Arc, tokio::io::ReadBuf, tokio::net::UdpSocket, tokio_test::assert_ok
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tokio/tests/task_join_set.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.1)
- **Top Global Matches:** file_cluster_12: 7.1, file_cluster_7: 8.902, file_cluster_5: 9.505
- **Magnitude:** 410.42 | **LOC:** 663 | **CtrlFlow:** 8.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.361; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (50.2%), Complexity Load (formerly Cognitive Load) (38.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (9.4%)
- **Documentation Coverage:** 65.5172% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_with_sleep` **(Annotated & Test Methods)** (Impact: 10.4)
  * `join_set_coop` **(I/O & Config Routines)** (Impact: 8.0)
    * *Intent:* // This ensures that `join_next` works correctly when the coop budget is // exhausted.
  * `spawn_pending_tasks` **(Many-Argument Workhorses)** (Impact: 7.8)
    * *Intent:* // Spawn `N` “pending” tasks that own a `oneshot::Sender`. // When the task is aborted the sender is...
  * `abort_tasks` **(Annotated & Test Methods)** (Impact: 7.7)
  * `try_join_next_with_id` **(Annotated & Test Methods)** (Impact: 7.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 5 instances
* *Amplified Race Conditions:* 24 instances
* *Amplified Cascading Flux:* 15 instances
* *High Risk Execution (weighted view):* 2
* *Concurrency (weighted view):* 243
* *State Mutation (weighted view):* 48
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 235`, `args: 32`, `func_start: 29`
* *Risk/State:* `safety_bypasses: 14`, `high_risk_execution: 7`, `state_mutation: 18`, `unreferenced_by_name: 12`
* *Architecture:* `concurrency: 123`, `import: 11`
* *Defense:* `safety: 12`, `doc: 11`, `test: 78`, `sync_locks: 2`, `immutability_locks: 14`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.361
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` futures::future::FutureExt, futures::future::pending, self::*, self::spawn_local::*, self::spawn_local_on::*, std::panic, tokio::sync::oneshot, tokio::task::JoinSet...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tokio/src/task/join_set.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.358)
- **Top Global Matches:** file_cluster_0: 6.358, file_cluster_13: 10.743, file_cluster_15: 11.083
- **Magnitude:** 383.74 | **LOC:** 852 | **CtrlFlow:** 10.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **14**; blast radius 0.939; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (94.6%), Concurrency Surface (formerly Concurrency) (85.0%), Connectivity (formerly Api Exposure) (59.0%), Complexity Load (formerly Cognitive Load) (50.0%)
- **Documentation Coverage:** 14.7059% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `poll_join_next_with_id` **(Defensive Guards)** (Impact: 12.0)
    * *Intent:* /// * `Poll::Pending` if the `JoinSet` is not empty but there is no task whose output is /// availab...
  * `poll_join_next` **(Defensive Guards)** (Impact: 11.8)
    * *Intent:* /// This function returns: /// /// * `Poll::Pending` if the `JoinSet` is not empty but there is no t...
  * `try_join_next` **(Defensive Guards)** (Impact: 6.6)
    * *Intent:* /// Tries to join one of the tasks in the set that has completed and return its output. /// /// Retu...
  * `try_join_next_with_id` **(Defensive Guards)** (Impact: 6.6)
    * *Intent:* /// Tries to join one of the tasks in the set that has completed and return its output, /// along wi...
  * `join_all` **(Defensive Guards)** (Impact: 6.3)
    * *Intent:* /// /// let mut output = Vec::new(); /// while let Some(res) = set.join_next().await{ /// match res ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 29 instances
* *Amplified Cascading Flux:* 11 instances
* *High Risk Execution (weighted view):* 4
* *Concurrency (weighted view):* 192
* *State Mutation (weighted view):* 41
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 100`, `args: 47`, `func_start: 34`, `class_start: 2`
* *Risk/State:* `high_risk_execution: 5`, `state_mutation: 19`
* *Architecture:* `io: 6`, `api: 32`, `concurrency: 47`, `import: 8`
* *Defense:* `safety: 7`, `doc: 465`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.939
  * `Choke Point (Betweenness):` 0.00112 | `Ripple Effect (Closeness):` 0.114948
  * `Imports (Out-Degree: 8):` crate::runtime::Handle, crate::task::AbortHandle, crate::task::Id, crate::task::JoinError, crate::task::JoinHandle, crate::task::LocalSet, crate::task::unconstrained, crate::util::IdleNotifiedSet...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `tokio-util/src/time/delay_queue.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.189)
- **Top Global Matches:** file_cluster_0: 6.189, file_cluster_16: 8.989, file_cluster_15: 9.102
- **Magnitude:** 383.16 | **LOC:** 1355 | **CtrlFlow:** 12.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **24**; blast radius 0.582; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Guard Balance (formerly Safety Score) (45.5%), Connectivity (formerly Api Exposure) (44.8%), Complexity Load (formerly Cognitive Load) (29.6%)
- **Documentation Coverage:** 48.4536% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `insert_at` **(Many-Argument Workhorses)** (Impact: 16.1)
    * *Intent:* /// let key = delay_queue.insert_at( /// "foo", Instant::now() + Duration::from_secs(5)); /// /// //...
  * `remove` **(Defensive Guards)** (Impact: 13.9)
  * `poll_idx` **(Defensive Guards)** (Impact: 13.8)
    * *Intent:* /// Polls the queue, returning the index of the next slot in the slab that /// should be returned. /...
  * `remove` **(Defensive Guards)** (Impact: 10.1)
    * *Intent:* /// ```rust /// use tokio_util::time::DelayQueue; /// use std::time::Duration; /// /// # #[tokio::ma...
  * `compact` **(Stateful Encapsulated Methods)** (Impact: 9.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 35 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 117
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 151`, `args: 63`, `func_start: 57`, `class_start: 7`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 47`
* *Architecture:* `api: 41`, `concurrency: 2`, `import: 17`
* *Defense:* `safety: 19`, `doc: 628`, `test: 11`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.582
  * `Choke Point (Betweenness):` 0.000598 | `Ripple Effect (Closeness):` 0.004
  * `Imports (Out-Degree: 5):` core::ops::Index, core::ops::IndexMut, crate::time::wheel, crate::time::wheel::Stack, crate::time::wheel::Wheel, self::wheel::InsertError, self::wheel::Stack, slab::Slab...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `tokio-util/tests/task_join_map.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.23)
- **Top Global Matches:** file_cluster_12: 7.23, file_cluster_7: 8.506, file_cluster_5: 8.692
- **Magnitude:** 377.34 | **LOC:** 672 | **CtrlFlow:** 7.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.361; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (48.3%), Complexity Load (formerly Cognitive Load) (38.2%)
- **Documentation Coverage:** 63.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_with_sleep` **(Annotated & Test Methods)** (Impact: 10.6)
  * `join_map_coop` **(I/O & Config Routines)** (Impact: 8.1)
    * *Intent:* // This ensures that `join_next` works correctly when the coop budget is // exhausted.
  * `abort_by_key` **(Annotated & Test Methods)** (Impact: 7.8)
  * `spawn_pending_tasks` **(Many-Argument Workhorses)** (Impact: 7.7)
    * *Intent:* // Spawn `N` “pending” tasks that own a `oneshot::Sender`. // When the task is aborted the sender is...
  * `abort_all` **(Annotated & Test Methods)** (Impact: 7.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Race Conditions:* 18 instances
* *Amplified Cascading Flux:* 12 instances
* *High Risk Execution (weighted view):* 1
* *Concurrency (weighted view):* 221
* *State Mutation (weighted view):* 40
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 235`, `args: 33`, `func_start: 30`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 19`, `high_risk_execution: 5`, `state_mutation: 16`, `unreferenced_by_name: 14`
* *Architecture:* `concurrency: 131`, `import: 13`
* *Defense:* `safety: 11`, `doc: 12`, `test: 99`, `sync_locks: 2`, `immutability_locks: 12`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.361
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` futures::future::FutureExt, futures::future::pending, self::*, self::spawn_local::*, self::spawn_local_on::*, std::collections::HashSet, std::panic::AssertUnwindSafe, tokio::sync::oneshot...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tokio/src/net/windows/named_pipe.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.418)
- **Top Global Matches:** file_cluster_0: 6.418, file_cluster_15: 9.112, file_cluster_13: 9.868
- **Magnitude:** 363.94 | **LOC:** 2700 | **CtrlFlow:** 8.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **29**; blast radius 1.636; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (78.7%), Concurrency Surface (formerly Concurrency) (60.2%)
- **Documentation Coverage:** 12.605% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `create_with_security_attributes_raw` **(Many-Argument Workhorses)** (Impact: 27.1)
    * *Intent:* /// has not [enabled I/O], or if any OS-specific I/O errors occur. /// /// [Tokio Runtime]: crate::r...
  * `open_with_security_attributes_raw` **(Many-Argument Workhorses)** (Impact: 14.6)
    * *Intent:* /// /// This is the same as [`open`] except that it supports providing the raw /// pointer to a stru...
  * `named_pipe_info` **(Compute Cores)** (Impact: 7.6)
    * *Intent:* /// Internal function to get the info out of a raw named pipe.
  * `connect` **(Compute Cores)** (Impact: 6.2)
    * *Intent:* /// ```no_run /// use tokio::net::windows::named_pipe::ServerOptions; /// /// const PIPE_NAME: &str ...
  * `try_read_buf` **(Generic / Templated Code)** (Impact: 6.1)
    * *Intent:* /// println!("read {} bytes", n); /// } /// Err(ref e) if e.kind() == io::ErrorKind::WouldBlock => {...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 53
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 181`, `args: 81`, `func_start: 68`, `class_start: 7`
* *Risk/State:* `state_mutation: 29`, `duplicate_logic: 44`
* *Architecture:* `io: 3`, `api: 69`, `concurrency: 18`, `import: 16`
* *Defense:* `doc: 2000`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.636
  * `Choke Point (Betweenness):` 0.002413 | `Ripple Effect (Closeness):` 0.012645
  * `Imports (Out-Degree: 7):` bytes::BufMut, crate::io::AsyncRead, crate::io::AsyncWrite, crate::io::Interest, crate::io::PollEvented, crate::io::ReadBuf, crate::io::Ready, crate::os::windows::ffi::OsStrExt...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `tokio/src/net/udp.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 5.728)
- **Top Global Matches:** file_cluster_0: 5.728, file_cluster_13: 8.581, file_cluster_15: 8.746
- **Magnitude:** 362.76 | **LOC:** 2334 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **27**; blast radius 1.63; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (90.1%), Connectivity (formerly Api Exposure) (65.6%), Guard Balance (formerly Safety Score) (26.4%), Mutation Surface (formerly State Flux) (15.0%)
- **Documentation Coverage:** 8.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `connect` **(Defensive Guards)** (Impact: 9.6)
    * *Intent:* /// # #[tokio::main] /// # async fn main() -> io::Result<()> { /// let sock = UdpSocket::bind("0.0.0...
  * `bind` **(Defensive Guards)** (Impact: 8.0)
    * *Intent:* /// /// ```no_run /// use tokio::net::UdpSocket; /// use std::io; /// /// #[tokio::main] /// async f...
  * `poll_recv_from` **(Generic / Templated Code)** (Impact: 7.1)
    * *Intent:* /// * `Poll::Ready(Err(e))` if an error is encountered. /// /// # Errors /// /// This function may e...
  * `poll_peek_from` **(Generic / Templated Code)** (Impact: 7.1)
    * *Intent:* /// # Return value /// /// The function returns: /// /// * `Poll::Pending` if the socket is not read...
  * `poll_recv` **(Generic / Templated Code)** (Impact: 6.9)
    * *Intent:* /// /// # Return value /// /// The function returns: /// /// * `Poll::Pending` if the socket is not ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 133`, `args: 108`, `func_start: 72`, `class_start: 1`
* *Risk/State:* `state_mutation: 10`
* *Architecture:* `io: 7`, `api: 64`, `concurrency: 33`, `import: 14`
* *Defense:* `safety: 4`, `doc: 1604`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.63
  * `Choke Point (Betweenness):` 0.003185 | `Ripple Effect (Closeness):` 0.02
  * `Imports (Out-Degree: 7):` bytes::BufMut, crate::io::Interest, crate::io::PollEvented, crate::io::ReadBuf, crate::io::Ready, crate::net::ToSocketAddrs, crate::net::to_socket_addrs, crate::os::windows::io::AsRawSocket...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `tokio/src/fs/file.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.77)
- **Top Global Matches:** file_cluster_4: 8.77, file_cluster_0: 9.508, file_cluster_5: 9.849
- **Magnitude:** 359.84 | **LOC:** 996 | **CtrlFlow:** 16.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **38**; blast radius 1.566; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (97.0%), Mutation Surface (formerly State Flux) (95.1%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (54.9%)
- **Documentation Coverage:** 53.8462% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `poll_write` **(Many-Argument Workhorses)** (Impact: 37.5)
  * `poll_write_vectored` **(Many-Argument Workhorses)** (Impact: 37.5)
  * `poll_read` **(Many-Argument Workhorses)** (Impact: 25.5)
  * `set_len` **(Compute Cores)** (Impact: 19.5)
    * *Intent:* /// use tokio::io::AsyncWriteExt; /// /// # async fn dox() -> std::io::Result<()> { /// let mut file...
  * `poll_complete` **(Compute Cores)** (Impact: 11.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 20 instances
* *High Risk Execution (weighted view):* 1
* *Concurrency (weighted view):* 46
* *State Mutation (weighted view):* 66
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 205`, `args: 52`, `func_start: 34`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 3`, `state_mutation: 26`, `dead_code: 2`, `planned_debt: 2`
* *Architecture:* `io: 6`, `api: 27`, `concurrency: 31`, `import: 21`
* *Defense:* `safety: 11`, `doc: 390`, `test: 9`, `sync_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.566
  * `Choke Point (Betweenness):` 0.017006 | `Ripple Effect (Closeness):` 0.077157
  * `Imports (Out-Degree: 13):` tests, crate::blocking::JoinHandle, crate::blocking::spawn_blocking, crate::blocking::spawn_mandatory_blocking, crate::fs::OpenOptions, crate::fs::asyncify, crate::io::AsyncRead, crate::io::AsyncSeek...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `tokio-util/tests/time_delay_queue.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 6.032)
- **Top Global Matches:** file_cluster_13: 6.032, file_cluster_10: 7.975, file_cluster_2: 8.252
- **Magnitude:** 350.74 | **LOC:** 900 | **CtrlFlow:** 3.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.361; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (45.0%), Complexity Load (formerly Cognitive Load) (41.4%)
- **Documentation Coverage:** 94.1176% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `multi_delay_at_start` **(Annotated & Test Methods)** (Impact: 8.1)
  * `compact_change_deadline` **(I/O & Config Routines)** (Impact: 6.6)
  * `compact_remove_remapped_keys` **(Annotated & Test Methods)** (Impact: 4.0)
  * `item_expiry_greater_than_wheel` **(Annotated & Test Methods)** (Impact: 3.8)
  * `insert_after_ready_poll` **(Annotated & Test Methods)** (Impact: 3.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 16 instances
* *Amplified Cascading Flux:* 13 instances
* *High Risk Execution (weighted view):* 1
* *Concurrency (weighted view):* 193
* *State Mutation (weighted view):* 53
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 242`, `args: 38`, `func_start: 34`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 27`, `fragile_debt: 2`, `unreferenced_by_name: 33`
* *Architecture:* `concurrency: 113`, `import: 4`
* *Defense:* `safety: 1`, `doc: 9`, `test: 117`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.361
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` futures::StreamExt, tokio::time, tokio::time::Duration, tokio::time::Instant, tokio::time::sleep, tokio::time::sleep_until, tokio_test::assert_pending, tokio_test::assert_ready...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tokio/tests/io_async_fd.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.082)
- **Top Global Matches:** file_cluster_5: 8.082, file_cluster_7: 8.754, file_cluster_12: 10.284
- **Magnitude:** 346.62 | **LOC:** 959 | **CtrlFlow:** 3.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **31**; blast radius 0.361; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (80.0%), Complexity Load (formerly Cognitive Load) (44.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (9.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `drain` **(Compute Cores)** (Impact: 7.5)
  * `await_error_readiness_invalid_address` **(I/O & Config Routines)** (Impact: 6.5)
  * `send_oob_data` **(Type Conversions)** (Impact: 6.0)
  * `poll_fns` **(I/O & Config Routines)** (Impact: 5.8)
  * `configure_timestamping_socket` **(Compute Cores)** (Impact: 5.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Race Conditions:* 19 instances
* *Amplified Cascading Flux:* 5 instances
* *High Risk Execution (weighted view):* 15
* *Concurrency (weighted view):* 161
* *Memory Alloc (weighted view):* 6
* *State Mutation (weighted view):* 49
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 293`, `args: 65`, `func_start: 46`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 80`, `high_risk_execution: 16`, `state_mutation: 39`, `planned_debt: 2`, `unreferenced_by_name: 25`
* *Architecture:* `io: 14`, `concurrency: 66`, `import: 19`
* *Defense:* `safety: 2`, `test: 46`, `sync_locks: 9`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.361
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` futures::poll, nix::fcntl::F_GETFL, nix::fcntl::F_SETFL, nix::fcntl::OFlag, nix::sys::socket, nix::sys::socket::AddressFamily, nix::sys::socket::SockFlag, nix::sys::socket::SockType...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tokio/src/runtime/scheduler/current_thread/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.129)
- **Top Global Matches:** file_cluster_0: 7.129, file_cluster_5: 7.766, file_cluster_12: 8.566
- **Magnitude:** 332.28 | **LOC:** 878 | **CtrlFlow:** 11.2% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **47**; blast radius 1.51; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (88.2%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (74.4%), Guard Balance (formerly Safety Score) (52.3%)
- **Documentation Coverage:** 77.4194% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `block_on` **(Many-Argument Workhorses)** (Impact: 28.7)
  * `block_on` **(Stateful Encapsulated Methods)** (Impact: 16.1)
  * `park` **(Defensive Guards)** (Impact: 13.4)
    * *Intent:* /// Blocks the current thread until an event is received by the driver, /// including I/O events, ti...
  * `dump` **(Stateful Encapsulated Methods)** (Impact: 10.9)
    * *Intent:* /// Capture a snapshot of this runtime's state.
  * `shutdown` **(Stateful Encapsulated Methods)** (Impact: 10.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 17 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 66
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 151`, `args: 65`, `func_start: 45`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 3`, `state_mutation: 32`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 12`
* *Architecture:* `api: 27`, `concurrency: 12`, `import: 25`
* *Defense:* `safety: 21`, `doc: 60`, `test: 2`, `sync_locks: 2`, `immutability_locks: 2`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.51
  * `Choke Point (Betweenness):` 0.004269 | `Ripple Effect (Closeness):` 0.177902
  * `Imports (Out-Degree: 21):` crate::loom::sync::Arc, crate::loom::sync::atomic::AtomicBool, crate::runtime::Config, crate::runtime::MetricsBatch, crate::runtime::SchedulerMetrics, crate::runtime::TaskHooks, crate::runtime::TaskMeta, crate::runtime::UnhandledPanic...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `tokio-util/tests/task_join_queue.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.315)
- **Top Global Matches:** file_cluster_12: 7.315, file_cluster_7: 8.193, file_cluster_5: 9.219
- **Magnitude:** 329.44 | **LOC:** 380 | **CtrlFlow:** 8.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.361; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (51.1%), Complexity Load (formerly Cognitive Load) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_join_queue_with_manual_abort` **(Annotated & Test Methods)** (Impact: 8.0)
  * `test_join_queue_abort_all` **(Annotated & Test Methods)** (Impact: 7.5)
  * `test_join_queue_try_join_next_with_id_disabled_coop` **(Annotated & Test Methods)** (Impact: 6.3)
  * `test_join_queue_join_next_with_id` **(Annotated & Test Methods)** (Impact: 5.8)
  * `test_join_queue_try_join_next_disabled_coop` **(Annotated & Test Methods)** (Impact: 5.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 6 instances
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Race Conditions:* 28 instances
* *Amplified Cascading Flux:* 14 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 214
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 48
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 146`, `args: 14`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 6`, `state_mutation: 20`, `unreferenced_by_name: 13`
* *Architecture:* `concurrency: 74`, `import: 5`
* *Defense:* `safety: 8`, `test: 55`, `sync_locks: 2`, `immutability_locks: 3`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.361
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` tokio::sync::oneshot, tokio::task::yield_now, tokio::time::Duration, tokio_test::assert_pending, tokio_test::assert_ready, tokio_test::task, tokio_util::task::JoinQueue
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tokio/src/runtime/builder.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.351)
- **Top Global Matches:** file_cluster_0: 6.351, file_cluster_13: 8.561, file_cluster_15: 9.162
- **Magnitude:** 328.2 | **LOC:** 1847 | **CtrlFlow:** 2.8% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **35** in-repo importer(s); it depends on **26**; blast radius 4.289; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (59.3%), Mutation Surface (formerly State Flux) (52.0%), Connectivity (formerly Api Exposure) (49.0%)
- **Documentation Coverage:** 8.642% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `build_current_thread_runtime_components` **(Compute Cores)** (Impact: 6.2)
  * `unhandled_panic` **(Compute Cores)** (Impact: 5.6)
    * *Intent:* /// rt.spawn(async { panic!("boom"); }); /// rt.spawn(async { /// // This task never completes. /// ...
  * `new` **(Many-Argument Workhorses)** (Impact: 5.5)
    * *Intent:* /// Returns a new runtime builder initialized with default configuration /// values. /// /// Configu...
  * `build_threaded_runtime` **(Compute Cores)** (Impact: 5.4)
  * `metrics_poll_count_histogram_builder` **(Generic / Templated Code)** (Impact: 4.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 18 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 114
* *State Mutation (weighted view):* 32
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 136`, `args: 53`, `func_start: 44`, `class_start: 3`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 28`, `planned_debt: 1`
* *Architecture:* `io: 1`, `api: 59`, `concurrency: 24`, `import: 20`
* *Defense:* `safety: 1`, `doc: 1205`, `test: 6`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.289
  * `Choke Point (Betweenness):` 0.013217 | `Ripple Effect (Closeness):` 0.184533
  * `Imports (Out-Degree: 17):` crate::loom::sys::num_cpus, crate::runtime::Callback, crate::runtime::Config, crate::runtime::HistogramBuilder, crate::runtime::LocalOptions, crate::runtime::LocalRuntime, crate::runtime::Runtime, crate::runtime::TaskCallback...
  * `Imported By (In-Degree: 35):` (Excluded from Brief to save tokens)

### `tokio-macros/src/entry.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.264)
- **Top Global Matches:** file_cluster_4: 6.264, file_cluster_0: 10.223, file_cluster_15: 10.631
- **Magnitude:** 327.7 | **LOC:** 782 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **16**; blast radius 1.336; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (61.3%), Guard Balance (formerly Safety Score) (51.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (22.6%)
- **Documentation Coverage:** 89.6552% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_knobs` **(Many-Argument Workhorses)** (Impact: 41.8)
  * `build_config` **(Many-Argument Workhorses)** (Impact: 40.5)
  * `parse` **(Compute Cores)** (Impact: 17.9)
  * `is_test_attribute` **(Compute Cores)** (Impact: 15.3)
    * *Intent:* // Check whether given attribute is a test attribute of forms: // * `#[test]` // * `#[core::prelude:...
  * `main` **(Stateful Encapsulated Methods)** (Impact: 13.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 47
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 100`, `structural_boundaries: 139`, `args: 46`, `func_start: 27`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 17`, `planned_debt: 1`
* *Architecture:* `api: 2`, `concurrency: 5`, `import: 6`
* *Defense:* `safety: 15`, `doc: 5`, `test: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.336
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.015016
  * `Imports (Out-Degree: 0):` RuntimeFlavor, proc_macro2::Span, proc_macro2::TokenStream, proc_macro2::TokenTree, quote::ToTokens, quote::quote, quote::quote_spanned, syn::Attribute...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tokio-stream/tests/stream_stream_map.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 7.373)
- **Top Global Matches:** file_cluster_13: 7.373, file_cluster_0: 8.002, file_cluster_12: 8.335
- **Magnitude:** 326.38 | **LOC:** 564 | **CtrlFlow:** 1.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 0.361; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (50.0%), Guard Balance (formerly Safety Score) (45.9%), Connectivity (formerly Api Exposure) (1.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `poll_next_many_correctly_loops_around` **(Annotated & Test Methods)** (Impact: 4.1)
  * `next_many_correctly_loops_around` **(Annotated & Test Methods)** (Impact: 4.1)
  * `multiple_entries` **(Annotated & Test Methods)** (Impact: 3.9)
  * `single_entry` **(Annotated & Test Methods)** (Impact: 2.9)
  * `one_ready_many_none` **(Annotated & Test Methods)** (Impact: 2.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 27 instances
* *Amplified Cascading Flux:* 4 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 188
* *State Mutation (weighted view):* 72
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 166`, `args: 52`, `func_start: 28`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 2`, `state_mutation: 64`, `unreferenced_by_name: 26`
* *Architecture:* `api: 1`, `concurrency: 53`, `import: 7`
* *Defense:* `safety: 2`, `test: 116`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.361
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` mpsc, futures::stream::iter, std::future::Future, std::future::poll_fn, std::pin::Pin, std::pin::pin, std::task::Poll, support::mpsc...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tokio/src/sync/broadcast.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.755)
- **Top Global Matches:** file_cluster_0: 6.755, file_cluster_15: 10.008, file_cluster_13: 10.522
- **Magnitude:** 315.48 | **LOC:** 1760 | **CtrlFlow:** 9.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **30**; blast radius 1.382; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (92.3%), Connectivity (formerly Api Exposure) (59.8%), Debt Markers (formerly Tech Debt) (48.1%), Guard Balance (formerly Safety Score) (41.5%)
- **Documentation Coverage:** 30.7692% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `recv_ref` **(Many-Argument Workhorses)** (Impact: 22.6)
    * *Intent:* /// Locks the next value if there is one.
  * `notify_rx` **(Many-Argument Workhorses)** (Impact: 13.5)
  * `drop` **(Compute Cores)** (Impact: 8.4)
  * `upgrade` **(Compute Cores)** (Impact: 6.9)
    * *Intent:* /// Tries to convert a `WeakSender` into a [`Sender`]. /// /// This will return `Some` if there are ...
  * `len` **(Type Conversions)** (Impact: 6.6)
    * *Intent:* /// tx.send(30).unwrap(); /// /// assert_eq!(tx.len(), 3); /// /// rx1.recv().await.unwrap(); /// //...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 76
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 191`, `args: 63`, `func_start: 58`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 34`, `duplicate_logic: 6`
* *Architecture:* `api: 38`, `concurrency: 8`, `import: 17`
* *Defense:* `safety: 5`, `doc: 859`, `test: 15`, `sync_locks: 25`, `immutability_locks: 1`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.382
  * `Choke Point (Betweenness):` 0.002492 | `Ripple Effect (Closeness):` 0.09181
  * `Imports (Out-Degree: 6):` crate::loom::cell::UnsafeCell, crate::loom::sync::Arc, crate::loom::sync::Mutex, crate::loom::sync::MutexGuard, crate::loom::sync::atomic::AtomicBool, crate::loom::sync::atomic::AtomicUsize, crate::task::coop::cooperative, crate::util::WakeList...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `tokio/src/sync/notify.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.047)
- **Top Global Matches:** file_cluster_0: 7.047, file_cluster_15: 9.508, file_cluster_12: 9.991
- **Magnitude:** 311.28 | **LOC:** 1410 | **CtrlFlow:** 10.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **18** in-repo importer(s); it depends on **22**; blast radius 3.119; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.9%), Debt Markers (formerly Tech Debt) (70.4%), Guard Balance (formerly Safety Score) (49.1%), Connectivity (formerly Api Exposure) (42.4%)
- **Documentation Coverage:** 48.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `poll_notified` **(Many-Argument Workhorses)** (Impact: 54.2)
  * `inner_notify_waiters` **(Many-Argument Workhorses)** (Impact: 17.6)
  * `notify_locked` **(Many-Argument Workhorses)** (Impact: 16.1)
  * `drop_notified` **(Compute Cores)** (Impact: 10.7)
  * `notify_with_strategy` **(Defensive Guards)** (Impact: 8.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 25 instances
* *State Mutation (weighted view):* 92
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 156`, `args: 50`, `func_start: 43`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 3`, `state_mutation: 42`, `duplicate_logic: 8`
* *Architecture:* `api: 18`, `concurrency: 8`, `import: 13`
* *Defense:* `safety: 12`, `doc: 528`, `test: 3`, `sync_locks: 13`, `immutability_locks: 10`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 3.119
  * `Choke Point (Betweenness):` 0.000518 | `Ripple Effect (Closeness):` 0.169496
  * `Imports (Out-Degree: 3):` crate::loom::cell::UnsafeCell, crate::loom::sync::Mutex, crate::loom::sync::atomic::AtomicUsize, crate::util::WakeList, crate::util::linked_list, crate::util::linked_list::GuardedLinkedList, crate::util::linked_list::LinkedList, std::future::Future...
  * `Imported By (In-Degree: 18):` (Excluded from Brief to save tokens)

### `tokio/src/runtime/tests/loom_multi_thread.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.479)
- **Top Global Matches:** file_cluster_0: 7.479, file_cluster_10: 8.827, file_cluster_13: 8.876
- **Magnitude:** 305.9 | **LOC:** 462 | **CtrlFlow:** 9.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **26**; blast radius 0.396; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (52.5%), Connectivity (formerly Api Exposure) (42.9%), Complexity Load (formerly Cognitive Load) (39.2%)
- **Documentation Coverage:** 95.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `gated2` **(Compute Cores)** (Impact: 11.7)
  * `blocking_and_regular_inner` **(Compute Cores)** (Impact: 10.3)
  * `only_blocking_inner` **(Callbacks & Closures)** (Impact: 6.6)
  * `pool_multi_notify` **(Annotated & Test Methods)** (Impact: 5.7)
  * `pool_multi_spawn` **(Annotated & Test Methods)** (Impact: 5.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 21 instances
* *Amplified Cascading Flux:* 9 instances
* *Concurrency (weighted view):* 169
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 128`, `args: 43`, `func_start: 25`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 9`
* *Architecture:* `api: 15`, `concurrency: 64`, `import: 21`
* *Defense:* `doc: 7`, `test: 13`, `sync_locks: 4`, `immutability_locks: 1`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.396
  * `Choke Point (Betweenness):` 0.004917 | `Ripple Effect (Closeness):` 0.132129
  * `Imports (Out-Degree: 8):` queue, shutdown, yield_now, crate::runtime, crate::runtime::Runtime, crate::runtime::tests::loom_oneshot, crate::spawn, crate::sync::oneshot...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `tokio/src/runtime/scheduler/defer.rs` (RUST) | Magnitude: 34.08 | Delta: **0.031** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 12, api: 6, state_mutation: 6
- `tokio/src/runtime/time/wheel/level.rs` (RUST) | Magnitude: 59.74 | Delta: **0.034** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 89, structural_boundaries: 27, doc: 19, args: 13
- `tokio/src/time/interval.rs` (RUST) | Magnitude: 61.44 | Delta: **0.057** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: doc: 454, indent_spaces: 109, structural_boundaries: 31, core_var_decl: 21
- `tokio/src/runtime/metrics/scheduler.rs` (RUST) | Magnitude: 10.92 | Delta: **0.078** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 14, doc: 10, api: 6, encapsulation: 6
- `tokio/src/io/ready.rs` (RUST) | Magnitude: 132.46 | Delta: **0.15** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 137, doc: 106, api: 28, structural_boundaries: 22

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `tokio/src/runtime/context/runtime_mt.rs` (RUST) | Magnitude: 10.72 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 7, args: 6, func_start: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `tokio-util/tests/io_sync_bridge.rs` (RUST) | Magnitude: 40.26 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 47, structural_boundaries: 42, branch: 14, concurrency: 13
- `tokio/src/runtime/scheduler/multi_thread/park.rs` (RUST) | Magnitude: 114.48 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 171, structural_boundaries: 43, branch: 24, doc: 22
- `tokio/tests/rt_metrics.rs` (RUST) | Magnitude: 84.56 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 145, structural_boundaries: 45, concurrency: 37, test: 29
- `tokio/tests/macros_test.rs` (RUST) | Magnitude: 69.04 | Delta: **0.07** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 62, concurrency: 29, decorators: 24, args: 20
- `tokio/tests/io_read_to_end.rs` (RUST) | Magnitude: 48.0 | Delta: **0.095** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 78, structural_boundaries: 44, core_var_decl: 13, design_snake_case: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `tokio/tests/io_read_buf.rs` (RUST) | Magnitude: 15.3 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 66, structural_boundaries: 39, test: 25, core_var_decl: 11
- `tokio/src/runtime/metrics/io.rs` (RUST) | Magnitude: 12.5 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 12, api: 7, encapsulation: 7, structural_boundaries: 4
- `tokio/src/util/metric_atomics.rs` (RUST) | Magnitude: 42.26 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 42, api: 14, encapsulation: 14, args: 12
- `tokio/src/runtime/time_alt/cancellation_queue/tests.rs` (RUST) | Magnitude: 49.16 | Delta: **0.06** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 58, structural_boundaries: 20, branch: 12, args: 12
- `tokio/src/util/error.rs` (RUST) | Magnitude: 16.64 | Delta: **0.079** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: doc: 5, api: 3, globals: 3, immutability_locks: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `tests-integration/tests/macros_select.rs` (RUST) | Magnitude: 40.1 | Delta: **0.089** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 15, safety_bypasses: 6, branch: 5
- `tests-integration/tests/process_stdio.rs` (RUST) | Magnitude: 84.98 | Delta: **0.095** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 136, structural_boundaries: 103, core_var_decl: 48, design_snake_case: 45

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `tokio/src/util/rand.rs` (RUST) | Magnitude: 28.76 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 50, structural_boundaries: 16, doc: 14, bitwise_ops: 9
- `tokio/src/runtime/scheduler/mod.rs` (RUST) | Magnitude: 145.2 | Delta: **0.137** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 257, api: 42, encapsulation: 42, structural_boundaries: 39

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `tokio/src/macros/pin.rs` (RUST) | Magnitude: 15.36 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 123, indent_spaces: 15, structural_boundaries: 7, decorators: 2
- `tokio-util/src/tracing.rs` (RUST) | Magnitude: 13.12 | Delta: **0.097** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 4, decorators: 1, reflection_metaprogramming: 1, macros: 1
- `tokio/src/sync/tests/mod.rs` (RUST) | Magnitude: 15.34 | Delta: **0.169** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 13, indent_spaces: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `tokio/src/macros/loom.rs` (RUST) | Magnitude: 14.16 | Delta: **0.062** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 6, decorators: 1, reflection_metaprogramming: 1, macros: 1
- `tokio/src/net/tcp/mod.rs` (RUST) | Magnitude: 21.2 | Delta: **0.122** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 8, api: 6, encapsulation: 4, import: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `tokio-util/tests/udp.rs` (RUST) | Magnitude: 70.8 | Delta: **0.034** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_spaces: 85, structural_boundaries: 83, core_var_decl: 45, design_snake_case: 42
- `tokio/tests/sync_mutex.rs` (RUST) | Magnitude: 44.46 | Delta: **0.105** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 83, structural_boundaries: 67, core_var_decl: 29, design_snake_case: 29
- `tokio/tests/io_copy_bidirectional.rs` (RUST) | Magnitude: 99.96 | Delta: **0.121** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 106, indent_spaces: 93, concurrency: 46, core_var_decl: 26

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `tokio/tests/fs_remove_dir_all.rs` (RUST) | Magnitude: 10.62 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 10, concurrency: 6, safety_bypasses: 4
- `tokio/tests/tcp_into_split.rs` (RUST) | Magnitude: 56.94 | Delta: **0.075** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 85, structural_boundaries: 68, branch: 24, core_var_decl: 24
- `tokio-stream/tests/stream_timeout.rs` (RUST) | Magnitude: 29.42 | Delta: **0.091** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 48, structural_boundaries: 25, concurrency: 16, core_var_decl: 9
- `tokio/src/sync/tests/loom_watch.rs` (RUST) | Magnitude: 30.62 | Delta: **0.129** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_spaces: 65, structural_boundaries: 39, safety_bypasses: 17, args: 16
- `tests-integration/tests/macros_main.rs` (RUST) | Magnitude: 17.12 | Delta: **0.154** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 11, concurrency: 9, decorators: 9, args: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `examples/named-pipe.rs` (RUST) | Magnitude: 28.72 | Delta: **0.046** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 34, structural_boundaries: 27, concurrency: 12, branch: 11

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `tokio/src/runtime/mod.rs` -> Churn: **85.35%** | Cog Load: 4.4923% | Debt: 85.5459%
- `tokio/src/lib.rs` -> Churn: **74.43%** | Cog Load: 0.0% | Debt: 66.8458%
- `tokio/src/runtime/scheduler/mod.rs` -> Churn: **52.1%** | Cog Load: 5.4053% | Debt: 99.9994%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `tokio/tests/sync_mpsc.rs` -> **KR-bluejay** (100.0% isolated ownership) | Magnitude: 694.18
- `tokio/tests/rt_threaded.rs` -> **ADD-SP** (100.0% isolated ownership) | Magnitude: 534.4
- `tokio/tests/udp.rs` -> **Jan Tojnar** (100.0% isolated ownership) | Magnitude: 436.22
- `tokio/tests/task_join_set.rs` -> **Elichai Turkel** (100.0% isolated ownership) | Magnitude: 410.42
- `tokio/src/task/join_set.rs` -> **Elichai Turkel** (100.0% isolated ownership) | Magnitude: 383.74

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `tokio/src/io/blocking.rs` -> **Severity: 3.329** (Bridge: 0.0333 * Flux: 99.8496%)
- `tokio/src/fs/file.rs` -> **Severity: 1.617** (Bridge: 0.017 * Flux: 95.1007%)
- `tokio/src/runtime/scheduler/multi_thread/worker.rs` -> **Severity: 1.448** (Bridge: 0.0157 * Flux: 92.1261%)
- `tokio/src/runtime/blocking/pool.rs` -> **Severity: 1.307** (Bridge: 0.014 * Flux: 93.4438%)
- `tokio/src/runtime/task/trace/mod.rs` -> **Severity: 1.113** (Bridge: 0.0114 * Flux: 97.4246%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `tokio/src/runtime/scheduler/mod.rs` -> **Severity: 13.478** (Embedded: 0.2166 * Error Risk: 62.222%)
- `tokio/src/loom/mocked.rs` -> **Severity: 12.565** (Embedded: 0.2265 * Error Risk: 55.4659%)
- `tokio/src/future/try_join.rs` -> **Severity: 11.46** (Embedded: 0.1432 * Error Risk: 80.0%)
- `tokio/src/runtime/park.rs` -> **Severity: 11.312** (Embedded: 0.1826 * Error Risk: 61.9563%)
- `tokio-test/src/macros.rs` -> **Severity: 10.575** (Embedded: 0.1376 * Error Risk: 76.875%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `tokio/src/fs/mod.rs` -> **Severity: 2172.7** (Blast Radius: 21.727 * Doc Risk: 100.0%)
- `tokio/src/loom/mocked.rs` -> **Severity: 1858.7** (Blast Radius: 18.587 * Doc Risk: 100.0%)
- `tokio/src/loom/std/mod.rs` -> **Severity: 1517.1** (Blast Radius: 15.171 * Doc Risk: 100.0%)
- `tokio/src/io/async_write.rs` -> **Severity: 1147.664** (Blast Radius: 12.948 * Doc Risk: 88.6364%)
- `tokio/src/io/async_read.rs` -> **Severity: 1094.25** (Blast Radius: 13.131 * Doc Risk: 83.3333%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`panics_and_aborts`:** 383 literal sites + 10 sites through wrappers = 393

- `drop` (function, panics_and_aborts, primitive): 8 call sites in 1 files -- `tokio-util/tests/task_join_map.rs`
- `drop` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `tokio/tests/join_handle_panic.rs`
- `exhausted` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `tokio/src/runtime/thread_id.rs`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 31292 call pairs -- scoped 18.5%, unique 0.0%, ambiguous 23.1%, external 58.3%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| rust | 31292 | 18.5% | 0.0% | 23.1% | 58.3% |

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
