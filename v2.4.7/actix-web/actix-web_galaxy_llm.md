# ARCHITECTURAL_BRIEF: actix-web
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_rust/actix-web` |
| **Timestamp** | `2026-08-07T04:04:29.791789+00:00` |
| **Scan Duration** | `1.28s` |
| **Git Branch** | `main` |
| **Git Commit** | `4702c0fdf97f796a38e45a9c1f8306ea08d79f1b` |
| **Git Remote** | `https://github.com/actix/actix-web.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 285 malicious artifacts.

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
> **Architectural Drift Z-Score:** `3.398`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_0 | 87 | 26.1% |
| file_cluster_4 | 60 | 18.0% |
| file_cluster_8 | 44 | 13.2% |
| file_cluster_13 | 42 | 12.6% |
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
| Cognitive Load Exposure | 0.0 | 100.0 | 23.5 | 16.5 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 28.9 | 24.3 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 39.7 | 15.5 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 3.2 | 2.3 | 0.0 |
| API Exposure | 0.0 | 8.7 | 3.5 | 3.8 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 51.3 | 66.4 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 38.1 | 25.7 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 14.7 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 96.7 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 7.2 | 0.9 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 58.0 | 4.8 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 20.5 | 13.5 | 0.0 |
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

- `handle_request` (@ `actix-http/src/h1/dispatcher.rs`) -> Impact: **183.1** | LOC: 502
- `poll_response` (@ `actix-http/src/h1/dispatcher.rs`) -> Impact: **98.7** | LOC: 208
- `set_headers` (@ `actix-http/src/h1/decoder.rs`) -> Impact: **92.7** | LOC: 139
- `call` (@ `actix-http/src/h1/dispatcher_tests.rs`) -> Impact: **88.4** | LOC: 972
- `read_available` (@ `actix-http/src/h1/dispatcher.rs`) -> Impact: **75.6** | LOC: 195
- `start_with` (@ `actix-test/src/lib.rs`) -> Impact: **68.3** | LOC: 362
  * *Intent:* /// Start default [`TestServer`]. /// /// # Examples /// ``` /// use actix_web::{get, web, test, App, HttpResponse, Error, Responder};
- `from_raw` (@ `actix-web/src/http/header/content_disposition.rs`) -> Impact: **68.3** | LOC: 87
  * *Intent:* /// Parse a raw Content-Disposition header value.
- `connect` (@ `awc/src/ws.rs`) -> Impact: **67.4** | LOC: 171
- `read_stream` (@ `actix-multipart/src/field.rs`) -> Impact: **65.7** | LOC: 73
- `send_request` (@ `awc/src/client/h1proto.rs`) -> Impact: **65.1** | LOC: 140

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `actix-web/src` | 23 | 4205.18 | 20.27% | 45.92% |
| `actix-http/src/h1` | 14 | 2844.56 | 31.58% | 49.29% |
| `actix-http/tests` | 6 | 2019.24 | 48.02% | 0.0% |
| `actix-web/src/types` | 10 | 1593.82 | 36.32% | 28.49% |
| `actix-http/src` | 14 | 1575.16 | 25.21% | 52.79% |
| `awc/src/client` | 8 | 1453.86 | 34.7% | 74.22% |
| `actix-web/src/middleware` | 11 | 1354.18 | 22.46% | 51.23% |
| `actix-files/src` | 10 | 1297.22 | 25.69% | 45.44% |
| `actix-router/src` | 10 | 1259.98 | 14.36% | 54.78% |
| `actix-web/src/http/header` | 27 | 1234.46 | 5.35% | 25.84% |

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
- `actix-router/src/de.rs` -> **19** Orphaned Functions | **16** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`actix-files/src/path_buf.rs`** -> AI Confidence: **99.31%**
2. **`actix-http/src/h1/utils.rs`** -> AI Confidence: **99.31%**
3. **`actix-http/src/header/shared/content_encoding.rs`** -> AI Confidence: **99.31%**
4. **`actix-http/src/header/shared/quality.rs`** -> AI Confidence: **99.31%**
5. **`actix-http/src/requests/head.rs`** -> AI Confidence: **99.31%**
6. **`actix-web/examples/basic.rs`** -> AI Confidence: **99.31%**
7. **`actix-web/examples/uds.rs`** -> AI Confidence: **99.31%**
8. **`actix-web/src/http/header/content_range.rs`** -> AI Confidence: **99.31%**
9. **`actix-files/src/directory.rs`** -> AI Confidence: **99.24%**
10. **`actix-http/src/encoding/decoder.rs`** -> AI Confidence: **99.24%**
11. **`actix-http/src/encoding/encoder.rs`** -> AI Confidence: **99.24%**
12. **`actix-http/src/h1/client.rs`** -> AI Confidence: **99.24%**
13. **`actix-http/src/h1/dispatcher.rs`** -> AI Confidence: **99.24%**
14. **`actix-http/src/ws/codec.rs`** -> AI Confidence: **99.24%**
15. **`actix-multipart/src/field.rs`** -> AI Confidence: **99.24%**
16. **`actix-web-codegen/src/route.rs`** -> AI Confidence: **99.24%**
17. **`actix-web/src/error/response_error.rs`** -> AI Confidence: **99.24%**
18. **`actix-web/src/guard/acceptable.rs`** -> AI Confidence: **99.24%**
19. **`actix-web-codegen/src/scope.rs`** -> AI Confidence: **99.23%**
20. **`actix-web/src/http/header/entity.rs`** -> AI Confidence: **99.23%**
21. **`awc/src/client/error.rs`** -> AI Confidence: **99.23%**
22. **`actix-files/src/chunked.rs`** -> AI Confidence: **99.18%**
23. **`actix-files/src/files.rs`** -> AI Confidence: **99.18%**
24. **`actix-files/src/named.rs`** -> AI Confidence: **99.18%**
25. **`actix-http/examples/actix-web.rs`** -> AI Confidence: **99.18%**
26. **`actix-http/examples/bench.rs`** -> AI Confidence: **99.18%**
27. **`actix-http/examples/echo.rs`** -> AI Confidence: **99.18%**
28. **`actix-http/src/body/either.rs`** -> AI Confidence: **99.18%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `5272` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `actix-http/src/date.rs` (RUST) -> Cumulative Risk: **617.76**
- **Archetype:** `file_cluster_4` (Distance: 11.435 IQR)
- **Magnitude:** 57.84 | **LOC:** 93 | **CtrlFlow:** 12.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9997%), Tech Debt (98.8393%), State Flux (94.6737%)
- **Heaviest Functions:** `new` (Impact: 4.5), `update` (Impact: 2.2), `drop` (Impact: 2.2)

