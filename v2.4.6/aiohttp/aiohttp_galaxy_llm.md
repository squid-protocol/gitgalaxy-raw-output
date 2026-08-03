# ARCHITECTURAL_BRIEF: aiohttp
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/aiohttp` |
| **Timestamp** | `2026-08-03T21:19:09.723840+00:00` |
| **Scan Duration** | `2.04s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 184 malicious artifacts.

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
| Total Artifacts | 232 |
| Analyzed Artifacts (Scanned) | 193 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 39 |
| Total LOC | 74446 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 83.2% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3673 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1465 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 18.6% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.6427 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 17 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 169 | 64794 | 87.6% |
| M4 | 9 | 40 | 4.7% |
| PLAINTEXT | 6 | 2 | 3.1% |
| C | 2 | 9332 | 1.0% |
| JSON | 2 | 23 | 1.0% |
| SHELL | 2 | 5 | 1.0% |
| MAKEFILE | 1 | 145 | 0.5% |
| HTML | 1 | 94 | 0.5% |
| DOCKERFILE | 1 | 11 | 0.5% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.333`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 76 | 39.4% |
| file_cluster_4 | 55 | 28.5% |
| file_cluster_16 | 27 | 14.0% |
| file_cluster_13 | 24 | 12.4% |
| file_cluster_0 | 5 | 2.6% |
| Unknown | 2 | 1.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 4 | 2.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 39*

**Composition by Extension & Reason:**
- `.txt`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 51 LOC), 1x Excluded (Machine-Generated Source Code Signature: 53 LOC)
- `.c`: 1x Excluded (Monolithic Amalgamation: 31398 LOC exceeds safe regex boundaries), 1x Excluded (Machine-Generated Source Code Signature: 10589 LOC), 1x Excluded (Machine-Generated Source Code Signature: 8687 LOC)
- `.in`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 1x Unsupported Format (.undeterminable), 1x Excluded (Unsupported Extension: '.unknown_mime_type'), 1x Excluded (Unsupported Extension: '.dockerignore')
- `.py`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rst`: 2x Excluded (Unsupported Extension: '.rst')
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')
- `.csr`: 1x Excluded (Unsupported Extension: '.csr')
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')
- `.jpg`: 1x Excluded (Explicitly Denied Extension: '.jpg')
- `.png`: 1x Excluded (Explicitly Denied Extension: '.png')
- `.aiohttp`: 1x Excluded (Unsupported Extension: '.aiohttp')
- `.autobahn`: 1x Excluded (Unsupported Extension: '.autobahn')
- `.zero_bytes`: 1x Excluded (Unsupported Extension: '.zero_bytes')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 98.9 | 29.4 | 22.8 | 5.0 |
| Error & Exception Exposure | 0.0 | 80.0 | 12.0 | 0.6 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 12.5 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 14.1 | 0.0 | 0.0 |
| API Exposure | 0.0 | 15.4 | 4.9 | 4.5 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 64.7 | 100.0 | 100.0 |
| State Flux Exposure | 0.0 | 100.0 | 21.5 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 21.7 | 0.8 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 92.5 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 27.6 | 0.0 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 67.0 | 99.9 | 100.0 |
| Obfuscation & Evasion Surface | 0.0 | 3.4 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 56.4 | 100.0 | 100.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 8.8 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 100.0 | 0.6 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `aiohttp-3.13.5/tests/test_connector.py` (Hits: 341)
- `aiohttp-3.13.5/tests/test_client_functional.py` (Hits: 203)
- `aiohttp-3.13.5/tests/test_multipart.py` (Hits: 131)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **multidict.in** (`aiohttp-3.13.5/requirements/multidict.in`) — 39 inbound connections
2. **abc.py** (`aiohttp-3.13.5/aiohttp/abc.py`) — 38 inbound connections
3. **typedefs.py** (`aiohttp-3.13.5/aiohttp/typedefs.py`) — 28 inbound connections
4. **http.py** (`aiohttp-3.13.5/aiohttp/http.py`) — 24 inbound connections
5. **pytest_plugin.py** (`aiohttp-3.13.5/aiohttp/pytest_plugin.py`) — 21 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **test_client_functional.py** (`aiohttp-3.13.5/tests/test_client_functional.py`) — 36 outbound dependencies
2. **helpers.py** (`aiohttp-3.13.5/aiohttp/helpers.py`) — 33 outbound dependencies
3. **client_reqrep.py** (`aiohttp-3.13.5/aiohttp/client_reqrep.py`) — 31 outbound dependencies
4. **client.py** (`aiohttp-3.13.5/aiohttp/client.py`) — 30 outbound dependencies
5. **test_utils.py** (`aiohttp-3.13.5/aiohttp/test_utils.py`) — 29 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `find_header` (@ `aiohttp-3.13.5/aiohttp/_find_header.c`) -> Impact: **5351.1** | LOC: 2492
- `_wait_for_close` (@ `aiohttp-3.13.5/aiohttp/connector.py`) -> Impact: **4410.4** | LOC: 1494
  * *Intent:* """Wait for all waiters to finish closing."""
- `links` (@ `aiohttp-3.13.5/aiohttp/client_reqrep.py`) -> Impact: **1693.9** | LOC: 657
- `test_tcp_connector_resolve_host` (@ `aiohttp-3.13.5/tests/test_connector.py`) -> Impact: **1598.2** | LOC: 3253
- `test_POST_FILES_SINGLE_content_dispositi` (@ `aiohttp-3.13.5/tests/test_client_functional.py`) -> Impact: **1051.3** | LOC: 2423
  * *Intent:* # if system cannot determine 'application/pgp-keys' MIME type
- `feed_data` (@ `aiohttp-3.13.5/aiohttp/http_parser.py`) -> Impact: **904.5** | LOC: 247
- `_wait` (@ `aiohttp-3.13.5/aiohttp/streams.py`) -> Impact: **775.7** | LOC: 238
  * *Intent:* # wake up readchunk when end of http chunk received waiter = self._waiter if waiter is not None: self._waiter = None set_result(waiter, None) async de...
- `append` (@ `aiohttp-3.13.5/aiohttp/multipart.py`) -> Impact: **620.1** | LOC: 194
  * *Intent:* # Refer to RFCs 7231, 7230, 5234. # # parameter = token "=" ( token / quoted-string ) # token = 1*tchar # quoted-string = DQUOTE *( qdtext / quoted-pa...
- `_refresh_access_token` (@ `aiohttp-3.13.5/examples/token_refresh_middleware.py`) -> Impact: **544.9** | LOC: 298
- `__setitem__` (@ `aiohttp-3.13.5/aiohttp/web_app.py`) -> Impact: **450.0** | LOC: 391

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `connection_lost` (@ `aiohttp-3.13.5/aiohttp/client_proto.py`) -> **O(2^N) [Recursive]**
- `links` (@ `aiohttp-3.13.5/aiohttp/client_reqrep.py`) -> **O(2^N) [Recursive]**
- `receive` (@ `aiohttp-3.13.5/aiohttp/client_ws.py`) -> **O(2^N) [Recursive]**
- `_wait_for_close` (@ `aiohttp-3.13.5/aiohttp/connector.py`) -> **O(2^N) [Recursive]**
  * *Intent:* """Wait for all waiters to finish closing."""
