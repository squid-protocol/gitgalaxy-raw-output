# ARCHITECTURAL_BRIEF: aiohttp
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/aiohttp` |
| **Timestamp** | `2026-08-07T05:21:10.428028+00:00` |
| **Scan Duration** | `1.94s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 184 malicious artifacts.

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
| file_cluster_8 | 75 | 38.9% |
| file_cluster_4 | 56 | 29.0% |
| file_cluster_16 | 28 | 14.5% |
| file_cluster_13 | 23 | 11.9% |
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
| Cognitive Load Exposure | 0.0 | 98.9 | 29.3 | 22.7 | 5.0 |
| Error & Exception Exposure | 0.0 | 92.7 | 28.0 | 9.3 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 13.0 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 9.9 | 0.0 | 0.0 |
| API Exposure | 0.0 | 15.4 | 4.9 | 4.5 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 62.4 | 99.2 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 21.5 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 21.7 | 0.8 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 92.5 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 99.7 | 19.5 | 0.0 | 0.0 |
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

- `find_header` (@ `aiohttp-3.13.5/aiohttp/_find_header.c`) -> Impact: **2215.2** | LOC: 2492
- `_wait_for_close` (@ `aiohttp-3.13.5/aiohttp/connector.py`) -> Impact: **694.1** | LOC: 1494
  * *Intent:* """Wait for all waiters to finish closing."""
- `test_tcp_connector_resolve_host` (@ `aiohttp-3.13.5/tests/test_connector.py`) -> Impact: **641.2** | LOC: 3253
- `handler` (@ `aiohttp-3.13.5/tests/test_client_functional.py`) -> Impact: **479.0** | LOC: 2420
- `test_POST_FILES_SINGLE_content_dispositi` (@ `aiohttp-3.13.5/tests/test_client_functional.py`) -> Impact: **431.2** | LOC: 2423
  * *Intent:* # if system cannot determine 'application/pgp-keys' MIME type
- `links` (@ `aiohttp-3.13.5/aiohttp/client_reqrep.py`) -> Impact: **270.1** | LOC: 657
- `test_urlencoded_formdata_charset` (@ `aiohttp-3.13.5/tests/test_client_request.py`) -> Impact: **182.3** | LOC: 1533
- `feed_data` (@ `aiohttp-3.13.5/aiohttp/http_parser.py`) -> Impact: **139.8** | LOC: 247
- `__setitem__` (@ `aiohttp-3.13.5/aiohttp/web_app.py`) -> Impact: **129.6** | LOC: 391
- `rfc822_formatted_time` (@ `aiohttp-3.13.5/aiohttp/helpers.py`) -> Impact: **129.0** | LOC: 466

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `aiohttp-3.13.5/tests` | 74 | 30174.6 | 21.11% | 0.0% |
| `aiohttp-3.13.5/aiohttp` | 55 | 17792.27 | 39.59% | 37.6% |
| `aiohttp-3.13.5/examples` | 27 | 13175.41 | 41.17% | 0.0% |
| `aiohttp-3.13.5/aiohttp/_websocket` | 10 | 843.64 | 26.7% | 27.14% |
| `aiohttp-3.13.5` | 5 | 357.5 | 7.53% | 0.0% |
| `aiohttp-3.13.5/requirements` | 9 | 107.8 | 6.09% | 0.0% |
| `aiohttp-3.13.5/tests/autobahn/server` | 2 | 68.7 | 27.44% | 0.0% |
| `aiohttp-3.13.5/tests/isolated` | 2 | 67.76 | 35.79% | 0.0% |
| `aiohttp-3.13.5/tests/autobahn` | 1 | 65.86 | 7.65% | 0.0% |
| `aiohttp-3.13.5/tests/autobahn/client` | 2 | 57.68 | 27.18% | 0.0% |

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
- `aiohttp-3.13.5/tests/test_client_functional.py` -> **129** Orphaned Functions | **150** Duplicates
- `aiohttp-3.13.5/tests/test_web_functional.py` -> **103** Orphaned Functions | **112** Duplicates
- `aiohttp-3.13.5/tests/test_client_ws_functional.py` -> **46** Orphaned Functions | **45** Duplicates
- `aiohttp-3.13.5/tests/test_urldispatch.py` -> **84** Orphaned Functions | **6** Duplicates
- `aiohttp-3.13.5/tests/test_client_request.py` -> **78** Orphaned Functions | **0** Duplicates

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

