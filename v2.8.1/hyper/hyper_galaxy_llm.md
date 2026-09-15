# ARCHITECTURAL_BRIEF: hyper
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/hyperium/hyper.git` |
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
| Total Artifacts | 130 |
| Analyzed Artifacts (Scanned) | 103 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 27 |
| Total LOC | 24426 |
| Volatility Index | 0.049 |
| % Scanned of codebase = | 79.2% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2266 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 1 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUST | 92 | 23822 | 89.3% |
| MARKDOWN | 6 | 0 | 5.8% |
| C | 2 | 538 | 1.9% |
| MAKEFILE | 1 | 15 | 1.0% |
| SHELL | 1 | 41 | 1.0% |
| HTML | 1 | 10 | 1.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Small Flat Repo` (z +0.04; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules 26%, Generic / Templated Code Files 22%, Data / Markup / Trivial 17%, Annotated Framework Methods Files 12%, Declarative / Non-Code 7%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 97 | 94.2% |

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
- `.toml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.toml), 1x Excluded (Unsupported Extension: '.toml')
- `.h`: 1x Excluded (Machine-Generated Source Code Signature: 545 LOC)
- `.svg`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 83.9 | 20.9 | 13.2 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 98.6 | 36.3 | 45.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 32.3 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 20.9 | 2.4 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 60.8 | 14.2 | 6.9 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 49.7 | 53.3 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 17.9 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 7.5 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 81.1 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 3.3 | 0.6 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 10.4 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 56.0 | 50.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1421 | 76 | 37 | `capi/examples/upload.c` |
| cleanup | 60 | 17 | 2 | `tests/server.rs` |
| guards | 874 | 74 | 28 | `src/proto/h1/role.rs` |
| danger | 1193 | 50 | 15 | `tests/server.rs` |
| concurrency | 1545 | 62 | 29 | `tests/server.rs` |
| connectivity | 875 | 84 | 26 | `src/error.rs` |
| io | 444 | 41 | 13 | `tests/server.rs` |
| crypto | 0 | 0 | 0 | - |
| ipc | 23 | 10 | 0 | `tests/server.rs` |
| time | 16 | 14 | 1 | `src/proto/h1/dispatch.rs` |
| serialization | 2 | 1 | 0 | `examples/web_api.rs` |
| regex | 0 | 0 | 0 | - |
| events | 262 | 26 | 10 | `src/proto/h1/conn.rs` |
| tests | 805 | 35 | 14 | `tests/server.rs` |
| docs | 2657 | 60 | 86 | `src/client/conn/http1.rs` |
| debt | 189 | 51 | 5 | `capi/examples/upload.c` |
| mutation | 3031 | 79 | 59 | `tests/server.rs` |
| dead_code | 502 | 50 | 15 | `tests/server.rs` |
| credential | 0 | 0 | 0 | - |
| threat | 148 | 34 | 6 | `tests/client.rs` |
| ml_ai | 8 | 2 | 0 | `src/proto/h2/ping.rs` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tests/server.rs` (Hits: 63)
- `tests/client.rs` (Hits: 60)
- `benches/support/tokiort.rs` (Hits: 26)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **CONTRIBUTING.md** (`CONTRIBUTING.md`) — 1 inbound connections
2. **client_json.rs** (`examples/client_json.rs`) — 1 inbound connections
3. **echo.rs** (`examples/echo.rs`) — 1 inbound connections
4. **gateway.rs** (`examples/gateway.rs`) — 1 inbound connections
5. **graceful_shutdown.rs** (`examples/graceful_shutdown.rs`) — 1 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **client.rs** (`tests/client.rs`) — 70 outbound dependencies
2. **server.rs** (`tests/server.rs`) — 66 outbound dependencies
3. **conn.rs** (`src/proto/h1/conn.rs`) — 57 outbound dependencies
4. **client.rs** (`src/proto/h2/client.rs`) — 47 outbound dependencies
5. **role.rs** (`src/proto/h1/role.rs`) — 39 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `encode_headers` **(Many-Argument Workhorses)** (@ `src/proto/h1/role.rs`) -> Impact: **183.9** | LOC: 344
- `parse` **(Many-Argument Workhorses)** (@ `src/proto/h1/role.rs`) -> Impact: **75.3** | LOC: 225
- `poll_write` **(Compute Cores)** (@ `src/proto/h1/dispatch.rs`) -> Impact: **72.2** | LOC: 94
- `parse` **(Many-Argument Workhorses)** (@ `src/proto/h1/role.rs`) -> Impact: **65.6** | LOC: 169
- `main` **(Many-Argument Workhorses)** (@ `capi/examples/upload.c`) -> Impact: **60.2** | LOC: 234
  * *Intent:* #define STR_ARG(XX) (uint8_t *)XX, strlen(XX)
- `main` **(Many-Argument Workhorses)** (@ `capi/examples/client.c`) -> Impact: **53.4** | LOC: 202
  * *Intent:* #define STR_ARG(XX) (uint8_t *)XX, strlen(XX)
- `poll` **(Many-Argument Workhorses)** (@ `src/proto/h2/client.rs`) -> Impact: **50.9** | LOC: 118
- `set_length` **(Many-Argument Workhorses)** (@ `src/proto/h1/role.rs`) -> Impact: **48.2** | LOC: 132
- `poll_read` **(Compute Cores)** (@ `src/proto/h1/dispatch.rs`) -> Impact: **41.9** | LOC: 75
- `encode` **(Many-Argument Workhorses)** (@ `src/proto/h1/role.rs`) -> Impact: **41.4** | LOC: 101

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src/proto/h1` | 7 | 3240.92 | 21.94% | 36.69% |
| `tests` | 3 | 1492.52 | 9.44% | 0.0% |
| `src/proto/h2` | 5 | 864.14 | 18.35% | 26.33% |
| `examples` | 18 | 725.38 | 46.77% | 0.0% |
| `src/ffi` | 8 | 562.12 | 9.45% | 42.15% |
| `src/client/conn` | 3 | 481.6 | 21.69% | 66.14% |
| `src` | 7 | 427.0 | 4.16% | 50.79% |
| `tests/support` | 3 | 337.08 | 20.9% | 0.0% |
| `capi/examples` | 3 | 332.46 | 21.93% | 0.0% |
| `src/server/conn` | 3 | 317.54 | 24.8% | 26.07% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/service/service.rs` -> **100.0%** Exposure
- `src/proto/h1/mod.rs` -> **99.9961%** Exposure
- `src/common/io/rewind.rs` -> **99.9939%** Exposure
- `src/ffi/error.rs` -> **99.9665%** Exposure
- `src/ext/h1_reason_phrase.rs` -> **99.9503%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `src/common/buf.rs` -> **100.0%** Exposure
- `capi/gen_header.sh` -> **99.9994%** Exposure
- `src/server/conn/http2.rs` -> **99.5958%** Exposure
- `src/proto/h2/ping.rs` -> **98.1937%** Exposure
- `src/ext/mod.rs` -> **97.2279%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tests/server.rs` -> **91** Orphaned Functions | **3** Duplicates
- `src/proto/h1/role.rs` -> **36** Orphaned Functions | **2** Duplicates
- `src/error.rs` -> **36** Orphaned Functions | **0** Duplicates
- `src/ffi/http_types.rs` -> **22** Orphaned Functions | **2** Duplicates
- `benches/end_to_end.rs` -> **19** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `1321` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/client/conn/http2.rs` (RUST) -> Cumulative Risk: **743.69**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.71)
- **Magnitude:** 291.22 | **LOC:** 712 | **CtrlFlow:** 4.9% | **Authorship Centralization:** 25.0%
- **Primary Risk Drivers:** Churn (100.0%), Concurrency (99.9993%), Tech Debt (98.7807%), Spec Match (96.3636%)
- **Heaviest Functions:** `try_send_request` (Generic / Templated Code, Impact: 6.4), `send_request` (Generic / Templated Code, Impact: 6.3), `poll_ready` (Generic / Templated Code, Impact: 5.5)

