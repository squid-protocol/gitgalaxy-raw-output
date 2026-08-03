# ARCHITECTURAL_BRIEF: hyper
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_rust/hyper` |
| **Timestamp** | `2026-08-03T19:44:13.503402+00:00` |
| **Scan Duration** | `0.64s` |
| **Git Branch** | `master` |
| **Git Commit** | `0d6c7d5469baa09e2fb127ee3758a79b3271a4f0` |
| **Git Remote** | `https://github.com/hyperium/hyper.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 96 malicious artifacts.

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
| Total Artifacts | 130 |
| Analyzed Artifacts (Scanned) | 103 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 27 |
| Total LOC | 21345 |
| Volatility Index | 0.058 |
| % Scanned of codebase = | 79.2% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 0 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUST | 92 | 20773 | 89.3% |
| MARKDOWN | 6 | 0 | 5.8% |
| C | 2 | 506 | 1.9% |
| MAKEFILE | 1 | 15 | 1.0% |
| SHELL | 1 | 41 | 1.0% |
| HTML | 1 | 10 | 1.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `3.744`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_4 | 26 | 25.2% |
| file_cluster_13 | 25 | 24.3% |
| file_cluster_0 | 21 | 20.4% |
| file_cluster_8 | 9 | 8.7% |
| file_cluster_16 | 8 | 7.8% |
| file_cluster_7 | 3 | 2.9% |
| file_cluster_6 | 2 | 1.9% |
| file_cluster_11 | 2 | 1.9% |
| file_cluster_17 | 1 | 1.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 6 | 5.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 27*

