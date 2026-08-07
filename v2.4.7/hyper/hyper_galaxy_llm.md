# ARCHITECTURAL_BRIEF: hyper
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_rust/hyper` |
| **Timestamp** | `2026-08-07T04:05:13.837202+00:00` |
| **Scan Duration** | `0.59s` |
| **Git Branch** | `master` |
| **Git Commit** | `0d6c7d5469baa09e2fb127ee3758a79b3271a4f0` |
| **Git Remote** | `https://github.com/hyperium/hyper.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 96 malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are a Senior Technical Storyteller and Codebase Architect. GitGalaxy has translated the non-visual architecture of this repository into measurable Structural Signatures (regex-derived counts, not an AST or compiler pass). Your job is to weave those signatures into a coherent, factual narrative about how this system is built -- its architecture, design patterns, and complexity -- not to render a verdict.
> 
> **CORE DIRECTIVES:**
> 1. **Narrate the Architecture, Don't Judge the Author:** Frame every observation as a blameless description of the system's physical reality. High Risk Exposure (e.g., Cognitive Load Exposure) describes where the architecture may be drifting into fragile territory, not developer incompetence -- it is a prompt to investigate, never a verdict.
> 2. **The Physical Reality Rule:** Base your narrative strictly on the provided Structural Signatures and the numbers derived from them. Do not hallucinate meaning, and do not restate a heuristic's raw label (e.g. a 'Logic Bomb' or 'O(2^N)' flag) as a confirmed finding of malice or a guaranteed defect -- explain what the signature actually measures, weave it into the story of the file, and let the reader draw their own conclusion.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`. Tell that balance as part of the narrative, not as an isolated alarm.
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
| Cognitive Load Exposure | 0.0 | 100.0 | 40.6 | 42.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.0 | 32.7 | 31.9 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 48.6 | 44.5 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 3.9 | 2.3 | 0.0 |
| API Exposure | 0.0 | 13.0 | 3.2 | 3.5 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 56.5 | 98.4 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 46.4 | 32.4 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 7.5 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 90.7 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 5.1 | 0.6 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 11.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 18.0 | 11.9 | 0.0 |
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

- `new` (@ `src/proto/h1/conn.rs`) -> Impact: **286.9** | LOC: 937
- `poll_catch` (@ `src/proto/h1/dispatch.rs`) -> Impact: **241.0** | LOC: 663
- `get_should_ignore_body` (@ `tests/server.rs`) -> Impact: **160.2** | LOC: 1818
- `poll_write` (@ `src/proto/h1/dispatch.rs`) -> Impact: **148.2** | LOC: 470
- `poll_flush` (@ `src/proto/h1/io.rs`) -> Impact: **112.0** | LOC: 577
- `write_header_name` (@ `src/proto/h1/role.rs`) -> Impact: **95.9** | LOC: 238
- `parse` (@ `src/proto/h1/role.rs`) -> Impact: **80.5** | LOC: 225
- `parse` (@ `src/proto/h1/role.rs`) -> Impact: **70.8** | LOC: 169
- `test_parse_request_errors` (@ `src/proto/h1/role.rs`) -> Impact: **68.3** | LOC: 777
- `main` (@ `capi/examples/client.c`) -> Impact: **65.5** | LOC: 202
  * *Intent:* #define STR_ARG(XX) (uint8_t *)XX, strlen(XX)

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src/proto/h1` | 7 | 4262.38 | 39.14% | 94.45% |
| `tests` | 3 | 2436.38 | 27.82% | 0.0% |
| `examples` | 18 | 1214.88 | 58.93% | 0.0% |
| `src/proto/h2` | 5 | 1064.24 | 61.76% | 61.02% |
| `src/ffi` | 8 | 721.36 | 29.18% | 72.8% |
| `src/client/conn` | 3 | 689.5 | 34.42% | 66.66% |
| `capi/examples` | 3 | 582.92 | 51.7% | 0.0% |
| `benches` | 5 | 526.68 | 59.55% | 61.1% |
| `tests/support` | 3 | 490.08 | 35.88% | 0.0% |
| `src` | 7 | 481.52 | 15.87% | 56.76% |

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
- `src/proto/h1/role.rs` -> **9** Orphaned Functions | **15** Duplicates
- `src/proto/h1/decode.rs` -> **17** Orphaned Functions | **5** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`capi/examples/client.c`** -> AI Confidence: **99.31%**
2. **`examples/hello-http2.rs`** -> AI Confidence: **99.24%**
3. **`src/proto/h1/conn.rs`** -> AI Confidence: **99.24%**
4. **`capi/examples/upload.c`** -> AI Confidence: **99.24%**
5. **`examples/client.rs`** -> AI Confidence: **99.18%**
6. **`examples/echo.rs`** -> AI Confidence: **99.18%**
7. **`examples/http_proxy.rs`** -> AI Confidence: **99.18%**
8. **`examples/params.rs`** -> AI Confidence: **99.18%**
9. **`examples/web_api.rs`** -> AI Confidence: **99.18%**
10. **`src/common/buf.rs`** -> AI Confidence: **99.18%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1303` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `benches/server.rs` (RUST) -> Cumulative Risk: **657.79**
- **Archetype:** `file_cluster_4` (Distance: 11.885 IQR)
- **Magnitude:** 177.9 | **LOC:** 228 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9999%), State Flux (99.9991%), Safety Score (98.9816%)
- **Heaviest Functions:** `raw_tcp_throughput_large_payload` (Impact: 17.9), `raw_tcp_throughput_small_payload` (Impact: 10.8), `throughput_fixedsize_many_chunks` (Impact: 4.9)