### 2. `actix-http-test/src/lib.rs` (RUST) -> Cumulative Risk: **613.67**
- **Archetype:** `file_cluster_4` (Distance: 15.027 IQR)
- **Magnitude:** 165.82 | **LOC:** 318 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Tech Debt (96.5285%), Verification (80.0%)
- **Heaviest Functions:** `test_server_with_addr` (Impact: 7.6), `url` (Impact: 5.5), `surl` (Impact: 5.5)

### 3. `actix-web/src/extract.rs` (RUST) -> Cumulative Risk: **564.62**
- **Archetype:** `file_cluster_4` (Distance: 18.822 IQR)
- **Magnitude:** 300.88 | **LOC:** 556 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Tech Debt (99.9767%), Dead Code (87.2548%)
- **Heaviest Functions:** `poll` (Impact: 11.9), `poll` (Impact: 5.7), `test_result` (Impact: 5.3)

### 4. `actix-http/src/h1/payload.rs` (RUST) -> Cumulative Risk: **563.08**
- **Archetype:** `file_cluster_4` (Distance: 13.716 IQR)
- **Magnitude:** 260.2 | **LOC:** 352 | **CtrlFlow:** 24.2% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Tech Debt (99.9964%), State Flux (99.8457%)
- **Heaviest Functions:** `poll_next` (Impact: 16.8), `prepare_waking_test` (Impact: 9.9), `need_read` (Impact: 9.5)

### 5. `scripts/unreleased` (SHELL) -> Cumulative Risk: **560.43**
- **Archetype:** `file_cluster_17` (Distance: 15.579 IQR)
- **Magnitude:** 54.66 | **LOC:** 53 | **CtrlFlow:** 68.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Cognitive Load (99.9793%), Safety Score (99.6452%)
- **Heaviest Functions:** `unreleased_for` (Impact: 20.3), `Anonymous_Block` (Impact: 4.2), `__global_context__` (Impact: 1.5)

### 6. `awc/src/client/connection.rs` (RUST) -> Cumulative Risk: **556.36**
- **Archetype:** `file_cluster_16` (Distance: 12.652 IQR)
- **Magnitude:** 255.24 | **LOC:** 455 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (98.8304%), Concurrency (98.4313%)
- **Heaviest Functions:** `test_h2_connection_drop` (Impact: 16.9), `poll` (Impact: 9.7), `open_tunnel` (Impact: 9.3)

### 7. `actix-http/src/h1/encoder.rs` (RUST) -> Cumulative Risk: **548.37**
- **Archetype:** `file_cluster_4` (Distance: 12.46 IQR)
- **Magnitude:** 329.98 | **LOC:** 688 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.824%), Concurrency (98.9967%), State Flux (96.9369%)
- **Heaviest Functions:** `encode_headers` (Impact: 55.8), `encode` (Impact: 28.1), `encode` (Impact: 20.1)

### 8. `actix-files/src/chunked.rs` (RUST) -> Cumulative Risk: **548.08**
- **Archetype:** `file_cluster_4` (Distance: 12.563 IQR)
- **Magnitude:** 153.26 | **LOC:** 245 | **CtrlFlow:** 28.0% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9999%), State Flux (99.0929%), Tech Debt (94.8764%)
- **Heaviest Functions:** `chunked_read_file_callback` (Impact: 13.1), `chunked_read_file_callback_sync` (Impact: 12.2), `poll_next` (Impact: 10.6)

### 9. `scripts/bump` (SHELL) -> Cumulative Risk: **546.44**
- **Archetype:** `file_cluster_11` (Distance: 13.862 IQR)
- **Magnitude:** 182.82 | **LOC:** 174 | **CtrlFlow:** 77.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Cognitive Load (99.9318%)
- **Heaviest Functions:** `Anonymous_Block_[Truncated]` (Impact: 45.0), `__global_context__` (Impact: 17.9), `Anonymous_Block` (Impact: 8.9)

### 10. `actix-router/src/path.rs` (RUST) -> Cumulative Risk: **544.01**
- **Archetype:** `file_cluster_0` (Distance: 12.29 IQR)
- **Magnitude:** 160.74 | **LOC:** 313 | **CtrlFlow:** 28.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (96.4514%), Tech Debt (83.6475%)
- **Heaviest Functions:** `update_with_reindex` (Impact: 15.7), `get` (Impact: 7.6), `next` (Impact: 6.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `actix-http/tests/test_server.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.18 IQR)
- **Top Global Matches:** file_cluster_4: 12.18, file_cluster_0: 12.829, file_cluster_8: 12.853
- **Magnitude:** 996.04 | **LOC:** 1024 | **CtrlFlow:** 12.9% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (48.7682%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `h2_flow_control_window_sizes` (Impact: 17.1)
  * `content_length_truncated` (Impact: 14.8)
  * `expect_continue_h1` (Impact: 13.7)
  * `expect_continue` (Impact: 13.6)
  * `slow_request_408` (Impact: 12.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 433`, `args: 97`, `func_start: 31`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 100`, `high_risk_execution: 2`, `state_mutation: 214`, `planned_debt: 3`, `fragile_debt: 1`, `duplicate_logic: 2`, `orphaned_logic: 29`
* *Architecture:* `concurrency: 557`, `import: 13`
* *Defense:* `safety: 33`, `doc: 2`, `test: 76`, `immutability_locks: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.304
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` time::sleep, futures_util::stream::once, HttpService, BodyStream, Response, header, thread, actix_http::
        header::HeaderName...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `actix-web/tests/test_server.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.173 IQR)