**Composition by Extension & Reason:**
- `.md`: 14x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.toml)
- `.h`: 1x Excluded (Machine-Generated Source Code Signature: 545 LOC)
- `.svg`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 41.1 | 43.9 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.0 | 32.4 | 31.9 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 40.2 | 10.6 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 21.6 | 2.4 | 0.0 |
| API Exposure | 0.0 | 13.0 | 3.2 | 3.5 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 57.9 | 100.0 | 100.0 |
| State Flux Exposure | 0.0 | 100.0 | 47.4 | 39.6 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 7.5 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 90.7 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 5.1 | 0.6 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 11.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 34.2 | 11.9 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 56.7 | 92.9 | 100.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 20.0 | 9.4 | 0.7 | 20.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 2.2 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 10.0 | 0.2 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tests/server.rs` (Hits: 54)
- `tests/client.rs` (Hits: 40)
- `benches/support/tokiort.rs` (Hits: 26)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **http.rs** (`src/service/http.rs`) — 1 inbound connections
2. **CHANGELOG.md** (`CHANGELOG.md`) — 0 inbound connections
3. **CONTRIBUTING.md** (`CONTRIBUTING.md`) — 0 inbound connections
4. **README.md** (`README.md`) — 0 inbound connections
5. **SECURITY.md** (`SECURITY.md`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **client.rs** (`tests/client.rs`) — 70 outbound dependencies
2. **server.rs** (`tests/server.rs`) — 66 outbound dependencies
3. **conn.rs** (`src/proto/h1/conn.rs`) — 57 outbound dependencies
4. **client.rs** (`src/proto/h2/client.rs`) — 47 outbound dependencies
5. **role.rs** (`src/proto/h1/role.rs`) — 39 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `poll_catch` (@ `src/proto/h1/dispatch.rs`) -> Impact: **1927.1** | LOC: 663
- `new` (@ `src/proto/h1/conn.rs`) -> Impact: **1852.8** | LOC: 937
- `poll_flush` (@ `src/proto/h1/io.rs`) -> Impact: **610.8** | LOC: 577
- `parse` (@ `src/proto/h1/role.rs`) -> Impact: **496.2** | LOC: 225
- `get_should_ignore_body` (@ `tests/server.rs`) -> Impact: **406.1** | LOC: 1818
- `encode` (@ `src/proto/h1/role.rs`) -> Impact: **355.0** | LOC: 100
- `write_header_name` (@ `src/proto/h1/role.rs`) -> Impact: **326.9** | LOC: 238
- `poll` (@ `src/proto/h2/client.rs`) -> Impact: **321.1** | LOC: 118
- `poll` (@ `src/server/conn/http1.rs`) -> Impact: **248.8** | LOC: 196
  * *Intent:* /// Start a graceful shutdown process for this connection. /// /// This `Connection` should continue to be polled until shutdown /// can finish. ///
- `poll_server` (@ `src/proto/h2/server.rs`) -> Impact: **227.0** | LOC: 96

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `echo` (@ `examples/echo.rs`) -> **O(2^N) [Recursive]**
  * *Intent:* /// This is our service handler. It receives a Request, routes on its /// path, and returns a Future of a Response.
- `main` (@ `examples/gateway.rs`) -> **O(2^N) [Recursive]**
- `main` (@ `examples/graceful_shutdown.rs`) -> **O(2^N) [Recursive]**
- `poll` (@ `src/client/dispatch.rs`) -> **O(2^N) [Recursive]**
- `new` (@ `src/proto/h1/conn.rs`) -> **O(2^N) [Recursive]**
- `read_extension` (@ `src/proto/h1/decode.rs`) -> **O(2^N) [Recursive]**
- `poll_catch` (@ `src/proto/h1/dispatch.rs`) -> **O(2^N) [Recursive]**
- `poll_flush` (@ `src/proto/h1/io.rs`) -> **O(2^N) [Recursive]**
- `parse` (@ `src/proto/h1/io.rs`) -> **O(2^N) [Recursive]**
- `parse` (@ `src/proto/h1/role.rs`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `get_should_ignore_body` (@ `tests/server.rs`) -> DB Complexity: **210**
- `test_parse_request_errors` (@ `src/proto/h1/role.rs`) -> DB Complexity: **109**
- `new` (@ `src/proto/h1/conn.rs`) -> DB Complexity: **67**
- `poll_catch` (@ `src/proto/h1/dispatch.rs`) -> DB Complexity: **57**
- `main` (@ `capi/examples/client.c`) -> DB Complexity: **48**
  * *Intent:* #define STR_ARG(XX) (uint8_t *)XX, strlen(XX)
- `main` (@ `capi/examples/upload.c`) -> DB Complexity: **48**
  * *Intent:* #define STR_ARG(XX) (uint8_t *)XX, strlen(XX)
- `poll_flush` (@ `src/proto/h1/io.rs`) -> DB Complexity: **41**
- `bench` (@ `benches/end_to_end.rs`) -> DB Complexity: **32**
- `poll_read` (@ `src/ffi/io.rs`) -> DB Complexity: **32**
- `poll` (@ `src/server/conn/http1.rs`) -> DB Complexity: **30**
  * *Intent:* /// Start a graceful shutdown process for this connection. /// /// This `Connection` should continue to be polled until shutdown /// can finish. ///

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src/proto/h1` | 7 | 9658.08 | 36.86% | 48.55% |
| `tests` | 3 | 3190.98 | 28.03% | 0.0% |
| `examples` | 18 | 2494.18 | 60.59% | 0.0% |
| `src/proto/h2` | 5 | 2437.04 | 60.08% | 41.6% |
| `src/ffi` | 8 | 1333.46 | 33.02% | 62.16% |
| `src/client/conn` | 3 | 981.9 | 32.4% | 59.38% |
| `capi/examples` | 3 | 849.22 | 57.74% | 0.0% |
| `tests/support` | 3 | 803.28 | 34.38% | 0.0% |
| `benches` | 5 | 767.08 | 59.66% | 61.1% |
| `src` | 7 | 754.92 | 15.96% | 56.76% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `benches/support/tokiort.rs` -> **100.0%** Exposure
- `src/client/dispatch.rs` -> **100.0%** Exposure
- `src/client/tests.rs` -> **100.0%** Exposure
- `src/common/io/compat.rs` -> **100.0%** Exposure
- `src/ext/h1_reason_phrase.rs` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `src/common/buf.rs` -> **100.0%** Exposure
- `src/common/date.rs` -> **100.0%** Exposure
- `src/common/either.rs` -> **100.0%** Exposure
- `src/common/future.rs` -> **100.0%** Exposure
- `src/common/io/compat.rs` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/error.rs` -> **26** Orphaned Functions | **9** Duplicates
- `tests/server.rs` -> **18** Orphaned Functions | **11** Duplicates
- `src/client/dispatch.rs` -> **10** Orphaned Functions | **15** Duplicates
- `src/proto/h1/decode.rs` -> **17** Orphaned Functions | **5** Duplicates
- `benches/end_to_end.rs` -> **19** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`capi/examples/client.c`** -> AI Confidence: **99.31%**
2. **`examples/hello-http2.rs`** -> AI Confidence: **99.24%**
3. **`src/proto/h1/conn.rs`** -> AI Confidence: **99.24%**
4. **`capi/examples/upload.c`** -> AI Confidence: **99.24%**
5. **`examples/client.rs`** -> AI Confidence: **99.18%**
6. **`examples/client_json.rs`** -> AI Confidence: **99.18%**
7. **`examples/echo.rs`** -> AI Confidence: **99.18%**
8. **`examples/graceful_shutdown.rs`** -> AI Confidence: **99.18%**
9. **`examples/params.rs`** -> AI Confidence: **99.18%**
10. **`examples/service_struct_impl.rs`** -> AI Confidence: **99.18%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `benches/end_to_end.rs` -> **20.0%** Exposure
- `benches/pipeline.rs` -> **20.0%** Exposure
- `benches/server.rs` -> **20.0%** Exposure
- `benches/support/tokiort.rs` -> **20.0%** Exposure
- `examples/echo.rs` -> **20.0%** Exposure
### Weaponizable Injection Vectors
- `tests/support/mod.rs` -> **100.0%** Exposure
- `capi/gen_header.sh` -> **99.9998%** Exposure
- `benches/end_to_end.rs` -> **17.1012%** Exposure
- `tests/client.rs` -> **0.0003%** Exposure
### Raw Memory Manipulation
- `capi/examples/upload.c` -> **9.9984%** Exposure
- `capi/examples/client.c` -> **9.995%** Exposure
- `src/rt/io.rs` -> **0.0002%** Exposure
### Algorithmic DoS Exposure
- `benches/end_to_end.rs` -> **100.0%** Exposure
- `benches/support/tokiort.rs` -> **100.0%** Exposure
- `src/body/incoming.rs` -> **100.0%** Exposure
- `src/client/conn/http1.rs` -> **100.0%** Exposure
- `src/client/conn/http2.rs` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1303` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/client/dispatch.rs` (RUST) -> Cumulative Risk: **890.09**
- **Archetype:** `file_cluster_0` (Distance: 14.159 IQR)
- **Magnitude:** 576.84 | **LOC:** 528 | **CtrlFlow:** 17.7% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `poll` (Impact: 38.0), `giver_queue_throughput` (Impact: 34.7), `drop` (Impact: 28.9)

### 2. `src/proto/h2/client.rs` (RUST) -> Cumulative Risk: **884.58**
- **Archetype:** `file_cluster_4` (Distance: 13.302 IQR)
- **Magnitude:** 941.66 | **LOC:** 792 | **CtrlFlow:** 28.7% | **Authorship Centralization:** 25.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Churn (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `poll` (Impact: 321.1), `poll` (Impact: 75.4), `handshake` (Impact: 61.9)

### 3. `benches/server.rs` (RUST) -> Cumulative Risk: **867.77**
- **Archetype:** `file_cluster_4` (Distance: 11.885 IQR)
- **Magnitude:** 230.4 | **LOC:** 228 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), State Flux (99.9991%), Algorithmic Dos (99.9337%)
- **Heaviest Functions:** `raw_tcp_throughput_large_payload` (Impact: 41.4), `raw_tcp_throughput_small_payload` (Impact: 24.2), `throughput_fixedsize_many_chunks` (Impact: 9.4)

### 4. `benches/support/tokiort.rs` (RUST) -> Cumulative Risk: **819.35**
- **Archetype:** `file_cluster_0` (Distance: 12.703 IQR)
- **Magnitude:** 230.3 | **LOC:** 233 | **CtrlFlow:** 14.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `poll_read` (Impact: 23.7), `poll_read` (Impact: 23.3), `reset` (Impact: 16.2)

### 5. `src/common/io/rewind.rs` (RUST) -> Cumulative Risk: **812.99**
- **Archetype:** `file_cluster_4` (Distance: 12.833 IQR)
- **Magnitude:** 109.96 | **LOC:** 171 | **CtrlFlow:** 4.8% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `poll_read` (Impact: 21.5), `new_buffered` (Impact: 3.8), `into_inner` (Impact: 2.7)

### 6. `benches/end_to_end.rs` (RUST) -> Cumulative Risk: **810.97**
- **Archetype:** `file_cluster_4` (Distance: 11.592 IQR)
- **Magnitude:** 413.54 | **LOC:** 452 | **CtrlFlow:** 15.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Tech Debt (99.4252%)
- **Heaviest Functions:** `bench` (Impact: 121.1), `spawn_server` (Impact: 38.8), `http2_adaptive_window` (Impact: 6.3)

### 7. `src/client/conn/http2.rs` (RUST) -> Cumulative Risk: **799.2**
- **Archetype:** `file_cluster_16` (Distance: 13.691 IQR)
- **Magnitude:** 544.88 | **LOC:** 712 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 25.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Churn (100.0%), Algorithmic Dos (100.0%), Spec Match (96.2963%)
- **Heaviest Functions:** `handshake` (Impact: 28.3), `send_request` (Impact: 22.2), `poll` (Impact: 21.1)

### 8. `benches/pipeline.rs` (RUST) -> Cumulative Risk: **766.36**
- **Archetype:** `file_cluster_13` (Distance: 10.449 IQR)
- **Magnitude:** 77.06 | **LOC:** 96 | **CtrlFlow:** 10.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (99.9802%), State Flux (99.7675%)
- **Heaviest Functions:** `hello_world_16` (Impact: 50.5)

### 9. `src/proto/h2/server.rs` (RUST) -> Cumulative Risk: **755.68**
- **Archetype:** `file_cluster_4` (Distance: 12.713 IQR)
- **Magnitude:** 795.68 | **LOC:** 551 | **CtrlFlow:** 24.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `poll_server` (Impact: 227.0), `poll` (Impact: 110.8), `new` (Impact: 108.5)

### 10. `src/proto/h1/decode.rs` (RUST) -> Cumulative Risk: **748.21**
- **Archetype:** `file_cluster_4` (Distance: 13.587 IQR)
- **Magnitude:** 1209.68 | **LOC:** 1255 | **CtrlFlow:** 18.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `test_read_chunk_size` (Impact: 102.7), `read_extension` (Impact: 64.2), `read_body` (Impact: 50.7)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/proto/h1/role.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.222 IQR)
- **Top Global Matches:** file_cluster_0: 13.222, file_cluster_8: 13.364, file_cluster_13: 13.445
- **Magnitude:** 2641.56 | **LOC:** 3174 | **CtrlFlow:** 35.4% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 109
- **Risk Profile:** Cognitive Load (26.3899%), Tech Debt (19.592%)
**Top Internal Functions/Classes:**
  * `parse` (Impact: 496.2 | O(2^N) | DB: 21)
  * `encode` (Impact: 355.0 | O(2^N) | DB: 4)
  * `write_header_name` (Impact: 326.9 | O(N^6) | DB: 21)
  * `set_length` (Impact: 194.5 | O(N^6) | DB: 3)
  * `decoder` (Impact: 183.2 | O(2^N) | DB: 1)
    * *Intent:* // Safety: httparse ensures that only valid reason phrase bytes are present in this
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 290`, `structural_boundaries: 530`, `args: 82`, `func_start: 71`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 370`, `dead_code: 1`, `planned_debt: 6`, `duplicate_logic: 2`, `orphaned_logic: 7`
* *Architecture:* `api: 7`, `import: 39`
* *Defense:* `safety: 306`, `doc: 7`, `test: 63`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.629
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::error::Kind, http::header::self, Http1Transaction, crate::proto::BodyLength, Encoder, crate::proto::RequestHead, ParsedMessage, StatusCode...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/server.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.076 IQR)
- **Top Global Matches:** file_cluster_4: 12.076, file_cluster_0: 12.523, file_cluster_8: 12.53
- **Magnitude:** 2429.48 | **LOC:** 3601 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 210
- **Risk Profile:** Cognitive Load (49.4678%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `get_should_ignore_body` (Impact: 406.1 | O(N^6) | DB: 210)
  * `read_until` (Impact: 61.2 | O(2^N) | DB: 4)
  * `serve` (Impact: 40.3 | O(N^6) | DB: 2)
  * `call` (Impact: 37.8 | O(N^6) | DB: 1)
  * `build_reply` (Impact: 31.4 | O(N^5) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 104`, `structural_boundaries: 1038`, `args: 191`, `func_start: 131`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 358`, `state_mutation: 389`, `planned_debt: 1`, `duplicate_logic: 11`, `orphaned_logic: 18`
* *Architecture:* `io: 54`, `api: 2`, `concurrency: 1027`, `import: 41`
* *Defense:* `safety: 110`, `doc: 2`, `test: 199`, `sync_locks: 14`, `immutability_locks: 13`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.629
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Ordering, std::io::self, std::net::IpAddr, hyper::body::Frame, TcpListener, std::net::TcpListener, tokio::pin, Read...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/proto/h1/dispatch.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.922 IQR)
- **Top Global Matches:** file_cluster_4: 13.922, file_cluster_13: 13.955, file_cluster_0: 13.978
- **Magnitude:** 2188.1 | **LOC:** 809 | **CtrlFlow:** 38.2% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 57
- **Risk Profile:** Cognitive Load (78.31%), Tech Debt (12.516%)
**Top Internal Functions/Classes:**
  * `poll_catch` (Impact: 1927.1 | O(2^N) | DB: 57)
  * `disable_keep_alive` (Impact: 18.6 | O(2^N) | DB: 1)
  * `poll_without_shutdown` (Impact: 10.5 | O(N^4) | DB: 2)
    * *Intent:* /// Run this dispatcher until HTTP says this connection is done, /// but don't call `Write::shutdown...
  * `into_inner` (Impact: 5.4 | O(2^N))
  * `new` (Impact: 4.9 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 123`, `structural_boundaries: 199`, `args: 45`, `func_start: 33`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 137`, `dead_code: 2`, `fragile_debt: 1`, `orphaned_logic: 1`
* *Architecture:* `api: 12`, `concurrency: 56`, `import: 17`
* *Defense:* `safety: 150`, `doc: 7`, `test: 13`, `immutability_locks: 2`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.629
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::rt::Read, Wants, crate::proto::h1::ClientTransaction, DecodedLength, super::Http1Transaction, crate::proto::BodyLength, std::time::Duration, future::Future...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/proto/h1/conn.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.574 IQR)
- **Top Global Matches:** file_cluster_0: 13.574, file_cluster_13: 13.66, file_cluster_11: 13.773
- **Magnitude:** 2052.1 | **LOC:** 1532 | **CtrlFlow:** 41.4% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 67
- **Risk Profile:** Cognitive Load (23.7492%), Tech Debt (10.6035%)
**Top Internal Functions/Classes:**
  * `new` (Impact: 1852.8 | O(2^N) | DB: 67)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 128`, `structural_boundaries: 181`, `args: 39`, `func_start: 50`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 161`, `planned_debt: 3`, `fragile_debt: 1`
