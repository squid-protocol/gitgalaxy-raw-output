# ARCHITECTURAL_BRIEF: tokio
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/tokio-rs/tokio.git` |
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
| Total Artifacts | 844 |
| Analyzed Artifacts (Scanned) | 787 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 57 |
| Total LOC | 93918 |
| Volatility Index | 0.009 |
| % Scanned of codebase = | 93.2% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7481 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3325 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.1487 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 14 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUST | 769 | 93870 | 97.7% |
| MARKDOWN | 17 | 0 | 2.2% |
| JSON | 1 | 48 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 770 | 97.8% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 17 | 2.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 57*

**Composition by Extension & Reason:**
- `.toml`: 13x Unsupported Format (.toml), 4x Excluded (Unsupported Extension: '.toml'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 4356 LOC)
- `.yml`: 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.stderr`: 6x Excluded (Unsupported Extension: '.stderr')
- `.dic`: 1x Excluded (Unsupported Extension: '.dic')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 15.5 | 8.7 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.1 | 37.2 | 43.4 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 25.2 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 11.7 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 81.8 | 11.3 | 3.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 52.2 | 53.3 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 15.8 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 14.2 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 93.1 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 8.1 | 1.7 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 91.8 | 7.5 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 66.9 | 85.7 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 6231 | 607 | 23 | `tokio/src/net/udp.rs` |
| cleanup | 771 | 183 | 2 | `tokio/tests/sync_mpsc.rs` |
| guards | 3226 | 471 | 12 | `tokio/src/runtime/scheduler/multi_thread/worker.rs` |
| danger | 3638 | 366 | 12 | `tokio-util/tests/codecs.rs` |
| concurrency | 11184 | 601 | 34 | `tokio/tests/async_send_sync.rs` |
| connectivity | 4571 | 504 | 18 | `tokio/src/net/windows/named_pipe.rs` |
| io | 801 | 264 | 2 | `tokio/tests/async_send_sync.rs` |
| crypto | 0 | 0 | 0 | - |
| ipc | 170 | 42 | 0 | `tokio/tests/sync_mpsc.rs` |
| time | 113 | 73 | 0 | `tokio/src/time/instant.rs` |
| serialization | 1 | 1 | 0 | `examples/tinyhttp.rs` |
| regex | 0 | 0 | 0 | - |
| events | 531 | 82 | 1 | `tokio/tests/async_send_sync.rs` |
| tests | 5718 | 399 | 18 | `tokio/tests/sync_mpsc.rs` |
| docs | 49273 | 464 | 137 | `tokio/src/net/windows/named_pipe.rs` |
| debt | 557 | 163 | 2 | `tokio/src/net/windows/named_pipe.rs` |
| mutation | 14454 | 661 | 51 | `tokio/tests/macros_select.rs` |
| dead_code | 7395 | 588 | 21 | `tokio/src/net/windows/named_pipe.rs` |
| credential | 0 | 0 | 0 | - |
| threat | 655 | 184 | 3 | `tokio/src/macros/cfg.rs` |
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

1. **mem.rs** (`tokio/src/io/util/mem.rs`) — 19 inbound connections
2. **ready.rs** (`tokio/src/io/ready.rs`) — 7 inbound connections
3. **sleep.rs** (`tokio/src/time/sleep.rs`) — 6 inbound connections
4. **oneshot.rs** (`tokio/src/sync/oneshot.rs`) — 5 inbound connections
5. **scheduler.rs** (`tokio/src/runtime/metrics/scheduler.rs`) — 3 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **mod.rs** (`tokio/src/io/mod.rs`) — 60 outbound dependencies
2. **stream.rs** (`tokio/src/net/tcp/stream.rs`) — 52 outbound dependencies
3. **mod.rs** (`tokio/src/process/mod.rs`) — 52 outbound dependencies
4. **named_pipe.rs** (`tokio/src/net/windows/named_pipe.rs`) — 51 outbound dependencies
5. **stream.rs** (`tokio/src/net/unix/stream.rs`) — 47 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `test_combination` (@ `tokio/src/runtime/tests/task_combinations.rs`) -> Impact: **181.1** | LOC: 333
- `poll_acquire` (@ `tokio/src/sync/batch_semaphore.rs`) -> Impact: **60.2** | LOC: 126
- `poll_notified` (@ `tokio/src/sync/notify.rs`) -> Impact: **58.0** | LOC: 225
- `test_named_pipe_multi_client_ready` (@ `tokio/tests/net_named_pipe.rs`) -> Impact: **52.9** | LOC: 178
- `fmt` (@ `tokio/src/io/interest.rs`) -> Impact: **46.2** | LOC: 58
- `windows_main` (@ `examples/named-pipe-ready.rs`) -> Impact: **43.2** | LOC: 144
- `build_config` (@ `tokio-macros/src/entry.rs`) -> Impact: **43.0** | LOC: 99
- `parse_knobs` (@ `tokio-macros/src/entry.rs`) -> Impact: **42.8** | LOC: 136
- `poll_next_many` (@ `tokio-stream/src/stream_map.rs`) -> Impact: **39.1** | LOC: 66
  * *Intent:* /// Polls to receive multiple items on this `StreamMap`, extending the provided `buffer`. /// /// This method returns: /// * `Poll::Pending` if no ite...