### Hardcoded Payload Artifacts
- `aiohttp-3.13.5/examples/fake_server.py` -> **99.9954%** Exposure
- `aiohttp-3.13.5/tests/test_client_functional.py` -> **11.4686%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1317` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `aiohttp-3.13.5/aiohttp/web_runner.py` (PYTHON) -> Cumulative Risk: **766.43**
- **Archetype:** `file_cluster_4` (Distance: 11.442 IQR)
- **Magnitude:** 325.28 | **LOC:** 400 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Concurrency (100.0%), Spec Match (100.0%), State Flux (97.3748%)
- **Heaviest Functions:** `cleanup` (Impact: 11.3), `addresses` (Impact: 9.2), `name` (Impact: 8.9)

### 2. `aiohttp-3.13.5/aiohttp/streams.py` (PYTHON) -> Cumulative Risk: **761.36**
- **Archetype:** `file_cluster_4` (Distance: 12.776 IQR)
- **Magnitude:** 714.22 | **LOC:** 763 | **CtrlFlow:** 43.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Concurrency (100.0%), Spec Match (100.0%), State Flux (99.9972%)
- **Heaviest Functions:** `_wait` (Impact: 121.0), `__repr__` (Impact: 47.4), `read` (Impact: 16.9)

### 3. `aiohttp-3.13.5/aiohttp/client_proto.py` (PYTHON) -> Cumulative Risk: **752.21**
- **Archetype:** `file_cluster_16` (Distance: 11.758 IQR)
- **Magnitude:** 269.12 | **LOC:** 362 | **CtrlFlow:** 49.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9908%), Concurrency (97.4871%), Tech Debt (84.9326%)
- **Heaviest Functions:** `data_received` (Impact: 39.8), `connection_lost` (Impact: 29.7), `should_close` (Impact: 14.4)

### 4. `aiohttp-3.13.5/aiohttp/web_response.py` (PYTHON) -> Cumulative Risk: **743.55**
- **Archetype:** `file_cluster_16` (Distance: 12.221 IQR)
- **Magnitude:** 559.84 | **LOC:** 857 | **CtrlFlow:** 47.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.7719%), Tech Debt (99.6041%), State Flux (97.8537%)
- **Heaviest Functions:** `text` (Impact: 73.3), `_prepare_headers` (Impact: 53.2), `etag` (Impact: 23.5)

### 5. `aiohttp-3.13.5/aiohttp/_websocket/reader_c.py` (PYTHON) -> Cumulative Risk: **730.06**
- **Archetype:** `file_cluster_13` (Distance: 12.219 IQR)
- **Magnitude:** 309.42 | **LOC:** 479 | **CtrlFlow:** 60.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9995%), Tech Debt (99.6654%), Concurrency (99.1052%)
- **Heaviest Functions:** `_feed_data` (Impact: 80.5), `_read_from_buffer` (Impact: 9.2), `read` (Impact: 8.5)

### 6. `aiohttp-3.13.5/aiohttp/_websocket/reader_py.py` (PYTHON) -> Cumulative Risk: **730.06**
- **Archetype:** `file_cluster_13` (Distance: 12.219 IQR)
- **Magnitude:** 309.42 | **LOC:** 479 | **CtrlFlow:** 60.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9995%), Tech Debt (99.6654%), Concurrency (99.1052%)
- **Heaviest Functions:** `_feed_data` (Impact: 80.5), `_read_from_buffer` (Impact: 9.2), `read` (Impact: 8.5)

### 7. `aiohttp-3.13.5/aiohttp/multipart.py` (PYTHON) -> Cumulative Risk: **686.59**
- **Archetype:** `file_cluster_4` (Distance: 12.408 IQR)
- **Magnitude:** 927.26 | **LOC:** 1214 | **CtrlFlow:** 41.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), State Flux (99.7332%), Tech Debt (94.1161%)
- **Heaviest Functions:** `append` (Impact: 87.7), `form` (Impact: 67.2), `read_chunk` (Impact: 28.0)

### 8. `aiohttp-3.13.5/aiohttp/payload_streamer.py` (PYTHON) -> Cumulative Risk: **676.41**
- **Archetype:** `file_cluster_16` (Distance: 10.769 IQR)
- **Magnitude:** 39.0 | **LOC:** 79 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Concurrency (99.9998%), Safety Score (91.4198%)
- **Heaviest Functions:** `__init__` (Impact: 2.3), `__init__` (Impact: 2.1), `__call__` (Impact: 2.1)

### 9. `aiohttp-3.13.5/aiohttp/worker.py` (PYTHON) -> Cumulative Risk: **660.4**
- **Archetype:** `file_cluster_4` (Distance: 11.241 IQR)
- **Magnitude:** 184.08 | **LOC:** 263 | **CtrlFlow:** 40.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), State Flux (87.5752%), Cognitive Load (81.3904%)
- **Heaviest Functions:** `_run` (Impact: 47.4), `_get_valid_log_format` (Impact: 9.3), `_create_ssl_context` (Impact: 8.7)

### 10. `aiohttp-3.13.5/aiohttp/test_utils.py` (PYTHON) -> Cumulative Risk: **641.65**
- **Archetype:** `file_cluster_4` (Distance: 11.714 IQR)
- **Magnitude:** 358.54 | **LOC:** 778 | **CtrlFlow:** 19.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), State Flux (93.027%), Tech Debt (85.1136%)
- **Heaviest Functions:** `close` (Impact: 6.5), `make_url` (Impact: 5.6), `mock_coro` (Impact: 5.5)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `aiohttp-3.13.5/examples/server.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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