* *Architecture:* `io: 1`, `api: 19`, `concurrency: 3`, `import: 23`
* *Defense:* `safety: 133`, `doc: 26`, `test: 28`, `immutability_locks: 1`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.629
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` mock::AsyncIo, crate::rt::Read, http_body::Frame, Wants, ::uri::Uri, std::str::FromStr, Method, std::future::Future...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/proto/h1/decode.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.587 IQR)
- **Top Global Matches:** file_cluster_4: 13.587, file_cluster_0: 13.902, file_cluster_13: 14.014
- **Magnitude:** 1209.68 | **LOC:** 1255 | **CtrlFlow:** 18.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 23
- **Risk Profile:** Cognitive Load (71.6197%), Tech Debt (88.663%)
**Top Internal Functions/Classes:**
  * `test_read_chunk_size` (Impact: 102.7 | O(N^6) | DB: 23)
  * `read_extension` (Impact: 64.2 | O(2^N) | DB: 3)
  * `read_body` (Impact: 50.7 | O(N^4) | DB: 4)
  * `decode_trailers` (Impact: 44.4 | O(N^6) | DB: 4)
  * `read_end_cr` (Impact: 35.8 | O(N^6) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 92`, `structural_boundaries: 399`, `args: 51`, `func_start: 43`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 43`, `state_mutation: 253`, `planned_debt: 2`, `duplicate_logic: 5`, `orphaned_logic: 17`
* *Architecture:* `io: 2`, `api: 1`, `concurrency: 287`, `import: 19`
* *Defense:* `safety: 163`, `doc: 28`, `test: 62`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.629
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::rt::Read, http_body::Frame, std::convert::TryFrom, bytes::BufMut, std::error::Error, std::time::Duration, Eof, bytes::BytesMut...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/proto/h1/io.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.868 IQR)
- **Top Global Matches:** file_cluster_0: 12.868, file_cluster_11: 13.098, file_cluster_13: 13.154
- **Magnitude:** 1095.48 | **LOC:** 968 | **CtrlFlow:** 28.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 41
- **Risk Profile:** Cognitive Load (36.2866%), Tech Debt (9.8881%)
**Top Internal Functions/Classes:**
  * `poll_flush` (Impact: 610.8 | O(2^N) | DB: 41)
  * `parse` (Impact: 143.5 | O(2^N) | DB: 3)
  * `consume_leading_lines` (Impact: 30.6 | O(N^5) | DB: 2)
  * `new` (Impact: 24.9 | O(2^N))
  * `poll_read_from_io` (Impact: 17.1 | O(N^5) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 166`, `args: 21`, `func_start: 57`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 133`, `dead_code: 8`, `planned_debt: 4`
* *Architecture:* `io: 1`, `api: 39`, `concurrency: 11`, `import: 14`
* *Defense:* `safety: 40`, `doc: 25`, `test: 46`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.629
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::rt::Read, std::io::self, crate::proto::h1::ClientTransaction, tokio_test::io::Builder, super::Http1Transaction, std::time::Duration, ParsedMessage, crate::common::io::Compat...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/proto/h2/client.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.302 IQR)
- **Top Global Matches:** file_cluster_4: 13.302, file_cluster_13: 13.398, file_cluster_16: 13.398
- **Magnitude:** 941.66 | **LOC:** 792 | **CtrlFlow:** 28.7% | **Authorship Centralization:** 25.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (69.1283%), Tech Debt (87.9774%)
**Top Internal Functions/Classes:**
  * `poll` (Impact: 321.1 | O(2^N) | DB: 5)
  * `poll` (Impact: 75.4 | O(2^N) | DB: 6)
  * `handshake` (Impact: 61.9 | O(2^N) | DB: 4)
  * `poll` (Impact: 53.8 | O(2^N) | DB: 4)
  * `poll_pipe` (Impact: 44.6 | O(N^6) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 164`, `args: 20`, `func_start: 17`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 85`, `dead_code: 1`, `fragile_debt: 1`, `duplicate_logic: 6`, `orphaned_logic: 2`
* *Architecture:* `api: 26`, `concurrency: 118`, `import: 24`
* *Defense:* `safety: 120`, `doc: 5`, `immutability_locks: 16`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.629
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::
    convert::Infallible, crate::rt::Read, Sender, FusedFuture, crate::Request, crate::upgrade::Upgraded, SendBuf, futures_channel::mpsc::Receiver...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/proto/h2/server.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.713 IQR)
- **Top Global Matches:** file_cluster_4: 12.713, file_cluster_13: 12.828, file_cluster_16: 12.949
- **Magnitude:** 795.68 | **LOC:** 551 | **CtrlFlow:** 24.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (75.874%), Tech Debt (20.407%)
**Top Internal Functions/Classes:**
  * `poll_server` (Impact: 227.0 | O(2^N) | DB: 7)
  * `poll` (Impact: 110.8 | O(2^N) | DB: 9)
  * `new` (Impact: 108.5 | O(2^N) | DB: 1)
  * `poll2` (Impact: 99.4 | O(2^N) | DB: 7)
  * `graceful_shutdown` (Impact: 36.6 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 124`, `args: 12`, `func_start: 9`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 75`, `dead_code: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 18`, `concurrency: 85`, `import: 25`
* *Defense:* `safety: 67`, `test: 2`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.629
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::rt::Read, Handshake, std::error::Error, std::future::Future, std::time::Duration, SendBuf, crate::rt::bounds::Http2ServerConnExec, h2::server::Connection...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/client.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.469 IQR)
- **Top Global Matches:** file_cluster_4: 11.469, file_cluster_8: 11.804, file_cluster_0: 11.905
- **Magnitude:** 741.56 | **LOC:** 2930 | **CtrlFlow:** 12.6% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 23
- **Risk Profile:** Cognitive Load (34.6295%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `client_100_then_http09` (Impact: 38.6 | O(N^6) | DB: 5)
  * `expect` (Impact: 26.7 | O(2^N))
  * `http2_detect_conn_eof` (Impact: 22.2 | O(N^6) | DB: 18)
  * `upgrade` (Impact: 18.1 | O(2^N) | DB: 12)
  * `fmt` (Impact: 14.3 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 374`, `args: 77`, `func_start: 31`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 123`, `high_risk_execution: 3`, `state_mutation: 116`, `dead_code: 4`, `duplicate_logic: 2`, `orphaned_logic: 11`
* *Architecture:* `io: 40`, `concurrency: 301`, `import: 27`
* *Defense:* `safety: 71`, `doc: 2`, `test: 44`, `immutability_locks: 4`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.629
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` support::TokioIo, Ordering, std::io::self, std::net::IpAddr, hyper::body::Frame, TcpListener, std::error::Error, std::future::Future...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/client/dispatch.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.159 IQR)
- **Top Global Matches:** file_cluster_0: 14.159, file_cluster_4: 14.179, file_cluster_13: 14.438
- **Magnitude:** 576.84 | **LOC:** 528 | **CtrlFlow:** 17.7% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (45.9591%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `poll` (Impact: 38.0 | O(2^N) | DB: 5)
  * `giver_queue_throughput` (Impact: 34.7 | O(N^5) | DB: 4)
  * `drop` (Impact: 28.9 | O(N^6) | DB: 1)
  * `send` (Impact: 20.5 | O(2^N) | DB: 3)
  * `poll_recv` (Impact: 17.9 | O(2^N) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 163`, `args: 51`, `func_start: 36`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 120`, `dead_code: 3`, `fragile_debt: 1`, `duplicate_logic: 15`, `orphaned_logic: 10`
* *Architecture:* `api: 33`, `concurrency: 96`, `import: 12`
* *Defense:* `safety: 67`, `doc: 36`, `test: 8`, `immutability_locks: 2`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.629
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Callback, http::Request, Response, proto::h2::client::ResponseFutMap, Receiver, std::pin::Pin, http_body::Body, pin_project_lite::pin_project...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/client/conn/http2.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.691 IQR)
- **Top Global Matches:** file_cluster_16: 13.691, file_cluster_4: 13.815, file_cluster_13: 13.882
- **Magnitude:** 544.88 | **LOC:** 712 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 25.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (42.551%), Tech Debt (83.3955%)
**Top Internal Functions/Classes:**
  * `handshake` (Impact: 28.3 | O(2^N))
  * `send_request` (Impact: 22.2 | O(N^6) | DB: 1)
    * *Intent:* /// Sends a `Request` on the associated connection. /// /// Returns a future that if successful, yie...
  * `poll` (Impact: 21.1 | O(2^N) | DB: 4)
    * *Intent:* /// Returns the current maximum receive stream count. /// /// This setting is configured in a [`SETT...
  * `adaptive_window` (Impact: 14.4 | O(2^N) | DB: 2)
    * *Intent:* /// Sets the max connection-level flow control for HTTP2 /// /// Passing `None` will do nothing. ///...
  * `initial_stream_window_size` (Impact: 14.2 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 150`, `args: 47`, `func_start: 46`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 70`, `fragile_debt: 2`, `duplicate_logic: 4`
* *Architecture:* `api: 40`, `concurrency: 121`, `import: 19`
* *Defense:* `safety: 51`, `doc: 187`, `test: 7`, `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.629
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::rt::Read, super::super::dispatch::self, std::error::Error, std::future::Future, std::time::Duration, Incoming, crate::body::Body, Poll...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/support/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_4` (Drift: 10.56 IQR)
- **Top Global Matches:** file_cluster_4: 10.56, file_cluster_8: 10.985, file_cluster_0: 11.061
- **Magnitude:** 504.58 | **LOC:** 594 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (44.4172%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `async_test` (Impact: 141.0 | O(N^6) | DB: 14)
  * `naive_proxy` (Impact: 95.8 | O(N^6) | DB: 18)
  * `runtime` (Impact: 5.5 | O(2^N))
  * `default` (Impact: 3.9 | O(N^3))
  * `default` (Impact: 3.9 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 152`, `args: 15`, `func_start: 6`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 31`, `state_mutation: 39`, `duplicate_logic: 2`
* *Architecture:* `io: 19`, `api: 34`, `concurrency: 169`, `import: 13`
* *Defense:* `safety: 34`, `test: 14`, `sync_locks: 4`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.629
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` StreamExt, Ordering, tokiort::TokioExecutor, futures_util::
    future, std::future::Future, FutureExt, TokioIo, TcpStream...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/single_threaded.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.554 IQR)
- **Top Global Matches:** file_cluster_4: 12.554, file_cluster_13: 12.974, file_cluster_11: 13.181
- **Magnitude:** 491.58 | **LOC:** 384 | **CtrlFlow:** 21.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (64.2172%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `http1_client` (Impact: 62.8 | O(N^4) | DB: 13)
  * `http2_client` (Impact: 62.8 | O(N^4) | DB: 13)
  * `main` (Impact: 42.3 | O(N^4) | DB: 6)
  * `http2_server` (Impact: 33.4 | O(N^5) | DB: 3)
  * `http1_server` (Impact: 27.6 | O(N^4) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 173`, `args: 20`, `func_start: 13`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 38`, `state_mutation: 52`, `orphaned_logic: 3`
* *Architecture:* `io: 24`, `concurrency: 163`, `import: 19`
* *Defense:* `safety: 40`, `doc: 11`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.629
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` support::TokioIo, hyper::Error, std::cell::Cell, hyper::Request, std::thread, Poll, AsyncWriteExt, hyper::server::conn::http2...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ffi/http_types.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.843 IQR)
- **Top Global Matches:** file_cluster_13: 13.843, file_cluster_8: 13.96, file_cluster_0: 14.051
- **Magnitude:** 486.68 | **LOC:** 707 | **CtrlFlow:** 25.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (19.9977%), Tech Debt (98.7855%)
**Top Internal Functions/Classes:**
  * `hyper_headers_foreach` (Impact: 107.8 | O(N^6) | DB: 3)
  * `hyper_request_set_uri_parts` (Impact: 44.4 | O(N^4) | DB: 3)
    * *Intent:* /// An HTTP response. /// /// Obtain one of these by making a request with `hyper_clientconn_send`, ...
  * `hyper_headers_set` (Impact: 19.0 | O(N^4) | DB: 2)
  * `hyper_headers_add` (Impact: 19.0 | O(N^4) | DB: 2)
  * `hyper_request_set_method` (Impact: 15.8 | O(N^4) | DB: 2)
    * *Intent:* /// An HTTP request. /// /// Once you've finished constructing a request, you can send it with /// `...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 149`, `args: 29`, `func_start: 28`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 112`, `planned_debt: 1`, `orphaned_logic: 19`
* *Architecture:* `api: 3`, `import: 13`
* *Defense:* `safety: 42`, `doc: 159`, `test: 5`, `immutability_locks: 22`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.629
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Method, super::UserDataPointer, super::error::hyper_code, crate::header::HeaderName, Uri, c_void, OriginalHeaderOrder, crate::HeaderMap...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/body/incoming.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.249 IQR)
- **Top Global Matches:** file_cluster_0: 13.249, file_cluster_4: 13.319, file_cluster_13: 13.54
- **Magnitude:** 452.34 | **LOC:** 633 | **CtrlFlow:** 22.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (48.8804%), Tech Debt (20.7084%)
**Top Internal Functions/Classes:**
  * `new_channel` (Impact: 90.6 | O(N^6) | DB: 8)
    * *Intent:* /// Create a `Body` stream with an associated sender half. /// /// Useful when wanting to stream chu...
  * `size_hint` (Impact: 26.9 | O(2^N))
    * *Intent:* /// Try to send data on this channel. /// /// # Errors /// /// Returns `Err(Bytes)` if the channel c...
  * `fmt` (Impact: 22.2 | O(2^N) | DB: 2)
  * `fmt` (Impact: 14.6 | O(2^N) | DB: 2)
  * `poll_ready` (Impact: 14.2 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 118`, `args: 21`, `func_start: 26`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 4`, `state_mutation: 64`, `dead_code: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 22`, `concurrency: 115`, `import: 18`
* *Defense:* `safety: 77`, `doc: 46`, `test: 32`, `immutability_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.629
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Sender, http_body::Body, std::future::Future, futures_core::stream::FusedStream, std::task::Poll, Incoming, super::DecodedLength, SizeHint...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `capi/examples/client.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.062 IQR)
- **Local Micro-Species:** `Cluster 0: Defensive Downstream Logic & Immutable State` (Drift: 6.682 IQR)
- **Top Global Matches:** file_cluster_13: 13.062, file_cluster_8: 13.341, file_cluster_0: 13.436
- **Magnitude:** 437.3 | **LOC:** 344 | **CtrlFlow:** 53.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 48
- **Risk Profile:** Cognitive Load (75.3989%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 176.4 | O(N^5) | DB: 48)
    * *Intent:* #define STR_ARG(XX) (uint8_t *)XX, strlen(XX)
  * `connect_to` (Impact: 36.4 | O(N^3) | DB: 11)
  * `read_cb` (Impact: 14.4 | O(N^2) | DB: 6)
  * `write_cb` (Impact: 14.4 | O(N^2) | DB: 6)
  * `free_conn_data` (Impact: 9.6 | O(N^2) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 41`, `args: 9`, `func_start: 7`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 107`, `orphaned_logic: 1`
* *Architecture:* `io: 11`, `api: 63`, `import: 12`
* *Defense:* `safety: 13`, `test: 3`, `immutability_locks: 12`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.629
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` stdlib.h, unistd.h, stdio.h, string.h, types.h, fcntl.h, errno.h, hyper.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/proto/h1/encode.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.399 IQR)
- **Top Global Matches:** file_cluster_0: 11.399, file_cluster_8: 11.527, file_cluster_13: 11.576
- **Magnitude:** 432.14 | **LOC:** 673 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (15.7555%), Tech Debt (99.3278%)
**Top Internal Functions/Classes:**
  * `encode_trailers` (Impact: 96.7 | O(N^6) | DB: 5)
  * `encode` (Impact: 43.3 | O(2^N) | DB: 2)
  * `encode_and_end` (Impact: 23.1 | O(N^6) | DB: 1)
  * `fmt` (Impact: 14.2 | O(2^N) | DB: 1)
  * `remaining` (Impact: 10.9 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 159`, `args: 43`, `func_start: 38`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 58`, `duplicate_logic: 17`
* *Architecture:* `io: 2`, `api: 27`, `import: 15`
* *Defense:* `safety: 38`, `doc: 9`, `test: 33`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.629
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` bytes::BufMut, super::super::io::Cursor, Take, std::cmp::Ordering, MAX_FORWARDS, CONTENT_ENCODING, std::fmt::Write, std::collections::HashSet...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/server/conn/http1.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_4` (Drift: 15.886 IQR)
- **Top Global Matches:** file_cluster_4: 15.886, file_cluster_13: 16.0, file_cluster_16: 16.182
- **Magnitude:** 429.38 | **LOC:** 560 | **CtrlFlow:** 28.3% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 30
- **Risk Profile:** Cognitive Load (49.8696%), Tech Debt (15.0869%)
**Top Internal Functions/Classes:**
  * `poll` (Impact: 248.8 | O(2^N) | DB: 30)
    * *Intent:* /// Start a graceful shutdown process for this connection. /// /// This `Connection` should continue...
  * `without_shutdown` (Impact: 7.3 | O(N^3) | DB: 1)
    * *Intent:* /// A buffer of bytes that have been read but not processed as HTTP. /// /// If the client sent addi...
  * `poll_without_shutdown` (Impact: 5.5 | O(2^N) | DB: 2)
    * *Intent:* /// Deconstructed parts of a `Connection`. /// /// This allows taking apart a `Connection` at a late...
  * `into_parts` (Impact: 3.9 | O(N^3))
  * `graceful_shutdown` (Impact: 3.8 | O(N^2) | DB: 2)
    * *Intent:* /// A configuration builder for HTTP/1 server connections. /// /// **Note**: The default values of o...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 76`, `args: 17`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 48`, `dead_code: 5`, `orphaned_logic: 2`
* *Architecture:* `io: 3`, `api: 14`, `concurrency: 90`, `import: 19`
* *Defense:* `safety: 48`, `doc: 208`, `test: 1`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.629
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::rt::Read, std::error::Error, std::future::Future, std::time::Duration, crate::upgrade::Upgraded, crate::
    common::time::Dur, Incoming, crate::body::Body...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/client/conn/http1.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_16` (Drift: 14.669 IQR)
- **Top Global Matches:** file_cluster_16: 14.669, file_cluster_4: 14.725, file_cluster_13: 14.787
- **Magnitude:** 421.42 | **LOC:** 612 | **CtrlFlow:** 19.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 25
- **Risk Profile:** Cognitive Load (49.6591%), Tech Debt (94.7457%)
**Top Internal Functions/Classes:**
  * `poll` (Impact: 167.5 | O(2^N) | DB: 25)
  * `send_request` (Impact: 22.2 | O(N^6) | DB: 1)
    * *Intent:* /// Returns a future that if successful, yields the `Response`. /// /// `req` must have a `Host` hea...
  * `without_shutdown` (Impact: 7.3 | O(N^3) | DB: 1)
    * *Intent:* /// Prevent shutdown of the underlying IO object at the end of service the request, /// instead run ...
  * `poll_without_shutdown` (Impact: 5.3 | O(2^N) | DB: 2)
    * *Intent:* /// Poll the connection for completion, but without calling `shutdown` /// on the underlying IO. ///...
  * `poll_ready` (Impact: 5.3 | O(2^N) | DB: 2)
    * *Intent:* /// Polls to determine whether this sender can be used yet for a request. /// /// If the associated ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 101`, `args: 25`, `func_start: 23`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 52`, `fragile_debt: 2`, `duplicate_logic: 2`, `orphaned_logic: 3`
* *Architecture:* `api: 27`, `concurrency: 95`, `import: 15`
* *Defense:* `safety: 64`, `doc: 214`, `test: 1`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.629
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::rt::Read, super::super::dispatch::self, std::error::Error, std::future::Future, crate::upgrade::Upgraded, Incoming, crate::body::Body, httparse::ParserConfig...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `benches/end_to_end.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.592 IQR)
- **Top Global Matches:** file_cluster_4: 11.592, file_cluster_0: 11.695, file_cluster_8: 11.929
- **Magnitude:** 413.54 | **LOC:** 452 | **CtrlFlow:** 15.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 32
- **Risk Profile:** Cognitive Load (91.9847%), Tech Debt (99.4252%)
**Top Internal Functions/Classes:**
  * `bench` (Impact: 121.1 | O(N^6) | DB: 32)
  * `spawn_server` (Impact: 38.8 | O(N^6) | DB: 23)
  * `http2_adaptive_window` (Impact: 6.3 | O(2^N) | DB: 1)
  * `request_chunks` (Impact: 6.3 | O(2^N) | DB: 1)
  * `http2` (Impact: 6.2 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 130`, `args: 39`, `func_start: 31`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 12`, `high_risk_execution: 1`, `state_mutation: 54`, `planned_debt: 2`, `orphaned_logic: 19`
* *Architecture:* `io: 16`, `concurrency: 75`, `import: 11`
* *Defense:* `safety: 26`, `test: 6`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.629
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` tokio::net::TcpListener, hyper::service::service_fn, Response, hyper::Method, futures_util::SinkExt, std::convert::Infallible, std::net::SocketAddr, hyper::body::Frame...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `capi/examples/upload.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.815 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 6.525 IQR)
- **Top Global Matches:** file_cluster_13: 12.815, file_cluster_8: 13.073, file_cluster_0: 13.199
- **Magnitude:** 394.62 | **LOC:** 401 | **CtrlFlow:** 46.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 48
- **Risk Profile:** Cognitive Load (68.5949%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 111.6 | O(N^5) | DB: 48)
    * *Intent:* #define STR_ARG(XX) (uint8_t *)XX, strlen(XX)
  * `connect_to` (Impact: 36.4 | O(N^3) | DB: 11)
  * `poll_req_upload` (Impact: 22.1 | O(N^6) | DB: 7)
  * `read_cb` (Impact: 14.4 | O(N^2) | DB: 6)
  * `write_cb` (Impact: 14.4 | O(N^2) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 50`, `args: 10`, `func_start: 8`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 107`, `orphaned_logic: 1`
* *Architecture:* `io: 13`, `api: 63`, `import: 12`
* *Defense:* `safety: 10`, `test: 2`, `immutability_locks: 10`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.629
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` stdlib.h, unistd.h, stdio.h, string.h, types.h, fcntl.h, errno.h, hyper.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/proto/h2/upgrade.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_11` (Drift: 15.017 IQR)
- **Top Global Matches:** file_cluster_11: 15.017, file_cluster_0: 15.025, file_cluster_13: 15.033
- **Magnitude:** 323.4 | **LOC:** 281 | **CtrlFlow:** 35.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (62.2459%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `poll_write` (Impact: 80.3 | O(N^6) | DB: 14)
  * `poll_read` (Impact: 72.1 | O(N^6) | DB: 13)
  * `tick` (Impact: 25.5 | O(N^6) | DB: 3)
  * `poll_flush` (Impact: 18.9 | O(N^5) | DB: 7)
  * `poll` (Impact: 16.2 | O(N^5) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 64`, `args: 9`, `func_start: 9`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 61`, `dead_code: 4`
* *Architecture:* `io: 15`, `api: 8`, `concurrency: 11`, `import: 12`
* *Defense:* `safety: 83`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.629
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::rt::Read, std::future::Future, std::io::Cursor, ReadBufCursor, super::SendBuf, futures_channel::mpsc, Poll, Stream...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/upgrade.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.583 IQR)
- **Top Global Matches:** file_cluster_13: 14.583, file_cluster_16: 14.654, file_cluster_0: 14.731
- **Magnitude:** 284.98 | **LOC:** 408 | **CtrlFlow:** 17.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (42.5571%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `poll` (Impact: 37.1 | O(2^N) | DB: 3)
  * `on_upgrade` (Impact: 17.8 | O(2^N) | DB: 1)
  * `__hyper_downcast` (Impact: 17.3 | O(N^4) | DB: 2)
  * `downcast` (Impact: 16.4 | O(N^4))
    * *Intent:* /// The deconstructed parts of an [`Upgraded`] type. /// /// Includes the original IO type, and a re...
  * `poll_read` (Impact: 9.3 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 86`, `args: 28`, `func_start: 27`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 55`, `dead_code: 1`, `planned_debt: 1`, `duplicate_logic: 14`
* *Architecture:* `io: 2`, `api: 10`, `concurrency: 9`, `import: 14`
* *Defense:* `safety: 47`, `doc: 82`, `test: 2`, `sync_locks: 2`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.629
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::rt::Read, crate::common::io::Rewind, super::OnUpgrade, bytes::Bytes, std::any::TypeId, super::*, ReadBufCursor, std::pin::Pin...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ffi/task.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_16` (Drift: 15.779 IQR)
- **Top Global Matches:** file_cluster_16: 15.779, file_cluster_13: 15.789, file_cluster_4: 15.835
- **Magnitude:** 272.0 | **LOC:** 550 | **CtrlFlow:** 31.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (47.1932%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `hyper_task_type` (Impact: 49.0 | O(N^3) | DB: 10)
  * `hyper_task_value` (Impact: 34.3 | O(N^4) | DB: 4)
    * *Intent:* /// drain_queue locks both self.spawn_queue and self.driver, so it requires
  * `poll` (Impact: 17.8 | O(2^N) | DB: 5)
  * `hyper_executor_poll` (Impact: 13.8 | O(N^3) | DB: 1)
  * `hyper_executor_push` (Impact: 8.1 | O(N^2) | DB: 1)
    * *Intent:* /// When nonblocking I/O in one of those callbacks can't make progress (returns /// `EAGAIN` or `EWO...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 61`, `args: 18`, `func_start: 18`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 58`
* *Architecture:* `api: 16`, `concurrency: 36`, `import: 9`
* *Defense:* `safety: 46`, `doc: 188`, `sync_locks: 3`, `immutability_locks: 11`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.629
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Ordering, std::sync::
    atomic::AtomicBool, Arc, super::error::hyper_code, Stream, Weak, std::task::Context, std::pin::Pin...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/proto/h2/ping.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.352 IQR)
- **Top Global Matches:** file_cluster_0: 14.352, file_cluster_16: 14.391, file_cluster_11: 14.422
- **Magnitude:** 269.04 | **LOC:** 515 | **CtrlFlow:** 35.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (24.6658%), Tech Debt (99.6016%)
**Top Internal Functions/Classes:**
  * `maybe_ping` (Impact: 61.6 | O(N^5) | DB: 5)
  * `maybe_schedule` (Impact: 30.9 | O(N^5) | DB: 1)
  * `maybe_timeout` (Impact: 21.4 | O(N^5) | DB: 3)
  * `send_ping` (Impact: 20.6 | O(2^N) | DB: 1)
  * `record_data` (Impact: 18.9 | O(N^3) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 53`, `args: 18`, `func_start: 17`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 50`, `dead_code: 2`, `fragile_debt: 2`, `orphaned_logic: 7`
* *Architecture:* `api: 5`
* *Defense:* `safety: 25`, `doc: 44`, `sync_locks: 2`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.629
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Instant, h2::Ping, PingPong, std::pin::Pin, crate::common::time::Time, std::future::Future, Mutex, std::time::Duration...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/client/dispatch.rs` (RUST) | Magnitude: 576.84 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 359, structural_boundaries: 163, state_mutation: 120, concurrency: 96
- `src/proto/mod.rs` (RUST) | Magnitude: 20.96 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 24, api: 16, encapsulation: 16, structural_boundaries: 14
- `examples/hello-http2.rs` (RUST) | Magnitude: 140.94 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 37, structural_boundaries: 19, branch: 13, concurrency: 12
- `src/proto/h2/ping.rs` (RUST) | Magnitude: 269.04 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 158, structural_boundaries: 53, state_mutation: 50, doc: 44
- `tests/support/tokiort.rs` (RUST) | Magnitude: 230.3 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 146, structural_boundaries: 63, generics: 55, state_mutation: 37

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `src/proto/h2/upgrade.rs` (RUST) | Magnitude: 323.4 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 203, safety: 83, structural_boundaries: 64, state_mutation: 61
- `src/common/task.rs` (RUST) | Magnitude: 25.1 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 16, doc: 7, pointers: 7, structural_boundaries: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `examples/params.rs` (RUST) | Magnitude: 152.72 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 80, structural_boundaries: 44, safety: 25, branch: 17
- `src/ffi/io.rs` (RUST) | Magnitude: 133.32 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: doc: 69, indent_spaces: 60, state_mutation: 51, structural_boundaries: 43
- `src/ffi/client.rs` (RUST) | Magnitude: 181.96 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 106, doc: 101, state_mutation: 65, structural_boundaries: 62
- `src/proto/h1/mod.rs` (RUST) | Magnitude: 39.02 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 55, structural_boundaries: 34, generics: 23, api: 13
- `src/server/conn/http2.rs` (RUST) | Magnitude: 265.48 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 216, doc: 108, structural_boundaries: 80, state_mutation: 58

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `src/ffi/task.rs` (RUST) | Magnitude: 272.0 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 188, indent_spaces: 119, structural_boundaries: 61, state_mutation: 58
- `src/client/conn/http1.rs` (RUST) | Magnitude: 421.42 | Delta: **0.056 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 237, doc: 214, structural_boundaries: 101, concurrency: 95
- `src/rt/timer.rs` (RUST) | Magnitude: 79.38 | Delta: **0.102 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: doc: 73, indent_spaces: 44, state_mutation: 19, concurrency: 19
- `src/client/conn/http2.rs` (RUST) | Magnitude: 544.88 | Delta: **0.124 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 401, doc: 187, structural_boundaries: 150, generics: 122
- `src/common/future.rs` (RUST) | Magnitude: 28.18 | Delta: **0.144 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: generics: 15, structural_boundaries: 12, concurrency: 12, indent_spaces: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `capi/gen_header.sh` (SHELL) | Magnitude: 61.22 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 25, indent_spaces: 22, state_mutation: 18, io: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/proto/h1/dispatch.rs` (RUST) | Magnitude: 2188.1 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 633, structural_boundaries: 199, safety: 150, state_mutation: 137
- `tests/support/trailers.rs` (RUST) | Magnitude: 68.4 | Delta: **0.053 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 48, structural_boundaries: 20, safety: 19, concurrency: 19
- `src/service/service.rs` (RUST) | Magnitude: 49.44 | Delta: **0.093 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: doc: 46, indent_spaces: 36, concurrency: 26, structural_boundaries: 23
- `src/proto/h2/client.rs` (RUST) | Magnitude: 941.66 | Delta: **0.096 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 509, structural_boundaries: 164, generics: 127, safety: 120
- `benches/end_to_end.rs` (RUST) | Magnitude: 413.54 | Delta: **0.103 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 310, structural_boundaries: 130, concurrency: 75, state_mutation: 54

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `benches/connect.rs` (RUST) | Magnitude: 11.56 | Delta: **0.057 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: dead_code: 14, decorators: 2, sec_dead_code: 2, planned_debt: 1
- `src/rt/mod.rs` (RUST) | Magnitude: 22.3 | Delta: **0.213 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 37, structural_boundaries: 6, api: 4, encapsulation: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `src/client/mod.rs` (RUST) | Magnitude: 15.64 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 12, structural_boundaries: 3, indent_spaces: 3, sec_dead_code: 3
- `src/server/conn/mod.rs` (RUST) | Magnitude: 14.08 | Delta: **0.137 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: doc: 15, structural_boundaries: 2, api: 2, decorators: 2
- `src/server/mod.rs` (RUST) | Magnitude: 11.52 | Delta: **0.239 IQR** | Secondary Pull: `file_cluster_1`
  * Top Architectural Signatures: doc: 8, sec_dead_code: 3, structural_boundaries: 1, api: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/mock.rs` (RUST) | Magnitude: 10.52 | Delta: **0.269 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: sec_high_risk_execution: 2, planned_debt: 1, fragile_debt: 1, sec_homoglyphs: 1
- `src/client/tests.rs` (RUST) | Magnitude: 10.52 | Delta: **0.306 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: sec_high_risk_execution: 2, planned_debt: 1, fragile_debt: 1
- `src/ffi/macros.rs` (RUST) | Magnitude: 22.96 | Delta: **0.332 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 44, branch: 12, safety: 7, state_mutation: 6
- `src/common/mod.rs` (RUST) | Magnitude: 23.42 | Delta: **0.339 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 8, api: 8, encapsulation: 8, decorators: 7
- `examples/send_file_index.html` (HTML) | Magnitude: 15.2 | Delta: **0.82 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 4, io: 4, doc: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/client/conn/http2.rs` -> Churn: **100.0%** | Cog Load: 42.551% | Debt: 83.3955%
- `src/proto/h2/client.rs` -> Churn: **100.0%** | Cog Load: 69.1283% | Debt: 87.9774%
- `src/proto/h2/mod.rs` -> Churn: **86.14%** | Cog Load: 68.5017% | Debt: 0.0%
- `src/client/dispatch.rs` -> Churn: **68.26%** | Cog Load: 45.9591% | Debt: 100.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/proto/h1/decode.rs` -> **Sean McArthur** (100.0% isolated ownership) | Magnitude: 1209.68
- `src/proto/h2/server.rs` -> **Sean McArthur** (100.0% isolated ownership) | Magnitude: 795.68
- `src/ffi/http_types.rs` -> **Dhruva D** (100.0% isolated ownership) | Magnitude: 486.68
- `src/body/incoming.rs` -> **Sean McArthur** (100.0% isolated ownership) | Magnitude: 452.34
- `src/proto/h1/encode.rs` -> **HueCodes** (100.0% isolated ownership) | Magnitude: 432.14

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/service/http.rs` -> **Severity: 0.323** (Embedded: 0.0098 * Error Risk: 32.9353%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `benches/support/tokiort.rs` -> **Severity: 962.9** (Blast Radius: 9.629 * Doc Risk: 100.0%)
- `src/client/dispatch.rs` -> **Severity: 962.9** (Blast Radius: 9.629 * Doc Risk: 100.0%)
- `src/common/io/rewind.rs` -> **Severity: 962.9** (Blast Radius: 9.629 * Doc Risk: 100.0%)
- `src/common/time.rs` -> **Severity: 962.9** (Blast Radius: 9.629 * Doc Risk: 100.0%)
- `src/proto/h1/decode.rs` -> **Severity: 962.9** (Blast Radius: 9.629 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
