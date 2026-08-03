# ARCHITECTURAL_BRIEF: actix-web
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_rust/actix-web` |
| **Timestamp** | `2026-08-03T19:43:26.906744+00:00` |
| **Scan Duration** | `1.38s` |
| **Git Branch** | `main` |
| **Git Commit** | `4702c0fdf97f796a38e45a9c1f8306ea08d79f1b` |
| **Git Remote** | `https://github.com/actix/actix-web.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 285 malicious artifacts.

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
| Total Artifacts | 442 |
| Analyzed Artifacts (Scanned) | 333 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 109 |
| Total LOC | 57215 |
| Volatility Index | 0.003 |
| % Scanned of codebase = | 75.3% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4461 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3361 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.3337 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 6 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUST | 281 | 57019 | 84.4% |
| MARKDOWN | 26 | 0 | 7.8% |
| PLAINTEXT | 22 | 0 | 6.6% |
| SHELL | 4 | 196 | 1.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `3.388`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_0 | 86 | 25.8% |
| file_cluster_4 | 60 | 18.0% |
| file_cluster_8 | 44 | 13.2% |
| file_cluster_13 | 43 | 12.9% |
| file_cluster_16 | 38 | 11.4% |
| file_cluster_7 | 4 | 1.2% |
| file_cluster_17 | 4 | 1.2% |
| file_cluster_9 | 4 | 1.2% |
| file_cluster_6 | 1 | 0.3% |
| file_cluster_11 | 1 | 0.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 48 | 14.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 109*

**Composition by Extension & Reason:**
- `.rs`: 31x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 12x Unsupported Format (.toml), 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.toml')
- `.yml`: 14x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.stderr`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.png`: 3x Excluded (Explicitly Denied Extension: '.png')
- `.binary`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.dot`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.br`: 2x Excluded (Unsupported Extension: '.br')
- `.gz`: 2x Excluded (Explicitly Denied Extension: '.gz')
- `.lock`: 1x Excluded (Unsupported Extension: '.lock')
- `.js`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.xz`: 1x Excluded (Explicitly Denied Extension: '.xz')
- `.zst`: 1x Excluded (Unsupported Extension: '.zst')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 24.2 | 17.1 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 29.0 | 24.3 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 37.6 | 10.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 20.9 | 2.4 | 80.0 |
| API Exposure | 0.0 | 8.7 | 3.5 | 3.8 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 54.3 | 98.2 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 38.5 | 26.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 14.7 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 96.7 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 7.2 | 0.9 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 58.0 | 4.8 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 47.2 | 36.8 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 61.2 | 98.6 | 100.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 20.0 | 9.1 | 0.6 | 20.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 4.9 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `scripts/bump` (Hits: 45)
- `scripts/unreleased` (Hits: 10)
- `awc/src/client/connector.rs` (Hits: 5)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **web.rs** (`actix-web/src/web.rs`) — 54 inbound connections
2. **guard.rs** (`actix-files/tests/guard.rs`) — 10 inbound connections
3. **read_body.rs** (`awc/src/responses/read_body.rs`) — 10 inbound connections
4. **header.rs** (`actix-web/src/types/header.rs`) — 6 inbound connections
5. **dev.rs** (`actix-web/src/dev.rs`) — 4 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **mod.rs** (`actix-http/src/header/mod.rs`) — 88 outbound dependencies
2. **connector.rs** (`awc/src/client/connector.rs`) — 67 outbound dependencies
3. **resource.rs** (`actix-web/src/resource.rs`) — 61 outbound dependencies
4. **app.rs** (`actix-web/src/app.rs`) — 59 outbound dependencies
5. **scope.rs** (`actix-web/src/scope.rs`) — 58 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `handle_request` (@ `actix-http/src/h1/dispatcher.rs`) -> Impact: **1308.6** | LOC: 502
- `poll_response` (@ `actix-http/src/h1/dispatcher.rs`) -> Impact: **381.4** | LOC: 208
- `call` (@ `actix-files/src/service.rs`) -> Impact: **356.7** | LOC: 102
- `set_headers` (@ `actix-http/src/h1/decoder.rs`) -> Impact: **341.3** | LOC: 139
- `new` (@ `actix-web-codegen/src/route.rs`) -> Impact: **307.6** | LOC: 90
- `poll_next` (@ `actix-http/src/encoding/encoder.rs`) -> Impact: **297.6** | LOC: 72
- `call` (@ `awc/src/client/pool.rs`) -> Impact: **283.4** | LOC: 91
- `call` (@ `actix-http/src/h1/dispatcher_tests.rs`) -> Impact: **282.4** | LOC: 972
- `start_with` (@ `actix-test/src/lib.rs`) -> Impact: **275.3** | LOC: 362
  * *Intent:* /// Start default [`TestServer`]. /// /// # Examples /// ``` /// use actix_web::{get, web, test, App, HttpResponse, Error, Responder};
- `send_request` (@ `awc/src/client/h1proto.rs`) -> Impact: **247.0** | LOC: 140

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `poll_next` (@ `actix-files/src/chunked.rs`) -> **O(2^N) [Recursive]**
- `poll_next` (@ `actix-files/src/chunked.rs`) -> **O(2^N) [Recursive]**
- `new_service` (@ `actix-files/src/files.rs`) -> **O(2^N) [Recursive]**
- `call` (@ `actix-files/src/service.rs`) -> **O(2^N) [Recursive]**
- `main` (@ `actix-http/examples/echo.rs`) -> **O(2^N) [Recursive]**
- `main` (@ `actix-http/examples/h2c-detect.rs`) -> **O(2^N) [Recursive]**
- `main` (@ `actix-http/examples/streaming-error.rs`) -> **O(2^N) [Recursive]**
- `main` (@ `actix-http/examples/tls_rustls.rs`) -> **O(2^N) [Recursive]**
  * *Intent:* //! Demonstrates TLS configuration (via Rustls) for HTTP/1.1 and HTTP/2 connections. //! //! Test using cURL: //! //! ```console //! $ curl --insecure...
