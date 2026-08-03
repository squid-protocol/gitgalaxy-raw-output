# ARCHITECTURAL_BRIEF: urllib3
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/urllib3` |
| **Timestamp** | `2026-08-03T21:26:05.308966+00:00` |
| **Scan Duration** | `0.34s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 42 malicious artifacts.

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
| Total Artifacts | 52 |
| Analyzed Artifacts (Scanned) | 44 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 8 |
| Total LOC | 8077 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 84.6% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2809 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2649 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 27.3% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.3604 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 3 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 41 | 7985 | 93.2% |
| PLAINTEXT | 1 | 0 | 2.3% |
| MARKDOWN | 1 | 0 | 2.3% |
| JAVASCRIPT | 1 | 92 | 2.3% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.594`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 26 | 59.1% |
| file_cluster_8 | 7 | 15.9% |
| file_cluster_16 | 6 | 13.6% |
| file_cluster_4 | 3 | 6.8% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 4.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 8*

**Composition by Extension & Reason:**
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.rst`: 2x Excluded (Unsupported Extension: '.rst')
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')
- `.py`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.lock`: 1x Excluded (Unsupported Extension: '.lock')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 3.3 | 100.0 | 25.1 | 14.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 71.7 | 18.0 | 6.4 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 33.8 | 0.0 | 0.0 |
| Testing Exposure | 0.2 | 80.0 | 35.5 | 2.5 | 80.0 |
| API Exposure | 0.0 | 8.9 | 3.0 | 2.6 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 14.8 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 50.8 | 53.6 | 0.0 |
| Commented Logic Exposure | 0.0 | 45.6 | 4.1 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 94.8 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 6.7 | 100.0 | 66.2 | 80.7 | 11.9 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 54.1 | 62.2 | 100.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 56.3 | 96.4 | 100.0 |
| Weaponizable Injection Vectors | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `urllib3-2.6.3/dummyserver/socketserver.py` (Hits: 27)
- `urllib3-2.6.3/src/urllib3/connection.py` (Hits: 27)
- `urllib3-2.6.3/dummyserver/hypercornserver.py` (Hits: 20)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **exceptions.py** (`urllib3-2.6.3/src/urllib3/exceptions.py`) — 16 inbound connections
2. **_base_connection.py** (`urllib3-2.6.3/src/urllib3/_base_connection.py`) — 10 inbound connections
3. **url.py** (`urllib3-2.6.3/src/urllib3/util/url.py`) — 10 inbound connections
4. **connectionpool.py** (`urllib3-2.6.3/src/urllib3/connectionpool.py`) — 8 inbound connections
5. **_collections.py** (`urllib3-2.6.3/src/urllib3/_collections.py`) — 7 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **connection.py** (`urllib3-2.6.3/src/urllib3/connection.py`) — 29 outbound dependencies
2. **connectionpool.py** (`urllib3-2.6.3/src/urllib3/connectionpool.py`) — 26 outbound dependencies
3. **response.py** (`urllib3-2.6.3/src/urllib3/response.py`) — 25 outbound dependencies
4. **poolmanager.py** (`urllib3-2.6.3/src/urllib3/poolmanager.py`) — 21 outbound dependencies
5. **__init__.py** (`urllib3-2.6.3/src/urllib3/__init__.py`) — 18 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `_new_conn` (@ `urllib3-2.6.3/src/urllib3/connectionpool.py`) -> Impact: **1088.9** | LOC: 682
- `get_subj_alt_name` (@ `urllib3-2.6.3/src/urllib3/contrib/pyopenssl.py`) -> Impact: **640.3** | LOC: 326
  * *Intent:* # pyOpenSSL 0.14 and above use cryptography for OpenSSL bindings. The _x509
- `_update_chunk_length` (@ `urllib3-2.6.3/src/urllib3/response.py`) -> Impact: **455.6** | LOC: 139
- `connect` (@ `urllib3-2.6.3/src/urllib3/connection.py`) -> Impact: **249.3** | LOC: 136
- `_tunnel` (@ `urllib3-2.6.3/src/urllib3/connection.py`) -> Impact: **209.9** | LOC: 76
- `_init_length` (@ `urllib3-2.6.3/src/urllib3/contrib/emscripten/response.py`) -> Impact: **193.3** | LOC: 108
- `send_request` (@ `urllib3-2.6.3/src/urllib3/contrib/emscripten/fetch.py`) -> Impact: **173.4** | LOC: 168
- `decompress` (@ `urllib3-2.6.3/src/urllib3/response.py`) -> Impact: **158.4** | LOC: 49
- `decompress` (@ `urllib3-2.6.3/src/urllib3/response.py`) -> Impact: **157.7** | LOC: 33
- `extend` (@ `urllib3-2.6.3/src/urllib3/_collections.py`) -> Impact: **141.5** | LOC: 30

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `connect` (@ `urllib3-2.6.3/src/urllib3/connection.py`) -> **O(2^N) [Recursive]**
- `_tunnel` (@ `urllib3-2.6.3/src/urllib3/connection.py`) -> **O(2^N) [Recursive]**
- `_new_conn` (@ `urllib3-2.6.3/src/urllib3/connectionpool.py`) -> **O(2^N) [Recursive]**
- `_update_chunk_length` (@ `urllib3-2.6.3/src/urllib3/response.py`) -> **O(2^N) [Recursive]**
- `readinto` (@ `urllib3-2.6.3/src/urllib3/contrib/emscripten/fetch.py`) -> **O(2^N) [Recursive]**
- `get_subj_alt_name` (@ `urllib3-2.6.3/src/urllib3/contrib/pyopenssl.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # pyOpenSSL 0.14 and above use cryptography for OpenSSL bindings. The _x509
- `close` (@ `urllib3-2.6.3/src/urllib3/http2/connection.py`) -> **O(2^N) [Recursive]**
- `decompress` (@ `urllib3-2.6.3/src/urllib3/response.py`) -> **O(2^N) [Recursive]**
- `decompress` (@ `urllib3-2.6.3/src/urllib3/response.py`) -> **O(2^N) [Recursive]**
- `decompress` (@ `urllib3-2.6.3/src/urllib3/response.py`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `get_subj_alt_name` (@ `urllib3-2.6.3/src/urllib3/contrib/pyopenssl.py`) -> DB Complexity: **48**
  * *Intent:* # pyOpenSSL 0.14 and above use cryptography for OpenSSL bindings. The _x509
- `_create_urllib3_sockets` (@ `urllib3-2.6.3/dummyserver/hypercornserver.py`) -> DB Complexity: **43**
- `_start_server` (@ `urllib3-2.6.3/dummyserver/socketserver.py`) -> DB Complexity: **28**
- `connect` (@ `urllib3-2.6.3/src/urllib3/connection.py`) -> DB Complexity: **23**
- `_new_conn` (@ `urllib3-2.6.3/src/urllib3/connectionpool.py`) -> DB Complexity: **16**
- `_retry_create_urllib3_sockets` (@ `urllib3-2.6.3/dummyserver/hypercornserver.py`) -> DB Complexity: **12**
  * *Intent:* # When we request a socket with host localhost and port zero, Hypercorn # only binds to IPv4. But we want to bind to IPv6 too, otherwise we # waste ab...
- `_resolves_to_ipv6` (@ `urllib3-2.6.3/dummyserver/socketserver.py`) -> DB Complexity: **12**
- `_has_ipv6` (@ `urllib3-2.6.3/dummyserver/socketserver.py`) -> DB Complexity: **12**
  * *Intent:* """Returns True if the system can bind an IPv6 address."""
- `_new_conn` (@ `urllib3-2.6.3/src/urllib3/connection.py`) -> DB Complexity: **12**
- `_has_ipv6` (@ `urllib3-2.6.3/src/urllib3/util/connection.py`) -> DB Complexity: **12**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `urllib3-2.6.3/src/urllib3` | 12 | 5084.6 | 16.98% | 42.25% |
| `urllib3-2.6.3/src/urllib3/util` | 12 | 753.7 | 15.41% | 29.13% |
| `urllib3-2.6.3/dummyserver` | 6 | 709.06 | 40.66% | 19.39% |
| `urllib3-2.6.3/src/urllib3/http2` | 3 | 248.54 | 34.35% | 65.6% |
| `urllib3-2.6.3/src/urllib3/contrib/emscripten` | 6 | 12.77 | 46.54% | 41.44% |
| `urllib3-2.6.3/src/urllib3/contrib` | 3 | 12.4 | 12.79% | 0.0% |
| `urllib3-2.6.3` | 2 | 3.46 | 0.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `urllib3-2.6.3/src/urllib3/exceptions.py` -> **100.0%** Exposure
- `urllib3-2.6.3/src/urllib3/response.py` -> **99.9999%** Exposure
- `urllib3-2.6.3/src/urllib3/_collections.py` -> **99.9998%** Exposure
- `urllib3-2.6.3/src/urllib3/contrib/emscripten/fetch.py` -> **99.9642%** Exposure
- `urllib3-2.6.3/src/urllib3/util/ssltransport.py` -> **99.7646%** Exposure
### Highest State Flux (Mutation/Volatility)
- `urllib3-2.6.3/src/urllib3/util/retry.py` -> **100.0%** Exposure
- `urllib3-2.6.3/src/urllib3/util/ssl_match_hostname.py` -> **100.0%** Exposure
- `urllib3-2.6.3/src/urllib3/util/wait.py` -> **100.0%** Exposure
- `urllib3-2.6.3/src/urllib3/contrib/emscripten/emscripten_fetch_worker.js` -> **100.0%** Exposure
- `urllib3-2.6.3/src/urllib3/contrib/emscripten/connection.py` -> **99.9988%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `urllib3-2.6.3/src/urllib3/response.py` -> **0** Orphaned Functions | **40** Duplicates
- `urllib3-2.6.3/src/urllib3/contrib/emscripten/fetch.py` -> **0** Orphaned Functions | **20** Duplicates
- `urllib3-2.6.3/src/urllib3/_collections.py` -> **0** Orphaned Functions | **17** Duplicates
- `urllib3-2.6.3/src/urllib3/exceptions.py` -> **0** Orphaned Functions | **17** Duplicates
- `urllib3-2.6.3/dummyserver/testcase.py` -> **4** Orphaned Functions | **7** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`urllib3-2.6.3/src/urllib3/connection.py`** -> AI Confidence: **99.31%**
2. **`urllib3-2.6.3/src/urllib3/http2/connection.py`** -> AI Confidence: **99.31%**
3. **`urllib3-2.6.3/src/urllib3/response.py`** -> AI Confidence: **99.31%**
4. **`urllib3-2.6.3/src/urllib3/util/request.py`** -> AI Confidence: **99.31%**
5. **`urllib3-2.6.3/src/urllib3/util/retry.py`** -> AI Confidence: **99.31%**
6. **`urllib3-2.6.3/src/urllib3/util/ssl_.py`** -> AI Confidence: **99.31%**
7. **`urllib3-2.6.3/src/urllib3/util/url.py`** -> AI Confidence: **99.31%**
8. **`urllib3-2.6.3/src/urllib3/_collections.py`** -> AI Confidence: **99.24%**
9. **`urllib3-2.6.3/src/urllib3/connectionpool.py`** -> AI Confidence: **99.24%**
10. **`urllib3-2.6.3/src/urllib3/contrib/emscripten/fetch.py`** -> AI Confidence: **99.24%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `urllib3-2.6.3/dummyserver/asgi_proxy.py` -> **100.0%** Exposure
- `urllib3-2.6.3/dummyserver/hypercornserver.py` -> **100.0%** Exposure
- `urllib3-2.6.3/dummyserver/socketserver.py` -> **100.0%** Exposure
- `urllib3-2.6.3/dummyserver/testcase.py` -> **100.0%** Exposure
- `urllib3-2.6.3/src/urllib3/_base_connection.py` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `urllib3-2.6.3/dummyserver/hypercornserver.py` -> **100.0%** Exposure
- `urllib3-2.6.3/dummyserver/socketserver.py` -> **100.0%** Exposure
- `urllib3-2.6.3/dummyserver/testcase.py` -> **100.0%** Exposure
- `urllib3-2.6.3/src/urllib3/_collections.py` -> **100.0%** Exposure
- `urllib3-2.6.3/src/urllib3/connection.py` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `6` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `280` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `urllib3-2.6.3/dummyserver/testcase.py` (PYTHON) -> Cumulative Risk: **866.08**
- **Archetype:** `file_cluster_13` (Distance: 10.562 IQR)
- **Magnitude:** 236.78 | **LOC:** 354 | **CtrlFlow:** 31.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (99.9218%)
- **Heaviest Functions:** `socket_handler` (Impact: 64.2), `consume_request` (Impact: 20.6), `quit_server_thread` (Impact: 12.4)

### 2. `urllib3-2.6.3/src/urllib3/http2/connection.py` (PYTHON) -> Cumulative Risk: **849.17**
- **Archetype:** `file_cluster_13` (Distance: 11.971 IQR)
- **Magnitude:** 150.82 | **LOC:** 357 | **CtrlFlow:** 50.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.9481%)
- **Heaviest Functions:** `close` (Impact: 42.3), `data` (Impact: 2.7), `get_redirect_location` (Impact: 2.7)

