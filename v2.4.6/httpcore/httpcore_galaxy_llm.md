# ARCHITECTURAL_BRIEF: httpcore
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/httpcore` |
| **Timestamp** | `2026-08-03T21:21:27.653125+00:00` |
| **Scan Duration** | `0.35s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 53 malicious artifacts.

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
| Total Artifacts | 61 |
| Analyzed Artifacts (Scanned) | 56 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 5 |
| Total LOC | 9280 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 91.8% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.1419 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0475 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.9828 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 3 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 53 | 9280 | 94.6% |
| MARKDOWN | 3 | 0 | 5.4% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.331`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 21 | 37.5% |
| file_cluster_13 | 18 | 32.1% |
| file_cluster_4 | 9 | 16.1% |
| file_cluster_16 | 4 | 7.1% |
| file_cluster_0 | 1 | 1.8% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 3 | 5.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 5*

**Composition by Extension & Reason:**
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.py`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 99.2 | 24.8 | 14.8 | 5.0 |
| Error & Exception Exposure | 0.0 | 82.3 | 11.7 | 1.3 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 25.5 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 26.1 | 1.0 | 0.0 |
| API Exposure | 0.0 | 13.1 | 4.7 | 4.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 49.1 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 29.6 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 91.6 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 49.9 | 40.0 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 74.0 | 99.8 | 100.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.1 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 64.2 | 100.0 | 100.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 3.8 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `httpcore-1.0.9/httpcore/_backends/sync.py` (Hits: 23)
- `httpcore-1.0.9/tests/benchmark/client.py` (Hits: 8)
- `httpcore-1.0.9/httpcore/_backends/trio.py` (Hits: 7)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **base.py** (`httpcore-1.0.9/httpcore/_backends/base.py`) — 17 inbound connections
2. **_exceptions.py** (`httpcore-1.0.9/httpcore/_exceptions.py`) — 17 inbound connections
3. **_models.py** (`httpcore-1.0.9/httpcore/_models.py`) — 17 inbound connections
4. **_synchronization.py** (`httpcore-1.0.9/httpcore/_synchronization.py`) — 13 inbound connections
5. **_trace.py** (`httpcore-1.0.9/httpcore/_trace.py`) — 10 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **http2.py** (`httpcore-1.0.9/httpcore/_async/http2.py`) — 17 outbound dependencies
2. **http2.py** (`httpcore-1.0.9/httpcore/_sync/http2.py`) — 17 outbound dependencies
3. **connection.py** (`httpcore-1.0.9/httpcore/_async/connection.py`) — 16 outbound dependencies
4. **http_proxy.py** (`httpcore-1.0.9/httpcore/_async/http_proxy.py`) — 16 outbound dependencies
5. **connection.py** (`httpcore-1.0.9/httpcore/_sync/connection.py`) — 16 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `handle_async_request` (@ `httpcore-1.0.9/httpcore/_async/socks_proxy.py`) -> Impact: **234.6** | LOC: 84
- `handle_request` (@ `httpcore-1.0.9/httpcore/_sync/socks_proxy.py`) -> Impact: **234.6** | LOC: 84
- `handle_async_request` (@ `httpcore-1.0.9/httpcore/_async/http_proxy.py`) -> Impact: **185.8** | LOC: 79
- `handle_request` (@ `httpcore-1.0.9/httpcore/_sync/http_proxy.py`) -> Impact: **185.8** | LOC: 79
- `handle_async_request` (@ `httpcore-1.0.9/httpcore/_async/connection_pool.py`) -> Impact: **136.7** | LOC: 67
- `handle_request` (@ `httpcore-1.0.9/httpcore/_sync/connection_pool.py`) -> Impact: **136.7** | LOC: 67
- `handle_async_request` (@ `httpcore-1.0.9/httpcore/_async/http2.py`) -> Impact: **126.4** | LOC: 103
- `handle_request` (@ `httpcore-1.0.9/httpcore/_sync/http2.py`) -> Impact: **126.4** | LOC: 103
- `handle_async_request` (@ `httpcore-1.0.9/httpcore/_async/connection.py`) -> Impact: **123.0** | LOC: 35
- `handle_request` (@ `httpcore-1.0.9/httpcore/_sync/connection.py`) -> Impact: **123.0** | LOC: 35

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `handle_async_request` (@ `httpcore-1.0.9/httpcore/_async/connection.py`) -> **O(2^N) [Recursive]**
- `handle_async_request` (@ `httpcore-1.0.9/httpcore/_async/connection_pool.py`) -> **O(2^N) [Recursive]**
- `handle_async_request` (@ `httpcore-1.0.9/httpcore/_async/http_proxy.py`) -> **O(2^N) [Recursive]**
- `handle_async_request` (@ `httpcore-1.0.9/httpcore/_async/socks_proxy.py`) -> **O(2^N) [Recursive]**
- `handle_request` (@ `httpcore-1.0.9/httpcore/_sync/connection.py`) -> **O(2^N) [Recursive]**
- `handle_request` (@ `httpcore-1.0.9/httpcore/_sync/connection_pool.py`) -> **O(2^N) [Recursive]**
- `handle_request` (@ `httpcore-1.0.9/httpcore/_sync/http_proxy.py`) -> **O(2^N) [Recursive]**
- `handle_request` (@ `httpcore-1.0.9/httpcore/_sync/socks_proxy.py`) -> **O(2^N) [Recursive]**
- `aclose` (@ `httpcore-1.0.9/httpcore/_async/connection_pool.py`) -> **O(2^N) [Recursive]**
- `close` (@ `httpcore-1.0.9/httpcore/_sync/connection_pool.py`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `get_extra_info` (@ `httpcore-1.0.9/httpcore/_backends/trio.py`) -> DB Complexity: **21**
- `run_async_requests` (@ `httpcore-1.0.9/tests/benchmark/client.py`) -> DB Complexity: **14**
- `_assign_requests_to_connections` (@ `httpcore-1.0.9/httpcore/_async/connection_pool.py`) -> DB Complexity: **9**
  * *Intent:* # Assign incoming requests to available connections,
- `_assign_requests_to_connections` (@ `httpcore-1.0.9/httpcore/_sync/connection_pool.py`) -> DB Complexity: **9**
  * *Intent:* # Assign incoming requests to available connections,
- `is_socket_readable` (@ `httpcore-1.0.9/httpcore/_utils.py`) -> DB Complexity: **9**
  * *Intent:* """ Return whether a socket, as identifed by its file descriptor, is readable. "A socket is readable" means that the read buffer isn't empty, i.e. tha...
- `__init__` (@ `httpcore-1.0.9/httpcore/_backends/sync.py`) -> DB Complexity: **7**
- `handle_async_request` (@ `httpcore-1.0.9/httpcore/_async/http2.py`) -> DB Complexity: **6**
- `__init__` (@ `httpcore-1.0.9/httpcore/_backends/sync.py`) -> DB Complexity: **6**
  * *Intent:* # Defined in RFC 8449 TLS_RECORD_SIZE = 16384 def __init__( self, sock: socket.socket, ssl_context: ssl.SSLContext, server_hostname: str | None = None...
- `handle_request` (@ `httpcore-1.0.9/httpcore/_sync/http2.py`) -> DB Complexity: **6**
- `main` (@ `httpcore-1.0.9/tests/benchmark/client.py`) -> DB Complexity: **6**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `httpcore-1.0.9/httpcore/_async` | 8 | 2917.88 | 50.24% | 59.98% |
| `httpcore-1.0.9/httpcore/_sync` | 8 | 2554.88 | 26.36% | 59.98% |
| `httpcore-1.0.9/tests/_async` | 8 | 1818.62 | 12.76% | 0.0% |
| `httpcore-1.0.9/tests/_sync` | 8 | 1293.36 | 2.83% | 0.0% |
| `httpcore-1.0.9/httpcore` | 8 | 1244.64 | 27.81% | 23.66% |
| `httpcore-1.0.9/httpcore/_backends` | 6 | 615.6 | 35.85% | 33.33% |
| `httpcore-1.0.9/tests` | 5 | 399.12 | 12.13% | 0.0% |
| `httpcore-1.0.9/tests/benchmark` | 2 | 318.58 | 38.31% | 0.0% |
| `httpcore-1.0.9` | 3 | 12.78 | 0.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `httpcore-1.0.9/httpcore/_async/__init__.py` -> **100.0%** Exposure
- `httpcore-1.0.9/httpcore/_async/http_proxy.py` -> **100.0%** Exposure
- `httpcore-1.0.9/httpcore/_backends/base.py` -> **100.0%** Exposure
- `httpcore-1.0.9/httpcore/_backends/sync.py` -> **100.0%** Exposure
- `httpcore-1.0.9/httpcore/_sync/__init__.py` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `httpcore-1.0.9/httpcore/_synchronization.py` -> **100.0%** Exposure
- `httpcore-1.0.9/httpcore/_sync/connection_pool.py` -> **99.997%** Exposure
- `httpcore-1.0.9/httpcore/_async/connection_pool.py` -> **99.996%** Exposure
- `httpcore-1.0.9/httpcore/_models.py` -> **99.8887%** Exposure
- `httpcore-1.0.9/httpcore/_trace.py` -> **99.8589%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `httpcore-1.0.9/httpcore/_synchronization.py` -> **0** Orphaned Functions | **29** Duplicates
- `httpcore-1.0.9/httpcore/_async/http_proxy.py` -> **0** Orphaned Functions | **21** Duplicates
- `httpcore-1.0.9/httpcore/_sync/http_proxy.py` -> **0** Orphaned Functions | **21** Duplicates
- `httpcore-1.0.9/tests/test_cancellations.py` -> **8** Orphaned Functions | **11** Duplicates
- `httpcore-1.0.9/tests/test_models.py` -> **17** Orphaned Functions | **2** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`httpcore-1.0.9/httpcore/_sync/http2.py`** -> AI Confidence: **99.31%**
2. **`httpcore-1.0.9/httpcore/_async/http2.py`** -> AI Confidence: **99.24%**
3. **`httpcore-1.0.9/httpcore/_backends/sync.py`** -> AI Confidence: **99.24%**
4. **`httpcore-1.0.9/httpcore/_sync/connection_pool.py`** -> AI Confidence: **99.24%**
5. **`httpcore-1.0.9/httpcore/_synchronization.py`** -> AI Confidence: **99.24%**
6. **`httpcore-1.0.9/httpcore/_async/http_proxy.py`** -> AI Confidence: **99.18%**
7. **`httpcore-1.0.9/httpcore/_sync/http_proxy.py`** -> AI Confidence: **99.18%**
8. **`httpcore-1.0.9/httpcore/_async/connection.py`** -> AI Confidence: **99.16%**
9. **`httpcore-1.0.9/httpcore/_async/connection_pool.py`** -> AI Confidence: **99.16%**
10. **`httpcore-1.0.9/httpcore/_async/http11.py`** -> AI Confidence: **99.16%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `httpcore-1.0.9/tests/_sync/test_socks_proxy.py` -> **0.0544%** Exposure
- `httpcore-1.0.9/tests/_async/test_socks_proxy.py` -> **0.049%** Exposure
### Exploit Generation Surface
- `httpcore-1.0.9/httpcore/_async/connection.py` -> **100.0%** Exposure
- `httpcore-1.0.9/httpcore/_async/connection_pool.py` -> **100.0%** Exposure
- `httpcore-1.0.9/httpcore/_async/http11.py` -> **100.0%** Exposure
- `httpcore-1.0.9/httpcore/_async/http2.py` -> **100.0%** Exposure
- `httpcore-1.0.9/httpcore/_async/http_proxy.py` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `httpcore-1.0.9/tests/_async/test_connection_pool.py` -> **100.0%** Exposure
- `httpcore-1.0.9/tests/_sync/test_connection_pool.py` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `httpcore-1.0.9/httpcore/_async/connection.py` -> **100.0%** Exposure
- `httpcore-1.0.9/httpcore/_async/connection_pool.py` -> **100.0%** Exposure
- `httpcore-1.0.9/httpcore/_async/http11.py` -> **100.0%** Exposure
- `httpcore-1.0.9/httpcore/_async/http2.py` -> **100.0%** Exposure
- `httpcore-1.0.9/httpcore/_async/http_proxy.py` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `220` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `httpcore-1.0.9/httpcore/_synchronization.py` (PYTHON) -> Cumulative Risk: **936.62**
- **Archetype:** `file_cluster_4` (Distance: 13.419 IQR)
- **Magnitude:** 723.88 | **LOC:** 319 | **CtrlFlow:** 39.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `wait` (Impact: 104.7), `current_async_library` (Impact: 70.5), `acquire` (Impact: 32.4)

### 2. `httpcore-1.0.9/httpcore/_async/http11.py` (PYTHON) -> Cumulative Risk: **930.79**
- **Archetype:** `file_cluster_4` (Distance: 10.98 IQR)
- **Magnitude:** 445.02 | **LOC:** 380 | **CtrlFlow:** 31.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `handle_async_request` (Impact: 81.5), `_response_closed` (Impact: 36.6), `__aiter__` (Impact: 30.6)

### 3. `httpcore-1.0.9/httpcore/_async/connection_pool.py` (PYTHON) -> Cumulative Risk: **911.57**
- **Archetype:** `file_cluster_4` (Distance: 11.985 IQR)
- **Magnitude:** 533.68 | **LOC:** 421 | **CtrlFlow:** 38.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `handle_async_request` (Impact: 136.7), `_assign_requests_to_connections` (Impact: 81.1), `aclose` (Impact: 60.6)

### 4. `httpcore-1.0.9/httpcore/_async/http_proxy.py` (PYTHON) -> Cumulative Risk: **874.85**
- **Archetype:** `file_cluster_13` (Distance: 10.287 IQR)
- **Magnitude:** 366.24 | **LOC:** 368 | **CtrlFlow:** 24.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `handle_async_request` (Impact: 185.8), `create_connection` (Impact: 9.7), `handle_async_request` (Impact: 7.7)

### 5. `httpcore-1.0.9/httpcore/_trace.py` (PYTHON) -> Cumulative Risk: **864.47**
- **Archetype:** `file_cluster_13` (Distance: 10.762 IQR)
- **Magnitude:** 241.6 | **LOC:** 108 | **CtrlFlow:** 53.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), Documentation (99.9994%)
- **Heaviest Functions:** `trace` (Impact: 121.6), `atrace` (Impact: 61.3), `__aenter__` (Impact: 8.2)

### 6. `httpcore-1.0.9/httpcore/_async/http2.py` (PYTHON) -> Cumulative Risk: **846.55**
- **Archetype:** `file_cluster_4` (Distance: 11.817 IQR)
- **Magnitude:** 598.72 | **LOC:** 593 | **CtrlFlow:** 39.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `handle_async_request` (Impact: 126.4), `_response_closed` (Impact: 42.3), `__aiter__` (Impact: 30.8)

### 7. `httpcore-1.0.9/httpcore/_async/socks_proxy.py` (PYTHON) -> Cumulative Risk: **832.0**
- **Archetype:** `file_cluster_13` (Distance: 10.572 IQR)
- **Magnitude:** 451.7 | **LOC:** 342 | **CtrlFlow:** 33.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `handle_async_request` (Impact: 234.6), `is_available` (Impact: 43.9), `info` (Impact: 27.9)

### 8. `httpcore-1.0.9/httpcore/_sync/connection_pool.py` (PYTHON) -> Cumulative Risk: **802.0**
- **Archetype:** `file_cluster_13` (Distance: 11.68 IQR)
- **Magnitude:** 479.28 | **LOC:** 421 | **CtrlFlow:** 42.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.997%)
- **Heaviest Functions:** `handle_request` (Impact: 136.7), `_assign_requests_to_connections` (Impact: 81.1), `close` (Impact: 52.6)

### 9. `httpcore-1.0.9/httpcore/_async/connection.py` (PYTHON) -> Cumulative Risk: **797.62**
- **Archetype:** `file_cluster_13` (Distance: 10.39 IQR)
- **Magnitude:** 452.58 | **LOC:** 223 | **CtrlFlow:** 35.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `handle_async_request` (Impact: 123.0), `_connect` (Impact: 100.0), `is_available` (Impact: 43.9)

### 10. `httpcore-1.0.9/httpcore/_sync/http11.py` (PYTHON) -> Cumulative Risk: **768.48**
- **Archetype:** `file_cluster_13` (Distance: 10.716 IQR)
- **Magnitude:** 345.22 | **LOC:** 380 | **CtrlFlow:** 36.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (99.9896%)
- **Heaviest Functions:** `handle_request` (Impact: 81.5), `_response_closed` (Impact: 31.8), `__iter__` (Impact: 26.6)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `httpcore-1.0.9/httpcore/_synchronization.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.419 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 8.27 IQR)
- **Top Global Matches:** file_cluster_4: 13.419, file_cluster_16: 13.789, file_cluster_13: 13.869
- **Magnitude:** 723.88 | **LOC:** 319 | **CtrlFlow:** 39.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (50.0%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `wait` (Impact: 104.7 | O(2^N) | DB: 2)
  * `current_async_library` (Impact: 70.5 | O(2^N))
    * *Intent:* # Determine if we're running under trio or asyncio. # See https://sniffio.readthedocs.io/en/latest/ ...
  * `acquire` (Impact: 32.4 | O(2^N) | DB: 2)
  * `set` (Impact: 28.1 | O(2^N) | DB: 2)
  * `release` (Impact: 24.2 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 72`, `args: 32`, `func_start: 32`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 116`, `duplicate_logic: 29`
* *Architecture:* `api: 24`, `concurrency: 159`, `import: 7`
* *Defense:* `safety: 6`, `doc: 16`, `sync_locks: 14`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 37.511
  * `Choke Point (Betweenness):` 0.010382 | `Ripple Effect (Closeness):` 0.227273
  * `Imports (Out-Degree: 3):` sniffio, types, __future__, threading, trio, anyio, ._exceptions
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `httpcore-1.0.9/tests/_async/test_connection_pool.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.256 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.81 IQR)
- **Top Global Matches:** file_cluster_4: 11.256, file_cluster_8: 11.5, file_cluster_0: 11.661
- **Magnitude:** 720.1 | **LOC:** 833 | **CtrlFlow:** 29.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (20.8322%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_connection_pool_with_keepalive` (Impact: 59.5 | O(N^4))
    * *Intent:* """ By default HTTP/1.1 requests should be returned to the connection pool. """
  * `test_connection_pool_concurrency_same_do` (Impact: 37.2 | O(N^4) | DB: 1)
  * `test_connection_pool_concurrency` (Impact: 37.0 | O(N^4) | DB: 1)
  * `test_connection_pool_concurrency_same_do` (Impact: 36.9 | O(N^4) | DB: 1)
  * `test_connection_pool_with_http2` (Impact: 30.9 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 163`, `args: 26`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 21`, `duplicate_logic: 2`, `orphaned_logic: 16`
* *Architecture:* `api: 27`, `concurrency: 183`, `import: 7`
* *Defense:* `safety: 64`, `doc: 34`, `test: 108`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.836
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` typing, pytest, trio, hyperframe.frame, logging, hpack, httpcore
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `httpcore-1.0.9/httpcore/_async/http2.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.817 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.688 IQR)
- **Top Global Matches:** file_cluster_4: 11.817, file_cluster_13: 11.989, file_cluster_16: 12.097
- **Magnitude:** 598.72 | **LOC:** 593 | **CtrlFlow:** 39.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (57.7191%), Tech Debt (52.1538%)
**Top Internal Functions/Classes:**
  * `handle_async_request` (Impact: 126.4 | O(N^6) | DB: 6)
  * `_response_closed` (Impact: 42.3 | O(N^5) | DB: 3)
  * `__aiter__` (Impact: 30.8 | O(N^5))
  * `_send_request_headers` (Impact: 26.4 | O(N^4))
  * `_read_incoming_data` (Impact: 18.7 | O(N^4) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 80`, `structural_boundaries: 122`, `args: 30`, `func_start: 30`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 63`, `duplicate_logic: 4`
* *Architecture:* `api: 23`, `concurrency: 124`, `import: 17`
* *Defense:* `safety: 25`, `doc: 20`, `test: 4`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.836
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` .._trace, .interfaces, types, __future__, h2.config, h2.connection, h2.events, typing...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `httpcore-1.0.9/httpcore/_async/connection_pool.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.985 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.443 IQR)
- **Top Global Matches:** file_cluster_4: 11.985, file_cluster_13: 11.989, file_cluster_16: 12.206
- **Magnitude:** 533.68 | **LOC:** 421 | **CtrlFlow:** 38.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (68.0406%), Tech Debt (90.4177%)
**Top Internal Functions/Classes:**
  * `handle_async_request` (Impact: 136.7 | O(2^N) | DB: 2)
  * `_assign_requests_to_connections` (Impact: 81.1 | O(N^4) | DB: 9)
    * *Intent:* # Assign incoming requests to available connections,
  * `aclose` (Impact: 60.6 | O(2^N) | DB: 2)
  * `create_connection` (Impact: 23.4 | O(N^5))
  * `__repr__` (Impact: 18.4 | O(N^4))
    * *Intent:* # There are three cases for how we may be able to handle the request: # # 2. We can create a new con...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 77`, `args: 18`, `func_start: 18`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 85`, `duplicate_logic: 5`
* *Architecture:* `io: 2`, `api: 17`, `concurrency: 45`, `import: 15`
* *Defense:* `safety: 10`, `doc: 10`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.836
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` .socks_proxy, .interfaces, types, __future__, .connection, typing, .._backends.auto, .http_proxy...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `httpcore-1.0.9/httpcore/_sync/connection_pool.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.68 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.962 IQR)
- **Top Global Matches:** file_cluster_13: 11.68, file_cluster_16: 11.924, file_cluster_8: 12.059
- **Magnitude:** 479.28 | **LOC:** 421 | **CtrlFlow:** 42.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (57.783%), Tech Debt (90.4177%)
**Top Internal Functions/Classes:**
  * `handle_request` (Impact: 136.7 | O(2^N) | DB: 2)
  * `_assign_requests_to_connections` (Impact: 81.1 | O(N^4) | DB: 9)
    * *Intent:* # Assign incoming requests to available connections,
  * `close` (Impact: 52.6 | O(2^N) | DB: 2)
  * `create_connection` (Impact: 23.4 | O(N^5))
  * `__repr__` (Impact: 18.4 | O(N^4))
    * *Intent:* # There are three cases for how we may be able to handle the request: # # 2. We can create a new con...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 66`, `args: 18`, `func_start: 18`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 87`, `duplicate_logic: 5`
* *Architecture:* `io: 2`, `api: 17`, `import: 15`
* *Defense:* `safety: 10`, `doc: 10`, `test: 2`, `sync_locks: 3`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 17.401
  * `Choke Point (Betweenness):` 0.002694 | `Ripple Effect (Closeness):` 0.024242
  * `Imports (Out-Degree: 5):` .socks_proxy, .interfaces, types, __future__, .connection, typing, .._backends.sync, .http_proxy...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `httpcore-1.0.9/tests/_sync/test_connection_pool.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.938 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.155 IQR)
- **Top Global Matches:** file_cluster_8: 10.938, file_cluster_17: 11.285, file_cluster_13: 11.37
- **Magnitude:** 477.94 | **LOC:** 833 | **CtrlFlow:** 33.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (2.4856%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_connection_pool_with_keepalive` (Impact: 52.2 | O(N^4))
    * *Intent:* """ By default HTTP/1.1 requests should be returned to the connection pool. """
  * `test_connection_pool_concurrency_same_do` (Impact: 32.6 | O(N^4) | DB: 1)
  * `test_connection_pool_concurrency` (Impact: 32.3 | O(N^4) | DB: 1)
  * `test_connection_pool_concurrency_same_do` (Impact: 32.2 | O(N^4) | DB: 1)
  * `test_connection_pool_with_http2` (Impact: 27.1 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 136`, `args: 26`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 21`, `duplicate_logic: 2`, `orphaned_logic: 16`
* *Architecture:* `api: 27`, `import: 7`
* *Defense:* `safety: 64`, `doc: 34`, `test: 90`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.836
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` typing, pytest, tests, hyperframe.frame, logging, hpack, httpcore
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `httpcore-1.0.9/httpcore/_sync/http2.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.527 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.957 IQR)
- **Top Global Matches:** file_cluster_13: 11.527, file_cluster_16: 11.653, file_cluster_8: 11.748
- **Magnitude:** 467.42 | **LOC:** 593 | **CtrlFlow:** 47.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (26.9011%), Tech Debt (52.1538%)
**Top Internal Functions/Classes:**
  * `handle_request` (Impact: 126.4 | O(N^6) | DB: 6)
  * `_response_closed` (Impact: 42.3 | O(N^5) | DB: 3)
  * `__iter__` (Impact: 26.7 | O(N^5))
  * `_send_request_headers` (Impact: 26.4 | O(N^4))
  * `_read_incoming_data` (Impact: 18.7 | O(N^4) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 80`, `structural_boundaries: 88`, `args: 30`, `func_start: 30`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 63`, `duplicate_logic: 4`
* *Architecture:* `api: 23`, `import: 17`
* *Defense:* `safety: 25`, `doc: 20`, `test: 4`, `sync_locks: 9`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.836
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` .._trace, .interfaces, types, __future__, h2.config, h2.connection, h2.events, typing...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `httpcore-1.0.9/httpcore/_async/connection.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.39 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.425 IQR)
- **Top Global Matches:** file_cluster_13: 10.39, file_cluster_4: 10.645, file_cluster_16: 10.721
- **Magnitude:** 452.58 | **LOC:** 223 | **CtrlFlow:** 35.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (59.3073%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `handle_async_request` (Impact: 123.0 | O(2^N) | DB: 3)
  * `_connect` (Impact: 100.0 | O(N^6))
  * `is_available` (Impact: 43.9 | O(2^N))
  * `aclose` (Impact: 30.2 | O(2^N))
  * `info` (Impact: 27.9 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 71`, `args: 14`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 25`
* *Architecture:* `api: 14`, `concurrency: 24`, `import: 16`
* *Defense:* `safety: 4`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.836
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` .._trace, .interfaces, types, __future__, typing, .._backends.auto, .._models, .._synchronization...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `httpcore-1.0.9/httpcore/_async/socks_proxy.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.572 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.722 IQR)
- **Top Global Matches:** file_cluster_13: 10.572, file_cluster_8: 10.669, file_cluster_16: 10.82
- **Magnitude:** 451.7 | **LOC:** 342 | **CtrlFlow:** 33.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (55.7698%), Tech Debt (41.5048%)
**Top Internal Functions/Classes:**
  * `handle_async_request` (Impact: 234.6 | O(2^N) | DB: 3)
  * `is_available` (Impact: 43.9 | O(2^N))
  * `info` (Impact: 27.9 | O(2^N))
  * `aclose` (Impact: 16.1 | O(2^N))
    * *Intent:* # Create the HTTP/1.1 or HTTP/2 connection if http2_negotiated or ( self._http2 and not self._http1 ...
  * `has_expired` (Impact: 14.1 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 77`, `args: 13`, `func_start: 13`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 35`, `duplicate_logic: 2`
* *Architecture:* `api: 14`, `concurrency: 18`, `import: 15`
* *Defense:* `safety: 9`, `doc: 4`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.836
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` .._trace, .interfaces, __future__, .._backends.auto, socksio, .._models, .._synchronization, .._ssl...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `httpcore-1.0.9/httpcore/_async/http11.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_4` (Drift: 10.98 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.753 IQR)
- **Top Global Matches:** file_cluster_4: 10.98, file_cluster_13: 11.195, file_cluster_16: 11.293
- **Magnitude:** 445.02 | **LOC:** 380 | **CtrlFlow:** 31.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (99.1994%), Tech Debt (95.7546%)
**Top Internal Functions/Classes:**
  * `handle_async_request` (Impact: 81.5 | O(N^5) | DB: 2)
  * `_response_closed` (Impact: 36.6 | O(N^5) | DB: 2)
  * `__aiter__` (Impact: 30.6 | O(N^5))
  * `read` (Impact: 24.4 | O(2^N) | DB: 1)
  * `aclose` (Impact: 15.2 | O(N^4) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 101`, `args: 28`, `func_start: 28`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 36`, `duplicate_logic: 6`
* *Architecture:* `api: 27`, `concurrency: 87`, `import: 14`
* *Defense:* `safety: 12`, `test: 1`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.836
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` .._trace, .interfaces, types, __future__, typing, .._models, .._synchronization, time...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `httpcore-1.0.9/httpcore/_sync/socks_proxy.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.349 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.394 IQR)
- **Top Global Matches:** file_cluster_13: 10.349, file_cluster_8: 10.466, file_cluster_16: 10.61
- **Magnitude:** 431.6 | **LOC:** 342 | **CtrlFlow:** 37.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (31.0174%), Tech Debt (41.5048%)
**Top Internal Functions/Classes:**
  * `handle_request` (Impact: 234.6 | O(2^N) | DB: 3)
  * `is_available` (Impact: 43.9 | O(2^N))
  * `info` (Impact: 27.9 | O(2^N))
  * `has_expired` (Impact: 14.1 | O(2^N))
  * `is_idle` (Impact: 14.1 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 66`, `args: 13`, `func_start: 13`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 35`, `duplicate_logic: 2`
* *Architecture:* `api: 14`, `import: 15`
* *Defense:* `safety: 9`, `doc: 4`, `test: 4`, `sync_locks: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.836
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` .._trace, .interfaces, __future__, .._backends.sync, socksio, .._models, .._synchronization, .._ssl...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `httpcore-1.0.9/httpcore/_sync/connection.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.025 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.006 IQR)
- **Top Global Matches:** file_cluster_13: 10.025, file_cluster_16: 10.39, file_cluster_8: 10.437
- **Magnitude:** 424.18 | **LOC:** 223 | **CtrlFlow:** 38.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (24.941%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `handle_request` (Impact: 123.0 | O(2^N) | DB: 3)
  * `_connect` (Impact: 100.0 | O(N^6))
  * `is_available` (Impact: 43.9 | O(2^N))
  * `info` (Impact: 27.9 | O(2^N))
  * `close` (Impact: 26.2 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 63`, `args: 14`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 25`
* *Architecture:* `api: 14`, `import: 16`
* *Defense:* `safety: 4`, `doc: 2`, `sync_locks: 2`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.836
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` .._trace, .interfaces, types, __future__, typing, .._backends.sync, .._models, .._synchronization...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `httpcore-1.0.9/httpcore/_async/http_proxy.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.287 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.943 IQR)
- **Top Global Matches:** file_cluster_13: 10.287, file_cluster_16: 10.288, file_cluster_8: 10.302
- **Magnitude:** 366.24 | **LOC:** 368 | **CtrlFlow:** 24.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (44.7739%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `handle_async_request` (Impact: 185.8 | O(2^N) | DB: 3)
  * `create_connection` (Impact: 9.7 | O(N^4))
    * *Intent:* """ super().__init__( ssl_context=ssl_context, max_connections=max_connections, max_keepalive_connec...
  * `handle_async_request` (Impact: 7.7 | O(2^N))
  * `aclose` (Impact: 6.1 | O(2^N))
  * `aclose` (Impact: 6.1 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 81`, `args: 23`, `func_start: 23`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 34`, `duplicate_logic: 21`
* *Architecture:* `api: 22`, `concurrency: 18`, `import: 16`
* *Defense:* `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.836
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` .._trace, .interfaces, __future__, .connection, typing, .http11, .._models, .._synchronization...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `httpcore-1.0.9/httpcore/_sync/http_proxy.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.082 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.711 IQR)
- **Top Global Matches:** file_cluster_13: 10.082, file_cluster_16: 10.106, file_cluster_8: 10.131
- **Magnitude:** 346.64 | **LOC:** 368 | **CtrlFlow:** 26.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (22.6762%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `handle_request` (Impact: 185.8 | O(2^N) | DB: 3)
  * `create_connection` (Impact: 9.7 | O(N^4))
    * *Intent:* """ super().__init__( ssl_context=ssl_context, max_connections=max_connections, max_keepalive_connec...
  * `handle_request` (Impact: 7.7 | O(2^N))
  * `close` (Impact: 5.3 | O(2^N))
  * `info` (Impact: 5.3 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 74`, `args: 23`, `func_start: 23`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 34`, `duplicate_logic: 21`
* *Architecture:* `api: 22`, `import: 16`
* *Defense:* `doc: 6`, `sync_locks: 2`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.836
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` .._trace, .interfaces, __future__, .connection, typing, .http11, .._models, .._synchronization...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `httpcore-1.0.9/httpcore/_sync/http11.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.716 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.008 IQR)
- **Top Global Matches:** file_cluster_13: 10.716, file_cluster_16: 10.842, file_cluster_8: 10.945
- **Magnitude:** 345.22 | **LOC:** 380 | **CtrlFlow:** 36.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (36.8845%), Tech Debt (95.7546%)
**Top Internal Functions/Classes:**
  * `handle_request` (Impact: 81.5 | O(N^5) | DB: 2)
  * `_response_closed` (Impact: 31.8 | O(N^5) | DB: 2)
  * `__iter__` (Impact: 26.6 | O(N^5))
  * `read` (Impact: 24.4 | O(2^N) | DB: 1)
  * `has_expired` (Impact: 14.5 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 81`, `args: 28`, `func_start: 28`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 36`, `duplicate_logic: 6`
* *Architecture:* `api: 27`, `import: 14`
* *Defense:* `safety: 12`, `test: 1`, `sync_locks: 4`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.836
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` .._trace, .interfaces, types, __future__, typing, .._models, .._synchronization, time...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `httpcore-1.0.9/tests/benchmark/client.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_4` (Drift: 10.135 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 6.823 IQR)
- **Top Global Matches:** file_cluster_4: 10.135, file_cluster_13: 10.534, file_cluster_11: 10.894
- **Magnitude:** 304.98 | **LOC:** 191 | **CtrlFlow:** 35.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (49.1345%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `run_async_requests` (Impact: 90.3 | O(N^5) | DB: 14)
  * `run_sync_requests` (Impact: 87.2 | O(N^5) | DB: 2)
  * `main` (Impact: 32.2 | O(2^N) | DB: 6)
  * `profile` (Impact: 8.1 | O(N^2))
  * `duration` (Impact: 2.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 58`, `args: 12`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 11`, `high_risk_execution: 7`, `state_mutation: 8`
* *Architecture:* `io: 8`, `api: 12`, `concurrency: 62`, `import: 13`
* *Defense:* `safety: 9`, `test: 9`, `sync_locks: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.836
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyinstrument, typing, matplotlib.pyplot, os, urllib3, time, contextlib, matplotlib.axes...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `httpcore-1.0.9/tests/_async/test_http2.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.293 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.145 IQR)
- **Top Global Matches:** file_cluster_8: 9.293, file_cluster_7: 9.884, file_cluster_4: 9.955
- **Magnitude:** 276.32 | **LOC:** 383 | **CtrlFlow:** 23.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (7.2042%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_http2_remote_max_streams_update` (Impact: 44.4 | O(N^6))
  * `test_http2_connection_with_goaway` (Impact: 30.2 | O(N^6))
  * `test_http2_connection_attempt_close` (Impact: 29.6 | O(N^6))
  * `test_http2_connection_with_rst_stream` (Impact: 23.1 | O(N^6))
  * `test_http2_connection_closed` (Impact: 22.6 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 72`, `args: 10`, `func_start: 10`
* *Risk/State:* `orphaned_logic: 10`
* *Architecture:* `api: 10`, `concurrency: 37`, `import: 4`
* *Defense:* `safety: 22`, `doc: 12`, `test: 50`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.836
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pytest, hpack, httpcore, hyperframe.frame
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `httpcore-1.0.9/tests/_async/test_connection.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.82%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.368 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.804 IQR)
- **Top Global Matches:** file_cluster_8: 10.368, file_cluster_16: 10.414, file_cluster_4: 10.478
- **Magnitude:** 268.98 | **LOC:** 382 | **CtrlFlow:** 19.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (16.7435%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_write_error_without_response_sent` (Impact: 21.9 | O(N^4) | DB: 1)
  * `test_concurrent_requests_not_available_o` (Impact: 21.0 | O(N^4))
    * *Intent:* """ Attempting to issue a request against an already active HTTP/1.1 connection will raise a `Connec...
  * `test_connection_retries_tls` (Impact: 17.4 | O(N^3))
  * `test_write_error_with_response_sent` (Impact: 17.3 | O(N^4) | DB: 1)
  * `test_connection_retries` (Impact: 17.2 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 94`, `args: 23`, `func_start: 23`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 6`, `duplicate_logic: 2`, `orphaned_logic: 9`
* *Architecture:* `api: 24`, `concurrency: 57`, `import: 6`
* *Defense:* `safety: 22`, `doc: 8`, `test: 52`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.836
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` typing, pytest, ssl, hyperframe.frame, hpack, httpcore
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `httpcore-1.0.9/httpcore/_trace.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.762 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.634 IQR)
- **Top Global Matches:** file_cluster_13: 10.762, file_cluster_16: 10.86, file_cluster_8: 10.903
- **Magnitude:** 241.6 | **LOC:** 108 | **CtrlFlow:** 53.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (79.197%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `trace` (Impact: 121.6 | O(2^N))
  * `atrace` (Impact: 61.3 | O(N^5))
  * `__aenter__` (Impact: 8.2 | O(N^3))
  * `__enter__` (Impact: 7.2 | O(N^3))
  * `__init__` (Impact: 1.8 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 24`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 21`
* *Architecture:* `api: 8`, `concurrency: 7`, `import: 6`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 28.988
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.181818
  * `Imports (Out-Degree: 1):` ._models, types, __future__, typing, inspect, logging
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `httpcore-1.0.9/tests/_async/test_http11.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.82%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.004 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.376 IQR)
- **Top Global Matches:** file_cluster_8: 11.004, file_cluster_4: 11.276, file_cluster_0: 11.317
- **Magnitude:** 227.76 | **LOC:** 381 | **CtrlFlow:** 19.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (8.5538%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_http11_connection_handles_one_activ` (Impact: 20.9 | O(N^4))
  * `test_http11_upgrade_with_trailing_data` (Impact: 17.1 | O(N^4))
  * `test_http11_early_hints` (Impact: 14.6 | O(N^3))
  * `test_http11_connection_with_local_protoc` (Impact: 13.3 | O(N^3))
  * `test_http11_connection_unread_response` (Impact: 13.2 | O(N^3))
    * *Intent:* """ If the client releases the response without reading it to termination, then the connection will ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 95`, `args: 13`, `func_start: 13`
* *Risk/State:* `orphaned_logic: 12`
* *Architecture:* `api: 13`, `concurrency: 47`, `import: 2`
* *Defense:* `safety: 44`, `doc: 24`, `test: 76`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.836
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pytest, httpcore
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `httpcore-1.0.9/tests/_sync/test_http2.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.847 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.065 IQR)
- **Top Global Matches:** file_cluster_8: 8.847, file_cluster_7: 9.522, file_cluster_1: 9.742
- **Magnitude:** 211.42 | **LOC:** 383 | **CtrlFlow:** 27.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (2.1333%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_http2_remote_max_streams_update` (Impact: 38.7 | O(N^6))
  * `test_http2_connection_with_goaway` (Impact: 26.5 | O(N^6))
  * `test_http2_connection_attempt_close` (Impact: 25.8 | O(N^6))
  * `test_http2_connection_with_rst_stream` (Impact: 20.2 | O(N^6))
  * `test_http2_connection_closed` (Impact: 19.8 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 58`, `args: 10`, `func_start: 10`
* *Risk/State:* `orphaned_logic: 10`
* *Architecture:* `api: 10`, `import: 4`
* *Defense:* `safety: 22`, `doc: 12`, `test: 40`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.836
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pytest, hpack, httpcore, hyperframe.frame
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `httpcore-1.0.9/tests/test_cancellations.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.425 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.433 IQR)
- **Top Global Matches:** file_cluster_4: 11.425, file_cluster_16: 11.589, file_cluster_0: 11.618
- **Magnitude:** 205.94 | **LOC:** 246 | **CtrlFlow:** 21.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (20.8188%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_h2_timeout_during_response` (Impact: 22.4 | O(N^6))
  * `test_connection_pool_timeout_during_resp` (Impact: 12.8 | O(N^3))
  * `test_h11_timeout_during_response` (Impact: 12.8 | O(N^3))
  * `test_h2_timeout_during_request` (Impact: 12.6 | O(N^3))
  * `test_connection_pool_timeout_during_requ` (Impact: 12.4 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 64`, `args: 19`, `func_start: 19`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 9`, `duplicate_logic: 11`, `orphaned_logic: 8`
* *Architecture:* `api: 21`, `concurrency: 46`, `import: 6`
* *Defense:* `safety: 9`, `doc: 20`, `test: 27`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.836
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` hyperframe, typing, pytest, anyio, hpack, httpcore
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `httpcore-1.0.9/tests/_sync/test_connection.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.877 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.855 IQR)
- **Top Global Matches:** file_cluster_8: 9.877, file_cluster_16: 9.981, file_cluster_13: 10.27
- **Magnitude:** 192.6 | **LOC:** 382 | **CtrlFlow:** 22.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (2.8868%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_write_error_without_response_sent` (Impact: 19.2 | O(N^4) | DB: 1)
  * `test_concurrent_requests_not_available_o` (Impact: 18.3 | O(N^4))
    * *Intent:* """ Attempting to issue a request against an already active HTTP/1.1 connection will raise a `Connec...
  * `test_write_error_with_response_sent` (Impact: 15.3 | O(N^4) | DB: 1)
  * `test_connection_retries_tls` (Impact: 15.3 | O(N^3))
  * `test_connection_retries` (Impact: 15.1 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 78`, `args: 23`, `func_start: 23`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 6`, `duplicate_logic: 2`, `orphaned_logic: 9`
* *Architecture:* `api: 24`, `import: 6`
* *Defense:* `safety: 22`, `doc: 8`, `test: 43`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.836
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` typing, pytest, ssl, hyperframe.frame, hpack, httpcore
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `httpcore-1.0.9/httpcore/_backends/trio.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.95%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.359 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.607 IQR)
- **Top Global Matches:** file_cluster_8: 9.359, file_cluster_13: 9.641, file_cluster_16: 9.711
- **Magnitude:** 187.98 | **LOC:** 160 | **CtrlFlow:** 43.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 21
- **Risk Profile:** Cognitive Load (55.9347%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `get_extra_info` (Impact: 70.2 | O(2^N) | DB: 21)
  * `write` (Impact: 30.6 | O(N^4))
  * `read` (Impact: 25.6 | O(N^4))
  * `_get_socket_stream` (Impact: 7.2 | O(N^3))
  * `aclose` (Impact: 6.1 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 44`, `args: 10`, `func_start: 10`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 1`
* *Architecture:* `io: 7`, `api: 16`, `concurrency: 15`, `import: 6`
* *Defense:* `safety: 9`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 37.335
  * `Choke Point (Betweenness):` 0.000954 | `Ripple Effect (Closeness):` 0.169501
  * `Imports (Out-Degree: 2):` __future__, typing, trio, ssl, .._exceptions, .base
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `httpcore-1.0.9/httpcore/_models.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.352 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.089 IQR)
- **Top Global Matches:** file_cluster_4: 12.352, file_cluster_16: 12.436, file_cluster_13: 12.568
- **Magnitude:** 187.12 | **LOC:** 517 | **CtrlFlow:** 49.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (42.1922%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `enforce_bytes` (Impact: 20.6 | O(N^3))
    * *Intent:* """ Any arguments that are ultimately represented as bytes can be specified either as bytes or as st...
  * `enforce_url` (Impact: 12.5 | O(N^2))
  * `enforce_stream` (Impact: 1.2 | O(N^1))
  * `include_request_headers` (Impact: 1.2 | O(N^1))
    * *Intent:* # * https://tools.ietf.org/html/rfc3986#section-3.2.3 # * https://url.spec.whatwg.org/#url-miscellan...
  * `enforce_headers` (Impact: 1.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 74`, `args: 29`, `func_start: 29`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 74`
* *Architecture:* `api: 20`, `concurrency: 50`, `import: 5`
* *Defense:* `safety: 24`, `doc: 20`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 85.54
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.309091
  * `Imports (Out-Degree: 0):` __future__, typing, ssl, base64, urllib.parse
  * `Imported By (In-Degree: 17):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `httpcore-1.0.9/tests/test_models.py` (PYTHON) | Magnitude: 145.24 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 100, structural_boundaries: 65, test: 60, safety: 33

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `httpcore-1.0.9/httpcore/_async/http_proxy.py` (PYTHON) | Magnitude: 366.24 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 252, encapsulation: 93, structural_boundaries: 81, state_mutation: 34
- `httpcore-1.0.9/tests/test_api.py` (PYTHON) | Magnitude: 12.46 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 10, indent_spaces: 8, test: 7, safety: 4
- `httpcore-1.0.9/httpcore/_sync/http_proxy.py` (PYTHON) | Magnitude: 346.64 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 252, encapsulation: 93, structural_boundaries: 74, state_mutation: 34
- `httpcore-1.0.9/httpcore/_exceptions.py` (PYTHON) | Magnitude: 38.24 | Delta: **0.087 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 35, indent_spaces: 22, api: 17, safety_bypasses: 16
- `httpcore-1.0.9/httpcore/_async/socks_proxy.py` (PYTHON) | Magnitude: 451.7 | Delta: **0.097 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 232, encapsulation: 83, structural_boundaries: 77, branch: 39

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `httpcore-1.0.9/httpcore/_backends/base.py` (PYTHON) | Magnitude: 73.18 | Delta: **0.06 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 69, structural_boundaries: 27, api: 22, generics: 19
- `httpcore-1.0.9/httpcore/_sync/interfaces.py` (PYTHON) | Magnitude: 46.5 | Delta: **0.166 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 78, structural_boundaries: 19, api: 19, args: 10
- `httpcore-1.0.9/httpcore/_async/interfaces.py` (PYTHON) | Magnitude: 55.9 | Delta: **0.17 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 78, structural_boundaries: 24, api: 19, args: 10
- `httpcore-1.0.9/tests/concurrency.py` (PYTHON) | Magnitude: 24.96 | Delta: **0.285 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 13, generics: 10, concurrency: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `httpcore-1.0.9/httpcore/_async/connection_pool.py` (PYTHON) | Magnitude: 533.68 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 259, encapsulation: 119, state_mutation: 85, structural_boundaries: 77
- `httpcore-1.0.9/httpcore/_models.py` (PYTHON) | Magnitude: 187.12 | Delta: **0.084 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 300, structural_boundaries: 74, state_mutation: 74, branch: 72
- `httpcore-1.0.9/tests/_async/test_integration.py` (PYTHON) | Magnitude: 38.54 | Delta: **0.103 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 22, test: 16, safety: 11
- `httpcore-1.0.9/tests/test_cancellations.py` (PYTHON) | Magnitude: 205.94 | Delta: **0.164 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 124, structural_boundaries: 64, concurrency: 46, test: 27
- `httpcore-1.0.9/httpcore/_async/http2.py` (PYTHON) | Magnitude: 598.72 | Delta: **0.172 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 383, encapsulation: 181, concurrency: 124, structural_boundaries: 122

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `httpcore-1.0.9/tests/_async/test_connection.py` (PYTHON) | Magnitude: 268.98 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 275, structural_boundaries: 94, concurrency: 57, test: 52
- `httpcore-1.0.9/httpcore/_backends/sync.py` (PYTHON) | Magnitude: 175.66 | Delta: **0.055 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 185, structural_boundaries: 53, encapsulation: 44, branch: 37
- `httpcore-1.0.9/tests/_sync/test_connection.py` (PYTHON) | Magnitude: 192.6 | Delta: **0.104 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 275, structural_boundaries: 78, test: 43, generics: 32
- `httpcore-1.0.9/tests/_sync/test_integration.py` (PYTHON) | Magnitude: 26.28 | Delta: **0.164 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 20, test: 13, safety: 11
- `httpcore-1.0.9/tests/_async/test_http11.py` (PYTHON) | Magnitude: 227.76 | Delta: **0.272 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 255, structural_boundaries: 95, test: 76, concurrency: 47

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `httpcore-1.0.9/httpcore/_synchronization.py` -> **Severity: 1.038** (Bridge: 0.0104 * Flux: 100.0%)
- `httpcore-1.0.9/httpcore/_sync/connection_pool.py` -> **Severity: 0.269** (Bridge: 0.0027 * Flux: 99.997%)
- `httpcore-1.0.9/httpcore/_backends/auto.py` -> **Severity: 0.095** (Bridge: 0.0015 * Flux: 62.497%)
- `httpcore-1.0.9/httpcore/_backends/anyio.py` -> **Severity: 0.063** (Bridge: 0.0052 * Flux: 12.2141%)
- `httpcore-1.0.9/httpcore/_backends/sync.py` -> **Severity: 0.033** (Bridge: 0.0015 * Flux: 21.9275%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `httpcore-1.0.9/httpcore/_exceptions.py` -> **Severity: 26.405** (Embedded: 0.3207 * Error Risk: 82.3277%)
- `httpcore-1.0.9/httpcore/_synchronization.py` -> **Severity: 12.385** (Embedded: 0.2273 * Error Risk: 54.4947%)
- `httpcore-1.0.9/httpcore/_trace.py` -> **Severity: 9.282** (Embedded: 0.1818 * Error Risk: 51.0526%)
- `httpcore-1.0.9/httpcore/_backends/anyio.py` -> **Severity: 7.693** (Embedded: 0.1695 * Error Risk: 45.3846%)
- `httpcore-1.0.9/httpcore/_backends/sync.py` -> **Severity: 3.995** (Embedded: 0.0758 * Error Risk: 52.7273%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `httpcore-1.0.9/httpcore/_exceptions.py` -> **Severity: 7764.9** (Blast Radius: 77.649 * Doc Risk: 100.0%)
- `httpcore-1.0.9/httpcore/_backends/base.py` -> **Severity: 7057.041** (Blast Radius: 70.575 * Doc Risk: 99.9935%)
- `httpcore-1.0.9/httpcore/_synchronization.py` -> **Severity: 3751.074** (Blast Radius: 37.511 * Doc Risk: 99.9993%)
- `httpcore-1.0.9/httpcore/_backends/trio.py` -> **Severity: 3733.16** (Blast Radius: 37.335 * Doc Risk: 99.9909%)
- `httpcore-1.0.9/httpcore/_backends/anyio.py` -> **Severity: 3732.682** (Blast Radius: 37.335 * Doc Risk: 99.9781%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