- `poll_next` (@ `actix-http/src/encoding/decoder.rs`) -> **O(2^N) [Recursive]**
- `poll_next` (@ `actix-http/src/encoding/encoder.rs`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `Anonymous_Block_[Truncated]` (@ `scripts/bump`) -> DB Complexity: **85**
- `call` (@ `actix-http/src/h1/dispatcher_tests.rs`) -> DB Complexity: **43**
- `unreleased_for` (@ `scripts/unreleased`) -> DB Complexity: **43**
- `test_parse_chunked_payload_chunk_extensi` (@ `actix-http/src/h1/chunked.rs`) -> DB Complexity: **42**
- `handle_request` (@ `actix-http/src/h1/dispatcher.rs`) -> DB Complexity: **30**
- `build_path_list` (@ `actix-router/src/resource.rs`) -> DB Complexity: **23**
- `Anonymous_Block` (@ `scripts/bump`) -> DB Complexity: **21**
- `test_write_content_length` (@ `actix-http/src/helpers.rs`) -> DB Complexity: **20**
- `test_recognizer_1` (@ `actix-router/src/router.rs`) -> DB Complexity: **20**
- `test_recognizer_with_prefix` (@ `actix-router/src/router.rs`) -> DB Complexity: **18**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `actix-web/src` | 23 | 7066.48 | 20.36% | 37.68% |
| `actix-http/src/h1` | 14 | 6305.86 | 35.02% | 47.43% |
| `awc/src/client` | 8 | 2982.76 | 35.1% | 73.65% |
| `actix-http/tests` | 6 | 2705.44 | 48.02% | 0.0% |
| `actix-web/src/middleware` | 11 | 2570.48 | 22.63% | 41.1% |
| `actix-http/src` | 14 | 2569.06 | 25.05% | 52.79% |
| `actix-web/src/types` | 10 | 2536.12 | 41.1% | 28.49% |
| `actix-files/src` | 10 | 2299.62 | 25.84% | 45.44% |
| `actix-web/src/http/header` | 27 | 2241.06 | 5.38% | 25.84% |
| `actix-router/src` | 10 | 2048.88 | 13.55% | 54.78% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `actix-http/src/body/message_body.rs` -> **100.0%** Exposure
- `actix-http/src/config.rs` -> **100.0%** Exposure
- `actix-http/src/error.rs` -> **100.0%** Exposure
- `actix-http/src/header/as_name.rs` -> **100.0%** Exposure
- `actix-http/src/header/into_pair.rs` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `scripts/bump` -> **100.0%** Exposure
- `scripts/unreleased` -> **100.0%** Exposure
- `actix-router/src/router.rs` -> **99.9997%** Exposure
- `actix-http/src/notify_on_drop.rs` -> **99.9995%** Exposure
- `actix-http/src/test.rs` -> **99.9984%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `actix-http/src/body/message_body.rs` -> **14** Orphaned Functions | **42** Duplicates
- `actix-files/src/lib.rs` -> **45** Orphaned Functions | **2** Duplicates
- `actix-http/src/h1/decoder.rs` -> **30** Orphaned Functions | **12** Duplicates
- `actix-http/src/header/map.rs` -> **12** Orphaned Functions | **28** Duplicates
- `actix-router/src/de.rs` -> **18** Orphaned Functions | **16** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`actix-web/examples/basic.rs`** -> AI Confidence: **99.39%**
2. **`actix-files/src/path_buf.rs`** -> AI Confidence: **99.31%**
3. **`actix-http/src/h1/utils.rs`** -> AI Confidence: **99.31%**
4. **`actix-http/src/header/shared/content_encoding.rs`** -> AI Confidence: **99.31%**
5. **`actix-http/src/header/shared/quality.rs`** -> AI Confidence: **99.31%**
6. **`actix-http/src/requests/head.rs`** -> AI Confidence: **99.31%**
7. **`actix-http/src/ws/codec.rs`** -> AI Confidence: **99.31%**
8. **`actix-web/examples/uds.rs`** -> AI Confidence: **99.31%**
9. **`actix-web/src/http/header/content_range.rs`** -> AI Confidence: **99.31%**
10. **`awc/src/client/error.rs`** -> AI Confidence: **99.31%**
11. **`actix-files/src/directory.rs`** -> AI Confidence: **99.24%**
12. **`actix-http/src/encoding/decoder.rs`** -> AI Confidence: **99.24%**
13. **`actix-http/src/encoding/encoder.rs`** -> AI Confidence: **99.24%**
14. **`actix-http/src/h1/client.rs`** -> AI Confidence: **99.24%**
15. **`actix-http/src/h1/dispatcher.rs`** -> AI Confidence: **99.24%**
16. **`actix-http/src/ws/proto.rs`** -> AI Confidence: **99.24%**
17. **`actix-multipart/src/field.rs`** -> AI Confidence: **99.24%**
18. **`actix-web-codegen/src/route.rs`** -> AI Confidence: **99.24%**
19. **`actix-web/examples/on-connect.rs`** -> AI Confidence: **99.24%**
20. **`actix-web/src/error/response_error.rs`** -> AI Confidence: **99.24%**
21. **`actix-web/src/guard/acceptable.rs`** -> AI Confidence: **99.24%**
22. **`actix-files/examples/guarded-listing.rs`** -> AI Confidence: **99.23%**
23. **`actix-web-codegen/src/scope.rs`** -> AI Confidence: **99.23%**
24. **`actix-web/src/http/header/entity.rs`** -> AI Confidence: **99.23%**
25. **`actix-web/examples/macroless.rs`** -> AI Confidence: **99.22%**
26. **`actix-files/src/files.rs`** -> AI Confidence: **99.18%**
27. **`actix-files/src/named.rs`** -> AI Confidence: **99.18%**
28. **`actix-http/examples/actix-web.rs`** -> AI Confidence: **99.18%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `actix-files/src/chunked.rs` -> **20.0%** Exposure
- `actix-files/src/files.rs` -> **20.0%** Exposure
- `actix-files/src/named.rs` -> **20.0%** Exposure
- `actix-files/src/service.rs` -> **20.0%** Exposure
- `actix-http-test/src/lib.rs` -> **20.0%** Exposure
### Weaponizable Injection Vectors
- `actix-multipart/src/form/mod.rs` -> **100.0%** Exposure
- `actix-web/src/guard/mod.rs` -> **100.0%** Exposure
- `actix-web/src/middleware/compress.rs` -> **100.0%** Exposure
- `actix-web/src/middleware/normalize.rs` -> **100.0%** Exposure
- `actix-web/src/request.rs` -> **100.0%** Exposure
### Raw Memory Manipulation
- `actix-http/src/responses/response.rs` -> **0.0009%** Exposure
- `actix-http-test/src/lib.rs` -> **0.0003%** Exposure
- `actix-web/src/error/response_error.rs` -> **0.0001%** Exposure
### Algorithmic DoS Exposure
- `actix-files/src/chunked.rs` -> **100.0%** Exposure
- `actix-files/src/files.rs` -> **100.0%** Exposure
- `actix-files/src/lib.rs` -> **100.0%** Exposure
- `actix-files/src/named.rs` -> **100.0%** Exposure
- `actix-files/src/service.rs` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `5272` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `actix-web/src/types/json.rs` (RUST) -> Cumulative Risk: **904.25**
- **Archetype:** `file_cluster_4` (Distance: 14.41 IQR)
- **Magnitude:** 623.16 | **LOC:** 771 | **CtrlFlow:** 18.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `poll` (Impact: 50.0), `limit` (Impact: 49.9), `poll` (Impact: 49.7)

### 2. `actix-web/src/service.rs` (RUST) -> Cumulative Risk: **863.58**
- **Archetype:** `file_cluster_0` (Distance: 13.478 IQR)
- **Magnitude:** 625.58 | **LOC:** 926 | **CtrlFlow:** 25.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Injection Surface (99.9967%)
- **Heaviest Functions:** `fmt` (Impact: 104.9), `fmt` (Impact: 42.3), `register` (Impact: 25.2)

### 3. `actix-files/src/chunked.rs` (RUST) -> Cumulative Risk: **824.36**
- **Archetype:** `file_cluster_4` (Distance: 12.572 IQR)
- **Magnitude:** 301.76 | **LOC:** 245 | **CtrlFlow:** 28.9% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `poll_next` (Impact: 62.6), `poll_next` (Impact: 62.5), `chunked_read_file_callback` (Impact: 37.6)

### 4. `awc/src/client/connection.rs` (RUST) -> Cumulative Risk: **819.37**
- **Archetype:** `file_cluster_16` (Distance: 12.66 IQR)
- **Magnitude:** 496.34 | **LOC:** 455 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `test_h2_connection_drop` (Impact: 51.5), `open_tunnel` (Impact: 49.4), `send_request` (Impact: 30.7)

### 5. `actix-http/src/h1/encoder.rs` (RUST) -> Cumulative Risk: **806.57**
- **Archetype:** `file_cluster_4` (Distance: 12.41 IQR)
- **Magnitude:** 630.08 | **LOC:** 688 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `encode_headers` (Impact: 183.0), `encode` (Impact: 94.5), `encode` (Impact: 56.1)

### 6. `actix-multipart/src/form/mod.rs` (RUST) -> Cumulative Risk: **806.02**
- **Archetype:** `file_cluster_4` (Distance: 13.338 IQR)
- **Magnitude:** 810.08 | **LOC:** 926 | **CtrlFlow:** 16.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `from_request` (Impact: 65.3), `try_consume_limits` (Impact: 41.6), `handle_field` (Impact: 38.4)

### 7. `awc/src/client/pool.rs` (RUST) -> Cumulative Risk: **782.65**
- **Archetype:** `file_cluster_4` (Distance: 12.675 IQR)
- **Magnitude:** 625.3 | **LOC:** 665 | **CtrlFlow:** 19.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Tech Debt (99.4217%)
- **Heaviest Functions:** `call` (Impact: 283.4), `close` (Impact: 21.2), `poll` (Impact: 14.3)

### 8. `actix-http/src/config.rs` (RUST) -> Cumulative Risk: **778.38**
- **Archetype:** `file_cluster_4` (Distance: 12.987 IQR)
- **Magnitude:** 268.08 | **LOC:** 380 | **CtrlFlow:** 13.2% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Tech Debt (100.0%), Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `new` (Impact: 11.6), `write_date_header` (Impact: 9.7), `test_date_service_update` (Impact: 9.4)

### 9. `actix-web/src/response/builder.rs` (RUST) -> Cumulative Risk: **770.23**
- **Archetype:** `file_cluster_0` (Distance: 15.063 IQR)
- **Magnitude:** 430.04 | **LOC:** 555 | **CtrlFlow:** 22.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Injection Surface (100.0%), Concurrency (99.9978%)
- **Heaviest Functions:** `json` (Impact: 26.9), `streaming` (Impact: 25.3), `insert_header` (Impact: 16.2)

### 10. `actix-http-test/src/lib.rs` (RUST) -> Cumulative Risk: **766.07**
- **Archetype:** `file_cluster_4` (Distance: 15.027 IQR)
- **Magnitude:** 232.02 | **LOC:** 318 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Tech Debt (96.5285%)
- **Heaviest Functions:** `test_server_with_addr` (Impact: 13.6), `stop` (Impact: 12.6), `url` (Impact: 10.7)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `actix-http/src/h1/dispatcher.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.595 IQR)
- **Top Global Matches:** file_cluster_0: 13.595, file_cluster_11: 13.66, file_cluster_13: 13.721
- **Magnitude:** 2109.86 | **LOC:** 1319 | **CtrlFlow:** 45.9% | **Authorship Centralization:** 20.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 30
- **Risk Profile:** Cognitive Load (37.2459%), Tech Debt (8.8737%)
**Top Internal Functions/Classes:**
  * `handle_request` (Impact: 1308.6 | O(2^N) | DB: 30)
  * `poll_response` (Impact: 381.4 | O(N^6) | DB: 6)
  * `poll_flush` (Impact: 53.4 | O(2^N) | DB: 4)
  * `send_response` (Impact: 48.3 | O(N^5) | DB: 3)
  * `send_error_response` (Impact: 48.3 | O(N^5) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 158`, `structural_boundaries: 186`, `args: 25`, `func_start: 18`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 135`, `dead_code: 7`, `planned_debt: 3`
* *Architecture:* `api: 13`, `concurrency: 6`, `import: 13`
* *Defense:* `safety: 153`, `doc: 19`, `test: 6`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.304
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` net, pin::Pin, std::
    collections::VecDeque, Poll, Error, crate::
    body::BodySize, actix_service::Service, io...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `actix-http/tests/test_server.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.18 IQR)
- **Top Global Matches:** file_cluster_4: 12.18, file_cluster_0: 12.829, file_cluster_8: 12.853
- **Magnitude:** 1279.24 | **LOC:** 1024 | **CtrlFlow:** 12.9% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(N^6) | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (48.7696%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `content_length_truncated` (Impact: 45.1 | O(N^6) | DB: 10)
  * `h2_flow_control_window_sizes` (Impact: 44.8 | O(N^5) | DB: 5)
  * `expect_continue_h1` (Impact: 44.0 | O(N^6) | DB: 7)
  * `expect_continue` (Impact: 37.9 | O(N^5) | DB: 7)
  * `chunked_payload` (Impact: 33.3 | O(N^6) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 433`, `args: 97`, `func_start: 31`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 100`, `high_risk_execution: 2`, `state_mutation: 214`, `planned_debt: 3`, `fragile_debt: 1`, `duplicate_logic: 2`, `orphaned_logic: 29`
* *Architecture:* `concurrency: 557`, `import: 13`
* *Defense:* `safety: 33`, `doc: 2`, `test: 76`, `immutability_locks: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.304
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` KeepAlive, actix_rt::
    net::TcpStream, net, timeout, thread, Write, Error, regex::Regex...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `actix-http/src/h1/decoder.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.047 IQR)