### 3. `urllib3-2.6.3/dummyserver/asgi_proxy.py` (PYTHON) -> Cumulative Risk: **837.55**
- **Archetype:** `file_cluster_4` (Distance: 10.51 IQR)
- **Magnitude:** 120.2 | **LOC:** 115 | **CtrlFlow:** 27.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), Algorithmic Dos (99.9928%)
- **Heaviest Functions:** `connect` (Impact: 37.2), `_read_body` (Impact: 18.4), `__init__` (Impact: 7.2)

### 4. `urllib3-2.6.3/src/urllib3/http2/probe.py` (PYTHON) -> Cumulative Risk: **817.62**
- **Archetype:** `file_cluster_16` (Distance: 11.358 IQR)
- **Magnitude:** 79.0 | **LOC:** 88 | **CtrlFlow:** 44.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (99.9982%), State Flux (91.5805%)
- **Heaviest Functions:** `acquire_and_get` (Impact: 31.6), `_values` (Impact: 10.6), `_reset` (Impact: 7.2)

### 5. `urllib3-2.6.3/src/urllib3/contrib/emscripten/fetch.py` (PYTHON) -> Cumulative Risk: **816.1**
- **Archetype:** `file_cluster_13` (Distance: 12.292 IQR)
- **Magnitude:** 6.72 | **LOC:** 727 | **CtrlFlow:** 42.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Tech Debt (99.9642%)
- **Heaviest Functions:** `send_request` (Impact: 173.4), `readinto` (Impact: 85.4), `send` (Impact: 50.3)