### 2. `src/proto/h1/decode.rs` (RUST) -> Cumulative Risk: **652.71**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.65)
- **Magnitude:** 557.74 | **LOC:** 1255 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9765%), State Flux (82.0231%)
- **Heaviest Functions:** `decode` (Many-Argument Workhorses, Impact: 41.1), `read_body` (Many-Argument Workhorses, Impact: 17.4), `test_read_chunk_size` (Tests & Verification, Impact: 16.8)

### 3. `src/proto/h2/mod.rs` (RUST) -> Cumulative Risk: **625.88**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.71)
- **Magnitude:** 112.96 | **LOC:** 265 | **CtrlFlow:** 15.0% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Churn (86.14%), Verification (80.0%)
- **Heaviest Functions:** `poll` (Defensive Guards, Impact: 33.1), `strip_connection_headers` (Defensive Guards, Impact: 19.2), `advance` (Defensive Guards, Impact: 3.9)

### 4. `src/client/dispatch.rs` (RUST) -> Cumulative Risk: **619.54**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.68)
- **Magnitude:** 172.6 | **LOC:** 528 | **CtrlFlow:** 8.1% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (92.4142%), Concurrency (87.0679%), Documentation (86.4407%)
- **Heaviest Functions:** `giver_queue_throughput` (Annotated Framework Methods, Impact: 8.2), `poll` (Compute Cores, Impact: 6.8), `drop` (Defensive Guards, Impact: 6.5)

### 5. `src/proto/h2/client.rs` (RUST) -> Cumulative Risk: **600.25**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.37)
- **Magnitude:** 247.58 | **LOC:** 792 | **CtrlFlow:** 10.1% | **Authorship Centralization:** 25.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Churn (100.0%), Documentation (93.75%), Concurrency (93.3666%)
- **Heaviest Functions:** `poll` (Many-Argument Workhorses, Impact: 50.9), `poll` (Defensive Guards, Impact: 13.0), `poll_pipe` (Many-Argument Workhorses, Impact: 12.7)

### 6. `benches/server.rs` (RUST) -> Cumulative Risk: **589.0**
- **Archetype:** `file_cluster_15` (Distance: N/A IQR)
- **Composition Archetype:** `Annotated Framework Methods Files` (z +2.00)
- **Magnitude:** 84.0 | **LOC:** 228 | **CtrlFlow:** 9.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.8804%), Safety Score (96.4189%)
- **Heaviest Functions:** `raw_tcp_throughput_large_payload` (Compute Cores, Impact: 12.1), `raw_tcp_throughput_small_payload` (Callbacks & Closures, Impact: 7.5), `throughput_fixedsize_many_chunks` (Callbacks & Closures, Impact: 3.3)

### 7. `benches/end_to_end.rs` (RUST) -> Cumulative Risk: **586.41**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Annotated Framework Methods Files` (z +0.46)
- **Magnitude:** 151.14 | **LOC:** 452 | **CtrlFlow:** 5.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.4252%), Concurrency (94.2468%)
- **Heaviest Functions:** `bench` (Many-Argument Workhorses, Impact: 38.8), `spawn_server` (Defensive Guards, Impact: 12.8), `request_chunks` (Generic / Templated Code, Impact: 2.3)