- `feed_data` (@ `aiohttp-3.13.5/aiohttp/http_parser.py`) -> **O(2^N) [Recursive]**
- `append` (@ `aiohttp-3.13.5/aiohttp/multipart.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # Refer to RFCs 7231, 7230, 5234. # # parameter = token "=" ( token / quoted-string ) # token = 1*tchar # quoted-string = DQUOTE *( qdtext / quoted-pa...
- `_wait` (@ `aiohttp-3.13.5/aiohttp/streams.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # wake up readchunk when end of http chunk received waiter = self._waiter if waiter is not None: self._waiter = None set_result(waiter, None) async de...
- `feed_eof` (@ `aiohttp-3.13.5/aiohttp/_http_parser.pyx`) -> **O(2^N) [Recursive]**
  * *Intent:* ### Public API ###
- `start_client` (@ `aiohttp-3.13.5/examples/client_ws.py`) -> **O(2^N) [Recursive]**
- `_refresh_access_token` (@ `aiohttp-3.13.5/examples/token_refresh_middleware.py`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `test_tcp_connector_resolve_host` (@ `aiohttp-3.13.5/tests/test_connector.py`) -> DB Complexity: **767**
- `test_POST_FILES_SINGLE_content_dispositi` (@ `aiohttp-3.13.5/tests/test_client_functional.py`) -> DB Complexity: **331**
  * *Intent:* # if system cannot determine 'application/pgp-keys' MIME type
- `_wait_for_close` (@ `aiohttp-3.13.5/aiohttp/connector.py`) -> DB Complexity: **159**
  * *Intent:* """Wait for all waiters to finish closing."""
- `test_urlencoded_formdata_charset` (@ `aiohttp-3.13.5/tests/test_client_request.py`) -> DB Complexity: **98**
- `test_parse_uri_utf8_percent_encoded` (@ `aiohttp-3.13.5/tests/test_http_parser.py`) -> DB Complexity: **93**
- `test_add_url_invalid4` (@ `aiohttp-3.13.5/tests/test_urldispatch.py`) -> DB Complexity: **78**
- `test_cookie_jar_usage` (@ `aiohttp-3.13.5/tests/test_client_session.py`) -> DB Complexity: **68**
- `test_read_json` (@ `aiohttp-3.13.5/tests/test_multipart.py`) -> DB Complexity: **63**
- `links` (@ `aiohttp-3.13.5/aiohttp/client_reqrep.py`) -> DB Complexity: **58**
- `test_attbrokenquotedfn3` (@ `aiohttp-3.13.5/tests/test_multipart_helpers.py`) -> DB Complexity: **45**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `aiohttp-3.13.5/tests` | 74 | 35862.9 | 20.82% | 0.0% |
| `aiohttp-3.13.5/aiohttp` | 55 | 35219.97 | 40.0% | 35.66% |
| `aiohttp-3.13.5/examples` | 27 | 14114.51 | 41.17% | 0.0% |
| `aiohttp-3.13.5/aiohttp/_websocket` | 10 | 1356.84 | 26.7% | 27.14% |
| `aiohttp-3.13.5` | 5 | 357.5 | 7.53% | 0.0% |
| `aiohttp-3.13.5/tests/autobahn` | 1 | 124.66 | 7.65% | 0.0% |
| `aiohttp-3.13.5/tests/autobahn/client` | 2 | 115.68 | 27.18% | 0.0% |
| `aiohttp-3.13.5/requirements` | 9 | 107.8 | 6.09% | 0.0% |
| `aiohttp-3.13.5/tests/autobahn/server` | 2 | 86.5 | 27.44% | 0.0% |
| `aiohttp-3.13.5/tests/isolated` | 2 | 80.36 | 35.79% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `aiohttp-3.13.5/aiohttp/compression_utils.py` -> **100.0%** Exposure
- `aiohttp-3.13.5/aiohttp/http_exceptions.py` -> **100.0%** Exposure
- `aiohttp-3.13.5/aiohttp/payload.py` -> **100.0%** Exposure
- `aiohttp-3.13.5/aiohttp/payload_streamer.py` -> **100.0%** Exposure
- `aiohttp-3.13.5/aiohttp/streams.py` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `aiohttp-3.13.5/aiohttp/_websocket/reader_c.py` -> **99.9995%** Exposure
- `aiohttp-3.13.5/aiohttp/_websocket/reader_py.py` -> **99.9995%** Exposure
- `aiohttp-3.13.5/aiohttp/http_exceptions.py` -> **99.9993%** Exposure
- `aiohttp-3.13.5/aiohttp/web_server.py` -> **99.9993%** Exposure
- `aiohttp-3.13.5/aiohttp/streams.py` -> **99.9972%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `aiohttp-3.13.5/tests/test_client_functional.py` -> **129** Orphaned Functions | **25** Duplicates
- `aiohttp-3.13.5/tests/test_web_functional.py` -> **102** Orphaned Functions | **5** Duplicates
- `aiohttp-3.13.5/tests/test_urldispatch.py` -> **84** Orphaned Functions | **0** Duplicates
- `aiohttp-3.13.5/tests/test_client_request.py` -> **78** Orphaned Functions | **0** Duplicates
- `aiohttp-3.13.5/tests/test_helpers.py` -> **74** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`aiohttp-3.13.5/aiohttp/_http_parser.pyx`** -> AI Confidence: **99.31%**
2. **`aiohttp-3.13.5/aiohttp/_websocket/helpers.py`** -> AI Confidence: **99.31%**
3. **`aiohttp-3.13.5/aiohttp/_websocket/reader_c.py`** -> AI Confidence: **99.31%**
4. **`aiohttp-3.13.5/aiohttp/_websocket/reader_py.py`** -> AI Confidence: **99.31%**
5. **`aiohttp-3.13.5/aiohttp/_websocket/writer.py`** -> AI Confidence: **99.31%**
6. **`aiohttp-3.13.5/tests/autobahn/test_autobahn.py`** -> AI Confidence: **99.31%**
7. **`aiohttp-3.13.5/aiohttp/client.py`** -> AI Confidence: **99.31%**
8. **`aiohttp-3.13.5/aiohttp/client_middleware_digest_auth.py`** -> AI Confidence: **99.31%**
9. **`aiohttp-3.13.5/aiohttp/client_proto.py`** -> AI Confidence: **99.31%**
10. **`aiohttp-3.13.5/aiohttp/client_reqrep.py`** -> AI Confidence: **99.31%**
11. **`aiohttp-3.13.5/aiohttp/connector.py`** -> AI Confidence: **99.31%**
12. **`aiohttp-3.13.5/aiohttp/cookiejar.py`** -> AI Confidence: **99.31%**
13. **`aiohttp-3.13.5/aiohttp/formdata.py`** -> AI Confidence: **99.31%**
14. **`aiohttp-3.13.5/aiohttp/http_parser.py`** -> AI Confidence: **99.31%**
15. **`aiohttp-3.13.5/aiohttp/http_writer.py`** -> AI Confidence: **99.31%**
16. **`aiohttp-3.13.5/aiohttp/web_protocol.py`** -> AI Confidence: **99.31%**
17. **`aiohttp-3.13.5/aiohttp/web_response.py`** -> AI Confidence: **99.31%**
18. **`aiohttp-3.13.5/tools/testing/entrypoint.sh`** -> AI Confidence: **99.29%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `aiohttp-3.13.5/tests/test_websocket_writer.py` -> **3.4441%** Exposure
- `aiohttp-3.13.5/tests/test_formdata.py` -> **0.0001%** Exposure
- `aiohttp-3.13.5/tests/test_web_server.py` -> **0.0001%** Exposure
### Exploit Generation Surface
- `aiohttp-3.13.5/aiohttp/_http_parser.pyx` -> **100.0%** Exposure
- `aiohttp-3.13.5/aiohttp/_http_writer.pyx` -> **100.0%** Exposure
- `aiohttp-3.13.5/aiohttp/_websocket/reader_c.py` -> **100.0%** Exposure
- `aiohttp-3.13.5/aiohttp/_websocket/reader_py.py` -> **100.0%** Exposure
- `aiohttp-3.13.5/examples/client_ws.py` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `aiohttp-3.13.5/tests/autobahn/test_autobahn.py` -> **100.0%** Exposure
- `aiohttp-3.13.5/tests/test_benchmarks_web_urldispatcher.py` -> **100.0%** Exposure
- `aiohttp-3.13.5/tests/test_client_functional.py` -> **100.0%** Exposure
- `aiohttp-3.13.5/tests/test_client_middleware.py` -> **100.0%** Exposure
- `aiohttp-3.13.5/tests/test_client_request.py` -> **100.0%** Exposure
### Hardcoded Payload Artifacts
- `aiohttp-3.13.5/examples/fake_server.py` -> **99.9954%** Exposure
- `aiohttp-3.13.5/tests/test_client_functional.py` -> **11.4686%** Exposure
### Algorithmic DoS Exposure
- `aiohttp-3.13.5/aiohttp/_http_parser.pyx` -> **100.0%** Exposure
- `aiohttp-3.13.5/aiohttp/_websocket/reader_c.py` -> **100.0%** Exposure
- `aiohttp-3.13.5/aiohttp/_websocket/reader_py.py` -> **100.0%** Exposure
- `aiohttp-3.13.5/examples/client_ws.py` -> **100.0%** Exposure
- `aiohttp-3.13.5/examples/curl.py` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1317` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `aiohttp-3.13.5/aiohttp/web_runner.py` (PYTHON) -> Cumulative Risk: **966.87**
- **Archetype:** `file_cluster_4` (Distance: 11.442 IQR)
- **Magnitude:** 437.38 | **LOC:** 400 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `addresses` (Impact: 30.8), `cleanup` (Impact: 26.3), `setup` (Impact: 15.6)

### 2. `aiohttp-3.13.5/aiohttp/web_urldispatcher.py` (PYTHON) -> Cumulative Risk: **959.03**
- **Archetype:** `file_cluster_16` (Distance: 11.986 IQR)
- **Magnitude:** 614.08 | **LOC:** 1310 | **CtrlFlow:** 27.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%), Concurrency (99.9928%)
- **Heaviest Functions:** `__init__` (Impact: 169.4), `_match` (Impact: 21.1), `__init__` (Impact: 20.4)

### 3. `aiohttp-3.13.5/aiohttp/_websocket/reader_c.py` (PYTHON) -> Cumulative Risk: **932.3**
- **Archetype:** `file_cluster_13` (Distance: 12.219 IQR)
- **Magnitude:** 536.22 | **LOC:** 479 | **CtrlFlow:** 60.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `_feed_data` (Impact: 262.4), `_read_from_buffer` (Impact: 22.2), `read` (Impact: 20.5)

### 4. `aiohttp-3.13.5/aiohttp/_websocket/reader_py.py` (PYTHON) -> Cumulative Risk: **932.3**
- **Archetype:** `file_cluster_13` (Distance: 12.219 IQR)
- **Magnitude:** 536.22 | **LOC:** 479 | **CtrlFlow:** 60.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `_feed_data` (Impact: 262.4), `_read_from_buffer` (Impact: 22.2), `read` (Impact: 20.5)

### 5. `aiohttp-3.13.5/aiohttp/streams.py` (PYTHON) -> Cumulative Risk: **923.4**
- **Archetype:** `file_cluster_4` (Distance: 12.774 IQR)
- **Magnitude:** 1620.12 | **LOC:** 763 | **CtrlFlow:** 43.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `_wait` (Impact: 775.7), `__repr__` (Impact: 109.8), `feed_data` (Impact: 40.9)

### 6. `aiohttp-3.13.5/aiohttp/client_proto.py` (PYTHON) -> Cumulative Risk: **920.65**
- **Archetype:** `file_cluster_16` (Distance: 11.758 IQR)
- **Magnitude:** 688.82 | **LOC:** 362 | **CtrlFlow:** 49.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `data_received` (Impact: 221.7), `connection_lost` (Impact: 185.6), `should_close` (Impact: 28.2)

### 7. `aiohttp-3.13.5/aiohttp/web_response.py` (PYTHON) -> Cumulative Risk: **916.75**
- **Archetype:** `file_cluster_16` (Distance: 12.223 IQR)
- **Magnitude:** 1345.84 | **LOC:** 857 | **CtrlFlow:** 47.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `text` (Impact: 411.1), `_prepare_headers` (Impact: 178.2), `etag` (Impact: 130.9)

### 8. `aiohttp-3.13.5/aiohttp/worker.py` (PYTHON) -> Cumulative Risk: **915.43**
- **Archetype:** `file_cluster_4` (Distance: 11.241 IQR)
- **Magnitude:** 326.28 | **LOC:** 263 | **CtrlFlow:** 40.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `_run` (Impact: 135.3), `_get_valid_log_format` (Impact: 22.3), `_create_ssl_context` (Impact: 16.7)

### 9. `aiohttp-3.13.5/aiohttp/multipart.py` (PYTHON) -> Cumulative Risk: **888.69**
- **Archetype:** `file_cluster_4` (Distance: 12.408 IQR)
- **Magnitude:** 2009.56 | **LOC:** 1214 | **CtrlFlow:** 41.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `append` (Impact: 620.1), `form` (Impact: 154.2), `write` (Impact: 94.6)

### 10. `aiohttp-3.13.5/aiohttp/base_protocol.py` (PYTHON) -> Cumulative Risk: **880.11**
- **Archetype:** `file_cluster_4` (Distance: 11.963 IQR)
- **Magnitude:** 231.36 | **LOC:** 101 | **CtrlFlow:** 34.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `pause_reading` (Impact: 35.0), `resume_reading` (Impact: 35.0), `connection_lost` (Impact: 26.9)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `aiohttp-3.13.5/aiohttp/_find_header.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.186 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.395 IQR)
- **Top Global Matches:** file_cluster_8: 11.186, file_cluster_12: 11.523, file_cluster_7: 11.718
- **Magnitude:** 6760.54 | **LOC:** 9871 | **CtrlFlow:** 72.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (83.0496%), Tech Debt (7.6994%)
**Top Internal Functions/Classes:**
  * `find_header` (Impact: 5351.1 | O(N^4) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4673`, `structural_boundaries: 1739`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 21`, `orphaned_logic: 1`
* *Architecture:* `api: 1202`, `import: 1`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.849
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` _find_header.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/examples/server.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.849
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/examples/server.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.849
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/aiohttp/connector.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.774 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.382 IQR)
- **Top Global Matches:** file_cluster_4: 12.774, file_cluster_16: 12.812, file_cluster_13: 12.864
- **Magnitude:** 4929.78 | **LOC:** 1855 | **CtrlFlow:** 48.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 159
- **Risk Profile:** Cognitive Load (48.5913%), Tech Debt (41.4069%)
**Top Internal Functions/Classes:**
  * `_wait_for_close` (Impact: 4410.4 | O(2^N) | DB: 159)
    * *Intent:* """Wait for all waiters to finish closing."""
  * `__del__` (Impact: 9.0 | O(N^4))
  * `__await__` (Impact: 5.3 | O(2^N) | DB: 1)
  * `path` (Impact: 2.8 | O(N^2))
  * `path` (Impact: 2.8 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 293`, `structural_boundaries: 312`, `args: 79`, `func_start: 79`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 211`, `dead_code: 2`, `planned_debt: 1`, `duplicate_logic: 7`
* *Architecture:* `io: 29`, `api: 34`, `concurrency: 219`, `import: 30`
* *Defense:* `safety: 75`, `doc: 86`, `test: 8`, `immutability_locks: 6`, `cleanup: 24`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.041
  * `Choke Point (Betweenness):` 0.007715 | `Ripple Effect (Closeness):` 0.163496
  * `Imports (Out-Degree: 8):` .log, warnings, itertools, .abc, .resolver, traceback, types, .tracing...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `aiohttp-3.13.5/tests/test_client_functional.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.752 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.444 IQR)
- **Top Global Matches:** file_cluster_4: 12.752, file_cluster_16: 13.19, file_cluster_8: 13.206
- **Magnitude:** 4829.06 | **LOC:** 5805 | **CtrlFlow:** 13.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 331
- **Risk Profile:** Cognitive Load (38.4985%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_POST_FILES_SINGLE_content_dispositi` (Impact: 1051.3 | O(N^5) | DB: 331)
    * *Intent:* # if system cannot determine 'application/pgp-keys' MIME type
  * `test_amazon_like_cookie_scenario` (Impact: 77.7 | O(N^6) | DB: 10)
  * `test_readline_error_on_conn_close` (Impact: 72.4 | O(N^6) | DB: 9)
  * `test_GET_DEFLATE` (Impact: 31.0 | O(N^4) | DB: 1)
  * `handler` (Impact: 28.2 | O(N^5) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 369`, `structural_boundaries: 2319`, `args: 538`, `func_start: 538`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 41`, `state_mutation: 69`, `dead_code: 3`, `duplicate_logic: 25`, `orphaned_logic: 129`
* *Architecture:* `io: 203`, `api: 545`, `concurrency: 1836`, `import: 37`
* *Defense:* `safety: 598`, `doc: 110`, `test: 924`, `sync_locks: 1`, `cleanup: 82`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.849
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` pytest_mock, aiohttp.abc, aiohttp.compression_utils, json, unittest, brotlicffi, aiohttp.payload, logging...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/tests/test_connector.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.698 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.912 IQR)
- **Top Global Matches:** file_cluster_4: 12.698, file_cluster_8: 12.944, file_cluster_16: 13.022
- **Magnitude:** 3447.3 | **LOC:** 4537 | **CtrlFlow:** 20.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 767
- **Risk Profile:** Cognitive Load (38.4734%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_tcp_connector_resolve_host` (Impact: 1598.2 | O(N^5) | DB: 767)
  * `test_tcp_connector_multiple_hosts_errors` (Impact: 98.0 | O(N^5) | DB: 40)
  * `test_tcp_connector_interleave` (Impact: 32.2 | O(N^4) | DB: 29)
  * `test_tcp_connector_family_is_respected` (Impact: 25.3 | O(N^4) | DB: 23)
  * `_resolve_host` (Impact: 20.6 | O(N^4) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 284`, `structural_boundaries: 1131`, `args: 255`, `func_start: 252`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 87`, `planned_debt: 1`, `duplicate_logic: 4`, `orphaned_logic: 45`
* *Architecture:* `io: 341`, `api: 240`, `concurrency: 1040`, `import: 30`
* *Defense:* `safety: 420`, `doc: 80`, `test: 922`, `sync_locks: 4`, `cleanup: 166`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.849
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` aiohttp.tracing, warnings, aiohttp.client_proto, pytest_mock, unittest, aiohttp.resolver, uuid, concurrent...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/aiohttp/client_reqrep.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.997 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.301 IQR)
- **Top Global Matches:** file_cluster_4: 12.997, file_cluster_13: 13.06, file_cluster_16: 13.089
- **Magnitude:** 2629.68 | **LOC:** 1537 | **CtrlFlow:** 52.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 58
- **Risk Profile:** Cognitive Load (59.876%), Tech Debt (9.3782%)
**Top Internal Functions/Classes:**
  * `links` (Impact: 1693.9 | O(2^N) | DB: 58)
  * `send` (Impact: 145.2 | O(N^5) | DB: 6)
  * `update_body_from_data` (Impact: 87.0 | O(N^4) | DB: 4)
  * `close` (Impact: 36.5 | O(N^5) | DB: 4)
    * *Intent:* # Specify request target: # - CONNECT request must send authority form URI # - not CONNECT proxy mus...
  * `__del__` (Impact: 26.7 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 276`, `structural_boundaries: 255`, `args: 81`, `func_start: 79`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 249`, `dead_code: 5`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `io: 6`, `api: 63`, `concurrency: 173`, `import: 34`
* *Defense:* `safety: 46`, `doc: 50`, `test: 13`, `immutability_locks: 1`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 17.763
  * `Choke Point (Betweenness):` 0.025696 | `Ripple Effect (Closeness):` 0.218347
  * `Imports (Out-Degree: 11):` warnings, .compression_utils, .formdata, .abc, traceback, .connector, types, attr...
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

### `aiohttp-3.13.5/tests/test_web_functional.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.154 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.568 IQR)
- **Top Global Matches:** file_cluster_4: 12.154, file_cluster_8: 12.68, file_cluster_0: 12.753
- **Magnitude:** 2067.3 | **LOC:** 2383 | **CtrlFlow:** 8.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 30
- **Risk Profile:** Cognitive Load (47.4405%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_cancel_shutdown` (Impact: 41.8 | O(N^5))
  * `test_response_with_streamer` (Impact: 27.5 | O(N^5) | DB: 9)
  * `test_response_with_streamer_no_params` (Impact: 27.5 | O(N^5) | DB: 9)
  * `test_request_tracing` (Impact: 27.0 | O(N^6) | DB: 30)
  * `test_keepalive_race_condition` (Impact: 24.4 | O(N^3) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 1121`, `args: 229`, `func_start: 229`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 61`, `fragile_debt: 4`, `duplicate_logic: 5`, `orphaned_logic: 102`
* *Architecture:* `io: 66`, `api: 229`, `concurrency: 905`, `import: 21`
* *Defense:* `safety: 288`, `doc: 6`, `test: 425`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.849
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` aiohttp.hdrs, aiohttp.compression_utils, json, unittest, brotlicffi, aiohttp, aiohttp.typedefs, aiohttp.pytest_plugin...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/aiohttp/multipart.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.408 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.633 IQR)
- **Top Global Matches:** file_cluster_4: 12.408, file_cluster_16: 12.517, file_cluster_13: 12.625
- **Magnitude:** 2009.56 | **LOC:** 1214 | **CtrlFlow:** 41.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (49.841%), Tech Debt (94.1161%)
**Top Internal Functions/Classes:**
  * `append` (Impact: 620.1 | O(2^N) | DB: 8)
    * *Intent:* # Refer to RFCs 7231, 7230, 5234. # # parameter = token "=" ( token / quoted-string ) # token = 1*tc...
  * `form` (Impact: 154.2 | O(N^4) | DB: 9)
  * `write` (Impact: 94.6 | O(2^N) | DB: 4)
  * `readline` (Impact: 91.5 | O(2^N) | DB: 3)
  * `read_chunk` (Impact: 80.0 | O(N^5) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 213`, `structural_boundaries: 307`, `args: 79`, `func_start: 79`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 177`, `duplicate_logic: 18`
* *Architecture:* `io: 1`, `api: 58`, `concurrency: 260`, `import: 25`
* *Defense:* `safety: 23`, `doc: 80`, `test: 9`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.223
  * `Choke Point (Betweenness):` 0.009907 | `Ripple Effect (Closeness):` 0.169219
  * `Imports (Out-Degree: 10):` .log, warnings, .compression_utils, .abc, .http_exceptions, json, uuid, .hdrs...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `aiohttp-3.13.5/aiohttp/streams.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.774 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 7.071 IQR)
- **Top Global Matches:** file_cluster_4: 12.774, file_cluster_16: 12.962, file_cluster_13: 13.153
- **Magnitude:** 1620.12 | **LOC:** 763 | **CtrlFlow:** 43.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (61.8946%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `_wait` (Impact: 775.7 | O(2^N) | DB: 9)
    * *Intent:* # wake up readchunk when end of http chunk received waiter = self._waiter if waiter is not None: sel...
  * `__repr__` (Impact: 109.8 | O(N^4) | DB: 18)
  * `feed_data` (Impact: 40.9 | O(2^N) | DB: 2)
  * `read` (Impact: 40.9 | O(N^4) | DB: 2)
  * `end_http_chunk_receiving` (Impact: 36.5 | O(N^4) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 124`, `structural_boundaries: 159`, `args: 64`, `func_start: 64`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 172`, `dead_code: 2`, `planned_debt: 4`, `duplicate_logic: 28`
* *Architecture:* `api: 60`, `concurrency: 155`, `import: 8`
* *Defense:* `safety: 21`, `doc: 24`, `test: 4`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 17.832
  * `Choke Point (Betweenness):` 0.003905 | `Ripple Effect (Closeness):` 0.258349
  * `Imports (Out-Degree: 3):` .log, .base_protocol, warnings, typing, .helpers, asyncio, .http_exceptions, collections
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `aiohttp-3.13.5/tests/test_multipart.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.276 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.837 IQR)
- **Top Global Matches:** file_cluster_4: 12.276, file_cluster_8: 12.605, file_cluster_16: 12.707
- **Magnitude:** 1577.7 | **LOC:** 1864 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 63
- **Risk Profile:** Cognitive Load (45.0265%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_release_next` (Impact: 137.6 | O(N^5) | DB: 40)
  * `test_read_json` (Impact: 126.0 | O(N^4) | DB: 63)
  * `test_read_with_content_transfer_encoding` (Impact: 81.7 | O(N^5) | DB: 21)
  * `test_read_boundary_across_chunks` (Impact: 64.8 | O(N^5) | DB: 14)
  * `test_read_incomplete_body_chunked` (Impact: 56.1 | O(N^5) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 139`, `structural_boundaries: 601`, `args: 145`, `func_start: 145`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 101`, `fragile_debt: 10`, `duplicate_logic: 9`, `orphaned_logic: 30`
* *Architecture:* `io: 131`, `api: 148`, `concurrency: 429`, `import: 17`
* *Defense:* `safety: 210`, `doc: 8`, `test: 373`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.849
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` typing, aiohttp.multipart, aiohttp.streams, sys, asyncio, io, aiohttp.abc, aiohttp...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/aiohttp/_cookie_helpers.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.048 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.042 IQR)
- **Top Global Matches:** file_cluster_13: 11.048, file_cluster_8: 11.128, file_cluster_16: 11.148
- **Magnitude:** 1489.05 | **LOC:** 339 | **CtrlFlow:** 65.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (18.6294%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 29`, `args: 5`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 15`, `dead_code: 2`
* *Architecture:* `api: 4`, `import: 4`
* *Defense:* `doc: 14`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 15.029
  * `Choke Point (Betweenness):` 0.000353 | `Ripple Effect (Closeness):` 0.226807
  * `Imports (Out-Degree: 1):` re, .log, typing, http.cookies
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `aiohttp-3.13.5/examples/combined_middleware.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.974 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 5.971 IQR)
- **Top Global Matches:** file_cluster_8: 10.974, file_cluster_4: 10.998, file_cluster_16: 11.026
- **Magnitude:** 1424.67 | **LOC:** 321 | **CtrlFlow:** 31.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (35.9998%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 67`, `args: 14`, `func_start: 14`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 21`
* *Architecture:* `io: 1`, `api: 11`, `concurrency: 41`, `import: 8`
* *Defense:* `safety: 5`, `doc: 28`, `test: 1`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.849
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` typing, time, logging, asyncio, base64, aiohttp, http, binascii
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/aiohttp/web_response.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.223 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.473 IQR)
- **Top Global Matches:** file_cluster_16: 12.223, file_cluster_13: 12.319, file_cluster_0: 12.325
- **Magnitude:** 1345.84 | **LOC:** 857 | **CtrlFlow:** 47.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (80.1365%), Tech Debt (99.6041%)
**Top Internal Functions/Classes:**
  * `text` (Impact: 411.1 | O(2^N) | DB: 7)
  * `_prepare_headers` (Impact: 178.2 | O(N^6) | DB: 1)
  * `etag` (Impact: 130.9 | O(2^N) | DB: 1)
  * `charset` (Impact: 44.0 | O(2^N) | DB: 1)
  * `enable_chunked_encoding` (Impact: 40.6 | O(N^4) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 179`, `structural_boundaries: 198`, `args: 59`, `func_start: 59`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 104`, `planned_debt: 2`, `duplicate_logic: 14`
* *Architecture:* `api: 57`, `concurrency: 70`, `import: 21`
* *Defense:* `safety: 43`, `doc: 12`, `test: 22`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 27.579
  * `Choke Point (Betweenness):` 0.004479 | `Ripple Effect (Closeness):` 0.22638
  * `Imports (Out-Degree: 7):` concurrent.futures, warnings, .compression_utils, .abc, json, .payload, .web_request, ...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `aiohttp-3.13.5/aiohttp/http_parser.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.008 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.051 IQR)
- **Top Global Matches:** file_cluster_8: 12.008, file_cluster_13: 12.077, file_cluster_16: 12.101
- **Magnitude:** 1310.5 | **LOC:** 1126 | **CtrlFlow:** 64.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 37
- **Risk Profile:** Cognitive Load (67.8605%), Tech Debt (21.7709%)
**Top Internal Functions/Classes:**
  * `feed_data` (Impact: 904.5 | O(2^N) | DB: 37)
  * `parse_message` (Impact: 76.5 | O(N^4))
  * `feed_eof` (Impact: 35.2 | O(2^N) | DB: 3)
  * `_is_chunked_te` (Impact: 10.7 | O(N^3))
  * `begin_http_chunk_receiving` (Impact: 5.3 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 196`, `structural_boundaries: 107`, `args: 25`, `func_start: 25`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 219`, `dead_code: 1`, `duplicate_logic: 4`
* *Architecture:* `api: 28`, `concurrency: 2`, `import: 18`
* *Defense:* `safety: 28`, `doc: 13`, `test: 6`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 15.531
  * `Choke Point (Betweenness):` 0.012521 | `Ripple Effect (Closeness):` 0.225625
  * `Imports (Out-Degree: 9):` , re, yarl, typing, contextlib, .base_protocol, .compression_utils, .helpers...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `aiohttp-3.13.5/tests/test_client_ws_functional.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.544 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.942 IQR)
- **Top Global Matches:** file_cluster_4: 11.544, file_cluster_8: 12.155, file_cluster_16: 12.323
- **Magnitude:** 1235.58 | **LOC:** 1279 | **CtrlFlow:** 8.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (42.7166%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_closed_async_for` (Impact: 21.6 | O(N^3) | DB: 4)
  * `test_ws_client_async_for` (Impact: 17.2 | O(N^3))
  * `test_ping_pong` (Impact: 15.1 | O(N^3) | DB: 6)
  * `handler` (Impact: 14.1 | O(N^3) | DB: 4)
  * `test_ping_pong_manual` (Impact: 13.9 | O(N^3) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 689`, `args: 93`, `func_start: 93`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 26`, `dead_code: 1`, `duplicate_logic: 6`, `orphaned_logic: 46`
* *Architecture:* `io: 47`, `api: 94`, `concurrency: 692`, `import: 13`
* *Defense:* `safety: 126`, `doc: 16`, `test: 182`, `cleanup: 65`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.849
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` typing, sys, asyncio, async_timeout, aiohttp, aiohttp._websocket.reader, unittest, pytest...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/tests/test_run_app.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.31 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.207 IQR)
- **Top Global Matches:** file_cluster_4: 11.31, file_cluster_8: 11.828, file_cluster_13: 11.972
- **Magnitude:** 1229.78 | **LOC:** 1316 | **CtrlFlow:** 19.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (49.1544%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test` (Impact: 64.0 | O(N^6))
  * `test_shutdown_close_websockets` (Impact: 51.2 | O(N^6) | DB: 11)
    * *Intent:* # If not, then shutdown_timeout will allow it to sleep until complete. assert t.cancelled() def test...
  * `test` (Impact: 36.0 | O(N^6) | DB: 3)
  * `test` (Impact: 31.8 | O(N^6))
  * `test` (Impact: 24.8 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 250`, `args: 82`, `func_start: 81`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 74`, `duplicate_logic: 16`, `orphaned_logic: 36`
* *Architecture:* `io: 58`, `api: 82`, `concurrency: 549`, `import: 18`
* *Defense:* `safety: 66`, `doc: 2`, `test: 121`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.849
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` platform, typing, time, sys, ssl, aiohttp.web_runner, asyncio, logging...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/tests/test_client_request.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.853 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.572 IQR)
- **Top Global Matches:** file_cluster_4: 12.853, file_cluster_16: 12.895, file_cluster_0: 13.045
- **Magnitude:** 1219.3 | **LOC:** 2283 | **CtrlFlow:** 10.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 98
- **Risk Profile:** Cognitive Load (22.8036%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_urlencoded_formdata_charset` (Impact: 340.8 | O(N^4) | DB: 98)
  * `transport` (Impact: 16.8 | O(2^N) | DB: 2)
  * `test_query_bytes_param_raises` (Impact: 10.6 | O(N^3))
  * `test_method_invalid` (Impact: 7.9 | O(N^2))
  * `test_content_type_auto_header_content_le` (Impact: 7.6 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 703`, `args: 202`, `func_start: 202`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 34`, `orphaned_logic: 78`
* *Architecture:* `io: 46`, `api: 200`, `concurrency: 354`, `import: 21`
* *Defense:* `safety: 296`, `doc: 84`, `test: 538`, `immutability_locks: 1`, `cleanup: 102`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.849
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` warnings, aiohttp.abc, aiohttp.compression_utils, unittest, aiohttp, urllib.parse, typing, asyncio...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/aiohttp/helpers.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.154 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.523 IQR)
- **Top Global Matches:** file_cluster_13: 12.154, file_cluster_16: 12.211, file_cluster_4: 12.367
- **Magnitude:** 1200.32 | **LOC:** 987 | **CtrlFlow:** 40.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 30
- **Risk Profile:** Cognitive Load (27.8835%), Tech Debt (9.3524%)
**Top Internal Functions/Classes:**
  * `rfc822_formatted_time` (Impact: 340.3 | O(N^5) | DB: 30)
  * `netrc_from_env` (Impact: 285.2 | O(2^N) | DB: 3)
    * *Intent:* """ netrc_env = os.environ.get("NETRC") if netrc_env is not None: netrc_path = Path(netrc_env) else:...
  * `parse_mimetype` (Impact: 180.6 | O(N^6) | DB: 4)
  * `decode` (Impact: 102.3 | O(2^N))
  * `get_env_proxy_for_url` (Impact: 21.6 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 148`, `structural_boundaries: 221`, `args: 67`, `func_start: 66`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 70`, `dead_code: 2`, `planned_debt: 2`
* *Architecture:* `io: 11`, `api: 63`, `concurrency: 60`, `import: 35`
* *Defense:* `safety: 30`, `doc: 60`, `test: 3`, `immutability_locks: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 6.15
  * `Choke Point (Betweenness):` 0.00025 | `Ripple Effect (Closeness):` 0.141297
  * `Imports (Out-Degree: 2):` email.policy, .log, email.utils, async_timeout, types, attr, platform, base64...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `aiohttp-3.13.5/tests/test_streams.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.247 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.203 IQR)
- **Top Global Matches:** file_cluster_4: 12.247, file_cluster_8: 12.338, file_cluster_16: 12.446
- **Magnitude:** 1171.48 | **LOC:** 1726 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (44.617%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_unread_data` (Impact: 158.1 | O(N^3))
  * `test_read_eof_unread_data_no_warning` (Impact: 57.5 | O(N^3) | DB: 3)
    * *Intent:* # Read bytes. stream = self._make_one() stream.feed_eof() with mock.patch("aiohttp.streams.internal_...
  * `get_memory_usage` (Impact: 27.1 | O(N^4) | DB: 1)
  * `test_ctor_global_loop` (Impact: 11.0 | O(N^3))
  * `test_readuntil_exception` (Impact: 10.9 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 574`, `args: 137`, `func_start: 137`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 11`, `duplicate_logic: 6`, `orphaned_logic: 56`
* *Architecture:* `io: 4`, `api: 138`, `concurrency: 435`, `import: 11`
* *Defense:* `safety: 248`, `doc: 12`, `test: 430`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.849
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` gc, itertools, asyncio, aiohttp, re_assert, unittest, pytest, aiohttp.http_exceptions...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/tests/test_web_websocket_functional.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.527 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.676 IQR)
- **Top Global Matches:** file_cluster_4: 11.527, file_cluster_8: 12.026, file_cluster_16: 12.23
- **Magnitude:** 1155.44 | **LOC:** 1397 | **CtrlFlow:** 4.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (39.7145%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_websocket_shutdown` (Impact: 30.8 | O(N^4) | DB: 11)
  * `handler` (Impact: 27.9 | O(N^5) | DB: 1)
  * `test_websocket_json` (Impact: 27.5 | O(N^3) | DB: 18)
  * `test_server_ws_async_for` (Impact: 23.2 | O(N^4) | DB: 9)
  * `test_closed_async_for` (Impact: 14.7 | O(N^4) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 742`, `args: 92`, `func_start: 92`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 21`, `duplicate_logic: 14`, `orphaned_logic: 39`
* *Architecture:* `io: 30`, `api: 92`, `concurrency: 700`, `import: 11`
* *Defense:* `safety: 160`, `doc: 24`, `test: 195`, `sync_locks: 4`, `cleanup: 65`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.849
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` typing, sys, asyncio, aiohttp, unittest, pytest, weakref, aiohttp.pytest_plugin...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/tests/test_client_middleware.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.424 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.318 IQR)
- **Top Global Matches:** file_cluster_4: 12.424, file_cluster_16: 12.743, file_cluster_8: 12.869
- **Magnitude:** 1105.62 | **LOC:** 1272 | **CtrlFlow:** 19.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (24.9543%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_client_middleware_multi_step_auth` (Impact: 124.9 | O(N^5))
  * `test_client_middleware_challenge_auth` (Impact: 97.3 | O(N^5) | DB: 1)
  * `test_client_middleware_stateful_retry` (Impact: 49.4 | O(N^5) | DB: 2)
  * `test_client_middleware_retry` (Impact: 35.2 | O(N^4) | DB: 1)
  * `test_client_middleware_auth_example` (Impact: 28.5 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 119`, `structural_boundaries: 483`, `args: 87`, `func_start: 87`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 45`, `duplicate_logic: 42`, `orphaned_logic: 19`
* *Architecture:* `io: 10`, `api: 84`, `concurrency: 385`, `import: 11`
* *Defense:* `safety: 121`, `doc: 82`, `test: 153`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.849
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` typing, aiohttp.client_proto, aiohttp.abc, aiohttp, socket, aiohttp.client_middlewares, json, pytest...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/tests/test_client_session.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.513 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.615 IQR)
- **Top Global Matches:** file_cluster_4: 12.513, file_cluster_0: 12.716, file_cluster_13: 12.786
- **Magnitude:** 1019.2 | **LOC:** 1414 | **CtrlFlow:** 16.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 68
- **Risk Profile:** Cognitive Load (37.1323%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_cookie_jar_usage` (Impact: 189.2 | O(N^5) | DB: 68)
  * `test_ssl_shutdown_timeout_passed_to_conn` (Impact: 66.9 | O(N^4))
  * `test_ssl_shutdown_timeout_passed_to_conn` (Impact: 56.9 | O(N^4))
    * *Intent:* # Test custom value - expect both deprecation and runtime warnings with warnings.catch_warnings(reco...
  * `test_connector_loop` (Impact: 21.1 | O(N^4))
  * `test_close_conn_on_error` (Impact: 17.9 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 93`, `structural_boundaries: 461`, `args: 110`, `func_start: 107`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 39`, `state_mutation: 42`, `dead_code: 5`, `duplicate_logic: 6`, `orphaned_logic: 47`
* *Architecture:* `io: 45`, `api: 107`, `concurrency: 247`, `import: 27`
* *Defense:* `safety: 168`, `doc: 18`, `test: 321`, `cleanup: 32`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.849
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` aiohttp.tracing, warnings, aiohttp.client_proto, json, unittest, uuid, gc, aiohttp...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/aiohttp/client_ws.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.465 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 7.396 IQR)
- **Top Global Matches:** file_cluster_4: 12.465, file_cluster_13: 12.736, file_cluster_16: 12.743
- **Magnitude:** 930.7 | **LOC:** 429 | **CtrlFlow:** 30.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (64.9905%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `receive` (Impact: 270.3 | O(2^N) | DB: 9)
  * `close` (Impact: 136.6 | O(2^N) | DB: 8)
    * *Intent:* # `close()` may be called from different task if self._waiting and not self._closing: assert self._l...
  * `_send_heartbeat` (Impact: 70.9 | O(2^N) | DB: 7)
  * `get_extra_info` (Impact: 24.5 | O(2^N))
  * `_reset_heartbeat` (Impact: 18.3 | O(N^3) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 134`, `args: 32`, `func_start: 32`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 95`
* *Architecture:* `io: 2`, `api: 31`, `concurrency: 147`, `import: 15`
* *Defense:* `safety: 18`, `doc: 14`, `test: 2`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.242
  * `Choke Point (Betweenness):` 0.000367 | `Ripple Effect (Closeness):` 0.005208
  * `Imports (Out-Degree: 7):` .streams, typing, .client_reqrep, .helpers, sys, .http, asyncio, async_timeout...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `aiohttp-3.13.5/tests/test_http_parser.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.645 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.174 IQR)
- **Top Global Matches:** file_cluster_8: 12.645, file_cluster_0: 12.647, file_cluster_16: 12.683
- **Magnitude:** 855.36 | **LOC:** 2232 | **CtrlFlow:** 19.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 93
- **Risk Profile:** Cognitive Load (4.8917%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_parse_chunked_payload_chunk_extensi` (Impact: 56.4 | O(N^3))
  * `test_parse_uri_utf8_percent_encoded` (Impact: 50.7 | O(N^3) | DB: 93)
  * `test_max_trailer_size` (Impact: 31.4 | O(N^4))
  * `test_max_header_field_size` (Impact: 21.2 | O(N^3))
  * `test_max_header_value_size` (Impact: 21.2 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 154`, `structural_boundaries: 636`, `args: 175`, `func_start: 175`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 48`, `state_mutation: 6`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 2`, `orphaned_logic: 67`
* *Architecture:* `io: 43`, `api: 176`, `concurrency: 86`, `import: 20`
* *Defense:* `safety: 412`, `doc: 36`, `test: 694`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.849
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` re, yarl, typing, sys, brotli, asyncio, aiohttp.http_parser, aiohttp...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `aiohttp-3.13.5/tests/test_tcp_helpers.py` (PYTHON) | Magnitude: 29.84 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 38, io: 33, test: 24, structural_boundaries: 22
- `aiohttp-3.13.5/tests/autobahn/test_autobahn.py` (PYTHON) | Magnitude: 124.66 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 98, branch: 24, structural_boundaries: 21, test: 16
- `aiohttp-3.13.5/tests/test_resolver.py` (PYTHON) | Magnitude: 293.96 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 374, structural_boundaries: 186, test: 166, concurrency: 114
- `aiohttp-3.13.5/tests/test_client_connection.py` (PYTHON) | Magnitude: 69.6 | Delta: **0.101 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 79, structural_boundaries: 50, test: 44, safety: 19
- `aiohttp-3.13.5/tests/test_route_def.py` (PYTHON) | Magnitude: 137.2 | Delta: **0.196 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 181, structural_boundaries: 143, test: 98, safety: 72

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `aiohttp-3.13.5/tests/test_classbasedview.py` (PYTHON) | Magnitude: 43.58 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: structural_boundaries: 31, indent_spaces: 31, test: 18, api: 10
- `aiohttp-3.13.5/aiohttp/_websocket/reader_c.py` (PYTHON) | Magnitude: 536.22 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 332, encapsulation: 152, state_mutation: 134, branch: 92
- `aiohttp-3.13.5/aiohttp/_websocket/reader_py.py` (PYTHON) | Magnitude: 536.22 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 332, encapsulation: 152, state_mutation: 134, branch: 92
- `aiohttp-3.13.5/aiohttp/client_middleware_digest_auth.py` (PYTHON) | Magnitude: 82.44 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 234, branch: 56, structural_boundaries: 56, state_mutation: 41
- `aiohttp-3.13.5/tests/test_benchmarks_client_request.py` (PYTHON) | Magnitude: 98.2 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 116, structural_boundaries: 51, concurrency: 22, generics: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `aiohttp-3.13.5/tests/test_websocket_parser.py` (PYTHON) | Magnitude: 229.44 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 394, structural_boundaries: 190, test: 165, encapsulation: 96
- `aiohttp-3.13.5/aiohttp/client_proto.py` (PYTHON) | Magnitude: 688.82 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 254, encapsulation: 108, state_mutation: 77, structural_boundaries: 55
- `aiohttp-3.13.5/aiohttp/web_app.py` (PYTHON) | Magnitude: 642.84 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 447, encapsulation: 211, structural_boundaries: 154, generics: 84
- `aiohttp-3.13.5/aiohttp/_websocket/models.py` (PYTHON) | Magnitude: 24.82 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 40, structural_boundaries: 16, doc: 8, safety_bypasses: 7
- `aiohttp-3.13.5/tests/test_web_response.py` (PYTHON) | Magnitude: 655.72 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 934, structural_boundaries: 551, test: 488, safety: 256

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `aiohttp-3.13.5/tests/test_payload.py` (PYTHON) | Magnitude: 572.48 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 707, structural_boundaries: 448, test: 256, concurrency: 203
- `aiohttp-3.13.5/aiohttp/web_ws.py` (PYTHON) | Magnitude: 747.46 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 471, encapsulation: 209, structural_boundaries: 175, concurrency: 106
- `aiohttp-3.13.5/aiohttp/_websocket/writer.py` (PYTHON) | Magnitude: 162.18 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 139, concurrency: 42, encapsulation: 34, branch: 31
- `aiohttp-3.13.5/tests/isolated/check_for_request_leak.py` (PYTHON) | Magnitude: 41.98 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 22, indent_spaces: 20, concurrency: 14, import: 6
- `aiohttp-3.13.5/aiohttp/connector.py` (PYTHON) | Magnitude: 4929.78 | Delta: **0.038 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 1235, encapsulation: 409, structural_boundaries: 312, branch: 293

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `aiohttp-3.13.5/tests/test_urldispatch.py` (PYTHON) | Magnitude: 698.42 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 851, structural_boundaries: 462, test: 390, safety: 224
- `aiohttp-3.13.5/tests/test_helpers.py` (PYTHON) | Magnitude: 577.04 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 598, test: 265, structural_boundaries: 254, safety: 116
- `aiohttp-3.13.5/tests/test_http_parser.py` (PYTHON) | Magnitude: 855.36 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 1459, test: 694, structural_boundaries: 636, safety: 412
- `aiohttp-3.13.5/aiohttp/typedefs.py` (PYTHON) | Magnitude: 4.74 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 31, structural_boundaries: 15, generics: 14, encapsulation: 13
- `aiohttp-3.13.5/tests/test_multipart_helpers.py` (PYTHON) | Magnitude: 375.98 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 584, test: 340, structural_boundaries: 304, safety: 195

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `aiohttp-3.13.5/aiohttp/client_reqrep.py` -> **Severity: 2.567** (Bridge: 0.0257 * Flux: 99.9025%)
- `aiohttp-3.13.5/aiohttp/web_request.py` -> **Severity: 1.879** (Bridge: 0.0208 * Flux: 90.3003%)
- `aiohttp-3.13.5/aiohttp/test_utils.py` -> **Severity: 1.844** (Bridge: 0.0198 * Flux: 93.027%)
- `aiohttp-3.13.5/aiohttp/client_exceptions.py` -> **Severity: 1.684** (Bridge: 0.0169 * Flux: 99.5938%)
- `aiohttp-3.13.5/aiohttp/abc.py` -> **Severity: 1.483** (Bridge: 0.0215 * Flux: 68.9316%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `aiohttp-3.13.5/aiohttp/typedefs.py` -> **Severity: 21.927** (Embedded: 0.2969 * Error Risk: 73.8596%)
- `aiohttp-3.13.5/aiohttp/base_protocol.py` -> **Severity: 15.228** (Embedded: 0.2302 * Error Risk: 66.1446%)
- `aiohttp-3.13.5/aiohttp/web_routedef.py` -> **Severity: 14.675** (Embedded: 0.1834 * Error Risk: 80.0%)
- `aiohttp-3.13.5/aiohttp/compression_utils.py` -> **Severity: 14.6** (Embedded: 0.2409 * Error Risk: 60.6122%)
- `aiohttp-3.13.5/aiohttp/web_app.py` -> **Severity: 12.81** (Embedded: 0.2219 * Error Risk: 57.7207%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `aiohttp-3.13.5/aiohttp/abc.py` -> **Severity: 6542.899** (Blast Radius: 66.029 * Doc Risk: 99.0913%)
- `aiohttp-3.13.5/aiohttp/typedefs.py` -> **Severity: 3111.649** (Blast Radius: 59.124 * Doc Risk: 52.6292%)
- `aiohttp-3.13.5/aiohttp/web_response.py` -> **Severity: 2752.558** (Blast Radius: 27.579 * Doc Risk: 99.8063%)
- `aiohttp-3.13.5/aiohttp/web_request.py` -> **Severity: 2072.321** (Blast Radius: 22.473 * Doc Risk: 92.2138%)
- `aiohttp-3.13.5/aiohttp/base_protocol.py` -> **Severity: 2009.2** (Blast Radius: 20.092 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