- **Top Global Matches:** file_cluster_0: 13.047, file_cluster_8: 13.286, file_cluster_13: 13.3
- **Magnitude:** 1176.44 | **LOC:** 1186 | **CtrlFlow:** 24.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (44.7955%), Tech Debt (98.6649%)
**Top Internal Functions/Classes:**
  * `set_headers` (Impact: 341.3 | O(N^6) | DB: 7)
  * `decode` (Impact: 160.7 | O(N^6) | DB: 9)
  * `decode` (Impact: 129.0 | O(N^6) | DB: 11)
  * `decode` (Impact: 87.8 | O(N^6) | DB: 7)
  * `chunk` (Impact: 17.6 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 103`, `structural_boundaries: 322`, `args: 50`, `func_start: 56`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 60`, `state_mutation: 200`, `dead_code: 1`, `duplicate_logic: 12`, `orphaned_logic: 30`
* *Architecture:* `api: 20`, `concurrency: 5`, `import: 10`
* *Defense:* `safety: 118`, `doc: 27`, `test: 95`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.304
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` actix_codec::Decoder, Uri, ResponseHead, error, super::chunked::ChunkedState, tracing::debug, HttpMessage, trace...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `actix-web/src/introspection.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.562 IQR)
- **Top Global Matches:** file_cluster_0: 12.562, file_cluster_16: 12.664, file_cluster_8: 12.669
- **Magnitude:** 1120.54 | **LOC:** 1338 | **CtrlFlow:** 34.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (14.2191%), Tech Debt (47.8932%)
**Top Internal Functions/Classes:**
  * `has_conflicting_methods` (Impact: 120.2 | O(N^5) | DB: 9)
  * `shadowed_route_context` (Impact: 112.3 | O(N^6) | DB: 4)
  * `shadowed_scope_context` (Impact: 100.5 | O(N^6) | DB: 3)
  * `finalize` (Impact: 65.8 | O(N^6) | DB: 14)
    * *Intent:* /// Produces the finalized introspection tree.
  * `merge_guard_detail_reports` (Impact: 59.0 | O(N^5) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 124`, `structural_boundaries: 232`, `args: 66`, `func_start: 53`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 146`, `dead_code: 1`, `duplicate_logic: 5`, `orphaned_logic: 14`
* *Architecture:* `api: 54`, `import: 5`
* *Defense:* `safety: 124`, `doc: 75`, `test: 39`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.304
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` BTreeSet, std::sync::Once, serde::Serialize, http::Method, super::*, GuardDetail, std::
    collections::BTreeMap, fmt::Write...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `actix-web/src/server.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.004 IQR)