### 2. `src/client/dispatch.rs` (RUST) -> Cumulative Risk: **652.39**
- **Archetype:** `file_cluster_0` (Distance: 14.148 IQR)
- **Magnitude:** 389.64 | **LOC:** 528 | **CtrlFlow:** 17.3% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Concurrency (100.0%), Spec Match (100.0%), State Flux (99.9861%)
- **Heaviest Functions:** `giver_queue_throughput` (Impact: 12.3), `drop` (Impact: 8.8), `can_send` (Impact: 8.7)

### 3. `src/common/io/rewind.rs` (RUST) -> Cumulative Risk: **630.58**
- **Archetype:** `file_cluster_4` (Distance: 12.876 IQR)
- **Magnitude:** 105.16 | **LOC:** 171 | **CtrlFlow:** 4.8% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9998%), Tech Debt (99.1845%)
- **Heaviest Functions:** `poll_read` (Impact: 10.7), `partial_rewind` (Impact: 2.8), `full_rewind` (Impact: 2.7)

### 4. `benches/end_to_end.rs` (RUST) -> Cumulative Risk: **629.29**
- **Archetype:** `file_cluster_4` (Distance: 11.591 IQR)
- **Magnitude:** 259.14 | **LOC:** 452 | **CtrlFlow:** 15.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9996%), Tech Debt (99.4252%), State Flux (94.2896%)
- **Heaviest Functions:** `bench` (Impact: 38.8), `spawn_server` (Impact: 12.8), `http2_parallel_x10_req_10mb` (Impact: 2.8)

### 5. `src/proto/h2/client.rs` (RUST) -> Cumulative Risk: **625.69**
- **Archetype:** `file_cluster_4` (Distance: 13.309 IQR)
- **Magnitude:** 399.96 | **LOC:** 792 | **CtrlFlow:** 28.7% | **Authorship Centralization:** 25.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Churn (100.0%), Concurrency (99.9997%), State Flux (92.9813%)
- **Heaviest Functions:** `poll` (Impact: 50.9), `poll_pipe` (Impact: 14.7), `new_builder` (Impact: 13.3)

### 6. `src/common/future.rs` (RUST) -> Cumulative Risk: **603.16**
- **Archetype:** `file_cluster_16` (Distance: 11.449 IQR)
- **Magnitude:** 27.08 | **LOC:** 31 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `poll` (Impact: 1.9), `poll_fn` (Impact: 1.7)

### 7. `src/client/conn/http2.rs` (RUST) -> Cumulative Risk: **596.1**
- **Archetype:** `file_cluster_16` (Distance: 13.712 IQR)
- **Magnitude:** 381.28 | **LOC:** 712 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 25.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Churn (100.0%), Tech Debt (99.9927%), Spec Match (96.2963%)
- **Heaviest Functions:** `send_request` (Impact: 7.2), `poll_ready` (Impact: 5.5), `poll` (Impact: 5.5)

### 8. `src/proto/h2/mod.rs` (RUST) -> Cumulative Risk: **567.45**
- **Archetype:** `file_cluster_4` (Distance: 13.837 IQR)
- **Magnitude:** 76.96 | **LOC:** 265 | **CtrlFlow:** 28.9% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.995%), State Flux (96.5586%), Churn (86.14%)
- **Heaviest Functions:** `send_eos_frame` (Impact: 5.0), `remaining` (Impact: 3.9), `chunk` (Impact: 3.9)

### 9. `src/proto/h1/dispatch.rs` (RUST) -> Cumulative Risk: **566.75**
- **Archetype:** `file_cluster_4` (Distance: 13.8 IQR)
- **Magnitude:** 796.4 | **LOC:** 809 | **CtrlFlow:** 38.0% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.7906%), State Flux (99.2953%), Concurrency (98.7872%)
- **Heaviest Functions:** `poll_catch` (Impact: 241.0), `poll_write` (Impact: 148.2), `poll_read` (Impact: 41.9)