- **Top Global Matches:** file_cluster_4: 12.173, file_cluster_0: 12.633, file_cluster_11: 12.918
- **Magnitude:** 706.72 | **LOC:** 909 | **CtrlFlow:** 14.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (49.7851%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_server_cookies` (Impact: 14.9)
  * `test_data_drop` (Impact: 9.3)
    * *Intent:* // allow deprecated App::data
  * `body_gzip_large` (Impact: 6.7)
    * *Intent:* // .request(actix_web::http::Method::GET, srv.url("/raw")) // .no_decompress() // .append_header((AC...
  * `test_body_gzip_large_random` (Impact: 6.6)
  * `test_body_chunked_implicit` (Impact: 6.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 314`, `args: 94`, `func_start: 36`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 69`, `state_mutation: 83`, `dead_code: 6`, `duplicate_logic: 4`, `orphaned_logic: 29`
* *Architecture:* `io: 1`, `concurrency: 419`, `import: 13`
* *Defense:* `safety: 43`, `test: 71`, `sync_locks: 1`, `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.304
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` pin::Pin, http::header, Arc, SslMethod, super::*, futures_core::ready, NormalizePath, SampleString...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `actix-web/src/introspection.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.6 IQR)
- **Top Global Matches:** file_cluster_0: 12.6, file_cluster_16: 12.701, file_cluster_8: 12.705
- **Magnitude:** 653.54 | **LOC:** 1338 | **CtrlFlow:** 34.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (13.9378%), Tech Debt (47.8932%)
**Top Internal Functions/Classes:**
  * `has_conflicting_methods` (Impact: 44.0)
  * `shadowed_route_context` (Impact: 34.4)
  * `shadowed_scope_context` (Impact: 30.5)
  * `guard_possible_methods` (Impact: 26.1)
  * `merge_guard_detail_reports` (Impact: 20.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 121`, `structural_boundaries: 232`, `args: 89`, `func_start: 53`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 146`, `dead_code: 1`, `duplicate_logic: 5`, `orphaned_logic: 14`
* *Architecture:* `api: 54`, `import: 5`
* *Defense:* `safety: 124`, `doc: 75`, `test: 39`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.304
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` http::Method, fmt::Write, guard::Guard, GuardDetail, std::sync::Once, crate::
    dev::ResourceDef, serde::Serialize, std::
    collections::BTreeMap...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `actix-http/src/h1/dispatcher.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.558 IQR)