- **Top Global Matches:** file_cluster_0: 14.004, file_cluster_13: 14.134, file_cluster_4: 14.189
- **Magnitude:** 1040.92 | **LOC:** 1305 | **CtrlFlow:** 32.3% | **Authorship Centralization:** 40.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (20.4569%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `listen` (Impact: 99.7 | O(2^N) | DB: 2)
    * *Intent:* /// and IPv6 addresses that result from a DNS lookup. You can test this by passing /// `localhost:80...
  * `listen_openssl_inner` (Impact: 73.7 | O(N^6) | DB: 2)
  * `listen_rustls_0_20_inner` (Impact: 73.5 | O(N^6) | DB: 2)
    * *Intent:* /// Resolves socket address(es) and binds server to created listener(s) for TLS connections /// usin...
  * `listen_rustls_0_21_inner` (Impact: 73.5 | O(N^6) | DB: 2)
  * `listen_rustls_0_22_inner` (Impact: 73.5 | O(N^6) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 98`, `structural_boundaries: 205`, `args: 98`, `func_start: 42`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 52`, `dead_code: 6`
* *Architecture:* `io: 2`, `api: 50`, `concurrency: 64`, `import: 17`
* *Defense:* `safety: 157`, `doc: 330`, `sync_locks: 21`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.304
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` KeepAlive, net, Error, actix_service::
    map_config, sync::Arc, std::
    any::Any, io, cmp...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `actix-web/src/middleware/logger.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.682 IQR)
- **Top Global Matches:** file_cluster_0: 13.682, file_cluster_13: 13.735, file_cluster_4: 13.745
- **Magnitude:** 1018.42 | **LOC:** 1031 | **CtrlFlow:** 28.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (22.496%), Tech Debt (64.6054%)
**Top Internal Functions/Classes:**
  * `new` (Impact: 156.6 | O(2^N) | DB: 2)
  * `render_request` (Impact: 100.8 | O(N^6) | DB: 1)
  * `poll` (Impact: 62.9 | O(2^N) | DB: 4)
  * `call` (Impact: 45.1 | O(2^N) | DB: 2)
  * `new_transform` (Impact: 32.3 | O(N^5))
    * *Intent:* /// Register a function that receives a `ServiceResponse` and returns a string for use in the /// lo...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 100`, `structural_boundaries: 252`, `args: 55`, `func_start: 34`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 135`, `dead_code: 4`, `duplicate_logic: 10`
* *Architecture:* `api: 23`, `concurrency: 58`, `import: 17`
* *Defense:* `safety: 108`, `doc: 132`, `test: 13`, `immutability_locks: 5`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.304
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pin::Pin, time::format_description::well_known::Rfc3339, test::self, Poll, Error, actix_service::IntoService, TestRequest, regex::Regex...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `actix-web/tests/test_server.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.213 IQR)
- **Top Global Matches:** file_cluster_4: 12.213, file_cluster_0: 12.672, file_cluster_11: 12.951
- **Magnitude:** 896.52 | **LOC:** 909 | **CtrlFlow:** 14.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (49.7946%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_server_cookies` (Impact: 45.2 | O(N^6))
  * `test_data_drop` (Impact: 16.3 | O(N^3) | DB: 5)
    * *Intent:* // allow deprecated App::data
  * `body_gzip_large` (Impact: 14.5 | O(N^4) | DB: 1)
    * *Intent:* // .request(actix_web::http::Method::GET, srv.url("/raw")) // .no_decompress() // .append_header((AC...
  * `test_body_gzip_large_random` (Impact: 14.4 | O(N^4) | DB: 2)
  * `test_body_chunked_implicit` (Impact: 14.4 | O(N^4) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 314`, `args: 94`, `func_start: 36`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 69`, `state_mutation: 87`, `dead_code: 6`, `duplicate_logic: 2`, `orphaned_logic: 28`
* *Architecture:* `io: 1`, `concurrency: 419`, `import: 13`
* *Defense:* `safety: 43`, `test: 71`, `sync_locks: 1`, `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.304
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ServerConfig, pin::Pin, Write, Poll, Error, actix_web::http, time::Duration, io::Read...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `awc/src/client/connector.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.972 IQR)
- **Top Global Matches:** file_cluster_0: 12.972, file_cluster_16: 13.035, file_cluster_13: 13.058
- **Magnitude:** 833.84 | **LOC:** 1154 | **CtrlFlow:** 24.9% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (23.248%), Tech Debt (95.0133%)
**Top Internal Functions/Classes:**
  * `finish` (Impact: 140.8 | O(N^6) | DB: 3)
  * `into_connection_io` (Impact: 64.2 | O(2^N) | DB: 6)
  * `resolver` (Impact: 63.2 | O(2^N) | DB: 1)
  * `call` (Impact: 31.8 | O(2^N))
  * `build_tls` (Impact: 28.9 | O(N^6) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 217`, `args: 63`, `func_start: 48`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 68`, `dead_code: 2`, `duplicate_logic: 19`
* *Architecture:* `io: 5`, `api: 34`, `concurrency: 79`, `import: 34`
* *Defense:* `safety: 105`, `doc: 110`, `test: 3`, `immutability_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.304
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` name_server::TokioConnectionProvider, pin::Pin, actix_tls::connect::Connection, Poll, actix_tls::connect::openssl::reexports::AsyncSslStream, pool::ConnectionPool, actix_service::Service, actix_tls::connect::rustls_0_20::reexports::ClientConfig...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `awc/tests/test_client.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.709 IQR)
- **Top Global Matches:** file_cluster_4: 11.709, file_cluster_0: 12.143, file_cluster_8: 12.153
- **Magnitude:** 829.98 | **LOC:** 841 | **CtrlFlow:** 16.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (48.7221%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `client_cookie_handling` (Impact: 45.5 | O(N^6) | DB: 3)
  * `response_timeout` (Impact: 40.0 | O(N^6) | DB: 9)
  * `timeout` (Impact: 28.9 | O(2^N))
  * `with_query_parameter` (Impact: 22.6 | O(N^4))
  * `no_decompress` (Impact: 22.5 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 279`, `args: 92`, `func_start: 27`
* *Risk/State:* `safety_bypasses: 66`, `state_mutation: 55`, `orphaned_logic: 23`
* *Architecture:* `io: 5`, `concurrency: 318`, `import: 14`
* *Defense:* `safety: 54`, `test: 61`, `sync_locks: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.304
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` map_config, SampleString, Write, Error, actix_http::HttpService, actix_http_test::test_server, time::Duration, actix_utils::future::ok...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `actix-router/src/resource.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_0` (Drift: 17.532 IQR)
- **Top Global Matches:** file_cluster_0: 17.532, file_cluster_11: 17.81, file_cluster_13: 17.814
- **Magnitude:** 826.2 | **LOC:** 1781 | **CtrlFlow:** 17.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 23
- **Risk Profile:** Cognitive Load (15.7007%), Tech Debt (18.3176%)
**Top Internal Functions/Classes:**
  * `capture_match_info_fn` (Impact: 136.8 | O(N^6) | DB: 3)
    * *Intent:* /// Assigns a new name to the resource. /// /// # Panics /// Panics if `name` is an empty string. //...
  * `join` (Impact: 116.7 | O(2^N))
  * `pattern_iter` (Impact: 44.9 | O(N^6) | DB: 1)
  * `construct` (Impact: 32.7 | O(N^6) | DB: 3)
    * *Intent:* /// Returns `true` if `path` matches this resource. /// /// The behavior of this method depends on h...
  * `build_resource_path` (Impact: 27.7 | O(N^5) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 70`, `structural_boundaries: 326`, `args: 66`, `func_start: 57`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 31`, `state_mutation: 152`, `dead_code: 54`, `duplicate_logic: 4`
* *Architecture:* `api: 45`, `import: 15`
* *Defense:* `safety: 94`, `doc: 541`, `test: 305`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.304
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::
    path::PathItem, crate::Path, Regex, actix_router::Path, ResourceDef, std::
    borrow::Borrow, RegexSet, std::collections::HashMap...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `actix-multipart/src/form/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.338 IQR)
- **Top Global Matches:** file_cluster_4: 13.338, file_cluster_0: 13.469, file_cluster_16: 13.537
- **Magnitude:** 810.08 | **LOC:** 926 | **CtrlFlow:** 16.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (49.2141%), Tech Debt (99.4298%)
**Top Internal Functions/Classes:**
  * `from_request` (Impact: 65.3 | O(N^5) | DB: 7)
  * `try_consume_limits` (Impact: 41.6 | O(N^5) | DB: 1)
    * *Intent:* /// This function should be called within a [`FieldReader`] when reading each chunk of a field /// t...
  * `handle_field` (Impact: 38.4 | O(N^6) | DB: 2)
  * `handle_field` (Impact: 38.4 | O(N^6) | DB: 2)
  * `field_try_next_panic` (Impact: 23.9 | O(N^4) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 267`, `args: 73`, `func_start: 50`, `class_start: 23`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 87`, `dead_code: 1`, `planned_debt: 3`, `duplicate_logic: 9`, `orphaned_logic: 14`
* *Architecture:* `api: 25`, `concurrency: 248`, `import: 17`
* *Defense:* `safety: 101`, `doc: 67`, `test: 35`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.304
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` futures_util::TryStreamExt, Limits, future::ready, Error, DerefMut, actix_web::
        dev::Payload, sync::Arc, std::
    any::Any...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `actix-http/src/service.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.993 IQR)
- **Top Global Matches:** file_cluster_16: 11.993, file_cluster_13: 12.35, file_cluster_0: 12.412
- **Magnitude:** 766.94 | **LOC:** 1130 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (10.8863%), Tech Debt (15.5083%)
**Top Internal Functions/Classes:**
  * `new_service` (Impact: 98.7 | O(2^N))
  * `rustls_with_config` (Impact: 57.1 | O(N^6) | DB: 3)
  * `rustls_021_with_config` (Impact: 57.1 | O(N^6) | DB: 3)
  * `rustls_0_22_with_config` (Impact: 57.1 | O(N^6) | DB: 3)
  * `rustls_0_23_with_config` (Impact: 57.1 | O(N^6) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 197`, `args: 50`, `func_start: 28`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 48`, `dead_code: 2`, `duplicate_logic: 3`
* *Architecture:* `io: 4`, `api: 39`, `concurrency: 68`, `import: 27`
* *Defense:* `safety: 94`, `doc: 64`, `immutability_locks: 76`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.304
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` net, actix_tls::accept::
        rustls_0_23::reexports::ServerConfig, pin::Pin, actix_rt::net::TcpStream, Poll, builder::HttpServiceBuilder, actix_service::ServiceFactoryExt, actix_http::HttpService...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `actix-web/src/request.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.734 IQR)
- **Top Global Matches:** file_cluster_0: 14.734, file_cluster_4: 15.037, file_cluster_11: 15.099
- **Magnitude:** 760.34 | **LOC:** 1249 | **CtrlFlow:** 19.5% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (17.0697%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `fmt` (Impact: 166.1 | O(2^N) | DB: 1)
  * `cookies` (Impact: 63.4 | O(2^N) | DB: 1)
    * *Intent:* /// Generates URL for a named resource. /// /// This substitutes in sequence all URL parameters that...
  * `cookie` (Impact: 35.2 | O(2^N))
    * *Intent:* /// Generates URL for a named resource using a map of dynamic segment values. /// /// This substitut...
  * `app_data` (Impact: 24.5 | O(2^N))
    * *Intent:* /// Returns a reference a piece of connection data set in an [on-connect] callback. /// /// ```ignor...
  * `test_data` (Impact: 23.3 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 219`, `args: 79`, `func_start: 58`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 46`, `dead_code: 20`
* *Architecture:* `api: 62`, `concurrency: 61`, `import: 12`
* *Defense:* `safety: 89`, `doc: 221`, `test: 84`, `immutability_locks: 5`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.304
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` net, test::self, crate::
        dev::ResourceDef, Error, TestRequest, Uri, actix_router::Path, smallvec::SmallVec...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `actix-web-actors/src/ws.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.392 IQR)
- **Top Global Matches:** file_cluster_16: 13.392, file_cluster_4: 13.653, file_cluster_13: 13.708
- **Magnitude:** 735.82 | **LOC:** 1053 | **CtrlFlow:** 25.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (37.5613%), Tech Debt (58.094%)
**Top Internal Functions/Classes:**
  * `poll_next` (Impact: 147.7 | O(2^N) | DB: 5)
  * `handshake_with_protocols` (Impact: 89.0 | O(N^4) | DB: 1)
  * `poll_next` (Impact: 53.2 | O(N^4) | DB: 5)
  * `start_with_addr` (Impact: 18.9 | O(N^5) | DB: 2)
  * `waiting` (Impact: 15.9 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 169`, `args: 47`, `func_start: 38`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 75`, `duplicate_logic: 9`
* *Architecture:* `api: 30`, `concurrency: 116`, `import: 13`
* *Defense:* `safety: 110`, `doc: 198`, `test: 18`, `immutability_locks: 14`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.304
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` actix_http::ws::hash_key, HttpResponseBuilder, actix_http::ws::CloseCode, ProtocolError, StreamHandler, pin::Pin, std::
    collections::VecDeque, actix_web::get...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `actix-web-codegen/src/route.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.027 IQR)
- **Top Global Matches:** file_cluster_17: 12.027, file_cluster_0: 12.036, file_cluster_8: 12.074
- **Magnitude:** 711.38 | **LOC:** 555 | **CtrlFlow:** 39.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (9.2334%), Tech Debt (99.2863%)
**Top Internal Functions/Classes:**
  * `new` (Impact: 307.6 | O(2^N) | DB: 4)
  * `parse` (Impact: 81.9 | O(2^N) | DB: 1)
  * `new` (Impact: 41.8 | O(2^N))
  * `with_methods` (Impact: 38.3 | O(N^5) | DB: 1)
  * `to_tokens` (Impact: 34.0 | O(N^6) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 98`, `args: 29`, `func_start: 18`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 25`, `dead_code: 2`, `planned_debt: 1`, `duplicate_logic: 9`
* *Architecture:* `api: 13`, `import: 8`
* *Defense:* `safety: 84`, `doc: 11`, `test: 2`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.304
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ToTokens, Ident, LitStr, quote::quote, Path, actix_router::ResourceDef, TokenStream, proc_macro2::Span...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `actix-http/src/encoding/encoder.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.53 IQR)
- **Top Global Matches:** file_cluster_0: 13.53, file_cluster_13: 13.86, file_cluster_11: 13.899
- **Magnitude:** 691.98 | **LOC:** 440 | **CtrlFlow:** 40.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (28.3686%), Tech Debt (81.9164%)
**Top Internal Functions/Classes:**
  * `poll_next` (Impact: 297.6 | O(2^N) | DB: 6)
  * `response` (Impact: 56.0 | O(N^5) | DB: 1)
  * `finish` (Impact: 53.3 | O(2^N) | DB: 1)
  * `try_into_bytes` (Impact: 40.9 | O(2^N) | DB: 1)
  * `poll_next` (Impact: 40.8 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 83`, `args: 26`, `func_start: 17`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 58`, `dead_code: 1`, `duplicate_logic: 6`
* *Architecture:* `api: 7`, `concurrency: 6`, `import: 11`
* *Defense:* `safety: 134`, `doc: 3`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.304
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` header::self, pin::Pin, Write, Poll, ResponseHead, std::
    error::Error, tracing::trace, CONTENT_ENCODING...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `awc/src/middleware/redirect.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.534 IQR)
- **Top Global Matches:** file_cluster_8: 11.534, file_cluster_0: 11.558, file_cluster_4: 11.581
- **Magnitude:** 679.2 | **LOC:** 681 | **CtrlFlow:** 31.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (28.4958%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `poll` (Impact: 186.9 | O(2^N) | DB: 8)
  * `test_redirect_cross_origin_headers` (Impact: 60.4 | O(N^5))
  * `call` (Impact: 50.5 | O(2^N))
  * `build_next_uri` (Impact: 36.6 | O(N^4) | DB: 1)
  * `test_redirect_headers` (Impact: 34.1 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 149`, `args: 38`, `func_start: 29`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 41`, `state_mutation: 34`, `dead_code: 1`
* *Architecture:* `api: 16`, `concurrency: 54`, `import: 11`
* *Defense:* `safety: 49`, `test: 23`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.304
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pin::Pin, Poll, ConnectResponse, Error, Uri, actix_service::Service, net::SocketAddr, actix_http::header...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `actix-multipart/src/field.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.57 IQR)
- **Top Global Matches:** file_cluster_4: 14.57, file_cluster_0: 14.703, file_cluster_13: 14.722
- **Magnitude:** 654.26 | **LOC:** 502 | **CtrlFlow:** 43.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (36.0825%), Tech Debt (8.6901%)
**Top Internal Functions/Classes:**
  * `read_stream` (Impact: 220.7 | O(N^6) | DB: 2)
  * `fmt` (Impact: 76.9 | O(2^N) | DB: 1)
  * `read_len` (Impact: 64.3 | O(N^6) | DB: 3)
  * `poll` (Impact: 54.4 | O(N^5) | DB: 5)
  * `bytes` (Impact: 38.3 | O(N^5) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 75`, `structural_boundaries: 97`, `args: 17`, `func_start: 13`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 61`, `dead_code: 3`, `planned_debt: 1`
* *Architecture:* `api: 15`, `concurrency: 44`, `import: 9`
* *Defense:* `safety: 113`, `doc: 57`, `test: 4`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.304
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ContentDisposition, pin::Pin, HeaderMap, Poll, Error, http::header::self, Context, safety::Safety...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `actix-http/src/h1/encoder.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.11%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.41 IQR)
- **Top Global Matches:** file_cluster_4: 12.41, file_cluster_0: 12.437, file_cluster_8: 12.532
- **Magnitude:** 630.08 | **LOC:** 688 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (44.287%), Tech Debt (99.824%)
**Top Internal Functions/Classes:**
  * `encode_headers` (Impact: 183.0 | O(N^6) | DB: 7)
  * `encode` (Impact: 94.5 | O(N^6) | DB: 3)
  * `encode` (Impact: 56.1 | O(N^5) | DB: 4)
  * `encode_eof` (Impact: 22.7 | O(N^4) | DB: 3)
  * `write_headers` (Impact: 11.2 | O(N^5) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 120`, `args: 28`, `func_start: 36`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 75`, `dead_code: 1`, `duplicate_logic: 18`
* *Architecture:* `api: 20`, `concurrency: 44`, `import: 8`
* *Defense:* `safety: 55`, `doc: 19`, `test: 25`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.304
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` UPGRADE_INSECURE_REQUESTS, HeaderMap, TRANSFER_ENCODING, Write, http::header::AUTHORIZATION, crate::
    body::BodySize, helpers, Response...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `actix-web/src/service.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.478 IQR)
- **Top Global Matches:** file_cluster_0: 13.478, file_cluster_4: 13.811, file_cluster_11: 13.855
- **Magnitude:** 625.58 | **LOC:** 926 | **CtrlFlow:** 25.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (25.4012%), Tech Debt (99.9904%)
**Top Internal Functions/Classes:**
  * `fmt` (Impact: 104.9 | O(2^N) | DB: 1)
    * *Intent:* /// Counterpart to [`HttpRequest::app_data`].
  * `fmt` (Impact: 42.3 | O(2^N) | DB: 1)
  * `register` (Impact: 25.2 | O(N^3) | DB: 4)
  * `test_services_vec` (Impact: 19.1 | O(N^3))
    * *Intent:* /// Macro to help register different types of services at the same time. /// /// The max number of s...
  * `test_services_macro` (Impact: 14.8 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 156`, `args: 81`, `func_start: 64`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 51`, `dead_code: 8`, `planned_debt: 2`, `duplicate_logic: 19`
* *Architecture:* `api: 61`, `concurrency: 52`, `import: 11`
* *Defense:* `safety: 45`, `doc: 123`, `test: 28`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.304
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` BoxedPayloadStream, net, test::self, Path, Error, TestRequest, Uri, ResponseHead...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `awc/src/client/pool.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.675 IQR)
- **Top Global Matches:** file_cluster_4: 12.675, file_cluster_16: 12.844, file_cluster_13: 12.866
- **Magnitude:** 625.3 | **LOC:** 665 | **CtrlFlow:** 19.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (46.2644%), Tech Debt (99.4217%)
**Top Internal Functions/Classes:**
  * `call` (Impact: 283.4 | O(2^N) | DB: 5)
  * `close` (Impact: 21.2 | O(N^5))
    * *Intent:* /// Spawns a graceful shutdown task for the underlying I/O with a timeout.
  * `poll` (Impact: 14.3 | O(2^N) | DB: 2)
  * `test_pool_drop` (Impact: 12.8 | O(N^2) | DB: 1)
  * `drop` (Impact: 12.6 | O(N^5) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 209`, `args: 29`, `func_start: 24`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 72`, `dead_code: 1`, `duplicate_logic: 12`, `orphaned_logic: 9`
* *Architecture:* `api: 7`, `concurrency: 95`, `import: 14`
* *Defense:* `safety: 64`, `doc: 27`, `test: 22`, `sync_locks: 4`, `immutability_locks: 12`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.304
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Semaphore, pin::Pin, Poll, sync::Arc, actix_service::Service, io, http::uri::Authority, http::Uri...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `actix-web/src/types/json.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.41 IQR)
- **Top Global Matches:** file_cluster_4: 14.41, file_cluster_0: 14.634, file_cluster_11: 14.772
- **Magnitude:** 623.16 | **LOC:** 771 | **CtrlFlow:** 18.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (49.7431%), Tech Debt (96.9789%)
**Top Internal Functions/Classes:**
  * `poll` (Impact: 50.0 | O(N^6) | DB: 5)
  * `limit` (Impact: 49.9 | O(2^N))
  * `poll` (Impact: 49.7 | O(2^N) | DB: 3)
  * `new` (Impact: 37.5 | O(N^4) | DB: 1)
    * *Intent:* /// Sets whether or not the request must have a `Content-Type` header to be parsed.
  * `respond_to` (Impact: 13.7 | O(N^4) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 167`, `args: 38`, `func_start: 28`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 59`, `dead_code: 13`, `planned_debt: 2`, `duplicate_logic: 4`, `orphaned_logic: 12`
* *Architecture:* `api: 12`, `concurrency: 222`, `import: 11`
* *Defense:* `safety: 58`, `doc: 106`, `test: 21`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.304
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` pin::Pin, actix_web::error, Poll, extract::FromRequest, TestRequest, sync::Arc, http::
            header::self, serde::Deserialize...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `actix-http/src/header/map.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_0` (Drift: 17.297 IQR)
- **Top Global Matches:** file_cluster_0: 17.297, file_cluster_11: 17.498, file_cluster_13: 17.499
- **Magnitude:** 619.48 | **LOC:** 1206 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (13.3058%), Tech Debt (99.9996%)
**Top Internal Functions/Classes:**
  * `next` (Impact: 51.0 | O(2^N) | DB: 3)
    * *Intent:* /// Returns true if iterator contains no elements, without consuming it. ///
  * `next` (Impact: 49.1 | O(2^N) | DB: 2)
  * `next` (Impact: 49.0 | O(2^N) | DB: 2)
  * `get_mut` (Impact: 21.1 | O(2^N) | DB: 2)
    * *Intent:* /// /// The number of values stored will be at least this number. See also: [`Self::len`]. /// /// #...
  * `append` (Impact: 20.5 | O(2^N) | DB: 2)
    * *Intent:* /// /// # Examples /// ``` /// # use actix_http::header::{self, HeaderMap, HeaderValue}; /// let mut...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 62`, `structural_boundaries: 240`, `args: 73`, `func_start: 62`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 114`, `dead_code: 42`, `planned_debt: 1`, `duplicate_logic: 28`, `orphaned_logic: 12`
* *Architecture:* `api: 29`, `import: 20`
* *Defense:* `safety: 78`, `doc: 458`, `test: 126`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.304
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` super::AsHeaderName, std::borrow::Cow, http::header::HeaderName, std::iter::FusedIterator, static_assertions::assert_impl_all, SmallVec, iter, ops...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `actix-web/src/scope.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.575 IQR)
- **Top Global Matches:** file_cluster_4: 13.575, file_cluster_0: 13.592, file_cluster_11: 13.931
- **Magnitude:** 605.54 | **LOC:** 1257 | **CtrlFlow:** 6.5% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (37.2844%), Tech Debt (17.6922%)
**Top Internal Functions/Classes:**
  * `register` (Impact: 76.7 | O(2^N) | DB: 15)
  * `new_service` (Impact: 32.9 | O(2^N) | DB: 2)
  * `call` (Impact: 27.0 | O(2^N) | DB: 2)
  * `can_be_returned_from_fn` (Impact: 19.0 | O(N^4))
  * `test_middleware_body_type` (Impact: 16.7 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 319`, `args: 78`, `func_start: 39`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 40`, `state_mutation: 37`, `dead_code: 17`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 34`, `concurrency: 170`, `import: 12`
* *Defense:* `safety: 68`, `doc: 174`, `test: 62`, `immutability_locks: 7`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.304
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` apply_fn_factory, middleware::DefaultHeaders, Route, HttpServiceFactory, Error, rmap::ResourceMap, TestRequest, http::
            header::self...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `actix-http/tests/test_rustls.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.171 IQR)
- **Top Global Matches:** file_cluster_4: 12.171, file_cluster_0: 12.61, file_cluster_8: 12.623
- **Magnitude:** 602.12 | **LOC:** 695 | **CtrlFlow:** 10.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (48.1605%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `h2_content_length` (Impact: 29.1 | O(N^5) | DB: 1)
  * `h2_headers` (Impact: 20.3 | O(N^6) | DB: 2)
  * `load_body` (Impact: 17.1 | O(N^3) | DB: 1)
  * `h2_body1` (Impact: 14.0 | O(N^4) | DB: 2)
  * `h2_response_http_error_handling` (Impact: 13.6 | O(N^6) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 245`, `args: 77`, `func_start: 29`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 50`, `state_mutation: 89`, `orphaned_logic: 19`
* *Architecture:* `api: 1`, `concurrency: 234`, `import: 15`
* *Defense:* `safety: 45`, `test: 49`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.304
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ServerConfig, header::self, actix_rt::net::TcpStream, fn_service, Write, Error, sync::Arc, poll_fn...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `actix-router/src/path.rs` (RUST) | Magnitude: 245.34 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 205, structural_boundaries: 66, generics: 41, state_mutation: 37
- `actix-web/src/test/mod.rs` (RUST) | Magnitude: 11.1 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 34, indent_spaces: 25, structural_boundaries: 17, import: 8
- `actix-http/src/body/boxed.rs` (RUST) | Magnitude: 137.44 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 84, safety: 31, structural_boundaries: 30, state_mutation: 17
- `actix-web/src/thin_data.rs` (RUST) | Magnitude: 50.02 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 53, doc: 39, structural_boundaries: 24, concurrency: 18
- `actix-http/src/body/either.rs` (RUST) | Magnitude: 73.96 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 69, doc: 19, structural_boundaries: 18, generics: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `scripts/bump` (SHELL) | Magnitude: 176.42 | Delta: **0.061 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: state_mutation: 72, indent_spaces: 54, branch: 46, io: 45

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `actix-http/src/http_message.rs` (RUST) | Magnitude: 231.16 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 172, structural_boundaries: 58, safety: 46, concurrency: 30
- `actix-http/src/header/shared/quality_item.rs` (RUST) | Magnitude: 87.38 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 148, structural_boundaries: 38, doc: 35, safety: 26
- `actix-web/src/http/header/mod.rs` (RUST) | Magnitude: 20.3 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 40, structural_boundaries: 37, doc: 8, api: 6
- `actix-web/src/http/header/allow.rs` (RUST) | Magnitude: 15.56 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 42, indent_spaces: 24, dead_code: 6, safety: 3
- `actix-http/src/body/sized_stream.rs` (RUST) | Magnitude: 44.84 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 107, structural_boundaries: 36, safety: 28, generics: 22

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `actix-http/src/test.rs` (RUST) | Magnitude: 395.72 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 271, state_mutation: 106, structural_boundaries: 98, safety: 74
- `awc/src/sender.rs` (RUST) | Magnitude: 245.66 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 223, safety: 75, structural_boundaries: 53, generics: 34
- `actix-http/src/h1/utils.rs` (RUST) | Magnitude: 186.58 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 98, structural_boundaries: 29, branch: 26, safety: 22
- `actix-http/src/header/into_pair.rs` (RUST) | Magnitude: 57.96 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 66, structural_boundaries: 34, generics: 20, branch: 15
- `actix-web/src/error/response_error.rs` (RUST) | Magnitude: 55.96 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 71, structural_boundaries: 26, generics: 20, branch: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `actix-web-codegen/src/route.rs` (RUST) | Magnitude: 711.38 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 420, structural_boundaries: 98, safety: 84, branch: 63
- `actix-router/src/pattern.rs` (RUST) | Magnitude: 73.6 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 46, structural_boundaries: 14, args: 14, generics: 12
- `scripts/unreleased` (SHELL) | Magnitude: 56.06 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 28, indent_spaces: 24, safety_bypasses: 10, io: 10
- `actix-web/src/http/header/cache_control.rs` (RUST) | Magnitude: 76.86 | Delta: **0.134 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 101, doc: 54, safety: 45, structural_boundaries: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `actix-multipart/src/form/text.rs` (RUST) | Magnitude: 232.88 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 110, structural_boundaries: 51, concurrency: 40, generics: 22
- `actix-web/src/request_data.rs` (RUST) | Magnitude: 85.64 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 97, doc: 41, structural_boundaries: 35, concurrency: 19
- `actix-web/src/middleware/err_handlers.rs` (RUST) | Magnitude: 255.72 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 331, doc: 172, structural_boundaries: 120, generics: 94
- `actix-web/src/scope.rs` (RUST) | Magnitude: 605.54 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 824, structural_boundaries: 319, doc: 174, concurrency: 170
- `actix-http/src/h2/dispatcher.rs` (RUST) | Magnitude: 533.5 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 239, structural_boundaries: 82, safety: 48, branch: 43

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `actix-web/src/http/header/accept_charset.rs` (RUST) | Magnitude: 13.64 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 53, dead_code: 6, indent_spaces: 4, sec_dead_code: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `actix-web-actors/src/lib.rs` (RUST) | Magnitude: 15.12 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 62, structural_boundaries: 3, decorators: 3, api: 2
- `actix-web/src/middleware/mod.rs` (RUST) | Magnitude: 15.54 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 244, indent_spaces: 26, structural_boundaries: 6, args: 2
- `actix-multipart/src/lib.rs` (RUST) | Magnitude: 21.36 | Delta: **0.123 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 65, structural_boundaries: 9, api: 6, encapsulation: 6
- `actix-http/src/header/common.rs` (RUST) | Magnitude: 24.26 | Delta: **0.124 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 34, api: 9, immutability_locks: 9, encapsulation: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `actix-files/src/error.rs` (RUST) | Magnitude: 8.04 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 19, doc: 10, decorators: 10, structural_boundaries: 6
- `actix-http/examples/h2c-detect.rs` (RUST) | Magnitude: 40.86 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 17, doc: 7, structural_boundaries: 5, safety: 4
- `awc/src/middleware/redirect.rs` (RUST) | Magnitude: 679.2 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 537, structural_boundaries: 149, branch: 69, concurrency: 54
- `awc/src/client/config.rs` (RUST) | Magnitude: 19.64 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 27, api: 11, encapsulation: 11, structural_boundaries: 6
- `actix-files/src/service.rs` (RUST) | Magnitude: 540.0 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 245, structural_boundaries: 89, safety: 80, branch: 48

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `actix-web/tests/test_weird_poll.rs` (RUST) | Magnitude: 10.52 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: dead_code: 14, doc: 1
- `actix-web/tests/weird_poll.rs` (RUST) | Magnitude: 10.52 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: dead_code: 14, doc: 1
- `actix-web/src/http/header/if_match.rs` (RUST) | Magnitude: 15.38 | Delta: **0.054 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 51, indent_spaces: 16, dead_code: 4, safety: 3
- `actix-web/src/http/header/etag.rs` (RUST) | Magnitude: 16.02 | Delta: **0.057 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 48, doc: 43, safety: 15, dead_code: 7

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `actix-web/src/introspection.rs` -> **Guillermo Céspedes Tabárez** (100.0% isolated ownership) | Magnitude: 1120.54
- `actix-web/tests/test_server.rs` -> **Yuki Okushi** (100.0% isolated ownership) | Magnitude: 896.52
- `actix-multipart/src/form/mod.rs` -> **fasilmveloor** (100.0% isolated ownership) | Magnitude: 810.08
- `actix-http/src/service.rs` -> **Yuki Okushi** (100.0% isolated ownership) | Magnitude: 766.94
- `actix-http/src/encoding/encoder.rs` -> **Yuki Okushi** (100.0% isolated ownership) | Magnitude: 691.98

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `actix-web/src/types/header.rs` -> **Severity: 0.011** (Bridge: 0.0001 * Flux: 97.6133%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `awc/src/responses/read_body.rs` -> **Severity: 1.25** (Embedded: 0.0301 * Error Risk: 41.5116%)
- `actix-web/src/types/header.rs` -> **Severity: 0.708** (Embedded: 0.0181 * Error Risk: 39.1689%)
- `actix-web/src/dev.rs` -> **Severity: 0.674** (Embedded: 0.012 * Error Risk: 55.9714%)
- `actix-http/src/notify_on_drop.rs` -> **Severity: 0.134** (Embedded: 0.003 * Error Risk: 44.3637%)
- `actix-http/src/body/boxed.rs` -> **Severity: 0.115** (Embedded: 0.009 * Error Risk: 12.6987%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `actix-web/src/web.rs` -> **Severity: 1836.71** (Blast Radius: 102.722 * Doc Risk: 17.8804%)
- `awc/src/responses/read_body.rs` -> **Severity: 1160.365** (Blast Radius: 11.604 * Doc Risk: 99.997%)
- `actix-web/src/dev.rs` -> **Severity: 556.699** (Blast Radius: 5.567 * Doc Risk: 99.9998%)
- `actix-http/src/notify_on_drop.rs` -> **Severity: 423.487** (Blast Radius: 4.261 * Doc Risk: 99.3867%)
- `awc/src/client/h1proto.rs` -> **Severity: 328.3** (Blast Radius: 3.283 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