### 6. `urllib3-2.6.3/src/urllib3/contrib/emscripten/response.py` (PYTHON) -> Cumulative Risk: **799.64**
- **Archetype:** `file_cluster_13` (Distance: 12.28 IQR)
- **Magnitude:** 3.56 | **LOC:** 278 | **CtrlFlow:** 43.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.6731%)
- **Heaviest Functions:** `_init_length` (Impact: 193.3), `_error_catcher` (Impact: 48.6), `close` (Impact: 35.0)

### 7. `urllib3-2.6.3/src/urllib3/response.py` (PYTHON) -> Cumulative Risk: **789.7**
- **Archetype:** `file_cluster_13` (Distance: 12.455 IQR)
- **Magnitude:** 1904.14 | **LOC:** 1481 | **CtrlFlow:** 51.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Tech Debt (99.9999%)
- **Heaviest Functions:** `_update_chunk_length` (Impact: 455.6), `decompress` (Impact: 158.4), `decompress` (Impact: 157.7)

### 8. `urllib3-2.6.3/src/urllib3/_collections.py` (PYTHON) -> Cumulative Risk: **761.27**
- **Archetype:** `file_cluster_16` (Distance: 12.17 IQR)
- **Magnitude:** 598.02 | **LOC:** 488 | **CtrlFlow:** 39.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `extend` (Impact: 141.5), `__init__` (Impact: 50.5), `__setitem__` (Impact: 37.2)

### 9. `urllib3-2.6.3/src/urllib3/exceptions.py` (PYTHON) -> Cumulative Risk: **755.0**
- **Archetype:** `file_cluster_16` (Distance: 11.94 IQR)
- **Magnitude:** 197.9 | **LOC:** 336 | **CtrlFlow:** 11.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `__init__` (Impact: 49.0), `pool` (Impact: 14.3), `__repr__` (Impact: 8.0)

### 10. `urllib3-2.6.3/src/urllib3/connection.py` (PYTHON) -> Cumulative Risk: **752.77**
- **Archetype:** `file_cluster_13` (Distance: 11.655 IQR)
- **Magnitude:** 810.7 | **LOC:** 1100 | **CtrlFlow:** 48.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.4004%)
- **Heaviest Functions:** `connect` (Impact: 249.3), `_tunnel` (Impact: 209.9), `putheader` (Impact: 60.6)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `urllib3-2.6.3/src/urllib3/response.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.455 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.604 IQR)
- **Top Global Matches:** file_cluster_13: 12.455, file_cluster_0: 12.563, file_cluster_16: 12.594
- **Magnitude:** 1904.14 | **LOC:** 1481 | **CtrlFlow:** 51.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (40.696%), Tech Debt (99.9999%)
**Top Internal Functions/Classes:**
  * `_update_chunk_length` (Impact: 455.6 | O(2^N) | DB: 8)
  * `decompress` (Impact: 158.4 | O(2^N) | DB: 6)
  * `decompress` (Impact: 157.7 | O(2^N) | DB: 4)
  * `decompress` (Impact: 122.0 | O(2^N) | DB: 7)
  * `decompress` (Impact: 97.2 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 287`, `structural_boundaries: 266`, `args: 82`, `func_start: 82`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 190`, `dead_code: 3`, `planned_debt: 1`, `fragile_debt: 5`, `duplicate_logic: 40`
* *Architecture:* `io: 6`, `api: 74`, `import: 27`
* *Defense:* `safety: 49`, `doc: 56`, `test: 2`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.129
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` brotli, json, zlib, collections, .util.retry, logging, warnings, ...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `urllib3-2.6.3/src/urllib3/connectionpool.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.524 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.849 IQR)
- **Top Global Matches:** file_cluster_13: 11.524, file_cluster_8: 11.739, file_cluster_16: 11.785
- **Magnitude:** 1231.78 | **LOC:** 1179 | **CtrlFlow:** 44.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (12.3364%), Tech Debt (34.9312%)
**Top Internal Functions/Classes:**
  * `_new_conn` (Impact: 1088.9 | O(2^N) | DB: 16)
  * `_close_pool_connections` (Impact: 20.5 | O(N^4))
  * `connection_from_url` (Impact: 13.5 | O(N^2))
    * *Intent:* # Put the connection back to be reused. If the connection is # expired then it will be None, which w...
  * `_normalize_host` (Impact: 11.1 | O(N^2))
  * `__init__` (Impact: 8.6 | O(N^3) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 103`, `structural_boundaries: 130`, `args: 27`, `func_start: 27`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 53`, `dead_code: 2`, `planned_debt: 2`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 2`, `api: 13`, `import: 30`