- `poll_copy` (@ `tokio/src/io/util/copy.rs`) -> Impact: **38.3** | LOC: 140

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `tokio/tests` | 163 | 13632.7 | 19.2% | 0.0% |
| `tokio-util/tests` | 29 | 2596.78 | 17.15% | 0.0% |
| `tokio/src/sync` | 12 | 2323.1 | 16.36% | 57.06% |
| `tokio/src/io/util` | 37 | 1379.96 | 10.6% | 28.56% |
| `benches` | 17 | 1234.98 | 48.83% | 9.65% |
| `tokio/src/io` | 18 | 1232.62 | 12.65% | 32.3% |
| `tokio/src/runtime/tests` | 11 | 1212.34 | 22.13% | 0.0% |
| `tokio/src/runtime` | 13 | 1122.76 | 8.81% | 29.95% |
| `tokio/src/runtime/scheduler/multi_thread` | 11 | 1122.32 | 15.22% | 15.98% |
| `tokio/src/runtime/task` | 11 | 1088.26 | 10.99% | 39.06% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `tokio-util/src/io/sync_bridge.rs` -> **100.0%** Exposure
- `tokio-util/src/task/abort_on_drop.rs` -> **100.0%** Exposure
- `tokio/src/fs/mocks.rs` -> **100.0%** Exposure
- `tokio/src/fs/open_options/mock_open_options.rs` -> **100.0%** Exposure
- `tokio/src/io/async_write.rs` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `tokio/src/io/util/buf_writer.rs` -> **100.0%** Exposure
- `tokio/src/io/util/read_line.rs` -> **100.0%** Exposure
- `tokio/src/io/util/read_to_end.rs` -> **100.0%** Exposure
- `tokio/src/runtime/scheduler/util/time_alt.rs` -> **100.0%** Exposure
- `tokio/src/util/idle_notified_set.rs` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tokio/tests/sync_mpsc.rs` -> **91** Orphaned Functions | **0** Duplicates
- `tokio/src/net/windows/named_pipe.rs` -> **4** Orphaned Functions | **44** Duplicates
- `tokio/src/net/udp.rs` -> **47** Orphaned Functions | **0** Duplicates
- `tokio/tests/rt_common.rs` -> **46** Orphaned Functions | **0** Duplicates
- `tokio-util/tests/length_delimited.rs` -> **42** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `7270` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `tokio/src/fs/mocks.rs` (RUST) -> Cumulative Risk: **728.36**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 102.78 | **LOC:** 177 | **CtrlFlow:** 9.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (98.2668%)
- **Heaviest Functions:** `poll` (Impact: 3.9), `spawn_blocking` (Impact: 3.5), `spawn_mandatory_blocking` (Impact: 3.5)

### 2. `tokio/src/fs/file.rs` (RUST) -> Cumulative Risk: **683.65**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 359.84 | **LOC:** 996 | **CtrlFlow:** 16.9% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (97.0495%), State Flux (95.1007%), Dead Code (89.8481%)
- **Heaviest Functions:** `poll_write` (Impact: 37.5), `poll_write_vectored` (Impact: 37.5), `poll_read` (Impact: 25.5)

### 3. `tokio-util/src/task/join_map.rs` (RUST) -> Cumulative Risk: **667.96**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 227.2 | **LOC:** 851 | **CtrlFlow:** 5.8% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.8711%), Concurrency (85.0%), Dead Code (81.9929%)
- **Heaviest Functions:** `join_next` (Impact: 7.8), `remove_by_id` (Impact: 5.9), `insert` (Impact: 5.8)

### 4. `tokio/src/fs/read_uring.rs` (RUST) -> Cumulative Risk: **659.62**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 100.76 | **LOC:** 135 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.9436%)
- **Heaviest Functions:** `read_to_end_uring` (Impact: 21.2), `op_read` (Impact: 10.1), `small_probe_read` (Impact: 7.2)

### 5. `tokio/src/task/join_set.rs` (RUST) -> Cumulative Risk: **656.32**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 380.74 | **LOC:** 852 | **CtrlFlow:** 10.3% | **Authorship Centralization:** 40.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (94.5649%), Concurrency (85.0%), Dead Code (83.4333%)
- **Heaviest Functions:** `poll_join_next_with_id` (Impact: 12.0), `poll_join_next` (Impact: 11.8), `try_join_next` (Impact: 6.6)

### 6. `benches/rt_multi_threaded.rs` (RUST) -> Cumulative Risk: **652.42**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 250.52 | **LOC:** 277 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (97.1417%)
- **Heaviest Functions:** `rt_multi_spawn_many_remote_busy2` (Impact: 10.5), `rt_multi_spawn_many_remote_busy1` (Impact: 10.1), `rt_multi_yield_many` (Impact: 8.4)

### 7. `tokio/src/sync/notify.rs` (RUST) -> Cumulative Risk: **649.98**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 320.16 | **LOC:** 1418 | **CtrlFlow:** 10.4% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (97.7109%), Verification (80.0%), Dead Code (76.8433%)
- **Heaviest Functions:** `poll_notified` (Impact: 58.0), `inner_notify_waiters` (Impact: 17.6), `notify_locked` (Impact: 16.1)

### 8. `tokio/src/runtime/time_alt/tests.rs` (RUST) -> Cumulative Risk: **644.57**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 103.92 | **LOC:** 169 | **CtrlFlow:** 14.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9998%), Concurrency (99.3012%)
- **Heaviest Functions:** `cancel_in_the_different_thread` (Impact: 9.2), `wake_up_in_the_different_thread` (Impact: 7.8), `cancel_in_the_same_thread` (Impact: 6.7)

### 9. `tokio/src/runtime/builder.rs` (RUST) -> Cumulative Risk: **629.24**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 339.94 | **LOC:** 1893 | **CtrlFlow:** 3.5% | **Authorship Centralization:** 27.3%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Churn (91.76%), Dead Code (89.072%)
- **Heaviest Functions:** `fmt` (Impact: 8.2), `build_current_thread_runtime_components` (Impact: 6.2), `build_local` (Impact: 5.6)

### 10. `tokio/src/runtime/time_alt/cancellation_queue/tests.rs` (RUST) -> Cumulative Risk: **621.74**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 46.16 | **LOC:** 98 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (98.6166%), Concurrency (95.472%)
- **Heaviest Functions:** `multi_thread` (Impact: 10.2), `single_thread` (Impact: 4.7), `drop_iter_should_not_leak_memory` (Impact: 3.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `tokio/tests/async_send_sync.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1105.26 | **LOC:** 779 | **CtrlFlow:** 3.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (50.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `as_raw_fd` (Impact: 1.6)
  * `require_send` (Impact: 1.5)
  * `require_sync` (Impact: 1.5)
  * `require_unpin` (Impact: 1.5)
  * `some_item` (Impact: 1.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 145`, `args: 11`, `func_start: 7`, `class_start: 8`
* *Risk/State:* `high_risk_execution: 4`, `planned_debt: 2`, `duplicate_logic: 3`, `unreferenced_by_name: 1`
* *Architecture:* `io: 90`, `concurrency: 1080`, `import: 22`
* *Defense:* `sync_locks: 28`, `immutability_locks: 3`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.171
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Instant, std::cell::Cell, std::future::Future, std::io::SeekFrom, std::net::SocketAddr, std::pin::Pin, std::rc::Rc, super::*...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tokio/tests/sync_mpsc.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 703.7 | **LOC:** 1537 | **CtrlFlow:** 6.6% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (48.9735%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `try_reserve_many_full` (Impact: 9.1)
  * `drop_all_elements_during_panic` (Impact: 6.2)
  * `try_recv_unbounded` (Impact: 4.9)
  * `send_recv_many_unbounded` (Impact: 4.4)
  * `try_reserve_many_edge_cases` (Impact: 4.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Race Conditions:* 17 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 440
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 454`, `args: 102`, `func_start: 96`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 53`, `high_risk_execution: 11`, `state_mutation: 9`, `dead_code: 1`, `unreferenced_by_name: 91`
* *Architecture:* `api: 1`, `concurrency: 355`, `import: 20`
* *Defense:* `test: 296`, `sync_locks: 5`, `immutability_locks: 3`, `cleanup: 66`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.171
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Timeout, TrySendError, futures::future::FutureExt, std::fmt, std::future::Future, std::panic, std::sync::Arc, std::sync::atomic::AtomicUsize...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tokio/tests/rt_common.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 694.5 | **LOC:** 1439 | **CtrlFlow:** 7.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (39.6904%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `yield_defers_until_park_inner` (Impact: 18.7)
    * *Intent:* /// Implementation of `yield_defers_until_park` test. Returns `true` if the /// test passed.
  * `ping_pong_saturation` (Impact: 10.1)
    * *Intent:* // Tests that the "next task" scheduler optimization is not able to starve // other tasks.
  * `wake_from_thread_local` (Impact: 9.5)
  * `spawn_many_from_task` (Impact: 7.6)
  * `spawn_many_from_block_on` (Impact: 7.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Race Conditions:* 29 instances
* *Amplified Cascading Flux:* 15 instances
* *Concurrency (weighted view):* 411
* *Memory Alloc (weighted view):* 4
* *State Mutation (weighted view):* 47
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 73`, `structural_boundaries: 467`, `args: 95`, `func_start: 63`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 75`, `high_risk_execution: 6`, `state_mutation: 17`, `dead_code: 3`, `unreferenced_by_name: 46`
* *Architecture:* `io: 3`, `concurrency: 266`, `import: 34`
* *Defense:* `safety: 2`, `doc: 14`, `test: 82`, `sync_locks: 18`, `immutability_locks: 12`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.171
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AsyncWriteExt, AtomicBool, Future, Instant, Ordering::SeqCst, Poll, Sender, TcpStream...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tokio/tests/macros_select.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 606.32 | **LOC:** 761 | **CtrlFlow:** 4.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.9967%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `biased_eventually_ready` (Impact: 8.8)
  * `join_with_select` (Impact: 6.7)
  * `select_streams` (Impact: 5.1)
  * `deterministic_select_multi_thread` (Impact: 5.1)
  * `select_is_budget_aware` (Impact: 4.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 43 instances
* *Amplified Cascading Flux:* 24 instances
* *Concurrency (weighted view):* 393
* *State Mutation (weighted view):* 98
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 162`, `args: 47`, `func_start: 42`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 18`, `high_risk_execution: 8`, `state_mutation: 50`, `unreferenced_by_name: 37`
* *Architecture:* `api: 1`, `concurrency: 178`, `import: 18`
* *Defense:* `test: 55`, `immutability_locks: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.171
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Duration, assert_pending, assert_ready, futures::future, std::cell::Cell, std::future::poll_fn, std::mem, std::task::Poll::Ready...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tokio/tests/rt_threaded.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 537.64 | **LOC:** 954 | **CtrlFlow:** 9.5% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (43.3538%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_tuning` (Impact: 22.7)
    * *Intent:* // Testing the tuning logic is tricky as it is inherently timing based, and more // of a heuristic t...
  * `many_multishot_futures` (Impact: 13.2)
  * `drop_threadpool_drops_futures` (Impact: 8.8)
  * `blocking` (Impact: 8.3)
  * `wake_during_shutdown` (Impact: 8.1)
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
* *Structure:* `branch: 66`, `structural_boundaries: 249`, `args: 60`, `func_start: 41`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 63`, `high_risk_execution: 1`, `state_mutation: 26`, `unreferenced_by_name: 30`
* *Architecture:* `io: 1`, `concurrency: 134`, `import: 17`
* *Defense:* `safety: 3`, `doc: 7`, `test: 46`, `sync_locks: 26`, `immutability_locks: 6`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.171
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Arc, AsyncWriteExt, Future, Mutex, Ordering, Poll, RecvTimeoutError, TcpStream...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tokio/src/runtime/scheduler/multi_thread/worker.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 502.68 | **LOC:** 1511 | **CtrlFlow:** 11.9% | **Authorship Centralization:** 20.0%
- **Risk Profile:** Cognitive Load (9.845%), Tech Debt (16.262%)
**Top Internal Functions/Classes:**
  * `block_in_place` (Impact: 26.8)
  * `run` (Impact: 24.2)
  * `run_task` (Impact: 19.8)
  * `schedule_local` (Impact: 17.3)
  * `park` (Impact: 15.3)
    * *Intent:* /// Parks the worker thread while waiting for tasks to execute. /// /// This function checks if inde...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 31 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 113
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 111`, `structural_boundaries: 244`, `args: 69`, `func_start: 55`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 2`, `state_mutation: 51`, `unreferenced_by_name: 8`
* *Architecture:* `api: 28`, `concurrency: 2`, `import: 18`
* *Defense:* `safety: 23`, `doc: 172`, `test: 10`, `sync_locks: 20`, `immutability_locks: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.171
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Config, Counters, Defer, Handle, Idle, Lock, Mutex, Overflow...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tokio/tests/task_local_set.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 495.22 | **LOC:** 809 | **CtrlFlow:** 5.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (44.4683%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `local_tasks_are_polled_after_tick_inner` (Impact: 11.1)
  * `with_timeout` (Impact: 8.7)
    * *Intent:* /// Runs a test function in a separate thread, and panics if the test does not /// complete within t...
  * `complete` (Impact: 6.1)
  * `run_until_does_not_get_own_budget` (Impact: 5.2)
    * *Intent:* // This test compares that, when the task driving `run_until` has already // consumed budget, the `r...
  * `drop_cancels_remote_tasks` (Impact: 4.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Race Conditions:* 34 instances
* *Amplified Cascading Flux:* 6 instances
* *Concurrency (weighted view):* 339
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 31
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 213`, `args: 82`, `func_start: 38`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 36`, `high_risk_execution: 8`, `state_mutation: 19`, `dead_code: 1`, `fragile_debt: 1`, `unreferenced_by_name: 29`
* *Architecture:* `concurrency: 169`, `import: 24`
* *Defense:* `safety: 1`, `doc: 7`, `test: 64`, `sync_locks: 4`, `immutability_locks: 26`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.171
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` FutureExt, LocalSet, Poll, futures::
    future::pending, futures::future, futures::future::join_all, futures::future::pending, oneshot...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tokio/tests/udp.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 479.82 | **LOC:** 771 | **CtrlFlow:** 29.8% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (46.5949%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `send_to_try_peek_from` (Impact: 16.9)
  * `try_send_to_recv_from` (Impact: 15.3)
  * `try_recv_buf_from` (Impact: 15.3)
  * `poll_ready` (Impact: 15.3)
  * `try_send_recv` (Impact: 14.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 12 instances
* *Amplified Cascading Flux:* 8 instances
* *Concurrency (weighted view):* 213
* *State Mutation (weighted view):* 26
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 176`, `structural_boundaries: 360`, `args: 41`, `func_start: 21`
* *Risk/State:* `safety_bypasses: 61`, `high_risk_execution: 10`, `state_mutation: 10`, `unreferenced_by_name: 19`
* *Architecture:* `io: 18`, `concurrency: 153`, `import: 5`
* *Defense:* `safety: 2`, `doc: 1`, `test: 87`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.171
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` net::UdpSocket, std::future::poll_fn, std::io, std::sync::Arc, tokio::io::ReadBuf, tokio_test::assert_ok
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tokio/tests/task_join_set.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 410.42 | **LOC:** 663 | **CtrlFlow:** 8.2% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (38.367%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_with_sleep` (Impact: 10.4)
  * `join_set_coop` (Impact: 8.0)
    * *Intent:* // This ensures that `join_next` works correctly when the coop budget is // exhausted.
  * `spawn_pending_tasks` (Impact: 7.8)
    * *Intent:* // Spawn `N` “pending” tasks that own a `oneshot::Sender`. // When the task is aborted the sender is...
  * `abort_tasks` (Impact: 7.7)
  * `try_join_next_with_id` (Impact: 7.1)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.171
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` FutureExt, LocalSet, futures::future::pending, std::panic, super::*, tokio::sync::oneshot, tokio::task::JoinSet, tokio::time::Duration
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tokio-util/src/time/delay_queue.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 383.16 | **LOC:** 1355 | **CtrlFlow:** 12.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (29.6489%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `insert_at` (Impact: 16.1)
    * *Intent:* /// let key = delay_queue.insert_at( /// "foo", Instant::now() + Duration::from_secs(5)); /// /// //...
  * `remove` (Impact: 13.9)
  * `poll_idx` (Impact: 13.8)
    * *Intent:* /// Polls the queue, returning the index of the next slot in the slab that /// should be returned. /...
  * `remove` (Impact: 10.1)
    * *Intent:* /// ```rust /// use tokio_util::time::DelayQueue; /// use std::time::Duration; /// /// # #[tokio::ma...
  * `compact` (Impact: 9.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 35 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 117
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 151`, `args: 63`, `func_start: 57`, `class_start: 7`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 47`, `dead_code: 78`
* *Architecture:* `api: 41`, `concurrency: 2`, `import: 17`
* *Defense:* `safety: 19`, `doc: 628`, `test: 11`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.171
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Context, Duration, IndexMut, Instant, Poll, Sleep, Stack, Waker...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tokio/src/task/join_set.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 380.74 | **LOC:** 852 | **CtrlFlow:** 10.3% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (49.9967%), Tech Debt (73.607%)
**Top Internal Functions/Classes:**
  * `poll_join_next_with_id` (Impact: 12.0)
    * *Intent:* /// * `Poll::Pending` if the `JoinSet` is not empty but there is no task whose output is /// availab...
  * `poll_join_next` (Impact: 11.8)
    * *Intent:* /// This function returns: /// /// * `Poll::Pending` if the `JoinSet` is not empty but there is no t...
  * `try_join_next` (Impact: 6.6)
    * *Intent:* /// Tries to join one of the tasks in the set that has completed and return its output. /// /// Retu...
  * `try_join_next_with_id` (Impact: 6.6)
    * *Intent:* /// Tries to join one of the tasks in the set that has completed and return its output, /// along wi...
  * `join_all` (Impact: 6.3)
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
* *Risk/State:* `high_risk_execution: 5`, `state_mutation: 19`, `dead_code: 40`, `unreferenced_by_name: 11`
* *Architecture:* `io: 6`, `api: 29`, `concurrency: 47`, `import: 8`
* *Defense:* `safety: 7`, `doc: 465`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.171
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AbortHandle, JoinError, JoinHandle, LocalSet, Poll, crate::runtime::Handle, crate::task::Id, crate::task::unconstrained...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tokio-util/tests/task_join_map.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 379.74 | **LOC:** 672 | **CtrlFlow:** 7.4% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (38.1771%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_with_sleep` (Impact: 10.6)
  * `join_map_coop` (Impact: 8.1)
    * *Intent:* // This ensures that `join_next` works correctly when the coop budget is // exhausted.
  * `abort_by_key` (Impact: 7.8)
  * `spawn_pending_tasks` (Impact: 7.7)
    * *Intent:* // Spawn `N` “pending” tasks that own a `oneshot::Sender`. // When the task is aborted the sender is...
  * `abort_all` (Impact: 7.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Race Conditions:* 18 instances
* *Amplified Cascading Flux:* 12 instances
* *High Risk Execution (weighted view):* 1
* *Concurrency (weighted view):* 221
* *State Mutation (weighted view):* 40
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 235`, `args: 33`, `func_start: 30`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 19`, `high_risk_execution: 5`, `state_mutation: 16`, `unreferenced_by_name: 14`
* *Architecture:* `concurrency: 131`, `import: 13`
* *Defense:* `safety: 11`, `doc: 12`, `test: 99`, `sync_locks: 2`, `immutability_locks: 12`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.171
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` FutureExt, futures::future::pending, std::collections::HashSet, std::panic::AssertUnwindSafe, super::*, tokio::sync::oneshot, tokio::task::LocalSet, tokio::time::Duration...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tokio/src/net/windows/named_pipe.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 363.94 | **LOC:** 2700 | **CtrlFlow:** 8.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (14.0591%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `create_with_security_attributes_raw` (Impact: 27.1)
    * *Intent:* /// has not [enabled I/O], or if any OS-specific I/O errors occur. /// /// [Tokio Runtime]: crate::r...
  * `open_with_security_attributes_raw` (Impact: 14.6)
    * *Intent:* /// /// This is the same as [`open`] except that it supports providing the raw /// pointer to a stru...
  * `named_pipe_info` (Impact: 7.6)
    * *Intent:* /// Internal function to get the info out of a raw named pipe.
  * `connect` (Impact: 6.2)
    * *Intent:* /// ```no_run /// use tokio::net::windows::named_pipe::ServerOptions; /// /// const PIPE_NAME: &str ...
  * `try_read_buf` (Impact: 6.1)
    * *Intent:* /// println!("read {} bytes", n); /// } /// Err(ref e) if e.kind() == io::ErrorKind::WouldBlock => {...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 53
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 181`, `args: 81`, `func_start: 68`, `class_start: 7`
* *Risk/State:* `state_mutation: 29`, `dead_code: 276`, `duplicate_logic: 44`, `unreferenced_by_name: 4`
* *Architecture:* `io: 3`, `api: 69`, `concurrency: 18`, `import: 16`
* *Defense:* `doc: 2000`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.171
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AsRawHandle, AsyncWrite, AsyncWriteExt, BorrowedHandle, ClientOptions, FromRawHandle, Interest, IoSliceMut...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tokio/src/fs/file.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 359.84 | **LOC:** 996 | **CtrlFlow:** 16.9% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (39.3628%), Tech Debt (9.1393%)
**Top Internal Functions/Classes:**
  * `poll_write` (Impact: 37.5)
  * `poll_write_vectored` (Impact: 37.5)
  * `poll_read` (Impact: 25.5)
  * `set_len` (Impact: 19.5)
    * *Intent:* /// use tokio::io::AsyncWriteExt; /// /// # async fn dox() -> std::io::Result<()> { /// let mut file...
  * `poll_complete` (Impact: 11.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 20 instances
* *High Risk Execution (weighted view):* 1
* *Concurrency (weighted view):* 46
* *State Mutation (weighted view):* 66
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 205`, `args: 52`, `func_start: 34`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 3`, `state_mutation: 26`, `dead_code: 53`, `planned_debt: 2`
* *Architecture:* `io: 6`, `api: 27`, `concurrency: 31`, `import: 21`
* *Defense:* `safety: 11`, `doc: 390`, `test: 9`, `sync_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.171
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AsHandle, AsyncSeek, AsyncWrite, BorrowedHandle, Context, DEFAULT_MAX_BUF_SIZE, FromRawHandle, OpenOptions...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tokio/src/net/udp.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 353.12 | **LOC:** 2342 | **CtrlFlow:** 9.8% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (6.3215%), Tech Debt (99.4472%)
**Top Internal Functions/Classes:**
  * `connect` (Impact: 9.6)
    * *Intent:* /// # #[tokio::main] /// # async fn main() -> io::Result<()> { /// let sock = UdpSocket::bind("0.0.0...
  * `bind` (Impact: 8.0)
    * *Intent:* /// /// ```no_run /// use tokio::net::UdpSocket; /// use std::io; /// /// #[tokio::main] /// async f...
  * `poll_recv_from` (Impact: 7.1)
    * *Intent:* /// * `Poll::Ready(Err(e))` if an error is encountered. /// /// # Errors /// /// This function may e...
  * `poll_peek_from` (Impact: 7.1)
    * *Intent:* /// # Return value /// /// The function returns: /// /// * `Poll::Pending` if the socket is not read...
  * `poll_recv` (Impact: 6.9)
    * *Intent:* /// /// # Return value /// /// The function returns: /// /// * `Poll::Pending` if the socket is not ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 133`, `args: 108`, `func_start: 72`, `class_start: 1`
* *Risk/State:* `state_mutation: 2`, `dead_code: 173`, `unreferenced_by_name: 47`
* *Architecture:* `io: 7`, `api: 62`, `concurrency: 33`, `import: 14`
* *Defense:* `safety: 4`, `doc: 1604`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.171
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AsRawFd, BorrowedFd, BorrowedSocket, Context, Interest, IntoRawFd, IntoRawSocket, Ipv4Addr...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tokio-util/tests/time_delay_queue.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 350.74 | **LOC:** 900 | **CtrlFlow:** 3.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (41.3623%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `multi_delay_at_start` (Impact: 8.1)
  * `compact_change_deadline` (Impact: 6.6)
  * `compact_remove_remapped_keys` (Impact: 4.0)
  * `item_expiry_greater_than_wheel` (Impact: 3.8)
  * `insert_after_ready_poll` (Impact: 3.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 16 instances
* *Amplified Cascading Flux:* 13 instances
* *High Risk Execution (weighted view):* 1
* *Concurrency (weighted view):* 193
* *State Mutation (weighted view):* 53
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 242`, `args: 38`, `func_start: 34`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 27`, `dead_code: 2`, `fragile_debt: 2`, `unreferenced_by_name: 33`
* *Architecture:* `concurrency: 113`, `import: 4`
* *Defense:* `safety: 1`, `doc: 9`, `test: 117`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.171
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Duration, Instant, assert_ready, futures::StreamExt, sleep, sleep_until, task, tokio::time::self...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tokio/tests/io_async_fd.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 346.62 | **LOC:** 959 | **CtrlFlow:** 3.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (44.0182%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `drain` (Impact: 7.5)
  * `await_error_readiness_invalid_address` (Impact: 6.5)
  * `send_oob_data` (Impact: 6.0)
  * `poll_fns` (Impact: 5.8)
  * `configure_timestamping_socket` (Impact: 5.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Rce:* 2 instances
* *Amplified Race Conditions:* 19 instances
* *Amplified Cascading Flux:* 5 instances
* *High Risk Execution (weighted view):* 15
* *Concurrency (weighted view):* 161
* *Memory Alloc (weighted view):* 6
* *Sec Tainted Injection (weighted view):* 2
* *State Mutation (weighted view):* 49
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 293`, `args: 65`, `func_start: 46`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 80`, `high_risk_execution: 16`, `state_mutation: 39`, `dead_code: 1`, `planned_debt: 2`, `unreferenced_by_name: 25`
* *Architecture:* `io: 14`, `concurrency: 66`, `import: 19`
* *Defense:* `safety: 2`, `test: 46`, `sync_locks: 9`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.171
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AddressFamily, Arc, AsyncFdReadyGuard, ErrorKind, F_GETFL, F_SETFL, Ordering, RawFd...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tokio/src/runtime/builder.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 339.94 | **LOC:** 1893 | **CtrlFlow:** 3.5% | **Authorship Centralization:** 27.3%
- **Risk Profile:** Cognitive Load (41.5805%), Tech Debt (8.2922%)
**Top Internal Functions/Classes:**
  * `fmt` (Impact: 8.2)
  * `build_current_thread_runtime_components` (Impact: 6.2)
  * `build_local` (Impact: 5.6)
    * *Intent:* /// /// # Examples /// /// ``` /// use tokio::runtime::{Builder, LocalOptions}; /// /// let rt = Bui...
  * `unhandled_panic` (Impact: 5.6)
    * *Intent:* /// rt.spawn(async { panic!("boom"); }); /// rt.spawn(async { /// // This task never completes. /// ...
  * `new` (Impact: 5.5)
    * *Intent:* /// Returns a new runtime builder initialized with default configuration /// values. /// /// Configu...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 18 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 114
* *State Mutation (weighted view):* 33
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 144`, `args: 54`, `func_start: 45`, `class_start: 3`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 29`, `dead_code: 99`, `planned_debt: 1`
* *Architecture:* `io: 1`, `api: 60`, `concurrency: 24`, `import: 21`
* *Defense:* `safety: 2`, `doc: 1226`, `test: 7`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.171
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Arc, Callback, HistogramBuilder, HistogramScale, LocalOptions, LocalRuntime, LogHistogram, MultiThread...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tokio-macros/src/entry.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 337.9 | **LOC:** 782 | **CtrlFlow:** 16.0% | **Authorship Centralization:** 20.0%
- **Risk Profile:** Cognitive Load (14.3886%), Tech Debt (8.143%)
**Top Internal Functions/Classes:**
  * `build_config` (Impact: 43.0)
  * `parse_knobs` (Impact: 42.8)
  * `parse` (Impact: 17.9)
  * `is_test_attribute` (Impact: 15.3)
    * *Intent:* // Check whether given attribute is a test attribute of forms: // * `#[test]` // * `#[core::prelude:...
  * `main` (Impact: 13.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 47
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 104`, `structural_boundaries: 138`, `args: 45`, `func_start: 28`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 17`, `planned_debt: 1`
* *Architecture:* `api: 2`, `concurrency: 5`, `import: 6`
* *Defense:* `safety: 16`, `doc: 5`, `test: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.171
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Attribute, Ident, ParseStream, Parser, Path, RuntimeFlavor, Signature, ToTokens...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tokio/src/runtime/scheduler/current_thread/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 335.3 | **LOC:** 887 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 37.5%
- **Risk Profile:** Cognitive Load (16.6862%), Tech Debt (73.6802%)
**Top Internal Functions/Classes:**
  * `block_on` (Impact: 28.7)
  * `block_on` (Impact: 16.1)
  * `park` (Impact: 13.4)
    * *Intent:* /// Blocks the current thread until an event is received by the driver, /// including I/O events, ti...
  * `dump` (Impact: 10.9)
    * *Intent:* /// Capture a snapshot of this runtime's state.
  * `shutdown` (Impact: 10.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 17 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 66
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 151`, `args: 66`, `func_start: 46`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 3`, `state_mutation: 32`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 12`
* *Architecture:* `api: 28`, `concurrency: 12`, `import: 25`
* *Defense:* `safety: 21`, `doc: 61`, `test: 2`, `sync_locks: 2`, `immutability_locks: 2`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.171
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Acquire, Config, Defer, Driver, Future, Inject, JoinHandle, MetricsBatch...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tokio-util/tests/task_join_queue.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 329.44 | **LOC:** 380 | **CtrlFlow:** 8.9% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (49.9601%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_join_queue_with_manual_abort` (Impact: 8.0)
  * `test_join_queue_abort_all` (Impact: 7.5)
  * `test_join_queue_try_join_next_with_id_disabled_coop` (Impact: 6.3)
  * `test_join_queue_join_next_with_id` (Impact: 5.8)
  * `test_join_queue_try_join_next_disabled_coop` (Impact: 5.8)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.171
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` assert_ready, task, tokio::sync::oneshot, tokio::task::yield_now, tokio::time::Duration, tokio_test::assert_pending, tokio_util::task::JoinQueue
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tokio-stream/tests/stream_stream_map.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 326.38 | **LOC:** 564 | **CtrlFlow:** 1.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.9589%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `poll_next_many_correctly_loops_around` (Impact: 4.1)
  * `next_many_correctly_loops_around` (Impact: 4.1)
  * `multiple_entries` (Impact: 3.9)
  * `single_entry` (Impact: 2.9)
  * `one_ready_many_none` (Impact: 2.8)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.171
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Future, Pin, Stream, StreamExt, StreamMap, assert_pending, assert_ready, futures::stream::iter...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tokio/src/sync/notify.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 320.16 | **LOC:** 1418 | **CtrlFlow:** 10.4% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (24.5783%), Tech Debt (69.9408%)
**Top Internal Functions/Classes:**
  * `poll_notified` (Impact: 58.0)
  * `inner_notify_waiters` (Impact: 17.6)
  * `notify_locked` (Impact: 16.1)
  * `drop_notified` (Impact: 10.7)
  * `notify_with_strategy` (Impact: 8.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 97
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 62`, `structural_boundaries: 156`, `args: 50`, `func_start: 43`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 3`, `state_mutation: 43`, `dead_code: 60`, `duplicate_logic: 8`
* *Architecture:* `api: 18`, `concurrency: 8`, `import: 13`
* *Defense:* `safety: 12`, `doc: 528`, `test: 3`, `sync_locks: 13`, `immutability_locks: 10`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.171
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Acquire, GuardedLinkedList, LinkedList, Poll, Relaxed, Release, SeqCst, UnwindSafe...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tokio/src/sync/broadcast.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 310.48 | **LOC:** 1760 | **CtrlFlow:** 9.9% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (17.5196%), Tech Debt (88.3235%)
**Top Internal Functions/Classes:**
  * `recv_ref` (Impact: 22.6)
    * *Intent:* /// Locks the next value if there is one.
  * `notify_rx` (Impact: 13.5)
  * `drop` (Impact: 8.4)
  * `upgrade` (Impact: 6.9)
    * *Intent:* /// Tries to convert a `WeakSender` into a [`Sender`]. /// /// This will return `Some` if there are ...
  * `len` (Impact: 6.6)
    * *Intent:* /// tx.send(30).unwrap(); /// /// assert_eq!(tx.len(), 3); /// /// rx1.recv().await.unwrap(); /// //...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 76
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 191`, `args: 63`, `func_start: 58`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 34`, `dead_code: 66`, `duplicate_logic: 6`, `unreferenced_by_name: 13`
* *Architecture:* `api: 33`, `concurrency: 8`, `import: 17`
* *Defense:* `safety: 5`, `doc: 859`, `test: 15`, `sync_locks: 25`, `immutability_locks: 1`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.171
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Acquire, AtomicUsize, Context, GuardedLinkedList, LinkedList, Mutex, MutexGuard, Poll...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tokio/src/runtime/tests/loom_multi_thread.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 293.9 | **LOC:** 462 | **CtrlFlow:** 9.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (39.238%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `gated2` (Impact: 11.7)
  * `blocking_and_regular_inner` (Impact: 10.3)
  * `only_blocking_inner` (Impact: 6.6)
  * `pool_multi_notify` (Impact: 5.7)
  * `pool_multi_spawn` (Impact: 5.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 21 instances
* *Amplified Cascading Flux:* 9 instances
* *Concurrency (weighted view):* 169
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 128`, `args: 43`, `func_start: 25`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 9`, `unreferenced_by_name: 12`
* *Architecture:* `api: 3`, `concurrency: 64`, `import: 21`
* *Defense:* `doc: 7`, `test: 13`, `sync_locks: 4`, `immutability_locks: 1`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.171
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AtomicUsize, Context, Future, Poll, Runtime, SeqCst, crate::runtime::self, crate::runtime::tests::loom_oneshot...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `tokio/src/runtime/mod.rs` -> Churn: **88.55%** | Cog Load: 4.4923% | Debt: 85.5459%
- `tokio/src/runtime/scheduler/current_thread/mod.rs` -> Churn: **81.14%** | Cog Load: 16.6862% | Debt: 73.6802%
- `tokio/src/lib.rs` -> Churn: **72.63%** | Cog Load: 0.0% | Debt: 66.8458%
- `tokio/src/fs/open_options.rs` -> Churn: **66.16%** | Cog Load: 6.7398% | Debt: 99.1922%
- `tokio/src/net/tcp/stream.rs` -> Churn: **66.16%** | Cog Load: 8.0282% | Debt: 50.6313%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `tokio-util/src/time/delay_queue.rs` -> **Lucas Black** (100.0% isolated ownership) | Magnitude: 383.16
- `tokio/src/net/windows/named_pipe.rs` -> **Qi** (100.0% isolated ownership) | Magnitude: 363.94
- `tokio/tests/io_async_fd.rs` -> **Ralf Jung** (100.0% isolated ownership) | Magnitude: 346.62
- `tokio/src/process/mod.rs` -> **Qi** (100.0% isolated ownership) | Magnitude: 286.64
- `tokio/src/sync/batch_semaphore.rs` -> **Qi** (100.0% isolated ownership) | Magnitude: 273.26

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `tokio/src/io/util/mem.rs` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 63.2104%)
- `tokio/src/sync/oneshot.rs` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 37.4602%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `tokio/src/io/ready.rs` -> **Severity: 1.639** (Embedded: 0.0239 * Error Risk: 68.5751%)
- `tokio/src/io/util/mem.rs` -> **Severity: 1.058** (Embedded: 0.0242 * Error Risk: 43.7699%)
- `tokio/src/time/sleep.rs` -> **Severity: 0.288** (Embedded: 0.0096 * Error Risk: 29.9133%)
- `tokio-util/src/io/simplex.rs` -> **Severity: 0.126** (Embedded: 0.0025 * Error Risk: 49.6471%)
- `tokio/src/io/util/copy_bidirectional.rs` -> **Severity: 0.124** (Embedded: 0.0025 * Error Risk: 48.9191%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `tokio/src/io/util/mem.rs` -> **Severity: 1602.164** (Blast Radius: 19.582 * Doc Risk: 81.8182%)
- `tokio/src/io/ready.rs` -> **Severity: 1109.602** (Blast Radius: 31.581 * Doc Risk: 35.1351%)
- `tokio/src/time/sleep.rs` -> **Severity: 403.237** (Blast Radius: 10.945 * Doc Risk: 36.8421%)
- `tokio/src/io/stdout.rs` -> **Severity: 278.912** (Blast Radius: 3.161 * Doc Risk: 88.2353%)
- `tokio/src/sync/oneshot.rs` -> **Severity: 240.606** (Blast Radius: 5.649 * Doc Risk: 42.5926%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
