# ARCHITECTURAL_BRIEF: tokio
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_rust/tokio` |
| **Timestamp** | `2026-08-03T19:47:39.134025+00:00` |
| **Scan Duration** | `2.48s` |
| **Git Branch** | `master` |
| **Git Commit** | `1fc450aefba4b05cdff9b7825ca5e39cccb3780e` |
| **Git Remote** | `https://github.com/tokio-rs/tokio.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 743 malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are analyzing software architecture through the lens of GitGalaxy Static Application Security Testing (SAST). GitGalaxy translates the non-visual architecture of repositories into measurable technical metrics.
> 
> **CORE DIRECTIVES:**
> 1. **Measure Risk, Not Quality:** Do not judge. We measure Risk Exposure (e.g., Cognitive Load Exposure). Frame all insights as blameless, objective observations. High risk highlights where the architecture might be drifting into fragile territory, not developer incompetence.
> 2. **The Physical Reality Rule:** Base your analysis strictly on the provided Structural Signatures (regex hit counts). Do not hallucinate meaning.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`.
> 
> **THE STRUCTURAL SIGNATURE LEXICON:**
> * **Structure & Mass:** `branch` (splits), `linear` (paths), `args` (coupling), `func_start` (entry points).
> * **Risk & Volatility:** `danger` (dynamic execution), `flux` (state mutation), `graveyard` (commented-out logic), `safety_neg` (security bypasses).
> * **Architecture & Domain:** `io` (network latency), `concurrency` (async orchestration), `api` (public surface), `import` (dependencies).
> * **Defensive Guardrails:** `safety` (Error handling), `freeze_hits` (immutability), `cleanup` (state destruction).
## 2. THE 13-POINT RISK EXPOSURE ANALYSIS (EQUATIONS & CONTEXT)
> **How the SAST Engine Calculates Risk Exposure (Lower Risk 0 - Higher Risk Exposure 100%):**
> Most scores use a Sigmoid curve based on density (Hits / LOC) to prevent massive files from mathematically hiding their flaws.
> 
> 1. **Cognitive Load Exposure:** Measures the mental effort required for a developer to read and understand the file. `Density(Branches + (Flux * 2) + Async/Danger)` mitigated by `Doc Coverage`.
> 2. **Error & Exception Risk Exposure:** Measures structural integrity and resilience against runtime errors. `Net Exposure = (Danger + Safety_Neg + Flux) - (Safety + Tests + Docs)`.
> 3. **Tech Debt Exposure:** Measures the density of developer-annotated structural stress. `Density(TODOs [1x] + FIXMEs/Hacks [3x] + Empty Stubs [0.5x])`.
> 4. **Verification Risk Exposure:** Evaluates test coverage by comparing a function's structural complexity against the scope of the tests validating it.
> 5. **API Risk Exposure:** Measures the public surface area of a module. `Ratio(API Hits / Total Functions & Classes)`.
> 6. **Concurrency Risk Exposure:** Measures the density of asynchronous operations, threading, and parallel execution logic.
> 7. **State Flux Risk Exposure:** Measures the frequency of data mutation and variable reassignment.
> 8. **Commented Logic (dead code):** Measures the presence of abandoned, commented-out logic blocks.
> 9. **Spec Match Risk Exposure:** Measures how closely code aligns with formal specifications or architectural requirements.
> 10. **Stability:** Measures the recency of edits relative to the repository's entire lifespan.
> 11. **Deep Churn:** Measures the historical volatility and frequency of modification.
> 12. **Documentation Risk Exposure:** Measures the lack of structured documentation and ownership metadata.
> 13. **Indentation Consistency:** Measures formatting alignment (Tabs vs. Spaces). Provided for codebase standardization context, not a functional risk.
> 
> **--- THE SECURITY & VULNERABILITY LENS ---**
> 14. **Obfuscation & Evasion Risk:** Measures the density of obfuscated logic, packed strings, and non-standard encoding.
> 15. **Logic Bomb / Sabotage Risk:** Measures condition-heavy execution leading to destructive OS, memory, or process commands.
> 16. **Injection Surface Risk Exposure:** Measures external network/I/O input flowing directly into dynamic execution contexts (XSS, SQLi, RCE).
> 17. **Memory Corruption Risk Exposure:** Measures the density of raw pointer math and manual memory allocations (Buffer Overflows, UAF).
> 18. **Secrets Risk Exposure:** Measures the presence of hardcoded credentials exposed to logs or globals.
> 
> **--- STRUCTURAL MAGNITUDE (NOT RISK) ---**
> **19. Function Magnitude (Impact Score):** Measures the physical footprint and 'heaviness' of a specific function. `((BranchHits + 1) * (Args + 1) + (0.05 * LOC)) * 10`. This is NOT a risk score.
> **20. File Magnitude (Total Impact):** Measures the total structural impact of a file. `Sum(Function Impacts) + API + Concurrency + Flux + (LOC / 50)`. This is NOT a risk score.

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 844 |
| Analyzed Artifacts (Scanned) | 758 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 86 |
| Total LOC | 85747 |
| Volatility Index | 0.005 |
| % Scanned of codebase = | 89.8% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7298 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3191 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.1309 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 13 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUST | 743 | 85699 | 98.0% |
| MARKDOWN | 14 | 0 | 1.8% |
| JSON | 1 | 48 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.258`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_4 | 279 | 36.8% |
| file_cluster_13 | 176 | 23.2% |
| file_cluster_0 | 114 | 15.0% |
| file_cluster_8 | 92 | 12.1% |
| file_cluster_16 | 70 | 9.2% |
| file_cluster_6 | 6 | 0.8% |
| file_cluster_11 | 4 | 0.5% |
| file_cluster_17 | 2 | 0.3% |
| file_cluster_1 | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 14 | 1.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 86*