### 10. `benches/support/tokiort.rs` (RUST) -> Cumulative Risk: **564.05**
- **Archetype:** `file_cluster_0` (Distance: 12.691 IQR)
- **Magnitude:** 113.3 | **LOC:** 233 | **CtrlFlow:** 14.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.4398%), Concurrency (89.0223%)
- **Heaviest Functions:** `poll_read` (Impact: 5.3), `poll_read` (Impact: 4.9), `reset` (Impact: 4.2)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `tests/server.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.988 IQR)
- **Top Global Matches:** file_cluster_4: 11.988, file_cluster_8: 12.431, file_cluster_0: 12.435
- **Magnitude:** 1848.98 | **LOC:** 3601 | **CtrlFlow:** 8.0% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (49.4512%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `get_should_ignore_body` (Impact: 160.2)
  * `serve` (Impact: 14.3)
  * `call` (Impact: 11.8)
  * `read_until` (Impact: 11.6)
  * `build_reply` (Impact: 11.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 1038`, `args: 189`, `func_start: 131`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 358`, `state_mutation: 377`, `planned_debt: 1`, `duplicate_logic: 11`, `orphaned_logic: 18`
* *Architecture:* `io: 54`, `api: 2`, `concurrency: 1027`, `import: 41`
* *Defense:* `safety: 110`, `doc: 2`, `test: 199`, `sync_locks: 14`, `immutability_locks: 13`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.629
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Full, hyper::Method, FutureExt, hyper::service::service_fn, AsyncWriteExt, Either, Request, TcpStream...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/proto/h1/role.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.149 IQR)
- **Top Global Matches:** file_cluster_0: 13.149, file_cluster_8: 13.291, file_cluster_13: 13.375
- **Magnitude:** 1113.46 | **LOC:** 3174 | **CtrlFlow:** 34.2% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (39.6664%), Tech Debt (74.8462%)
**Top Internal Functions/Classes:**
  * `write_header_name` (Impact: 95.9)
  * `parse` (Impact: 80.5)
  * `parse` (Impact: 70.8)
  * `test_parse_request_errors` (Impact: 68.3)
  * `set_length` (Impact: 60.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 275`, `structural_boundaries: 530`, `args: 87`, `func_start: 71`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 354`, `dead_code: 1`, `planned_debt: 6`, `duplicate_logic: 15`, `orphaned_logic: 9`
* *Architecture:* `api: 7`, `import: 39`
* *Defense:* `safety: 306`, `doc: 7`, `test: 63`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.629
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` httparse::ParserConfig, http::header::HeaderValue, bytes::BytesMut, smallvec::smallvec, ParsedMessage, http::header::ValueIter, crate::headers, test::Bencher...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/proto/h1/dispatch.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.8 IQR)
- **Top Global Matches:** file_cluster_4: 13.8, file_cluster_13: 13.838, file_cluster_0: 13.855
- **Magnitude:** 796.4 | **LOC:** 809 | **CtrlFlow:** 38.0% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (76.6893%), Tech Debt (99.7906%)
**Top Internal Functions/Classes:**
  * `poll_catch` (Impact: 241.0)
  * `poll_write` (Impact: 148.2)
  * `poll_read` (Impact: 41.9)
    * *Intent:* // This could happen if reading paused before blocking on IO, // such as getting to the end of a fra...
  * `poll_read_head` (Impact: 23.6)
  * `recv_msg` (Impact: 19.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 122`, `structural_boundaries: 199`, `args: 44`, `func_start: 33`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 125`, `dead_code: 2`, `fragile_debt: 1`, `duplicate_logic: 13`, `orphaned_logic: 5`
* *Architecture:* `api: 12`, `concurrency: 56`, `import: 17`
* *Defense:* `safety: 150`, `doc: 7`, `test: 13`, `immutability_locks: 2`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.629
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::body::Body, future::Future, DecodedLength, task::Context, http::Request, std::convert::Infallible, crate::common::task, bytes::Buf...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/proto/h1/decode.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.488 IQR)
- **Top Global Matches:** file_cluster_4: 13.488, file_cluster_0: 13.809, file_cluster_8: 13.914
- **Magnitude:** 781.58 | **LOC:** 1255 | **CtrlFlow:** 17.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (68.1632%), Tech Debt (88.663%)
**Top Internal Functions/Classes:**
  * `test_read_chunk_size` (Impact: 24.8)
  * `read_async` (Impact: 13.7)
  * `read` (Impact: 13.6)
  * `read_err` (Impact: 12.4)
  * `read_body` (Impact: 11.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 399`, `args: 49`, `func_start: 43`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 43`, `state_mutation: 245`, `planned_debt: 2`, `duplicate_logic: 5`, `orphaned_logic: 17`
* *Architecture:* `io: 2`, `api: 1`, `concurrency: 292`, `import: 19`
* *Defense:* `safety: 163`, `doc: 28`, `test: 62`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.629
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` self::ChunkedState::*, bytes::BytesMut, self::Kind::Chunked, std::io, std::io::Write, Eof, super::io::MemRead, Poll...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/proto/h1/conn.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.435 IQR)
- **Top Global Matches:** file_cluster_0: 13.435, file_cluster_13: 13.532, file_cluster_11: 13.663
- **Magnitude:** 767.8 | **LOC:** 1532 | **CtrlFlow:** 39.7% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (34.363%), Tech Debt (99.2994%)
**Top Internal Functions/Classes:**
  * `new` (Impact: 286.9)
  * `maybe_notify` (Impact: 17.9)
  * `idle` (Impact: 17.2)
  * `write_trailers` (Impact: 16.8)
  * `require_empty_read` (Impact: 15.5)
    * *Intent:* #[cfg(feature = "client")]
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 119`, `structural_boundaries: 181`, `args: 54`, `func_start: 50`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 141`, `planned_debt: 3`, `fragile_debt: 1`, `duplicate_logic: 15`
* *Architecture:* `io: 1`, `api: 31`, `concurrency: 3`, `import: 23`
* *Defense:* `safety: 133`, `doc: 26`, `test: 28`, `immutability_locks: 1`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.629
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` httparse::ParserConfig, super::io::Buffered, http::header::HeaderValue, ClientTransaction, std::marker::PhantomData, std::io, CONNECTION, crate::rt::Sleep...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/client.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.445 IQR)
- **Top Global Matches:** file_cluster_4: 11.445, file_cluster_8: 11.782, file_cluster_0: 11.883
- **Magnitude:** 567.46 | **LOC:** 2930 | **CtrlFlow:** 11.8% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (34.0188%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `client_100_then_http09` (Impact: 12.6)
  * `http2_detect_conn_eof` (Impact: 9.2)
  * `connect_method` (Impact: 7.9)
  * `upgrade` (Impact: 7.7)
  * `http2_connect_detect_close` (Impact: 7.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 374`, `args: 79`, `func_start: 31`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 123`, `high_risk_execution: 3`, `state_mutation: 116`, `dead_code: 4`, `duplicate_logic: 4`, `orphaned_logic: 11`
* *Architecture:* `io: 40`, `concurrency: 301`, `import: 27`
* *Defense:* `safety: 71`, `doc: 2`, `test: 44`, `immutability_locks: 4`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.629
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Full, hyper::Method, std::io::Read, FutureExt, TryFuture, std::sync::atomic::AtomicUsize, std::convert::Infallible, hyper::service::service_fn...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/proto/h1/io.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.909 IQR)
- **Top Global Matches:** file_cluster_0: 12.909, file_cluster_11: 13.154, file_cluster_13: 13.2
- **Magnitude:** 534.18 | **LOC:** 968 | **CtrlFlow:** 28.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (33.4403%), Tech Debt (99.9245%)
**Top Internal Functions/Classes:**
  * `poll_flush` (Impact: 112.0)
  * `parse` (Impact: 20.6)
  * `record` (Impact: 15.5)
  * `consume_leading_lines` (Impact: 10.6)
  * `read_mem` (Impact: 9.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 166`, `args: 60`, `func_start: 57`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 125`, `dead_code: 8`, `planned_debt: 4`, `duplicate_logic: 17`
* *Architecture:* `io: 1`, `api: 48`, `concurrency: 11`, `import: 14`
* *Defense:* `safety: 40`, `doc: 25`, `test: 46`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.629
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` BufMut, ParsedMessage, crate::common::buf::BufList, test::Bencher, bytes::Buf, Poll, IoSlice, super::*...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/proto/h2/client.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.309 IQR)
- **Top Global Matches:** file_cluster_4: 13.309, file_cluster_13: 13.406, file_cluster_16: 13.406
- **Magnitude:** 399.96 | **LOC:** 792 | **CtrlFlow:** 28.7% | **Authorship Centralization:** 25.0%
- **Risk Profile:** Cognitive Load (69.1283%), Tech Debt (87.9774%)
**Top Internal Functions/Classes:**
  * `poll` (Impact: 50.9)
  * `poll_pipe` (Impact: 14.7)
  * `new_builder` (Impact: 13.3)
  * `poll` (Impact: 13.0)
  * `handshake` (Impact: 12.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 164`, `args: 23`, `func_start: 17`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 85`, `dead_code: 1`, `fragile_debt: 1`, `duplicate_logic: 6`, `orphaned_logic: 2`
* *Architecture:* `api: 26`, `concurrency: 118`, `import: 24`
* *Defense:* `safety: 120`, `doc: 5`, `immutability_locks: 16`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.629
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` h2::client::ResponseFuture, SendWhen, crate::body::Body, future::Future, task::Context, TrySendError, SendBuf, futures_channel::mpsc::Receiver...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/client/dispatch.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.148 IQR)
- **Top Global Matches:** file_cluster_0: 14.148, file_cluster_4: 14.168, file_cluster_13: 14.427
- **Magnitude:** 389.64 | **LOC:** 528 | **CtrlFlow:** 17.3% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (45.9237%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `giver_queue_throughput` (Impact: 12.3)
  * `drop` (Impact: 8.8)
  * `can_send` (Impact: 8.7)
  * `poll` (Impact: 6.8)
  * `dispatch_gone` (Impact: 5.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 163`, `args: 50`, `func_start: 36`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 120`, `dead_code: 3`, `fragile_debt: 1`, `duplicate_logic: 15`, `orphaned_logic: 10`
* *Architecture:* `api: 33`, `concurrency: 96`, `import: 12`
* *Defense:* `safety: 67`, `doc: 36`, `test: 8`, `immutability_locks: 2`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.629
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Poll, tokio::sync::mpsc, std::pin::Pin, crate::body::Incoming, pin::Pin, pin_project_lite::pin_project, http::Request, std::task::Context...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/client/conn/http2.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.712 IQR)
- **Top Global Matches:** file_cluster_16: 13.712, file_cluster_4: 13.822, file_cluster_13: 13.894
- **Magnitude:** 381.28 | **LOC:** 712 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 25.0%
- **Risk Profile:** Cognitive Load (48.5908%), Tech Debt (99.9927%)
**Top Internal Functions/Classes:**
  * `send_request` (Impact: 7.2)
    * *Intent:* /// Sends a `Request` on the associated connection. /// /// Returns a future that if successful, yie...
  * `poll_ready` (Impact: 5.5)
    * *Intent:* /// Polls to determine whether this sender can be used yet for a request. /// /// If the associated ...
  * `poll` (Impact: 5.5)
    * *Intent:* /// Returns the current maximum receive stream count. /// /// This setting is configured in a [`SETT...
  * `handshake` (Impact: 5.5)
  * `send_not_sync_executor_of_send_futures` (Impact: 5.3)
    * *Intent:* #[tokio::test] #[ignore] // only compilation is checked
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 150`, `args: 47`, `func_start: 46`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 70`, `fragile_debt: 2`, `duplicate_logic: 14`
* *Architecture:* `api: 40`, `concurrency: 121`, `import: 19`
* *Defense:* `safety: 51`, `doc: 187`, `test: 7`, `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.629
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::body::Body, crate::proto, TrySendError, http::Request, std::marker::PhantomData, super::super::dispatch::self, crate::rt::Timer, Response...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/body/incoming.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.26 IQR)
- **Top Global Matches:** file_cluster_0: 13.26, file_cluster_4: 13.329, file_cluster_13: 13.551
- **Magnitude:** 334.04 | **LOC:** 633 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (48.4012%), Tech Debt (45.3836%)
**Top Internal Functions/Classes:**
  * `new_channel` (Impact: 29.9)
    * *Intent:* /// Create a `Body` stream with an associated sender half. /// /// Useful when wanting to stream chu...
  * `size_hint` (Impact: 8.1)
  * `opt_len` (Impact: 6.5)
  * `eq` (Impact: 6.2)
  * `channel_notices_closure` (Impact: 6.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 118`, `args: 31`, `func_start: 26`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 4`, `state_mutation: 64`, `dead_code: 1`, `duplicate_logic: 4`
* *Architecture:* `api: 22`, `concurrency: 115`, `import: 18`
* *Defense:* `safety: 77`, `doc: 46`, `test: 32`, `immutability_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.629
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` futures_core::stream::FusedStream, std::mem, super::Body, http_body::Body, Poll, http::HeaderMap, Frame, super::DecodedLength...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/support/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 10.514 IQR)
- **Top Global Matches:** file_cluster_4: 10.514, file_cluster_8: 10.935, file_cluster_0: 11.017
- **Magnitude:** 329.58 | **LOC:** 594 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.9168%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `async_test` (Impact: 42.0)
  * `naive_proxy` (Impact: 26.9)
  * `__run_test` (Impact: 2.2)
  * `default` (Impact: 2.1)
  * `default` (Impact: 2.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 152`, `args: 15`, `func_start: 6`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 31`, `state_mutation: 39`, `duplicate_logic: 2`
* *Architecture:* `io: 19`, `api: 34`, `concurrency: 169`, `import: 13`
* *Defense:* `safety: 34`, `test: 14`, `sync_locks: 4`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.629
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Full, hyper::body::Incoming, tokiort::TokioExecutor, hyper::service::service_fn, FutureExt, Request, TcpStream, Response...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/single_threaded.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.473 IQR)
- **Top Global Matches:** file_cluster_4: 12.473, file_cluster_13: 12.894, file_cluster_11: 13.114
- **Magnitude:** 321.88 | **LOC:** 384 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (64.1918%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `http1_client` (Impact: 22.8)
  * `http2_client` (Impact: 22.8)
  * `main` (Impact: 18.9)
  * `http2_server` (Impact: 10.9)
  * `http1_server` (Impact: 10.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 173`, `args: 20`, `func_start: 13`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 38`, `state_mutation: 50`, `orphaned_logic: 3`
* *Architecture:* `io: 24`, `concurrency: 163`, `import: 19`
* *Defense:* `safety: 40`, `doc: 11`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.629
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` hyper::service::service_fn, AsyncWriteExt, std::marker::PhantomData, Response, Poll, hyper::body::Body, std::rc::Rc, hyper::Request...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/client/conn/http1.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_16` (Drift: 14.705 IQR)
- **Top Global Matches:** file_cluster_16: 14.705, file_cluster_4: 14.751, file_cluster_13: 14.815
- **Magnitude:** 292.62 | **LOC:** 612 | **CtrlFlow:** 19.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.6632%), Tech Debt (99.9964%)
**Top Internal Functions/Classes:**
  * `poll` (Impact: 37.6)
  * `handshake` (Impact: 24.8)
    * *Intent:* /// Set whether HTTP/1 connections will silently ignored malformed header lines. ///
  * `send_request` (Impact: 7.2)
    * *Intent:* /// Returns a future that if successful, yields the `Response`. /// /// `req` must have a `Host` hea...
  * `poll` (Impact: 4.0)
    * *Intent:* /// Sets the exact size of the read buffer to *always* use.
  * `without_shutdown` (Impact: 3.9)
    * *Intent:* /// Prevent shutdown of the underlying IO object at the end of service the request, /// instead run ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 101`, `args: 25`, `func_start: 23`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 52`, `fragile_debt: 2`, `duplicate_logic: 6`, `orphaned_logic: 8`
* *Architecture:* `api: 27`, `concurrency: 95`, `import: 15`
* *Defense:* `safety: 64`, `doc: 214`, `test: 1`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.629
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` httparse::ParserConfig, crate::body::Body, crate::proto, TrySendError, http::Request, super::super::dispatch::self, Response, crate::upgrade::Upgraded...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `capi/examples/client.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.041 IQR)
- **Local Micro-Species:** `Cluster 0: Defensive Downstream Logic & Immutable State` (Drift: 6.684 IQR)
- **Top Global Matches:** file_cluster_13: 13.041, file_cluster_8: 13.32, file_cluster_0: 13.416
- **Magnitude:** 290.9 | **LOC:** 344 | **CtrlFlow:** 53.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.3989%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 65.5)
    * *Intent:* #define STR_ARG(XX) (uint8_t *)XX, strlen(XX)
  * `connect_to` (Impact: 19.1)
  * `read_cb` (Impact: 9.9)
  * `write_cb` (Impact: 9.9)
  * `free_conn_data` (Impact: 6.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 41`, `args: 7`, `func_start: 7`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 107`, `orphaned_logic: 1`
* *Architecture:* `io: 11`, `api: 63`, `import: 12`
* *Defense:* `safety: 13`, `test: 3`, `immutability_locks: 12`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.629
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` socket.h, stdio.h, netdb.h, unistd.h, stdlib.h, select.h, string.h, errno.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/proto/h2/server.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.684 IQR)
- **Top Global Matches:** file_cluster_4: 12.684, file_cluster_13: 12.802, file_cluster_16: 12.926
- **Magnitude:** 290.28 | **LOC:** 551 | **CtrlFlow:** 23.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (75.7069%), Tech Debt (44.4703%)
**Top Internal Functions/Classes:**
  * `poll_server` (Impact: 25.6)
  * `new` (Impact: 23.8)
  * `poll` (Impact: 17.3)
  * `poll2` (Impact: 14.5)
  * `graceful_shutdown` (Impact: 6.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 124`, `args: 12`, `func_start: 9`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 75`, `dead_code: 1`, `duplicate_logic: 4`
* *Architecture:* `api: 18`, `concurrency: 85`, `import: 25`
* *Defense:* `safety: 67`, `test: 2`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.629
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::Response, Pending, crate::body::Body, SendBuf, Request, crate::headers, super::ping, crate::proto::Dispatched...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `capi/examples/upload.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.794 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 6.525 IQR)
- **Top Global Matches:** file_cluster_13: 12.794, file_cluster_8: 13.053, file_cluster_0: 13.179
- **Magnitude:** 274.72 | **LOC:** 401 | **CtrlFlow:** 46.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (68.5949%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 42.3)
    * *Intent:* #define STR_ARG(XX) (uint8_t *)XX, strlen(XX)
  * `connect_to` (Impact: 19.1)
  * `read_cb` (Impact: 9.9)
  * `write_cb` (Impact: 9.9)
  * `poll_req_upload` (Impact: 7.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 50`, `args: 8`, `func_start: 8`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 107`, `orphaned_logic: 1`
* *Architecture:* `io: 13`, `api: 63`, `import: 12`
* *Defense:* `safety: 10`, `test: 2`, `immutability_locks: 10`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.629
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` socket.h, stdio.h, netdb.h, unistd.h, stdlib.h, select.h, string.h, errno.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `benches/end_to_end.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.591 IQR)
- **Top Global Matches:** file_cluster_4: 11.591, file_cluster_0: 11.695, file_cluster_8: 11.928
- **Magnitude:** 259.14 | **LOC:** 452 | **CtrlFlow:** 15.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (91.4112%), Tech Debt (99.4252%)
**Top Internal Functions/Classes:**
  * `bench` (Impact: 38.8)
  * `spawn_server` (Impact: 12.8)
  * `http2_parallel_x10_req_10mb` (Impact: 2.8)
  * `http2_parallel_x10_req_10kb_100_chunks_a` (Impact: 2.8)
  * `http2_parallel_x10_req_10kb_100_chunks_m` (Impact: 2.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 130`, `args: 39`, `func_start: 31`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 12`, `high_risk_execution: 1`, `state_mutation: 54`, `planned_debt: 2`, `orphaned_logic: 19`
* *Architecture:* `io: 16`, `concurrency: 75`, `import: 11`
* *Defense:* `safety: 26`, `test: 6`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.629
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` hyper::Method, http_body_util::Full, hyper::service::service_fn, http_body_util::BodyExt, std::convert::Infallible, futures_util::SinkExt, hyper::body::Frame, Request...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/server/conn/http1.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_4` (Drift: 15.87 IQR)
- **Top Global Matches:** file_cluster_4: 15.87, file_cluster_13: 15.992, file_cluster_16: 16.184
- **Magnitude:** 246.58 | **LOC:** 560 | **CtrlFlow:** 28.3% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (49.8917%), Tech Debt (98.8454%)
**Top Internal Functions/Classes:**
  * `poll` (Impact: 49.6)
    * *Intent:* /// Start a graceful shutdown process for this connection. /// /// This `Connection` should continue...
  * `graceful_shutdown` (Impact: 7.7)
  * `poll` (Impact: 7.7)
    * *Intent:* /// Set whether to support preserving original header cases. /// /// Currently, this will record the...
  * `without_shutdown` (Impact: 3.8)
    * *Intent:* /// A buffer of bytes that have been read but not processed as HTTP. /// /// If the client sent addi...
  * `graceful_shutdown` (Impact: 2.6)
    * *Intent:* /// A configuration builder for HTTP/1 server connections. /// /// **Note**: The default values of o...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 76`, `args: 17`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 48`, `dead_code: 5`, `duplicate_logic: 6`, `orphaned_logic: 3`
* *Architecture:* `io: 3`, `api: 14`, `concurrency: 90`, `import: 19`
* *Defense:* `safety: 48`, `doc: 208`, `test: 1`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.629
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` hyper::body::Incoming, crate::body::Body, crate::proto, Request, Response, crate::upgrade::Upgraded, Poll, Time...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/proto/h1/encode.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.397 IQR)
- **Top Global Matches:** file_cluster_0: 11.397, file_cluster_8: 11.525, file_cluster_13: 11.574
- **Magnitude:** 233.94 | **LOC:** 673 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (15.7555%), Tech Debt (99.3278%)
**Top Internal Functions/Classes:**
  * `encode_trailers` (Impact: 29.6)
  * `encode` (Impact: 8.6)
  * `encode_and_end` (Impact: 8.2)
  * `end` (Impact: 4.0)
  * `remaining` (Impact: 4.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 159`, `args: 43`, `func_start: 38`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 58`, `duplicate_logic: 17`
* *Architecture:* `io: 2`, `api: 27`, `import: 15`
* *Defense:* `safety: 38`, `doc: 9`, `test: 33`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.629
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` write_headers_title_case, CONTENT_ENCODING, http::
    header::
        AUTHORIZATION, super::io::WriteBuf, http::
        header::
            AUTHORIZATION, std::collections::HashSet, std::io::Write, std::cmp::Ordering...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ffi/http_types.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.361 IQR)
- **Top Global Matches:** file_cluster_13: 13.361, file_cluster_8: 13.434, file_cluster_0: 13.578
- **Magnitude:** 229.58 | **LOC:** 707 | **CtrlFlow:** 16.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (18.616%), Tech Debt (99.7908%)
**Top Internal Functions/Classes:**
  * `hyper_headers_foreach` (Impact: 30.9)
  * `hyper_request_set_uri_parts` (Impact: 16.1)
    * *Intent:* /// An HTTP response. /// /// Obtain one of these by making a request with `hyper_clientconn_send`, ...
  * `raw_name_value` (Impact: 8.3)
  * `reason_phrase` (Impact: 5.7)
  * `hyper_headers_set` (Impact: 5.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 149`, `args: 29`, `func_start: 28`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 78`, `planned_debt: 1`, `duplicate_logic: 2`, `orphaned_logic: 19`
* *Architecture:* `api: 3`, `import: 13`
* *Defense:* `safety: 42`, `doc: 159`, `test: 5`, `immutability_locks: 22`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.629
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::ffi::size_t, Request, AsTaskType, Response, crate::HeaderMap, crate::header::HeaderName, super::error::hyper_code, super::task::hyper_task_return_type...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ffi/task.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_16` (Drift: 15.392 IQR)
- **Top Global Matches:** file_cluster_16: 15.392, file_cluster_13: 15.42, file_cluster_4: 15.473
- **Magnitude:** 179.0 | **LOC:** 550 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.7534%), Tech Debt (84.1131%)
**Top Internal Functions/Classes:**
  * `hyper_task_type` (Impact: 17.7)
  * `hyper_task_value` (Impact: 11.9)
    * *Intent:* /// drain_queue locks both self.spawn_queue and self.driver, so it requires
  * `hyper_executor_poll` (Impact: 4.8)
  * `poll` (Impact: 4.0)
  * `output_type` (Impact: 3.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 61`, `args: 18`, `func_start: 18`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 44`, `duplicate_logic: 3`
* *Architecture:* `api: 20`, `concurrency: 36`, `import: 9`
* *Defense:* `safety: 46`, `doc: 188`, `sync_locks: 3`, `immutability_locks: 11`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.629
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Poll, Weak, std::pin::Pin, futures_util::stream::FuturesUnordered, super::error::hyper_code, std::sync::
    atomic::AtomicBool, Arc, std::task::Context...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/server/conn/http2.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.033 IQR)
- **Top Global Matches:** file_cluster_13: 14.033, file_cluster_16: 14.071, file_cluster_4: 14.197
- **Magnitude:** 178.88 | **LOC:** 313 | **CtrlFlow:** 19.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.3913%), Tech Debt (9.1531%)
**Top Internal Functions/Classes:**
  * `poll` (Impact: 4.0)
  * `adaptive_window` (Impact: 4.0)
    * *Intent:* /// Sets the [`SETTINGS_INITIAL_WINDOW_SIZE`][spec] option for HTTP2 /// stream-level flow control. ...
  * `initial_stream_window_size` (Impact: 3.8)
  * `initial_connection_window_size` (Impact: 3.8)
    * *Intent:* /// Configures the maximum number of local reset streams allowed before a GOAWAY will be sent. /// /...
  * `max_frame_size` (Impact: 3.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 80`, `args: 18`, `func_start: 18`
* *Risk/State:* `state_mutation: 58`, `planned_debt: 1`
* *Architecture:* `api: 20`, `concurrency: 49`, `import: 20`
* *Defense:* `safety: 33`, `doc: 108`, `test: 1`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.629
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::body::Body, crate::proto, Poll, pin_project_lite::pin_project, std::future::Future, futures_core::ready, std::pin::Pin, crate::rt::Read...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `benches/server.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.885 IQR)
- **Top Global Matches:** file_cluster_4: 11.885, file_cluster_13: 12.167, file_cluster_0: 12.215
- **Magnitude:** 177.9 | **LOC:** 228 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (95.5714%), Tech Debt (83.2376%)
**Top Internal Functions/Classes:**
  * `raw_tcp_throughput_large_payload` (Impact: 17.9)
  * `raw_tcp_throughput_small_payload` (Impact: 10.8)
  * `throughput_fixedsize_many_chunks` (Impact: 4.9)
  * `throughput_chunked_many_chunks` (Impact: 4.9)
  * `throughput_fixedsize_large_payload` (Impact: 4.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 84`, `args: 24`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 70`, `orphaned_logic: 8`
* *Architecture:* `io: 8`, `concurrency: 44`, `import: 12`
* *Defense:* `safety: 4`, `test: 3`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.629
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` TcpListener, std::sync::mpsc, Full, std::io::Read, hyper::service::service_fn, http_body_util::BodyExt, std::time::Duration, hyper::body::Frame...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/error.rs` (RUST | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.719 IQR)
- **Top Global Matches:** file_cluster_0: 10.719, file_cluster_8: 10.963, file_cluster_16: 11.138
- **Magnitude:** 163.28 | **LOC:** 703 | **CtrlFlow:** 29.5% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (4.4633%), Tech Debt (99.9752%)
**Top Internal Functions/Classes:**
  * `new_h2` (Impact: 6.4)
  * `description` (Impact: 6.0)
    * *Intent:* // Find an h2::Reason somewhere in the cause stack, if it exists, // otherwise assume an INTERNAL_ER...
  * `from` (Impact: 4.5)
  * `fmt` (Impact: 3.9)
  * `assert_send_sync` (Impact: 2.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 43`, `args: 48`, `func_start: 45`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 11`, `duplicate_logic: 9`, `orphaned_logic: 26`
* *Architecture:* `io: 3`, `api: 33`, `concurrency: 4`, `import: 4`
* *Defense:* `safety: 19`, `doc: 75`, `test: 10`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.629
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::error::Error, super::*, std::fmt, std::mem
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/client/dispatch.rs` (RUST) | Magnitude: 389.64 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 359, structural_boundaries: 163, state_mutation: 120, concurrency: 96
- `src/proto/mod.rs` (RUST) | Magnitude: 20.06 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 24, api: 16, encapsulation: 16, structural_boundaries: 14
- `examples/hello-http2.rs` (RUST) | Magnitude: 43.14 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 37, structural_boundaries: 19, branch: 13, concurrency: 12
- `src/proto/h2/ping.rs` (RUST) | Magnitude: 137.34 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 158, structural_boundaries: 53, state_mutation: 50, doc: 44
- `benches/support/tokiort.rs` (RUST) | Magnitude: 113.3 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 146, structural_boundaries: 63, generics: 55, state_mutation: 37

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `src/proto/h2/upgrade.rs` (RUST) | Magnitude: 159.7 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 203, safety: 83, structural_boundaries: 64, state_mutation: 61
- `src/common/task.rs` (RUST) | Magnitude: 24.2 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 16, doc: 7, pointers: 7, structural_boundaries: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `examples/params.rs` (RUST) | Magnitude: 53.12 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 80, structural_boundaries: 44, safety: 25, branch: 16
- `src/proto/h1/mod.rs` (RUST) | Magnitude: 35.02 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 55, structural_boundaries: 34, generics: 23, api: 13
- `src/ffi/io.rs` (RUST) | Magnitude: 83.02 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: doc: 69, indent_spaces: 60, structural_boundaries: 43, state_mutation: 29
- `src/server/conn/http2.rs` (RUST) | Magnitude: 178.88 | Delta: **0.038 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 216, doc: 108, structural_boundaries: 80, state_mutation: 58
- `src/ffi/body.rs` (RUST) | Magnitude: 105.56 | Delta: **0.064 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: doc: 124, indent_spaces: 92, structural_boundaries: 53, pointers: 36

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `src/ffi/task.rs` (RUST) | Magnitude: 179.0 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 188, indent_spaces: 119, structural_boundaries: 61, safety: 46
- `src/client/conn/http1.rs` (RUST) | Magnitude: 292.62 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 237, doc: 214, structural_boundaries: 101, concurrency: 95
- `src/rt/timer.rs` (RUST) | Magnitude: 61.68 | Delta: **0.102 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: doc: 73, indent_spaces: 44, state_mutation: 19, concurrency: 19
- `src/client/conn/http2.rs` (RUST) | Magnitude: 381.28 | Delta: **0.11 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 401, doc: 187, structural_boundaries: 150, generics: 122
- `src/common/future.rs` (RUST) | Magnitude: 27.08 | Delta: **0.143 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: generics: 15, structural_boundaries: 12, concurrency: 12, indent_spaces: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `capi/gen_header.sh` (SHELL) | Magnitude: 53.72 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 25, indent_spaces: 22, state_mutation: 18, io: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/proto/h1/dispatch.rs` (RUST) | Magnitude: 796.4 | Delta: **0.038 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 633, structural_boundaries: 199, safety: 150, state_mutation: 125
- `tests/support/trailers.rs` (RUST) | Magnitude: 47.2 | Delta: **0.053 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 48, structural_boundaries: 20, safety: 19, concurrency: 19
- `src/service/service.rs` (RUST) | Magnitude: 40.44 | Delta: **0.073 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: doc: 46, indent_spaces: 36, concurrency: 26, structural_boundaries: 23
- `src/proto/h2/client.rs` (RUST) | Magnitude: 399.96 | Delta: **0.097 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 509, structural_boundaries: 164, generics: 127, safety: 120
- `benches/end_to_end.rs` (RUST) | Magnitude: 259.14 | Delta: **0.104 IQR** | Secondary Pull: `file_cluster_0`
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
- `src/common/mod.rs` (RUST) | Magnitude: 23.42 | Delta: **0.339 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 8, api: 8, encapsulation: 8, decorators: 7
- `src/ffi/macros.rs` (RUST) | Magnitude: 18.96 | Delta: **0.564 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 44, safety: 7, pointers: 6, structural_boundaries: 5
- `examples/send_file_index.html` (HTML) | Magnitude: 15.2 | Delta: **0.82 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 4, io: 4, doc: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/client/conn/http2.rs` -> Churn: **100.0%** | Cog Load: 48.5908% | Debt: 99.9927%
- `src/proto/h2/client.rs` -> Churn: **100.0%** | Cog Load: 69.1283% | Debt: 87.9774%
- `src/proto/h2/mod.rs` -> Churn: **86.14%** | Cog Load: 65.8955% | Debt: 73.0371%
- `src/client/dispatch.rs` -> Churn: **68.26%** | Cog Load: 45.9237% | Debt: 100.0%
- `src/proto/h1/conn.rs` -> Churn: **68.26%** | Cog Load: 34.363% | Debt: 99.2994%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/proto/h1/decode.rs` -> **Sean McArthur** (100.0% isolated ownership) | Magnitude: 781.58
- `src/body/incoming.rs` -> **Sean McArthur** (100.0% isolated ownership) | Magnitude: 334.04
- `src/proto/h2/server.rs` -> **Sean McArthur** (100.0% isolated ownership) | Magnitude: 290.28
- `src/proto/h1/encode.rs` -> **HueCodes** (100.0% isolated ownership) | Magnitude: 233.94
- `src/ffi/http_types.rs` -> **Dhruva D** (100.0% isolated ownership) | Magnitude: 229.58

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/service/http.rs` -> **Severity: 0.323** (Embedded: 0.0098 * Error Risk: 32.9353%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/common/time.rs` -> **Severity: 962.9** (Blast Radius: 9.629 * Doc Risk: 100.0%)
- `src/common/mod.rs` -> **Severity: 960.007** (Blast Radius: 9.629 * Doc Risk: 99.6996%)
- `src/proto/mod.rs` -> **Severity: 955.561** (Blast Radius: 9.629 * Doc Risk: 99.2378%)
- `src/proto/h1/mod.rs` -> **Severity: 879.443** (Blast Radius: 9.629 * Doc Risk: 91.3327%)
- `src/common/future.rs` -> **Severity: 795.884** (Blast Radius: 9.629 * Doc Risk: 82.6549%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