* *Defense:* `safety: 37`, `doc: 84`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 99.68
  * `Choke Point (Betweenness):` 0.136351 | `Ripple Effect (Closeness):` 0.308245
  * `Imports (Out-Degree: 11):` .util.connection, .util.timeout, typing_extensions, .util.ssl_match_hostname, .util.url, .util.retry, weakref, logging...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `urllib3-2.6.3/src/urllib3/connection.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.655 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.037 IQR)
- **Top Global Matches:** file_cluster_13: 11.655, file_cluster_8: 11.964, file_cluster_11: 11.992
- **Magnitude:** 810.7 | **LOC:** 1100 | **CtrlFlow:** 48.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 23
- **Risk Profile:** Cognitive Load (38.185%), Tech Debt (49.5861%)
**Top Internal Functions/Classes:**
  * `connect` (Impact: 249.3 | O(2^N) | DB: 23)
  * `_tunnel` (Impact: 209.9 | O(2^N) | DB: 8)
  * `putheader` (Impact: 60.6 | O(2^N))
    * *Intent:* """ Return True if a tunneling proxy is configured, else return False """
  * `close` (Impact: 21.5 | O(2^N) | DB: 8)
  * `_wrap_ipv6` (Impact: 13.2 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 134`, `structural_boundaries: 140`, `args: 31`, `func_start: 31`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 140`, `dead_code: 2`, `planned_debt: 4`, `duplicate_logic: 4`
* *Architecture:* `io: 27`, `api: 24`, `concurrency: 3`, `import: 37`
* *Defense:* `safety: 28`, `doc: 35`, `immutability_locks: 1`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 12.736
  * `Choke Point (Betweenness):` 0.010705 | `Ripple Effect (Closeness):` 0.046512
  * `Imports (Out-Degree: 12):` .util.timeout, re, .util.ssl_match_hostname, .util.url, errors, os, .util.ssltransport, logging...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `urllib3-2.6.3/src/urllib3/_collections.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.17 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.322 IQR)