**Composition by Extension & Reason:**
- `.rs`: 26x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 13x Unsupported Format (.toml), 4x Excluded (Unsupported Extension: '.toml'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 14x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 4356 LOC)
- `.yml`: 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.stderr`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.dic`: 1x Excluded (Unsupported Extension: '.dic')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 30.8 | 29.3 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.5 | 38.8 | 37.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 29.2 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 17.8 | 2.3 | 0.0 |
| API Exposure | 0.0 | 9.7 | 2.6 | 2.7 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 62.9 | 100.0 | 100.0 |
| State Flux Exposure | 0.0 | 100.0 | 40.9 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 14.7 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 94.9 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 9.7 | 1.9 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 92.5 | 7.9 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 32.6 | 13.9 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 53.9 | 74.9 | 100.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 20.0 | 8.1 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.3 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.2 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tokio/tests/async_send_sync.rs` (Hits: 35)
- `tokio/tests/fs_file.rs` (Hits: 35)
- `tokio/src/fs/file/tests.rs` (Hits: 28)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **mem.rs** (`tokio/src/io/util/mem.rs`) — 19 inbound connections
2. **ready.rs** (`tokio/src/io/ready.rs`) — 7 inbound connections
3. **oneshot.rs** (`tokio/src/sync/oneshot.rs`) — 5 inbound connections
4. **sleep.rs** (`tokio/src/time/sleep.rs`) — 5 inbound connections
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

- `new` (@ `tokio/src/sync/broadcast.rs`) -> Impact: **702.2** | LOC: 604
- `connect_mio` (@ `tokio/src/net/tcp/stream.rs`) -> Impact: **504.6** | LOC: 733
  * *Intent:* /// use std::error::Error; /// /// #[tokio::main] /// async fn main() -> Result<(), Box<dyn Error>> { /// // Connect to a peer /// let mut stream = Tc...
- `block_in_place` (@ `tokio/src/runtime/scheduler/multi_thread/worker.rs`) -> Impact: **488.8** | LOC: 683
- `scope_inner` (@ `tokio/src/task/task_local.rs`) -> Impact: **466.4** | LOC: 249
- `poll_copy` (@ `tokio/src/io/util/copy.rs`) -> Impact: **379.5** | LOC: 181
- `spawn_pinned` (@ `tokio-util/src/task/spawn_pinned.rs`) -> Impact: **318.1** | LOC: 189
  * *Intent:* /// let pool = LocalPoolHandle::new(1); /// /// // Spawn a !Send future onto the pool and await it /// let output = pool /// .spawn_pinned(|| { /// //...
- `reserve_disarm` (@ `tokio/tests/sync_mpsc.rs`) -> Impact: **260.4** | LOC: 965
- `poll_write` (@ `tokio-test/src/io.rs`) -> Impact: **238.9** | LOC: 83
- `run` (@ `tokio/src/runtime/blocking/pool.rs`) -> Impact: **233.7** | LOC: 101
- `windows_main` (@ `examples/named-pipe-ready.rs`) -> Impact: **225.4** | LOC: 144

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `async_read_std_file` (@ `benches/fs.rs`) -> **O(2^N) [Recursive]**
- `async_read_buf` (@ `benches/fs.rs`) -> **O(2^N) [Recursive]**
- `main` (@ `examples/echo-tcp.rs`) -> **O(2^N) [Recursive]**
  * *Intent:* //! //! Because the Tokio runtime uses a thread pool, each TCP connection is //! processed concurrently with all other TCP connections across multiple...
- `main` (@ `examples/graceful-shutdown.rs`) -> **O(2^N) [Recursive]**
- `main` (@ `examples/proxy.rs`) -> **O(2^N) [Recursive]**
  * *Intent:* //! A proxy that forwards data to another server and forwards that server's //! responses back to clients. //! //! Because the Tokio runtime uses a th...
- `contains_impl_trait` (@ `tokio-macros/src/entry.rs`) -> **O(2^N) [Recursive]**
- `poll_next` (@ `tokio-stream/src/stream_ext/chunks_timeout.rs`) -> **O(2^N) [Recursive]**
- `poll_next` (@ `tokio-stream/src/stream_ext/filter.rs`) -> **O(2^N) [Recursive]**
- `poll_next` (@ `tokio-stream/src/stream_ext/filter_map.rs`) -> **O(2^N) [Recursive]**
- `poll_next` (@ `tokio-stream/src/stream_ext/skip.rs`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `poll_read_internal` (@ `tokio/src/io/util/mem.rs`) -> DB Complexity: **75**
  * *Intent:* /// /// The `max_buf_size` argument is the maximum amount of bytes that can be /// written to a buffer before the it returns `Poll::Pending`. /// /// ...
- `connect_mio` (@ `tokio/src/net/tcp/stream.rs`) -> DB Complexity: **68**
  * *Intent:* /// use std::error::Error; /// /// #[tokio::main] /// async fn main() -> Result<(), Box<dyn Error>> { /// // Connect to a peer /// let mut stream = Tc...
- `reserve_disarm` (@ `tokio/tests/sync_mpsc.rs`) -> DB Complexity: **57**
- `block_in_place` (@ `tokio/src/runtime/scheduler/multi_thread/worker.rs`) -> DB Complexity: **47**
- `new` (@ `tokio/src/sync/broadcast.rs`) -> DB Complexity: **27**
- `maybe_pending_seek` (@ `tokio/tests/io_buf_reader.rs`) -> DB Complexity: **25**
  * *Intent:* // https://github.com/rust-lang/futures-rs/pull/1573#discussion_r281162309
- `for_each` (@ `tokio/src/util/idle_notified_set.rs`) -> DB Complexity: **22**
  * *Intent:* // Safety: We just put the entry in the idle list, so it is in one of the lists.
- `write_all_vectored_with_empty_slice` (@ `tokio-util/tests/io_write_all_vectored.rs`) -> DB Complexity: **21**
- `poll_write_vectored` (@ `tokio-util/tests/io_inspect.rs`) -> DB Complexity: **20**
- `maybe_pending_buf_writer_seek` (@ `tokio/tests/io_buf_writer.rs`) -> DB Complexity: **20**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `tokio/tests` | 160 | 28832.58 | 34.09% | 0.0% |
| `tokio-util/tests` | 29 | 5865.96 | 32.15% | 0.0% |
| `tokio/src/sync` | 12 | 4660.52 | 29.27% | 66.86% |
| `tokio/src/io/util` | 37 | 3726.04 | 42.57% | 26.95% |
| `benches` | 16 | 3553.88 | 72.24% | 8.09% |
| `tokio/src/sync/tests` | 14 | 2148.54 | 35.32% | 0.0% |
| `examples` | 21 | 2045.56 | 45.26% | 0.0% |
| `tokio-stream/src/stream_ext` | 23 | 2025.84 | 63.67% | 14.71% |
| `tokio/src/runtime/tests` | 11 | 1973.8 | 31.87% | 0.0% |
| `tokio/src/io` | 18 | 1973.3 | 27.3% | 53.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `tokio-stream/src/stream_ext/collect.rs` -> **100.0%** Exposure
- `tokio-stream/src/wrappers/signal_windows.rs` -> **100.0%** Exposure
- `tokio-test/src/task.rs` -> **100.0%** Exposure
- `tokio-util/src/compat.rs` -> **100.0%** Exposure
- `tokio-util/src/future/with_cancellation_token.rs` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `benches/fs.rs` -> **100.0%** Exposure
- `benches/sync_mpsc.rs` -> **100.0%** Exposure
- `tests-integration/src/bin/test-cat.rs` -> **100.0%** Exposure
- `tokio-util/src/io/read_arc.rs` -> **100.0%** Exposure
- `tokio-util/src/time/wheel/stack.rs` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tokio-util/tests/length_delimited.rs` -> **35** Orphaned Functions | **2** Duplicates
- `tokio/src/io/async_write.rs` -> **0** Orphaned Functions | **37** Duplicates
- `tokio/tests/rt_common.rs` -> **35** Orphaned Functions | **2** Duplicates
- `tokio-stream/src/stream_ext/collect.rs` -> **0** Orphaned Functions | **36** Duplicates
- `tokio/src/sync/mutex.rs` -> **0** Orphaned Functions | **36** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`tokio/src/macros/select.rs`** -> AI Confidence: **99.31%**
2. **`tokio/src/net/unix/pipe.rs`** -> AI Confidence: **99.31%**
3. **`tokio/src/sync/rwlock/owned_read_guard.rs`** -> AI Confidence: **99.31%**
4. **`tokio/tests/task_blocking.rs`** -> AI Confidence: **99.31%**
5. **`tokio/src/macros/thread_local.rs`** -> AI Confidence: **99.29%**
6. **`tokio-macros/src/entry.rs`** -> AI Confidence: **99.24%**
7. **`tokio-test/src/macros.rs`** -> AI Confidence: **99.24%**
8. **`tokio-util/src/task/join_queue.rs`** -> AI Confidence: **99.24%**
9. **`tokio/src/net/udp.rs`** -> AI Confidence: **99.24%**
10. **`tokio/src/sync/once_cell.rs`** -> AI Confidence: **99.24%**
11. **`tokio/src/task/builder.rs`** -> AI Confidence: **99.24%**
12. **`tokio/src/loom/std/barrier.rs`** -> AI Confidence: **99.23%**
13. **`tokio/src/runtime/task/state.rs`** -> AI Confidence: **99.23%**
14. **`benches/fs.rs`** -> AI Confidence: **99.18%**
15. **`benches/signal.rs`** -> AI Confidence: **99.18%**
16. **`benches/sync_mpsc.rs`** -> AI Confidence: **99.18%**
17. **`benches/sync_notify.rs`** -> AI Confidence: **99.18%**
18. **`examples/connect-tcp.rs`** -> AI Confidence: **99.18%**
19. **`examples/graceful-shutdown.rs`** -> AI Confidence: **99.18%**
20. **`examples/tinyhttp.rs`** -> AI Confidence: **99.18%**
21. **`examples/udp-codec.rs`** -> AI Confidence: **99.18%**
22. **`tokio-stream/src/empty.rs`** -> AI Confidence: **99.18%**
23. **`tokio-stream/src/stream_close.rs`** -> AI Confidence: **99.18%**
24. **`tokio-stream/src/stream_ext/all.rs`** -> AI Confidence: **99.18%**
25. **`tokio-stream/src/stream_ext/any.rs`** -> AI Confidence: **99.18%**
26. **`tokio-stream/src/stream_ext/collect.rs`** -> AI Confidence: **99.18%**
27. **`tokio-stream/src/stream_ext/filter.rs`** -> AI Confidence: **99.18%**
28. **`tokio-stream/src/stream_ext/filter_map.rs`** -> AI Confidence: **99.18%**
29. **`tokio-stream/src/stream_ext/skip_while.rs`** -> AI Confidence: **99.18%**
30. **`tokio-stream/src/stream_ext/take.rs`** -> AI Confidence: **99.18%**
31. **`tokio-stream/src/stream_ext/throttle.rs`** -> AI Confidence: **99.18%**
32. **`tokio-stream/src/stream_ext/timeout.rs`** -> AI Confidence: **99.18%**
33. **`tokio-stream/src/wrappers/broadcast.rs`** -> AI Confidence: **99.18%**
34. **`tokio-stream/src/wrappers/mpsc_bounded.rs`** -> AI Confidence: **99.18%**
35. **`tokio-stream/src/wrappers/mpsc_unbounded.rs`** -> AI Confidence: **99.18%**
36. **`tokio-test/src/stream_mock.rs`** -> AI Confidence: **99.18%**
37. **`tokio-util/src/future/with_cancellation_token.rs`** -> AI Confidence: **99.18%**
38. **`tokio-util/src/io/write_all_vectored.rs`** -> AI Confidence: **99.18%**
39. **`tokio-util/src/sync/mpsc.rs`** -> AI Confidence: **99.18%**
40. **`tokio-util/src/sync/poll_semaphore.rs`** -> AI Confidence: **99.18%**
41. **`tokio-util/src/task/abort_on_drop.rs`** -> AI Confidence: **99.18%**
42. **`tokio-util/src/task/spawn_pinned.rs`** -> AI Confidence: **99.18%**
43. **`tokio-util/src/task/task_tracker.rs`** -> AI Confidence: **99.18%**
44. **`tokio-util/src/udp/frame.rs`** -> AI Confidence: **99.18%**
45. **`tokio-util/src/util/poll_buf.rs`** -> AI Confidence: **99.18%**
46. **`tokio-util/tests/length_delimited.rs`** -> AI Confidence: **99.18%**
47. **`tokio/src/fs/mocks.rs`** -> AI Confidence: **99.18%**
48. **`tokio/src/io/async_fd.rs`** -> AI Confidence: **99.18%**
49. **`tokio/src/io/blocking.rs`** -> AI Confidence: **99.18%**
50. **`tokio/src/io/seek.rs`** -> AI Confidence: **99.18%**
51. **`tokio/src/io/uring/open.rs`** -> AI Confidence: **99.18%**
52. **`tokio/src/io/util/chain.rs`** -> AI Confidence: **99.18%**
53. **`tokio/src/io/util/fill_buf.rs`** -> AI Confidence: **99.18%**
54. **`tokio/src/io/util/read_buf.rs`** -> AI Confidence: **99.18%**
55. **`tokio/src/io/util/read_to_end.rs`** -> AI Confidence: **99.18%**
56. **`tokio/src/io/util/write_all.rs`** -> AI Confidence: **99.18%**
57. **`tokio/src/net/addr.rs`** -> AI Confidence: **99.18%**
58. **`tokio/src/net/tcp/listener.rs`** -> AI Confidence: **99.18%**
59. **`tokio/src/net/tcp/socket.rs`** -> AI Confidence: **99.18%**
60. **`tokio/src/net/tcp/split.rs`** -> AI Confidence: **99.18%**
61. **`tokio/src/net/tcp/split_owned.rs`** -> AI Confidence: **99.18%**
62. **`tokio/src/net/unix/split.rs`** -> AI Confidence: **99.18%**
63. **`tokio/src/net/unix/split_owned.rs`** -> AI Confidence: **99.18%**
64. **`tokio/src/net/windows/named_pipe.rs`** -> AI Confidence: **99.18%**
65. **`tokio/src/process/unix/pidfd_reaper.rs`** -> AI Confidence: **99.18%**
66. **`tokio/src/runtime/context/blocking.rs`** -> AI Confidence: **99.18%**
67. **`tokio/src/runtime/context/current.rs`** -> AI Confidence: **99.18%**
68. **`tokio/src/runtime/driver/op.rs`** -> AI Confidence: **99.18%**
69. **`tokio/src/runtime/handle.rs`** -> AI Confidence: **99.18%**
70. **`tokio/src/runtime/local_runtime/runtime.rs`** -> AI Confidence: **99.18%**
71. **`tokio/src/runtime/scheduler/multi_thread/queue.rs`** -> AI Confidence: **99.18%**
72. **`tokio/src/runtime/task/core.rs`** -> AI Confidence: **99.18%**
73. **`tokio/src/runtime/task/list.rs`** -> AI Confidence: **99.18%**
74. **`tokio/src/runtime/task/mod.rs`** -> AI Confidence: **99.18%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `tokio-util/tests/length_delimited.rs` -> **0.0018%** Exposure
- `tokio-util/tests/framed_read.rs` -> **0.0003%** Exposure
- `tokio-util/tests/framed_write.rs` -> **0.0002%** Exposure
### Exploit Generation Surface
- `benches/copy.rs` -> **20.0%** Exposure
- `benches/fs.rs` -> **20.0%** Exposure
- `benches/remote_spawn.rs` -> **20.0%** Exposure
- `benches/rt_current_thread.rs` -> **20.0%** Exposure
- `benches/rt_multi_threaded.rs` -> **20.0%** Exposure
### Weaponizable Injection Vectors
- `tokio/tests/io_async_fd.rs` -> **99.9898%** Exposure
- `tokio/tests/fs_file.rs` -> **98.3535%** Exposure
### Raw Memory Manipulation
- `tokio/src/io/util/async_read_ext.rs` -> **0.1978%** Exposure
- `tokio/src/runtime/time_alt/entry.rs` -> **0.0649%** Exposure
- `tokio/src/io/read_buf.rs` -> **0.0069%** Exposure
- `tokio/src/runtime/task/core.rs` -> **0.0018%** Exposure
- `tokio-test/src/task.rs` -> **0.001%** Exposure
### Algorithmic DoS Exposure
- `benches/copy.rs` -> **100.0%** Exposure
- `benches/fs.rs` -> **100.0%** Exposure
- `benches/signal.rs` -> **100.0%** Exposure
- `benches/sync_mpsc.rs` -> **100.0%** Exposure
- `examples/connect-tcp.rs` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `7177` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `tokio/src/fs/read_uring.rs` (RUST) -> Cumulative Risk: **833.44**
- **Archetype:** `file_cluster_4` (Distance: 13.064 IQR)
- **Magnitude:** 166.32 | **LOC:** 135 | **CtrlFlow:** 28.3% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `read_to_end_uring` (Impact: 49.7), `op_read` (Impact: 25.6), `read_uring` (Impact: 12.9)