- **Top Global Matches:** file_cluster_0: 13.558, file_cluster_11: 13.626, file_cluster_13: 13.683
- **Magnitude:** 649.36 | **LOC:** 1319 | **CtrlFlow:** 45.1% | **Authorship Centralization:** 20.0%
- **Risk Profile:** Cognitive Load (35.5586%), Tech Debt (8.8737%)
**Top Internal Functions/Classes:**
  * `handle_request` (Impact: 183.1)
  * `poll_response` (Impact: 98.7)
  * `read_available` (Impact: 75.6)
  * `send_response` (Impact: 17.0)
  * `send_error_response` (Impact: 17.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 153`, `structural_boundaries: 186`, `args: 24`, `func_start: 18`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 133`, `dead_code: 7`, `planned_debt: 3`
* *Architecture:* `api: 13`, `concurrency: 6`, `import: 13`
* *Defense:* `safety: 153`, `doc: 19`, `test: 6`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.304
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pin::Pin, bitflags::bitflags, io, trace, payload::Payload, PayloadStatus, std::
    collections::VecDeque, futures_core::ready...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `actix-multipart/src/form/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.339 IQR)
- **Top Global Matches:** file_cluster_4: 13.339, file_cluster_0: 13.474, file_cluster_16: 13.544
- **Magnitude:** 585.18 | **LOC:** 926 | **CtrlFlow:** 16.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (49.2238%), Tech Debt (99.8737%)
**Top Internal Functions/Classes:**
  * `from_request` (Impact: 23.7)
  * `try_consume_limits` (Impact: 14.8)
    * *Intent:* /// This function should be called within a [`FieldReader`] when reading each chunk of a field /// t...
  * `field_try_next_panic` (Impact: 10.9)
  * `from_state` (Impact: 10.8)
    * *Intent:* /// Construct `Self` from the group of processed fields.
  * `handle_field` (Impact: 8.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 267`, `args: 73`, `func_start: 50`, `class_start: 23`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 89`, `dead_code: 1`, `planned_debt: 3`, `duplicate_logic: 12`, `orphaned_logic: 14`
* *Architecture:* `api: 25`, `concurrency: 248`, `import: 17`
* *Defense:* `safety: 101`, `doc: 67`, `test: 35`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.304
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` derive_more::Deref, TryStreamExt, Multipart, Future, tempfile::TempFile, sync::Arc, text::Text, Responder...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `actix-http/src/h1/decoder.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.053 IQR)
- **Top Global Matches:** file_cluster_0: 13.053, file_cluster_8: 13.29, file_cluster_13: 13.307
- **Magnitude:** 573.04 | **LOC:** 1186 | **CtrlFlow:** 23.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (44.2159%), Tech Debt (98.6649%)
**Top Internal Functions/Classes:**
  * `set_headers` (Impact: 92.7)
  * `decode` (Impact: 48.9)
  * `decode` (Impact: 39.5)
  * `decode` (Impact: 27.1)
  * `record` (Impact: 4.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 98`, `structural_boundaries: 322`, `args: 59`, `func_start: 56`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 60`, `state_mutation: 200`, `dead_code: 1`, `duplicate_logic: 12`, `orphaned_logic: 30`
* *Architecture:* `api: 20`, `concurrency: 5`, `import: 10`
* *Defense:* `safety: 118`, `doc: 27`, `test: 95`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.304
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` trace, super::*, crate::error::ParseError, tracing::debug, ConnectionType, HttpMessage, BytesMut, crate::header::SET_COOKIE...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `awc/tests/test_client.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.703 IQR)
- **Top Global Matches:** file_cluster_4: 11.703, file_cluster_0: 12.137, file_cluster_8: 12.147
- **Magnitude:** 565.98 | **LOC:** 841 | **CtrlFlow:** 16.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.7147%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `client_cookie_handling` (Impact: 15.2)
  * `response_timeout` (Impact: 14.0)
  * `client_basic_auth` (Impact: 8.3)
  * `client_bearer_auth` (Impact: 8.3)
  * `timeout` (Impact: 8.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 279`, `args: 92`, `func_start: 27`
* *Risk/State:* `safety_bypasses: 66`, `state_mutation: 55`, `orphaned_logic: 23`
* *Architecture:* `io: 5`, `concurrency: 318`, `import: 14`
* *Defense:* `safety: 54`, `test: 61`, `sync_locks: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.304
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` http::header, Arc, futures_util::stream::once, net::IpAddr, futures_util::stream, actix_utils::future::ok, base64::prelude::*, SampleString...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `actix-web/src/middleware/logger.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.66 IQR)
- **Top Global Matches:** file_cluster_0: 13.66, file_cluster_13: 13.714, file_cluster_4: 13.724
- **Magnitude:** 474.92 | **LOC:** 1031 | **CtrlFlow:** 27.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (22.1894%), Tech Debt (64.6054%)
**Top Internal Functions/Classes:**
  * `render_request` (Impact: 26.9)
  * `new` (Impact: 24.6)
  * `poll` (Impact: 12.7)
  * `test_escape_percent` (Impact: 12.0)
  * `test_remote_addr_format` (Impact: 12.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 95`, `structural_boundaries: 252`, `args: 54`, `func_start: 34`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 135`, `dead_code: 4`, `duplicate_logic: 10`
* *Architecture:* `api: 23`, `concurrency: 58`, `import: 17`
* *Defense:* `safety: 108`, `doc: 132`, `test: 13`, `immutability_locks: 5`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.304
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pin::Pin, Ready, std::
    borrow::Cow, log::debug, super::*, futures_core::ready, MessageBody, service::ServiceRequest...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `actix-router/src/resource.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_0` (Drift: 17.498 IQR)
- **Top Global Matches:** file_cluster_0: 17.498, file_cluster_13: 17.779, file_cluster_17: 17.782
- **Magnitude:** 472.7 | **LOC:** 1781 | **CtrlFlow:** 15.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (14.9282%), Tech Debt (18.3176%)
**Top Internal Functions/Classes:**
  * `capture_match_info_fn` (Impact: 37.8)
    * *Intent:* /// Assigns a new name to the resource. /// /// # Panics /// Panics if `name` is an empty string. //...
  * `pattern_iter` (Impact: 14.6)
  * `static_match` (Impact: 12.7)
  * `next` (Impact: 11.2)
  * `construct` (Impact: 11.1)
    * *Intent:* /// Returns `true` if `path` matches this resource. /// /// The behavior of this method depends on h...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 326`, `args: 65`, `func_start: 57`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 31`, `state_mutation: 152`, `dead_code: 54`, `duplicate_logic: 4`
* *Architecture:* `api: 46`, `import: 15`
* *Defense:* `safety: 94`, `doc: 541`, `test: 305`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.304
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ResourcePath, Cow, std::collections::HashMap, ResourceDef, regex_set::escape, super::*, hash::BuildHasher, mem...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `actix-http/tests/test_rustls.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.171 IQR)
- **Top Global Matches:** file_cluster_4: 12.171, file_cluster_0: 12.61, file_cluster_8: 12.623
- **Magnitude:** 468.22 | **LOC:** 695 | **CtrlFlow:** 10.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (48.1605%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `h2_content_length` (Impact: 11.8)
  * `load_body` (Impact: 9.1)
  * `h2_headers` (Impact: 7.3)
  * `h2_body1` (Impact: 6.2)
  * `alpn_h2_1` (Impact: 5.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 245`, `args: 77`, `func_start: 29`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 50`, `state_mutation: 89`, `orphaned_logic: 19`
* *Architecture:* `api: 1`, `concurrency: 234`, `import: 15`
* *Defense:* `safety: 45`, `test: 49`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.304
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` io::self, futures_util::stream::once, header::self, HttpService, connect::rustls_0_23::webpki_roots_cert_store, Stream, TlsAcceptorConfig, openssl::ssl::SslConnector...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `actix-web/src/server.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.999 IQR)
- **Top Global Matches:** file_cluster_0: 13.999, file_cluster_13: 14.129, file_cluster_4: 14.184
- **Magnitude:** 463.02 | **LOC:** 1305 | **CtrlFlow:** 31.9% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (20.3695%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `listen_openssl_inner` (Impact: 23.4)
  * `listen_rustls_0_20_inner` (Impact: 23.2)
    * *Intent:* /// Resolves socket address(es) and binds server to created listener(s) for TLS connections /// usin...
  * `listen_rustls_0_21_inner` (Impact: 23.2)
  * `listen_rustls_0_22_inner` (Impact: 23.2)
  * `listen_rustls_0_23_inner` (Impact: 23.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 96`, `structural_boundaries: 205`, `args: 98`, `func_start: 42`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 52`, `dead_code: 6`
* *Architecture:* `io: 2`, `api: 50`, `concurrency: 64`, `import: 17`
* *Defense:* `safety: 157`, `doc: 330`, `sync_locks: 21`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.304
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` actix_http::TlsAcceptorConfig, Service, Mutex, io, HttpService, actix_http::body::MessageBody, actix_rt::net::UnixStream, sync::Arc...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `actix-files/src/lib.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.567 IQR)
- **Top Global Matches:** file_cluster_8: 9.567, file_cluster_4: 9.664, file_cluster_0: 9.978
- **Magnitude:** 450.4 | **LOC:** 1104 | **CtrlFlow:** 2.3% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (72.6139%), Tech Debt (95.3685%)
**Top Internal Functions/Classes:**
  * `test_named_file_empty_range_headers` (Impact: 6.0)
  * `test_named_file_content_length_headers` (Impact: 5.4)
  * `test_named_file_content_encoding_gzip` (Impact: 4.8)
  * `test_named_file_content_range_headers` (Impact: 4.7)
  * `test_percent_encoding_2` (Impact: 4.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 425`, `args: 61`, `func_start: 49`
* *Risk/State:* `safety_bypasses: 104`, `state_mutation: 27`, `duplicate_logic: 2`, `orphaned_logic: 45`
* *Architecture:* `io: 4`, `api: 2`, `concurrency: 252`, `import: 10`
* *Defense:* `safety: 6`, `doc: 17`, `test: 110`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.304
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` self::
    directory::directory_listing, mime_guess::from_ext, ContentDisposition, DirectoryRenderer, actix_web::
        dev::ServiceFactory, directory::Directory, super::*, path_buf::PathBufWrap...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `awc/src/client/connector.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.976 IQR)
- **Top Global Matches:** file_cluster_0: 12.976, file_cluster_16: 13.042, file_cluster_13: 13.062
- **Magnitude:** 441.84 | **LOC:** 1154 | **CtrlFlow:** 24.7% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (22.3867%), Tech Debt (99.604%)
**Top Internal Functions/Classes:**
  * `finish` (Impact: 49.9)
  * `into_connection_io` (Impact: 12.2)
  * `resolver` (Impact: 11.2)
  * `poll` (Impact: 9.8)
  * `build_tls` (Impact: 8.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 217`, `args: 68`, `func_start: 48`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 68`, `dead_code: 2`, `duplicate_logic: 28`
* *Architecture:* `io: 5`, `api: 35`, `concurrency: 79`, `import: 34`
* *Defense:* `safety: 105`, `doc: 110`, `test: 3`, `immutability_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.304
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pin::Pin, actix_tls::connect::
    ConnectError, actix_tls::connect::openssl::reexports::SslConnector, actix_tls::connect::rustls_0_22::reexports::AsyncTlsStream, time::sleep, Resolver, Sleep, Ready...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `actix-multipart/src/multipart.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.349 IQR)
- **Top Global Matches:** file_cluster_4: 13.349, file_cluster_0: 13.7, file_cluster_13: 13.73
- **Magnitude:** 437.06 | **LOC:** 884 | **CtrlFlow:** 25.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (45.6247%), Tech Debt (10.2887%)
**Top Internal Functions/Classes:**
  * `test_multipart` (Impact: 16.4)
  * `poll_next` (Impact: 13.3)
  * `find_ct_and_boundary` (Impact: 11.1)
    * *Intent:* /// Extract Content-Type and boundary info from headers.
  * `test_boundary` (Impact: 9.0)
  * `test_stream` (Impact: 8.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 195`, `args: 35`, `func_start: 24`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 39`, `state_mutation: 100`, `planned_debt: 4`
* *Architecture:* `api: 22`, `concurrency: 177`, `import: 14`
* *Defense:* `safety: 131`, `doc: 37`, `test: 21`, `immutability_locks: 4`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.304
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` pin::Pin, ContentDisposition, std::
    cell::RefCell, http::header::self, web::BufMut, test::TestRequest, futures_util::stream, super::*...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `actix-web-actors/src/ws.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.384 IQR)
- **Top Global Matches:** file_cluster_16: 13.384, file_cluster_4: 13.644, file_cluster_13: 13.7
- **Magnitude:** 427.62 | **LOC:** 1053 | **CtrlFlow:** 25.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (37.5613%), Tech Debt (58.094%)
**Top Internal Functions/Classes:**
  * `handshake_with_protocols` (Impact: 38.0)
  * `poll_next` (Impact: 23.0)
  * `poll_next` (Impact: 22.0)
  * `test_handshake` (Impact: 10.7)
  * `start_with_protocols` (Impact: 8.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 169`, `args: 45`, `func_start: 38`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 75`, `duplicate_logic: 9`
* *Architecture:* `api: 30`, `concurrency: 116`, `import: 13`
* *Defense:* `safety: 110`, `doc: 198`, `test: 18`, `immutability_locks: 14`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.304
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` pin::Pin, ActorContext, io, actix::Actor, std::
    collections::VecDeque, super::*, actix::
    dev::
        AsyncContextParts, actix_http::ws::CloseCode...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `actix-web/src/types/json.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.41 IQR)
- **Top Global Matches:** file_cluster_4: 14.41, file_cluster_0: 14.634, file_cluster_11: 14.772
- **Magnitude:** 424.56 | **LOC:** 771 | **CtrlFlow:** 18.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (49.7431%), Tech Debt (96.9789%)
**Top Internal Functions/Classes:**
  * `new` (Impact: 16.6)
    * *Intent:* /// Sets whether or not the request must have a `Content-Type` header to be parsed.
  * `poll` (Impact: 15.4)
  * `limit` (Impact: 8.3)
  * `poll` (Impact: 8.2)
  * `respond_to` (Impact: 5.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 167`, `args: 38`, `func_start: 28`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 59`, `dead_code: 13`, `planned_debt: 2`, `duplicate_logic: 4`, `orphaned_logic: 12`
* *Architecture:* `api: 12`, `concurrency: 222`, `import: 11`
* *Defense:* `safety: 58`, `doc: 106`, `test: 21`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.304
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` pin::Pin, ops, serde::de::DeserializeOwned, Stream, test::assert_body_eq, super::*, crate::dev::Decompress, futures_core::ready...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `actix-web/src/scope.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.56 IQR)
- **Top Global Matches:** file_cluster_4: 13.56, file_cluster_0: 13.577, file_cluster_13: 13.916
- **Magnitude:** 402.34 | **LOC:** 1257 | **CtrlFlow:** 6.2% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (36.8635%), Tech Debt (17.6922%)
**Top Internal Functions/Classes:**
  * `register` (Impact: 16.1)
  * `can_be_returned_from_fn` (Impact: 8.6)
  * `new_service` (Impact: 6.9)
  * `test_middleware_body_type` (Impact: 6.3)
  * `call` (Impact: 6.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 319`, `args: 78`, `func_start: 39`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 40`, `state_mutation: 37`, `dead_code: 17`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 34`, `concurrency: 170`, `import: 12`
* *Defense:* `safety: 68`, `doc: 174`, `test: 62`, `immutability_locks: 7`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.304
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` crate::
        guard, std::cell::Cell, Service, actix_http::body::MessageBody, guard::Guard, data::Data, test::assert_body_eq, super::*...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `actix-http/src/h1/dispatcher_tests.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.909 IQR)
- **Top Global Matches:** file_cluster_8: 10.909, file_cluster_4: 11.166, file_cluster_0: 11.367
- **Magnitude:** 387.56 | **LOC:** 1273 | **CtrlFlow:** 10.7% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (27.5809%), Tech Debt (34.4441%)
**Top Internal Functions/Classes:**
  * `call` (Impact: 88.4)
  * `expect_eager` (Impact: 28.8)
  * `keep_alive_follow_up_req` (Impact: 11.4)
  * `expect_handling` (Impact: 10.7)
  * `handler_drop_payload_drains_body` (Impact: 9.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 192`, `args: 37`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 1`, `state_mutation: 53`, `orphaned_logic: 15`
* *Architecture:* `concurrency: 94`, `import: 11`
* *Defense:* `safety: 57`, `test: 83`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.304
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Flags, pin::Pin, crate::config::ServiceConfigBuilder, time::sleep, Service, Ready, futures_util::future::lazy, MessageBody...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `actix-web/src/request.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.586 IQR)
- **Top Global Matches:** file_cluster_0: 14.586, file_cluster_4: 14.895, file_cluster_11: 14.98
- **Magnitude:** 379.14 | **LOC:** 1249 | **CtrlFlow:** 15.1% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (15.3056%), Tech Debt (22.0829%)
**Top Internal Functions/Classes:**
  * `fmt` (Impact: 20.7)
  * `check_full_url` (Impact: 13.2)
  * `cookies` (Impact: 11.4)
    * *Intent:* /// Generates URL for a named resource. /// /// This substitutes in sequence all URL parameters that...
  * `test_data` (Impact: 10.3)
  * `cookie` (Impact: 7.5)
    * *Intent:* /// Generates URL for a named resource using a map of dynamic segment values. /// /// This substitut...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 219`, `args: 79`, `func_start: 58`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 40`, `dead_code: 20`, `duplicate_logic: 4`
* *Architecture:* `api: 62`, `concurrency: 61`, `import: 12`
* *Defense:* `safety: 89`, `doc: 221`, `test: 84`, `immutability_locks: 5`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.304
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` error::UrlGenerationError, Service, http::header, Ready, std::collections::HashMap, RefCell, super::*, actix_utils::future::ok...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `actix-web/src/service.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.33 IQR)
- **Top Global Matches:** file_cluster_0: 13.33, file_cluster_4: 13.673, file_cluster_16: 13.701
- **Magnitude:** 354.68 | **LOC:** 926 | **CtrlFlow:** 21.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (22.5489%), Tech Debt (99.9948%)
**Top Internal Functions/Classes:**
  * `fmt` (Impact: 16.6)
    * *Intent:* /// Counterpart to [`HttpRequest::app_data`].
  * `register` (Impact: 13.1)
  * `test_services_vec` (Impact: 10.4)
    * *Intent:* /// Macro to help register different types of services at the same time. /// /// The max number of s...
  * `test_services_macro` (Impact: 7.0)
  * `test_fmt_debug` (Impact: 6.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 156`, `args: 80`, `func_start: 64`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 45`, `dead_code: 8`, `planned_debt: 2`, `duplicate_logic: 20`
* *Architecture:* `api: 61`, `concurrency: 52`, `import: 11`
* *Defense:* `safety: 45`, `doc: 123`, `test: 28`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.304
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` crate::
        guard, GuardContext, ResourceDef, actix_service::
    boxed::BoxService, guard::Guard, super::*, actix_web::services, actix_utils::future::ok...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `awc/src/middleware/redirect.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.604 IQR)
- **Top Global Matches:** file_cluster_8: 11.604, file_cluster_0: 11.614, file_cluster_4: 11.631
- **Magnitude:** 350.6 | **LOC:** 681 | **CtrlFlow:** 31.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (28.4958%), Tech Debt (72.6763%)
**Top Internal Functions/Classes:**
  * `poll` (Impact: 31.0)
  * `test_redirect_cross_origin_headers` (Impact: 22.3)
  * `build_next_uri` (Impact: 15.9)
  * `test_redirect_headers` (Impact: 13.3)
  * `test_redirect_status_kind_301_302_303` (Impact: 11.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 149`, `args: 57`, `func_start: 29`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 41`, `state_mutation: 34`, `dead_code: 1`, `duplicate_logic: 8`
* *Architecture:* `api: 16`, `concurrency: 54`, `import: 11`
* *Defense:* `safety: 49`, `test: 23`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.304
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pin::Pin, RequestHeadType, connect::ConnectRequest, net::SocketAddr, super::*, futures_core::ready, ConnectResponse, Error...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `actix-http/src/service.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.934 IQR)
- **Top Global Matches:** file_cluster_16: 11.934, file_cluster_13: 12.297, file_cluster_0: 12.36
- **Magnitude:** 347.64 | **LOC:** 1130 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (16.3193%), Tech Debt (15.5083%)
**Top Internal Functions/Classes:**
  * `rustls_with_config` (Impact: 18.0)
  * `rustls_021_with_config` (Impact: 18.0)
  * `rustls_0_22_with_config` (Impact: 18.0)
  * `rustls_0_23_with_config` (Impact: 18.0)
  * `openssl_with_config` (Impact: 17.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 197`, `args: 50`, `func_start: 28`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 46`, `dead_code: 2`, `duplicate_logic: 3`
* *Architecture:* `io: 4`, `api: 39`, `concurrency: 68`, `import: 27`
* *Defense:* `safety: 94`, `doc: 64`, `immutability_locks: 76`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.304
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pin::Pin, Framed, Service, std::convert::Infallible, super::*, actix_rt::net::TcpStream, MessageBody, Response...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `actix-http/src/header/map.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_0` (Drift: 17.292 IQR)
- **Top Global Matches:** file_cluster_0: 17.292, file_cluster_11: 17.493, file_cluster_13: 17.493
- **Magnitude:** 341.48 | **LOC:** 1206 | **CtrlFlow:** 20.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (13.239%), Tech Debt (99.9996%)
**Top Internal Functions/Classes:**
  * `next` (Impact: 11.0)
    * *Intent:* /// Returns true if iterator contains no elements, without consuming it. ///
  * `next` (Impact: 9.2)
  * `next` (Impact: 9.1)
  * `get_all_iteration_order_matches_insertio` (Impact: 5.9)
  * `from_drain` (Impact: 5.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 240`, `args: 73`, `func_start: 62`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 114`, `dead_code: 42`, `planned_debt: 1`, `duplicate_logic: 28`, `orphaned_logic: 12`
* *Architecture:* `api: 29`, `import: 20`
* *Defense:* `safety: 78`, `doc: 458`, `test: 126`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.304
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` foldhash::HashMap, http::header::HeaderName, super::AsHeaderName, collections::hash_map, actix_http::header::HeaderMap, std::iter::FusedIterator, http::header, static_assertions::assert_impl_all...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `actix-http/src/h1/encoder.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.11%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.46 IQR)
- **Top Global Matches:** file_cluster_4: 12.46, file_cluster_0: 12.487, file_cluster_8: 12.581
- **Magnitude:** 329.98 | **LOC:** 688 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (44.287%), Tech Debt (99.824%)
**Top Internal Functions/Classes:**
  * `encode_headers` (Impact: 55.8)
  * `encode` (Impact: 28.1)
  * `encode` (Impact: 20.1)
  * `encode_eof` (Impact: 9.7)
  * `test_camel_case` (Impact: 5.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 120`, `args: 40`, `func_start: 36`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 75`, `dead_code: 1`, `duplicate_logic: 18`
* *Architecture:* `api: 20`, `concurrency: 44`, `import: 8`
* *Defense:* `safety: 55`, `doc: 19`, `test: 25`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.304
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` io::self, RequestHeadType, DATE, crate::
        header::HeaderValue, http::header::AUTHORIZATION, super::*, bytes::BufMut, Response...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `actix-web/src/resource.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.668 IQR)
- **Top Global Matches:** file_cluster_0: 14.668, file_cluster_4: 14.728, file_cluster_11: 14.787
- **Magnitude:** 328.0 | **LOC:** 926 | **CtrlFlow:** 16.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (27.3196%), Tech Debt (44.2687%)
**Top Internal Functions/Classes:**
  * `register` (Impact: 32.6)
    * *Intent:* #[doc = concat!(" Adds a ", $method_upper, " route.")] /// /// Use [`route`](Self::route) if you nee...
  * `can_be_returned_from_fn` (Impact: 10.3)
  * `new` (Impact: 8.1)
  * `test_middleware_body_type` (Impact: 6.2)
  * `new_service` (Impact: 6.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 212`, `args: 62`, `func_start: 30`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 2`, `state_mutation: 45`, `dead_code: 19`, `planned_debt: 3`, `duplicate_logic: 4`
* *Architecture:* `api: 29`, `concurrency: 98`, `import: 23`
* *Defense:* `safety: 71`, `doc: 188`, `test: 29`, `immutability_locks: 15`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.304
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` std::cell::Cell, Service, http::header, actix_http::body::MessageBody, ResourceDef, data::Data, fn_service, super::*...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `actix-router/src/path.rs` (RUST) | Magnitude: 160.74 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 205, structural_boundaries: 66, generics: 41, state_mutation: 37
- `actix-web/examples/uds.rs` (RUST) | Magnitude: 22.96 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 25, args: 7, decorators: 7, concurrency: 6
- `actix-web/src/test/mod.rs` (RUST) | Magnitude: 11.1 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 34, indent_spaces: 25, structural_boundaries: 17, import: 8
- `actix-http/src/body/boxed.rs` (RUST) | Magnitude: 71.24 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 84, safety: 31, structural_boundaries: 30, state_mutation: 17
- `actix-web/src/thin_data.rs` (RUST) | Magnitude: 38.92 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 53, doc: 39, structural_boundaries: 24, concurrency: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `scripts/bump` (SHELL) | Magnitude: 182.82 | Delta: **0.08 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: branch: 82, state_mutation: 72, indent_spaces: 54, io: 45

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `actix-http/src/http_message.rs` (RUST) | Magnitude: 107.36 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 172, structural_boundaries: 58, safety: 46, concurrency: 30
- `actix-web/src/http/header/mod.rs` (RUST) | Magnitude: 18.5 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 40, structural_boundaries: 37, doc: 8, api: 6
- `actix-web/src/http/header/allow.rs` (RUST) | Magnitude: 15.56 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 42, indent_spaces: 24, dead_code: 6, safety: 3
- `actix-http/src/body/sized_stream.rs` (RUST) | Magnitude: 36.94 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 107, structural_boundaries: 36, safety: 28, generics: 22
- `actix-files/src/encoding.rs` (RUST) | Magnitude: 20.04 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 9, doc: 9, branch: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `actix-http/src/test.rs` (RUST) | Magnitude: 272.12 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 271, state_mutation: 106, structural_boundaries: 98, safety: 74
- `awc/src/sender.rs` (RUST) | Magnitude: 113.26 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 223, safety: 75, structural_boundaries: 53, generics: 34
- `actix-http/src/h1/utils.rs` (RUST) | Magnitude: 71.68 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 98, structural_boundaries: 29, branch: 26, safety: 22
- `actix-http/src/header/into_pair.rs` (RUST) | Magnitude: 34.86 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 66, structural_boundaries: 34, generics: 20, branch: 15
- `actix-web/src/error/response_error.rs` (RUST) | Magnitude: 37.56 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 71, structural_boundaries: 26, generics: 20, branch: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `actix-web-codegen/src/route.rs` (RUST) | Magnitude: 206.68 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 420, structural_boundaries: 98, safety: 84, branch: 63
- `scripts/unreleased` (SHELL) | Magnitude: 54.66 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 28, indent_spaces: 24, branch: 15, safety_bypasses: 10
- `actix-router/src/pattern.rs` (RUST) | Magnitude: 34.3 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 46, structural_boundaries: 14, args: 14, generics: 12
- `actix-web/src/http/header/cache_control.rs` (RUST) | Magnitude: 30.46 | Delta: **0.134 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 101, doc: 54, safety: 45, structural_boundaries: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `actix-multipart/src/form/text.rs` (RUST) | Magnitude: 98.48 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 110, structural_boundaries: 51, concurrency: 40, generics: 22
- `actix-web/src/request_data.rs` (RUST) | Magnitude: 50.14 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 97, doc: 41, structural_boundaries: 35, concurrency: 19
- `actix-web/src/middleware/err_handlers.rs` (RUST) | Magnitude: 183.62 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 331, doc: 172, structural_boundaries: 120, generics: 94
- `actix-web/src/scope.rs` (RUST) | Magnitude: 402.34 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 824, structural_boundaries: 319, doc: 174, concurrency: 170
- `actix-http/src/h2/dispatcher.rs` (RUST) | Magnitude: 185.3 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 239, structural_boundaries: 82, safety: 48, state_mutation: 41

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
- `awc/src/middleware/redirect.rs` (RUST) | Magnitude: 350.6 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 537, structural_boundaries: 149, branch: 69, args: 57
- `actix-files/src/error.rs` (RUST) | Magnitude: 6.44 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 19, doc: 10, decorators: 10, structural_boundaries: 6
- `actix-http/examples/h2c-detect.rs` (RUST) | Magnitude: 9.66 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 17, doc: 7, structural_boundaries: 5, safety: 4
- `awc/src/client/config.rs` (RUST) | Magnitude: 17.14 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 27, api: 11, encapsulation: 11, structural_boundaries: 6
- `actix-files/src/service.rs` (RUST) | Magnitude: 177.5 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_13`
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

- `actix-web/tests/test_server.rs` -> **Yuki Okushi** (100.0% isolated ownership) | Magnitude: 706.72
- `actix-web/src/introspection.rs` -> **Guillermo Céspedes Tabárez** (100.0% isolated ownership) | Magnitude: 653.54
- `actix-multipart/src/form/mod.rs` -> **fasilmveloor** (100.0% isolated ownership) | Magnitude: 585.18
- `actix-http/tests/test_rustls.rs` -> **Yuki Okushi** (100.0% isolated ownership) | Magnitude: 468.22
- `actix-web/src/types/json.rs` -> **Andrew Scott** (100.0% isolated ownership) | Magnitude: 424.56

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
- `awc/src/responses/read_body.rs` -> **Severity: 936.07** (Blast Radius: 11.604 * Doc Risk: 80.6679%)
- `actix-web/src/dev.rs` -> **Severity: 511.618** (Blast Radius: 5.567 * Doc Risk: 91.9019%)
- `actix-http/src/requests/head.rs` -> **Severity: 230.4** (Blast Radius: 2.304 * Doc Risk: 100.0%)
- `actix-http/src/test.rs` -> **Severity: 230.4** (Blast Radius: 2.304 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