- **Top Global Matches:** file_cluster_16: 12.17, file_cluster_13: 12.304, file_cluster_0: 12.517
- **Magnitude:** 598.02 | **LOC:** 488 | **CtrlFlow:** 39.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (16.9484%), Tech Debt (99.9998%)
**Top Internal Functions/Classes:**
  * `extend` (Impact: 141.5 | O(2^N))
  * `__init__` (Impact: 50.5 | O(2^N) | DB: 3)
  * `__setitem__` (Impact: 37.2 | O(N^5) | DB: 1)
  * `clear` (Impact: 35.1 | O(2^N) | DB: 1)
  * `add` (Impact: 31.5 | O(N^4) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 104`, `args: 42`, `func_start: 42`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 42`, `dead_code: 1`, `duplicate_logic: 17`
* *Architecture:* `api: 26`, `concurrency: 1`, `import: 7`
* *Defense:* `safety: 28`, `doc: 22`, `test: 1`, `sync_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 26.93
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.260465
  * `Imports (Out-Degree: 0):` __future__, threading, enum, typing_extensions, Protocol, function, typing, collections
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `urllib3-2.6.3/dummyserver/testcase.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.562 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.72 IQR)
- **Top Global Matches:** file_cluster_13: 10.562, file_cluster_0: 10.587, file_cluster_4: 10.786
- **Magnitude:** 236.78 | **LOC:** 354 | **CtrlFlow:** 31.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (59.7803%), Tech Debt (99.5437%)
**Top Internal Functions/Classes:**
  * `socket_handler` (Impact: 64.2 | O(N^6) | DB: 10)
  * `consume_request` (Impact: 20.6 | O(N^4) | DB: 6)
  * `quit_server_thread` (Impact: 12.4 | O(N^3))
  * `_get_socket_mark` (Impact: 12.3 | O(N^3) | DB: 6)
  * `setup_class` (Impact: 11.3 | O(N^5) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 71`, `args: 19`, `func_start: 19`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 25`, `duplicate_logic: 7`, `orphaned_logic: 4`
* *Architecture:* `io: 15`, `api: 24`, `concurrency: 23`, `import: 14`
* *Defense:* `safety: 10`, `doc: 8`, `test: 7`, `sync_locks: 11`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.129
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` dummyserver.asgi_proxy, __future__, threading, ssl, socket, dummyserver.app, pytest, dummyserver.hypercornserver...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `urllib3-2.6.3/src/urllib3/util/ssltransport.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_16` (Drift: 9.876 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.151 IQR)
- **Top Global Matches:** file_cluster_16: 9.876, file_cluster_13: 10.042, file_cluster_0: 10.188
- **Magnitude:** 225.36 | **LOC:** 272 | **CtrlFlow:** 36.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (11.9557%), Tech Debt (99.7646%)
**Top Internal Functions/Classes:**
  * `sendall` (Impact: 40.5 | O(2^N))
  * `_wrap_ssl_read` (Impact: 25.4 | O(N^4))
  * `recv` (Impact: 16.2 | O(2^N))
  * `send` (Impact: 16.2 | O(2^N))
  * `_validate_ssl_context_for_tls_in_tls` (Impact: 10.4 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 67`, `args: 29`, `func_start: 29`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 5`, `planned_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `io: 16`, `api: 25`, `import: 8`
* *Defense:* `safety: 7`, `doc: 10`, `test: 2`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 19.504
  * `Choke Point (Betweenness):` 0.001569 | `Ripple Effect (Closeness):` 0.15137
  * `Imports (Out-Degree: 2):` __future__, typing_extensions, ssl, socket, io, .ssl_, typing, ..exceptions
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `urllib3-2.6.3/src/urllib3/exceptions.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.94 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.129 IQR)
- **Top Global Matches:** file_cluster_16: 11.94, file_cluster_13: 11.989, file_cluster_7: 12.346
- **Magnitude:** 197.9 | **LOC:** 336 | **CtrlFlow:** 11.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (17.1029%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 49.0 | O(2^N))
    * *Intent:* """Fetching HTTPS resources through HTTPS proxies is unsupported"""
  * `pool` (Impact: 14.3 | O(2^N))
  * `__repr__` (Impact: 8.0 | O(2^N) | DB: 2)
  * `__init__` (Impact: 7.0 | O(2^N) | DB: 5)
  * `__init__` (Impact: 6.9 | O(2^N) | DB: 1)
    * *Intent:* # For pickling purposes. return self.__class__, (None, self.url, self._message) class SSLError(HTTPE...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 85`, `args: 21`, `func_start: 21`, `class_start: 38`
* *Risk/State:* `state_mutation: 20`, `planned_debt: 1`, `duplicate_logic: 17`
* *Architecture:* `io: 3`, `api: 39`, `import: 10`
* *Defense:* `doc: 81`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 134.572
  * `Choke Point (Betweenness):` 0.106497 | `Ripple Effect (Closeness):` 0.423837
  * `Imports (Out-Degree: 2):` .connection, __future__, warnings, email.errors, socket, http.client, .connectionpool, .response...
  * `Imported By (In-Degree: 16):` (Excluded from Brief to save tokens)

### `urllib3-2.6.3/dummyserver/app.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_4` (Drift: 9.743 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.477 IQR)
- **Top Global Matches:** file_cluster_4: 9.743, file_cluster_0: 9.878, file_cluster_13: 10.056
- **Magnitude:** 168.22 | **LOC:** 484 | **CtrlFlow:** 24.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (59.5522%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `wheel` (Impact: 12.6 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 184`, `args: 37`, `func_start: 36`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 6`, `dead_code: 1`
* *Architecture:* `io: 1`, `api: 34`, `concurrency: 109`, `import: 15`
* *Defense:* `safety: 4`, `doc: 12`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 13.225
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.046512
  * `Imports (Out-Degree: 0):` __future__, mimetypes, datetime, quart_trio, quart, quart.typing, io, email.utils...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `urllib3-2.6.3/src/urllib3/http2/connection.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.971 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.021 IQR)
- **Top Global Matches:** file_cluster_13: 11.971, file_cluster_16: 12.162, file_cluster_11: 12.257
- **Magnitude:** 150.82 | **LOC:** 357 | **CtrlFlow:** 50.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (52.607%), Tech Debt (89.9121%)
**Top Internal Functions/Classes:**
  * `close` (Impact: 42.3 | O(2^N) | DB: 4)
  * `data` (Impact: 2.7 | O(N^2))
  * `get_redirect_location` (Impact: 2.7 | O(N^2))
  * `close` (Impact: 2.7 | O(N^2))
  * `request` (Impact: 2.0 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 64`, `args: 20`, `func_start: 20`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 63`, `planned_debt: 5`, `duplicate_logic: 2`
* *Architecture:* `api: 18`, `concurrency: 7`, `import: 14`
* *Defense:* `safety: 14`, `doc: 12`, `test: 1`, `sync_locks: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.129
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` __future__, logging, h2.config, .._base_connection, h2.connection, ..connection, threading, h2.events...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `urllib3-2.6.3/src/urllib3/util/ssl_.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.634 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.708 IQR)
- **Top Global Matches:** file_cluster_13: 10.634, file_cluster_8: 10.755, file_cluster_16: 10.915
- **Magnitude:** 143.0 | **LOC:** 528 | **CtrlFlow:** 55.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (10.8368%), Tech Debt (54.157%)
**Top Internal Functions/Classes:**
  * `assert_fingerprint` (Impact: 29.0 | O(N^3))
  * `resolve_cert_reqs` (Impact: 23.3 | O(N^3))
  * `resolve_ssl_version` (Impact: 23.3 | O(N^3))
  * `_is_key_file_encrypted` (Impact: 20.5 | O(N^4) | DB: 3)
  * `is_ipaddress` (Impact: 18.7 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 77`, `structural_boundaries: 62`, `args: 12`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `dead_code: 2`, `duplicate_logic: 3`
* *Architecture:* `io: 18`, `api: 12`, `import: 17`
* *Defense:* `safety: 21`, `doc: 35`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 33.144
  * `Choke Point (Betweenness):` 0.020856 | `Ripple Effect (Closeness):` 0.188372
  * `Imports (Out-Degree: 3):` __future__, warnings, .url, .ssltransport, ssl, socket, hmac, os...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `urllib3-2.6.3/src/urllib3/fields.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.548 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.229 IQR)
- **Top Global Matches:** file_cluster_16: 11.548, file_cluster_13: 11.568, file_cluster_8: 11.818
- **Magnitude:** 133.04 | **LOC:** 342 | **CtrlFlow:** 45.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (29.5961%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `format_header_param_rfc2231` (Impact: 64.4 | O(2^N))
  * `format_header_param_html5` (Impact: 5.8 | O(2^N))
  * `format_header_param` (Impact: 5.8 | O(2^N))
  * `_render_parts` (Impact: 4.8 | O(N^3))
  * `_render_part` (Impact: 3.2 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 33`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 30`
* *Architecture:* `api: 11`, `import: 8`
* *Defense:* `safety: 6`, `doc: 40`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 19.86
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.148168
  * `Imports (Out-Degree: 0):` __future__, mimetypes, warnings, email.utils, typing
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `urllib3-2.6.3/dummyserver/asgi_proxy.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_4` (Drift: 10.51 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.24 IQR)
- **Top Global Matches:** file_cluster_4: 10.51, file_cluster_13: 10.702, file_cluster_8: 10.859
- **Magnitude:** 120.2 | **LOC:** 115 | **CtrlFlow:** 27.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (94.4799%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `connect` (Impact: 37.2 | O(N^5))
  * `_read_body` (Impact: 18.4 | O(N^3) | DB: 1)
  * `__init__` (Impact: 7.2 | O(N^3) | DB: 2)
  * `absolute_uri` (Impact: 1.8 | O(N^2))
  * `__call__` (Impact: 1.6 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 42`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 15`
* *Architecture:* `io: 2`, `api: 6`, `concurrency: 31`, `import: 6`
* *Defense:* `safety: 3`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 9.281
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.023256
  * `Imports (Out-Degree: 0):` __future__, httpx, hypercorn.typing, ssl, trio, typing
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `urllib3-2.6.3/dummyserver/socketserver.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.346 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.114 IQR)
- **Top Global Matches:** file_cluster_13: 10.346, file_cluster_16: 10.759, file_cluster_8: 10.852
- **Magnitude:** 105.32 | **LOC:** 191 | **CtrlFlow:** 29.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 28
- **Risk Profile:** Cognitive Load (11.9449%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_start_server` (Impact: 27.0 | O(N^4) | DB: 28)
  * `_resolves_to_ipv6` (Impact: 20.6 | O(N^4) | DB: 12)
  * `_has_ipv6` (Impact: 17.1 | O(N^3) | DB: 12)
    * *Intent:* """Returns True if the system can bind an IPv6 address."""
  * `encrypt_key_pem` (Impact: 3.1 | O(N^2))
  * `run` (Impact: 2.7 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 38`, `args: 8`, `func_start: 8`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 14`
* *Architecture:* `io: 27`, `api: 9`, `concurrency: 4`, `import: 15`
* *Defense:* `safety: 4`, `doc: 12`, `sync_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.281
  * `Choke Point (Betweenness):` 0.001846 | `Ripple Effect (Closeness):` 0.023256
  * `Imports (Out-Degree: 2):` __future__, logging, warnings, urllib3.exceptions, urllib3.util, threading, typing_extensions, ssl...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `urllib3-2.6.3/src/urllib3/poolmanager.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.938 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.988 IQR)
- **Top Global Matches:** file_cluster_13: 10.938, file_cluster_16: 11.011, file_cluster_8: 11.148
- **Magnitude:** 92.5 | **LOC:** 652 | **CtrlFlow:** 40.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (15.3952%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_proxy_requires_url_absolute_form` (Impact: 7.4 | O(N^3))
  * `clear` (Impact: 5.4 | O(2^N) | DB: 1)
    * *Intent:* # Locally set the pool classes and keys so other PoolManagers can # override them. self.pool_classes...
  * `__enter__` (Impact: 2.7 | O(N^2))
  * `__init__` (Impact: 1.8 | O(N^2))
    * *Intent:* #: A dictionary that maps a scheme to a callable that creates a pool key. #: This can be used to alt...
  * `__exit__` (Impact: 1.8 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 82`, `args: 18`, `func_start: 18`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 36`, `dead_code: 1`
* *Architecture:* `api: 16`, `import: 20`
* *Defense:* `safety: 10`, `doc: 42`, `immutability_locks: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 10.72
  * `Choke Point (Betweenness):` 0.002907 | `Ripple Effect (Closeness):` 0.046512
  * `Imports (Out-Degree: 8):` .util.connection, .util.timeout, typing_extensions, .util.url, typing, .util.retry, logging, urllib3...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `urllib3-2.6.3/src/urllib3/util/retry.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.336 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.627 IQR)
- **Top Global Matches:** file_cluster_13: 11.336, file_cluster_8: 11.42, file_cluster_16: 11.509
- **Magnitude:** 85.74 | **LOC:** 550 | **CtrlFlow:** 47.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (19.2554%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `new` (Impact: 4.6 | O(N^3) | DB: 1)
  * `__repr__` (Impact: 3.7 | O(N^3))
  * `__init__` (Impact: 3.0 | O(N^3))
  * `from_int` (Impact: 1.8 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 62`, `structural_boundaries: 69`, `args: 17`, `func_start: 16`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 52`
* *Architecture:* `api: 15`, `import: 14`
* *Defense:* `safety: 4`, `doc: 41`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 79.638
  * `Choke Point (Betweenness):` 0.011213 | `Ripple Effect (Closeness):` 0.302741
  * `Imports (Out-Degree: 3):` __future__, logging, itertools, time, email, typing_extensions, re, .util...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `urllib3-2.6.3/src/urllib3/http2/probe.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.358 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 7.242 IQR)
- **Top Global Matches:** file_cluster_16: 11.358, file_cluster_4: 11.364, file_cluster_13: 11.492
- **Magnitude:** 79.0 | **LOC:** 88 | **CtrlFlow:** 44.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (41.6009%), Tech Debt (50.0%)
**Top Internal Functions/Classes:**
  * `acquire_and_get` (Impact: 31.6 | O(N^5))
    * *Intent:* # By the end of this block we know that # _cache_[values,locks] is available. value = None with self...
  * `_values` (Impact: 10.6 | O(N^3))
    * *Intent:* """This function is for testing purposes only. Gets the current state of the probe cache"""
  * `_reset` (Impact: 7.2 | O(N^3) | DB: 2)
  * `__init__` (Impact: 2.8 | O(N^2) | DB: 1)
  * `set_and_release` (Impact: 1.6 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 14`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 7`, `orphaned_logic: 1`
* *Architecture:* `api: 3`, `concurrency: 14`, `import: 2`
* *Defense:* `safety: 6`, `doc: 4`, `test: 1`, `sync_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.129
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` threading, __future__
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `urllib3-2.6.3/src/urllib3/util/request.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.637 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.897 IQR)
- **Top Global Matches:** file_cluster_13: 10.637, file_cluster_8: 10.783, file_cluster_16: 10.913
- **Magnitude:** 72.24 | **LOC:** 264 | **CtrlFlow:** 47.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (9.3047%), Tech Debt (14.2366%)
**Top Internal Functions/Classes:**
  * `rewind_body` (Impact: 35.6 | O(N^4))
  * `chunk_readable` (Impact: 21.2 | O(N^5))
  * `make_headers` (Impact: 1.4 | O(N^1))
  * `set_file_position` (Impact: 1.1 | O(N^1))
  * `body_to_chunks` (Impact: 1.1 | O(N^1))
    * *Intent:* """ if pos is not None: rewind_body(body, pos) elif getattr(body, "tell", None) is not None: try: po...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 44`, `args: 5`, `func_start: 5`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `planned_debt: 1`
* *Architecture:* `io: 1`, `api: 9`, `import: 13`
* *Defense:* `safety: 22`, `doc: 16`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 17.528
  * `Choke Point (Betweenness):` 0.000508 | `Ripple Effect (Closeness):` 0.226047
  * `Imports (Out-Degree: 2):` base64, __future__, brotlicffi, urllib3, compression, brotli, enum, backports...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `urllib3-2.6.3/dummyserver/hypercornserver.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 8.628 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 6.383 IQR)
- **Top Global Matches:** file_cluster_13: 8.628, file_cluster_8: 9.097, file_cluster_16: 9.147
- **Magnitude:** 68.02 | **LOC:** 147 | **CtrlFlow:** 32.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 43
- **Risk Profile:** Cognitive Load (13.2058%), Tech Debt (16.8108%)
**Top Internal Functions/Classes:**
  * `_retry_create_urllib3_sockets` (Impact: 25.2 | O(N^6) | DB: 12)
    * *Intent:* # When we request a socket with host localhost and port zero, Hypercorn # only binds to IPv4. But we...
  * `_create_urllib3_sockets` (Impact: 15.1 | O(N^3) | DB: 43)
  * `create_sockets` (Impact: 10.9 | O(N^3))
  * `main` (Impact: 2.2 | O(N^1))
    * *Intent:* # For debugging dummyserver itself - PYTHONPATH=src python -m dummyserver.hypercornserver from .app ...
  * `_start_server` (Impact: 1.3 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 38`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 1`, `planned_debt: 1`
* *Architecture:* `io: 20`, `api: 6`, `concurrency: 3`, `import: 17`
* *Defense:* `safety: 6`, `test: 2`, `sync_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.281
  * `Choke Point (Betweenness):` 0.000277 | `Ripple Effect (Closeness):` 0.023256
  * `Imports (Out-Degree: 2):` hypercorn, __future__, .app, anyio.abc, hypercorn.typing, urllib3.util.url, anyio.to_thread, hypercorn.trio...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `urllib3-2.6.3/src/urllib3/util/response.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.607 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.42 IQR)
- **Top Global Matches:** file_cluster_13: 11.607, file_cluster_16: 11.838, file_cluster_8: 11.842
- **Magnitude:** 56.26 | **LOC:** 102 | **CtrlFlow:** 34.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (7.86%), Tech Debt (94.0652%)
**Top Internal Functions/Classes:**
  * `assert_header_parsing` (Impact: 34.0 | O(N^3))
  * `is_fp_closed` (Impact: 13.2 | O(N^2))
    * *Intent:* """ Checks whether a given file-like object is closed. :param obj: The file-like object to check. ""...
  * `is_response_to_head` (Impact: 2.3 | O(N^1))
    * *Intent:* # httplib is assuming a response body is available # when parsing headers even when httplib only sen...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 19`, `args: 3`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `fragile_debt: 1`
* *Architecture:* `api: 6`, `import: 4`
* *Defense:* `safety: 9`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 10.114
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.062016
  * `Imports (Out-Degree: 1):` __future__, http.client, ..exceptions, email.errors
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `urllib3-2.6.3/src/urllib3/util/wait.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.976 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.908 IQR)
- **Top Global Matches:** file_cluster_13: 11.976, file_cluster_16: 12.298, file_cluster_11: 12.325
- **Magnitude:** 43.02 | **LOC:** 125 | **CtrlFlow:** 40.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (25.3224%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `do_poll` (Impact: 10.0 | O(N^3))
    * *Intent:* # For some reason, poll() takes timeout in milliseconds
  * `_have_working_poll` (Impact: 8.3 | O(N^2))
    * *Intent:* # Apparently some systems have a select.poll that fails as soon as you try # to use it, either due t...
  * `wait_for_read` (Impact: 1.9 | O(N^1) | DB: 6)
    * *Intent:* """Waits for reading to be available on a given socket. Returns True if the socket is readable, or F...
  * `wait_for_write` (Impact: 1.9 | O(N^1) | DB: 6)
  * `select_wait_for_socket` (Impact: 1.2 | O(N^1) | DB: 6)
    * *Intent:* # # Now, how do we choose between select() and poll()? On traditional Unixes, # select() has a stran...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 22`, `args: 7`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 9`, `dead_code: 1`
* *Architecture:* `io: 11`, `api: 7`, `import: 4`
* *Defense:* `safety: 3`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.689
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.062016
  * `Imports (Out-Degree: 0):` but, __future__, time, functools, select, socket
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `urllib3-2.6.3/src/urllib3/util/url.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.835 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.645 IQR)
- **Top Global Matches:** file_cluster_8: 9.835, file_cluster_16: 9.952, file_cluster_13: 10.134
- **Magnitude:** 34.76 | **LOC:** 470 | **CtrlFlow:** 59.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (14.7002%), Tech Debt (87.2926%)
**Top Internal Functions/Classes:**
  * `__str__` (Impact: 2.7 | O(N^2))
  * `_encode_invalid_chars` (Impact: 1.1 | O(N^1))
    * *Intent:* # "https://google.com/mail/"
  * `_encode_invalid_chars` (Impact: 1.1 | O(N^1))
  * `_encode_invalid_chars` (Impact: 1.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 55`, `args: 18`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 15`, `planned_debt: 1`, `duplicate_logic: 3`
* *Architecture:* `api: 8`, `import: 6`
* *Defense:* `safety: 6`, `doc: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 73.241
  * `Choke Point (Betweenness):` 0.0299 | `Ripple Effect (Closeness):` 0.360713
  * `Imports (Out-Degree: 2):` __future__, urllib3, idna, re, typing, .util, ..exceptions
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `urllib3-2.6.3/src/urllib3/util/connection.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.188 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.288 IQR)
- **Top Global Matches:** file_cluster_13: 10.188, file_cluster_8: 10.263, file_cluster_16: 10.275
- **Magnitude:** 33.7 | **LOC:** 138 | **CtrlFlow:** 45.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (6.9504%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_has_ipv6` (Impact: 17.1 | O(N^3) | DB: 12)
  * `allowed_gai_family` (Impact: 5.6 | O(N^2) | DB: 9)
  * `is_connection_dropped` (Impact: 2.2 | O(N^1))
    * *Intent:* """ Returns True if the connection is dropped and should be closed. :param conn: :class:`urllib3.con...
  * `create_connection` (Impact: 1.2 | O(N^1))
    * *Intent:* # This function is copied from socket.py in the Python 2.7 standard # library test suite. Added to i...
  * `_set_socket_options` (Impact: 1.1 | O(N^1) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 23`, `args: 5`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 2`
* *Architecture:* `io: 16`, `api: 5`, `import: 6`
* *Defense:* `safety: 8`, `doc: 9`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 39.466
  * `Choke Point (Betweenness):` 0.009044 | `Ripple Effect (Closeness):` 0.260823
  * `Imports (Out-Degree: 2):` __future__, .._base_connection, socket, typing, .timeout, ..exceptions
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `urllib3-2.6.3/src/urllib3/filepost.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.611 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.104 IQR)
- **Top Global Matches:** file_cluster_13: 9.611, file_cluster_16: 9.742, file_cluster_8: 10.022
- **Magnitude:** 32.76 | **LOC:** 90 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (5.9601%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `iter_field_objects` (Impact: 24.8 | O(N^3))
  * `choose_boundary` (Impact: 1.9 | O(N^1) | DB: 3)
    * *Intent:* """ Our embarrassingly-simple replacement for mimetools.choose_boundary. """
  * `encode_multipart_formdata` (Impact: 1.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 15`, `args: 3`, `func_start: 3`
* *Risk/State:* None
* *Architecture:* `io: 1`, `api: 4`, `import: 7`
* *Defense:* `safety: 4`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.801
  * `Choke Point (Betweenness):` 0.015504 | `Ripple Effect (Closeness):` 0.177015
  * `Imports (Out-Degree: 1):` __future__, codecs, .fields, io, os, typing, binascii
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `urllib3-2.6.3/src/urllib3/_request_methods.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_16` (Drift: 9.771 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.394 IQR)
- **Top Global Matches:** file_cluster_16: 9.771, file_cluster_13: 9.845, file_cluster_8: 9.914
- **Magnitude:** 30.02 | **LOC:** 279 | **CtrlFlow:** 43.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (11.0309%), Tech Debt (23.0251%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 6.1 | O(N^2) | DB: 1)
  * `urlopen` (Impact: 1.9 | O(N^2))
  * `request` (Impact: 1.9 | O(N^2))
  * `request_encode_url` (Impact: 1.9 | O(N^2))
  * `request_encode_body` (Impact: 1.9 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 26`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 7`, `planned_debt: 2`
* *Architecture:* `api: 7`, `import: 8`
* *Defense:* `doc: 25`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 16.971
  * `Choke Point (Betweenness):` 0.028977 | `Ripple Effect (Closeness):` 0.220175
  * `Imports (Out-Degree: 3):` __future__, ._base_connection, .filepost, urllib.parse, json, ._collections, .response, typing
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `urllib3-2.6.3/src/urllib3/util/ssl_match_hostname.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.984 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.283 IQR)
- **Top Global Matches:** file_cluster_13: 10.984, file_cluster_8: 11.169, file_cluster_16: 11.377
- **Magnitude:** 29.12 | **LOC:** 160 | **CtrlFlow:** 63.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (35.8558%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_ipaddress_match` (Impact: 2.1 | O(N^1))
  * `match_hostname` (Impact: 1.2 | O(N^1))
    * *Intent:* # OpenSSL may add a trailing newline to a subjectAltName's IP address # Divergence from upstream: ip...
  * `_dnsname_match` (Impact: 1.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 21`, `args: 3`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 21`
* *Architecture:* `io: 1`, `api: 2`, `import: 6`
* *Defense:* `safety: 2`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 16.664
  * `Choke Point (Betweenness):` 0.023256 | `Ripple Effect (Closeness):` 0.226047
  * `Imports (Out-Degree: 1):` __future__, re, .ssl_, typing, ipaddress
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `urllib3-2.6.3/src/urllib3/contrib/socks.py` (PYTHON) | Magnitude: 4.61 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 119, structural_boundaries: 40, branch: 18, encapsulation: 18
- `urllib3-2.6.3/dummyserver/testcase.py` (PYTHON) | Magnitude: 236.78 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 253, structural_boundaries: 71, branch: 32, state_mutation: 25
- `urllib3-2.6.3/src/urllib3/contrib/pyopenssl.py` (PYTHON) | Magnitude: 7.68 | Delta: **0.043 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 334, structural_boundaries: 135, encapsulation: 107, branch: 68
- `urllib3-2.6.3/src/urllib3/util/proxy.py` (PYTHON) | Magnitude: 3.62 | Delta: **0.055 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 12, branch: 6, doc: 5
- `urllib3-2.6.3/src/urllib3/poolmanager.py` (PYTHON) | Magnitude: 92.5 | Delta: **0.073 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 311, structural_boundaries: 82, branch: 55, doc: 42

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `urllib3-2.6.3/src/urllib3/http2/probe.py` (PYTHON) | Magnitude: 79.0 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 50, encapsulation: 37, structural_boundaries: 14, concurrency: 14
- `urllib3-2.6.3/src/urllib3/fields.py` (PYTHON) | Magnitude: 133.04 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 148, doc: 40, structural_boundaries: 33, state_mutation: 30
- `urllib3-2.6.3/src/urllib3/exceptions.py` (PYTHON) | Magnitude: 197.9 | Delta: **0.049 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 98, structural_boundaries: 85, doc: 81, encapsulation: 52
- `urllib3-2.6.3/src/urllib3/_request_methods.py` (PYTHON) | Magnitude: 30.02 | Delta: **0.074 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 104, structural_boundaries: 26, doc: 25, branch: 20
- `urllib3-2.6.3/src/urllib3/_collections.py` (PYTHON) | Magnitude: 598.02 | Delta: **0.134 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 253, structural_boundaries: 104, encapsulation: 102, branch: 69

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `urllib3-2.6.3/dummyserver/app.py` (PYTHON) | Magnitude: 168.22 | Delta: **0.135 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 239, structural_boundaries: 184, concurrency: 109, branch: 58
- `urllib3-2.6.3/dummyserver/asgi_proxy.py` (PYTHON) | Magnitude: 120.2 | Delta: **0.192 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 91, structural_boundaries: 42, concurrency: 31, branch: 16
- `urllib3-2.6.3/src/urllib3/contrib/emscripten/emscripten_fetch_worker.js` (JAVASCRIPT) | Magnitude: 0.95 | Delta: **0.466 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 84, state_mutation: 59, structural_boundaries: 24, concurrency: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `urllib3-2.6.3/src/urllib3/_base_connection.py` (PYTHON) | Magnitude: 25.86 | Delta: **0.08 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 109, structural_boundaries: 28, encapsulation: 18, generics: 16
- `urllib3-2.6.3/src/urllib3/util/url.py` (PYTHON) | Magnitude: 34.76 | Delta: **0.117 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 233, encapsulation: 87, branch: 81, structural_boundaries: 55
- `urllib3-2.6.3/src/urllib3/util/util.py` (PYTHON) | Magnitude: 10.1 | Delta: **0.153 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 19, branch: 15, safety: 6
- `urllib3-2.6.3/src/urllib3/util/__init__.py` (PYTHON) | Magnitude: 16.78 | Delta: **0.514 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 27, structural_boundaries: 18, import: 9, encapsulation: 2

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `urllib3-2.6.3/src/urllib3/exceptions.py` -> **Severity: 10.247** (Bridge: 0.1065 * Flux: 96.2212%)
- `urllib3-2.6.3/src/urllib3/connectionpool.py` -> **Severity: 10.068** (Bridge: 0.1364 * Flux: 73.8403%)
- `urllib3-2.6.3/src/urllib3/util/ssl_match_hostname.py` -> **Severity: 2.326** (Bridge: 0.0233 * Flux: 100.0%)
- `urllib3-2.6.3/src/urllib3/util/url.py` -> **Severity: 1.551** (Bridge: 0.0299 * Flux: 51.864%)
- `urllib3-2.6.3/src/urllib3/_request_methods.py` -> **Severity: 1.546** (Bridge: 0.029 * Flux: 53.3398%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `urllib3-2.6.3/src/urllib3/util/ssl_match_hostname.py` -> **Severity: 12.038** (Embedded: 0.226 * Error Risk: 53.2558%)
- `urllib3-2.6.3/src/urllib3/_request_methods.py` -> **Severity: 11.35** (Embedded: 0.2202 * Error Risk: 51.5517%)
- `urllib3-2.6.3/src/urllib3/fields.py` -> **Severity: 6.732** (Embedded: 0.1482 * Error Risk: 45.4321%)
- `urllib3-2.6.3/src/urllib3/util/retry.py` -> **Severity: 3.299** (Embedded: 0.3027 * Error Risk: 10.8962%)
- `urllib3-2.6.3/src/urllib3/util/wait.py` -> **Severity: 3.27** (Embedded: 0.062 * Error Risk: 52.7273%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `urllib3-2.6.3/src/urllib3/exceptions.py` -> **Severity: 13391.085** (Blast Radius: 134.572 * Doc Risk: 99.5087%)
- `urllib3-2.6.3/src/urllib3/util/util.py` -> **Severity: 8582.224** (Blast Radius: 86.035 * Doc Risk: 99.7527%)
- `urllib3-2.6.3/src/urllib3/_base_connection.py` -> **Severity: 5285.485** (Blast Radius: 52.928 * Doc Risk: 99.8618%)
- `urllib3-2.6.3/src/urllib3/util/connection.py` -> **Severity: 3189.117** (Blast Radius: 39.466 * Doc Risk: 80.8067%)
- `urllib3-2.6.3/src/urllib3/_collections.py` -> **Severity: 2693.0** (Blast Radius: 26.93 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