### 2. `tokio/src/task/coop/mod.rs` (RUST) -> Cumulative Risk: **831.58**
- **Archetype:** `file_cluster_0` (Distance: 23.737 IQR)
- **Magnitude:** 143.38 | **LOC:** 574 | **CtrlFlow:** 35.6% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Tech Debt (99.984%), State Flux (97.0444%)
- **Heaviest Functions:** `decrement` (Impact: 30.8), `poll` (Impact: 26.5), `poll_budget_available` (Impact: 10.6)

### 3. `benches/sync_mpsc.rs` (RUST) -> Cumulative Risk: **830.52**
- **Archetype:** `file_cluster_4` (Distance: 12.338 IQR)
- **Magnitude:** 781.92 | **LOC:** 332 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `contention_bounded_recv_many` (Impact: 40.4), `contention_bounded_full_recv_many` (Impact: 40.4), `contention_unbounded_recv_many` (Impact: 40.4)

### 4. `benches/copy.rs` (RUST) -> Cumulative Risk: **827.83**
- **Archetype:** `file_cluster_4` (Distance: 12.928 IQR)
- **Magnitude:** 339.58 | **LOC:** 251 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), State Flux (99.998%)
- **Heaviest Functions:** `copy_chunk_to_mem` (Impact: 41.0), `copy_chunk_to_slow_hdd` (Impact: 41.0), `copy_mem_to_mem` (Impact: 34.3)

### 5. `tokio/src/runtime/scheduler/current_thread/mod.rs` (RUST) -> Cumulative Risk: **824.11**
- **Archetype:** `file_cluster_13` (Distance: 13.722 IQR)
- **Magnitude:** 754.24 | **LOC:** 887 | **CtrlFlow:** 30.2% | **Authorship Centralization:** 37.5%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Concurrency (99.9913%)
- **Heaviest Functions:** `block_on` (Impact: 100.0), `unhandled_panic` (Impact: 86.3), `block_on` (Impact: 44.4)

### 6. `tokio/src/runtime/time_alt/tests.rs` (RUST) -> Cumulative Risk: **818.1**
- **Archetype:** `file_cluster_0` (Distance: 12.174 IQR)
- **Magnitude:** 190.02 | **LOC:** 169 | **CtrlFlow:** 28.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.9987%)
- **Heaviest Functions:** `wake_up_in_the_different_thread` (Impact: 38.1), `cancel_in_the_different_thread` (Impact: 32.5), `wake_up_in_the_same_thread` (Impact: 27.4)

### 7. `tokio-stream/src/stream_map.rs` (RUST) -> Cumulative Risk: **808.49**
- **Archetype:** `file_cluster_4` (Distance: 23.982 IQR)
- **Magnitude:** 519.42 | **LOC:** 819 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Concurrency (99.9993%), State Flux (99.6675%)
- **Heaviest Functions:** `poll_next_many` (Impact: 151.5), `poll_next_entry` (Impact: 68.5), `size_hint` (Impact: 26.8)

### 8. `tokio-util/src/codec/framed_impl.rs` (RUST) -> Cumulative Risk: **802.8**
- **Archetype:** `file_cluster_13` (Distance: 12.748 IQR)
- **Magnitude:** 262.14 | **LOC:** 313 | **CtrlFlow:** 30.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Tech Debt (99.9608%)
- **Heaviest Functions:** `poll_next` (Impact: 61.7), `poll_flush` (Impact: 53.3), `poll_ready` (Impact: 10.7)

### 9. `tokio-stream/src/stream_ext/collect.rs` (RUST) -> Cumulative Risk: **798.4**
- **Archetype:** `file_cluster_16` (Distance: 13.102 IQR)
- **Magnitude:** 256.28 | **LOC:** 364 | **CtrlFlow:** 24.0% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `extend` (Impact: 25.3), `poll` (Impact: 21.7), `finalize` (Impact: 21.2)