### 8. `src/proto/h1/conn.rs` (RUST) -> Cumulative Risk: **573.24**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.47)
- **Magnitude:** 562.8 | **LOC:** 1532 | **CtrlFlow:** 14.5% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (98.4127%), State Flux (88.7028%), Verification (80.0%)
- **Heaviest Functions:** `poll_read_head` (Many-Argument Workhorses, Impact: 37.4), `poll_read_body` (Compute Cores, Impact: 29.2), `maybe_notify` (Compute Cores, Impact: 17.9)

### 9. `src/proto/h1/role.rs` (RUST) -> Cumulative Risk: **570.08**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.00)
- **Magnitude:** 1187.36 | **LOC:** 3174 | **CtrlFlow:** 10.3% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (96.7033%), State Flux (88.5385%), Verification (80.0%)
- **Heaviest Functions:** `encode_headers` (Many-Argument Workhorses, Impact: 183.9), `parse` (Many-Argument Workhorses, Impact: 75.3), `parse` (Many-Argument Workhorses, Impact: 65.6)

### 10. `src/proto/h2/ping.rs` (RUST) -> Cumulative Risk: **556.77**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.43)
- **Magnitude:** 224.38 | **LOC:** 515 | **CtrlFlow:** 13.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (98.1937%), Documentation (91.1765%), Verification (80.0%)
- **Heaviest Functions:** `poll` (Defensive Guards, Impact: 18.5), `calculate` (Many-Argument Workhorses, Impact: 18.1), `record_data` (Defensive Guards, Impact: 17.2)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/proto/h1/role.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1187.36 | **LOC:** 3174 | **CtrlFlow:** 10.3% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (24.5815%), Tech Debt (50.2854%)
**Top Internal Functions/Classes:**
  * `encode_headers` **(Many-Argument Workhorses)** (Impact: 183.9)
  * `parse` **(Many-Argument Workhorses)** (Impact: 75.3)
  * `parse` **(Many-Argument Workhorses)** (Impact: 65.6)
  * `set_length` **(Many-Argument Workhorses)** (Impact: 48.2)
  * `encode` **(Many-Argument Workhorses)** (Impact: 41.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Cascading Flux:* 82 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 296
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 271`, `structural_boundaries: 654`, `args: 103`, `func_start: 86`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 53`, `high_risk_execution: 5`, `state_mutation: 132`, `dead_code: 1`, `planned_debt: 6`, `duplicate_logic: 2`, `unreferenced_by_name: 36`
* *Architecture:* `api: 7`, `import: 41`
* *Defense:* `safety: 49`, `doc: 7`, `test: 123`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.474
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CONTENT_LENGTH, Encoder, HeaderMap, HeaderName, HeaderValue, Http1Transaction, MessageHead, ParseContext...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/server.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 894.18 | **LOC:** 3601 | **CtrlFlow:** 3.3% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (17.0999%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `run_test` **(Compute Cores)** (Impact: 15.6)
  * `h2_connect_multiplex` **(Tests & Verification)** (Impact: 15.4)
  * `serve` **(Compute Cores)** (Impact: 12.4)
  * `call` **(Defensive Guards)** (Impact: 11.8)
  * `read_until` **(Generic / Templated Code)** (Impact: 11.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Rce:* 1 instances
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 5 instances
* *Concurrency (weighted view):* 352
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 32
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 98`, `structural_boundaries: 1200`, `args: 210`, `func_start: 144`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 417`, `high_risk_execution: 8`, `state_mutation: 22`, `planned_debt: 1`, `duplicate_logic: 3`, `unreferenced_by_name: 91`
* *Architecture:* `io: 63`, `api: 2`, `concurrency: 322`, `import: 42`
* *Defense:* `safety: 7`, `doc: 2`, `test: 239`, `sync_locks: 14`, `immutability_locks: 9`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.474
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AsyncWriteExt, BodyExt, DuplexStream, Either, Empty, Full, FutureExt, HeaderName...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/client.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 577.04 | **LOC:** 2930 | **CtrlFlow:** 3.1% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (11.2166%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_try_send_request` **(Tests & Verification)** (Impact: 12.1)
  * `http2_detect_conn_eof` **(I/O & Config Routines)** (Impact: 7.0)
  * `connect_method` **(Tests & Verification)** (Impact: 6.5)
  * `upgrade` **(Tests & Verification)** (Impact: 6.2)
  * `drain_til_eof` **(Generic / Templated Code)** (Impact: 6.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Rce:* 1 instances
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 9 instances
* *High Risk Execution (weighted view):* 9
* *Concurrency (weighted view):* 288
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 37
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 76`, `structural_boundaries: 751`, `args: 132`, `func_start: 51`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 250`, `high_risk_execution: 11`, `state_mutation: 19`, `dead_code: 4`
* *Architecture:* `io: 60`, `api: 27`, `concurrency: 263`, `import: 51`
* *Defense:* `safety: 9`, `doc: 2`, `test: 94`, `sync_locks: 1`, `immutability_locks: 4`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.474
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AsyncWriteExt, Bytes, DuplexStream, Empty, Frame, Full, FutureExt, FutureHyperExt...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/proto/h1/conn.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 562.8 | **LOC:** 1532 | **CtrlFlow:** 14.5% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (22.8581%), Tech Debt (10.1027%)
**Top Internal Functions/Classes:**
  * `poll_read_head` **(Many-Argument Workhorses)** (Impact: 37.4)
  * `poll_read_body` **(Compute Cores)** (Impact: 29.2)
  * `maybe_notify` **(Compute Cores)** (Impact: 17.9)
  * `write_trailers` **(Compute Cores)** (Impact: 16.8)
  * `require_empty_read` **(Compute Cores)** (Impact: 15.5)
    * *Intent:* // This will check to make sure the io object read is empty. // // This should only be called for Cl...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 22 instances
* *High Risk Execution (weighted view):* 3
* *State Mutation (weighted view):* 107
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 138`, `structural_boundaries: 207`, `args: 82`, `func_start: 77`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 6`, `state_mutation: 63`, `planned_debt: 3`, `fragile_debt: 1`
* *Architecture:* `io: 1`, `api: 46`, `concurrency: 1`, `import: 23`
* *Defense:* `safety: 18`, `doc: 26`, `test: 20`, `immutability_locks: 1`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.474
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ::uri::Uri, Bytes, CONNECTION, ClientTransaction, Decoder, Encode, EncodedBuf, Encoder...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/proto/h1/decode.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 557.74 | **LOC:** 1255 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (50.2575%), Tech Debt (50.4664%)
**Top Internal Functions/Classes:**
  * `decode` **(Many-Argument Workhorses)** (Impact: 41.1)
  * `read_body` **(Many-Argument Workhorses)** (Impact: 17.4)
  * `test_read_chunk_size` **(Tests & Verification)** (Impact: 16.8)
    * *Intent:* */
  * `read_async` **(Many-Argument Workhorses)** (Impact: 13.7)
    * *Intent:* // perform an async read using a custom buffer size and causing a blocking // read at the specified ...
  * `read_err` **(Compute Cores)** (Impact: 12.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 12 instances
* *Amplified Cascading Flux:* 30 instances
* *Concurrency (weighted view):* 142
* *State Mutation (weighted view):* 107
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 403`, `args: 56`, `func_start: 49`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 43`, `high_risk_execution: 1`, `state_mutation: 47`, `planned_debt: 2`, `unreferenced_by_name: 17`
* *Architecture:* `io: 2`, `api: 7`, `concurrency: 82`, `import: 19`
* *Defense:* `safety: 7`, `doc: 28`, `test: 62`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.474
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Bytes, BytesMut, Eof, HeaderName, HeaderValue, InvalidInput, Length, Poll...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/proto/h1/dispatch.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 364.8 | **LOC:** 809 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (30.4465%), Tech Debt (36.1656%)
**Top Internal Functions/Classes:**
  * `poll_write` **(Compute Cores)** (Impact: 72.2)
  * `poll_read` **(Compute Cores)** (Impact: 41.9)
  * `poll_inner` **(Many-Argument Workhorses)** (Impact: 21.1)
  * `recv_msg` **(Defensive Guards)** (Impact: 19.4)
  * `poll_read_head` **(Many-Argument Workhorses)** (Impact: 16.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Cascading Flux:* 10 instances
* *High Risk Execution (weighted view):* 2
* *State Mutation (weighted view):* 34
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 120`, `structural_boundaries: 202`, `args: 46`, `func_start: 35`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 6`, `state_mutation: 14`, `dead_code: 2`, `fragile_debt: 1`, `unreferenced_by_name: 7`
* *Architecture:* `api: 12`, `concurrency: 21`, `import: 17`
* *Defense:* `safety: 17`, `doc: 7`, `test: 13`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.474
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Bytes, Conn, DecodedLength, Dispatched, Incoming, MessageHead, Poll, RequestHead...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/proto/h1/io.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 352.28 | **LOC:** 968 | **CtrlFlow:** 9.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.3952%), Tech Debt (9.7807%)
**Top Internal Functions/Classes:**
  * `poll_flush` **(Compute Cores)** (Impact: 24.3)
  * `parse` **(Many-Argument Workhorses)** (Impact: 20.6)
  * `record` **(Compute Cores)** (Impact: 15.5)
  * `poll_flush_flattened` **(Compute Cores)** (Impact: 13.0)
    * *Intent:* /// Specialized version of `flush` when strategy is Flatten. /// /// Since all buffered bytes are fl...
  * `buffer` **(Compute Cores)** (Impact: 8.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 60
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 70`, `structural_boundaries: 181`, `args: 64`, `func_start: 61`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 30`, `dead_code: 8`, `planned_debt: 4`
* *Architecture:* `io: 1`, `api: 39`, `concurrency: 8`, `import: 15`
* *Defense:* `safety: 2`, `doc: 25`, `test: 51`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.474
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` BufMut, Bytes, BytesMut, IoSlice, ParseContext, ParsedMessage, Poll, ReadBuf...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/client/conn/http2.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 291.22 | **LOC:** 712 | **CtrlFlow:** 4.9% | **Authorship Centralization:** 25.0%
- **Risk Profile:** Cognitive Load (41.7635%), Tech Debt (98.7807%)
**Top Internal Functions/Classes:**
  * `try_send_request` **(Generic / Templated Code)** (Impact: 6.4)
    * *Intent:* /// Sends a `Request` on the associated connection. /// /// Returns a future that if successful, yie...
  * `send_request` **(Generic / Templated Code)** (Impact: 6.3)
    * *Intent:* /// Sends a `Request` on the associated connection. /// /// Returns a future that if successful, yie...
  * `poll_ready` **(Generic / Templated Code)** (Impact: 5.5)
    * *Intent:* /// Polls to determine whether this sender can be used yet for a request. /// /// If the associated ...
  * `poll` **(Generic / Templated Code)** (Impact: 5.5)
  * `handshake` **(Generic / Templated Code)** (Impact: 4.9)
    * *Intent:* /// Constructs a connection with the configured options and IO. /// See [`client::conn`](crate::clie...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 8 instances
* *Concurrency (weighted view):* 82
* *State Mutation (weighted view):* 36
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 152`, `args: 48`, `func_start: 47`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 3`, `state_mutation: 20`, `fragile_debt: 2`, `duplicate_logic: 7`
* *Architecture:* `api: 39`, `concurrency: 72`, `import: 18`
* *Defense:* `safety: 3`, `doc: 187`, `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.474
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Incoming, Poll, Response, TrySendError, Write, crate::body::Body, crate::common::time::Time, crate::proto...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/proto/h2/client.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 247.58 | **LOC:** 792 | **CtrlFlow:** 10.1% | **Authorship Centralization:** 25.0%
- **Risk Profile:** Cognitive Load (18.4161%), Tech Debt (9.3291%)
**Top Internal Functions/Classes:**
  * `poll` **(Many-Argument Workhorses)** (Impact: 50.9)
  * `poll` **(Defensive Guards)** (Impact: 13.0)
  * `poll_pipe` **(Many-Argument Workhorses)** (Impact: 12.7)
  * `handshake` **(Many-Argument Workhorses)** (Impact: 12.6)
  * `new_builder` **(Defensive Guards)** (Impact: 9.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 181`, `args: 25`, `func_start: 19`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 5`, `dead_code: 1`, `fragile_debt: 1`
* *Architecture:* `api: 26`, `concurrency: 40`, `import: 24`
* *Defense:* `safety: 14`, `doc: 5`, `immutability_locks: 6`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.474
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Connection, FusedFuture, FusedStream, Http2UpgradedExec, Incoming, PipeToSendStream, Poll, Recorder...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/support/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 237.38 | **LOC:** 594 | **CtrlFlow:** 6.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (42.2408%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `async_test` **(Compute Cores)** (Impact: 32.0)
  * `naive_proxy` **(Compute Cores)** (Impact: 20.4)
  * `__run_test` **(Interface Declarations)** (Impact: 1.6)
  * `default` **(State Mutators)** (Impact: 1.4)
  * `default` **(State Mutators)** (Impact: 1.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Rce:* 3 instances
* *Amplified Race Conditions:* 11 instances
* *Amplified Cascading Flux:* 5 instances
* *High Risk Execution (weighted view):* 1
* *Concurrency (weighted view):* 114
* *Sec Tainted Injection (weighted view):* 3
* *State Mutation (weighted view):* 21
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 152`, `args: 15`, `func_start: 6`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 31`, `high_risk_execution: 5`, `state_mutation: 11`
* *Architecture:* `io: 19`, `api: 34`, `concurrency: 59`, `import: 13`
* *Defense:* `safety: 5`, `test: 14`, `sync_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.474
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Arc, Full, FutureExt, Mutex, Ordering, Request, Response, StreamExt...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/proto/h2/ping.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 224.38 | **LOC:** 515 | **CtrlFlow:** 13.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (13.1823%), Tech Debt (76.1067%)
**Top Internal Functions/Classes:**
  * `poll` **(Defensive Guards)** (Impact: 18.5)
  * `calculate` **(Many-Argument Workhorses)** (Impact: 18.1)
  * `record_data` **(Defensive Guards)** (Impact: 17.2)
  * `maybe_ping` **(Many-Argument Workhorses)** (Impact: 14.7)
  * `maybe_schedule` **(Compute Cores)** (Impact: 10.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 60
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 115`, `args: 26`, `func_start: 23`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 22`, `dead_code: 2`, `fragile_debt: 2`, `unreferenced_by_name: 6`
* *Architecture:* `api: 18`, `concurrency: 1`, `import: 9`
* *Defense:* `safety: 11`, `doc: 44`, `test: 1`, `sync_locks: 8`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.474
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Instant, Mutex, PingPong, Poll, crate::common::time::Time, crate::rt::Sleep, h2::Ping, std::fmt...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ffi/http_types.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 191.8 | **LOC:** 707 | **CtrlFlow:** 6.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (7.8026%), Tech Debt (99.8124%)
**Top Internal Functions/Classes:**
  * `hyper_headers_foreach` **(Many-Argument Workhorses)** (Impact: 30.9)
    * *Intent:* /// Iterates the headers passing each name and value pair to the callback. /// /// The `userdata` po...
  * `hyper_request_set_uri_parts` **(Many-Argument Workhorses)** (Impact: 16.1)
    * *Intent:* /// Set the URI of the request with separate scheme, authority, and /// path/query strings. /// /// ...
  * `raw_name_value` **(Many-Argument Workhorses)** (Impact: 7.7)
  * `hyper_headers_set` **(Many-Argument Workhorses)** (Impact: 5.5)
    * *Intent:* /// Sets the header with the provided name to the provided value. /// /// This overwrites any previo...
  * `hyper_headers_add` **(Many-Argument Workhorses)** (Impact: 5.5)
    * *Intent:* /// Adds the provided value to the list of the provided name. /// /// If there were already existing...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 39
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 165`, `args: 32`, `func_start: 31`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 25`, `planned_debt: 1`, `duplicate_logic: 2`, `unreferenced_by_name: 22`
* *Architecture:* `api: 9`, `import: 14`
* *Defense:* `safety: 9`, `doc: 159`, `test: 5`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.474
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AsTaskType, HYPER_ITER_CONTINUE, HeaderValue, Method, OriginalHeaderOrder, ReasonPhrase, Request, Response...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/proto/h1/encode.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 186.76 | **LOC:** 673 | **CtrlFlow:** 5.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (9.0441%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `encode_trailers` **(Many-Argument Workhorses)** (Impact: 26.8)
  * `encode` **(Generic / Templated Code)** (Impact: 8.6)
  * `encode_and_end` **(Many-Argument Workhorses)** (Impact: 8.2)
  * `advance` **(Annotated Framework Methods)** (Impact: 4.0)
  * `chunks_vectored` **(Generic / Templated Code)** (Impact: 4.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 159`, `args: 43`, `func_start: 38`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 19`
* *Architecture:* `io: 2`, `api: 25`, `import: 15`
* *Defense:* `safety: 1`, `doc: 9`, `test: 33`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.474
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Bytes, CACHE_CONTROL, CONTENT_ENCODING, CONTENT_LENGTH, CONTENT_RANGE, CONTENT_TYPE, HOST, HeaderMap...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/body/incoming.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 183.78 | **LOC:** 633 | **CtrlFlow:** 6.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (6.0357%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `poll_frame` **(Compute Cores)** (Impact: 18.5)
  * `h2` **(Many-Argument Workhorses)** (Impact: 7.0)
  * `size_hint` **(Annotated Framework Methods)** (Impact: 6.8)
  * `new_channel` **(Compute Cores)** (Impact: 6.4)
  * `eq` **(Compute Cores)** (Impact: 6.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 136`, `args: 37`, `func_start: 32`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 6`, `state_mutation: 5`, `dead_code: 1`
* *Architecture:* `api: 24`, `concurrency: 21`, `import: 18`
* *Defense:* `safety: 5`, `doc: 46`, `test: 31`, `immutability_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.474
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Frame, Incoming, Poll, Sender, SizeHint, Stream, bytes::Bytes, crate::common::watch...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/error.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 177.52 | **LOC:** 703 | **CtrlFlow:** 3.7% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (3.9213%), Tech Debt (98.4546%)
**Top Internal Functions/Classes:**
  * `find_source` **(Defensive Guards)** (Impact: 4.8)
  * `description` **(Annotated Framework Methods)** (Impact: 4.8)
  * `new_h2` **(Annotated Framework Methods)** (Impact: 4.6)
  * `fmt` **(Defensive Guards)** (Impact: 3.9)
  * `from` **(State Mutators)** (Impact: 3.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 50`, `args: 62`, `func_start: 59`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 7`, `unreferenced_by_name: 36`
* *Architecture:* `io: 3`, `api: 48`, `concurrency: 4`, `import: 4`
* *Defense:* `safety: 4`, `doc: 75`, `test: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.474
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::error::Error, std::fmt, std::mem, super::*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/proto/h2/server.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 177.08 | **LOC:** 551 | **CtrlFlow:** 9.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (14.1654%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `poll_server` **(Many-Argument Workhorses)** (Impact: 31.6)
  * `poll2` **(Many-Argument Workhorses)** (Impact: 28.8)
  * `new` **(Many-Argument Workhorses)** (Impact: 17.3)
  * `poll` **(Compute Cores)** (Impact: 17.3)
  * `poll_ping` **(Defensive Guards)** (Impact: 5.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 13
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 135`, `args: 13`, `func_start: 9`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 5`, `dead_code: 1`
* *Architecture:* `api: 18`, `concurrency: 22`, `import: 25`
* *Defense:* `safety: 13`, `test: 2`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.474
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Handshake, Http2UpgradedExec, Incoming, Pending, PipeToSendStream, Poll, RecvStream, Request...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `capi/examples/upload.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 175.06 | **LOC:** 401 | **CtrlFlow:** 15.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (30.0016%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `main` **(Many-Argument Workhorses)** (Impact: 60.2)
    * *Intent:* #define STR_ARG(XX) (uint8_t *)XX, strlen(XX)
  * `connect_to` **(C Struct Operations)** (Impact: 15.7)
  * `read_cb` **(C Struct Operations)** (Impact: 9.9)
  * `write_cb` **(C Struct Operations)** (Impact: 9.9)
  * `poll_req_upload` **(C Struct Operations)** (Impact: 7.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 16 instances
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 53
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 62`, `args: 11`, `func_start: 8`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 21`, `unreferenced_by_name: 1`
* *Architecture:* `io: 6`, `api: 4`, `import: 12`
* *Defense:* `safety: 11`, `immutability_locks: 10`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.474
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` assert.h, errno.h, fcntl.h, hyper.h, netdb.h, stdio.h, stdlib.h, string.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/client/conn/http1.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 174.78 | **LOC:** 612 | **CtrlFlow:** 6.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (23.2989%), Tech Debt (99.6256%)
**Top Internal Functions/Classes:**
  * `handshake` **(Defensive Guards)** (Impact: 21.8)
    * *Intent:* /// Constructs a connection with the configured options and IO. /// See [`client::conn`](crate::clie...
  * `try_send_request` **(Generic / Templated Code)** (Impact: 6.4)
    * *Intent:* /// Sends a `Request` on the associated connection. /// /// Returns a future that if successful, yie...
  * `send_request` **(Generic / Templated Code)** (Impact: 6.2)
    * *Intent:* /// Returns a future that if successful, yields the `Response`. /// /// `req` must have a `Host` hea...
  * `poll` **(Generic / Templated Code)** (Impact: 5.8)
  * `poll` **(Generic / Templated Code)** (Impact: 4.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 111`, `args: 30`, `func_start: 28`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 2`, `state_mutation: 10`, `fragile_debt: 2`, `unreferenced_by_name: 15`
* *Architecture:* `api: 32`, `concurrency: 38`, `import: 15`
* *Defense:* `safety: 4`, `doc: 214`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.474
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Incoming, Poll, Response, TrySendError, Write, bytes::Bytes, crate::body::Body, crate::proto...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/client/dispatch.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 172.6 | **LOC:** 528 | **CtrlFlow:** 8.1% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (6.5404%), Tech Debt (92.4142%)
**Top Internal Functions/Classes:**
  * `giver_queue_throughput` **(Annotated Framework Methods)** (Impact: 8.2)
  * `poll` **(Compute Cores)** (Impact: 6.8)
  * `drop` **(Defensive Guards)** (Impact: 6.5)
  * `can_send` **(Annotated Framework Methods)** (Impact: 6.3)
  * `try_send` **(Generic / Templated Code)** (Impact: 4.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 162`, `args: 50`, `func_start: 36`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 19`, `high_risk_execution: 3`, `state_mutation: 1`, `dead_code: 3`, `fragile_debt: 1`, `unreferenced_by_name: 12`
* *Architecture:* `api: 33`, `concurrency: 21`, `import: 12`
* *Defense:* `safety: 3`, `doc: 36`, `test: 8`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.474
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Callback, Poll, Receiver, Request, Response, crate::body::Incoming, http::Request, http_body::Body...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/server/conn/http1.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 170.32 | **LOC:** 560 | **CtrlFlow:** 6.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (28.8986%), Tech Debt (68.3082%)
**Top Internal Functions/Classes:**
  * `serve_connection` **(Many-Argument Workhorses)** (Impact: 26.5)
    * *Intent:* /// # I: Read + Write + Unpin + Send + 'static, /// # S: Service<hyper::Request<Incoming>, Response=...
  * `poll` **(Defensive Guards)** (Impact: 7.7)
  * `poll` **(Generic / Templated Code)** (Impact: 6.1)
  * `without_shutdown` **(Generic / Templated Code)** (Impact: 3.2)
    * *Intent:* /// Prevent shutdown of the underlying IO object at the end of service the request, /// instead run ...
  * `graceful_shutdown` **(Defensive Guards)** (Impact: 3.2)
    * *Intent:* /// Start a graceful shutdown process for this connection. /// /// This `Connection` should continue...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Concurrency (weighted view):* 39
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 97`, `args: 27`, `func_start: 25`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 11`, `dead_code: 5`, `unreferenced_by_name: 10`
* *Architecture:* `api: 30`, `concurrency: 29`, `import: 15`
* *Defense:* `safety: 6`, `doc: 208`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.474
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Incoming, Poll, Request, Response, Time, Write, bytes::Bytes, crate::
    common::time::Dur...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ffi/task.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 160.42 | **LOC:** 550 | **CtrlFlow:** 9.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (27.0749%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `poll_next` **(Compute Cores)** (Impact: 11.6)
  * `hyper_task_value` **(Defensive Guards)** (Impact: 7.8)
    * *Intent:* /// Takes the output value of this task. /// /// This must only be called once polling the task on a...
  * `drain_queue` **(Compute Cores)** (Impact: 4.9)
    * *Intent:* /// drain_queue locks both self.spawn_queue and self.driver, so it requires /// that neither of them...
  * `poll` **(Generic / Templated Code)** (Impact: 4.0)
  * `hyper_task_set_userdata` **(Parameter Forwarders)** (Impact: 3.8)
    * *Intent:* /// Set a user data pointer to be associated with this task. /// /// This value will be passed to ta...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 31
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 92`, `args: 31`, `func_start: 31`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 6`
* *Architecture:* `api: 30`, `concurrency: 26`, `import: 9`
* *Defense:* `safety: 5`, `doc: 188`, `sync_locks: 10`, `immutability_locks: 3`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.474
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Arc, Mutex, Ordering, Poll, Stream, Weak, c_void, futures_util::stream::FuturesUnordered...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `capi/examples/client.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 152.6 | **LOC:** 344 | **CtrlFlow:** 15.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (35.8013%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `main` **(Many-Argument Workhorses)** (Impact: 53.4)
    * *Intent:* #define STR_ARG(XX) (uint8_t *)XX, strlen(XX)
  * `connect_to` **(C Struct Operations)** (Impact: 15.7)
  * `read_cb` **(C Struct Operations)** (Impact: 9.9)
  * `write_cb` **(C Struct Operations)** (Impact: 9.9)
  * `free_conn_data` **(Compute Cores)** (Impact: 4.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 14 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 46
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 47`, `args: 10`, `func_start: 7`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 18`, `unreferenced_by_name: 1`
* *Architecture:* `io: 4`, `api: 3`, `import: 12`
* *Defense:* `safety: 13`, `immutability_locks: 12`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.474
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` assert.h, errno.h, fcntl.h, hyper.h, netdb.h, stdio.h, stdlib.h, string.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `benches/end_to_end.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 151.14 | **LOC:** 452 | **CtrlFlow:** 5.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (24.3917%), Tech Debt (99.4252%)
**Top Internal Functions/Classes:**
  * `bench` **(Many-Argument Workhorses)** (Impact: 38.8)
  * `spawn_server` **(Defensive Guards)** (Impact: 12.8)
  * `request_chunks` **(Generic / Templated Code)** (Impact: 2.3)
  * `http2_parallel_x10_req_10mb` **(Annotated Framework Methods)** (Impact: 2.0)
  * `http2_parallel_x10_req_10kb_100_chunks_adaptive_window` **(Annotated Framework Methods)** (Impact: 2.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Rce:* 1 instances
* *Amplified Cascading Flux:* 1 instances
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 13
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 130`, `args: 39`, `func_start: 31`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 12`, `high_risk_execution: 1`, `state_mutation: 11`, `planned_debt: 2`, `unreferenced_by_name: 19`
* *Architecture:* `io: 16`, `concurrency: 25`, `import: 11`
* *Defense:* `safety: 6`, `test: 6`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.474
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Request, Response, futures_util::SinkExt, futures_util::future::join_all, http_body_util::BodyExt, http_body_util::Full, hyper::Method, hyper::body::Frame...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/single_threaded.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 136.84 | **LOC:** 384 | **CtrlFlow:** 12.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (34.7768%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `http1_client` **(Defensive Guards)** (Impact: 16.9)
  * `http2_client` **(Defensive Guards)** (Impact: 16.9)
  * `main` **(Callbacks & Closures)** (Impact: 8.3)
  * `http2_server` **(Interface Declarations)** (Impact: 7.2)
  * `http1_server` **(Interface Declarations)** (Impact: 6.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 171`, `args: 20`, `func_start: 13`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 38`
* *Architecture:* `io: 24`, `api: 7`, `concurrency: 52`, `import: 17`
* *Defense:* `safety: 10`, `doc: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.049
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.009804
  * `Imports (Out-Degree: 0):` AsyncWriteExt, Bytes, Frame, Poll, Response, http_body_util::BodyExt, hyper::Error, hyper::Request...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/server/conn/http2.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 133.14 | **LOC:** 313 | **CtrlFlow:** 4.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (45.5038%), Tech Debt (9.8918%)
**Top Internal Functions/Classes:**
  * `poll` **(Generic / Templated Code)** (Impact: 4.0)
  * `adaptive_window` **(Parameter Forwarders)** (Impact: 4.0)
    * *Intent:* /// Sets whether to use an adaptive flow control. /// /// Enabling this will override the limits set...
  * `initial_stream_window_size` **(Generic / Templated Code)** (Impact: 3.8)
    * *Intent:* /// Sets the [`SETTINGS_INITIAL_WINDOW_SIZE`][spec] option for HTTP2 /// stream-level flow control. ...
  * `initial_connection_window_size` **(Generic / Templated Code)** (Impact: 3.8)
    * *Intent:* /// Sets the max connection-level flow control for HTTP2. /// /// Passing `None` will do nothing. //...
  * `max_frame_size` **(Generic / Templated Code)** (Impact: 3.8)
    * *Intent:* /// Sets the maximum frame size to use for HTTP2. /// /// Passing `None` will do nothing. /// /// If...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 8 instances
* *Concurrency (weighted view):* 29
* *State Mutation (weighted view):* 34
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 75`, `args: 19`, `func_start: 19`, `class_start: 2`
* *Risk/State:* `state_mutation: 18`, `planned_debt: 1`
* *Architecture:* `api: 20`, `concurrency: 19`, `import: 16`
* *Defense:* `safety: 3`, `doc: 108`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.474
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Incoming, Poll, Write, crate::body::Body, crate::common::time::Time, crate::proto, crate::rt::Read, crate::rt::bounds::Http2ServerConnExec...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/client/conn/http2.rs` -> Churn: **100.0%** | Cog Load: 41.7635% | Debt: 98.7807%
- `src/client/dispatch.rs` -> Churn: **68.26%** | Cog Load: 6.5404% | Debt: 92.4142%
- `src/proto/h1/role.rs` -> Churn: **55.8%** | Cog Load: 24.5815% | Debt: 50.2854%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/proto/h1/decode.rs` -> **Sean McArthur** (100.0% isolated ownership) | Magnitude: 557.74
- `src/proto/h2/ping.rs` -> **Ariel Ben-Yehuda** (100.0% isolated ownership) | Magnitude: 224.38
- `src/ffi/http_types.rs` -> **Dhruva D** (100.0% isolated ownership) | Magnitude: 191.8
- `src/proto/h1/encode.rs` -> **HueCodes** (100.0% isolated ownership) | Magnitude: 186.76
- `src/body/incoming.rs` -> **Sean McArthur** (100.0% isolated ownership) | Magnitude: 183.78

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `examples/single_threaded.rs` -> **Severity: 0.837** (Embedded: 0.0098 * Error Risk: 85.3883%)
- `examples/web_api.rs` -> **Severity: 0.715** (Embedded: 0.0098 * Error Risk: 72.9431%)
- `examples/graceful_shutdown.rs` -> **Severity: 0.662** (Embedded: 0.0098 * Error Risk: 67.4746%)
- `examples/send_file.rs` -> **Severity: 0.648** (Embedded: 0.0098 * Error Risk: 66.1096%)
- `examples/multi_server.rs` -> **Severity: 0.633** (Embedded: 0.0098 * Error Risk: 64.5656%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `benches/end_to_end.rs` -> **Severity: 947.4** (Blast Radius: 9.474 * Doc Risk: 100.0%)
- `benches/pipeline.rs` -> **Severity: 947.4** (Blast Radius: 9.474 * Doc Risk: 100.0%)
- `benches/server.rs` -> **Severity: 947.4** (Blast Radius: 9.474 * Doc Risk: 100.0%)
- `src/body/mod.rs` -> **Severity: 947.4** (Blast Radius: 9.474 * Doc Risk: 100.0%)
- `src/common/buf.rs` -> **Severity: 947.4** (Blast Radius: 9.474 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