### `aiohttp-3.13.5/tests/test_client_functional.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.738 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.44 IQR)
- **Top Global Matches:** file_cluster_4: 12.738, file_cluster_16: 13.196, file_cluster_8: 13.212
- **Magnitude:** 4495.36 | **LOC:** 5805 | **CtrlFlow:** 13.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (38.5301%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `handler` (Impact: 479.0)
  * `test_POST_FILES_SINGLE_content_dispositi` (Impact: 431.2)
    * *Intent:* # if system cannot determine 'application/pgp-keys' MIME type
  * `test_amazon_like_cookie_scenario` (Impact: 27.4)
  * `test_readline_error_on_conn_close` (Impact: 22.1)
  * `test_GET_DEFLATE` (Impact: 14.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 369`, `structural_boundaries: 2319`, `args: 538`, `func_start: 538`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 41`, `state_mutation: 69`, `dead_code: 3`, `duplicate_logic: 150`, `orphaned_logic: 129`
* *Architecture:* `io: 203`, `api: 545`, `concurrency: 1831`, `import: 37`
* *Defense:* `safety: 598`, `doc: 110`, `test: 924`, `sync_locks: 1`, `cleanup: 82`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.849
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` http.cookies, aiohttp.typedefs, time, zlib, zipfile, ssl, datetime, aiohttp.http_exceptions...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/aiohttp/_find_header.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.186 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.395 IQR)
- **Top Global Matches:** file_cluster_8: 11.186, file_cluster_12: 11.523, file_cluster_7: 11.718
- **Magnitude:** 3624.64 | **LOC:** 9871 | **CtrlFlow:** 72.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (83.0496%), Tech Debt (7.6994%)
**Top Internal Functions/Classes:**
  * `find_header` (Impact: 2215.2)
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

### `aiohttp-3.13.5/tests/test_connector.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.679 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.899 IQR)
- **Top Global Matches:** file_cluster_4: 12.679, file_cluster_8: 12.923, file_cluster_16: 13.004
- **Magnitude:** 2401.4 | **LOC:** 4537 | **CtrlFlow:** 20.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (38.4135%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_tcp_connector_resolve_host` (Impact: 641.2)
  * `test_tcp_connector_multiple_hosts_errors` (Impact: 38.0)
  * `create_connection` (Impact: 24.6)
  * `test_tcp_connector_interleave` (Impact: 15.4)
  * `test_tcp_connector_family_is_respected` (Impact: 11.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 284`, `structural_boundaries: 1131`, `args: 262`, `func_start: 252`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 81`, `planned_debt: 1`, `duplicate_logic: 19`, `orphaned_logic: 45`
* *Architecture:* `io: 341`, `api: 240`, `concurrency: 1040`, `import: 30`
* *Defense:* `safety: 420`, `doc: 80`, `test: 922`, `sync_locks: 4`, `cleanup: 166`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.849
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` aiohttp.resolver, ssl, aiohttp.client, uuid, warnings, pytest_mock, logging, gc...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/tests/test_web_functional.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.1 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.555 IQR)
- **Top Global Matches:** file_cluster_4: 12.1, file_cluster_8: 12.645, file_cluster_0: 12.7
- **Magnitude:** 2021.6 | **LOC:** 2383 | **CtrlFlow:** 8.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.4206%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_cancel_shutdown` (Impact: 15.0)
  * `test_keepalive_race_condition` (Impact: 13.2)
  * `handler` (Impact: 12.2)
  * `test_post_files` (Impact: 11.5)
  * `test_response_with_streamer` (Impact: 10.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 1121`, `args: 229`, `func_start: 229`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 57`, `fragile_debt: 4`, `duplicate_logic: 112`, `orphaned_logic: 103`
* *Architecture:* `io: 66`, `api: 229`, `concurrency: 875`, `import: 21`
* *Defense:* `safety: 288`, `doc: 6`, `test: 425`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.849
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` aiohttp.typedefs, ssl, aiohttp.web_protocol, typing, aiohttp.hdrs, asyncio, aiohttp.pytest_plugin, io...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/aiohttp/_cookie_helpers.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.048 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.042 IQR)
- **Top Global Matches:** file_cluster_13: 11.048, file_cluster_8: 11.128, file_cluster_16: 11.148
- **Magnitude:** 1489.05 | **LOC:** 339 | **CtrlFlow:** 65.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (18.6294%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 29`, `args: 5`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 15`, `dead_code: 2`
* *Architecture:* `api: 4`, `import: 4`
* *Defense:* `doc: 14`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 15.029
  * `Choke Point (Betweenness):` 0.000353 | `Ripple Effect (Closeness):` 0.226807
  * `Imports (Out-Degree: 1):` http.cookies, typing, re, .log
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `aiohttp-3.13.5/examples/combined_middleware.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.974 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 5.971 IQR)
- **Top Global Matches:** file_cluster_8: 10.974, file_cluster_4: 10.998, file_cluster_16: 11.026
- **Magnitude:** 1424.67 | **LOC:** 321 | **CtrlFlow:** 31.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (35.9998%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 67`, `args: 14`, `func_start: 14`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 21`
* *Architecture:* `io: 1`, `api: 11`, `concurrency: 41`, `import: 8`
* *Defense:* `safety: 5`, `doc: 28`, `test: 1`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.849
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` time, base64, binascii, logging, asyncio, aiohttp, http, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/aiohttp/connector.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.775 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.34 IQR)
- **Top Global Matches:** file_cluster_4: 12.775, file_cluster_16: 12.786, file_cluster_13: 12.839
- **Magnitude:** 1263.48 | **LOC:** 1855 | **CtrlFlow:** 48.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.3501%), Tech Debt (48.5942%)
**Top Internal Functions/Classes:**
  * `_wait_for_close` (Impact: 694.1)
    * *Intent:* """Wait for all waiters to finish closing."""
  * `_check_loop_for_start_tls` (Impact: 24.2)
  * `_get_ssl_context` (Impact: 13.2)
    * *Intent:* # In this case we need to create a task to ensure that we can shield # the task from cancellation as...
  * `_close` (Impact: 6.7)
  * `close` (Impact: 6.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 293`, `structural_boundaries: 312`, `args: 79`, `func_start: 79`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 211`, `dead_code: 2`, `planned_debt: 1`, `duplicate_logic: 8`
* *Architecture:* `io: 29`, `api: 35`, `concurrency: 199`, `import: 30`
* *Defense:* `safety: 75`, `doc: 86`, `test: 8`, `immutability_locks: 6`, `cleanup: 24`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.041
  * `Choke Point (Betweenness):` 0.007715 | `Ripple Effect (Closeness):` 0.163496
  * `Imports (Out-Degree: 8):` .helpers, time, .resolver, ssl, traceback, http, .abc, collections.abc...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `aiohttp-3.13.5/tests/test_client_ws_functional.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.524 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.951 IQR)
- **Top Global Matches:** file_cluster_4: 11.524, file_cluster_8: 12.165, file_cluster_13: 12.324
- **Magnitude:** 1214.98 | **LOC:** 1279 | **CtrlFlow:** 8.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (42.7215%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_closed_async_for` (Impact: 11.7)
  * `test_receive_timeout_deprecation` (Impact: 9.2)
  * `test_ws_client_async_for` (Impact: 9.2)
  * `test_ping_pong` (Impact: 8.4)
  * `test_ping_pong_manual` (Impact: 8.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 689`, `args: 94`, `func_start: 93`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 26`, `dead_code: 1`, `duplicate_logic: 45`, `orphaned_logic: 46`
* *Architecture:* `io: 47`, `api: 94`, `concurrency: 697`, `import: 13`
* *Defense:* `safety: 126`, `doc: 16`, `test: 182`, `cleanup: 65`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.849
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` pytest, unittest, aiohttp.client_ws, asyncio, aiohttp, typing, aiohttp.pytest_plugin, sys...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/tests/test_web_websocket_functional.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.525 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.686 IQR)
- **Top Global Matches:** file_cluster_4: 11.525, file_cluster_8: 12.041, file_cluster_16: 12.244
- **Magnitude:** 1123.84 | **LOC:** 1397 | **CtrlFlow:** 4.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (39.7144%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_websocket_json` (Impact: 18.9)
  * `test_websocket_shutdown` (Impact: 14.0)
  * `test_server_ws_async_for` (Impact: 10.2)
  * `handler` (Impact: 10.0)
  * `websocket_handler` (Impact: 9.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 742`, `args: 92`, `func_start: 92`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 21`, `duplicate_logic: 37`, `orphaned_logic: 39`
* *Architecture:* `io: 30`, `api: 92`, `concurrency: 705`, `import: 11`
* *Defense:* `safety: 160`, `doc: 24`, `test: 195`, `sync_locks: 4`, `cleanup: 65`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.849
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` weakref, pytest, unittest, asyncio, aiohttp, typing, aiohttp.pytest_plugin, sys...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/tests/test_multipart.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.269 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.829 IQR)
- **Top Global Matches:** file_cluster_4: 12.269, file_cluster_8: 12.605, file_cluster_16: 12.707
- **Magnitude:** 1119.5 | **LOC:** 1864 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (45.0839%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_read_json` (Impact: 57.0)
  * `test_release_next` (Impact: 53.5)
  * `test_read_with_content_transfer_encoding` (Impact: 29.7)
  * `test_read_boundary_across_chunks` (Impact: 24.8)
  * `test_default_headers` (Impact: 23.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 139`, `structural_boundaries: 601`, `args: 145`, `func_start: 145`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 101`, `fragile_debt: 10`, `duplicate_logic: 19`, `orphaned_logic: 30`
* *Architecture:* `io: 131`, `api: 148`, `concurrency: 429`, `import: 17`
* *Defense:* `safety: 210`, `doc: 8`, `test: 373`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.849
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` io, pytest, unittest, pathlib, multidict, aiohttp.multipart, asyncio, aiohttp...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/tests/test_client_request.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.831 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.57 IQR)
- **Top Global Matches:** file_cluster_4: 12.831, file_cluster_16: 12.864, file_cluster_0: 13.02
- **Magnitude:** 1002.2 | **LOC:** 2283 | **CtrlFlow:** 10.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (22.6716%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_urlencoded_formdata_charset` (Impact: 182.3)
  * `test_query_bytes_param_raises` (Impact: 5.4)
  * `test_method_invalid` (Impact: 5.3)
  * `transport` (Impact: 4.8)
  * `test_cookie_coded_value_preserved` (Impact: 4.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 703`, `args: 202`, `func_start: 202`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 30`, `orphaned_logic: 78`
* *Architecture:* `io: 46`, `api: 200`, `concurrency: 354`, `import: 21`
* *Defense:* `safety: 296`, `doc: 84`, `test: 538`, `immutability_locks: 1`, `cleanup: 102`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.849
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` http.cookies, collections.abc, warnings, hashlib, typing, urllib.parse, aiohttp.client_reqrep, asyncio...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/tests/test_run_app.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.294 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.166 IQR)
- **Top Global Matches:** file_cluster_4: 11.294, file_cluster_8: 11.796, file_cluster_13: 11.939
- **Magnitude:** 986.68 | **LOC:** 1316 | **CtrlFlow:** 19.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.1032%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test` (Impact: 19.0)
  * `test_shutdown_close_websockets` (Impact: 16.6)
    * *Intent:* # If not, then shutdown_timeout will allow it to sleep until complete. assert t.cancelled() def test...
  * `test` (Impact: 10.9)
  * `test` (Impact: 10.6)
  * `test` (Impact: 9.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 250`, `args: 83`, `func_start: 81`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 72`, `duplicate_logic: 28`, `orphaned_logic: 36`
* *Architecture:* `io: 58`, `api: 82`, `concurrency: 514`, `import: 18`
* *Defense:* `safety: 66`, `doc: 2`, `test: 121`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.849
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` os, pytest, time, unittest, aiohttp.web_runner, socket, logging, asyncio...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/tests/test_streams.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.238 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.195 IQR)
- **Top Global Matches:** file_cluster_4: 12.238, file_cluster_8: 12.336, file_cluster_16: 12.444
- **Magnitude:** 978.38 | **LOC:** 1726 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (44.6594%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_unread_data` (Impact: 92.0)
  * `test_read_eof_unread_data_no_warning` (Impact: 35.5)
    * *Intent:* # Read bytes. stream = self._make_one() stream.feed_eof() with mock.patch("aiohttp.streams.internal_...
  * `get_memory_usage` (Impact: 11.5)
  * `test_stream_reader_iter_chunks_chunked_e` (Impact: 6.7)
  * `test_ctor_global_loop` (Impact: 5.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 574`, `args: 137`, `func_start: 137`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 11`, `duplicate_logic: 13`, `orphaned_logic: 56`
* *Architecture:* `io: 4`, `api: 138`, `concurrency: 435`, `import: 11`
* *Defense:* `safety: 248`, `doc: 12`, `test: 430`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.849
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` pytest, unittest, aiohttp.http_exceptions, itertools, abc, asyncio, gc, collections...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/aiohttp/client_reqrep.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.997 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.301 IQR)
- **Top Global Matches:** file_cluster_4: 12.997, file_cluster_13: 13.06, file_cluster_16: 13.089
- **Magnitude:** 955.58 | **LOC:** 1537 | **CtrlFlow:** 52.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (59.876%), Tech Debt (9.3782%)
**Top Internal Functions/Classes:**
  * `links` (Impact: 270.1)
  * `send` (Impact: 51.7)
  * `update_body_from_data` (Impact: 36.0)
  * `close` (Impact: 12.6)
    * *Intent:* # Specify request target: # - CONNECT request must send authority form URI # - not CONNECT proxy mus...
  * `_update_body` (Impact: 11.3)
    * *Intent:* # enable chunked encoding if needed if not self.chunked and hdrs.CONTENT_LENGTH not in self.headers:...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 276`, `structural_boundaries: 255`, `args: 81`, `func_start: 79`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 249`, `dead_code: 5`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `io: 6`, `api: 63`, `concurrency: 173`, `import: 34`
* *Defense:* `safety: 46`, `doc: 50`, `test: 13`, `immutability_locks: 1`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 17.763
  * `Choke Point (Betweenness):` 0.025696 | `Ripple Effect (Closeness):` 0.218347
  * `Imports (Out-Degree: 11):` http.cookies, .helpers, .streams, ssl, traceback, .abc, collections.abc, .http...
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

### `aiohttp-3.13.5/aiohttp/multipart.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.408 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.633 IQR)
- **Top Global Matches:** file_cluster_4: 12.408, file_cluster_16: 12.516, file_cluster_13: 12.625
- **Magnitude:** 927.26 | **LOC:** 1214 | **CtrlFlow:** 41.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.841%), Tech Debt (94.1161%)
**Top Internal Functions/Classes:**
  * `append` (Impact: 87.7)
    * *Intent:* # Refer to RFCs 7231, 7230, 5234. # # parameter = token "=" ( token / quoted-string ) # token = 1*tc...
  * `form` (Impact: 67.2)
  * `read_chunk` (Impact: 28.0)
  * `_read_chunk_from_stream` (Impact: 26.4)
    * *Intent:* # Reads body part content chunk of the specified size.
  * `readline` (Impact: 19.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 213`, `structural_boundaries: 307`, `args: 79`, `func_start: 79`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 177`, `duplicate_logic: 18`
* *Architecture:* `io: 1`, `api: 58`, `concurrency: 260`, `import: 25`
* *Defense:* `safety: 23`, `doc: 80`, `test: 9`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.223
  * `Choke Point (Betweenness):` 0.009907 | `Ripple Effect (Closeness):` 0.169219
  * `Imports (Out-Degree: 10):` .helpers, .streams, .abc, collections.abc, uuid, .http, warnings, .client_reqrep...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `aiohttp-3.13.5/tests/test_client_session.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.508 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.608 IQR)
- **Top Global Matches:** file_cluster_4: 12.508, file_cluster_0: 12.704, file_cluster_13: 12.775
- **Magnitude:** 857.1 | **LOC:** 1414 | **CtrlFlow:** 16.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (37.1579%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `handler` (Impact: 88.0)
  * `test_cookie_jar_usage` (Impact: 81.8)
  * `test_ssl_shutdown_timeout_passed_to_conn` (Impact: 27.9)
  * `test_ssl_shutdown_timeout_passed_to_conn` (Impact: 23.9)
    * *Intent:* # Test custom value - expect both deprecation and runtime warnings with warnings.catch_warnings(reco...
  * `test_close_conn_on_error` (Impact: 9.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 93`, `structural_boundaries: 461`, `args: 116`, `func_start: 107`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 39`, `state_mutation: 40`, `dead_code: 5`, `duplicate_logic: 11`, `orphaned_logic: 50`
* *Architecture:* `io: 45`, `api: 107`, `concurrency: 242`, `import: 27`
* *Defense:* `safety: 168`, `doc: 18`, `test: 321`, `cleanup: 32`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.849
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` http.cookies, aiohttp.client, uuid, aiohttp.helpers, warnings, re_assert, gc, collections...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/tests/test_client_middleware.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.423 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.28 IQR)
- **Top Global Matches:** file_cluster_4: 12.423, file_cluster_16: 12.723, file_cluster_8: 12.849
- **Magnitude:** 834.82 | **LOC:** 1272 | **CtrlFlow:** 19.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (24.9155%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_client_middleware_multi_step_auth` (Impact: 44.4)
  * `test_client_middleware_challenge_auth` (Impact: 34.7)
  * `test_client_middleware_stateful_retry` (Impact: 18.1)
  * `handler` (Impact: 16.9)
  * `test_client_middleware_retry` (Impact: 15.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 119`, `structural_boundaries: 483`, `args: 87`, `func_start: 87`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 45`, `duplicate_logic: 56`, `orphaned_logic: 19`
* *Architecture:* `io: 10`, `api: 84`, `concurrency: 355`, `import: 11`
* *Defense:* `safety: 121`, `doc: 82`, `test: 153`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.849
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` pytest, socket, aiohttp.resolver, aiohttp, typing, aiohttp.pytest_plugin, aiohttp.tracing, aiohttp.abc...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/aiohttp/streams.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.776 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 7.071 IQR)
- **Top Global Matches:** file_cluster_4: 12.776, file_cluster_16: 12.964, file_cluster_13: 13.155
- **Magnitude:** 714.22 | **LOC:** 763 | **CtrlFlow:** 43.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (61.8946%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `_wait` (Impact: 121.0)
    * *Intent:* # wake up readchunk when end of http chunk received waiter = self._waiter if waiter is not None: sel...
  * `__repr__` (Impact: 47.4)
  * `read` (Impact: 16.9)
  * `end_http_chunk_receiving` (Impact: 15.8)
  * `read` (Impact: 12.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 124`, `structural_boundaries: 159`, `args: 65`, `func_start: 64`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 172`, `dead_code: 2`, `planned_debt: 4`, `duplicate_logic: 28`
* *Architecture:* `api: 60`, `concurrency: 155`, `import: 8`
* *Defense:* `safety: 21`, `doc: 24`, `test: 4`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 17.832
  * `Choke Point (Betweenness):` 0.003905 | `Ripple Effect (Closeness):` 0.258349
  * `Imports (Out-Degree: 3):` .helpers, .http_exceptions, asyncio, collections, typing, .base_protocol, .log, warnings
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `aiohttp-3.13.5/tests/test_http_writer.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.093 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.856 IQR)
- **Top Global Matches:** file_cluster_4: 12.093, file_cluster_0: 12.366, file_cluster_8: 12.494
- **Magnitude:** 700.88 | **LOC:** 1654 | **CtrlFlow:** 13.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (31.3927%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_serialize_headers_raises_on_new_lin` (Impact: 6.8)
  * `test_write_to_closed_transport` (Impact: 6.6)
    * *Intent:* """Test that writing to a closed transport raises ClientConnectionResetError. The StreamWriter check...
  * `test_write_headers_prevents_injection` (Impact: 6.5)
  * `test_serialize_headers_raises_on_null_by` (Impact: 5.8)
  * `decode_chunked` (Impact: 4.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 424`, `args: 82`, `func_start: 82`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 50`, `duplicate_logic: 18`, `orphaned_logic: 54`
* *Architecture:* `io: 7`, `api: 82`, `concurrency: 385`, `import: 11`
* *Defense:* `safety: 172`, `doc: 48`, `test: 320`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.849
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` aiohttp.compression_utils, pytest, unittest, aiohttp.base_protocol, zlib, multidict, asyncio, aiohttp...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/tests/test_http_parser.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.645 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.174 IQR)
- **Top Global Matches:** file_cluster_8: 12.645, file_cluster_0: 12.647, file_cluster_16: 12.683
- **Magnitude:** 674.96 | **LOC:** 2232 | **CtrlFlow:** 19.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.8917%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_parse_uri_utf8_percent_encoded` (Impact: 35.1)
  * `test_parse_chunked_payload_chunk_extensi` (Impact: 33.9)
  * `test_max_trailer_size` (Impact: 13.2)
  * `test_max_header_field_size` (Impact: 10.8)
  * `test_max_header_value_size` (Impact: 10.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 154`, `structural_boundaries: 636`, `args: 175`, `func_start: 175`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 48`, `state_mutation: 6`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 2`, `orphaned_logic: 67`
* *Architecture:* `io: 43`, `api: 176`, `concurrency: 86`, `import: 20`
* *Defense:* `safety: 412`, `doc: 36`, `test: 694`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.849
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` yarl, pytest, unittest, aiohttp.base_protocol, aiohttp.http_parser, zlib, multidict, brotlicffi...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/examples/logging_middleware.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_4` (Drift: 10.573 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 6.822 IQR)
- **Top Global Matches:** file_cluster_4: 10.573, file_cluster_13: 10.818, file_cluster_16: 10.879
- **Magnitude:** 661.08 | **LOC:** 170 | **CtrlFlow:** 27.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.4507%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 46`, `args: 8`, `func_start: 8`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 3`, `planned_debt: 1`
* *Architecture:* `io: 2`, `api: 9`, `concurrency: 55`, `import: 6`
* *Defense:* `safety: 4`, `doc: 18`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.849
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` time, logging, asyncio, aiohttp, typing, json
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/tests/test_urldispatch.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.366 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.844 IQR)
- **Top Global Matches:** file_cluster_16: 12.366, file_cluster_8: 12.367, file_cluster_4: 12.56
- **Magnitude:** 615.12 | **LOC:** 1386 | **CtrlFlow:** 10.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.963%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_add_url_invalid4` (Impact: 52.6)
  * `test_set_options_route` (Impact: 11.1)
  * `test_match_domain` (Impact: 6.3)
  * `test_add_route_invalid_method` (Impact: 5.9)
  * `test_dynamic_match_unquoted_path` (Impact: 5.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 462`, `args: 153`, `func_start: 153`
* *Risk/State:* `safety_bypasses: 8`, `fragile_debt: 2`, `duplicate_logic: 6`, `orphaned_logic: 84`
* *Architecture:* `io: 61`, `api: 153`, `concurrency: 117`, `import: 14`
* *Defense:* `safety: 224`, `doc: 12`, `test: 390`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.849
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` yarl, pytest, pathlib, re, re_assert, aiohttp, aiohttp.web, aiohttp.web_urldispatcher...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohttp-3.13.5/tests/test_web_response.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.651 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.767 IQR)
- **Top Global Matches:** file_cluster_16: 12.651, file_cluster_4: 12.687, file_cluster_0: 12.715
- **Magnitude:** 583.42 | **LOC:** 1608 | **CtrlFlow:** 9.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (22.7226%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_setting_charset` (Impact: 81.7)
  * `test_cookie_set_after_del` (Impact: 22.4)
  * `test_response_with_immutable_headers` (Impact: 16.3)
  * `test_assign_nonbyteish_body` (Impact: 4.7)
  * `test_ctor_charset_in_content_type` (Impact: 4.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 551`, `args: 163`, `func_start: 163`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 16`, `duplicate_logic: 2`, `orphaned_logic: 28`
* *Architecture:* `io: 10`, `api: 163`, `concurrency: 173`, `import: 21`
* *Defense:* `safety: 256`, `doc: 18`, `test: 488`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.849
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` aiohttp.web, aiosignal, datetime, collections.abc, aiohttp.helpers, concurrent.futures, aiohttp.multipart, gzip...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `aiohttp-3.13.5/tests/test_tcp_helpers.py` (PYTHON) | Magnitude: 24.74 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 38, io: 33, test: 24, structural_boundaries: 22
- `aiohttp-3.13.5/tests/autobahn/test_autobahn.py` (PYTHON) | Magnitude: 65.86 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 98, branch: 24, structural_boundaries: 21, test: 16
- `aiohttp-3.13.5/tests/test_resolver.py` (PYTHON) | Magnitude: 262.56 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 374, structural_boundaries: 186, test: 166, concurrency: 114
- `aiohttp-3.13.5/tests/test_client_connection.py` (PYTHON) | Magnitude: 68.2 | Delta: **0.103 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 79, structural_boundaries: 50, test: 44, safety: 19
- `aiohttp-3.13.5/tests/test_route_def.py` (PYTHON) | Magnitude: 162.2 | Delta: **0.227 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 181, structural_boundaries: 143, test: 98, safety: 72

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `aiohttp-3.13.5/aiohttp/_websocket/reader_c.py` (PYTHON) | Magnitude: 309.42 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 332, encapsulation: 152, state_mutation: 134, branch: 92
- `aiohttp-3.13.5/aiohttp/_websocket/reader_py.py` (PYTHON) | Magnitude: 309.42 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 332, encapsulation: 152, state_mutation: 134, branch: 92
- `aiohttp-3.13.5/aiohttp/client_middleware_digest_auth.py` (PYTHON) | Magnitude: 76.34 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 234, branch: 56, structural_boundaries: 56, state_mutation: 41
- `aiohttp-3.13.5/tests/test_benchmarks_client_request.py` (PYTHON) | Magnitude: 77.9 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 116, structural_boundaries: 51, concurrency: 22, generics: 20
- `aiohttp-3.13.5/aiohttp/helpers.py` (PYTHON) | Magnitude: 517.12 | Delta: **0.057 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 539, structural_boundaries: 221, encapsulation: 175, branch: 148

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `aiohttp-3.13.5/tests/test_urldispatch.py` (PYTHON) | Magnitude: 615.12 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 851, structural_boundaries: 462, test: 390, safety: 224
- `aiohttp-3.13.5/tests/test_websocket_parser.py` (PYTHON) | Magnitude: 203.64 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 394, structural_boundaries: 190, test: 165, encapsulation: 96
- `aiohttp-3.13.5/aiohttp/client_proto.py` (PYTHON) | Magnitude: 269.12 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 254, encapsulation: 108, state_mutation: 77, structural_boundaries: 55
- `aiohttp-3.13.5/aiohttp/web_app.py` (PYTHON) | Magnitude: 289.34 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 447, encapsulation: 211, structural_boundaries: 154, generics: 84
- `aiohttp-3.13.5/aiohttp/_websocket/models.py` (PYTHON) | Magnitude: 15.12 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 40, structural_boundaries: 16, doc: 8, safety_bypasses: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `aiohttp-3.13.5/tests/test_payload.py` (PYTHON) | Magnitude: 509.08 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 707, structural_boundaries: 448, test: 256, concurrency: 203
- `aiohttp-3.13.5/aiohttp/connector.py` (PYTHON) | Magnitude: 1263.48 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 1235, encapsulation: 409, structural_boundaries: 312, branch: 293
- `aiohttp-3.13.5/aiohttp/web_ws.py` (PYTHON) | Magnitude: 407.06 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 471, encapsulation: 209, structural_boundaries: 175, concurrency: 106
- `aiohttp-3.13.5/tests/test_classbasedview.py` (PYTHON) | Magnitude: 39.88 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 31, indent_spaces: 31, test: 18, api: 10
- `aiohttp-3.13.5/aiohttp/_websocket/writer.py` (PYTHON) | Magnitude: 114.88 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 139, concurrency: 42, encapsulation: 34, branch: 31

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `aiohttp-3.13.5/tests/test_helpers.py` (PYTHON) | Magnitude: 428.94 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 598, test: 265, structural_boundaries: 254, safety: 116
- `aiohttp-3.13.5/tests/test_http_parser.py` (PYTHON) | Magnitude: 674.96 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 1459, test: 694, structural_boundaries: 636, safety: 412
- `aiohttp-3.13.5/aiohttp/typedefs.py` (PYTHON) | Magnitude: 4.24 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 31, structural_boundaries: 15, generics: 14, encapsulation: 13
- `aiohttp-3.13.5/tests/test_multipart_helpers.py` (PYTHON) | Magnitude: 246.98 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 584, test: 340, structural_boundaries: 304, safety: 195
- `aiohttp-3.13.5/tests/test_web_websocket.py` (PYTHON) | Magnitude: 440.52 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 394, structural_boundaries: 256, test: 166, concurrency: 152

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

- `aiohttp-3.13.5/aiohttp/typedefs.py` -> **Severity: 22.331** (Embedded: 0.2969 * Error Risk: 75.2202%)
- `aiohttp-3.13.5/aiohttp/streams.py` -> **Severity: 20.081** (Embedded: 0.2583 * Error Risk: 77.7275%)
- `aiohttp-3.13.5/aiohttp/base_protocol.py` -> **Severity: 17.552** (Embedded: 0.2302 * Error Risk: 76.2354%)
- `aiohttp-3.13.5/aiohttp/http_exceptions.py` -> **Severity: 17.048** (Embedded: 0.2241 * Error Risk: 76.0648%)
- `aiohttp-3.13.5/aiohttp/web_routedef.py` -> **Severity: 16.61** (Embedded: 0.1834 * Error Risk: 90.55%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `aiohttp-3.13.5/aiohttp/abc.py` -> **Severity: 6468.075** (Blast Radius: 66.029 * Doc Risk: 97.9581%)
- `aiohttp-3.13.5/aiohttp/typedefs.py` -> **Severity: 2313.936** (Blast Radius: 59.124 * Doc Risk: 39.137%)
- `aiohttp-3.13.5/aiohttp/web_response.py` -> **Severity: 2240.3** (Blast Radius: 27.579 * Doc Risk: 81.2321%)
- `aiohttp-3.13.5/aiohttp/base_protocol.py` -> **Severity: 1992.317** (Blast Radius: 20.092 * Doc Risk: 99.1597%)
- `aiohttp-3.13.5/aiohttp/web_exceptions.py` -> **Severity: 1771.203** (Blast Radius: 17.77 * Doc Risk: 99.6738%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