### 10. `benches/fs.rs` (RUST) -> Cumulative Risk: **797.58**
- **Archetype:** `file_cluster_4` (Distance: 11.933 IQR)
- **Magnitude:** 365.48 | **LOC:** 113 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `async_read_std_file` (Impact: 95.1), `async_read_buf` (Impact: 95.0), `async_read_codec` (Impact: 54.6)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `tokio/tests/async_send_sync.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.41 IQR)
- **Top Global Matches:** file_cluster_4: 12.41, file_cluster_16: 13.076, file_cluster_0: 13.198
- **Magnitude:** 1979.32 | **LOC:** 779 | **CtrlFlow:** 17.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (50.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `as_raw_fd` (Impact: 3.6 | O(N^3))
  * `require_send` (Impact: 2.3 | O(N^1))
  * `require_sync` (Impact: 2.3 | O(N^1))
  * `require_unpin` (Impact: 2.3 | O(N^1))
  * `some_item` (Impact: 1.8 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 139`, `args: 9`, `func_start: 7`, `class_start: 8`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 83`, `planned_debt: 2`, `duplicate_logic: 3`, `orphaned_logic: 1`
* *Architecture:* `io: 35`, `concurrency: 1867`, `import: 21`
* *Defense:* `safety: 61`, `sync_locks: 28`, `immutability_locks: 2`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` tokio::net::unix::pipe::*, tokio::time::Duration, std::io::SeekFrom, tokio::net::TcpStream, std::pin::Pin, std::net::SocketAddr, tokio::io::unix::*, tokio::net::windows::named_pipe::*...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tokio/tests/sync_mpsc.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.156 IQR)
- **Top Global Matches:** file_cluster_4: 12.156, file_cluster_0: 12.667, file_cluster_13: 13.067
- **Magnitude:** 1407.62 | **LOC:** 1537 | **CtrlFlow:** 17.5% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(N^4) | **DB Complexity:** 57
- **Risk Profile:** Cognitive Load (50.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `reserve_disarm` (Impact: 260.4 | O(N^4) | DB: 57)
  * `send_recv_with_buffer` (Impact: 2.9 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 312`, `args: 76`, `func_start: 73`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 30`, `high_risk_execution: 3`, `state_mutation: 108`, `dead_code: 1`, `orphaned_logic: 2`
* *Architecture:* `api: 1`, `concurrency: 1020`, `import: 18`
* *Defense:* `safety: 37`, `test: 183`, `sync_locks: 5`, `immutability_locks: 3`, `cleanup: 44`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` tokio::sync::mpsc, futures::future::FutureExt, tokio::sync::mpsc::error::SendTimeoutError::Closed, std::future::Future, tokio::sync::mpsc::error::TryRecvError, std::sync::Arc, tokio::sync::mpsc::UnboundedReceiver, wasm_bindgen_test::wasm_bindgen_test...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tokio/tests/udp.rs` (RUST | Tier 2 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.741 IQR)
- **Top Global Matches:** file_cluster_4: 12.741, file_cluster_0: 13.349, file_cluster_8: 13.622
- **Magnitude:** 1125.84 | **LOC:** 771 | **CtrlFlow:** 34.4% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (48.7704%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `try_recv_buf` (Impact: 147.6 | O(2^N) | DB: 2)
  * `try_recv_buf_from` (Impact: 132.2 | O(2^N) | DB: 2)
  * `try_send_recv` (Impact: 74.9 | O(N^5) | DB: 2)
  * `try_send_to_recv_from` (Impact: 67.3 | O(N^4) | DB: 2)
  * `poll_ready` (Impact: 67.3 | O(N^4) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 107`, `structural_boundaries: 204`, `args: 21`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 61`, `state_mutation: 107`, `orphaned_logic: 7`
* *Architecture:* `io: 8`, `concurrency: 357`
* *Defense:* `safety: 60`, `doc: 1`, `test: 52`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` net::UdpSocket, tokio_test::assert_ok, std::io, std::future::poll_fn, std::sync::Arc, tokio::io::ReadBuf
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tokio/tests/task_join_set.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.527 IQR)
- **Top Global Matches:** file_cluster_4: 12.527, file_cluster_0: 13.239, file_cluster_8: 13.406
- **Magnitude:** 1008.22 | **LOC:** 663 | **CtrlFlow:** 15.2% | **Authorship Centralization:** 25.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (39.2364%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `try_join_next_with_id` (Impact: 45.4 | O(2^N) | DB: 5)
  * `try_join_next` (Impact: 45.0 | O(2^N) | DB: 3)
  * `abort_all` (Impact: 36.1 | O(2^N) | DB: 2)
  * `test_with_sleep` (Impact: 30.2 | O(N^3) | DB: 3)
  * `join_set_coop` (Impact: 28.0 | O(N^4) | DB: 3)
    * *Intent:* // This ensures that `join_next` works correctly when the coop budget is // exhausted.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 235`, `args: 32`, `func_start: 29`
* *Risk/State:* `safety_bypasses: 14`, `high_risk_execution: 1`, `state_mutation: 127`, `duplicate_logic: 10`, `orphaned_logic: 9`
* *Architecture:* `concurrency: 513`, `import: 11`
* *Defense:* `safety: 60`, `doc: 11`, `test: 78`, `sync_locks: 2`, `immutability_locks: 14`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::panic, FutureExt, tokio::sync::oneshot, tokio::time::Duration, futures::future::pending, super::*, LocalSet, tokio::task::JoinSet
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tokio/tests/net_unix_pipe.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.755 IQR)
- **Top Global Matches:** file_cluster_4: 13.755, file_cluster_0: 14.187, file_cluster_13: 14.428
- **Magnitude:** 987.0 | **LOC:** 547 | **CtrlFlow:** 35.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (43.4974%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `try_read_write_vectored` (Impact: 97.6 | O(2^N) | DB: 5)
  * `try_read_write` (Impact: 97.3 | O(2^N) | DB: 4)
  * `try_read_buf` (Impact: 97.3 | O(2^N) | DB: 7)
  * `from_file` (Impact: 43.4 | O(2^N) | DB: 11)
  * `fifo_resilient_reader` (Impact: 37.9 | O(2^N) | DB: 5)
    * *Intent:* /// Checks behavior of a resilient reader (Receiver in O_RDWR access mode) /// with writers sequenti...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 107`, `structural_boundaries: 194`, `args: 22`, `func_start: 22`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 153`, `orphaned_logic: 11`
* *Architecture:* `io: 18`, `concurrency: 236`, `import: 11`
* *Defense:* `safety: 62`, `doc: 5`, `test: 52`, `immutability_locks: 11`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` tokio::process::Command, assert_ok, std::os::unix::fs::OpenOptionsExt, AsyncWriteExt, std::io, std::path::Path, nix::fcntl::OFlag, assert_ready_ok...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tokio/tests/uds_datagram.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.44 IQR)
- **Top Global Matches:** file_cluster_4: 13.44, file_cluster_0: 13.919, file_cluster_8: 14.264
- **Magnitude:** 953.42 | **LOC:** 426 | **CtrlFlow:** 39.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (49.9752%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `try_recv_buf_from` (Impact: 189.4 | O(2^N) | DB: 5)
  * `try_send_to_recv_from` (Impact: 95.9 | O(N^5) | DB: 5)
  * `poll_ready` (Impact: 95.9 | O(N^5) | DB: 2)
  * `try_recv_buf_never_block` (Impact: 64.7 | O(N^5) | DB: 5)
    * *Intent:* // Even though we use sync non-blocking io we still need a reactor.
  * `try_send_recv_never_block` (Impact: 64.6 | O(N^5) | DB: 4)
    * *Intent:* // Even though we use sync non-blocking io we still need a reactor.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 107`, `structural_boundaries: 166`, `args: 19`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 105`, `orphaned_logic: 8`
* *Architecture:* `io: 9`, `concurrency: 187`, `import: 6`
* *Defense:* `safety: 73`, `test: 40`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::io, tokio::try_join, std::sync::Arc, std::future::poll_fn, tokio::net::UnixDatagram, tokio::io::ReadBuf
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tokio/tests/rt_threaded.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.803 IQR)
- **Top Global Matches:** file_cluster_4: 11.803, file_cluster_0: 12.213, file_cluster_8: 12.368
- **Magnitude:** 929.28 | **LOC:** 954 | **CtrlFlow:** 21.9% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (44.3083%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `blocking` (Impact: 95.8 | O(2^N) | DB: 1)
  * `many_multishot_futures` (Impact: 63.8 | O(N^6) | DB: 5)
  * `test_tuning` (Impact: 47.2 | O(N^4) | DB: 8)
    * *Intent:* // Testing the tuning logic is tricky as it is inherently timing based, and more // of a heuristic t...
  * `drop_threadpool_drops_futures` (Impact: 33.1 | O(N^4) | DB: 7)
  * `coop_and_block_in_place` (Impact: 32.7 | O(N^6) | DB: 2)
    * *Intent:* // When `block_in_place` returns, it attempts to reclaim the yielded runtime // worker. In this case...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 225`, `args: 55`, `func_start: 37`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 56`, `state_mutation: 102`, `orphaned_logic: 26`
* *Architecture:* `io: 1`, `concurrency: 332`, `import: 15`
* *Defense:* `safety: 36`, `doc: 7`, `test: 41`, `sync_locks: 26`, `immutability_locks: 6`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::pin::Pin, RecvTimeoutError, TcpStream, std::time::Duration, tokio::io::AsyncReadExt, std::sync::mpsc, Future, tokio::sync::oneshot...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tokio/src/sync/broadcast.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 22.599 IQR)
- **Top Global Matches:** file_cluster_0: 22.599, file_cluster_11: 22.659, file_cluster_6: 22.709
- **Magnitude:** 879.26 | **LOC:** 1760 | **CtrlFlow:** 30.4% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 27
- **Risk Profile:** Cognitive Load (29.3778%), Tech Debt (41.0174%)
**Top Internal Functions/Classes:**
  * `new` (Impact: 702.2 | O(2^N) | DB: 27)
  * `fmt` (Impact: 17.7 | O(2^N) | DB: 1)
    * *Intent:* //! assert_eq!(rx2.recv().await.unwrap(), 10); //! assert_eq!(rx2.recv().await.unwrap(), 20); //! })...
  * `fmt` (Impact: 17.6 | O(2^N) | DB: 1)
    * *Intent:* //! When **all** [`Sender`] handles have been dropped, no new values may be //! sent. At this point,...
  * `new` (Impact: 7.3 | O(2^N) | DB: 1)
    * *Intent:* /// [`WeakSender::upgrade`], which returns `Option<Sender>`. It returns `None` /// if all `Sender`s ...
  * `addr_of_pointers` (Impact: 4.2 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 128`, `args: 43`, `func_start: 39`, `class_start: 9`
* *Risk/State:* `state_mutation: 87`, `dead_code: 66`, `duplicate_logic: 4`
* *Architecture:* `api: 17`, `concurrency: 13`, `import: 3`
* *Defense:* `safety: 51`, `doc: 859`, `test: 12`, `sync_locks: 29`, `immutability_locks: 1`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` tokio::sync::broadcast, std::task::ready, std::pin::Pin, std::future::Future, crate::loom::sync::Arc, Acquire, crate::util::linked_list::self, futures::FutureExt...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tokio/src/net/tcp/stream.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_4` (Drift: 24.153 IQR)
- **Top Global Matches:** file_cluster_4: 24.153, file_cluster_0: 24.218, file_cluster_11: 24.255
- **Magnitude:** 836.74 | **LOC:** 1584 | **CtrlFlow:** 37.2% | **Authorship Centralization:** 28.6%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 68
- **Risk Profile:** Cognitive Load (42.0222%), Tech Debt (25.6302%)
**Top Internal Functions/Classes:**
  * `connect_mio` (Impact: 504.6 | O(N^5) | DB: 68)
    * *Intent:* /// use std::error::Error; /// /// #[tokio::main] /// async fn main() -> Result<(), Box<dyn Error>> ...
  * `connect` (Impact: 34.5 | O(N^5) | DB: 1)
    * *Intent:* /// Opens a TCP connection to a remote host. /// /// `addr` is an address of the remote host. Anythi...
  * `connect_addr` (Impact: 8.2 | O(N^3))
    * *Intent:* /// # Examples /// /// ```no_run /// use tokio::net::TcpStream; /// use tokio::io::AsyncWriteExt; //...
  * `as_raw_fd` (Impact: 7.1 | O(2^N))
  * `as_raw_socket` (Impact: 7.1 | O(2^N))
    * *Intent:* /// Tries to write several buffers to the stream, returning how many bytes /// were written. /// ///...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 94`, `structural_boundaries: 159`, `args: 48`, `func_start: 42`, `class_start: 1`
* *Risk/State:* `state_mutation: 74`, `dead_code: 137`, `duplicate_logic: 4`
* *Architecture:* `io: 20`, `api: 33`, `concurrency: 104`, `import: 36`
* *Defense:* `safety: 101`, `doc: 1085`, `test: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` RawSocket, std::task::ready, tokio::net::TcpStream, std::os::fd::FromRawFd, crate::util::check_socket_for_blocking, std::pin::Pin, AsyncWrite, std::os::unix::prelude::*...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tokio/tests/uds_stream.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.945 IQR)
- **Top Global Matches:** file_cluster_4: 12.945, file_cluster_0: 13.61, file_cluster_17: 13.705
- **Magnitude:** 820.6 | **LOC:** 447 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (50.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `try_read_buf` (Impact: 211.9 | O(2^N) | DB: 10)
  * `try_read_write` (Impact: 157.9 | O(N^4) | DB: 16)
  * `shutdown` (Impact: 27.1 | O(2^N) | DB: 8)
  * `read_until_pending` (Impact: 23.0 | O(N^4) | DB: 3)
  * `write_until_pending` (Impact: 23.0 | O(N^4) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 163`, `args: 16`, `func_start: 11`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 109`, `orphaned_logic: 4`
* *Architecture:* `io: 6`, `concurrency: 223`, `import: 9`
* *Defense:* `safety: 40`, `test: 20`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` tokio_test::assert_ok, std::io, try_join, UnixStream, tokio::net::UnixListener, assert_pending, assert_ready_ok, tokio::io::AsyncReadExt...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tokio/src/fs/file/tests.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.13 IQR)
- **Top Global Matches:** file_cluster_4: 12.13, file_cluster_8: 12.693, file_cluster_0: 12.739
- **Magnitude:** 810.2 | **LOC:** 979 | **CtrlFlow:** 2.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (99.9912%), Tech Debt (95.6405%)
**Top Internal Functions/Classes:**
  * `write_with_buffer_larger_than_max` (Impact: 17.3 | O(N^3) | DB: 14)
  * `read_with_buffer_larger_than_max` (Impact: 13.9 | O(N^3) | DB: 15)
  * `sync_all_err_ordered_after_write` (Impact: 6.8 | O(N^2) | DB: 9)
  * `sync_data_err_ordered_after_write` (Impact: 6.8 | O(N^2) | DB: 9)
  * `sync_all_ordered_after_write` (Impact: 6.7 | O(N^2) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 421`, `args: 86`, `func_start: 28`
* *Risk/State:* `state_mutation: 269`, `planned_debt: 1`, `orphaned_logic: 28`
* *Architecture:* `io: 28`, `concurrency: 372`, `import: 4`
* *Defense:* `safety: 56`, `test: 87`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::
    fs::mocks::*, Sequence, tokio_test::assert_pending, mockall::predicate::eq, assert_ready_ok, AsyncSeekExt, task, super::*...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tokio/tests/rt_common.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.23 IQR)
- **Top Global Matches:** file_cluster_4: 11.23, file_cluster_0: 11.489, file_cluster_13: 11.778
- **Magnitude:** 798.1 | **LOC:** 1439 | **CtrlFlow:** 12.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (39.0637%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ping_pong_saturation` (Impact: 39.4 | O(N^5) | DB: 6)
    * *Intent:* // Setting flag to true ensures that the tasks we spawned at // the beginning of the test will exit.
  * `wake_from_thread_local` (Impact: 37.5 | O(N^6) | DB: 2)
  * `spawn_many_from_task` (Impact: 32.9 | O(N^6) | DB: 3)
  * `spawn_many_from_block_on` (Impact: 28.5 | O(N^5) | DB: 3)
  * `shutdown_concurrent_spawn` (Impact: 23.4 | O(N^4) | DB: 1)
    * *Intent:* #[cfg(not(target_os="wasi"))] // Wasi does not support threads
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 313`, `args: 70`, `func_start: 46`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 41`, `high_risk_execution: 2`, `state_mutation: 65`, `dead_code: 3`, `duplicate_logic: 2`, `orphaned_logic: 35`
* *Architecture:* `io: 1`, `concurrency: 322`, `import: 24`
* *Defense:* `safety: 25`, `doc: 14`, `test: 65`, `sync_locks: 8`, `immutability_locks: 8`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` tokio::sync::mpsc, tokio_test::assert_ok, tokio::sync::Barrier, std::pin::Pin, TcpStream, std::time::Duration, tokio::io::AsyncReadExt, time...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tokio/src/sync/oneshot.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_0` (Drift: 20.496 IQR)
- **Top Global Matches:** file_cluster_0: 20.496, file_cluster_4: 20.523, file_cluster_11: 20.572
- **Magnitude:** 796.46 | **LOC:** 1608 | **CtrlFlow:** 36.5% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (30.7904%), Tech Debt (78.2707%)
**Top Internal Functions/Classes:**
  * `poll_recv` (Impact: 112.5 | O(N^6) | DB: 2)
    * *Intent:* /// /// // A receiver is not terminated it is polled and is still pending. /// let poll = futures::p...
  * `try_recv` (Impact: 71.8 | O(N^6) | DB: 1)
  * `poll_closed` (Impact: 44.0 | O(N^5) | DB: 3)
  * `drop` (Impact: 41.0 | O(2^N) | DB: 1)
    * *Intent:* /// # #[tokio::main(flavor = "current_thread")] /// # async fn main() { /// let (tx, mut rx) = onesh...
  * `close` (Impact: 31.5 | O(N^4))
    * *Intent:* /// /// # #[tokio::main(flavor = "current_thread")] /// # async fn main() { /// let (tx, mut rx) = o...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 101`, `structural_boundaries: 176`, `args: 32`, `func_start: 27`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 80`, `dead_code: 89`, `planned_debt: 2`, `duplicate_logic: 8`
* *Architecture:* `api: 16`, `concurrency: 139`, `import: 30`
* *Defense:* `safety: 74`, `doc: 853`, `test: 22`, `sync_locks: 3`, `immutability_locks: 2`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 5.865
  * `Choke Point (Betweenness):` 1.3e-05 | `Ripple Effect (Closeness):` 0.006605
  * `Imports (Out-Degree: 1):` std::task::ready, std::mem::MaybeUninit, AcqRel, std::pin::Pin, crate::util::trace, tokio::time::interval, std::task::Poll::Pending, std::future::Future...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `benches/sync_mpsc.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.338 IQR)
- **Top Global Matches:** file_cluster_4: 12.338, file_cluster_8: 12.954, file_cluster_11: 13.172
- **Magnitude:** 781.92 | **LOC:** 332 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (99.9987%), Tech Debt (33.4388%)
**Top Internal Functions/Classes:**
  * `contention_bounded_recv_many` (Impact: 40.4 | O(N^6) | DB: 5)
  * `contention_bounded_full_recv_many` (Impact: 40.4 | O(N^6) | DB: 5)
  * `contention_unbounded_recv_many` (Impact: 40.4 | O(N^6) | DB: 5)
  * `contention_bounded` (Impact: 40.3 | O(N^6) | DB: 2)
  * `contention_bounded_full` (Impact: 40.3 | O(N^6) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 148`, `args: 43`, `func_start: 19`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 137`, `duplicate_logic: 2`
* *Architecture:* `concurrency: 245`, `import: 3`
* *Defense:* `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` tokio::sync::mpsc, criterion_group, criterion::measurement::WallTime, BenchmarkGroup, criterion::black_box, criterion_main, Criterion
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tokio/src/runtime/scheduler/current_thread/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.722 IQR)
- **Top Global Matches:** file_cluster_13: 13.722, file_cluster_16: 13.784, file_cluster_0: 13.903
- **Magnitude:** 754.24 | **LOC:** 887 | **CtrlFlow:** 30.2% | **Authorship Centralization:** 37.5%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (24.1686%), Tech Debt (98.3501%)
**Top Internal Functions/Classes:**
  * `block_on` (Impact: 100.0 | O(2^N))
  * `unhandled_panic` (Impact: 86.3 | O(2^N) | DB: 2)
  * `block_on` (Impact: 44.4 | O(N^5) | DB: 3)
    * *Intent:* /// Wake by reference
  * `schedule` (Impact: 42.7 | O(2^N) | DB: 2)
  * `dump` (Impact: 34.4 | O(2^N) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 148`, `args: 65`, `func_start: 43`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 86`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 6`, `orphaned_logic: 9`
* *Architecture:* `api: 27`, `concurrency: 22`, `import: 25`
* *Defense:* `safety: 112`, `doc: 61`, `test: 2`, `sync_locks: 3`, `immutability_locks: 5`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` TaskHarnessScheduleHooks, Config, SpawnLocation, scheduler::Context::CurrentThread, RngSeedGenerator, std::time::Duration, std::task::Poll::Pending, Inject...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tokio-test/src/io.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_11` (Drift: 15.02 IQR)
- **Top Global Matches:** file_cluster_11: 15.02, file_cluster_16: 15.039, file_cluster_0: 15.074
- **Magnitude:** 744.44 | **LOC:** 578 | **CtrlFlow:** 32.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (46.2587%), Tech Debt (94.9867%)
**Top Internal Functions/Classes:**
  * `poll_write` (Impact: 238.9 | O(2^N) | DB: 4)
  * `action` (Impact: 114.2 | O(N^6) | DB: 7)
  * `poll_read` (Impact: 88.3 | O(N^6) | DB: 5)
  * `write` (Impact: 50.7 | O(N^6) | DB: 7)
  * `fmt` (Impact: 26.6 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 119`, `args: 33`, `func_start: 21`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 122`, `dead_code: 1`, `planned_debt: 3`, `duplicate_logic: 4`
* *Architecture:* `api: 15`, `concurrency: 1`
* *Defense:* `safety: 88`, `doc: 65`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` tokio::sync::mpsc, tokio::io::AsyncRead, std::pin::Pin, AsyncWrite, Sleep, std::future::Future, std::sync::Arc, futures_core::Stream...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tokio-util/tests/time_delay_queue.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_4` (Drift: 10.433 IQR)
- **Top Global Matches:** file_cluster_4: 10.433, file_cluster_8: 11.089, file_cluster_0: 11.148
- **Magnitude:** 740.84 | **LOC:** 900 | **CtrlFlow:** 8.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (42.1328%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `multi_delay_at_start` (Impact: 36.7 | O(N^4) | DB: 1)
  * `compact_change_deadline` (Impact: 12.9 | O(N^2) | DB: 3)
  * `remove_at_timer_wheel_threshold` (Impact: 11.7 | O(N^3) | DB: 1)
    * *Intent:* /// Regression test: it should be possible to remove entries which fall in the /// 0th slot of the i...
  * `item_expiry_greater_than_wheel` (Impact: 8.5 | O(N^2) | DB: 1)
  * `compact_remove_remapped_keys` (Impact: 7.2 | O(N^2) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 242`, `args: 38`, `func_start: 34`
* *Risk/State:* `state_mutation: 56`, `dead_code: 2`, `fragile_debt: 2`, `orphaned_logic: 31`
* *Architecture:* `concurrency: 493`, `import: 4`
* *Defense:* `safety: 10`, `doc: 9`, `test: 117`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` futures::StreamExt, sleep, tokio_test::assert_pending, Duration, tokio::time::self, sleep_until, assert_ready, tokio_util::time::DelayQueue...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tokio-macros/src/entry.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.913 IQR)
- **Top Global Matches:** file_cluster_8: 12.913, file_cluster_4: 13.171, file_cluster_0: 13.179
- **Magnitude:** 731.22 | **LOC:** 782 | **CtrlFlow:** 41.5% | **Authorship Centralization:** 16.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (22.2502%), Tech Debt (26.8407%)
**Top Internal Functions/Classes:**
  * `parse_knobs` (Impact: 159.5 | O(N^5) | DB: 14)
  * `build_config` (Impact: 150.7 | O(N^6) | DB: 1)
  * `contains_impl_trait` (Impact: 99.4 | O(2^N))
  * `build` (Impact: 39.4 | O(N^5))
  * `set_worker_threads` (Impact: 23.3 | O(N^4) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 110`, `args: 39`, `func_start: 22`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 51`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 2`, `concurrency: 26`, `import: 7`
* *Defense:* `safety: 137`, `doc: 5`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` quote::quote, TokenTree, ToTokens, Path, ParseStream, TokenStream, Parser, proc_macro2::Span...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tokio/tests/macros_select.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 10.74 IQR)
- **Top Global Matches:** file_cluster_4: 10.74, file_cluster_8: 11.238, file_cluster_0: 11.28
- **Magnitude:** 724.92 | **LOC:** 761 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (49.9916%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `biased_eventually_ready` (Impact: 32.1 | O(N^4) | DB: 4)
  * `join_with_select` (Impact: 23.4 | O(N^4) | DB: 7)
  * `select_streams` (Impact: 15.0 | O(N^4) | DB: 4)
  * `select_is_budget_aware` (Impact: 14.1 | O(N^4) | DB: 2)
  * `deterministic_select_multi_thread` (Impact: 12.5 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 162`, `args: 49`, `func_start: 42`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 18`, `high_risk_execution: 4`, `state_mutation: 67`, `duplicate_logic: 2`, `orphaned_logic: 33`
* *Architecture:* `api: 1`, `concurrency: 373`, `import: 18`
* *Defense:* `safety: 15`, `test: 55`, `immutability_locks: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` tokio::sync::mpsc, wasm_bindgen_test::wasm_bindgen_test, tokio_test::assert_ok, tokio::sync::oneshot, tokio::task::yield_now, Duration, tokio::time::self, std::task::Poll::Ready...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tokio/src/net/udp.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_4` (Drift: 24.168 IQR)
- **Top Global Matches:** file_cluster_4: 24.168, file_cluster_0: 24.191, file_cluster_11: 24.282
- **Magnitude:** 721.08 | **LOC:** 2342 | **CtrlFlow:** 39.8% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (31.9397%), Tech Debt (24.1855%)
**Top Internal Functions/Classes:**
  * `connect` (Impact: 44.2 | O(2^N) | DB: 1)
    * *Intent:* /// # Example: one to many (bind) /// /// Using `bind` we can create a simple echo server that sends...
  * `peek_sender_inner` (Impact: 43.2 | O(N^3) | DB: 7)
    * *Intent:* /// Ok((n, _addr)) => { /// println!("GOT {:?}", &buf[..n]); /// break; /// } /// Err(ref e) if e.ki...
  * `async_io` (Impact: 18.4 | O(2^N) | DB: 2)
    * *Intent:* /// match socket.try_recv(&mut buf) { /// Ok(n) => { /// println!("GOT {:?}", &buf[..n]); /// break;...
  * `try_io` (Impact: 18.3 | O(2^N))
    * *Intent:* /// Tries to receive a single datagram message on the socket from the remote /// address to which it...
  * `poll_recv_from` (Impact: 17.9 | O(N^4) | DB: 5)
    * *Intent:* /// Polls for read/receive readiness. /// /// If the udp stream is not currently ready for receiving...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 105`, `structural_boundaries: 159`, `args: 83`, `func_start: 52`
* *Risk/State:* `state_mutation: 126`, `dead_code: 173`, `orphaned_logic: 12`
* *Architecture:* `io: 16`, `api: 44`, `concurrency: 144`, `import: 26`
* *Defense:* `safety: 108`, `doc: 1604`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` RawSocket, std::task::ready, std::os::fd::FromRawFd, crate::util::check_socket_for_blocking, RawFd, BorrowedSocket, super::UdpSocket, ReadBuf...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tokio/src/sync/notify.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 19.142 IQR)
- **Top Global Matches:** file_cluster_0: 19.142, file_cluster_13: 19.236, file_cluster_11: 19.245
- **Magnitude:** 708.16 | **LOC:** 1418 | **CtrlFlow:** 32.1% | **Authorship Centralization:** 40.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (23.4618%), Tech Debt (94.3325%)
**Top Internal Functions/Classes:**
  * `poll_notified` (Impact: 211.3 | O(N^6) | DB: 10)
  * `inner_notify_waiters` (Impact: 86.9 | O(N^6) | DB: 5)
    * *Intent:* /// Pending notification.
  * `drop_notified` (Impact: 49.0 | O(N^5) | DB: 3)
  * `notify_locked` (Impact: 46.8 | O(N^5) | DB: 2)
    * *Intent:* /// yet been polled. /// /// [`notify_one()`]: Notify::notify_one /// [`Notified::enable()`]: Notifi...
  * `notify_with_strategy` (Impact: 22.4 | O(N^5) | DB: 3)
    * *Intent:* /// Future returned from [`Notify::notified_owned()`].
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 171`, `args: 36`, `func_start: 37`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 92`, `dead_code: 60`, `duplicate_logic: 16`
* *Architecture:* `api: 21`, `concurrency: 29`, `import: 18`
* *Defense:* `safety: 66`, `doc: 528`, `test: 3`, `sync_locks: 42`, `immutability_locks: 7`, `cleanup: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::panic::RefUnwindSafe, std::pin::Pin, crate::loom::sync::Mutex, std::future::Future, std::sync::Arc, Acquire, crate::util::linked_list::self, Waker...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tokio/tests/tcp_stream.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.549 IQR)
- **Top Global Matches:** file_cluster_4: 12.549, file_cluster_0: 13.178, file_cluster_17: 13.374
- **Magnitude:** 691.62 | **LOC:** 444 | **CtrlFlow:** 25.6% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (50.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `try_read_buf` (Impact: 151.5 | O(2^N) | DB: 8)
  * `try_read_write` (Impact: 96.7 | O(N^3) | DB: 13)
  * `read_until_pending` (Impact: 23.1 | O(N^4) | DB: 4)
  * `write_until_pending` (Impact: 23.1 | O(N^4) | DB: 2)
  * `buffer_not_included_in_future` (Impact: 18.5 | O(N^4) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 151`, `args: 15`, `func_start: 11`
* *Risk/State:* `safety_bypasses: 31`, `state_mutation: 102`, `orphaned_logic: 4`
* *Architecture:* `io: 2`, `concurrency: 246`, `import: 10`
* *Defense:* `safety: 32`, `test: 21`, `immutability_locks: 3`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` tokio_test::assert_ok, std::io, tokio::try_join, tokio::net::TcpListener, TcpStream, tokio_test::task, assert_pending, tokio::io::AsyncReadExt...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tokio-util/tests/task_join_map.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.068 IQR)
- **Top Global Matches:** file_cluster_4: 12.068, file_cluster_0: 12.768, file_cluster_13: 12.859
- **Magnitude:** 687.1 | **LOC:** 672 | **CtrlFlow:** 11.3% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (35.7143%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_with_sleep` (Impact: 30.3 | O(N^3) | DB: 3)
  * `abort_by_key` (Impact: 27.8 | O(N^4) | DB: 3)
  * `abort_by_predicate` (Impact: 19.0 | O(N^4) | DB: 3)
  * `spawn_pending_tasks` (Impact: 16.9 | O(N^3) | DB: 2)
    * *Intent:* // Spawn `N` “pending” tasks that own a `oneshot::Sender`. // When the task is aborted the sender is...
  * `spawn_index_tasks` (Impact: 13.9 | O(N^3) | DB: 1)
    * *Intent:* // Spawn `N` tasks that return their index (`i`).
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 197`, `args: 27`, `func_start: 25`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 92`, `duplicate_logic: 10`, `orphaned_logic: 10`
* *Architecture:* `concurrency: 386`, `import: 13`
* *Defense:* `safety: 36`, `doc: 12`, `test: 79`, `sync_locks: 2`, `immutability_locks: 12`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` FutureExt, tokio::sync::oneshot, tokio::time::Duration, futures::future::pending, std::collections::HashSet, std::panic::AssertUnwindSafe, tokio_util::task::JoinMap, super::*...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tokio/src/runtime/scheduler/multi_thread/worker.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.317 IQR)
- **Top Global Matches:** file_cluster_13: 14.317, file_cluster_0: 14.374, file_cluster_16: 14.433
- **Magnitude:** 685.66 | **LOC:** 1511 | **CtrlFlow:** 32.1% | **Authorship Centralization:** 16.7%
- **Algorithmic:** O(N^6) | **DB Complexity:** 47
- **Risk Profile:** Cognitive Load (20.5545%), Tech Debt (10.3684%)
**Top Internal Functions/Classes:**
  * `block_in_place` (Impact: 488.8 | O(N^6) | DB: 47)
  * `create` (Impact: 28.2 | O(N^4) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 76`, `structural_boundaries: 161`, `args: 47`, `func_start: 34`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 125`, `orphaned_logic: 2`
* *Architecture:* `api: 20`, `concurrency: 12`, `import: 18`
* *Defense:* `safety: 103`, `doc: 172`, `test: 5`, `sync_locks: 16`, `immutability_locks: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` crate::runtime::time_alt, Config, crate::runtime::scheduler::util, Stats, TimerFlavor, RngSeedGenerator, std::time::Duration, Parker...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tokio/tests/io_buf_writer.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.232 IQR)
- **Top Global Matches:** file_cluster_4: 12.232, file_cluster_0: 12.895, file_cluster_8: 12.92
- **Magnitude:** 683.44 | **LOC:** 538 | **CtrlFlow:** 6.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 20
- **Risk Profile:** Cognitive Load (49.9999%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `maybe_pending_buf_writer_seek` (Impact: 38.6 | O(N^4) | DB: 20)
  * `poll_write` (Impact: 27.5 | O(2^N) | DB: 4)
  * `poll_write_vectored` (Impact: 23.2 | O(N^4) | DB: 3)
  * `write_all` (Impact: 9.5 | O(N^3) | DB: 4)
  * `new` (Impact: 8.3 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 234`, `args: 40`, `func_start: 39`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 36`, `state_mutation: 130`, `duplicate_logic: 9`, `orphaned_logic: 17`
* *Architecture:* `io: 2`, `api: 1`, `concurrency: 330`, `import: 9`
* *Defense:* `safety: 23`, `test: 114`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.216
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` support::io_vec::IoBufs, BufWriter, tokio_test::assert_ok, std::cmp, std::pin::Pin, AsyncWrite, futures::future, AsyncSeekExt...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `tokio/src/macros/join.rs` (RUST) | Magnitude: 59.32 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: doc: 108, indent_spaces: 65, structural_boundaries: 40, state_mutation: 25
- `tokio/src/runtime/task_hooks.rs` (RUST) | Magnitude: 47.74 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 50, api: 16, generics: 16, encapsulation: 16
- `tokio/tests/io_driver.rs` (RUST) | Magnitude: 33.8 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 38, structural_boundaries: 31, safety_bypasses: 9, import: 9
- `tokio/src/runtime/metrics/batch.rs` (RUST) | Magnitude: 205.42 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 224, structural_boundaries: 39, state_mutation: 34, args: 27
- `tokio/src/runtime/time_alt/tests.rs` (RUST) | Magnitude: 190.02 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 113, state_mutation: 48, structural_boundaries: 47, branch: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `tokio/src/sync/mpsc/mod.rs` (RUST) | Magnitude: 20.38 | Delta: **0.25 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 117, structural_boundaries: 8, api: 5, encapsulation: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `tokio-util/src/io/stream_reader.rs` (RUST) | Magnitude: 182.04 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: doc: 175, indent_spaces: 111, structural_boundaries: 58, state_mutation: 45
- `tokio-test/src/io.rs` (RUST) | Magnitude: 744.44 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 299, state_mutation: 122, structural_boundaries: 119, safety: 88
- `tokio/src/fs/file.rs` (RUST) | Magnitude: 635.4 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: doc: 390, indent_spaces: 340, structural_boundaries: 157, state_mutation: 97
- `tokio/src/task/local.rs` (RUST) | Magnitude: 365.08 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: doc: 530, indent_spaces: 458, structural_boundaries: 122, generics: 74

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `tokio/src/runtime/tests/loom_local.rs` (RUST) | Magnitude: 34.0 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 16, doc: 8, concurrency: 8
- `tokio/src/io/util/read_int.rs` (RUST) | Magnitude: 123.06 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 98, structural_boundaries: 48, state_mutation: 36, concurrency: 17
- `tokio/src/loom/std/atomic_usize.rs` (RUST) | Magnitude: 82.78 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: state_mutation: 43, structural_boundaries: 22, indent_spaces: 21, concurrency: 12
- `tokio/src/runtime/scheduler/inject/rt_multi_thread.rs` (RUST) | Magnitude: 66.64 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 62, structural_boundaries: 32, state_mutation: 21, generics: 16
- `tokio/src/fs/symlink.rs` (RUST) | Magnitude: 10.36 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 9, doc: 5, generics: 4, import: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `tokio-test/src/stream_mock.rs` (RUST) | Magnitude: 96.04 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 70, doc: 41, structural_boundaries: 28, generics: 21
- `tokio/src/fs/symlink_dir.rs` (RUST) | Magnitude: 10.36 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 9, doc: 8, generics: 4, import: 3
- `tokio/src/fs/symlink_file.rs` (RUST) | Magnitude: 10.36 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 9, doc: 8, generics: 4, import: 3
- `tokio/src/signal/registry.rs` (RUST) | Magnitude: 159.4 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 156, structural_boundaries: 54, concurrency: 26, generics: 26
- `tokio/tests/support/mpsc_stream.rs` (RUST) | Magnitude: 34.06 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: structural_boundaries: 20, generics: 20, concurrency: 17, indent_spaces: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `tokio-util/src/io/read_arc.rs` (RUST) | Magnitude: 35.1 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: doc: 19, structural_boundaries: 12, state_mutation: 12, safety: 9
- `tokio/src/time/timeout.rs` (RUST) | Magnitude: 25.56 | Delta: **0.096 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 121, indent_spaces: 23, structural_boundaries: 14, dead_code: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `tokio/src/io/util/read_to_end.rs` (RUST) | Magnitude: 166.06 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 98, structural_boundaries: 51, state_mutation: 48, branch: 20
- `benches/remote_spawn.rs` (RUST) | Magnitude: 80.34 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 58, structural_boundaries: 23, doc: 15, state_mutation: 12
- `tokio/src/io/util/fill_buf.rs` (RUST) | Magnitude: 61.44 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 37, structural_boundaries: 21, concurrency: 13, state_mutation: 11
- `tokio-stream/src/stream_map.rs` (RUST) | Magnitude: 519.42 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: doc: 452, indent_spaces: 278, structural_boundaries: 92, state_mutation: 64
- `tokio/src/net/tcp/listener.rs` (RUST) | Magnitude: 85.02 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 260, indent_spaces: 51, dead_code: 30, structural_boundaries: 24

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `tokio/src/net/unix/pipe.rs` (RUST) | Magnitude: 281.66 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: doc: 1021, indent_spaces: 341, dead_code: 111, structural_boundaries: 93
- `tokio/src/sync/set_once.rs` (RUST) | Magnitude: 15.68 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: doc: 159, structural_boundaries: 15, dead_code: 13, import: 11
- `tokio/src/io/async_fd.rs` (RUST) | Magnitude: 142.86 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: doc: 992, dead_code: 125, indent_spaces: 93, structural_boundaries: 38
- `tokio/src/task/spawn.rs` (RUST) | Magnitude: 16.12 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: doc: 165, indent_spaces: 35, dead_code: 19, structural_boundaries: 10
- `tokio/src/io/util/async_read_ext.rs` (RUST) | Magnitude: 60.46 | Delta: **0.06 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: doc: 1318, dead_code: 105, indent_spaces: 81, structural_boundaries: 54

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `tokio/tests/rt_poll_callbacks.rs` (RUST) | Magnitude: 31.94 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 101, structural_boundaries: 36, safety: 34, sync_locks: 26
- `tokio/src/net/unix/datagram/mod.rs` (RUST) | Magnitude: 11.52 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 1, api: 1, doc: 1, encapsulation: 1
- `tokio/src/net/windows/mod.rs` (RUST) | Magnitude: 11.52 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 1, api: 1, doc: 1, encapsulation: 1
- `tokio/src/util/metric_atomics.rs` (RUST) | Magnitude: 83.96 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 42, api: 14, encapsulation: 14, args: 12
- `tokio/src/runtime/metrics/mock.rs` (RUST) | Magnitude: 8.68 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: api: 4, encapsulation: 4, indent_spaces: 4, structural_boundaries: 3

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `tokio/src/runtime/handle.rs` -> Churn: **79.25%** | Cog Load: 22.2336% | Debt: 89.375%
- `tokio/src/runtime/scheduler/current_thread/mod.rs` -> Churn: **79.25%** | Cog Load: 24.1686% | Debt: 98.3501%
- `tokio/src/task/local.rs` -> Churn: **79.25%** | Cog Load: 25.7672% | Debt: 98.6683%
- `tokio/src/lib.rs` -> Churn: **70.94%** | Cog Load: 0.0% | Debt: 91.7325%
- `tokio/src/fs/open_options.rs` -> Churn: **70.18%** | Cog Load: 32.5472% | Debt: 99.994%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `tokio/tests/net_unix_pipe.rs` -> **n4n5** (100.0% isolated ownership) | Magnitude: 987.0
- `tokio-test/src/io.rs` -> **ADD-SP** (100.0% isolated ownership) | Magnitude: 744.44
- `tokio/tests/macros_select.rs` -> **Motoyuki Kimura** (100.0% isolated ownership) | Magnitude: 724.92
- `tokio/src/net/windows/named_pipe.rs` -> **Qi** (100.0% isolated ownership) | Magnitude: 627.28
- `tokio/tests/io_async_fd.rs` -> **Ralf Jung** (100.0% isolated ownership) | Magnitude: 578.4

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `tokio/src/sync/oneshot.rs` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 80.1153%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `tokio/src/io/ready.rs` -> **Severity: 0.931** (Embedded: 0.0242 * Error Risk: 38.5664%)
- `tokio/src/io/util/mem.rs` -> **Severity: 0.821** (Embedded: 0.0251 * Error Risk: 32.7203%)
- `tokio/src/runtime/metrics/scheduler.rs` -> **Severity: 0.241** (Embedded: 0.004 * Error Risk: 60.8027%)
- `tokio/src/io/util/copy_bidirectional.rs` -> **Severity: 0.2** (Embedded: 0.0026 * Error Risk: 75.877%)
- `tokio/src/process/kill.rs` -> **Severity: 0.191** (Embedded: 0.0026 * Error Risk: 72.1462%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `tokio/src/io/ready.rs` -> **Severity: 449.921** (Blast Radius: 31.91 * Doc Risk: 14.0997%)
- `tokio/src/runtime/metrics/scheduler.rs` -> **Severity: 379.9** (Blast Radius: 3.799 * Doc Risk: 100.0%)
- `tokio/src/io/util/mem.rs` -> **Severity: 242.34** (Blast Radius: 20.33 * Doc Risk: 11.9203%)
- `tokio-util/src/io/simplex.rs` -> **Severity: 193.561** (Blast Radius: 2.455 * Doc Risk: 78.8436%)
- `tokio/src/time/sleep.rs` -> **Severity: 143.639** (Blast Radius: 10.33 * Doc Risk: 13.905%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
